# Class BasicListUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicListUI.html`

### Class Description

```java
public class
BasicListUI

extends
ListUI
```

An extensible implementation of

ListUI

.

BasicListUI

instances cannot be shared between multiple
lists.

**Direct Known Subclasses:** SynthListUI

---

### Field Details

#### protected
JList
<
Object
> list

The instance of

JList

.

---

#### protected
CellRendererPane
rendererPane

The instance of

CellRendererPane

.

---

#### protected
FocusListener
focusListener

FocusListener

that attached to

JList

.

---

#### protected
MouseInputListener
mouseInputListener

MouseInputListener

that attached to

JList

.

---

#### protected
ListSelectionListener
listSelectionListener

ListSelectionListener

that attached to

JList

.

---

#### protected
ListDataListener
listDataListener

ListDataListener

that attached to

JList

.

---

#### protected
PropertyChangeListener
propertyChangeListener

PropertyChangeListener

that attached to

JList

.

---

#### protected int[] cellHeights

The array of cells' height

---

#### protected int cellHeight

The height of cell.

---

#### protected int cellWidth

The width of cell.

---

#### protected int updateLayoutStateNeeded

The value represents changes to

JList

model.

---

#### protected static final int modelChanged

The bit relates to model changed property.

**See Also:**
- Constant Field Values

---

#### protected static final int selectionModelChanged

The bit relates to selection model changed property.

**See Also:**
- Constant Field Values

---

#### protected static final int fontChanged

The bit relates to font changed property.

**See Also:**
- Constant Field Values

---

#### protected static final int fixedCellWidthChanged

The bit relates to fixed cell width changed property.

**See Also:**
- Constant Field Values

---

#### protected static final int fixedCellHeightChanged

The bit relates to fixed cell height changed property.

**See Also:**
- Constant Field Values

---

#### protected static final int prototypeCellValueChanged

The bit relates to prototype cell value changed property.

**See Also:**
- Constant Field Values

---

#### protected static final int cellRendererChanged

The bit relates to cell renderer changed property.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public BasicListUI()

*No description found.*

---

### Method Details

#### protected void paintCell​(
Graphics
g,
int row,

Rectangle
rowBounds,

ListCellRenderer
<
Object
> cellRenderer,

ListModel
<
Object
> dataModel,

ListSelectionModel
selModel,
int leadIndex)

Paint one List cell: compute the relevant state, get the "rubber stamp"
cell renderer component, and then use the

CellRendererPane

to paint it.
Subclasses may want to override this method rather than

paint()

.

**Parameters:**
- g

- an instance of

Graphics
- row

- a row
- rowBounds

- a bounding rectangle to render to
- cellRenderer

- a list of

ListCellRenderer
- dataModel

- a list model
- selModel

- a selection model
- leadIndex

- a lead index

**See Also:**
- paint(java.awt.Graphics, javax.swing.JComponent)

---

#### public void paint​(
Graphics
g,

JComponent
c)

Paint the rows that intersect the Graphics objects clipRect. This
method calls paintCell as necessary. Subclasses
may want to override these methods.

**Overrides:**
- paint

in class

ComponentUI

**Parameters:**
- g

- the

Graphics

context in which to paint
- c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**See Also:**
- paintCell(java.awt.Graphics, int, java.awt.Rectangle, javax.swing.ListCellRenderer<java.lang.Object>, javax.swing.ListModel<java.lang.Object>, javax.swing.ListSelectionModel, int)

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

#### public
Dimension
getPreferredSize​(
JComponent
c)

The preferredSize of the list depends upon the layout orientation.

Describes the preferred size for each layout orientation

Layout Orientation

Preferred Size

JList.VERTICAL

The preferredSize of the list is total height of the rows
and the maximum width of the cells. If JList.fixedCellHeight
is specified then the total height of the rows is just
(cellVerticalMargins + fixedCellHeight) * model.getSize() where
rowVerticalMargins is the space we allocate for drawing
the yellow focus outline. Similarly if fixedCellWidth is
specified then we just use that.

JList.VERTICAL_WRAP

If the visible row count is greater than zero, the preferredHeight
is the maximum cell height * visibleRowCount. If the visible row
count is <= 0, the preferred height is either the current height
of the list, or the maximum cell height, whichever is
bigger. The preferred width is than the maximum cell width *
number of columns needed. Where the number of columns needs is
list.height / max cell height. Max cell height is either the fixed
cell height, or is determined by iterating through all the cells
to find the maximum height from the ListCellRenderer.

JList.HORIZONTAL_WRAP

If the visible row count is greater than zero, the preferredHeight
is the maximum cell height * adjustedRowCount. Where
visibleRowCount is used to determine the number of columns.
Because this lays out horizontally the number of rows is
then determined from the column count. For example, lets say
you have a model with 10 items and the visible row count is 8.
The number of columns needed to display this is 2, but you no
longer need 8 rows to display this, you only need 5, thus
the adjustedRowCount is 5.

If the visible row count is <= 0, the preferred height is dictated
by the number of columns, which will be as many as can fit in the
width of the

JList

(width / max cell width), with at least
one column. The preferred height then becomes the model size / number
of columns * maximum cell height. Max cell height is either the fixed
cell height, or is determined by iterating through all the cells to
find the maximum height from the ListCellRenderer.

The above specifies the raw preferred width and height. The resulting
preferred width is the above width + insets.left + insets.right and
the resulting preferred height is the above height + insets.top +
insets.bottom. Where the

Insets

are determined from

list.getInsets()

.

**Overrides:**
- getPreferredSize

in class

ComponentUI

**Parameters:**
- c

- The JList component.

**Returns:**
- The total size of the list.

**See Also:**
- JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

---

#### protected void selectPreviousIndex()

Selected the previous row and force it to be visible.

**See Also:**
- JList.ensureIndexIsVisible(int)

---

#### protected void selectNextIndex()

Selected the previous row and force it to be visible.

**See Also:**
- JList.ensureIndexIsVisible(int)

---

#### protected void installKeyboardActions()

Registers the keyboard bindings on the

JList

that the

BasicListUI

is associated with. This method is called at
installUI() time.

**See Also:**
- installUI(javax.swing.JComponent)

---

#### protected void uninstallKeyboardActions()

Unregisters keyboard actions installed from

installKeyboardActions

.
This method is called at uninstallUI() time - subclassess should
ensure that all of the keyboard actions registered at installUI
time are removed here.

**See Also:**
- installUI(javax.swing.JComponent)

---

#### protected void installListeners()

Creates and installs the listeners for the JList, its model, and its
selectionModel. This method is called at installUI() time.

**See Also:**
- installUI(javax.swing.JComponent)

,

uninstallListeners()

---

#### protected void uninstallListeners()

Removes the listeners from the JList, its model, and its
selectionModel. All of the listener fields, are reset to
null here. This method is called at uninstallUI() time,
it should be kept in sync with installListeners.

**See Also:**
- uninstallUI(javax.swing.JComponent)

,

installListeners()

---

#### protected void installDefaults()

Initializes list properties such as font, foreground, and background,
and adds the CellRendererPane. The font, foreground, and background
properties are only set if their current value is either null
or a UIResource, other properties are set if the current
value is null.

**See Also:**
- uninstallDefaults()

,

installUI(javax.swing.JComponent)

,

CellRendererPane

---

#### protected void uninstallDefaults()

Sets the list properties that have not been explicitly overridden to

null

. A property is considered overridden if its current value
is not a

UIResource

.

**See Also:**
- installDefaults()

,

uninstallUI(javax.swing.JComponent)

,

CellRendererPane

---

#### public void installUI​(
JComponent
c)

Initializes

this.list

by calling

installDefaults()

,

installListeners()

, and

installKeyboardActions()

in order.

**Overrides:**
- installUI

in class

ComponentUI

**Parameters:**
- c

- the component where this UI delegate is being installed

**See Also:**
- installDefaults()

,

installListeners()

,

installKeyboardActions()

---

#### public void uninstallUI​(
JComponent
c)

Uninitializes

this.list

by calling

uninstallListeners()

,

uninstallKeyboardActions()

, and

uninstallDefaults()

in order. Sets this.list to null.

**Overrides:**
- uninstallUI

in class

ComponentUI

**Parameters:**
- c

- the component from which this UI delegate is being removed;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components

**See Also:**
- uninstallListeners()

,

uninstallKeyboardActions()

,

uninstallDefaults()

---

#### public static
ComponentUI
createUI​(
JComponent
list)

Returns a new instance of

BasicListUI

.

BasicListUI

delegates are allocated one per

JList

.

**Parameters:**
- list

- a component

**Returns:**
- a new

ListUI

implementation for the Windows look and feel.

---

#### public int locationToIndex​(
JList
<?> list,

Point
location)

Returns the cell index in the specified

JList

closest to the
given location in the list's coordinate system. To determine if the
cell actually contains the specified location, compare the point against
the cell's bounds, as provided by

getCellBounds

.
This method returns

-1

if the list's model is empty.

**Specified by:**
- locationToIndex

in class

ListUI

**Parameters:**
- list

- the list
- location

- the coordinates of the point

**Returns:**
- the cell index closest to the given location, or

-1

**Throws:**
- NullPointerException

- if

location

is null

---

#### protected int getRowHeight​(int row)

Returns the height of the specified row based on the current layout.

**Parameters:**
- row

- a row

**Returns:**
- the specified row height or -1 if row isn't valid

**See Also:**
- convertYToRow(int)

,

convertRowToY(int)

,

updateLayoutState()

---

#### protected int convertYToRow​(int y0)

Convert the

JList

relative coordinate to the row that contains it,
based on the current layout. If

y0

doesn't fall within any row,
return -1.

**Parameters:**
- y0

- a relative Y coordinate

**Returns:**
- the row that contains y0, or -1

**See Also:**
- getRowHeight(int)

,

updateLayoutState()

---

#### protected int convertRowToY​(int row)

Return the

JList

relative Y coordinate of the origin of the specified
row or -1 if row isn't valid.

**Parameters:**
- row

- a row

**Returns:**
- the Y coordinate of the origin of row, or -1

**See Also:**
- getRowHeight(int)

,

updateLayoutState()

---

#### protected void maybeUpdateLayoutState()

