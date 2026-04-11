# Class DefaultTableCellRenderer

**Source:** `java.desktop\javax\swing\table\DefaultTableCellRenderer.html`

### Class Description

```java
public class
DefaultTableCellRenderer

extends
JLabel

implements
TableCellRenderer
,
Serializable
```

The standard class for rendering (displaying) individual cells
in a

JTable

.

Implementation Note:

This class inherits from

JLabel

, a standard component class.
However

JTable

employs a unique mechanism for rendering
its cells and therefore requires some slightly modified behavior
from its cell renderer.
The table class defines a single cell renderer and uses it as a
as a rubber-stamp for rendering all cells in the table;
it renders the first cell,
changes the contents of that cell renderer,
shifts the origin to the new location, re-draws it, and so on.
The standard

JLabel

component was not
designed to be used this way and we want to avoid
triggering a

revalidate

each time the
cell is drawn. This would greatly decrease performance because the

revalidate

message would be
passed up the hierarchy of the container to determine whether any other
components would be affected.
As the renderer is only parented for the lifetime of a painting operation
we similarly want to avoid the overhead associated with walking the
hierarchy for painting operations.
So this class
overrides the

validate

,

invalidate

,

revalidate

,

repaint

, and

firePropertyChange

methods to be
no-ops and override the

isOpaque

method solely to improve
performance. If you write your own renderer,
please keep this performance consideration in mind.

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

SwingConstants

,

TableCellRenderer

---

### Field Details

#### protected static
Border
noFocusBorder

A border without focus.

---

### Constructor Details

#### public DefaultTableCellRenderer()

Creates a default table cell renderer.

---

### Method Details

#### public void setForeground​(
Color
c)

Overrides

JComponent.setForeground

to assign
the unselected-foreground color to the specified color.

**Overrides:**
- setForeground

in class

JComponent

**Parameters:**
- c

- set the foreground color to this value

**See Also:**
- Component.getForeground()

---

#### public void setBackground​(
Color
c)

Overrides

JComponent.setBackground

to assign
the unselected-background color to the specified color.

**Overrides:**
- setBackground

in class

JComponent

**Parameters:**
- c

- set the background color to this value

**See Also:**
- Component.getBackground()

,

JComponent.setOpaque(boolean)

---

#### public void updateUI()

Notification from the

UIManager

that the look and feel
[L&F] has changed.
Replaces the current UI object with the latest version from the

UIManager

.

**Overrides:**
- updateUI

in class

JLabel

**See Also:**
- JComponent.updateUI()

---

#### public
Component
getTableCellRendererComponent​(
JTable
table,

Object
value,
boolean isSelected,
boolean hasFocus,
int row,
int column)

Returns the default table cell renderer.

During a printing operation, this method will be called with

isSelected

and

hasFocus

values of

false

to prevent selection and focus from appearing
in the printed output. To do other customization based on whether
or not the table is being printed, check the return value from

JComponent.isPaintingForPrint()

.

**Specified by:**
- getTableCellRendererComponent

in interface

TableCellRenderer

**Parameters:**
- table

- the

JTable
- value

- the value to assign to the cell at

[row, column]
- isSelected

- true if cell is selected
- hasFocus

- true if cell has focus
- row

- the row of the cell to render
- column

- the column of the cell to render

**Returns:**
- the default table cell renderer

**See Also:**
- JComponent.isPaintingForPrint()

---

#### public boolean isOpaque()

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- isOpaque

in class

JComponent

**Returns:**
- true if this component is completely opaque

**See Also:**
- JComponent.setOpaque(boolean)

---

#### public void invalidate()

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- invalidate

in class

Container

**See Also:**
- Container.validate()

,

Container.layout()

,

LayoutManager2

**Since:**
- 1.5

---

#### public void validate()

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- validate

in class

Container

**See Also:**
- Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.isValidateRoot()

,

JComponent.revalidate()

,

Container.validateTree()

---

#### public void revalidate()

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- revalidate

