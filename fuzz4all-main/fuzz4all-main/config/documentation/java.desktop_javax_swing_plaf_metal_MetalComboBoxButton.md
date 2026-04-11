# Class MetalComboBoxButton

**Source:** `java.desktop\javax\swing\plaf\metal\MetalComboBoxButton.html`

### Class Description

```java
public class
MetalComboBoxButton

extends
JButton
```

JButton subclass to help out MetalComboBoxUI

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

ItemSelectable

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

#### protected
JComboBox
<
Object
> comboBox

The instance of

JComboBox

.

---

#### protected
JList
<
Object
> listBox

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
Icon
comboIcon

The icon.

---

#### protected boolean iconOnly

The

iconOnly

value.

---

### Constructor Details

#### public MetalComboBoxButton​(
JComboBox
<
Object
> cb,

Icon
i,

CellRendererPane
pane,

JList
<
Object
> list)

Constructs a new instance of

MetalComboBoxButton

.

**Parameters:**
- cb

- an instance of

JComboBox
- i

- an icon
- pane

- an instance of

CellRendererPane
- list

- an instance of

JList

---

#### public MetalComboBoxButton​(
JComboBox
<
Object
> cb,

Icon
i,
boolean onlyIcon,

CellRendererPane
pane,

JList
<
Object
> list)

Constructs a new instance of

MetalComboBoxButton

.

**Parameters:**
- cb

- an instance of

JComboBox
- i

- an icon
- onlyIcon

- if

true

only icon is painted
- pane

- an instance of

CellRendererPane
- list

- an instance of

JList

---

### Method Details

#### public final
JComboBox
<
Object
> getComboBox()

Returns the

JComboBox

.

**Returns:**
- the

JComboBox

---

#### public final void setComboBox​(
JComboBox
<
Object
> cb)

Sets the

JComboBox

.

**Parameters:**
- cb

- the

JComboBox

---

#### public final
Icon
getComboIcon()

Returns the icon of the

JComboBox

.

**Returns:**
- the icon of the

JComboBox

---

#### public final void setComboIcon​(
Icon
i)

Sets the icon of the

JComboBox

.

**Parameters:**
- i

- the icon of the

JComboBox

---

#### public final boolean isIconOnly()

Returns the

isIconOnly

value.

**Returns:**
- the

isIconOnly

value

---

#### public final void setIconOnly​(boolean isIconOnly)

If

isIconOnly

is

true

then only icon is painted.

**Parameters:**
- isIconOnly

- if

true

then only icon is painted

---

### Additional Sections

#### Class MetalComboBoxButton

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.AbstractButton
- - javax.swing.JButton
- - javax.swing.plaf.metal.MetalComboBoxButton

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.AbstractButton
- - javax.swing.JButton
- - javax.swing.plaf.metal.MetalComboBoxButton

java.awt.Container

- javax.swing.JComponent
- - javax.swing.AbstractButton
- - javax.swing.JButton
- - javax.swing.plaf.metal.MetalComboBoxButton

javax.swing.JComponent

- javax.swing.AbstractButton
- - javax.swing.JButton
- - javax.swing.plaf.metal.MetalComboBoxButton

javax.swing.AbstractButton

- javax.swing.JButton
- - javax.swing.plaf.metal.MetalComboBoxButton

javax.swing.JButton

- javax.swing.plaf.metal.MetalComboBoxButton

javax.swing.plaf.metal.MetalComboBoxButton

**All Implemented Interfaces:** ImageObserver

,

ItemSelectable

,

MenuContainer

,

Serializable

,

Accessible

,

SwingConstants

```java
public class
MetalComboBoxButton

extends
JButton
```

JButton subclass to help out MetalComboBoxUI

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

**See Also:** MetalComboBoxButton

,

Serialized Form

public class

MetalComboBoxButton

extends

JButton

JButton subclass to help out MetalComboBoxUI

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

- Nested classes/interfaces declared in class javax.swing.

JButton

JButton.AccessibleJButton

- Nested classes/interfaces declared in class javax.swing.

