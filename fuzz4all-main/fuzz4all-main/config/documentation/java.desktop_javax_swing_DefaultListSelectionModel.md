# Class DefaultListSelectionModel

**Source:** `java.desktop\javax\swing\DefaultListSelectionModel.html`

### Class Description

```java
public class
DefaultListSelectionModel

extends
Object

implements
ListSelectionModel
,
Cloneable
,
Serializable
```

Default data model for list selections.

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

**All Implemented Interfaces:** Serializable

,

Cloneable

,

ListSelectionModel

---

### Field Details

#### protected
EventListenerList
listenerList

The list of listeners.

---

#### protected boolean leadAnchorNotificationEnabled

Whether or not the lead anchor notification is enabled.

---

### Constructor Details

#### public DefaultListSelectionModel()

*No description found.*

---

### Method Details

#### public void setSelectionMode​(int selectionMode)

Sets the selection mode. The following list describes the accepted
selection modes:

- ListSelectionModel.SINGLE_SELECTION

-
Only one list index can be selected at a time. In this mode,

setSelectionInterval

and

addSelectionInterval

are
equivalent, both replacing the current selection with the index
represented by the second argument (the "lead").

ListSelectionModel.SINGLE_INTERVAL_SELECTION

-
Only one contiguous interval can be selected at a time.
In this mode,

addSelectionInterval

behaves like

setSelectionInterval

(replacing the current selection),
unless the given interval is immediately adjacent to or overlaps
the existing selection, and can therefore be used to grow it.

ListSelectionModel.MULTIPLE_INTERVAL_SELECTION

-
In this mode, there's no restriction on what can be selected.

**Specified by:**
- setSelectionMode

in interface

ListSelectionModel

**Parameters:**
- selectionMode

- the selection mode

**Throws:**
- IllegalArgumentException

- if the selection mode isn't
one of those allowed

**See Also:**
- ListSelectionModel.getSelectionMode()

---

#### public
ListSelectionListener
[] getListSelectionListeners()

Returns an array of all the list selection listeners
registered on this

DefaultListSelectionModel

.

**Returns:**
- all of this model's

ListSelectionListener

s
or an empty
array if no list selection listeners are currently registered

**See Also:**
- ListSelectionModel.addListSelectionListener(javax.swing.event.ListSelectionListener)

,

ListSelectionModel.removeListSelectionListener(javax.swing.event.ListSelectionListener)

**Since:**
- 1.4

---

#### protected void fireValueChanged​(boolean isAdjusting)

Notifies listeners that we have ended a series of adjustments.

**Parameters:**
- isAdjusting

- true if this is the final change in a series of
adjustments

---

#### protected void fireValueChanged​(int firstIndex,
int lastIndex)

Notifies

ListSelectionListeners

that the value
of the selection, in the closed interval

firstIndex

,

lastIndex

, has changed.

**Parameters:**
- firstIndex

- the first index in the interval
- lastIndex

- the last index in the interval

---

#### protected void fireValueChanged​(int firstIndex,
int lastIndex,
boolean isAdjusting)

**Parameters:**
- firstIndex

- the first index in the interval
- lastIndex

- the last index in the interval
- isAdjusting

- true if this is the final change in a series of
adjustments

**See Also:**
- EventListenerList

---

#### public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Foo

Listener

s
are registered using the

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

DefaultListSelectionModel

instance

m

for its list selection listeners
with the following code:

```java
ListSelectionListener[] lsls = (ListSelectionListener[])(m.getListeners(ListSelectionListener.class));
```

If no such listeners exist,
this method returns an empty array.

**Parameters:**
- listenerType

- the type of listeners requested;
this parameter should specify an interface
that descends from

java.util.EventListener

**Returns:**
- an array of all objects registered as

Foo

Listener

s
on this model,
or an empty array if no such
listeners have been added

**Throws:**
- ClassCastException

- if

listenerType

doesn't
specify a class or interface that implements

java.util.EventListener

**See Also:**
- getListSelectionListeners()

**Since:**
- 1.3

**Type Parameters:**
- T

- the type of

EventListener

class being requested

---

#### public void setLeadAnchorNotificationEnabled​(boolean flag)

Sets the value of the leadAnchorNotificationEnabled flag.

**Parameters:**
- flag

- boolean value for

leadAnchorNotificationEnabled

**See Also:**
- isLeadAnchorNotificationEnabled()

---

#### public boolean isLeadAnchorNotificationEnabled()

Returns the value of the

leadAnchorNotificationEnabled

flag.
When

leadAnchorNotificationEnabled

is true the model
generates notification events with bounds that cover all the changes to
the selection plus the changes to the lead and anchor indices.
Setting the flag to false causes a narrowing of the event's bounds to
include only the elements that have been selected or deselected since
the last change. Either way, the model continues to maintain the lead
and anchor variables internally. The default is true.

Note: It is possible for the lead or anchor to be changed without a
change to the selection. Notification of these changes is often
important, such as when the new lead or anchor needs to be updated in
the view. Therefore, caution is urged when changing the default value.

**Returns:**
- the value of the

leadAnchorNotificationEnabled

flag

**See Also:**
- setLeadAnchorNotificationEnabled(boolean)

---

#### public void setSelectionInterval​(int index0,
int index1)

Changes the selection to be between

index0

and

index1

inclusive.

index0

doesn't have to be less than or equal to

index1

.

In

SINGLE_SELECTION

selection mode, only the second index
is used.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

**Specified by:**
- setSelectionInterval

in interface

ListSelectionModel

**Parameters:**
- index0

- one end of the interval.
- index1

- other end of the interval

**Throws:**
- IndexOutOfBoundsException

- if either index is less than

-1

(and neither index is

-1

)

**See Also:**
- ListSelectionModel.addListSelectionListener(javax.swing.event.ListSelectionListener)

---

#### public void addSelectionInterval​(int index0,
int index1)

Changes the selection to be the set union of the current selection
and the indices between

index0

and

index1

inclusive.

In

SINGLE_SELECTION

selection mode, this is equivalent
to calling

setSelectionInterval

, and only the second index
is used. In

SINGLE_INTERVAL_SELECTION

selection mode, this
method behaves like

setSelectionInterval

, unless the given
interval is immediately adjacent to or overlaps the existing selection,
and can therefore be used to grow it.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change. Note that

index0

doesn't have to be less than or equal to

index1

.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

**Specified by:**
- addSelectionInterval

in interface

ListSelectionModel

**Parameters:**
- index0

- one end of the interval.
- index1

- other end of the interval

**Throws:**
- IndexOutOfBoundsException

- if either index is less than

-1

(and neither index is

-1

)

**See Also:**
- ListSelectionModel.addListSelectionListener(javax.swing.event.ListSelectionListener)

,

setSelectionInterval(int, int)

---

#### public void removeSelectionInterval​(int index0,
int index1)

Changes the selection to be the set difference of the current selection
and the indices between

index0

and

index1

inclusive.

index0

doesn't have to be less than or equal to

index1

.

In

SINGLE_INTERVAL_SELECTION

selection mode, if the removal
would produce two disjoint selections, the removal is extended through
the greater end of the selection. For example, if the selection is

0-10

and you supply indices

5,6

(in any order) the
resulting selection is

0-4

.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

**Specified by:**
- removeSelectionInterval

in interface

ListSelectionModel

**Parameters:**
- index0

- one end of the interval
- index1

- other end of the interval

**Throws:**
- IndexOutOfBoundsException

- if either index is less than

-1

(and neither index is

-1

)

**See Also:**
- ListSelectionModel.addListSelectionListener(javax.swing.event.ListSelectionListener)

---

#### public void insertIndexInterval​(int index,
int length,
boolean before)

Insert length indices beginning before/after index. If the value
at index is itself selected and the selection mode is not
SINGLE_SELECTION, set all of the newly inserted items as selected.
Otherwise leave them unselected. This method is typically
called to sync the selection model with a corresponding change
in the data model.

