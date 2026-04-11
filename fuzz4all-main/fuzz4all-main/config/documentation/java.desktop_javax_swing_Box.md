# Class Box

**Source:** `java.desktop\javax\swing\Box.html`

### Class Description

```java
@JavaBean
(
defaultProperty
="accessibleContext")
public class
Box

extends
JComponent

implements
Accessible
```

A lightweight container
that uses a BoxLayout object as its layout manager.
Box provides several class methods
that are useful for containers using BoxLayout --
even non-Box containers.

The

Box

class can create several kinds
of invisible components
that affect layout:
glue, struts, and rigid areas.
If all the components your

Box

contains
have a fixed size,
you might want to use a glue component
(returned by

createGlue

)
to control the components' positions.
If you need a fixed amount of space between two components,
try using a strut
(

createHorizontalStrut

or

createVerticalStrut

).
If you need an invisible component
that always takes up the same amount of space,
get it by invoking

createRigidArea

.

If you are implementing a

BoxLayout

you
can find further information and examples in

How to Use BoxLayout

,
a section in

The Java Tutorial.

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

---

### Field Details

*No entries found.*

### Constructor Details

#### public Box​(int axis)

Creates a

Box

that displays its components
along the specified axis.

**Parameters:**
- axis

- can be

BoxLayout.X_AXIS

,

BoxLayout.Y_AXIS

,

BoxLayout.LINE_AXIS

or

BoxLayout.PAGE_AXIS

.

**Throws:**
- AWTError

- if the

axis

is invalid

**See Also:**
- createHorizontalBox()

,

createVerticalBox()

---

### Method Details

#### public static
Box
createHorizontalBox()

Creates a

Box

that displays its components
from left to right. If you want a

Box

that
respects the component orientation you should create the

Box

using the constructor and pass in

BoxLayout.LINE_AXIS

, eg:

```java
Box lineBox = new Box(BoxLayout.LINE_AXIS);
```

**Returns:**
- the box

---

#### public static
Box
createVerticalBox()

Creates a

Box

that displays its components
from top to bottom. If you want a

Box

that
respects the component orientation you should create the

Box

using the constructor and pass in

BoxLayout.PAGE_AXIS

, eg:

```java
Box lineBox = new Box(BoxLayout.PAGE_AXIS);
```

**Returns:**
- the box

---

#### public static
Component
createRigidArea​(
Dimension
d)

Creates an invisible component that's always the specified size.

WHEN WOULD YOU USE THIS AS OPPOSED TO A STRUT?

**Parameters:**
- d

- the dimensions of the invisible component

**Returns:**
- the component

**See Also:**
- createGlue()

,

createHorizontalStrut(int)

,

createVerticalStrut(int)

---

#### public static
Component
createHorizontalStrut​(int width)

Creates an invisible, fixed-width component.
In a horizontal box,
you typically use this method
to force a certain amount of space between two components.
In a vertical box,
you might use this method
to force the box to be at least the specified width.
The invisible component has no height
unless excess space is available,
in which case it takes its share of available space,
just like any other component that has no maximum height.

**Parameters:**
- width

- the width of the invisible component, in pixels >= 0

**Returns:**
- the component

**See Also:**
- createVerticalStrut(int)

,

createGlue()

,

createRigidArea(java.awt.Dimension)

---

#### public static
Component
createVerticalStrut​(int height)

Creates an invisible, fixed-height component.
In a vertical box,
you typically use this method
to force a certain amount of space between two components.
In a horizontal box,
you might use this method
to force the box to be at least the specified height.
The invisible component has no width
unless excess space is available,
in which case it takes its share of available space,
just like any other component that has no maximum width.

**Parameters:**
- height

- the height of the invisible component, in pixels >= 0

**Returns:**
- the component

**See Also:**
- createHorizontalStrut(int)

,

createGlue()

,

createRigidArea(java.awt.Dimension)

---

#### public static
Component
createGlue()

Creates an invisible "glue" component
that can be useful in a Box
whose visible components have a maximum width
(for a horizontal box)
or height (for a vertical box).
You can think of the glue component
as being a gooey substance
that expands as much as necessary
to fill the space between its neighboring components.

