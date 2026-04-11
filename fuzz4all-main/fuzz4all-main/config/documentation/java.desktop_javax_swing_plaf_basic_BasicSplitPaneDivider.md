# Class BasicSplitPaneDivider

**Source:** `java.desktop\javax\swing\plaf\basic\BasicSplitPaneDivider.html`

### Class Description

```java
public class
BasicSplitPaneDivider

extends
Container

implements
PropertyChangeListener
```

Divider used by BasicSplitPaneUI. Subclassers may wish to override
paint to do something more interesting.
The border effect is drawn in BasicSplitPaneUI, so if you don't like
that border, reset it there.
To conditionally drag from certain areas subclass mousePressed and
call super when you wish the dragging to begin.

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

PropertyChangeListener

,

Serializable

,

EventListener

---

### Field Details

#### protected static final int ONE_TOUCH_SIZE

Width or height of the divider based on orientation

BasicSplitPaneUI

adds two to this.

**See Also:**
- Constant Field Values

---

#### protected static final int ONE_TOUCH_OFFSET

The offset of the divider.

**See Also:**
- Constant Field Values

---

#### protected
BasicSplitPaneDivider.DragController
dragger

Handles mouse dragging message to do the actual dragging.

---

#### protected
BasicSplitPaneUI
splitPaneUI

UI this instance was created from.

---

#### protected int dividerSize

Size of the divider.

---

#### protected
Component
hiddenDivider

Divider that is used for noncontinuous layout mode.

---

#### protected
JSplitPane
splitPane

JSplitPane the receiver is contained in.

---

#### protected
BasicSplitPaneDivider.MouseHandler
mouseHandler

Handles mouse events from both this class, and the split pane.
Mouse events are handled for the splitpane since you want to be able
to drag when clicking on the border of the divider, which is not
drawn by the divider.

---

#### protected int orientation

Orientation of the JSplitPane.

---

#### protected
JButton
leftButton

Button for quickly toggling the left component.

---

#### protected
JButton
rightButton

Button for quickly toggling the right component.

---

### Constructor Details

#### public BasicSplitPaneDivider​(
BasicSplitPaneUI
ui)

Creates an instance of

BasicSplitPaneDivider

. Registers this
instance for mouse events and mouse dragged events.

**Parameters:**
- ui

- an instance of

BasicSplitPaneUI

---

### Method Details

#### public void setBasicSplitPaneUI​(
BasicSplitPaneUI
newUI)

Sets the

SplitPaneUI

that is using the receiver.

**Parameters:**
- newUI

- the new

SplitPaneUI

---

#### public
BasicSplitPaneUI
getBasicSplitPaneUI()

Returns the

SplitPaneUI

the receiver is currently in.

**Returns:**
- the

SplitPaneUI

the receiver is currently in

---

#### public void setDividerSize​(int newSize)

Sets the size of the divider to

newSize

. That is
the width if the splitpane is

HORIZONTAL_SPLIT

, or
the height of

VERTICAL_SPLIT

.

**Parameters:**
- newSize

- a new size

---

#### public int getDividerSize()

Returns the size of the divider, that is the width if the splitpane
is HORIZONTAL_SPLIT, or the height of VERTICAL_SPLIT.

**Returns:**
- the size of the divider

---

#### public void setBorder​(
Border
border)

Sets the border of this component.

**Parameters:**
- border

- a new border

**Since:**
- 1.3

---

#### public
Border
getBorder()

Returns the border of this component or null if no border is
currently set.

**Returns:**
- the border object for this component

**See Also:**
- setBorder(javax.swing.border.Border)

**Since:**
- 1.3

---

#### public
Insets
getInsets()

If a border has been set on this component, returns the
border's insets, else calls super.getInsets.

**Overrides:**
- getInsets

in class

Container

**Returns:**
- the value of the insets property.

**See Also:**
- setBorder(javax.swing.border.Border)

---

#### protected void setMouseOver​(boolean mouseOver)

Sets whether or not the mouse is currently over the divider.

**Parameters:**
- mouseOver

- whether or not the mouse is currently over the divider

**Since:**
- 1.5

---

#### public boolean isMouseOver()

Returns whether or not the mouse is currently over the divider

**Returns:**
- whether or not the mouse is currently over the divider

**Since:**
- 1.5

---

#### public
Dimension
getPreferredSize()

Returns dividerSize x dividerSize

**Overrides:**
- getPreferredSize

in class

Container

**Returns:**
- an instance of

Dimension

that represents
the preferred size of this container.

**See Also:**
- Container.getMinimumSize()

,

Container.getMaximumSize()

,

Container.getLayout()

,

LayoutManager.preferredLayoutSize(Container)

,

Component.getPreferredSize()

---

#### public
Dimension
getMinimumSize()

Returns dividerSize x dividerSize

**Overrides:**
- getMinimumSize

in class

Container

**Returns:**
- an instance of

Dimension

that represents
the minimum size of this container.

**See Also:**
- Container.getPreferredSize()

,

Container.getMaximumSize()

,

Container.getLayout()

,

LayoutManager.minimumLayoutSize(Container)

,

Component.getMinimumSize()

---

#### public void propertyChange​(
PropertyChangeEvent
e)

Property change event, presumably from the JSplitPane, will message
updateOrientation if necessary.

**Specified by:**
- propertyChange

in interface

PropertyChangeListener

**Parameters:**
- e

- A PropertyChangeEvent object describing the event source
and the property that has changed.

---

#### public void paint​(
Graphics
g)

Paints the divider.

