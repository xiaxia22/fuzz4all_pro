# Class MetalInternalFrameTitlePane

**Source:** `java.desktop\javax\swing\plaf\metal\MetalInternalFrameTitlePane.html`

### Class Description

```java
public class
MetalInternalFrameTitlePane

extends
BasicInternalFrameTitlePane
```

Class that manages a JLF title bar

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

---

### Field Details

#### protected boolean isPalette

The value

isPalette

---

#### protected
Icon
paletteCloseIcon

The palette close icon.

---

#### protected int paletteTitleHeight

The height of the palette title.

---

### Constructor Details

#### public MetalInternalFrameTitlePane​(
JInternalFrame
f)

Constructs a new instance of

MetalInternalFrameTitlePane

**Parameters:**
- f

- an instance of

JInternalFrame

---

### Method Details

#### protected void assembleSystemMenu()

Override the parent's method to do nothing. Metal frames do not
have system menus.

**Overrides:**
- assembleSystemMenu

in class

BasicInternalFrameTitlePane

---

#### protected void addSystemMenuItems​(
JMenu
systemMenu)

Override the parent's method to do nothing. Metal frames do not
have system menus.

**Overrides:**
- addSystemMenuItems

in class

BasicInternalFrameTitlePane

**Parameters:**
- systemMenu

- an instance of

JMenu

---

#### protected void showSystemMenu()

Override the parent's method to do nothing. Metal frames do not
have system menus.

**Overrides:**
- showSystemMenu

in class

BasicInternalFrameTitlePane

---

#### protected void addSubComponents()

Override the parent's method avoid creating a menu bar. Metal frames
do not have system menus.

**Overrides:**
- addSubComponents

in class

BasicInternalFrameTitlePane

---

#### public void paintPalette​(
Graphics
g)

Paints palette.

**Parameters:**
- g

- a instance of

Graphics

---

#### public void setPalette​(boolean b)

If

b

is

true

, sets palette icons.

**Parameters:**
- b

- if

true

, sets palette icons

---

### Additional Sections

#### Class MetalInternalFrameTitlePane

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.plaf.basic.BasicInternalFrameTitlePane
- - javax.swing.plaf.metal.MetalInternalFrameTitlePane

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.plaf.basic.BasicInternalFrameTitlePane
- - javax.swing.plaf.metal.MetalInternalFrameTitlePane

java.awt.Container

- javax.swing.JComponent
- - javax.swing.plaf.basic.BasicInternalFrameTitlePane
- - javax.swing.plaf.metal.MetalInternalFrameTitlePane

javax.swing.JComponent

- javax.swing.plaf.basic.BasicInternalFrameTitlePane
- - javax.swing.plaf.metal.MetalInternalFrameTitlePane

javax.swing.plaf.basic.BasicInternalFrameTitlePane

- javax.swing.plaf.metal.MetalInternalFrameTitlePane

javax.swing.plaf.metal.MetalInternalFrameTitlePane

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

```java
public class
MetalInternalFrameTitlePane

extends
BasicInternalFrameTitlePane
```

Class that manages a JLF title bar

**Since:** 1.3
**See Also:** Serialized Form

public class

MetalInternalFrameTitlePane

extends

BasicInternalFrameTitlePane

Class that manages a JLF title bar

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicInternalFrameTitlePane

BasicInternalFrameTitlePane.CloseAction

,

BasicInternalFrameTitlePane.IconifyAction

,

BasicInternalFrameTitlePane.MaximizeAction

,

BasicInternalFrameTitlePane.MoveAction

,

BasicInternalFrameTitlePane.PropertyChangeHandler

,

BasicInternalFrameTitlePane.RestoreAction

,

BasicInternalFrameTitlePane.SizeAction

,

BasicInternalFrameTitlePane.SystemMenuBar

,

BasicInternalFrameTitlePane.TitlePaneLayout

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

protected boolean

isPalette

The value

isPalette

protected

Icon

paletteCloseIcon

The palette close icon.

protected int

paletteTitleHeight

The height of the palette title.

- Fields declared in class javax.swing.plaf.basic.

BasicInternalFrameTitlePane

CLOSE_CMD

,

closeAction

,

closeButton

,

closeIcon

,

frame

,

iconButton

,

iconIcon

,

ICONIFY_CMD

,

iconifyAction

,

maxButton

,

maxIcon

,

MAXIMIZE_CMD

,

maximizeAction

,

menuBar

,

minIcon

,

