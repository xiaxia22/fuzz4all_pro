# Class JButton

**Source:** `java.desktop\javax\swing\JButton.html`

### Class Description

```java
@JavaBean
(
defaultProperty
="UIClassID",

description
="An implementation of a \"push\" button.")
public class
JButton

extends
AbstractButton

implements
Accessible
```

An implementation of a "push" button.

Buttons can be configured, and to some degree controlled, by

Action

s. Using an

Action

with a button has many benefits beyond directly
configuring a button. Refer to

Swing Components Supporting

Action

for more
details, and you can find more information in

How
to Use Actions

, a section in

The Java Tutorial

.

See

How to Use Buttons, Check Boxes, and Radio Buttons

in

The Java Tutorial

for information and examples of using buttons.

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

*No entries found.*

### Constructor Details

#### public JButton()

Creates a button with no set text or icon.

---

#### public JButton​(
Icon
icon)

Creates a button with an icon.

**Parameters:**
- icon

- the Icon image to display on the button

---

#### @ConstructorProperties
("text")
public JButton​(
String
text)

Creates a button with text.

**Parameters:**
- text

- the text of the button

---

#### public JButton​(
Action
a)

Creates a button where properties are taken from the

Action

supplied.

**Parameters:**
- a

- the

Action

used to specify the new button

**Since:**
- 1.3

---

#### public JButton​(
String
text,

Icon
icon)

Creates a button with initial text and an icon.

**Parameters:**
- text

- the text of the button
- icon

- the Icon image to display on the button

---

### Method Details

#### public void updateUI()

Resets the UI property to a value from the current look and
feel.

**Overrides:**
- updateUI

in class

AbstractButton

**See Also:**
- JComponent.updateUI()

---

#### @BeanProperty
(
bound
=false,

expert
=true,

description
="A string that specifies the name of the L&F class.")
public
String
getUIClassID()

Returns a string that specifies the name of the L&F class
that renders this component.

**Overrides:**
- getUIClassID

in class

JComponent

**Returns:**
- the string "ButtonUI"

**See Also:**
- JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### @BeanProperty
(
bound
=false,

description
="Whether or not this button is the default button")
public boolean isDefaultButton()

Gets the value of the

defaultButton

property,
which if

true

means that this button is the current
default button for its

JRootPane

.
Most look and feels render the default button
differently, and may potentially provide bindings
to access the default button.

**Returns:**
- the value of the

defaultButton

property

**See Also:**
- JRootPane.setDefaultButton(javax.swing.JButton)

,

isDefaultCapable()

---

#### public boolean isDefaultCapable()

Gets the value of the

defaultCapable

property.

**Returns:**
- the value of the

defaultCapable

property

**See Also:**
- setDefaultCapable(boolean)

,

isDefaultButton()

,

JRootPane.setDefaultButton(javax.swing.JButton)

---

#### @BeanProperty
(
visualUpdate
=true,

description
="Whether or not this button can be the default button")
public void setDefaultCapable​(boolean defaultCapable)

Sets the

defaultCapable

property,
which determines whether this button can be
made the default button for its root pane.
The default value of the

defaultCapable

property is

true

unless otherwise
specified by the look and feel.

**Parameters:**
- defaultCapable

-

true

if this button will be
capable of being the default button on the

RootPane

; otherwise

false

**See Also:**
- isDefaultCapable()

---

#### public void removeNotify()

Overrides

JComponent.removeNotify

to check if
this button is currently set as the default button on the

RootPane

, and if so, sets the

RootPane

's
default button to

null

to ensure the

RootPane

doesn't hold onto an invalid button reference.

**Overrides:**
- removeNotify

in class

AbstractButton

**See Also:**
- JComponent.registerKeyboardAction(java.awt.event.ActionListener, java.lang.String, javax.swing.KeyStroke, int)

---

#### protected
String
paramString()

Returns a string representation of this

JButton

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:**
- paramString

in class

AbstractButton

**Returns:**
- a string representation of this

JButton

---

#### @BeanProperty
(
bound
=false,

expert
=true,

description
="The AccessibleContext associated with this Button.")
public
AccessibleContext
getAccessibleContext()

Gets the

AccessibleContext

associated with this

JButton

. For

JButton

s,
the

AccessibleContext

takes the form of an

AccessibleJButton

.
A new

AccessibleJButton

instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- an

AccessibleJButton

that serves as the

AccessibleContext

of this

JButton

---

### Additional Sections

#### Class JButton

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.AbstractButton
- - javax.swing.JButton

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.AbstractButton
- - javax.swing.JButton

java.awt.Container

