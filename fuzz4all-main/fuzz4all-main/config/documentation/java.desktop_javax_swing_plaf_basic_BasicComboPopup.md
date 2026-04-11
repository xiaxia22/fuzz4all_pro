# Class BasicComboPopup

**Source:** `java.desktop\javax\swing\plaf\basic\BasicComboPopup.html`

### Class Description

```java
public class
BasicComboPopup

extends
JPopupMenu

implements
ComboPopup
```

This is a basic implementation of the

ComboPopup

interface.

This class represents the ui for the popup portion of the combo box.

All event handling is handled by listener classes created with the

createxxxListener()

methods and internal classes.
You can change the behavior of this class by overriding the

createxxxListener()

methods and supplying your own
event listeners or subclassing from the ones supplied in this class.

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

,

MenuElement

,

ComboPopup

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
> list

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:**
- getList()

,

createList()

---

#### protected
JScrollPane
scroller

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

**See Also:**
- createScroller()

---

#### protected boolean valueIsAdjusting

As of Java 2 platform v1.4 this previously undocumented field is no
longer used.

---

#### protected
MouseMotionListener
mouseMotionListener

This protected field is implementation specific. Do not access directly
or override. Use the accessor or create methods instead.

**See Also:**
- getMouseMotionListener()

,

createMouseMotionListener()

---

#### protected
MouseListener
mouseListener

This protected field is implementation specific. Do not access directly
or override. Use the accessor or create methods instead.

**See Also:**
- getMouseListener()

,

createMouseListener()

---

#### protected
KeyListener
keyListener

This protected field is implementation specific. Do not access directly
or override. Use the accessor or create methods instead.

**See Also:**
- getKeyListener()

,

createKeyListener()

---

#### protected
ListSelectionListener
listSelectionListener

This protected field is implementation specific. Do not access directly
or override. Use the create method instead.

**See Also:**
- createListSelectionListener()

---

#### protected
MouseListener
listMouseListener

This protected field is implementation specific. Do not access directly
or override. Use the create method instead.

**See Also:**
- createListMouseListener()

---

#### protected
MouseMotionListener
listMouseMotionListener

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

**See Also:**
- createListMouseMotionListener()

---

#### protected
PropertyChangeListener
propertyChangeListener

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

**See Also:**
- createPropertyChangeListener()

---

#### protected
ListDataListener
listDataListener

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

**See Also:**
- createListDataListener()

---

#### protected
ItemListener
itemListener

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

**See Also:**
- createItemListener()

---

#### protected
Timer
autoscrollTimer

This protected field is implementation specific. Do not access directly
or override.

---

#### protected boolean hasEntered

true

if the mouse cursor is in the popup.

---

#### protected boolean isAutoScrolling

If

true

the auto-scrolling is enabled.

---

#### protected int scrollDirection

The direction of scrolling.

---

#### protected static final int SCROLL_UP

The direction of scrolling up.

**See Also:**
- Constant Field Values

---

#### protected static final int SCROLL_DOWN

The direction of scrolling down.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public BasicComboPopup​(
JComboBox
<
Object
> combo)

Constructs a new instance of

BasicComboPopup

.

**Parameters:**
- combo

- an instance of

JComboBox

---

### Method Details

#### public void show()

Implementation of ComboPopup.show().

**Specified by:**
- show

in interface

ComboPopup

**Overrides:**
- show

in class

Component

---

#### public void hide()

Implementation of ComboPopup.hide().

**Specified by:**
- hide

in interface

ComboPopup

**Overrides:**
- hide

in class

Component

---

#### public
JList
<
Object
> getList()

Implementation of ComboPopup.getList().

**Specified by:**
- getList

in interface

ComboPopup

**Returns:**
- the list that is being used to draw the items in the combo box

---

#### public
MouseListener
getMouseListener()

Implementation of ComboPopup.getMouseListener().

**Specified by:**
- getMouseListener

in interface

ComboPopup

**Returns:**
- a

MouseListener

or null

**See Also:**
- ComboPopup.getMouseListener()

---

#### public
MouseMotionListener
getMouseMotionListener()

Implementation of ComboPopup.getMouseMotionListener().

**Specified by:**
- getMouseMotionListener

in interface

ComboPopup

**Returns:**
- a

MouseMotionListener

or null

**See Also:**
- ComboPopup.getMouseMotionListener()

---

#### public
KeyListener
getKeyListener()

Implementation of ComboPopup.getKeyListener().

**Specified by:**
- getKeyListener

in interface

ComboPopup

**Returns:**
- a

KeyListener

or null

**See Also:**
- ComboPopup.getKeyListener()

---

#### public void uninstallingUI()

Called when the UI is uninstalling. Since this popup isn't in the component
tree, it won't get it's uninstallUI() called. It removes the listeners that
were added in addComboBoxListeners().

**Specified by:**
- uninstallingUI

in interface

ComboPopup

---

#### protected void uninstallComboBoxModelListeners​(
ComboBoxModel
<?> model)

Removes the listeners from the combo box model

**Parameters:**
- model

- The combo box model to install listeners

**See Also:**
- installComboBoxModelListeners(javax.swing.ComboBoxModel<?>)

---

#### protected void uninstallKeyboardActions()

Unregisters keyboard actions.

---

#### protected
MouseListener
createMouseListener()

Creates a listener
that will watch for mouse-press and release events on the combo box.

Warning:

When overriding this method, make sure to maintain the existing
behavior.

**Returns:**
- a

MouseListener

which will be added to
the combo box or null

---

#### protected
MouseMotionListener
createMouseMotionListener()

Creates the mouse motion listener which will be added to the combo
box.

Warning:

When overriding this method, make sure to maintain the existing
behavior.

**Returns:**
- a

MouseMotionListener

which will be added to
the combo box or null

---

#### protected
KeyListener
createKeyListener()

Creates the key listener that will be added to the combo box. If
this method returns null then it will not be added to the combo box.

**Returns:**
- a

KeyListener

or null

---

#### protected
ListSelectionListener
createListSelectionListener()

Creates a list selection listener that watches for selection changes in
the popup's list. If this method returns null then it will not
be added to the popup list.

**Returns:**
- an instance of a

ListSelectionListener

or null

---

#### protected
ListDataListener
createListDataListener()

Creates a list data listener which will be added to the

ComboBoxModel

. If this method returns null then
it will not be added to the combo box model.

**Returns:**
- an instance of a

ListDataListener

or null

---

#### protected
MouseListener
createListMouseListener()

Creates a mouse listener that watches for mouse events in
the popup's list. If this method returns null then it will
not be added to the combo box.

**Returns:**
- an instance of a

MouseListener

or null

---

#### protected
MouseMotionListener
createListMouseMotionListener()

Creates a mouse motion listener that watches for mouse motion
events in the popup's list. If this method returns null then it will
not be added to the combo box.

**Returns:**
- an instance of a

MouseMotionListener

or null

---

#### protected
PropertyChangeListener
createPropertyChangeListener()

Creates a

PropertyChangeListener

which will be added to
the combo box. If this method returns null then it will not
be added to the combo box.

**Returns:**
- an instance of a

PropertyChangeListener

or null

---

#### protected
ItemListener
createItemListener()

Creates an

ItemListener

which will be added to the
combo box. If this method returns null then it will not
be added to the combo box.

Subclasses may override this method to return instances of their own
ItemEvent handlers.

**Returns:**
- an instance of an

ItemListener

or null

---

#### protected
JList
<
Object
> createList()

Creates the JList used in the popup to display
the items in the combo box model. This method is called when the UI class
is created.

**Returns:**
- a

JList

used to display the combo box items

---

#### protected void configureList()

Configures the list which is used to hold the combo box items in the
popup. This method is called when the UI class
is created.

**See Also:**
- createList()

---

#### protected void installListListeners()

Adds the listeners to the list control.

---

#### protected
JScrollPane
createScroller()

Creates the scroll pane which houses the scrollable list.

**Returns:**
- the scroll pane which houses the scrollable list

---

#### protected void configureScroller()

Configures the scrollable portion which holds the list within
the combo box popup. This method is called when the UI class
is created.

---

#### protected void configurePopup()

Configures the popup portion of the combo box. This method is called
when the UI class is created.

---

#### protected void installComboBoxListeners()

This method adds the necessary listeners to the JComboBox.

---

#### protected void installComboBoxModelListeners​(
ComboBoxModel
<?> model)

Installs the listeners on the combo box model. Any listeners installed
on the combo box model should be removed in

uninstallComboBoxModelListeners

.

**Parameters:**
- model

- The combo box model to install listeners

**See Also:**
- uninstallComboBoxModelListeners(javax.swing.ComboBoxModel<?>)

---

#### protected void installKeyboardActions()

Registers keyboard actions.

---

#### public boolean isFocusTraversable()

Overridden to unconditionally return false.

**Overrides:**
- isFocusTraversable

in class

Component

**Returns:**
- true

if this

Component

is
focusable;

false

otherwise

**See Also:**
- Component.setFocusable(boolean)

---

#### protected void startAutoScrolling​(int direction)

This protected method is implementation specific and should be private.
do not call or override.

**Parameters:**
- direction

- the direction of scrolling

---

#### protected void stopAutoScrolling()

This protected method is implementation specific and should be private.
do not call or override.

---

#### protected void autoScrollUp()

This protected method is implementation specific and should be private.
do not call or override.

---

#### protected void autoScrollDown()

This protected method is implementation specific and should be private.
do not call or override.