MOVE_CMD

,

moveAction

,

notSelectedTextColor

,

notSelectedTitleColor

,

propertyChangeListener

,

RESTORE_CMD

,

restoreAction

,

selectedTextColor

,

selectedTitleColor

,

SIZE_CMD

,

sizeAction

,

windowMenu

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

MetalInternalFrameTitlePane

​(

JInternalFrame

f)

Constructs a new instance of

MetalInternalFrameTitlePane

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

addSubComponents

()

Override the parent's method avoid creating a menu bar.

protected void

addSystemMenuItems

​(

JMenu

systemMenu)

Override the parent's method to do nothing.

protected void

assembleSystemMenu

()

Override the parent's method to do nothing.

void

paintPalette

​(

Graphics

g)

Paints palette.

void

setPalette

​(boolean b)

If

b

is

true

, sets palette icons.

protected void

showSystemMenu

()

Override the parent's method to do nothing.

- Methods declared in class javax.swing.plaf.basic.

BasicInternalFrameTitlePane

createActions

,

createButtons

,

createLayout

,

createPropertyChangeListener

,

createSystemMenu

,

createSystemMenuBar

,

enableActions

,

getTitle

,

installDefaults

,

installListeners

,

installTitlePane

,

paintTitleBackground

,

postClosingEvent

,

setButtonIcons

,

uninstallDefaults

,

uninstallListeners

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

paintComponent

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

getAccessibleContext

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

- Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicInternalFrameTitlePane

BasicInternalFrameTitlePane.CloseAction

,

BasicInternalFrameTitlePane.IconifyAction

,

BasicInternalFrameTitlePane.MaximizeAction

,

BasicInternalFrameTitlePane.MoveAction

,

BasicInternalFrameTitlePane.PropertyChangeHandler

,

BasicInternalFrameTitlePane.RestoreAction

,

BasicInternalFrameTitlePane.SizeAction

,

BasicInternalFrameTitlePane.SystemMenuBar

,

BasicInternalFrameTitlePane.TitlePaneLayout

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

Nested classes/interfaces declared in class javax.swing.plaf.basic.

BasicInternalFrameTitlePane

BasicInternalFrameTitlePane.CloseAction

,

BasicInternalFrameTitlePane.IconifyAction

,

BasicInternalFrameTitlePane.MaximizeAction

,

BasicInternalFrameTitlePane.MoveAction

,

BasicInternalFrameTitlePane.PropertyChangeHandler

,

BasicInternalFrameTitlePane.RestoreAction

,

BasicInternalFrameTitlePane.SizeAction

,

BasicInternalFrameTitlePane.SystemMenuBar

,

BasicInternalFrameTitlePane.TitlePaneLayout

---

#### Nested classes/interfaces declared in class javax.swing.plaf.basic. BasicInternalFrameTitlePane

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

protected boolean

isPalette

The value

isPalette

protected

Icon

paletteCloseIcon

The palette close icon.

protected int

paletteTitleHeight

The height of the palette title.

- Fields declared in class javax.swing.plaf.basic.

BasicInternalFrameTitlePane

CLOSE_CMD

,

closeAction

,

closeButton

,

closeIcon

,

frame

,

iconButton

,

iconIcon

,

ICONIFY_CMD

,

iconifyAction

,

maxButton

,

maxIcon

,

MAXIMIZE_CMD

,

maximizeAction

,

menuBar

,

minIcon

,

MOVE_CMD

,

moveAction

,

notSelectedTextColor

,

notSelectedTitleColor

,

propertyChangeListener

,

RESTORE_CMD

,

restoreAction

,

selectedTextColor

,

selectedTitleColor

,

SIZE_CMD

,

sizeAction

,

windowMenu

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

The value

isPalette

The palette close icon.

The height of the palette title.

Fields declared in class javax.swing.plaf.basic.

BasicInternalFrameTitlePane

CLOSE_CMD

,

closeAction

,

closeButton

,

closeIcon

,

frame

,

iconButton

,

iconIcon

,

ICONIFY_CMD

,

iconifyAction

,

maxButton

,

maxIcon

,

MAXIMIZE_CMD

,

maximizeAction

,

menuBar

,

minIcon

,

MOVE_CMD

,

moveAction

,

notSelectedTextColor

,

notSelectedTitleColor

,

propertyChangeListener

,

RESTORE_CMD

,

restoreAction

,

selectedTextColor

,

selectedTitleColor

,

SIZE_CMD

,

sizeAction