**Overrides:**
- paint

in class

Container

**Parameters:**
- g

- the specified Graphics window

**See Also:**
- Component.update(Graphics)

---

#### protected void oneTouchExpandableChanged()

Messaged when the oneTouchExpandable value of the JSplitPane the
receiver is contained in changes. Will create the

leftButton

and

rightButton

if they
are null. invalidates the receiver as well.

---

#### protected
JButton
createLeftOneTouchButton()

Creates and return an instance of

JButton

that can be used to
collapse the left component in the split pane.

**Returns:**
- an instance of

JButton

---

#### protected
JButton
createRightOneTouchButton()

Creates and return an instance of

JButton

that can be used to
collapse the right component in the split pane.

**Returns:**
- an instance of

JButton

---

#### protected void prepareForDragging()

Message to prepare for dragging. This messages the BasicSplitPaneUI
with startDragging.

---

#### protected void dragDividerTo​(int location)

Messages the BasicSplitPaneUI with dragDividerTo that this instance
is contained in.

**Parameters:**
- location

- a location

---

#### protected void finishDraggingTo​(int location)

Messages the BasicSplitPaneUI with finishDraggingTo that this instance
is contained in.

**Parameters:**
- location

- a location

---

### Additional Sections

#### Class BasicSplitPaneDivider

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.plaf.basic.BasicSplitPaneDivider

java.awt.Component

- java.awt.Container
- - javax.swing.plaf.basic.BasicSplitPaneDivider

java.awt.Container

- javax.swing.plaf.basic.BasicSplitPaneDivider

javax.swing.plaf.basic.BasicSplitPaneDivider

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

PropertyChangeListener

,

Serializable

,

EventListener

```java
public class
BasicSplitPaneDivider

extends
Container

implements
PropertyChangeListener
```

Divider used by BasicSplitPaneUI. Subclassers may wish to override
paint to do something more interesting.
The border effect is drawn in BasicSplitPaneUI, so if you don't like
that border, reset it there.
To conditionally drag from certain areas subclass mousePressed and
call super when you wish the dragging to begin.

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

**See Also:** Serialized Form

public class

BasicSplitPaneDivider

extends

Container

implements

PropertyChangeListener

Divider used by BasicSplitPaneUI. Subclassers may wish to override
paint to do something more interesting.
The border effect is drawn in BasicSplitPaneUI, so if you don't like
that border, reset it there.
To conditionally drag from certain areas subclass mousePressed and
call super when you wish the dragging to begin.

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

BasicSplitPaneDivider.DividerLayout

Used to layout a

BasicSplitPaneDivider

.

protected class

BasicSplitPaneDivider.DragController

Handles the events during a dragging session for a
HORIZONTAL_SPLIT oriented split pane.

protected class

BasicSplitPaneDivider.MouseHandler

MouseHandler is responsible for converting mouse events
(released, dragged...) into the appropriate DragController
methods.

protected class

BasicSplitPaneDivider.VerticalDragController

Handles the events during a dragging session for a
VERTICAL_SPLIT oriented split pane.

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

protected int

dividerSize

Size of the divider.

protected

BasicSplitPaneDivider.DragController

dragger

Handles mouse dragging message to do the actual dragging.

protected

Component

hiddenDivider

Divider that is used for noncontinuous layout mode.

protected

JButton

leftButton

Button for quickly toggling the left component.

protected

BasicSplitPaneDivider.MouseHandler

mouseHandler

Handles mouse events from both this class, and the split pane.

protected static int

ONE_TOUCH_OFFSET

The offset of the divider.

protected static int

ONE_TOUCH_SIZE

Width or height of the divider based on orientation

BasicSplitPaneUI

adds two to this.

protected int

orientation

Orientation of the JSplitPane.

protected

JButton

rightButton

Button for quickly toggling the right component.

protected

JSplitPane

splitPane

JSplitPane the receiver is contained in.

protected

BasicSplitPaneUI

splitPaneUI

UI this instance was created from.

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

BasicSplitPaneDivider

​(

BasicSplitPaneUI

ui)

Creates an instance of

BasicSplitPaneDivider

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

JButton

createLeftOneTouchButton

()

Creates and return an instance of

JButton

that can be used to
collapse the left component in the split pane.

protected

JButton

createRightOneTouchButton

()

Creates and return an instance of

JButton

that can be used to
collapse the right component in the split pane.

protected void

dragDividerTo

​(int location)

Messages the BasicSplitPaneUI with dragDividerTo that this instance
is contained in.

protected void

finishDraggingTo

​(int location)

Messages the BasicSplitPaneUI with finishDraggingTo that this instance
is contained in.

BasicSplitPaneUI

getBasicSplitPaneUI

()

Returns the

SplitPaneUI

the receiver is currently in.

Border

getBorder

()

Returns the border of this component or null if no border is
currently set.

int

getDividerSize

()

Returns the size of the divider, that is the width if the splitpane
is HORIZONTAL_SPLIT, or the height of VERTICAL_SPLIT.

Insets

getInsets

()

If a border has been set on this component, returns the
border's insets, else calls super.getInsets.

Dimension

getMinimumSize

()

Returns dividerSize x dividerSize

Dimension

getPreferredSize

()

Returns dividerSize x dividerSize

boolean

isMouseOver

()

Returns whether or not the mouse is currently over the divider

protected void

oneTouchExpandableChanged

()

Messaged when the oneTouchExpandable value of the JSplitPane the
receiver is contained in changes.

void

paint

​(

Graphics

g)

