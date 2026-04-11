# Class BasicInternalFrameTitlePane

**Source:** `java.desktop\javax\swing\plaf\basic\BasicInternalFrameTitlePane.html`

### Class Description

```java
public class
BasicInternalFrameTitlePane

extends
JComponent
```

The class that manages a basic title bar

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

---

### Field Details

#### protected
JMenuBar
menuBar

The instance of

JMenuBar

.

---

#### protected
JButton
iconButton

The iconify button.

---

#### protected
JButton
maxButton

The maximize button.

---

#### protected
JButton
closeButton

The close button.

---

#### protected
JMenu
windowMenu

The instance of

JMenu

.

---

#### protected
JInternalFrame
frame

The instance of

JInternalFrame

.

---

#### protected
Color
selectedTitleColor

The color of a selected title.

---

#### protected
Color
selectedTextColor

The color of a selected text.

---

#### protected
Color
notSelectedTitleColor

The color of a not selected title.

---

#### protected
Color
notSelectedTextColor

The color of a not selected text.

---

#### protected
Icon
maxIcon

The maximize icon.

---

#### protected
Icon
minIcon

The minimize icon.

---

#### protected
Icon
iconIcon

The iconify icon.

---

#### protected
Icon
closeIcon

The close icon.

---

#### protected
PropertyChangeListener
propertyChangeListener

The instance of a

PropertyChangeListener

.

---

#### protected
Action
closeAction

The instance of a

CloseAction

.

---

#### protected
Action
maximizeAction

The instance of a

MaximizeAction

.

---

#### protected
Action
iconifyAction

The instance of an

IconifyAction

.

---

#### protected
Action
restoreAction

The instance of a

RestoreAction

.

---

#### protected
Action
moveAction

The instance of a

MoveAction

.

---

#### protected
Action
sizeAction

The instance of a

SizeAction

.

---

#### protected static final
String
CLOSE_CMD

The close button text property.

---

#### protected static final
String
ICONIFY_CMD

The minimize button text property.

---

#### protected static final
String
RESTORE_CMD

The restore button text property.

---

#### protected static final
String
MAXIMIZE_CMD

The maximize button text property.

---

#### protected static final
String
MOVE_CMD

The move button text property.

---

#### protected static final
String
SIZE_CMD

The size button text property.

---

### Constructor Details

#### public BasicInternalFrameTitlePane​(
JInternalFrame
f)

Constructs a new instance of

BasicInternalFrameTitlePane

.

**Parameters:**
- f

- an instance of

JInternalFrame

---

### Method Details

#### protected void installTitlePane()

Installs the title pane.

---

#### protected void addSubComponents()

Adds subcomponents.

---

#### protected void createActions()

Creates actions.

---

#### protected void installListeners()

Registers listeners.

---

#### protected void uninstallListeners()

Unregisters listeners.

---

#### protected void installDefaults()

Installs default properties.

---

#### protected void uninstallDefaults()

Uninstalls default properties.

---

#### protected void createButtons()

Creates buttons.

---

#### protected void setButtonIcons()

Sets the button icons.

---

#### protected void assembleSystemMenu()

Assembles system menu.

---

#### protected void addSystemMenuItems​(
JMenu
systemMenu)

Adds system menu items to

systemMenu

.

**Parameters:**
- systemMenu

- an instance of

JMenu

---

#### protected
JMenu
createSystemMenu()

Returns a new instance of

JMenu

.

**Returns:**
- a new instance of

JMenu

---

#### protected
JMenuBar
createSystemMenuBar()

Returns a new instance of

JMenuBar

.

**Returns:**
- a new instance of

JMenuBar

---

#### protected void showSystemMenu()

Shows system menu.

---

#### protected void paintTitleBackground​(
Graphics
g)

Invoked from paintComponent.
Paints the background of the titlepane. All text and icons will
then be rendered on top of this background.

**Parameters:**
- g

- the graphics to use to render the background

**Since:**
- 1.4

---

#### protected
String
getTitle​(
String
text,

FontMetrics
fm,
int availTextWidth)

Returns the title.

**Parameters:**
- text

- a text
- fm

- an instance of

FontMetrics
- availTextWidth

- an available text width

**Returns:**
- the title.

---

#### protected void postClosingEvent​(
JInternalFrame
frame)

Post a WINDOW_CLOSING-like event to the frame, so that it can
be treated like a regular

Frame

.

**Parameters:**
- frame

- an instance of

JInternalFrame

---

#### protected void enableActions()

Enables actions.