---

#### public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this BasicComboPopup.
The AccessibleContext will have its parent set to the ComboBox.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

JPopupMenu

**Returns:**
- an AccessibleContext for the BasicComboPopup

**Since:**
- 1.5

---

#### protected void delegateFocus​(
MouseEvent
e)

This is a utility method that helps event handlers figure out where to
send the focus when the popup is brought up. The standard implementation
delegates the focus to the editor (if the combo box is editable) or to
the JComboBox if it is not editable.

**Parameters:**
- e

- a mouse event

---

#### protected void togglePopup()

Makes the popup visible if it is hidden and makes it hidden if it is
visible.

---

#### protected
MouseEvent
convertMouseEvent​(
MouseEvent
e)

Converts mouse event.

**Parameters:**
- e

- a mouse event

**Returns:**
- converted mouse event

---

#### protected int getPopupHeightForRowCount​(int maxRowCount)

Retrieves the height of the popup based on the current
ListCellRenderer and the maximum row count.

**Parameters:**
- maxRowCount

- the row count

**Returns:**
- the height of the popup

---

#### protected
Rectangle
computePopupBounds​(int px,
int py,
int pw,
int ph)

Calculate the placement and size of the popup portion of the combo box based
on the combo box location and the enclosing screen bounds. If
no transformations are required, then the returned rectangle will
have the same values as the parameters.

**Parameters:**
- px

- starting x location
- py

- starting y location
- pw

- starting width
- ph

- starting height

**Returns:**
- a rectangle which represents the placement and size of the popup

---

#### protected void updateListBoxSelectionForEvent​(
MouseEvent
anEvent,
boolean shouldScroll)

A utility method used by the event listeners. Given a mouse event, it changes
the list selection to the list item below the mouse.

**Parameters:**
- anEvent

- a mouse event
- shouldScroll

- if

true

list should be scrolled.

---

### Additional Sections

#### Class BasicComboPopup

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JPopupMenu
- - javax.swing.plaf.basic.BasicComboPopup

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JPopupMenu
- - javax.swing.plaf.basic.BasicComboPopup

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JPopupMenu
- - javax.swing.plaf.basic.BasicComboPopup

javax.swing.JComponent

- javax.swing.JPopupMenu
- - javax.swing.plaf.basic.BasicComboPopup

javax.swing.JPopupMenu

- javax.swing.plaf.basic.BasicComboPopup

javax.swing.plaf.basic.BasicComboPopup

**All Implemented Interfaces:** ImageObserver

,

MenuContainer

,

Serializable

,

Accessible

,

MenuElement

,

ComboPopup

**Direct Known Subclasses:** MetalComboBoxUI.MetalComboPopup

```java
public class
BasicComboPopup

extends
JPopupMenu

implements
ComboPopup
```

This is a basic implementation of the

ComboPopup

interface.

This class represents the ui for the popup portion of the combo box.

All event handling is handled by listener classes created with the

createxxxListener()

methods and internal classes.
You can change the behavior of this class by overriding the

createxxxListener()

methods and supplying your own
event listeners or subclassing from the ones supplied in this class.

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

BasicComboPopup

extends

JPopupMenu

implements

ComboPopup

This is a basic implementation of the

ComboPopup

interface.

This class represents the ui for the popup portion of the combo box.

All event handling is handled by listener classes created with the

createxxxListener()

methods and internal classes.
You can change the behavior of this class by overriding the

createxxxListener()

methods and supplying your own
event listeners or subclassing from the ones supplied in this class.

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

All event handling is handled by listener classes created with the

createxxxListener()

methods and internal classes.
You can change the behavior of this class by overriding the

createxxxListener()

methods and supplying your own
event listeners or subclassing from the ones supplied in this class.

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

BasicComboPopup.InvocationKeyHandler

As of Java 2 platform v 1.4, this class is now obsolete and is only included for
backwards API compatibility.

protected class

BasicComboPopup.InvocationMouseHandler

A listener to be registered upon the combo box
(

not

its popup menu)
to handle mouse events
that affect the state of the popup menu.

protected class

BasicComboPopup.InvocationMouseMotionHandler

This listener watches for dragging and updates the current selection in the
list if it is dragging over the list.

protected class

BasicComboPopup.ItemHandler

This listener watches for changes to the selection in the
combo box.

class

BasicComboPopup.ListDataHandler

As of 1.4, this class is now obsolete, doesn't do anything, and
is only included for backwards API compatibility.

protected class

BasicComboPopup.ListMouseHandler

This listener hides the popup when the mouse is released in the list.

protected class

BasicComboPopup.ListMouseMotionHandler

This listener changes the selected item as you move the mouse over the list.

protected class

BasicComboPopup.ListSelectionHandler

As of Java 2 platform v 1.4, this class is now obsolete, doesn't do anything, and
is only included for backwards API compatibility.

protected class

BasicComboPopup.PropertyChangeHandler

This listener watches for bound properties that have changed in the
combo box.

- Nested classes/interfaces declared in class javax.swing.

JPopupMenu

JPopupMenu.AccessibleJPopupMenu

,

JPopupMenu.Separator

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

Timer

autoscrollTimer

This protected field is implementation specific.

protected

JComboBox

<

Object

>

comboBox

The instance of

JComboBox

.

protected boolean

hasEntered

true

if the mouse cursor is in the popup.

protected boolean

isAutoScrolling

If

true

the auto-scrolling is enabled.

protected

ItemListener

itemListener

This protected field is implementation specific.

protected

KeyListener

keyListener

This protected field is implementation specific.

protected

JList

<

Object

>

list

This protected field is implementation specific.

protected

ListDataListener

listDataListener

This protected field is implementation specific.

protected

MouseListener

listMouseListener

This protected field is implementation specific.

protected

MouseMotionListener

listMouseMotionListener

This protected field is implementation specific.

protected

ListSelectionListener

listSelectionListener

This protected field is implementation specific.

protected

MouseListener

mouseListener

This protected field is implementation specific.

protected

MouseMotionListener

mouseMotionListener

This protected field is implementation specific.

protected

PropertyChangeListener

propertyChangeListener

This protected field is implementation specific.

protected static int

SCROLL_DOWN

The direction of scrolling down.

protected static int

SCROLL_UP

The direction of scrolling up.

protected int

scrollDirection

The direction of scrolling.

protected

JScrollPane

scroller

This protected field is implementation specific.

protected boolean

valueIsAdjusting

As of Java 2 platform v1.4 this previously undocumented field is no
longer used.

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

BasicComboPopup

​(

JComboBox

<

Object

> combo)

Constructs a new instance of

BasicComboPopup

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

autoScrollDown

()

This protected method is implementation specific and should be private.

protected void

autoScrollUp

()

This protected method is implementation specific and should be private.

protected

Rectangle

computePopupBounds

​(int px,
int py,
int pw,
int ph)

Calculate the placement and size of the popup portion of the combo box based
on the combo box location and the enclosing screen bounds.

protected void

configureList

()

Configures the list which is used to hold the combo box items in the
popup.

protected void

configurePopup

()

Configures the popup portion of the combo box.

protected void

configureScroller

()

Configures the scrollable portion which holds the list within
the combo box popup.

protected

MouseEvent

convertMouseEvent

​(

MouseEvent

e)

Converts mouse event.

protected

ItemListener

createItemListener

()

Creates an

ItemListener

which will be added to the
combo box.

protected

KeyListener

createKeyListener

()

Creates the key listener that will be added to the combo box.

protected

JList

<

Object

>

createList

()

Creates the JList used in the popup to display
the items in the combo box model.

protected

ListDataListener

createListDataListener

()

Creates a list data listener which will be added to the

ComboBoxModel

.

protected

MouseListener

createListMouseListener

()

Creates a mouse listener that watches for mouse events in
the popup's list.

protected

MouseMotionListener

createListMouseMotionListener

()

Creates a mouse motion listener that watches for mouse motion
events in the popup's list.

protected

ListSelectionListener

createListSelectionListener

()

Creates a list selection listener that watches for selection changes in
the popup's list.

protected

MouseListener

createMouseListener

()

Creates a listener
that will watch for mouse-press and release events on the combo box.

protected

MouseMotionListener

createMouseMotionListener

()

Creates the mouse motion listener which will be added to the combo
box.

protected

PropertyChangeListener

createPropertyChangeListener

()

Creates a

PropertyChangeListener

which will be added to
the combo box.

protected

JScrollPane

createScroller

()

Creates the scroll pane which houses the scrollable list.

protected void

delegateFocus

​(

MouseEvent

e)

This is a utility method that helps event handlers figure out where to
send the focus when the popup is brought up.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this BasicComboPopup.

KeyListener

getKeyListener

()

Implementation of ComboPopup.getKeyListener().

JList

<

Object

>

getList

()

Implementation of ComboPopup.getList().

MouseListener

getMouseListener

()

Implementation of ComboPopup.getMouseListener().

MouseMotionListener

getMouseMotionListener

()

Implementation of ComboPopup.getMouseMotionListener().

protected int

getPopupHeightForRowCount

​(int maxRowCount)

Retrieves the height of the popup based on the current
ListCellRenderer and the maximum row count.

void

hide

()

Implementation of ComboPopup.hide().

protected void

installComboBoxListeners

()

This method adds the necessary listeners to the JComboBox.

protected void

installComboBoxModelListeners

​(

ComboBoxModel

<?> model)

Installs the listeners on the combo box model.

