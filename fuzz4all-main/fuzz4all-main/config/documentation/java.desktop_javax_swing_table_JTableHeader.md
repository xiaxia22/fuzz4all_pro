# Class JTableHeader

**Source:** `java.desktop\javax\swing\table\JTableHeader.html`

### Class Description

```java
public class
JTableHeader

extends
JComponent

implements
TableColumnModelListener
,
Accessible
```

This is the object which manages the header of the

JTable

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

EventListener

,

Accessible

,

TableColumnModelListener

---

### Field Details

#### protected
JTable
table

The table for which this object is the header;
the default is

null

.

---

#### protected
TableColumnModel
columnModel

The

TableColumnModel

of the table header.

---

#### protected boolean reorderingAllowed

If true, reordering of columns are allowed by the user;
the default is true.

---

#### protected boolean resizingAllowed

If true, resizing of columns are allowed by the user;
the default is true.

---

#### protected boolean updateTableInRealTime

Obsolete as of Java 2 platform v1.3. Real time repaints, in response
to column dragging or resizing, are now unconditional.

---

#### protected transient
TableColumn
resizingColumn

The index of the column being resized.

null

if not resizing.

---

#### protected transient
TableColumn
draggedColumn

The index of the column being dragged.

null

if not dragging.

---

#### protected transient int draggedDistance

The distance from its original position the column has been dragged.

---

### Constructor Details

#### public JTableHeader()

Constructs a

JTableHeader

with a default

TableColumnModel

.

**See Also:**
- createDefaultColumnModel()

---

#### public JTableHeader​(
TableColumnModel
cm)

Constructs a

JTableHeader

which is initialized with

cm

as the column model. If

cm

is

null

this method will initialize the table header
with a default

TableColumnModel

.

**Parameters:**
- cm

- the column model for the table

**See Also:**
- createDefaultColumnModel()

---

### Method Details

#### @BeanProperty
(
description
="The table associated with this header.")
public void setTable​(
JTable
table)

Sets the table associated with this header.

**Parameters:**
- table

- the new table

---

#### public
JTable
getTable()

Returns the table associated with this header.

**Returns:**
- the

table

property

---

#### @BeanProperty
(
description
="Whether the user can drag column headers to reorder columns.")
public void setReorderingAllowed​(boolean reorderingAllowed)

Sets whether the user can drag column headers to reorder columns.

**Parameters:**
- reorderingAllowed

- true if the table view should allow
reordering; otherwise false

**See Also:**
- getReorderingAllowed()

---

#### public boolean getReorderingAllowed()

Returns true if the user is allowed to rearrange columns by
dragging their headers, false otherwise. The default is true. You can
rearrange columns programmatically regardless of this setting.

**Returns:**
- the

reorderingAllowed

property

**See Also:**
- setReorderingAllowed(boolean)

---

#### @BeanProperty
(
description
="Whether the user can resize columns by dragging between headers.")
public void setResizingAllowed​(boolean resizingAllowed)

Sets whether the user can resize columns by dragging between headers.

**Parameters:**
- resizingAllowed

- true if table view should allow
resizing

**See Also:**
- getResizingAllowed()

---

#### public boolean getResizingAllowed()

Returns true if the user is allowed to resize columns by dragging
between their headers, false otherwise. The default is true. You can
resize columns programmatically regardless of this setting.

**Returns:**
- the

resizingAllowed

property

**See Also:**
- setResizingAllowed(boolean)

---

#### public
TableColumn
getDraggedColumn()

Returns the dragged column, if and only if, a drag is in
process, otherwise returns

null

.

**Returns:**
- the dragged column, if a drag is in
process, otherwise returns

null

**See Also:**
- getDraggedDistance()

---

#### public int getDraggedDistance()

Returns the column's horizontal distance from its original
position, if and only if, a drag is in process. Otherwise, the
the return value is meaningless.

**Returns:**
- the column's horizontal distance from its original
position, if a drag is in process, otherwise the return
value is meaningless

**See Also:**
- getDraggedColumn()

---

#### public
TableColumn
getResizingColumn()

Returns the resizing column. If no column is being
resized this method returns

null

.

**Returns:**
- the resizing column, if a resize is in process, otherwise
returns

null

---

#### public void setUpdateTableInRealTime​(boolean flag)

Obsolete as of Java 2 platform v1.3. Real time repaints, in response to
column dragging or resizing, are now unconditional.

**Parameters:**
- flag

- true if tableView should update the body of the
table in real time

---

#### public boolean getUpdateTableInRealTime()

Obsolete as of Java 2 platform v1.3. Real time repaints, in response to
column dragging or resizing, are now unconditional.

**Returns:**
- true if the table updates in real time

---

#### public void setDefaultRenderer​(
TableCellRenderer
defaultRenderer)

Sets the default renderer to be used when no

headerRenderer

is defined by a

TableColumn

.

**Parameters:**
- defaultRenderer

- the default renderer

**Since:**
- 1.3

---

#### public
TableCellRenderer
getDefaultRenderer()

Returns the default renderer used when no

headerRenderer

is defined by a

TableColumn

.

**Returns:**
- the default renderer

**Since:**
- 1.3

---

#### public int columnAtPoint​(
Point
point)

Returns the index of the column that

point

lies in, or -1 if it
lies out of bounds.

**Parameters:**
- point

- if this

point

lies within a column, the index of
that column will be returned; otherwise it is out of bounds
and -1 is returned

**Returns:**
- the index of the column that

point

lies in, or -1 if it
lies out of bounds

---

#### public
Rectangle
getHeaderRect​(int column)

Returns the rectangle containing the header tile at

column

.
When the

column

parameter is out of bounds this method uses the
same conventions as the

JTable

method

getCellRect

.

**Parameters:**
- column

- index of the column

**Returns:**
- the rectangle containing the header tile at

column

**See Also:**
- JTable.getCellRect(int, int, boolean)

---

#### public
String
getToolTipText​(
MouseEvent
event)

Allows the renderer's tips to be used if there is text set.

**Overrides:**
- getToolTipText

in class

JComponent

**Parameters:**
- event

- the location of the event identifies the proper
renderer and, therefore, the proper tip

**Returns:**
- the tool tip for this component

---

#### public
Dimension
getPreferredSize()

Returns the preferred size of the table header.
This is the size required to display the header and requested for
the viewport.
The returned

Dimension

width

will always be calculated by
the underlying TableHeaderUI, regardless of any width specified by

JComponent.setPreferredSize(java.awt.Dimension)

**Overrides:**
- getPreferredSize

in class

JComponent

**Returns:**
- the size

**See Also:**
- JComponent.setPreferredSize(java.awt.Dimension)

,

ComponentUI

---

#### public
TableHeaderUI
getUI()

Returns the look and feel (L&F) object that renders this component.

**Overrides:**
- getUI

in class

JComponent

**Returns:**
- the

TableHeaderUI

object that renders this component

---

#### public void setUI​(
TableHeaderUI
ui)

Sets the look and feel (L&F) object that renders this component.

**Parameters:**
- ui

- the

TableHeaderUI

L&F object

**See Also:**
- UIDefaults.getUI(javax.swing.JComponent)

---

#### public void updateUI()

Notification from the

UIManager

that the look and feel
(L&F) has changed.
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

#### public
String
getUIClassID()

Returns the suffix used to construct the name of the look and feel
(L&F) class used to render this component.

**Overrides:**
- getUIClassID

in class

JComponent

**Returns:**
- the string "TableHeaderUI"

**See Also:**
- JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### @BeanProperty
(
description
="The object governing the way columns appear in the view.")
public void setColumnModel​(
TableColumnModel
columnModel)

Sets the column model for this table to

newModel

and registers
for listener notifications from the new column model.

**Parameters:**
- columnModel

- the new data source for this table

**Throws:**
- IllegalArgumentException

- if

newModel

is

null

**See Also:**
- getColumnModel()

---

#### public
TableColumnModel
getColumnModel()

Returns the

TableColumnModel

that contains all column information
of this table header.

**Returns:**
- the

columnModel

property

**See Also:**
- setColumnModel(javax.swing.table.TableColumnModel)

---

#### public void columnAdded​(
TableColumnModelEvent
e)

Invoked when a column is added to the table column model.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

**Specified by:**
- columnAdded

in interface

TableColumnModelListener

**Parameters:**
- e