in class

JComponent

**See Also:**
- Component.invalidate()

,

Container.validate()

,

JComponent.isValidateRoot()

,

RepaintManager.addInvalidComponent(javax.swing.JComponent)

---

#### public void repaint​(long tm,
int x,
int y,
int width,
int height)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- repaint

in class

JComponent

**Parameters:**
- tm

- this parameter is not used
- x

- the x value of the dirty region
- y

- the y value of the dirty region
- width

- the width of the dirty region
- height

- the height of the dirty region

**See Also:**
- JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

---

#### public void repaint​(
Rectangle
r)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- repaint

in class

JComponent

**Parameters:**
- r

- a

Rectangle

containing the dirty region

**See Also:**
- JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

---

#### public void repaint()

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- repaint

in class

Component

**See Also:**
- Component.update(Graphics)

**Since:**
- 1.5

---

#### protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- firePropertyChange

in class

Component

**Parameters:**
- propertyName

- the property whose value has changed
- oldValue

- the property's previous value
- newValue

- the property's new value

---

#### public void firePropertyChange​(
String
propertyName,
boolean oldValue,
boolean newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:**
- firePropertyChange

in class

JComponent

**Parameters:**
- propertyName

- the property whose value has changed
- oldValue

- the property's previous value
- newValue

- the property's new value

---

#### protected void setValue​(
Object
value)

Sets the

String

object for the cell being rendered to

value

.

**Parameters:**
- value

- the string value for this cell; if value is

null

it sets the text value to an empty string

**See Also:**
- JLabel.setText(java.lang.String)

---

### Additional Sections

#### Class DefaultTableCellRenderer

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JLabel
- - javax.swing.table.DefaultTableCellRenderer

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JLabel
- - javax.swing.table.DefaultTableCellRenderer

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JLabel
- - javax.swing.table.DefaultTableCellRenderer

javax.swing.JComponent

- javax.swing.JLabel
- - javax.swing.table.DefaultTableCellRenderer

javax.swing.JLabel

- javax.swing.table.DefaultTableCellRenderer

javax.swing.table.DefaultTableCellRenderer

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

,

SwingConstants

,

TableCellRenderer

**Direct Known Subclasses:** DefaultTableCellRenderer.UIResource

```java
public class
DefaultTableCellRenderer

extends
JLabel

implements
TableCellRenderer
,
Serializable
```

The standard class for rendering (displaying) individual cells
in a

JTable

.

Implementation Note:

This class inherits from

JLabel

, a standard component class.
However

JTable

employs a unique mechanism for rendering
its cells and therefore requires some slightly modified behavior
from its cell renderer.
The table class defines a single cell renderer and uses it as a
as a rubber-stamp for rendering all cells in the table;
it renders the first cell,
changes the contents of that cell renderer,
shifts the origin to the new location, re-draws it, and so on.
The standard

JLabel

component was not
designed to be used this way and we want to avoid
triggering a

revalidate

each time the
cell is drawn. This would greatly decrease performance because the

revalidate

message would be
passed up the hierarchy of the container to determine whether any other
components would be affected.
As the renderer is only parented for the lifetime of a painting operation
we similarly want to avoid the overhead associated with walking the
hierarchy for painting operations.
So this class
overrides the

validate

,

invalidate

,

revalidate

,

repaint

, and

firePropertyChange

methods to be
no-ops and override the

isOpaque

method solely to improve
performance. If you write your own renderer,
please keep this performance consideration in mind.

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

DefaultTableCellRenderer

extends

JLabel

implements

TableCellRenderer

,

Serializable

The standard class for rendering (displaying) individual cells
in a

JTable

.

Implementation Note:

This class inherits from

JLabel

, a standard component class.
However

JTable

employs a unique mechanism for rendering
its cells and therefore requires some slightly modified behavior
from its cell renderer.
The table class defines a single cell renderer and uses it as a
as a rubber-stamp for rendering all cells in the table;
it renders the first cell,
changes the contents of that cell renderer,
shifts the origin to the new location, re-draws it, and so on.
The standard