- javax.swing.JComponent
- - javax.swing.AbstractButton
- - javax.swing.JButton

javax.swing.JComponent

- javax.swing.AbstractButton
- - javax.swing.JButton

javax.swing.AbstractButton

- javax.swing.JButton

javax.swing.JButton

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

**Direct Known Subclasses:** BasicArrowButton

,

MetalComboBoxButton

```java
@JavaBean
(
defaultProperty
="UIClassID",

description
="An implementation of a \"push\" button.")
public class
JButton

extends
AbstractButton

implements
Accessible
```

An implementation of a "push" button.

Buttons can be configured, and to some degree controlled, by

Action

s. Using an

Action

with a button has many benefits beyond directly
configuring a button. Refer to

Swing Components Supporting

Action

for more
details, and you can find more information in

How
to Use Actions

, a section in

The Java Tutorial

.

See

How to Use Buttons, Check Boxes, and Radio Buttons

in

The Java Tutorial

for information and examples of using buttons.

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
**See Also:** Serialized Form

@JavaBean

(

defaultProperty

="UIClassID",

description

="An implementation of a \"push\" button.")
public class

JButton

extends

AbstractButton

implements

Accessible

An implementation of a "push" button.

Buttons can be configured, and to some degree controlled, by

Action

s. Using an

Action

with a button has many benefits beyond directly
configuring a button. Refer to

Swing Components Supporting

Action

for more
details, and you can find more information in

How
to Use Actions

, a section in

The Java Tutorial

.

See

How to Use Buttons, Check Boxes, and Radio Buttons

in

The Java Tutorial

for information and examples of using buttons.

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

Buttons can be configured, and to some degree controlled, by

Action

s. Using an

Action

with a button has many benefits beyond directly
configuring a button. Refer to

Swing Components Supporting

Action

for more
details, and you can find more information in

How
to Use Actions

, a section in

The Java Tutorial

.

See

How to Use Buttons, Check Boxes, and Radio Buttons

in

The Java Tutorial

for information and examples of using buttons.

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

How to Use Buttons, Check Boxes, and Radio Buttons

in

The Java Tutorial

for information and examples of using buttons.

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

JButton.AccessibleJButton

This class implements accessibility support for the

JButton

class.

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

JButton

()

Creates a button with no set text or icon.

JButton

​(

String

text)

Creates a button with text.

JButton

​(

String

text,

Icon

icon)

Creates a button with initial text and an icon.

JButton

​(

Action

a)

Creates a button where properties are taken from the

Action

supplied.

JButton

​(

Icon

icon)

Creates a button with an icon.

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

Gets the

AccessibleContext

associated with this

JButton

.

String

getUIClassID

()

Returns a string that specifies the name of the L&F class
that renders this component.

boolean

isDefaultButton

()

Gets the value of the

defaultButton

property,
which if

true

means that this button is the current
default button for its

JRootPane

.

boolean

isDefaultCapable

()

Gets the value of the

defaultCapable

property.

protected

String

paramString

()

Returns a string representation of this

JButton

.

void

removeNotify

()

Overrides

JComponent.removeNotify

to check if
this button is currently set as the default button on the

RootPane

, and if so, sets the

RootPane

's
default button to

null

to ensure the

RootPane

doesn't hold onto an invalid button reference.

void

setDefaultCapable

​(boolean defaultCapable)

Sets the

defaultCapable

property,
which determines whether this button can be
made the default button for its root pane.

void

updateUI

()

Resets the UI property to a value from the current look and
feel.

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

Nested Classes

Modifier and Type

Class

Description

protected class

JButton.AccessibleJButton

This class implements accessibility support for the

JButton

class.

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

This class implements accessibility support for the

JButton

class.

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

JButton

()

Creates a button with no set text or icon.

JButton

​(

String

text)

Creates a button with text.

JButton

​(

String

text,

Icon

icon)

Creates a button with initial text and an icon.

JButton

​(

Action

a)

Creates a button where properties are taken from the

Action

supplied.

JButton

​(

Icon

icon)

Creates a button with an icon.

---

#### Constructor Summary

Creates a button with no set text or icon.

Creates a button with text.

Creates a button with initial text and an icon.

Creates a button where properties are taken from the

Action

supplied.

Creates a button with an icon.

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

Gets the

AccessibleContext

associated with this

JButton

.

String

getUIClassID

()

Returns a string that specifies the name of the L&F class
that renders this component.

boolean

isDefaultButton

()

Gets the value of the

defaultButton

property,
which if

true

means that this button is the current
default button for its

JRootPane

.

boolean

isDefaultCapable

