# Class JRadioButtonMenuItem

**Source:** `java.desktop\javax\swing\JRadioButtonMenuItem.html`

### Class Description

```java
@JavaBean
(
description
="A component within a group of menu items which can be selected.")
public class
JRadioButtonMenuItem

extends
JMenuItem

implements
Accessible
```

An implementation of a radio button menu item.
A

JRadioButtonMenuItem

is
a menu item that is part of a group of menu items in which only one
item in the group can be selected. The selected item displays its
selected state. Selecting it causes any other selected item to
switch to the unselected state.
To control the selected state of a group of radio button menu items,
use a

ButtonGroup

object.

Menu items can be configured, and to some degree controlled, by

Action

s. Using an

Action

with a menu item has many benefits beyond directly
configuring a menu item. Refer to

Swing Components Supporting

Action

for more
details, and you can find more information in

How
to Use Actions

, a section in

The Java Tutorial

.

Some menus can have several button groups with radio button menu items. In
this case it is useful that clicking on one radio button menu item does not
close the menu. Such behavior can be controlled either by client

JComponent.putClientProperty(java.lang.Object, java.lang.Object)

or the Look and Feel

UIManager.put(java.lang.Object, java.lang.Object)

property named

"RadioButtonMenuItem.doNotCloseOnMouseClick"

. The default value is

false

. Setting the property to

true

prevents the menu from
closing when it is clicked by the mouse. If the client property is set its
value is always used; otherwise the L&F property is queried.
Note: some

L&F

s may ignore this property. All built-in

L&F

s
inherit this behaviour.

For further documentation and examples see

How to Use Menus

,
a section in

The Java Tutorial.

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

MenuElement

,

SwingConstants

---

### Field Details

*No entries found.*

### Constructor Details

#### public JRadioButtonMenuItem()

Creates a

JRadioButtonMenuItem

with no set text or icon.

---

#### public JRadioButtonMenuItem​(
Icon
icon)

Creates a

JRadioButtonMenuItem

with an icon.

**Parameters:**
- icon

- the

Icon

to display on the

JRadioButtonMenuItem

---

#### public JRadioButtonMenuItem​(
String
text)

Creates a

JRadioButtonMenuItem

with text.

**Parameters:**
- text

- the text of the

JRadioButtonMenuItem

---

#### public JRadioButtonMenuItem​(
Action
a)

Creates a radio button menu item whose properties are taken from the

Action

supplied.

**Parameters:**
- a

- the

Action

on which to base the radio
button menu item

**Since:**
- 1.3

---

#### public JRadioButtonMenuItem​(
String
text,

Icon
icon)

Creates a radio button menu item with the specified text
and

Icon

.

**Parameters:**
- text

- the text of the

JRadioButtonMenuItem
- icon

- the icon to display on the

JRadioButtonMenuItem

---

#### public JRadioButtonMenuItem​(
String
text,
boolean selected)

Creates a radio button menu item with the specified text
and selection state.

**Parameters:**
- text

- the text of the

CheckBoxMenuItem
- selected

- the selected state of the

CheckBoxMenuItem

---

#### public JRadioButtonMenuItem​(
Icon
icon,
boolean selected)

Creates a radio button menu item with the specified image
and selection state, but no text.

**Parameters:**
- icon

- the image that the button should display
- selected

- if true, the button is initially selected;
otherwise, the button is initially unselected

---

#### public JRadioButtonMenuItem​(
String
text,

Icon
icon,
boolean selected)

Creates a radio button menu item that has the specified
text, image, and selection state. All other constructors
defer to this one.

**Parameters:**
- text

- the string displayed on the radio button
- icon

- the image that the button should display
- selected

- if

true

, the button is initially selected,
otherwise, the button is initially unselected

---

### Method Details

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

JMenuItem

**Returns:**
- the string "RadioButtonMenuItemUI"

**See Also:**
- JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### protected
String
paramString()

Returns a string representation of this

JRadioButtonMenuItem

. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:**
- paramString

in class

JMenuItem

