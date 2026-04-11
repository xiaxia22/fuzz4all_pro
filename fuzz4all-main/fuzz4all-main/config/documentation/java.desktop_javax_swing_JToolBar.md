# Class JToolBar

**Source:** `java.desktop\javax\swing\JToolBar.html`

### Class Description

```java
@JavaBean
(
defaultProperty
="UI",

description
="A component which displays commonly used controls or Actions.")
public class
JToolBar

extends
JComponent

implements
SwingConstants
,
Accessible
```

JToolBar

provides a component that is useful for
displaying commonly used

Action

s or controls.
For examples and information on using tool bars see

How to Use Tool Bars

,
a section in

The Java Tutorial

.

With most look and feels,
the user can drag out a tool bar into a separate window
(unless the

floatable

property is set to

false

).
For drag-out to work correctly, it is recommended that you add

JToolBar

instances to one of the four "sides" of a
container whose layout manager is a

BorderLayout

,
and do not add children to any of the other four "sides".

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

SwingConstants

---

### Field Details

*No entries found.*

### Constructor Details

#### public JToolBar()

Creates a new tool bar; orientation defaults to

HORIZONTAL

.

---

#### public JToolBar​(int orientation)

Creates a new tool bar with the specified

orientation

.
The

orientation

must be either

HORIZONTAL

or

VERTICAL

.

**Parameters:**
- orientation

- the orientation desired

---

#### public JToolBar​(
String
name)

Creates a new tool bar with the specified

name

. The
name is used as the title of the undocked tool bar. The default
orientation is

HORIZONTAL

.

**Parameters:**
- name

- the name of the tool bar

**Since:**
- 1.3

---

#### public JToolBar​(
String
name,
int orientation)

Creates a new tool bar with a specified

name

and

orientation

.
All other constructors call this constructor.
If

orientation

is an invalid value, an exception will
be thrown.

**Parameters:**
- name

- the name of the tool bar
- orientation

- the initial orientation -- it must be
either

HORIZONTAL

or

VERTICAL

**Throws:**
- IllegalArgumentException

- if orientation is neither

HORIZONTAL

nor

VERTICAL

**Since:**
- 1.3

---

### Method Details

#### public
ToolBarUI
getUI()

Returns the tool bar's current UI.

**Overrides:**
- getUI

in class

JComponent

**Returns:**
- the tool bar's current UI.

**See Also:**
- setUI(javax.swing.plaf.ToolBarUI)

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
ToolBarUI
ui)

Sets the L&F object that renders this component.

**Parameters:**
- ui

- the

ToolBarUI

L&F object

**See Also:**
- UIDefaults.getUI(javax.swing.JComponent)

---

#### public void updateUI()

Notification from the

UIFactory

that the L&F has changed.
Called to replace the UI with the latest version from the

UIFactory

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
- the string "ToolBarUI"

**See Also:**
- JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### public int getComponentIndex​(
Component
c)

Returns the index of the specified component.
(Note: Separators occupy index positions.)

**Parameters:**
- c

- the

Component

to find

**Returns:**
- an integer indicating the component's position,
where 0 is first

---

#### public
Component
getComponentAtIndex​(int i)

Returns the component at the specified index.

**Parameters:**
- i

- the component's position, where 0 is first

**Returns:**
- the

Component

at that position,
or

null

for an invalid index

---

#### @BeanProperty
(
expert
=true,

description
="The margin between the tool bar\'s border and contents")
public void setMargin​(
Insets
m)

Sets the margin between the tool bar's border and
its buttons. Setting to

null

causes the tool bar to
use the default margins. The tool bar's default

Border

object uses this value to create the proper margin.
However, if a non-default border is set on the tool bar,
it is that

Border

object's responsibility to create the
appropriate margin space (otherwise this property will
effectively be ignored).

**Parameters:**
- m

- an

Insets

object that defines the space
between the border and the buttons

**See Also:**
- Insets

---

#### public
Insets
getMargin()

Returns the margin between the tool bar's border and
its buttons.

**Returns:**
- an

Insets

object containing the margin values

**See Also:**
- Insets

---

#### public boolean isBorderPainted()

Gets the

borderPainted

property.

**Returns:**
- the value of the

borderPainted

property

**See Also:**
- setBorderPainted(boolean)

---

#### @BeanProperty
(
expert
=true,

description
="Does the tool bar paint its borders?")
public void setBorderPainted​(boolean b)

Sets the

borderPainted

property, which is

true

if the border should be painted.
The default value for this property is

true

.
Some look and feels might not implement painted borders;
they will ignore this property.

**Parameters:**
- b

- if true, the border is painted

**See Also:**
- isBorderPainted()

---

#### protected void paintBorder​(
Graphics
g)

Paints the tool bar's border if the

borderPainted

property
is

true

.

**Overrides:**
- paintBorder

in class

JComponent

**Parameters:**
- g

- the

Graphics

context in which the painting
is done

**See Also:**
- JComponent.paint(java.awt.Graphics)

,

JComponent.setBorder(javax.swing.border.Border)

---

#### public boolean isFloatable()

Gets the

floatable

property.

**Returns:**
- the value of the

floatable

property

**See Also:**
- setFloatable(boolean)

---

#### @BeanProperty
(
preferred
=true,

description
="Can the tool bar be made to float by the user?")
public void setFloatable​(boolean b)

Sets the

floatable

property,
which must be

true

for the user to move the tool bar.
Typically, a floatable tool bar can be
dragged into a different position within the same container
or out into its own window.
The default value of this property is

true

.
Some look and feels might not implement floatable tool bars;
they will ignore this property.

**Parameters:**
- b

- if

true

, the tool bar can be moved;

false

otherwise

**See Also:**
- isFloatable()

---

#### public int getOrientation()

Returns the current orientation of the tool bar. The value is either

HORIZONTAL

or

VERTICAL

.

**Returns:**
- an integer representing the current orientation -- either

HORIZONTAL

or

VERTICAL

**See Also:**
- setOrientation(int)

---

#### @BeanProperty
(
preferred
=true,

enumerationValues
={"SwingConstants.HORIZONTAL","SwingConstants.VERTICAL"},

description
="The current orientation of the tool bar")
public void setOrientation​(int o)