If updateLayoutStateNeeded is non zero, call updateLayoutState() and reset
updateLayoutStateNeeded. This method should be called by methods
before doing any computation based on the geometry of the list.
For example it's the first call in paint() and getPreferredSize().

**See Also:**
- updateLayoutState()

---

#### protected void updateLayoutState()

Recompute the value of cellHeight or cellHeights based
and cellWidth, based on the current font and the current
values of fixedCellWidth, fixedCellHeight, and prototypeCellValue.

**See Also:**
- maybeUpdateLayoutState()

---

#### protected
MouseInputListener
createMouseInputListener()

Creates a delegate that implements

MouseInputListener

.
The delegate is added to the corresponding

java.awt.Component

listener
lists at

installUI()

time. Subclasses can override this method to return
a custom

MouseInputListener

, e.g.

```java
class MyListUI extends BasicListUI {
protected MouseInputListener
createMouseInputListener
() {
return new MyMouseInputHandler();
}
public class MyMouseInputHandler extends MouseInputHandler {
public void mouseMoved(MouseEvent e) {
// do some extra work when the mouse moves
super.mouseMoved(e);
}
}
}
```

**Returns:**
- an instance of

MouseInputListener

**See Also:**
- BasicListUI.MouseInputHandler

,

installUI(javax.swing.JComponent)

---

#### protected
FocusListener
createFocusListener()

Returns an instance of

FocusListener

.

**Returns:**
- an instance of

FocusListener

---

#### protected
ListSelectionListener
createListSelectionListener()

Creates an instance of

ListSelectionHandler

that's added to
the

JLists

by selectionModel as needed. Subclasses can override
this method to return a custom

ListSelectionListener

, e.g.

```java
class MyListUI extends BasicListUI {
protected ListSelectionListener
createListSelectionListener
() {
return new MySelectionListener();
}
public class MySelectionListener extends ListSelectionHandler {
public void valueChanged(ListSelectionEvent e) {
// do some extra work when the selection changes
super.valueChange(e);
}
}
}
```

**Returns:**
- an instance of

ListSelectionHandler

**See Also:**
- BasicListUI.ListSelectionHandler

,

installUI(javax.swing.JComponent)

---

#### protected
ListDataListener
createListDataListener()

Creates an instance of

ListDataListener

that's added to
the

JLists

by model as needed. Subclasses can override
this method to return a custom

ListDataListener

, e.g.

```java
class MyListUI extends BasicListUI {
protected ListDataListener
createListDataListener
() {
return new MyListDataListener();
}
public class MyListDataListener extends ListDataHandler {
public void contentsChanged(ListDataEvent e) {
// do some extra work when the models contents change
super.contentsChange(e);
}
}
}
```

**Returns:**
- an instance of

ListDataListener

**See Also:**
- ListDataListener

,

JList.getModel()

,

installUI(javax.swing.JComponent)

---

#### protected
PropertyChangeListener
createPropertyChangeListener()

Creates an instance of

PropertyChangeHandler

that's added to
the

JList

by

installUI()

. Subclasses can override this method
to return a custom

PropertyChangeListener

, e.g.

```java
class MyListUI extends BasicListUI {
protected PropertyChangeListener
createPropertyChangeListener
() {
return new MyPropertyChangeListener();
}
public class MyPropertyChangeListener extends PropertyChangeHandler {
public void propertyChange(PropertyChangeEvent e) {
if (e.getPropertyName().equals("model")) {
// do some extra work when the model changes
}
super.propertyChange(e);
}
}
}
```

**Returns:**
- an instance of

PropertyChangeHandler

**See Also:**
- PropertyChangeListener

,

installUI(javax.swing.JComponent)

---

### Additional Sections

#### Class BasicListUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ListUI
- - javax.swing.plaf.basic.BasicListUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ListUI
- - javax.swing.plaf.basic.BasicListUI

javax.swing.plaf.ListUI

- javax.swing.plaf.basic.BasicListUI

javax.swing.plaf.basic.BasicListUI

**Direct Known Subclasses:** SynthListUI

```java
public class
BasicListUI

extends
ListUI
```

An extensible implementation of

ListUI

.

BasicListUI

instances cannot be shared between multiple
lists.

public class

BasicListUI

extends

ListUI

An extensible implementation of

ListUI

.

BasicListUI

instances cannot be shared between multiple
lists.

BasicListUI

instances cannot be shared between multiple
lists.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

BasicListUI.FocusHandler

This class should be treated as a "protected" inner class.

class

BasicListUI.ListDataHandler

The

ListDataListener

that's added to the

JLists

model at

installUI time

, and whenever the JList.model property changes.

class

BasicListUI.ListSelectionHandler

The ListSelectionListener that's added to the JLists selection
model at installUI time, and whenever the JList.selectionModel property
changes.

class

BasicListUI.MouseInputHandler

Mouse input, and focus handling for JList.

class

BasicListUI.PropertyChangeHandler

The PropertyChangeListener that's added to the JList at
installUI time.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected int

cellHeight

The height of cell.

protected int[]

cellHeights

The array of cells' height

protected static int

cellRendererChanged

The bit relates to cell renderer changed property.

protected int

cellWidth

The width of cell.

protected static int

fixedCellHeightChanged

The bit relates to fixed cell height changed property.

protected static int

fixedCellWidthChanged

The bit relates to fixed cell width changed property.

protected

FocusListener

focusListener

FocusListener

that attached to

JList

.

protected static int

fontChanged

The bit relates to font changed property.

protected

JList

<

Object

>

list

The instance of

JList

.

protected

ListDataListener

listDataListener

ListDataListener

that attached to

JList

.

protected

ListSelectionListener

listSelectionListener

ListSelectionListener

that attached to

JList

.

protected static int

modelChanged

The bit relates to model changed property.

protected

MouseInputListener

mouseInputListener

MouseInputListener

that attached to

JList

.

protected

PropertyChangeListener

propertyChangeListener

PropertyChangeListener

that attached to

JList

.

protected static int

prototypeCellValueChanged

The bit relates to prototype cell value changed property.

protected

CellRendererPane

rendererPane

The instance of

CellRendererPane

.

protected static int

selectionModelChanged

The bit relates to selection model changed property.

protected int

updateLayoutStateNeeded

The value represents changes to

JList

model.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicListUI

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

protected int

convertRowToY

​(int row)

Return the

JList

relative Y coordinate of the origin of the specified
row or -1 if row isn't valid.

protected int

convertYToRow

​(int y0)

Convert the

JList

relative coordinate to the row that contains it,
based on the current layout.

protected

FocusListener

createFocusListener

()

Returns an instance of

FocusListener

.

protected

ListDataListener

createListDataListener

()

Creates an instance of

ListDataListener

that's added to
the

JLists

by model as needed.

protected

ListSelectionListener

createListSelectionListener

()

Creates an instance of

ListSelectionHandler

that's added to
the

JLists

by selectionModel as needed.

protected

MouseInputListener

createMouseInputListener

()

Creates a delegate that implements

MouseInputListener

.

protected

PropertyChangeListener

createPropertyChangeListener

()

Creates an instance of

PropertyChangeHandler

that's added to
the

JList

by

installUI()

.

static

ComponentUI

createUI

​(

JComponent

list)

Returns a new instance of

BasicListUI

.

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

Dimension

getPreferredSize

​(

JComponent

c)

The preferredSize of the list depends upon the layout orientation.

protected int

getRowHeight

​(int row)

Returns the height of the specified row based on the current layout.

protected void

installDefaults

()

Initializes list properties such as font, foreground, and background,
and adds the CellRendererPane.

protected void

installKeyboardActions

()

Registers the keyboard bindings on the

JList

that the

BasicListUI

is associated with.

protected void

installListeners

()

Creates and installs the listeners for the JList, its model, and its
selectionModel.

void

installUI

​(

JComponent

c)

Initializes

this.list

by calling

installDefaults()

,

installListeners()

, and

installKeyboardActions()

in order.

int

locationToIndex

​(

JList

<?> list,

Point

location)

Returns the cell index in the specified

JList

closest to the
given location in the list's coordinate system.

protected void

maybeUpdateLayoutState

()

If updateLayoutStateNeeded is non zero, call updateLayoutState() and reset
updateLayoutStateNeeded.

void

paint

​(

Graphics

g,

JComponent

c)

Paint the rows that intersect the Graphics objects clipRect.

protected void

paintCell

​(

Graphics

g,
int row,

Rectangle

rowBounds,

ListCellRenderer

<

Object

> cellRenderer,

ListModel

<

Object

> dataModel,

ListSelectionModel

selModel,
int leadIndex)

Paint one List cell: compute the relevant state, get the "rubber stamp"
cell renderer component, and then use the

CellRendererPane

to paint it.

protected void

selectNextIndex

()

Selected the previous row and force it to be visible.

protected void

selectPreviousIndex

()

Selected the previous row and force it to be visible.

protected void

uninstallDefaults

()

Sets the list properties that have not been explicitly overridden to

null

.

protected void

uninstallKeyboardActions

()

Unregisters keyboard actions installed from

installKeyboardActions

.

protected void

uninstallListeners

()

Removes the listeners from the JList, its model, and its
selectionModel.

void

uninstallUI

​(

JComponent

c)

Uninitializes

this.list

by calling

uninstallListeners()

,

uninstallKeyboardActions()

, and

uninstallDefaults()

in order.

protected void

updateLayoutState

()

Recompute the value of cellHeight or cellHeights based
and cellWidth, based on the current font and the current
values of fixedCellWidth, fixedCellHeight, and prototypeCellValue.

- Methods declared in class javax.swing.plaf.

ListUI

getCellBounds

,

indexToLocation

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

BasicListUI.FocusHandler

This class should be treated as a "protected" inner class.

class

BasicListUI.ListDataHandler

The

ListDataListener

that's added to the

JLists

model at

installUI time

, and whenever the JList.model property changes.

class

BasicListUI.ListSelectionHandler

The ListSelectionListener that's added to the JLists selection
model at installUI time, and whenever the JList.selectionModel property
changes.

class

BasicListUI.MouseInputHandler

Mouse input, and focus handling for JList.

class

BasicListUI.PropertyChangeHandler

The PropertyChangeListener that's added to the JList at
installUI time.