,

windowMenu

---

#### Fields declared in class javax.swing.plaf.basic. BasicInternalFrameTitlePane

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

MetalInternalFrameTitlePane

​(

JInternalFrame

f)

Constructs a new instance of

MetalInternalFrameTitlePane

---

#### Constructor Summary

Constructs a new instance of

MetalInternalFrameTitlePane

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

addSubComponents

()

Override the parent's method avoid creating a menu bar.

protected void

addSystemMenuItems

​(

JMenu

systemMenu)

Override the parent's method to do nothing.

protected void

assembleSystemMenu

()

Override the parent's method to do nothing.

void

paintPalette

​(

Graphics

g)

Paints palette.

void

setPalette

​(boolean b)

If

b

is

true

, sets palette icons.

protected void

showSystemMenu

()

Override the parent's method to do nothing.

- Methods declared in class javax.swing.plaf.basic.

BasicInternalFrameTitlePane

createActions

,

createButtons

,

createLayout

,

createPropertyChangeListener

,

createSystemMenu

,

createSystemMenuBar

,

enableActions

,

getTitle

,

installDefaults

,

installListeners

,

installTitlePane

,

paintTitleBackground

,

postClosingEvent

,

setButtonIcons

,

uninstallDefaults

,

uninstallListeners

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

paintComponent

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

getAccessibleContext

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

Override the parent's method avoid creating a menu bar.

Override the parent's method to do nothing.

Paints palette.

If

b

is

true

, sets palette icons.

Methods declared in class javax.swing.plaf.basic.

BasicInternalFrameTitlePane

createActions

,

createButtons

,

createLayout

,

createPropertyChangeListener

,

createSystemMenu

,

createSystemMenuBar

,

enableActions

,

getTitle

,

installDefaults

,

installListeners

,

installTitlePane

,

paintTitleBackground

,

postClosingEvent

,

setButtonIcons

,

uninstallDefaults

,

uninstallListeners

---

#### Methods declared in class javax.swing.plaf.basic. BasicInternalFrameTitlePane

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

paintComponent

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

getAccessibleContext

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

- isPalette

```java
protected boolean isPalette
```

The value

isPalette

- paletteCloseIcon

```java
protected
Icon
paletteCloseIcon
```

The palette close icon.

- paletteTitleHeight

```java
protected int paletteTitleHeight
```

The height of the palette title.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MetalInternalFrameTitlePane

```java
public MetalInternalFrameTitlePane​(
JInternalFrame
f)
```

Constructs a new instance of

MetalInternalFrameTitlePane

**Parameters:** f

- an instance of

JInternalFrame

============ METHOD DETAIL ==========

- Method Detail

- assembleSystemMenu

```java
protected void assembleSystemMenu()
```

Override the parent's method to do nothing. Metal frames do not
have system menus.

**Overrides:** assembleSystemMenu

in class

BasicInternalFrameTitlePane

- addSystemMenuItems

```java
protected void addSystemMenuItems​(
JMenu
systemMenu)
```

Override the parent's method to do nothing. Metal frames do not
have system menus.

**Overrides:** addSystemMenuItems

in class

BasicInternalFrameTitlePane
**Parameters:** systemMenu

- an instance of

JMenu

- showSystemMenu

```java
protected void showSystemMenu()
```

Override the parent's method to do nothing. Metal frames do not
have system menus.

**Overrides:** showSystemMenu

in class

BasicInternalFrameTitlePane

- addSubComponents

```java
protected void addSubComponents()
```

Override the parent's method avoid creating a menu bar. Metal frames
do not have system menus.

**Overrides:** addSubComponents

in class

BasicInternalFrameTitlePane

- paintPalette

```java
public void paintPalette​(
Graphics
g)
```

Paints palette.

**Parameters:** g

- a instance of

Graphics

- setPalette

```java
public void setPalette​(boolean b)
```

If

b

is

true

, sets palette icons.

**Parameters:** b

- if

true

, sets palette icons

Field Detail

- isPalette

```java
protected boolean isPalette
```

The value

isPalette

- paletteCloseIcon

```java
protected
Icon
paletteCloseIcon
```

The palette close icon.

- paletteTitleHeight

```java
protected int paletteTitleHeight
```

The height of the palette title.

---

#### Field Detail

isPalette

```java
protected boolean isPalette
```

The value

isPalette

---

#### isPalette

protected boolean isPalette

The value

isPalette

paletteCloseIcon