protected void

installKeyboardActions

()

Registers keyboard actions.

protected void

installListListeners

()

Adds the listeners to the list control.

boolean

isFocusTraversable

()

Overridden to unconditionally return false.

void

show

()

Implementation of ComboPopup.show().

protected void

startAutoScrolling

​(int direction)

This protected method is implementation specific and should be private.

protected void

stopAutoScrolling

()

This protected method is implementation specific and should be private.

protected void

togglePopup

()

Makes the popup visible if it is hidden and makes it hidden if it is
visible.

protected void

uninstallComboBoxModelListeners

​(

ComboBoxModel

<?> model)

Removes the listeners from the combo box model

void

uninstallingUI

()

Called when the UI is uninstalling.

protected void

uninstallKeyboardActions

()

Unregisters keyboard actions.

protected void

updateListBoxSelectionForEvent

​(

MouseEvent

anEvent,
boolean shouldScroll)

A utility method used by the event listeners.

- Methods declared in class javax.swing.

JPopupMenu

add

,

add

,

add

,

addMenuKeyListener

,

addPopupMenuListener

,

addSeparator

,

createActionChangeListener

,

createActionComponent

,

firePopupMenuCanceled

,

firePopupMenuWillBecomeInvisible

,

firePopupMenuWillBecomeVisible

,

getComponent

,

getComponentAtIndex

,

getComponentIndex

,

getDefaultLightWeightPopupEnabled

,

getInvoker

,

getLabel

,

getMargin

,

getMenuKeyListeners

,

getPopupMenuListeners

,

getSelectionModel

,

getSubElements

,

getUI

,

getUIClassID

,

insert

,

insert

,

isBorderPainted

,

isLightWeightPopupEnabled

,

isPopupTrigger

,

isVisible

,

menuSelectionChanged

,

pack

,

paintBorder

,

paramString

,

processKeyEvent

,

processKeyEvent

,

processMouseEvent

,

remove

,

removeMenuKeyListener

,

removePopupMenuListener

,

setBorderPainted

,

setDefaultLightWeightPopupEnabled

,

setInvoker

,

setLabel

,

setLightWeightPopupEnabled

,

setLocation

,

setPopupSize

,

setPopupSize

,

setSelected

,

setSelectionModel

,

setUI

,

setVisible

,

show

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

- Methods declared in interface javax.swing.plaf.basic.

ComboPopup

isVisible

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

BasicComboPopup.InvocationKeyHandler

As of Java 2 platform v 1.4, this class is now obsolete and is only included for
backwards API compatibility.

protected class

BasicComboPopup.InvocationMouseHandler

A listener to be registered upon the combo box
(

not

its popup menu)
to handle mouse events
that affect the state of the popup menu.

protected class

BasicComboPopup.InvocationMouseMotionHandler

This listener watches for dragging and updates the current selection in the
list if it is dragging over the list.

protected class

BasicComboPopup.ItemHandler

This listener watches for changes to the selection in the
combo box.

class

BasicComboPopup.ListDataHandler

As of 1.4, this class is now obsolete, doesn't do anything, and
is only included for backwards API compatibility.

protected class

BasicComboPopup.ListMouseHandler

This listener hides the popup when the mouse is released in the list.

protected class

BasicComboPopup.ListMouseMotionHandler

This listener changes the selected item as you move the mouse over the list.

protected class

BasicComboPopup.ListSelectionHandler

As of Java 2 platform v 1.4, this class is now obsolete, doesn't do anything, and
is only included for backwards API compatibility.

protected class

BasicComboPopup.PropertyChangeHandler

This listener watches for bound properties that have changed in the
combo box.

- Nested classes/interfaces declared in class javax.swing.

JPopupMenu

JPopupMenu.AccessibleJPopupMenu

,

JPopupMenu.Separator

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

As of Java 2 platform v 1.4, this class is now obsolete and is only included for
backwards API compatibility.

A listener to be registered upon the combo box
(

not

its popup menu)
to handle mouse events
that affect the state of the popup menu.

This listener watches for dragging and updates the current selection in the
list if it is dragging over the list.

This listener watches for changes to the selection in the
combo box.

As of 1.4, this class is now obsolete, doesn't do anything, and
is only included for backwards API compatibility.

This listener hides the popup when the mouse is released in the list.

This listener changes the selected item as you move the mouse over the list.

As of Java 2 platform v 1.4, this class is now obsolete, doesn't do anything, and
is only included for backwards API compatibility.

This listener watches for bound properties that have changed in the
combo box.

Nested classes/interfaces declared in class javax.swing.

JPopupMenu

JPopupMenu.AccessibleJPopupMenu

,

JPopupMenu.Separator

---

#### Nested classes/interfaces declared in class javax.swing. JPopupMenu

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

Timer

autoscrollTimer

This protected field is implementation specific.

protected

JComboBox

<

Object

>

comboBox

The instance of

JComboBox

.

protected boolean

hasEntered

true

if the mouse cursor is in the popup.

protected boolean

isAutoScrolling

If

true

the auto-scrolling is enabled.

protected

ItemListener

itemListener

This protected field is implementation specific.

protected

KeyListener

keyListener

This protected field is implementation specific.

protected

JList

<

Object

>

list

This protected field is implementation specific.

protected

ListDataListener

listDataListener

This protected field is implementation specific.

protected

MouseListener

listMouseListener

This protected field is implementation specific.

protected

MouseMotionListener

listMouseMotionListener

This protected field is implementation specific.

protected

ListSelectionListener

listSelectionListener

This protected field is implementation specific.

protected

MouseListener

mouseListener

This protected field is implementation specific.

protected

MouseMotionListener

mouseMotionListener

This protected field is implementation specific.

protected

PropertyChangeListener

propertyChangeListener

This protected field is implementation specific.

protected static int

SCROLL_DOWN

The direction of scrolling down.

protected static int

SCROLL_UP

The direction of scrolling up.

protected int

scrollDirection

The direction of scrolling.

protected

JScrollPane

scroller

This protected field is implementation specific.

protected boolean

valueIsAdjusting

As of Java 2 platform v1.4 this previously undocumented field is no
longer used.

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

This protected field is implementation specific.

The instance of

JComboBox

.

true

if the mouse cursor is in the popup.

If

true

the auto-scrolling is enabled.

The direction of scrolling down.

The direction of scrolling up.

The direction of scrolling.

As of Java 2 platform v1.4 this previously undocumented field is no
longer used.

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

BasicComboPopup

​(

JComboBox

<

Object

> combo)

Constructs a new instance of

BasicComboPopup

.

---

#### Constructor Summary

Constructs a new instance of

BasicComboPopup

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

autoScrollDown

()

This protected method is implementation specific and should be private.

protected void

autoScrollUp

()

This protected method is implementation specific and should be private.

protected

Rectangle

computePopupBounds

​(int px,
int py,
int pw,
int ph)

Calculate the placement and size of the popup portion of the combo box based
on the combo box location and the enclosing screen bounds.

protected void

configureList

()

Configures the list which is used to hold the combo box items in the
popup.

protected void

configurePopup

()

Configures the popup portion of the combo box.

protected void

configureScroller

()

Configures the scrollable portion which holds the list within
the combo box popup.

protected

MouseEvent

convertMouseEvent

​(

MouseEvent

e)

Converts mouse event.

protected

ItemListener

createItemListener

()

Creates an

ItemListener

which will be added to the
combo box.

protected

KeyListener

createKeyListener

()

Creates the key listener that will be added to the combo box.

protected

JList

<

Object

>

createList

()

Creates the JList used in the popup to display
the items in the combo box model.

protected

ListDataListener

createListDataListener

()

Creates a list data listener which will be added to the

ComboBoxModel

.

protected

MouseListener

createListMouseListener

()

Creates a mouse listener that watches for mouse events in
the popup's list.

protected

MouseMotionListener

createListMouseMotionListener

()

Creates a mouse motion listener that watches for mouse motion
events in the popup's list.

protected

ListSelectionListener

createListSelectionListener

()

Creates a list selection listener that watches for selection changes in
the popup's list.

protected

MouseListener

createMouseListener

()

Creates a listener
that will watch for mouse-press and release events on the combo box.

protected

MouseMotionListener

createMouseMotionListener

()

Creates the mouse motion listener which will be added to the combo
box.

protected

PropertyChangeListener

createPropertyChangeListener

()

Creates a

PropertyChangeListener

which will be added to
the combo box.

protected

JScrollPane

createScroller

()

Creates the scroll pane which houses the scrollable list.

protected void

delegateFocus

​(

MouseEvent

e)

This is a utility method that helps event handlers figure out where to
send the focus when the popup is brought up.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this BasicComboPopup.

KeyListener

getKeyListener

()

Implementation of ComboPopup.getKeyListener().

JList

<

Object

>

getList

()

Implementation of ComboPopup.getList().

MouseListener

getMouseListener

()

Implementation of ComboPopup.getMouseListener().

MouseMotionListener

getMouseMotionListener

()

Implementation of ComboPopup.getMouseMotionListener().

protected int

getPopupHeightForRowCount

​(int maxRowCount)

Retrieves the height of the popup based on the current
ListCellRenderer and the maximum row count.

void

hide

()

Implementation of ComboPopup.hide().

protected void

installComboBoxListeners

()

This method adds the necessary listeners to the JComboBox.

protected void

installComboBoxModelListeners

​(

ComboBoxModel

<?> model)

Installs the listeners on the combo box model.