- the event received

**See Also:**
- TableColumnModelListener

---

#### public void columnRemoved​(
TableColumnModelEvent
e)

Invoked when a column is removed from the table column model.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

**Specified by:**
- columnRemoved

in interface

TableColumnModelListener

**Parameters:**
- e

- the event received

**See Also:**
- TableColumnModelListener

---

#### public void columnMoved​(
TableColumnModelEvent
e)

Invoked when a column is repositioned.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

**Specified by:**
- columnMoved

in interface

TableColumnModelListener

**Parameters:**
- e

- the event received

**See Also:**
- TableColumnModelListener

---

#### public void columnMarginChanged​(
ChangeEvent
e)

Invoked when a column is moved due to a margin change.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

**Specified by:**
- columnMarginChanged

in interface

TableColumnModelListener

**Parameters:**
- e

- the event received

**See Also:**
- TableColumnModelListener

---

#### public void columnSelectionChanged​(
ListSelectionEvent
e)

Invoked when the selection model of the

TableColumnModel

is changed. This method currently has no effect (the header is not
redrawn).

Application code will not use these methods explicitly, they
are used internally by

JTable

.

**Specified by:**
- columnSelectionChanged

in interface

TableColumnModelListener

**Parameters:**
- e

- the event received

**See Also:**
- TableColumnModelListener

---

#### protected
TableColumnModel
createDefaultColumnModel()

Returns the default column model object which is
a

DefaultTableColumnModel

. A subclass can override this
method to return a different column model object

**Returns:**
- the default column model object

---

#### protected
TableCellRenderer
createDefaultRenderer()

Returns a default renderer to be used when no header renderer
is defined by a

TableColumn

.

**Returns:**
- the default table column renderer

**Since:**
- 1.3

---

#### protected void initializeLocalVars()

Initializes the local variables and properties with default values.
Used by the constructor methods.

---

#### public void resizeAndRepaint()

Sizes the header and marks it as needing display. Equivalent
to

revalidate

followed by

repaint

.

---

#### public void setDraggedColumn​(
TableColumn
aColumn)

Sets the header's

draggedColumn

to

aColumn

.

Application code will not use this method explicitly, it is used
internally by the column dragging mechanism.

**Parameters:**
- aColumn

- the column being dragged, or

null

if
no column is being dragged

---

#### public void setDraggedDistance​(int distance)

Sets the header's

draggedDistance

to

distance

.

**Parameters:**
- distance

- the distance dragged

---

#### public void setResizingColumn​(
TableColumn
aColumn)

Sets the header's

resizingColumn

to

aColumn

.

Application code will not use this method explicitly, it
is used internally by the column sizing mechanism.

**Parameters:**
- aColumn

- the column being resized, or

null

if
no column is being resized

---

#### protected
String
paramString()

Returns a string representation of this

JTableHeader

. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

Overriding

paramString

to provide information about the
specific new aspects of the JFC components.

**Overrides:**
- paramString

in class

JComponent

**Returns:**
- a string representation of this

JTableHeader

---

#### public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this JTableHeader.
For JTableHeaders, the AccessibleContext takes the form of an
AccessibleJTableHeader.
A new AccessibleJTableHeader instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- an AccessibleJTableHeader that serves as the
AccessibleContext of this JTableHeader

---

### Additional Sections

#### Class JTableHeader

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.table.JTableHeader

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.table.JTableHeader

java.awt.Container

- javax.swing.JComponent
- - javax.swing.table.JTableHeader

javax.swing.JComponent

- javax.swing.table.JTableHeader

javax.swing.table.JTableHeader

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

EventListener

,

Accessible

,

TableColumnModelListener

```java
public class
JTableHeader

extends
JComponent

implements
TableColumnModelListener
,
Accessible
```

This is the object which manages the header of the

JTable

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

**See Also:** JTable

,

Serialized Form

public class

JTableHeader

extends

JComponent

implements

TableColumnModelListener

,

Accessible

This is the object which manages the header of the

JTable

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

JTableHeader.AccessibleJTableHeader

This class implements accessibility support for the

JTableHeader

class.

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

protected

TableColumnModel

columnModel

The

TableColumnModel

of the table header.

protected

TableColumn

draggedColumn

The index of the column being dragged.

protected int

draggedDistance

The distance from its original position the column has been dragged.

protected boolean

reorderingAllowed

If true, reordering of columns are allowed by the user;
the default is true.

protected boolean

resizingAllowed

If true, resizing of columns are allowed by the user;
the default is true.

protected

TableColumn

resizingColumn

The index of the column being resized.

protected

JTable

table

The table for which this object is the header;
the default is

null

.

protected boolean

updateTableInRealTime

Obsolete as of Java 2 platform v1.3.

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

JTableHeader

()

Constructs a

JTableHeader

with a default

TableColumnModel

.

JTableHeader

​(

TableColumnModel

cm)

Constructs a

JTableHeader

which is initialized with

cm

as the column model.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

columnAdded

​(

TableColumnModelEvent

e)

Invoked when a column is added to the table column model.

int

columnAtPoint

​(

Point

point)

Returns the index of the column that

point

lies in, or -1 if it
lies out of bounds.

void

columnMarginChanged

​(

ChangeEvent

e)

Invoked when a column is moved due to a margin change.

void

columnMoved

​(

TableColumnModelEvent

e)

Invoked when a column is repositioned.

void

columnRemoved

​(

TableColumnModelEvent

e)

Invoked when a column is removed from the table column model.

void

columnSelectionChanged

​(

ListSelectionEvent

e)

Invoked when the selection model of the

TableColumnModel

is changed.

protected

TableColumnModel

createDefaultColumnModel

()

Returns the default column model object which is
a

DefaultTableColumnModel

.

protected

TableCellRenderer

createDefaultRenderer

()

Returns a default renderer to be used when no header renderer
is defined by a

TableColumn

.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JTableHeader.

TableColumnModel

getColumnModel

()

Returns the

TableColumnModel

that contains all column information
of this table header.

TableCellRenderer

getDefaultRenderer

()

Returns the default renderer used when no

headerRenderer

is defined by a

TableColumn

.

TableColumn

getDraggedColumn

()

Returns the dragged column, if and only if, a drag is in
process, otherwise returns

null

.

int

getDraggedDistance

()

Returns the column's horizontal distance from its original
position, if and only if, a drag is in process.

Rectangle

getHeaderRect

​(int column)

Returns the rectangle containing the header tile at

column

.

Dimension

getPreferredSize

()

Returns the preferred size of the table header.

boolean

getReorderingAllowed

()

Returns true if the user is allowed to rearrange columns by
dragging their headers, false otherwise.

boolean

getResizingAllowed

()

Returns true if the user is allowed to resize columns by dragging
between their headers, false otherwise.

TableColumn

getResizingColumn

()

Returns the resizing column.

JTable

getTable

()

Returns the table associated with this header.

String

getToolTipText

​(

MouseEvent

event)

Allows the renderer's tips to be used if there is text set.

TableHeaderUI

getUI

()

Returns the look and feel (L&F) object that renders this component.

String

getUIClassID

()

Returns the suffix used to construct the name of the look and feel
(L&F) class used to render this component.

boolean

getUpdateTableInRealTime

()

Obsolete as of Java 2 platform v1.3.

protected void

initializeLocalVars

()

Initializes the local variables and properties with default values.

protected

String

paramString

()

Returns a string representation of this

JTableHeader

.

void

resizeAndRepaint

()

Sizes the header and marks it as needing display.

void

setColumnModel

​(

TableColumnModel

columnModel)

Sets the column model for this table to

newModel

and registers
for listener notifications from the new column model.

void

setDefaultRenderer

​(

TableCellRenderer

defaultRenderer)

Sets the default renderer to be used when no

headerRenderer

is defined by a

TableColumn

.

void

setDraggedColumn

​(

TableColumn

aColumn)

Sets the header's

draggedColumn

to

aColumn

.

void

setDraggedDistance

​(int distance)

Sets the header's

draggedDistance

to

distance

.

void

setReorderingAllowed

​(boolean reorderingAllowed)

Sets whether the user can drag column headers to reorder columns.

void

setResizingAllowed

​(boolean resizingAllowed)

Sets whether the user can resize columns by dragging between headers.

void

setResizingColumn

​(

TableColumn

aColumn)

Sets the header's