JLabel

component was not
designed to be used this way and we want to avoid
triggering a

revalidate

each time the
cell is drawn. This would greatly decrease performance because the

revalidate

message would be
passed up the hierarchy of the container to determine whether any other
components would be affected.
As the renderer is only parented for the lifetime of a painting operation
we similarly want to avoid the overhead associated with walking the
hierarchy for painting operations.
So this class
overrides the

validate

,

invalidate

,

revalidate

,

repaint

, and

firePropertyChange

methods to be
no-ops and override the

isOpaque

method solely to improve
performance. If you write your own renderer,
please keep this performance consideration in mind.

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

Implementation Note:

This class inherits from

JLabel

, a standard component class.
However

JTable

employs a unique mechanism for rendering
its cells and therefore requires some slightly modified behavior
from its cell renderer.
The table class defines a single cell renderer and uses it as a
as a rubber-stamp for rendering all cells in the table;
it renders the first cell,
changes the contents of that cell renderer,
shifts the origin to the new location, re-draws it, and so on.
The standard

JLabel

component was not
designed to be used this way and we want to avoid
triggering a

revalidate

each time the
cell is drawn. This would greatly decrease performance because the

revalidate

message would be
passed up the hierarchy of the container to determine whether any other
components would be affected.
As the renderer is only parented for the lifetime of a painting operation
we similarly want to avoid the overhead associated with walking the
hierarchy for painting operations.
So this class
overrides the

validate

,

invalidate

,

revalidate

,

repaint

, and

firePropertyChange

methods to be
no-ops and override the

isOpaque

method solely to improve
performance. If you write your own renderer,
please keep this performance consideration in mind.

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

static class

DefaultTableCellRenderer.UIResource

A subclass of

DefaultTableCellRenderer

that
implements

UIResource

.

- Nested classes/interfaces declared in class javax.swing.

JLabel

JLabel.AccessibleJLabel

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

protected static

Border

noFocusBorder

A border without focus.

- Fields declared in class javax.swing.

JLabel

labelFor

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

DefaultTableCellRenderer

()

Creates a default table cell renderer.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

firePropertyChange

​(

String

propertyName,
boolean oldValue,
boolean newValue)

Overridden for performance reasons.

protected void

firePropertyChange

​(

String

propertyName,

Object

oldValue,

Object

newValue)

Overridden for performance reasons.

Component

getTableCellRendererComponent

​(

JTable

table,

Object

value,
boolean isSelected,
boolean hasFocus,
int row,
int column)

Returns the default table cell renderer.

void

invalidate

()

Overridden for performance reasons.

boolean

isOpaque

()

Overridden for performance reasons.

void

repaint

()

Overridden for performance reasons.

void

repaint

​(long tm,
int x,
int y,
int width,
int height)

Overridden for performance reasons.

void

repaint

​(

Rectangle

r)

Overridden for performance reasons.

void

revalidate

()

Overridden for performance reasons.

void

setBackground

​(

Color

c)

Overrides

JComponent.setBackground

to assign
the unselected-background color to the specified color.

void

setForeground

​(

Color

c)

Overrides

JComponent.setForeground

to assign
the unselected-foreground color to the specified color.

protected void

setValue

​(

Object

value)

Sets the

String

object for the cell being rendered to

value

.

void

updateUI

()

Notification from the

UIManager

that the look and feel
[L&F] has changed.

void

validate

()

Overridden for performance reasons.

- Methods declared in class javax.swing.

JLabel

checkHorizontalKey

,

checkVerticalKey

,

getAccessibleContext

,

getDisabledIcon

,

getDisplayedMnemonic

,

getDisplayedMnemonicIndex

,

getHorizontalAlignment

,

getHorizontalTextPosition

,

getIcon

,

getIconTextGap

,

getLabelFor

,

getText

,

getUI

,

getUIClassID

,