protected void

installKeyboardActions

()

Registers keyboard actions.

protected void

installListListeners

()

Adds the listeners to the list control.

boolean

isFocusTraversable

()

Overridden to unconditionally return false.

void

show

()

Implementation of ComboPopup.show().

protected void

startAutoScrolling

​(int direction)

This protected method is implementation specific and should be private.

protected void

stopAutoScrolling

()

This protected method is implementation specific and should be private.

protected void

togglePopup

()

Makes the popup visible if it is hidden and makes it hidden if it is
visible.

protected void

uninstallComboBoxModelListeners

​(

ComboBoxModel

<?> model)

Removes the listeners from the combo box model

void

uninstallingUI

()

Called when the UI is uninstalling.

protected void

uninstallKeyboardActions

()

Unregisters keyboard actions.

protected void

updateListBoxSelectionForEvent

​(

MouseEvent

anEvent,
boolean shouldScroll)

A utility method used by the event listeners.

- Methods declared in class javax.swing.

JPopupMenu

add

,

add

,

add

,

addMenuKeyListener

,

addPopupMenuListener

,

addSeparator

,

createActionChangeListener

,

createActionComponent

,

firePopupMenuCanceled

,

firePopupMenuWillBecomeInvisible

,

firePopupMenuWillBecomeVisible

,

getComponent

,

getComponentAtIndex

,

getComponentIndex

,

getDefaultLightWeightPopupEnabled

,

getInvoker

,

getLabel

,

getMargin

,

getMenuKeyListeners

,

getPopupMenuListeners

,

getSelectionModel

,

getSubElements

,

getUI

,

getUIClassID

,

insert

,

insert

,

isBorderPainted

,

isLightWeightPopupEnabled

,

isPopupTrigger

,

isVisible

,

menuSelectionChanged

,

pack

,

paintBorder

,

paramString

,

processKeyEvent

,

processKeyEvent

,

processMouseEvent

,

remove

,

removeMenuKeyListener

,

removePopupMenuListener

,

setBorderPainted

,

setDefaultLightWeightPopupEnabled

,

setInvoker

,

setLabel

,

setLightWeightPopupEnabled

,

setLocation

,

setPopupSize

,

setPopupSize

,

setSelected

,

setSelectionModel

,

setUI

,

setVisible

,

show

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

- Methods declared in interface javax.swing.plaf.basic.

ComboPopup

isVisible

---

#### Method Summary

This protected method is implementation specific and should be private.

Calculate the placement and size of the popup portion of the combo box based
on the combo box location and the enclosing screen bounds.

Configures the list which is used to hold the combo box items in the
popup.

Configures the popup portion of the combo box.

Configures the scrollable portion which holds the list within
the combo box popup.

Converts mouse event.

Creates an

ItemListener

which will be added to the
combo box.

Creates the key listener that will be added to the combo box.

Creates the JList used in the popup to display
the items in the combo box model.

Creates a list data listener which will be added to the

ComboBoxModel

.

Creates a mouse listener that watches for mouse events in
the popup's list.

Creates a mouse motion listener that watches for mouse motion
events in the popup's list.

Creates a list selection listener that watches for selection changes in
the popup's list.

Creates a listener
that will watch for mouse-press and release events on the combo box.

Creates the mouse motion listener which will be added to the combo
box.

Creates a

PropertyChangeListener

which will be added to
the combo box.

Creates the scroll pane which houses the scrollable list.

This is a utility method that helps event handlers figure out where to
send the focus when the popup is brought up.

Gets the AccessibleContext associated with this BasicComboPopup.

Implementation of ComboPopup.getKeyListener().

Implementation of ComboPopup.getList().

Implementation of ComboPopup.getMouseListener().

Implementation of ComboPopup.getMouseMotionListener().

Retrieves the height of the popup based on the current
ListCellRenderer and the maximum row count.

Implementation of ComboPopup.hide().

This method adds the necessary listeners to the JComboBox.

Installs the listeners on the combo box model.

Registers keyboard actions.

Adds the listeners to the list control.

Overridden to unconditionally return false.

Implementation of ComboPopup.show().

Makes the popup visible if it is hidden and makes it hidden if it is
visible.

Removes the listeners from the combo box model

Called when the UI is uninstalling.

Unregisters keyboard actions.

A utility method used by the event listeners.

Methods declared in class javax.swing.

JPopupMenu

add

,

add

,

add

,

addMenuKeyListener

,

addPopupMenuListener

,

addSeparator

,

createActionChangeListener

,

createActionComponent

,

firePopupMenuCanceled

,

firePopupMenuWillBecomeInvisible

,

firePopupMenuWillBecomeVisible

,

getComponent

,

getComponentAtIndex

,

getComponentIndex

,

getDefaultLightWeightPopupEnabled

,

getInvoker

,

getLabel

,

getMargin

,

getMenuKeyListeners

,

getPopupMenuListeners

,

getSelectionModel

,

getSubElements

,

getUI

,

getUIClassID

,

insert

,

insert

,

isBorderPainted

,

isLightWeightPopupEnabled

,

isPopupTrigger

,

isVisible

,

menuSelectionChanged

,

pack

,

paintBorder

,

paramString

,

processKeyEvent

,

processKeyEvent

,

processMouseEvent

,

remove

,

removeMenuKeyListener

,

removePopupMenuListener

,

setBorderPainted

,

setDefaultLightWeightPopupEnabled

,

setInvoker

,

setLabel

,

setLightWeightPopupEnabled

,

setLocation

,

setPopupSize

,

setPopupSize

,

setSelected

,

setSelectionModel

,

setUI

,

setVisible

,

show

,

updateUI

---

#### Methods declared in class javax.swing. JPopupMenu

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

Methods declared in interface javax.swing.plaf.basic.

ComboPopup

isVisible

---

#### Methods declared in interface javax.swing.plaf.basic. ComboPopup

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

- list

```java
protected
JList
<
Object
> list
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** getList()

,

createList()

- scroller

```java
protected
JScrollPane
scroller
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

**See Also:** createScroller()

- valueIsAdjusting

```java
protected boolean valueIsAdjusting
```

As of Java 2 platform v1.4 this previously undocumented field is no
longer used.

- mouseMotionListener

```java
protected
MouseMotionListener
mouseMotionListener
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor or create methods instead.

**See Also:** getMouseMotionListener()

,

createMouseMotionListener()

- mouseListener

```java
protected
MouseListener
mouseListener
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor or create methods instead.

**See Also:** getMouseListener()

,

createMouseListener()

- keyListener

```java
protected
KeyListener
keyListener
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor or create methods instead.

**See Also:** getKeyListener()

,

createKeyListener()

- listSelectionListener

```java
protected
ListSelectionListener
listSelectionListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead.

**See Also:** createListSelectionListener()

- listMouseListener

```java
protected
MouseListener
listMouseListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead.

**See Also:** createListMouseListener()

- listMouseMotionListener

```java
protected
MouseMotionListener
listMouseMotionListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

**See Also:** createListMouseMotionListener()

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

**See Also:** createPropertyChangeListener()

- listDataListener

```java
protected
ListDataListener
listDataListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

**See Also:** createListDataListener()

- itemListener

```java
protected
ItemListener
itemListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

**See Also:** createItemListener()

- autoscrollTimer

```java
protected
Timer
autoscrollTimer
```

This protected field is implementation specific. Do not access directly
or override.

- hasEntered

```java
protected boolean hasEntered
```

true

if the mouse cursor is in the popup.

- isAutoScrolling

```java
protected boolean isAutoScrolling
```

If

true

the auto-scrolling is enabled.

- scrollDirection

```java
protected int scrollDirection
```

The direction of scrolling.

- SCROLL_UP

```java
protected static final int SCROLL_UP
```

The direction of scrolling up.

**See Also:** Constant Field Values

- SCROLL_DOWN

```java
protected static final int SCROLL_DOWN
```

The direction of scrolling down.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicComboPopup

```java
public BasicComboPopup​(
JComboBox
<
Object
> combo)
```

Constructs a new instance of

BasicComboPopup

.

**Parameters:** combo

- an instance of

JComboBox

============ METHOD DETAIL ==========

- Method Detail

- show

```java
public void show()
```

Implementation of ComboPopup.show().

**Specified by:** show

in interface

ComboPopup
**Overrides:** show

in class

Component

- hide

```java
public void hide()
```

Implementation of ComboPopup.hide().

**Specified by:** hide

in interface

ComboPopup
**Overrides:** hide

in class

Component

- getList

```java
public
JList
<
Object
> getList()
```

Implementation of ComboPopup.getList().

**Specified by:** getList

in interface

ComboPopup
**Returns:** the list that is being used to draw the items in the combo box

- getMouseListener

```java
public
MouseListener
getMouseListener()
```

Implementation of ComboPopup.getMouseListener().

**Specified by:** getMouseListener

in interface

ComboPopup
**Returns:** a

MouseListener

or null
**See Also:** ComboPopup.getMouseListener()

- getMouseMotionListener

```java
public
MouseMotionListener
getMouseMotionListener()
```

Implementation of ComboPopup.getMouseMotionListener().

**Specified by:** getMouseMotionListener

in interface

ComboPopup
**Returns:** a

MouseMotionListener

or null
**See Also:** ComboPopup.getMouseMotionListener()

- getKeyListener

```java
public
KeyListener
getKeyListener()
```

Implementation of ComboPopup.getKeyListener().