---

#### protected
PropertyChangeListener
createPropertyChangeListener()

Returns an instance of

PropertyChangeListener

.

**Returns:**
- an instance of

PropertyChangeListener

---

#### protected
LayoutManager
createLayout()

Returns a layout manager.

**Returns:**
- a layout manager

---

### Additional Sections

#### Class BasicInternalFrameTitlePane

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.plaf.basic.BasicInternalFrameTitlePane

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.plaf.basic.BasicInternalFrameTitlePane

java.awt.Container

- javax.swing.JComponent
- - javax.swing.plaf.basic.BasicInternalFrameTitlePane

javax.swing.JComponent

- javax.swing.plaf.basic.BasicInternalFrameTitlePane

javax.swing.plaf.basic.BasicInternalFrameTitlePane

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

**Direct Known Subclasses:** MetalInternalFrameTitlePane

```java
public class
BasicInternalFrameTitlePane

extends
JComponent
```

The class that manages a basic title bar

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

BasicInternalFrameTitlePane

extends

JComponent

The class that manages a basic title bar

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

class

BasicInternalFrameTitlePane.CloseAction

This class should be treated as a "protected" inner class.

class

BasicInternalFrameTitlePane.IconifyAction

This class should be treated as a "protected" inner class.

class

BasicInternalFrameTitlePane.MaximizeAction

This class should be treated as a "protected" inner class.

class

BasicInternalFrameTitlePane.MoveAction

This class should be treated as a "protected" inner class.

class

BasicInternalFrameTitlePane.PropertyChangeHandler

This class should be treated as a "protected" inner class.

class

BasicInternalFrameTitlePane.RestoreAction

This class should be treated as a "protected" inner class.

class

BasicInternalFrameTitlePane.SizeAction

This class should be treated as a "protected" inner class.

class

BasicInternalFrameTitlePane.SystemMenuBar

This class should be treated as a "protected" inner class.

class

BasicInternalFrameTitlePane.TitlePaneLayout

This class should be treated as a "protected" inner class.

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

String

CLOSE_CMD

The close button text property.

protected

Action

closeAction

The instance of a

CloseAction

.

protected

JButton

closeButton

The close button.

protected

Icon

closeIcon

The close icon.

protected

JInternalFrame

frame

The instance of

JInternalFrame

.

protected

JButton

iconButton

The iconify button.

protected

Icon

iconIcon

The iconify icon.

protected static

String

ICONIFY_CMD

The minimize button text property.

protected

Action

iconifyAction

The instance of an

IconifyAction

.

protected

JButton

maxButton

The maximize button.

protected

Icon

maxIcon

The maximize icon.

protected static

String

MAXIMIZE_CMD

The maximize button text property.

protected

Action

maximizeAction

The instance of a

MaximizeAction

.

protected

JMenuBar

menuBar

The instance of

JMenuBar

.

protected

Icon

minIcon

The minimize icon.

protected static

String

MOVE_CMD

The move button text property.

protected

Action

moveAction

The instance of a

MoveAction

.

protected

Color

notSelectedTextColor

The color of a not selected text.

protected

Color

notSelectedTitleColor

The color of a not selected title.

protected

PropertyChangeListener

propertyChangeListener

The instance of a

PropertyChangeListener

.

protected static

String

RESTORE_CMD

The restore button text property.

protected

Action

restoreAction

The instance of a

RestoreAction

.

protected

Color

selectedTextColor

The color of a selected text.

protected

Color

selectedTitleColor

The color of a selected title.

protected static

String

SIZE_CMD

The size button text property.

protected

Action

sizeAction

The instance of a

SizeAction

.

protected

JMenu

windowMenu

The instance of

JMenu

.

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

BasicInternalFrameTitlePane

​(

JInternalFrame

f)

Constructs a new instance of

BasicInternalFrameTitlePane

.

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

Adds subcomponents.

protected void

addSystemMenuItems

​(

JMenu

systemMenu)

Adds system menu items to

systemMenu

.

protected void

assembleSystemMenu

()

Assembles system menu.

protected void

createActions

()

Creates actions.

protected void

createButtons

()

Creates buttons.

protected

LayoutManager

createLayout

()

Returns a layout manager.

protected

PropertyChangeListener

createPropertyChangeListener

()

Returns an instance of

PropertyChangeListener

.

protected

JMenu

createSystemMenu

()

Returns a new instance of

JMenu

.

protected

JMenuBar

createSystemMenuBar

()

Returns a new instance of

JMenuBar