**Specified by:**
- insertIndexInterval

in interface

ListSelectionModel

**Parameters:**
- index

- the beginning of the interval
- length

- the length of the interval
- before

- if

true

, interval inserts before the

index

,
otherwise, interval inserts after the

index

---

#### public void removeIndexInterval​(int index0,
int index1)

Remove the indices in the interval index0,index1 (inclusive) from
the selection model. This is typically called to sync the selection
model width a corresponding change in the data model. Note
that (as always) index0 need not be <= index1.

**Specified by:**
- removeIndexInterval

in interface

ListSelectionModel

**Parameters:**
- index0

- the beginning of the interval
- index1

- the end of the interval

---

#### public
String
toString()

Returns a string that displays and identifies this
object's properties.

**Overrides:**
- toString

in class

Object

**Returns:**
- a

String

representation of this object

---

#### public
Object
clone()
throws
CloneNotSupportedException

Returns a clone of this selection model with the same selection.

listenerLists

are not duplicated.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this instance.

**Throws:**
- CloneNotSupportedException

- if the selection model does not
both (a) implement the Cloneable interface and (b) define a

clone

method.

**See Also:**
- Cloneable

---

#### public void setAnchorSelectionIndex​(int anchorIndex)

Set the anchor selection index, leaving all selection values unchanged.
If leadAnchorNotificationEnabled is true, send a notification covering
the old and new anchor cells.

**Specified by:**
- setAnchorSelectionIndex

in interface

ListSelectionModel

**Parameters:**
- anchorIndex

- the anchor selection index

**See Also:**
- ListSelectionModel.getAnchorSelectionIndex()

,

setLeadSelectionIndex(int)

---

#### public void moveLeadSelectionIndex​(int leadIndex)

Set the lead selection index, leaving all selection values unchanged.
If leadAnchorNotificationEnabled is true, send a notification covering
the old and new lead cells.

**Parameters:**
- leadIndex

- the new lead selection index

**See Also:**
- setAnchorSelectionIndex(int)

,

setLeadSelectionIndex(int)

,

ListSelectionModel.getLeadSelectionIndex()

**Since:**
- 1.5

---

#### public void setLeadSelectionIndex​(int leadIndex)

Sets the lead selection index, ensuring that values between the
anchor and the new lead are either all selected or all deselected.
If the value at the anchor index is selected, first clear all the
values in the range [anchor, oldLeadIndex], then select all the values
values in the range [anchor, newLeadIndex], where oldLeadIndex is the old
leadIndex and newLeadIndex is the new one.

If the value at the anchor index is not selected, do the same thing in
reverse selecting values in the old range and deselecting values in the
new one.

Generate a single event for this change and notify all listeners.
For the purposes of generating minimal bounds in this event, do the
operation in a single pass; that way the first and last index inside the
ListSelectionEvent that is broadcast will refer to cells that actually
changed value because of this method. If, instead, this operation were
done in two steps the effect on the selection state would be the same
but two events would be generated and the bounds around the changed
values would be wider, including cells that had been first cleared only
to later be set.

This method can be used in the

mouseDragged

method
of a UI class to extend a selection.

**Specified by:**
- setLeadSelectionIndex

in interface

ListSelectionModel

**Parameters:**
- leadIndex

- the lead selection index

**See Also:**
- ListSelectionModel.getLeadSelectionIndex()

,

setAnchorSelectionIndex(int)

---

### Additional Sections

#### Class DefaultListSelectionModel

java.lang.Object

- javax.swing.DefaultListSelectionModel

javax.swing.DefaultListSelectionModel

**All Implemented Interfaces:** Serializable

,

Cloneable

,

ListSelectionModel

```java
public class
DefaultListSelectionModel

extends
Object

implements
ListSelectionModel
,
Cloneable
,
Serializable
```

Default data model for list selections.

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
**See Also:** ListSelectionModel

,

Serialized Form

public class

DefaultListSelectionModel

extends

Object

implements

ListSelectionModel

,

Cloneable

,

Serializable

Default data model for list selections.

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

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected boolean

leadAnchorNotificationEnabled

Whether or not the lead anchor notification is enabled.

protected

EventListenerList

listenerList

The list of listeners.

- Fields declared in interface javax.swing.

ListSelectionModel

MULTIPLE_INTERVAL_SELECTION

,

SINGLE_INTERVAL_SELECTION

,

SINGLE_SELECTION

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultListSelectionModel

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addSelectionInterval

​(int index0,
int index1)

Changes the selection to be the set union of the current selection
and the indices between

index0

and

index1

inclusive.

Object

clone

()

Returns a clone of this selection model with the same selection.

protected void

fireValueChanged

​(boolean isAdjusting)

Notifies listeners that we have ended a series of adjustments.

protected void

fireValueChanged

​(int firstIndex,
int lastIndex)

Notifies

ListSelectionListeners

that the value
of the selection, in the closed interval

firstIndex

,

lastIndex

, has changed.

protected void

fireValueChanged

​(int firstIndex,
int lastIndex,
boolean isAdjusting)

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

ListSelectionListener

[]

getListSelectionListeners

()

Returns an array of all the list selection listeners
registered on this

DefaultListSelectionModel

.

void

insertIndexInterval

​(int index,
int length,
boolean before)

Insert length indices beginning before/after index.

boolean

isLeadAnchorNotificationEnabled

()

Returns the value of the

leadAnchorNotificationEnabled

flag.

void

moveLeadSelectionIndex

​(int leadIndex)

Set the lead selection index, leaving all selection values unchanged.

void

removeIndexInterval

​(int index0,
int index1)

Remove the indices in the interval index0,index1 (inclusive) from
the selection model.

void

removeSelectionInterval

​(int index0,
int index1)

Changes the selection to be the set difference of the current selection
and the indices between

index0

and

index1

inclusive.

void

setAnchorSelectionIndex

​(int anchorIndex)

Set the anchor selection index, leaving all selection values unchanged.

void

setLeadAnchorNotificationEnabled

​(boolean flag)

Sets the value of the leadAnchorNotificationEnabled flag.

void

setLeadSelectionIndex

​(int leadIndex)

Sets the lead selection index, ensuring that values between the
anchor and the new lead are either all selected or all deselected.

void

setSelectionInterval

​(int index0,
int index1)

Changes the selection to be between

index0

and

index1

inclusive.

void

setSelectionMode

​(int selectionMode)

Sets the selection mode.

String

toString

()

Returns a string that displays and identifies this
object's properties.

- Methods declared in class java.lang.

Object

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

- Methods declared in interface javax.swing.

ListSelectionModel

addListSelectionListener

,

clearSelection

,

getAnchorSelectionIndex

,

getLeadSelectionIndex

,

getMaxSelectionIndex

,

getMinSelectionIndex

,

getSelectedIndices

,

getSelectedItemsCount

,

getSelectionMode

,

getValueIsAdjusting

,

isSelectedIndex

,

isSelectionEmpty

,

removeListSelectionListener

,

setValueIsAdjusting

Field Summary

Fields

Modifier and Type

Field

Description

protected boolean

leadAnchorNotificationEnabled

Whether or not the lead anchor notification is enabled.

protected

EventListenerList

listenerList

The list of listeners.

- Fields declared in interface javax.swing.

ListSelectionModel

MULTIPLE_INTERVAL_SELECTION

,

SINGLE_INTERVAL_SELECTION

,

SINGLE_SELECTION

---

#### Field Summary

Whether or not the lead anchor notification is enabled.

The list of listeners.

Fields declared in interface javax.swing.

ListSelectionModel

MULTIPLE_INTERVAL_SELECTION

,

SINGLE_INTERVAL_SELECTION

,

SINGLE_SELECTION

---

#### Fields declared in interface javax.swing. ListSelectionModel

Constructor Summary

Constructors

Constructor

Description

DefaultListSelectionModel

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addSelectionInterval

​(int index0,
int index1)

Changes the selection to be the set union of the current selection
and the indices between