**Specified by:** getKeyListener

in interface

ComboPopup
**Returns:** a

KeyListener

or null
**See Also:** ComboPopup.getKeyListener()

- uninstallingUI

```java
public void uninstallingUI()
```

Called when the UI is uninstalling. Since this popup isn't in the component
tree, it won't get it's uninstallUI() called. It removes the listeners that
were added in addComboBoxListeners().

**Specified by:** uninstallingUI

in interface

ComboPopup

- uninstallComboBoxModelListeners

```java
protected void uninstallComboBoxModelListeners​(
ComboBoxModel
<?> model)
```

Removes the listeners from the combo box model

**Parameters:** model

- The combo box model to install listeners
**See Also:** installComboBoxModelListeners(javax.swing.ComboBoxModel<?>)

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

- createMouseListener

```java
protected
MouseListener
createMouseListener()
```

Creates a listener
that will watch for mouse-press and release events on the combo box.

Warning:

When overriding this method, make sure to maintain the existing
behavior.

**Returns:** a

MouseListener

which will be added to
the combo box or null

- createMouseMotionListener

```java
protected
MouseMotionListener
createMouseMotionListener()
```

Creates the mouse motion listener which will be added to the combo
box.

Warning:

When overriding this method, make sure to maintain the existing
behavior.

**Returns:** a

MouseMotionListener

which will be added to
the combo box or null

- createKeyListener

```java
protected
KeyListener
createKeyListener()
```

Creates the key listener that will be added to the combo box. If
this method returns null then it will not be added to the combo box.

**Returns:** a

KeyListener

or null

- createListSelectionListener

```java
protected
ListSelectionListener
createListSelectionListener()
```

Creates a list selection listener that watches for selection changes in
the popup's list. If this method returns null then it will not
be added to the popup list.

**Returns:** an instance of a

ListSelectionListener

or null

- createListDataListener

```java
protected
ListDataListener
createListDataListener()
```

Creates a list data listener which will be added to the

ComboBoxModel

. If this method returns null then
it will not be added to the combo box model.

**Returns:** an instance of a

ListDataListener

or null

- createListMouseListener

```java
protected
MouseListener
createListMouseListener()
```

Creates a mouse listener that watches for mouse events in
the popup's list. If this method returns null then it will
not be added to the combo box.

**Returns:** an instance of a

MouseListener

or null

- createListMouseMotionListener

```java
protected
MouseMotionListener
createListMouseMotionListener()
```

Creates a mouse motion listener that watches for mouse motion
events in the popup's list. If this method returns null then it will
not be added to the combo box.

**Returns:** an instance of a

MouseMotionListener

or null

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates a

PropertyChangeListener

which will be added to
the combo box. If this method returns null then it will not
be added to the combo box.

**Returns:** an instance of a

PropertyChangeListener

or null

- createItemListener

```java
protected
ItemListener
createItemListener()
```

Creates an

ItemListener

which will be added to the
combo box. If this method returns null then it will not
be added to the combo box.

Subclasses may override this method to return instances of their own
ItemEvent handlers.

**Returns:** an instance of an

ItemListener

or null

- createList

```java
protected
JList
<
Object
> createList()
```

Creates the JList used in the popup to display
the items in the combo box model. This method is called when the UI class
is created.

**Returns:** a

JList

used to display the combo box items

- configureList

```java
protected void configureList()
```

Configures the list which is used to hold the combo box items in the
popup. This method is called when the UI class
is created.

**See Also:** createList()

- installListListeners

```java
protected void installListListeners()
```

Adds the listeners to the list control.

- createScroller

```java
protected
JScrollPane
createScroller()
```

Creates the scroll pane which houses the scrollable list.

**Returns:** the scroll pane which houses the scrollable list

- configureScroller

```java
protected void configureScroller()
```

Configures the scrollable portion which holds the list within
the combo box popup. This method is called when the UI class
is created.

- configurePopup

```java
protected void configurePopup()
```

Configures the popup portion of the combo box. This method is called
when the UI class is created.

- installComboBoxListeners

```java
protected void installComboBoxListeners()
```

This method adds the necessary listeners to the JComboBox.

- installComboBoxModelListeners

```java
protected void installComboBoxModelListeners​(
ComboBoxModel
<?> model)
```

Installs the listeners on the combo box model. Any listeners installed
on the combo box model should be removed in

uninstallComboBoxModelListeners

.

**Parameters:** model

- The combo box model to install listeners
**See Also:** uninstallComboBoxModelListeners(javax.swing.ComboBoxModel<?>)

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Registers keyboard actions.

- isFocusTraversable

```java
public boolean isFocusTraversable()
```

Overridden to unconditionally return false.

**Overrides:** isFocusTraversable

in class

Component
**Returns:** true

if this

Component

is
focusable;

false

otherwise
**See Also:** Component.setFocusable(boolean)

- startAutoScrolling

```java
protected void startAutoScrolling​(int direction)
```

This protected method is implementation specific and should be private.
do not call or override.

**Parameters:** direction

- the direction of scrolling

- stopAutoScrolling

```java
protected void stopAutoScrolling()
```

This protected method is implementation specific and should be private.
do not call or override.

- autoScrollUp

```java
protected void autoScrollUp()
```

This protected method is implementation specific and should be private.
do not call or override.

- autoScrollDown

```java
protected void autoScrollDown()
```

This protected method is implementation specific and should be private.
do not call or override.

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this BasicComboPopup.
The AccessibleContext will have its parent set to the ComboBox.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

JPopupMenu
**Returns:** an AccessibleContext for the BasicComboPopup
**Since:** 1.5

- delegateFocus

```java
protected void delegateFocus​(
MouseEvent
e)
```

This is a utility method that helps event handlers figure out where to
send the focus when the popup is brought up. The standard implementation
delegates the focus to the editor (if the combo box is editable) or to
the JComboBox if it is not editable.

**Parameters:** e

- a mouse event

- togglePopup

```java
protected void togglePopup()
```

Makes the popup visible if it is hidden and makes it hidden if it is
visible.

- convertMouseEvent

```java
protected
MouseEvent
convertMouseEvent​(
MouseEvent
e)
```

Converts mouse event.

**Parameters:** e

- a mouse event
**Returns:** converted mouse event

- getPopupHeightForRowCount

```java
protected int getPopupHeightForRowCount​(int maxRowCount)
```

Retrieves the height of the popup based on the current
ListCellRenderer and the maximum row count.

**Parameters:** maxRowCount

- the row count
**Returns:** the height of the popup

- computePopupBounds

```java
protected
Rectangle
computePopupBounds​(int px,
int py,
int pw,
int ph)
```

Calculate the placement and size of the popup portion of the combo box based
on the combo box location and the enclosing screen bounds. If
no transformations are required, then the returned rectangle will
have the same values as the parameters.

**Parameters:** px

- starting x location
**Parameters:** py

- starting y location
**Parameters:** pw

- starting width
**Parameters:** ph

- starting height
**Returns:** a rectangle which represents the placement and size of the popup

- updateListBoxSelectionForEvent

```java
protected void updateListBoxSelectionForEvent​(
MouseEvent
anEvent,
boolean shouldScroll)
```

A utility method used by the event listeners. Given a mouse event, it changes
the list selection to the list item below the mouse.

**Parameters:** anEvent

- a mouse event
**Parameters:** shouldScroll

- if

true

list should be scrolled.

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

- list

```java
protected
JList
<
Object
> list
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** getList()

,

createList()

- scroller

```java
protected
JScrollPane
scroller
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

**See Also:** createScroller()

- valueIsAdjusting

```java
protected boolean valueIsAdjusting
```

As of Java 2 platform v1.4 this previously undocumented field is no
longer used.

- mouseMotionListener

```java
protected
MouseMotionListener
mouseMotionListener
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor or create methods instead.

**See Also:** getMouseMotionListener()

,

createMouseMotionListener()

- mouseListener

```java
protected
MouseListener
mouseListener
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor or create methods instead.

**See Also:** getMouseListener()

,

createMouseListener()

- keyListener

```java
protected
KeyListener
keyListener
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor or create methods instead.

**See Also:** getKeyListener()

,

createKeyListener()

- listSelectionListener

```java
protected
ListSelectionListener
listSelectionListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead.

**See Also:** createListSelectionListener()

- listMouseListener

```java
protected
MouseListener
listMouseListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead.

**See Also:** createListMouseListener()

- listMouseMotionListener

```java
protected
MouseMotionListener
listMouseMotionListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

**See Also:** createListMouseMotionListener()

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

**See Also:** createPropertyChangeListener()

- listDataListener

```java
protected
ListDataListener
listDataListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

**See Also:** createListDataListener()

- itemListener

```java
protected
ItemListener
itemListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

**See Also:** createItemListener()

- autoscrollTimer

```java
protected
Timer
autoscrollTimer
```

This protected field is implementation specific. Do not access directly
or override.

- hasEntered

```java
protected boolean hasEntered
```

true

if the mouse cursor is in the popup.

- isAutoScrolling

```java
protected boolean isAutoScrolling
```

If

true

the auto-scrolling is enabled.

- scrollDirection

```java
protected int scrollDirection
```

The direction of scrolling.

- SCROLL_UP

```java
protected static final int SCROLL_UP
```

The direction of scrolling up.

**See Also:** Constant Field Values

- SCROLL_DOWN

```java
protected static final int SCROLL_DOWN
```

The direction of scrolling down.

**See Also:** Constant Field Values

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