()

Gets the value of the

defaultCapable

property.

protected

String

paramString

()

Returns a string representation of this

JButton

.

void

removeNotify

()

Overrides

JComponent.removeNotify

to check if
this button is currently set as the default button on the

RootPane

, and if so, sets the

RootPane

's
default button to

null

to ensure the

RootPane

doesn't hold onto an invalid button reference.

void

setDefaultCapable

​(boolean defaultCapable)

Sets the

defaultCapable

property,
which determines whether this button can be
made the default button for its root pane.

void

updateUI

()

Resets the UI property to a value from the current look and
feel.

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

Gets the

AccessibleContext

associated with this

JButton

.

Returns a string that specifies the name of the L&F class
that renders this component.

Gets the value of the

defaultButton

property,
which if

true

means that this button is the current
default button for its

JRootPane

.

Gets the value of the

defaultCapable

property.

Returns a string representation of this

JButton

.

Overrides

JComponent.removeNotify

to check if
this button is currently set as the default button on the

RootPane

, and if so, sets the

RootPane

's
default button to

null

to ensure the

RootPane

doesn't hold onto an invalid button reference.

Sets the

defaultCapable

property,
which determines whether this button can be
made the default button for its root pane.

Resets the UI property to a value from the current look and
feel.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JButton

```java
public JButton()
```

Creates a button with no set text or icon.

- JButton

```java
public JButton​(
Icon
icon)
```

Creates a button with an icon.

**Parameters:** icon

- the Icon image to display on the button

- JButton

```java
@ConstructorProperties
("text")
public JButton​(
String
text)
```

Creates a button with text.

**Parameters:** text

- the text of the button

- JButton

```java
public JButton​(
Action
a)
```

Creates a button where properties are taken from the

Action

supplied.

**Parameters:** a

- the

Action

used to specify the new button
**Since:** 1.3

- JButton

```java
public JButton​(
String
text,

Icon
icon)
```

Creates a button with initial text and an icon.

**Parameters:** text

- the text of the button
**Parameters:** icon

- the Icon image to display on the button

============ METHOD DETAIL ==========

- Method Detail

- updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look and
feel.

**Overrides:** updateUI

in class

AbstractButton
**See Also:** JComponent.updateUI()

- getUIClassID

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="A string that specifies the name of the L&F class.")
public
String
getUIClassID()
```

Returns a string that specifies the name of the L&F class
that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "ButtonUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- isDefaultButton

```java
@BeanProperty
(
bound
=false,

description
="Whether or not this button is the default button")
public boolean isDefaultButton()
```

Gets the value of the

defaultButton

property,
which if

true

means that this button is the current
default button for its

JRootPane

.
Most look and feels render the default button
differently, and may potentially provide bindings
to access the default button.

**Returns:** the value of the

defaultButton

property
**See Also:** JRootPane.setDefaultButton(javax.swing.JButton)

,

isDefaultCapable()

- isDefaultCapable

```java
public boolean isDefaultCapable()
```

Gets the value of the

defaultCapable

property.

**Returns:** the value of the

defaultCapable

property
**See Also:** setDefaultCapable(boolean)

,

isDefaultButton()

,

JRootPane.setDefaultButton(javax.swing.JButton)

- setDefaultCapable

```java
@BeanProperty
(
visualUpdate
=true,

description
="Whether or not this button can be the default button")
public void setDefaultCapable​(boolean defaultCapable)
```

Sets the

defaultCapable

property,
which determines whether this button can be
made the default button for its root pane.
The default value of the

defaultCapable

property is

true

unless otherwise
specified by the look and feel.

**Parameters:** defaultCapable

-

true

if this button will be
capable of being the default button on the

RootPane

; otherwise

false
**See Also:** isDefaultCapable()

- removeNotify

```java
public void removeNotify()
```

Overrides

JComponent.removeNotify

to check if
this button is currently set as the default button on the

RootPane

, and if so, sets the

RootPane

's
default button to

null

to ensure the

RootPane

doesn't hold onto an invalid button reference.

**Overrides:** removeNotify

in class

AbstractButton
**See Also:** JComponent.registerKeyboardAction(java.awt.event.ActionListener, java.lang.String, javax.swing.KeyStroke, int)

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JButton

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

AbstractButton
**Returns:** a string representation of this

JButton

- getAccessibleContext

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The AccessibleContext associated with this Button.")
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated with this

JButton

. For

JButton

s,
the

AccessibleContext

takes the form of an

AccessibleJButton

.
A new

AccessibleJButton

instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an

AccessibleJButton

that serves as the

AccessibleContext

of this

JButton

Constructor Detail

- JButton

```java
public JButton()
```

Creates a button with no set text or icon.

- JButton

```java
public JButton​(
Icon
icon)
```

Creates a button with an icon.

**Parameters:** icon

- the Icon image to display on the button

- JButton

```java
@ConstructorProperties
("text")
public JButton​(
String
text)
```

Creates a button with text.

**Parameters:** text

- the text of the button

- JButton

```java
public JButton​(
Action
a)
```

Creates a button where properties are taken from the

Action

supplied.

**Parameters:** a

- the

Action

used to specify the new button
**Since:** 1.3

- JButton

```java
public JButton​(
String
text,

Icon
icon)
```

Creates a button with initial text and an icon.

**Parameters:** text

- the text of the button
**Parameters:** icon

- the Icon image to display on the button

---

#### Constructor Detail

JButton

```java
public JButton()
```

Creates a button with no set text or icon.

---

#### JButton

public JButton()

Creates a button with no set text or icon.

JButton

```java
public JButton​(
Icon
icon)
```

Creates a button with an icon.

**Parameters:** icon

- the Icon image to display on the button

---

#### JButton

public JButton​(

Icon

icon)

Creates a button with an icon.

JButton

```java
@ConstructorProperties
("text")
public JButton​(
String
text)
```

Creates a button with text.

**Parameters:** text

- the text of the button

---

#### JButton

@ConstructorProperties

("text")
public JButton​(

String

text)

Creates a button with text.

JButton

```java
public JButton​(
Action
a)
```

Creates a button where properties are taken from the

Action

supplied.

**Parameters:** a

- the

Action

used to specify the new button
**Since:** 1.3

---

#### JButton

public JButton​(

Action

a)

Creates a button where properties are taken from the

Action

supplied.

JButton

```java
public JButton​(
String
text,

Icon
icon)
```

Creates a button with initial text and an icon.

**Parameters:** text

- the text of the button
**Parameters:** icon

- the Icon image to display on the button

---

#### JButton

public JButton​(

String

text,

Icon

icon)

Creates a button with initial text and an icon.

Method Detail

- updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look and
feel.

**Overrides:** updateUI

in class

AbstractButton
**See Also:** JComponent.updateUI()

- getUIClassID

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="A string that specifies the name of the L&F class.")
public
String
getUIClassID()
```