Sets the orientation of the tool bar. The orientation must have
either the value

HORIZONTAL

or

VERTICAL

.
If

orientation

is
an invalid value, an exception will be thrown.

**Parameters:**
- o

- the new orientation -- either

HORIZONTAL

or

VERTICAL

**Throws:**
- IllegalArgumentException

- if orientation is neither

HORIZONTAL

nor

VERTICAL

**See Also:**
- getOrientation()

---

#### @BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="Will draw rollover button borders in the toolbar.")
public void setRollover​(boolean rollover)

Sets the rollover state of this toolbar. If the rollover state is true
then the border of the toolbar buttons will be drawn only when the
mouse pointer hovers over them. The default value of this property
is false.

The implementation of a look and feel may choose to ignore this
property.

**Parameters:**
- rollover

- true for rollover toolbar buttons; otherwise false

**Since:**
- 1.4

---

#### public boolean isRollover()

Returns the rollover state.

**Returns:**
- true if rollover toolbar buttons are to be drawn; otherwise false

**See Also:**
- setRollover(boolean)

**Since:**
- 1.4

---

#### public void addSeparator()

Appends a separator of default size to the end of the tool bar.
The default size is determined by the current look and feel.

---

#### public void addSeparator​(
Dimension
size)

Appends a separator of a specified size to the end
of the tool bar.

**Parameters:**
- size

- the

Dimension

of the separator

---

#### public
JButton
add​(
Action
a)

Adds a new

JButton

which dispatches the action.

**Parameters:**
- a

- the

Action

object to add as a new menu item

**Returns:**
- the new button which dispatches the action

---

#### protected
JButton
createActionComponent​(
Action
a)

Factory method which creates the

JButton

for

Action

s added to the

JToolBar

.
The default name is empty if a

null

action is passed.

**Parameters:**
- a

- the

Action

for the button to be added

**Returns:**
- the newly created button

**See Also:**
- Action

**Since:**
- 1.3

---

#### protected
PropertyChangeListener
createActionChangeListener​(
JButton
b)

Returns a properly configured

PropertyChangeListener

which updates the control as changes to the

Action

occur,
or

null

if the default
property change listener for the control is desired.

**Parameters:**
- b

- a

JButton

**Returns:**
- null

---

#### protected void addImpl​(
Component
comp,

Object
constraints,
int index)

If a

JButton

is being added, it is initially
set to be disabled.

**Overrides:**
- addImpl

in class

Container

**Parameters:**
- comp

- the component to be enhanced
- constraints

- the constraints to be enforced on the component
- index

- the index of the component

**See Also:**
- Container.add(Component)

,

Container.add(Component, int)

,

Container.add(Component, java.lang.Object)

,

Container.invalidate()

,

LayoutManager

,

LayoutManager2

---

#### protected
String
paramString()

Returns a string representation of this

JToolBar

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

JToolBar

.

---

#### @BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this JToolBar.
For tool bars, the AccessibleContext takes the form of an
AccessibleJToolBar.
A new AccessibleJToolBar instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- an AccessibleJToolBar that serves as the
AccessibleContext of this JToolBar

---

### Additional Sections

#### Class JToolBar

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JToolBar

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JToolBar

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JToolBar

javax.swing.JComponent

- javax.swing.JToolBar

javax.swing.JToolBar

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

,

SwingConstants

```java
@JavaBean
(
defaultProperty
="UI",

description
="A component which displays commonly used controls or Actions.")
public class
JToolBar

extends
JComponent

implements
SwingConstants
,
Accessible
```

JToolBar

provides a component that is useful for
displaying commonly used

Action

s or controls.
For examples and information on using tool bars see

How to Use Tool Bars

,
a section in

The Java Tutorial

.

With most look and feels,
the user can drag out a tool bar into a separate window
(unless the

floatable

property is set to

false

).
For drag-out to work correctly, it is recommended that you add

JToolBar

instances to one of the four "sides" of a
container whose layout manager is a

BorderLayout

,
and do not add children to any of the other four "sides".

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
**See Also:** Action

,

Serialized Form

@JavaBean

(

defaultProperty

="UI",

description

="A component which displays commonly used controls or Actions.")
public class

JToolBar

extends

JComponent

implements

SwingConstants

,

Accessible

JToolBar

provides a component that is useful for
displaying commonly used

Action

s or controls.
For examples and information on using tool bars see

How to Use Tool Bars

,
a section in

The Java Tutorial

.

With most look and feels,
the user can drag out a tool bar into a separate window
(unless the

floatable

property is set to

false

).
For drag-out to work correctly, it is recommended that you add

JToolBar

instances to one of the four "sides" of a
container whose layout manager is a

BorderLayout

,
and do not add children to any of the other four "sides".

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

With most look and feels,
the user can drag out a tool bar into a separate window
(unless the

floatable

property is set to

false

).
For drag-out to work correctly, it is recommended that you add

JToolBar

instances to one of the four "sides" of a
container whose layout manager is a

BorderLayout

,
and do not add children to any of the other four "sides".

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

JToolBar.AccessibleJToolBar

This class implements accessibility support for the

JToolBar

class.

static class

JToolBar.Separator

A toolbar-specific separator.

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

JToolBar

()

Creates a new tool bar; orientation defaults to

HORIZONTAL

.

JToolBar

​(int orientation)

Creates a new tool bar with the specified

orientation

.

JToolBar

​(

String

name)

Creates a new tool bar with the specified

name

.

JToolBar

​(

String

name,
int orientation)

Creates a new tool bar with a specified

name

and

orientation

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JButton

add

​(

Action

a)

Adds a new

JButton

which dispatches the action.

protected void

addImpl

​(

Component

comp,

Object

constraints,
int index)

If a

JButton

is being added, it is initially
set to be disabled.

void

addSeparator

()

Appends a separator of default size to the end of the tool bar.

void

addSeparator

​(

Dimension

size)

Appends a separator of a specified size to the end
of the tool bar.

protected

PropertyChangeListener

createActionChangeListener

​(

JButton

b)