resizingColumn

to

aColumn

.

void

setTable

​(

JTable

table)

Sets the table associated with this header.

void

setUI

​(

TableHeaderUI

ui)

Sets the look and feel (L&F) object that renders this component.

void

setUpdateTableInRealTime

​(boolean flag)

Obsolete as of Java 2 platform v1.3.

void

updateUI

()

Notification from the

UIManager

that the look and feel
(L&F) has changed.

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

JTableHeader.AccessibleJTableHeader

This class implements accessibility support for the

JTableHeader

class.

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

JTableHeader

class.

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

protected

TableColumnModel

columnModel

The

TableColumnModel

of the table header.

protected

TableColumn

draggedColumn

The index of the column being dragged.

protected int

draggedDistance

The distance from its original position the column has been dragged.

protected boolean

reorderingAllowed

If true, reordering of columns are allowed by the user;
the default is true.

protected boolean

resizingAllowed

If true, resizing of columns are allowed by the user;
the default is true.

protected

TableColumn

resizingColumn

The index of the column being resized.

protected

JTable

table

The table for which this object is the header;
the default is

null

.

protected boolean

updateTableInRealTime

Obsolete as of Java 2 platform v1.3.

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

The

TableColumnModel

of the table header.

The index of the column being dragged.

The distance from its original position the column has been dragged.

If true, reordering of columns are allowed by the user;
the default is true.

If true, resizing of columns are allowed by the user;
the default is true.

The index of the column being resized.

The table for which this object is the header;
the default is

null

.

Obsolete as of Java 2 platform v1.3.

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

JTableHeader

()

Constructs a

JTableHeader

with a default

TableColumnModel

.

JTableHeader

​(

TableColumnModel

cm)

Constructs a

JTableHeader

which is initialized with

cm

as the column model.

---

#### Constructor Summary

Constructs a

JTableHeader

with a default

TableColumnModel

.

Constructs a

JTableHeader

which is initialized with

cm

as the column model.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

columnAdded

​(

TableColumnModelEvent

e)

Invoked when a column is added to the table column model.

int

columnAtPoint

​(

Point

point)

Returns the index of the column that

point

lies in, or -1 if it
lies out of bounds.

void

columnMarginChanged

​(

ChangeEvent

e)

Invoked when a column is moved due to a margin change.

void

columnMoved

​(

TableColumnModelEvent

e)

Invoked when a column is repositioned.

void

columnRemoved

​(

TableColumnModelEvent

e)

Invoked when a column is removed from the table column model.

void

columnSelectionChanged

​(

ListSelectionEvent

e)

Invoked when the selection model of the

TableColumnModel

is changed.

protected

TableColumnModel

createDefaultColumnModel

()

Returns the default column model object which is
a

DefaultTableColumnModel

.

protected

TableCellRenderer

createDefaultRenderer

()

Returns a default renderer to be used when no header renderer
is defined by a

TableColumn

.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JTableHeader.

TableColumnModel

getColumnModel

()

Returns the

TableColumnModel

that contains all column information
of this table header.

TableCellRenderer

getDefaultRenderer

()

Returns the default renderer used when no

headerRenderer

is defined by a

TableColumn

.

TableColumn

getDraggedColumn

()

Returns the dragged column, if and only if, a drag is in
process, otherwise returns

null

.

int

getDraggedDistance

()

Returns the column's horizontal distance from its original
position, if and only if, a drag is in process.

Rectangle

getHeaderRect

​(int column)

Returns the rectangle containing the header tile at

column

.

Dimension

getPreferredSize

()

Returns the preferred size of the table header.

boolean

getReorderingAllowed

()

Returns true if the user is allowed to rearrange columns by
dragging their headers, false otherwise.

boolean

getResizingAllowed

()

Returns true if the user is allowed to resize columns by dragging
between their headers, false otherwise.

TableColumn

getResizingColumn

()

Returns the resizing column.

JTable

getTable

()

Returns the table associated with this header.

String

getToolTipText

​(

MouseEvent

event)

Allows the renderer's tips to be used if there is text set.

TableHeaderUI

getUI

()

Returns the look and feel (L&F) object that renders this component.

String

getUIClassID

()

Returns the suffix used to construct the name of the look and feel
(L&F) class used to render this component.

boolean

getUpdateTableInRealTime

()

Obsolete as of Java 2 platform v1.3.

protected void

initializeLocalVars

()

Initializes the local variables and properties with default values.

protected

String

paramString

()

Returns a string representation of this

JTableHeader

.

void

resizeAndRepaint

()

Sizes the header and marks it as needing display.

void

setColumnModel

​(

TableColumnModel

columnModel)

Sets the column model for this table to

newModel

and registers
for listener notifications from the new column model.

void

setDefaultRenderer

​(

TableCellRenderer

defaultRenderer)

Sets the default renderer to be used when no

headerRenderer

is defined by a

TableColumn

.

void

setDraggedColumn

​(

TableColumn

aColumn)

Sets the header's

draggedColumn

to

aColumn

.

void

setDraggedDistance

​(int distance)

Sets the header's

draggedDistance

to

distance

.

void

setReorderingAllowed

​(boolean reorderingAllowed)

Sets whether the user can drag column headers to reorder columns.

void

setResizingAllowed

​(boolean resizingAllowed)

Sets whether the user can resize columns by dragging between headers.

void

setResizingColumn

​(

TableColumn

aColumn)

Sets the header's

resizingColumn

to

aColumn

.

void

setTable

​(

JTable

table)

Sets the table associated with this header.

void

setUI

​(

TableHeaderUI

ui)

Sets the look and feel (L&F) object that renders this component.

void

setUpdateTableInRealTime

​(boolean flag)

Obsolete as of Java 2 platform v1.3.

void

updateUI

()

Notification from the

UIManager

that the look and feel
(L&F) has changed.

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

Invoked when a column is added to the table column model.

Returns the index of the column that

point

lies in, or -1 if it
lies out of bounds.

Invoked when a column is moved due to a margin change.

Invoked when a column is repositioned.

Invoked when a column is removed from the table column model.

Invoked when the selection model of the

TableColumnModel

is changed.

Returns the default column model object which is
a

DefaultTableColumnModel

.

Returns a default renderer to be used when no header renderer
is defined by a

TableColumn

.

Gets the AccessibleContext associated with this JTableHeader.

Returns the

TableColumnModel

that contains all column information
of this table header.

Returns the default renderer used when no

headerRenderer

is defined by a

TableColumn

.

Returns the dragged column, if and only if, a drag is in
process, otherwise returns

null

.

Returns the column's horizontal distance from its original
position, if and only if, a drag is in process.

Returns the rectangle containing the header tile at

column

.

Returns the preferred size of the table header.

Returns true if the user is allowed to rearrange columns by
dragging their headers, false otherwise.

Returns true if the user is allowed to resize columns by dragging
between their headers, false otherwise.

Returns the resizing column.

Returns the table associated with this header.

Allows the renderer's tips to be used if there is text set.

Returns the look and feel (L&F) object that renders this component.

Returns the suffix used to construct the name of the look and feel
(L&F) class used to render this component.

Obsolete as of Java 2 platform v1.3.

Initializes the local variables and properties with default values.

Returns a string representation of this

JTableHeader

.

Sizes the header and marks it as needing display.

Sets the column model for this table to

newModel

and registers
for listener notifications from the new column model.

Sets the default renderer to be used when no

headerRenderer

is defined by a

TableColumn

.

Sets the header's

draggedColumn

to

aColumn

.

Sets the header's

draggedDistance

to

distance

.

Sets whether the user can drag column headers to reorder columns.

Sets whether the user can resize columns by dragging between headers.

Sets the header's

resizingColumn

to

aColumn

.

Sets the table associated with this header.

Sets the look and feel (L&F) object that renders this component.

Notification from the

UIManager

that the look and feel
(L&F) has changed.

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

- table

```java
protected
JTable
table
```

The table for which this object is the header;
the default is

null

.

- columnModel

```java
protected
TableColumnModel
columnModel
```

The

TableColumnModel

of the table header.

- reorderingAllowed

```java
protected boolean reorderingAllowed
```

If true, reordering of columns are allowed by the user;
the default is true.

- resizingAllowed

```java
protected boolean resizingAllowed
```

If true, resizing of columns are allowed by the user;
the default is true.