---

#### Nested Class Summary

This class should be treated as a "protected" inner class.

The

ListDataListener

that's added to the

JLists

model at

installUI time

, and whenever the JList.model property changes.

The ListSelectionListener that's added to the JLists selection
model at installUI time, and whenever the JList.selectionModel property
changes.

Mouse input, and focus handling for JList.

The PropertyChangeListener that's added to the JList at
installUI time.

Field Summary

Fields

Modifier and Type

Field

Description

protected int

cellHeight

The height of cell.

protected int[]

cellHeights

The array of cells' height

protected static int

cellRendererChanged

The bit relates to cell renderer changed property.

protected int

cellWidth

The width of cell.

protected static int

fixedCellHeightChanged

The bit relates to fixed cell height changed property.

protected static int

fixedCellWidthChanged

The bit relates to fixed cell width changed property.

protected

FocusListener

focusListener

FocusListener

that attached to

JList

.

protected static int

fontChanged

The bit relates to font changed property.

protected

JList

<

Object

>

list

The instance of

JList

.

protected

ListDataListener

listDataListener

ListDataListener

that attached to

JList

.

protected

ListSelectionListener

listSelectionListener

ListSelectionListener

that attached to

JList

.

protected static int

modelChanged

The bit relates to model changed property.

protected

MouseInputListener

mouseInputListener

MouseInputListener

that attached to

JList

.

protected

PropertyChangeListener

propertyChangeListener

PropertyChangeListener

that attached to

JList

.

protected static int

prototypeCellValueChanged

The bit relates to prototype cell value changed property.

protected

CellRendererPane

rendererPane

The instance of

CellRendererPane

.

protected static int

selectionModelChanged

The bit relates to selection model changed property.

protected int

updateLayoutStateNeeded

The value represents changes to

JList

model.

---

#### Field Summary

The height of cell.

The array of cells' height

The bit relates to cell renderer changed property.

The width of cell.

The bit relates to fixed cell height changed property.

The bit relates to fixed cell width changed property.

FocusListener

that attached to

JList

.

The bit relates to font changed property.

The instance of

JList

.

ListDataListener

that attached to

JList

.

ListSelectionListener

that attached to

JList

.

The bit relates to model changed property.

MouseInputListener

that attached to

JList

.

PropertyChangeListener

that attached to

JList

.

The bit relates to prototype cell value changed property.

The instance of

CellRendererPane

.

The bit relates to selection model changed property.

The value represents changes to

JList

model.

Constructor Summary

Constructors

Constructor

Description

BasicListUI

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

protected int

convertRowToY

​(int row)

Return the

JList

relative Y coordinate of the origin of the specified
row or -1 if row isn't valid.

protected int

convertYToRow

​(int y0)

Convert the

JList

relative coordinate to the row that contains it,
based on the current layout.

protected

FocusListener

createFocusListener

()

Returns an instance of

FocusListener

.

protected

ListDataListener

createListDataListener

()

Creates an instance of

ListDataListener

that's added to
the

JLists

by model as needed.

protected

ListSelectionListener

createListSelectionListener

()

Creates an instance of

ListSelectionHandler

that's added to
the

JLists

by selectionModel as needed.

protected

MouseInputListener

createMouseInputListener

()

Creates a delegate that implements

MouseInputListener

.

protected

PropertyChangeListener

createPropertyChangeListener

()

Creates an instance of

PropertyChangeHandler

that's added to
the

JList

by

installUI()

.

static

ComponentUI

createUI

​(

JComponent

list)

Returns a new instance of

BasicListUI

.

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

Dimension

getPreferredSize

​(

JComponent

c)

The preferredSize of the list depends upon the layout orientation.

protected int

getRowHeight

​(int row)

Returns the height of the specified row based on the current layout.

protected void

installDefaults

()

Initializes list properties such as font, foreground, and background,
and adds the CellRendererPane.

protected void

installKeyboardActions

()

Registers the keyboard bindings on the

JList

that the

BasicListUI

is associated with.

protected void

installListeners

()

Creates and installs the listeners for the JList, its model, and its
selectionModel.

void

installUI

​(

JComponent

c)

Initializes

this.list

by calling

installDefaults()

,

installListeners()

, and

installKeyboardActions()

in order.

int

locationToIndex

​(

JList

<?> list,

Point

location)

Returns the cell index in the specified

JList

closest to the
given location in the list's coordinate system.

protected void

maybeUpdateLayoutState

()

If updateLayoutStateNeeded is non zero, call updateLayoutState() and reset
updateLayoutStateNeeded.

void

paint

​(

Graphics

g,

JComponent

c)

Paint the rows that intersect the Graphics objects clipRect.

protected void

paintCell

​(

Graphics

g,
int row,

Rectangle

rowBounds,

ListCellRenderer

<

Object

> cellRenderer,

ListModel

<

Object

> dataModel,

ListSelectionModel

selModel,
int leadIndex)

Paint one List cell: compute the relevant state, get the "rubber stamp"
cell renderer component, and then use the

CellRendererPane

to paint it.

protected void

selectNextIndex

()

Selected the previous row and force it to be visible.

protected void

selectPreviousIndex

()

Selected the previous row and force it to be visible.

protected void

uninstallDefaults

()

Sets the list properties that have not been explicitly overridden to

null

.

protected void

uninstallKeyboardActions

()

Unregisters keyboard actions installed from

installKeyboardActions

.

protected void

uninstallListeners

()

Removes the listeners from the JList, its model, and its
selectionModel.

void

uninstallUI

​(

JComponent

c)

Uninitializes

this.list

by calling

uninstallListeners()

,

uninstallKeyboardActions()

, and

uninstallDefaults()

in order.

protected void

updateLayoutState

()

Recompute the value of cellHeight or cellHeights based
and cellWidth, based on the current font and the current
values of fixedCellWidth, fixedCellHeight, and prototypeCellValue.

- Methods declared in class javax.swing.plaf.

ListUI

getCellBounds

,

indexToLocation

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

Return the

JList

relative Y coordinate of the origin of the specified
row or -1 if row isn't valid.

Convert the

JList

relative coordinate to the row that contains it,
based on the current layout.

Returns an instance of

FocusListener

.

Creates an instance of

ListDataListener

that's added to
the

JLists

by model as needed.

Creates an instance of

ListSelectionHandler

that's added to
the

JLists

by selectionModel as needed.

Creates a delegate that implements

MouseInputListener

.

Creates an instance of

PropertyChangeHandler

that's added to
the

JList

by

installUI()

.

Returns a new instance of

BasicListUI

.

Returns the baseline.

Returns an enum indicating how the baseline of the component
changes as the size changes.

The preferredSize of the list depends upon the layout orientation.

Returns the height of the specified row based on the current layout.

Initializes list properties such as font, foreground, and background,
and adds the CellRendererPane.

Registers the keyboard bindings on the

JList

that the

BasicListUI

is associated with.

Creates and installs the listeners for the JList, its model, and its
selectionModel.

Initializes

this.list

by calling

installDefaults()

,

installListeners()

, and

installKeyboardActions()

in order.

Returns the cell index in the specified

JList

closest to the
given location in the list's coordinate system.

If updateLayoutStateNeeded is non zero, call updateLayoutState() and reset
updateLayoutStateNeeded.

Paint the rows that intersect the Graphics objects clipRect.

Paint one List cell: compute the relevant state, get the "rubber stamp"
cell renderer component, and then use the

CellRendererPane

to paint it.

Selected the previous row and force it to be visible.

Sets the list properties that have not been explicitly overridden to

null

.

Unregisters keyboard actions installed from

installKeyboardActions

.

Removes the listeners from the JList, its model, and its
selectionModel.

Uninitializes

this.list

by calling

uninstallListeners()

,

uninstallKeyboardActions()

, and

uninstallDefaults()

in order.

Recompute the value of cellHeight or cellHeights based
and cellWidth, based on the current font and the current
values of fixedCellWidth, fixedCellHeight, and prototypeCellValue.

Methods declared in class javax.swing.plaf.

ListUI

getCellBounds

,

indexToLocation

---

#### Methods declared in class javax.swing.plaf. ListUI

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

- list

```java
protected
JList
<
Object
> list
```

The instance of

JList

.

- rendererPane

```java
protected
CellRendererPane
rendererPane
```

The instance of

CellRendererPane

.

- focusListener

```java
protected
FocusListener
focusListener
```

FocusListener

that attached to

JList

.

- mouseInputListener

```java
protected
MouseInputListener
mouseInputListener
```

MouseInputListener

that attached to

JList

.

- listSelectionListener

```java
protected
ListSelectionListener
listSelectionListener
```

ListSelectionListener

that attached to

JList

.

- listDataListener

```java
protected
ListDataListener
listDataListener
```

ListDataListener

that attached to

JList

.

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

PropertyChangeListener

that attached to

JList

.

- cellHeights

```java
protected int[] cellHeights
```

The array of cells' height

- cellHeight

```java
protected int cellHeight
```

The height of cell.

- cellWidth

```java
protected int cellWidth
```

The width of cell.

- updateLayoutStateNeeded

```java
protected int updateLayoutStateNeeded
```

The value represents changes to

JList

model.

- modelChanged

```java
protected static final int modelChanged
```

The bit relates to model changed property.

**See Also:** Constant Field Values

- selectionModelChanged

```java
protected static final int selectionModelChanged
```

The bit relates to selection model changed property.

**See Also:** Constant Field Values

- fontChanged

```java
protected static final int fontChanged
```

The bit relates to font changed property.

**See Also:** Constant Field Values

- fixedCellWidthChanged

```java
protected static final int fixedCellWidthChanged
```

The bit relates to fixed cell width changed property.

**See Also:** Constant Field Values

- fixedCellHeightChanged

```java
protected static final int fixedCellHeightChanged
```

The bit relates to fixed cell height changed property.

**See Also:** Constant Field Values

- prototypeCellValueChanged

```java
protected static final int prototypeCellValueChanged
```

The bit relates to prototype cell value changed property.

**See Also:** Constant Field Values

- cellRendererChanged

```java
protected static final int cellRendererChanged
```

The bit relates to cell renderer changed property.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicListUI

```java
public BasicListUI()
```