Paints the divider.

protected void

prepareForDragging

()

Message to prepare for dragging.

void

propertyChange

​(

PropertyChangeEvent

e)

Property change event, presumably from the JSplitPane, will message
updateOrientation if necessary.

void

setBasicSplitPaneUI

​(

BasicSplitPaneUI

newUI)

Sets the

SplitPaneUI

that is using the receiver.

void

setBorder

​(

Border

border)

Sets the border of this component.

void

setDividerSize

​(int newSize)

Sets the size of the divider to

newSize

.

protected void

setMouseOver

​(boolean mouseOver)

Sets whether or not the mouse is currently over the divider.

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

addNotify

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

getAlignmentX

,

getAlignmentY

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

getListeners

,

getMaximumSize

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

isValidateRoot

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

paramString

,

preferredSize

,

print

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

removeNotify

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalKeys

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setFont

,

setLayout

,

transferFocusDownCycle

,

update

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

disable

,

disableEvents

,

dispatchEvent

,

enable

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

firePropertyChange

,

firePropertyChange

,

getAccessibleContext

,

getBackground

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

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

getFontMetrics

,

getForeground

,

getGraphics

,

getGraphicsConfiguration

,

getHeight

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

getSize

,

getToolkit

,

getTreeLock

,

getWidth

,

getX

,

getY

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

isDoubleBuffered

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

isOpaque

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

printAll

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

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

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

repaint

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

reshape

,

resize

,

resize

,

revalidate

,

setBackground

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

setEnabled

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

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

BasicSplitPaneDivider.DividerLayout

Used to layout a

BasicSplitPaneDivider

.

protected class

BasicSplitPaneDivider.DragController

Handles the events during a dragging session for a
HORIZONTAL_SPLIT oriented split pane.

protected class

BasicSplitPaneDivider.MouseHandler

MouseHandler is responsible for converting mouse events
(released, dragged...) into the appropriate DragController
methods.

protected class

BasicSplitPaneDivider.VerticalDragController

Handles the events during a dragging session for a
VERTICAL_SPLIT oriented split pane.

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

Used to layout a

BasicSplitPaneDivider

.

Handles the events during a dragging session for a
HORIZONTAL_SPLIT oriented split pane.

MouseHandler is responsible for converting mouse events
(released, dragged...) into the appropriate DragController
methods.

Handles the events during a dragging session for a
VERTICAL_SPLIT oriented split pane.

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

protected int

dividerSize

Size of the divider.

protected

BasicSplitPaneDivider.DragController

dragger

Handles mouse dragging message to do the actual dragging.

protected

Component

hiddenDivider

Divider that is used for noncontinuous layout mode.

protected

JButton

leftButton

Button for quickly toggling the left component.

protected

BasicSplitPaneDivider.MouseHandler

mouseHandler

Handles mouse events from both this class, and the split pane.

protected static int

ONE_TOUCH_OFFSET

The offset of the divider.

protected static int

ONE_TOUCH_SIZE

Width or height of the divider based on orientation

BasicSplitPaneUI

adds two to this.

protected int

orientation

Orientation of the JSplitPane.

protected

JButton

rightButton

Button for quickly toggling the right component.

protected

JSplitPane

splitPane

JSplitPane the receiver is contained in.

protected

BasicSplitPaneUI

splitPaneUI

UI this instance was created from.

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

Size of the divider.

Handles mouse dragging message to do the actual dragging.

Divider that is used for noncontinuous layout mode.

Button for quickly toggling the left component.

Handles mouse events from both this class, and the split pane.

The offset of the divider.

Width or height of the divider based on orientation

BasicSplitPaneUI

adds two to this.

Orientation of the JSplitPane.

Button for quickly toggling the right component.

JSplitPane the receiver is contained in.

UI this instance was created from.

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

BasicSplitPaneDivider

​(

BasicSplitPaneUI

ui)

Creates an instance of

BasicSplitPaneDivider

.

---

#### Constructor Summary

Creates an instance of

BasicSplitPaneDivider

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

JButton

createLeftOneTouchButton

()

Creates and return an instance of

JButton

that can be used to
collapse the left component in the split pane.

protected

JButton

createRightOneTouchButton

()

Creates and return an instance of

JButton

that can be used to
collapse the right component in the split pane.

protected void

dragDividerTo

​(int location)

Messages the BasicSplitPaneUI with dragDividerTo that this instance
is contained in.

protected void

finishDraggingTo

​(int location)

Messages the BasicSplitPaneUI with finishDraggingTo that this instance
is contained in.

BasicSplitPaneUI

getBasicSplitPaneUI

()

Returns the

SplitPaneUI

the receiver is currently in.

Border

getBorder

()

Returns the border of this component or null if no border is
currently set.

int

getDividerSize

()

Returns the size of the divider, that is the width if the splitpane
is HORIZONTAL_SPLIT, or the height of VERTICAL_SPLIT.

Insets

getInsets

()

If a border has been set on this component, returns the
border's insets, else calls super.getInsets.

Dimension

getMinimumSize

()

Returns dividerSize x dividerSize

Dimension

getPreferredSize

()

Returns dividerSize x dividerSize

boolean

isMouseOver

()

Returns whether or not the mouse is currently over the divider

protected void

oneTouchExpandableChanged

()

Messaged when the oneTouchExpandable value of the JSplitPane the
receiver is contained in changes.

void

paint

​(

Graphics

g)

Paints the divider.

protected void

prepareForDragging

()

Message to prepare for dragging.

void

propertyChange