AbstractButton

AbstractButton.AccessibleAbstractButton

,

AbstractButton.ButtonChangeListener

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

JComboBox

<

Object

>

comboBox

The instance of

JComboBox

.

protected

Icon

comboIcon

The icon.

protected boolean

iconOnly

The

iconOnly

value.

protected

JList

<

Object

>

listBox

The instance of

JList

.

protected

CellRendererPane

rendererPane

The instance of

CellRendererPane

.

- Fields declared in class javax.swing.

AbstractButton

actionListener

,

BORDER_PAINTED_CHANGED_PROPERTY

,

changeEvent

,

changeListener

,

CONTENT_AREA_FILLED_CHANGED_PROPERTY

,

DISABLED_ICON_CHANGED_PROPERTY

,

DISABLED_SELECTED_ICON_CHANGED_PROPERTY

,

FOCUS_PAINTED_CHANGED_PROPERTY

,

HORIZONTAL_ALIGNMENT_CHANGED_PROPERTY

,

HORIZONTAL_TEXT_POSITION_CHANGED_PROPERTY

,

ICON_CHANGED_PROPERTY

,

itemListener

,

MARGIN_CHANGED_PROPERTY

,

MNEMONIC_CHANGED_PROPERTY

,

model

,

MODEL_CHANGED_PROPERTY

,

PRESSED_ICON_CHANGED_PROPERTY

,

ROLLOVER_ENABLED_CHANGED_PROPERTY

,

ROLLOVER_ICON_CHANGED_PROPERTY

,

ROLLOVER_SELECTED_ICON_CHANGED_PROPERTY

,

SELECTED_ICON_CHANGED_PROPERTY

,

TEXT_CHANGED_PROPERTY

,

VERTICAL_ALIGNMENT_CHANGED_PROPERTY

,

VERTICAL_TEXT_POSITION_CHANGED_PROPERTY

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

MetalComboBoxButton

​(

JComboBox

<

Object

> cb,

Icon

i,
boolean onlyIcon,

CellRendererPane

pane,

JList

<

Object

> list)

Constructs a new instance of

MetalComboBoxButton

.

MetalComboBoxButton

​(

JComboBox

<

Object

> cb,

Icon

i,

CellRendererPane

pane,

JList

<

Object

> list)

Constructs a new instance of

MetalComboBoxButton

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JComboBox

<

Object

>

getComboBox

()

Returns the

JComboBox

.

Icon

getComboIcon

()

Returns the icon of the

JComboBox

.

boolean

isIconOnly

()

Returns the

isIconOnly

value.

void

setComboBox

​(

JComboBox

<

Object

> cb)

Sets the

JComboBox

.

void

setComboIcon

​(

Icon

i)

Sets the icon of the

JComboBox

.

void

setIconOnly

​(boolean isIconOnly)

If

isIconOnly

is

true

then only icon is painted.

- Methods declared in class javax.swing.

JButton

getAccessibleContext

,

getUIClassID

,

isDefaultButton

,

isDefaultCapable

,

paramString

,

removeNotify

,

setDefaultCapable

,

updateUI

- Methods declared in class javax.swing.

AbstractButton

actionPropertyChanged

,

addActionListener

,

addChangeListener

,

addImpl

,

addItemListener

,

checkHorizontalKey

,

checkVerticalKey

,

configurePropertiesFromAction

,

createActionListener

,

createActionPropertyChangeListener

,

createChangeListener

,

createItemListener

,

doClick

,

doClick

,

fireActionPerformed

,

fireItemStateChanged

,

fireStateChanged

,

getAction

,

getActionCommand

,

getActionListeners

,

getChangeListeners

,

getDisabledIcon

,

getDisabledSelectedIcon

,

getDisplayedMnemonicIndex

,

getHideActionText

,

getHorizontalAlignment

,

getHorizontalTextPosition

,

getIcon

,

getIconTextGap

,

getItemListeners

,

getLabel

,

getMargin

,

getMnemonic

,

getModel

,

getMultiClickThreshhold

,

getPressedIcon