.

protected void

enableActions

()

Enables actions.

protected

String

getTitle

​(

String

text,

FontMetrics

fm,
int availTextWidth)

Returns the title.

protected void

installDefaults

()

Installs default properties.

protected void

installListeners

()

Registers listeners.

protected void

installTitlePane

()

Installs the title pane.

protected void

paintTitleBackground

​(

Graphics

g)

Invoked from paintComponent.

protected void

postClosingEvent

​(

JInternalFrame

frame)

Post a WINDOW_CLOSING-like event to the frame, so that it can
be treated like a regular

Frame

.

protected void

setButtonIcons

()

Sets the button icons.

protected void

showSystemMenu

()

Shows system menu.

protected void

uninstallDefaults

()

Uninstalls default properties.

protected void

uninstallListeners

()

Unregisters listeners.

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

Nested Classes

Modifier and Type

Class

Description

class

BasicInternalFrameTitlePane.CloseAction

This class should be treated as a "protected" inner class.

class

BasicInternalFrameTitlePane.IconifyAction

This class should be treated as a "protected" inner class.

class

BasicInternalFrameTitlePane.MaximizeAction

This class should be treated as a "protected" inner class.

class

BasicInternalFrameTitlePane.MoveAction

This class should be treated as a "protected" inner class.

class

BasicInternalFrameTitlePane.PropertyChangeHandler

This class should be treated as a "protected" inner class.

class

BasicInternalFrameTitlePane.RestoreAction

This class should be treated as a "protected" inner class.

class

BasicInternalFrameTitlePane.SizeAction

This class should be treated as a "protected" inner class.

class

BasicInternalFrameTitlePane.SystemMenuBar

This class should be treated as a "protected" inner class.

class

BasicInternalFrameTitlePane.TitlePaneLayout

This class should be treated as a "protected" inner class.

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

This class should be treated as a "protected" inner class.

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

String

CLOSE_CMD

The close button text property.

protected

Action

closeAction

The instance of a

CloseAction

.

protected

JButton

closeButton

The close button.

protected

Icon

closeIcon

The close icon.

protected

JInternalFrame

frame

The instance of

JInternalFrame

.

protected

JButton

iconButton

The iconify button.

protected

Icon

iconIcon

The iconify icon.

protected static

String

ICONIFY_CMD

The minimize button text property.

protected

Action

iconifyAction

The instance of an

IconifyAction

.

protected

JButton

maxButton

The maximize button.

protected

Icon

maxIcon

The maximize icon.

protected static

String

MAXIMIZE_CMD

The maximize button text property.

protected

Action

maximizeAction

The instance of a

MaximizeAction

.

protected

JMenuBar

menuBar

The instance of

JMenuBar

.

protected

Icon

minIcon

The minimize icon.

protected static

String

MOVE_CMD

The move button text property.

protected

Action

moveAction

The instance of a

MoveAction

.

protected

Color

notSelectedTextColor

The color of a not selected text.

protected

Color

notSelectedTitleColor

The color of a not selected title.

protected

PropertyChangeListener

propertyChangeListener

The instance of a

PropertyChangeListener

.

protected static

String

RESTORE_CMD

The restore button text property.

protected

Action

restoreAction

The instance of a

RestoreAction

.

protected

Color

selectedTextColor

The color of a selected text.

protected

Color

selectedTitleColor

The color of a selected title.

protected static

String

SIZE_CMD

The size button text property.

protected

Action

sizeAction

The instance of a

SizeAction

.

protected

JMenu

windowMenu

The instance of

JMenu

.

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

The close button text property.

The instance of a

CloseAction

.

The close button.

The close icon.

The instance of

JInternalFrame

.

The iconify button.

The iconify icon.

The minimize button text property.

The instance of an

IconifyAction

.

The maximize button.

The maximize icon.

The maximize button text property.

The instance of a

MaximizeAction

.

The instance of

JMenuBar

.

The minimize icon.

The move button text property.

The instance of a

MoveAction

.

The color of a not selected text.

The color of a not selected title.

The instance of a

PropertyChangeListener

.

The restore button text property.

The instance of a

RestoreAction

.

The color of a selected text.

The color of a selected title.

The size button text property.

The instance of a

SizeAction

.

The instance of

JMenu

.

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

BasicInternalFrameTitlePane

​(

JInternalFrame

f)

Constructs a new instance of

BasicInternalFrameTitlePane

.

---

#### Constructor Summary

Constructs a new instance of

BasicInternalFrameTitlePane

.

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