**Returns:**
- a string representation of this

JRadioButtonMenuItem

---

#### @BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this JRadioButtonMenuItem.
For JRadioButtonMenuItems, the AccessibleContext takes the form of an
AccessibleJRadioButtonMenuItem.
A new AccessibleJRadioButtonMenuItem instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

JMenuItem

**Returns:**
- an AccessibleJRadioButtonMenuItem that serves as the
AccessibleContext of this JRadioButtonMenuItem

---

### Additional Sections

#### Class JRadioButtonMenuItem

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.AbstractButton
- - javax.swing.JMenuItem
- - javax.swing.JRadioButtonMenuItem

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.AbstractButton
- - javax.swing.JMenuItem
- - javax.swing.JRadioButtonMenuItem

java.awt.Container

- javax.swing.JComponent
- - javax.swing.AbstractButton
- - javax.swing.JMenuItem
- - javax.swing.JRadioButtonMenuItem

javax.swing.JComponent

- javax.swing.AbstractButton
- - javax.swing.JMenuItem
- - javax.swing.JRadioButtonMenuItem

javax.swing.AbstractButton

- javax.swing.JMenuItem
- - javax.swing.JRadioButtonMenuItem

javax.swing.JMenuItem

- javax.swing.JRadioButtonMenuItem

javax.swing.JRadioButtonMenuItem

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

MenuElement

,

SwingConstants

```java
@JavaBean
(
description
="A component within a group of menu items which can be selected.")
public class
JRadioButtonMenuItem

extends
JMenuItem

implements
Accessible
```

An implementation of a radio button menu item.
A

JRadioButtonMenuItem

is
a menu item that is part of a group of menu items in which only one
item in the group can be selected. The selected item displays its
selected state. Selecting it causes any other selected item to
switch to the unselected state.
To control the selected state of a group of radio button menu items,
use a

ButtonGroup

object.

Menu items can be configured, and to some degree controlled, by

Action

s. Using an

Action

with a menu item has many benefits beyond directly
configuring a menu item. Refer to

Swing Components Supporting

Action

for more
details, and you can find more information in

How
to Use Actions

, a section in

The Java Tutorial

.

Some menus can have several button groups with radio button menu items. In
this case it is useful that clicking on one radio button menu item does not
close the menu. Such behavior can be controlled either by client

JComponent.putClientProperty(java.lang.Object, java.lang.Object)

or the Look and Feel

UIManager.put(java.lang.Object, java.lang.Object)

property named

"RadioButtonMenuItem.doNotCloseOnMouseClick"

. The default value is

false

. Setting the property to

true

prevents the menu from
closing when it is clicked by the mouse. If the client property is set its
value is always used; otherwise the L&F property is queried.
Note: some

L&F

s may ignore this property. All built-in

L&F

s
inherit this behaviour.

For further documentation and examples see

How to Use Menus

,
a section in

The Java Tutorial.

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

Serialized Form

@JavaBean

(

description

="A component within a group of menu items which can be selected.")
public class

JRadioButtonMenuItem

extends

JMenuItem

implements

Accessible

An implementation of a radio button menu item.
A

JRadioButtonMenuItem

is
a menu item that is part of a group of menu items in which only one
item in the group can be selected. The selected item displays its
selected state. Selecting it causes any other selected item to
switch to the unselected state.
To control the selected state of a group of radio button menu items,
use a

ButtonGroup

object.

Menu items can be configured, and to some degree controlled, by

Action

s. Using an

Action

with a menu item has many benefits beyond directly
configuring a menu item. Refer to

Swing Components Supporting

Action

for more
details, and you can find more information in

How
to Use Actions

, a section in

The Java Tutorial

.

Some menus can have several button groups with radio button menu items. In
this case it is useful that clicking on one radio button menu item does not
close the menu. Such behavior can be controlled either by client

JComponent.putClientProperty(java.lang.Object, java.lang.Object)

or the Look and Feel

UIManager.put(java.lang.Object, java.lang.Object)

property named

