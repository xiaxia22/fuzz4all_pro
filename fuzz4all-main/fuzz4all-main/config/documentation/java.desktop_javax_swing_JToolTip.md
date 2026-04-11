# Class JToolTip

**Source:** `java.desktop\javax\swing\JToolTip.html`

### Class Description

```java
public class
JToolTip

extends
JComponent

implements
Accessible
```

Used to display a "Tip" for a Component. Typically components provide api
to automate the process of using

ToolTip

s.
For example, any Swing component can use the

JComponent

setToolTipText

method to specify the text
for a standard tooltip. A component that wants to create a custom

ToolTip

display can override

JComponent

's

createToolTip

method and use a subclass of this class.

See

How to Use Tool Tips

in

The Java Tutorial

for further documentation.

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

---

### Field Details

*No entries found.*

### Constructor Details

#### public JToolTip()

Creates a tool tip.

---

### Method Details

#### public
ToolTipUI
getUI()

Returns the L&F object that renders this component.

**Overrides:**
- getUI

in class

JComponent

**Returns:**
- the

ToolTipUI

object that renders this component

---

#### public void updateUI()

Resets the UI property to a value from the current look and feel.

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

Returns the name of the L&F class that renders this component.

**Overrides:**
- getUIClassID

in class

JComponent

**Returns:**
- the string "ToolTipUI"

**See Also:**
- JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### @BeanProperty
(
preferred
=true,

description
="Sets the text of the tooltip")
public void setTipText​(
String
tipText)

Sets the text to show when the tool tip is displayed.
The string

tipText

may be

null

.

**Parameters:**
- tipText

- the

String

to display

---

#### public
String
getTipText()

Returns the text that is shown when the tool tip is displayed.
The returned value may be

null

.

**Returns:**
- the

String

that is displayed

---

#### @BeanProperty
(
description
="Sets the component that the tooltip describes.")
public void setComponent​(
JComponent
c)

Specifies the component that the tooltip describes.
The component

c

may be

null

and will have no effect.

This is a bound property.

**Parameters:**
- c

- the

JComponent

being described

**See Also:**
- JComponent.createToolTip()

---

#### public
JComponent
getComponent()

Returns the component the tooltip applies to.
The returned value may be

null

.

**Returns:**
- the component that the tooltip describes

**See Also:**
- JComponent.createToolTip()

---

#### protected
String
paramString()

Returns a string representation of this

JToolTip

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

JToolTip

---

#### public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this JToolTip.
For tool tips, the AccessibleContext takes the form of an
AccessibleJToolTip.
A new AccessibleJToolTip instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- an AccessibleJToolTip that serves as the
AccessibleContext of this JToolTip

---

### Additional Sections

#### Class JToolTip

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JToolTip

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JToolTip

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JToolTip

javax.swing.JComponent

- javax.swing.JToolTip

javax.swing.JToolTip

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

```java
public class
JToolTip

extends
JComponent

implements
Accessible
```

Used to display a "Tip" for a Component. Typically components provide api
to automate the process of using

ToolTip

s.
For example, any Swing component can use the

JComponent

setToolTipText

method to specify the text
for a standard tooltip. A component that wants to create a custom

ToolTip

display can override

JComponent

's

createToolTip

method and use a subclass of this class.

See

How to Use Tool Tips

in

The Java Tutorial

for further documentation.

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
**See Also:** JComponent.setToolTipText(java.lang.String)

,

JComponent.createToolTip()

,

Serialized Form

public class

JToolTip

extends

JComponent

implements

Accessible

Used to display a "Tip" for a Component. Typically components provide api
to automate the process of using

ToolTip

s.
For example, any Swing component can use the

JComponent

setToolTipText

method to specify the text
for a standard tooltip. A component that wants to create a custom

ToolTip

display can override

JComponent

's

createToolTip

method and use a subclass of this class.

See

How to Use Tool Tips

in

The Java Tutorial

for further documentation.

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

See

How to Use Tool Tips

in

The Java Tutorial

for further documentation.

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

JToolTip.AccessibleJToolTip

This class implements accessibility support for the

JToolTip

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

