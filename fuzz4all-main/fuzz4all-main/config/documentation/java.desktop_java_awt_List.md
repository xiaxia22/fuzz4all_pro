# Class List

**Source:** `java.desktop\java\awt\List.html`

### Class Description

```java
public class
List

extends
Component

implements
ItemSelectable
,
Accessible
```

The

List

component presents the user with a
scrolling list of text items. The list can be set up so that
the user can choose either one item or multiple items.

For example, the code . . .

```java
List lst = new List(4, false);
lst.add("Mercury");
lst.add("Venus");
lst.add("Earth");
lst.add("JavaSoft");
lst.add("Mars");
lst.add("Jupiter");
lst.add("Saturn");
lst.add("Uranus");
lst.add("Neptune");
lst.add("Pluto");
cnt.add(lst);
```

where

cnt

is a container, produces the following
scrolling list:

If the List allows multiple selections, then clicking on
an item that is already selected deselects it. In the preceding
example, only one item from the scrolling list can be selected
at a time, since the second argument when creating the new scrolling
list is

false

. If the List does not allow multiple
selections, selecting an item causes any other selected item
to be deselected.

Note that the list in the example shown was created with four visible
rows. Once the list has been created, the number of visible rows
cannot be changed. A default

List

is created with
four rows, so that

lst = new List()

is equivalent to

list = new List(4, false)

.

Beginning with Java 1.1, the Abstract Window Toolkit
sends the

List

object all mouse, keyboard, and focus events
that occur over it. (The old AWT event model is being maintained
only for backwards compatibility, and its use is discouraged.)

When an item is selected or deselected by the user, AWT sends an instance
of

ItemEvent

to the list.
When the user double-clicks on an item in a scrolling list,
AWT sends an instance of

ActionEvent

to the
list following the item event. AWT also generates an action event
when the user presses the return key while an item in the
list is selected.

If an application wants to perform some action based on an item
in this list being selected or activated by the user, it should implement

ItemListener

or

ActionListener

as appropriate and register the new listener to receive
events from this list.

For multiple-selection scrolling lists, it is considered a better
user interface to use an external gesture (such as clicking on a
button) to trigger the action.

**All Implemented Interfaces:** ImageObserver

,

ItemSelectable

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

#### public List()
throws
HeadlessException

Creates a new scrolling list.
By default, there are four visible lines and multiple selections are
not allowed. Note that this is a convenience method for

List(0, false)

. Also note that the number of visible
lines in the list cannot be changed after it has been created.

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.

**See Also:**
- GraphicsEnvironment.isHeadless()

---

#### public List​(int rows)
throws
HeadlessException

Creates a new scrolling list initialized with the specified
number of visible lines. By default, multiple selections are
not allowed. Note that this is a convenience method for

List(rows, false)

. Also note that the number
of visible rows in the list cannot be changed after it has
been created.

**Parameters:**
- rows

- the number of items to show.

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.

**See Also:**
- GraphicsEnvironment.isHeadless()

**Since:**
- 1.1

---

#### public List​(int rows,
boolean multipleMode)
throws
HeadlessException

Creates a new scrolling list initialized to display the specified
number of rows. Note that if zero rows are specified, then
the list will be created with a default of four rows.
Also note that the number of visible rows in the list cannot
be changed after it has been created.
If the value of

multipleMode

is

true

, then the user can select multiple items from
the list. If it is

false

, only one item at a time
can be selected.

**Parameters:**
- rows

- the number of items to show.
- multipleMode

- if

true

,
then multiple selections are allowed;
otherwise, only one item can be selected at a time.

**Throws:**
- HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.

**See Also:**
- GraphicsEnvironment.isHeadless()

---

### Method Details

#### public void addNotify()

Creates the peer for the list. The peer allows us to modify the
list's appearance without changing its functionality.

**Overrides:**
- addNotify

in class

Component

**See Also:**
- Component.isDisplayable()

,

Component.removeNotify()

,

Component.invalidate()

---

#### public void removeNotify()

Removes the peer for this list. The peer allows us to modify the
list's appearance without changing its functionality.

**Overrides:**
- removeNotify

in class

Component

**See Also:**
- Component.isDisplayable()

,

Component.addNotify()

---

#### public int getItemCount()

Gets the number of items in the list.

**Returns:**
- the number of items in the list

**See Also:**
- getItem(int)

**Since:**
- 1.1

---

#### @Deprecated

public int countItems()

Returns the number of items in the list.

**Returns:**
- the number of items in the list

---

#### public
String
getItem​(int index)

Gets the item associated with the specified index.

**Parameters:**
- index

- the position of the item

**Returns:**
- an item that is associated with
the specified index

**See Also:**
- getItemCount()

---

#### public
String
[] getItems()

Gets the items in the list.

**Returns:**
- a string array containing items of the list

**See Also:**
- select(int)

,

deselect(int)

,

isIndexSelected(int)

**Since:**
- 1.1

---

#### public void add​(
String
item)

Adds the specified item to the end of scrolling list.

**Parameters:**
- item

- the item to be added

**Since:**
- 1.1

---

#### @Deprecated

public void addItem​(
String
item)

Adds the specified item to the end of the list.

**Parameters:**
- item

- the item to be added

---

#### public void add​(
String
item,
int index)

Adds the specified item to the scrolling list
at the position indicated by the index. The index is
zero-based. If the value of the index is less than zero,
or if the value of the index is greater than or equal to
the number of items in the list, then the item is added
to the end of the list.

**Parameters:**
- item

- the item to be added;
if this parameter is

null

then the item is
treated as an empty string,

""
- index

- the position at which to add the item

**Since:**
- 1.1

---

#### @Deprecated

public void addItem​(
String
item,
int index)

Adds the specified item to the list
at the position indicated by the index.

**Parameters:**
- item

- the item to be added
- index

- the position at which to add the item

---

#### public void replaceItem​(
String
newValue,
int index)

Replaces the item at the specified index in the scrolling list
with the new string.

**Parameters:**
- newValue

- a new string to replace an existing item
- index

- the position of the item to replace

**Throws:**
- ArrayIndexOutOfBoundsException

- if

index

is out of range

---

#### public void removeAll()

Removes all items from this list.

**See Also:**
- remove(java.lang.String)

,

delItems(int, int)

**Since:**
- 1.1

---

#### @Deprecated

public void clear()

*No description found.*

---

#### public void remove​(
String
item)

Removes the first occurrence of an item from the list.
If the specified item is selected, and is the only selected
item in the list, the list is set to have no selection.

**Parameters:**
- item

- the item to remove from the list

**Throws:**
- IllegalArgumentException

- if the item doesn't exist in the list

**Since:**
- 1.1

---

#### public void remove​(int position)

Removes the item at the specified position
from this scrolling list.
If the item with the specified position is selected, and is the
only selected item in the list, the list is set to have no selection.

**Parameters:**
- position

- the index of the item to delete

**Throws:**
- ArrayIndexOutOfBoundsException

- if the

position

is less than 0 or
greater than

getItemCount()-1

**See Also:**
- add(String, int)

**Since:**
- 1.1

---

#### @Deprecated

public void delItem​(int position)

Removes the item at the specified position.

**Parameters:**
- position

- the index of the item to delete

---

#### public int getSelectedIndex()

Gets the index of the selected item on the list,

**Returns:**
- the index of the selected item;
if no item is selected, or if multiple items are
selected,

-1

is returned.

**See Also:**
- select(int)

,

deselect(int)

,

isIndexSelected(int)

---

#### public int[] getSelectedIndexes()

Gets the selected indexes on the list.

**Returns:**
- an array of the selected indexes on this scrolling list;
if no item is selected, a zero-length array is returned.

**See Also:**
- select(int)

,

deselect(int)

,

isIndexSelected(int)

---

#### public
String
getSelectedItem()

Gets the selected item on this scrolling list.

**Returns:**
- the selected item on the list;
if no item is selected, or if multiple items are
selected,

null

is returned.

**See Also:**
- select(int)

,

deselect(int)

,

isIndexSelected(int)

---

#### public
String
[] getSelectedItems()

Gets the selected items on this scrolling list.

**Returns:**
- an array of the selected items on this scrolling list;
if no item is selected, a zero-length array is returned.

**See Also:**
- select(int)

,

deselect(int)

,

isIndexSelected(int)

---

#### public
Object
[] getSelectedObjects()

Gets the selected items on this scrolling list in an array of Objects.

**Specified by:**
- getSelectedObjects

in interface

ItemSelectable

**Returns:**
- an array of

Object

s representing the
selected items on this scrolling list;
if no item is selected, a zero-length array is returned.

**See Also:**
- getSelectedItems()

,

ItemSelectable

---

#### public void select​(int index)

Selects the item at the specified index in the scrolling list.

Note that passing out of range parameters is invalid,
and will result in unspecified behavior.

Note that this method should be primarily used to
initially select an item in this component.
Programmatically calling this method will

not

trigger
an

ItemEvent

. The only way to trigger an

ItemEvent

is by user interaction.

**Parameters:**
- index

- the position of the item to select

**See Also:**
- getSelectedItem()

,

deselect(int)

,

isIndexSelected(int)

---

#### public void deselect​(int index)

Deselects the item at the specified index.

Note that passing out of range parameters is invalid,
and will result in unspecified behavior.

If the item at the specified index is not selected,
then the operation is ignored.

**Parameters:**
- index

- the position of the item to deselect

**See Also:**
- select(int)

,

getSelectedItem()

,

isIndexSelected(int)

---

#### public boolean isIndexSelected​(int index)

Determines if the specified item in this scrolling list is
selected.

**Parameters:**
- index

- the item to be checked

**Returns:**
- true

if the specified item has been
selected;

false

otherwise

**See Also:**
- select(int)

,

deselect(int)

**Since:**
- 1.1

---

#### @Deprecated

public boolean isSelected​(int index)

Determines if the specified item in the list is selected.

**Parameters:**
- index

- specifies the item to be checked

**Returns:**
- true

if the item is selected; otherwise

false

---

#### public int getRows()

Gets the number of visible lines in this list. Note that
once the

List

has been created, this number
will never change.

**Returns:**
- the number of visible lines in this scrolling list

---

#### public boolean isMultipleMode()

Determines whether this list allows multiple selections.

**Returns:**
- true

if this list allows multiple
selections; otherwise,

false

**See Also:**
- setMultipleMode(boolean)

**Since:**
- 1.1

---

#### @Deprecated

public boolean allowsMultipleSelections()

Determines whether this list allows multiple selections.

**Returns:**
- true

if this list allows multiple
selections; otherwise

false

---

#### public void setMultipleMode​(boolean b)

Sets the flag that determines whether this list
allows multiple selections.
When the selection mode is changed from multiple-selection to
single-selection, the selected items change as follows:
If a selected item has the location cursor, only that
item will remain selected. If no selected item has the
location cursor, all items will be deselected.

**Parameters:**
- b

- if

true

then multiple selections
are allowed; otherwise, only one item from
the list can be selected at once

**See Also:**
- isMultipleMode()

**Since:**
- 1.1

---

#### @Deprecated

public void setMultipleSelections​(boolean b)

Enables or disables multiple selection mode for this list.

**Parameters:**
- b

-

true

to enable multiple mode,

false

otherwise

---

#### public int getVisibleIndex()

Gets the index of the item that was last made visible by
the method

makeVisible

.

**Returns:**
- the index of the item that was last made visible

**See Also:**
- makeVisible(int)

---

#### public void makeVisible​(int index)

Makes the item at the specified index visible.

**Parameters:**
- index

- the position of the item

**See Also:**
- getVisibleIndex()

---

#### public
Dimension
getPreferredSize​(int rows)

Gets the preferred dimensions for a list with the specified
number of rows.

**Parameters:**
- rows

- number of rows in the list

**Returns:**
- the preferred dimensions for displaying this scrolling list
given that the specified number of rows must be visible

**See Also:**
- Component.getPreferredSize()

**Since:**
- 1.1

---

#### @Deprecated

public
Dimension
preferredSize​(int rows)

Returns the preferred size of this component
assuming it has the specified number of rows.

**Parameters:**
- rows

- the number of rows

**Returns:**
- the preferred dimensions for displaying this list

---

#### public
Dimension
getPreferredSize()

Gets the preferred size of this scrolling list.

**Overrides:**
- getPreferredSize

in class

Component

**Returns:**
- the preferred dimensions for displaying this scrolling list

**See Also:**
- Component.getPreferredSize()

**Since:**
- 1.1

---

#### @Deprecated

public
Dimension
preferredSize()

Description copied from class:

Component

**Overrides:**
- preferredSize

in class

Component

**Returns:**
- the component's preferred size

---

#### public
Dimension
getMinimumSize​(int rows)

Gets the minimum dimensions for a list with the specified
number of rows.

**Parameters:**
- rows

- number of rows in the list

**Returns:**
- the minimum dimensions for displaying this scrolling list
given that the specified number of rows must be visible

**See Also:**
- Component.getMinimumSize()

**Since:**
- 1.1

---

#### @Deprecated

public
Dimension
minimumSize​(int rows)

Returns the minimum dimensions for the list
with the specified number of rows.

**Parameters:**
- rows

- the number of rows in the list

**Returns:**
- the minimum dimensions for displaying this list

---

#### public
Dimension
getMinimumSize()

Determines the minimum size of this scrolling list.

**Overrides:**
- getMinimumSize

in class

Component

**Returns:**
- the minimum dimensions needed
to display this scrolling list

**See Also:**
- Component.getMinimumSize()

**Since:**
- 1.1

---

#### @Deprecated

public
Dimension
minimumSize()

Description copied from class:

Component

**Overrides:**
- minimumSize

in class

Component

**Returns:**
- the minimum size of this component

---

#### public void addItemListener​(
ItemListener
l)

Adds the specified item listener to receive item events from
this list. Item events are sent in response to user input, but not
in response to calls to

select

or

deselect

.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:**
- addItemListener

in interface