- updateTableInRealTime

```java
protected boolean updateTableInRealTime
```

Obsolete as of Java 2 platform v1.3. Real time repaints, in response
to column dragging or resizing, are now unconditional.

- resizingColumn

```java
protected transient
TableColumn
resizingColumn
```

The index of the column being resized.

null

if not resizing.

- draggedColumn

```java
protected transient
TableColumn
draggedColumn
```

The index of the column being dragged.

null

if not dragging.

- draggedDistance

```java
protected transient int draggedDistance
```

The distance from its original position the column has been dragged.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JTableHeader

```java
public JTableHeader()
```

Constructs a

JTableHeader

with a default

TableColumnModel

.

**See Also:** createDefaultColumnModel()

- JTableHeader

```java
public JTableHeader​(
TableColumnModel
cm)
```

Constructs a

JTableHeader

which is initialized with

cm

as the column model. If

cm

is

null

this method will initialize the table header
with a default

TableColumnModel

.

**Parameters:** cm

- the column model for the table
**See Also:** createDefaultColumnModel()

============ METHOD DETAIL ==========

- Method Detail

- setTable

```java
@BeanProperty
(
description
="The table associated with this header.")
public void setTable​(
JTable
table)
```

Sets the table associated with this header.

**Parameters:** table

- the new table

- getTable

```java
public
JTable
getTable()
```

Returns the table associated with this header.

**Returns:** the

table

property

- setReorderingAllowed

```java
@BeanProperty
(
description
="Whether the user can drag column headers to reorder columns.")
public void setReorderingAllowed​(boolean reorderingAllowed)
```

Sets whether the user can drag column headers to reorder columns.

**Parameters:** reorderingAllowed

- true if the table view should allow
reordering; otherwise false
**See Also:** getReorderingAllowed()

- getReorderingAllowed

```java
public boolean getReorderingAllowed()
```

Returns true if the user is allowed to rearrange columns by
dragging their headers, false otherwise. The default is true. You can
rearrange columns programmatically regardless of this setting.

**Returns:** the

reorderingAllowed

property
**See Also:** setReorderingAllowed(boolean)

- setResizingAllowed

```java
@BeanProperty
(
description
="Whether the user can resize columns by dragging between headers.")
public void setResizingAllowed​(boolean resizingAllowed)
```

Sets whether the user can resize columns by dragging between headers.

**Parameters:** resizingAllowed

- true if table view should allow
resizing
**See Also:** getResizingAllowed()

- getResizingAllowed

```java
public boolean getResizingAllowed()
```

Returns true if the user is allowed to resize columns by dragging
between their headers, false otherwise. The default is true. You can
resize columns programmatically regardless of this setting.

**Returns:** the

resizingAllowed

property
**See Also:** setResizingAllowed(boolean)

- getDraggedColumn

```java
public
TableColumn
getDraggedColumn()
```

Returns the dragged column, if and only if, a drag is in
process, otherwise returns

null

.

**Returns:** the dragged column, if a drag is in
process, otherwise returns

null
**See Also:** getDraggedDistance()

- getDraggedDistance

```java
public int getDraggedDistance()
```

Returns the column's horizontal distance from its original
position, if and only if, a drag is in process. Otherwise, the
the return value is meaningless.

**Returns:** the column's horizontal distance from its original
position, if a drag is in process, otherwise the return
value is meaningless
**See Also:** getDraggedColumn()

- getResizingColumn

```java
public
TableColumn
getResizingColumn()
```

Returns the resizing column. If no column is being
resized this method returns

null

.

**Returns:** the resizing column, if a resize is in process, otherwise
returns

null

- setUpdateTableInRealTime

```java
public void setUpdateTableInRealTime​(boolean flag)
```

Obsolete as of Java 2 platform v1.3. Real time repaints, in response to
column dragging or resizing, are now unconditional.

**Parameters:** flag

- true if tableView should update the body of the
table in real time

- getUpdateTableInRealTime

```java
public boolean getUpdateTableInRealTime()
```

Obsolete as of Java 2 platform v1.3. Real time repaints, in response to
column dragging or resizing, are now unconditional.

**Returns:** true if the table updates in real time

- setDefaultRenderer

```java
public void setDefaultRenderer​(
TableCellRenderer
defaultRenderer)
```

Sets the default renderer to be used when no

headerRenderer

is defined by a

TableColumn

.

**Parameters:** defaultRenderer

- the default renderer
**Since:** 1.3

- getDefaultRenderer

```java
public
TableCellRenderer
getDefaultRenderer()
```

Returns the default renderer used when no

headerRenderer

is defined by a

TableColumn

.

**Returns:** the default renderer
**Since:** 1.3

- columnAtPoint

```java
public int columnAtPoint​(
Point
point)
```

Returns the index of the column that

point

lies in, or -1 if it
lies out of bounds.

**Parameters:** point

- if this

point

lies within a column, the index of
that column will be returned; otherwise it is out of bounds
and -1 is returned
**Returns:** the index of the column that

point

lies in, or -1 if it
lies out of bounds

- getHeaderRect

```java
public
Rectangle
getHeaderRect​(int column)
```

Returns the rectangle containing the header tile at

column

.
When the

column

parameter is out of bounds this method uses the
same conventions as the

JTable

method

getCellRect

.

**Parameters:** column

- index of the column
**Returns:** the rectangle containing the header tile at

column
**See Also:** JTable.getCellRect(int, int, boolean)

- getToolTipText

```java
public
String
getToolTipText​(
MouseEvent
event)
```

Allows the renderer's tips to be used if there is text set.

**Overrides:** getToolTipText

in class

JComponent
**Parameters:** event

- the location of the event identifies the proper
renderer and, therefore, the proper tip
**Returns:** the tool tip for this component

- getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Returns the preferred size of the table header.
This is the size required to display the header and requested for
the viewport.
The returned

Dimension

width

will always be calculated by
the underlying TableHeaderUI, regardless of any width specified by

JComponent.setPreferredSize(java.awt.Dimension)

**Overrides:** getPreferredSize

in class

JComponent
**Returns:** the size
**See Also:** JComponent.setPreferredSize(java.awt.Dimension)

,

ComponentUI

- getUI

```java
public
TableHeaderUI
getUI()
```

Returns the look and feel (L&F) object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

TableHeaderUI

object that renders this component

- setUI

```java
public void setUI​(
TableHeaderUI
ui)
```

Sets the look and feel (L&F) object that renders this component.

**Parameters:** ui

- the

TableHeaderUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

- updateUI

```java
public void updateUI()
```

Notification from the

UIManager

that the look and feel
(L&F) has changed.
Replaces the current UI object with the latest version from the

UIManager

.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

- getUIClassID

```java
public
String
getUIClassID()
```

Returns the suffix used to construct the name of the look and feel
(L&F) class used to render this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "TableHeaderUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- setColumnModel

```java
@BeanProperty
(
description
="The object governing the way columns appear in the view.")
public void setColumnModel​(
TableColumnModel
columnModel)
```

Sets the column model for this table to

newModel

and registers
for listener notifications from the new column model.

**Parameters:** columnModel

- the new data source for this table
**Throws:** IllegalArgumentException

- if

newModel

is

null
**See Also:** getColumnModel()

- getColumnModel

```java
public
TableColumnModel
getColumnModel()
```

Returns the

TableColumnModel

that contains all column information
of this table header.

**Returns:** the

columnModel

property
**See Also:** setColumnModel(javax.swing.table.TableColumnModel)

- columnAdded

```java
public void columnAdded​(
TableColumnModelEvent
e)
```

Invoked when a column is added to the table column model.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

**Specified by:** columnAdded

in interface

TableColumnModelListener
**Parameters:** e

- the event received
**See Also:** TableColumnModelListener

- columnRemoved

```java
public void columnRemoved​(
TableColumnModelEvent
e)
```

Invoked when a column is removed from the table column model.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

**Specified by:** columnRemoved

in interface

TableColumnModelListener
**Parameters:** e

- the event received
**See Also:** TableColumnModelListener

- columnMoved

```java
public void columnMoved​(
TableColumnModelEvent
e)
```

Invoked when a column is repositioned.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

**Specified by:** columnMoved

in interface

TableColumnModelListener
**Parameters:** e

- the event received
**See Also:** TableColumnModelListener

- columnMarginChanged