,

getRolloverIcon

,

getRolloverSelectedIcon

,

getSelectedIcon

,

getSelectedObjects

,

getText

,

getUI

,

getVerticalAlignment

,

getVerticalTextPosition

,

imageUpdate

,

init

,

isBorderPainted

,

isContentAreaFilled

,

isFocusPainted

,

isRolloverEnabled

,

isSelected

,

paintBorder

,

removeActionListener

,

removeChangeListener

,

removeItemListener

,

setAction

,

setActionCommand

,

setBorderPainted

,

setContentAreaFilled

,

setDisabledIcon

,

setDisabledSelectedIcon

,

setDisplayedMnemonicIndex

,

setEnabled

,

setFocusPainted

,

setHideActionText

,

setHorizontalAlignment

,

setHorizontalTextPosition

,

setIcon

,

setIconTextGap

,

setLabel

,

setLayout

,

setMargin

,

setMnemonic

,

setMnemonic

,

setModel

,

setMultiClickThreshhold

,

setPressedIcon

,

setRolloverEnabled

,

setRolloverIcon

,

setRolloverSelectedIcon

,

setSelected

,

setSelectedIcon

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

JButton

JButton.AccessibleJButton

- Nested classes/interfaces declared in class javax.swing.

AbstractButton

AbstractButton.AccessibleAbstractButton

,

AbstractButton.ButtonChangeListener

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

JButton

JButton.AccessibleJButton

---

#### Nested classes/interfaces declared in class javax.swing. JButton

Nested classes/interfaces declared in class javax.swing.

AbstractButton

AbstractButton.AccessibleAbstractButton

,

AbstractButton.ButtonChangeListener

---

#### Nested classes/interfaces declared in class javax.swing. AbstractButton

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

JComboBox

<

Object

>

comboBox

The instance of

JComboBox

.

protected

Icon

comboIcon

The icon.

protected boolean

iconOnly

The

iconOnly

value.

protected

JList

<

Object

>

listBox

The instance of

JList

.

protected

CellRendererPane

rendererPane

The instance of

CellRendererPane

.

- Fields declared in class javax.swing.

AbstractButton

actionListener

,

BORDER_PAINTED_CHANGED_PROPERTY

,

changeEvent

,

changeListener

,

CONTENT_AREA_FILLED_CHANGED_PROPERTY

,

DISABLED_ICON_CHANGED_PROPERTY

,

DISABLED_SELECTED_ICON_CHANGED_PROPERTY

,

FOCUS_PAINTED_CHANGED_PROPERTY

,

HORIZONTAL_ALIGNMENT_CHANGED_PROPERTY

,

HORIZONTAL_TEXT_POSITION_CHANGED_PROPERTY

,

ICON_CHANGED_PROPERTY

,

itemListener

,

MARGIN_CHANGED_PROPERTY

,

MNEMONIC_CHANGED_PROPERTY

,

model

,

MODEL_CHANGED_PROPERTY

,

PRESSED_ICON_CHANGED_PROPERTY

,

ROLLOVER_ENABLED_CHANGED_PROPERTY

,

ROLLOVER_ICON_CHANGED_PROPERTY

,

ROLLOVER_SELECTED_ICON_CHANGED_PROPERTY

,

SELECTED_ICON_CHANGED_PROPERTY

,

TEXT_CHANGED_PROPERTY

,

VERTICAL_ALIGNMENT_CHANGED_PROPERTY

,

VERTICAL_TEXT_POSITION_CHANGED_PROPERTY

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

The instance of

JComboBox

.

The icon.

The

iconOnly

value.

The instance of

JList

.

The instance of

CellRendererPane

.

Fields declared in class javax.swing.

AbstractButton

actionListener

,

BORDER_PAINTED_CHANGED_PROPERTY

,

changeEvent

,

changeListener

,

CONTENT_AREA_FILLED_CHANGED_PROPERTY

,

DISABLED_ICON_CHANGED_PROPERTY

,

DISABLED_SELECTED_ICON_CHANGED_PROPERTY