ItemSelectable

**Parameters:**
- l

- the item listener

**See Also:**
- removeItemListener(java.awt.event.ItemListener)

,

getItemListeners()

,

select(int)

,

deselect(int)

,

ItemEvent

,

ItemListener

**Since:**
- 1.1

---

#### public void removeItemListener​(
ItemListener
l)

Removes the specified item listener so that it no longer
receives item events from this list.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:**
- removeItemListener

in interface

ItemSelectable

**Parameters:**
- l

- the item listener

**See Also:**
- addItemListener(java.awt.event.ItemListener)

,

getItemListeners()

,

ItemEvent

,

ItemListener

**Since:**
- 1.1

---

#### public
ItemListener
[] getItemListeners()

Returns an array of all the item listeners
registered on this list.

**Returns:**
- all of this list's

ItemListener

s
or an empty array if no item
listeners are currently registered

**See Also:**
- addItemListener(java.awt.event.ItemListener)

,

removeItemListener(java.awt.event.ItemListener)

,

ItemEvent

,

ItemListener

**Since:**
- 1.4

---

#### public void addActionListener​(
ActionListener
l)

Adds the specified action listener to receive action events from
this list. Action events occur when a user double-clicks
on a list item or types Enter when the list has the keyboard
focus.

If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the action listener

**See Also:**
- removeActionListener(java.awt.event.ActionListener)

,

getActionListeners()

,

ActionEvent

,

ActionListener

**Since:**
- 1.1

---

#### public void removeActionListener​(
ActionListener
l)

Removes the specified action listener so that it no longer
receives action events from this list. Action events
occur when a user double-clicks on a list item.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:**
- l

- the action listener

**See Also:**
- addActionListener(java.awt.event.ActionListener)

,

getActionListeners()

,

ActionEvent

,

ActionListener

**Since:**
- 1.1

---

#### public
ActionListener
[] getActionListeners()

Returns an array of all the action listeners
registered on this list.

**Returns:**
- all of this list's

ActionListener

s
or an empty array if no action
listeners are currently registered

**See Also:**
- addActionListener(java.awt.event.ActionListener)

,

removeActionListener(java.awt.event.ActionListener)

,

ActionEvent

,

ActionListener

**Since:**
- 1.4

---

#### public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

List

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

List l

for its item listeners with the following code:

```java
ItemListener[] ils = (ItemListener[])(l.getListeners(ItemListener.class));
```

If no such listeners exist, this method returns an empty array.

**Overrides:**
- getListeners

in class

Component

**Parameters:**
- listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener

**Returns:**
- an array of all objects registered as

Foo

Listener

s on this list,
or an empty array if no such
listeners have been added

**Throws:**
- ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener

**See Also:**
- getItemListeners()

**Since:**
- 1.3

**Type Parameters:**
- T

- the type of the listeners

---

#### protected void processEvent​(
AWTEvent
e)

Processes events on this scrolling list. If an event is
an instance of

ItemEvent

, it invokes the

processItemEvent

method. Else, if the
event is an instance of

ActionEvent

,
it invokes

processActionEvent

.
If the event is not an item event or an action event,
it invokes

processEvent

on the superclass.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:**
- processEvent

in class

Component

**Parameters:**
- e

- the event

**See Also:**
- ActionEvent

,

ItemEvent

,

processActionEvent(java.awt.event.ActionEvent)

,

processItemEvent(java.awt.event.ItemEvent)

**Since:**
- 1.1

---

#### protected void processItemEvent​(
ItemEvent
e)

Processes item events occurring on this list by
dispatching them to any registered

ItemListener

objects.

This method is not called unless item events are
enabled for this component. Item events are enabled
when one of the following occurs:

- An

ItemListener

object is registered
via

addItemListener

.

Item events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:**
- e

- the item event

**See Also:**
- ItemEvent

,

ItemListener

,

addItemListener(java.awt.event.ItemListener)

,

Component.enableEvents(long)

**Since:**
- 1.1

---

#### protected void processActionEvent​(
ActionEvent
e)

Processes action events occurring on this component
by dispatching them to any registered

ActionListener

objects.

This method is not called unless action events are
enabled for this component. Action events are enabled
when one of the following occurs:

- An

ActionListener

object is registered
via

addActionListener

.

Action events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:**
- e

- the action event

**See Also:**
- ActionEvent

,

ActionListener

,

addActionListener(java.awt.event.ActionListener)

,

Component.enableEvents(long)

**Since:**
- 1.1

---

#### protected
String
paramString()

Returns the parameter string representing the state of this
scrolling list. This string is useful for debugging.

**Overrides:**
- paramString

in class

Component

**Returns:**
- the parameter string of this scrolling list

---

#### @Deprecated

public void delItems​(int start,
int end)

Deletes the list items in the specified index range.

**Parameters:**
- start

- the beginning index of the range to delete
- end

- the ending index of the range to delete

---

#### public
AccessibleContext
getAccessibleContext()

Gets the

AccessibleContext

associated with this

List

. For lists, the

AccessibleContext

takes the form of an

AccessibleAWTList

.
A new

AccessibleAWTList

instance is created, if necessary.

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

AccessibleAWTList

that serves as the

AccessibleContext

of this

List

**Since:**
- 1.3

---

### Additional Sections

#### Class List

java.lang.Object

- java.awt.Component
- - java.awt.List

java.awt.Component

- java.awt.List

java.awt.List

**All Implemented Interfaces:** ImageObserver

,

ItemSelectable

,

MenuContainer

,

Serializable

,

Accessible

```java
public class
List

extends
Component

implements
ItemSelectable
,
Accessible
```

The

List

component presents the user with a
scrolling list of text items. The list can be set up so that
the user can choose either one item or multiple items.

For example, the code . . .

```java
List lst = new List(4, false);
lst.add("Mercury");
lst.add("Venus");
lst.add("Earth");
lst.add("JavaSoft");
lst.add("Mars");
lst.add("Jupiter");
lst.add("Saturn");
lst.add("Uranus");
lst.add("Neptune");
lst.add("Pluto");
cnt.add(lst);
```

where

cnt

is a container, produces the following
scrolling list:

If the List allows multiple selections, then clicking on
an item that is already selected deselects it. In the preceding
example, only one item from the scrolling list can be selected
at a time, since the second argument when creating the new scrolling
list is

false

. If the List does not allow multiple
selections, selecting an item causes any other selected item
to be deselected.

Note that the list in the example shown was created with four visible
rows. Once the list has been created, the number of visible rows
cannot be changed. A default

List

is created with
four rows, so that

lst = new List()

is equivalent to

list = new List(4, false)

.

Beginning with Java 1.1, the Abstract Window Toolkit
sends the

List

object all mouse, keyboard, and focus events
that occur over it. (The old AWT event model is being maintained
only for backwards compatibility, and its use is discouraged.)

When an item is selected or deselected by the user, AWT sends an instance
of

ItemEvent

to the list.
When the user double-clicks on an item in a scrolling list,
AWT sends an instance of

ActionEvent

to the
list following the item event. AWT also generates an action event
when the user presses the return key while an item in the
list is selected.

If an application wants to perform some action based on an item
in this list being selected or activated by the user, it should implement

ItemListener

or

ActionListener

as appropriate and register the new listener to receive
events from this list.

For multiple-selection scrolling lists, it is considered a better
user interface to use an external gesture (such as clicking on a
button) to trigger the action.

**Since:** 1.0
**See Also:** ItemEvent

,

ItemListener

,

ActionEvent

,

ActionListener

,

Serialized Form

public class

List

extends

Component

implements

ItemSelectable

,

Accessible

The

List

component presents the user with a
scrolling list of text items. The list can be set up so that
the user can choose either one item or multiple items.

For example, the code . . .

```java
List lst = new List(4, false);
lst.add("Mercury");
lst.add("Venus");
lst.add("Earth");
lst.add("JavaSoft");
lst.add("Mars");
lst.add("Jupiter");
lst.add("Saturn");
lst.add("Uranus");
lst.add("Neptune");
lst.add("Pluto");
cnt.add(lst);
```

where

cnt

is a container, produces the following
scrolling list:

If the List allows multiple selections, then clicking on
an item that is already selected deselects it. In the preceding
example, only one item from the scrolling list can be selected
at a time, since the second argument when creating the new scrolling
list is

false

. If the List does not allow multiple
selections, selecting an item causes any other selected item
to be deselected.

Note that the list in the example shown was created with four visible
rows. Once the list has been created, the number of visible rows
cannot be changed. A default

List

is created with
four rows, so that

lst = new List()

is equivalent to

list = new List(4, false)

.

Beginning with Java 1.1, the Abstract Window Toolkit
sends the

List

object all mouse, keyboard, and focus events
that occur over it. (The old AWT event model is being maintained
only for backwards compatibility, and its use is discouraged.)

When an item is selected or deselected by the user, AWT sends an instance
of

ItemEvent

to the list.
When the user double-clicks on an item in a scrolling list,
AWT sends an instance of

ActionEvent

to the
list following the item event. AWT also generates an action event
when the user presses the return key while an item in the
list is selected.

If an application wants to perform some action based on an item
in this list being selected or activated by the user, it should implement

ItemListener

or

ActionListener

as appropriate and register the new listener to receive
events from this list.

For multiple-selection scrolling lists, it is considered a better
user interface to use an external gesture (such as clicking on a
button) to trigger the action.

For example, the code . . .

```java
List lst = new List(4, false);
lst.add("Mercury");
lst.add("Venus");
lst.add("Earth");
lst.add("JavaSoft");
lst.add("Mars");
lst.add("Jupiter");
lst.add("Saturn");
lst.add("Uranus");
lst.add("Neptune");
lst.add("Pluto");
cnt.add(lst);
```

where

cnt

is a container, produces the following
scrolling list:

If the List allows multiple selections, then clicking on
an item that is already selected deselects it. In the preceding
example, only one item from the scrolling list can be selected
at a time, since the second argument when creating the new scrolling
list is

false

. If the List does not allow multiple
selections, selecting an item causes any other selected item
to be deselected.

Note that the list in the example shown was created with four visible
rows. Once the list has been created, the number of visible rows
cannot be changed. A default

List

is created with
four rows, so that

lst = new List()

is equivalent to

list = new List(4, false)

.

Beginning with Java 1.1, the Abstract Window Toolkit
sends the

List

object all mouse, keyboard, and focus events
that occur over it. (The old AWT event model is being maintained
only for backwards compatibility, and its use is discouraged.)

When an item is selected or deselected by the user, AWT sends an instance
of

ItemEvent

to the list.
When the user double-clicks on an item in a scrolling list,
AWT sends an instance of

ActionEvent

to the
list following the item event. AWT also generates an action event
when the user presses the return key while an item in the
list is selected.

If an application wants to perform some action based on an item
in this list being selected or activated by the user, it should implement

ItemListener

or

ActionListener

as appropriate and register the new listener to receive
events from this list.

For multiple-selection scrolling lists, it is considered a better
user interface to use an external gesture (such as clicking on a
button) to trigger the action.

List lst = new List(4, false);
lst.add("Mercury");
lst.add("Venus");
lst.add("Earth");
lst.add("JavaSoft");
lst.add("Mars");
lst.add("Jupiter");
lst.add("Saturn");
lst.add("Uranus");
lst.add("Neptune");
lst.add("Pluto");
cnt.add(lst);

where

cnt

is a container, produces the following
scrolling list:

If the List allows multiple selections, then clicking on
an item that is already selected deselects it. In the preceding
example, only one item from the scrolling list can be selected
at a time, since the second argument when creating the new scrolling
list is

false

. If the List does not allow multiple
selections, selecting an item causes any other selected item
to be deselected.

Note that the list in the example shown was created with four visible
rows. Once the list has been created, the number of visible rows
cannot be changed. A default

List

is created with
four rows, so that

lst = new List()

is equivalent to

list = new List(4, false)

.

Beginning with Java 1.1, the Abstract Window Toolkit
sends the

List

object all mouse, keyboard, and focus events
that occur over it. (The old AWT event model is being maintained
only for backwards compatibility, and its use is discouraged.)

When an item is selected or deselected by the user, AWT sends an instance
of

ItemEvent

to the list.
When the user double-clicks on an item in a scrolling list,
AWT sends an instance of

ActionEvent

to the
list following the item event. AWT also generates an action event
when the user presses the return key while an item in the
list is selected.

If an application wants to perform some action based on an item
in this list being selected or activated by the user, it should implement

ItemListener

or

ActionListener

as appropriate and register the new listener to receive
events from this list.

For multiple-selection scrolling lists, it is considered a better
user interface to use an external gesture (such as clicking on a
button) to trigger the action.

If the List allows multiple selections, then clicking on
an item that is already selected deselects it. In the preceding
example, only one item from the scrolling list can be selected
at a time, since the second argument when creating the new scrolling
list is

false

. If the List does not allow multiple
selections, selecting an item causes any other selected item
to be deselected.

Note that the list in the example shown was created with four visible
rows. Once the list has been created, the number of visible rows
cannot be changed. A default

List

is created with
four rows, so that

lst = new List()

is equivalent to

list = new List(4, false)

.

Beginning with Java 1.1, the Abstract Window Toolkit
sends the

List

object all mouse, keyboard, and focus events
that occur over it. (The old AWT event model is being maintained
only for backwards compatibility, and its use is discouraged.)

When an item is selected or deselected by the user, AWT sends an instance
of

ItemEvent

to the list.
When the user double-clicks on an item in a scrolling list,
AWT sends an instance of

ActionEvent

to the
list following the item event. AWT also generates an action event
when the user presses the return key while an item in the
list is selected.

If an application wants to perform some action based on an item
in this list being selected or activated by the user, it should implement

ItemListener

or

ActionListener

as appropriate and register the new listener to receive
events from this list.

For multiple-selection scrolling lists, it is considered a better
user interface to use an external gesture (such as clicking on a
button) to trigger the action.