list

```java
protected
JList
<
Object
> list
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** getList()

,

createList()

---

#### list

protected

JList

<

Object

> list

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

scroller

```java
protected
JScrollPane
scroller
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

**See Also:** createScroller()

---

#### scroller

protected

JScrollPane

scroller

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

valueIsAdjusting

```java
protected boolean valueIsAdjusting
```

As of Java 2 platform v1.4 this previously undocumented field is no
longer used.

---

#### valueIsAdjusting

protected boolean valueIsAdjusting

As of Java 2 platform v1.4 this previously undocumented field is no
longer used.

mouseMotionListener

```java
protected
MouseMotionListener
mouseMotionListener
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor or create methods instead.

**See Also:** getMouseMotionListener()

,

createMouseMotionListener()

---

#### mouseMotionListener

protected

MouseMotionListener

mouseMotionListener

This protected field is implementation specific. Do not access directly
or override. Use the accessor or create methods instead.

mouseListener

```java
protected
MouseListener
mouseListener
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor or create methods instead.

**See Also:** getMouseListener()

,

createMouseListener()

---

#### mouseListener

protected

MouseListener

mouseListener

This protected field is implementation specific. Do not access directly
or override. Use the accessor or create methods instead.

keyListener

```java
protected
KeyListener
keyListener
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor or create methods instead.

**See Also:** getKeyListener()

,

createKeyListener()

---

#### keyListener

protected

KeyListener

keyListener

This protected field is implementation specific. Do not access directly
or override. Use the accessor or create methods instead.

listSelectionListener

```java
protected
ListSelectionListener
listSelectionListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead.

**See Also:** createListSelectionListener()

---

#### listSelectionListener

protected

ListSelectionListener

listSelectionListener

This protected field is implementation specific. Do not access directly
or override. Use the create method instead.

listMouseListener

```java
protected
MouseListener
listMouseListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead.

**See Also:** createListMouseListener()

---

#### listMouseListener

protected

MouseListener

listMouseListener

This protected field is implementation specific. Do not access directly
or override. Use the create method instead.

listMouseMotionListener

```java
protected
MouseMotionListener
listMouseMotionListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

**See Also:** createListMouseMotionListener()

---

#### listMouseMotionListener

protected

MouseMotionListener

listMouseMotionListener

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

**See Also:** createPropertyChangeListener()

---

#### propertyChangeListener

protected

PropertyChangeListener

propertyChangeListener

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

listDataListener