```java
public void columnMarginChanged​(
ChangeEvent
e)
```

Invoked when a column is moved due to a margin change.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

**Specified by:** columnMarginChanged

in interface

TableColumnModelListener
**Parameters:** e

- the event received
**See Also:** TableColumnModelListener

- columnSelectionChanged

```java
public void columnSelectionChanged​(
ListSelectionEvent
e)
```

Invoked when the selection model of the

TableColumnModel

is changed. This method currently has no effect (the header is not
redrawn).

Application code will not use these methods explicitly, they
are used internally by

JTable

.

**Specified by:** columnSelectionChanged

in interface

TableColumnModelListener
**Parameters:** e

- the event received
**See Also:** TableColumnModelListener

- createDefaultColumnModel

```java
protected
TableColumnModel
createDefaultColumnModel()
```

Returns the default column model object which is
a

DefaultTableColumnModel

. A subclass can override this
method to return a different column model object

**Returns:** the default column model object

- createDefaultRenderer

```java
protected
TableCellRenderer
createDefaultRenderer()
```

Returns a default renderer to be used when no header renderer
is defined by a

TableColumn

.

**Returns:** the default table column renderer
**Since:** 1.3

- initializeLocalVars

```java
protected void initializeLocalVars()
```

Initializes the local variables and properties with default values.
Used by the constructor methods.

- resizeAndRepaint

```java
public void resizeAndRepaint()
```

Sizes the header and marks it as needing display. Equivalent
to

revalidate

followed by

repaint

.

- setDraggedColumn

```java
public void setDraggedColumn​(
TableColumn
aColumn)
```

Sets the header's

draggedColumn

to

aColumn

.

Application code will not use this method explicitly, it is used
internally by the column dragging mechanism.

**Parameters:** aColumn

- the column being dragged, or

null

if
no column is being dragged

- setDraggedDistance

```java
public void setDraggedDistance​(int distance)
```

Sets the header's

draggedDistance

to

distance

.

**Parameters:** distance

- the distance dragged

- setResizingColumn

```java
public void setResizingColumn​(
TableColumn
aColumn)
```

Sets the header's

resizingColumn

to

aColumn

.

Application code will not use this method explicitly, it
is used internally by the column sizing mechanism.

**Parameters:** aColumn

- the column being resized, or

null

if
no column is being resized

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JTableHeader

. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

Overriding

paramString

to provide information about the
specific new aspects of the JFC components.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

JTableHeader

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JTableHeader.
For JTableHeaders, the AccessibleContext takes the form of an
AccessibleJTableHeader.
A new AccessibleJTableHeader instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJTableHeader that serves as the
AccessibleContext of this JTableHeader

Field Detail

- table

```java
protected
JTable
table
```

The table for which this object is the header;
the default is

null

.

- columnModel

```java
protected
TableColumnModel
columnModel
```

The

TableColumnModel

of the table header.

- reorderingAllowed

```java
protected boolean reorderingAllowed
```

If true, reordering of columns are allowed by the user;
the default is true.

- resizingAllowed

```java
protected boolean resizingAllowed
```

If true, resizing of columns are allowed by the user;
the default is true.

- updateTableInRealTime

```java
protected boolean updateTableInRealTime
```

Obsolete as of Java 2 platform v1.3. Real time repaints, in response
to column dragging or resizing, are now unconditional.

- resizingColumn

```java
protected transient
TableColumn
resizingColumn
```

The index of the column being resized.

null

if not resizing.

- draggedColumn

```java
protected transient
TableColumn
draggedColumn
```

The index of the column being dragged.

null

if not dragging.

- draggedDistance

```java
protected transient int draggedDistance
```

The distance from its original position the column has been dragged.

---

#### Field Detail

table

```java
protected
JTable
table
```

The table for which this object is the header;
the default is

null

.

---

#### table

protected

JTable

table

The table for which this object is the header;
the default is

null

.

columnModel

```java
protected
TableColumnModel
columnModel
```

The

TableColumnModel

of the table header.

---

#### columnModel

protected

TableColumnModel

columnModel

The

TableColumnModel

of the table header.

reorderingAllowed

```java
protected boolean reorderingAllowed
```

If true, reordering of columns are allowed by the user;
the default is true.

---

#### reorderingAllowed

protected boolean reorderingAllowed

If true, reordering of columns are allowed by the user;
the default is true.

resizingAllowed

```java
protected boolean resizingAllowed
```

If true, resizing of columns are allowed by the user;
the default is true.

---

#### resizingAllowed

protected boolean resizingAllowed

If true, resizing of columns are allowed by the user;
the default is true.

updateTableInRealTime

```java
protected boolean updateTableInRealTime
```

Obsolete as of Java 2 platform v1.3. Real time repaints, in response
to column dragging or resizing, are now unconditional.

---

#### updateTableInRealTime

protected boolean updateTableInRealTime

Obsolete as of Java 2 platform v1.3. Real time repaints, in response
to column dragging or resizing, are now unconditional.

resizingColumn

```java
protected transient
TableColumn
resizingColumn
```

The index of the column being resized.

null

if not resizing.

---

#### resizingColumn

protected transient

TableColumn

resizingColumn

The index of the column being resized.

null

if not resizing.

draggedColumn

```java
protected transient
TableColumn
draggedColumn
```

The index of the column being dragged.

null

if not dragging.

---

#### draggedColumn

protected transient

TableColumn

draggedColumn

The index of the column being dragged.

null

if not dragging.

draggedDistance

```java
protected transient int draggedDistance
```

The distance from its original position the column has been dragged.

---

#### draggedDistance

protected transient int draggedDistance

The distance from its original position the column has been dragged.

Constructor Detail

- JTableHeader

```java
public JTableHeader()
```

Constructs a

JTableHeader

with a default

TableColumnModel

.

**See Also:** createDefaultColumnModel()

- JTableHeader

```java
public JTableHeader​(
TableColumnModel
cm)
```

Constructs a

JTableHeader

which is initialized with

cm

as the column model. If

cm

is

null

this method will initialize the table header
with a default

TableColumnModel

.

**Parameters:** cm

- the column model for the table
**See Also:** createDefaultColumnModel()

---

#### Constructor Detail

JTableHeader

```java
public JTableHeader()
```

Constructs a

JTableHeader

with a default

TableColumnModel

.

**See Also:** createDefaultColumnModel()

---

#### JTableHeader

public JTableHeader()

Constructs a

JTableHeader

with a default

TableColumnModel

.

JTableHeader

```java
public JTableHeader​(
TableColumnModel
cm)
```

Constructs a

JTableHeader

which is initialized with

cm

as the column model. If

cm

is

null

this method will initialize the table header
with a default

TableColumnModel

.

**Parameters:** cm

- the column model for the table
**See Also:** createDefaultColumnModel()

---

#### JTableHeader

public JTableHeader​(

TableColumnModel

cm)

Constructs a

JTableHeader

which is initialized with

cm

as the column model. If

cm

is

null

this method will initialize the table header
with a default

TableColumnModel

.

Method Detail

- setTable

```java
@BeanProperty
(
description
="The table associated with this header.")
public void setTable​(
JTable
table)
```

Sets the table associated with this header.

**Parameters:** table

- the new table

- getTable

```java
public
JTable
getTable()
```

Returns the table associated with this header.

**Returns:** the

table

property

- setReorderingAllowed

```java
@BeanProperty
(
description
="Whether the user can drag column headers to reorder columns.")
public void setReorderingAllowed​(boolean reorderingAllowed)
```

Sets whether the user can drag column headers to reorder columns.

**Parameters:** reorderingAllowed

- true if the table view should allow
reordering; otherwise false
**See Also:** getReorderingAllowed()

- getReorderingAllowed

```java
public boolean getReorderingAllowed()
```

Returns true if the user is allowed to rearrange columns by
dragging their headers, false otherwise. The default is true. You can
rearrange columns programmatically regardless of this setting.

**Returns:** the

reorderingAllowed

property
**See Also:** setReorderingAllowed(boolean)

- setResizingAllowed

```java
@BeanProperty
(
description
="Whether the user can resize columns by dragging between headers.")
public void setResizingAllowed​(boolean resizingAllowed)
```

Sets whether the user can resize columns by dragging between headers.

**Parameters:** resizingAllowed

- true if table view should allow
resizing
**See Also:** getResizingAllowed()

- getResizingAllowed