Note that the list in the example shown was created with four visible
rows. Once the list has been created, the number of visible rows
cannot be changed. A default

List

is created with
four rows, so that

lst = new List()

is equivalent to

list = new List(4, false)

.

Beginning with Java 1.1, the Abstract Window Toolkit
sends the

List

object all mouse, keyboard, and focus events
that occur over it. (The old AWT event model is being maintained
only for backwards compatibility, and its use is discouraged.)

When an item is selected or deselected by the user, AWT sends an instance
of

ItemEvent

to the list.
When the user double-clicks on an item in a scrolling list,
AWT sends an instance of

ActionEvent

to the
list following the item event. AWT also generates an action event
when the user presses the return key while an item in the
list is selected.

If an application wants to perform some action based on an item
in this list being selected or activated by the user, it should implement

ItemListener

or

ActionListener

as appropriate and register the new listener to receive
events from this list.

For multiple-selection scrolling lists, it is considered a better
user interface to use an external gesture (such as clicking on a
button) to trigger the action.

Beginning with Java 1.1, the Abstract Window Toolkit
sends the

List

object all mouse, keyboard, and focus events
that occur over it. (The old AWT event model is being maintained
only for backwards compatibility, and its use is discouraged.)

When an item is selected or deselected by the user, AWT sends an instance
of

ItemEvent

to the list.
When the user double-clicks on an item in a scrolling list,
AWT sends an instance of

ActionEvent

to the
list following the item event. AWT also generates an action event
when the user presses the return key while an item in the
list is selected.

If an application wants to perform some action based on an item
in this list being selected or activated by the user, it should implement

ItemListener

or

ActionListener

as appropriate and register the new listener to receive
events from this list.

For multiple-selection scrolling lists, it is considered a better
user interface to use an external gesture (such as clicking on a
button) to trigger the action.

When an item is selected or deselected by the user, AWT sends an instance
of

ItemEvent

to the list.
When the user double-clicks on an item in a scrolling list,
AWT sends an instance of

ActionEvent

to the
list following the item event. AWT also generates an action event
when the user presses the return key while an item in the
list is selected.

If an application wants to perform some action based on an item
in this list being selected or activated by the user, it should implement

ItemListener

or

ActionListener

as appropriate and register the new listener to receive
events from this list.

For multiple-selection scrolling lists, it is considered a better
user interface to use an external gesture (such as clicking on a
button) to trigger the action.

If an application wants to perform some action based on an item
in this list being selected or activated by the user, it should implement

ItemListener

or

ActionListener

as appropriate and register the new listener to receive
events from this list.

For multiple-selection scrolling lists, it is considered a better
user interface to use an external gesture (such as clicking on a
button) to trigger the action.

For multiple-selection scrolling lists, it is considered a better
user interface to use an external gesture (such as clicking on a
button) to trigger the action.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

protected class

List.AccessibleAWTList

This class implements accessibility support for the

List

class.

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

List

()

Creates a new scrolling list.

List

​(int rows)

Creates a new scrolling list initialized with the specified
number of visible lines.

List

​(int rows,
boolean multipleMode)

Creates a new scrolling list initialized to display the specified
number of rows.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

add

​(

String

item)

Adds the specified item to the end of scrolling list.

void

add

​(

String

item,
int index)

Adds the specified item to the scrolling list
at the position indicated by the index.

void

addActionListener

​(

ActionListener

l)

Adds the specified action listener to receive action events from
this list.

void

addItem

​(

String

item)

Deprecated.

replaced by

add(String)

.

void

addItem

​(

String

item,
int index)

Deprecated.

replaced by

add(String, int)

.

void

addItemListener

​(

ItemListener

l)

Adds the specified item listener to receive item events from
this list.

void

addNotify

()

Creates the peer for the list.

boolean

allowsMultipleSelections

()

Deprecated.

As of JDK version 1.1,
replaced by

isMultipleMode()

.

void

clear

()

Deprecated.

As of JDK version 1.1,
replaced by

removeAll()

.

int

countItems

()

Deprecated.

As of JDK version 1.1,
replaced by

getItemCount()

.

void

delItem

​(int position)

Deprecated.

replaced by

remove(String)

and

remove(int)

.

void

delItems

​(int start,
int end)

Deprecated.

As of JDK version 1.1,
Not for public use in the future.

void

deselect

​(int index)

Deselects the item at the specified index.

AccessibleContext

getAccessibleContext

()

Gets the

AccessibleContext

associated with this

List

.

ActionListener

[]

getActionListeners

()

Returns an array of all the action listeners
registered on this list.

String

getItem

​(int index)

Gets the item associated with the specified index.

int

getItemCount

()

Gets the number of items in the list.

ItemListener

[]

getItemListeners

()

Returns an array of all the item listeners
registered on this list.

String

[]

getItems

()

Gets the items in the list.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

List

.

Dimension

getMinimumSize

()

Determines the minimum size of this scrolling list.

Dimension

getMinimumSize

​(int rows)

Gets the minimum dimensions for a list with the specified
number of rows.

Dimension

getPreferredSize

()

Gets the preferred size of this scrolling list.

Dimension

getPreferredSize

​(int rows)

Gets the preferred dimensions for a list with the specified
number of rows.

int

getRows

()

Gets the number of visible lines in this list.

int

getSelectedIndex

()

Gets the index of the selected item on the list,

int[]

getSelectedIndexes

()

Gets the selected indexes on the list.

String

getSelectedItem

()

Gets the selected item on this scrolling list.

String

[]

getSelectedItems

()

Gets the selected items on this scrolling list.

Object

[]

getSelectedObjects

()

Gets the selected items on this scrolling list in an array of Objects.

int

getVisibleIndex

()

Gets the index of the item that was last made visible by
the method

makeVisible

.

boolean

isIndexSelected

​(int index)

Determines if the specified item in this scrolling list is
selected.

boolean

isMultipleMode

()

Determines whether this list allows multiple selections.

boolean

isSelected

​(int index)

Deprecated.

As of JDK version 1.1,
replaced by

isIndexSelected(int)

.

void

makeVisible

​(int index)

Makes the item at the specified index visible.

Dimension

minimumSize

()

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

Dimension

minimumSize

​(int rows)

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize(int)

.

protected

String

paramString

()

Returns the parameter string representing the state of this
scrolling list.

Dimension

preferredSize

()

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

Dimension

preferredSize

​(int rows)

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize(int)

.

protected void

processActionEvent

​(

ActionEvent

e)

Processes action events occurring on this component
by dispatching them to any registered

ActionListener

objects.

protected void

processEvent

​(

AWTEvent

e)

Processes events on this scrolling list.

protected void

processItemEvent

​(

ItemEvent

e)

Processes item events occurring on this list by
dispatching them to any registered

ItemListener

objects.

void

remove

​(int position)

Removes the item at the specified position
from this scrolling list.

void

remove

​(

String

item)

Removes the first occurrence of an item from the list.

void

removeActionListener

​(

ActionListener

l)

Removes the specified action listener so that it no longer
receives action events from this list.

void

removeAll

()

Removes all items from this list.

void

removeItemListener

​(

ItemListener

l)

Removes the specified item listener so that it no longer
receives item events from this list.

void

removeNotify

()

Removes the peer for this list.

void

replaceItem

​(

String

newValue,
int index)

Replaces the item at the specified index in the scrolling list
with the new string.

void

select

​(int index)

Selects the item at the specified index in the scrolling list.

void

setMultipleMode

​(boolean b)

Sets the flag that determines whether this list
allows multiple selections.

void

setMultipleSelections

​(boolean b)

Deprecated.

As of JDK version 1.1,
replaced by

setMultipleMode(boolean)

.

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

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

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

deliverEvent

,

disable

,

disableEvents

,

dispatchEvent

,

doLayout

,

enable

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

firePropertyChange

,

firePropertyChange

,

getAlignmentX

,

getAlignmentY

,

getBackground

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

,

getBounds

,

getColorModel

,

getComponentAt

,

getComponentAt

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

getFocusTraversalKeys

,

getFocusTraversalKeysEnabled

,

getFont

,

getFontMetrics

,

getForeground

,

getGraphics

,

getGraphicsConfiguration

,

getHeight

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

getLocation

,

getLocationOnScreen

,

getMaximumSize

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

getSize

,

getToolkit

,

getTreeLock

,

getWidth

,

getX

,

getY

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

invalidate

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isDoubleBuffered

,

isEnabled

,

isFocusable

,

isFocusCycleRoot

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

isOpaque

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

layout

,

list

,

list

,

list

,

list

,

list

,

locate

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

paint

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

print

,

printAll

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

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

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

repaint

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

reshape

,

resize

,

resize

,

revalidate

,

setBackground

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

setEnabled

,

setFocusable

,

setFocusTraversalKeys

,

setFocusTraversalKeysEnabled

,

setFont

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

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

,

update

,

validate

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

List.AccessibleAWTList

This class implements accessibility support for the

List

class.

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

List

class.

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

List

()

Creates a new scrolling list.

List

​(int rows)

Creates a new scrolling list initialized with the specified
number of visible lines.

List

​(int rows,
boolean multipleMode)

Creates a new scrolling list initialized to display the specified
number of rows.

---

#### Constructor Summary

Creates a new scrolling list.

Creates a new scrolling list initialized with the specified
number of visible lines.

Creates a new scrolling list initialized to display the specified
number of rows.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

add

​(

String

item)

Adds the specified item to the end of scrolling list.

void

add

​(

String

item,
int index)

Adds the specified item to the scrolling list
at the position indicated by the index.

void

addActionListener

​(

ActionListener

l)

Adds the specified action listener to receive action events from
this list.

void

addItem

​(

String

item)

Deprecated.

replaced by

add(String)

.

void

addItem

​(

String

item,
int index)

Deprecated.

replaced by

add(String, int)

.

void

addItemListener

​(

ItemListener

l)

Adds the specified item listener to receive item events from
this list.

void

addNotify

()

Creates the peer for the list.

boolean

allowsMultipleSelections

()

Deprecated.

As of JDK version 1.1,
replaced by

isMultipleMode()

.

void

clear

()

Deprecated.

As of JDK version 1.1,
replaced by

removeAll()

.

int

countItems

()

Deprecated.

As of JDK version 1.1,
replaced by

getItemCount()

.

void

delItem

​(int position)

Deprecated.

replaced by

remove(String)

and

remove(int)

.

void

delItems

​(int start,
int end)

Deprecated.

As of JDK version 1.1,
Not for public use in the future.

void

deselect

​(int index)

Deselects the item at the specified index.

AccessibleContext

getAccessibleContext

()

Gets the

AccessibleContext

associated with this

List

.

ActionListener

[]

getActionListeners

()

Returns an array of all the action listeners
registered on this list.

String

getItem

​(int index)

Gets the item associated with the specified index.

int

getItemCount

()

Gets the number of items in the list.

ItemListener

[]

getItemListeners

()

Returns an array of all the item listeners
registered on this list.

String

[]

getItems

()

Gets the items in the list.

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

List

.

Dimension

getMinimumSize

()

Determines the minimum size of this scrolling list.

Dimension

getMinimumSize

​(int rows)

Gets the minimum dimensions for a list with the specified
number of rows.

Dimension

getPreferredSize

()

Gets the preferred size of this scrolling list.

Dimension

getPreferredSize

​(int rows)

Gets the preferred dimensions for a list with the specified
number of rows.

int

getRows

()

Gets the number of visible lines in this list.

int

getSelectedIndex

()

Gets the index of the selected item on the list,

int[]

getSelectedIndexes

()

Gets the selected indexes on the list.

String

getSelectedItem

()

Gets the selected item on this scrolling list.

String

[]

getSelectedItems

()

Gets the selected items on this scrolling list.

Object

[]

getSelectedObjects

()

Gets the selected items on this scrolling list in an array of Objects.

int

getVisibleIndex

()

Gets the index of the item that was last made visible by
the method

makeVisible

.

boolean

isIndexSelected

​(int index)

Determines if the specified item in this scrolling list is
selected.

boolean

isMultipleMode

()

Determines whether this list allows multiple selections.

boolean

isSelected

​(int index)

Deprecated.

As of JDK version 1.1,
replaced by

isIndexSelected(int)

.

void

makeVisible

​(int index)

Makes the item at the specified index visible.

Dimension

minimumSize

()

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

Dimension

minimumSize

​(int rows)

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize(int)

.

protected

String

paramString

()

Returns the parameter string representing the state of this
scrolling list.

Dimension

preferredSize

()

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

Dimension

preferredSize

​(int rows)

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize(int)

.

protected void

processActionEvent

​(

ActionEvent

e)

Processes action events occurring on this component
by dispatching them to any registered

ActionListener

objects.

protected void

processEvent

​(

AWTEvent

e)

Processes events on this scrolling list.

protected void

processItemEvent

​(

ItemEvent

e)

Processes item events occurring on this list by
dispatching them to any registered

ItemListener

objects.

void

remove

​(int position)

Removes the item at the specified position
from this scrolling list.

void

remove

​(

String

item)

Removes the first occurrence of an item from the list.

void

removeActionListener

​(

ActionListener

l)

Removes the specified action listener so that it no longer
receives action events from this list.

void

removeAll

()

Removes all items from this list.

void

removeItemListener

​(

ItemListener

l)

Removes the specified item listener so that it no longer
receives item events from this list.

void

removeNotify

()

Removes the peer for this list.

void

replaceItem

​(

String

newValue,
int index)

Replaces the item at the specified index in the scrolling list
with the new string.

void

select

​(int index)

Selects the item at the specified index in the scrolling list.

void

setMultipleMode

​(boolean b)

Sets the flag that determines whether this list
allows multiple selections.

void

setMultipleSelections

​(boolean b)

Deprecated.

As of JDK version 1.1,
replaced by

setMultipleMode(boolean)

.

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

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

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

deliverEvent

,

disable

,

disableEvents

,

dispatchEvent

,

doLayout

,

enable

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

firePropertyChange