============ METHOD DETAIL ==========

- Method Detail

- paintCell

```java
protected void paintCell​(
Graphics
g,
int row,

Rectangle
rowBounds,

ListCellRenderer
<
Object
> cellRenderer,

ListModel
<
Object
> dataModel,

ListSelectionModel
selModel,
int leadIndex)
```

Paint one List cell: compute the relevant state, get the "rubber stamp"
cell renderer component, and then use the

CellRendererPane

to paint it.
Subclasses may want to override this method rather than

paint()

.

**Parameters:** g

- an instance of

Graphics
**Parameters:** row

- a row
**Parameters:** rowBounds

- a bounding rectangle to render to
**Parameters:** cellRenderer

- a list of

ListCellRenderer
**Parameters:** dataModel

- a list model
**Parameters:** selModel

- a selection model
**Parameters:** leadIndex

- a lead index
**See Also:** paint(java.awt.Graphics, javax.swing.JComponent)

- paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paint the rows that intersect the Graphics objects clipRect. This
method calls paintCell as necessary. Subclasses
may want to override these methods.

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** paintCell(java.awt.Graphics, int, java.awt.Rectangle, javax.swing.ListCellRenderer<java.lang.Object>, javax.swing.ListModel<java.lang.Object>, javax.swing.ListSelectionModel, int)

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

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

The preferredSize of the list depends upon the layout orientation.

Describes the preferred size for each layout orientation

Layout Orientation

Preferred Size

JList.VERTICAL

The preferredSize of the list is total height of the rows
and the maximum width of the cells. If JList.fixedCellHeight
is specified then the total height of the rows is just
(cellVerticalMargins + fixedCellHeight) * model.getSize() where
rowVerticalMargins is the space we allocate for drawing
the yellow focus outline. Similarly if fixedCellWidth is
specified then we just use that.

JList.VERTICAL_WRAP

If the visible row count is greater than zero, the preferredHeight
is the maximum cell height * visibleRowCount. If the visible row
count is <= 0, the preferred height is either the current height
of the list, or the maximum cell height, whichever is
bigger. The preferred width is than the maximum cell width *
number of columns needed. Where the number of columns needs is
list.height / max cell height. Max cell height is either the fixed
cell height, or is determined by iterating through all the cells
to find the maximum height from the ListCellRenderer.

JList.HORIZONTAL_WRAP

If the visible row count is greater than zero, the preferredHeight
is the maximum cell height * adjustedRowCount. Where
visibleRowCount is used to determine the number of columns.
Because this lays out horizontally the number of rows is
then determined from the column count. For example, lets say
you have a model with 10 items and the visible row count is 8.
The number of columns needed to display this is 2, but you no
longer need 8 rows to display this, you only need 5, thus
the adjustedRowCount is 5.

If the visible row count is <= 0, the preferred height is dictated
by the number of columns, which will be as many as can fit in the
width of the

JList

(width / max cell width), with at least
one column. The preferred height then becomes the model size / number
of columns * maximum cell height. Max cell height is either the fixed
cell height, or is determined by iterating through all the cells to
find the maximum height from the ListCellRenderer.

The above specifies the raw preferred width and height. The resulting
preferred width is the above width + insets.left + insets.right and
the resulting preferred height is the above height + insets.top +
insets.bottom. Where the

Insets

are determined from

list.getInsets()

.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** c

- The JList component.
**Returns:** The total size of the list.
**See Also:** JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

- selectPreviousIndex

```java
protected void selectPreviousIndex()
```

Selected the previous row and force it to be visible.

**See Also:** JList.ensureIndexIsVisible(int)

- selectNextIndex

```java
protected void selectNextIndex()
```

Selected the previous row and force it to be visible.

**See Also:** JList.ensureIndexIsVisible(int)

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Registers the keyboard bindings on the

JList

that the

BasicListUI

is associated with. This method is called at
installUI() time.

**See Also:** installUI(javax.swing.JComponent)

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions installed from

installKeyboardActions

.
This method is called at uninstallUI() time - subclassess should
ensure that all of the keyboard actions registered at installUI
time are removed here.

**See Also:** installUI(javax.swing.JComponent)

- installListeners

```java
protected void installListeners()
```

Creates and installs the listeners for the JList, its model, and its
selectionModel. This method is called at installUI() time.

**See Also:** installUI(javax.swing.JComponent)

,

uninstallListeners()

- uninstallListeners

```java
protected void uninstallListeners()
```

Removes the listeners from the JList, its model, and its
selectionModel. All of the listener fields, are reset to
null here. This method is called at uninstallUI() time,
it should be kept in sync with installListeners.

**See Also:** uninstallUI(javax.swing.JComponent)

,

installListeners()

- installDefaults

```java
protected void installDefaults()
```

Initializes list properties such as font, foreground, and background,
and adds the CellRendererPane. The font, foreground, and background
properties are only set if their current value is either null
or a UIResource, other properties are set if the current
value is null.

**See Also:** uninstallDefaults()

,

installUI(javax.swing.JComponent)

,

CellRendererPane

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Sets the list properties that have not been explicitly overridden to

null

. A property is considered overridden if its current value
is not a

UIResource

.

**See Also:** installDefaults()

,

uninstallUI(javax.swing.JComponent)

,

CellRendererPane

- installUI

```java
public void installUI​(
JComponent
c)
```

Initializes

this.list

by calling

installDefaults()

,

installListeners()

, and

installKeyboardActions()

in order.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- the component where this UI delegate is being installed
**See Also:** installDefaults()

,

installListeners()

,

installKeyboardActions()

- uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Uninitializes

this.list

by calling

uninstallListeners()

,

uninstallKeyboardActions()

, and

uninstallDefaults()

in order. Sets this.list to null.

**Overrides:** uninstallUI

in class

ComponentUI
**Parameters:** c

- the component from which this UI delegate is being removed;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** uninstallListeners()

,

uninstallKeyboardActions()

,