Returns a properly configured

PropertyChangeListener

which updates the control as changes to the

Action

occur,
or

null

if the default
property change listener for the control is desired.

protected

JButton

createActionComponent

​(

Action

a)

Factory method which creates the

JButton

for

Action

s added to the

JToolBar

.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JToolBar.

Component

getComponentAtIndex

​(int i)

Returns the component at the specified index.

int

getComponentIndex

​(

Component

c)

Returns the index of the specified component.

Insets

getMargin

()

Returns the margin between the tool bar's border and
its buttons.

int

getOrientation

()

Returns the current orientation of the tool bar.

ToolBarUI

getUI

()

Returns the tool bar's current UI.

String

getUIClassID

()

Returns the name of the L&F class that renders this component.

boolean

isBorderPainted

()

Gets the

borderPainted

property.

boolean

isFloatable

()

Gets the

floatable

property.

boolean

isRollover

()

Returns the rollover state.

protected void

paintBorder

​(

Graphics

g)

Paints the tool bar's border if the

borderPainted

property
is

true

.

protected

String

paramString

()

Returns a string representation of this

JToolBar

.

void

setBorderPainted

​(boolean b)

Sets the

borderPainted

property, which is

true

if the border should be painted.

void

setFloatable

​(boolean b)

Sets the

floatable

property,
which must be

true

for the user to move the tool bar.

void

setMargin

​(

Insets

m)

Sets the margin between the tool bar's border and
its buttons.

void

setOrientation

​(int o)

Sets the orientation of the tool bar.

void

setRollover

​(boolean rollover)

Sets the rollover state of this toolbar.

void

setUI

​(

ToolBarUI

ui)

Sets the L&F object that renders this component.

void

updateUI

()

Notification from the

UIFactory

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

JToolBar.AccessibleJToolBar

This class implements accessibility support for the

JToolBar

class.

static class

JToolBar.Separator

A toolbar-specific separator.

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

JToolBar

class.

A toolbar-specific separator.

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

JToolBar

()

Creates a new tool bar; orientation defaults to

HORIZONTAL

.

JToolBar

​(int orientation)

Creates a new tool bar with the specified

orientation

.

JToolBar

​(

String

name)

Creates a new tool bar with the specified

name

.

JToolBar

​(

String

name,
int orientation)

Creates a new tool bar with a specified

name

and

orientation

.

---

#### Constructor Summary

Creates a new tool bar; orientation defaults to

HORIZONTAL

.

Creates a new tool bar with the specified

orientation

.

Creates a new tool bar with the specified

name

.

Creates a new tool bar with a specified

name

and

orientation

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JButton

add

​(

Action

a)

Adds a new

JButton

which dispatches the action.

protected void

addImpl

​(

Component

comp,

Object

constraints,
int index)

If a

JButton

is being added, it is initially
set to be disabled.

void

addSeparator

()

Appends a separator of default size to the end of the tool bar.

void

addSeparator

​(

Dimension

size)

Appends a separator of a specified size to the end
of the tool bar.

protected

PropertyChangeListener

createActionChangeListener

​(

JButton

b)

Returns a properly configured

PropertyChangeListener

which updates the control as changes to the

Action

occur,
or

null

if the default
property change listener for the control is desired.

protected

JButton

createActionComponent

​(

Action

a)

Factory method which creates the

JButton

for

Action

s added to the

JToolBar

.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JToolBar.

Component

getComponentAtIndex

​(int i)

Returns the component at the specified index.

int

getComponentIndex

​(

Component

c)

Returns the index of the specified component.

Insets

getMargin

()

Returns the margin between the tool bar's border and
its buttons.

int

getOrientation

()

Returns the current orientation of the tool bar.

ToolBarUI

getUI

()

Returns the tool bar's current UI.

String

getUIClassID

()

Returns the name of the L&F class that renders this component.

boolean

isBorderPainted

()

Gets the

borderPainted

property.

boolean

isFloatable

()

Gets the

floatable

property.

boolean

isRollover

()

Returns the rollover state.

protected void

paintBorder

​(

Graphics

g)

Paints the tool bar's border if the

borderPainted

property
is

true

.

protected

String

paramString

()

Returns a string representation of this

JToolBar

.

void

setBorderPainted

​(boolean b)

Sets the

borderPainted

property, which is

true

if the border should be painted.

void

setFloatable

​(boolean b)

Sets the

floatable

property,
which must be

true

for the user to move the tool bar.

void

setMargin

​(

Insets

m)

Sets the margin between the tool bar's border and
its buttons.

void

setOrientation

​(int o)

Sets the orientation of the tool bar.

void

setRollover

​(boolean rollover)

Sets the rollover state of this toolbar.

void

setUI

​(

ToolBarUI

ui)

Sets the L&F object that renders this component.

void

updateUI

()

Notification from the

UIFactory

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

Adds a new

JButton

which dispatches the action.

If a

JButton

is being added, it is initially
set to be disabled.

Appends a separator of default size to the end of the tool bar.

Appends a separator of a specified size to the end
of the tool bar.

Returns a properly configured

PropertyChangeListener

which updates the control as changes to the

Action

occur,
or

null

if the default
property change listener for the control is desired.

Factory method which creates the

JButton

for

Action

s added to the

JToolBar

.

Gets the AccessibleContext associated with this JToolBar.

Returns the component at the specified index.

Returns the index of the specified component.

Returns the margin between the tool bar's border and
its buttons.

Returns the current orientation of the tool bar.

Returns the tool bar's current UI.

Returns the name of the L&F class that renders this component.

Gets the

borderPainted

property.

Gets the

floatable

property.

Returns the rollover state.

Paints the tool bar's border if the

borderPainted

property
is

true

.

Returns a string representation of this

JToolBar

.

Sets the

borderPainted

property, which is

true

if the border should be painted.

Sets the

floatable

property,
which must be

true

for the user to move the tool bar.

Sets the margin between the tool bar's border and
its buttons.

Sets the orientation of the tool bar.

Sets the rollover state of this toolbar.

Sets the L&F object that renders this component.

Notification from the

UIFactory

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JToolBar

```java
public JToolBar()
```