,

FOCUS_PAINTED_CHANGED_PROPERTY

,

HORIZONTAL_ALIGNMENT_CHANGED_PROPERTY

,

HORIZONTAL_TEXT_POSITION_CHANGED_PROPERTY

,

ICON_CHANGED_PROPERTY

,

itemListener

,

MARGIN_CHANGED_PROPERTY

,

MNEMONIC_CHANGED_PROPERTY

,

model

,

MODEL_CHANGED_PROPERTY

,

PRESSED_ICON_CHANGED_PROPERTY

,

ROLLOVER_ENABLED_CHANGED_PROPERTY

,

ROLLOVER_ICON_CHANGED_PROPERTY

,

ROLLOVER_SELECTED_ICON_CHANGED_PROPERTY

,

SELECTED_ICON_CHANGED_PROPERTY

,

TEXT_CHANGED_PROPERTY

,

VERTICAL_ALIGNMENT_CHANGED_PROPERTY

,

VERTICAL_TEXT_POSITION_CHANGED_PROPERTY

---

#### Fields declared in class javax.swing. AbstractButton

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

MetalComboBoxButton

​(

JComboBox

<

Object

> cb,

Icon

i,
boolean onlyIcon,

CellRendererPane

pane,

JList

<

Object

> list)

Constructs a new instance of

MetalComboBoxButton

.

MetalComboBoxButton

​(

JComboBox

<

Object

> cb,

Icon

i,

CellRendererPane

pane,

JList

<

Object

> list)

Constructs a new instance of

MetalComboBoxButton

.

---

#### Constructor Summary

Constructs a new instance of

MetalComboBoxButton

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JComboBox

<

Object

>

getComboBox

()

Returns the

JComboBox

.

Icon

getComboIcon

()

Returns the icon of the

JComboBox

.

boolean

isIconOnly

()

Returns the

isIconOnly

value.

void

setComboBox

​(

JComboBox

<

Object

> cb)

Sets the

JComboBox

.

void

setComboIcon

​(

Icon

i)

Sets the icon of the

JComboBox

.

void

setIconOnly

​(boolean isIconOnly)

If

isIconOnly

is

true

then only icon is painted.

- Methods declared in class javax.swing.

JButton

getAccessibleContext

,

getUIClassID

,

isDefaultButton

,

isDefaultCapable

,

paramString

,

removeNotify

,

setDefaultCapable

,

updateUI

- Methods declared in class javax.swing.

AbstractButton

actionPropertyChanged

,

addActionListener

,

addChangeListener

,

addImpl

,

addItemListener

,

checkHorizontalKey

,

checkVerticalKey

,

configurePropertiesFromAction

,

createActionListener

,

createActionPropertyChangeListener

,

createChangeListener

,

createItemListener

,

doClick

,

doClick

,

fireActionPerformed

,

fireItemStateChanged

,

fireStateChanged

,

getAction

,

getActionCommand

,

getActionListeners

,

getChangeListeners

,

getDisabledIcon

,

getDisabledSelectedIcon

,

getDisplayedMnemonicIndex

,

getHideActionText

,

getHorizontalAlignment

,

getHorizontalTextPosition

,

getIcon

,

getIconTextGap

,

getItemListeners

,

getLabel

,

getMargin

,

getMnemonic

,

getModel

,

getMultiClickThreshhold

,

getPressedIcon

,

getRolloverIcon

,

getRolloverSelectedIcon

,

getSelectedIcon

,

getSelectedObjects

,

getText

,

getUI

,

getVerticalAlignment

,

getVerticalTextPosition

,

imageUpdate

,

init

,

isBorderPainted

,

isContentAreaFilled

,

isFocusPainted

,

isRolloverEnabled

,

isSelected

,

paintBorder

,

removeActionListener

,

removeChangeListener

,

removeItemListener

,

setAction

,

setActionCommand

,

setBorderPainted

,

setContentAreaFilled

,

setDisabledIcon

,

setDisabledSelectedIcon

,

setDisplayedMnemonicIndex

,

setEnabled