uninstallDefaults()

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
list)
```

Returns a new instance of

BasicListUI

.

BasicListUI

delegates are allocated one per

JList

.

**Parameters:** list

- a component
**Returns:** a new

ListUI

implementation for the Windows look and feel.

- locationToIndex

```java
public int locationToIndex​(
JList
<?> list,

Point
location)
```

Returns the cell index in the specified

JList

closest to the
given location in the list's coordinate system. To determine if the
cell actually contains the specified location, compare the point against
the cell's bounds, as provided by

getCellBounds

.
This method returns

-1

if the list's model is empty.

**Specified by:** locationToIndex

in class

ListUI
**Parameters:** list

- the list
**Parameters:** location

- the coordinates of the point
**Returns:** the cell index closest to the given location, or

-1
**Throws:** NullPointerException

- if

location

is null

- getRowHeight

```java
protected int getRowHeight​(int row)
```

Returns the height of the specified row based on the current layout.

**Parameters:** row

- a row
**Returns:** the specified row height or -1 if row isn't valid
**See Also:** convertYToRow(int)

,

convertRowToY(int)

,

updateLayoutState()

- convertYToRow

```java
protected int convertYToRow​(int y0)
```

Convert the

JList

relative coordinate to the row that contains it,
based on the current layout. If

y0

doesn't fall within any row,
return -1.

**Parameters:** y0

- a relative Y coordinate
**Returns:** the row that contains y0, or -1
**See Also:** getRowHeight(int)

,

updateLayoutState()

- convertRowToY

```java
protected int convertRowToY​(int row)
```

Return the

JList

relative Y coordinate of the origin of the specified
row or -1 if row isn't valid.

**Parameters:** row

- a row
**Returns:** the Y coordinate of the origin of row, or -1
**See Also:** getRowHeight(int)

,

updateLayoutState()

- maybeUpdateLayoutState

```java
protected void maybeUpdateLayoutState()
```

If updateLayoutStateNeeded is non zero, call updateLayoutState() and reset
updateLayoutStateNeeded. This method should be called by methods
before doing any computation based on the geometry of the list.
For example it's the first call in paint() and getPreferredSize().

**See Also:** updateLayoutState()

- updateLayoutState

```java
protected void updateLayoutState()
```

Recompute the value of cellHeight or cellHeights based
and cellWidth, based on the current font and the current
values of fixedCellWidth, fixedCellHeight, and prototypeCellValue.

**See Also:** maybeUpdateLayoutState()

- createMouseInputListener

```java
protected
MouseInputListener
createMouseInputListener()
```

Creates a delegate that implements

MouseInputListener

.
The delegate is added to the corresponding

java.awt.Component

listener
lists at

installUI()

time. Subclasses can override this method to return
a custom

MouseInputListener

, e.g.

```java
class MyListUI extends BasicListUI {
protected MouseInputListener
createMouseInputListener
() {
return new MyMouseInputHandler();
}
public class MyMouseInputHandler extends MouseInputHandler {
public void mouseMoved(MouseEvent e) {
// do some extra work when the mouse moves
super.mouseMoved(e);
}
}
}
```

**Returns:** an instance of

MouseInputListener
**See Also:** BasicListUI.MouseInputHandler

,

installUI(javax.swing.JComponent)

- createFocusListener

```java
protected
FocusListener
createFocusListener()
```

Returns an instance of

FocusListener

.

**Returns:** an instance of

FocusListener

- createListSelectionListener

```java
protected
ListSelectionListener
createListSelectionListener()
```

Creates an instance of

ListSelectionHandler

that's added to
the

JLists

by selectionModel as needed. Subclasses can override
this method to return a custom

ListSelectionListener

, e.g.

```java
class MyListUI extends BasicListUI {
protected ListSelectionListener
createListSelectionListener
() {
return new MySelectionListener();
}
public class MySelectionListener extends ListSelectionHandler {
public void valueChanged(ListSelectionEvent e) {
// do some extra work when the selection changes
super.valueChange(e);
}
}
}
```

**Returns:** an instance of

ListSelectionHandler
**See Also:** BasicListUI.ListSelectionHandler

,

installUI(javax.swing.JComponent)

- createListDataListener

```java
protected
ListDataListener
createListDataListener()
```

Creates an instance of

ListDataListener

that's added to
the

JLists

by model as needed. Subclasses can override
this method to return a custom

ListDataListener

, e.g.

```java
class MyListUI extends BasicListUI {
protected ListDataListener
createListDataListener
() {
return new MyListDataListener();
}
public class MyListDataListener extends ListDataHandler {
public void contentsChanged(ListDataEvent e) {
// do some extra work when the models contents change
super.contentsChange(e);
}
}
}
```

**Returns:** an instance of

ListDataListener
**See Also:** ListDataListener

,

JList.getModel()

,

installUI(javax.swing.JComponent)

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates an instance of

PropertyChangeHandler

that's added to
the

JList

by

installUI()

. Subclasses can override this method
to return a custom

PropertyChangeListener

, e.g.

```java
class MyListUI extends BasicListUI {
protected PropertyChangeListener
createPropertyChangeListener
() {
return new MyPropertyChangeListener();
}
public class MyPropertyChangeListener extends PropertyChangeHandler {
public void propertyChange(PropertyChangeEvent e) {
if (e.getPropertyName().equals("model")) {
// do some extra work when the model changes
}
super.propertyChange(e);
}
}
}
```

**Returns:** an instance of

PropertyChangeHandler
**See Also:** PropertyChangeListener

,

installUI(javax.swing.JComponent)

Field Detail

- list

```java
protected
JList
<
Object
> list
```

The instance of

JList

.

- rendererPane

```java
protected
CellRendererPane
rendererPane
```

The instance of

CellRendererPane

.

- focusListener

```java
protected
FocusListener
focusListener
```

FocusListener

that attached to

JList

.

- mouseInputListener

```java
protected
MouseInputListener
mouseInputListener
```

MouseInputListener

that attached to

JList

.

- listSelectionListener

```java
protected
ListSelectionListener
listSelectionListener
```

ListSelectionListener

that attached to

JList

.

- listDataListener

```java
protected
ListDataListener
listDataListener
```

ListDataListener

that attached to

JList

.

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

PropertyChangeListener

that attached to

JList

.

- cellHeights

```java
protected int[] cellHeights
```

The array of cells' height

- cellHeight

```java
protected int cellHeight
```

The height of cell.

- cellWidth

```java
protected int cellWidth
```

The width of cell.

- updateLayoutStateNeeded

```java
protected int updateLayoutStateNeeded
```

The value represents changes to

JList

model.

- modelChanged

```java
protected static final int modelChanged
```

The bit relates to model changed property.

**See Also:** Constant Field Values

- selectionModelChanged

```java
protected static final int selectionModelChanged
```

The bit relates to selection model changed property.

**See Also:** Constant Field Values

- fontChanged

```java
protected static final int fontChanged
```

The bit relates to font changed property.

**See Also:** Constant Field Values

- fixedCellWidthChanged

```java
protected static final int fixedCellWidthChanged
```

The bit relates to fixed cell width changed property.

**See Also:** Constant Field Values

- fixedCellHeightChanged

```java
protected static final int fixedCellHeightChanged
```

The bit relates to fixed cell height changed property.

**See Also:** Constant Field Values

- prototypeCellValueChanged

```java
protected static final int prototypeCellValueChanged
```

The bit relates to prototype cell value changed property.

**See Also:** Constant Field Values

- cellRendererChanged

```java
protected static final int cellRendererChanged
```

The bit relates to cell renderer changed property.

**See Also:** Constant Field Values

---

#### Field Detail

list

```java
protected
JList
<
Object
> list
```

The instance of

JList

.

---

#### list

protected

JList

<

Object

> list

The instance of

JList

.

rendererPane

```java
protected
CellRendererPane
rendererPane
```

The instance of

CellRendererPane

.

---

#### rendererPane

protected

CellRendererPane

rendererPane

The instance of

CellRendererPane

.

focusListener

```java
protected
FocusListener
focusListener
```

FocusListener

that attached to

JList

.

---

#### focusListener

protected

FocusListener

focusListener

FocusListener

that attached to

JList

.

mouseInputListener

```java
protected
MouseInputListener
mouseInputListener
```

MouseInputListener

that attached to

JList

.

---

#### mouseInputListener

protected

MouseInputListener

mouseInputListener

MouseInputListener

that attached to

JList

.

listSelectionListener

```java
protected
ListSelectionListener
listSelectionListener
```

ListSelectionListener

that attached to

JList

.

---

#### listSelectionListener

protected

ListSelectionListener

listSelectionListener

ListSelectionListener

that attached to

JList

.

listDataListener

```java
protected
ListDataListener
listDataListener
```

ListDataListener

that attached to

JList

.

---

#### listDataListener

protected

ListDataListener

listDataListener

ListDataListener

that attached to

JList

.

propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

PropertyChangeListener

that attached to

JList

.

---

#### propertyChangeListener

protected

PropertyChangeListener

propertyChangeListener

PropertyChangeListener

that attached to

JList

.

cellHeights

```java
protected int[] cellHeights
```

The array of cells' height

---

#### cellHeights

protected int[] cellHeights

The array of cells' height

cellHeight

```java
protected int cellHeight
```

The height of cell.

---

#### cellHeight

protected int cellHeight

The height of cell.

cellWidth

```java
protected int cellWidth
```

The width of cell.

---

#### cellWidth

protected int cellWidth

The width of cell.

updateLayoutStateNeeded

```java
protected int updateLayoutStateNeeded
```

The value represents changes to

JList

model.

---

#### updateLayoutStateNeeded

protected int updateLayoutStateNeeded

The value represents changes to

JList

model.

modelChanged

```java
protected static final int modelChanged
```

The bit relates to model changed property.

**See Also:** Constant Field Values

---

#### modelChanged

protected static final int modelChanged

The bit relates to model changed property.

selectionModelChanged

```java
protected static final int selectionModelChanged
```

The bit relates to selection model changed property.

**See Also:** Constant Field Values

---

#### selectionModelChanged

protected static final int selectionModelChanged

The bit relates to selection model changed property.

fontChanged

```java
protected static final int fontChanged
```

The bit relates to font changed property.

**See Also:** Constant Field Values

---

#### fontChanged

protected static final int fontChanged

The bit relates to font changed property.

fixedCellWidthChanged

```java
protected static final int fixedCellWidthChanged
```

The bit relates to fixed cell width changed property.

**See Also:** Constant Field Values

---

#### fixedCellWidthChanged

protected static final int fixedCellWidthChanged

The bit relates to fixed cell width changed property.

fixedCellHeightChanged

```java
protected static final int fixedCellHeightChanged
```

The bit relates to fixed cell height changed property.

**See Also:** Constant Field Values

---

#### fixedCellHeightChanged

protected static final int fixedCellHeightChanged

The bit relates to fixed cell height changed property.

prototypeCellValueChanged

```java
protected static final int prototypeCellValueChanged
```

The bit relates to prototype cell value changed property.

**See Also:** Constant Field Values

---

#### prototypeCellValueChanged

protected static final int prototypeCellValueChanged

The bit relates to prototype cell value changed property.

cellRendererChanged

```java
protected static final int cellRendererChanged
```

The bit relates to cell renderer changed property.

**See Also:** Constant Field Values

---

#### cellRendererChanged

protected static final int cellRendererChanged

The bit relates to cell renderer changed property.

Constructor Detail

- BasicListUI

```java
public BasicListUI()
```

---

#### Constructor Detail

BasicListUI

```java
public BasicListUI()
```

---

#### BasicListUI

public BasicListUI()

Method Detail

- paintCell

```java
protected void paintCell​(
Graphics
g,
int row,

Rectangle
rowBounds,

ListCellRenderer
<
Object
> cellRenderer,

ListModel
<
Object
> dataModel,

ListSelectionModel
selModel,
int leadIndex)
```

Paint one List cell: compute the relevant state, get the "rubber stamp"
cell renderer component, and then use the

CellRendererPane

to paint it.
Subclasses may want to override this method rather than

paint()

.

**Parameters:** g

- an instance of

Graphics
**Parameters:** row

- a row
**Parameters:** rowBounds

- a bounding rectangle to render to
**Parameters:** cellRenderer

- a list of

ListCellRenderer
**Parameters:** dataModel

- a list model
**Parameters:** selModel

- a selection model
**Parameters:** leadIndex

- a lead index
**See Also:** paint(java.awt.Graphics, javax.swing.JComponent)

- paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paint the rows that intersect the Graphics objects clipRect. This
method calls paintCell as necessary. Subclasses
may want to override these methods.

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** paintCell(java.awt.Graphics, int, java.awt.Rectangle, javax.swing.ListCellRenderer<java.lang.Object>, javax.swing.ListModel<java.lang.Object>, javax.swing.ListSelectionModel, int)

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

- getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

The preferredSize of the list depends upon the layout orientation.

Describes the preferred size for each layout orientation

Layout Orientation

Preferred Size

JList.VERTICAL

The preferredSize of the list is total height of the rows
and the maximum width of the cells. If JList.fixedCellHeight
is specified then the total height of the rows is just
(cellVerticalMargins + fixedCellHeight) * model.getSize() where
rowVerticalMargins is the space we allocate for drawing
the yellow focus outline. Similarly if fixedCellWidth is
specified then we just use that.

JList.VERTICAL_WRAP

If the visible row count is greater than zero, the preferredHeight
is the maximum cell height * visibleRowCount. If the visible row
count is <= 0, the preferred height is either the current height
of the list, or the maximum cell height, whichever is
bigger. The preferred width is than the maximum cell width *
number of columns needed. Where the number of columns needs is
list.height / max cell height. Max cell height is either the fixed
cell height, or is determined by iterating through all the cells
to find the maximum height from the ListCellRenderer.

JList.HORIZONTAL_WRAP

If the visible row count is greater than zero, the preferredHeight
is the maximum cell height * adjustedRowCount. Where
visibleRowCount is used to determine the number of columns.
Because this lays out horizontally the number of rows is
then determined from the column count. For example, lets say
you have a model with 10 items and the visible row count is 8.
The number of columns needed to display this is 2, but you no
longer need 8 rows to display this, you only need 5, thus
the adjustedRowCount is 5.

If the visible row count is <= 0, the preferred height is dictated
by the number of columns, which will be as many as can fit in the
width of the

JList

(width / max cell width), with at least
one column. The preferred height then becomes the model size / number
of columns * maximum cell height. Max cell height is either the fixed
cell height, or is determined by iterating through all the cells to
find the maximum height from the ListCellRenderer.

The above specifies the raw preferred width and height. The resulting
preferred width is the above width + insets.left + insets.right and
the resulting preferred height is the above height + insets.top +
insets.bottom. Where the

Insets

are determined from

list.getInsets()

.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** c

- The JList component.
**Returns:** The total size of the list.
**See Also:** JComponent.getPreferredSize()

,

LayoutManager.preferredLayoutSize(java.awt.Container)

- selectPreviousIndex

```java
protected void selectPreviousIndex()
```

Selected the previous row and force it to be visible.

**See Also:** JList.ensureIndexIsVisible(int)

- selectNextIndex

```java
protected void selectNextIndex()
```

Selected the previous row and force it to be visible.

**See Also:** JList.ensureIndexIsVisible(int)

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Registers the keyboard bindings on the

JList

that the

BasicListUI

is associated with. This method is called at
installUI() time.

**See Also:** installUI(javax.swing.JComponent)

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions installed from

installKeyboardActions

.
This method is called at uninstallUI() time - subclassess should
ensure that all of the keyboard actions registered at installUI
time are removed here.

**See Also:** installUI(javax.swing.JComponent)

- installListeners

```java
protected void installListeners()
```

Creates and installs the listeners for the JList, its model, and its
selectionModel. This method is called at installUI() time.

**See Also:** installUI(javax.swing.JComponent)

,

uninstallListeners()

- uninstallListeners

```java
protected void uninstallListeners()
```

Removes the listeners from the JList, its model, and its
selectionModel. All of the listener fields, are reset to
null here. This method is called at uninstallUI() time,
it should be kept in sync with installListeners.

**See Also:** uninstallUI(javax.swing.JComponent)

,

installListeners()

- installDefaults

```java
protected void installDefaults()
```

Initializes list properties such as font, foreground, and background,
and adds the CellRendererPane. The font, foreground, and background
properties are only set if their current value is either null
or a UIResource, other properties are set if the current
value is null.

**See Also:** uninstallDefaults()

,

installUI(javax.swing.JComponent)

,

CellRendererPane

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Sets the list properties that have not been explicitly overridden to

null

. A property is considered overridden if its current value
is not a

UIResource

.

**See Also:** installDefaults()

,

uninstallUI(javax.swing.JComponent)

,

CellRendererPane

- installUI

```java
public void installUI​(
JComponent
c)
```

Initializes

this.list

by calling

installDefaults()

,

installListeners()

, and

installKeyboardActions()

in order.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- the component where this UI delegate is being installed
**See Also:** installDefaults()

,

installListeners()

,

installKeyboardActions()

- uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Uninitializes

this.list

by calling

uninstallListeners()

,

uninstallKeyboardActions()

, and

uninstallDefaults()

in order. Sets this.list to null.

**Overrides:** uninstallUI

in class

ComponentUI
**Parameters:** c

- the component from which this UI delegate is being removed;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** uninstallListeners()

,

uninstallKeyboardActions()

,

uninstallDefaults()

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
list)
```