​(

PropertyChangeEvent

e)

Property change event, presumably from the JSplitPane, will message
updateOrientation if necessary.

void

setBasicSplitPaneUI

​(

BasicSplitPaneUI

newUI)

Sets the

SplitPaneUI

that is using the receiver.

void

setBorder

​(

Border

border)

Sets the border of this component.

void

setDividerSize

​(int newSize)

Sets the size of the divider to

newSize

.

protected void

setMouseOver

​(boolean mouseOver)

Sets whether or not the mouse is currently over the divider.

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

addNotify

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

getAlignmentX

,

getAlignmentY

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

getListeners

,

getMaximumSize

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

isValidateRoot

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

paramString

,

preferredSize

,

print

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

removeNotify

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalKeys

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setFont

,

setLayout

,

transferFocusDownCycle

,

update

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

disable

,

disableEvents

,

dispatchEvent

,

enable

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

firePropertyChange

,

firePropertyChange

,

getAccessibleContext

,

getBackground

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

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

getFontMetrics

,

getForeground

,

getGraphics

,

getGraphicsConfiguration

,

getHeight

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

getSize

,

getToolkit

,

getTreeLock

,

getWidth

,

getX

,

getY

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

isDoubleBuffered

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

isOpaque

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

printAll

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

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

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

repaint

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

reshape

,

resize

,

resize

,

revalidate

,

setBackground

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

setEnabled

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

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

Creates and return an instance of

JButton

that can be used to
collapse the left component in the split pane.

Creates and return an instance of

JButton

that can be used to
collapse the right component in the split pane.

Messages the BasicSplitPaneUI with dragDividerTo that this instance
is contained in.

Messages the BasicSplitPaneUI with finishDraggingTo that this instance
is contained in.

Returns the

SplitPaneUI

the receiver is currently in.

Returns the border of this component or null if no border is
currently set.

Returns the size of the divider, that is the width if the splitpane
is HORIZONTAL_SPLIT, or the height of VERTICAL_SPLIT.

If a border has been set on this component, returns the
border's insets, else calls super.getInsets.

Returns dividerSize x dividerSize

Returns whether or not the mouse is currently over the divider

Messaged when the oneTouchExpandable value of the JSplitPane the
receiver is contained in changes.

Paints the divider.

Message to prepare for dragging.

Property change event, presumably from the JSplitPane, will message
updateOrientation if necessary.

Sets the

SplitPaneUI

that is using the receiver.

Sets the border of this component.

Sets the size of the divider to

newSize

.

Sets whether or not the mouse is currently over the divider.

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

addNotify

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

getAlignmentX

,

getAlignmentY

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

getListeners

,

getMaximumSize

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

isValidateRoot

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

paramString

,

preferredSize

,

print

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

removeNotify

,

setComponentZOrder

,

setFocusCycleRoot

,

setFocusTraversalKeys

,

setFocusTraversalPolicy

,

setFocusTraversalPolicyProvider

,

setFont

,

setLayout

,

transferFocusDownCycle

,

update

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

disable

,

disableEvents

,

dispatchEvent

,

enable

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

firePropertyChange

,

firePropertyChange

,

getAccessibleContext

,

getBackground

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

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

getFontMetrics

,

getForeground

,

getGraphics

,

getGraphicsConfiguration

,

getHeight

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

getSize

,

getToolkit

,

getTreeLock

,

getWidth

,

getX

,

getY

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

isDoubleBuffered

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

isOpaque

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

printAll

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

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

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

repaint

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

reshape

,

resize

,

resize

,

revalidate

,

setBackground

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

setEnabled

,

setFocusable

,

setFocusTraversalKeysEnabled

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

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

- ONE_TOUCH_SIZE

```java
protected static final int ONE_TOUCH_SIZE
```

Width or height of the divider based on orientation

BasicSplitPaneUI

adds two to this.

**See Also:** Constant Field Values

- ONE_TOUCH_OFFSET

```java
protected static final int ONE_TOUCH_OFFSET
```

The offset of the divider.

**See Also:** Constant Field Values

- dragger

```java
protected
BasicSplitPaneDivider.DragController
dragger
```

Handles mouse dragging message to do the actual dragging.

- splitPaneUI

```java
protected
BasicSplitPaneUI
splitPaneUI
```

UI this instance was created from.

- dividerSize

```java
protected int dividerSize
```

Size of the divider.

- hiddenDivider

```java
protected
Component
hiddenDivider
```

Divider that is used for noncontinuous layout mode.

- splitPane

```java
protected
JSplitPane
splitPane
```

JSplitPane the receiver is contained in.

- mouseHandler

```java
protected
BasicSplitPaneDivider.MouseHandler
mouseHandler
```

Handles mouse events from both this class, and the split pane.
Mouse events are handled for the splitpane since you want to be able
to drag when clicking on the border of the divider, which is not
drawn by the divider.

- orientation

```java
protected int orientation
```

Orientation of the JSplitPane.

- leftButton

```java
protected
JButton
leftButton
```

Button for quickly toggling the left component.

- rightButton

```java
protected
JButton
rightButton
```

Button for quickly toggling the right component.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicSplitPaneDivider

```java
public BasicSplitPaneDivider​(
BasicSplitPaneUI
ui)
```

Creates an instance of

BasicSplitPaneDivider

. Registers this
instance for mouse events and mouse dragged events.

**Parameters:** ui

- an instance of

BasicSplitPaneUI

============ METHOD DETAIL ==========

- Method Detail

- setBasicSplitPaneUI