Returns a string that specifies the name of the L&F class
that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "ButtonUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- isDefaultButton

```java
@BeanProperty
(
bound
=false,

description
="Whether or not this button is the default button")
public boolean isDefaultButton()
```

Gets the value of the

defaultButton

property,
which if

true

means that this button is the current
default button for its

JRootPane

.
Most look and feels render the default button
differently, and may potentially provide bindings
to access the default button.

**Returns:** the value of the

defaultButton

property
**See Also:** JRootPane.setDefaultButton(javax.swing.JButton)

,

isDefaultCapable()

- isDefaultCapable

```java
public boolean isDefaultCapable()
```

Gets the value of the

defaultCapable

property.

**Returns:** the value of the

defaultCapable

property
**See Also:** setDefaultCapable(boolean)

,

isDefaultButton()

,

JRootPane.setDefaultButton(javax.swing.JButton)

- setDefaultCapable

```java
@BeanProperty
(
visualUpdate
=true,

description
="Whether or not this button can be the default button")
public void setDefaultCapable​(boolean defaultCapable)
```

Sets the

defaultCapable

property,
which determines whether this button can be
made the default button for its root pane.
The default value of the

defaultCapable

property is

true

unless otherwise
specified by the look and feel.

**Parameters:** defaultCapable

-

true

if this button will be
capable of being the default button on the

RootPane

; otherwise

false
**See Also:** isDefaultCapable()

- removeNotify

```java
public void removeNotify()
```

Overrides

JComponent.removeNotify

to check if
this button is currently set as the default button on the

RootPane

, and if so, sets the

RootPane

's
default button to

null

to ensure the

RootPane

doesn't hold onto an invalid button reference.

**Overrides:** removeNotify

in class

AbstractButton
**See Also:** JComponent.registerKeyboardAction(java.awt.event.ActionListener, java.lang.String, javax.swing.KeyStroke, int)

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JButton

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

AbstractButton
**Returns:** a string representation of this

JButton

- getAccessibleContext

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The AccessibleContext associated with this Button.")
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated with this

JButton

. For

JButton

s,
the

AccessibleContext

takes the form of an

AccessibleJButton

.
A new

AccessibleJButton

instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an

AccessibleJButton

that serves as the

AccessibleContext