,

setFocusPainted

,

setHideActionText

,

setHorizontalAlignment

,

setHorizontalTextPosition

,

setIcon

,

setIconTextGap

,

setLabel

,

setLayout

,

setMargin

,

setMnemonic

,

setMnemonic

,

setModel

,

setMultiClickThreshhold

,

setPressedIcon

,

setRolloverEnabled

,

setRolloverIcon

,

setRolloverSelectedIcon

,

setSelected

,

setSelectedIcon

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

Returns the

JComboBox

.

Returns the icon of the

JComboBox

.

Returns the

isIconOnly

value.

Sets the

JComboBox

.

Sets the icon of the

JComboBox

.

If

isIconOnly

is

true

then only icon is painted.

Methods declared in class javax.swing.

JButton

getAccessibleContext

,

getUIClassID

,

isDefaultButton

,

isDefaultCapable

,

paramString

,

removeNotify

,

setDefaultCapable

,

updateUI

---

#### Methods declared in class javax.swing. JButton

Methods declared in class javax.swing.

AbstractButton

actionPropertyChanged

,

addActionListener

,

addChangeListener

,

addImpl

,

addItemListener

,

checkHorizontalKey

,

checkVerticalKey

,

configurePropertiesFromAction

,

createActionListener

,

createActionPropertyChangeListener

,

createChangeListener

,

createItemListener

,

doClick

,

doClick

,

fireActionPerformed

,

fireItemStateChanged

,

fireStateChanged

,

getAction

,

getActionCommand

,

getActionListeners

,

getChangeListeners

,

getDisabledIcon

,

getDisabledSelectedIcon

,

getDisplayedMnemonicIndex

,

getHideActionText

,

getHorizontalAlignment

,

getHorizontalTextPosition

,

getIcon

,

getIconTextGap

,

getItemListeners

,

getLabel

,

getMargin

,

getMnemonic

,

getModel

,

getMultiClickThreshhold

,

getPressedIcon

,

getRolloverIcon

,

getRolloverSelectedIcon

,

getSelectedIcon

,

getSelectedObjects

,

getText

,

getUI

,

getVerticalAlignment

,

getVerticalTextPosition

,

imageUpdate

,

init

,

isBorderPainted

,

isContentAreaFilled

,

isFocusPainted

,

isRolloverEnabled

,

isSelected

,

paintBorder

,

removeActionListener

,

removeChangeListener

,

removeItemListener

,

setAction

,

setActionCommand

,

setBorderPainted

,

setContentAreaFilled

,

setDisabledIcon

,

setDisabledSelectedIcon

,

setDisplayedMnemonicIndex

,

setEnabled

,

setFocusPainted

,

setHideActionText

,

setHorizontalAlignment

,

setHorizontalTextPosition

,

setIcon

,

setIconTextGap

,

setLabel

,

setLayout

,

setMargin

,

setMnemonic

,

setMnemonic

,

setModel

,

setMultiClickThreshhold

,

setPressedIcon

,

setRolloverEnabled

,

setRolloverIcon

,

setRolloverSelectedIcon

,

setSelected

,

setSelectedIcon

,

setText

,

setUI

,

setVerticalAlignment

,

setVerticalTextPosition

---

#### Methods declared in class javax.swing. AbstractButton

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

- comboBox

```java
protected
JComboBox
<
Object
> comboBox
```

The instance of

JComboBox

.

- listBox

