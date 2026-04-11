# Class JRadioButton

**Source:** `java.desktop\javax\swing\JRadioButton.html`

### Class Description

```java
@JavaBean
(
description
="A component which can display it\'s state as selected or deselected.")
public class
JRadioButton

extends
JToggleButton

implements
Accessible
```

An implementation of a radio button -- an item that can be selected or
deselected, and which displays its state to the user.
Used with a

ButtonGroup

object to create a group of buttons
in which only one button at a time can be selected. (Create a ButtonGroup
object and use its

add

method to include the JRadioButton objects
in the group.)

Note:

The ButtonGroup object is a logical grouping -- not a physical grouping.
To create a button panel, you should still create a

JPanel

or similar
container-object and add a

Border

to it to set it off from surrounding
components.

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

#### public JRadioButton()

Creates an initially unselected radio button
with no set text.

---

#### public JRadioButton​(
Icon
icon)

Creates an initially unselected radio button
with the specified image but no text.

**Parameters:**
- icon

- the image that the button should display

---

#### public JRadioButton​(
Action
a)

Creates a radiobutton where properties are taken from the
Action supplied.

**Parameters:**
- a

- an

Action

**Since:**
- 1.3

---

#### public JRadioButton​(
Icon
icon,
boolean selected)

Creates a radio button with the specified image
and selection state, but no text.

**Parameters:**
- icon

- the image that the button should display
- selected

- if true, the button is initially selected;
otherwise, the button is initially unselected

---

#### public JRadioButton​(
String
text)

Creates an unselected radio button with the specified text.

**Parameters:**
- text

- the string displayed on the radio button

---

#### public JRadioButton​(
String
text,
boolean selected)

Creates a radio button with the specified text
and selection state.

**Parameters:**
- text

- the string displayed on the radio button
- selected

- if true, the button is initially selected;
otherwise, the button is initially unselected

---

#### public JRadioButton​(
String
text,

Icon
icon)

Creates a radio button that has the specified text and image,
and that is initially unselected.

**Parameters:**
- text

- the string displayed on the radio button
- icon

- the image that the button should display

---

#### public JRadioButton​(
String
text,

Icon
icon,
boolean selected)

Creates a radio button that has the specified text, image,
and selection state.

**Parameters:**
- text

- the string displayed on the radio button
- icon

- the image that the button should display
- selected

- if

true

, the button is initially selected
otherwise, the button is initially unselected

---

### Method Details

#### public void updateUI()

Resets the UI property to a value from the current look and feel.

**Overrides:**
- updateUI

in class

JToggleButton

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

Returns the name of the L&F class
that renders this component.

**Overrides:**
- getUIClassID

in class

JToggleButton

**Returns:**
- String "RadioButtonUI"

**See Also:**
- JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### protected
String
paramString()

Returns a string representation of this JRadioButton. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:**
- paramString

in class

JToggleButton

**Returns:**
- a string representation of this JRadioButton.

---

#### @BeanProperty
(
bound
=false,

expert
=true,

description
="The AccessibleContext associated with this Button")
public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this JRadioButton.
For JRadioButtons, the AccessibleContext takes the form of an
AccessibleJRadioButton.
A new AccessibleJRadioButton instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

JToggleButton

**Returns:**
- an AccessibleJRadioButton that serves as the
AccessibleContext of this JRadioButton

---

### Additional Sections

#### Class JRadioButton

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.AbstractButton
- - javax.swing.JToggleButton
- - javax.swing.JRadioButton

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.AbstractButton
- - javax.swing.JToggleButton
- - javax.swing.JRadioButton

java.awt.Container

- javax.swing.JComponent
- - javax.swing.AbstractButton
- - javax.swing.JToggleButton
- - javax.swing.JRadioButton

javax.swing.JComponent

- javax.swing.AbstractButton
- - javax.swing.JToggleButton
- - javax.swing.JRadioButton

javax.swing.AbstractButton

- javax.swing.JToggleButton
- - javax.swing.JRadioButton

javax.swing.JToggleButton

- javax.swing.JRadioButton

javax.swing.JRadioButton

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
@JavaBean
(
description
="A component which can display it\'s state as selected or deselected.")
public class
JRadioButton

extends
JToggleButton

