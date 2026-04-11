# Class JComboBox<E>

**Source:** `java.desktop\javax\swing\JComboBox.html`

### Class Description

```java
@JavaBean
(
defaultProperty
="UI",

description
="A combination of a text field and a drop-down list.")
public class
JComboBox<E>

extends
JComponent

implements
ItemSelectable
,
ListDataListener
,
ActionListener
,
Accessible
```

A component that combines a button or editable field and a drop-down list.
The user can select a value from the drop-down list, which appears at the
user's request. If you make the combo box editable, then the combo box
includes an editable field into which the user can type a value.

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

How to Use Combo Boxes

in

The Java Tutorial

for further information.

**Type Parameters:** E

- the type of the elements of this combo box

---

### Field Details

#### protected
ComboBoxModel
<
E
> dataModel

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:**
- getModel()

,

setModel(javax.swing.ComboBoxModel<E>)

---

#### protected
ListCellRenderer
<? super
E
> renderer

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:**
- getRenderer()

,

setRenderer(javax.swing.ListCellRenderer<? super E>)

---

#### protected
ComboBoxEditor
editor

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:**
- getEditor()

,

setEditor(javax.swing.ComboBoxEditor)

---

#### protected int maximumRowCount

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:**
- getMaximumRowCount()

,

setMaximumRowCount(int)

---

#### protected boolean isEditable

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:**
- isEditable

,

setEditable(boolean)

---

#### protected
JComboBox.KeySelectionManager
keySelectionManager

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:**
- setKeySelectionManager(javax.swing.JComboBox.KeySelectionManager)

,

getKeySelectionManager()

---

#### protected
String
actionCommand

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:**
- setActionCommand(java.lang.String)

,

getActionCommand()

---

#### protected boolean lightWeightPopupEnabled

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:**
- setLightWeightPopupEnabled(boolean)

,

isLightWeightPopupEnabled()

---

#### protected
Object
selectedItemReminder

This protected field is implementation specific. Do not access directly
or override.

---

### Constructor Details

#### public JComboBox​(
ComboBoxModel
<
E
> aModel)

Creates a

JComboBox

that takes its items from an
existing

ComboBoxModel

. Since the

ComboBoxModel

is provided, a combo box created using
this constructor does not create a default combo box model and
may impact how the insert, remove and add methods behave.

**Parameters:**
- aModel

- the

ComboBoxModel

that provides the
displayed list of items

**See Also:**
- DefaultComboBoxModel

---

#### public JComboBox​(
E
[] items)

Creates a

JComboBox

that contains the elements
in the specified array. By default the first item in the array
(and therefore the data model) becomes selected.

**Parameters:**
- items

- an array of objects to insert into the combo box

**See Also:**
- DefaultComboBoxModel

---

#### public JComboBox​(
Vector
<
E
> items)

Creates a

JComboBox

that contains the elements
in the specified Vector. By default the first item in the vector
(and therefore the data model) becomes selected.

**Parameters:**
- items

- an array of vectors to insert into the combo box

**See Also:**
- DefaultComboBoxModel

---

#### public JComboBox()

Creates a

JComboBox

with a default data model.
The default data model is an empty list of objects.
Use

addItem

to add items. By default the first item
in the data model becomes selected.

**See Also:**
- DefaultComboBoxModel

---

### Method Details

#### protected void installAncestorListener()

Registers ancestor listener so that it will receive

AncestorEvents

when it or any of its ancestors
move or are made visible or invisible.
Events are also sent when the component or its ancestors are added
or removed from the containment hierarchy.

---

#### @BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
ComboBoxUI
ui)

Sets the L&F object that renders this component.

**Parameters:**
- ui

- the

ComboBoxUI

L&F object

**See Also:**
- UIDefaults.getUI(javax.swing.JComponent)

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

JComponent

**Returns:**
- the string "ComboBoxUI"

**See Also:**
- JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

---

#### public
ComboBoxUI
getUI()

Returns the L&F object that renders this component.

**Overrides:**
- getUI

in class

JComponent

**Returns:**
- the ComboBoxUI object that renders this component

---

#### @BeanProperty
(
description
="Model that the combo box uses to get data to display.")
public void setModel​(
ComboBoxModel
<
E
> aModel)

Sets the data model that the

JComboBox

uses to obtain
the list of items.

**Parameters:**
- aModel

- the

ComboBoxModel

that provides the
displayed list of items

---

#### public
ComboBoxModel
<
E
> getModel()

Returns the data model currently used by the

JComboBox

.

**Returns:**
- the

ComboBoxModel

that provides the displayed
list of items

---

#### @BeanProperty
(
expert
=true,

description
="Set to <code>false</code> to require heavyweight popups.")
public void setLightWeightPopupEnabled​(boolean aFlag)

Sets the

lightWeightPopupEnabled

property, which
provides a hint as to whether or not a lightweight

Component

should be used to contain the

JComboBox

, versus a heavyweight

Component

such as a

Panel

or a

Window

. The decision of lightweight
versus heavyweight is ultimately up to the

JComboBox

. Lightweight windows are more
efficient than heavyweight windows, but lightweight
and heavyweight components do not mix well in a GUI.
If your application mixes lightweight and heavyweight
components, you should disable lightweight popups.
The default value for the

lightWeightPopupEnabled

property is

true

, unless otherwise specified
by the look and feel. Some look and feels always use
heavyweight popups, no matter what the value of this property.

See the article

Mixing Heavy and Light Components

This method fires a property changed event.

**Parameters:**
- aFlag

- if

true

, lightweight popups are desired

---

#### public boolean isLightWeightPopupEnabled()

Gets the value of the

lightWeightPopupEnabled

property.

**Returns:**
- the value of the

lightWeightPopupEnabled

property

**See Also:**
- setLightWeightPopupEnabled(boolean)

---

#### @BeanProperty
(
preferred
=true,

description
="If true, the user can type a new value in the combo box.")
public void setEditable​(boolean aFlag)

Determines whether the

JComboBox

field is editable.
An editable

JComboBox

allows the user to type into the
field or selected an item from the list to initialize the field,
after which it can be edited. (The editing affects only the field,
the list item remains intact.) A non editable

JComboBox

displays the selected item in the field,
but the selection cannot be modified.

**Parameters:**
- aFlag

- a boolean value, where true indicates that the
field is editable

---

#### public boolean isEditable()

Returns true if the

JComboBox

is editable.
By default, a combo box is not editable.

**Returns:**
- true if the

JComboBox

is editable, else false

---

#### @BeanProperty
(
preferred
=true,

description
="The maximum number of rows the popup should have")
public void setMaximumRowCount​(int count)

Sets the maximum number of rows the

JComboBox

displays.
If the number of objects in the model is greater than count,
the combo box uses a scrollbar.

**Parameters:**
- count

- an integer specifying the maximum number of items to
display in the list before using a scrollbar

---

#### public int getMaximumRowCount()

Returns the maximum number of items the combo box can display
without a scrollbar

**Returns:**
- an integer specifying the maximum number of items that are
displayed in the list before using a scrollbar

---

#### @BeanProperty
(
expert
=true,

description
="The renderer that paints the item selected in the list.")
public void setRenderer​(
ListCellRenderer
<? super
E
> aRenderer)

Sets the renderer that paints the list items and the item selected from the list in
the JComboBox field. The renderer is used if the JComboBox is not
editable. If it is editable, the editor is used to render and edit
the selected item.

The default renderer displays a string or an icon.
Other renderers can handle graphic images and composite items.

To display the selected item,

aRenderer.getListCellRendererComponent

is called, passing the list object and an index of -1.

**Parameters:**
- aRenderer

- the

ListCellRenderer

that
displays the selected item

**See Also:**
- setEditor(javax.swing.ComboBoxEditor)

---

#### public
ListCellRenderer
<? super
E
> getRenderer()

Returns the renderer used to display the selected item in the

JComboBox

field.

**Returns:**
- the

ListCellRenderer

that displays
the selected item.

---

#### @BeanProperty
(
expert
=true,

description
="The editor that combo box uses to edit the current value")
public void setEditor​(
ComboBoxEditor
anEditor)

Sets the editor used to paint and edit the selected item in the

JComboBox

field. The editor is used only if the
receiving

JComboBox

is editable. If not editable,
the combo box uses the renderer to paint the selected item.

**Parameters:**
- anEditor

- the

ComboBoxEditor

that
displays the selected item

**See Also:**
- setRenderer(javax.swing.ListCellRenderer<? super E>)

---

#### public
ComboBoxEditor
getEditor()

Returns the editor used to paint and edit the selected item in the

JComboBox

field.

**Returns:**
- the

ComboBoxEditor

that displays the selected item

---

#### @BeanProperty
(
bound
=false,

preferred
=true,

description
="Sets the selected item in the JComboBox.")
public void setSelectedItem​(
Object
anObject)

Sets the selected item in the combo box display area to the object in
the argument.
If

anObject

is in the list, the display area shows

anObject

selected.

If

anObject

is

not

in the list and the combo box is
uneditable, it will not change the current selection. For editable
combo boxes, the selection will change to

anObject

.

If this constitutes a change in the selected item,

ItemListener

s added to the combo box will be notified with
one or two

ItemEvent

s.
If there is a current selected item, an

ItemEvent

will be
fired and the state change will be

ItemEvent.DESELECTED

.
If

anObject

is in the list and is not currently selected
then an

ItemEvent

will be fired and the state change will
be

ItemEvent.SELECTED

.

ActionListener

s added to the combo box will be notified
with an

ActionEvent

when this method is called.

**Parameters:**
- anObject

- the list object to select; use

null

to
clear the selection

---

#### public
Object
getSelectedItem()

Returns the current selected item.

If the combo box is editable, then this value may not have been added
to the combo box with

addItem

,

insertItemAt

or the data constructors.

**Returns:**
- the current selected Object

**See Also:**
- setSelectedItem(java.lang.Object)

---

#### @BeanProperty
(
bound
=false,

preferred
=true,

description
="The item at index is selected.")
public void setSelectedIndex​(int anIndex)

Selects the item at index

anIndex

.

**Parameters:**
- anIndex

- an integer specifying the list item to select,
where 0 specifies the first item in the list and -1 indicates no selection

**Throws:**
- IllegalArgumentException

- if

anIndex

< -1 or

anIndex

is greater than or equal to size

---

#### public int getSelectedIndex()

Returns the first item in the list that matches the given item.
The result is not always defined if the

JComboBox

allows selected items that are not in the list.
Returns -1 if there is no selected item or if the user specified
an item which is not in the list.

**Returns:**
- an integer specifying the currently selected list item,
where 0 specifies
the first item in the list;
or -1 if no item is selected or if
the currently selected item is not in the list

---

#### public
E
getPrototypeDisplayValue()

Returns the "prototypical display" value - an Object used
for the calculation of the display height and width.

**Returns:**
- the value of the

prototypeDisplayValue

property

**See Also:**
- setPrototypeDisplayValue(E)

**Since:**
- 1.4

---

#### @BeanProperty
(
visualUpdate
=true,

description
="The display prototype value, used to compute display width and height.")
public void setPrototypeDisplayValue​(
E
prototypeDisplayValue)

Sets the prototype display value used to calculate the size of the display
for the UI portion.

If a prototype display value is specified, the preferred size of
the combo box is calculated by configuring the renderer with the
prototype display value and obtaining its preferred size. Specifying
the preferred display value is often useful when the combo box will be
displaying large amounts of data. If no prototype display value has
been specified, the renderer must be configured for each value from
the model and its preferred size obtained, which can be
relatively expensive.

**Parameters:**
- prototypeDisplayValue

- the prototype display value

**See Also:**
- getPrototypeDisplayValue()

**Since:**
- 1.4

---

#### public void addItem​(
E
item)

Adds an item to the item list.
This method works only if the

JComboBox

uses a
mutable data model.

Warning:

Focus and keyboard navigation problems may arise if you add duplicate
String objects. A workaround is to add new objects instead of String
objects and make sure that the toString() method is defined.
For example:

```java
comboBox.addItem(makeObj("Item 1"));
comboBox.addItem(makeObj("Item 1"));
...
private Object makeObj(final String item) {
return new Object() { public String toString() { return item; } };
}
```

**Parameters:**
- item

- the item to add to the list

**See Also:**
- MutableComboBoxModel

---

#### public void insertItemAt​(
E
item,
int index)

Inserts an item into the item list at a given index.
This method works only if the

JComboBox

uses a
mutable data model.

**Parameters:**
- item

- the item to add to the list
- index

- an integer specifying the position at which
to add the item

**See Also:**
- MutableComboBoxModel

---

#### public void removeItem​(
Object
anObject)

Removes an item from the item list.
This method works only if the

JComboBox

uses a
mutable data model.

**Parameters:**
- anObject

- the object to remove from the item list

**See Also:**
- MutableComboBoxModel

---

#### public void removeItemAt​(int anIndex)

Removes the item at

anIndex

This method works only if the

JComboBox

uses a
mutable data model.

**Parameters:**
- anIndex

- an int specifying the index of the item to remove,
where 0
indicates the first item in the list

**See Also:**
- MutableComboBoxModel

---

#### public void removeAllItems()

Removes all items from the item list.

---

#### public void showPopup()

Causes the combo box to display its popup window.

**See Also:**
- setPopupVisible(boolean)

---

#### public void hidePopup()

Causes the combo box to close its popup window.

**See Also:**
- setPopupVisible(boolean)

---

#### public void setPopupVisible​(boolean v)

Sets the visibility of the popup.

**Parameters:**
- v

- if

true

shows the popup, otherwise, hides the popup.

---

#### public boolean isPopupVisible()

Determines the visibility of the popup.

**Returns:**
- true if the popup is visible, otherwise returns false

---

#### public void addItemListener​(
ItemListener
aListener)

Adds an

ItemListener

.

aListener

will receive one or two

ItemEvent

s when
the selected item changes.

**Specified by:**
- addItemListener

in interface

ItemSelectable

**Parameters:**
- aListener

- the

ItemListener

that is to be notified

**See Also:**
- setSelectedItem(java.lang.Object)

---

#### public void removeItemListener​(
ItemListener
aListener)

Removes an

ItemListener

.

**Specified by:**
- removeItemListener

in interface

ItemSelectable

**Parameters:**
- aListener

- the

ItemListener

to remove

**See Also:**
- ItemEvent

---

#### @BeanProperty
(
bound
=false)
public
ItemListener
[] getItemListeners()

Returns an array of all the

ItemListener

s added
to this JComboBox with addItemListener().

**Returns:**
- all of the

ItemListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### public void addActionListener​(
ActionListener
l)

Adds an

ActionListener

.

The

ActionListener

will receive an

ActionEvent

when a selection has been made. If the combo box is editable, then
an

ActionEvent

will be fired when editing has stopped.

**Parameters:**
- l

- the

ActionListener

that is to be notified

**See Also:**
- setSelectedItem(java.lang.Object)

---

#### public void removeActionListener​(
ActionListener
l)

Removes an

ActionListener

.

**Parameters:**
- l

- the

ActionListener

to remove

---

#### @BeanProperty
(
bound
=false)
public
ActionListener
[] getActionListeners()

Returns an array of all the

ActionListener

s added
to this JComboBox with addActionListener().

**Returns:**
- all of the

ActionListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### public void addPopupMenuListener​(
PopupMenuListener
l)

Adds a

PopupMenu

listener which will listen to notification
messages from the popup portion of the combo box.

For all standard look and feels shipped with Java, the popup list
portion of combo box is implemented as a

JPopupMenu

.
A custom look and feel may not implement it this way and will
therefore not receive the notification.

**Parameters:**
- l

- the

PopupMenuListener

to add

**Since:**
- 1.4

---

#### public void removePopupMenuListener​(
PopupMenuListener
l)

Removes a

PopupMenuListener

.

**Parameters:**
- l

- the

PopupMenuListener

to remove

**See Also:**
- addPopupMenuListener(javax.swing.event.PopupMenuListener)

**Since:**
- 1.4

---

#### @BeanProperty
(
bound
=false)
public
PopupMenuListener
[] getPopupMenuListeners()

Returns an array of all the

PopupMenuListener

s added
to this JComboBox with addPopupMenuListener().

**Returns:**
- all of the

PopupMenuListener

s added or an empty
array if no listeners have been added

**Since:**
- 1.4

---

#### public void firePopupMenuWillBecomeVisible()

Notifies

PopupMenuListener

s that the popup portion of the
combo box will become visible.

This method is public but should not be called by anything other than
the UI delegate.

**See Also:**
- addPopupMenuListener(javax.swing.event.PopupMenuListener)

**Since:**
- 1.4

---

#### public void firePopupMenuWillBecomeInvisible()

Notifies

PopupMenuListener

s that the popup portion of the
combo box has become invisible.

This method is public but should not be called by anything other than
the UI delegate.

**See Also:**
- addPopupMenuListener(javax.swing.event.PopupMenuListener)

**Since:**
- 1.4

---

#### public void firePopupMenuCanceled()

Notifies

PopupMenuListener

s that the popup portion of the
combo box has been canceled.

This method is public but should not be called by anything other than
the UI delegate.

**See Also:**
- addPopupMenuListener(javax.swing.event.PopupMenuListener)

**Since:**
- 1.4

---

#### public void setActionCommand​(
String
aCommand)

Sets the action command that should be included in the event
sent to action listeners.

**Parameters:**
- aCommand

- a string containing the "command" that is sent
to action listeners; the same listener can then
do different things depending on the command it
receives

---

#### public
String
getActionCommand()

Returns the action command that is included in the event sent to
action listeners.

**Returns:**
- the string containing the "command" that is sent
to action listeners.

---

#### @BeanProperty
(
visualUpdate
=true,

description
="the Action instance connected with this ActionEvent source")
public void setAction​(
Action
a)

Sets the

Action

for the

ActionEvent

source.
The new

Action

replaces any previously set

Action

but does not affect

ActionListeners

independently added with

addActionListener

.
If the

Action

is already a registered

ActionListener

for the

ActionEvent

source,
it is not re-registered.

Setting the

Action

results in immediately changing
all the properties described in

Swing Components Supporting

Action

.
Subsequently, the combobox's properties are automatically updated
as the

Action

's properties change.

This method uses three other methods to set
and help track the

Action

's property values.
It uses the

configurePropertiesFromAction

method
to immediately change the combobox's properties.
To track changes in the

Action

's property values,
this method registers the

PropertyChangeListener

returned by

createActionPropertyChangeListener

. The
default

PropertyChangeListener

invokes the

actionPropertyChanged

method when a property in the

Action

changes.

**Parameters:**
- a

- the

Action

for the

JComboBox

,
or

null

.

**See Also:**
- Action

,

getAction()

,