index0

and

index1

inclusive.

Object

clone

()

Returns a clone of this selection model with the same selection.

protected void

fireValueChanged

​(boolean isAdjusting)

Notifies listeners that we have ended a series of adjustments.

protected void

fireValueChanged

​(int firstIndex,
int lastIndex)

Notifies

ListSelectionListeners

that the value
of the selection, in the closed interval

firstIndex

,

lastIndex

, has changed.

protected void

fireValueChanged

​(int firstIndex,
int lastIndex,
boolean isAdjusting)

<T extends

EventListener

>

T[]

getListeners

​(

Class

<T> listenerType)

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

ListSelectionListener

[]

getListSelectionListeners

()

Returns an array of all the list selection listeners
registered on this

DefaultListSelectionModel

.

void

insertIndexInterval

​(int index,
int length,
boolean before)

Insert length indices beginning before/after index.

boolean

isLeadAnchorNotificationEnabled

()

Returns the value of the

leadAnchorNotificationEnabled

flag.

void

moveLeadSelectionIndex

​(int leadIndex)

Set the lead selection index, leaving all selection values unchanged.

void

removeIndexInterval

​(int index0,
int index1)

Remove the indices in the interval index0,index1 (inclusive) from
the selection model.

void

removeSelectionInterval

​(int index0,
int index1)

Changes the selection to be the set difference of the current selection
and the indices between

index0

and

index1

inclusive.

void

setAnchorSelectionIndex

​(int anchorIndex)

Set the anchor selection index, leaving all selection values unchanged.

void

setLeadAnchorNotificationEnabled

​(boolean flag)

Sets the value of the leadAnchorNotificationEnabled flag.

void

setLeadSelectionIndex

​(int leadIndex)

Sets the lead selection index, ensuring that values between the
anchor and the new lead are either all selected or all deselected.

void

setSelectionInterval

​(int index0,
int index1)

Changes the selection to be between

index0

and

index1

inclusive.

void

setSelectionMode

​(int selectionMode)

Sets the selection mode.

String

toString

()

Returns a string that displays and identifies this
object's properties.

- Methods declared in class java.lang.

Object

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

- Methods declared in interface javax.swing.

ListSelectionModel

addListSelectionListener

,

clearSelection

,

getAnchorSelectionIndex

,

getLeadSelectionIndex

,

getMaxSelectionIndex

,

getMinSelectionIndex

,

getSelectedIndices

,

getSelectedItemsCount

,

getSelectionMode

,

getValueIsAdjusting

,

isSelectedIndex

,

isSelectionEmpty

,

removeListSelectionListener

,

setValueIsAdjusting

---

#### Method Summary

Changes the selection to be the set union of the current selection
and the indices between

index0

and

index1

inclusive.

Returns a clone of this selection model with the same selection.

Notifies listeners that we have ended a series of adjustments.

Notifies

ListSelectionListeners

that the value
of the selection, in the closed interval

firstIndex

,

lastIndex

, has changed.

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Returns an array of all the list selection listeners
registered on this

DefaultListSelectionModel

.

Insert length indices beginning before/after index.

Returns the value of the

leadAnchorNotificationEnabled

flag.

Set the lead selection index, leaving all selection values unchanged.

Remove the indices in the interval index0,index1 (inclusive) from
the selection model.

Changes the selection to be the set difference of the current selection
and the indices between

index0

and

index1

inclusive.

Set the anchor selection index, leaving all selection values unchanged.

Sets the value of the leadAnchorNotificationEnabled flag.

Sets the lead selection index, ensuring that values between the
anchor and the new lead are either all selected or all deselected.

Changes the selection to be between

index0

and

index1

inclusive.

Sets the selection mode.

Returns a string that displays and identifies this
object's properties.

Methods declared in class java.lang.

Object

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

Methods declared in interface javax.swing.

ListSelectionModel

addListSelectionListener

,

clearSelection

,

getAnchorSelectionIndex

,

getLeadSelectionIndex

,

getMaxSelectionIndex

,

getMinSelectionIndex

,

getSelectedIndices

,

getSelectedItemsCount

,

getSelectionMode

,

getValueIsAdjusting

,

isSelectedIndex

,

isSelectionEmpty

,

removeListSelectionListener

,

setValueIsAdjusting

---

#### Methods declared in interface javax.swing. ListSelectionModel

============ FIELD DETAIL ===========

- Field Detail

- listenerList

```java
protected
EventListenerList
listenerList
```

The list of listeners.

- leadAnchorNotificationEnabled

```java
protected boolean leadAnchorNotificationEnabled
```

Whether or not the lead anchor notification is enabled.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultListSelectionModel

```java
public DefaultListSelectionModel()
```

============ METHOD DETAIL ==========

- Method Detail

- setSelectionMode

```java
public void setSelectionMode​(int selectionMode)
```

Sets the selection mode. The following list describes the accepted
selection modes:

- ListSelectionModel.SINGLE_SELECTION

-
Only one list index can be selected at a time. In this mode,

setSelectionInterval

and

addSelectionInterval

are
equivalent, both replacing the current selection with the index
represented by the second argument (the "lead").

ListSelectionModel.SINGLE_INTERVAL_SELECTION

-
Only one contiguous interval can be selected at a time.
In this mode,

addSelectionInterval

behaves like

setSelectionInterval

(replacing the current selection),
unless the given interval is immediately adjacent to or overlaps
the existing selection, and can therefore be used to grow it.

ListSelectionModel.MULTIPLE_INTERVAL_SELECTION

-
In this mode, there's no restriction on what can be selected.

**Specified by:** setSelectionMode

in interface

ListSelectionModel
**Parameters:** selectionMode

- the selection mode
**Throws:** IllegalArgumentException

- if the selection mode isn't
one of those allowed
**See Also:** ListSelectionModel.getSelectionMode()

- getListSelectionListeners

```java
public
ListSelectionListener
[] getListSelectionListeners()
```

Returns an array of all the list selection listeners
registered on this

DefaultListSelectionModel

.

**Returns:** all of this model's

ListSelectionListener

s
or an empty
array if no list selection listeners are currently registered
**Since:** 1.4
**See Also:** ListSelectionModel.addListSelectionListener(javax.swing.event.ListSelectionListener)

,

ListSelectionModel.removeListSelectionListener(javax.swing.event.ListSelectionListener)

- fireValueChanged

```java
protected void fireValueChanged​(boolean isAdjusting)
```

Notifies listeners that we have ended a series of adjustments.

**Parameters:** isAdjusting

- true if this is the final change in a series of
adjustments

- fireValueChanged

```java
protected void fireValueChanged​(int firstIndex,
int lastIndex)
```

Notifies

ListSelectionListeners

that the value
of the selection, in the closed interval

firstIndex

,

lastIndex

, has changed.

**Parameters:** firstIndex

- the first index in the interval
**Parameters:** lastIndex

- the last index in the interval

- fireValueChanged

```java
protected void fireValueChanged​(int firstIndex,
int lastIndex,
boolean isAdjusting)
```

**Parameters:** firstIndex

- the first index in the interval
**Parameters:** lastIndex

- the last index in the interval
**Parameters:** isAdjusting

- true if this is the final change in a series of
adjustments
**See Also:** EventListenerList

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Foo

Listener

s
are registered using the

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

DefaultListSelectionModel

instance

m

for its list selection listeners
with the following code:

```java
ListSelectionListener[] lsls = (ListSelectionListener[])(m.getListeners(ListSelectionListener.class));
```

If no such listeners exist,
this method returns an empty array.

**Type Parameters:** T

- the type of

EventListener

class being requested
**Parameters:** listenerType

- the type of listeners requested;
this parameter should specify an interface
that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s
on this model,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't
specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getListSelectionListeners()

- setLeadAnchorNotificationEnabled

```java
public void setLeadAnchorNotificationEnabled​(boolean flag)
```

Sets the value of the leadAnchorNotificationEnabled flag.