"RadioButtonMenuItem.doNotCloseOnMouseClick"

. The default value is

false

. Setting the property to

true

prevents the menu from
closing when it is clicked by the mouse. If the client property is set its
value is always used; otherwise the L&F property is queried.
Note: some

L&F

s may ignore this property. All built-in

L&F

s
inherit this behaviour.

For further documentation and examples see

How to Use Menus

,
a section in

The Java Tutorial.

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

Menu items can be configured, and to some degree controlled, by

Action

s. Using an

Action

with a menu item has many benefits beyond directly
configuring a menu item. Refer to

Swing Components Supporting

Action

for more
details, and you can find more information in

How
to Use Actions

, a section in

The Java Tutorial

.

Some menus can have several button groups with radio button menu items. In
this case it is useful that clicking on one radio button menu item does not
close the menu. Such behavior can be controlled either by client

JComponent.putClientProperty(java.lang.Object, java.lang.Object)

or the Look and Feel

UIManager.put(java.lang.Object, java.lang.Object)

property named

"RadioButtonMenuItem.doNotCloseOnMouseClick"

. The default value is

false

. Setting the property to

true

prevents the menu from
closing when it is clicked by the mouse. If the client property is set its
value is always used; otherwise the L&F property is queried.
Note: some

L&F

s may ignore this property. All built-in

L&F

s
inherit this behaviour.

For further documentation and examples see

How to Use Menus

,
a section in

The Java Tutorial.

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

Some menus can have several button groups with radio button menu items. In
this case it is useful that clicking on one radio button menu item does not
close the menu. Such behavior can be controlled either by client

JComponent.putClientProperty(java.lang.Object, java.lang.Object)

or the Look and Feel

UIManager.put(java.lang.Object, java.lang.Object)

property named

"RadioButtonMenuItem.doNotCloseOnMouseClick"

. The default value is

false

. Setting the property to

true

prevents the menu from
closing when it is clicked by the mouse. If the client property is set its
value is always used; otherwise the L&F property is queried.
Note: some

L&F

s may ignore this property. All built-in

L&F

s
inherit this behaviour.

For further documentation and examples see

How to Use Menus

,
a section in

The Java Tutorial.

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

For further documentation and examples see

How to Use Menus

,
a section in

The Java Tutorial.

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

JRadioButtonMenuItem.AccessibleJRadioButtonMenuItem

This class implements accessibility support for the

JRadioButtonMenuItem

class.

- Nested classes/interfaces declared in class javax.swing.

JMenuItem

JMenuItem.AccessibleJMenuItem

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

JRadioButtonMenuItem

()

Creates a

JRadioButtonMenuItem

with no set text or icon.

JRadioButtonMenuItem

​(

String

text)

Creates a

JRadioButtonMenuItem

with text.

JRadioButtonMenuItem

​(

String

text,
boolean selected)

Creates a radio button menu item with the specified text
and selection state.

JRadioButtonMenuItem

​(

String

text,

Icon

icon)

Creates a radio button menu item with the specified text
and

Icon

.

JRadioButtonMenuItem

​(

String

text,

Icon

icon,
boolean selected)

Creates a radio button menu item that has the specified
text, image, and selection state.

JRadioButtonMenuItem

​(

Action

a)

Creates a radio button menu item whose properties are taken from the

Action

supplied.

JRadioButtonMenuItem

​(

Icon

icon)

Creates a

JRadioButtonMenuItem

with an icon.

JRadioButtonMenuItem

​(

Icon

icon,
boolean selected)

Creates a radio button menu item with the specified image
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

Gets the AccessibleContext associated with this JRadioButtonMenuItem.

String

getUIClassID

()

Returns the name of the L&F class that renders this component.

protected

String

paramString

()

Returns a string representation of this

JRadioButtonMenuItem

.

- Methods declared in class javax.swing.

JMenuItem

actionPropertyChanged

,

addMenuDragMouseListener

,

addMenuKeyListener

,

configurePropertiesFromAction

,

fireMenuDragMouseDragged

,