```java
public boolean getResizingAllowed()
```

Returns true if the user is allowed to resize columns by dragging
between their headers, false otherwise. The default is true. You can
resize columns programmatically regardless of this setting.

**Returns:** the

resizingAllowed

property
**See Also:** setResizingAllowed(boolean)

- getDraggedColumn

```java
public
TableColumn
getDraggedColumn()
```

Returns the dragged column, if and only if, a drag is in
process, otherwise returns

null

.

**Returns:** the dragged column, if a drag is in
process, otherwise returns

null
**See Also:** getDraggedDistance()

- getDraggedDistance

```java
public int getDraggedDistance()
```

Returns the column's horizontal distance from its original
position, if and only if, a drag is in process. Otherwise, the
the return value is meaningless.

**Returns:** the column's horizontal distance from its original
position, if a drag is in process, otherwise the return
value is meaningless
**See Also:** getDraggedColumn()

- getResizingColumn

```java
public
TableColumn
getResizingColumn()
```

Returns the resizing column. If no column is being
resized this method returns

null

.

**Returns:** the resizing column, if a resize is in process, otherwise
returns

null

- setUpdateTableInRealTime

```java
public void setUpdateTableInRealTime​(boolean flag)
```

Obsolete as of Java 2 platform v1.3. Real time repaints, in response to
column dragging or resizing, are now unconditional.

**Parameters:** flag

- true if tableView should update the body of the
table in real time

- getUpdateTableInRealTime

```java
public boolean getUpdateTableInRealTime()
```

Obsolete as of Java 2 platform v1.3. Real time repaints, in response to
column dragging or resizing, are now unconditional.

**Returns:** true if the table updates in real time

- setDefaultRenderer

```java
public void setDefaultRenderer​(
TableCellRenderer
defaultRenderer)
```

Sets the default renderer to be used when no

headerRenderer

is defined by a

TableColumn

.

**Parameters:** defaultRenderer

- the default renderer
**Since:** 1.3

- getDefaultRenderer

```java
public
TableCellRenderer
getDefaultRenderer()
```

Returns the default renderer used when no

headerRenderer

is defined by a

TableColumn

.

**Returns:** the default renderer
**Since:** 1.3

- columnAtPoint

```java
public int columnAtPoint​(
Point
point)
```

Returns the index of the column that

point

lies in, or -1 if it
lies out of bounds.

**Parameters:** point

- if this

point

lies within a column, the index of
that column will be returned; otherwise it is out of bounds
and -1 is returned
**Returns:** the index of the column that

point

lies in, or -1 if it
lies out of bounds

- getHeaderRect

```java
public
Rectangle
getHeaderRect​(int column)
```

Returns the rectangle containing the header tile at

column

.
When the

column

parameter is out of bounds this method uses the
same conventions as the

JTable

method

getCellRect

.

**Parameters:** column

- index of the column
**Returns:** the rectangle containing the header tile at

column
**See Also:** JTable.getCellRect(int, int, boolean)

- getToolTipText

```java
public
String
getToolTipText​(
MouseEvent
event)
```

Allows the renderer's tips to be used if there is text set.

**Overrides:** getToolTipText

in class

JComponent
**Parameters:** event

- the location of the event identifies the proper
renderer and, therefore, the proper tip
**Returns:** the tool tip for this component

- getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Returns the preferred size of the table header.
This is the size required to display the header and requested for
the viewport.
The returned

Dimension

width

will always be calculated by
the underlying TableHeaderUI, regardless of any width specified by

JComponent.setPreferredSize(java.awt.Dimension)

**Overrides:** getPreferredSize

in class

JComponent
**Returns:** the size
**See Also:** JComponent.setPreferredSize(java.awt.Dimension)

,

ComponentUI

- getUI

```java
public
TableHeaderUI
getUI()
```

Returns the look and feel (L&F) object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

TableHeaderUI

object that renders this component

- setUI

```java
public void setUI​(
TableHeaderUI
ui)
```

Sets the look and feel (L&F) object that renders this component.

**Parameters:** ui

- the

TableHeaderUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

- updateUI

```java
public void updateUI()
```

Notification from the

UIManager

that the look and feel
(L&F) has changed.
Replaces the current UI object with the latest version from the

UIManager

.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

- getUIClassID

```java
public
String
getUIClassID()
```

Returns the suffix used to construct the name of the look and feel
(L&F) class used to render this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "TableHeaderUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- setColumnModel

```java
@BeanProperty
(
description
="The object governing the way columns appear in the view.")
public void setColumnModel​(
TableColumnModel
columnModel)
```

Sets the column model for this table to

newModel

and registers
for listener notifications from the new column model.

**Parameters:** columnModel

- the new data source for this table
**Throws:** IllegalArgumentException

- if

newModel

is

null
**See Also:** getColumnModel()

- getColumnModel

```java
public
TableColumnModel
getColumnModel()
```

Returns the

TableColumnModel

that contains all column information
of this table header.

**Returns:** the

columnModel

property
**See Also:** setColumnModel(javax.swing.table.TableColumnModel)

- columnAdded

```java
public void columnAdded​(
TableColumnModelEvent
e)
```

Invoked when a column is added to the table column model.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

**Specified by:** columnAdded

in interface

TableColumnModelListener
**Parameters:** e

- the event received
**See Also:** TableColumnModelListener

- columnRemoved

```java
public void columnRemoved​(
TableColumnModelEvent
e)
```

Invoked when a column is removed from the table column model.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

**Specified by:** columnRemoved

in interface

TableColumnModelListener
**Parameters:** e

- the event received
**See Also:** TableColumnModelListener

- columnMoved

```java
public void columnMoved​(
TableColumnModelEvent
e)
```

Invoked when a column is repositioned.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

**Specified by:** columnMoved

in interface

TableColumnModelListener
**Parameters:** e

- the event received
**See Also:** TableColumnModelListener

- columnMarginChanged

```java
public void columnMarginChanged​(
ChangeEvent
e)
```

Invoked when a column is moved due to a margin change.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

**Specified by:** columnMarginChanged

in interface

TableColumnModelListener
**Parameters:** e

- the event received
**See Also:** TableColumnModelListener

- columnSelectionChanged

```java
public void columnSelectionChanged​(
ListSelectionEvent
e)
```

Invoked when the selection model of the

TableColumnModel

is changed. This method currently has no effect (the header is not
redrawn).

Application code will not use these methods explicitly, they
are used internally by

JTable

.

**Specified by:** columnSelectionChanged

in interface

TableColumnModelListener
**Parameters:** e

- the event received
**See Also:** TableColumnModelListener

- createDefaultColumnModel

```java
protected
TableColumnModel
createDefaultColumnModel()
```

Returns the default column model object which is
a

DefaultTableColumnModel

. A subclass can override this
method to return a different column model object

**Returns:** the default column model object

- createDefaultRenderer

```java
protected
TableCellRenderer
createDefaultRenderer()
```

Returns a default renderer to be used when no header renderer
is defined by a

TableColumn

.

**Returns:** the default table column renderer
**Since:** 1.3

- initializeLocalVars

```java
protected void initializeLocalVars()
```

Initializes the local variables and properties with default values.
Used by the constructor methods.

- resizeAndRepaint

```java
public void resizeAndRepaint()
```

Sizes the header and marks it as needing display. Equivalent
to

revalidate

followed by

repaint

.

- setDraggedColumn

```java
public void setDraggedColumn​(
TableColumn
aColumn)
```

Sets the header's

draggedColumn

to

aColumn

.

Application code will not use this method explicitly, it is used
internally by the column dragging mechanism.

**Parameters:** aColumn

- the column being dragged, or

null

if
no column is being dragged

- setDraggedDistance

```java
public void setDraggedDistance​(int distance)
```

Sets the header's

draggedDistance

to

distance

.

**Parameters:** distance

- the distance dragged

- setResizingColumn

```java
public void setResizingColumn​(
TableColumn
aColumn)
```

Sets the header's

resizingColumn

to

aColumn

.

Application code will not use this method explicitly, it
is used internally by the column sizing mechanism.

**Parameters:** aColumn

- the column being resized, or

null

if
no column is being resized

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JTableHeader

. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

Overriding

paramString

to provide information about the
specific new aspects of the JFC components.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