**Parameters:** flag

- boolean value for

leadAnchorNotificationEnabled
**See Also:** isLeadAnchorNotificationEnabled()

- isLeadAnchorNotificationEnabled

```java
public boolean isLeadAnchorNotificationEnabled()
```

Returns the value of the

leadAnchorNotificationEnabled

flag.
When

leadAnchorNotificationEnabled

is true the model
generates notification events with bounds that cover all the changes to
the selection plus the changes to the lead and anchor indices.
Setting the flag to false causes a narrowing of the event's bounds to
include only the elements that have been selected or deselected since
the last change. Either way, the model continues to maintain the lead
and anchor variables internally. The default is true.

Note: It is possible for the lead or anchor to be changed without a
change to the selection. Notification of these changes is often
important, such as when the new lead or anchor needs to be updated in
the view. Therefore, caution is urged when changing the default value.

**Returns:** the value of the

leadAnchorNotificationEnabled

flag
**See Also:** setLeadAnchorNotificationEnabled(boolean)

- setSelectionInterval

```java
public void setSelectionInterval​(int index0,
int index1)
```

Changes the selection to be between

index0

and

index1

inclusive.

index0

doesn't have to be less than or equal to

index1

.

In

SINGLE_SELECTION

selection mode, only the second index
is used.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

**Specified by:** setSelectionInterval

in interface

ListSelectionModel
**Parameters:** index0

- one end of the interval.
**Parameters:** index1

- other end of the interval
**Throws:** IndexOutOfBoundsException

- if either index is less than

-1

(and neither index is

-1

)
**See Also:** ListSelectionModel.addListSelectionListener(javax.swing.event.ListSelectionListener)

- addSelectionInterval

```java
public void addSelectionInterval​(int index0,
int index1)
```

Changes the selection to be the set union of the current selection
and the indices between

index0

and

index1

inclusive.

In

SINGLE_SELECTION

selection mode, this is equivalent
to calling

setSelectionInterval

, and only the second index
is used. In

SINGLE_INTERVAL_SELECTION

selection mode, this
method behaves like

setSelectionInterval

, unless the given
interval is immediately adjacent to or overlaps the existing selection,
and can therefore be used to grow it.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change. Note that

index0

doesn't have to be less than or equal to

index1

.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

**Specified by:** addSelectionInterval

in interface

ListSelectionModel
**Parameters:** index0

- one end of the interval.
**Parameters:** index1

- other end of the interval
**Throws:** IndexOutOfBoundsException

- if either index is less than

-1

(and neither index is

-1

)
**See Also:** ListSelectionModel.addListSelectionListener(javax.swing.event.ListSelectionListener)

,

setSelectionInterval(int, int)

- removeSelectionInterval

```java
public void removeSelectionInterval​(int index0,
int index1)
```

Changes the selection to be the set difference of the current selection
and the indices between

index0

and

index1

inclusive.

index0

doesn't have to be less than or equal to

index1

.

In

SINGLE_INTERVAL_SELECTION

selection mode, if the removal
would produce two disjoint selections, the removal is extended through
the greater end of the selection. For example, if the selection is

0-10

and you supply indices

5,6

(in any order) the
resulting selection is

0-4

.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

**Specified by:** removeSelectionInterval

in interface

ListSelectionModel
**Parameters:** index0

- one end of the interval
**Parameters:** index1

- other end of the interval
**Throws:** IndexOutOfBoundsException

- if either index is less than

-1

(and neither index is

-1

)
**See Also:** ListSelectionModel.addListSelectionListener(javax.swing.event.ListSelectionListener)

- insertIndexInterval

```java
public void insertIndexInterval​(int index,
int length,
boolean before)
```

Insert length indices beginning before/after index. If the value
at index is itself selected and the selection mode is not
SINGLE_SELECTION, set all of the newly inserted items as selected.
Otherwise leave them unselected. This method is typically
called to sync the selection model with a corresponding change
in the data model.

**Specified by:** insertIndexInterval

in interface

ListSelectionModel
**Parameters:** index

- the beginning of the interval
**Parameters:** length

- the length of the interval
**Parameters:** before

- if

true

, interval inserts before the

index

,
otherwise, interval inserts after the

index

- removeIndexInterval

```java
public void removeIndexInterval​(int index0,
int index1)
```

Remove the indices in the interval index0,index1 (inclusive) from
the selection model. This is typically called to sync the selection
model width a corresponding change in the data model. Note
that (as always) index0 need not be <= index1.

**Specified by:** removeIndexInterval

in interface

ListSelectionModel
**Parameters:** index0

- the beginning of the interval
**Parameters:** index1

- the end of the interval

- toString

```java
public
String
toString()
```

Returns a string that displays and identifies this
object's properties.

**Overrides:** toString

in class

Object
**Returns:** a

String

representation of this object

- clone

```java
public
Object
clone()
throws
CloneNotSupportedException
```

Returns a clone of this selection model with the same selection.

listenerLists

are not duplicated.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** CloneNotSupportedException

- if the selection model does not
both (a) implement the Cloneable interface and (b) define a

clone

method.
**See Also:** Cloneable

- setAnchorSelectionIndex

```java
public void setAnchorSelectionIndex​(int anchorIndex)
```

Set the anchor selection index, leaving all selection values unchanged.
If leadAnchorNotificationEnabled is true, send a notification covering
the old and new anchor cells.

**Specified by:** setAnchorSelectionIndex

in interface

ListSelectionModel
**Parameters:** anchorIndex

- the anchor selection index
**See Also:** ListSelectionModel.getAnchorSelectionIndex()

,

setLeadSelectionIndex(int)

- moveLeadSelectionIndex

```java
public void moveLeadSelectionIndex​(int leadIndex)
```

Set the lead selection index, leaving all selection values unchanged.
If leadAnchorNotificationEnabled is true, send a notification covering
the old and new lead cells.

**Parameters:** leadIndex

- the new lead selection index
**Since:** 1.5
**See Also:** setAnchorSelectionIndex(int)

,

setLeadSelectionIndex(int)

,

ListSelectionModel.getLeadSelectionIndex()

- setLeadSelectionIndex

```java
public void setLeadSelectionIndex​(int leadIndex)
```

Sets the lead selection index, ensuring that values between the
anchor and the new lead are either all selected or all deselected.
If the value at the anchor index is selected, first clear all the
values in the range [anchor, oldLeadIndex], then select all the values
values in the range [anchor, newLeadIndex], where oldLeadIndex is the old
leadIndex and newLeadIndex is the new one.

If the value at the anchor index is not selected, do the same thing in
reverse selecting values in the old range and deselecting values in the
new one.

Generate a single event for this change and notify all listeners.
For the purposes of generating minimal bounds in this event, do the
operation in a single pass; that way the first and last index inside the
ListSelectionEvent that is broadcast will refer to cells that actually
changed value because of this method. If, instead, this operation were
done in two steps the effect on the selection state would be the same
but two events would be generated and the bounds around the changed
values would be wider, including cells that had been first cleared only
to later be set.

This method can be used in the

mouseDragged

method
of a UI class to extend a selection.

**Specified by:** setLeadSelectionIndex

in interface

ListSelectionModel
**Parameters:** leadIndex

- the lead selection index
**See Also:** ListSelectionModel.getLeadSelectionIndex()

,

setAnchorSelectionIndex(int)

Field Detail

- listenerList

```java
protected
EventListenerList
listenerList
```

The list of listeners.

- leadAnchorNotificationEnabled

```java
protected boolean leadAnchorNotificationEnabled
```

Whether or not the lead anchor notification is enabled.

---

#### Field Detail

listenerList

```java
protected
EventListenerList
listenerList
```

The list of listeners.

---

#### listenerList

protected

EventListenerList

listenerList

The list of listeners.

leadAnchorNotificationEnabled

```java
protected boolean leadAnchorNotificationEnabled
```

Whether or not the lead anchor notification is enabled.

---