```java
public void setBasicSplitPaneUI​(
BasicSplitPaneUI
newUI)
```

Sets the

SplitPaneUI

that is using the receiver.

**Parameters:** newUI

- the new

SplitPaneUI

- getBasicSplitPaneUI

```java
public
BasicSplitPaneUI
getBasicSplitPaneUI()
```

Returns the

SplitPaneUI

the receiver is currently in.

**Returns:** the

SplitPaneUI

the receiver is currently in

- setDividerSize

```java
public void setDividerSize​(int newSize)
```

Sets the size of the divider to

newSize

. That is
the width if the splitpane is

HORIZONTAL_SPLIT

, or
the height of

VERTICAL_SPLIT

.

**Parameters:** newSize

- a new size

- getDividerSize

```java
public int getDividerSize()
```

Returns the size of the divider, that is the width if the splitpane
is HORIZONTAL_SPLIT, or the height of VERTICAL_SPLIT.

**Returns:** the size of the divider

- setBorder

```java
public void setBorder​(
Border
border)
```

Sets the border of this component.

**Parameters:** border

- a new border
**Since:** 1.3

- getBorder

```java
public
Border
getBorder()
```

Returns the border of this component or null if no border is
currently set.

**Returns:** the border object for this component
**Since:** 1.3
**See Also:** setBorder(javax.swing.border.Border)

- getInsets

```java
public
Insets
getInsets()
```

If a border has been set on this component, returns the
border's insets, else calls super.getInsets.

**Overrides:** getInsets

in class

Container
**Returns:** the value of the insets property.
**See Also:** setBorder(javax.swing.border.Border)

- setMouseOver

```java
protected void setMouseOver​(boolean mouseOver)
```

Sets whether or not the mouse is currently over the divider.

**Parameters:** mouseOver

- whether or not the mouse is currently over the divider
**Since:** 1.5

- isMouseOver

```java
public boolean isMouseOver()
```

Returns whether or not the mouse is currently over the divider

**Returns:** whether or not the mouse is currently over the divider
**Since:** 1.5

- getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Returns dividerSize x dividerSize

**Overrides:** getPreferredSize

in class

Container
**Returns:** an instance of

Dimension

that represents
the preferred size of this container.
**See Also:** Container.getMinimumSize()

,

Container.getMaximumSize()

,

Container.getLayout()

,

LayoutManager.preferredLayoutSize(Container)

,

Component.getPreferredSize()

- getMinimumSize

```java
public
Dimension
getMinimumSize()
```

Returns dividerSize x dividerSize

**Overrides:** getMinimumSize

in class

Container
**Returns:** an instance of

Dimension

that represents
the minimum size of this container.
**See Also:** Container.getPreferredSize()

,

Container.getMaximumSize()

,

Container.getLayout()

,

LayoutManager.minimumLayoutSize(Container)

,

Component.getMinimumSize()

- propertyChange

```java
public void propertyChange​(
PropertyChangeEvent
e)
```

Property change event, presumably from the JSplitPane, will message
updateOrientation if necessary.

**Specified by:** propertyChange

in interface

PropertyChangeListener
**Parameters:** e

- A PropertyChangeEvent object describing the event source
and the property that has changed.

- paint

```java
public void paint​(
Graphics
g)
```

Paints the divider.

**Overrides:** paint

in class

Container
**Parameters:** g

- the specified Graphics window
**See Also:** Component.update(Graphics)

- oneTouchExpandableChanged

```java
protected void oneTouchExpandableChanged()
```

Messaged when the oneTouchExpandable value of the JSplitPane the
receiver is contained in changes. Will create the

leftButton

and

rightButton

if they
are null. invalidates the receiver as well.

- createLeftOneTouchButton

```java
protected
JButton
createLeftOneTouchButton()
```

Creates and return an instance of

JButton

that can be used to
collapse the left component in the split pane.

**Returns:** an instance of

JButton

- createRightOneTouchButton

```java
protected
JButton
createRightOneTouchButton()
```

Creates and return an instance of

JButton

that can be used to
collapse the right component in the split pane.

**Returns:** an instance of

JButton

- prepareForDragging

```java
protected void prepareForDragging()
```

Message to prepare for dragging. This messages the BasicSplitPaneUI
with startDragging.

- dragDividerTo

```java
protected void dragDividerTo​(int location)
```

Messages the BasicSplitPaneUI with dragDividerTo that this instance
is contained in.

**Parameters:** location

- a location

- finishDraggingTo

```java
protected void finishDraggingTo​(int location)
```

Messages the BasicSplitPaneUI with finishDraggingTo that this instance
is contained in.

**Parameters:** location

- a location

Field Detail

- ONE_TOUCH_SIZE

```java
protected static final int ONE_TOUCH_SIZE
```

Width or height of the divider based on orientation

BasicSplitPaneUI

adds two to this.

**See Also:** Constant Field Values

- ONE_TOUCH_OFFSET

```java
protected static final int ONE_TOUCH_OFFSET
```

The offset of the divider.

**See Also:** Constant Field Values

- dragger

```java
protected
BasicSplitPaneDivider.DragController
dragger
```

Handles mouse dragging message to do the actual dragging.

- splitPaneUI

```java
protected
BasicSplitPaneUI
splitPaneUI
```

UI this instance was created from.

- dividerSize

```java
protected int dividerSize
```

Size of the divider.

- hiddenDivider

```java
protected
Component
hiddenDivider
```

Divider that is used for noncontinuous layout mode.

- splitPane