For example, suppose you have
a horizontal box that contains two fixed-size components.
If the box gets extra space,
the fixed-size components won't become larger,
so where does the extra space go?
Without glue,
the extra space goes to the right of the second component.
If you put glue between the fixed-size components,
then the extra space goes there.
If you put glue before the first fixed-size component,
the extra space goes there,
and the fixed-size components are shoved against the right
edge of the box.
If you put glue before the first fixed-size component
and after the second fixed-size component,
the fixed-size components are centered in the box.

To use glue,
call

Box.createGlue

and add the returned component to a container.
The glue component has no minimum or preferred size,
so it takes no space unless excess space is available.
If excess space is available,
then the glue component takes its share of available
horizontal or vertical space,
just like any other component that has no maximum width or height.

**Returns:**
- the component

---

#### public static
Component
createHorizontalGlue()

Creates a horizontal glue component.

**Returns:**
- the component

---

#### public static
Component
createVerticalGlue()

Creates a vertical glue component.

**Returns:**
- the component

---

#### public void setLayout​(
LayoutManager
l)

Throws an AWTError, since a Box can use only a BoxLayout.

**Overrides:**
- setLayout

in class

Container

**Parameters:**
- l

- the layout manager to use

**See Also:**
- Container.doLayout()

,

Container.getLayout()

,

Container.invalidate()

---

#### protected void paintComponent​(
Graphics
g)

Paints this

Box

. If this

Box

has a UI this
method invokes super's implementation, otherwise if this

Box

is opaque the

Graphics

is filled
using the background.

**Overrides:**
- paintComponent

in class

JComponent

**Parameters:**
- g

- the

Graphics

to paint to

**Throws:**
- NullPointerException

- if

g

is null

**See Also:**
- JComponent.paint(java.awt.Graphics)

,

ComponentUI

**Since:**
- 1.6

---

#### @BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this Box.
For boxes, the AccessibleContext takes the form of an
AccessibleBox.
A new AccessibleAWTBox instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- an AccessibleBox that serves as the
AccessibleContext of this Box

---

### Additional Sections

#### Class Box

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.Box

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.Box

java.awt.Container

- javax.swing.JComponent
- - javax.swing.Box

javax.swing.JComponent

- javax.swing.Box

javax.swing.Box

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

```java
@JavaBean
(
defaultProperty
="accessibleContext")
public class
Box

extends
JComponent

implements
Accessible
```

A lightweight container
that uses a BoxLayout object as its layout manager.
Box provides several class methods
that are useful for containers using BoxLayout --
even non-Box containers.

The

Box

class can create several kinds
of invisible components
that affect layout:
glue, struts, and rigid areas.
If all the components your

Box

contains
have a fixed size,
you might want to use a glue component
(returned by

createGlue

)
to control the components' positions.
If you need a fixed amount of space between two components,
try using a strut
(

createHorizontalStrut

or

createVerticalStrut

).
If you need an invisible component
that always takes up the same amount of space,
get it by invoking

createRigidArea

.

If you are implementing a

BoxLayout

you
can find further information and examples in

How to Use BoxLayout

,
a section in

The Java Tutorial.

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
**See Also:** BoxLayout

,

Serialized Form

@JavaBean

(

defaultProperty

="accessibleContext")
public class

Box

extends

JComponent

implements

Accessible

A lightweight container
that uses a BoxLayout object as its layout manager.
Box provides several class methods
that are useful for containers using BoxLayout --
even non-Box containers.

The

Box

class can create several kinds
of invisible components
that affect layout:
glue, struts, and rigid areas.
If all the components your

Box

contains
have a fixed size,
you might want to use a glue component
(returned by

createGlue

)
to control the components' positions.
If you need a fixed amount of space between two components,
try using a strut
(

createHorizontalStrut

or

createVerticalStrut

).
If you need an invisible component
that always takes up the same amount of space,
get it by invoking

createRigidArea

.

If you are implementing a

BoxLayout

you
can find further information and examples in

How to Use BoxLayout

,
a section in

The Java Tutorial.

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

The

Box