Returns a new instance of

BasicListUI

.

BasicListUI

delegates are allocated one per

JList

.

**Parameters:** list

- a component
**Returns:** a new

ListUI

implementation for the Windows look and feel.

- locationToIndex

```java
public int locationToIndex​(
JList
<?> list,

Point
location)
```

Returns the cell index in the specified

JList

closest to the
given location in the list's coordinate system. To determine if the
cell actually contains the specified location, compare the point against
the cell's bounds, as provided by

getCellBounds

.
This method returns

-1

if the list's model is empty.

**Specified by:** locationToIndex

in class

ListUI
**Parameters:** list

- the list
**Parameters:** location

- the coordinates of the point
**Returns:** the cell index closest to the given location, or

-1
**Throws:** NullPointerException

- if

location

is null

- getRowHeight

```java
protected int getRowHeight​(int row)
```

Returns the height of the specified row based on the current layout.

**Parameters:** row

- a row
**Returns:** the specified row height or -1 if row isn't valid
**See Also:** convertYToRow(int)

,

convertRowToY(int)

,

updateLayoutState()

- convertYToRow

```java
protected int convertYToRow​(int y0)
```

Convert the

JList

relative coordinate to the row that contains it,
based on the current layout. If

y0

doesn't fall within any row,
return -1.

**Parameters:** y0

- a relative Y coordinate
**Returns:** the row that contains y0, or -1
**See Also:** getRowHeight(int)

,

updateLayoutState()

- convertRowToY

```java
protected int convertRowToY​(int row)
```

Return the

JList

relative Y coordinate of the origin of the specified
row or -1 if row isn't valid.

**Parameters:** row

- a row
**Returns:** the Y coordinate of the origin of row, or -1
**See Also:** getRowHeight(int)

,

updateLayoutState()

- maybeUpdateLayoutState

```java
protected void maybeUpdateLayoutState()
```

If updateLayoutStateNeeded is non zero, call updateLayoutState() and reset
updateLayoutStateNeeded. This method should be called by methods
before doing any computation based on the geometry of the list.
For example it's the first call in paint() and getPreferredSize().

**See Also:** updateLayoutState()

- updateLayoutState

```java
protected void updateLayoutState()
```

Recompute the value of cellHeight or cellHeights based
and cellWidth, based on the current font and the current
values of fixedCellWidth, fixedCellHeight, and prototypeCellValue.

**See Also:** maybeUpdateLayoutState()

- createMouseInputListener

```java
protected
MouseInputListener
createMouseInputListener()
```

Creates a delegate that implements

MouseInputListener

.
The delegate is added to the corresponding

java.awt.Component

listener
lists at

installUI()

time. Subclasses can override this method to return
a custom

MouseInputListener

, e.g.

```java
class MyListUI extends BasicListUI {
protected MouseInputListener
createMouseInputListener
() {
return new MyMouseInputHandler();
}
public class MyMouseInputHandler extends MouseInputHandler {
public void mouseMoved(MouseEvent e) {
// do some extra work when the mouse moves
super.mouseMoved(e);
}
}
}
```

**Returns:** an instance of

MouseInputListener
**See Also:** BasicListUI.MouseInputHandler

,

installUI(javax.swing.JComponent)

- createFocusListener

```java
protected
FocusListener
createFocusListener()
```

Returns an instance of

FocusListener

.

**Returns:** an instance of

FocusListener

- createListSelectionListener

```java
protected
ListSelectionListener
createListSelectionListener()
```

Creates an instance of

ListSelectionHandler

that's added to
the

JLists

by selectionModel as needed. Subclasses can override
this method to return a custom

ListSelectionListener

, e.g.

```java
class MyListUI extends BasicListUI {
protected ListSelectionListener
createListSelectionListener
() {
return new MySelectionListener();
}
public class MySelectionListener extends ListSelectionHandler {
public void valueChanged(ListSelectionEvent e) {
// do some extra work when the selection changes
super.valueChange(e);
}
}
}
```

**Returns:** an instance of

ListSelectionHandler
**See Also:** BasicListUI.ListSelectionHandler

,

installUI(javax.swing.JComponent)

- createListDataListener

```java
protected
ListDataListener
createListDataListener()
```

Creates an instance of

ListDataListener

that's added to
the

JLists

by model as needed. Subclasses can override
this method to return a custom

ListDataListener

, e.g.

```java
class MyListUI extends BasicListUI {
protected ListDataListener
createListDataListener
() {
return new MyListDataListener();
}
public class MyListDataListener extends ListDataHandler {
public void contentsChanged(ListDataEvent e) {
// do some extra work when the models contents change
super.contentsChange(e);
}
}
}
```

**Returns:** an instance of

ListDataListener
**See Also:** ListDataListener

,

JList.getModel()

,

installUI(javax.swing.JComponent)

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates an instance of

PropertyChangeHandler

that's added to
the

JList

by

installUI()

. Subclasses can override this method
to return a custom

PropertyChangeListener

, e.g.

```java
class MyListUI extends BasicListUI {
protected PropertyChangeListener
createPropertyChangeListener
() {
return new MyPropertyChangeListener();
}
public class MyPropertyChangeListener extends PropertyChangeHandler {
public void propertyChange(PropertyChangeEvent e) {
if (e.getPropertyName().equals("model")) {
// do some extra work when the model changes
}
super.propertyChange(e);
}
}
}
```

**Returns:** an instance of

PropertyChangeHandler
**See Also:** PropertyChangeListener

,

installUI(javax.swing.JComponent)

---

#### Method Detail

paintCell

```java
protected void paintCell​(
Graphics
g,
int row,

Rectangle
rowBounds,

ListCellRenderer
<
Object
> cellRenderer,

ListModel
<
Object
> dataModel,

ListSelectionModel
selModel,
int leadIndex)
```

Paint one List cell: compute the relevant state, get the "rubber stamp"
cell renderer component, and then use the

CellRendererPane

to paint it.
Subclasses may want to override this method rather than

paint()

.

**Parameters:** g

- an instance of

Graphics
**Parameters:** row

- a row
**Parameters:** rowBounds

- a bounding rectangle to render to
**Parameters:** cellRenderer

- a list of

ListCellRenderer
**Parameters:** dataModel

- a list model
**Parameters:** selModel

- a selection model
**Parameters:** leadIndex

- a lead index
**See Also:** paint(java.awt.Graphics, javax.swing.JComponent)

---

#### paintCell

protected void paintCell​(

Graphics

g,
int row,

Rectangle

rowBounds,

ListCellRenderer

<

Object

> cellRenderer,

ListModel

<

Object

> dataModel,

ListSelectionModel

selModel,
int leadIndex)

Paint one List cell: compute the relevant state, get the "rubber stamp"
cell renderer component, and then use the

CellRendererPane

to paint it.
Subclasses may want to override this method rather than

paint()

.

paint

```java
public void paint​(
Graphics
g,

JComponent
c)
```

Paint the rows that intersect the Graphics objects clipRect. This
method calls paintCell as necessary. Subclasses
may want to override these methods.

**Overrides:** paint

in class

ComponentUI
**Parameters:** g

- the

Graphics

context in which to paint
**Parameters:** c