Creates a new tool bar; orientation defaults to

HORIZONTAL

.

- JToolBar

```java
public JToolBar​(int orientation)
```

Creates a new tool bar with the specified

orientation

.
The

orientation

must be either

HORIZONTAL

or

VERTICAL

.

**Parameters:** orientation

- the orientation desired

- JToolBar

```java
public JToolBar​(
String
name)
```

Creates a new tool bar with the specified

name

. The
name is used as the title of the undocked tool bar. The default
orientation is

HORIZONTAL

.

**Parameters:** name

- the name of the tool bar
**Since:** 1.3

- JToolBar

```java
public JToolBar​(
String
name,
int orientation)
```

Creates a new tool bar with a specified

name

and

orientation

.
All other constructors call this constructor.
If

orientation

is an invalid value, an exception will
be thrown.

**Parameters:** name

- the name of the tool bar
**Parameters:** orientation

- the initial orientation -- it must be
either

HORIZONTAL

or

VERTICAL
**Throws:** IllegalArgumentException

- if orientation is neither

HORIZONTAL

nor

VERTICAL
**Since:** 1.3

============ METHOD DETAIL ==========

- Method Detail

- getUI

```java
public
ToolBarUI
getUI()
```

Returns the tool bar's current UI.

**Overrides:** getUI

in class

JComponent
**Returns:** the tool bar's current UI.
**See Also:** setUI(javax.swing.plaf.ToolBarUI)

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
ToolBarUI
ui)
```

Sets the L&F object that renders this component.

**Parameters:** ui

- the

ToolBarUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

- updateUI

```java
public void updateUI()
```

Notification from the

UIFactory

that the L&F has changed.
Called to replace the UI with the latest version from the

UIFactory

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
**Returns:** the string "ToolBarUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- getComponentIndex

```java
public int getComponentIndex​(
Component
c)
```

Returns the index of the specified component.
(Note: Separators occupy index positions.)

**Parameters:** c

- the

Component

to find
**Returns:** an integer indicating the component's position,
where 0 is first

- getComponentAtIndex

```java
public
Component
getComponentAtIndex​(int i)
```

Returns the component at the specified index.

**Parameters:** i

- the component's position, where 0 is first
**Returns:** the

Component

at that position,
or

null

for an invalid index

- setMargin

```java
@BeanProperty
(
expert
=true,

description
="The margin between the tool bar\'s border and contents")
public void setMargin​(
Insets
m)
```

Sets the margin between the tool bar's border and
its buttons. Setting to

null

causes the tool bar to
use the default margins. The tool bar's default

Border

object uses this value to create the proper margin.
However, if a non-default border is set on the tool bar,
it is that

Border

object's responsibility to create the
appropriate margin space (otherwise this property will
effectively be ignored).

**Parameters:** m

- an

Insets

object that defines the space
between the border and the buttons
**See Also:** Insets

- getMargin

```java
public
Insets
getMargin()
```

Returns the margin between the tool bar's border and
its buttons.

**Returns:** an

Insets

object containing the margin values
**See Also:** Insets

- isBorderPainted

```java
public boolean isBorderPainted()
```

Gets the

borderPainted

property.

**Returns:** the value of the

borderPainted

property
**See Also:** setBorderPainted(boolean)

- setBorderPainted

```java
@BeanProperty
(
expert
=true,

description
="Does the tool bar paint its borders?")
public void setBorderPainted​(boolean b)
```

Sets the

borderPainted

property, which is

true

if the border should be painted.
The default value for this property is

true

.
Some look and feels might not implement painted borders;
they will ignore this property.

**Parameters:** b

- if true, the border is painted
**See Also:** isBorderPainted()

- paintBorder

```java
protected void paintBorder​(
Graphics
g)
```

Paints the tool bar's border if the

borderPainted

property
is

true

.

**Overrides:** paintBorder

in class

JComponent
**Parameters:** g

- the

Graphics

context in which the painting
is done
**See Also:** JComponent.paint(java.awt.Graphics)

,

JComponent.setBorder(javax.swing.border.Border)

- isFloatable

```java
public boolean isFloatable()
```

Gets the

floatable

property.

**Returns:** the value of the

floatable

property
**See Also:** setFloatable(boolean)

- setFloatable

```java
@BeanProperty
(
preferred
=true,

description
="Can the tool bar be made to float by the user?")
public void setFloatable​(boolean b)
```

Sets the

floatable

property,
which must be

true

for the user to move the tool bar.
Typically, a floatable tool bar can be
dragged into a different position within the same container
or out into its own window.
The default value of this property is

true

.
Some look and feels might not implement floatable tool bars;
they will ignore this property.

**Parameters:** b

- if

true

, the tool bar can be moved;

false

otherwise
**See Also:** isFloatable()

- getOrientation

```java
public int getOrientation()
```

Returns the current orientation of the tool bar. The value is either

HORIZONTAL

or

VERTICAL

.

**Returns:** an integer representing the current orientation -- either

HORIZONTAL

or

VERTICAL
**See Also:** setOrientation(int)

- setOrientation

```java
@BeanProperty
(
preferred
=true,

enumerationValues
={"SwingConstants.HORIZONTAL","SwingConstants.VERTICAL"},

description
="The current orientation of the tool bar")
public void setOrientation​(int o)
```

Sets the orientation of the tool bar. The orientation must have
either the value

HORIZONTAL

or

VERTICAL

.
If

orientation

is
an invalid value, an exception will be thrown.

**Parameters:** o

- the new orientation -- either

HORIZONTAL

or

VERTICAL
**Throws:** IllegalArgumentException

- if orientation is neither

HORIZONTAL

nor

VERTICAL
**See Also:** getOrientation()

- setRollover

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="Will draw rollover button borders in the toolbar.")
public void setRollover​(boolean rollover)
```

Sets the rollover state of this toolbar. If the rollover state is true
then the border of the toolbar buttons will be drawn only when the
mouse pointer hovers over them. The default value of this property
is false.

The implementation of a look and feel may choose to ignore this
property.

**Parameters:** rollover

- true for rollover toolbar buttons; otherwise false
**Since:** 1.4