class can create several kinds
of invisible components
that affect layout:
glue, struts, and rigid areas.
If all the components your

Box

contains
have a fixed size,
you might want to use a glue component
(returned by

createGlue

)
to control the components' positions.
If you need a fixed amount of space between two components,
try using a strut
(

createHorizontalStrut

or

createVerticalStrut

).
If you need an invisible component
that always takes up the same amount of space,
get it by invoking

createRigidArea

.

If you are implementing a

BoxLayout

you
can find further information and examples in

How to Use BoxLayout

,
a section in

The Java Tutorial.

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

If you are implementing a

BoxLayout

you
can find further information and examples in

How to Use BoxLayout

,
a section in

The Java Tutorial.

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

Box.AccessibleBox

This class implements accessibility support for the

Box

class.

static class

Box.Filler

An implementation of a lightweight component that participates in
layout but has no view.

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

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Box

​(int axis)

Creates a

Box

that displays its components
along the specified axis.

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

Component

createGlue

()

Creates an invisible "glue" component
that can be useful in a Box
whose visible components have a maximum width
(for a horizontal box)
or height (for a vertical box).

static

Box

createHorizontalBox

()

Creates a

Box

that displays its components
from left to right.

static

Component

createHorizontalGlue

()

Creates a horizontal glue component.

static

Component

createHorizontalStrut

​(int width)

Creates an invisible, fixed-width component.

static

Component

createRigidArea

​(

Dimension

d)

Creates an invisible component that's always the specified size.

static

Box

createVerticalBox

()

Creates a

Box

that displays its components
from top to bottom.

static

Component

createVerticalGlue

()

Creates a vertical glue component.

static

Component

createVerticalStrut

​(int height)

Creates an invisible, fixed-height component.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this Box.

protected void

paintComponent

​(

Graphics

g)

Paints this

Box

.

void

setLayout

​(

LayoutManager

l)

Throws an AWTError, since a Box can use only a BoxLayout.

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

getUI

,

getUIClassID

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

paintImmediately

,

paintImmediately

,

paramString

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

,

updateUI

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

Box.AccessibleBox

This class implements accessibility support for the

Box

class.

static class

Box.Filler

An implementation of a lightweight component that participates in
layout but has no view.

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

Box

class.

An implementation of a lightweight component that participates in
layout but has no view.

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

Constructor Summary

Constructors

Constructor

Description

Box

​(int axis)

Creates a

Box

that displays its components
along the specified axis.

---

#### Constructor Summary

Creates a

Box

that displays its components
along the specified axis.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

Component

createGlue

()

Creates an invisible "glue" component
that can be useful in a Box
whose visible components have a maximum width
(for a horizontal box)
or height (for a vertical box).

static

Box

createHorizontalBox

()

Creates a

Box

that displays its components
from left to right.

static

Component

createHorizontalGlue

()

Creates a horizontal glue component.

static

Component

createHorizontalStrut

​(int width)

Creates an invisible, fixed-width component.

static

Component

createRigidArea

​(

Dimension

d)

Creates an invisible component that's always the specified size.

static

Box

createVerticalBox

()

Creates a

Box

that displays its components
from top to bottom.

static

Component

createVerticalGlue

()

Creates a vertical glue component.

static

Component

createVerticalStrut

​(int height)

Creates an invisible, fixed-height component.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this Box.

protected void

paintComponent

​(

Graphics

g)

Paints this

Box

.

void

setLayout

​(

LayoutManager

l)

Throws an AWTError, since a Box can use only a BoxLayout.

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

getUI

,

getUIClassID

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

paintImmediately

,

paintImmediately

,

paramString

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

,

updateUI

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

Creates an invisible "glue" component
that can be useful in a Box
whose visible components have a maximum width
(for a horizontal box)
or height (for a vertical box).

Creates a

Box

that displays its components
from left to right.

Creates a horizontal glue component.

Creates an invisible, fixed-width component.

Creates an invisible component that's always the specified size.

Creates a

Box

that displays its components
from top to bottom.

Creates a vertical glue component.

Creates an invisible, fixed-height component.

Gets the AccessibleContext associated with this Box.

Paints this

Box

.