fireMenuDragMouseEntered

,

fireMenuDragMouseExited

,

fireMenuDragMouseReleased

,

fireMenuKeyPressed

,

fireMenuKeyReleased

,

fireMenuKeyTyped

,

getAccelerator

,

getComponent

,

getMenuDragMouseListeners

,

getMenuKeyListeners

,

getSubElements

,

init

,

isArmed

,

menuSelectionChanged

,

processKeyEvent

,

processMenuDragMouseEvent

,

processMenuKeyEvent

,

processMouseEvent

,

removeMenuDragMouseListener

,

removeMenuKeyListener

,

setAccelerator

,

setArmed

,

setEnabled

,

setUI

,

updateUI

- Methods declared in class javax.swing.

AbstractButton

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

JRadioButtonMenuItem.AccessibleJRadioButtonMenuItem

This class implements accessibility support for the

JRadioButtonMenuItem

class.

- Nested classes/interfaces declared in class javax.swing.

JMenuItem

JMenuItem.AccessibleJMenuItem

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

JRadioButtonMenuItem

class.

Nested classes/interfaces declared in class javax.swing.

JMenuItem

JMenuItem.AccessibleJMenuItem

---

#### Nested classes/interfaces declared in class javax.swing. JMenuItem

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

JRadioButtonMenuItem

()

Creates a

JRadioButtonMenuItem

with no set text or icon.

JRadioButtonMenuItem

​(

String

text)

Creates a

JRadioButtonMenuItem

with text.

JRadioButtonMenuItem

​(

String

text,
boolean selected)

Creates a radio button menu item with the specified text
and selection state.

JRadioButtonMenuItem

​(

String

text,

Icon

icon)

Creates a radio button menu item with the specified text
and

Icon

.

JRadioButtonMenuItem

​(

String

text,

Icon

icon,
boolean selected)

Creates a radio button menu item that has the specified
text, image, and selection state.

JRadioButtonMenuItem

​(

Action

a)

Creates a radio button menu item whose properties are taken from the

Action

supplied.

JRadioButtonMenuItem

​(

Icon

icon)

Creates a

JRadioButtonMenuItem

with an icon.

JRadioButtonMenuItem

​(

Icon

icon,
boolean selected)

Creates a radio button menu item with the specified image
and selection state, but no text.

---

#### Constructor Summary

Creates a

JRadioButtonMenuItem

with no set text or icon.

Creates a

JRadioButtonMenuItem

with text.

Creates a radio button menu item with the specified text
and selection state.

Creates a radio button menu item with the specified text
and

Icon

.

Creates a radio button menu item that has the specified
text, image, and selection state.

Creates a radio button menu item whose properties are taken from the

Action

supplied.

Creates a

JRadioButtonMenuItem

with an icon.

Creates a radio button menu item with the specified image
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

Gets the AccessibleContext associated with this JRadioButtonMenuItem.

String

getUIClassID

()

Returns the name of the L&F class that renders this component.

protected

String

paramString

()

Returns a string representation of this

JRadioButtonMenuItem

.

- Methods declared in class javax.swing.

JMenuItem

actionPropertyChanged

,

addMenuDragMouseListener

,

addMenuKeyListener

,

configurePropertiesFromAction

,

fireMenuDragMouseDragged

,

fireMenuDragMouseEntered

,

fireMenuDragMouseExited

,

fireMenuDragMouseReleased

,

fireMenuKeyPressed

,

fireMenuKeyReleased

,

fireMenuKeyTyped

,

getAccelerator

,

getComponent

,

getMenuDragMouseListeners

,

getMenuKeyListeners

,

getSubElements

,

init

,

isArmed

,

menuSelectionChanged

,

processKeyEvent

,

processMenuDragMouseEvent

,

processMenuKeyEvent

,

processMouseEvent

,

removeMenuDragMouseListener

,

removeMenuKeyListener

,

setAccelerator

,

setArmed

,

setEnabled

,

setUI

,

updateUI

- Methods declared in class javax.swing.

AbstractButton

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