```java
protected
JList
<
Object
> listBox
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

- comboIcon

```java
protected
Icon
comboIcon
```

The icon.

- iconOnly

```java
protected boolean iconOnly
```

The

iconOnly

value.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MetalComboBoxButton

```java
public MetalComboBoxButton​(
JComboBox
<
Object
> cb,

Icon
i,

CellRendererPane
pane,

JList
<
Object
> list)
```

Constructs a new instance of

MetalComboBoxButton

.

**Parameters:** cb

- an instance of

JComboBox
**Parameters:** i

- an icon
**Parameters:** pane

- an instance of

CellRendererPane
**Parameters:** list

- an instance of

JList

- MetalComboBoxButton

```java
public MetalComboBoxButton​(
JComboBox
<
Object
> cb,

Icon
i,
boolean onlyIcon,

CellRendererPane
pane,

JList
<
Object
> list)
```

Constructs a new instance of

MetalComboBoxButton

.

**Parameters:** cb

- an instance of

JComboBox
**Parameters:** i

- an icon
**Parameters:** onlyIcon

- if

true

only icon is painted
**Parameters:** pane

- an instance of

CellRendererPane
**Parameters:** list

- an instance of

JList

============ METHOD DETAIL ==========

- Method Detail

- getComboBox

```java
public final
JComboBox
<
Object
> getComboBox()
```

Returns the

JComboBox

.

**Returns:** the

JComboBox

- setComboBox

```java
public final void setComboBox​(
JComboBox
<
Object
> cb)
```

Sets the

JComboBox

.

**Parameters:** cb

- the

JComboBox

- getComboIcon

```java
public final
Icon
getComboIcon()
```

Returns the icon of the

JComboBox

.

**Returns:** the icon of the

JComboBox

- setComboIcon

```java
public final void setComboIcon​(
Icon
i)
```

Sets the icon of the

JComboBox

.

**Parameters:** i

- the icon of the

JComboBox

- isIconOnly

```java
public final boolean isIconOnly()
```

Returns the

isIconOnly

value.

**Returns:** the

isIconOnly

value

- setIconOnly

```java
public final void setIconOnly​(boolean isIconOnly)
```

If

isIconOnly

is

true

then only icon is painted.

**Parameters:** isIconOnly

- if

true

then only icon is painted

Field Detail

- comboBox

```java
protected
JComboBox
<
Object
> comboBox
```

The instance of

JComboBox

.

- listBox

```java
protected
JList
<
Object
> listBox
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

- comboIcon

```java
protected
Icon
comboIcon
```

The icon.

- iconOnly

```java
protected boolean iconOnly
```

The

iconOnly

value.

---

#### Field Detail

comboBox

```java
protected
JComboBox
<
Object
> comboBox
```

The instance of

JComboBox

.

---

#### comboBox

protected

JComboBox

<

Object

> comboBox

The instance of

JComboBox

.

listBox

```java
protected
JList
<
Object
> listBox
```

The instance of

JList

.

---

#### listBox

protected

JList

<

Object

> listBox

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

comboIcon

```java
protected
Icon
comboIcon
```

The icon.

---

#### comboIcon

protected

Icon

comboIcon

The icon.

iconOnly

```java
protected boolean iconOnly
```

The

iconOnly

value.

---

#### iconOnly

protected boolean iconOnly

The

iconOnly

value.

Constructor Detail

- MetalComboBoxButton

```java
public MetalComboBoxButton​(
JComboBox
<
Object
> cb,

Icon
i,

CellRendererPane
pane,

JList
<
Object
> list)
```

Constructs a new instance of

MetalComboBoxButton

.

**Parameters:** cb

- an instance of

JComboBox
**Parameters:** i

- an icon
**Parameters:** pane

- an instance of

CellRendererPane
**Parameters:** list

- an instance of

JList

- MetalComboBoxButton

```java
public MetalComboBoxButton​(
JComboBox
<
Object
> cb,

Icon
i,
boolean onlyIcon,

CellRendererPane
pane,

JList
<
Object
> list)
```

Constructs a new instance of

MetalComboBoxButton

.

**Parameters:** cb

- an instance of

JComboBox
**Parameters:** i

- an icon
**Parameters:** onlyIcon

- if

true

only icon is painted
**Parameters:** pane

- an instance of

CellRendererPane
**Parameters:** list

- an instance of

JList

---

#### Constructor Detail

MetalComboBoxButton

```java
public MetalComboBoxButton​(
JComboBox
<
Object
> cb,

Icon
i,

CellRendererPane
pane,

JList
<
Object
> list)
```

Constructs a new instance of

MetalComboBoxButton

.

**Parameters:** cb