- isRollover

```java
public boolean isRollover()
```

Returns the rollover state.

**Returns:** true if rollover toolbar buttons are to be drawn; otherwise false
**Since:** 1.4
**See Also:** setRollover(boolean)

- addSeparator

```java
public void addSeparator()
```

Appends a separator of default size to the end of the tool bar.
The default size is determined by the current look and feel.

- addSeparator

```java
public void addSeparator​(
Dimension
size)
```

Appends a separator of a specified size to the end
of the tool bar.

**Parameters:** size

- the

Dimension

of the separator

- add

```java
public
JButton
add​(
Action
a)
```

Adds a new

JButton

which dispatches the action.

**Parameters:** a

- the

Action

object to add as a new menu item
**Returns:** the new button which dispatches the action

- createActionComponent

```java
protected
JButton
createActionComponent​(
Action
a)
```

Factory method which creates the

JButton

for

Action

s added to the

JToolBar

.
The default name is empty if a

null

action is passed.

**Parameters:** a

- the

Action

for the button to be added
**Returns:** the newly created button
**Since:** 1.3
**See Also:** Action

- createActionChangeListener

```java
protected
PropertyChangeListener
createActionChangeListener​(
JButton
b)
```

Returns a properly configured

PropertyChangeListener

which updates the control as changes to the

Action

occur,
or

null

if the default
property change listener for the control is desired.

**Parameters:** b

- a

JButton
**Returns:** null

- addImpl

```java
protected void addImpl​(
Component
comp,

Object
constraints,
int index)
```

If a

JButton

is being added, it is initially
set to be disabled.

**Overrides:** addImpl

in class

Container
**Parameters:** comp

- the component to be enhanced
**Parameters:** constraints

- the constraints to be enforced on the component
**Parameters:** index

- the index of the component
**See Also:** Container.add(Component)

,

Container.add(Component, int)

,

Container.add(Component, java.lang.Object)

,

Container.invalidate()

,

LayoutManager

,

LayoutManager2

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JToolBar

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

JToolBar

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

Gets the AccessibleContext associated with this JToolBar.
For tool bars, the AccessibleContext takes the form of an
AccessibleJToolBar.
A new AccessibleJToolBar instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJToolBar that serves as the
AccessibleContext of this JToolBar

Constructor Detail

- JToolBar

```java
public JToolBar()
```

Creates a new tool bar; orientation defaults to

HORIZONTAL

.

- JToolBar

```java
public JToolBar​(int orientation)
```

Creates a new tool bar with the specified

orientation

.
The

orientation

must be either

HORIZONTAL

or

VERTICAL

.

**Parameters:** orientation

- the orientation desired

- JToolBar

```java
public JToolBar​(
String
name)
```

Creates a new tool bar with the specified

name

. The
name is used as the title of the undocked tool bar. The default
orientation is

HORIZONTAL

.

**Parameters:** name

- the name of the tool bar
**Since:** 1.3

- JToolBar

```java
public JToolBar​(
String
name,
int orientation)
```

Creates a new tool bar with a specified

name

and

orientation

.
All other constructors call this constructor.
If

orientation

is an invalid value, an exception will
be thrown.

**Parameters:** name

- the name of the tool bar
**Parameters:** orientation

- the initial orientation -- it must be
either

HORIZONTAL

or

VERTICAL
**Throws:** IllegalArgumentException

- if orientation is neither

HORIZONTAL

nor

VERTICAL
**Since:** 1.3

---

#### Constructor Detail

JToolBar

```java
public JToolBar()
```

Creates a new tool bar; orientation defaults to

HORIZONTAL

.

---

#### JToolBar

public JToolBar()

Creates a new tool bar; orientation defaults to

HORIZONTAL

.

JToolBar

```java
public JToolBar​(int orientation)
```

Creates a new tool bar with the specified

orientation

.
The

orientation

must be either

HORIZONTAL

or

VERTICAL

.

**Parameters:** orientation

- the orientation desired

---

#### JToolBar

public JToolBar​(int orientation)

Creates a new tool bar with the specified

orientation

.
The

orientation

must be either

HORIZONTAL

or

VERTICAL

.

JToolBar

```java
public JToolBar​(
String
name)
```

Creates a new tool bar with the specified

name

. The
name is used as the title of the undocked tool bar. The default
orientation is

HORIZONTAL

.

**Parameters:** name

- the name of the tool bar
**Since:** 1.3

---

#### JToolBar

public JToolBar​(

String

name)

Creates a new tool bar with the specified

name

. The
name is used as the title of the undocked tool bar. The default
orientation is

HORIZONTAL

.

JToolBar

```java
public JToolBar​(
String
name,
int orientation)
```

Creates a new tool bar with a specified

name

and

orientation

.
All other constructors call this constructor.
If

orientation

is an invalid value, an exception will
be thrown.

**Parameters:** name

- the name of the tool bar
**Parameters:** orientation

- the initial orientation -- it must be
either

HORIZONTAL

or

VERTICAL
**Throws:** IllegalArgumentException

- if orientation is neither

HORIZONTAL

nor

VERTICAL
**Since:** 1.3

---

#### JToolBar

public JToolBar​(

String

name,
int orientation)

Creates a new tool bar with a specified

name

and

orientation

.
All other constructors call this constructor.
If

orientation

is an invalid value, an exception will
be thrown.

Method Detail

- getUI

```java
public
ToolBarUI
getUI()
```

Returns the tool bar's current UI.

**Overrides:** getUI

in class