- the component being painted;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** paintCell(java.awt.Graphics, int, java.awt.Rectangle, javax.swing.ListCellRenderer<java.lang.Object>, javax.swing.ListModel<java.lang.Object>, javax.swing.ListSelectionModel, int)

---

#### paint

public void paint​(

Graphics

g,

JComponent

c)

Paint the rows that intersect the Graphics objects clipRect. This
method calls paintCell as necessary. Subclasses
may want to override these methods.

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

getPreferredSize

```java
public
Dimension
getPreferredSize​(
JComponent
c)
```

The preferredSize of the list depends upon the layout orientation.

Describes the preferred size for each layout orientation

Layout Orientation

Preferred Size

JList.VERTICAL

The preferredSize of the list is total height of the rows
and the maximum width of the cells. If JList.fixedCellHeight
is specified then the total height of the rows is just
(cellVerticalMargins + fixedCellHeight) * model.getSize() where
rowVerticalMargins is the space we allocate for drawing
the yellow focus outline. Similarly if fixedCellWidth is
specified then we just use that.

JList.VERTICAL_WRAP

If the visible row count is greater than zero, the preferredHeight
is the maximum cell height * visibleRowCount. If the visible row
count is <= 0, the preferred height is either the current height
of the list, or the maximum cell height, whichever is
bigger. The preferred width is than the maximum cell width *
number of columns needed. Where the number of columns needs is
list.height / max cell height. Max cell height is either the fixed
cell height, or is determined by iterating through all the cells
to find the maximum height from the ListCellRenderer.

JList.HORIZONTAL_WRAP

If the visible row count is greater than zero, the preferredHeight
is the maximum cell height * adjustedRowCount. Where
visibleRowCount is used to determine the number of columns.
Because this lays out horizontally the number of rows is
then determined from the column count. For example, lets say
you have a model with 10 items and the visible row count is 8.
The number of columns needed to display this is 2, but you no
longer need 8 rows to display this, you only need 5, thus
the adjustedRowCount is 5.

If the visible row count is <= 0, the preferred height is dictated
by the number of columns, which will be as many as can fit in the
width of the

JList

(width / max cell width), with at least
one column. The preferred height then becomes the model size / number
of columns * maximum cell height. Max cell height is either the fixed
cell height, or is determined by iterating through all the cells to
find the maximum height from the ListCellRenderer.

The above specifies the raw preferred width and height. The resulting
preferred width is the above width + insets.left + insets.right and
the resulting preferred height is the above height + insets.top +
insets.bottom. Where the

Insets

are determined from

list.getInsets()

.

**Overrides:** getPreferredSize

in class

ComponentUI
**Parameters:** c

- The JList component.
**Returns:** The total size of the list.
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

The preferredSize of the list depends upon the layout orientation.

Describes the preferred size for each layout orientation

Layout Orientation

Preferred Size

JList.VERTICAL

The preferredSize of the list is total height of the rows
and the maximum width of the cells. If JList.fixedCellHeight
is specified then the total height of the rows is just
(cellVerticalMargins + fixedCellHeight) * model.getSize() where
rowVerticalMargins is the space we allocate for drawing
the yellow focus outline. Similarly if fixedCellWidth is
specified then we just use that.

JList.VERTICAL_WRAP

If the visible row count is greater than zero, the preferredHeight
is the maximum cell height * visibleRowCount. If the visible row
count is <= 0, the preferred height is either the current height
of the list, or the maximum cell height, whichever is
bigger. The preferred width is than the maximum cell width *
number of columns needed. Where the number of columns needs is
list.height / max cell height. Max cell height is either the fixed
cell height, or is determined by iterating through all the cells
to find the maximum height from the ListCellRenderer.

JList.HORIZONTAL_WRAP

If the visible row count is greater than zero, the preferredHeight
is the maximum cell height * adjustedRowCount. Where
visibleRowCount is used to determine the number of columns.
Because this lays out horizontally the number of rows is
then determined from the column count. For example, lets say
you have a model with 10 items and the visible row count is 8.
The number of columns needed to display this is 2, but you no
longer need 8 rows to display this, you only need 5, thus
the adjustedRowCount is 5.

If the visible row count is <= 0, the preferred height is dictated
by the number of columns, which will be as many as can fit in the
width of the

JList

(width / max cell width), with at least
one column. The preferred height then becomes the model size / number
of columns * maximum cell height. Max cell height is either the fixed
cell height, or is determined by iterating through all the cells to
find the maximum height from the ListCellRenderer.

The above specifies the raw preferred width and height. The resulting
preferred width is the above width + insets.left + insets.right and
the resulting preferred height is the above height + insets.top +
insets.bottom. Where the

Insets

are determined from

list.getInsets()

.

If the visible row count is <= 0, the preferred height is dictated
by the number of columns, which will be as many as can fit in the
width of the

JList

(width / max cell width), with at least
one column. The preferred height then becomes the model size / number
of columns * maximum cell height. Max cell height is either the fixed
cell height, or is determined by iterating through all the cells to
find the maximum height from the ListCellRenderer.

selectPreviousIndex

```java
protected void selectPreviousIndex()
```

Selected the previous row and force it to be visible.

**See Also:** JList.ensureIndexIsVisible(int)

---

#### selectPreviousIndex

protected void selectPreviousIndex()

Selected the previous row and force it to be visible.

selectNextIndex

```java
protected void selectNextIndex()
```

Selected the previous row and force it to be visible.

**See Also:** JList.ensureIndexIsVisible(int)

---

#### selectNextIndex

protected void selectNextIndex()

Selected the previous row and force it to be visible.

installKeyboardActions

```java
protected void installKeyboardActions()
```

Registers the keyboard bindings on the

JList

that the

BasicListUI

is associated with. This method is called at
installUI() time.

**See Also:** installUI(javax.swing.JComponent)

---

#### installKeyboardActions

protected void installKeyboardActions()

Registers the keyboard bindings on the

JList

that the

BasicListUI

is associated with. This method is called at
installUI() time.

uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions installed from

installKeyboardActions

.
This method is called at uninstallUI() time - subclassess should
ensure that all of the keyboard actions registered at installUI
time are removed here.

**See Also:** installUI(javax.swing.JComponent)

---

#### uninstallKeyboardActions

protected void uninstallKeyboardActions()

Unregisters keyboard actions installed from

installKeyboardActions

.
This method is called at uninstallUI() time - subclassess should
ensure that all of the keyboard actions registered at installUI
time are removed here.

installListeners

```java
protected void installListeners()
```

Creates and installs the listeners for the JList, its model, and its
selectionModel. This method is called at installUI() time.

**See Also:** installUI(javax.swing.JComponent)

,

uninstallListeners()

---

#### installListeners

protected void installListeners()

Creates and installs the listeners for the JList, its model, and its
selectionModel. This method is called at installUI() time.

uninstallListeners

```java
protected void uninstallListeners()
```

Removes the listeners from the JList, its model, and its
selectionModel. All of the listener fields, are reset to
null here. This method is called at uninstallUI() time,
it should be kept in sync with installListeners.

**See Also:** uninstallUI(javax.swing.JComponent)

,

installListeners()

---

#### uninstallListeners

protected void uninstallListeners()

Removes the listeners from the JList, its model, and its
selectionModel. All of the listener fields, are reset to
null here. This method is called at uninstallUI() time,
it should be kept in sync with installListeners.

installDefaults

```java
protected void installDefaults()
```

Initializes list properties such as font, foreground, and background,
and adds the CellRendererPane. The font, foreground, and background
properties are only set if their current value is either null
or a UIResource, other properties are set if the current
value is null.

**See Also:** uninstallDefaults()

,

installUI(javax.swing.JComponent)

,

CellRendererPane

---

#### installDefaults

protected void installDefaults()

Initializes list properties such as font, foreground, and background,
and adds the CellRendererPane. The font, foreground, and background
properties are only set if their current value is either null
or a UIResource, other properties are set if the current
value is null.

uninstallDefaults

```java
protected void uninstallDefaults()
```

Sets the list properties that have not been explicitly overridden to

null

. A property is considered overridden if its current value
is not a

UIResource

.

**See Also:** installDefaults()

,

uninstallUI(javax.swing.JComponent)

,

CellRendererPane

---

#### uninstallDefaults

protected void uninstallDefaults()

Sets the list properties that have not been explicitly overridden to

null

. A property is considered overridden if its current value
is not a

UIResource

.

installUI

```java
public void installUI​(
JComponent
c)
```

Initializes

this.list

by calling

installDefaults()

,

installListeners()

, and

installKeyboardActions()

in order.

**Overrides:** installUI

in class

ComponentUI
**Parameters:** c

- the component where this UI delegate is being installed
**See Also:** installDefaults()

,

installListeners()

,

installKeyboardActions()

---

#### installUI

public void installUI​(

JComponent

c)

Initializes

this.list

by calling

installDefaults()

,

installListeners()

, and

installKeyboardActions()

in order.

uninstallUI

```java
public void uninstallUI​(
JComponent
c)
```

Uninitializes

this.list

by calling

uninstallListeners()

,

uninstallKeyboardActions()

, and

uninstallDefaults()

in order. Sets this.list to null.

**Overrides:** uninstallUI

in class

ComponentUI
**Parameters:** c

- the component from which this UI delegate is being removed;
this argument is often ignored,
but might be used if the UI object is stateless
and shared by multiple components
**See Also:** uninstallListeners()

,

uninstallKeyboardActions()

,

uninstallDefaults()

---

#### uninstallUI

public void uninstallUI​(

JComponent

c)

Uninitializes

this.list

by calling

uninstallListeners()

,

uninstallKeyboardActions()

, and

uninstallDefaults()

in order. Sets this.list to null.

createUI

```java
public static
ComponentUI
createUI​(
JComponent
list)
```

Returns a new instance of

BasicListUI

.

BasicListUI

delegates are allocated one per

JList

.

**Parameters:** list

- a component
**Returns:** a new

ListUI

implementation for the Windows look and feel.

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

list)

Returns a new instance of

BasicListUI

.

BasicListUI

delegates are allocated one per

JList

.

locationToIndex

```java
public int locationToIndex​(
JList
<?> list,

Point
location)
```

Returns the cell index in the specified

JList

