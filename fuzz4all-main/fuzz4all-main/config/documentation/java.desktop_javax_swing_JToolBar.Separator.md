# Class JToolBar.Separator

**Source:** `java.desktop\javax\swing\JToolBar.Separator.html`

### Class Description

```java
public static class
JToolBar.Separator

extends
JSeparator
```

A toolbar-specific separator. An object with dimension but
no contents used to divide buttons on a tool bar into groups.

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

#### public Separator()

Creates a new toolbar separator with the default size
as defined by the current look and feel.

---

#### public Separator​(
Dimension
size)

Creates a new toolbar separator with the specified size.

**Parameters:**
- size

- the

Dimension

of the separator

---

### Method Details

#### public
String
getUIClassID()

Returns the name of the L&F class that renders this component.

**Overrides:**
- getUIClassID

in class

JSeparator

**Returns:**
- the string "ToolBarSeparatorUI"

**See Also:**
- JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### public void setSeparatorSize​(
Dimension
size)

Sets the size of the separator.

**Parameters:**
- size

- the new

Dimension

of the separator

---

#### public
Dimension
getSeparatorSize()

Returns the size of the separator

**Returns:**
- the

Dimension

object containing the separator's
size (This is a reference, NOT a copy!)

---

#### public
Dimension
getMinimumSize()

Returns the minimum size for the separator.

**Overrides:**
- getMinimumSize

in class

JComponent

**Returns:**
- the

Dimension

object containing the separator's
minimum size

**See Also:**
- JComponent.setMinimumSize(java.awt.Dimension)

,

ComponentUI

---

#### public
Dimension
getMaximumSize()

Returns the maximum size for the separator.

**Overrides:**
- getMaximumSize

in class

JComponent

**Returns:**
- the

Dimension

object containing the separator's
maximum size

**See Also:**
- JComponent.setMaximumSize(java.awt.Dimension)

,

ComponentUI

---

#### public
Dimension
getPreferredSize()

Returns the preferred size for the separator.

**Overrides:**
- getPreferredSize

in class

JComponent

**Returns:**
- the

Dimension

object containing the separator's
preferred size

**See Also:**
- JComponent.setPreferredSize(java.awt.Dimension)

,

ComponentUI

---

### Additional Sections

#### Class JToolBar.Separator

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JSeparator
- - javax.swing.JToolBar.Separator

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JSeparator
- - javax.swing.JToolBar.Separator

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JSeparator
- - javax.swing.JToolBar.Separator

javax.swing.JComponent

- javax.swing.JSeparator
- - javax.swing.JToolBar.Separator

javax.swing.JSeparator

- javax.swing.JToolBar.Separator

javax.swing.JToolBar.Separator

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

,

SwingConstants

**Enclosing class:** JToolBar

```java
public static class
JToolBar.Separator

extends
JSeparator
```

A toolbar-specific separator. An object with dimension but
no contents used to divide buttons on a tool bar into groups.

**See Also:** Serialized Form

public static class

JToolBar.Separator

extends

JSeparator

A toolbar-specific separator. An object with dimension but
no contents used to divide buttons on a tool bar into groups.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.

JSeparator

JSeparator.AccessibleJSeparator

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

Separator

()

Creates a new toolbar separator with the default size
as defined by the current look and feel.

Separator

​(

Dimension

size)

Creates a new toolbar separator with the specified size.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Dimension

getMaximumSize

()

Returns the maximum size for the separator.

Dimension

getMinimumSize

()

Returns the minimum size for the separator.

Dimension

getPreferredSize

()

Returns the preferred size for the separator.

Dimension

getSeparatorSize

()

Returns the size of the separator

String

getUIClassID

()

Returns the name of the L&F class that renders this component.

void

setSeparatorSize

​(

Dimension

size)

Sets the size of the separator.

- Methods declared in class javax.swing.

JSeparator

getAccessibleContext

,

getOrientation

,

getUI

,

paramString

,

setOrientation

,

setUI

,

updateUI

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

- Nested classes/interfaces declared in class javax.swing.