Throws an AWTError, since a Box can use only a BoxLayout.

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

getUI

,

getUIClassID

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

paintImmediately

,

paintImmediately

,

paramString

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

,

updateUI

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

- Box

```java
public Box​(int axis)
```

Creates a

Box

that displays its components
along the specified axis.

**Parameters:** axis

- can be

BoxLayout.X_AXIS

,

BoxLayout.Y_AXIS

,

BoxLayout.LINE_AXIS

or

BoxLayout.PAGE_AXIS

.
**Throws:** AWTError

- if the

axis

is invalid
**See Also:** createHorizontalBox()

,

createVerticalBox()

============ METHOD DETAIL ==========

- Method Detail

- createHorizontalBox

```java
public static
Box
createHorizontalBox()
```

Creates a

Box

that displays its components
from left to right. If you want a

Box

that
respects the component orientation you should create the

Box

using the constructor and pass in

BoxLayout.LINE_AXIS

, eg:

```java
Box lineBox = new Box(BoxLayout.LINE_AXIS);
```

**Returns:** the box

- createVerticalBox

```java
public static
Box
createVerticalBox()
```

Creates a

Box

that displays its components
from top to bottom. If you want a

Box

that
respects the component orientation you should create the

Box

using the constructor and pass in

BoxLayout.PAGE_AXIS

, eg:

```java
Box lineBox = new Box(BoxLayout.PAGE_AXIS);
```

**Returns:** the box

- createRigidArea

```java
public static
Component
createRigidArea​(
Dimension
d)
```

Creates an invisible component that's always the specified size.

WHEN WOULD YOU USE THIS AS OPPOSED TO A STRUT?

**Parameters:** d

- the dimensions of the invisible component
**Returns:** the component
**See Also:** createGlue()

,

createHorizontalStrut(int)

,

createVerticalStrut(int)

- createHorizontalStrut

```java
public static
Component
createHorizontalStrut​(int width)
```

Creates an invisible, fixed-width component.
In a horizontal box,
you typically use this method
to force a certain amount of space between two components.
In a vertical box,
you might use this method
to force the box to be at least the specified width.
The invisible component has no height
unless excess space is available,
in which case it takes its share of available space,
just like any other component that has no maximum height.

**Parameters:** width

- the width of the invisible component, in pixels >= 0
**Returns:** the component
**See Also:** createVerticalStrut(int)

,

createGlue()

,

createRigidArea(java.awt.Dimension)

- createVerticalStrut

```java
public static
Component
createVerticalStrut​(int height)
```

Creates an invisible, fixed-height component.
In a vertical box,
you typically use this method
to force a certain amount of space between two components.
In a horizontal box,
you might use this method
to force the box to be at least the specified height.
The invisible component has no width
unless excess space is available,
in which case it takes its share of available space,
just like any other component that has no maximum width.

**Parameters:** height

- the height of the invisible component, in pixels >= 0
**Returns:** the component
**See Also:** createHorizontalStrut(int)

,

createGlue()

,

createRigidArea(java.awt.Dimension)

- createGlue

```java
public static
Component
createGlue()
```

Creates an invisible "glue" component
that can be useful in a Box
whose visible components have a maximum width
(for a horizontal box)
or height (for a vertical box).
You can think of the glue component
as being a gooey substance
that expands as much as necessary
to fill the space between its neighboring components.

For example, suppose you have
a horizontal box that contains two fixed-size components.
If the box gets extra space,
the fixed-size components won't become larger,
so where does the extra space go?
Without glue,
the extra space goes to the right of the second component.
If you put glue between the fixed-size components,
then the extra space goes there.
If you put glue before the first fixed-size component,
the extra space goes there,
and the fixed-size components are shoved against the right
edge of the box.
If you put glue before the first fixed-size component
and after the second fixed-size component,
the fixed-size components are centered in the box.

To use glue,
call

Box.createGlue

and add the returned component to a container.
The glue component has no minimum or preferred size,
so it takes no space unless excess space is available.
If excess space is available,
then the glue component takes its share of available
horizontal or vertical space,
just like any other component that has no maximum width or height.

**Returns:** the component

- createHorizontalGlue