JTableHeader

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JTableHeader.
For JTableHeaders, the AccessibleContext takes the form of an
AccessibleJTableHeader.
A new AccessibleJTableHeader instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJTableHeader that serves as the
AccessibleContext of this JTableHeader

---

#### Method Detail

setTable

```java
@BeanProperty
(
description
="The table associated with this header.")
public void setTable​(
JTable
table)
```

Sets the table associated with this header.

**Parameters:** table

- the new table

---

#### setTable

@BeanProperty

(

description

="The table associated with this header.")
public void setTable​(

JTable

table)

Sets the table associated with this header.

getTable

```java
public
JTable
getTable()
```

Returns the table associated with this header.

**Returns:** the

table

property

---

#### getTable

public

JTable

getTable()

Returns the table associated with this header.

setReorderingAllowed

```java
@BeanProperty
(
description
="Whether the user can drag column headers to reorder columns.")
public void setReorderingAllowed​(boolean reorderingAllowed)
```

Sets whether the user can drag column headers to reorder columns.

**Parameters:** reorderingAllowed

- true if the table view should allow
reordering; otherwise false
**See Also:** getReorderingAllowed()

---

#### setReorderingAllowed

@BeanProperty

(

description

="Whether the user can drag column headers to reorder columns.")
public void setReorderingAllowed​(boolean reorderingAllowed)

Sets whether the user can drag column headers to reorder columns.

getReorderingAllowed

```java
public boolean getReorderingAllowed()
```

Returns true if the user is allowed to rearrange columns by
dragging their headers, false otherwise. The default is true. You can
rearrange columns programmatically regardless of this setting.

**Returns:** the

reorderingAllowed

property
**See Also:** setReorderingAllowed(boolean)

---

#### getReorderingAllowed

public boolean getReorderingAllowed()

Returns true if the user is allowed to rearrange columns by
dragging their headers, false otherwise. The default is true. You can
rearrange columns programmatically regardless of this setting.

setResizingAllowed

```java
@BeanProperty
(
description
="Whether the user can resize columns by dragging between headers.")
public void setResizingAllowed​(boolean resizingAllowed)
```

Sets whether the user can resize columns by dragging between headers.

**Parameters:** resizingAllowed

- true if table view should allow
resizing
**See Also:** getResizingAllowed()

---

#### setResizingAllowed

@BeanProperty

(

description

="Whether the user can resize columns by dragging between headers.")
public void setResizingAllowed​(boolean resizingAllowed)

Sets whether the user can resize columns by dragging between headers.

getResizingAllowed

```java
public boolean getResizingAllowed()
```

Returns true if the user is allowed to resize columns by dragging
between their headers, false otherwise. The default is true. You can
resize columns programmatically regardless of this setting.

**Returns:** the

resizingAllowed

property
**See Also:** setResizingAllowed(boolean)

---

#### getResizingAllowed

public boolean getResizingAllowed()

Returns true if the user is allowed to resize columns by dragging
between their headers, false otherwise. The default is true. You can
resize columns programmatically regardless of this setting.

getDraggedColumn

```java
public
TableColumn
getDraggedColumn()
```

Returns the dragged column, if and only if, a drag is in
process, otherwise returns

null

.

**Returns:** the dragged column, if a drag is in
process, otherwise returns

null
**See Also:** getDraggedDistance()

---

#### getDraggedColumn

public

TableColumn

getDraggedColumn()

Returns the dragged column, if and only if, a drag is in
process, otherwise returns

null

.

getDraggedDistance

```java
public int getDraggedDistance()
```

Returns the column's horizontal distance from its original
position, if and only if, a drag is in process. Otherwise, the
the return value is meaningless.

**Returns:** the column's horizontal distance from its original
position, if a drag is in process, otherwise the return
value is meaningless
**See Also:** getDraggedColumn()

---

#### getDraggedDistance

public int getDraggedDistance()

Returns the column's horizontal distance from its original
position, if and only if, a drag is in process. Otherwise, the
the return value is meaningless.

getResizingColumn

```java
public
TableColumn
getResizingColumn()
```

Returns the resizing column. If no column is being
resized this method returns

null

.

**Returns:** the resizing column, if a resize is in process, otherwise
returns

null

---

#### getResizingColumn

public

TableColumn

getResizingColumn()

Returns the resizing column. If no column is being
resized this method returns

null

.

setUpdateTableInRealTime

```java
public void setUpdateTableInRealTime​(boolean flag)
```

Obsolete as of Java 2 platform v1.3. Real time repaints, in response to
column dragging or resizing, are now unconditional.

**Parameters:** flag

- true if tableView should update the body of the
table in real time

---

#### setUpdateTableInRealTime

public void setUpdateTableInRealTime​(boolean flag)

Obsolete as of Java 2 platform v1.3. Real time repaints, in response to
column dragging or resizing, are now unconditional.

getUpdateTableInRealTime

```java
public boolean getUpdateTableInRealTime()
```

Obsolete as of Java 2 platform v1.3. Real time repaints, in response to
column dragging or resizing, are now unconditional.

**Returns:** true if the table updates in real time

---

#### getUpdateTableInRealTime

public boolean getUpdateTableInRealTime()

Obsolete as of Java 2 platform v1.3. Real time repaints, in response to
column dragging or resizing, are now unconditional.

setDefaultRenderer

```java
public void setDefaultRenderer​(
TableCellRenderer
defaultRenderer)
```

Sets the default renderer to be used when no

headerRenderer

is defined by a

TableColumn

.

**Parameters:** defaultRenderer

- the default renderer
**Since:** 1.3

---

#### setDefaultRenderer

public void setDefaultRenderer​(

TableCellRenderer

defaultRenderer)

Sets the default renderer to be used when no

headerRenderer

is defined by a

TableColumn

.

getDefaultRenderer

```java
public
TableCellRenderer
getDefaultRenderer()
```

Returns the default renderer used when no

headerRenderer

is defined by a

TableColumn

.

**Returns:** the default renderer
**Since:** 1.3

---

#### getDefaultRenderer

public

TableCellRenderer

getDefaultRenderer()

Returns the default renderer used when no

headerRenderer

is defined by a

TableColumn

.

columnAtPoint

```java
public int columnAtPoint​(
Point
point)
```

Returns the index of the column that

point

lies in, or -1 if it
lies out of bounds.

**Parameters:** point

- if this

point

lies within a column, the index of
that column will be returned; otherwise it is out of bounds
and -1 is returned
**Returns:** the index of the column that

point

lies in, or -1 if it
lies out of bounds

---

#### columnAtPoint

public int columnAtPoint​(

Point

point)

Returns the index of the column that

point

lies in, or -1 if it
lies out of bounds.

getHeaderRect

```java
public
Rectangle
getHeaderRect​(int column)
```

Returns the rectangle containing the header tile at

column

.
When the

column

parameter is out of bounds this method uses the
same conventions as the

JTable

method

getCellRect

.

**Parameters:** column

- index of the column
**Returns:** the rectangle containing the header tile at

column
**See Also:** JTable.getCellRect(int, int, boolean)

---

#### getHeaderRect

public

Rectangle

getHeaderRect​(int column)

Returns the rectangle containing the header tile at

column

.
When the

column

parameter is out of bounds this method uses the
same conventions as the

JTable

method

getCellRect

.

getToolTipText

```java
public
String
getToolTipText​(
MouseEvent
event)
```

Allows the renderer's tips to be used if there is text set.

**Overrides:** getToolTipText

in class

JComponent
**Parameters:** event

- the location of the event identifies the proper
renderer and, therefore, the proper tip
**Returns:** the tool tip for this component

---

#### getToolTipText

public

String

getToolTipText​(

MouseEvent

event)

Allows the renderer's tips to be used if there is text set.

getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Returns the preferred size of the table header.
This is the size required to display the header and requested for
the viewport.
The returned

Dimension

width

will always be calculated by
the underlying TableHeaderUI, regardless of any width specified by

JComponent.setPreferredSize(java.awt.Dimension)

**Overrides:** getPreferredSize

in class

JComponent
**Returns:** the size
**See Also:** JComponent.setPreferredSize(java.awt.Dimension)

,

ComponentUI

---

#### getPreferredSize

public

Dimension

getPreferredSize()

Returns the preferred size of the table header.
This is the size required to display the header and requested for
the viewport.
The returned

Dimension

width

will always be calculated by
the underlying TableHeaderUI, regardless of any width specified by