JSeparator

JSeparator.AccessibleJSeparator

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

Nested classes/interfaces declared in class javax.swing.

JSeparator

JSeparator.AccessibleJSeparator

---

#### Nested classes/interfaces declared in class javax.swing. JSeparator

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

Separator

()

Creates a new toolbar separator with the default size
as defined by the current look and feel.

Separator

​(

Dimension

size)

Creates a new toolbar separator with the specified size.

---

#### Constructor Summary

Creates a new toolbar separator with the default size
as defined by the current look and feel.

Creates a new toolbar separator with the specified size.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Dimension

getMaximumSize

()

Returns the maximum size for the separator.

Dimension

getMinimumSize

()

Returns the minimum size for the separator.

Dimension

getPreferredSize

()

Returns the preferred size for the separator.

Dimension

getSeparatorSize

()

Returns the size of the separator

String

getUIClassID

()

Returns the name of the L&F class that renders this component.

void

setSeparatorSize

​(

Dimension

size)

Sets the size of the separator.

- Methods declared in class javax.swing.

JSeparator

getAccessibleContext

,

getOrientation

,

getUI

,

paramString

,

setOrientation

,

setUI

,

updateUI

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

Returns the maximum size for the separator.

Returns the minimum size for the separator.

Returns the preferred size for the separator.

Returns the size of the separator

Returns the name of the L&F class that renders this component.

Sets the size of the separator.

Methods declared in class javax.swing.

JSeparator

getAccessibleContext

,

getOrientation

,

getUI

,

paramString

,

setOrientation

,

setUI

,

updateUI

---

#### Methods declared in class javax.swing. JSeparator

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

- Separator

```java
public Separator()
```

Creates a new toolbar separator with the default size
as defined by the current look and feel.

- Separator

```java
public Separator​(
Dimension
size)
```

Creates a new toolbar separator with the specified size.

**Parameters:** size

- the

Dimension

of the separator

============ METHOD DETAIL ==========

- Method Detail

- getUIClassID

```java
public
String
getUIClassID()
```

Returns the name of the L&F class that renders this component.

**Overrides:** getUIClassID

in class

JSeparator
**Returns:** the string "ToolBarSeparatorUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- setSeparatorSize

```java
public void setSeparatorSize​(
Dimension
size)
```

Sets the size of the separator.

**Parameters:** size

- the new

Dimension

of the separator

- getSeparatorSize

```java
public
Dimension
getSeparatorSize()
```

Returns the size of the separator

**Returns:** the

Dimension

object containing the separator's
size (This is a reference, NOT a copy!)

- getMinimumSize

```java
public
Dimension
getMinimumSize()
```

Returns the minimum size for the separator.

**Overrides:** getMinimumSize

in class

JComponent
**Returns:** the

Dimension

object containing the separator's
minimum size
**See Also:** JComponent.setMinimumSize(java.awt.Dimension)

,

ComponentUI

- getMaximumSize

```java
public
Dimension
getMaximumSize()
```

Returns the maximum size for the separator.

**Overrides:** getMaximumSize

in class

JComponent
**Returns:** the

Dimension

object containing the separator's
maximum size
**See Also:** JComponent.setMaximumSize(java.awt.Dimension)

,

ComponentUI

- getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Returns the preferred size for the separator.

**Overrides:** getPreferredSize

in class

JComponent
**Returns:** the

Dimension

object containing the separator's
preferred size
**See Also:** JComponent.setPreferredSize(java.awt.Dimension)

,

ComponentUI

Constructor Detail

- Separator

```java
public Separator()
```

Creates a new toolbar separator with the default size
as defined by the current look and feel.

- Separator

```java
public Separator​(
Dimension
size)
```

Creates a new toolbar separator with the specified size.

**Parameters:** size

- the

Dimension

of the separator

---

#### Constructor Detail

Separator

```java
public Separator()
```

Creates a new toolbar separator with the default size
as defined by the current look and feel.

---

#### Separator

public Separator()