#### leadAnchorNotificationEnabled

protected boolean leadAnchorNotificationEnabled

Whether or not the lead anchor notification is enabled.

Constructor Detail

- DefaultListSelectionModel

```java
public DefaultListSelectionModel()
```

---

#### Constructor Detail

DefaultListSelectionModel

```java
public DefaultListSelectionModel()
```

---

#### DefaultListSelectionModel

public DefaultListSelectionModel()

Method Detail

- setSelectionMode

```java
public void setSelectionMode​(int selectionMode)
```

Sets the selection mode. The following list describes the accepted
selection modes:

- ListSelectionModel.SINGLE_SELECTION

-
Only one list index can be selected at a time. In this mode,

setSelectionInterval

and

addSelectionInterval

are
equivalent, both replacing the current selection with the index
represented by the second argument (the "lead").

ListSelectionModel.SINGLE_INTERVAL_SELECTION

-
Only one contiguous interval can be selected at a time.
In this mode,

addSelectionInterval

behaves like

setSelectionInterval

(replacing the current selection),
unless the given interval is immediately adjacent to or overlaps
the existing selection, and can therefore be used to grow it.

ListSelectionModel.MULTIPLE_INTERVAL_SELECTION

-
In this mode, there's no restriction on what can be selected.

**Specified by:** setSelectionMode

in interface

ListSelectionModel
**Parameters:** selectionMode

- the selection mode
**Throws:** IllegalArgumentException

- if the selection mode isn't
one of those allowed
**See Also:** ListSelectionModel.getSelectionMode()

- getListSelectionListeners

```java
public
ListSelectionListener
[] getListSelectionListeners()
```

Returns an array of all the list selection listeners
registered on this

DefaultListSelectionModel

.

**Returns:** all of this model's

ListSelectionListener

s
or an empty
array if no list selection listeners are currently registered
**Since:** 1.4
**See Also:** ListSelectionModel.addListSelectionListener(javax.swing.event.ListSelectionListener)

,

ListSelectionModel.removeListSelectionListener(javax.swing.event.ListSelectionListener)

- fireValueChanged

```java
protected void fireValueChanged​(boolean isAdjusting)
```

Notifies listeners that we have ended a series of adjustments.

**Parameters:** isAdjusting

- true if this is the final change in a series of
adjustments

- fireValueChanged

```java
protected void fireValueChanged​(int firstIndex,
int lastIndex)
```

Notifies

ListSelectionListeners

that the value
of the selection, in the closed interval

firstIndex

,

lastIndex

, has changed.

**Parameters:** firstIndex

- the first index in the interval
**Parameters:** lastIndex

- the last index in the interval

- fireValueChanged

```java
protected void fireValueChanged​(int firstIndex,
int lastIndex,
boolean isAdjusting)
```

**Parameters:** firstIndex

- the first index in the interval
**Parameters:** lastIndex

- the last index in the interval
**Parameters:** isAdjusting

- true if this is the final change in a series of
adjustments
**See Also:** EventListenerList

- getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Foo

Listener

s
are registered using the

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

DefaultListSelectionModel

instance

m

for its list selection listeners
with the following code:

```java
ListSelectionListener[] lsls = (ListSelectionListener[])(m.getListeners(ListSelectionListener.class));
```

If no such listeners exist,
this method returns an empty array.

**Type Parameters:** T

- the type of

EventListener

class being requested
**Parameters:** listenerType

- the type of listeners requested;
this parameter should specify an interface
that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s
on this model,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't
specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getListSelectionListeners()

- setLeadAnchorNotificationEnabled

```java
public void setLeadAnchorNotificationEnabled​(boolean flag)
```

Sets the value of the leadAnchorNotificationEnabled flag.

**Parameters:** flag

- boolean value for

leadAnchorNotificationEnabled
**See Also:** isLeadAnchorNotificationEnabled()

- isLeadAnchorNotificationEnabled

```java
public boolean isLeadAnchorNotificationEnabled()
```

Returns the value of the

leadAnchorNotificationEnabled

flag.
When

leadAnchorNotificationEnabled

is true the model
generates notification events with bounds that cover all the changes to
the selection plus the changes to the lead and anchor indices.
Setting the flag to false causes a narrowing of the event's bounds to
include only the elements that have been selected or deselected since
the last change. Either way, the model continues to maintain the lead
and anchor variables internally. The default is true.

Note: It is possible for the lead or anchor to be changed without a
change to the selection. Notification of these changes is often
important, such as when the new lead or anchor needs to be updated in
the view. Therefore, caution is urged when changing the default value.

**Returns:** the value of the

leadAnchorNotificationEnabled

flag
**See Also:** setLeadAnchorNotificationEnabled(boolean)

- setSelectionInterval

```java
public void setSelectionInterval​(int index0,
int index1)
```

Changes the selection to be between

index0

and

index1

inclusive.

index0

doesn't have to be less than or equal to

index1

.

In

SINGLE_SELECTION

selection mode, only the second index
is used.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

**Specified by:** setSelectionInterval

in interface

ListSelectionModel
**Parameters:** index0

- one end of the interval.
**Parameters:** index1

- other end of the interval
**Throws:** IndexOutOfBoundsException

- if either index is less than

-1

(and neither index is

-1

)
**See Also:** ListSelectionModel.addListSelectionListener(javax.swing.event.ListSelectionListener)

- addSelectionInterval

```java
public void addSelectionInterval​(int index0,
int index1)
```

Changes the selection to be the set union of the current selection
and the indices between

index0

and

index1

inclusive.

In

SINGLE_SELECTION

selection mode, this is equivalent
to calling

setSelectionInterval

, and only the second index
is used. In

SINGLE_INTERVAL_SELECTION

selection mode, this
method behaves like

setSelectionInterval

, unless the given
interval is immediately adjacent to or overlaps the existing selection,
and can therefore be used to grow it.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change. Note that

index0

doesn't have to be less than or equal to

index1

.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

**Specified by:** addSelectionInterval

in interface

ListSelectionModel
**Parameters:** index0

- one end of the interval.
**Parameters:** index1

- other end of the interval
**Throws:** IndexOutOfBoundsException

- if either index is less than

-1

(and neither index is

-1

)
**See Also:** ListSelectionModel.addListSelectionListener(javax.swing.event.ListSelectionListener)

,

setSelectionInterval(int, int)

- removeSelectionInterval

```java
public void removeSelectionInterval​(int index0,
int index1)
```

Changes the selection to be the set difference of the current selection
and the indices between

index0

and

index1

inclusive.

index0

doesn't have to be less than or equal to

index1

.

In

SINGLE_INTERVAL_SELECTION

selection mode, if the removal
would produce two disjoint selections, the removal is extended through
the greater end of the selection. For example, if the selection is

0-10

and you supply indices

5,6

(in any order) the
resulting selection is

0-4

.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

**Specified by:** removeSelectionInterval

in interface

ListSelectionModel
**Parameters:** index0

- one end of the interval
**Parameters:** index1

- other end of the interval
**Throws:** IndexOutOfBoundsException

- if either index is less than

-1

(and neither index is

-1

)
**See Also:** ListSelectionModel.addListSelectionListener(javax.swing.event.ListSelectionListener)

- insertIndexInterval

```java
public void insertIndexInterval​(int index,
int length,
boolean before)
```

Insert length indices beginning before/after index. If the value
at index is itself selected and the selection mode is not
SINGLE_SELECTION, set all of the newly inserted items as selected.
Otherwise leave them unselected. This method is typically
called to sync the selection model with a corresponding change
in the data model.

**Specified by:** insertIndexInterval

in interface

ListSelectionModel
**Parameters:** index

- the beginning of the interval
**Parameters:** length

- the length of the interval
**Parameters:** before

- if

true

, interval inserts before the

index

,
otherwise, interval inserts after the

index

- removeIndexInterval

```java
public void removeIndexInterval​(int index0,
int index1)
```