```java
public static
Component
createHorizontalGlue()
```

Creates a horizontal glue component.

**Returns:** the component

- createVerticalGlue

```java
public static
Component
createVerticalGlue()
```

Creates a vertical glue component.

**Returns:** the component

- setLayout

```java
public void setLayout​(
LayoutManager
l)
```

Throws an AWTError, since a Box can use only a BoxLayout.

**Overrides:** setLayout

in class

Container
**Parameters:** l

- the layout manager to use
**See Also:** Container.doLayout()

,

Container.getLayout()

,

Container.invalidate()

- paintComponent

```java
protected void paintComponent​(
Graphics
g)
```

Paints this

Box

. If this

Box

has a UI this
method invokes super's implementation, otherwise if this

Box

is opaque the

Graphics

is filled
using the background.

**Overrides:** paintComponent

in class

JComponent
**Parameters:** g

- the

Graphics

to paint to
**Throws:** NullPointerException

- if

g

is null
**Since:** 1.6
**See Also:** JComponent.paint(java.awt.Graphics)

,

ComponentUI

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

Gets the AccessibleContext associated with this Box.
For boxes, the AccessibleContext takes the form of an
AccessibleBox.
A new AccessibleAWTBox instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleBox that serves as the
AccessibleContext of this Box

Constructor Detail

- Box

```java
public Box​(int axis)
```

Creates a

Box

that displays its components
along the specified axis.

**Parameters:** axis

- can be

BoxLayout.X_AXIS

,

BoxLayout.Y_AXIS

,

BoxLayout.LINE_AXIS

or

BoxLayout.PAGE_AXIS

.
**Throws:** AWTError

- if the

axis

is invalid
**See Also:** createHorizontalBox()

,

createVerticalBox()

---

#### Constructor Detail

Box

```java
public Box​(int axis)
```

Creates a

Box

that displays its components
along the specified axis.

**Parameters:** axis

- can be

BoxLayout.X_AXIS

,

BoxLayout.Y_AXIS

,

BoxLayout.LINE_AXIS

or

BoxLayout.PAGE_AXIS

.
**Throws:** AWTError

- if the

axis

is invalid
**See Also:** createHorizontalBox()

,

createVerticalBox()

---

#### Box

public Box​(int axis)

Creates a

Box

that displays its components
along the specified axis.

Method Detail

- createHorizontalBox

```java
public static
Box
createHorizontalBox()
```

Creates a

Box

that displays its components
from left to right. If you want a

Box

that
respects the component orientation you should create the

Box

using the constructor and pass in

BoxLayout.LINE_AXIS

, eg:

```java
Box lineBox = new Box(BoxLayout.LINE_AXIS);
```

**Returns:** the box

- createVerticalBox

```java
public static
Box
createVerticalBox()
```

Creates a

Box

that displays its components
from top to bottom. If you want a

Box

that
respects the component orientation you should create the

Box

using the constructor and pass in

BoxLayout.PAGE_AXIS

, eg:

```java
Box lineBox = new Box(BoxLayout.PAGE_AXIS);
```

**Returns:** the box

- createRigidArea

```java
public static
Component
createRigidArea​(
Dimension
d)
```

Creates an invisible component that's always the specified size.

WHEN WOULD YOU USE THIS AS OPPOSED TO A STRUT?

**Parameters:** d

- the dimensions of the invisible component
**Returns:** the component
**See Also:** createGlue()

,

createHorizontalStrut(int)

,

createVerticalStrut(int)

- createHorizontalStrut

```java
public static
Component
createHorizontalStrut​(int width)
```

Creates an invisible, fixed-width component.
In a horizontal box,
you typically use this method
to force a certain amount of space between two components.
In a vertical box,
you might use this method
to force the box to be at least the specified width.
The invisible component has no height
unless excess space is available,
in which case it takes its share of available space,
just like any other component that has no maximum height.

**Parameters:** width

- the width of the invisible component, in pixels >= 0
**Returns:** the component
**See Also:** createVerticalStrut(int)

,

createGlue()

,

createRigidArea(java.awt.Dimension)

- createVerticalStrut

```java
public static
Component
createVerticalStrut​(int height)
```