```java
protected
JSplitPane
splitPane
```

JSplitPane the receiver is contained in.

- mouseHandler

```java
protected
BasicSplitPaneDivider.MouseHandler
mouseHandler
```

Handles mouse events from both this class, and the split pane.
Mouse events are handled for the splitpane since you want to be able
to drag when clicking on the border of the divider, which is not
drawn by the divider.

- orientation

```java
protected int orientation
```

Orientation of the JSplitPane.

- leftButton

```java
protected
JButton
leftButton
```

Button for quickly toggling the left component.

- rightButton

```java
protected
JButton
rightButton
```

Button for quickly toggling the right component.

---

#### Field Detail

ONE_TOUCH_SIZE

```java
protected static final int ONE_TOUCH_SIZE
```

Width or height of the divider based on orientation

BasicSplitPaneUI

adds two to this.

**See Also:** Constant Field Values

---

#### ONE_TOUCH_SIZE

protected static final int ONE_TOUCH_SIZE

Width or height of the divider based on orientation

BasicSplitPaneUI

adds two to this.

ONE_TOUCH_OFFSET

```java
protected static final int ONE_TOUCH_OFFSET
```

The offset of the divider.

**See Also:** Constant Field Values

---

#### ONE_TOUCH_OFFSET

protected static final int ONE_TOUCH_OFFSET

The offset of the divider.

dragger

```java
protected
BasicSplitPaneDivider.DragController
dragger
```

Handles mouse dragging message to do the actual dragging.

---

#### dragger

protected

BasicSplitPaneDivider.DragController

dragger

Handles mouse dragging message to do the actual dragging.

splitPaneUI

```java
protected
BasicSplitPaneUI
splitPaneUI
```

UI this instance was created from.

---

#### splitPaneUI

protected

BasicSplitPaneUI

splitPaneUI

UI this instance was created from.

dividerSize

```java
protected int dividerSize
```

Size of the divider.

---

#### dividerSize

protected int dividerSize

Size of the divider.

hiddenDivider

```java
protected
Component
hiddenDivider
```

Divider that is used for noncontinuous layout mode.

---

#### hiddenDivider

protected

Component

hiddenDivider

Divider that is used for noncontinuous layout mode.

splitPane

```java
protected
JSplitPane
splitPane
```

JSplitPane the receiver is contained in.

---

#### splitPane

protected

JSplitPane

splitPane

JSplitPane the receiver is contained in.

mouseHandler

```java
protected
BasicSplitPaneDivider.MouseHandler
mouseHandler
```

Handles mouse events from both this class, and the split pane.
Mouse events are handled for the splitpane since you want to be able
to drag when clicking on the border of the divider, which is not
drawn by the divider.

---

#### mouseHandler

protected

BasicSplitPaneDivider.MouseHandler

mouseHandler

Handles mouse events from both this class, and the split pane.
Mouse events are handled for the splitpane since you want to be able
to drag when clicking on the border of the divider, which is not
drawn by the divider.

orientation

```java
protected int orientation
```

Orientation of the JSplitPane.

---

#### orientation

protected int orientation

Orientation of the JSplitPane.

leftButton

```java
protected
JButton
leftButton
```

Button for quickly toggling the left component.

---

#### leftButton

protected

JButton

leftButton

Button for quickly toggling the left component.

rightButton

```java
protected
JButton
rightButton
```

Button for quickly toggling the right component.

---

#### rightButton

protected

JButton

rightButton

Button for quickly toggling the right component.

Constructor Detail

- BasicSplitPaneDivider

```java
public BasicSplitPaneDivider​(
BasicSplitPaneUI
ui)
```

Creates an instance of

BasicSplitPaneDivider

. Registers this
instance for mouse events and mouse dragged events.

**Parameters:** ui

- an instance of

BasicSplitPaneUI

---

#### Constructor Detail

BasicSplitPaneDivider

```java
public BasicSplitPaneDivider​(
BasicSplitPaneUI
ui)
```

Creates an instance of

BasicSplitPaneDivider

. Registers this
instance for mouse events and mouse dragged events.

**Parameters:** ui

- an instance of

BasicSplitPaneUI

---

#### BasicSplitPaneDivider

public BasicSplitPaneDivider​(

BasicSplitPaneUI

ui)

Creates an instance of

BasicSplitPaneDivider

. Registers this
instance for mouse events and mouse dragged events.

Method Detail

- setBasicSplitPaneUI

```java
public void setBasicSplitPaneUI​(
BasicSplitPaneUI
newUI)
```

Sets the

SplitPaneUI

that is using the receiver.

**Parameters:** newUI

- the new

SplitPaneUI

- getBasicSplitPaneUI

```java
public
BasicSplitPaneUI
getBasicSplitPaneUI()
```

Returns the

SplitPaneUI

the receiver is currently in.

**Returns:** the

SplitPaneUI

the receiver is currently in

- setDividerSize

```java
public void setDividerSize​(int newSize)
```

Sets the size of the divider to

newSize

. That is
the width if the splitpane is

HORIZONTAL_SPLIT

, or
the height of

VERTICAL_SPLIT

.

**Parameters:** newSize

- a new size

- getDividerSize

```java
public int getDividerSize()
```

Returns the size of the divider, that is the width if the splitpane
is HORIZONTAL_SPLIT, or the height of VERTICAL_SPLIT.

**Returns:** the size of the divider

- setBorder

```java
public void setBorder​(
Border
border)
```

Sets the border of this component.

**Parameters:** border

- a new border
**Since:** 1.3