JComponent
**Returns:** the tool bar's current UI.
**See Also:** setUI(javax.swing.plaf.ToolBarUI)

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
ToolBarUI
ui)
```

Sets the L&F object that renders this component.

**Parameters:** ui

- the

ToolBarUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

- updateUI

```java
public void updateUI()
```

Notification from the

UIFactory

that the L&F has changed.
Called to replace the UI with the latest version from the

UIFactory

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
**Returns:** the string "ToolBarUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- getComponentIndex

```java
public int getComponentIndex​(
Component
c)
```

Returns the index of the specified component.
(Note: Separators occupy index positions.)

**Parameters:** c

- the

Component

to find
**Returns:** an integer indicating the component's position,
where 0 is first

- getComponentAtIndex

```java
public
Component
getComponentAtIndex​(int i)
```

Returns the component at the specified index.

**Parameters:** i

- the component's position, where 0 is first
**Returns:** the

Component

at that position,
or

null

for an invalid index

- setMargin

```java
@BeanProperty
(
expert
=true,

description
="The margin between the tool bar\'s border and contents")
public void setMargin​(
Insets
m)
```

Sets the margin between the tool bar's border and
its buttons. Setting to

null

causes the tool bar to
use the default margins. The tool bar's default

Border

object uses this value to create the proper margin.
However, if a non-default border is set on the tool bar,
it is that

Border

object's responsibility to create the
appropriate margin space (otherwise this property will
effectively be ignored).

**Parameters:** m

- an

Insets

object that defines the space
between the border and the buttons
**See Also:** Insets

- getMargin

```java
public
Insets
getMargin()
```

Returns the margin between the tool bar's border and
its buttons.

**Returns:** an

Insets

object containing the margin values
**See Also:** Insets

- isBorderPainted

```java
public boolean isBorderPainted()
```

Gets the

borderPainted

property.

**Returns:** the value of the

borderPainted

property
**See Also:** setBorderPainted(boolean)

- setBorderPainted

```java
@BeanProperty
(
expert
=true,

description
="Does the tool bar paint its borders?")
public void setBorderPainted​(boolean b)
```

Sets the

borderPainted

property, which is

true

if the border should be painted.
The default value for this property is

true

.
Some look and feels might not implement painted borders;
they will ignore this property.

**Parameters:** b

- if true, the border is painted
**See Also:** isBorderPainted()

- paintBorder

```java
protected void paintBorder​(
Graphics
g)
```

Paints the tool bar's border if the

borderPainted

property
is

true

.

**Overrides:** paintBorder

in class

JComponent
**Parameters:** g

- the

Graphics

context in which the painting
is done
**See Also:** JComponent.paint(java.awt.Graphics)

,

JComponent.setBorder(javax.swing.border.Border)

- isFloatable

```java
public boolean isFloatable()
```

Gets the

floatable

property.

**Returns:** the value of the

floatable

property
**See Also:** setFloatable(boolean)

- setFloatable

```java
@BeanProperty
(
preferred
=true,

description
="Can the tool bar be made to float by the user?")
public void setFloatable​(boolean b)
```

Sets the

floatable

property,
which must be

true

for the user to move the tool bar.
Typically, a floatable tool bar can be
dragged into a different position within the same container
or out into its own window.
The default value of this property is

true

.
Some look and feels might not implement floatable tool bars;
they will ignore this property.

**Parameters:** b

- if

true

, the tool bar can be moved;

false

otherwise
**See Also:** isFloatable()

- getOrientation

```java
public int getOrientation()
```

Returns the current orientation of the tool bar. The value is either

HORIZONTAL

or

VERTICAL

.

**Returns:** an integer representing the current orientation -- either

HORIZONTAL

or

VERTICAL
**See Also:** setOrientation(int)

- setOrientation

```java
@BeanProperty
(
preferred
=true,

enumerationValues
={"SwingConstants.HORIZONTAL","SwingConstants.VERTICAL"},

description
="The current orientation of the tool bar")
public void setOrientation​(int o)
```

Sets the orientation of the tool bar. The orientation must have
either the value

HORIZONTAL

or

VERTICAL

.
If

orientation

is
an invalid value, an exception will be thrown.

**Parameters:** o

- the new orientation -- either

HORIZONTAL

or

VERTICAL
**Throws:** IllegalArgumentException

- if orientation is neither

HORIZONTAL

nor

VERTICAL
**See Also:** getOrientation()

- setRollover

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="Will draw rollover button borders in the toolbar.")
public void setRollover​(boolean rollover)
```

Sets the rollover state of this toolbar. If the rollover state is true
then the border of the toolbar buttons will be drawn only when the
mouse pointer hovers over them. The default value of this property
is false.

The implementation of a look and feel may choose to ignore this
property.

**Parameters:** rollover

- true for rollover toolbar buttons; otherwise false
**Since:** 1.4

- isRollover

```java
public boolean isRollover()
```

Returns the rollover state.

**Returns:** true if rollover toolbar buttons are to be drawn; otherwise false
**Since:** 1.4
**See Also:** setRollover(boolean)

- addSeparator

```java
public void addSeparator()
```

Appends a separator of default size to the end of the tool bar.
The default size is determined by the current look and feel.

- addSeparator

```java
public void addSeparator​(
Dimension
size)
```

Appends a separator of a specified size to the end
of the tool bar.

**Parameters:** size

- the

Dimension

of the separator

- add

```java
public
JButton
add​(
Action
a)
```

Adds a new

JButton

which dispatches the action.

**Parameters:** a

- the

Action

object to add as a new menu item
**Returns:** the new button which dispatches the action

- createActionComponent

```java
protected
JButton
createActionComponent​(
Action
a)
```

Factory method which creates the

JButton

for

Action

s added to the

JToolBar

.
The default name is empty if a

null

action is passed.

**Parameters:** a

- the

Action

for the button to be added
**Returns:** the newly created button
**Since:** 1.3
**See Also:** Action

- createActionChangeListener

```java
protected
PropertyChangeListener
createActionChangeListener​(
JButton
b)
```

Returns a properly configured

PropertyChangeListener

which updates the control as changes to the

Action

occur,
or

null

if the default
property change listener for the control is desired.

**Parameters:** b

- a

JButton
**Returns:** null

- addImpl

```java
protected void addImpl​(
Component
comp,

Object
constraints,
int index)
```

If a

JButton

is being added, it is initially
set to be disabled.

**Overrides:** addImpl

in class

Container
**Parameters:** comp

- the component to be enhanced
**Parameters:** constraints

- the constraints to be enforced on the component
**Parameters:** index

- the index of the component
**See Also:** Container.add(Component)

,

Container.add(Component, int)

,

Container.add(Component, java.lang.Object)

,

Container.invalidate()

,