- an instance of

JComboBox
**Parameters:** i

- an icon
**Parameters:** pane

- an instance of

CellRendererPane
**Parameters:** list

- an instance of

JList

---

#### MetalComboBoxButton

public MetalComboBoxButton​(

JComboBox

<

Object

> cb,

Icon

i,

CellRendererPane

pane,

JList

<

Object

> list)

Constructs a new instance of

MetalComboBoxButton

.

MetalComboBoxButton

```java
public MetalComboBoxButton​(
JComboBox
<
Object
> cb,

Icon
i,
boolean onlyIcon,

CellRendererPane
pane,

JList
<
Object
> list)
```

Constructs a new instance of

MetalComboBoxButton

.

**Parameters:** cb

- an instance of

JComboBox
**Parameters:** i

- an icon
**Parameters:** onlyIcon

- if

true

only icon is painted
**Parameters:** pane

- an instance of

CellRendererPane
**Parameters:** list

- an instance of

JList

---

#### MetalComboBoxButton

public MetalComboBoxButton​(

JComboBox

<

Object

> cb,

Icon

i,
boolean onlyIcon,

CellRendererPane

pane,

JList

<

Object

> list)

Constructs a new instance of

MetalComboBoxButton

.

Method Detail

- getComboBox

```java
public final
JComboBox
<
Object
> getComboBox()
```

Returns the

JComboBox

.

**Returns:** the

JComboBox

- setComboBox

```java
public final void setComboBox​(
JComboBox
<
Object
> cb)
```

Sets the

JComboBox

.

**Parameters:** cb

- the

JComboBox

- getComboIcon

```java
public final
Icon
getComboIcon()
```

Returns the icon of the

JComboBox

.

**Returns:** the icon of the

JComboBox

- setComboIcon

```java
public final void setComboIcon​(
Icon
i)
```

Sets the icon of the

JComboBox

.

**Parameters:** i

- the icon of the

JComboBox

- isIconOnly

```java
public final boolean isIconOnly()
```

Returns the

isIconOnly

value.

**Returns:** the

isIconOnly

value

- setIconOnly

```java
public final void setIconOnly​(boolean isIconOnly)
```

If

isIconOnly

is

true

then only icon is painted.

**Parameters:** isIconOnly

- if

true

then only icon is painted

---

#### Method Detail

getComboBox

```java
public final
JComboBox
<
Object
> getComboBox()
```

Returns the

JComboBox

.

**Returns:** the

JComboBox

---

#### getComboBox

public final

JComboBox

<

Object

> getComboBox()

Returns the

JComboBox

.

setComboBox

```java
public final void setComboBox​(
JComboBox
<
Object
> cb)
```

Sets the

JComboBox

.

**Parameters:** cb

- the

JComboBox

---

#### setComboBox

public final void setComboBox​(

JComboBox

<

Object

> cb)

Sets the

JComboBox

.

getComboIcon

```java
public final
Icon
getComboIcon()
```

Returns the icon of the

JComboBox

.

**Returns:** the icon of the

JComboBox

---

#### getComboIcon

public final

Icon

getComboIcon()

Returns the icon of the

JComboBox

.

setComboIcon

```java
public final void setComboIcon​(
Icon
i)
```

Sets the icon of the

JComboBox

.

**Parameters:** i

- the icon of the

JComboBox

---

#### setComboIcon

public final void setComboIcon​(

Icon

i)

Sets the icon of the

JComboBox

.

isIconOnly

```java
public final boolean isIconOnly()
```

Returns the

isIconOnly

value.

**Returns:** the

isIconOnly

value

---

#### isIconOnly

public final boolean isIconOnly()

Returns the

isIconOnly

value.

setIconOnly

```java
public final void setIconOnly​(boolean isIconOnly)
```

If

isIconOnly

is

true

then only icon is painted.

**Parameters:** isIconOnly

- if

true

then only icon is painted

---

#### setIconOnly

public final void setIconOnly​(boolean isIconOnly)

If

isIconOnly

is

true

then only icon is painted.

---