,

firePropertyChange

,

getAlignmentX

,

getAlignmentY

,

getBackground

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

,

getBounds

,

getColorModel

,

getComponentAt

,

getComponentAt

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

getFocusTraversalKeys

,

getFocusTraversalKeysEnabled

,

getFont

,

getFontMetrics

,

getForeground

,

getGraphics

,

getGraphicsConfiguration

,

getHeight

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

getLocation

,

getLocationOnScreen

,

getMaximumSize

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

getSize

,

getToolkit

,

getTreeLock

,

getWidth

,

getX

,

getY

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

invalidate

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isDoubleBuffered

,

isEnabled

,

isFocusable

,

isFocusCycleRoot

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

isOpaque

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

layout

,

list

,

list

,

list

,

list

,

list

,

locate

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

paint

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

print

,

printAll

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

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

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

repaint

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

reshape

,

resize

,

resize

,

revalidate

,

setBackground

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

setEnabled

,

setFocusable

,

setFocusTraversalKeys

,

setFocusTraversalKeysEnabled

,

setFont

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

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

,

update

,

validate

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

Adds the specified item to the end of scrolling list.

Adds the specified item to the scrolling list
at the position indicated by the index.

Adds the specified action listener to receive action events from
this list.

Deprecated.

replaced by

add(String)

.

Deprecated.

replaced by

add(String, int)

.

Adds the specified item listener to receive item events from
this list.

Creates the peer for the list.

Deprecated.

As of JDK version 1.1,
replaced by

isMultipleMode()

.

Deprecated.

As of JDK version 1.1,
replaced by

removeAll()

.

Deprecated.

As of JDK version 1.1,
replaced by

getItemCount()

.

Deprecated.

replaced by

remove(String)

and

remove(int)

.

Deprecated.

As of JDK version 1.1,
Not for public use in the future.

Deselects the item at the specified index.

Gets the

AccessibleContext

associated with this

List

.

Returns an array of all the action listeners
registered on this list.

Gets the item associated with the specified index.

Gets the number of items in the list.

Returns an array of all the item listeners
registered on this list.

Gets the items in the list.

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

List

.

Determines the minimum size of this scrolling list.

Gets the minimum dimensions for a list with the specified
number of rows.

Gets the preferred size of this scrolling list.

Gets the preferred dimensions for a list with the specified
number of rows.

Gets the number of visible lines in this list.

Gets the index of the selected item on the list,

Gets the selected indexes on the list.

Gets the selected item on this scrolling list.

Gets the selected items on this scrolling list.

Gets the selected items on this scrolling list in an array of Objects.

Gets the index of the item that was last made visible by
the method

makeVisible

.

Determines if the specified item in this scrolling list is
selected.

Determines whether this list allows multiple selections.

Deprecated.

As of JDK version 1.1,
replaced by

isIndexSelected(int)

.

Makes the item at the specified index visible.

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize(int)

.

Returns the parameter string representing the state of this
scrolling list.

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize(int)

.

Processes action events occurring on this component
by dispatching them to any registered

ActionListener

objects.

Processes events on this scrolling list.

Processes item events occurring on this list by
dispatching them to any registered

ItemListener

objects.

Removes the item at the specified position
from this scrolling list.

Removes the first occurrence of an item from the list.

Removes the specified action listener so that it no longer
receives action events from this list.

Removes all items from this list.

Removes the specified item listener so that it no longer
receives item events from this list.

Removes the peer for this list.

Replaces the item at the specified index in the scrolling list
with the new string.

Selects the item at the specified index in the scrolling list.

Sets the flag that determines whether this list
allows multiple selections.

Deprecated.

As of JDK version 1.1,
replaced by

setMultipleMode(boolean)

.

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

addPropertyChangeListener

,

addPropertyChangeListener

,

applyComponentOrientation

,

areFocusTraversalKeysSet

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

deliverEvent

,

disable

,

disableEvents

,

dispatchEvent

,

doLayout

,

enable

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

firePropertyChange

,

firePropertyChange

,

getAlignmentX

,

getAlignmentY

,

getBackground

,

getBaseline

,

getBaselineResizeBehavior

,

getBounds

,

getBounds

,

getColorModel

,

getComponentAt

,

getComponentAt

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

getFocusTraversalKeys

,

getFocusTraversalKeysEnabled

,

getFont

,

getFontMetrics

,

getForeground

,

getGraphics

,

getGraphicsConfiguration

,

getHeight

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

getLocation

,

getLocationOnScreen

,

getMaximumSize

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

getSize

,

getToolkit

,

getTreeLock

,

getWidth

,

getX

,

getY

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

invalidate

,

isBackgroundSet

,

isCursorSet

,

isDisplayable

,

isDoubleBuffered

,

isEnabled

,

isFocusable

,

isFocusCycleRoot

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

isOpaque

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

layout

,

list

,

list

,

list

,

list

,

list

,

locate

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

paint

,

paintAll

,

postEvent

,

prepareImage

,

prepareImage

,

print

,

printAll

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

processKeyEvent

,

processMouseEvent

,

processMouseMotionEvent

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

repaint

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocus

,

requestFocusInWindow

,

requestFocusInWindow

,

requestFocusInWindow

,

reshape

,

resize

,

resize

,

revalidate

,

setBackground

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

setEnabled

,

setFocusable

,

setFocusTraversalKeys

,

setFocusTraversalKeysEnabled

,

setFont

,

setForeground

,

setIgnoreRepaint

,

setLocale

,

setLocation

,

setLocation

,

setMaximumSize

,

setMinimumSize

,

setMixingCutoutShape

,

setName

,

setPreferredSize

,

setSize

,

setSize

,

setVisible

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

,

update

,

validate

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

- List

```java
public List()
throws
HeadlessException
```

Creates a new scrolling list.
By default, there are four visible lines and multiple selections are
not allowed. Note that this is a convenience method for

List(0, false)

. Also note that the number of visible
lines in the list cannot be changed after it has been created.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

- List

```java
public List​(int rows)
throws
HeadlessException
```

Creates a new scrolling list initialized with the specified
number of visible lines. By default, multiple selections are
not allowed. Note that this is a convenience method for

List(rows, false)

. Also note that the number
of visible rows in the list cannot be changed after it has
been created.

**Parameters:** rows

- the number of items to show.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**Since:** 1.1
**See Also:** GraphicsEnvironment.isHeadless()

- List

```java
public List​(int rows,
boolean multipleMode)
throws
HeadlessException
```

Creates a new scrolling list initialized to display the specified
number of rows. Note that if zero rows are specified, then
the list will be created with a default of four rows.
Also note that the number of visible rows in the list cannot
be changed after it has been created.
If the value of

multipleMode

is

true

, then the user can select multiple items from
the list. If it is

false

, only one item at a time
can be selected.

**Parameters:** rows

- the number of items to show.
**Parameters:** multipleMode

- if

true

,
then multiple selections are allowed;
otherwise, only one item can be selected at a time.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

============ METHOD DETAIL ==========

- Method Detail

- addNotify

```java
public void addNotify()
```

Creates the peer for the list. The peer allows us to modify the
list's appearance without changing its functionality.

**Overrides:** addNotify

in class

Component
**See Also:** Component.isDisplayable()

,

Component.removeNotify()

,

Component.invalidate()

- removeNotify

```java
public void removeNotify()
```

Removes the peer for this list. The peer allows us to modify the
list's appearance without changing its functionality.

**Overrides:** removeNotify

in class

Component
**See Also:** Component.isDisplayable()

,

Component.addNotify()

- getItemCount

```java
public int getItemCount()
```

Gets the number of items in the list.

**Returns:** the number of items in the list
**Since:** 1.1
**See Also:** getItem(int)

- countItems

```java
@Deprecated

public int countItems()
```

Deprecated.

As of JDK version 1.1,
replaced by

getItemCount()

.

Returns the number of items in the list.

**Returns:** the number of items in the list

- getItem

```java
public
String
getItem​(int index)
```

Gets the item associated with the specified index.

**Parameters:** index

- the position of the item
**Returns:** an item that is associated with
the specified index
**See Also:** getItemCount()

- getItems

```java
public
String
[] getItems()
```

Gets the items in the list.

**Returns:** a string array containing items of the list
**Since:** 1.1
**See Also:** select(int)

,

deselect(int)

,

isIndexSelected(int)

- add

```java
public void add​(
String
item)
```

Adds the specified item to the end of scrolling list.

**Parameters:** item

- the item to be added
**Since:** 1.1

- addItem

```java
@Deprecated

public void addItem​(
String
item)
```

Deprecated.

replaced by

add(String)

.

Adds the specified item to the end of the list.

**Parameters:** item

- the item to be added

- add

```java
public void add​(
String
item,
int index)
```

Adds the specified item to the scrolling list
at the position indicated by the index. The index is
zero-based. If the value of the index is less than zero,
or if the value of the index is greater than or equal to
the number of items in the list, then the item is added
to the end of the list.

**Parameters:** item

- the item to be added;
if this parameter is

null

then the item is
treated as an empty string,

""
**Parameters:** index

- the position at which to add the item
**Since:** 1.1

- addItem

```java
@Deprecated

public void addItem​(
String
item,
int index)
```

Deprecated.

replaced by

add(String, int)

.

Adds the specified item to the list
at the position indicated by the index.

**Parameters:** item

- the item to be added
**Parameters:** index

- the position at which to add the item

- replaceItem

```java
public void replaceItem​(
String
newValue,
int index)
```

Replaces the item at the specified index in the scrolling list
with the new string.

**Parameters:** newValue

- a new string to replace an existing item
**Parameters:** index

- the position of the item to replace
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is out of range

- removeAll

```java
public void removeAll()
```

Removes all items from this list.

**Since:** 1.1
**See Also:** remove(java.lang.String)

,

delItems(int, int)

- clear

```java
@Deprecated

public void clear()
```

Deprecated.

As of JDK version 1.1,
replaced by

removeAll()

.

- remove

```java
public void remove​(
String
item)
```

Removes the first occurrence of an item from the list.
If the specified item is selected, and is the only selected
item in the list, the list is set to have no selection.

**Parameters:** item

- the item to remove from the list
**Throws:** IllegalArgumentException

- if the item doesn't exist in the list
**Since:** 1.1

- remove

```java
public void remove​(int position)
```

Removes the item at the specified position
from this scrolling list.
If the item with the specified position is selected, and is the
only selected item in the list, the list is set to have no selection.

**Parameters:** position

- the index of the item to delete
**Throws:** ArrayIndexOutOfBoundsException

- if the

position

is less than 0 or
greater than

getItemCount()-1
**Since:** 1.1
**See Also:** add(String, int)

- delItem

```java
@Deprecated

public void delItem​(int position)
```

Deprecated.

replaced by

remove(String)

and

remove(int)

.

Removes the item at the specified position.

**Parameters:** position

- the index of the item to delete

- getSelectedIndex

```java
public int getSelectedIndex()
```

Gets the index of the selected item on the list,

**Returns:** the index of the selected item;
if no item is selected, or if multiple items are
selected,

-1

is returned.
**See Also:** select(int)

,

deselect(int)

,

isIndexSelected(int)

- getSelectedIndexes

```java
public int[] getSelectedIndexes()
```

Gets the selected indexes on the list.

**Returns:** an array of the selected indexes on this scrolling list;
if no item is selected, a zero-length array is returned.
**See Also:** select(int)

,

deselect(int)

,

isIndexSelected(int)

- getSelectedItem

```java
public
String
getSelectedItem()
```

Gets the selected item on this scrolling list.

**Returns:** the selected item on the list;
if no item is selected, or if multiple items are
selected,

null

is returned.
**See Also:** select(int)

,

deselect(int)

,

isIndexSelected(int)

- getSelectedItems

```java
public
String
[] getSelectedItems()
```

Gets the selected items on this scrolling list.

**Returns:** an array of the selected items on this scrolling list;
if no item is selected, a zero-length array is returned.
**See Also:** select(int)

,

deselect(int)

,

isIndexSelected(int)

- getSelectedObjects

```java
public
Object
[] getSelectedObjects()
```

Gets the selected items on this scrolling list in an array of Objects.

**Specified by:** getSelectedObjects

in interface

ItemSelectable
**Returns:** an array of

Object

s representing the
selected items on this scrolling list;
if no item is selected, a zero-length array is returned.
**See Also:** getSelectedItems()

,

ItemSelectable

- select

```java
public void select​(int index)
```

Selects the item at the specified index in the scrolling list.

Note that passing out of range parameters is invalid,
and will result in unspecified behavior.

Note that this method should be primarily used to
initially select an item in this component.
Programmatically calling this method will

not

trigger
an

ItemEvent

. The only way to trigger an

ItemEvent

is by user interaction.

**Parameters:** index

- the position of the item to select
**See Also:** getSelectedItem()

,

deselect(int)

,

isIndexSelected(int)

- deselect

```java
public void deselect​(int index)
```

Deselects the item at the specified index.

Note that passing out of range parameters is invalid,
and will result in unspecified behavior.

If the item at the specified index is not selected,
then the operation is ignored.

**Parameters:** index

- the position of the item to deselect
**See Also:** select(int)

,

getSelectedItem()

,

isIndexSelected(int)

- isIndexSelected

```java
public boolean isIndexSelected​(int index)
```

Determines if the specified item in this scrolling list is
selected.

**Parameters:** index

- the item to be checked
**Returns:** true

if the specified item has been
selected;

false

otherwise
**Since:** 1.1
**See Also:** select(int)

,

deselect(int)

- isSelected

```java
@Deprecated

public boolean isSelected​(int index)
```

Deprecated.

As of JDK version 1.1,
replaced by

isIndexSelected(int)

.

Determines if the specified item in the list is selected.

**Parameters:** index

- specifies the item to be checked
**Returns:** true

if the item is selected; otherwise

false

- getRows

```java
public int getRows()
```

Gets the number of visible lines in this list. Note that
once the

List