getVerticalAlignment

,

getVerticalTextPosition

,

imageUpdate

,

paramString

,

setDisabledIcon

,

setDisplayedMnemonic

,

setDisplayedMnemonic

,

setDisplayedMnemonicIndex

,

setHorizontalAlignment

,

setHorizontalTextPosition

,

setIcon

,

setIconTextGap

,

setLabelFor

,

setText

,

setUI

,

setVerticalAlignment

,

setVerticalTextPosition

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

static class

DefaultTableCellRenderer.UIResource

A subclass of

DefaultTableCellRenderer

that
implements

UIResource

.

- Nested classes/interfaces declared in class javax.swing.

JLabel

JLabel.AccessibleJLabel

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

A subclass of

DefaultTableCellRenderer

that
implements

UIResource

.

Nested classes/interfaces declared in class javax.swing.

JLabel

JLabel.AccessibleJLabel

---

#### Nested classes/interfaces declared in class javax.swing. JLabel

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

protected static

Border

noFocusBorder

A border without focus.

- Fields declared in class javax.swing.

JLabel

labelFor

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

A border without focus.

Fields declared in class javax.swing.

JLabel

labelFor

---

#### Fields declared in class javax.swing. JLabel

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

DefaultTableCellRenderer

()

Creates a default table cell renderer.

---

#### Constructor Summary

Creates a default table cell renderer.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

firePropertyChange

​(

String

propertyName,
boolean oldValue,
boolean newValue)

Overridden for performance reasons.

protected void

firePropertyChange

​(

String

propertyName,

Object

oldValue,

Object

newValue)

Overridden for performance reasons.

Component

getTableCellRendererComponent

​(

JTable

table,

Object

value,
boolean isSelected,
boolean hasFocus,
int row,
int column)

Returns the default table cell renderer.

void

invalidate

()

Overridden for performance reasons.

boolean

isOpaque

()

Overridden for performance reasons.

void

repaint

()

Overridden for performance reasons.

void

repaint

​(long tm,
int x,
int y,
int width,
int height)

Overridden for performance reasons.

void

repaint

​(

Rectangle

r)

Overridden for performance reasons.

void

revalidate

()

Overridden for performance reasons.

void

setBackground

​(

Color

c)

Overrides

JComponent.setBackground

to assign
the unselected-background color to the specified color.

void

setForeground

​(

Color

c)

Overrides

JComponent.setForeground

to assign
the unselected-foreground color to the specified color.

protected void

setValue

​(

Object

value)

Sets the

String

object for the cell being rendered to

value

.

void

updateUI

()

Notification from the

UIManager

that the look and feel
[L&F] has changed.

void

validate

()

Overridden for performance reasons.

- Methods declared in class javax.swing.

JLabel

checkHorizontalKey

,

checkVerticalKey

,

getAccessibleContext

,

getDisabledIcon

,

getDisplayedMnemonic

,

getDisplayedMnemonicIndex

,

getHorizontalAlignment

,

getHorizontalTextPosition

,

getIcon

,

getIconTextGap

,

getLabelFor

,

getText

,

getUI

,

getUIClassID

,

getVerticalAlignment

,

getVerticalTextPosition

,

imageUpdate

,

paramString

,

setDisabledIcon

,

setDisplayedMnemonic

,

setDisplayedMnemonic

,

setDisplayedMnemonicIndex

,

setHorizontalAlignment

,

setHorizontalTextPosition

,

setIcon

,

setIconTextGap

,

setLabelFor

,

setText

,

setUI

,

setVerticalAlignment

,

setVerticalTextPosition

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

Overridden for performance reasons.

Returns the default table cell renderer.

Overrides

JComponent.setBackground

to assign
the unselected-background color to the specified color.

Overrides

JComponent.setForeground

to assign
the unselected-foreground color to the specified color.

Sets the

String

object for the cell being rendered to

value

.

Notification from the

UIManager

that the look and feel
[L&F] has changed.