Remove the indices in the interval index0,index1 (inclusive) from
the selection model. This is typically called to sync the selection
model width a corresponding change in the data model. Note
that (as always) index0 need not be <= index1.

**Specified by:** removeIndexInterval

in interface

ListSelectionModel
**Parameters:** index0

- the beginning of the interval
**Parameters:** index1

- the end of the interval

- toString

```java
public
String
toString()
```

Returns a string that displays and identifies this
object's properties.

**Overrides:** toString

in class

Object
**Returns:** a

String

representation of this object

- clone

```java
public
Object
clone()
throws
CloneNotSupportedException
```

Returns a clone of this selection model with the same selection.

listenerLists

are not duplicated.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** CloneNotSupportedException

- if the selection model does not
both (a) implement the Cloneable interface and (b) define a

clone

method.
**See Also:** Cloneable

- setAnchorSelectionIndex

```java
public void setAnchorSelectionIndex​(int anchorIndex)
```

Set the anchor selection index, leaving all selection values unchanged.
If leadAnchorNotificationEnabled is true, send a notification covering
the old and new anchor cells.

**Specified by:** setAnchorSelectionIndex

in interface

ListSelectionModel
**Parameters:** anchorIndex

- the anchor selection index
**See Also:** ListSelectionModel.getAnchorSelectionIndex()

,

setLeadSelectionIndex(int)

- moveLeadSelectionIndex

```java
public void moveLeadSelectionIndex​(int leadIndex)
```

Set the lead selection index, leaving all selection values unchanged.
If leadAnchorNotificationEnabled is true, send a notification covering
the old and new lead cells.

**Parameters:** leadIndex

- the new lead selection index
**Since:** 1.5
**See Also:** setAnchorSelectionIndex(int)

,

setLeadSelectionIndex(int)

,

ListSelectionModel.getLeadSelectionIndex()

- setLeadSelectionIndex

```java
public void setLeadSelectionIndex​(int leadIndex)
```

Sets the lead selection index, ensuring that values between the
anchor and the new lead are either all selected or all deselected.
If the value at the anchor index is selected, first clear all the
values in the range [anchor, oldLeadIndex], then select all the values
values in the range [anchor, newLeadIndex], where oldLeadIndex is the old
leadIndex and newLeadIndex is the new one.

If the value at the anchor index is not selected, do the same thing in
reverse selecting values in the old range and deselecting values in the
new one.

Generate a single event for this change and notify all listeners.
For the purposes of generating minimal bounds in this event, do the
operation in a single pass; that way the first and last index inside the
ListSelectionEvent that is broadcast will refer to cells that actually
changed value because of this method. If, instead, this operation were
done in two steps the effect on the selection state would be the same
but two events would be generated and the bounds around the changed
values would be wider, including cells that had been first cleared only
to later be set.

This method can be used in the

mouseDragged

method
of a UI class to extend a selection.

**Specified by:** setLeadSelectionIndex

in interface

ListSelectionModel
**Parameters:** leadIndex

- the lead selection index
**See Also:** ListSelectionModel.getLeadSelectionIndex()

,

setAnchorSelectionIndex(int)

---

#### Method Detail

setSelectionMode

```java
public void setSelectionMode​(int selectionMode)
```

Sets the selection mode. The following list describes the accepted
selection modes:

- ListSelectionModel.SINGLE_SELECTION

-
Only one list index can be selected at a time. In this mode,

setSelectionInterval

and

addSelectionInterval

are
equivalent, both replacing the current selection with the index
represented by the second argument (the "lead").

ListSelectionModel.SINGLE_INTERVAL_SELECTION

-
Only one contiguous interval can be selected at a time.
In this mode,

addSelectionInterval

behaves like

setSelectionInterval

(replacing the current selection),
unless the given interval is immediately adjacent to or overlaps
the existing selection, and can therefore be used to grow it.

ListSelectionModel.MULTIPLE_INTERVAL_SELECTION

-
In this mode, there's no restriction on what can be selected.

**Specified by:** setSelectionMode

in interface

ListSelectionModel
**Parameters:** selectionMode

- the selection mode
**Throws:** IllegalArgumentException

- if the selection mode isn't
one of those allowed
**See Also:** ListSelectionModel.getSelectionMode()

---

#### setSelectionMode

public void setSelectionMode​(int selectionMode)

Sets the selection mode. The following list describes the accepted
selection modes:

- ListSelectionModel.SINGLE_SELECTION

-
Only one list index can be selected at a time. In this mode,

setSelectionInterval

and

addSelectionInterval

are
equivalent, both replacing the current selection with the index
represented by the second argument (the "lead").

ListSelectionModel.SINGLE_INTERVAL_SELECTION

-
Only one contiguous interval can be selected at a time.
In this mode,

addSelectionInterval

behaves like

setSelectionInterval

(replacing the current selection),
unless the given interval is immediately adjacent to or overlaps
the existing selection, and can therefore be used to grow it.

ListSelectionModel.MULTIPLE_INTERVAL_SELECTION

-
In this mode, there's no restriction on what can be selected.

ListSelectionModel.SINGLE_SELECTION

-
Only one list index can be selected at a time. In this mode,

setSelectionInterval

and

addSelectionInterval

are
equivalent, both replacing the current selection with the index
represented by the second argument (the "lead").

ListSelectionModel.SINGLE_INTERVAL_SELECTION

-
Only one contiguous interval can be selected at a time.
In this mode,

addSelectionInterval

behaves like

setSelectionInterval

(replacing the current selection),
unless the given interval is immediately adjacent to or overlaps
the existing selection, and can therefore be used to grow it.

ListSelectionModel.MULTIPLE_INTERVAL_SELECTION

-
In this mode, there's no restriction on what can be selected.

getListSelectionListeners

```java
public
ListSelectionListener
[] getListSelectionListeners()
```

Returns an array of all the list selection listeners
registered on this

DefaultListSelectionModel

.

**Returns:** all of this model's

ListSelectionListener

s
or an empty
array if no list selection listeners are currently registered
**Since:** 1.4
**See Also:** ListSelectionModel.addListSelectionListener(javax.swing.event.ListSelectionListener)

,

ListSelectionModel.removeListSelectionListener(javax.swing.event.ListSelectionListener)

---

#### getListSelectionListeners

public

ListSelectionListener

[] getListSelectionListeners()

Returns an array of all the list selection listeners
registered on this

DefaultListSelectionModel

.

fireValueChanged

```java
protected void fireValueChanged​(boolean isAdjusting)
```

Notifies listeners that we have ended a series of adjustments.

**Parameters:** isAdjusting

- true if this is the final change in a series of
adjustments

---

#### fireValueChanged

protected void fireValueChanged​(boolean isAdjusting)

Notifies listeners that we have ended a series of adjustments.

fireValueChanged

```java
protected void fireValueChanged​(int firstIndex,
int lastIndex)
```

Notifies

ListSelectionListeners

that the value
of the selection, in the closed interval

firstIndex

,

lastIndex

, has changed.

**Parameters:** firstIndex

- the first index in the interval
**Parameters:** lastIndex

- the last index in the interval

---

#### fireValueChanged

protected void fireValueChanged​(int firstIndex,
int lastIndex)

Notifies

ListSelectionListeners

that the value
of the selection, in the closed interval

firstIndex

,

lastIndex

, has changed.

fireValueChanged

```java
protected void fireValueChanged​(int firstIndex,
int lastIndex,
boolean isAdjusting)
```

**Parameters:** firstIndex

- the first index in the interval
**Parameters:** lastIndex

- the last index in the interval
**Parameters:** isAdjusting

- true if this is the final change in a series of
adjustments
**See Also:** EventListenerList

---

#### fireValueChanged

protected void fireValueChanged​(int firstIndex,
int lastIndex,
boolean isAdjusting)

getListeners

```java
public <T extends
EventListener
> T[] getListeners​(
Class
<T> listenerType)
```

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Foo

Listener

s
are registered using the

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

DefaultListSelectionModel