Adds subcomponents.

protected void

addSystemMenuItems

​(

JMenu

systemMenu)

Adds system menu items to

systemMenu

.

protected void

assembleSystemMenu

()

Assembles system menu.

protected void

createActions

()

Creates actions.

protected void

createButtons

()

Creates buttons.

protected

LayoutManager

createLayout

()

Returns a layout manager.

protected

PropertyChangeListener

createPropertyChangeListener

()

Returns an instance of

PropertyChangeListener

.

protected

JMenu

createSystemMenu

()

Returns a new instance of

JMenu

.

protected

JMenuBar

createSystemMenuBar

()

Returns a new instance of

JMenuBar

.

protected void

enableActions

()

Enables actions.

protected

String

getTitle

​(

String

text,

FontMetrics

fm,
int availTextWidth)

Returns the title.

protected void

installDefaults

()

Installs default properties.

protected void

installListeners

()

Registers listeners.

protected void

installTitlePane

()

Installs the title pane.

protected void

paintTitleBackground

​(

Graphics

g)

Invoked from paintComponent.

protected void

postClosingEvent

​(

JInternalFrame

frame)

Post a WINDOW_CLOSING-like event to the frame, so that it can
be treated like a regular

Frame

.

protected void

setButtonIcons

()

Sets the button icons.

protected void

showSystemMenu

()

Shows system menu.

protected void

uninstallDefaults

()

Uninstalls default properties.

protected void

uninstallListeners

()

Unregisters listeners.

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

Adds subcomponents.

Adds system menu items to

systemMenu

.

Assembles system menu.

Creates actions.

Creates buttons.

Returns a layout manager.

Returns an instance of

PropertyChangeListener

.

Returns a new instance of

JMenu

.

Returns a new instance of

JMenuBar

.

Enables actions.

Returns the title.

Installs default properties.

Registers listeners.

Installs the title pane.

Invoked from paintComponent.

Post a WINDOW_CLOSING-like event to the frame, so that it can
be treated like a regular

Frame

.

Sets the button icons.

Shows system menu.

Uninstalls default properties.

Unregisters listeners.

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

- menuBar

```java
protected
JMenuBar
menuBar
```

The instance of

JMenuBar

.

- iconButton

```java
protected
JButton
iconButton
```

The iconify button.

- maxButton

```java
protected
JButton
maxButton
```

The maximize button.

- closeButton

```java
protected
JButton
closeButton
```

The close button.

- windowMenu

```java
protected
JMenu
windowMenu
```

The instance of

JMenu

.

- frame

```java
protected
JInternalFrame
frame
```

The instance of

JInternalFrame

.

- selectedTitleColor

```java
protected
Color
selectedTitleColor
```

The color of a selected title.

- selectedTextColor

```java
protected
Color
selectedTextColor
```

The color of a selected text.

- notSelectedTitleColor

```java
protected
Color
notSelectedTitleColor
```

The color of a not selected title.

- notSelectedTextColor

```java
protected
Color
notSelectedTextColor
```

The color of a not selected text.

- maxIcon

```java
protected
Icon
maxIcon
```

The maximize icon.

- minIcon

```java
protected
Icon
minIcon
```

The minimize icon.

- iconIcon

```java
protected
Icon
iconIcon
```

The iconify icon.

- closeIcon

```java
protected
Icon
closeIcon
```

The close icon.

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

The instance of a

PropertyChangeListener

.

- closeAction

```java
protected
Action
closeAction
```

The instance of a

CloseAction

.

- maximizeAction

```java
protected
Action
maximizeAction
```

The instance of a

MaximizeAction

.

- iconifyAction

```java
protected
Action
iconifyAction
```

The instance of an

IconifyAction

.

- restoreAction

```java
protected
Action
restoreAction
```

The instance of a

RestoreAction

.

- moveAction

```java
protected
Action
moveAction
```

The instance of a

MoveAction

.

- sizeAction

```java
protected
Action
sizeAction
```

The instance of a

SizeAction

.

- CLOSE_CMD

```java
protected static final
String
CLOSE_CMD
```

The close button text property.

- ICONIFY_CMD

```java
protected static final
String
ICONIFY_CMD
```

The minimize button text property.

- RESTORE_CMD

```java
protected static final
String
RESTORE_CMD
```

The restore button text property.

- MAXIMIZE_CMD

```java
protected static final
String
MAXIMIZE_CMD
```

The maximize button text property.

- MOVE_CMD

```java
protected static final
String
MOVE_CMD
```