closest to the
given location in the list's coordinate system. To determine if the
cell actually contains the specified location, compare the point against
the cell's bounds, as provided by

getCellBounds

.
This method returns

-1

if the list's model is empty.

**Specified by:** locationToIndex

in class

ListUI
**Parameters:** list

- the list
**Parameters:** location

- the coordinates of the point
**Returns:** the cell index closest to the given location, or

-1
**Throws:** NullPointerException

- if

location

is null

---

#### locationToIndex

public int locationToIndex​(

JList

<?> list,

Point

location)

Returns the cell index in the specified

JList

closest to the
given location in the list's coordinate system. To determine if the
cell actually contains the specified location, compare the point against
the cell's bounds, as provided by

getCellBounds

.
This method returns

-1

if the list's model is empty.

getRowHeight

```java
protected int getRowHeight​(int row)
```

Returns the height of the specified row based on the current layout.

**Parameters:** row

- a row
**Returns:** the specified row height or -1 if row isn't valid
**See Also:** convertYToRow(int)

,

convertRowToY(int)

,

updateLayoutState()

---

#### getRowHeight

protected int getRowHeight​(int row)

Returns the height of the specified row based on the current layout.

convertYToRow

```java
protected int convertYToRow​(int y0)
```

Convert the

JList

relative coordinate to the row that contains it,
based on the current layout. If

y0

doesn't fall within any row,
return -1.

**Parameters:** y0

- a relative Y coordinate
**Returns:** the row that contains y0, or -1
**See Also:** getRowHeight(int)

,

updateLayoutState()

---

#### convertYToRow

protected int convertYToRow​(int y0)

Convert the

JList

relative coordinate to the row that contains it,
based on the current layout. If

y0

doesn't fall within any row,
return -1.

convertRowToY

```java
protected int convertRowToY​(int row)
```

Return the

JList

relative Y coordinate of the origin of the specified
row or -1 if row isn't valid.

**Parameters:** row

- a row
**Returns:** the Y coordinate of the origin of row, or -1
**See Also:** getRowHeight(int)

,

updateLayoutState()

---

#### convertRowToY

protected int convertRowToY​(int row)

Return the

JList

relative Y coordinate of the origin of the specified
row or -1 if row isn't valid.

maybeUpdateLayoutState

```java
protected void maybeUpdateLayoutState()
```

If updateLayoutStateNeeded is non zero, call updateLayoutState() and reset
updateLayoutStateNeeded. This method should be called by methods
before doing any computation based on the geometry of the list.
For example it's the first call in paint() and getPreferredSize().

**See Also:** updateLayoutState()

---

#### maybeUpdateLayoutState

protected void maybeUpdateLayoutState()

If updateLayoutStateNeeded is non zero, call updateLayoutState() and reset
updateLayoutStateNeeded. This method should be called by methods
before doing any computation based on the geometry of the list.
For example it's the first call in paint() and getPreferredSize().

updateLayoutState

```java
protected void updateLayoutState()
```

Recompute the value of cellHeight or cellHeights based
and cellWidth, based on the current font and the current
values of fixedCellWidth, fixedCellHeight, and prototypeCellValue.

**See Also:** maybeUpdateLayoutState()

---

#### updateLayoutState

protected void updateLayoutState()

Recompute the value of cellHeight or cellHeights based
and cellWidth, based on the current font and the current
values of fixedCellWidth, fixedCellHeight, and prototypeCellValue.

createMouseInputListener

```java
protected
MouseInputListener
createMouseInputListener()
```

Creates a delegate that implements

MouseInputListener

.
The delegate is added to the corresponding

java.awt.Component

listener
lists at

installUI()

time. Subclasses can override this method to return
a custom

MouseInputListener

, e.g.

```java
class MyListUI extends BasicListUI {
protected MouseInputListener
createMouseInputListener
() {
return new MyMouseInputHandler();
}
public class MyMouseInputHandler extends MouseInputHandler {
public void mouseMoved(MouseEvent e) {
// do some extra work when the mouse moves
super.mouseMoved(e);
}
}
}
```

**Returns:** an instance of

MouseInputListener
**See Also:** BasicListUI.MouseInputHandler

,

installUI(javax.swing.JComponent)

---

#### createMouseInputListener

protected

MouseInputListener

createMouseInputListener()

Creates a delegate that implements

MouseInputListener

.
The delegate is added to the corresponding

java.awt.Component

listener
lists at

installUI()

time. Subclasses can override this method to return
a custom

MouseInputListener

, e.g.

```java
class MyListUI extends BasicListUI {
protected MouseInputListener
createMouseInputListener
() {
return new MyMouseInputHandler();
}
public class MyMouseInputHandler extends MouseInputHandler {
public void mouseMoved(MouseEvent e) {
// do some extra work when the mouse moves
super.mouseMoved(e);
}
}
}
```

class MyListUI extends BasicListUI {
protected MouseInputListener

createMouseInputListener

() {
return new MyMouseInputHandler();
}
public class MyMouseInputHandler extends MouseInputHandler {
public void mouseMoved(MouseEvent e) {
// do some extra work when the mouse moves
super.mouseMoved(e);
}
}
}

createFocusListener

```java
protected
FocusListener
createFocusListener()
```

Returns an instance of

FocusListener

.

**Returns:** an instance of

FocusListener

---

#### createFocusListener

protected

FocusListener

createFocusListener()

Returns an instance of

FocusListener

.

createListSelectionListener

```java
protected
ListSelectionListener
createListSelectionListener()
```

Creates an instance of

ListSelectionHandler

that's added to
the

JLists

by selectionModel as needed. Subclasses can override
this method to return a custom

ListSelectionListener

, e.g.

```java
class MyListUI extends BasicListUI {
protected ListSelectionListener
createListSelectionListener
() {
return new MySelectionListener();
}
public class MySelectionListener extends ListSelectionHandler {
public void valueChanged(ListSelectionEvent e) {
// do some extra work when the selection changes
super.valueChange(e);
}
}
}
```

**Returns:** an instance of

ListSelectionHandler
**See Also:** BasicListUI.ListSelectionHandler

,

installUI(javax.swing.JComponent)

---

#### createListSelectionListener

protected

ListSelectionListener

createListSelectionListener()

Creates an instance of

ListSelectionHandler

that's added to
the

JLists

by selectionModel as needed. Subclasses can override
this method to return a custom

ListSelectionListener

, e.g.

```java
class MyListUI extends BasicListUI {
protected ListSelectionListener
createListSelectionListener
() {
return new MySelectionListener();
}
public class MySelectionListener extends ListSelectionHandler {
public void valueChanged(ListSelectionEvent e) {
// do some extra work when the selection changes
super.valueChange(e);
}
}
}
```

class MyListUI extends BasicListUI {
protected ListSelectionListener

createListSelectionListener

() {
return new MySelectionListener();
}
public class MySelectionListener extends ListSelectionHandler {
public void valueChanged(ListSelectionEvent e) {
// do some extra work when the selection changes
super.valueChange(e);
}
}
}

createListDataListener

```java
protected
ListDataListener
createListDataListener()
```

Creates an instance of

ListDataListener

that's added to
the

JLists

by model as needed. Subclasses can override
this method to return a custom

ListDataListener

, e.g.

```java
class MyListUI extends BasicListUI {
protected ListDataListener
createListDataListener
() {
return new MyListDataListener();
}
public class MyListDataListener extends ListDataHandler {
public void contentsChanged(ListDataEvent e) {
// do some extra work when the models contents change
super.contentsChange(e);
}
}
}
```

**Returns:** an instance of

ListDataListener
**See Also:** ListDataListener

,

JList.getModel()

,

installUI(javax.swing.JComponent)

---

#### createListDataListener

protected

ListDataListener

createListDataListener()

Creates an instance of

ListDataListener

that's added to
the

JLists

by model as needed. Subclasses can override
this method to return a custom

ListDataListener

, e.g.

```java
class MyListUI extends BasicListUI {
protected ListDataListener
createListDataListener
() {
return new MyListDataListener();
}
public class MyListDataListener extends ListDataHandler {
public void contentsChanged(ListDataEvent e) {
// do some extra work when the models contents change
super.contentsChange(e);
}
}
}
```

class MyListUI extends BasicListUI {
protected ListDataListener

createListDataListener

() {
return new MyListDataListener();
}
public class MyListDataListener extends ListDataHandler {
public void contentsChanged(ListDataEvent e) {
// do some extra work when the models contents change
super.contentsChange(e);
}
}
}

createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates an instance of

PropertyChangeHandler

that's added to
the

JList

by

installUI()

. Subclasses can override this method
to return a custom

PropertyChangeListener

, e.g.

```java
class MyListUI extends BasicListUI {
protected PropertyChangeListener
createPropertyChangeListener
() {
return new MyPropertyChangeListener();
}
public class MyPropertyChangeListener extends PropertyChangeHandler {
public void propertyChange(PropertyChangeEvent e) {
if (e.getPropertyName().equals("model")) {
// do some extra work when the model changes
}
super.propertyChange(e);
}
}
}
```

**Returns:** an instance of

PropertyChangeHandler
**See Also:** PropertyChangeListener

,

installUI(javax.swing.JComponent)

---

#### createPropertyChangeListener

protected

PropertyChangeListener

createPropertyChangeListener()

Creates an instance of

PropertyChangeHandler

that's added to
the

JList

by

installUI()

. Subclasses can override this method
to return a custom

PropertyChangeListener

, e.g.

```java
class MyListUI extends BasicListUI {
protected PropertyChangeListener
createPropertyChangeListener
() {
return new MyPropertyChangeListener();
}
public class MyPropertyChangeListener extends PropertyChangeHandler {
public void propertyChange(PropertyChangeEvent e) {
if (e.getPropertyName().equals("model")) {
// do some extra work when the model changes
}
super.propertyChange(e);
}
}
}
```

class MyListUI extends BasicListUI {
protected PropertyChangeListener

createPropertyChangeListener

() {
return new MyPropertyChangeListener();
}
public class MyPropertyChangeListener extends PropertyChangeHandler {
public void propertyChange(PropertyChangeEvent e) {
if (e.getPropertyName().equals("model")) {
// do some extra work when the model changes
}
super.propertyChange(e);
}
}
}

---