Creates an invisible, fixed-height component.
In a vertical box,
you typically use this method
to force a certain amount of space between two components.
In a horizontal box,
you might use this method
to force the box to be at least the specified height.
The invisible component has no width
unless excess space is available,
in which case it takes its share of available space,
just like any other component that has no maximum width.

**Parameters:** height

- the height of the invisible component, in pixels >= 0
**Returns:** the component
**See Also:** createHorizontalStrut(int)

,

createGlue()

,

createRigidArea(java.awt.Dimension)

- createGlue

```java
public static
Component
createGlue()
```

Creates an invisible "glue" component
that can be useful in a Box
whose visible components have a maximum width
(for a horizontal box)
or height (for a vertical box).
You can think of the glue component
as being a gooey substance
that expands as much as necessary
to fill the space between its neighboring components.

For example, suppose you have
a horizontal box that contains two fixed-size components.
If the box gets extra space,
the fixed-size components won't become larger,
so where does the extra space go?
Without glue,
the extra space goes to the right of the second component.
If you put glue between the fixed-size components,
then the extra space goes there.
If you put glue before the first fixed-size component,
the extra space goes there,
and the fixed-size components are shoved against the right
edge of the box.
If you put glue before the first fixed-size component
and after the second fixed-size component,
the fixed-size components are centered in the box.

To use glue,
call

Box.createGlue

and add the returned component to a container.
The glue component has no minimum or preferred size,
so it takes no space unless excess space is available.
If excess space is available,
then the glue component takes its share of available
horizontal or vertical space,
just like any other component that has no maximum width or height.

**Returns:** the component

- createHorizontalGlue

```java
public static
Component
createHorizontalGlue()
```

Creates a horizontal glue component.

**Returns:** the component

- createVerticalGlue

```java
public static
Component
createVerticalGlue()
```

Creates a vertical glue component.

**Returns:** the component

- setLayout

```java
public void setLayout​(
LayoutManager
l)
```

Throws an AWTError, since a Box can use only a BoxLayout.

**Overrides:** setLayout

in class

Container
**Parameters:** l

- the layout manager to use
**See Also:** Container.doLayout()

,

Container.getLayout()

,

Container.invalidate()

- paintComponent

```java
protected void paintComponent​(
Graphics
g)
```

Paints this

Box

. If this

Box

has a UI this
method invokes super's implementation, otherwise if this

Box

is opaque the

Graphics

is filled
using the background.

**Overrides:** paintComponent

in class

JComponent
**Parameters:** g

- the

Graphics

to paint to
**Throws:** NullPointerException

- if

g

is null
**Since:** 1.6
**See Also:** JComponent.paint(java.awt.Graphics)

,

ComponentUI

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

Gets the AccessibleContext associated with this Box.
For boxes, the AccessibleContext takes the form of an
AccessibleBox.
A new AccessibleAWTBox instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleBox that serves as the
AccessibleContext of this Box

---

#### Method Detail

createHorizontalBox

```java
public static
Box
createHorizontalBox()
```

Creates a

Box

that displays its components
from left to right. If you want a

Box

that
respects the component orientation you should create the

Box

using the constructor and pass in

BoxLayout.LINE_AXIS

, eg:

```java
Box lineBox = new Box(BoxLayout.LINE_AXIS);
```

**Returns:** the box

---

#### createHorizontalBox

public static

Box

createHorizontalBox()

Creates a

Box

that displays its components
from left to right. If you want a

Box

that
respects the component orientation you should create the

Box

using the constructor and pass in

BoxLayout.LINE_AXIS

, eg:

```java
Box lineBox = new Box(BoxLayout.LINE_AXIS);
```

Box lineBox = new Box(BoxLayout.LINE_AXIS);

createVerticalBox

```java
public static
Box
createVerticalBox()
```

Creates a

Box

that displays its components
from top to bottom. If you want a

Box

that
respects the component orientation you should create the

Box

using the constructor and pass in

BoxLayout.PAGE_AXIS

, eg:

```java
Box lineBox = new Box(BoxLayout.PAGE_AXIS);
```

**Returns:** the box

---