The move button text property.

- SIZE_CMD

```java
protected static final
String
SIZE_CMD
```

The size button text property.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicInternalFrameTitlePane

```java
public BasicInternalFrameTitlePane​(
JInternalFrame
f)
```

Constructs a new instance of

BasicInternalFrameTitlePane

.

**Parameters:** f

- an instance of

JInternalFrame

============ METHOD DETAIL ==========

- Method Detail

- installTitlePane

```java
protected void installTitlePane()
```

Installs the title pane.

- addSubComponents

```java
protected void addSubComponents()
```

Adds subcomponents.

- createActions

```java
protected void createActions()
```

Creates actions.

- installListeners

```java
protected void installListeners()
```

Registers listeners.

- uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

- installDefaults

```java
protected void installDefaults()
```

Installs default properties.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

- createButtons

```java
protected void createButtons()
```

Creates buttons.

- setButtonIcons

```java
protected void setButtonIcons()
```

Sets the button icons.

- assembleSystemMenu

```java
protected void assembleSystemMenu()
```

Assembles system menu.

- addSystemMenuItems

```java
protected void addSystemMenuItems​(
JMenu
systemMenu)
```

Adds system menu items to

systemMenu

.

**Parameters:** systemMenu

- an instance of

JMenu

- createSystemMenu

```java
protected
JMenu
createSystemMenu()
```

Returns a new instance of

JMenu

.

**Returns:** a new instance of

JMenu

- createSystemMenuBar

```java
protected
JMenuBar
createSystemMenuBar()
```

Returns a new instance of

JMenuBar

.

**Returns:** a new instance of

JMenuBar

- showSystemMenu

```java
protected void showSystemMenu()
```

Shows system menu.

- paintTitleBackground

```java
protected void paintTitleBackground​(
Graphics
g)
```

Invoked from paintComponent.
Paints the background of the titlepane. All text and icons will
then be rendered on top of this background.

**Parameters:** g

- the graphics to use to render the background
**Since:** 1.4

- getTitle

```java
protected
String
getTitle​(
String
text,

FontMetrics
fm,
int availTextWidth)
```

Returns the title.

**Parameters:** text

- a text
**Parameters:** fm

- an instance of

FontMetrics
**Parameters:** availTextWidth

- an available text width
**Returns:** the title.

- postClosingEvent

```java
protected void postClosingEvent​(
JInternalFrame
frame)
```

Post a WINDOW_CLOSING-like event to the frame, so that it can
be treated like a regular

Frame

.

**Parameters:** frame

- an instance of

JInternalFrame

- enableActions

```java
protected void enableActions()
```

Enables actions.

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Returns an instance of

PropertyChangeListener

.

**Returns:** an instance of

PropertyChangeListener

- createLayout

```java
protected
LayoutManager
createLayout()
```

Returns a layout manager.

**Returns:** a layout manager

Field Detail

- menuBar

```java
protected
JMenuBar
menuBar
```

The instance of

JMenuBar

.

- iconButton

```java
protected
JButton
iconButton
```

The iconify button.

- maxButton

```java
protected
JButton
maxButton
```

The maximize button.

- closeButton

```java
protected
JButton
closeButton
```

The close button.

- windowMenu

```java
protected
JMenu
windowMenu
```

The instance of

JMenu

.

- frame

```java
protected
JInternalFrame
frame
```

The instance of

JInternalFrame

.

- selectedTitleColor

```java
protected
Color
selectedTitleColor
```

The color of a selected title.

- selectedTextColor

```java
protected
Color
selectedTextColor
```

The color of a selected text.

- notSelectedTitleColor

```java
protected
Color
notSelectedTitleColor
```

The color of a not selected title.

- notSelectedTextColor

```java
protected
Color
notSelectedTextColor
```

The color of a not selected text.

- maxIcon

```java
protected
Icon
maxIcon
```

The maximize icon.

- minIcon

```java
protected
Icon
minIcon
```

The minimize icon.

- iconIcon

```java
protected
Icon
iconIcon
```

The iconify icon.

- closeIcon

```java
protected
Icon
closeIcon
```

The close icon.

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

The instance of a

PropertyChangeListener

.

- closeAction

```java
protected
Action
closeAction
```

The instance of a

CloseAction

.

- maximizeAction

```java
protected
Action
maximizeAction
```

The instance of a

MaximizeAction

.

- iconifyAction

```java
protected
Action
iconifyAction
```

The instance of an

IconifyAction

.

- restoreAction