JComponent.setPreferredSize(java.awt.Dimension)

getUI

```java
public
TableHeaderUI
getUI()
```

Returns the look and feel (L&F) object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

TableHeaderUI

object that renders this component

---

#### getUI

public

TableHeaderUI

getUI()

Returns the look and feel (L&F) object that renders this component.

setUI

```java
public void setUI​(
TableHeaderUI
ui)
```

Sets the look and feel (L&F) object that renders this component.

**Parameters:** ui

- the

TableHeaderUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

---

#### setUI

public void setUI​(

TableHeaderUI

ui)

Sets the look and feel (L&F) object that renders this component.

updateUI

```java
public void updateUI()
```

Notification from the

UIManager

that the look and feel
(L&F) has changed.
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

that the look and feel
(L&F) has changed.
Replaces the current UI object with the latest version from the

UIManager

.

getUIClassID

```java
public
String
getUIClassID()
```

Returns the suffix used to construct the name of the look and feel
(L&F) class used to render this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "TableHeaderUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### getUIClassID

public

String

getUIClassID()

Returns the suffix used to construct the name of the look and feel
(L&F) class used to render this component.

setColumnModel

```java
@BeanProperty
(
description
="The object governing the way columns appear in the view.")
public void setColumnModel​(
TableColumnModel
columnModel)
```

Sets the column model for this table to

newModel

and registers
for listener notifications from the new column model.

**Parameters:** columnModel

- the new data source for this table
**Throws:** IllegalArgumentException

- if

newModel

is

null
**See Also:** getColumnModel()

---

#### setColumnModel

@BeanProperty

(

description

="The object governing the way columns appear in the view.")
public void setColumnModel​(

TableColumnModel

columnModel)

Sets the column model for this table to

newModel

and registers
for listener notifications from the new column model.

getColumnModel

```java
public
TableColumnModel
getColumnModel()
```

Returns the

TableColumnModel

that contains all column information
of this table header.

**Returns:** the

columnModel

property
**See Also:** setColumnModel(javax.swing.table.TableColumnModel)

---

#### getColumnModel

public

TableColumnModel

getColumnModel()

Returns the

TableColumnModel

that contains all column information
of this table header.

columnAdded

```java
public void columnAdded​(
TableColumnModelEvent
e)
```

Invoked when a column is added to the table column model.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

**Specified by:** columnAdded

in interface

TableColumnModelListener
**Parameters:** e

- the event received
**See Also:** TableColumnModelListener

---

#### columnAdded

public void columnAdded​(

TableColumnModelEvent

e)

Invoked when a column is added to the table column model.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

columnRemoved

```java
public void columnRemoved​(
TableColumnModelEvent
e)
```

Invoked when a column is removed from the table column model.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

**Specified by:** columnRemoved

in interface

TableColumnModelListener
**Parameters:** e

- the event received
**See Also:** TableColumnModelListener

---

#### columnRemoved

public void columnRemoved​(

TableColumnModelEvent

e)

Invoked when a column is removed from the table column model.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

columnMoved

```java
public void columnMoved​(
TableColumnModelEvent
e)
```

Invoked when a column is repositioned.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

**Specified by:** columnMoved

in interface

TableColumnModelListener
**Parameters:** e

- the event received
**See Also:** TableColumnModelListener

---

#### columnMoved

public void columnMoved​(

TableColumnModelEvent

e)

Invoked when a column is repositioned.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

columnMarginChanged

```java
public void columnMarginChanged​(
ChangeEvent
e)
```

Invoked when a column is moved due to a margin change.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

**Specified by:** columnMarginChanged

in interface

TableColumnModelListener
**Parameters:** e

- the event received
**See Also:** TableColumnModelListener

---

#### columnMarginChanged

public void columnMarginChanged​(

ChangeEvent

e)

Invoked when a column is moved due to a margin change.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

columnSelectionChanged

```java
public void columnSelectionChanged​(
ListSelectionEvent
e)
```

Invoked when the selection model of the

TableColumnModel

is changed. This method currently has no effect (the header is not
redrawn).

Application code will not use these methods explicitly, they
are used internally by

JTable

.

**Specified by:** columnSelectionChanged

in interface

TableColumnModelListener
**Parameters:** e

- the event received
**See Also:** TableColumnModelListener

---

#### columnSelectionChanged

public void columnSelectionChanged​(

ListSelectionEvent

e)

Invoked when the selection model of the

TableColumnModel

is changed. This method currently has no effect (the header is not
redrawn).

Application code will not use these methods explicitly, they
are used internally by

JTable

.

Application code will not use these methods explicitly, they
are used internally by

JTable

.

createDefaultColumnModel

```java
protected
TableColumnModel
createDefaultColumnModel()
```

Returns the default column model object which is
a

DefaultTableColumnModel

. A subclass can override this
method to return a different column model object

**Returns:** the default column model object

---

#### createDefaultColumnModel

protected

TableColumnModel

createDefaultColumnModel()

Returns the default column model object which is
a

DefaultTableColumnModel

. A subclass can override this
method to return a different column model object

createDefaultRenderer

```java
protected
TableCellRenderer
createDefaultRenderer()
```

Returns a default renderer to be used when no header renderer
is defined by a

TableColumn

.

**Returns:** the default table column renderer
**Since:** 1.3

---

#### createDefaultRenderer

protected

TableCellRenderer

createDefaultRenderer()

Returns a default renderer to be used when no header renderer
is defined by a

TableColumn

.

initializeLocalVars

```java
protected void initializeLocalVars()
```

Initializes the local variables and properties with default values.
Used by the constructor methods.

---

#### initializeLocalVars

protected void initializeLocalVars()

Initializes the local variables and properties with default values.
Used by the constructor methods.

resizeAndRepaint

```java
public void resizeAndRepaint()
```

Sizes the header and marks it as needing display. Equivalent
to

revalidate

followed by

repaint

.

---

#### resizeAndRepaint

public void resizeAndRepaint()

Sizes the header and marks it as needing display. Equivalent
to

revalidate

followed by

repaint

.

setDraggedColumn

```java
public void setDraggedColumn​(
TableColumn
aColumn)
```

Sets the header's

draggedColumn

to

aColumn

.

Application code will not use this method explicitly, it is used
internally by the column dragging mechanism.

**Parameters:** aColumn

- the column being dragged, or

null

if
no column is being dragged

---

#### setDraggedColumn

public void setDraggedColumn​(

TableColumn

aColumn)

Sets the header's

draggedColumn

to

aColumn

.

Application code will not use this method explicitly, it is used
internally by the column dragging mechanism.

Application code will not use this method explicitly, it is used
internally by the column dragging mechanism.

setDraggedDistance

```java
public void setDraggedDistance​(int distance)
```

Sets the header's

draggedDistance

to

distance

.

**Parameters:** distance

- the distance dragged

---

#### setDraggedDistance

public void setDraggedDistance​(int distance)

Sets the header's

draggedDistance

to

distance

.

setResizingColumn

```java
public void setResizingColumn​(
TableColumn
aColumn)
```

Sets the header's

resizingColumn

to

aColumn

.

Application code will not use this method explicitly, it
is used internally by the column sizing mechanism.

**Parameters:** aColumn

- the column being resized, or

null

if
no column is being resized

---

#### setResizingColumn

public void setResizingColumn​(

TableColumn

aColumn)

Sets the header's

resizingColumn

to

aColumn

.

Application code will not use this method explicitly, it
is used internally by the column sizing mechanism.

Application code will not use this method explicitly, it
is used internally by the column sizing mechanism.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JTableHeader

. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

Overriding

paramString

to provide information about the
specific new aspects of the JFC components.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

JTableHeader

---

#### paramString

protected

String

paramString()

Returns a string representation of this

JTableHeader

. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

Overriding

paramString

to provide information about the
specific new aspects of the JFC components.

Overriding

paramString

to provide information about the
specific new aspects of the JFC components.

getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JTableHeader.
For JTableHeaders, the AccessibleContext takes the form of an
AccessibleJTableHeader.
A new AccessibleJTableHeader instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJTableHeader that serves as the
AccessibleContext of this JTableHeader

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this JTableHeader.
For JTableHeaders, the AccessibleContext takes the form of an
AccessibleJTableHeader.
A new AccessibleJTableHeader instance is created if necessary.

---