Methods declared in class javax.swing.

JLabel

checkHorizontalKey

,

checkVerticalKey

,

getAccessibleContext

,

getDisabledIcon

,

getDisplayedMnemonic

,

getDisplayedMnemonicIndex

,

getHorizontalAlignment

,

getHorizontalTextPosition

,

getIcon

,

getIconTextGap

,

getLabelFor

,

getText

,

getUI

,

getUIClassID

,

getVerticalAlignment

,

getVerticalTextPosition

,

imageUpdate

,

paramString

,

setDisabledIcon

,

setDisplayedMnemonic

,

setDisplayedMnemonic

,

setDisplayedMnemonicIndex

,

setHorizontalAlignment

,

setHorizontalTextPosition

,

setIcon

,

setIconTextGap

,

setLabelFor

,

setText

,

setUI

,

setVerticalAlignment

,

setVerticalTextPosition

---

#### Methods declared in class javax.swing. JLabel

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

- noFocusBorder

```java
protected static
Border
noFocusBorder
```

A border without focus.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultTableCellRenderer

```java
public DefaultTableCellRenderer()
```

Creates a default table cell renderer.

============ METHOD DETAIL ==========

- Method Detail

- setForeground

```java
public void setForeground​(
Color
c)
```

Overrides

JComponent.setForeground

to assign
the unselected-foreground color to the specified color.

**Overrides:** setForeground

in class

JComponent
**Parameters:** c

- set the foreground color to this value
**See Also:** Component.getForeground()

- setBackground

```java
public void setBackground​(
Color
c)
```

Overrides

JComponent.setBackground

to assign
the unselected-background color to the specified color.

**Overrides:** setBackground

in class

JComponent
**Parameters:** c

- set the background color to this value
**See Also:** Component.getBackground()

,

JComponent.setOpaque(boolean)

- updateUI

```java
public void updateUI()
```

Notification from the

UIManager

that the look and feel
[L&F] has changed.
Replaces the current UI object with the latest version from the

UIManager

.

**Overrides:** updateUI

in class

JLabel
**See Also:** JComponent.updateUI()

- getTableCellRendererComponent

```java
public
Component
getTableCellRendererComponent​(
JTable
table,

Object
value,
boolean isSelected,
boolean hasFocus,
int row,
int column)
```

Returns the default table cell renderer.

During a printing operation, this method will be called with

isSelected

and

hasFocus

values of

false

to prevent selection and focus from appearing
in the printed output. To do other customization based on whether
or not the table is being printed, check the return value from

JComponent.isPaintingForPrint()

.

**Specified by:** getTableCellRendererComponent

in interface

TableCellRenderer
**Parameters:** table

- the

JTable
**Parameters:** value

- the value to assign to the cell at

[row, column]
**Parameters:** isSelected

- true if cell is selected
**Parameters:** hasFocus

- true if cell has focus
**Parameters:** row

- the row of the cell to render
**Parameters:** column

- the column of the cell to render
**Returns:** the default table cell renderer
**See Also:** JComponent.isPaintingForPrint()

- isOpaque

```java
public boolean isOpaque()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** isOpaque

in class

JComponent
**Returns:** true if this component is completely opaque
**See Also:** JComponent.setOpaque(boolean)

- invalidate

```java
public void invalidate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** invalidate

in class

Container
**Since:** 1.5
**See Also:** Container.validate()

,

Container.layout()

,

LayoutManager2

- validate

```java
public void validate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** validate

in class

Container
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.isValidateRoot()

,

JComponent.revalidate()

,

Container.validateTree()

- revalidate

```java
public void revalidate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** revalidate

in class

JComponent
**See Also:** Component.invalidate()

,

Container.validate()

,

JComponent.isValidateRoot()

,

RepaintManager.addInvalidComponent(javax.swing.JComponent)

- repaint