Gets the AccessibleContext associated with this JRadioButtonMenuItem.

Returns the name of the L&F class that renders this component.

Returns a string representation of this

JRadioButtonMenuItem

.

Methods declared in class javax.swing.

JMenuItem

actionPropertyChanged

,

addMenuDragMouseListener

,

addMenuKeyListener

,

configurePropertiesFromAction

,

fireMenuDragMouseDragged

,

fireMenuDragMouseEntered

,

fireMenuDragMouseExited

,

fireMenuDragMouseReleased

,

fireMenuKeyPressed

,

fireMenuKeyReleased

,

fireMenuKeyTyped

,

getAccelerator

,

getComponent

,

getMenuDragMouseListeners

,

getMenuKeyListeners

,

getSubElements

,

init

,

isArmed

,

menuSelectionChanged

,

processKeyEvent

,

processMenuDragMouseEvent

,

processMenuKeyEvent

,

processMouseEvent

,

removeMenuDragMouseListener

,

removeMenuKeyListener

,

setAccelerator

,

setArmed

,

setEnabled

,

setUI

,

updateUI

---

#### Methods declared in class javax.swing. JMenuItem

Methods declared in class javax.swing.

AbstractButton

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

- JRadioButtonMenuItem

```java
public JRadioButtonMenuItem()
```

Creates a

JRadioButtonMenuItem

with no set text or icon.

- JRadioButtonMenuItem

```java
public JRadioButtonMenuItem​(
Icon
icon)
```

Creates a

JRadioButtonMenuItem

with an icon.

**Parameters:** icon

- the

Icon

to display on the

JRadioButtonMenuItem

- JRadioButtonMenuItem

```java
public JRadioButtonMenuItem​(
String
text)
```

Creates a

JRadioButtonMenuItem

with text.

**Parameters:** text

- the text of the

JRadioButtonMenuItem

- JRadioButtonMenuItem

```java
public JRadioButtonMenuItem​(
Action
a)
```

Creates a radio button menu item whose properties are taken from the

Action

supplied.

**Parameters:** a

- the

Action

on which to base the radio
button menu item
**Since:** 1.3

- JRadioButtonMenuItem

```java
public JRadioButtonMenuItem​(
String
text,

Icon
icon)
```

Creates a radio button menu item with the specified text
and

Icon

.

**Parameters:** text

- the text of the

JRadioButtonMenuItem
**Parameters:** icon

- the icon to display on the

JRadioButtonMenuItem

- JRadioButtonMenuItem

```java
public JRadioButtonMenuItem​(
String
text,
boolean selected)
```

Creates a radio button menu item with the specified text
and selection state.

**Parameters:** text

- the text of the

CheckBoxMenuItem
**Parameters:** selected

- the selected state of the

CheckBoxMenuItem

- JRadioButtonMenuItem

```java
public JRadioButtonMenuItem​(
Icon
icon,
boolean selected)
```

Creates a radio button menu item with the specified image
and selection state, but no text.

**Parameters:** icon

- the image that the button should display
**Parameters:** selected

- if true, the button is initially selected;
otherwise, the button is initially unselected

- JRadioButtonMenuItem

```java
public JRadioButtonMenuItem​(
String
text,

Icon
icon,
boolean selected)
```

Creates a radio button menu item that has the specified
text, image, and selection state. All other constructors
defer to this one.

**Parameters:** text

- the string displayed on the radio button
**Parameters:** icon

- the image that the button should display
**Parameters:** selected

- if

true

, the button is initially selected,
otherwise, the button is initially unselected

============ METHOD DETAIL ==========

- Method Detail

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

JMenuItem
**Returns:** the string "RadioButtonMenuItemUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JRadioButtonMenuItem

. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JMenuItem
**Returns:** a string representation of this

JRadioButtonMenuItem

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

Gets the AccessibleContext associated with this JRadioButtonMenuItem.
For JRadioButtonMenuItems, the AccessibleContext takes the form of an
AccessibleJRadioButtonMenuItem.
A new AccessibleJRadioButtonMenuItem instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