configurePropertiesFromAction(javax.swing.Action)

,

createActionPropertyChangeListener(javax.swing.Action)

,

actionPropertyChanged(javax.swing.Action, java.lang.String)

**Since:**
- 1.3

---

#### public
Action
getAction()

Returns the currently set

Action

for this

ActionEvent

source, or

null

if no

Action

is set.

**Returns:**
- the

Action

for this

ActionEvent

source; or

null

**See Also:**
- Action

,

setAction(javax.swing.Action)

**Since:**
- 1.3

---

#### protected void configurePropertiesFromAction​(
Action
a)

Sets the properties on this combobox to match those in the specified

Action

. Refer to

Swing Components Supporting

Action

for more
details as to which properties this sets.

**Parameters:**
- a

- the

Action

from which to get the properties,
or

null

**See Also:**
- Action

,

setAction(javax.swing.Action)

**Since:**
- 1.3

---

#### protected
PropertyChangeListener
createActionPropertyChangeListener​(
Action
a)

Creates and returns a

PropertyChangeListener

that is
responsible for listening for changes from the specified

Action

and updating the appropriate properties.

Warning:

If you subclass this do not create an anonymous
inner class. If you do the lifetime of the combobox will be tied to
that of the

Action

.

**Parameters:**
- a

- the combobox's action

**Returns:**
- the

PropertyChangeListener

**See Also:**
- Action

,

setAction(javax.swing.Action)

**Since:**
- 1.3

---

#### protected void actionPropertyChanged​(
Action
action,

String
propertyName)

Updates the combobox's state in response to property changes in
associated action. This method is invoked from the

PropertyChangeListener

returned from

createActionPropertyChangeListener

. Subclasses do not normally
need to invoke this. Subclasses that support additional

Action

properties should override this and

configurePropertiesFromAction

.

Refer to the table at

Swing Components Supporting

Action

for a list of
the properties this method sets.

**Parameters:**
- action

- the

Action

associated with this combobox
- propertyName

- the name of the property that changed

**See Also:**
- Action

,

configurePropertiesFromAction(javax.swing.Action)

**Since:**
- 1.6

---

#### protected void fireItemStateChanged​(
ItemEvent
e)

Notifies all listeners that have registered interest for
notification on this event type.

**Parameters:**
- e

- the event of interest

**See Also:**
- EventListenerList

---

#### protected void fireActionEvent()

Notifies all listeners that have registered interest for
notification on this event type.

**See Also:**
- EventListenerList

---

#### protected void selectedItemChanged()

This protected method is implementation specific. Do not access directly
or override.

---

#### @BeanProperty
(
bound
=false)
public
Object
[] getSelectedObjects()

Returns an array containing the selected item.
This method is implemented for compatibility with

ItemSelectable

.

**Specified by:**
- getSelectedObjects

in interface

ItemSelectable

**Returns:**
- an array of

Objects

containing one
element -- the selected item

---

#### public void actionPerformed​(
ActionEvent
e)

This method is public as an implementation side effect.
do not call or override.

**Specified by:**
- actionPerformed

in interface

ActionListener

**Parameters:**
- e

- the event to be processed

---

#### public void contentsChanged​(
ListDataEvent
e)

This method is public as an implementation side effect.
do not call or override.

**Specified by:**
- contentsChanged

in interface

ListDataListener

**Parameters:**
- e

- a

ListDataEvent

encapsulating the
event information

---

#### public void intervalAdded​(
ListDataEvent
e)

This method is public as an implementation side effect.
do not call or override.

**Specified by:**
- intervalAdded

in interface

ListDataListener

**Parameters:**
- e

- a

ListDataEvent

encapsulating the
event information

---

#### public void intervalRemoved​(
ListDataEvent
e)

This method is public as an implementation side effect.
do not call or override.

**Specified by:**
- intervalRemoved

in interface

ListDataListener

**Parameters:**
- e

- a

ListDataEvent

encapsulating the
event information

---

#### public boolean selectWithKeyChar​(char keyChar)

Selects the list item that corresponds to the specified keyboard
character and returns true, if there is an item corresponding
to that character. Otherwise, returns false.

**Parameters:**
- keyChar

- a char, typically this is a keyboard key
typed by the user

**Returns:**
- true

if there is an item corresponding to that character.
Otherwise, returns

false

.

---

#### @BeanProperty
(
preferred
=true,

description
="The enabled state of the component.")
public void setEnabled​(boolean b)

Enables the combo box so that items can be selected. When the
combo box is disabled, items cannot be selected and values
cannot be typed into its field (if it is editable).

**Overrides:**
- setEnabled

in class

JComponent

**Parameters:**
- b

- a boolean value, where true enables the component and
false disables it

**See Also:**
- Component.isEnabled()

,

Component.isLightweight()

---

#### public void configureEditor​(
ComboBoxEditor
anEditor,

Object
anItem)

Initializes the editor with the specified item.

**Parameters:**
- anEditor

- the

ComboBoxEditor

that displays
the list item in the
combo box field and allows it to be edited
- anItem

- the object to display and edit in the field

---

#### public void processKeyEvent​(
KeyEvent
e)

Handles

KeyEvent

s, looking for the Tab key.
If the Tab key is found, the popup window is closed.

**Overrides:**
- processKeyEvent

in class

JComponent

**Parameters:**
- e

- the

KeyEvent

containing the keyboard
key that was pressed

**See Also:**
- KeyEvent

,

KeyListener

,

KeyboardFocusManager

,

DefaultKeyboardFocusManager

,

Component.processEvent(java.awt.AWTEvent)

,

Component.dispatchEvent(java.awt.AWTEvent)

,

Component.addKeyListener(java.awt.event.KeyListener)

,

Component.enableEvents(long)

,

Component.isShowing()

---

#### @BeanProperty
(
bound
=false,

expert
=true,

description
="The objects that changes the selection when a key is pressed.")
public void setKeySelectionManager​(
JComboBox.KeySelectionManager
aManager)

Sets the object that translates a keyboard character into a list
selection. Typically, the first selection with a matching first
character becomes the selected item.

**Parameters:**
- aManager

- a key selection manager

---

#### public
JComboBox.KeySelectionManager
getKeySelectionManager()

Returns the list's key-selection manager.

**Returns:**
- the

KeySelectionManager

currently in use

---

#### @BeanProperty
(
bound
=false)
public int getItemCount()

Returns the number of items in the list.

**Returns:**
- an integer equal to the number of items in the list

---

#### public
E
getItemAt​(int index)

Returns the list item at the specified index. If

index

is out of range (less than zero or greater than or equal to size)
it will return

null

.

**Parameters:**
- index

- an integer indicating the list position, where the first
item starts at zero

**Returns:**
- the item at that list position; or

null

if out of range

---

#### protected
JComboBox.KeySelectionManager
createDefaultKeySelectionManager()

Returns an instance of the default key-selection manager.

**Returns:**
- the

KeySelectionManager

currently used by the list

**See Also:**
- setKeySelectionManager(javax.swing.JComboBox.KeySelectionManager)

---

#### protected
String
paramString()

Returns a string representation of this

JComboBox

.
This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary between
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

JComboBox

---

#### @BeanProperty
(
bound
=false)
public
AccessibleContext
getAccessibleContext()

Gets the AccessibleContext associated with this JComboBox.
For combo boxes, the AccessibleContext takes the form of an
AccessibleJComboBox.
A new AccessibleJComboBox instance is created if necessary.

**Specified by:**
- getAccessibleContext

in interface

Accessible

**Overrides:**
- getAccessibleContext

in class

Component

**Returns:**
- an AccessibleJComboBox that serves as the
AccessibleContext of this JComboBox

---

### Additional Sections

#### Class JComboBox<E>

java.lang.Object

- java.awt.Component
- - java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JComboBox<E>

java.awt.Component

- java.awt.Container
- - javax.swing.JComponent
- - javax.swing.JComboBox<E>

java.awt.Container

- javax.swing.JComponent
- - javax.swing.JComboBox<E>

javax.swing.JComponent

- javax.swing.JComboBox<E>

javax.swing.JComboBox<E>

**Type Parameters:** E

- the type of the elements of this combo box

**All Implemented Interfaces:** ActionListener

,

ImageObserver

,

ItemSelectable

,

MenuContainer

,

Serializable

,

EventListener

,

Accessible

,

ListDataListener

```java
@JavaBean
(
defaultProperty
="UI",

description
="A combination of a text field and a drop-down list.")
public class
JComboBox<E>

extends
JComponent

implements
ItemSelectable
,
ListDataListener
,
ActionListener
,
Accessible
```

A component that combines a button or editable field and a drop-down list.
The user can select a value from the drop-down list, which appears at the
user's request. If you make the combo box editable, then the combo box
includes an editable field into which the user can type a value.

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

How to Use Combo Boxes

in

The Java Tutorial

for further information.

**Since:** 1.2
**See Also:** ComboBoxModel

,

DefaultComboBoxModel

,

Serialized Form

@JavaBean

(

defaultProperty

="UI",

description

="A combination of a text field and a drop-down list.")
public class

JComboBox<E>

extends

JComponent

implements

ItemSelectable

,

ListDataListener

,

ActionListener

,

Accessible

A component that combines a button or editable field and a drop-down list.
The user can select a value from the drop-down list, which appears at the
user's request. If you make the combo box editable, then the combo box
includes an editable field into which the user can type a value.

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

How to Use Combo Boxes

in

The Java Tutorial

for further information.

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

How to Use Combo Boxes

in

The Java Tutorial

for further information.

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

How to Use Combo Boxes

in

The Java Tutorial

for further information.

See

How to Use Combo Boxes

in

The Java Tutorial

for further information.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

JComboBox.AccessibleJComboBox

This class implements accessibility support for the

JComboBox

class.

static interface

JComboBox.KeySelectionManager

The interface that defines a

KeySelectionManager

.

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

String

actionCommand

This protected field is implementation specific.

protected

ComboBoxModel

<

E

>

dataModel

This protected field is implementation specific.

protected

ComboBoxEditor

editor

This protected field is implementation specific.

protected boolean

isEditable

This protected field is implementation specific.

protected

JComboBox.KeySelectionManager

keySelectionManager

This protected field is implementation specific.

protected boolean

lightWeightPopupEnabled

This protected field is implementation specific.

protected int

maximumRowCount

This protected field is implementation specific.

protected

ListCellRenderer

<? super

E

>

renderer

This protected field is implementation specific.

protected

Object

selectedItemReminder

This protected field is implementation specific.

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

JComboBox

()

Creates a

JComboBox

with a default data model.

JComboBox

​(

E

[] items)

Creates a

JComboBox

that contains the elements
in the specified array.

JComboBox

​(

Vector

<

E

> items)

Creates a

JComboBox

that contains the elements
in the specified Vector.

JComboBox

​(

ComboBoxModel

<

E

> aModel)

Creates a

JComboBox

that takes its items from an
existing

ComboBoxModel

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

actionPerformed

​(

ActionEvent

e)

This method is public as an implementation side effect.

protected void

actionPropertyChanged

​(

Action

action,

String

propertyName)

Updates the combobox's state in response to property changes in
associated action.

void

addActionListener

​(

ActionListener

l)

Adds an

ActionListener

.

void

addItem

​(

E

item)

Adds an item to the item list.

void

addItemListener

​(

ItemListener

aListener)

Adds an

ItemListener

.

void

addPopupMenuListener

​(

PopupMenuListener

l)

Adds a

PopupMenu

listener which will listen to notification
messages from the popup portion of the combo box.

void

configureEditor

​(

ComboBoxEditor

anEditor,

Object

anItem)

Initializes the editor with the specified item.

protected void

configurePropertiesFromAction

​(

Action

a)

Sets the properties on this combobox to match those in the specified

Action

.

void

contentsChanged

​(

ListDataEvent

e)

This method is public as an implementation side effect.

protected

PropertyChangeListener

createActionPropertyChangeListener

​(

Action

a)

Creates and returns a

PropertyChangeListener

that is
responsible for listening for changes from the specified

Action

and updating the appropriate properties.

protected

JComboBox.KeySelectionManager

createDefaultKeySelectionManager

()

Returns an instance of the default key-selection manager.

protected void

fireActionEvent

()

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireItemStateChanged

​(

ItemEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

void

firePopupMenuCanceled

()

Notifies

PopupMenuListener

s that the popup portion of the
combo box has been canceled.

void

firePopupMenuWillBecomeInvisible

()

Notifies

PopupMenuListener

s that the popup portion of the
combo box has become invisible.

void

firePopupMenuWillBecomeVisible

()

Notifies

PopupMenuListener

s that the popup portion of the
combo box will become visible.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JComboBox.

Action

getAction

()

Returns the currently set

Action

for this

ActionEvent

source, or

null

if no

Action

is set.

String

getActionCommand

()

Returns the action command that is included in the event sent to
action listeners.

ActionListener

[]

getActionListeners

()

Returns an array of all the

ActionListener

s added
to this JComboBox with addActionListener().

ComboBoxEditor

getEditor

()

Returns the editor used to paint and edit the selected item in the

JComboBox

field.

E

getItemAt

​(int index)

Returns the list item at the specified index.

int

getItemCount

()

Returns the number of items in the list.

ItemListener

[]

getItemListeners

()

Returns an array of all the

ItemListener

s added
to this JComboBox with addItemListener().

JComboBox.KeySelectionManager

getKeySelectionManager

()

Returns the list's key-selection manager.

int

getMaximumRowCount

()

Returns the maximum number of items the combo box can display
without a scrollbar

ComboBoxModel

<

E

>

getModel

()

Returns the data model currently used by the

JComboBox

.

PopupMenuListener

[]

getPopupMenuListeners

()

Returns an array of all the

PopupMenuListener

s added
to this JComboBox with addPopupMenuListener().

E

getPrototypeDisplayValue

()

Returns the "prototypical display" value - an Object used
for the calculation of the display height and width.

ListCellRenderer

<? super

E

>

getRenderer

()

Returns the renderer used to display the selected item in the

JComboBox

field.

int

getSelectedIndex

()

Returns the first item in the list that matches the given item.

Object

getSelectedItem

()

Returns the current selected item.

Object

[]

getSelectedObjects

()

Returns an array containing the selected item.

ComboBoxUI

getUI

()

Returns the L&F object that renders this component.

String

getUIClassID

()

Returns the name of the L&F class that renders this component.

void

hidePopup

()

Causes the combo box to close its popup window.

void

insertItemAt

​(

E

item,
int index)

Inserts an item into the item list at a given index.

protected void

installAncestorListener

()

Registers ancestor listener so that it will receive

AncestorEvents

when it or any of its ancestors
move or are made visible or invisible.

void

intervalAdded

​(

ListDataEvent

e)

This method is public as an implementation side effect.

void

intervalRemoved

​(

ListDataEvent

e)

This method is public as an implementation side effect.

boolean

isEditable

()

Returns true if the

JComboBox

is editable.

boolean

isLightWeightPopupEnabled

()

Gets the value of the

lightWeightPopupEnabled

property.

boolean

isPopupVisible

()

Determines the visibility of the popup.

protected

String

paramString

()

Returns a string representation of this

JComboBox

.

void

processKeyEvent

​(

KeyEvent

e)

Handles

KeyEvent

s, looking for the Tab key.

void

removeActionListener

​(

ActionListener

l)

Removes an

ActionListener

.

void

removeAllItems

()

Removes all items from the item list.

void

removeItem

​(

Object

anObject)

Removes an item from the item list.

void

removeItemAt

​(int anIndex)

Removes the item at

anIndex

This method works only if the

JComboBox

uses a
mutable data model.

void

removeItemListener

​(

ItemListener

aListener)

Removes an

ItemListener

.

void

removePopupMenuListener

​(

PopupMenuListener

l)

Removes a

PopupMenuListener

.

protected void

selectedItemChanged

()

This protected method is implementation specific.

boolean

selectWithKeyChar

​(char keyChar)

Selects the list item that corresponds to the specified keyboard
character and returns true, if there is an item corresponding
to that character.

void

setAction

​(

Action

a)

Sets the

Action

for the

ActionEvent

source.

void

setActionCommand

​(

String

aCommand)

Sets the action command that should be included in the event
sent to action listeners.

void

setEditable

​(boolean aFlag)

Determines whether the

JComboBox

field is editable.

void

setEditor

​(

ComboBoxEditor

anEditor)

Sets the editor used to paint and edit the selected item in the

JComboBox

field.

void

setEnabled

​(boolean b)

Enables the combo box so that items can be selected.

void

setKeySelectionManager

​(

JComboBox.KeySelectionManager

aManager)

Sets the object that translates a keyboard character into a list
selection.

void

setLightWeightPopupEnabled

​(boolean aFlag)

Sets the

lightWeightPopupEnabled

property, which
provides a hint as to whether or not a lightweight

Component

should be used to contain the

JComboBox

, versus a heavyweight

Component

such as a

Panel

or a

Window

.

void

setMaximumRowCount

​(int count)

Sets the maximum number of rows the

JComboBox

displays.

void

setModel

​(

ComboBoxModel

<

E

> aModel)

Sets the data model that the

JComboBox

uses to obtain
the list of items.

void

setPopupVisible

​(boolean v)

Sets the visibility of the popup.

void

setPrototypeDisplayValue

​(

E

prototypeDisplayValue)

Sets the prototype display value used to calculate the size of the display
for the UI portion.

void

setRenderer

​(

ListCellRenderer

<? super

E

> aRenderer)

Sets the renderer that paints the list items and the item selected from the list in
the JComboBox field.

void

setSelectedIndex

​(int anIndex)

Selects the item at index

anIndex

.

void

setSelectedItem

​(

Object

anObject)

Sets the selected item in the combo box display area to the object in
the argument.

void

setUI

​(

ComboBoxUI

ui)

Sets the L&F object that renders this component.

void

showPopup

()

Causes the combo box to display its popup window.

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

JComboBox.AccessibleJComboBox

This class implements accessibility support for the

JComboBox

class.

static interface

JComboBox.KeySelectionManager

The interface that defines a

KeySelectionManager

.

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

JComboBox

class.

The interface that defines a

KeySelectionManager

.

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

String

actionCommand

This protected field is implementation specific.

protected

ComboBoxModel

<

E

>

dataModel

This protected field is implementation specific.

protected

ComboBoxEditor

editor

This protected field is implementation specific.

protected boolean

isEditable

This protected field is implementation specific.

protected

JComboBox.KeySelectionManager

keySelectionManager

This protected field is implementation specific.

protected boolean

lightWeightPopupEnabled

This protected field is implementation specific.

protected int

maximumRowCount

This protected field is implementation specific.

protected

ListCellRenderer

<? super

E

>

renderer

This protected field is implementation specific.

protected

Object

selectedItemReminder

This protected field is implementation specific.

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

JComboBox

()

Creates a

JComboBox

with a default data model.

JComboBox

​(

E

[] items)

Creates a

JComboBox

that contains the elements
in the specified array.

JComboBox

​(

Vector

<

E

> items)

Creates a

JComboBox

that contains the elements
in the specified Vector.

JComboBox

​(

ComboBoxModel

<

E

> aModel)

Creates a

JComboBox

that takes its items from an
existing

ComboBoxModel

.

---

#### Constructor Summary

Creates a

JComboBox

with a default data model.

Creates a

JComboBox

that contains the elements
in the specified array.

Creates a

JComboBox

that contains the elements
in the specified Vector.

Creates a

JComboBox

that takes its items from an
existing

ComboBoxModel

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

actionPerformed

​(

ActionEvent

e)

This method is public as an implementation side effect.

protected void

actionPropertyChanged

​(

Action

action,

String

propertyName)

Updates the combobox's state in response to property changes in
associated action.

void

addActionListener

​(

ActionListener

l)

Adds an

ActionListener

.

void

addItem

​(

E

item)

Adds an item to the item list.

void

addItemListener

​(

ItemListener

aListener)

Adds an

ItemListener

.

void

addPopupMenuListener

​(

PopupMenuListener

l)

Adds a

PopupMenu

listener which will listen to notification
messages from the popup portion of the combo box.

void

configureEditor

​(

ComboBoxEditor

anEditor,

Object

anItem)

Initializes the editor with the specified item.

protected void

configurePropertiesFromAction

​(

Action

a)

Sets the properties on this combobox to match those in the specified

Action

.

void

contentsChanged

​(

ListDataEvent

e)

This method is public as an implementation side effect.

protected

PropertyChangeListener

createActionPropertyChangeListener

​(

Action

a)

Creates and returns a

PropertyChangeListener

that is
responsible for listening for changes from the specified

Action

and updating the appropriate properties.

protected

JComboBox.KeySelectionManager

createDefaultKeySelectionManager

()

Returns an instance of the default key-selection manager.

protected void

fireActionEvent

()

Notifies all listeners that have registered interest for
notification on this event type.

protected void

fireItemStateChanged

​(

ItemEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

void

firePopupMenuCanceled

()

Notifies

PopupMenuListener

s that the popup portion of the
combo box has been canceled.

void

firePopupMenuWillBecomeInvisible

()

Notifies

PopupMenuListener

s that the popup portion of the
combo box has become invisible.

void

firePopupMenuWillBecomeVisible

()

Notifies

PopupMenuListener

s that the popup portion of the
combo box will become visible.

AccessibleContext

getAccessibleContext

()

Gets the AccessibleContext associated with this JComboBox.

Action

getAction

()

Returns the currently set

Action

for this

ActionEvent

source, or

null

if no

Action

is set.

String

getActionCommand

()

Returns the action command that is included in the event sent to
action listeners.

ActionListener

[]

getActionListeners

()

Returns an array of all the

ActionListener

s added
to this JComboBox with addActionListener().

ComboBoxEditor

getEditor

()

Returns the editor used to paint and edit the selected item in the

JComboBox

field.

E

getItemAt

​(int index)

Returns the list item at the specified index.

int

getItemCount

()

Returns the number of items in the list.

ItemListener

[]

getItemListeners

()

Returns an array of all the

ItemListener

s added
to this JComboBox with addItemListener().

JComboBox.KeySelectionManager

getKeySelectionManager

()

Returns the list's key-selection manager.

int

getMaximumRowCount

()

Returns the maximum number of items the combo box can display
without a scrollbar

ComboBoxModel

<

E

>

getModel

()

Returns the data model currently used by the

JComboBox

.

PopupMenuListener

[]

getPopupMenuListeners

()

Returns an array of all the

PopupMenuListener

s added
to this JComboBox with addPopupMenuListener().

E

getPrototypeDisplayValue

()

Returns the "prototypical display" value - an Object used
for the calculation of the display height and width.

ListCellRenderer

<? super

E

>

getRenderer

()

Returns the renderer used to display the selected item in the

JComboBox

field.

int

getSelectedIndex

()

Returns the first item in the list that matches the given item.

Object

getSelectedItem

()

Returns the current selected item.

Object

[]

getSelectedObjects

()

Returns an array containing the selected item.

ComboBoxUI

getUI

()

Returns the L&F object that renders this component.

String

getUIClassID

()

Returns the name of the L&F class that renders this component.

void

hidePopup

()

Causes the combo box to close its popup window.

void

insertItemAt

​(

E

item,
int index)

Inserts an item into the item list at a given index.

protected void

installAncestorListener

()

Registers ancestor listener so that it will receive

AncestorEvents

when it or any of its ancestors
move or are made visible or invisible.

void

intervalAdded

​(

ListDataEvent

e)

This method is public as an implementation side effect.

void

intervalRemoved

​(

ListDataEvent

e)

This method is public as an implementation side effect.

boolean

isEditable

()

Returns true if the

JComboBox

is editable.

boolean

isLightWeightPopupEnabled

()

Gets the value of the

lightWeightPopupEnabled

property.

boolean

isPopupVisible

()

Determines the visibility of the popup.

protected

String

paramString

()

Returns a string representation of this

JComboBox

.

void

processKeyEvent

​(

KeyEvent

e)

Handles

KeyEvent

s, looking for the Tab key.

void

removeActionListener

​(

ActionListener

l)

Removes an

ActionListener

.

void

removeAllItems

()

Removes all items from the item list.

void

removeItem

​(

Object

anObject)

Removes an item from the item list.

void

removeItemAt

​(int anIndex)

Removes the item at

anIndex

This method works only if the

JComboBox

uses a
mutable data model.

void

removeItemListener

​(

ItemListener

aListener)

Removes an

ItemListener

.

void

removePopupMenuListener

​(

PopupMenuListener

l)

Removes a

PopupMenuListener

.

protected void

selectedItemChanged

()

This protected method is implementation specific.

boolean

selectWithKeyChar

​(char keyChar)

Selects the list item that corresponds to the specified keyboard
character and returns true, if there is an item corresponding
to that character.

void

setAction

​(

Action

a)

Sets the

Action

for the

ActionEvent

source.

void

setActionCommand

​(

String

aCommand)

Sets the action command that should be included in the event
sent to action listeners.

void

setEditable

​(boolean aFlag)

Determines whether the

JComboBox

field is editable.

void

setEditor

​(

ComboBoxEditor

anEditor)

Sets the editor used to paint and edit the selected item in the

JComboBox

field.

void

setEnabled

​(boolean b)

Enables the combo box so that items can be selected.

void

setKeySelectionManager

​(

JComboBox.KeySelectionManager

aManager)

Sets the object that translates a keyboard character into a list
selection.

void

setLightWeightPopupEnabled

​(boolean aFlag)

Sets the

lightWeightPopupEnabled

property, which
provides a hint as to whether or not a lightweight

Component

should be used to contain the

JComboBox

, versus a heavyweight

Component

such as a

Panel

or a

Window

.

void

setMaximumRowCount

​(int count)

Sets the maximum number of rows the

JComboBox

displays.

void

setModel

​(

ComboBoxModel

<

E

> aModel)

Sets the data model that the

JComboBox

uses to obtain
the list of items.

void

setPopupVisible

​(boolean v)

Sets the visibility of the popup.

void

setPrototypeDisplayValue

​(

E

prototypeDisplayValue)

Sets the prototype display value used to calculate the size of the display
for the UI portion.

void

setRenderer

​(

ListCellRenderer

<? super

E

> aRenderer)

Sets the renderer that paints the list items and the item selected from the list in
the JComboBox field.

void

setSelectedIndex

​(int anIndex)

Selects the item at index

anIndex

.

void

setSelectedItem

​(

Object

anObject)

Sets the selected item in the combo box display area to the object in
the argument.

void

setUI

​(

ComboBoxUI

ui)

Sets the L&F object that renders this component.

void

showPopup

()

Causes the combo box to display its popup window.

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

This method is public as an implementation side effect.

Updates the combobox's state in response to property changes in
associated action.

Adds an

ActionListener

.

Adds an item to the item list.

Adds an

ItemListener

.

Adds a

PopupMenu

listener which will listen to notification
messages from the popup portion of the combo box.

Initializes the editor with the specified item.

Sets the properties on this combobox to match those in the specified

Action

.

Creates and returns a

PropertyChangeListener

that is
responsible for listening for changes from the specified

Action

and updating the appropriate properties.

Returns an instance of the default key-selection manager.

Notifies all listeners that have registered interest for
notification on this event type.

Notifies

PopupMenuListener

s that the popup portion of the
combo box has been canceled.

Notifies

PopupMenuListener

s that the popup portion of the
combo box has become invisible.

Notifies

PopupMenuListener

s that the popup portion of the
combo box will become visible.

Gets the AccessibleContext associated with this JComboBox.

Returns the currently set

Action

for this

ActionEvent

source, or

null

if no

Action

is set.

Returns the action command that is included in the event sent to
action listeners.

Returns an array of all the

ActionListener

s added
to this JComboBox with addActionListener().

Returns the editor used to paint and edit the selected item in the

JComboBox

field.

Returns the list item at the specified index.

Returns the number of items in the list.

Returns an array of all the

ItemListener

s added
to this JComboBox with addItemListener().

Returns the list's key-selection manager.

Returns the maximum number of items the combo box can display
without a scrollbar

Returns the data model currently used by the

JComboBox

.

Returns an array of all the

PopupMenuListener

s added
to this JComboBox with addPopupMenuListener().

Returns the "prototypical display" value - an Object used
for the calculation of the display height and width.

Returns the renderer used to display the selected item in the

JComboBox

field.

Returns the first item in the list that matches the given item.

Returns the current selected item.

Returns an array containing the selected item.

Returns the L&F object that renders this component.

Returns the name of the L&F class that renders this component.

Causes the combo box to close its popup window.

Inserts an item into the item list at a given index.

Registers ancestor listener so that it will receive

AncestorEvents

when it or any of its ancestors
move or are made visible or invisible.

Returns true if the

JComboBox

is editable.

Gets the value of the

lightWeightPopupEnabled

property.

Determines the visibility of the popup.

Returns a string representation of this

JComboBox

.

Handles

KeyEvent

s, looking for the Tab key.

Removes an

ActionListener

.

Removes all items from the item list.

Removes an item from the item list.

Removes the item at

anIndex

This method works only if the

JComboBox

uses a
mutable data model.

Removes an

ItemListener

.

Removes a

PopupMenuListener

.

This protected method is implementation specific.

Selects the list item that corresponds to the specified keyboard
character and returns true, if there is an item corresponding
to that character.

Sets the

Action

for the

ActionEvent

source.

Sets the action command that should be included in the event
sent to action listeners.

Determines whether the

JComboBox

field is editable.

Sets the editor used to paint and edit the selected item in the

JComboBox

field.

Enables the combo box so that items can be selected.

Sets the object that translates a keyboard character into a list
selection.

Sets the

lightWeightPopupEnabled

property, which
provides a hint as to whether or not a lightweight

Component

should be used to contain the

JComboBox

, versus a heavyweight

Component

such as a

Panel

or a

Window

.

Sets the maximum number of rows the

JComboBox

displays.

Sets the data model that the

JComboBox

uses to obtain
the list of items.

Sets the visibility of the popup.

Sets the prototype display value used to calculate the size of the display
for the UI portion.

Sets the renderer that paints the list items and the item selected from the list in
the JComboBox field.

Selects the item at index

anIndex

.

Sets the selected item in the combo box display area to the object in
the argument.

Sets the L&F object that renders this component.

Causes the combo box to display its popup window.

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

============ FIELD DETAIL ===========

- Field Detail

- dataModel

```java
protected
ComboBoxModel
<
E
> dataModel
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** getModel()

,

setModel(javax.swing.ComboBoxModel<E>)

- renderer

```java
protected
ListCellRenderer
<? super
E
> renderer
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** getRenderer()

,

setRenderer(javax.swing.ListCellRenderer<? super E>)

- editor

```java
protected
ComboBoxEditor
editor
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** getEditor()

,

setEditor(javax.swing.ComboBoxEditor)

- maximumRowCount

```java
protected int maximumRowCount
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** getMaximumRowCount()

,

setMaximumRowCount(int)

- isEditable

```java
protected boolean isEditable
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** isEditable

,

setEditable(boolean)

- keySelectionManager

```java
protected
JComboBox.KeySelectionManager
keySelectionManager
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** setKeySelectionManager(javax.swing.JComboBox.KeySelectionManager)

,

getKeySelectionManager()

- actionCommand

```java
protected
String
actionCommand
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** setActionCommand(java.lang.String)

,

getActionCommand()

- lightWeightPopupEnabled

```java
protected boolean lightWeightPopupEnabled
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** setLightWeightPopupEnabled(boolean)

,

isLightWeightPopupEnabled()

- selectedItemReminder

```java
protected
Object
selectedItemReminder
```

This protected field is implementation specific. Do not access directly
or override.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- JComboBox

```java
public JComboBox​(
ComboBoxModel
<
E
> aModel)
```

Creates a

JComboBox

that takes its items from an
existing

ComboBoxModel

. Since the

ComboBoxModel

is provided, a combo box created using
this constructor does not create a default combo box model and
may impact how the insert, remove and add methods behave.

**Parameters:** aModel

- the

ComboBoxModel

that provides the
displayed list of items
**See Also:** DefaultComboBoxModel

- JComboBox

```java
public JComboBox​(
E
[] items)
```

Creates a

JComboBox

that contains the elements
in the specified array. By default the first item in the array
(and therefore the data model) becomes selected.

**Parameters:** items

- an array of objects to insert into the combo box
**See Also:** DefaultComboBoxModel

- JComboBox

```java
public JComboBox​(
Vector
<
E
> items)
```

Creates a

JComboBox

that contains the elements
in the specified Vector. By default the first item in the vector
(and therefore the data model) becomes selected.

**Parameters:** items

- an array of vectors to insert into the combo box
**See Also:** DefaultComboBoxModel

- JComboBox

```java
public JComboBox()
```

Creates a

JComboBox

with a default data model.
The default data model is an empty list of objects.
Use

addItem

to add items. By default the first item
in the data model becomes selected.

**See Also:** DefaultComboBoxModel

============ METHOD DETAIL ==========

- Method Detail

- installAncestorListener

```java
protected void installAncestorListener()
```

Registers ancestor listener so that it will receive

AncestorEvents

when it or any of its ancestors
move or are made visible or invisible.
Events are also sent when the component or its ancestors are added
or removed from the containment hierarchy.

- setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
ComboBoxUI
ui)
```

Sets the L&F object that renders this component.

**Parameters:** ui

- the

ComboBoxUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

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

JComponent
**Returns:** the string "ComboBoxUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- getUI

```java
public
ComboBoxUI
getUI()
```

Returns the L&F object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the ComboBoxUI object that renders this component

- setModel

```java
@BeanProperty
(
description
="Model that the combo box uses to get data to display.")
public void setModel​(
ComboBoxModel
<
E
> aModel)
```

Sets the data model that the

JComboBox

uses to obtain
the list of items.

**Parameters:** aModel

- the

ComboBoxModel

that provides the
displayed list of items

- getModel

```java
public
ComboBoxModel
<
E
> getModel()
```

Returns the data model currently used by the

JComboBox

.

**Returns:** the

ComboBoxModel

that provides the displayed
list of items

- setLightWeightPopupEnabled

```java
@BeanProperty
(
expert
=true,

description
="Set to <code>false</code> to require heavyweight popups.")
public void setLightWeightPopupEnabled​(boolean aFlag)
```

Sets the

lightWeightPopupEnabled

property, which
provides a hint as to whether or not a lightweight

Component

should be used to contain the

JComboBox

, versus a heavyweight

Component

such as a

Panel

or a

Window

. The decision of lightweight
versus heavyweight is ultimately up to the

JComboBox

. Lightweight windows are more
efficient than heavyweight windows, but lightweight
and heavyweight components do not mix well in a GUI.
If your application mixes lightweight and heavyweight
components, you should disable lightweight popups.
The default value for the

lightWeightPopupEnabled

property is

true

, unless otherwise specified
by the look and feel. Some look and feels always use
heavyweight popups, no matter what the value of this property.

See the article

Mixing Heavy and Light Components

This method fires a property changed event.

**Parameters:** aFlag

- if

true

, lightweight popups are desired

- isLightWeightPopupEnabled

```java
public boolean isLightWeightPopupEnabled()
```

Gets the value of the

lightWeightPopupEnabled

property.

**Returns:** the value of the

lightWeightPopupEnabled

property
**See Also:** setLightWeightPopupEnabled(boolean)

- setEditable

```java
@BeanProperty
(
preferred
=true,

description
="If true, the user can type a new value in the combo box.")
public void setEditable​(boolean aFlag)
```

Determines whether the

JComboBox

field is editable.
An editable

JComboBox

allows the user to type into the
field or selected an item from the list to initialize the field,
after which it can be edited. (The editing affects only the field,
the list item remains intact.) A non editable

JComboBox

displays the selected item in the field,
but the selection cannot be modified.

**Parameters:** aFlag

- a boolean value, where true indicates that the
field is editable

- isEditable

```java
public boolean isEditable()
```

Returns true if the

JComboBox

is editable.
By default, a combo box is not editable.

**Returns:** true if the

JComboBox

is editable, else false

- setMaximumRowCount

```java
@BeanProperty
(
preferred
=true,

description
="The maximum number of rows the popup should have")
public void setMaximumRowCount​(int count)
```

Sets the maximum number of rows the

JComboBox

displays.
If the number of objects in the model is greater than count,
the combo box uses a scrollbar.

**Parameters:** count

- an integer specifying the maximum number of items to
display in the list before using a scrollbar

- getMaximumRowCount

```java
public int getMaximumRowCount()
```

Returns the maximum number of items the combo box can display
without a scrollbar

**Returns:** an integer specifying the maximum number of items that are
displayed in the list before using a scrollbar

- setRenderer

```java
@BeanProperty
(
expert
=true,

description
="The renderer that paints the item selected in the list.")
public void setRenderer​(
ListCellRenderer
<? super
E
> aRenderer)
```

Sets the renderer that paints the list items and the item selected from the list in
the JComboBox field. The renderer is used if the JComboBox is not
editable. If it is editable, the editor is used to render and edit
the selected item.

The default renderer displays a string or an icon.
Other renderers can handle graphic images and composite items.

To display the selected item,

aRenderer.getListCellRendererComponent

is called, passing the list object and an index of -1.

**Parameters:** aRenderer

- the

ListCellRenderer

that
displays the selected item
**See Also:** setEditor(javax.swing.ComboBoxEditor)

- getRenderer

```java
public
ListCellRenderer
<? super
E
> getRenderer()
```

Returns the renderer used to display the selected item in the

JComboBox

field.

**Returns:** the

ListCellRenderer

that displays
the selected item.

- setEditor

```java
@BeanProperty
(
expert
=true,

description
="The editor that combo box uses to edit the current value")
public void setEditor​(
ComboBoxEditor
anEditor)
```

Sets the editor used to paint and edit the selected item in the

JComboBox

field. The editor is used only if the
receiving

JComboBox

is editable. If not editable,
the combo box uses the renderer to paint the selected item.

**Parameters:** anEditor

- the

ComboBoxEditor

that
displays the selected item
**See Also:** setRenderer(javax.swing.ListCellRenderer<? super E>)

- getEditor

```java
public
ComboBoxEditor
getEditor()
```

Returns the editor used to paint and edit the selected item in the

JComboBox

field.

**Returns:** the

ComboBoxEditor

that displays the selected item

- setSelectedItem

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="Sets the selected item in the JComboBox.")
public void setSelectedItem​(
Object
anObject)
```

Sets the selected item in the combo box display area to the object in
the argument.
If

anObject

is in the list, the display area shows

anObject

selected.

If

anObject

is

not

in the list and the combo box is
uneditable, it will not change the current selection. For editable
combo boxes, the selection will change to

anObject

.

If this constitutes a change in the selected item,

ItemListener

s added to the combo box will be notified with
one or two

ItemEvent

s.
If there is a current selected item, an

ItemEvent

will be
fired and the state change will be

ItemEvent.DESELECTED

.
If

anObject

is in the list and is not currently selected
then an

ItemEvent

will be fired and the state change will
be

ItemEvent.SELECTED

.

ActionListener

s added to the combo box will be notified
with an

ActionEvent

when this method is called.

**Parameters:** anObject

- the list object to select; use

null

to
clear the selection

- getSelectedItem

```java
public
Object
getSelectedItem()
```

Returns the current selected item.

If the combo box is editable, then this value may not have been added
to the combo box with

addItem

,

insertItemAt

or the data constructors.

**Returns:** the current selected Object
**See Also:** setSelectedItem(java.lang.Object)

- setSelectedIndex

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The item at index is selected.")
public void setSelectedIndex​(int anIndex)
```

Selects the item at index

anIndex

.

**Parameters:** anIndex

- an integer specifying the list item to select,
where 0 specifies the first item in the list and -1 indicates no selection
**Throws:** IllegalArgumentException

- if

anIndex

< -1 or

anIndex

is greater than or equal to size

- getSelectedIndex

```java
public int getSelectedIndex()
```

Returns the first item in the list that matches the given item.
The result is not always defined if the

JComboBox

allows selected items that are not in the list.
Returns -1 if there is no selected item or if the user specified
an item which is not in the list.

**Returns:** an integer specifying the currently selected list item,
where 0 specifies
the first item in the list;
or -1 if no item is selected or if
the currently selected item is not in the list

- getPrototypeDisplayValue

```java
public
E
getPrototypeDisplayValue()
```

Returns the "prototypical display" value - an Object used
for the calculation of the display height and width.

**Returns:** the value of the

prototypeDisplayValue

property
**Since:** 1.4
**See Also:** setPrototypeDisplayValue(E)

- setPrototypeDisplayValue

```java
@BeanProperty
(
visualUpdate
=true,

description
="The display prototype value, used to compute display width and height.")
public void setPrototypeDisplayValue​(
E
prototypeDisplayValue)
```

Sets the prototype display value used to calculate the size of the display
for the UI portion.

If a prototype display value is specified, the preferred size of
the combo box is calculated by configuring the renderer with the
prototype display value and obtaining its preferred size. Specifying
the preferred display value is often useful when the combo box will be
displaying large amounts of data. If no prototype display value has
been specified, the renderer must be configured for each value from
the model and its preferred size obtained, which can be
relatively expensive.

**Parameters:** prototypeDisplayValue

- the prototype display value
**Since:** 1.4
**See Also:** getPrototypeDisplayValue()

- addItem

```java
public void addItem​(
E
item)
```

Adds an item to the item list.
This method works only if the

JComboBox

uses a
mutable data model.

Warning:

Focus and keyboard navigation problems may arise if you add duplicate
String objects. A workaround is to add new objects instead of String
objects and make sure that the toString() method is defined.
For example:

```java
comboBox.addItem(makeObj("Item 1"));
comboBox.addItem(makeObj("Item 1"));
...
private Object makeObj(final String item) {
return new Object() { public String toString() { return item; } };
}
```

**Parameters:** item

- the item to add to the list
**See Also:** MutableComboBoxModel

- insertItemAt

```java
public void insertItemAt​(
E
item,
int index)
```

Inserts an item into the item list at a given index.
This method works only if the

JComboBox

uses a
mutable data model.

**Parameters:** item

- the item to add to the list
**Parameters:** index

- an integer specifying the position at which
to add the item
**See Also:** MutableComboBoxModel

- removeItem

```java
public void removeItem​(
Object
anObject)
```

Removes an item from the item list.
This method works only if the

JComboBox

uses a
mutable data model.

**Parameters:** anObject

- the object to remove from the item list
**See Also:** MutableComboBoxModel

- removeItemAt

```java
public void removeItemAt​(int anIndex)
```

Removes the item at

anIndex

This method works only if the

JComboBox

uses a
mutable data model.

**Parameters:** anIndex

- an int specifying the index of the item to remove,
where 0
indicates the first item in the list
**See Also:** MutableComboBoxModel

- removeAllItems

```java
public void removeAllItems()
```

Removes all items from the item list.

- showPopup

```java
public void showPopup()
```

Causes the combo box to display its popup window.

**See Also:** setPopupVisible(boolean)

- hidePopup

```java
public void hidePopup()
```

Causes the combo box to close its popup window.

**See Also:** setPopupVisible(boolean)

- setPopupVisible

```java
public void setPopupVisible​(boolean v)
```

Sets the visibility of the popup.

**Parameters:** v

- if

true

shows the popup, otherwise, hides the popup.

- isPopupVisible

```java
public boolean isPopupVisible()
```

Determines the visibility of the popup.

**Returns:** true if the popup is visible, otherwise returns false

- addItemListener

```java
public void addItemListener​(
ItemListener
aListener)
```

Adds an

ItemListener

.

aListener

will receive one or two

ItemEvent

s when
the selected item changes.

**Specified by:** addItemListener

in interface

ItemSelectable
**Parameters:** aListener

- the

ItemListener

that is to be notified
**See Also:** setSelectedItem(java.lang.Object)

- removeItemListener

```java
public void removeItemListener​(
ItemListener
aListener)
```

Removes an

ItemListener

.

**Specified by:** removeItemListener

in interface

ItemSelectable
**Parameters:** aListener

- the

ItemListener

to remove
**See Also:** ItemEvent

- getItemListeners

```java
@BeanProperty
(
bound
=false)
public
ItemListener
[] getItemListeners()
```

Returns an array of all the

ItemListener

s added
to this JComboBox with addItemListener().

**Returns:** all of the

ItemListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- addActionListener

```java
public void addActionListener​(
ActionListener
l)
```

Adds an

ActionListener

.

The

ActionListener

will receive an

ActionEvent

when a selection has been made. If the combo box is editable, then
an

ActionEvent

will be fired when editing has stopped.

**Parameters:** l

- the

ActionListener

that is to be notified
**See Also:** setSelectedItem(java.lang.Object)

- removeActionListener

```java
public void removeActionListener​(
ActionListener
l)
```

Removes an

ActionListener

.

**Parameters:** l

- the

ActionListener

to remove

- getActionListeners

```java
@BeanProperty
(
bound
=false)
public
ActionListener
[] getActionListeners()
```

Returns an array of all the

ActionListener

s added
to this JComboBox with addActionListener().

**Returns:** all of the

ActionListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- addPopupMenuListener

```java
public void addPopupMenuListener​(
PopupMenuListener
l)
```

Adds a

PopupMenu

listener which will listen to notification
messages from the popup portion of the combo box.

For all standard look and feels shipped with Java, the popup list
portion of combo box is implemented as a

JPopupMenu

.
A custom look and feel may not implement it this way and will
therefore not receive the notification.

**Parameters:** l

- the

PopupMenuListener

to add
**Since:** 1.4

- removePopupMenuListener

```java
public void removePopupMenuListener​(
PopupMenuListener
l)
```

Removes a

PopupMenuListener

.

**Parameters:** l

- the

PopupMenuListener

to remove
**Since:** 1.4
**See Also:** addPopupMenuListener(javax.swing.event.PopupMenuListener)

- getPopupMenuListeners

```java
@BeanProperty
(
bound
=false)
public
PopupMenuListener
[] getPopupMenuListeners()
```

Returns an array of all the

PopupMenuListener

s added
to this JComboBox with addPopupMenuListener().

**Returns:** all of the

PopupMenuListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- firePopupMenuWillBecomeVisible

```java
public void firePopupMenuWillBecomeVisible()
```

Notifies

PopupMenuListener

s that the popup portion of the
combo box will become visible.

This method is public but should not be called by anything other than
the UI delegate.

**Since:** 1.4
**See Also:** addPopupMenuListener(javax.swing.event.PopupMenuListener)

- firePopupMenuWillBecomeInvisible

```java
public void firePopupMenuWillBecomeInvisible()
```

Notifies

PopupMenuListener

s that the popup portion of the
combo box has become invisible.

This method is public but should not be called by anything other than
the UI delegate.

**Since:** 1.4
**See Also:** addPopupMenuListener(javax.swing.event.PopupMenuListener)

- firePopupMenuCanceled

```java
public void firePopupMenuCanceled()
```

Notifies

PopupMenuListener

s that the popup portion of the
combo box has been canceled.

This method is public but should not be called by anything other than
the UI delegate.

**Since:** 1.4
**See Also:** addPopupMenuListener(javax.swing.event.PopupMenuListener)

- setActionCommand

```java
public void setActionCommand​(
String
aCommand)
```

Sets the action command that should be included in the event
sent to action listeners.

**Parameters:** aCommand

- a string containing the "command" that is sent
to action listeners; the same listener can then
do different things depending on the command it
receives

- getActionCommand

```java
public
String
getActionCommand()
```

Returns the action command that is included in the event sent to
action listeners.

**Returns:** the string containing the "command" that is sent
to action listeners.

- setAction

```java
@BeanProperty
(
visualUpdate
=true,

description
="the Action instance connected with this ActionEvent source")
public void setAction​(
Action
a)
```

Sets the

Action

for the

ActionEvent

source.
The new

Action

replaces any previously set

Action

but does not affect

ActionListeners

independently added with

addActionListener

.
If the

Action

is already a registered

ActionListener

for the

ActionEvent

source,
it is not re-registered.

Setting the

Action

results in immediately changing
all the properties described in

Swing Components Supporting

Action

.
Subsequently, the combobox's properties are automatically updated
as the

Action

's properties change.

This method uses three other methods to set
and help track the

Action

's property values.
It uses the

configurePropertiesFromAction

method
to immediately change the combobox's properties.
To track changes in the

Action

's property values,
this method registers the

PropertyChangeListener

returned by

createActionPropertyChangeListener

. The
default

PropertyChangeListener

invokes the

actionPropertyChanged

method when a property in the

Action

changes.

**Parameters:** a

- the

Action

for the

JComboBox

,
or

null

.
**Since:** 1.3
**See Also:** Action

,

getAction()

,

configurePropertiesFromAction(javax.swing.Action)

,

createActionPropertyChangeListener(javax.swing.Action)

,

actionPropertyChanged(javax.swing.Action, java.lang.String)

- getAction

```java
public
Action
getAction()
```

Returns the currently set

Action

for this

ActionEvent

source, or

null

if no

Action

is set.

**Returns:** the

Action

for this

ActionEvent

source; or

null
**Since:** 1.3
**See Also:** Action

,

setAction(javax.swing.Action)

- configurePropertiesFromAction

```java
protected void configurePropertiesFromAction​(
Action
a)
```

Sets the properties on this combobox to match those in the specified

Action

. Refer to

Swing Components Supporting

Action

for more
details as to which properties this sets.

**Parameters:** a

- the

Action

from which to get the properties,
or

null
**Since:** 1.3
**See Also:** Action

,

setAction(javax.swing.Action)

- createActionPropertyChangeListener

```java
protected
PropertyChangeListener
createActionPropertyChangeListener​(
Action
a)
```

Creates and returns a

PropertyChangeListener

that is
responsible for listening for changes from the specified

Action

and updating the appropriate properties.

Warning:

If you subclass this do not create an anonymous
inner class. If you do the lifetime of the combobox will be tied to
that of the

Action

.

**Parameters:** a

- the combobox's action
**Returns:** the

PropertyChangeListener
**Since:** 1.3
**See Also:** Action

,

setAction(javax.swing.Action)

- actionPropertyChanged

```java
protected void actionPropertyChanged​(
Action
action,

String
propertyName)
```

Updates the combobox's state in response to property changes in
associated action. This method is invoked from the

PropertyChangeListener

returned from

createActionPropertyChangeListener

. Subclasses do not normally
need to invoke this. Subclasses that support additional

Action

properties should override this and

configurePropertiesFromAction

.

Refer to the table at

Swing Components Supporting

Action

for a list of
the properties this method sets.

**Parameters:** action

- the

Action

associated with this combobox
**Parameters:** propertyName

- the name of the property that changed
**Since:** 1.6
**See Also:** Action

,

configurePropertiesFromAction(javax.swing.Action)

- fireItemStateChanged

```java
protected void fireItemStateChanged​(
ItemEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type.

**Parameters:** e

- the event of interest
**See Also:** EventListenerList

- fireActionEvent

```java
protected void fireActionEvent()
```

Notifies all listeners that have registered interest for
notification on this event type.

**See Also:** EventListenerList

- selectedItemChanged

```java
protected void selectedItemChanged()
```

This protected method is implementation specific. Do not access directly
or override.

- getSelectedObjects

```java
@BeanProperty
(
bound
=false)
public
Object
[] getSelectedObjects()
```

Returns an array containing the selected item.
This method is implemented for compatibility with

ItemSelectable

.

**Specified by:** getSelectedObjects

in interface

ItemSelectable
**Returns:** an array of

Objects

containing one
element -- the selected item

- actionPerformed

```java
public void actionPerformed​(
ActionEvent
e)
```

This method is public as an implementation side effect.
do not call or override.

**Specified by:** actionPerformed

in interface

ActionListener
**Parameters:** e

- the event to be processed

- contentsChanged

```java
public void contentsChanged​(
ListDataEvent
e)
```

This method is public as an implementation side effect.
do not call or override.

**Specified by:** contentsChanged

in interface

ListDataListener
**Parameters:** e

- a

ListDataEvent

encapsulating the
event information

- intervalAdded

```java
public void intervalAdded​(
ListDataEvent
e)
```

This method is public as an implementation side effect.
do not call or override.

**Specified by:** intervalAdded

in interface

ListDataListener
**Parameters:** e

- a

ListDataEvent

encapsulating the
event information

- intervalRemoved

```java
public void intervalRemoved​(
ListDataEvent
e)
```

This method is public as an implementation side effect.
do not call or override.

**Specified by:** intervalRemoved

in interface

ListDataListener
**Parameters:** e

- a

ListDataEvent

encapsulating the
event information

- selectWithKeyChar

```java
public boolean selectWithKeyChar​(char keyChar)
```

Selects the list item that corresponds to the specified keyboard
character and returns true, if there is an item corresponding
to that character. Otherwise, returns false.

**Parameters:** keyChar

- a char, typically this is a keyboard key
typed by the user
**Returns:** true

if there is an item corresponding to that character.
Otherwise, returns

false

.

- setEnabled

```java
@BeanProperty
(
preferred
=true,

description
="The enabled state of the component.")
public void setEnabled​(boolean b)
```

Enables the combo box so that items can be selected. When the
combo box is disabled, items cannot be selected and values
cannot be typed into its field (if it is editable).

**Overrides:** setEnabled

in class

JComponent
**Parameters:** b

- a boolean value, where true enables the component and
false disables it
**See Also:** Component.isEnabled()

,

Component.isLightweight()

- configureEditor

```java
public void configureEditor​(
ComboBoxEditor
anEditor,

Object
anItem)
```

Initializes the editor with the specified item.

**Parameters:** anEditor

- the

ComboBoxEditor

that displays
the list item in the
combo box field and allows it to be edited
**Parameters:** anItem

- the object to display and edit in the field

- processKeyEvent

```java
public void processKeyEvent​(
KeyEvent
e)
```

Handles

KeyEvent

s, looking for the Tab key.
If the Tab key is found, the popup window is closed.

**Overrides:** processKeyEvent

in class

JComponent
**Parameters:** e

- the

KeyEvent

containing the keyboard
key that was pressed
**See Also:** KeyEvent

,

KeyListener

,

KeyboardFocusManager

,

DefaultKeyboardFocusManager

,

Component.processEvent(java.awt.AWTEvent)

,

Component.dispatchEvent(java.awt.AWTEvent)

,

Component.addKeyListener(java.awt.event.KeyListener)

,

Component.enableEvents(long)

,

Component.isShowing()

- setKeySelectionManager

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The objects that changes the selection when a key is pressed.")
public void setKeySelectionManager​(
JComboBox.KeySelectionManager
aManager)
```

Sets the object that translates a keyboard character into a list
selection. Typically, the first selection with a matching first
character becomes the selected item.

**Parameters:** aManager

- a key selection manager

- getKeySelectionManager

```java
public
JComboBox.KeySelectionManager
getKeySelectionManager()
```

Returns the list's key-selection manager.

**Returns:** the

KeySelectionManager

currently in use

- getItemCount

```java
@BeanProperty
(
bound
=false)
public int getItemCount()
```

Returns the number of items in the list.

**Returns:** an integer equal to the number of items in the list

- getItemAt

```java
public
E
getItemAt​(int index)
```

Returns the list item at the specified index. If

index

is out of range (less than zero or greater than or equal to size)
it will return

null

.

**Parameters:** index

- an integer indicating the list position, where the first
item starts at zero
**Returns:** the item at that list position; or

null

if out of range

- createDefaultKeySelectionManager

```java
protected
JComboBox.KeySelectionManager
createDefaultKeySelectionManager()
```

Returns an instance of the default key-selection manager.

**Returns:** the

KeySelectionManager

currently used by the list
**See Also:** setKeySelectionManager(javax.swing.JComboBox.KeySelectionManager)

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JComboBox

.
This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

JComboBox

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

Gets the AccessibleContext associated with this JComboBox.
For combo boxes, the AccessibleContext takes the form of an
AccessibleJComboBox.
A new AccessibleJComboBox instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJComboBox that serves as the
AccessibleContext of this JComboBox

Field Detail

- dataModel

```java
protected
ComboBoxModel
<
E
> dataModel
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** getModel()

,

setModel(javax.swing.ComboBoxModel<E>)

- renderer

```java
protected
ListCellRenderer
<? super
E
> renderer
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** getRenderer()

,

setRenderer(javax.swing.ListCellRenderer<? super E>)

- editor

```java
protected
ComboBoxEditor
editor
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** getEditor()

,

setEditor(javax.swing.ComboBoxEditor)

- maximumRowCount

```java
protected int maximumRowCount
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** getMaximumRowCount()

,

setMaximumRowCount(int)

- isEditable

```java
protected boolean isEditable
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** isEditable

,

setEditable(boolean)

- keySelectionManager

```java
protected
JComboBox.KeySelectionManager
keySelectionManager
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** setKeySelectionManager(javax.swing.JComboBox.KeySelectionManager)

,

getKeySelectionManager()

- actionCommand

```java
protected
String
actionCommand
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** setActionCommand(java.lang.String)

,

getActionCommand()

- lightWeightPopupEnabled

```java
protected boolean lightWeightPopupEnabled
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** setLightWeightPopupEnabled(boolean)

,

isLightWeightPopupEnabled()

- selectedItemReminder

```java
protected
Object
selectedItemReminder
```

This protected field is implementation specific. Do not access directly
or override.

---

#### Field Detail

dataModel

```java
protected
ComboBoxModel
<
E
> dataModel
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** getModel()

,

setModel(javax.swing.ComboBoxModel<E>)

---

#### dataModel

protected

ComboBoxModel

<

E

> dataModel

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

renderer

```java
protected
ListCellRenderer
<? super
E
> renderer
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** getRenderer()

,

setRenderer(javax.swing.ListCellRenderer<? super E>)

---

#### renderer

protected

ListCellRenderer

<? super

E

> renderer

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

editor

```java
protected
ComboBoxEditor
editor
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** getEditor()

,

setEditor(javax.swing.ComboBoxEditor)

---

#### editor

protected

ComboBoxEditor

editor

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

maximumRowCount

```java
protected int maximumRowCount
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** getMaximumRowCount()

,

setMaximumRowCount(int)

---

#### maximumRowCount

protected int maximumRowCount

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

isEditable

```java
protected boolean isEditable
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** isEditable

,

setEditable(boolean)

---

#### isEditable

protected boolean isEditable

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

keySelectionManager

```java
protected
JComboBox.KeySelectionManager
keySelectionManager
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** setKeySelectionManager(javax.swing.JComboBox.KeySelectionManager)

,

getKeySelectionManager()

---

#### keySelectionManager

protected

JComboBox.KeySelectionManager

keySelectionManager

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

actionCommand

```java
protected
String
actionCommand
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** setActionCommand(java.lang.String)

,

getActionCommand()

---

#### actionCommand

protected

String

actionCommand

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

lightWeightPopupEnabled

```java
protected boolean lightWeightPopupEnabled
```

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

**See Also:** setLightWeightPopupEnabled(boolean)

,

isLightWeightPopupEnabled()

---

#### lightWeightPopupEnabled

protected boolean lightWeightPopupEnabled

This protected field is implementation specific. Do not access directly
or override. Use the accessor methods instead.

selectedItemReminder

```java
protected
Object
selectedItemReminder
```

This protected field is implementation specific. Do not access directly
or override.

---

#### selectedItemReminder

protected

Object

selectedItemReminder

This protected field is implementation specific. Do not access directly
or override.

Constructor Detail

- JComboBox

```java
public JComboBox​(
ComboBoxModel
<
E
> aModel)
```

Creates a

JComboBox

that takes its items from an
existing

ComboBoxModel

. Since the

ComboBoxModel

is provided, a combo box created using
this constructor does not create a default combo box model and
may impact how the insert, remove and add methods behave.

**Parameters:** aModel

- the

ComboBoxModel

that provides the
displayed list of items
**See Also:** DefaultComboBoxModel

- JComboBox

```java
public JComboBox​(
E
[] items)
```

Creates a

JComboBox

that contains the elements
in the specified array. By default the first item in the array
(and therefore the data model) becomes selected.

**Parameters:** items

- an array of objects to insert into the combo box
**See Also:** DefaultComboBoxModel

- JComboBox

```java
public JComboBox​(
Vector
<
E
> items)
```

Creates a

JComboBox

that contains the elements
in the specified Vector. By default the first item in the vector
(and therefore the data model) becomes selected.

**Parameters:** items

- an array of vectors to insert into the combo box
**See Also:** DefaultComboBoxModel

- JComboBox

```java
public JComboBox()
```

Creates a

JComboBox

with a default data model.
The default data model is an empty list of objects.
Use

addItem

to add items. By default the first item
in the data model becomes selected.

**See Also:** DefaultComboBoxModel

---

#### Constructor Detail

JComboBox

```java
public JComboBox​(
ComboBoxModel
<
E
> aModel)
```

Creates a

JComboBox

that takes its items from an
existing

ComboBoxModel

. Since the

ComboBoxModel

is provided, a combo box created using
this constructor does not create a default combo box model and
may impact how the insert, remove and add methods behave.

**Parameters:** aModel

- the

ComboBoxModel

that provides the
displayed list of items
**See Also:** DefaultComboBoxModel

---

#### JComboBox

public JComboBox​(

ComboBoxModel

<

E

> aModel)

Creates a

JComboBox

that takes its items from an
existing

ComboBoxModel

. Since the

ComboBoxModel

is provided, a combo box created using
this constructor does not create a default combo box model and
may impact how the insert, remove and add methods behave.

JComboBox

```java
public JComboBox​(
E
[] items)
```

Creates a

JComboBox

that contains the elements
in the specified array. By default the first item in the array
(and therefore the data model) becomes selected.

**Parameters:** items

- an array of objects to insert into the combo box
**See Also:** DefaultComboBoxModel

---

#### JComboBox

public JComboBox​(

E

[] items)

Creates a

JComboBox

that contains the elements
in the specified array. By default the first item in the array
(and therefore the data model) becomes selected.

JComboBox

```java
public JComboBox​(
Vector
<
E
> items)
```

Creates a

JComboBox

that contains the elements
in the specified Vector. By default the first item in the vector
(and therefore the data model) becomes selected.

**Parameters:** items

- an array of vectors to insert into the combo box
**See Also:** DefaultComboBoxModel

---

#### JComboBox

public JComboBox​(

Vector

<

E

> items)

Creates a

JComboBox

that contains the elements
in the specified Vector. By default the first item in the vector
(and therefore the data model) becomes selected.

JComboBox

```java
public JComboBox()
```

Creates a

JComboBox

with a default data model.
The default data model is an empty list of objects.
Use

addItem

to add items. By default the first item
in the data model becomes selected.

**See Also:** DefaultComboBoxModel

---

#### JComboBox

public JComboBox()

Creates a

JComboBox

with a default data model.
The default data model is an empty list of objects.
Use

addItem

to add items. By default the first item
in the data model becomes selected.

Method Detail

- installAncestorListener

```java
protected void installAncestorListener()
```

Registers ancestor listener so that it will receive

AncestorEvents

when it or any of its ancestors
move or are made visible or invisible.
Events are also sent when the component or its ancestors are added
or removed from the containment hierarchy.

- setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
ComboBoxUI
ui)
```

Sets the L&F object that renders this component.

**Parameters:** ui

- the

ComboBoxUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

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

JComponent
**Returns:** the string "ComboBoxUI"
**See Also:** JComponent.getUIClassID()

,

UIDefaults.getUI(javax.swing.JComponent)

- getUI

```java
public
ComboBoxUI
getUI()
```

Returns the L&F object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the ComboBoxUI object that renders this component

- setModel

```java
@BeanProperty
(
description
="Model that the combo box uses to get data to display.")
public void setModel​(
ComboBoxModel
<
E
> aModel)
```

Sets the data model that the

JComboBox

uses to obtain
the list of items.

**Parameters:** aModel

- the

ComboBoxModel

that provides the
displayed list of items

- getModel

```java
public
ComboBoxModel
<
E
> getModel()
```

Returns the data model currently used by the

JComboBox

.

**Returns:** the

ComboBoxModel

that provides the displayed
list of items

- setLightWeightPopupEnabled

```java
@BeanProperty
(
expert
=true,

description
="Set to <code>false</code> to require heavyweight popups.")
public void setLightWeightPopupEnabled​(boolean aFlag)
```

Sets the

lightWeightPopupEnabled

property, which
provides a hint as to whether or not a lightweight

Component

should be used to contain the

JComboBox

, versus a heavyweight

Component

such as a

Panel

or a

Window

. The decision of lightweight
versus heavyweight is ultimately up to the

JComboBox

. Lightweight windows are more
efficient than heavyweight windows, but lightweight
and heavyweight components do not mix well in a GUI.
If your application mixes lightweight and heavyweight
components, you should disable lightweight popups.
The default value for the

lightWeightPopupEnabled

property is

true

, unless otherwise specified
by the look and feel. Some look and feels always use
heavyweight popups, no matter what the value of this property.

See the article

Mixing Heavy and Light Components

This method fires a property changed event.

**Parameters:** aFlag

- if

true

, lightweight popups are desired

- isLightWeightPopupEnabled

```java
public boolean isLightWeightPopupEnabled()
```

Gets the value of the

lightWeightPopupEnabled

property.

**Returns:** the value of the

lightWeightPopupEnabled

property
**See Also:** setLightWeightPopupEnabled(boolean)

- setEditable

```java
@BeanProperty
(
preferred
=true,

description
="If true, the user can type a new value in the combo box.")
public void setEditable​(boolean aFlag)
```

Determines whether the

JComboBox

field is editable.
An editable

JComboBox

allows the user to type into the
field or selected an item from the list to initialize the field,
after which it can be edited. (The editing affects only the field,
the list item remains intact.) A non editable

JComboBox

displays the selected item in the field,
but the selection cannot be modified.

**Parameters:** aFlag

- a boolean value, where true indicates that the
field is editable

- isEditable

```java
public boolean isEditable()
```

Returns true if the

JComboBox

is editable.
By default, a combo box is not editable.

**Returns:** true if the

JComboBox

is editable, else false

- setMaximumRowCount

```java
@BeanProperty
(
preferred
=true,

description
="The maximum number of rows the popup should have")
public void setMaximumRowCount​(int count)
```

Sets the maximum number of rows the

JComboBox

displays.
If the number of objects in the model is greater than count,
the combo box uses a scrollbar.

**Parameters:** count

- an integer specifying the maximum number of items to
display in the list before using a scrollbar

- getMaximumRowCount

```java
public int getMaximumRowCount()
```

Returns the maximum number of items the combo box can display
without a scrollbar

**Returns:** an integer specifying the maximum number of items that are
displayed in the list before using a scrollbar

- setRenderer

```java
@BeanProperty
(
expert
=true,

description
="The renderer that paints the item selected in the list.")
public void setRenderer​(
ListCellRenderer
<? super
E
> aRenderer)
```

Sets the renderer that paints the list items and the item selected from the list in
the JComboBox field. The renderer is used if the JComboBox is not
editable. If it is editable, the editor is used to render and edit
the selected item.

The default renderer displays a string or an icon.
Other renderers can handle graphic images and composite items.

To display the selected item,

aRenderer.getListCellRendererComponent

is called, passing the list object and an index of -1.

**Parameters:** aRenderer

- the

ListCellRenderer

that
displays the selected item
**See Also:** setEditor(javax.swing.ComboBoxEditor)

- getRenderer

```java
public
ListCellRenderer
<? super
E
> getRenderer()
```

Returns the renderer used to display the selected item in the

JComboBox

field.

**Returns:** the

ListCellRenderer

that displays
the selected item.

- setEditor

```java
@BeanProperty
(
expert
=true,

description
="The editor that combo box uses to edit the current value")
public void setEditor​(
ComboBoxEditor
anEditor)
```

Sets the editor used to paint and edit the selected item in the

JComboBox

field. The editor is used only if the
receiving

JComboBox

is editable. If not editable,
the combo box uses the renderer to paint the selected item.

**Parameters:** anEditor

- the

ComboBoxEditor

that
displays the selected item
**See Also:** setRenderer(javax.swing.ListCellRenderer<? super E>)

- getEditor

```java
public
ComboBoxEditor
getEditor()
```

Returns the editor used to paint and edit the selected item in the

JComboBox

field.

**Returns:** the

ComboBoxEditor

that displays the selected item

- setSelectedItem

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="Sets the selected item in the JComboBox.")
public void setSelectedItem​(
Object
anObject)
```

Sets the selected item in the combo box display area to the object in
the argument.
If

anObject

is in the list, the display area shows

anObject

selected.

If

anObject

is

not

in the list and the combo box is
uneditable, it will not change the current selection. For editable
combo boxes, the selection will change to

anObject

.

If this constitutes a change in the selected item,

ItemListener

s added to the combo box will be notified with
one or two

ItemEvent

s.
If there is a current selected item, an

ItemEvent

will be
fired and the state change will be

ItemEvent.DESELECTED

.
If

anObject

is in the list and is not currently selected
then an

ItemEvent

will be fired and the state change will
be

ItemEvent.SELECTED

.

ActionListener

s added to the combo box will be notified
with an

ActionEvent

when this method is called.

**Parameters:** anObject

- the list object to select; use

null

to
clear the selection

- getSelectedItem

```java
public
Object
getSelectedItem()
```

Returns the current selected item.

If the combo box is editable, then this value may not have been added
to the combo box with

addItem

,

insertItemAt

or the data constructors.

**Returns:** the current selected Object
**See Also:** setSelectedItem(java.lang.Object)

- setSelectedIndex

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The item at index is selected.")
public void setSelectedIndex​(int anIndex)
```

Selects the item at index

anIndex

.

**Parameters:** anIndex

- an integer specifying the list item to select,
where 0 specifies the first item in the list and -1 indicates no selection
**Throws:** IllegalArgumentException

- if

anIndex

< -1 or

anIndex

is greater than or equal to size

- getSelectedIndex

```java
public int getSelectedIndex()
```

Returns the first item in the list that matches the given item.
The result is not always defined if the

JComboBox

allows selected items that are not in the list.
Returns -1 if there is no selected item or if the user specified
an item which is not in the list.

**Returns:** an integer specifying the currently selected list item,
where 0 specifies
the first item in the list;
or -1 if no item is selected or if
the currently selected item is not in the list

- getPrototypeDisplayValue

```java
public
E
getPrototypeDisplayValue()
```

Returns the "prototypical display" value - an Object used
for the calculation of the display height and width.

**Returns:** the value of the

prototypeDisplayValue

property
**Since:** 1.4
**See Also:** setPrototypeDisplayValue(E)

- setPrototypeDisplayValue

```java
@BeanProperty
(
visualUpdate
=true,

description
="The display prototype value, used to compute display width and height.")
public void setPrototypeDisplayValue​(
E
prototypeDisplayValue)
```

Sets the prototype display value used to calculate the size of the display
for the UI portion.

If a prototype display value is specified, the preferred size of
the combo box is calculated by configuring the renderer with the
prototype display value and obtaining its preferred size. Specifying
the preferred display value is often useful when the combo box will be
displaying large amounts of data. If no prototype display value has
been specified, the renderer must be configured for each value from
the model and its preferred size obtained, which can be
relatively expensive.

**Parameters:** prototypeDisplayValue

- the prototype display value
**Since:** 1.4
**See Also:** getPrototypeDisplayValue()

- addItem

```java
public void addItem​(
E
item)
```

Adds an item to the item list.
This method works only if the

JComboBox

uses a
mutable data model.

Warning:

Focus and keyboard navigation problems may arise if you add duplicate
String objects. A workaround is to add new objects instead of String
objects and make sure that the toString() method is defined.
For example:

```java
comboBox.addItem(makeObj("Item 1"));
comboBox.addItem(makeObj("Item 1"));
...
private Object makeObj(final String item) {
return new Object() { public String toString() { return item; } };
}
```

**Parameters:** item

- the item to add to the list
**See Also:** MutableComboBoxModel

- insertItemAt

```java
public void insertItemAt​(
E
item,
int index)
```

Inserts an item into the item list at a given index.
This method works only if the

JComboBox

uses a
mutable data model.

**Parameters:** item

- the item to add to the list
**Parameters:** index

- an integer specifying the position at which
to add the item
**See Also:** MutableComboBoxModel

- removeItem

```java
public void removeItem​(
Object
anObject)
```

Removes an item from the item list.
This method works only if the

JComboBox

uses a
mutable data model.

**Parameters:** anObject

- the object to remove from the item list
**See Also:** MutableComboBoxModel

- removeItemAt

```java
public void removeItemAt​(int anIndex)
```

Removes the item at

anIndex

This method works only if the

JComboBox

uses a
mutable data model.

**Parameters:** anIndex

- an int specifying the index of the item to remove,
where 0
indicates the first item in the list
**See Also:** MutableComboBoxModel

- removeAllItems

```java
public void removeAllItems()
```

Removes all items from the item list.

- showPopup

```java
public void showPopup()
```

Causes the combo box to display its popup window.

**See Also:** setPopupVisible(boolean)

- hidePopup

```java
public void hidePopup()
```

Causes the combo box to close its popup window.

**See Also:** setPopupVisible(boolean)

- setPopupVisible

```java
public void setPopupVisible​(boolean v)
```

Sets the visibility of the popup.

**Parameters:** v

- if

true

shows the popup, otherwise, hides the popup.

- isPopupVisible

```java
public boolean isPopupVisible()
```

Determines the visibility of the popup.

**Returns:** true if the popup is visible, otherwise returns false

- addItemListener

```java
public void addItemListener​(
ItemListener
aListener)
```

Adds an

ItemListener

.

aListener

will receive one or two

ItemEvent

s when
the selected item changes.

**Specified by:** addItemListener

in interface

ItemSelectable
**Parameters:** aListener

- the

ItemListener

that is to be notified
**See Also:** setSelectedItem(java.lang.Object)

- removeItemListener

```java
public void removeItemListener​(
ItemListener
aListener)
```

Removes an

ItemListener

.

**Specified by:** removeItemListener

in interface

ItemSelectable
**Parameters:** aListener

- the

ItemListener

to remove
**See Also:** ItemEvent

- getItemListeners

```java
@BeanProperty
(
bound
=false)
public
ItemListener
[] getItemListeners()
```

Returns an array of all the

ItemListener

s added
to this JComboBox with addItemListener().

**Returns:** all of the

ItemListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- addActionListener

```java
public void addActionListener​(
ActionListener
l)
```

Adds an

ActionListener

.

The

ActionListener

will receive an

ActionEvent

when a selection has been made. If the combo box is editable, then
an

ActionEvent

will be fired when editing has stopped.

**Parameters:** l

- the

ActionListener

that is to be notified
**See Also:** setSelectedItem(java.lang.Object)

- removeActionListener

```java
public void removeActionListener​(
ActionListener
l)
```

Removes an

ActionListener

.

**Parameters:** l

- the

ActionListener

to remove

- getActionListeners

```java
@BeanProperty
(
bound
=false)
public
ActionListener
[] getActionListeners()
```

Returns an array of all the

ActionListener

s added
to this JComboBox with addActionListener().

**Returns:** all of the

ActionListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- addPopupMenuListener

```java
public void addPopupMenuListener​(
PopupMenuListener
l)
```

Adds a

PopupMenu

listener which will listen to notification
messages from the popup portion of the combo box.

For all standard look and feels shipped with Java, the popup list
portion of combo box is implemented as a

JPopupMenu

.
A custom look and feel may not implement it this way and will
therefore not receive the notification.

**Parameters:** l

- the

PopupMenuListener

to add
**Since:** 1.4

- removePopupMenuListener

```java
public void removePopupMenuListener​(
PopupMenuListener
l)
```

Removes a

PopupMenuListener

.

**Parameters:** l

- the

PopupMenuListener

to remove
**Since:** 1.4
**See Also:** addPopupMenuListener(javax.swing.event.PopupMenuListener)

- getPopupMenuListeners

```java
@BeanProperty
(
bound
=false)
public
PopupMenuListener
[] getPopupMenuListeners()
```

Returns an array of all the

PopupMenuListener

s added
to this JComboBox with addPopupMenuListener().

**Returns:** all of the

PopupMenuListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

- firePopupMenuWillBecomeVisible

```java
public void firePopupMenuWillBecomeVisible()
```

Notifies

PopupMenuListener

s that the popup portion of the
combo box will become visible.

This method is public but should not be called by anything other than
the UI delegate.

**Since:** 1.4
**See Also:** addPopupMenuListener(javax.swing.event.PopupMenuListener)

- firePopupMenuWillBecomeInvisible

```java
public void firePopupMenuWillBecomeInvisible()
```

Notifies

PopupMenuListener

s that the popup portion of the
combo box has become invisible.

This method is public but should not be called by anything other than
the UI delegate.

**Since:** 1.4
**See Also:** addPopupMenuListener(javax.swing.event.PopupMenuListener)

- firePopupMenuCanceled

```java
public void firePopupMenuCanceled()
```

Notifies

PopupMenuListener

s that the popup portion of the
combo box has been canceled.

This method is public but should not be called by anything other than
the UI delegate.

**Since:** 1.4
**See Also:** addPopupMenuListener(javax.swing.event.PopupMenuListener)

- setActionCommand

```java
public void setActionCommand​(
String
aCommand)
```

Sets the action command that should be included in the event
sent to action listeners.

**Parameters:** aCommand

- a string containing the "command" that is sent
to action listeners; the same listener can then
do different things depending on the command it
receives

- getActionCommand

```java
public
String
getActionCommand()
```

Returns the action command that is included in the event sent to
action listeners.

**Returns:** the string containing the "command" that is sent
to action listeners.

- setAction

```java
@BeanProperty
(
visualUpdate
=true,

description
="the Action instance connected with this ActionEvent source")
public void setAction​(
Action
a)
```

Sets the

Action

for the

ActionEvent

source.
The new

Action

replaces any previously set

Action

but does not affect

ActionListeners

independently added with

addActionListener

.
If the

Action

is already a registered

ActionListener

for the

ActionEvent

source,
it is not re-registered.

Setting the

Action

results in immediately changing
all the properties described in

Swing Components Supporting

Action

.
Subsequently, the combobox's properties are automatically updated
as the

Action

's properties change.

This method uses three other methods to set
and help track the

Action

's property values.
It uses the

configurePropertiesFromAction

method
to immediately change the combobox's properties.
To track changes in the

Action

's property values,
this method registers the

PropertyChangeListener

returned by

createActionPropertyChangeListener

. The
default

PropertyChangeListener

invokes the

actionPropertyChanged

method when a property in the

Action

changes.

**Parameters:** a

- the

Action

for the

JComboBox

,
or

null

.
**Since:** 1.3
**See Also:** Action

,

getAction()

,

configurePropertiesFromAction(javax.swing.Action)

,

createActionPropertyChangeListener(javax.swing.Action)

,

actionPropertyChanged(javax.swing.Action, java.lang.String)

- getAction

```java
public
Action
getAction()
```

Returns the currently set

Action

for this

ActionEvent

source, or

null

if no

Action

is set.

**Returns:** the

Action

for this

ActionEvent

source; or

null
**Since:** 1.3
**See Also:** Action

,

setAction(javax.swing.Action)

- configurePropertiesFromAction

```java
protected void configurePropertiesFromAction​(
Action
a)
```

Sets the properties on this combobox to match those in the specified

Action

. Refer to

Swing Components Supporting

Action

for more
details as to which properties this sets.

**Parameters:** a

- the

Action

from which to get the properties,
or

null
**Since:** 1.3
**See Also:** Action

,

setAction(javax.swing.Action)

- createActionPropertyChangeListener

```java
protected
PropertyChangeListener
createActionPropertyChangeListener​(
Action
a)
```

Creates and returns a

PropertyChangeListener

that is
responsible for listening for changes from the specified

Action

and updating the appropriate properties.

Warning:

If you subclass this do not create an anonymous
inner class. If you do the lifetime of the combobox will be tied to
that of the

Action

.

**Parameters:** a

- the combobox's action
**Returns:** the

PropertyChangeListener
**Since:** 1.3
**See Also:** Action

,

setAction(javax.swing.Action)

- actionPropertyChanged

```java
protected void actionPropertyChanged​(
Action
action,

String
propertyName)
```

Updates the combobox's state in response to property changes in
associated action. This method is invoked from the

PropertyChangeListener

returned from

createActionPropertyChangeListener

. Subclasses do not normally
need to invoke this. Subclasses that support additional

Action

properties should override this and

configurePropertiesFromAction

.

Refer to the table at

Swing Components Supporting

Action

for a list of
the properties this method sets.

**Parameters:** action

- the

Action

associated with this combobox
**Parameters:** propertyName

- the name of the property that changed
**Since:** 1.6
**See Also:** Action

,

configurePropertiesFromAction(javax.swing.Action)

- fireItemStateChanged

```java
protected void fireItemStateChanged​(
ItemEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type.

**Parameters:** e

- the event of interest
**See Also:** EventListenerList

- fireActionEvent

```java
protected void fireActionEvent()
```

Notifies all listeners that have registered interest for
notification on this event type.

**See Also:** EventListenerList

- selectedItemChanged

```java
protected void selectedItemChanged()
```

This protected method is implementation specific. Do not access directly
or override.

- getSelectedObjects

```java
@BeanProperty
(
bound
=false)
public
Object
[] getSelectedObjects()
```

Returns an array containing the selected item.
This method is implemented for compatibility with

ItemSelectable

.

**Specified by:** getSelectedObjects

in interface

ItemSelectable
**Returns:** an array of

Objects

containing one
element -- the selected item

- actionPerformed

```java
public void actionPerformed​(
ActionEvent
e)
```

This method is public as an implementation side effect.
do not call or override.

**Specified by:** actionPerformed

in interface

ActionListener
**Parameters:** e

- the event to be processed

- contentsChanged

```java
public void contentsChanged​(
ListDataEvent
e)
```

This method is public as an implementation side effect.
do not call or override.

**Specified by:** contentsChanged

in interface

ListDataListener
**Parameters:** e

- a

ListDataEvent

encapsulating the
event information

- intervalAdded

```java
public void intervalAdded​(
ListDataEvent
e)
```

This method is public as an implementation side effect.
do not call or override.

**Specified by:** intervalAdded

in interface

ListDataListener
**Parameters:** e

- a

ListDataEvent

encapsulating the
event information

- intervalRemoved

```java
public void intervalRemoved​(
ListDataEvent
e)
```

This method is public as an implementation side effect.
do not call or override.

**Specified by:** intervalRemoved

in interface

ListDataListener
**Parameters:** e

- a

ListDataEvent

encapsulating the
event information

- selectWithKeyChar

```java
public boolean selectWithKeyChar​(char keyChar)
```

Selects the list item that corresponds to the specified keyboard
character and returns true, if there is an item corresponding
to that character. Otherwise, returns false.

**Parameters:** keyChar

- a char, typically this is a keyboard key
typed by the user
**Returns:** true

if there is an item corresponding to that character.
Otherwise, returns

false

.

- setEnabled

```java
@BeanProperty
(
preferred
=true,

description
="The enabled state of the component.")
public void setEnabled​(boolean b)
```

Enables the combo box so that items can be selected. When the
combo box is disabled, items cannot be selected and values
cannot be typed into its field (if it is editable).

**Overrides:** setEnabled

in class

JComponent
**Parameters:** b

- a boolean value, where true enables the component and
false disables it
**See Also:** Component.isEnabled()

,

Component.isLightweight()

- configureEditor

```java
public void configureEditor​(
ComboBoxEditor
anEditor,

Object
anItem)
```

Initializes the editor with the specified item.

**Parameters:** anEditor

- the

ComboBoxEditor

that displays
the list item in the
combo box field and allows it to be edited
**Parameters:** anItem

- the object to display and edit in the field

- processKeyEvent

```java
public void processKeyEvent​(
KeyEvent
e)
```

Handles

KeyEvent

s, looking for the Tab key.
If the Tab key is found, the popup window is closed.

**Overrides:** processKeyEvent

in class

JComponent
**Parameters:** e

- the

KeyEvent

containing the keyboard
key that was pressed
**See Also:** KeyEvent

,

KeyListener

,

KeyboardFocusManager

,

DefaultKeyboardFocusManager

,

Component.processEvent(java.awt.AWTEvent)

,

Component.dispatchEvent(java.awt.AWTEvent)

,

Component.addKeyListener(java.awt.event.KeyListener)

,

Component.enableEvents(long)

,

Component.isShowing()

- setKeySelectionManager

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The objects that changes the selection when a key is pressed.")
public void setKeySelectionManager​(
JComboBox.KeySelectionManager
aManager)
```

Sets the object that translates a keyboard character into a list
selection. Typically, the first selection with a matching first
character becomes the selected item.

**Parameters:** aManager

- a key selection manager

- getKeySelectionManager

```java
public
JComboBox.KeySelectionManager
getKeySelectionManager()
```

Returns the list's key-selection manager.

**Returns:** the

KeySelectionManager

currently in use

- getItemCount

```java
@BeanProperty
(
bound
=false)
public int getItemCount()
```

Returns the number of items in the list.

**Returns:** an integer equal to the number of items in the list

- getItemAt

```java
public
E
getItemAt​(int index)
```

Returns the list item at the specified index. If

index

is out of range (less than zero or greater than or equal to size)
it will return

null

.

**Parameters:** index

- an integer indicating the list position, where the first
item starts at zero
**Returns:** the item at that list position; or

null

if out of range

- createDefaultKeySelectionManager

```java
protected
JComboBox.KeySelectionManager
createDefaultKeySelectionManager()
```

Returns an instance of the default key-selection manager.

**Returns:** the

KeySelectionManager

currently used by the list
**See Also:** setKeySelectionManager(javax.swing.JComboBox.KeySelectionManager)

- paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JComboBox

.
This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

JComboBox

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

Gets the AccessibleContext associated with this JComboBox.
For combo boxes, the AccessibleContext takes the form of an
AccessibleJComboBox.
A new AccessibleJComboBox instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJComboBox that serves as the
AccessibleContext of this JComboBox

---

#### Method Detail

installAncestorListener

```java
protected void installAncestorListener()
```

Registers ancestor listener so that it will receive

AncestorEvents

when it or any of its ancestors
move or are made visible or invisible.
Events are also sent when the component or its ancestors are added
or removed from the containment hierarchy.

---

#### installAncestorListener

protected void installAncestorListener()

Registers ancestor listener so that it will receive

AncestorEvents

when it or any of its ancestors
move or are made visible or invisible.
Events are also sent when the component or its ancestors are added
or removed from the containment hierarchy.

setUI

```java
@BeanProperty
(
hidden
=true,

visualUpdate
=true,

description
="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(
ComboBoxUI
ui)
```

Sets the L&F object that renders this component.

**Parameters:** ui

- the

ComboBoxUI

L&F object
**See Also:** UIDefaults.getUI(javax.swing.JComponent)

---

#### setUI

@BeanProperty

(

hidden

=true,

visualUpdate

=true,

description

="The UI object that implements the Component\'s LookAndFeel.")
public void setUI​(

ComboBoxUI

ui)

Sets the L&F object that renders this component.

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

JComponent
**Returns:** the string "ComboBoxUI"
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

getUI

```java
public
ComboBoxUI
getUI()
```

Returns the L&F object that renders this component.

**Overrides:** getUI

in class

JComponent
**Returns:** the ComboBoxUI object that renders this component

---

#### getUI

public

ComboBoxUI

getUI()

Returns the L&F object that renders this component.

setModel

```java
@BeanProperty
(
description
="Model that the combo box uses to get data to display.")
public void setModel​(
ComboBoxModel
<
E
> aModel)
```

Sets the data model that the

JComboBox

uses to obtain
the list of items.

**Parameters:** aModel

- the

ComboBoxModel

that provides the
displayed list of items

---

#### setModel

@BeanProperty

(

description

="Model that the combo box uses to get data to display.")
public void setModel​(

ComboBoxModel

<

E

> aModel)

Sets the data model that the

JComboBox

uses to obtain
the list of items.

getModel

```java
public
ComboBoxModel
<
E
> getModel()
```

Returns the data model currently used by the

JComboBox

.

**Returns:** the

ComboBoxModel

that provides the displayed
list of items

---

#### getModel

public

ComboBoxModel

<

E

> getModel()

Returns the data model currently used by the

JComboBox

.

setLightWeightPopupEnabled

```java
@BeanProperty
(
expert
=true,

description
="Set to <code>false</code> to require heavyweight popups.")
public void setLightWeightPopupEnabled​(boolean aFlag)
```

Sets the

lightWeightPopupEnabled

property, which
provides a hint as to whether or not a lightweight

Component

should be used to contain the

JComboBox

, versus a heavyweight

Component

such as a

Panel

or a

Window

. The decision of lightweight
versus heavyweight is ultimately up to the

JComboBox

. Lightweight windows are more
efficient than heavyweight windows, but lightweight
and heavyweight components do not mix well in a GUI.
If your application mixes lightweight and heavyweight
components, you should disable lightweight popups.
The default value for the

lightWeightPopupEnabled

property is

true

, unless otherwise specified
by the look and feel. Some look and feels always use
heavyweight popups, no matter what the value of this property.

See the article

Mixing Heavy and Light Components

This method fires a property changed event.

**Parameters:** aFlag

- if

true

, lightweight popups are desired

---

#### setLightWeightPopupEnabled

@BeanProperty

(

expert

=true,

description

="Set to <code>false</code> to require heavyweight popups.")
public void setLightWeightPopupEnabled​(boolean aFlag)

Sets the

lightWeightPopupEnabled

property, which
provides a hint as to whether or not a lightweight

Component

should be used to contain the

JComboBox

, versus a heavyweight

Component

such as a

Panel

or a

Window

. The decision of lightweight
versus heavyweight is ultimately up to the

JComboBox

. Lightweight windows are more
efficient than heavyweight windows, but lightweight
and heavyweight components do not mix well in a GUI.
If your application mixes lightweight and heavyweight
components, you should disable lightweight popups.
The default value for the

lightWeightPopupEnabled

property is

true

, unless otherwise specified
by the look and feel. Some look and feels always use
heavyweight popups, no matter what the value of this property.

See the article

Mixing Heavy and Light Components

This method fires a property changed event.

See the article

Mixing Heavy and Light Components

This method fires a property changed event.

isLightWeightPopupEnabled

```java
public boolean isLightWeightPopupEnabled()
```

Gets the value of the

lightWeightPopupEnabled

property.

**Returns:** the value of the

lightWeightPopupEnabled

property
**See Also:** setLightWeightPopupEnabled(boolean)

---

#### isLightWeightPopupEnabled

public boolean isLightWeightPopupEnabled()

Gets the value of the

lightWeightPopupEnabled

property.

setEditable

```java
@BeanProperty
(
preferred
=true,

description
="If true, the user can type a new value in the combo box.")
public void setEditable​(boolean aFlag)
```

Determines whether the

JComboBox

field is editable.
An editable

JComboBox

allows the user to type into the
field or selected an item from the list to initialize the field,
after which it can be edited. (The editing affects only the field,
the list item remains intact.) A non editable

JComboBox

displays the selected item in the field,
but the selection cannot be modified.

**Parameters:** aFlag

- a boolean value, where true indicates that the
field is editable

---

#### setEditable

@BeanProperty

(

preferred

=true,

description

="If true, the user can type a new value in the combo box.")
public void setEditable​(boolean aFlag)

Determines whether the

JComboBox

field is editable.
An editable

JComboBox

allows the user to type into the
field or selected an item from the list to initialize the field,
after which it can be edited. (The editing affects only the field,
the list item remains intact.) A non editable

JComboBox

displays the selected item in the field,
but the selection cannot be modified.

isEditable

```java
public boolean isEditable()
```

Returns true if the

JComboBox

is editable.
By default, a combo box is not editable.

**Returns:** true if the

JComboBox

is editable, else false

---

#### isEditable

public boolean isEditable()

Returns true if the

JComboBox

is editable.
By default, a combo box is not editable.

setMaximumRowCount

```java
@BeanProperty
(
preferred
=true,

description
="The maximum number of rows the popup should have")
public void setMaximumRowCount​(int count)
```

Sets the maximum number of rows the

JComboBox

displays.
If the number of objects in the model is greater than count,
the combo box uses a scrollbar.

**Parameters:** count

- an integer specifying the maximum number of items to
display in the list before using a scrollbar

---

#### setMaximumRowCount

@BeanProperty

(

preferred

=true,

description

="The maximum number of rows the popup should have")
public void setMaximumRowCount​(int count)

Sets the maximum number of rows the

JComboBox

displays.
If the number of objects in the model is greater than count,
the combo box uses a scrollbar.

getMaximumRowCount

```java
public int getMaximumRowCount()
```

Returns the maximum number of items the combo box can display
without a scrollbar

**Returns:** an integer specifying the maximum number of items that are
displayed in the list before using a scrollbar

---

#### getMaximumRowCount

public int getMaximumRowCount()

Returns the maximum number of items the combo box can display
without a scrollbar

setRenderer

```java
@BeanProperty
(
expert
=true,

description
="The renderer that paints the item selected in the list.")
public void setRenderer​(
ListCellRenderer
<? super
E
> aRenderer)
```

Sets the renderer that paints the list items and the item selected from the list in
the JComboBox field. The renderer is used if the JComboBox is not
editable. If it is editable, the editor is used to render and edit
the selected item.

The default renderer displays a string or an icon.
Other renderers can handle graphic images and composite items.

To display the selected item,

aRenderer.getListCellRendererComponent

is called, passing the list object and an index of -1.

**Parameters:** aRenderer

- the

ListCellRenderer

that
displays the selected item
**See Also:** setEditor(javax.swing.ComboBoxEditor)

---

#### setRenderer

@BeanProperty

(

expert

=true,

description

="The renderer that paints the item selected in the list.")
public void setRenderer​(

ListCellRenderer

<? super

E

> aRenderer)

Sets the renderer that paints the list items and the item selected from the list in
the JComboBox field. The renderer is used if the JComboBox is not
editable. If it is editable, the editor is used to render and edit
the selected item.

The default renderer displays a string or an icon.
Other renderers can handle graphic images and composite items.

To display the selected item,

aRenderer.getListCellRendererComponent

is called, passing the list object and an index of -1.

The default renderer displays a string or an icon.
Other renderers can handle graphic images and composite items.

To display the selected item,

aRenderer.getListCellRendererComponent

is called, passing the list object and an index of -1.

To display the selected item,

aRenderer.getListCellRendererComponent

is called, passing the list object and an index of -1.

getRenderer

```java
public
ListCellRenderer
<? super
E
> getRenderer()
```

Returns the renderer used to display the selected item in the

JComboBox

field.

**Returns:** the

ListCellRenderer

that displays
the selected item.

---

#### getRenderer

public

ListCellRenderer

<? super

E

> getRenderer()

Returns the renderer used to display the selected item in the

JComboBox

field.

setEditor

```java
@BeanProperty
(
expert
=true,

description
="The editor that combo box uses to edit the current value")
public void setEditor​(
ComboBoxEditor
anEditor)
```

Sets the editor used to paint and edit the selected item in the

JComboBox

field. The editor is used only if the
receiving

JComboBox

is editable. If not editable,
the combo box uses the renderer to paint the selected item.

**Parameters:** anEditor

- the

ComboBoxEditor

that
displays the selected item
**See Also:** setRenderer(javax.swing.ListCellRenderer<? super E>)

---

#### setEditor

@BeanProperty

(

expert

=true,

description

="The editor that combo box uses to edit the current value")
public void setEditor​(

ComboBoxEditor

anEditor)

Sets the editor used to paint and edit the selected item in the

JComboBox

field. The editor is used only if the
receiving

JComboBox

is editable. If not editable,
the combo box uses the renderer to paint the selected item.

getEditor

```java
public
ComboBoxEditor
getEditor()
```

Returns the editor used to paint and edit the selected item in the

JComboBox

field.

**Returns:** the

ComboBoxEditor

that displays the selected item

---

#### getEditor

public

ComboBoxEditor

getEditor()

Returns the editor used to paint and edit the selected item in the

JComboBox

field.

setSelectedItem

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="Sets the selected item in the JComboBox.")
public void setSelectedItem​(
Object
anObject)
```

Sets the selected item in the combo box display area to the object in
the argument.
If

anObject

is in the list, the display area shows

anObject

selected.

If

anObject

is

not

in the list and the combo box is
uneditable, it will not change the current selection. For editable
combo boxes, the selection will change to

anObject

.

If this constitutes a change in the selected item,

ItemListener

s added to the combo box will be notified with
one or two

ItemEvent

s.
If there is a current selected item, an

ItemEvent

will be
fired and the state change will be

ItemEvent.DESELECTED

.
If

anObject

is in the list and is not currently selected
then an

ItemEvent

will be fired and the state change will
be

ItemEvent.SELECTED

.

ActionListener

s added to the combo box will be notified
with an

ActionEvent

when this method is called.

**Parameters:** anObject

- the list object to select; use

null

to
clear the selection

---

#### setSelectedItem

@BeanProperty

(

bound

=false,

preferred

=true,

description

="Sets the selected item in the JComboBox.")
public void setSelectedItem​(

Object

anObject)

Sets the selected item in the combo box display area to the object in
the argument.
If

anObject

is in the list, the display area shows

anObject

selected.

If

anObject

is

not

in the list and the combo box is
uneditable, it will not change the current selection. For editable
combo boxes, the selection will change to

anObject

.

If this constitutes a change in the selected item,

ItemListener

s added to the combo box will be notified with
one or two

ItemEvent

s.
If there is a current selected item, an

ItemEvent

will be
fired and the state change will be

ItemEvent.DESELECTED

.
If

anObject

is in the list and is not currently selected
then an

ItemEvent

will be fired and the state change will
be

ItemEvent.SELECTED

.

ActionListener

s added to the combo box will be notified
with an

ActionEvent

when this method is called.

If

anObject

is

not

in the list and the combo box is
uneditable, it will not change the current selection. For editable
combo boxes, the selection will change to

anObject

.

If this constitutes a change in the selected item,

ItemListener

s added to the combo box will be notified with
one or two

ItemEvent

s.
If there is a current selected item, an

ItemEvent

will be
fired and the state change will be

ItemEvent.DESELECTED

.
If

anObject

is in the list and is not currently selected
then an

ItemEvent

will be fired and the state change will
be

ItemEvent.SELECTED

.

ActionListener

s added to the combo box will be notified
with an

ActionEvent

when this method is called.

If this constitutes a change in the selected item,

ItemListener

s added to the combo box will be notified with
one or two

ItemEvent

s.
If there is a current selected item, an

ItemEvent

will be
fired and the state change will be

ItemEvent.DESELECTED

.
If

anObject

is in the list and is not currently selected
then an

ItemEvent

will be fired and the state change will
be

ItemEvent.SELECTED

.

ActionListener

s added to the combo box will be notified
with an

ActionEvent

when this method is called.

ActionListener

s added to the combo box will be notified
with an

ActionEvent

when this method is called.

getSelectedItem

```java
public
Object
getSelectedItem()
```

Returns the current selected item.

If the combo box is editable, then this value may not have been added
to the combo box with

addItem

,

insertItemAt

or the data constructors.

**Returns:** the current selected Object
**See Also:** setSelectedItem(java.lang.Object)

---

#### getSelectedItem

public

Object

getSelectedItem()

Returns the current selected item.

If the combo box is editable, then this value may not have been added
to the combo box with

addItem

,

insertItemAt

or the data constructors.

If the combo box is editable, then this value may not have been added
to the combo box with

addItem

,

insertItemAt

or the data constructors.

setSelectedIndex

```java
@BeanProperty
(
bound
=false,

preferred
=true,

description
="The item at index is selected.")
public void setSelectedIndex​(int anIndex)
```

Selects the item at index

anIndex

.

**Parameters:** anIndex

- an integer specifying the list item to select,
where 0 specifies the first item in the list and -1 indicates no selection
**Throws:** IllegalArgumentException

- if

anIndex

< -1 or

anIndex

is greater than or equal to size

---

#### setSelectedIndex

@BeanProperty

(

bound

=false,

preferred

=true,

description

="The item at index is selected.")
public void setSelectedIndex​(int anIndex)

Selects the item at index

anIndex

.

getSelectedIndex

```java
public int getSelectedIndex()
```

Returns the first item in the list that matches the given item.
The result is not always defined if the

JComboBox

allows selected items that are not in the list.
Returns -1 if there is no selected item or if the user specified
an item which is not in the list.

**Returns:** an integer specifying the currently selected list item,
where 0 specifies
the first item in the list;
or -1 if no item is selected or if
the currently selected item is not in the list

---

#### getSelectedIndex

public int getSelectedIndex()

Returns the first item in the list that matches the given item.
The result is not always defined if the

JComboBox

allows selected items that are not in the list.
Returns -1 if there is no selected item or if the user specified
an item which is not in the list.

getPrototypeDisplayValue

```java
public
E
getPrototypeDisplayValue()
```

Returns the "prototypical display" value - an Object used
for the calculation of the display height and width.

**Returns:** the value of the

prototypeDisplayValue

property
**Since:** 1.4
**See Also:** setPrototypeDisplayValue(E)

---

#### getPrototypeDisplayValue

public

E

getPrototypeDisplayValue()

Returns the "prototypical display" value - an Object used
for the calculation of the display height and width.

setPrototypeDisplayValue

```java
@BeanProperty
(
visualUpdate
=true,

description
="The display prototype value, used to compute display width and height.")
public void setPrototypeDisplayValue​(
E
prototypeDisplayValue)
```

Sets the prototype display value used to calculate the size of the display
for the UI portion.

If a prototype display value is specified, the preferred size of
the combo box is calculated by configuring the renderer with the
prototype display value and obtaining its preferred size. Specifying
the preferred display value is often useful when the combo box will be
displaying large amounts of data. If no prototype display value has
been specified, the renderer must be configured for each value from
the model and its preferred size obtained, which can be
relatively expensive.

**Parameters:** prototypeDisplayValue

- the prototype display value
**Since:** 1.4
**See Also:** getPrototypeDisplayValue()

---

#### setPrototypeDisplayValue

@BeanProperty

(

visualUpdate

=true,

description

="The display prototype value, used to compute display width and height.")
public void setPrototypeDisplayValue​(

E

prototypeDisplayValue)

Sets the prototype display value used to calculate the size of the display
for the UI portion.

If a prototype display value is specified, the preferred size of
the combo box is calculated by configuring the renderer with the
prototype display value and obtaining its preferred size. Specifying
the preferred display value is often useful when the combo box will be
displaying large amounts of data. If no prototype display value has
been specified, the renderer must be configured for each value from
the model and its preferred size obtained, which can be
relatively expensive.

If a prototype display value is specified, the preferred size of
the combo box is calculated by configuring the renderer with the
prototype display value and obtaining its preferred size. Specifying
the preferred display value is often useful when the combo box will be
displaying large amounts of data. If no prototype display value has
been specified, the renderer must be configured for each value from
the model and its preferred size obtained, which can be
relatively expensive.

addItem

```java
public void addItem​(
E
item)
```

Adds an item to the item list.
This method works only if the

JComboBox

uses a
mutable data model.

Warning:

Focus and keyboard navigation problems may arise if you add duplicate
String objects. A workaround is to add new objects instead of String
objects and make sure that the toString() method is defined.
For example:

```java
comboBox.addItem(makeObj("Item 1"));
comboBox.addItem(makeObj("Item 1"));
...
private Object makeObj(final String item) {
return new Object() { public String toString() { return item; } };
}
```

**Parameters:** item

- the item to add to the list
**See Also:** MutableComboBoxModel

---

#### addItem

public void addItem​(

E

item)

Adds an item to the item list.
This method works only if the

JComboBox

uses a
mutable data model.

Warning:

Focus and keyboard navigation problems may arise if you add duplicate
String objects. A workaround is to add new objects instead of String
objects and make sure that the toString() method is defined.
For example:

```java
comboBox.addItem(makeObj("Item 1"));
comboBox.addItem(makeObj("Item 1"));
...
private Object makeObj(final String item) {
return new Object() { public String toString() { return item; } };
}
```

Warning:

Focus and keyboard navigation problems may arise if you add duplicate
String objects. A workaround is to add new objects instead of String
objects and make sure that the toString() method is defined.
For example:

```java
comboBox.addItem(makeObj("Item 1"));
comboBox.addItem(makeObj("Item 1"));
...
private Object makeObj(final String item) {
return new Object() { public String toString() { return item; } };
}
```

comboBox.addItem(makeObj("Item 1"));
comboBox.addItem(makeObj("Item 1"));
...
private Object makeObj(final String item) {
return new Object() { public String toString() { return item; } };
}

insertItemAt

```java
public void insertItemAt​(
E
item,
int index)
```

Inserts an item into the item list at a given index.
This method works only if the

JComboBox

uses a
mutable data model.

**Parameters:** item

- the item to add to the list
**Parameters:** index

- an integer specifying the position at which
to add the item
**See Also:** MutableComboBoxModel

---

#### insertItemAt

public void insertItemAt​(

E

item,
int index)

Inserts an item into the item list at a given index.
This method works only if the

JComboBox

uses a
mutable data model.

removeItem

```java
public void removeItem​(
Object
anObject)
```

Removes an item from the item list.
This method works only if the

JComboBox

uses a
mutable data model.

**Parameters:** anObject

- the object to remove from the item list
**See Also:** MutableComboBoxModel

---

#### removeItem

public void removeItem​(

Object

anObject)

Removes an item from the item list.
This method works only if the

JComboBox

uses a
mutable data model.

removeItemAt

```java
public void removeItemAt​(int anIndex)
```

Removes the item at

anIndex

This method works only if the

JComboBox

uses a
mutable data model.

**Parameters:** anIndex

- an int specifying the index of the item to remove,
where 0
indicates the first item in the list
**See Also:** MutableComboBoxModel

---

#### removeItemAt

public void removeItemAt​(int anIndex)

Removes the item at

anIndex

This method works only if the

JComboBox

uses a
mutable data model.

removeAllItems

```java
public void removeAllItems()
```

Removes all items from the item list.

---

#### removeAllItems

public void removeAllItems()

Removes all items from the item list.

showPopup

```java
public void showPopup()
```

Causes the combo box to display its popup window.

**See Also:** setPopupVisible(boolean)

---

#### showPopup

public void showPopup()

Causes the combo box to display its popup window.

hidePopup

```java
public void hidePopup()
```

Causes the combo box to close its popup window.

**See Also:** setPopupVisible(boolean)

---

#### hidePopup

public void hidePopup()

Causes the combo box to close its popup window.

setPopupVisible

```java
public void setPopupVisible​(boolean v)
```

Sets the visibility of the popup.

**Parameters:** v

- if

true

shows the popup, otherwise, hides the popup.

---

#### setPopupVisible

public void setPopupVisible​(boolean v)

Sets the visibility of the popup.

isPopupVisible

```java
public boolean isPopupVisible()
```

Determines the visibility of the popup.

**Returns:** true if the popup is visible, otherwise returns false

---

#### isPopupVisible

public boolean isPopupVisible()

Determines the visibility of the popup.

addItemListener

```java
public void addItemListener​(
ItemListener
aListener)
```

Adds an

ItemListener

.

aListener

will receive one or two

ItemEvent

s when
the selected item changes.

**Specified by:** addItemListener

in interface

ItemSelectable
**Parameters:** aListener

- the

ItemListener

that is to be notified
**See Also:** setSelectedItem(java.lang.Object)

---

#### addItemListener

public void addItemListener​(

ItemListener

aListener)

Adds an

ItemListener

.

aListener

will receive one or two

ItemEvent

s when
the selected item changes.

aListener

will receive one or two

ItemEvent

s when
the selected item changes.

removeItemListener

```java
public void removeItemListener​(
ItemListener
aListener)
```

Removes an

ItemListener

.

**Specified by:** removeItemListener

in interface

ItemSelectable
**Parameters:** aListener

- the

ItemListener

to remove
**See Also:** ItemEvent

---

#### removeItemListener

public void removeItemListener​(

ItemListener

aListener)

Removes an

ItemListener

.

getItemListeners

```java
@BeanProperty
(
bound
=false)
public
ItemListener
[] getItemListeners()
```

Returns an array of all the

ItemListener

s added
to this JComboBox with addItemListener().

**Returns:** all of the

ItemListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

---

#### getItemListeners

@BeanProperty

(

bound

=false)
public

ItemListener

[] getItemListeners()

Returns an array of all the

ItemListener

s added
to this JComboBox with addItemListener().

addActionListener

```java
public void addActionListener​(
ActionListener
l)
```

Adds an

ActionListener

.

The

ActionListener

will receive an

ActionEvent

when a selection has been made. If the combo box is editable, then
an

ActionEvent

will be fired when editing has stopped.

**Parameters:** l

- the

ActionListener

that is to be notified
**See Also:** setSelectedItem(java.lang.Object)

---

#### addActionListener

public void addActionListener​(

ActionListener

l)

Adds an

ActionListener

.

The

ActionListener

will receive an

ActionEvent

when a selection has been made. If the combo box is editable, then
an

ActionEvent

will be fired when editing has stopped.

The

ActionListener

will receive an

ActionEvent

when a selection has been made. If the combo box is editable, then
an

ActionEvent

will be fired when editing has stopped.

removeActionListener

```java
public void removeActionListener​(
ActionListener
l)
```

Removes an

ActionListener

.

**Parameters:** l

- the

ActionListener

to remove

---

#### removeActionListener

public void removeActionListener​(

ActionListener

l)

Removes an

ActionListener

.

getActionListeners

```java
@BeanProperty
(
bound
=false)
public
ActionListener
[] getActionListeners()
```

Returns an array of all the

ActionListener

s added
to this JComboBox with addActionListener().

**Returns:** all of the

ActionListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

---

#### getActionListeners

@BeanProperty

(

bound

=false)
public

ActionListener

[] getActionListeners()

Returns an array of all the

ActionListener

s added
to this JComboBox with addActionListener().

addPopupMenuListener

```java
public void addPopupMenuListener​(
PopupMenuListener
l)
```

Adds a

PopupMenu

listener which will listen to notification
messages from the popup portion of the combo box.

For all standard look and feels shipped with Java, the popup list
portion of combo box is implemented as a

JPopupMenu

.
A custom look and feel may not implement it this way and will
therefore not receive the notification.

**Parameters:** l

- the

PopupMenuListener

to add
**Since:** 1.4

---

#### addPopupMenuListener

public void addPopupMenuListener​(

PopupMenuListener

l)

Adds a

PopupMenu

listener which will listen to notification
messages from the popup portion of the combo box.

For all standard look and feels shipped with Java, the popup list
portion of combo box is implemented as a

JPopupMenu

.
A custom look and feel may not implement it this way and will
therefore not receive the notification.

For all standard look and feels shipped with Java, the popup list
portion of combo box is implemented as a

JPopupMenu

.
A custom look and feel may not implement it this way and will
therefore not receive the notification.

removePopupMenuListener

```java
public void removePopupMenuListener​(
PopupMenuListener
l)
```

Removes a

PopupMenuListener

.

**Parameters:** l

- the

PopupMenuListener

to remove
**Since:** 1.4
**See Also:** addPopupMenuListener(javax.swing.event.PopupMenuListener)

---

#### removePopupMenuListener

public void removePopupMenuListener​(

PopupMenuListener

l)

Removes a

PopupMenuListener

.

getPopupMenuListeners

```java
@BeanProperty
(
bound
=false)
public
PopupMenuListener
[] getPopupMenuListeners()
```

Returns an array of all the

PopupMenuListener

s added
to this JComboBox with addPopupMenuListener().

**Returns:** all of the

PopupMenuListener

s added or an empty
array if no listeners have been added
**Since:** 1.4

---

#### getPopupMenuListeners

@BeanProperty

(

bound

=false)
public

PopupMenuListener

[] getPopupMenuListeners()

Returns an array of all the

PopupMenuListener

s added
to this JComboBox with addPopupMenuListener().

firePopupMenuWillBecomeVisible

```java
public void firePopupMenuWillBecomeVisible()
```

Notifies

PopupMenuListener

s that the popup portion of the
combo box will become visible.

This method is public but should not be called by anything other than
the UI delegate.

**Since:** 1.4
**See Also:** addPopupMenuListener(javax.swing.event.PopupMenuListener)

---

#### firePopupMenuWillBecomeVisible

public void firePopupMenuWillBecomeVisible()

Notifies

PopupMenuListener

s that the popup portion of the
combo box will become visible.

This method is public but should not be called by anything other than
the UI delegate.

This method is public but should not be called by anything other than
the UI delegate.

firePopupMenuWillBecomeInvisible

```java
public void firePopupMenuWillBecomeInvisible()
```

Notifies

PopupMenuListener

s that the popup portion of the
combo box has become invisible.

This method is public but should not be called by anything other than
the UI delegate.

**Since:** 1.4
**See Also:** addPopupMenuListener(javax.swing.event.PopupMenuListener)

---

#### firePopupMenuWillBecomeInvisible

public void firePopupMenuWillBecomeInvisible()

Notifies

PopupMenuListener

s that the popup portion of the
combo box has become invisible.

This method is public but should not be called by anything other than
the UI delegate.

This method is public but should not be called by anything other than
the UI delegate.

firePopupMenuCanceled

```java
public void firePopupMenuCanceled()
```

Notifies

PopupMenuListener

s that the popup portion of the
combo box has been canceled.

This method is public but should not be called by anything other than
the UI delegate.

**Since:** 1.4
**See Also:** addPopupMenuListener(javax.swing.event.PopupMenuListener)

---

#### firePopupMenuCanceled

public void firePopupMenuCanceled()

Notifies

PopupMenuListener

s that the popup portion of the
combo box has been canceled.

This method is public but should not be called by anything other than
the UI delegate.

This method is public but should not be called by anything other than
the UI delegate.

setActionCommand

```java
public void setActionCommand​(
String
aCommand)
```

Sets the action command that should be included in the event
sent to action listeners.

**Parameters:** aCommand

- a string containing the "command" that is sent
to action listeners; the same listener can then
do different things depending on the command it
receives

---

#### setActionCommand

public void setActionCommand​(

String

aCommand)

Sets the action command that should be included in the event
sent to action listeners.

getActionCommand

```java
public
String
getActionCommand()
```

Returns the action command that is included in the event sent to
action listeners.

**Returns:** the string containing the "command" that is sent
to action listeners.

---

#### getActionCommand

public

String

getActionCommand()

Returns the action command that is included in the event sent to
action listeners.

setAction

```java
@BeanProperty
(
visualUpdate
=true,

description
="the Action instance connected with this ActionEvent source")
public void setAction​(
Action
a)
```

Sets the

Action

for the

ActionEvent

source.
The new

Action

replaces any previously set

Action

but does not affect

ActionListeners

independently added with

addActionListener

.
If the

Action

is already a registered

ActionListener

for the

ActionEvent

source,
it is not re-registered.

Setting the

Action

results in immediately changing
all the properties described in

Swing Components Supporting

Action

.
Subsequently, the combobox's properties are automatically updated
as the

Action

's properties change.

This method uses three other methods to set
and help track the

Action

's property values.
It uses the

configurePropertiesFromAction

method
to immediately change the combobox's properties.
To track changes in the

Action

's property values,
this method registers the

PropertyChangeListener

returned by

createActionPropertyChangeListener

. The
default

PropertyChangeListener

invokes the

actionPropertyChanged

method when a property in the

Action

changes.

**Parameters:** a

- the

Action

for the

JComboBox

,
or

null

.
**Since:** 1.3
**See Also:** Action

,

getAction()

,

configurePropertiesFromAction(javax.swing.Action)

,

createActionPropertyChangeListener(javax.swing.Action)

,

actionPropertyChanged(javax.swing.Action, java.lang.String)

---

#### setAction

@BeanProperty

(

visualUpdate

=true,

description

="the Action instance connected with this ActionEvent source")
public void setAction​(

Action

a)

Sets the

Action

for the

ActionEvent

source.
The new

Action

replaces any previously set

Action

but does not affect

ActionListeners

independently added with

addActionListener

.
If the

Action

is already a registered

ActionListener

for the

ActionEvent

source,
it is not re-registered.

Setting the

Action

results in immediately changing
all the properties described in

Swing Components Supporting

Action

.
Subsequently, the combobox's properties are automatically updated
as the

Action

's properties change.

This method uses three other methods to set
and help track the

Action

's property values.
It uses the

configurePropertiesFromAction

method
to immediately change the combobox's properties.
To track changes in the

Action

's property values,
this method registers the

PropertyChangeListener

returned by

createActionPropertyChangeListener

. The
default

PropertyChangeListener

invokes the

actionPropertyChanged

method when a property in the

Action

changes.

Setting the

Action

results in immediately changing
all the properties described in

Swing Components Supporting

Action

.
Subsequently, the combobox's properties are automatically updated
as the

Action

's properties change.

This method uses three other methods to set
and help track the

Action

's property values.
It uses the

configurePropertiesFromAction

method
to immediately change the combobox's properties.
To track changes in the

Action

's property values,
this method registers the

PropertyChangeListener

returned by

createActionPropertyChangeListener

. The
default

PropertyChangeListener

invokes the

actionPropertyChanged

method when a property in the

Action

changes.

This method uses three other methods to set
and help track the

Action

's property values.
It uses the

configurePropertiesFromAction

method
to immediately change the combobox's properties.
To track changes in the

Action

's property values,
this method registers the

PropertyChangeListener

returned by

createActionPropertyChangeListener

. The
default

PropertyChangeListener

invokes the

actionPropertyChanged

method when a property in the

Action

changes.

getAction

```java
public
Action
getAction()
```

Returns the currently set

Action

for this

ActionEvent

source, or

null

if no

Action

is set.

**Returns:** the

Action

for this

ActionEvent

source; or

null
**Since:** 1.3
**See Also:** Action

,

setAction(javax.swing.Action)

---

#### getAction

public

Action

getAction()

Returns the currently set

Action

for this

ActionEvent

source, or

null

if no

Action

is set.

configurePropertiesFromAction

```java
protected void configurePropertiesFromAction​(
Action
a)
```

Sets the properties on this combobox to match those in the specified

Action

. Refer to

Swing Components Supporting

Action

for more
details as to which properties this sets.

**Parameters:** a

- the

Action

from which to get the properties,
or

null
**Since:** 1.3
**See Also:** Action

,

setAction(javax.swing.Action)

---

#### configurePropertiesFromAction

protected void configurePropertiesFromAction​(

Action

a)

Sets the properties on this combobox to match those in the specified

Action

. Refer to

Swing Components Supporting

Action

for more
details as to which properties this sets.

createActionPropertyChangeListener

```java
protected
PropertyChangeListener
createActionPropertyChangeListener​(
Action
a)
```

Creates and returns a

PropertyChangeListener

that is
responsible for listening for changes from the specified

Action

and updating the appropriate properties.

Warning:

If you subclass this do not create an anonymous
inner class. If you do the lifetime of the combobox will be tied to
that of the

Action

.

**Parameters:** a

- the combobox's action
**Returns:** the

PropertyChangeListener
**Since:** 1.3
**See Also:** Action

,

setAction(javax.swing.Action)

---

#### createActionPropertyChangeListener

protected

PropertyChangeListener

createActionPropertyChangeListener​(

Action

a)

Creates and returns a

PropertyChangeListener

that is
responsible for listening for changes from the specified

Action

and updating the appropriate properties.

Warning:

If you subclass this do not create an anonymous
inner class. If you do the lifetime of the combobox will be tied to
that of the

Action

.

Warning:

If you subclass this do not create an anonymous
inner class. If you do the lifetime of the combobox will be tied to
that of the

Action

.

actionPropertyChanged

```java
protected void actionPropertyChanged​(
Action
action,

String
propertyName)
```

Updates the combobox's state in response to property changes in
associated action. This method is invoked from the

PropertyChangeListener

returned from

createActionPropertyChangeListener

. Subclasses do not normally
need to invoke this. Subclasses that support additional

Action

properties should override this and

configurePropertiesFromAction

.

Refer to the table at

Swing Components Supporting

Action

for a list of
the properties this method sets.

**Parameters:** action

- the

Action

associated with this combobox
**Parameters:** propertyName

- the name of the property that changed
**Since:** 1.6
**See Also:** Action

,

configurePropertiesFromAction(javax.swing.Action)

---

#### actionPropertyChanged

protected void actionPropertyChanged​(

Action

action,

String

propertyName)

Updates the combobox's state in response to property changes in
associated action. This method is invoked from the

PropertyChangeListener

returned from

createActionPropertyChangeListener

. Subclasses do not normally
need to invoke this. Subclasses that support additional

Action

properties should override this and

configurePropertiesFromAction

.

Refer to the table at

Swing Components Supporting

Action

for a list of
the properties this method sets.

Refer to the table at

Swing Components Supporting

Action

for a list of
the properties this method sets.

fireItemStateChanged

```java
protected void fireItemStateChanged​(
ItemEvent
e)
```

Notifies all listeners that have registered interest for
notification on this event type.

**Parameters:** e

- the event of interest
**See Also:** EventListenerList

---

#### fireItemStateChanged

protected void fireItemStateChanged​(

ItemEvent

e)

Notifies all listeners that have registered interest for
notification on this event type.

fireActionEvent

```java
protected void fireActionEvent()
```

Notifies all listeners that have registered interest for
notification on this event type.

**See Also:** EventListenerList

---

#### fireActionEvent

protected void fireActionEvent()

Notifies all listeners that have registered interest for
notification on this event type.

selectedItemChanged

```java
protected void selectedItemChanged()
```

This protected method is implementation specific. Do not access directly
or override.

---

#### selectedItemChanged

protected void selectedItemChanged()

This protected method is implementation specific. Do not access directly
or override.

getSelectedObjects

```java
@BeanProperty
(
bound
=false)
public
Object
[] getSelectedObjects()
```

Returns an array containing the selected item.
This method is implemented for compatibility with

ItemSelectable

.

**Specified by:** getSelectedObjects

in interface

ItemSelectable
**Returns:** an array of

Objects

containing one
element -- the selected item

---

#### getSelectedObjects

@BeanProperty

(

bound

=false)
public

Object

[] getSelectedObjects()

Returns an array containing the selected item.
This method is implemented for compatibility with

ItemSelectable

.

actionPerformed

```java
public void actionPerformed​(
ActionEvent
e)
```

This method is public as an implementation side effect.
do not call or override.

**Specified by:** actionPerformed

in interface

ActionListener
**Parameters:** e

- the event to be processed

---

#### actionPerformed

public void actionPerformed​(

ActionEvent

e)

This method is public as an implementation side effect.
do not call or override.

contentsChanged

```java
public void contentsChanged​(
ListDataEvent
e)
```

This method is public as an implementation side effect.
do not call or override.

**Specified by:** contentsChanged

in interface

ListDataListener
**Parameters:** e

- a

ListDataEvent

encapsulating the
event information

---

#### contentsChanged

public void contentsChanged​(

ListDataEvent

e)

This method is public as an implementation side effect.
do not call or override.

intervalAdded

```java
public void intervalAdded​(
ListDataEvent
e)
```

This method is public as an implementation side effect.
do not call or override.

**Specified by:** intervalAdded

in interface

ListDataListener
**Parameters:** e

- a

ListDataEvent

encapsulating the
event information

---

#### intervalAdded

public void intervalAdded​(

ListDataEvent

e)

This method is public as an implementation side effect.
do not call or override.

intervalRemoved

```java
public void intervalRemoved​(
ListDataEvent
e)
```

This method is public as an implementation side effect.
do not call or override.

**Specified by:** intervalRemoved

in interface

ListDataListener
**Parameters:** e

- a

ListDataEvent

encapsulating the
event information

---

#### intervalRemoved

public void intervalRemoved​(

ListDataEvent

e)

This method is public as an implementation side effect.
do not call or override.

selectWithKeyChar

```java
public boolean selectWithKeyChar​(char keyChar)
```

Selects the list item that corresponds to the specified keyboard
character and returns true, if there is an item corresponding
to that character. Otherwise, returns false.

**Parameters:** keyChar

- a char, typically this is a keyboard key
typed by the user
**Returns:** true

if there is an item corresponding to that character.
Otherwise, returns

false

.

---

#### selectWithKeyChar

public boolean selectWithKeyChar​(char keyChar)

Selects the list item that corresponds to the specified keyboard
character and returns true, if there is an item corresponding
to that character. Otherwise, returns false.

setEnabled

```java
@BeanProperty
(
preferred
=true,

description
="The enabled state of the component.")
public void setEnabled​(boolean b)
```

Enables the combo box so that items can be selected. When the
combo box is disabled, items cannot be selected and values
cannot be typed into its field (if it is editable).

**Overrides:** setEnabled

in class

JComponent
**Parameters:** b

- a boolean value, where true enables the component and
false disables it
**See Also:** Component.isEnabled()

,

Component.isLightweight()

---

#### setEnabled

@BeanProperty

(

preferred

=true,

description

="The enabled state of the component.")
public void setEnabled​(boolean b)

Enables the combo box so that items can be selected. When the
combo box is disabled, items cannot be selected and values
cannot be typed into its field (if it is editable).

configureEditor

```java
public void configureEditor​(
ComboBoxEditor
anEditor,

Object
anItem)
```

Initializes the editor with the specified item.

**Parameters:** anEditor

- the

ComboBoxEditor

that displays
the list item in the
combo box field and allows it to be edited
**Parameters:** anItem

- the object to display and edit in the field

---

#### configureEditor

public void configureEditor​(

ComboBoxEditor

anEditor,

Object

anItem)

Initializes the editor with the specified item.

processKeyEvent

```java
public void processKeyEvent​(
KeyEvent
e)
```

Handles

KeyEvent

s, looking for the Tab key.
If the Tab key is found, the popup window is closed.

**Overrides:** processKeyEvent

in class

JComponent
**Parameters:** e

- the

KeyEvent

containing the keyboard
key that was pressed
**See Also:** KeyEvent

,

KeyListener

,

KeyboardFocusManager

,

DefaultKeyboardFocusManager

,

Component.processEvent(java.awt.AWTEvent)

,

Component.dispatchEvent(java.awt.AWTEvent)

,

Component.addKeyListener(java.awt.event.KeyListener)

,

Component.enableEvents(long)

,

Component.isShowing()

---

#### processKeyEvent

public void processKeyEvent​(

KeyEvent

e)

Handles

KeyEvent

s, looking for the Tab key.
If the Tab key is found, the popup window is closed.

setKeySelectionManager

```java
@BeanProperty
(
bound
=false,

expert
=true,

description
="The objects that changes the selection when a key is pressed.")
public void setKeySelectionManager​(
JComboBox.KeySelectionManager
aManager)
```

Sets the object that translates a keyboard character into a list
selection. Typically, the first selection with a matching first
character becomes the selected item.

**Parameters:** aManager

- a key selection manager

---

#### setKeySelectionManager

@BeanProperty

(

bound

=false,

expert

=true,

description

="The objects that changes the selection when a key is pressed.")
public void setKeySelectionManager​(

JComboBox.KeySelectionManager

aManager)

Sets the object that translates a keyboard character into a list
selection. Typically, the first selection with a matching first
character becomes the selected item.

getKeySelectionManager

```java
public
JComboBox.KeySelectionManager
getKeySelectionManager()
```

Returns the list's key-selection manager.

**Returns:** the

KeySelectionManager

currently in use

---

#### getKeySelectionManager

public

JComboBox.KeySelectionManager

getKeySelectionManager()

Returns the list's key-selection manager.

getItemCount

```java
@BeanProperty
(
bound
=false)
public int getItemCount()
```

Returns the number of items in the list.

**Returns:** an integer equal to the number of items in the list

---

#### getItemCount

@BeanProperty

(

bound

=false)
public int getItemCount()

Returns the number of items in the list.

getItemAt

```java
public
E
getItemAt​(int index)
```

Returns the list item at the specified index. If

index

is out of range (less than zero or greater than or equal to size)
it will return

null

.

**Parameters:** index

- an integer indicating the list position, where the first
item starts at zero
**Returns:** the item at that list position; or

null

if out of range

---

#### getItemAt

public

E

getItemAt​(int index)

Returns the list item at the specified index. If

index

is out of range (less than zero or greater than or equal to size)
it will return

null

.

createDefaultKeySelectionManager

```java
protected
JComboBox.KeySelectionManager
createDefaultKeySelectionManager()
```

Returns an instance of the default key-selection manager.

**Returns:** the

KeySelectionManager

currently used by the list
**See Also:** setKeySelectionManager(javax.swing.JComboBox.KeySelectionManager)

---

#### createDefaultKeySelectionManager

protected

JComboBox.KeySelectionManager

createDefaultKeySelectionManager()

Returns an instance of the default key-selection manager.

paramString

```java
protected
String
paramString()
```

Returns a string representation of this

JComboBox

.
This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary between
implementations. The returned string may be empty but may not
be

null

.

**Overrides:** paramString

in class

JComponent
**Returns:** a string representation of this

JComboBox

---

#### paramString

protected

String

paramString()

Returns a string representation of this

JComboBox

.
This method is intended to be used only for debugging purposes,
and the content and format of the returned string may vary between
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

Gets the AccessibleContext associated with this JComboBox.
For combo boxes, the AccessibleContext takes the form of an
AccessibleJComboBox.
A new AccessibleJComboBox instance is created if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an AccessibleJComboBox that serves as the
AccessibleContext of this JComboBox

---

#### getAccessibleContext

@BeanProperty

(

bound

=false)
public

AccessibleContext

getAccessibleContext()

Gets the AccessibleContext associated with this JComboBox.
For combo boxes, the AccessibleContext takes the form of an
AccessibleJComboBox.
A new AccessibleJComboBox instance is created if necessary.

---