- getBorder

```java
public
Border
getBorder()
```

Returns the border of this component or null if no border is
currently set.

**Returns:** the border object for this component
**Since:** 1.3
**See Also:** setBorder(javax.swing.border.Border)

- getInsets

```java
public
Insets
getInsets()
```

If a border has been set on this component, returns the
border's insets, else calls super.getInsets.

**Overrides:** getInsets

in class

Container
**Returns:** the value of the insets property.
**See Also:** setBorder(javax.swing.border.Border)

- setMouseOver

```java
protected void setMouseOver​(boolean mouseOver)
```

Sets whether or not the mouse is currently over the divider.

**Parameters:** mouseOver

- whether or not the mouse is currently over the divider
**Since:** 1.5

- isMouseOver

```java
public boolean isMouseOver()
```

Returns whether or not the mouse is currently over the divider

**Returns:** whether or not the mouse is currently over the divider
**Since:** 1.5

- getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Returns dividerSize x dividerSize

**Overrides:** getPreferredSize

in class

Container
**Returns:** an instance of

Dimension

that represents
the preferred size of this container.
**See Also:** Container.getMinimumSize()

,

Container.getMaximumSize()

,

Container.getLayout()

,

LayoutManager.preferredLayoutSize(Container)

,

Component.getPreferredSize()

- getMinimumSize

```java
public
Dimension
getMinimumSize()
```

Returns dividerSize x dividerSize

**Overrides:** getMinimumSize

in class

Container
**Returns:** an instance of

Dimension

that represents
the minimum size of this container.
**See Also:** Container.getPreferredSize()

,

Container.getMaximumSize()

,

Container.getLayout()

,

LayoutManager.minimumLayoutSize(Container)

,

Component.getMinimumSize()

- propertyChange

```java
public void propertyChange​(
PropertyChangeEvent
e)
```

Property change event, presumably from the JSplitPane, will message
updateOrientation if necessary.

**Specified by:** propertyChange

in interface

PropertyChangeListener
**Parameters:** e

- A PropertyChangeEvent object describing the event source
and the property that has changed.

- paint

```java
public void paint​(
Graphics
g)
```

Paints the divider.

**Overrides:** paint

in class

Container
**Parameters:** g

- the specified Graphics window
**See Also:** Component.update(Graphics)

- oneTouchExpandableChanged

```java
protected void oneTouchExpandableChanged()
```

Messaged when the oneTouchExpandable value of the JSplitPane the
receiver is contained in changes. Will create the

leftButton

and

rightButton

if they
are null. invalidates the receiver as well.

- createLeftOneTouchButton

```java
protected
JButton
createLeftOneTouchButton()
```

Creates and return an instance of

JButton

that can be used to
collapse the left component in the split pane.

**Returns:** an instance of

JButton

- createRightOneTouchButton

```java
protected
JButton
createRightOneTouchButton()
```

Creates and return an instance of

JButton

that can be used to
collapse the right component in the split pane.

**Returns:** an instance of

JButton

- prepareForDragging

```java
protected void prepareForDragging()
```

Message to prepare for dragging. This messages the BasicSplitPaneUI
with startDragging.

- dragDividerTo

```java
protected void dragDividerTo​(int location)
```

Messages the BasicSplitPaneUI with dragDividerTo that this instance
is contained in.

**Parameters:** location

- a location

- finishDraggingTo

```java
protected void finishDraggingTo​(int location)
```

Messages the BasicSplitPaneUI with finishDraggingTo that this instance
is contained in.

**Parameters:** location

- a location

---

#### Method Detail

setBasicSplitPaneUI

```java
public void setBasicSplitPaneUI​(
BasicSplitPaneUI
newUI)
```

Sets the

SplitPaneUI

that is using the receiver.

**Parameters:** newUI

- the new

SplitPaneUI

---

#### setBasicSplitPaneUI

public void setBasicSplitPaneUI​(

BasicSplitPaneUI

newUI)

Sets the

SplitPaneUI

that is using the receiver.

getBasicSplitPaneUI

```java
public
BasicSplitPaneUI
getBasicSplitPaneUI()
```

Returns the

SplitPaneUI

the receiver is currently in.

**Returns:** the

SplitPaneUI

the receiver is currently in

---

#### getBasicSplitPaneUI

public

BasicSplitPaneUI

getBasicSplitPaneUI()

Returns the

SplitPaneUI

the receiver is currently in.

setDividerSize

```java
public void setDividerSize​(int newSize)
```

Sets the size of the divider to

newSize

. That is
the width if the splitpane is

HORIZONTAL_SPLIT

, or
the height of

VERTICAL_SPLIT

.

**Parameters:** newSize

- a new size

---

#### setDividerSize

public void setDividerSize​(int newSize)

Sets the size of the divider to

newSize

. That is
the width if the splitpane is

HORIZONTAL_SPLIT

, or
the height of

VERTICAL_SPLIT

.

getDividerSize

```java
public int getDividerSize()
```

Returns the size of the divider, that is the width if the splitpane
is HORIZONTAL_SPLIT, or the height of VERTICAL_SPLIT.

**Returns:** the size of the divider

---

#### getDividerSize

public int getDividerSize()

Returns the size of the divider, that is the width if the splitpane
is HORIZONTAL_SPLIT, or the height of VERTICAL_SPLIT.

setBorder

```java
public void setBorder​(
Border
border)
```

Sets the border of this component.

**Parameters:** border

- a new border
**Since:** 1.3

---

#### setBorder

public void setBorder​(

Border

border)