JMenuItem
**Returns:** an AccessibleJRadioButtonMenuItem that serves as the
AccessibleContext of this JRadioButtonMenuItem

Constructor Detail

- JRadioButtonMenuItem

```java
public JRadioButtonMenuItem()
```

Creates a

JRadioButtonMenuItem

with no set text or icon.

- JRadioButtonMenuItem

```java
public JRadioButtonMenuItem​(
Icon
icon)
```

Creates a

JRadioButtonMenuItem

with an icon.

**Parameters:** icon

- the

Icon

to display on the

JRadioButtonMenuItem

- JRadioButtonMenuItem

```java
public JRadioButtonMenuItem​(
String
text)
```

Creates a

JRadioButtonMenuItem

with text.

**Parameters:** text

- the text of the

JRadioButtonMenuItem

- JRadioButtonMenuItem

```java
public JRadioButtonMenuItem​(
Action
a)
```

Creates a radio button menu item whose properties are taken from the

Action

supplied.

**Parameters:** a

- the

Action

on which to base the radio
button menu item
**Since:** 1.3

- JRadioButtonMenuItem

```java
public JRadioButtonMenuItem​(
String
text,

Icon
icon)
```

Creates a radio button menu item with the specified text
and

Icon

.

**Parameters:** text

- the text of the

JRadioButtonMenuItem
**Parameters:** icon

- the icon to display on the

JRadioButtonMenuItem

- JRadioButtonMenuItem

```java
public JRadioButtonMenuItem​(
String
text,
boolean selected)
```

Creates a radio button menu item with the specified text
and selection state.

**Parameters:** text

- the text of the

CheckBoxMenuItem
**Parameters:** selected

- the selected state of the

CheckBoxMenuItem

- JRadioButtonMenuItem

```java
public JRadioButtonMenuItem​(
Icon
icon,
boolean selected)
```

Creates a radio button menu item with the specified image
and selection state, but no text.

**Parameters:** icon

- the image that the button should display
**Parameters:** selected

- if true, the button is initially selected;
otherwise, the button is initially unselected

- JRadioButtonMenuItem

```java
public JRadioButtonMenuItem​(
String
text,

Icon
icon,
boolean selected)
```

Creates a radio button menu item that has the specified
text, image, and selection state. All other constructors
defer to this one.

**Parameters:** text

- the string displayed on the radio button
**Parameters:** icon

- the image that the button should display
**Parameters:** selected

- if

true

, the button is initially selected,
otherwise, the button is initially unselected

---

#### Constructor Detail

JRadioButtonMenuItem

```java
public JRadioButtonMenuItem()
```

Creates a

JRadioButtonMenuItem

with no set text or icon.

---

#### JRadioButtonMenuItem

public JRadioButtonMenuItem()

Creates a

JRadioButtonMenuItem

with no set text or icon.

JRadioButtonMenuItem

```java
public JRadioButtonMenuItem​(
Icon
icon)
```

Creates a

JRadioButtonMenuItem

with an icon.

**Parameters:** icon

- the

Icon

to display on the

JRadioButtonMenuItem

---

#### JRadioButtonMenuItem

public JRadioButtonMenuItem​(

Icon

icon)

Creates a

JRadioButtonMenuItem

with an icon.

JRadioButtonMenuItem

```java
public JRadioButtonMenuItem​(
String
text)
```

Creates a

JRadioButtonMenuItem

with text.

**Parameters:** text

- the text of the

JRadioButtonMenuItem

---

#### JRadioButtonMenuItem

public JRadioButtonMenuItem​(

String

text)

Creates a

JRadioButtonMenuItem

with text.

JRadioButtonMenuItem

```java
public JRadioButtonMenuItem​(
Action
a)
```

Creates a radio button menu item whose properties are taken from the

Action

supplied.

**Parameters:** a

- the

Action

on which to base the radio
button menu item
**Since:** 1.3

---

#### JRadioButtonMenuItem

public JRadioButtonMenuItem​(

Action

a)