has been created, this number
will never change.

**Returns:** the number of visible lines in this scrolling list

- isMultipleMode

```java
public boolean isMultipleMode()
```

Determines whether this list allows multiple selections.

**Returns:** true

if this list allows multiple
selections; otherwise,

false
**Since:** 1.1
**See Also:** setMultipleMode(boolean)

- allowsMultipleSelections

```java
@Deprecated

public boolean allowsMultipleSelections()
```

Deprecated.

As of JDK version 1.1,
replaced by

isMultipleMode()

.

Determines whether this list allows multiple selections.

**Returns:** true

if this list allows multiple
selections; otherwise

false

- setMultipleMode

```java
public void setMultipleMode​(boolean b)
```

Sets the flag that determines whether this list
allows multiple selections.
When the selection mode is changed from multiple-selection to
single-selection, the selected items change as follows:
If a selected item has the location cursor, only that
item will remain selected. If no selected item has the
location cursor, all items will be deselected.

**Parameters:** b

- if

true

then multiple selections
are allowed; otherwise, only one item from
the list can be selected at once
**Since:** 1.1
**See Also:** isMultipleMode()

- setMultipleSelections

```java
@Deprecated

public void setMultipleSelections​(boolean b)
```

Deprecated.

As of JDK version 1.1,
replaced by

setMultipleMode(boolean)

.

Enables or disables multiple selection mode for this list.

**Parameters:** b

-

true

to enable multiple mode,

false

otherwise

- getVisibleIndex

```java
public int getVisibleIndex()
```

Gets the index of the item that was last made visible by
the method

makeVisible

.

**Returns:** the index of the item that was last made visible
**See Also:** makeVisible(int)

- makeVisible

```java
public void makeVisible​(int index)
```

Makes the item at the specified index visible.

**Parameters:** index

- the position of the item
**See Also:** getVisibleIndex()

- getPreferredSize

```java
public
Dimension
getPreferredSize​(int rows)
```

Gets the preferred dimensions for a list with the specified
number of rows.

**Parameters:** rows

- number of rows in the list
**Returns:** the preferred dimensions for displaying this scrolling list
given that the specified number of rows must be visible
**Since:** 1.1
**See Also:** Component.getPreferredSize()

- preferredSize

```java
@Deprecated

public
Dimension
preferredSize​(int rows)
```

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize(int)

.

Returns the preferred size of this component
assuming it has the specified number of rows.

**Parameters:** rows

- the number of rows
**Returns:** the preferred dimensions for displaying this list

- getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Gets the preferred size of this scrolling list.

**Overrides:** getPreferredSize

in class

Component
**Returns:** the preferred dimensions for displaying this scrolling list
**Since:** 1.1
**See Also:** Component.getPreferredSize()

- preferredSize

```java
@Deprecated

public
Dimension
preferredSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

Description copied from class:

Component

Returns the component's preferred size.

**Overrides:** preferredSize

in class

Component
**Returns:** the component's preferred size

- getMinimumSize

```java
public
Dimension
getMinimumSize​(int rows)
```

Gets the minimum dimensions for a list with the specified
number of rows.

**Parameters:** rows

- number of rows in the list
**Returns:** the minimum dimensions for displaying this scrolling list
given that the specified number of rows must be visible
**Since:** 1.1
**See Also:** Component.getMinimumSize()

- minimumSize

```java
@Deprecated

public
Dimension
minimumSize​(int rows)
```

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize(int)

.

Returns the minimum dimensions for the list
with the specified number of rows.

**Parameters:** rows

- the number of rows in the list
**Returns:** the minimum dimensions for displaying this list

- getMinimumSize

```java
public
Dimension
getMinimumSize()
```

Determines the minimum size of this scrolling list.

**Overrides:** getMinimumSize

in class

Component
**Returns:** the minimum dimensions needed
to display this scrolling list
**Since:** 1.1
**See Also:** Component.getMinimumSize()

- minimumSize

```java
@Deprecated

public
Dimension
minimumSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

Description copied from class:

Component

Returns the minimum size of this component.

**Overrides:** minimumSize

in class

Component
**Returns:** the minimum size of this component

- addItemListener

```java
public void addItemListener​(
ItemListener
l)
```

Adds the specified item listener to receive item events from
this list. Item events are sent in response to user input, but not
in response to calls to

select

or

deselect

.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** addItemListener

in interface

ItemSelectable
**Parameters:** l

- the item listener
**Since:** 1.1
**See Also:** removeItemListener(java.awt.event.ItemListener)

,

getItemListeners()

,

select(int)

,

deselect(int)

,

ItemEvent

,

ItemListener

- removeItemListener

```java
public void removeItemListener​(
ItemListener
l)
```

Removes the specified item listener so that it no longer
receives item events from this list.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** removeItemListener

in interface

ItemSelectable
**Parameters:** l

- the item listener
**Since:** 1.1
**See Also:** addItemListener(java.awt.event.ItemListener)

,

getItemListeners()

,

ItemEvent

,

ItemListener

- getItemListeners

```java
public
ItemListener
[] getItemListeners()
```

Returns an array of all the item listeners
registered on this list.

**Returns:** all of this list's

ItemListener

s
or an empty array if no item
listeners are currently registered
**Since:** 1.4
**See Also:** addItemListener(java.awt.event.ItemListener)

,

removeItemListener(java.awt.event.ItemListener)

,

ItemEvent

,

ItemListener

- addActionListener

```java
public void addActionListener​(
ActionListener
l)
```

Adds the specified action listener to receive action events from
this list. Action events occur when a user double-clicks
on a list item or types Enter when the list has the keyboard
focus.

If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the action listener
**Since:** 1.1
**See Also:** removeActionListener(java.awt.event.ActionListener)

,

getActionListeners()

,

ActionEvent

,

ActionListener

- removeActionListener

```java
public void removeActionListener​(
ActionListener
l)
```

Removes the specified action listener so that it no longer
receives action events from this list. Action events
occur when a user double-clicks on a list item.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the action listener
**Since:** 1.1
**See Also:** addActionListener(java.awt.event.ActionListener)

,

getActionListeners()

,

ActionEvent

,

ActionListener

- getActionListeners

```java
public
ActionListener
[] getActionListeners()
```

Returns an array of all the action listeners
registered on this list.

**Returns:** all of this list's

ActionListener

s
or an empty array if no action
listeners are currently registered
**Since:** 1.4
**See Also:** addActionListener(java.awt.event.ActionListener)

,

removeActionListener(java.awt.event.ActionListener)

,

ActionEvent

,

ActionListener

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

List

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

List l

for its item listeners with the following code:

```java
ItemListener[] ils = (ItemListener[])(l.getListeners(ItemListener.class));
```

If no such listeners exist, this method returns an empty array.

**Overrides:** getListeners

in class

Component
**Type Parameters:** T

- the type of the listeners
**Parameters:** listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s on this list,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getItemListeners()

- processEvent

```java
protected void processEvent​(
AWTEvent
e)
```

Processes events on this scrolling list. If an event is
an instance of

ItemEvent

, it invokes the

processItemEvent

method. Else, if the
event is an instance of

ActionEvent

,
it invokes

processActionEvent

.
If the event is not an item event or an action event,
it invokes

processEvent

on the superclass.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:** processEvent

in class

Component
**Parameters:** e

- the event
**Since:** 1.1
**See Also:** ActionEvent

,

ItemEvent

,

processActionEvent(java.awt.event.ActionEvent)

,

processItemEvent(java.awt.event.ItemEvent)

- processItemEvent

```java
protected void processItemEvent​(
ItemEvent
e)
```

Processes item events occurring on this list by
dispatching them to any registered

ItemListener

objects.

This method is not called unless item events are
enabled for this component. Item events are enabled
when one of the following occurs:

- An

ItemListener

object is registered
via

addItemListener

.

Item events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the item event
**Since:** 1.1
**See Also:** ItemEvent

,

ItemListener

,

addItemListener(java.awt.event.ItemListener)

,

Component.enableEvents(long)

- processActionEvent

```java
protected void processActionEvent​(
ActionEvent
e)
```

Processes action events occurring on this component
by dispatching them to any registered

ActionListener

objects.

This method is not called unless action events are
enabled for this component. Action events are enabled
when one of the following occurs:

- An

ActionListener

object is registered
via

addActionListener

.

Action events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the action event
**Since:** 1.1
**See Also:** ActionEvent

,

ActionListener

,

addActionListener(java.awt.event.ActionListener)

,

Component.enableEvents(long)

- paramString

```java
protected
String
paramString()
```

Returns the parameter string representing the state of this
scrolling list. This string is useful for debugging.

**Overrides:** paramString

in class

Component
**Returns:** the parameter string of this scrolling list

- delItems

```java
@Deprecated

public void delItems​(int start,
int end)
```

Deprecated.

As of JDK version 1.1,
Not for public use in the future.
This method is expected to be retained only as a package
private method.

Deletes the list items in the specified index range.

**Parameters:** start

- the beginning index of the range to delete
**Parameters:** end

- the ending index of the range to delete

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated with this

List

. For lists, the

AccessibleContext

takes the form of an

AccessibleAWTList

.
A new

AccessibleAWTList

instance is created, if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an

AccessibleAWTList

that serves as the

AccessibleContext

of this

List
**Since:** 1.3

Constructor Detail

- List

```java
public List()
throws
HeadlessException
```

Creates a new scrolling list.
By default, there are four visible lines and multiple selections are
not allowed. Note that this is a convenience method for

List(0, false)

. Also note that the number of visible
lines in the list cannot be changed after it has been created.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

- List

```java
public List​(int rows)
throws
HeadlessException
```

Creates a new scrolling list initialized with the specified
number of visible lines. By default, multiple selections are
not allowed. Note that this is a convenience method for

List(rows, false)

. Also note that the number
of visible rows in the list cannot be changed after it has
been created.

**Parameters:** rows

- the number of items to show.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**Since:** 1.1
**See Also:** GraphicsEnvironment.isHeadless()

- List

```java
public List​(int rows,
boolean multipleMode)
throws
HeadlessException
```

Creates a new scrolling list initialized to display the specified
number of rows. Note that if zero rows are specified, then
the list will be created with a default of four rows.
Also note that the number of visible rows in the list cannot
be changed after it has been created.
If the value of

multipleMode

is

true

, then the user can select multiple items from
the list. If it is

false

, only one item at a time
can be selected.

**Parameters:** rows

- the number of items to show.
**Parameters:** multipleMode

- if

true

,
then multiple selections are allowed;
otherwise, only one item can be selected at a time.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

---

#### Constructor Detail

List

```java
public List()
throws
HeadlessException
```

Creates a new scrolling list.
By default, there are four visible lines and multiple selections are
not allowed. Note that this is a convenience method for

List(0, false)

. Also note that the number of visible
lines in the list cannot be changed after it has been created.

**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

---

#### List

public List()
throws

HeadlessException

Creates a new scrolling list.
By default, there are four visible lines and multiple selections are
not allowed. Note that this is a convenience method for

List(0, false)

. Also note that the number of visible
lines in the list cannot be changed after it has been created.

List

```java
public List​(int rows)
throws
HeadlessException
```

Creates a new scrolling list initialized with the specified
number of visible lines. By default, multiple selections are
not allowed. Note that this is a convenience method for

List(rows, false)

. Also note that the number
of visible rows in the list cannot be changed after it has
been created.

**Parameters:** rows

- the number of items to show.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**Since:** 1.1
**See Also:** GraphicsEnvironment.isHeadless()

---

#### List

public List​(int rows)
throws

HeadlessException

Creates a new scrolling list initialized with the specified
number of visible lines. By default, multiple selections are
not allowed. Note that this is a convenience method for

List(rows, false)

. Also note that the number
of visible rows in the list cannot be changed after it has
been created.

List

```java
public List​(int rows,
boolean multipleMode)
throws
HeadlessException
```

Creates a new scrolling list initialized to display the specified
number of rows. Note that if zero rows are specified, then
the list will be created with a default of four rows.
Also note that the number of visible rows in the list cannot
be changed after it has been created.
If the value of

multipleMode

is

true

, then the user can select multiple items from
the list. If it is

false

, only one item at a time
can be selected.

**Parameters:** rows

- the number of items to show.
**Parameters:** multipleMode

- if

true

,
then multiple selections are allowed;
otherwise, only one item can be selected at a time.
**Throws:** HeadlessException

- if GraphicsEnvironment.isHeadless()
returns true.
**See Also:** GraphicsEnvironment.isHeadless()

---

#### List

public List​(int rows,
boolean multipleMode)
throws

HeadlessException

Creates a new scrolling list initialized to display the specified
number of rows. Note that if zero rows are specified, then
the list will be created with a default of four rows.
Also note that the number of visible rows in the list cannot
be changed after it has been created.
If the value of

multipleMode

is

true

, then the user can select multiple items from
the list. If it is

false

, only one item at a time
can be selected.

Method Detail

- addNotify

```java
public void addNotify()
```

Creates the peer for the list. The peer allows us to modify the
list's appearance without changing its functionality.

**Overrides:** addNotify

in class

Component
**See Also:** Component.isDisplayable()

,

Component.removeNotify()

,

Component.invalidate()

- removeNotify

```java
public void removeNotify()
```

Removes the peer for this list. The peer allows us to modify the
list's appearance without changing its functionality.

**Overrides:** removeNotify

in class

Component
**See Also:** Component.isDisplayable()

,

Component.addNotify()

- getItemCount

```java
public int getItemCount()
```

Gets the number of items in the list.

**Returns:** the number of items in the list
**Since:** 1.1
**See Also:** getItem(int)

- countItems

```java
@Deprecated

public int countItems()
```

Deprecated.

As of JDK version 1.1,
replaced by

getItemCount()

.

Returns the number of items in the list.

**Returns:** the number of items in the list

- getItem

```java
public
String
getItem​(int index)
```

Gets the item associated with the specified index.

**Parameters:** index