```java
protected
Action
restoreAction
```

The instance of a

RestoreAction

.

- moveAction

```java
protected
Action
moveAction
```

The instance of a

MoveAction

.

- sizeAction

```java
protected
Action
sizeAction
```

The instance of a

SizeAction

.

- CLOSE_CMD

```java
protected static final
String
CLOSE_CMD
```

The close button text property.

- ICONIFY_CMD

```java
protected static final
String
ICONIFY_CMD
```

The minimize button text property.

- RESTORE_CMD

```java
protected static final
String
RESTORE_CMD
```

The restore button text property.

- MAXIMIZE_CMD

```java
protected static final
String
MAXIMIZE_CMD
```

The maximize button text property.

- MOVE_CMD

```java
protected static final
String
MOVE_CMD
```

The move button text property.

- SIZE_CMD

```java
protected static final
String
SIZE_CMD
```

The size button text property.

---

#### Field Detail

menuBar

```java
protected
JMenuBar
menuBar
```

The instance of

JMenuBar

.

---

#### menuBar

protected

JMenuBar

menuBar

The instance of

JMenuBar

.

iconButton

```java
protected
JButton
iconButton
```

The iconify button.

---

#### iconButton

protected

JButton

iconButton

The iconify button.

maxButton

```java
protected
JButton
maxButton
```

The maximize button.

---

#### maxButton

protected

JButton

maxButton

The maximize button.

closeButton

```java
protected
JButton
closeButton
```

The close button.

---

#### closeButton

protected

JButton

closeButton

The close button.

windowMenu

```java
protected
JMenu
windowMenu
```

The instance of

JMenu

.

---

#### windowMenu

protected

JMenu

windowMenu

The instance of

JMenu

.

frame

```java
protected
JInternalFrame
frame
```

The instance of

JInternalFrame

.

---

#### frame

protected

JInternalFrame

frame

The instance of

JInternalFrame

.

selectedTitleColor

```java
protected
Color
selectedTitleColor
```

The color of a selected title.

---

#### selectedTitleColor

protected

Color

selectedTitleColor

The color of a selected title.

selectedTextColor

```java
protected
Color
selectedTextColor
```

The color of a selected text.

---

#### selectedTextColor

protected

Color

selectedTextColor

The color of a selected text.

notSelectedTitleColor

```java
protected
Color
notSelectedTitleColor
```

The color of a not selected title.

---

#### notSelectedTitleColor

protected

Color

notSelectedTitleColor

The color of a not selected title.

notSelectedTextColor

```java
protected
Color
notSelectedTextColor
```

The color of a not selected text.

---

#### notSelectedTextColor

protected

Color

notSelectedTextColor

The color of a not selected text.

maxIcon

```java
protected
Icon
maxIcon
```

The maximize icon.

---

#### maxIcon

protected

Icon

maxIcon

The maximize icon.

minIcon

```java
protected
Icon
minIcon
```

The minimize icon.

---

#### minIcon

protected

Icon

minIcon

The minimize icon.

iconIcon

```java
protected
Icon
iconIcon
```

The iconify icon.

---

#### iconIcon

protected

Icon

iconIcon

The iconify icon.

closeIcon

```java
protected
Icon
closeIcon
```

The close icon.

---

#### closeIcon

protected

Icon

closeIcon

The close icon.

propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

The instance of a

PropertyChangeListener

.

---

#### propertyChangeListener

protected

PropertyChangeListener

propertyChangeListener

The instance of a

PropertyChangeListener

.

closeAction

```java
protected
Action
closeAction
```

The instance of a

CloseAction

.

---

#### closeAction

protected

Action

closeAction

The instance of a

CloseAction

.

maximizeAction

```java
protected
Action
maximizeAction
```

The instance of a

MaximizeAction

.

---

#### maximizeAction

protected

Action

maximizeAction

The instance of a

MaximizeAction

.

iconifyAction

```java
protected
Action
iconifyAction
```

The instance of an

IconifyAction

.

---

#### iconifyAction

protected

Action

iconifyAction

The instance of an

IconifyAction

.

restoreAction

```java
protected
Action
restoreAction
```

The instance of a

RestoreAction

.

---

#### restoreAction

protected

Action

restoreAction

The instance of a

RestoreAction

.

moveAction

```java
protected
Action
moveAction
```

The instance of a

MoveAction

.

---

#### moveAction

protected

Action

moveAction

The instance of a

MoveAction

.

sizeAction

```java
protected
Action
sizeAction
```

The instance of a

SizeAction