```java
public void repaint​(long tm,
int x,
int y,
int width,
int height)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

JComponent
**Parameters:** tm

- this parameter is not used
**Parameters:** x

- the x value of the dirty region
**Parameters:** y

- the y value of the dirty region
**Parameters:** width

- the width of the dirty region
**Parameters:** height

- the height of the dirty region
**See Also:** JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

- repaint

```java
public void repaint​(
Rectangle
r)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

JComponent
**Parameters:** r

- a

Rectangle

containing the dirty region
**See Also:** JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

- repaint

```java
public void repaint()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

Component
**Since:** 1.5
**See Also:** Component.update(Graphics)

- firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
boolean oldValue,
boolean newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

JComponent
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

- setValue

```java
protected void setValue​(
Object
value)
```

Sets the

String

object for the cell being rendered to

value

.

**Parameters:** value

- the string value for this cell; if value is

null

it sets the text value to an empty string
**See Also:** JLabel.setText(java.lang.String)

Field Detail

- noFocusBorder

```java
protected static
Border
noFocusBorder
```

A border without focus.

---

#### Field Detail

noFocusBorder

```java
protected static
Border
noFocusBorder
```

A border without focus.

---

#### noFocusBorder

protected static

Border

noFocusBorder

A border without focus.

Constructor Detail

- DefaultTableCellRenderer

```java
public DefaultTableCellRenderer()
```

Creates a default table cell renderer.

---

#### Constructor Detail

DefaultTableCellRenderer

```java
public DefaultTableCellRenderer()
```

Creates a default table cell renderer.

---

#### DefaultTableCellRenderer

public DefaultTableCellRenderer()

Creates a default table cell renderer.

Method Detail

- setForeground

```java
public void setForeground​(
Color
c)
```

Overrides

JComponent.setForeground

to assign
the unselected-foreground color to the specified color.

**Overrides:** setForeground

in class

JComponent
**Parameters:** c

- set the foreground color to this value
**See Also:** Component.getForeground()

- setBackground

```java
public void setBackground​(
Color
c)
```

Overrides

JComponent.setBackground

to assign
the unselected-background color to the specified color.

**Overrides:** setBackground

in class

JComponent
**Parameters:** c

- set the background color to this value
**See Also:** Component.getBackground()

,

JComponent.setOpaque(boolean)

- updateUI

```java
public void updateUI()
```

Notification from the

UIManager

that the look and feel
[L&F] has changed.
Replaces the current UI object with the latest version from the

UIManager

.

**Overrides:** updateUI

in class

JLabel
**See Also:** JComponent.updateUI()

- getTableCellRendererComponent

```java
public
Component
getTableCellRendererComponent​(
JTable
table,

Object
value,
boolean isSelected,
boolean hasFocus,
int row,
int column)
```

Returns the default table cell renderer.

During a printing operation, this method will be called with

isSelected

and

hasFocus

values of

false

to prevent selection and focus from appearing
in the printed output. To do other customization based on whether
or not the table is being printed, check the return value from

JComponent.isPaintingForPrint()

.

**Specified by:** getTableCellRendererComponent

in interface

TableCellRenderer
**Parameters:** table

- the

JTable
**Parameters:** value

- the value to assign to the cell at

[row, column]
**Parameters:** isSelected

- true if cell is selected
**Parameters:** hasFocus

- true if cell has focus
**Parameters:** row

- the row of the cell to render
**Parameters:** column

- the column of the cell to render
**Returns:** the default table cell renderer
**See Also:** JComponent.isPaintingForPrint()

- isOpaque

```java
public boolean isOpaque()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** isOpaque

in class

JComponent
**Returns:** true if this component is completely opaque
**See Also:** JComponent.setOpaque(boolean)

- invalidate

```java
public void invalidate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** invalidate

in class

Container
**Since:** 1.5
**See Also:** Container.validate()

,

Container.layout()

,

LayoutManager2

- validate

```java
public void validate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** validate

in class

Container
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.isValidateRoot()

,

JComponent.revalidate()

,

Container.validateTree()

- revalidate