#### createVerticalBox

public static

Box

createVerticalBox()

Creates a

Box

that displays its components
from top to bottom. If you want a

Box

that
respects the component orientation you should create the

Box

using the constructor and pass in

BoxLayout.PAGE_AXIS

, eg:

```java
Box lineBox = new Box(BoxLayout.PAGE_AXIS);
```

Box lineBox = new Box(BoxLayout.PAGE_AXIS);

createRigidArea

```java
public static
Component
createRigidArea​(
Dimension
d)
```

Creates an invisible component that's always the specified size.

WHEN WOULD YOU USE THIS AS OPPOSED TO A STRUT?

**Parameters:** d

- the dimensions of the invisible component
**Returns:** the component
**See Also:** createGlue()

,

createHorizontalStrut(int)

,

createVerticalStrut(int)

---

#### createRigidArea

public static

Component

createRigidArea​(

Dimension

d)

Creates an invisible component that's always the specified size.

WHEN WOULD YOU USE THIS AS OPPOSED TO A STRUT?

createHorizontalStrut

```java
public static
Component
createHorizontalStrut​(int width)
```

Creates an invisible, fixed-width component.
In a horizontal box,
you typically use this method
to force a certain amount of space between two components.
In a vertical box,
you might use this method
to force the box to be at least the specified width.
The invisible component has no height
unless excess space is available,
in which case it takes its share of available space,
just like any other component that has no maximum height.

**Parameters:** width

- the width of the invisible component, in pixels >= 0
**Returns:** the component
**See Also:** createVerticalStrut(int)

,

createGlue()

,

createRigidArea(java.awt.Dimension)

---

#### createHorizontalStrut

public static

Component

createHorizontalStrut​(int width)

Creates an invisible, fixed-width component.
In a horizontal box,
you typically use this method
to force a certain amount of space between two components.
In a vertical box,
you might use this method
to force the box to be at least the specified width.
The invisible component has no height
unless excess space is available,
in which case it takes its share of available space,
just like any other component that has no maximum height.

createVerticalStrut

```java
public static
Component
createVerticalStrut​(int height)
```

Creates an invisible, fixed-height component.
In a vertical box,
you typically use this method
to force a certain amount of space between two components.
In a horizontal box,
you might use this method
to force the box to be at least the specified height.
The invisible component has no width
unless excess space is available,
in which case it takes its share of available space,
just like any other component that has no maximum width.

**Parameters:** height

- the height of the invisible component, in pixels >= 0
**Returns:** the component
**See Also:** createHorizontalStrut(int)

,

createGlue()

,

createRigidArea(java.awt.Dimension)

---

#### createVerticalStrut

public static

Component

createVerticalStrut​(int height)

Creates an invisible, fixed-height component.
In a vertical box,
you typically use this method
to force a certain amount of space between two components.
In a horizontal box,
you might use this method
to force the box to be at least the specified height.
The invisible component has no width
unless excess space is available,
in which case it takes its share of available space,
just like any other component that has no maximum width.

createGlue

```java
public static
Component
createGlue()
```

Creates an invisible "glue" component
that can be useful in a Box
whose visible components have a maximum width
(for a horizontal box)
or height (for a vertical box).
You can think of the glue component
as being a gooey substance
that expands as much as necessary
to fill the space between its neighboring components.

For example, suppose you have
a horizontal box that contains two fixed-size components.
If the box gets extra space,
the fixed-size components won't become larger,
so where does the extra space go?
Without glue,
the extra space goes to the right of the second component.
If you put glue between the fixed-size components,
then the extra space goes there.
If you put glue before the first fixed-size component,
the extra space goes there,
and the fixed-size components are shoved against the right
edge of the box.
If you put glue before the first fixed-size component
and after the second fixed-size component,
the fixed-size components are centered in the box.

To use glue,
call

Box.createGlue

and add the returned component to a container.
The glue component has no minimum or preferred size,
so it takes no space unless excess space is available.
If excess space is available,
then the glue component takes its share of available
horizontal or vertical space,
just like any other component that has no maximum width or height.

**Returns:** the component

---

#### createGlue

public static

Component

createGlue()