.

---

#### sizeAction

protected

Action

sizeAction

The instance of a

SizeAction

.

CLOSE_CMD

```java
protected static final
String
CLOSE_CMD
```

The close button text property.

---

#### CLOSE_CMD

protected static final

String

CLOSE_CMD

The close button text property.

ICONIFY_CMD

```java
protected static final
String
ICONIFY_CMD
```

The minimize button text property.

---

#### ICONIFY_CMD

protected static final

String

ICONIFY_CMD

The minimize button text property.

RESTORE_CMD

```java
protected static final
String
RESTORE_CMD
```

The restore button text property.

---

#### RESTORE_CMD

protected static final

String

RESTORE_CMD

The restore button text property.

MAXIMIZE_CMD

```java
protected static final
String
MAXIMIZE_CMD
```

The maximize button text property.

---

#### MAXIMIZE_CMD

protected static final

String

MAXIMIZE_CMD

The maximize button text property.

MOVE_CMD

```java
protected static final
String
MOVE_CMD
```

The move button text property.

---

#### MOVE_CMD

protected static final

String

MOVE_CMD

The move button text property.

SIZE_CMD

```java
protected static final
String
SIZE_CMD
```

The size button text property.

---

#### SIZE_CMD

protected static final

String

SIZE_CMD

The size button text property.

Constructor Detail

- BasicInternalFrameTitlePane

```java
public BasicInternalFrameTitlePane​(
JInternalFrame
f)
```

Constructs a new instance of

BasicInternalFrameTitlePane

.

**Parameters:** f

- an instance of

JInternalFrame

---

#### Constructor Detail

BasicInternalFrameTitlePane

```java
public BasicInternalFrameTitlePane​(
JInternalFrame
f)
```

Constructs a new instance of

BasicInternalFrameTitlePane

.

**Parameters:** f

- an instance of

JInternalFrame

---

#### BasicInternalFrameTitlePane

public BasicInternalFrameTitlePane​(

JInternalFrame

f)

Constructs a new instance of

BasicInternalFrameTitlePane

.

Method Detail

- installTitlePane

```java
protected void installTitlePane()
```

Installs the title pane.

- addSubComponents

```java
protected void addSubComponents()
```

Adds subcomponents.

- createActions

```java
protected void createActions()
```

Creates actions.

- installListeners

```java
protected void installListeners()
```

Registers listeners.

- uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

- installDefaults

```java
protected void installDefaults()
```

Installs default properties.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

- createButtons

```java
protected void createButtons()
```

Creates buttons.

- setButtonIcons

```java
protected void setButtonIcons()
```

Sets the button icons.

- assembleSystemMenu

```java
protected void assembleSystemMenu()
```

Assembles system menu.

- addSystemMenuItems

```java
protected void addSystemMenuItems​(
JMenu
systemMenu)
```

Adds system menu items to

systemMenu

.

**Parameters:** systemMenu

- an instance of

JMenu

- createSystemMenu

```java
protected
JMenu
createSystemMenu()
```

Returns a new instance of

JMenu

.

**Returns:** a new instance of

JMenu

- createSystemMenuBar

```java
protected
JMenuBar
createSystemMenuBar()
```

Returns a new instance of

JMenuBar

.

**Returns:** a new instance of

JMenuBar

- showSystemMenu

```java
protected void showSystemMenu()
```

Shows system menu.

- paintTitleBackground

```java
protected void paintTitleBackground​(
Graphics
g)
```

Invoked from paintComponent.
Paints the background of the titlepane. All text and icons will
then be rendered on top of this background.

**Parameters:** g

- the graphics to use to render the background
**Since:** 1.4

- getTitle

```java
protected
String
getTitle​(
String
text,

FontMetrics
fm,
int availTextWidth)
```

Returns the title.

**Parameters:** text

- a text
**Parameters:** fm

- an instance of

FontMetrics
**Parameters:** availTextWidth

- an available text width
**Returns:** the title.

- postClosingEvent

```java
protected void postClosingEvent​(
JInternalFrame
frame)
```

Post a WINDOW_CLOSING-like event to the frame, so that it can
be treated like a regular

Frame

.

**Parameters:** frame

- an instance of

JInternalFrame

- enableActions

```java
protected void enableActions()
```

Enables actions.

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Returns an instance of

PropertyChangeListener

.

**Returns:** an instance of

PropertyChangeListener

- createLayout

```java
protected
LayoutManager
createLayout()
```

Returns a layout manager.

**Returns:** a layout manager

---