```java
public void revalidate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** revalidate

in class

JComponent
**See Also:** Component.invalidate()

,

Container.validate()

,

JComponent.isValidateRoot()

,

RepaintManager.addInvalidComponent(javax.swing.JComponent)

- repaint

```java
public void repaint​(long tm,
int x,
int y,
int width,
int height)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

JComponent
**Parameters:** tm

- this parameter is not used
**Parameters:** x

- the x value of the dirty region
**Parameters:** y

- the y value of the dirty region
**Parameters:** width

- the width of the dirty region
**Parameters:** height

- the height of the dirty region
**See Also:** JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

- repaint

```java
public void repaint​(
Rectangle
r)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

JComponent
**Parameters:** r

- a

Rectangle

containing the dirty region
**See Also:** JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

- repaint

```java
public void repaint()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

Component
**Since:** 1.5
**See Also:** Component.update(Graphics)

- firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

- firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
boolean oldValue,
boolean newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

JComponent
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

- setValue

```java
protected void setValue​(
Object
value)
```

Sets the

String

object for the cell being rendered to

value

.

**Parameters:** value

- the string value for this cell; if value is

null

it sets the text value to an empty string
**See Also:** JLabel.setText(java.lang.String)

---

#### Method Detail

setForeground

```java
public void setForeground​(
Color
c)
```

Overrides

JComponent.setForeground

to assign
the unselected-foreground color to the specified color.

**Overrides:** setForeground

in class

JComponent
**Parameters:** c

- set the foreground color to this value
**See Also:** Component.getForeground()

---

#### setForeground

public void setForeground​(

Color

c)

Overrides

JComponent.setForeground

to assign
the unselected-foreground color to the specified color.

setBackground

```java
public void setBackground​(
Color
c)
```

Overrides

JComponent.setBackground

to assign
the unselected-background color to the specified color.

**Overrides:** setBackground

in class

JComponent
**Parameters:** c

- set the background color to this value
**See Also:** Component.getBackground()

,

JComponent.setOpaque(boolean)

---

#### setBackground

public void setBackground​(

Color

c)

Overrides

JComponent.setBackground

to assign
the unselected-background color to the specified color.

updateUI

```java
public void updateUI()
```

Notification from the

UIManager

that the look and feel
[L&F] has changed.
Replaces the current UI object with the latest version from the

UIManager

.

**Overrides:** updateUI

in class

JLabel
**See Also:** JComponent.updateUI()

---

#### updateUI

public void updateUI()

Notification from the

UIManager

that the look and feel
[L&F] has changed.
Replaces the current UI object with the latest version from the

UIManager

.

getTableCellRendererComponent

```java
public
Component
getTableCellRendererComponent​(
JTable
table,

Object
value,
boolean isSelected,
boolean hasFocus,
int row,
int column)
```

Returns the default table cell renderer.

During a printing operation, this method will be called with

isSelected

and

hasFocus

values of

false

to prevent selection and focus from appearing
in the printed output. To do other customization based on whether
or not the table is being printed, check the return value from

JComponent.isPaintingForPrint()

.

**Specified by:** getTableCellRendererComponent

in interface

TableCellRenderer
**Parameters:** table

- the

JTable
**Parameters:** value

- the value to assign to the cell at

[row, column]
**Parameters:** isSelected

- true if cell is selected
**Parameters:** hasFocus

- true if cell has focus
**Parameters:** row

- the row of the cell to render
**Parameters:** column

- the column of the cell to render
**Returns:** the default table cell renderer
**See Also:** JComponent.isPaintingForPrint()

---

#### getTableCellRendererComponent

public

Component

getTableCellRendererComponent​(

JTable

table,

Object

value,
boolean isSelected,
boolean hasFocus,
int row,
int column)

Returns the default table cell renderer.

During a printing operation, this method will be called with

isSelected

and

hasFocus

values of

false

to prevent selection and focus from appearing
in the printed output. To do other customization based on whether
or not the table is being printed, check the return value from