Sets the border of this component.

getBorder

```java
public
Border
getBorder()
```

Returns the border of this component or null if no border is
currently set.

**Returns:** the border object for this component
**Since:** 1.3
**See Also:** setBorder(javax.swing.border.Border)

---

#### getBorder

public

Border

getBorder()

Returns the border of this component or null if no border is
currently set.

getInsets

```java
public
Insets
getInsets()
```

If a border has been set on this component, returns the
border's insets, else calls super.getInsets.

**Overrides:** getInsets

in class

Container
**Returns:** the value of the insets property.
**See Also:** setBorder(javax.swing.border.Border)

---

#### getInsets

public

Insets

getInsets()

If a border has been set on this component, returns the
border's insets, else calls super.getInsets.

setMouseOver

```java
protected void setMouseOver​(boolean mouseOver)
```

Sets whether or not the mouse is currently over the divider.

**Parameters:** mouseOver

- whether or not the mouse is currently over the divider
**Since:** 1.5

---

#### setMouseOver

protected void setMouseOver​(boolean mouseOver)

Sets whether or not the mouse is currently over the divider.

isMouseOver

```java
public boolean isMouseOver()
```

Returns whether or not the mouse is currently over the divider

**Returns:** whether or not the mouse is currently over the divider
**Since:** 1.5

---

#### isMouseOver

public boolean isMouseOver()

Returns whether or not the mouse is currently over the divider

getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Returns dividerSize x dividerSize

**Overrides:** getPreferredSize

in class

Container
**Returns:** an instance of

Dimension

that represents
the preferred size of this container.
**See Also:** Container.getMinimumSize()

,

Container.getMaximumSize()

,

Container.getLayout()

,

LayoutManager.preferredLayoutSize(Container)

,

Component.getPreferredSize()

---

#### getPreferredSize

public

Dimension

getPreferredSize()

Returns dividerSize x dividerSize

getMinimumSize

```java
public
Dimension
getMinimumSize()
```

Returns dividerSize x dividerSize

**Overrides:** getMinimumSize

in class

Container
**Returns:** an instance of

Dimension

that represents
the minimum size of this container.
**See Also:** Container.getPreferredSize()

,

Container.getMaximumSize()

,

Container.getLayout()

,

LayoutManager.minimumLayoutSize(Container)

,

Component.getMinimumSize()

---

#### getMinimumSize

public

Dimension

getMinimumSize()

Returns dividerSize x dividerSize

propertyChange

```java
public void propertyChange​(
PropertyChangeEvent
e)
```

Property change event, presumably from the JSplitPane, will message
updateOrientation if necessary.

**Specified by:** propertyChange

in interface

PropertyChangeListener
**Parameters:** e

- A PropertyChangeEvent object describing the event source
and the property that has changed.

---

#### propertyChange

public void propertyChange​(

PropertyChangeEvent

e)

Property change event, presumably from the JSplitPane, will message
updateOrientation if necessary.

paint

```java
public void paint​(
Graphics
g)
```

Paints the divider.

**Overrides:** paint

in class

Container
**Parameters:** g

- the specified Graphics window
**See Also:** Component.update(Graphics)

---

#### paint

public void paint​(

Graphics

g)

Paints the divider.

oneTouchExpandableChanged

```java
protected void oneTouchExpandableChanged()
```

Messaged when the oneTouchExpandable value of the JSplitPane the
receiver is contained in changes. Will create the

leftButton

and

rightButton

if they
are null. invalidates the receiver as well.

---

#### oneTouchExpandableChanged

protected void oneTouchExpandableChanged()

Messaged when the oneTouchExpandable value of the JSplitPane the
receiver is contained in changes. Will create the

leftButton

and

rightButton

if they
are null. invalidates the receiver as well.

createLeftOneTouchButton

```java
protected
JButton
createLeftOneTouchButton()
```

Creates and return an instance of

JButton

that can be used to
collapse the left component in the split pane.

**Returns:** an instance of

JButton

---

#### createLeftOneTouchButton

protected

JButton

createLeftOneTouchButton()

Creates and return an instance of

JButton

that can be used to
collapse the left component in the split pane.

createRightOneTouchButton

```java
protected
JButton
createRightOneTouchButton()
```

Creates and return an instance of

JButton

that can be used to
collapse the right component in the split pane.

**Returns:** an instance of

JButton

---

#### createRightOneTouchButton

protected

JButton

createRightOneTouchButton()

Creates and return an instance of

JButton

that can be used to
collapse the right component in the split pane.

prepareForDragging

```java
protected void prepareForDragging()
```

Message to prepare for dragging. This messages the BasicSplitPaneUI
with startDragging.

---

#### prepareForDragging

protected void prepareForDragging()

Message to prepare for dragging. This messages the BasicSplitPaneUI
with startDragging.

dragDividerTo

```java
protected void dragDividerTo​(int location)
```

Messages the BasicSplitPaneUI with dragDividerTo that this instance
is contained in.

**Parameters:** location

- a location

---

#### dragDividerTo

protected void dragDividerTo​(int location)

Messages the BasicSplitPaneUI with dragDividerTo that this instance
is contained in.

finishDraggingTo

```java
protected void finishDraggingTo​(int location)
```

Messages the BasicSplitPaneUI with finishDraggingTo that this instance
is contained in.

**Parameters:** location

- a location

---

#### finishDraggingTo

protected void finishDraggingTo​(int location)

Messages the BasicSplitPaneUI with finishDraggingTo that this instance
is contained in.

---