Creates a new toolbar separator with the default size
as defined by the current look and feel.

Separator

```java
public Separator​(
Dimension
size)
```

Creates a new toolbar separator with the specified size.

**Parameters:** size

- the

Dimension

of the separator

---

#### Separator

public Separator​(

Dimension

size)

Creates a new toolbar separator with the specified size.

Method Detail

- getUIClassID

```java
public
String
getUIClassID()
```

Returns the name of the L&F class that renders this component.

**Overrides:** getUIClassID

in class

JSeparator
**Returns:** the string "ToolBarSeparatorUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- setSeparatorSize

```java
public void setSeparatorSize​(
Dimension
size)
```

Sets the size of the separator.

**Parameters:** size

- the new

Dimension

of the separator

- getSeparatorSize

```java
public
Dimension
getSeparatorSize()
```

Returns the size of the separator

**Returns:** the

Dimension

object containing the separator's
size (This is a reference, NOT a copy!)

- getMinimumSize

```java
public
Dimension
getMinimumSize()
```

Returns the minimum size for the separator.

**Overrides:** getMinimumSize

in class

JComponent
**Returns:** the

Dimension

object containing the separator's
minimum size
**See Also:** JComponent.setMinimumSize(java.awt.Dimension)

,

ComponentUI

- getMaximumSize

```java
public
Dimension
getMaximumSize()
```

Returns the maximum size for the separator.

**Overrides:** getMaximumSize

in class

JComponent
**Returns:** the

Dimension

object containing the separator's
maximum size
**See Also:** JComponent.setMaximumSize(java.awt.Dimension)

,

ComponentUI

- getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Returns the preferred size for the separator.

**Overrides:** getPreferredSize

in class

JComponent
**Returns:** the

Dimension

object containing the separator's
preferred size
**See Also:** JComponent.setPreferredSize(java.awt.Dimension)

,

ComponentUI

---

#### Method Detail

getUIClassID

```java
public
String
getUIClassID()
```

Returns the name of the L&F class that renders this component.

**Overrides:** getUIClassID

in class

JSeparator
**Returns:** the string "ToolBarSeparatorUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### getUIClassID

public

String

getUIClassID()

Returns the name of the L&F class that renders this component.

setSeparatorSize

```java
public void setSeparatorSize​(
Dimension
size)
```

Sets the size of the separator.

**Parameters:** size

- the new

Dimension

of the separator

---

#### setSeparatorSize

public void setSeparatorSize​(

Dimension

size)

Sets the size of the separator.

getSeparatorSize

```java
public
Dimension
getSeparatorSize()
```

Returns the size of the separator

**Returns:** the

Dimension

object containing the separator's
size (This is a reference, NOT a copy!)

---

#### getSeparatorSize

public

Dimension

getSeparatorSize()

Returns the size of the separator

getMinimumSize

```java
public
Dimension
getMinimumSize()
```

Returns the minimum size for the separator.

**Overrides:** getMinimumSize

in class

JComponent
**Returns:** the

Dimension

object containing the separator's
minimum size
**See Also:** JComponent.setMinimumSize(java.awt.Dimension)

,

ComponentUI

---

#### getMinimumSize

public

Dimension

getMinimumSize()

Returns the minimum size for the separator.

getMaximumSize

```java
public
Dimension
getMaximumSize()
```

Returns the maximum size for the separator.

**Overrides:** getMaximumSize

in class

JComponent
**Returns:** the

Dimension

object containing the separator's
maximum size
**See Also:** JComponent.setMaximumSize(java.awt.Dimension)

,

ComponentUI

---

#### getMaximumSize

public

Dimension

getMaximumSize()

Returns the maximum size for the separator.

getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Returns the preferred size for the separator.

**Overrides:** getPreferredSize

in class

JComponent
**Returns:** the

Dimension

object containing the separator's
preferred size
**See Also:** JComponent.setPreferredSize(java.awt.Dimension)

,

ComponentUI

---

#### getPreferredSize

public

Dimension

getPreferredSize()

Returns the preferred size for the separator.

---