Creates an invisible "glue" component
that can be useful in a Box
whose visible components have a maximum width
(for a horizontal box)
or height (for a vertical box).
You can think of the glue component
as being a gooey substance
that expands as much as necessary
to fill the space between its neighboring components.

For example, suppose you have
a horizontal box that contains two fixed-size components.
If the box gets extra space,
the fixed-size components won't become larger,
so where does the extra space go?
Without glue,
the extra space goes to the right of the second component.
If you put glue between the fixed-size components,
then the extra space goes there.
If you put glue before the first fixed-size component,
the extra space goes there,
and the fixed-size components are shoved against the right
edge of the box.
If you put glue before the first fixed-size component
and after the second fixed-size component,
the fixed-size components are centered in the box.

To use glue,
call

Box.createGlue

and add the returned component to a container.
The glue component has no minimum or preferred size,
so it takes no space unless excess space is available.
If excess space is available,
then the glue component takes its share of available
horizontal or vertical space,
just like any other component that has no maximum width or height.

For example, suppose you have
a horizontal box that contains two fixed-size components.
If the box gets extra space,
the fixed-size components won't become larger,
so where does the extra space go?
Without glue,
the extra space goes to the right of the second component.
If you put glue between the fixed-size components,
then the extra space goes there.
If you put glue before the first fixed-size component,
the extra space goes there,
and the fixed-size components are shoved against the right
edge of the box.
If you put glue before the first fixed-size component
and after the second fixed-size component,
the fixed-size components are centered in the box.

To use glue,
call

Box.createGlue

and add the returned component to a container.
The glue component has no minimum or preferred size,
so it takes no space unless excess space is available.
If excess space is available,
then the glue component takes its share of available
horizontal or vertical space,
just like any other component that has no maximum width or height.

To use glue,
call

Box.createGlue

and add the returned component to a container.
The glue component has no minimum or preferred size,
so it takes no space unless excess space is available.
If excess space is available,
then the glue component takes its share of available
horizontal or vertical space,
just like any other component that has no maximum width or height.

createHorizontalGlue

```java
public static
Component
createHorizontalGlue()
```

Creates a horizontal glue component.

**Returns:** the component

---

#### createHorizontalGlue

public static

Component

createHorizontalGlue()

Creates a horizontal glue component.

createVerticalGlue

```java
public static
Component
createVerticalGlue()
```

Creates a vertical glue component.

**Returns:** the component

---

#### createVerticalGlue

public static

Component

createVerticalGlue()

Creates a vertical glue component.

setLayout

```java
public void setLayout​(
LayoutManager
l)
```

Throws an AWTError, since a Box can use only a BoxLayout.

**Overrides:** setLayout

in class

Container
**Parameters:** l

- the layout manager to use
**See Also:** Container.doLayout()

,

Container.getLayout()

,

Container.invalidate()

---

#### setLayout

public void setLayout​(

LayoutManager

l)

Throws an AWTError, since a Box can use only a BoxLayout.

paintComponent

```java
protected void paintComponent​(
Graphics
g)
```

Paints this

Box

. If this

Box

has a UI this
method invokes super's implementation, otherwise if this

Box

is opaque the

Graphics

is filled
using the background.

**Overrides:** paintComponent

in class

JComponent
**Parameters:** g

- the

Graphics

to paint to
**Throws:** NullPointerException

- if

g

is null
**Since:** 1.6
**See Also:** JComponent.paint(java.awt.Graphics)

,

ComponentUI

---

#### paintComponent

protected void paintComponent​(

Graphics

g)

Paints this

Box

. If this

Box

has a UI this
method invokes super's implementation, otherwise if this

Box

is opaque the

Graphics

is filled
using the background.

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

Gets the AccessibleContext associated with this Box.
For boxes, the AccessibleContext takes the form of an
AccessibleBox.
A new AccessibleAWTBox instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleBox that serves as the
AccessibleContext of this Box

---

#### getAccessibleContext

@BeanProperty

(

bound

=false)
public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this Box.
For boxes, the AccessibleContext takes the form of an
AccessibleBox.
A new AccessibleAWTBox instance is created if necessary.

---