instance

m

for its list selection listeners
with the following code:

```java
ListSelectionListener[] lsls = (ListSelectionListener[])(m.getListeners(ListSelectionListener.class));
```

If no such listeners exist,
this method returns an empty array.

**Type Parameters:** T

- the type of

EventListener

class being requested
**Parameters:** listenerType

- the type of listeners requested;
this parameter should specify an interface
that descends from

java.util.EventListener
**Returns:** an array of all objects registered as

Foo

Listener

s
on this model,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't
specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getListSelectionListeners()

---

#### getListeners

public <T extends

EventListener

> T[] getListeners​(

Class

<T> listenerType)

Returns an array of all the objects currently registered as

Foo

Listener

s
upon this model.

Foo

Listener

s
are registered using the

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

DefaultListSelectionModel

instance

m

for its list selection listeners
with the following code:

```java
ListSelectionListener[] lsls = (ListSelectionListener[])(m.getListeners(ListSelectionListener.class));
```

If no such listeners exist,
this method returns an empty array.

You can specify the

listenerType

argument
with a class literal, such as

Foo

Listener.class

.
For example, you can query a

DefaultListSelectionModel

instance

m

for its list selection listeners
with the following code:

```java
ListSelectionListener[] lsls = (ListSelectionListener[])(m.getListeners(ListSelectionListener.class));
```

If no such listeners exist,
this method returns an empty array.

ListSelectionListener[] lsls = (ListSelectionListener[])(m.getListeners(ListSelectionListener.class));

setLeadAnchorNotificationEnabled

```java
public void setLeadAnchorNotificationEnabled​(boolean flag)
```

Sets the value of the leadAnchorNotificationEnabled flag.

**Parameters:** flag

- boolean value for

leadAnchorNotificationEnabled
**See Also:** isLeadAnchorNotificationEnabled()

---

#### setLeadAnchorNotificationEnabled

public void setLeadAnchorNotificationEnabled​(boolean flag)

Sets the value of the leadAnchorNotificationEnabled flag.

isLeadAnchorNotificationEnabled

```java
public boolean isLeadAnchorNotificationEnabled()
```

Returns the value of the

leadAnchorNotificationEnabled

flag.
When

leadAnchorNotificationEnabled

is true the model
generates notification events with bounds that cover all the changes to
the selection plus the changes to the lead and anchor indices.
Setting the flag to false causes a narrowing of the event's bounds to
include only the elements that have been selected or deselected since
the last change. Either way, the model continues to maintain the lead
and anchor variables internally. The default is true.

Note: It is possible for the lead or anchor to be changed without a
change to the selection. Notification of these changes is often
important, such as when the new lead or anchor needs to be updated in
the view. Therefore, caution is urged when changing the default value.

**Returns:** the value of the

leadAnchorNotificationEnabled

flag
**See Also:** setLeadAnchorNotificationEnabled(boolean)

---

#### isLeadAnchorNotificationEnabled

public boolean isLeadAnchorNotificationEnabled()

Returns the value of the

leadAnchorNotificationEnabled

flag.
When

leadAnchorNotificationEnabled

is true the model
generates notification events with bounds that cover all the changes to
the selection plus the changes to the lead and anchor indices.
Setting the flag to false causes a narrowing of the event's bounds to
include only the elements that have been selected or deselected since
the last change. Either way, the model continues to maintain the lead
and anchor variables internally. The default is true.

Note: It is possible for the lead or anchor to be changed without a
change to the selection. Notification of these changes is often
important, such as when the new lead or anchor needs to be updated in
the view. Therefore, caution is urged when changing the default value.

Note: It is possible for the lead or anchor to be changed without a
change to the selection. Notification of these changes is often
important, such as when the new lead or anchor needs to be updated in
the view. Therefore, caution is urged when changing the default value.

setSelectionInterval

```java
public void setSelectionInterval​(int index0,
int index1)
```

Changes the selection to be between

index0

and

index1

inclusive.

index0

doesn't have to be less than or equal to

index1

.

In

SINGLE_SELECTION

selection mode, only the second index
is used.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

**Specified by:** setSelectionInterval

in interface

ListSelectionModel
**Parameters:** index0

- one end of the interval.
**Parameters:** index1

- other end of the interval
**Throws:** IndexOutOfBoundsException

- if either index is less than

-1

(and neither index is

-1

)
**See Also:** ListSelectionModel.addListSelectionListener(javax.swing.event.ListSelectionListener)

---

#### setSelectionInterval

public void setSelectionInterval​(int index0,
int index1)

Changes the selection to be between

index0

and

index1

inclusive.

index0

doesn't have to be less than or equal to

index1

.

In

SINGLE_SELECTION

selection mode, only the second index
is used.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

In

SINGLE_SELECTION

selection mode, only the second index
is used.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

addSelectionInterval

```java
public void addSelectionInterval​(int index0,
int index1)
```

Changes the selection to be the set union of the current selection
and the indices between

index0

and

index1

inclusive.

In

SINGLE_SELECTION

selection mode, this is equivalent
to calling

setSelectionInterval

, and only the second index
is used. In

SINGLE_INTERVAL_SELECTION

selection mode, this
method behaves like

setSelectionInterval

, unless the given
interval is immediately adjacent to or overlaps the existing selection,
and can therefore be used to grow it.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change. Note that

index0

doesn't have to be less than or equal to

index1

.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

**Specified by:** addSelectionInterval

in interface

ListSelectionModel
**Parameters:** index0

- one end of the interval.
**Parameters:** index1

- other end of the interval
**Throws:** IndexOutOfBoundsException

- if either index is less than

-1

(and neither index is

-1

)
**See Also:** ListSelectionModel.addListSelectionListener(javax.swing.event.ListSelectionListener)

,

setSelectionInterval(int, int)

---

#### addSelectionInterval

public void addSelectionInterval​(int index0,
int index1)

Changes the selection to be the set union of the current selection
and the indices between

index0

and

index1

inclusive.

In

SINGLE_SELECTION

selection mode, this is equivalent
to calling

setSelectionInterval

, and only the second index
is used. In

SINGLE_INTERVAL_SELECTION

selection mode, this
method behaves like

setSelectionInterval

, unless the given
interval is immediately adjacent to or overlaps the existing selection,
and can therefore be used to grow it.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change. Note that

index0

doesn't have to be less than or equal to

index1

.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

In

SINGLE_SELECTION

selection mode, this is equivalent
to calling

setSelectionInterval

, and only the second index
is used. In

SINGLE_INTERVAL_SELECTION

selection mode, this
method behaves like

setSelectionInterval

, unless the given
interval is immediately adjacent to or overlaps the existing selection,
and can therefore be used to grow it.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change. Note that

index0

doesn't have to be less than or equal to

index1

.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change. Note that

index0

doesn't have to be less than or equal to

index1

.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

removeSelectionInterval

```java
public void removeSelectionInterval​(int index0,
int index1)
```

Changes the selection to be the set difference of the current selection
and the indices between

index0

and

index1

inclusive.

index0

doesn't have to be less than or equal to

index1

.

In

SINGLE_INTERVAL_SELECTION

selection mode, if the removal
would produce two disjoint selections, the removal is extended through
the greater end of the selection. For example, if the selection is

0-10

and you supply indices

5,6

(in any order) the
resulting selection is

0-4

.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

**Specified by:** removeSelectionInterval

in interface

ListSelectionModel
**Parameters:** index0

- one end of the interval
**Parameters:** index1

- other end of the interval
**Throws:** IndexOutOfBoundsException

- if either index is less than

-1

(and neither index is

-1

)
**See Also:** ListSelectionModel.addListSelectionListener(javax.swing.event.ListSelectionListener)

---

#### removeSelectionInterval

public void removeSelectionInterval​(int index0,
int index1)

Changes the selection to be the set difference of the current selection
and the indices between

index0

and

index1

inclusive.

index0

doesn't have to be less than or equal to

index1

.

In