- the position of the item
**Returns:** an item that is associated with
the specified index
**See Also:** getItemCount()

- getItems

```java
public
String
[] getItems()
```

Gets the items in the list.

**Returns:** a string array containing items of the list
**Since:** 1.1
**See Also:** select(int)

,

deselect(int)

,

isIndexSelected(int)

- add

```java
public void add​(
String
item)
```

Adds the specified item to the end of scrolling list.

**Parameters:** item

- the item to be added
**Since:** 1.1

- addItem

```java
@Deprecated

public void addItem​(
String
item)
```

Deprecated.

replaced by

add(String)

.

Adds the specified item to the end of the list.

**Parameters:** item

- the item to be added

- add

```java
public void add​(
String
item,
int index)
```

Adds the specified item to the scrolling list
at the position indicated by the index. The index is
zero-based. If the value of the index is less than zero,
or if the value of the index is greater than or equal to
the number of items in the list, then the item is added
to the end of the list.

**Parameters:** item

- the item to be added;
if this parameter is

null

then the item is
treated as an empty string,

""
**Parameters:** index

- the position at which to add the item
**Since:** 1.1

- addItem

```java
@Deprecated

public void addItem​(
String
item,
int index)
```

Deprecated.

replaced by

add(String, int)

.

Adds the specified item to the list
at the position indicated by the index.

**Parameters:** item

- the item to be added
**Parameters:** index

- the position at which to add the item

- replaceItem

```java
public void replaceItem​(
String
newValue,
int index)
```

Replaces the item at the specified index in the scrolling list
with the new string.

**Parameters:** newValue

- a new string to replace an existing item
**Parameters:** index

- the position of the item to replace
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is out of range

- removeAll

```java
public void removeAll()
```

Removes all items from this list.

**Since:** 1.1
**See Also:** remove(java.lang.String)

,

delItems(int, int)

- clear

```java
@Deprecated

public void clear()
```

Deprecated.

As of JDK version 1.1,
replaced by

removeAll()

.

- remove

```java
public void remove​(
String
item)
```

Removes the first occurrence of an item from the list.
If the specified item is selected, and is the only selected
item in the list, the list is set to have no selection.

**Parameters:** item

- the item to remove from the list
**Throws:** IllegalArgumentException

- if the item doesn't exist in the list
**Since:** 1.1

- remove

```java
public void remove​(int position)
```

Removes the item at the specified position
from this scrolling list.
If the item with the specified position is selected, and is the
only selected item in the list, the list is set to have no selection.

**Parameters:** position

- the index of the item to delete
**Throws:** ArrayIndexOutOfBoundsException

- if the

position

is less than 0 or
greater than

getItemCount()-1
**Since:** 1.1
**See Also:** add(String, int)

- delItem

```java
@Deprecated

public void delItem​(int position)
```

Deprecated.

replaced by

remove(String)

and

remove(int)

.

Removes the item at the specified position.

**Parameters:** position

- the index of the item to delete

- getSelectedIndex

```java
public int getSelectedIndex()
```

Gets the index of the selected item on the list,

**Returns:** the index of the selected item;
if no item is selected, or if multiple items are
selected,

-1

is returned.
**See Also:** select(int)

,

deselect(int)

,

isIndexSelected(int)

- getSelectedIndexes

```java
public int[] getSelectedIndexes()
```

Gets the selected indexes on the list.

**Returns:** an array of the selected indexes on this scrolling list;
if no item is selected, a zero-length array is returned.
**See Also:** select(int)

,

deselect(int)

,

isIndexSelected(int)

- getSelectedItem

```java
public
String
getSelectedItem()
```

Gets the selected item on this scrolling list.

**Returns:** the selected item on the list;
if no item is selected, or if multiple items are
selected,

null

is returned.
**See Also:** select(int)

,

deselect(int)

,

isIndexSelected(int)

- getSelectedItems

```java
public
String
[] getSelectedItems()
```

Gets the selected items on this scrolling list.

**Returns:** an array of the selected items on this scrolling list;
if no item is selected, a zero-length array is returned.
**See Also:** select(int)

,

deselect(int)

,

isIndexSelected(int)

- getSelectedObjects

```java
public
Object
[] getSelectedObjects()
```

Gets the selected items on this scrolling list in an array of Objects.

**Specified by:** getSelectedObjects

in interface

ItemSelectable
**Returns:** an array of

Object

s representing the
selected items on this scrolling list;
if no item is selected, a zero-length array is returned.
**See Also:** getSelectedItems()

,

ItemSelectable

- select

```java
public void select​(int index)
```

Selects the item at the specified index in the scrolling list.

Note that passing out of range parameters is invalid,
and will result in unspecified behavior.

Note that this method should be primarily used to
initially select an item in this component.
Programmatically calling this method will

not

trigger
an

ItemEvent

. The only way to trigger an

ItemEvent

is by user interaction.

**Parameters:** index

- the position of the item to select
**See Also:** getSelectedItem()

,

deselect(int)

,

isIndexSelected(int)

- deselect

```java
public void deselect​(int index)
```

Deselects the item at the specified index.

Note that passing out of range parameters is invalid,
and will result in unspecified behavior.

If the item at the specified index is not selected,
then the operation is ignored.

**Parameters:** index

- the position of the item to deselect
**See Also:** select(int)

,

getSelectedItem()

,

isIndexSelected(int)

- isIndexSelected

```java
public boolean isIndexSelected​(int index)
```

Determines if the specified item in this scrolling list is
selected.

**Parameters:** index

- the item to be checked
**Returns:** true

if the specified item has been
selected;

false

otherwise
**Since:** 1.1
**See Also:** select(int)

,

deselect(int)

- isSelected

```java
@Deprecated

public boolean isSelected​(int index)
```

Deprecated.

As of JDK version 1.1,
replaced by

isIndexSelected(int)

.

Determines if the specified item in the list is selected.

**Parameters:** index

- specifies the item to be checked
**Returns:** true

if the item is selected; otherwise

false

- getRows

```java
public int getRows()
```

Gets the number of visible lines in this list. Note that
once the

List

has been created, this number
will never change.

**Returns:** the number of visible lines in this scrolling list

- isMultipleMode

```java
public boolean isMultipleMode()
```

Determines whether this list allows multiple selections.

**Returns:** true

if this list allows multiple
selections; otherwise,

false
**Since:** 1.1
**See Also:** setMultipleMode(boolean)

- allowsMultipleSelections

```java
@Deprecated

public boolean allowsMultipleSelections()
```

Deprecated.

As of JDK version 1.1,
replaced by

isMultipleMode()

.

Determines whether this list allows multiple selections.

**Returns:** true

if this list allows multiple
selections; otherwise

false

- setMultipleMode

```java
public void setMultipleMode​(boolean b)
```

Sets the flag that determines whether this list
allows multiple selections.
When the selection mode is changed from multiple-selection to
single-selection, the selected items change as follows:
If a selected item has the location cursor, only that
item will remain selected. If no selected item has the
location cursor, all items will be deselected.

**Parameters:** b

- if

true

then multiple selections
are allowed; otherwise, only one item from
the list can be selected at once
**Since:** 1.1
**See Also:** isMultipleMode()

- setMultipleSelections

```java
@Deprecated

public void setMultipleSelections​(boolean b)
```

Deprecated.

As of JDK version 1.1,
replaced by

setMultipleMode(boolean)

.

Enables or disables multiple selection mode for this list.

**Parameters:** b

-

true

to enable multiple mode,

false

otherwise

- getVisibleIndex

```java
public int getVisibleIndex()
```

Gets the index of the item that was last made visible by
the method

makeVisible

.

**Returns:** the index of the item that was last made visible
**See Also:** makeVisible(int)

- makeVisible

```java
public void makeVisible​(int index)
```

Makes the item at the specified index visible.

**Parameters:** index

- the position of the item
**See Also:** getVisibleIndex()

- getPreferredSize

```java
public
Dimension
getPreferredSize​(int rows)
```

Gets the preferred dimensions for a list with the specified
number of rows.

**Parameters:** rows

- number of rows in the list
**Returns:** the preferred dimensions for displaying this scrolling list
given that the specified number of rows must be visible
**Since:** 1.1
**See Also:** Component.getPreferredSize()

- preferredSize

```java
@Deprecated

public
Dimension
preferredSize​(int rows)
```

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize(int)

.

Returns the preferred size of this component
assuming it has the specified number of rows.

**Parameters:** rows

- the number of rows
**Returns:** the preferred dimensions for displaying this list

- getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Gets the preferred size of this scrolling list.

**Overrides:** getPreferredSize

in class

Component
**Returns:** the preferred dimensions for displaying this scrolling list
**Since:** 1.1
**See Also:** Component.getPreferredSize()

- preferredSize

```java
@Deprecated

public
Dimension
preferredSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

Description copied from class:

Component

Returns the component's preferred size.

**Overrides:** preferredSize

in class

Component
**Returns:** the component's preferred size

- getMinimumSize

```java
public
Dimension
getMinimumSize​(int rows)
```

Gets the minimum dimensions for a list with the specified
number of rows.

**Parameters:** rows

- number of rows in the list
**Returns:** the minimum dimensions for displaying this scrolling list
given that the specified number of rows must be visible
**Since:** 1.1
**See Also:** Component.getMinimumSize()

- minimumSize

```java
@Deprecated

public
Dimension
minimumSize​(int rows)
```

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize(int)

.

Returns the minimum dimensions for the list
with the specified number of rows.

**Parameters:** rows

- the number of rows in the list
**Returns:** the minimum dimensions for displaying this list

- getMinimumSize

```java
public
Dimension
getMinimumSize()
```

Determines the minimum size of this scrolling list.

**Overrides:** getMinimumSize

in class

Component
**Returns:** the minimum dimensions needed
to display this scrolling list
**Since:** 1.1
**See Also:** Component.getMinimumSize()

- minimumSize

```java
@Deprecated

public
Dimension
minimumSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

Description copied from class:

Component

Returns the minimum size of this component.

**Overrides:** minimumSize

in class

Component
**Returns:** the minimum size of this component

- addItemListener

```java
public void addItemListener​(
ItemListener
l)
```

Adds the specified item listener to receive item events from
this list. Item events are sent in response to user input, but not
in response to calls to

select

or

deselect

.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** addItemListener

in interface

ItemSelectable
**Parameters:** l

- the item listener
**Since:** 1.1
**See Also:** removeItemListener(java.awt.event.ItemListener)

,

getItemListeners()

,

select(int)

,

deselect(int)

,

ItemEvent

,

ItemListener

- removeItemListener

```java
public void removeItemListener​(
ItemListener
l)
```

Removes the specified item listener so that it no longer
receives item events from this list.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** removeItemListener

in interface

ItemSelectable
**Parameters:** l

- the item listener
**Since:** 1.1
**See Also:** addItemListener(java.awt.event.ItemListener)

,

getItemListeners()

,

ItemEvent

,

ItemListener

- getItemListeners

```java
public
ItemListener
[] getItemListeners()
```

Returns an array of all the item listeners
registered on this list.

**Returns:** all of this list's

ItemListener

s
or an empty array if no item
listeners are currently registered
**Since:** 1.4
**See Also:** addItemListener(java.awt.event.ItemListener)

,

removeItemListener(java.awt.event.ItemListener)

,

ItemEvent

,

ItemListener

- addActionListener

```java
public void addActionListener​(
ActionListener
l)
```

Adds the specified action listener to receive action events from
this list. Action events occur when a user double-clicks
on a list item or types Enter when the list has the keyboard
focus.

If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the action listener
**Since:** 1.1
**See Also:** removeActionListener(java.awt.event.ActionListener)

,

getActionListeners()

,

ActionEvent

,

ActionListener

- removeActionListener

```java
public void removeActionListener​(
ActionListener
l)
```

Removes the specified action listener so that it no longer
receives action events from this list. Action events
occur when a user double-clicks on a list item.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the action listener
**Since:** 1.1
**See Also:** addActionListener(java.awt.event.ActionListener)

,

getActionListeners()

,

ActionEvent

,

ActionListener

- getActionListeners

```java
public
ActionListener
[] getActionListeners()
```

Returns an array of all the action listeners
registered on this list.

**Returns:** all of this list's

ActionListener

s
or an empty array if no action
listeners are currently registered
**Since:** 1.4
**See Also:** addActionListener(java.awt.event.ActionListener)

,

removeActionListener(java.awt.event.ActionListener)

,

ActionEvent

,

ActionListener

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

List

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

List l

for its item listeners with the following code:

```java
ItemListener[] ils = (ItemListener[])(l.getListeners(ItemListener.class));
```

If no such listeners exist, this method returns an empty array.

**Overrides:** getListeners

in class

Component
**Type Parameters:** T

- the type of the listeners
**Parameters:** listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s on this list,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getItemListeners()

- processEvent

```java
protected void processEvent​(
AWTEvent
e)
```

Processes events on this scrolling list. If an event is
an instance of

ItemEvent

, it invokes the

processItemEvent

method. Else, if the
event is an instance of

ActionEvent

,
it invokes

processActionEvent

.
If the event is not an item event or an action event,
it invokes

processEvent

on the superclass.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:** processEvent

in class

Component
**Parameters:** e

- the event
**Since:** 1.1
**See Also:** ActionEvent

,

ItemEvent

,

processActionEvent(java.awt.event.ActionEvent)

,

processItemEvent(java.awt.event.ItemEvent)

- processItemEvent

```java
protected void processItemEvent​(
ItemEvent
e)
```

Processes item events occurring on this list by
dispatching them to any registered

ItemListener

objects.

This method is not called unless item events are
enabled for this component. Item events are enabled
when one of the following occurs:

- An

ItemListener

object is registered
via

addItemListener

.

Item events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the item event
**Since:** 1.1
**See Also:** ItemEvent

,

ItemListener

,

addItemListener(java.awt.event.ItemListener)

,

Component.enableEvents(long)

- processActionEvent