Creates a radio button menu item whose properties are taken from the

Action

supplied.

JRadioButtonMenuItem

```java
public JRadioButtonMenuItem​(
String
text,

Icon
icon)
```

Creates a radio button menu item with the specified text
and

Icon

.

**Parameters:** text

- the text of the

JRadioButtonMenuItem
**Parameters:** icon

- the icon to display on the

JRadioButtonMenuItem

---

#### JRadioButtonMenuItem

public JRadioButtonMenuItem​(

String

text,

Icon

icon)

Creates a radio button menu item with the specified text
and

Icon

.

JRadioButtonMenuItem

```java
public JRadioButtonMenuItem​(
String
text,
boolean selected)
```

Creates a radio button menu item with the specified text
and selection state.

**Parameters:** text

- the text of the

CheckBoxMenuItem
**Parameters:** selected

- the selected state of the

CheckBoxMenuItem

---

#### JRadioButtonMenuItem

public JRadioButtonMenuItem​(

String

text,
boolean selected)

Creates a radio button menu item with the specified text
and selection state.

JRadioButtonMenuItem

```java
public JRadioButtonMenuItem​(
Icon
icon,
boolean selected)
```

Creates a radio button menu item with the specified image
and selection state, but no text.

**Parameters:** icon

- the image that the button should display
**Parameters:** selected

- if true, the button is initially selected;
otherwise, the button is initially unselected

---

#### JRadioButtonMenuItem

public JRadioButtonMenuItem​(

Icon

icon,
boolean selected)

Creates a radio button menu item with the specified image
and selection state, but no text.

JRadioButtonMenuItem

```java
public JRadioButtonMenuItem​(
String
text,

Icon
icon,
boolean selected)
```

Creates a radio button menu item that has the specified
text, image, and selection state. All other constructors
defer to this one.

**Parameters:** text

- the string displayed on the radio button
**Parameters:** icon

- the image that the button should display
**Parameters:** selected

- if

true

, the button is initially selected,
otherwise, the button is initially unselected

---

#### JRadioButtonMenuItem

public JRadioButtonMenuItem​(

String

text,

Icon

icon,
boolean selected)

Creates a radio button menu item that has the specified
text, image, and selection state. All other constructors
defer to this one.

Method Detail

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

JMenuItem
**Returns:** the string "RadioButtonMenuItemUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JRadioButtonMenuItem

. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JMenuItem
**Returns:** a string representation of this

JRadioButtonMenuItem

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

Gets the AccessibleContext associated with this JRadioButtonMenuItem.
For JRadioButtonMenuItems, the AccessibleContext takes the form of an
AccessibleJRadioButtonMenuItem.
A new AccessibleJRadioButtonMenuItem instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

JMenuItem
**Returns:** an AccessibleJRadioButtonMenuItem that serves as the
AccessibleContext of this JRadioButtonMenuItem

---

#### Method Detail

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

JMenuItem
**Returns:** the string "RadioButtonMenuItemUI"
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

paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JRadioButtonMenuItem

. This method
is intended to be used only for debugging purposes, and the
content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JMenuItem
**Returns:** a string representation of this

JRadioButtonMenuItem

---

#### paramString

protected

String

paramString()

Returns a string representation of this

JRadioButtonMenuItem

. This method
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

Gets the AccessibleContext associated with this JRadioButtonMenuItem.
For JRadioButtonMenuItems, the AccessibleContext takes the form of an
AccessibleJRadioButtonMenuItem.
A new AccessibleJRadioButtonMenuItem instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

JMenuItem
**Returns:** an AccessibleJRadioButtonMenuItem that serves as the
AccessibleContext of this JRadioButtonMenuItem

---

#### getAccessibleContext

@BeanProperty

(

bound

=false)
public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this JRadioButtonMenuItem.
For JRadioButtonMenuItems, the AccessibleContext takes the form of an
AccessibleJRadioButtonMenuItem.
A new AccessibleJRadioButtonMenuItem instance is created if necessary.

---