LayoutManager

,

LayoutManager2

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JToolBar

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

JToolBar

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

Gets the AccessibleContext associated with this JToolBar.
For tool bars, the AccessibleContext takes the form of an
AccessibleJToolBar.
A new AccessibleJToolBar instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJToolBar that serves as the
AccessibleContext of this JToolBar

---

#### Method Detail

getUI

```java
public
ToolBarUI
getUI()
```

Returns the tool bar's current UI.

**Overrides:** getUI

in class

JComponent
**Returns:** the tool bar's current UI.
**See Also:** setUI(javax.swing.plaf.ToolBarUI)

---

#### getUI

public

ToolBarUI

getUI()

Returns the tool bar's current UI.

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
ToolBarUI
ui)
```

Sets the L&F object that renders this component.

**Parameters:** ui

- the

ToolBarUI

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

ToolBarUI

ui)

Sets the L&F object that renders this component.

updateUI

```java
public void updateUI()
```

Notification from the

UIFactory

that the L&F has changed.
Called to replace the UI with the latest version from the

UIFactory

.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

---

#### updateUI

public void updateUI()

Notification from the

UIFactory

that the L&F has changed.
Called to replace the UI with the latest version from the

UIFactory

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
**Returns:** the string "ToolBarUI"
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

getComponentIndex

```java
public int getComponentIndex​(
Component
c)
```

Returns the index of the specified component.
(Note: Separators occupy index positions.)

**Parameters:** c

- the

Component

to find
**Returns:** an integer indicating the component's position,
where 0 is first

---

#### getComponentIndex

public int getComponentIndex​(

Component

c)

Returns the index of the specified component.
(Note: Separators occupy index positions.)

getComponentAtIndex

```java
public
Component
getComponentAtIndex​(int i)
```

Returns the component at the specified index.

**Parameters:** i

- the component's position, where 0 is first
**Returns:** the

Component

at that position,
or

null

for an invalid index

---

#### getComponentAtIndex

public

Component

getComponentAtIndex​(int i)

Returns the component at the specified index.

setMargin

```java
@BeanProperty
(
expert
=true,

description
="The margin between the tool bar\'s border and contents")
public void setMargin​(
Insets
m)
```

Sets the margin between the tool bar's border and
its buttons. Setting to

null

causes the tool bar to
use the default margins. The tool bar's default

Border

object uses this value to create the proper margin.
However, if a non-default border is set on the tool bar,
it is that

Border

object's responsibility to create the
appropriate margin space (otherwise this property will
effectively be ignored).

**Parameters:** m

- an

Insets

object that defines the space
between the border and the buttons
**See Also:** Insets

---

#### setMargin

@BeanProperty

(

expert

=true,

description

="The margin between the tool bar\'s border and contents")
public void setMargin​(

Insets

m)

Sets the margin between the tool bar's border and
its buttons. Setting to

null

causes the tool bar to
use the default margins. The tool bar's default

Border

object uses this value to create the proper margin.
However, if a non-default border is set on the tool bar,
it is that

Border

object's responsibility to create the
appropriate margin space (otherwise this property will
effectively be ignored).

getMargin

```java
public
Insets
getMargin()
```

Returns the margin between the tool bar's border and
its buttons.

**Returns:** an

Insets

object containing the margin values
**See Also:** Insets

---

#### getMargin

public

Insets

getMargin()

Returns the margin between the tool bar's border and
its buttons.

isBorderPainted

```java
public boolean isBorderPainted()
```

Gets the

borderPainted

property.

**Returns:** the value of the

borderPainted

property
**See Also:** setBorderPainted(boolean)

---

#### isBorderPainted

public boolean isBorderPainted()

Gets the

borderPainted

property.

setBorderPainted

```java
@BeanProperty
(
expert
=true,

description
="Does the tool bar paint its borders?")
public void setBorderPainted​(boolean b)
```

Sets the

borderPainted

property, which is

true

if the border should be painted.
The default value for this property is

true

.
Some look and feels might not implement painted borders;
they will ignore this property.

**Parameters:** b

- if true, the border is painted
**See Also:** isBorderPainted()

---

#### setBorderPainted

@BeanProperty

(

expert

=true,

description

="Does the tool bar paint its borders?")
public void setBorderPainted​(boolean b)

Sets the

borderPainted

property, which is

true

if the border should be painted.
The default value for this property is

true

.
Some look and feels might not implement painted borders;
they will ignore this property.

paintBorder

```java
protected void paintBorder​(
Graphics
g)
```

Paints the tool bar's border if the

borderPainted

property
is

true

.

**Overrides:** paintBorder

in class

JComponent
**Parameters:** g

- the

Graphics

context in which the painting
is done
**See Also:** JComponent.paint(java.awt.Graphics)

,

JComponent.setBorder(javax.swing.border.Border)

---

#### paintBorder

protected void paintBorder​(

Graphics

g)

Paints the tool bar's border if the

borderPainted

property
is

true

.

isFloatable

```java
public boolean isFloatable()
```

Gets the

floatable

property.

**Returns:** the value of the

floatable

property
**See Also:** setFloatable(boolean)

---

#### isFloatable

public boolean isFloatable()

Gets the

floatable

property.

setFloatable

```java
@BeanProperty
(
preferred
=true,

description
="Can the tool bar be made to float by the user?")
public void setFloatable​(boolean b)
```

Sets the

floatable

property,
which must be

true

for the user to move the tool bar.
Typically, a floatable tool bar can be
dragged into a different position within the same container
or out into its own window.
The default value of this property is

true

.
Some look and feels might not implement floatable tool bars;
they will ignore this property.

**Parameters:** b

- if

true

, the tool bar can be moved;

false

otherwise
**See Also:** isFloatable()

---

#### setFloatable

@BeanProperty

(

preferred

=true,

description

="Can the tool bar be made to float by the user?")
public void setFloatable​(boolean b)

Sets the

floatable

property,
which must be

true

for the user to move the tool bar.
Typically, a floatable tool bar can be
dragged into a different position within the same container
or out into its own window.
The default value of this property is

true

.
Some look and feels might not implement floatable tool bars;
they will ignore this property.

getOrientation

```java
public int getOrientation()
```

Returns the current orientation of the tool bar. The value is either

HORIZONTAL

or

VERTICAL

.

**Returns:** an integer representing the current orientation -- either

HORIZONTAL

or

VERTICAL
**See Also:** setOrientation(int)

---

#### getOrientation

public int getOrientation()

Returns the current orientation of the tool bar. The value is either

HORIZONTAL

or

VERTICAL

.

setOrientation

```java
@BeanProperty
(
preferred
=true,

enumerationValues
={"SwingConstants.HORIZONTAL","SwingConstants.VERTICAL"},

description
="The current orientation of the tool bar")
public void setOrientation​(int o)
```

Sets the orientation of the tool bar. The orientation must have
either the value

HORIZONTAL

or

VERTICAL

.
If

orientation

is
an invalid value, an exception will be thrown.

**Parameters:** o

- the new orientation -- either

HORIZONTAL

or

VERTICAL
**Throws:** IllegalArgumentException

- if orientation is neither

HORIZONTAL

nor

VERTICAL
**See Also:** getOrientation()

---

#### setOrientation

@BeanProperty

(

preferred

=true,

enumerationValues

={"SwingConstants.HORIZONTAL","SwingConstants.VERTICAL"},

description

="The current orientation of the tool bar")
public void setOrientation​(int o)

Sets the orientation of the tool bar. The orientation must have
either the value

HORIZONTAL

or

VERTICAL

.
If

orientation

is
an invalid value, an exception will be thrown.

setRollover

```java
@BeanProperty
(
preferred
=true,

visualUpdate
=true,

description
="Will draw rollover button borders in the toolbar.")
public void setRollover​(boolean rollover)
```

Sets the rollover state of this toolbar. If the rollover state is true
then the border of the toolbar buttons will be drawn only when the
mouse pointer hovers over them. The default value of this property
is false.

The implementation of a look and feel may choose to ignore this
property.

**Parameters:** rollover

- true for rollover toolbar buttons; otherwise false
**Since:** 1.4

---

#### setRollover

@BeanProperty

(

preferred

=true,

visualUpdate

=true,

description

="Will draw rollover button borders in the toolbar.")
public void setRollover​(boolean rollover)

Sets the rollover state of this toolbar. If the rollover state is true
then the border of the toolbar buttons will be drawn only when the
mouse pointer hovers over them. The default value of this property
is false.

The implementation of a look and feel may choose to ignore this
property.

The implementation of a look and feel may choose to ignore this
property.

isRollover

```java
public boolean isRollover()
```

Returns the rollover state.

**Returns:** true if rollover toolbar buttons are to be drawn; otherwise false
**Since:** 1.4
**See Also:** setRollover(boolean)

---

#### isRollover

public boolean isRollover()

Returns the rollover state.

addSeparator

```java
public void addSeparator()
```

Appends a separator of default size to the end of the tool bar.
The default size is determined by the current look and feel.

---

#### addSeparator

public void addSeparator()

Appends a separator of default size to the end of the tool bar.
The default size is determined by the current look and feel.

addSeparator

```java
public void addSeparator​(
Dimension
size)
```

Appends a separator of a specified size to the end
of the tool bar.

**Parameters:** size

- the

Dimension

of the separator

---

#### addSeparator

public void addSeparator​(

Dimension

size)

Appends a separator of a specified size to the end
of the tool bar.

add

```java
public
JButton
add​(
Action
a)
```

Adds a new

JButton

which dispatches the action.

**Parameters:** a

- the

Action

object to add as a new menu item
**Returns:** the new button which dispatches the action

---

#### add

public

JButton

add​(

Action

a)

Adds a new

JButton

which dispatches the action.

createActionComponent

```java
protected
JButton
createActionComponent​(
Action
a)
```

Factory method which creates the

JButton

for

Action

s added to the

JToolBar

.
The default name is empty if a

null

action is passed.

**Parameters:** a

- the

Action

for the button to be added
**Returns:** the newly created button
**Since:** 1.3
**See Also:** Action

---

#### createActionComponent

protected

JButton

createActionComponent​(

Action

a)

Factory method which creates the

JButton

for

Action

s added to the

JToolBar

.
The default name is empty if a

null

action is passed.

createActionChangeListener

```java
protected
PropertyChangeListener
createActionChangeListener​(
JButton
b)
```

Returns a properly configured

PropertyChangeListener

which updates the control as changes to the

Action

occur,
or

null

if the default
property change listener for the control is desired.

**Parameters:** b

- a

JButton
**Returns:** null

---

#### createActionChangeListener

protected

PropertyChangeListener

createActionChangeListener​(

JButton

b)

Returns a properly configured

PropertyChangeListener

which updates the control as changes to the

Action

occur,
or

null

if the default
property change listener for the control is desired.

addImpl

```java
protected void addImpl​(
Component
comp,

Object
constraints,
int index)
```

If a

JButton

is being added, it is initially
set to be disabled.

**Overrides:** addImpl

in class

Container
**Parameters:** comp

- the component to be enhanced
**Parameters:** constraints

- the constraints to be enforced on the component
**Parameters:** index

- the index of the component
**See Also:** Container.add(Component)

,

Container.add(Component, int)

,

Container.add(Component, java.lang.Object)

,

Container.invalidate()

,

LayoutManager

,

LayoutManager2

---

#### addImpl

protected void addImpl​(

Component

comp,

Object

constraints,
int index)

If a

JButton

is being added, it is initially
set to be disabled.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JToolBar

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

JToolBar

.

---

#### paramString

protected

String

paramString()

Returns a string representation of this

JToolBar

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

Gets the AccessibleContext associated with this JToolBar.
For tool bars, the AccessibleContext takes the form of an
AccessibleJToolBar.
A new AccessibleJToolBar instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJToolBar that serves as the
AccessibleContext of this JToolBar

---

#### getAccessibleContext

@BeanProperty

(

bound

=false)
public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this JToolBar.
For tool bars, the AccessibleContext takes the form of an
AccessibleJToolBar.
A new AccessibleJToolBar instance is created if necessary.

---