JToolTip

()

Creates a tool tip.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JToolTip.

JComponent

getComponent

()

Returns the component the tooltip applies to.

String

getTipText

()

Returns the text that is shown when the tool tip is displayed.

ToolTipUI

getUI

()

Returns the L&F object that renders this component.

String

getUIClassID

()

Returns the name of the L&F class that renders this component.

protected

String

paramString

()

Returns a string representation of this

JToolTip

.

void

setComponent

​(

JComponent

c)

Specifies the component that the tooltip describes.

void

setTipText

​(

String

tipText)

Sets the text to show when the tool tip is displayed.

void

updateUI

()

Resets the UI property to a value from the current look and feel.

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

JToolTip.AccessibleJToolTip

This class implements accessibility support for the

JToolTip

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

JToolTip

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

JToolTip

()

Creates a tool tip.

---

#### Constructor Summary

Creates a tool tip.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JToolTip.

JComponent

getComponent

()

Returns the component the tooltip applies to.

String

getTipText

()

Returns the text that is shown when the tool tip is displayed.

ToolTipUI

getUI

()

Returns the L&F object that renders this component.

String

getUIClassID

()

Returns the name of the L&F class that renders this component.

protected

String

paramString

()

Returns a string representation of this

JToolTip

.

void

setComponent

​(

JComponent

c)

Specifies the component that the tooltip describes.

void

setTipText

​(

String

tipText)

Sets the text to show when the tool tip is displayed.

void

updateUI

()

Resets the UI property to a value from the current look and feel.

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

Gets the AccessibleContext associated with this JToolTip.

Returns the component the tooltip applies to.

Returns the text that is shown when the tool tip is displayed.

Returns the L&F object that renders this component.

Returns the name of the L&F class that renders this component.

Returns a string representation of this

JToolTip

.

Specifies the component that the tooltip describes.

Sets the text to show when the tool tip is displayed.

Resets the UI property to a value from the current look and feel.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JToolTip

```java
public JToolTip()
```

Creates a tool tip.

============ METHOD DETAIL ==========

- Method Detail

- getUI

```java
public
ToolTipUI
getUI()
```

Returns the L&F object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

ToolTipUI

object that renders this component

- updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look and feel.

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

Returns the name of the L&F class that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "ToolTipUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- setTipText

```java
@BeanProperty
(
preferred
=true,

description
="Sets the text of the tooltip")
public void setTipText​(
String
tipText)
```

Sets the text to show when the tool tip is displayed.
The string

tipText

may be

null

.

**Parameters:** tipText

- the

String

to display

- getTipText

```java
public
String
getTipText()
```

Returns the text that is shown when the tool tip is displayed.
The returned value may be

null

.

**Returns:** the

String

that is displayed

- setComponent

```java
@BeanProperty
(
description
="Sets the component that the tooltip describes.")
public void setComponent​(
JComponent
c)
```

Specifies the component that the tooltip describes.
The component

c

may be

null

and will have no effect.

This is a bound property.

**Parameters:** c

- the

JComponent

being described
**See Also:** JComponent.createToolTip()

- getComponent

```java
public
JComponent
getComponent()
```

Returns the component the tooltip applies to.
The returned value may be

null

.

**Returns:** the component that the tooltip describes
**See Also:** JComponent.createToolTip()

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JToolTip

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

JToolTip

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JToolTip.
For tool tips, the AccessibleContext takes the form of an
AccessibleJToolTip.
A new AccessibleJToolTip instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJToolTip that serves as the
AccessibleContext of this JToolTip

Constructor Detail

- JToolTip

```java
public JToolTip()
```

Creates a tool tip.

---

#### Constructor Detail

JToolTip

```java
public JToolTip()
```

Creates a tool tip.

---

#### JToolTip

public JToolTip()

Creates a tool tip.

Method Detail

- getUI

```java
public
ToolTipUI
getUI()
```

Returns the L&F object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

ToolTipUI

object that renders this component

- updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look and feel.

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

Returns the name of the L&F class that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "ToolTipUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- setTipText