```java
protected void processActionEvent​(
ActionEvent
e)
```

Processes action events occurring on this component
by dispatching them to any registered

ActionListener

objects.

This method is not called unless action events are
enabled for this component. Action events are enabled
when one of the following occurs:

- An

ActionListener

object is registered
via

addActionListener

.

Action events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the action event
**Since:** 1.1
**See Also:** ActionEvent

,

ActionListener

,

addActionListener(java.awt.event.ActionListener)

,

Component.enableEvents(long)

- paramString

```java
protected
String
paramString()
```

Returns the parameter string representing the state of this
scrolling list. This string is useful for debugging.

**Overrides:** paramString

in class

Component
**Returns:** the parameter string of this scrolling list

- delItems

```java
@Deprecated

public void delItems​(int start,
int end)
```

Deprecated.

As of JDK version 1.1,
Not for public use in the future.
This method is expected to be retained only as a package
private method.

Deletes the list items in the specified index range.

**Parameters:** start

- the beginning index of the range to delete
**Parameters:** end

- the ending index of the range to delete

- getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated with this

List

. For lists, the

AccessibleContext

takes the form of an

AccessibleAWTList

.
A new

AccessibleAWTList

instance is created, if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an

AccessibleAWTList

that serves as the

AccessibleContext

of this

List
**Since:** 1.3

---

#### Method Detail

addNotify

```java
public void addNotify()
```

Creates the peer for the list. The peer allows us to modify the
list's appearance without changing its functionality.

**Overrides:** addNotify

in class

Component
**See Also:** Component.isDisplayable()

,

Component.removeNotify()

,

Component.invalidate()

---

#### addNotify

public void addNotify()

Creates the peer for the list. The peer allows us to modify the
list's appearance without changing its functionality.

removeNotify

```java
public void removeNotify()
```

Removes the peer for this list. The peer allows us to modify the
list's appearance without changing its functionality.

**Overrides:** removeNotify

in class

Component
**See Also:** Component.isDisplayable()

,

Component.addNotify()

---

#### removeNotify

public void removeNotify()

Removes the peer for this list. The peer allows us to modify the
list's appearance without changing its functionality.

getItemCount

```java
public int getItemCount()
```

Gets the number of items in the list.

**Returns:** the number of items in the list
**Since:** 1.1
**See Also:** getItem(int)

---

#### getItemCount

public int getItemCount()

Gets the number of items in the list.

countItems

```java
@Deprecated

public int countItems()
```

Deprecated.

As of JDK version 1.1,
replaced by

getItemCount()

.

Returns the number of items in the list.

**Returns:** the number of items in the list

---

#### countItems

@Deprecated

public int countItems()

Returns the number of items in the list.

getItem

```java
public
String
getItem​(int index)
```

Gets the item associated with the specified index.

**Parameters:** index

- the position of the item
**Returns:** an item that is associated with
the specified index
**See Also:** getItemCount()

---

#### getItem

public

String

getItem​(int index)

Gets the item associated with the specified index.

getItems

```java
public
String
[] getItems()
```

Gets the items in the list.

**Returns:** a string array containing items of the list
**Since:** 1.1
**See Also:** select(int)

,

deselect(int)

,

isIndexSelected(int)

---

#### getItems

public

String

[] getItems()

Gets the items in the list.

add

```java
public void add​(
String
item)
```

Adds the specified item to the end of scrolling list.

**Parameters:** item

- the item to be added
**Since:** 1.1

---

#### add

public void add​(

String

item)

Adds the specified item to the end of scrolling list.

addItem

```java
@Deprecated

public void addItem​(
String
item)
```

Deprecated.

replaced by

add(String)

.

Adds the specified item to the end of the list.

**Parameters:** item

- the item to be added

---

#### addItem

@Deprecated

public void addItem​(

String

item)

Adds the specified item to the end of the list.

add

```java
public void add​(
String
item,
int index)
```

Adds the specified item to the scrolling list
at the position indicated by the index. The index is
zero-based. If the value of the index is less than zero,
or if the value of the index is greater than or equal to
the number of items in the list, then the item is added
to the end of the list.

**Parameters:** item

- the item to be added;
if this parameter is

null

then the item is
treated as an empty string,

""
**Parameters:** index

- the position at which to add the item
**Since:** 1.1

---

#### add

public void add​(

String

item,
int index)

Adds the specified item to the scrolling list
at the position indicated by the index. The index is
zero-based. If the value of the index is less than zero,
or if the value of the index is greater than or equal to
the number of items in the list, then the item is added
to the end of the list.

addItem

```java
@Deprecated

public void addItem​(
String
item,
int index)
```

Deprecated.

replaced by

add(String, int)

.

Adds the specified item to the list
at the position indicated by the index.

**Parameters:** item

- the item to be added
**Parameters:** index

- the position at which to add the item

---

#### addItem

@Deprecated

public void addItem​(

String

item,
int index)

Adds the specified item to the list
at the position indicated by the index.

replaceItem

```java
public void replaceItem​(
String
newValue,
int index)
```

Replaces the item at the specified index in the scrolling list
with the new string.

**Parameters:** newValue

- a new string to replace an existing item
**Parameters:** index

- the position of the item to replace
**Throws:** ArrayIndexOutOfBoundsException

- if

index

is out of range

---

#### replaceItem

public void replaceItem​(

String

newValue,
int index)

Replaces the item at the specified index in the scrolling list
with the new string.

removeAll

```java
public void removeAll()
```

Removes all items from this list.

**Since:** 1.1
**See Also:** remove(java.lang.String)

,

delItems(int, int)

---

#### removeAll

public void removeAll()

Removes all items from this list.

clear

```java
@Deprecated

public void clear()
```

Deprecated.

As of JDK version 1.1,
replaced by

removeAll()

.

---

#### clear

@Deprecated

public void clear()

remove

```java
public void remove​(
String
item)
```

Removes the first occurrence of an item from the list.
If the specified item is selected, and is the only selected
item in the list, the list is set to have no selection.

**Parameters:** item

- the item to remove from the list
**Throws:** IllegalArgumentException

- if the item doesn't exist in the list
**Since:** 1.1

---

#### remove

public void remove​(

String

item)

Removes the first occurrence of an item from the list.
If the specified item is selected, and is the only selected
item in the list, the list is set to have no selection.

remove

```java
public void remove​(int position)
```

Removes the item at the specified position
from this scrolling list.
If the item with the specified position is selected, and is the
only selected item in the list, the list is set to have no selection.

**Parameters:** position

- the index of the item to delete
**Throws:** ArrayIndexOutOfBoundsException

- if the

position

is less than 0 or
greater than

getItemCount()-1
**Since:** 1.1
**See Also:** add(String, int)

---

#### remove

public void remove​(int position)

Removes the item at the specified position
from this scrolling list.
If the item with the specified position is selected, and is the
only selected item in the list, the list is set to have no selection.

delItem

```java
@Deprecated

public void delItem​(int position)
```

Deprecated.

replaced by

remove(String)

and

remove(int)

.

Removes the item at the specified position.

**Parameters:** position

- the index of the item to delete

---

#### delItem

@Deprecated

public void delItem​(int position)

Removes the item at the specified position.

getSelectedIndex

```java
public int getSelectedIndex()
```

Gets the index of the selected item on the list,

**Returns:** the index of the selected item;
if no item is selected, or if multiple items are
selected,

-1

is returned.
**See Also:** select(int)

,

deselect(int)

,

isIndexSelected(int)

---

#### getSelectedIndex

public int getSelectedIndex()

Gets the index of the selected item on the list,

getSelectedIndexes

```java
public int[] getSelectedIndexes()
```

Gets the selected indexes on the list.

**Returns:** an array of the selected indexes on this scrolling list;
if no item is selected, a zero-length array is returned.
**See Also:** select(int)

,

deselect(int)

,

isIndexSelected(int)

---

#### getSelectedIndexes

public int[] getSelectedIndexes()

Gets the selected indexes on the list.

getSelectedItem

```java
public
String
getSelectedItem()
```

Gets the selected item on this scrolling list.

**Returns:** the selected item on the list;
if no item is selected, or if multiple items are
selected,

null

is returned.
**See Also:** select(int)

,

deselect(int)

,

isIndexSelected(int)

---

#### getSelectedItem

public

String

getSelectedItem()

Gets the selected item on this scrolling list.

getSelectedItems

```java
public
String
[] getSelectedItems()
```

Gets the selected items on this scrolling list.

**Returns:** an array of the selected items on this scrolling list;
if no item is selected, a zero-length array is returned.
**See Also:** select(int)

,

deselect(int)

,

isIndexSelected(int)

---

#### getSelectedItems

public

String

[] getSelectedItems()

Gets the selected items on this scrolling list.

getSelectedObjects

```java
public
Object
[] getSelectedObjects()
```

Gets the selected items on this scrolling list in an array of Objects.

**Specified by:** getSelectedObjects

in interface

ItemSelectable
**Returns:** an array of

Object

s representing the
selected items on this scrolling list;
if no item is selected, a zero-length array is returned.
**See Also:** getSelectedItems()

,

ItemSelectable

---

#### getSelectedObjects

public

Object

[] getSelectedObjects()

Gets the selected items on this scrolling list in an array of Objects.

select

```java
public void select​(int index)
```

Selects the item at the specified index in the scrolling list.

Note that passing out of range parameters is invalid,
and will result in unspecified behavior.

Note that this method should be primarily used to
initially select an item in this component.
Programmatically calling this method will

not

trigger
an

ItemEvent

. The only way to trigger an

ItemEvent

is by user interaction.

**Parameters:** index

- the position of the item to select
**See Also:** getSelectedItem()

,

deselect(int)

,

isIndexSelected(int)

---

#### select

public void select​(int index)

Selects the item at the specified index in the scrolling list.

Note that passing out of range parameters is invalid,
and will result in unspecified behavior.

Note that this method should be primarily used to
initially select an item in this component.
Programmatically calling this method will

not

trigger
an

ItemEvent

. The only way to trigger an

ItemEvent

is by user interaction.

Note that passing out of range parameters is invalid,
and will result in unspecified behavior.

Note that this method should be primarily used to
initially select an item in this component.
Programmatically calling this method will

not

trigger
an

ItemEvent

. The only way to trigger an

ItemEvent

is by user interaction.

Note that this method should be primarily used to
initially select an item in this component.
Programmatically calling this method will

not

trigger
an

ItemEvent

. The only way to trigger an

ItemEvent

is by user interaction.

deselect

```java
public void deselect​(int index)
```

Deselects the item at the specified index.

Note that passing out of range parameters is invalid,
and will result in unspecified behavior.

If the item at the specified index is not selected,
then the operation is ignored.

**Parameters:** index

- the position of the item to deselect
**See Also:** select(int)

,

getSelectedItem()

,

isIndexSelected(int)

---

#### deselect

public void deselect​(int index)

Deselects the item at the specified index.

Note that passing out of range parameters is invalid,
and will result in unspecified behavior.

If the item at the specified index is not selected,
then the operation is ignored.

Note that passing out of range parameters is invalid,
and will result in unspecified behavior.

If the item at the specified index is not selected,
then the operation is ignored.

If the item at the specified index is not selected,
then the operation is ignored.

isIndexSelected

```java
public boolean isIndexSelected​(int index)
```

Determines if the specified item in this scrolling list is
selected.

**Parameters:** index

- the item to be checked
**Returns:** true

if the specified item has been
selected;

false

otherwise
**Since:** 1.1
**See Also:** select(int)

,

deselect(int)

---

#### isIndexSelected

public boolean isIndexSelected​(int index)

Determines if the specified item in this scrolling list is
selected.

isSelected

```java
@Deprecated

public boolean isSelected​(int index)
```

Deprecated.

As of JDK version 1.1,
replaced by

isIndexSelected(int)

.

Determines if the specified item in the list is selected.

**Parameters:** index

- specifies the item to be checked
**Returns:** true

if the item is selected; otherwise

false

---

#### isSelected

@Deprecated

public boolean isSelected​(int index)

Determines if the specified item in the list is selected.

getRows

```java
public int getRows()
```

Gets the number of visible lines in this list. Note that
once the

List

has been created, this number
will never change.

**Returns:** the number of visible lines in this scrolling list

---

#### getRows

public int getRows()

Gets the number of visible lines in this list. Note that
once the

List

has been created, this number
will never change.

isMultipleMode

```java
public boolean isMultipleMode()
```

Determines whether this list allows multiple selections.

**Returns:** true

if this list allows multiple
selections; otherwise,

false
**Since:** 1.1
**See Also:** setMultipleMode(boolean)

---

#### isMultipleMode

public boolean isMultipleMode()

Determines whether this list allows multiple selections.

allowsMultipleSelections

```java
@Deprecated

public boolean allowsMultipleSelections()
```

Deprecated.

As of JDK version 1.1,
replaced by

isMultipleMode()

.

Determines whether this list allows multiple selections.

**Returns:** true

if this list allows multiple
selections; otherwise

false

---

#### allowsMultipleSelections

@Deprecated

public boolean allowsMultipleSelections()

Determines whether this list allows multiple selections.

setMultipleMode

```java
public void setMultipleMode​(boolean b)
```

Sets the flag that determines whether this list
allows multiple selections.
When the selection mode is changed from multiple-selection to
single-selection, the selected items change as follows:
If a selected item has the location cursor, only that
item will remain selected. If no selected item has the
location cursor, all items will be deselected.

**Parameters:** b

- if

true

then multiple selections
are allowed; otherwise, only one item from
the list can be selected at once
**Since:** 1.1
**See Also:** isMultipleMode()

---

#### setMultipleMode

public void setMultipleMode​(boolean b)

Sets the flag that determines whether this list
allows multiple selections.
When the selection mode is changed from multiple-selection to
single-selection, the selected items change as follows:
If a selected item has the location cursor, only that
item will remain selected. If no selected item has the
location cursor, all items will be deselected.

setMultipleSelections