JComponent.isPaintingForPrint()

.

During a printing operation, this method will be called with

isSelected

and

hasFocus

values of

false

to prevent selection and focus from appearing
in the printed output. To do other customization based on whether
or not the table is being printed, check the return value from

JComponent.isPaintingForPrint()

.

isOpaque

```java
public boolean isOpaque()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** isOpaque

in class

JComponent
**Returns:** true if this component is completely opaque
**See Also:** JComponent.setOpaque(boolean)

---

#### isOpaque

public boolean isOpaque()

Overridden for performance reasons.
See the

Implementation Note

for more information.

invalidate

```java
public void invalidate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** invalidate

in class

Container
**Since:** 1.5
**See Also:** Container.validate()

,

Container.layout()

,

LayoutManager2

---

#### invalidate

public void invalidate()

Overridden for performance reasons.
See the

Implementation Note

for more information.

validate

```java
public void validate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** validate

in class

Container
**See Also:** Container.add(java.awt.Component)

,

Container.invalidate()

,

Container.isValidateRoot()

,

JComponent.revalidate()

,

Container.validateTree()

---

#### validate

public void validate()

Overridden for performance reasons.
See the

Implementation Note

for more information.

revalidate

```java
public void revalidate()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** revalidate

in class

JComponent
**See Also:** Component.invalidate()

,

Container.validate()

,

JComponent.isValidateRoot()

,

RepaintManager.addInvalidComponent(javax.swing.JComponent)

---

#### revalidate

public void revalidate()

Overridden for performance reasons.
See the

Implementation Note

for more information.

repaint

```java
public void repaint​(long tm,
int x,
int y,
int width,
int height)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

JComponent
**Parameters:** tm

- this parameter is not used
**Parameters:** x

- the x value of the dirty region
**Parameters:** y

- the y value of the dirty region
**Parameters:** width

- the width of the dirty region
**Parameters:** height

- the height of the dirty region
**See Also:** JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

---

#### repaint

public void repaint​(long tm,
int x,
int y,
int width,
int height)

Overridden for performance reasons.
See the

Implementation Note

for more information.

repaint

```java
public void repaint​(
Rectangle
r)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

JComponent
**Parameters:** r

- a

Rectangle

containing the dirty region
**See Also:** JComponent.isPaintingOrigin()

,

Component.isShowing()

,

RepaintManager.addDirtyRegion(javax.swing.JComponent, int, int, int, int)

---

#### repaint

public void repaint​(

Rectangle

r)

Overridden for performance reasons.
See the

Implementation Note

for more information.

repaint

```java
public void repaint()
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** repaint

in class

Component
**Since:** 1.5
**See Also:** Component.update(Graphics)

---

#### repaint

public void repaint()

Overridden for performance reasons.
See the

Implementation Note

for more information.

firePropertyChange

```java
protected void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

Component
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

---

#### firePropertyChange

protected void firePropertyChange​(

String

propertyName,

Object

oldValue,

Object

newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

firePropertyChange

```java
public void firePropertyChange​(
String
propertyName,
boolean oldValue,
boolean newValue)
```

Overridden for performance reasons.
See the

Implementation Note

for more information.

**Overrides:** firePropertyChange

in class

JComponent
**Parameters:** propertyName

- the property whose value has changed
**Parameters:** oldValue

- the property's previous value
**Parameters:** newValue

- the property's new value

---

#### firePropertyChange

public void firePropertyChange​(

String

propertyName,
boolean oldValue,
boolean newValue)

Overridden for performance reasons.
See the

Implementation Note

for more information.

setValue

```java
protected void setValue​(
Object
value)
```

Sets the

String

object for the cell being rendered to

value

.

**Parameters:** value

- the string value for this cell; if value is

null

it sets the text value to an empty string
**See Also:** JLabel.setText(java.lang.String)

---

#### setValue

protected void setValue​(

Object

value)

Sets the

String

object for the cell being rendered to

value

.

---