of this

JButton

---

#### Method Detail

updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look and
feel.

**Overrides:** updateUI

in class

AbstractButton
**See Also:** JComponent.updateUI()

---

#### updateUI

public void updateUI()

Resets the UI property to a value from the current look and
feel.

getUIClassID

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="A string that specifies the name of the L&F class.")
public
String
getUIClassID()
```

Returns a string that specifies the name of the L&F class
that renders this component.

**Overrides:** getUIClassID

in class

JComponent
**Returns:** the string "ButtonUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### getUIClassID

@BeanProperty

(

bound

=false,

expert

=true,

description

="A string that specifies the name of the L&F class.")
public

String

getUIClassID()

Returns a string that specifies the name of the L&F class
that renders this component.

isDefaultButton

```java
@BeanProperty
(
bound
=false,

description
="Whether or not this button is the default button")
public boolean isDefaultButton()
```

Gets the value of the

defaultButton

property,
which if

true

means that this button is the current
default button for its

JRootPane

.
Most look and feels render the default button
differently, and may potentially provide bindings
to access the default button.

**Returns:** the value of the

defaultButton

property
**See Also:** JRootPane.setDefaultButton(javax.swing.JButton)

,

isDefaultCapable()

---

#### isDefaultButton

@BeanProperty

(

bound

=false,

description

="Whether or not this button is the default button")
public boolean isDefaultButton()

Gets the value of the

defaultButton

property,
which if

true

means that this button is the current
default button for its

JRootPane

.
Most look and feels render the default button
differently, and may potentially provide bindings
to access the default button.

isDefaultCapable

```java
public boolean isDefaultCapable()
```

Gets the value of the

defaultCapable

property.

**Returns:** the value of the

defaultCapable

property
**See Also:** setDefaultCapable(boolean)

,

isDefaultButton()

,

JRootPane.setDefaultButton(javax.swing.JButton)

---

#### isDefaultCapable

public boolean isDefaultCapable()

Gets the value of the

defaultCapable

property.

setDefaultCapable

```java
@BeanProperty
(
visualUpdate
=true,

description
="Whether or not this button can be the default button")
public void setDefaultCapable​(boolean defaultCapable)
```

Sets the

defaultCapable

property,
which determines whether this button can be
made the default button for its root pane.
The default value of the

defaultCapable

property is

true

unless otherwise
specified by the look and feel.

**Parameters:** defaultCapable

-

true

if this button will be
capable of being the default button on the

RootPane

; otherwise

false
**See Also:** isDefaultCapable()

---

#### setDefaultCapable

@BeanProperty

(

visualUpdate

=true,

description

="Whether or not this button can be the default button")
public void setDefaultCapable​(boolean defaultCapable)

Sets the

defaultCapable

property,
which determines whether this button can be
made the default button for its root pane.
The default value of the

defaultCapable

property is

true

unless otherwise
specified by the look and feel.

removeNotify

```java
public void removeNotify()
```

Overrides

JComponent.removeNotify

to check if
this button is currently set as the default button on the

RootPane

, and if so, sets the

RootPane

's
default button to

null

to ensure the

RootPane

doesn't hold onto an invalid button reference.

**Overrides:** removeNotify

in class

AbstractButton
**See Also:** JComponent.registerKeyboardAction(java.awt.event.ActionListener, java.lang.String, javax.swing.KeyStroke, int)

---

#### removeNotify

public void removeNotify()

Overrides

JComponent.removeNotify

to check if
this button is currently set as the default button on the

RootPane

, and if so, sets the

RootPane

's
default button to

null

to ensure the

RootPane

doesn't hold onto an invalid button reference.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JButton

.
This method is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

AbstractButton
**Returns:** a string representation of this

JButton

---

#### paramString

protected

String

paramString()

Returns a string representation of this

JButton

.
This method is intended to be used only for debugging purposes, and the
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
=false,

expert
=true,

description
="The AccessibleContext associated with this Button.")
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated with this

JButton

. For

JButton

s,
the

AccessibleContext

takes the form of an

AccessibleJButton

.
A new

AccessibleJButton

instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an

AccessibleJButton

that serves as the

AccessibleContext

of this

JButton

---

#### getAccessibleContext

@BeanProperty

(

bound

=false,

expert

=true,

description

="The AccessibleContext associated with this Button.")
public

AccessibleContext

getAccessibleContext()

Gets the

AccessibleContext

associated with this

JButton

. For

JButton

s,
the

AccessibleContext

takes the form of an

AccessibleJButton

.
A new

AccessibleJButton

instance is created if necessary.

---