SINGLE_INTERVAL_SELECTION

selection mode, if the removal
would produce two disjoint selections, the removal is extended through
the greater end of the selection. For example, if the selection is

0-10

and you supply indices

5,6

(in any order) the
resulting selection is

0-4

.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

In

SINGLE_INTERVAL_SELECTION

selection mode, if the removal
would produce two disjoint selections, the removal is extended through
the greater end of the selection. For example, if the selection is

0-10

and you supply indices

5,6

(in any order) the
resulting selection is

0-4

.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

If either index is

-1

, this method does nothing and returns
without exception. Otherwise, if either index is less than

-1

,
an

IndexOutOfBoundsException

is thrown.

insertIndexInterval

```java
public void insertIndexInterval​(int index,
int length,
boolean before)
```

Insert length indices beginning before/after index. If the value
at index is itself selected and the selection mode is not
SINGLE_SELECTION, set all of the newly inserted items as selected.
Otherwise leave them unselected. This method is typically
called to sync the selection model with a corresponding change
in the data model.

**Specified by:** insertIndexInterval

in interface

ListSelectionModel
**Parameters:** index

- the beginning of the interval
**Parameters:** length

- the length of the interval
**Parameters:** before

- if

true

, interval inserts before the

index

,
otherwise, interval inserts after the

index

---

#### insertIndexInterval

public void insertIndexInterval​(int index,
int length,
boolean before)

Insert length indices beginning before/after index. If the value
at index is itself selected and the selection mode is not
SINGLE_SELECTION, set all of the newly inserted items as selected.
Otherwise leave them unselected. This method is typically
called to sync the selection model with a corresponding change
in the data model.

removeIndexInterval

```java
public void removeIndexInterval​(int index0,
int index1)
```

Remove the indices in the interval index0,index1 (inclusive) from
the selection model. This is typically called to sync the selection
model width a corresponding change in the data model. Note
that (as always) index0 need not be <= index1.

**Specified by:** removeIndexInterval

in interface

ListSelectionModel
**Parameters:** index0

- the beginning of the interval
**Parameters:** index1

- the end of the interval

---

#### removeIndexInterval

public void removeIndexInterval​(int index0,
int index1)

Remove the indices in the interval index0,index1 (inclusive) from
the selection model. This is typically called to sync the selection
model width a corresponding change in the data model. Note
that (as always) index0 need not be <= index1.

toString

```java
public
String
toString()
```

Returns a string that displays and identifies this
object's properties.

**Overrides:** toString

in class

Object
**Returns:** a

String

representation of this object

---

#### toString

public

String

toString()

Returns a string that displays and identifies this
object's properties.

clone

```java
public
Object
clone()
throws
CloneNotSupportedException
```

Returns a clone of this selection model with the same selection.

listenerLists

are not duplicated.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** CloneNotSupportedException

- if the selection model does not
both (a) implement the Cloneable interface and (b) define a

clone

method.
**See Also:** Cloneable

---

#### clone

public

Object

clone()
throws

CloneNotSupportedException

Returns a clone of this selection model with the same selection.

listenerLists

are not duplicated.

setAnchorSelectionIndex

```java
public void setAnchorSelectionIndex​(int anchorIndex)
```

Set the anchor selection index, leaving all selection values unchanged.
If leadAnchorNotificationEnabled is true, send a notification covering
the old and new anchor cells.

**Specified by:** setAnchorSelectionIndex

in interface

ListSelectionModel
**Parameters:** anchorIndex

- the anchor selection index
**See Also:** ListSelectionModel.getAnchorSelectionIndex()

,

setLeadSelectionIndex(int)

---

#### setAnchorSelectionIndex

public void setAnchorSelectionIndex​(int anchorIndex)

Set the anchor selection index, leaving all selection values unchanged.
If leadAnchorNotificationEnabled is true, send a notification covering
the old and new anchor cells.

moveLeadSelectionIndex

```java
public void moveLeadSelectionIndex​(int leadIndex)
```

Set the lead selection index, leaving all selection values unchanged.
If leadAnchorNotificationEnabled is true, send a notification covering
the old and new lead cells.

**Parameters:** leadIndex

- the new lead selection index
**Since:** 1.5
**See Also:** setAnchorSelectionIndex(int)

,

setLeadSelectionIndex(int)

,

ListSelectionModel.getLeadSelectionIndex()

---

#### moveLeadSelectionIndex

public void moveLeadSelectionIndex​(int leadIndex)

Set the lead selection index, leaving all selection values unchanged.
If leadAnchorNotificationEnabled is true, send a notification covering
the old and new lead cells.

setLeadSelectionIndex

```java
public void setLeadSelectionIndex​(int leadIndex)
```

Sets the lead selection index, ensuring that values between the
anchor and the new lead are either all selected or all deselected.
If the value at the anchor index is selected, first clear all the
values in the range [anchor, oldLeadIndex], then select all the values
values in the range [anchor, newLeadIndex], where oldLeadIndex is the old
leadIndex and newLeadIndex is the new one.

If the value at the anchor index is not selected, do the same thing in
reverse selecting values in the old range and deselecting values in the
new one.

Generate a single event for this change and notify all listeners.
For the purposes of generating minimal bounds in this event, do the
operation in a single pass; that way the first and last index inside the
ListSelectionEvent that is broadcast will refer to cells that actually
changed value because of this method. If, instead, this operation were
done in two steps the effect on the selection state would be the same
but two events would be generated and the bounds around the changed
values would be wider, including cells that had been first cleared only
to later be set.

This method can be used in the

mouseDragged

method
of a UI class to extend a selection.

**Specified by:** setLeadSelectionIndex

in interface

ListSelectionModel
**Parameters:** leadIndex

- the lead selection index
**See Also:** ListSelectionModel.getLeadSelectionIndex()

,

setAnchorSelectionIndex(int)

---

#### setLeadSelectionIndex

public void setLeadSelectionIndex​(int leadIndex)

Sets the lead selection index, ensuring that values between the
anchor and the new lead are either all selected or all deselected.
If the value at the anchor index is selected, first clear all the
values in the range [anchor, oldLeadIndex], then select all the values
values in the range [anchor, newLeadIndex], where oldLeadIndex is the old
leadIndex and newLeadIndex is the new one.

If the value at the anchor index is not selected, do the same thing in
reverse selecting values in the old range and deselecting values in the
new one.

Generate a single event for this change and notify all listeners.
For the purposes of generating minimal bounds in this event, do the
operation in a single pass; that way the first and last index inside the
ListSelectionEvent that is broadcast will refer to cells that actually
changed value because of this method. If, instead, this operation were
done in two steps the effect on the selection state would be the same
but two events would be generated and the bounds around the changed
values would be wider, including cells that had been first cleared only
to later be set.

This method can be used in the

mouseDragged

method
of a UI class to extend a selection.

If the value at the anchor index is not selected, do the same thing in
reverse selecting values in the old range and deselecting values in the
new one.

Generate a single event for this change and notify all listeners.
For the purposes of generating minimal bounds in this event, do the
operation in a single pass; that way the first and last index inside the
ListSelectionEvent that is broadcast will refer to cells that actually
changed value because of this method. If, instead, this operation were
done in two steps the effect on the selection state would be the same
but two events would be generated and the bounds around the changed
values would be wider, including cells that had been first cleared only
to later be set.

This method can be used in the

mouseDragged

method
of a UI class to extend a selection.

Generate a single event for this change and notify all listeners.
For the purposes of generating minimal bounds in this event, do the
operation in a single pass; that way the first and last index inside the
ListSelectionEvent that is broadcast will refer to cells that actually
changed value because of this method. If, instead, this operation were
done in two steps the effect on the selection state would be the same
but two events would be generated and the bounds around the changed
values would be wider, including cells that had been first cleared only
to later be set.

This method can be used in the

mouseDragged

method
of a UI class to extend a selection.

This method can be used in the

mouseDragged

method
of a UI class to extend a selection.

---