```java
@Deprecated

public void setMultipleSelections​(boolean b)
```

Deprecated.

As of JDK version 1.1,
replaced by

setMultipleMode(boolean)

.

Enables or disables multiple selection mode for this list.

**Parameters:** b

-

true

to enable multiple mode,

false

otherwise

---

#### setMultipleSelections

@Deprecated

public void setMultipleSelections​(boolean b)

Enables or disables multiple selection mode for this list.

getVisibleIndex

```java
public int getVisibleIndex()
```

Gets the index of the item that was last made visible by
the method

makeVisible

.

**Returns:** the index of the item that was last made visible
**See Also:** makeVisible(int)

---

#### getVisibleIndex

public int getVisibleIndex()

Gets the index of the item that was last made visible by
the method

makeVisible

.

makeVisible

```java
public void makeVisible​(int index)
```

Makes the item at the specified index visible.

**Parameters:** index

- the position of the item
**See Also:** getVisibleIndex()

---

#### makeVisible

public void makeVisible​(int index)

Makes the item at the specified index visible.

getPreferredSize

```java
public
Dimension
getPreferredSize​(int rows)
```

Gets the preferred dimensions for a list with the specified
number of rows.

**Parameters:** rows

- number of rows in the list
**Returns:** the preferred dimensions for displaying this scrolling list
given that the specified number of rows must be visible
**Since:** 1.1
**See Also:** Component.getPreferredSize()

---

#### getPreferredSize

public

Dimension

getPreferredSize​(int rows)

Gets the preferred dimensions for a list with the specified
number of rows.

preferredSize

```java
@Deprecated

public
Dimension
preferredSize​(int rows)
```

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize(int)

.

Returns the preferred size of this component
assuming it has the specified number of rows.

**Parameters:** rows

- the number of rows
**Returns:** the preferred dimensions for displaying this list

---

#### preferredSize

@Deprecated

public

Dimension

preferredSize​(int rows)

Returns the preferred size of this component
assuming it has the specified number of rows.

getPreferredSize

```java
public
Dimension
getPreferredSize()
```

Gets the preferred size of this scrolling list.

**Overrides:** getPreferredSize

in class

Component
**Returns:** the preferred dimensions for displaying this scrolling list
**Since:** 1.1
**See Also:** Component.getPreferredSize()

---

#### getPreferredSize

public

Dimension

getPreferredSize()

Gets the preferred size of this scrolling list.

preferredSize

```java
@Deprecated

public
Dimension
preferredSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getPreferredSize()

.

Description copied from class:

Component

Returns the component's preferred size.

**Overrides:** preferredSize

in class

Component
**Returns:** the component's preferred size

---

#### preferredSize

@Deprecated

public

Dimension

preferredSize()

Description copied from class:

Component

Returns the component's preferred size.

getMinimumSize

```java
public
Dimension
getMinimumSize​(int rows)
```

Gets the minimum dimensions for a list with the specified
number of rows.

**Parameters:** rows

- number of rows in the list
**Returns:** the minimum dimensions for displaying this scrolling list
given that the specified number of rows must be visible
**Since:** 1.1
**See Also:** Component.getMinimumSize()

---

#### getMinimumSize

public

Dimension

getMinimumSize​(int rows)

Gets the minimum dimensions for a list with the specified
number of rows.

minimumSize

```java
@Deprecated

public
Dimension
minimumSize​(int rows)
```

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize(int)

.

Returns the minimum dimensions for the list
with the specified number of rows.

**Parameters:** rows

- the number of rows in the list
**Returns:** the minimum dimensions for displaying this list

---

#### minimumSize

@Deprecated

public

Dimension

minimumSize​(int rows)

Returns the minimum dimensions for the list
with the specified number of rows.

getMinimumSize

```java
public
Dimension
getMinimumSize()
```

Determines the minimum size of this scrolling list.

**Overrides:** getMinimumSize

in class

Component
**Returns:** the minimum dimensions needed
to display this scrolling list
**Since:** 1.1
**See Also:** Component.getMinimumSize()

---

#### getMinimumSize

public

Dimension

getMinimumSize()

Determines the minimum size of this scrolling list.

minimumSize

```java
@Deprecated

public
Dimension
minimumSize()
```

Deprecated.

As of JDK version 1.1,
replaced by

getMinimumSize()

.

Description copied from class:

Component

Returns the minimum size of this component.

**Overrides:** minimumSize

in class

Component
**Returns:** the minimum size of this component

---

#### minimumSize

@Deprecated

public

Dimension

minimumSize()

Description copied from class:

Component

Returns the minimum size of this component.

addItemListener

```java
public void addItemListener​(
ItemListener
l)
```

Adds the specified item listener to receive item events from
this list. Item events are sent in response to user input, but not
in response to calls to

select

or

deselect

.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** addItemListener

in interface

ItemSelectable
**Parameters:** l

- the item listener
**Since:** 1.1
**See Also:** removeItemListener(java.awt.event.ItemListener)

,

getItemListeners()

,

select(int)

,

deselect(int)

,

ItemEvent

,

ItemListener

---

#### addItemListener

public void addItemListener​(

ItemListener

l)

Adds the specified item listener to receive item events from
this list. Item events are sent in response to user input, but not
in response to calls to

select

or

deselect

.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

removeItemListener

```java
public void removeItemListener​(
ItemListener
l)
```

Removes the specified item listener so that it no longer
receives item events from this list.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Specified by:** removeItemListener

in interface

ItemSelectable
**Parameters:** l

- the item listener
**Since:** 1.1
**See Also:** addItemListener(java.awt.event.ItemListener)

,

getItemListeners()

,

ItemEvent

,

ItemListener

---

#### removeItemListener

public void removeItemListener​(

ItemListener

l)

Removes the specified item listener so that it no longer
receives item events from this list.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

getItemListeners

```java
public
ItemListener
[] getItemListeners()
```

Returns an array of all the item listeners
registered on this list.

**Returns:** all of this list's

ItemListener

s
or an empty array if no item
listeners are currently registered
**Since:** 1.4
**See Also:** addItemListener(java.awt.event.ItemListener)

,

removeItemListener(java.awt.event.ItemListener)

,

ItemEvent

,

ItemListener

---

#### getItemListeners

public

ItemListener

[] getItemListeners()

Returns an array of all the item listeners
registered on this list.

addActionListener

```java
public void addActionListener​(
ActionListener
l)
```

Adds the specified action listener to receive action events from
this list. Action events occur when a user double-clicks
on a list item or types Enter when the list has the keyboard
focus.

If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the action listener
**Since:** 1.1
**See Also:** removeActionListener(java.awt.event.ActionListener)

,

getActionListeners()

,

ActionEvent

,

ActionListener

---

#### addActionListener

public void addActionListener​(

ActionListener

l)

Adds the specified action listener to receive action events from
this list. Action events occur when a user double-clicks
on a list item or types Enter when the list has the keyboard
focus.

If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

removeActionListener

```java
public void removeActionListener​(
ActionListener
l)
```

Removes the specified action listener so that it no longer
receives action events from this list. Action events
occur when a user double-clicks on a list item.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

**Parameters:** l

- the action listener
**Since:** 1.1
**See Also:** addActionListener(java.awt.event.ActionListener)

,

getActionListeners()

,

ActionEvent

,

ActionListener

---

#### removeActionListener

public void removeActionListener​(

ActionListener

l)

Removes the specified action listener so that it no longer
receives action events from this list. Action events
occur when a user double-clicks on a list item.
If listener

l

is

null

,
no exception is thrown and no action is performed.

Refer to

AWT Threading Issues

for details on AWT's threading model.

Refer to

AWT Threading Issues

for details on AWT's threading model.

getActionListeners

```java
public
ActionListener
[] getActionListeners()
```

Returns an array of all the action listeners
registered on this list.

**Returns:** all of this list's

ActionListener

s
or an empty array if no action
listeners are currently registered
**Since:** 1.4
**See Also:** addActionListener(java.awt.event.ActionListener)

,

removeActionListener(java.awt.event.ActionListener)

,

ActionEvent

,

ActionListener

---

#### getActionListeners

public

ActionListener

[] getActionListeners()

Returns an array of all the action listeners
registered on this list.

getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

List

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

List l

for its item listeners with the following code:

```java
ItemListener[] ils = (ItemListener[])(l.getListeners(ItemListener.class));
```

If no such listeners exist, this method returns an empty array.

**Overrides:** getListeners

in class

Component
**Type Parameters:** T

- the type of the listeners
**Parameters:** listenerType

- the type of listeners requested; this parameter
should specify an interface that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s on this list,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getItemListeners()

---

#### getListeners

public <T extends

EventListener

> T[] getListeners​(

Class

<T> listenerType)

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this

List

.

Foo

Listener

s are registered using the

add

Foo

Listener

method.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

List l

for its item listeners with the following code:

```java
ItemListener[] ils = (ItemListener[])(l.getListeners(ItemListener.class));
```

If no such listeners exist, this method returns an empty array.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

List l

for its item listeners with the following code:

```java
ItemListener[] ils = (ItemListener[])(l.getListeners(ItemListener.class));
```

If no such listeners exist, this method returns an empty array.

ItemListener[] ils = (ItemListener[])(l.getListeners(ItemListener.class));

processEvent

```java
protected void processEvent​(
AWTEvent
e)
```

Processes events on this scrolling list. If an event is
an instance of

ItemEvent

, it invokes the

processItemEvent

method. Else, if the
event is an instance of

ActionEvent

,
it invokes

processActionEvent

.
If the event is not an item event or an action event,
it invokes

processEvent

on the superclass.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Overrides:** processEvent

in class

Component
**Parameters:** e

- the event
**Since:** 1.1
**See Also:** ActionEvent

,

ItemEvent

,

processActionEvent(java.awt.event.ActionEvent)

,

processItemEvent(java.awt.event.ItemEvent)

---

#### processEvent

protected void processEvent​(

AWTEvent

e)

Processes events on this scrolling list. If an event is
an instance of

ItemEvent

, it invokes the

processItemEvent

method. Else, if the
event is an instance of

ActionEvent

,
it invokes

processActionEvent

.
If the event is not an item event or an action event,
it invokes

processEvent

on the superclass.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

processItemEvent

```java
protected void processItemEvent​(
ItemEvent
e)
```

Processes item events occurring on this list by
dispatching them to any registered

ItemListener

objects.

This method is not called unless item events are
enabled for this component. Item events are enabled
when one of the following occurs:

- An

ItemListener

object is registered
via

addItemListener

.

Item events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the item event
**Since:** 1.1
**See Also:** ItemEvent

,

ItemListener

,

addItemListener(java.awt.event.ItemListener)

,

Component.enableEvents(long)

---

#### processItemEvent

protected void processItemEvent​(

ItemEvent

e)

Processes item events occurring on this list by
dispatching them to any registered

ItemListener

objects.

This method is not called unless item events are
enabled for this component. Item events are enabled
when one of the following occurs:

- An

ItemListener

object is registered
via

addItemListener

.

Item events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

This method is not called unless item events are
enabled for this component. Item events are enabled
when one of the following occurs:

- An

ItemListener

object is registered
via

addItemListener

.

Item events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

An

ItemListener

object is registered
via

addItemListener

.

Item events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

processActionEvent

```java
protected void processActionEvent​(
ActionEvent
e)
```

Processes action events occurring on this component
by dispatching them to any registered

ActionListener

objects.

This method is not called unless action events are
enabled for this component. Action events are enabled
when one of the following occurs:

- An

ActionListener

object is registered
via

addActionListener

.

Action events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

**Parameters:** e

- the action event
**Since:** 1.1
**See Also:** ActionEvent

,

ActionListener

,

addActionListener(java.awt.event.ActionListener)

,

Component.enableEvents(long)

---

#### processActionEvent

protected void processActionEvent​(

ActionEvent

e)

Processes action events occurring on this component
by dispatching them to any registered

ActionListener

objects.

This method is not called unless action events are
enabled for this component. Action events are enabled
when one of the following occurs:

- An

ActionListener

object is registered
via

addActionListener

.

Action events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

This method is not called unless action events are
enabled for this component. Action events are enabled
when one of the following occurs:

- An

ActionListener

object is registered
via

addActionListener

.

Action events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

An

ActionListener

object is registered
via

addActionListener

.

Action events are enabled via

enableEvents

.

Note that if the event parameter is

null

the behavior is unspecified and may result in an
exception.

paramString

```java
protected
String
paramString()
```

Returns the parameter string representing the state of this
scrolling list. This string is useful for debugging.

**Overrides:** paramString

in class

Component
**Returns:** the parameter string of this scrolling list

---

#### paramString

protected

String

paramString()

Returns the parameter string representing the state of this
scrolling list. This string is useful for debugging.

delItems

```java
@Deprecated

public void delItems​(int start,
int end)
```

Deprecated.

As of JDK version 1.1,
Not for public use in the future.
This method is expected to be retained only as a package
private method.

Deletes the list items in the specified index range.

**Parameters:** start

- the beginning index of the range to delete
**Parameters:** end

- the ending index of the range to delete

---

#### delItems

@Deprecated

public void delItems​(int start,
int end)

Deletes the list items in the specified index range.

getAccessibleContext

```java
public
AccessibleContext
getAccessibleContext()
```

Gets the

AccessibleContext

associated with this

List

. For lists, the

AccessibleContext

takes the form of an

AccessibleAWTList

.
A new

AccessibleAWTList

instance is created, if necessary.

**Specified by:** getAccessibleContext

in interface

Accessible
**Overrides:** getAccessibleContext

in class

Component
**Returns:** an

AccessibleAWTList

that serves as the

AccessibleContext

of this

List
**Since:** 1.3

---

#### getAccessibleContext

public

AccessibleContext

getAccessibleContext()

Gets the

AccessibleContext

associated with this

List

. For lists, the

AccessibleContext

takes the form of an

AccessibleAWTList

.
A new

AccessibleAWTList

instance is created, if necessary.

---