```java
@BeanProperty
(
preferred
=true,

description
="Sets the text of the tooltip")
public void setTipText​(
String
tipText)
```

Sets the text to show when the tool tip is displayed.
The string

tipText

may be

null

.

**Parameters:** tipText

- the

String

to display

- getTipText

```java
public
String
getTipText()
```

Returns the text that is shown when the tool tip is displayed.
The returned value may be

null

.

**Returns:** the

String

that is displayed

- setComponent

```java
@BeanProperty
(
description
="Sets the component that the tooltip describes.")
public void setComponent​(
JComponent
c)
```

Specifies the component that the tooltip describes.
The component

c

may be

null

and will have no effect.

This is a bound property.

**Parameters:** c

- the

JComponent

being described
**See Also:** JComponent.createToolTip()

- getComponent

```java
public
JComponent
getComponent()
```

Returns the component the tooltip applies to.
The returned value may be

null

.

**Returns:** the component that the tooltip describes
**See Also:** JComponent.createToolTip()

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JToolTip

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

JToolTip

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JToolTip.
For tool tips, the AccessibleContext takes the form of an
AccessibleJToolTip.
A new AccessibleJToolTip instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJToolTip that serves as the
AccessibleContext of this JToolTip

---

#### Method Detail

getUI

```java
public
ToolTipUI
getUI()
```

Returns the L&F object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the

ToolTipUI

object that renders this component

---

#### getUI

public

ToolTipUI

getUI()

Returns the L&F object that renders this component.

updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look and feel.

**Overrides:** updateUI

in class

JComponent
**See Also:** JComponent.updateUI()

---

#### updateUI

public void updateUI()

Resets the UI property to a value from the current look and feel.

getUIClassID

```java
public
String
getUIClassID()
```

Returns the name of the L&F class that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "ToolTipUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### getUIClassID

public

String

getUIClassID()

Returns the name of the L&F class that renders this component.

setTipText

```java
@BeanProperty
(
preferred
=true,

description
="Sets the text of the tooltip")
public void setTipText​(
String
tipText)
```

Sets the text to show when the tool tip is displayed.
The string

tipText

may be

null

.

**Parameters:** tipText

- the

String

to display

---

#### setTipText

@BeanProperty

(

preferred

=true,

description

="Sets the text of the tooltip")
public void setTipText​(

String

tipText)

Sets the text to show when the tool tip is displayed.
The string

tipText

may be

null

.

getTipText

```java
public
String
getTipText()
```

Returns the text that is shown when the tool tip is displayed.
The returned value may be

null

.

**Returns:** the

String

that is displayed

---

#### getTipText

public

String

getTipText()

Returns the text that is shown when the tool tip is displayed.
The returned value may be

null

.

setComponent

```java
@BeanProperty
(
description
="Sets the component that the tooltip describes.")
public void setComponent​(
JComponent
c)
```

Specifies the component that the tooltip describes.
The component

c

may be

null

and will have no effect.

This is a bound property.

**Parameters:** c

- the

JComponent

being described
**See Also:** JComponent.createToolTip()

---

#### setComponent

@BeanProperty

(

description

="Sets the component that the tooltip describes.")
public void setComponent​(

JComponent

c)

Specifies the component that the tooltip describes.
The component

c

may be

null

and will have no effect.

This is a bound property.

This is a bound property.

getComponent

```java
public
JComponent
getComponent()
```

Returns the component the tooltip applies to.
The returned value may be

null

.

**Returns:** the component that the tooltip describes
**See Also:** JComponent.createToolTip()

---

#### getComponent

public

JComponent

getComponent()

Returns the component the tooltip applies to.
The returned value may be

null

.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JToolTip

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

JToolTip

---

#### paramString

protected

String

paramString()

Returns a string representation of this

JToolTip

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
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JToolTip.
For tool tips, the AccessibleContext takes the form of an
AccessibleJToolTip.
A new AccessibleJToolTip instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJToolTip that serves as the
AccessibleContext of this JToolTip

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this JToolTip.
For tool tips, the AccessibleContext takes the form of an
AccessibleJToolTip.
A new AccessibleJToolTip instance is created if necessary.

---