```java
protected
ListDataListener
listDataListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

**See Also:** createListDataListener()

---

#### listDataListener

protected

ListDataListener

listDataListener

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

itemListener

```java
protected
ItemListener
itemListener
```

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

**See Also:** createItemListener()

---

#### itemListener

protected

ItemListener

itemListener

This protected field is implementation specific. Do not access directly
or override. Use the create method instead

autoscrollTimer

```java
protected
Timer
autoscrollTimer
```

This protected field is implementation specific. Do not access directly
or override.

---

#### autoscrollTimer

protected

Timer

autoscrollTimer

This protected field is implementation specific. Do not access directly
or override.

hasEntered

```java
protected boolean hasEntered
```

true

if the mouse cursor is in the popup.

---

#### hasEntered

protected boolean hasEntered

true

if the mouse cursor is in the popup.

isAutoScrolling

```java
protected boolean isAutoScrolling
```

If

true

the auto-scrolling is enabled.

---

#### isAutoScrolling

protected boolean isAutoScrolling

If

true

the auto-scrolling is enabled.

scrollDirection

```java
protected int scrollDirection
```

The direction of scrolling.

---

#### scrollDirection

protected int scrollDirection

The direction of scrolling.

SCROLL_UP

```java
protected static final int SCROLL_UP
```

The direction of scrolling up.

**See Also:** Constant Field Values

---

#### SCROLL_UP

protected static final int SCROLL_UP

The direction of scrolling up.

SCROLL_DOWN

```java
protected static final int SCROLL_DOWN
```

The direction of scrolling down.

**See Also:** Constant Field Values

---

#### SCROLL_DOWN

protected static final int SCROLL_DOWN

The direction of scrolling down.

Constructor Detail

- BasicComboPopup

```java
public BasicComboPopup​(
JComboBox
<
Object
> combo)
```

Constructs a new instance of

BasicComboPopup

.

**Parameters:** combo

- an instance of

JComboBox

---

#### Constructor Detail

BasicComboPopup

```java
public BasicComboPopup​(
JComboBox
<
Object
> combo)
```

Constructs a new instance of

BasicComboPopup

.

**Parameters:** combo

- an instance of

JComboBox

---

#### BasicComboPopup

public BasicComboPopup​(

JComboBox

<

Object

> combo)

Constructs a new instance of

BasicComboPopup

.

Method Detail

- show

```java
public void show()
```

Implementation of ComboPopup.show().

**Specified by:** show

in interface

ComboPopup
**Overrides:** show

in class

Component

- hide

```java
public void hide()
```

Implementation of ComboPopup.hide().

**Specified by:** hide

in interface

ComboPopup
**Overrides:** hide

in class

Component

- getList

```java
public
JList
<
Object
> getList()
```

Implementation of ComboPopup.getList().

**Specified by:** getList

in interface

ComboPopup
**Returns:** the list that is being used to draw the items in the combo box

- getMouseListener

```java
public
MouseListener
getMouseListener()
```

Implementation of ComboPopup.getMouseListener().

**Specified by:** getMouseListener

in interface

ComboPopup
**Returns:** a

MouseListener

or null
**See Also:** ComboPopup.getMouseListener()

- getMouseMotionListener

```java
public
MouseMotionListener
getMouseMotionListener()
```

Implementation of ComboPopup.getMouseMotionListener().

**Specified by:** getMouseMotionListener

in interface

ComboPopup
**Returns:** a

MouseMotionListener

or null
**See Also:** ComboPopup.getMouseMotionListener()

- getKeyListener

```java
public
KeyListener
getKeyListener()
```

Implementation of ComboPopup.getKeyListener().

**Specified by:** getKeyListener

in interface

ComboPopup
**Returns:** a

KeyListener

or null
**See Also:** ComboPopup.getKeyListener()

- uninstallingUI

```java
public void uninstallingUI()
```

Called when the UI is uninstalling. Since this popup isn't in the component
tree, it won't get it's uninstallUI() called. It removes the listeners that
were added in addComboBoxListeners().

**Specified by:** uninstallingUI

in interface

ComboPopup

- uninstallComboBoxModelListeners

```java
protected void uninstallComboBoxModelListeners​(
ComboBoxModel
<?> model)
```

Removes the listeners from the combo box model

**Parameters:** model

- The combo box model to install listeners
**See Also:** installComboBoxModelListeners(javax.swing.ComboBoxModel<?>)

- uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

- createMouseListener

```java
protected
MouseListener
createMouseListener()
```

Creates a listener
that will watch for mouse-press and release events on the combo box.

Warning:

When overriding this method, make sure to maintain the existing
behavior.

**Returns:** a

MouseListener

which will be added to
the combo box or null

- createMouseMotionListener

```java
protected
MouseMotionListener
createMouseMotionListener()
```

Creates the mouse motion listener which will be added to the combo
box.

Warning:

When overriding this method, make sure to maintain the existing
behavior.

**Returns:** a

MouseMotionListener

which will be added to
the combo box or null

- createKeyListener

```java
protected
KeyListener
createKeyListener()
```

Creates the key listener that will be added to the combo box. If
this method returns null then it will not be added to the combo box.

**Returns:** a

KeyListener

or null

- createListSelectionListener

```java
protected
ListSelectionListener
createListSelectionListener()
```

Creates a list selection listener that watches for selection changes in
the popup's list. If this method returns null then it will not
be added to the popup list.

**Returns:** an instance of a

ListSelectionListener

or null

- createListDataListener

```java
protected
ListDataListener
createListDataListener()
```

Creates a list data listener which will be added to the

ComboBoxModel

. If this method returns null then
it will not be added to the combo box model.

**Returns:** an instance of a

ListDataListener

or null

- createListMouseListener

```java
protected
MouseListener
createListMouseListener()
```

Creates a mouse listener that watches for mouse events in
the popup's list. If this method returns null then it will
not be added to the combo box.

**Returns:** an instance of a

MouseListener

or null

- createListMouseMotionListener

```java
protected
MouseMotionListener
createListMouseMotionListener()
```

Creates a mouse motion listener that watches for mouse motion
events in the popup's list. If this method returns null then it will
not be added to the combo box.

**Returns:** an instance of a

MouseMotionListener

or null

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates a

PropertyChangeListener

which will be added to
the combo box. If this method returns null then it will not
be added to the combo box.

**Returns:** an instance of a

PropertyChangeListener

or null

- createItemListener

```java
protected
ItemListener
createItemListener()
```

Creates an

ItemListener

which will be added to the
combo box. If this method returns null then it will not
be added to the combo box.

Subclasses may override this method to return instances of their own
ItemEvent handlers.

**Returns:** an instance of an

ItemListener

or null

- createList

```java
protected
JList
<
Object
> createList()
```

Creates the JList used in the popup to display
the items in the combo box model. This method is called when the UI class
is created.

**Returns:** a

JList

used to display the combo box items

- configureList

```java
protected void configureList()
```

Configures the list which is used to hold the combo box items in the
popup. This method is called when the UI class
is created.

**See Also:** createList()

- installListListeners

```java
protected void installListListeners()
```

Adds the listeners to the list control.

- createScroller

```java
protected
JScrollPane
createScroller()
```

Creates the scroll pane which houses the scrollable list.

**Returns:** the scroll pane which houses the scrollable list

- configureScroller

```java
protected void configureScroller()
```

Configures the scrollable portion which holds the list within
the combo box popup. This method is called when the UI class
is created.

- configurePopup

```java
protected void configurePopup()
```

Configures the popup portion of the combo box. This method is called
when the UI class is created.

- installComboBoxListeners

```java
protected void installComboBoxListeners()
```

This method adds the necessary listeners to the JComboBox.

- installComboBoxModelListeners

```java
protected void installComboBoxModelListeners​(
ComboBoxModel
<?> model)
```

Installs the listeners on the combo box model. Any listeners installed
on the combo box model should be removed in

uninstallComboBoxModelListeners

.

**Parameters:** model

- The combo box model to install listeners
**See Also:** uninstallComboBoxModelListeners(javax.swing.ComboBoxModel<?>)

- installKeyboardActions

```java
protected void installKeyboardActions()
```

Registers keyboard actions.

- isFocusTraversable

```java
public boolean isFocusTraversable()
```

Overridden to unconditionally return false.

**Overrides:** isFocusTraversable

in class

Component
**Returns:** true

if this

Component

is
focusable;

false

otherwise
**See Also:** Component.setFocusable(boolean)

- startAutoScrolling

```java
protected void startAutoScrolling​(int direction)
```

This protected method is implementation specific and should be private.
do not call or override.

**Parameters:** direction

- the direction of scrolling

- stopAutoScrolling

```java
protected void stopAutoScrolling()
```

This protected method is implementation specific and should be private.
do not call or override.

- autoScrollUp

```java
protected void autoScrollUp()
```

This protected method is implementation specific and should be private.
do not call or override.

- autoScrollDown

```java
protected void autoScrollDown()
```

This protected method is implementation specific and should be private.
do not call or override.

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this BasicComboPopup.
The AccessibleContext will have its parent set to the ComboBox.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

JPopupMenu
**Returns:** an AccessibleContext for the BasicComboPopup
**Since:** 1.5

- delegateFocus

```java
protected void delegateFocus​(
MouseEvent
e)
```

This is a utility method that helps event handlers figure out where to
send the focus when the popup is brought up. The standard implementation
delegates the focus to the editor (if the combo box is editable) or to
the JComboBox if it is not editable.

**Parameters:** e

- a mouse event

- togglePopup

```java
protected void togglePopup()
```

Makes the popup visible if it is hidden and makes it hidden if it is
visible.

- convertMouseEvent

```java
protected
MouseEvent
convertMouseEvent​(
MouseEvent
e)
```

Converts mouse event.

**Parameters:** e

- a mouse event
**Returns:** converted mouse event

- getPopupHeightForRowCount

```java
protected int getPopupHeightForRowCount​(int maxRowCount)
```

Retrieves the height of the popup based on the current
ListCellRenderer and the maximum row count.

**Parameters:** maxRowCount

- the row count
**Returns:** the height of the popup

- computePopupBounds

```java
protected
Rectangle
computePopupBounds​(int px,
int py,
int pw,
int ph)
```

Calculate the placement and size of the popup portion of the combo box based
on the combo box location and the enclosing screen bounds. If
no transformations are required, then the returned rectangle will
have the same values as the parameters.

**Parameters:** px

- starting x location
**Parameters:** py

- starting y location
**Parameters:** pw

- starting width
**Parameters:** ph

- starting height
**Returns:** a rectangle which represents the placement and size of the popup

- updateListBoxSelectionForEvent

```java
protected void updateListBoxSelectionForEvent​(
MouseEvent
anEvent,
boolean shouldScroll)
```

A utility method used by the event listeners. Given a mouse event, it changes
the list selection to the list item below the mouse.

**Parameters:** anEvent

- a mouse event
**Parameters:** shouldScroll

- if

true

list should be scrolled.

---

#### Method Detail

show

```java
public void show()
```

Implementation of ComboPopup.show().

**Specified by:** show

in interface

ComboPopup
**Overrides:** show

in class

Component

---

#### show

public void show()

Implementation of ComboPopup.show().

hide

```java
public void hide()
```

Implementation of ComboPopup.hide().

**Specified by:** hide

in interface

ComboPopup
**Overrides:** hide

in class

Component

---

#### hide

public void hide()

Implementation of ComboPopup.hide().

getList

```java
public
JList
<
Object
> getList()
```

Implementation of ComboPopup.getList().

**Specified by:** getList

in interface

ComboPopup
**Returns:** the list that is being used to draw the items in the combo box

---

#### getList

public

JList

<

Object

> getList()

Implementation of ComboPopup.getList().

getMouseListener

```java
public
MouseListener
getMouseListener()
```

Implementation of ComboPopup.getMouseListener().

**Specified by:** getMouseListener

in interface

ComboPopup
**Returns:** a

MouseListener

or null
**See Also:** ComboPopup.getMouseListener()

---

#### getMouseListener

public

MouseListener

getMouseListener()

Implementation of ComboPopup.getMouseListener().

getMouseMotionListener

```java
public
MouseMotionListener
getMouseMotionListener()
```

Implementation of ComboPopup.getMouseMotionListener().

**Specified by:** getMouseMotionListener

in interface

ComboPopup
**Returns:** a

MouseMotionListener

or null
**See Also:** ComboPopup.getMouseMotionListener()

---

#### getMouseMotionListener

public

MouseMotionListener

getMouseMotionListener()

Implementation of ComboPopup.getMouseMotionListener().

getKeyListener

```java
public
KeyListener
getKeyListener()
```

Implementation of ComboPopup.getKeyListener().

**Specified by:** getKeyListener

in interface

ComboPopup
**Returns:** a

KeyListener

or null
**See Also:** ComboPopup.getKeyListener()

---

#### getKeyListener

public

KeyListener

getKeyListener()

Implementation of ComboPopup.getKeyListener().

uninstallingUI

```java
public void uninstallingUI()
```

Called when the UI is uninstalling. Since this popup isn't in the component
tree, it won't get it's uninstallUI() called. It removes the listeners that
were added in addComboBoxListeners().

**Specified by:** uninstallingUI

in interface

ComboPopup

---

#### uninstallingUI

public void uninstallingUI()

Called when the UI is uninstalling. Since this popup isn't in the component
tree, it won't get it's uninstallUI() called. It removes the listeners that
were added in addComboBoxListeners().

uninstallComboBoxModelListeners

```java
protected void uninstallComboBoxModelListeners​(
ComboBoxModel
<?> model)
```

Removes the listeners from the combo box model

**Parameters:** model

- The combo box model to install listeners
**See Also:** installComboBoxModelListeners(javax.swing.ComboBoxModel<?>)

---

#### uninstallComboBoxModelListeners

protected void uninstallComboBoxModelListeners​(

ComboBoxModel

<?> model)

Removes the listeners from the combo box model

uninstallKeyboardActions

```java
protected void uninstallKeyboardActions()
```

Unregisters keyboard actions.

---

#### uninstallKeyboardActions

protected void uninstallKeyboardActions()

Unregisters keyboard actions.

createMouseListener

```java
protected
MouseListener
createMouseListener()
```

Creates a listener
that will watch for mouse-press and release events on the combo box.

Warning:

When overriding this method, make sure to maintain the existing
behavior.

**Returns:** a

MouseListener

which will be added to
the combo box or null

---

#### createMouseListener

protected

MouseListener

createMouseListener()

Creates a listener
that will watch for mouse-press and release events on the combo box.

Warning:

When overriding this method, make sure to maintain the existing
behavior.

createMouseMotionListener

```java
protected
MouseMotionListener
createMouseMotionListener()
```

Creates the mouse motion listener which will be added to the combo
box.

Warning:

When overriding this method, make sure to maintain the existing
behavior.

**Returns:** a

MouseMotionListener

which will be added to
the combo box or null

---

#### createMouseMotionListener

protected

MouseMotionListener

createMouseMotionListener()

Creates the mouse motion listener which will be added to the combo
box.

Warning:

When overriding this method, make sure to maintain the existing
behavior.

createKeyListener

```java
protected
KeyListener
createKeyListener()
```

Creates the key listener that will be added to the combo box. If
this method returns null then it will not be added to the combo box.

**Returns:** a

KeyListener

or null

---

#### createKeyListener

protected

KeyListener

createKeyListener()

Creates the key listener that will be added to the combo box. If
this method returns null then it will not be added to the combo box.

createListSelectionListener

```java
protected
ListSelectionListener
createListSelectionListener()
```

Creates a list selection listener that watches for selection changes in
the popup's list. If this method returns null then it will not
be added to the popup list.

**Returns:** an instance of a

ListSelectionListener

or null

---

#### createListSelectionListener

protected

ListSelectionListener

createListSelectionListener()

Creates a list selection listener that watches for selection changes in
the popup's list. If this method returns null then it will not
be added to the popup list.

createListDataListener

```java
protected
ListDataListener
createListDataListener()
```

Creates a list data listener which will be added to the

ComboBoxModel

. If this method returns null then
it will not be added to the combo box model.

**Returns:** an instance of a

ListDataListener

or null

---

#### createListDataListener

protected

ListDataListener

createListDataListener()

Creates a list data listener which will be added to the

ComboBoxModel

. If this method returns null then
it will not be added to the combo box model.

createListMouseListener

```java
protected
MouseListener
createListMouseListener()
```

Creates a mouse listener that watches for mouse events in
the popup's list. If this method returns null then it will
not be added to the combo box.

**Returns:** an instance of a

MouseListener

or null

---

#### createListMouseListener

protected

MouseListener

createListMouseListener()

Creates a mouse listener that watches for mouse events in
the popup's list. If this method returns null then it will
not be added to the combo box.

createListMouseMotionListener

```java
protected
MouseMotionListener
createListMouseMotionListener()
```

Creates a mouse motion listener that watches for mouse motion
events in the popup's list. If this method returns null then it will
not be added to the combo box.

**Returns:** an instance of a

MouseMotionListener

or null

---

#### createListMouseMotionListener

protected

MouseMotionListener

createListMouseMotionListener()

Creates a mouse motion listener that watches for mouse motion
events in the popup's list. If this method returns null then it will
not be added to the combo box.

createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Creates a

PropertyChangeListener

which will be added to
the combo box. If this method returns null then it will not
be added to the combo box.

**Returns:** an instance of a

PropertyChangeListener

or null

---

#### createPropertyChangeListener

protected

PropertyChangeListener

createPropertyChangeListener()

Creates a

PropertyChangeListener

which will be added to
the combo box. If this method returns null then it will not
be added to the combo box.

createItemListener

```java
protected
ItemListener
createItemListener()
```

Creates an

ItemListener

which will be added to the
combo box. If this method returns null then it will not
be added to the combo box.

Subclasses may override this method to return instances of their own
ItemEvent handlers.

**Returns:** an instance of an

ItemListener

or null

---

#### createItemListener

protected

ItemListener

createItemListener()

Creates an

ItemListener

which will be added to the
combo box. If this method returns null then it will not
be added to the combo box.

Subclasses may override this method to return instances of their own
ItemEvent handlers.

Subclasses may override this method to return instances of their own
ItemEvent handlers.

createList

```java
protected
JList
<
Object
> createList()
```

Creates the JList used in the popup to display
the items in the combo box model. This method is called when the UI class
is created.

**Returns:** a

JList

used to display the combo box items

---

#### createList

protected

JList

<

Object

> createList()

Creates the JList used in the popup to display
the items in the combo box model. This method is called when the UI class
is created.

configureList

```java
protected void configureList()
```

Configures the list which is used to hold the combo box items in the
popup. This method is called when the UI class
is created.

**See Also:** createList()

---

#### configureList

protected void configureList()

Configures the list which is used to hold the combo box items in the
popup. This method is called when the UI class
is created.

installListListeners

```java
protected void installListListeners()
```

Adds the listeners to the list control.

---

#### installListListeners

protected void installListListeners()

Adds the listeners to the list control.

createScroller

```java
protected
JScrollPane
createScroller()
```

Creates the scroll pane which houses the scrollable list.

**Returns:** the scroll pane which houses the scrollable list

---

#### createScroller

protected

JScrollPane

createScroller()

Creates the scroll pane which houses the scrollable list.

configureScroller

```java
protected void configureScroller()
```

Configures the scrollable portion which holds the list within
the combo box popup. This method is called when the UI class
is created.

---

#### configureScroller

protected void configureScroller()

Configures the scrollable portion which holds the list within
the combo box popup. This method is called when the UI class
is created.

configurePopup

```java
protected void configurePopup()
```

Configures the popup portion of the combo box. This method is called
when the UI class is created.

---

#### configurePopup

protected void configurePopup()

Configures the popup portion of the combo box. This method is called
when the UI class is created.

installComboBoxListeners

```java
protected void installComboBoxListeners()
```

This method adds the necessary listeners to the JComboBox.

---

#### installComboBoxListeners

protected void installComboBoxListeners()

This method adds the necessary listeners to the JComboBox.

installComboBoxModelListeners

```java
protected void installComboBoxModelListeners​(
ComboBoxModel
<?> model)
```

Installs the listeners on the combo box model. Any listeners installed
on the combo box model should be removed in

uninstallComboBoxModelListeners

.

**Parameters:** model

- The combo box model to install listeners
**See Also:** uninstallComboBoxModelListeners(javax.swing.ComboBoxModel<?>)

---

#### installComboBoxModelListeners

protected void installComboBoxModelListeners​(

ComboBoxModel

<?> model)

Installs the listeners on the combo box model. Any listeners installed
on the combo box model should be removed in

uninstallComboBoxModelListeners

.

installKeyboardActions

```java
protected void installKeyboardActions()
```

Registers keyboard actions.

---

#### installKeyboardActions

protected void installKeyboardActions()

Registers keyboard actions.

isFocusTraversable

```java
public boolean isFocusTraversable()
```

Overridden to unconditionally return false.

**Overrides:** isFocusTraversable

in class

Component
**Returns:** true

if this

Component

is
focusable;

false

otherwise
**See Also:** Component.setFocusable(boolean)

---

#### isFocusTraversable

public boolean isFocusTraversable()

Overridden to unconditionally return false.

startAutoScrolling

```java
protected void startAutoScrolling​(int direction)
```

This protected method is implementation specific and should be private.
do not call or override.

**Parameters:** direction

- the direction of scrolling

---

#### startAutoScrolling

protected void startAutoScrolling​(int direction)

This protected method is implementation specific and should be private.
do not call or override.

stopAutoScrolling

```java
protected void stopAutoScrolling()
```

This protected method is implementation specific and should be private.
do not call or override.

---

#### stopAutoScrolling

protected void stopAutoScrolling()

This protected method is implementation specific and should be private.
do not call or override.

autoScrollUp

```java
protected void autoScrollUp()
```

This protected method is implementation specific and should be private.
do not call or override.

---

#### autoScrollUp

protected void autoScrollUp()

This protected method is implementation specific and should be private.
do not call or override.

autoScrollDown

```java
protected void autoScrollDown()
```

This protected method is implementation specific and should be private.
do not call or override.

---

#### autoScrollDown

protected void autoScrollDown()

This protected method is implementation specific and should be private.
do not call or override.

getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the AccessibleContext associated with this BasicComboPopup.
The AccessibleContext will have its parent set to the ComboBox.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

JPopupMenu
**Returns:** an AccessibleContext for the BasicComboPopup
**Since:** 1.5

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this BasicComboPopup.
The AccessibleContext will have its parent set to the ComboBox.

delegateFocus

```java
protected void delegateFocus​(
MouseEvent
e)
```

This is a utility method that helps event handlers figure out where to
send the focus when the popup is brought up. The standard implementation
delegates the focus to the editor (if the combo box is editable) or to
the JComboBox if it is not editable.

**Parameters:** e

- a mouse event

---

#### delegateFocus

protected void delegateFocus​(

MouseEvent

e)

This is a utility method that helps event handlers figure out where to
send the focus when the popup is brought up. The standard implementation
delegates the focus to the editor (if the combo box is editable) or to
the JComboBox if it is not editable.

togglePopup

```java
protected void togglePopup()
```

Makes the popup visible if it is hidden and makes it hidden if it is
visible.

---

#### togglePopup

protected void togglePopup()

Makes the popup visible if it is hidden and makes it hidden if it is
visible.

convertMouseEvent

```java
protected
MouseEvent
convertMouseEvent​(
MouseEvent
e)
```

Converts mouse event.

**Parameters:** e

- a mouse event
**Returns:** converted mouse event

---

#### convertMouseEvent

protected

MouseEvent

convertMouseEvent​(

MouseEvent

e)

Converts mouse event.

getPopupHeightForRowCount

```java
protected int getPopupHeightForRowCount​(int maxRowCount)
```

Retrieves the height of the popup based on the current
ListCellRenderer and the maximum row count.

**Parameters:** maxRowCount

- the row count
**Returns:** the height of the popup

---

#### getPopupHeightForRowCount

protected int getPopupHeightForRowCount​(int maxRowCount)

Retrieves the height of the popup based on the current
ListCellRenderer and the maximum row count.

computePopupBounds

```java
protected
Rectangle
computePopupBounds​(int px,
int py,
int pw,
int ph)
```

Calculate the placement and size of the popup portion of the combo box based
on the combo box location and the enclosing screen bounds. If
no transformations are required, then the returned rectangle will
have the same values as the parameters.

**Parameters:** px

- starting x location
**Parameters:** py

- starting y location
**Parameters:** pw

- starting width
**Parameters:** ph

- starting height
**Returns:** a rectangle which represents the placement and size of the popup

---

#### computePopupBounds

protected

Rectangle

computePopupBounds​(int px,
int py,
int pw,
int ph)

Calculate the placement and size of the popup portion of the combo box based
on the combo box location and the enclosing screen bounds. If
no transformations are required, then the returned rectangle will
have the same values as the parameters.

updateListBoxSelectionForEvent

```java
protected void updateListBoxSelectionForEvent​(
MouseEvent
anEvent,
boolean shouldScroll)
```

A utility method used by the event listeners. Given a mouse event, it changes
the list selection to the list item below the mouse.

**Parameters:** anEvent

- a mouse event
**Parameters:** shouldScroll

- if

true

list should be scrolled.

---

#### updateListBoxSelectionForEvent

protected void updateListBoxSelectionForEvent​(

MouseEvent

anEvent,
boolean shouldScroll)

A utility method used by the event listeners. Given a mouse event, it changes
the list selection to the list item below the mouse.

---