```java
protected
Icon
paletteCloseIcon
```

The palette close icon.

---

#### paletteCloseIcon

protected

Icon

paletteCloseIcon

The palette close icon.

paletteTitleHeight

```java
protected int paletteTitleHeight
```

The height of the palette title.

---

#### paletteTitleHeight

protected int paletteTitleHeight

The height of the palette title.

Constructor Detail

- MetalInternalFrameTitlePane

```java
public MetalInternalFrameTitlePane​(
JInternalFrame
f)
```

Constructs a new instance of

MetalInternalFrameTitlePane

**Parameters:** f

- an instance of

JInternalFrame

---

#### Constructor Detail

MetalInternalFrameTitlePane

```java
public MetalInternalFrameTitlePane​(
JInternalFrame
f)
```

Constructs a new instance of

MetalInternalFrameTitlePane

**Parameters:** f

- an instance of

JInternalFrame

---

#### MetalInternalFrameTitlePane

public MetalInternalFrameTitlePane​(

JInternalFrame

f)

Constructs a new instance of

MetalInternalFrameTitlePane

Method Detail

- assembleSystemMenu

```java
protected void assembleSystemMenu()
```

Override the parent's method to do nothing. Metal frames do not
have system menus.

**Overrides:** assembleSystemMenu

in class

BasicInternalFrameTitlePane

- addSystemMenuItems

```java
protected void addSystemMenuItems​(
JMenu
systemMenu)
```

Override the parent's method to do nothing. Metal frames do not
have system menus.

**Overrides:** addSystemMenuItems

in class

BasicInternalFrameTitlePane
**Parameters:** systemMenu

- an instance of

JMenu

- showSystemMenu

```java
protected void showSystemMenu()
```

Override the parent's method to do nothing. Metal frames do not
have system menus.

**Overrides:** showSystemMenu

in class

BasicInternalFrameTitlePane

- addSubComponents

```java
protected void addSubComponents()
```

Override the parent's method avoid creating a menu bar. Metal frames
do not have system menus.

**Overrides:** addSubComponents

in class

BasicInternalFrameTitlePane

- paintPalette

```java
public void paintPalette​(
Graphics
g)
```

Paints palette.

**Parameters:** g

- a instance of

Graphics

- setPalette

```java
public void setPalette​(boolean b)
```

If

b

is

true

, sets palette icons.

**Parameters:** b

- if

true

, sets palette icons

---

#### Method Detail

assembleSystemMenu

```java
protected void assembleSystemMenu()
```

Override the parent's method to do nothing. Metal frames do not
have system menus.

**Overrides:** assembleSystemMenu

in class

BasicInternalFrameTitlePane

---

#### assembleSystemMenu

protected void assembleSystemMenu()

Override the parent's method to do nothing. Metal frames do not
have system menus.

addSystemMenuItems

```java
protected void addSystemMenuItems​(
JMenu
systemMenu)
```

Override the parent's method to do nothing. Metal frames do not
have system menus.

**Overrides:** addSystemMenuItems

in class

BasicInternalFrameTitlePane
**Parameters:** systemMenu

- an instance of

JMenu

---

#### addSystemMenuItems

protected void addSystemMenuItems​(

JMenu

systemMenu)

Override the parent's method to do nothing. Metal frames do not
have system menus.

showSystemMenu

```java
protected void showSystemMenu()
```

Override the parent's method to do nothing. Metal frames do not
have system menus.

**Overrides:** showSystemMenu

in class

BasicInternalFrameTitlePane

---

#### showSystemMenu

protected void showSystemMenu()

Override the parent's method to do nothing. Metal frames do not
have system menus.

addSubComponents

```java
protected void addSubComponents()
```

Override the parent's method avoid creating a menu bar. Metal frames
do not have system menus.

**Overrides:** addSubComponents

in class

BasicInternalFrameTitlePane

---

#### addSubComponents

protected void addSubComponents()

Override the parent's method avoid creating a menu bar. Metal frames
do not have system menus.

paintPalette

```java
public void paintPalette​(
Graphics
g)
```

Paints palette.

**Parameters:** g

- a instance of

Graphics

---

#### paintPalette

public void paintPalette​(

Graphics

g)

Paints palette.

setPalette

```java
public void setPalette​(boolean b)
```

If

b

is

true

, sets palette icons.

**Parameters:** b

- if

true

, sets palette icons

---

#### setPalette

public void setPalette​(boolean b)

If

b

is

true

, sets palette icons.

---