#### Method Detail

installTitlePane

```java
protected void installTitlePane()
```

Installs the title pane.

---

#### installTitlePane

protected void installTitlePane()

Installs the title pane.

addSubComponents

```java
protected void addSubComponents()
```

Adds subcomponents.

---

#### addSubComponents

protected void addSubComponents()

Adds subcomponents.

createActions

```java
protected void createActions()
```

Creates actions.

---

#### createActions

protected void createActions()

Creates actions.

installListeners

```java
protected void installListeners()
```

Registers listeners.

---

#### installListeners

protected void installListeners()

Registers listeners.

uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

---

#### uninstallListeners

protected void uninstallListeners()

Unregisters listeners.

installDefaults

```java
protected void installDefaults()
```

Installs default properties.

---

#### installDefaults

protected void installDefaults()

Installs default properties.

uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

---

#### uninstallDefaults

protected void uninstallDefaults()

Uninstalls default properties.

createButtons

```java
protected void createButtons()
```

Creates buttons.

---

#### createButtons

protected void createButtons()

Creates buttons.

setButtonIcons

```java
protected void setButtonIcons()
```

Sets the button icons.

---

#### setButtonIcons

protected void setButtonIcons()

Sets the button icons.

assembleSystemMenu

```java
protected void assembleSystemMenu()
```

Assembles system menu.

---

#### assembleSystemMenu

protected void assembleSystemMenu()

Assembles system menu.

addSystemMenuItems

```java
protected void addSystemMenuItems​(
JMenu
systemMenu)
```

Adds system menu items to

systemMenu

.

**Parameters:** systemMenu

- an instance of

JMenu

---

#### addSystemMenuItems

protected void addSystemMenuItems​(

JMenu

systemMenu)

Adds system menu items to

systemMenu

.

createSystemMenu

```java
protected
JMenu
createSystemMenu()
```

Returns a new instance of

JMenu

.

**Returns:** a new instance of

JMenu

---

#### createSystemMenu

protected

JMenu

createSystemMenu()

Returns a new instance of

JMenu

.

createSystemMenuBar

```java
protected
JMenuBar
createSystemMenuBar()
```

Returns a new instance of

JMenuBar

.

**Returns:** a new instance of

JMenuBar

---

#### createSystemMenuBar

protected

JMenuBar

createSystemMenuBar()

Returns a new instance of

JMenuBar

.

showSystemMenu

```java
protected void showSystemMenu()
```

Shows system menu.

---

#### showSystemMenu

protected void showSystemMenu()

Shows system menu.

paintTitleBackground

```java
protected void paintTitleBackground​(
Graphics
g)
```

Invoked from paintComponent.
Paints the background of the titlepane. All text and icons will
then be rendered on top of this background.

**Parameters:** g

- the graphics to use to render the background
**Since:** 1.4

---

#### paintTitleBackground

protected void paintTitleBackground​(

Graphics

g)

Invoked from paintComponent.
Paints the background of the titlepane. All text and icons will
then be rendered on top of this background.

getTitle

```java
protected
String
getTitle​(
String
text,

FontMetrics
fm,
int availTextWidth)
```

Returns the title.

**Parameters:** text

- a text
**Parameters:** fm

- an instance of

FontMetrics
**Parameters:** availTextWidth

- an available text width
**Returns:** the title.

---

#### getTitle

protected

String

getTitle​(

String

text,

FontMetrics

fm,
int availTextWidth)

Returns the title.

postClosingEvent

```java
protected void postClosingEvent​(
JInternalFrame
frame)
```

Post a WINDOW_CLOSING-like event to the frame, so that it can
be treated like a regular

Frame

.

**Parameters:** frame

- an instance of

JInternalFrame

---

#### postClosingEvent

protected void postClosingEvent​(

JInternalFrame

frame)

Post a WINDOW_CLOSING-like event to the frame, so that it can
be treated like a regular

Frame

.

enableActions

```java
protected void enableActions()
```

Enables actions.

---

#### enableActions

protected void enableActions()

Enables actions.

createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Returns an instance of

PropertyChangeListener

.

**Returns:** an instance of

PropertyChangeListener

---

#### createPropertyChangeListener

protected

PropertyChangeListener

createPropertyChangeListener()

Returns an instance of

PropertyChangeListener

.

createLayout

```java
protected
LayoutManager
createLayout()
```

Returns a layout manager.

**Returns:** a layout manager

---

#### createLayout

protected

LayoutManager

createLayout()

Returns a layout manager.

---