implements
Accessible
```

An implementation of a radio button -- an item that can be selected or
deselected, and which displays its state to the user.
Used with a

ButtonGroup

object to create a group of buttons
in which only one button at a time can be selected. (Create a ButtonGroup
object and use its

add

method to include the JRadioButton objects
in the group.)

Note:

The ButtonGroup object is a logical grouping -- not a physical grouping.
To create a button panel, you should still create a

JPanel

or similar
container-object and add a

Border

to it to set it off from surrounding
components.

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
**See Also:** ButtonGroup

,

JCheckBox

,

Serialized Form

@JavaBean

(

description

="A component which can display it\'s state as selected or deselected.")
public class

JRadioButton

extends

JToggleButton

implements

Accessible

An implementation of a radio button -- an item that can be selected or
deselected, and which displays its state to the user.
Used with a

ButtonGroup

object to create a group of buttons
in which only one button at a time can be selected. (Create a ButtonGroup
object and use its

add

method to include the JRadioButton objects
in the group.)

Note:

The ButtonGroup object is a logical grouping -- not a physical grouping.
To create a button panel, you should still create a

JPanel

or similar
container-object and add a

Border

to it to set it off from surrounding
components.

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

How to Use Buttons, Check Boxes, and Radio Buttons

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

JRadioButton.AccessibleJRadioButton

This class implements accessibility support for the

JRadioButton

class.

- Nested classes/interfaces declared in class javax.swing.

JToggleButton

JToggleButton.AccessibleJToggleButton

,

JToggleButton.ToggleButtonModel

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

JRadioButton

()

Creates an initially unselected radio button
with no set text.

JRadioButton

​(

String

text)

Creates an unselected radio button with the specified text.

JRadioButton

​(

String

text,
boolean selected)

Creates a radio button with the specified text
and selection state.

JRadioButton

​(

String

text,

Icon

icon)

Creates a radio button that has the specified text and image,
and that is initially unselected.

JRadioButton

​(

String

text,

Icon

icon,
boolean selected)

Creates a radio button that has the specified text, image,
and selection state.

JRadioButton

​(

Action

a)

Creates a radiobutton where properties are taken from the
Action supplied.

JRadioButton

​(

Icon

icon)

Creates an initially unselected radio button
with the specified image but no text.

JRadioButton

​(

Icon

icon,
boolean selected)

Creates a radio button with the specified image
and selection state, but no text.

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

Gets the AccessibleContext associated with this JRadioButton.

String

getUIClassID

()

Returns the name of the L&F class
that renders this component.

protected

String

paramString

()

Returns a string representation of this JRadioButton.

void

updateUI

()

Resets the UI property to a value from the current look and feel.

- Methods declared in class javax.swing.

JToggleButton

requestFocus

,

requestFocusInWindow

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

removeNotify

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

JRadioButton.AccessibleJRadioButton

This class implements accessibility support for the

JRadioButton

class.

- Nested classes/interfaces declared in class javax.swing.

JToggleButton

JToggleButton.AccessibleJToggleButton

,

JToggleButton.ToggleButtonModel

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

JRadioButton

class.

Nested classes/interfaces declared in class javax.swing.

JToggleButton

JToggleButton.AccessibleJToggleButton

,

JToggleButton.ToggleButtonModel

---

#### Nested classes/interfaces declared in class javax.swing. JToggleButton

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

JRadioButton

()

Creates an initially unselected radio button
with no set text.

JRadioButton

​(

String

text)

Creates an unselected radio button with the specified text.

JRadioButton

​(

String

text,
boolean selected)

Creates a radio button with the specified text
and selection state.

JRadioButton

​(

String

text,

Icon

icon)

Creates a radio button that has the specified text and image,
and that is initially unselected.

JRadioButton

​(

String

text,

Icon

icon,
boolean selected)

Creates a radio button that has the specified text, image,
and selection state.

JRadioButton

​(

Action

a)

Creates a radiobutton where properties are taken from the
Action supplied.

JRadioButton

​(

Icon

icon)

Creates an initially unselected radio button
with the specified image but no text.

JRadioButton

​(

Icon

icon,
boolean selected)

Creates a radio button with the specified image
and selection state, but no text.

---

#### Constructor Summary

Creates an initially unselected radio button
with no set text.

Creates an unselected radio button with the specified text.

Creates a radio button with the specified text
and selection state.

Creates a radio button that has the specified text and image,
and that is initially unselected.

Creates a radio button that has the specified text, image,
and selection state.

Creates a radiobutton where properties are taken from the
Action supplied.

Creates an initially unselected radio button
with the specified image but no text.

Creates a radio button with the specified image
and selection state, but no text.

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

Gets the AccessibleContext associated with this JRadioButton.

String

getUIClassID

()

Returns the name of the L&F class
that renders this component.

protected

String

paramString

()

Returns a string representation of this JRadioButton.

void

updateUI

()

Resets the UI property to a value from the current look and feel.

- Methods declared in class javax.swing.

JToggleButton

requestFocus

,

requestFocusInWindow

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

removeNotify

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

Gets the AccessibleContext associated with this JRadioButton.

Returns the name of the L&F class
that renders this component.

Returns a string representation of this JRadioButton.

Resets the UI property to a value from the current look and feel.

Methods declared in class javax.swing.

JToggleButton

requestFocus

,

requestFocusInWindow

---

#### Methods declared in class javax.swing. JToggleButton

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

removeNotify

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

- JRadioButton

```java
public JRadioButton()
```

Creates an initially unselected radio button
with no set text.

- JRadioButton

```java
public JRadioButton​(
Icon
icon)
```

Creates an initially unselected radio button
with the specified image but no text.

**Parameters:** icon

- the image that the button should display

- JRadioButton

```java
public JRadioButton​(
Action
a)
```

Creates a radiobutton where properties are taken from the
Action supplied.

**Parameters:** a

- an

Action
**Since:** 1.3

- JRadioButton

```java
public JRadioButton​(
Icon
icon,
boolean selected)
```

Creates a radio button with the specified image
and selection state, but no text.

**Parameters:** icon

- the image that the button should display
**Parameters:** selected

- if true, the button is initially selected;
otherwise, the button is initially unselected

- JRadioButton

```java
public JRadioButton​(
String
text)
```

Creates an unselected radio button with the specified text.

**Parameters:** text

- the string displayed on the radio button

- JRadioButton

```java
public JRadioButton​(
String
text,
boolean selected)
```

Creates a radio button with the specified text
and selection state.

**Parameters:** text

- the string displayed on the radio button
**Parameters:** selected

- if true, the button is initially selected;
otherwise, the button is initially unselected

- JRadioButton

```java
public JRadioButton​(
String
text,

Icon
icon)
```

Creates a radio button that has the specified text and image,
and that is initially unselected.

**Parameters:** text

- the string displayed on the radio button
**Parameters:** icon

- the image that the button should display

- JRadioButton

```java
public JRadioButton​(
String
text,

Icon
icon,
boolean selected)
```

Creates a radio button that has the specified text, image,
and selection state.

**Parameters:** text

- the string displayed on the radio button
**Parameters:** icon

- the image that the button should display
**Parameters:** selected

- if

true

, the button is initially selected
otherwise, the button is initially unselected

============ METHOD DETAIL ==========

- Method Detail

- updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look and feel.

**Overrides:** updateUI

in class

JToggleButton
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

Returns the name of the L&F class
that renders this component.

**Overrides:** getUIClassID

in class

JToggleButton
**Returns:** String "RadioButtonUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this JRadioButton. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JToggleButton
**Returns:** a string representation of this JRadioButton.

- getAccessibleContext

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The AccessibleContext associated with this Button")
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JRadioButton.
For JRadioButtons, the AccessibleContext takes the form of an
AccessibleJRadioButton.
A new AccessibleJRadioButton instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

JToggleButton
**Returns:** an AccessibleJRadioButton that serves as the
AccessibleContext of this JRadioButton

Constructor Detail

- JRadioButton

```java
public JRadioButton()
```

Creates an initially unselected radio button
with no set text.

- JRadioButton

```java
public JRadioButton​(
Icon
icon)
```

Creates an initially unselected radio button
with the specified image but no text.

**Parameters:** icon

- the image that the button should display

- JRadioButton

```java
public JRadioButton​(
Action
a)
```

Creates a radiobutton where properties are taken from the
Action supplied.

**Parameters:** a

- an

Action
**Since:** 1.3

- JRadioButton

```java
public JRadioButton​(
Icon
icon,
boolean selected)
```

Creates a radio button with the specified image
and selection state, but no text.

**Parameters:** icon

- the image that the button should display
**Parameters:** selected

- if true, the button is initially selected;
otherwise, the button is initially unselected

- JRadioButton

```java
public JRadioButton​(
String
text)
```

Creates an unselected radio button with the specified text.

**Parameters:** text

- the string displayed on the radio button

- JRadioButton

```java
public JRadioButton​(
String
text,
boolean selected)
```

Creates a radio button with the specified text
and selection state.

**Parameters:** text

- the string displayed on the radio button
**Parameters:** selected

- if true, the button is initially selected;
otherwise, the button is initially unselected

- JRadioButton

```java
public JRadioButton​(
String
text,

Icon
icon)
```

Creates a radio button that has the specified text and image,
and that is initially unselected.

**Parameters:** text

- the string displayed on the radio button
**Parameters:** icon

- the image that the button should display

- JRadioButton

```java
public JRadioButton​(
String
text,

Icon
icon,
boolean selected)
```

Creates a radio button that has the specified text, image,
and selection state.

**Parameters:** text

- the string displayed on the radio button
**Parameters:** icon

- the image that the button should display
**Parameters:** selected

- if

true

, the button is initially selected
otherwise, the button is initially unselected

---

#### Constructor Detail

JRadioButton

```java
public JRadioButton()
```

Creates an initially unselected radio button
with no set text.

---

#### JRadioButton

public JRadioButton()

Creates an initially unselected radio button
with no set text.

JRadioButton

```java
public JRadioButton​(
Icon
icon)
```

Creates an initially unselected radio button
with the specified image but no text.

**Parameters:** icon

- the image that the button should display

---

#### JRadioButton

public JRadioButton​(

Icon

icon)

Creates an initially unselected radio button
with the specified image but no text.

JRadioButton

```java
public JRadioButton​(
Action
a)
```

Creates a radiobutton where properties are taken from the
Action supplied.

**Parameters:** a

- an

Action
**Since:** 1.3

---

#### JRadioButton

public JRadioButton​(

Action

a)

Creates a radiobutton where properties are taken from the
Action supplied.

JRadioButton

```java
public JRadioButton​(
Icon
icon,
boolean selected)
```

Creates a radio button with the specified image
and selection state, but no text.

**Parameters:** icon

- the image that the button should display
**Parameters:** selected

- if true, the button is initially selected;
otherwise, the button is initially unselected

---

#### JRadioButton

public JRadioButton​(

Icon

icon,
boolean selected)

Creates a radio button with the specified image
and selection state, but no text.

JRadioButton

```java
public JRadioButton​(
String
text)
```

Creates an unselected radio button with the specified text.

**Parameters:** text

- the string displayed on the radio button

---

#### JRadioButton

public JRadioButton​(

String

text)

Creates an unselected radio button with the specified text.

JRadioButton

```java
public JRadioButton​(
String
text,
boolean selected)
```

Creates a radio button with the specified text
and selection state.

**Parameters:** text

- the string displayed on the radio button
**Parameters:** selected

- if true, the button is initially selected;
otherwise, the button is initially unselected

---

#### JRadioButton

public JRadioButton​(

String

text,
boolean selected)

Creates a radio button with the specified text
and selection state.

JRadioButton

```java
public JRadioButton​(
String
text,

Icon
icon)
```

Creates a radio button that has the specified text and image,
and that is initially unselected.

**Parameters:** text

- the string displayed on the radio button
**Parameters:** icon

- the image that the button should display

---

#### JRadioButton

public JRadioButton​(

String

text,

Icon

icon)

Creates a radio button that has the specified text and image,
and that is initially unselected.

JRadioButton

```java
public JRadioButton​(
String
text,

Icon
icon,
boolean selected)
```

Creates a radio button that has the specified text, image,
and selection state.

**Parameters:** text

- the string displayed on the radio button
**Parameters:** icon

- the image that the button should display
**Parameters:** selected

- if

true

, the button is initially selected
otherwise, the button is initially unselected

---

#### JRadioButton

public JRadioButton​(

String

text,

Icon

icon,
boolean selected)

Creates a radio button that has the specified text, image,
and selection state.

Method Detail

- updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look and feel.

**Overrides:** updateUI

in class

JToggleButton
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

Returns the name of the L&F class
that renders this component.

**Overrides:** getUIClassID

in class

JToggleButton
**Returns:** String "RadioButtonUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this JRadioButton. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JToggleButton
**Returns:** a string representation of this JRadioButton.

- getAccessibleContext

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The AccessibleContext associated with this Button")
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JRadioButton.
For JRadioButtons, the AccessibleContext takes the form of an
AccessibleJRadioButton.
A new AccessibleJRadioButton instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

JToggleButton
**Returns:** an AccessibleJRadioButton that serves as the
AccessibleContext of this JRadioButton

---

#### Method Detail

updateUI

```java
public void updateUI()
```

Resets the UI property to a value from the current look and feel.

**Overrides:** updateUI

in class

JToggleButton
**See Also:** JComponent.updateUI()

---

#### updateUI

public void updateUI()

Resets the UI property to a value from the current look and feel.

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

Returns the name of the L&F class
that renders this component.

**Overrides:** getUIClassID

in class

JToggleButton
**Returns:** String "RadioButtonUI"
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

Returns the name of the L&F class
that renders this component.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this JRadioButton. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JToggleButton
**Returns:** a string representation of this JRadioButton.

---

#### paramString

protected

String

paramString()

Returns a string representation of this JRadioButton. This method
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
=false,

expert
=true,

description
="The AccessibleContext associated with this Button")
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this JRadioButton.
For JRadioButtons, the AccessibleContext takes the form of an
AccessibleJRadioButton.
A new AccessibleJRadioButton instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

JToggleButton
**Returns:** an AccessibleJRadioButton that serves as the
AccessibleContext of this JRadioButton

---

#### getAccessibleContext

@BeanProperty

(

bound

=false,

expert

=true,

description

="The AccessibleContext associated with this Button")
public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this JRadioButton.
For JRadioButtons, the AccessibleContext takes the form of an
AccessibleJRadioButton.
A new AccessibleJRadioButton instance is created if necessary.

---

