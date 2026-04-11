# Interface ListSelectionModel

**Source:** `java.desktop\javax\swing\ListSelectionModel.html`

### Class Description

```java
public interface
ListSelectionModel
```

This interface represents the current state of the
selection for any of the components that display a
list of values with stable indices. The selection is
modeled as a set of intervals, each interval represents
a contiguous range of selected list elements.
The methods for modifying the set of selected intervals
all take a pair of indices, index0 and index1, that represent
a closed interval, i.e. the interval includes both index0 and
index1.

**All Known Implementing Classes:** DefaultListSelectionModel

---

### Field Details

#### static final int SINGLE_SELECTION

A value for the selectionMode property: select one list index
at a time.

**See Also:**
- setSelectionMode(int)

,

Constant Field Values

---

#### static final int SINGLE_INTERVAL_SELECTION

A value for the selectionMode property: select one contiguous
range of indices at a time.

**See Also:**
- setSelectionMode(int)

,

Constant Field Values

---

#### static final int MULTIPLE_INTERVAL_SELECTION

A value for the selectionMode property: select one or more
contiguous ranges of indices at a time.

**See Also:**
- setSelectionMode(int)

,

Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### void setSelectionInterval​(int index0,
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

**Parameters:**
- index0

- one end of the interval.
- index1

- other end of the interval

**See Also:**
- addListSelectionListener(javax.swing.event.ListSelectionListener)

---

#### void addSelectionInterval​(int index0,
int index1)

Changes the selection to be the set union of the current selection
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
and can therefore be used to grow the selection.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

**Parameters:**
- index0

- one end of the interval.
- index1

- other end of the interval

**See Also:**
- addListSelectionListener(javax.swing.event.ListSelectionListener)

,

setSelectionInterval(int, int)

---

#### void removeSelectionInterval​(int index0,
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

**Parameters:**
- index0

- one end of the interval.
- index1

- other end of the interval

**See Also:**
- addListSelectionListener(javax.swing.event.ListSelectionListener)

---

#### int getMinSelectionIndex()

Returns the first selected index or -1 if the selection is empty.

**Returns:**
- the first selected index or -1 if the selection is empty.

---

#### int getMaxSelectionIndex()

Returns the last selected index or -1 if the selection is empty.

**Returns:**
- the last selected index or -1 if the selection is empty.

---

#### boolean isSelectedIndex​(int index)

Returns true if the specified index is selected.

**Parameters:**
- index

- an index

**Returns:**
- true

if the specified index is selected

---

#### int getAnchorSelectionIndex()

Return the first index argument from the most recent call to
setSelectionInterval(), addSelectionInterval() or removeSelectionInterval().
The most recent index0 is considered the "anchor" and the most recent
index1 is considered the "lead". Some interfaces display these
indices specially, e.g. Windows95 displays the lead index with a
dotted yellow outline.

**Returns:**
- the anchor selection index

**See Also:**
- getLeadSelectionIndex()

,

setSelectionInterval(int, int)

,

addSelectionInterval(int, int)

---

#### void setAnchorSelectionIndex​(int index)

Set the anchor selection index.

**Parameters:**
- index

- the anchor selection index

**See Also:**
- getAnchorSelectionIndex()

---

#### int getLeadSelectionIndex()

Return the second index argument from the most recent call to
setSelectionInterval(), addSelectionInterval() or removeSelectionInterval().

**Returns:**
- the lead selection index.

**See Also:**
- getAnchorSelectionIndex()

,

setSelectionInterval(int, int)

,

addSelectionInterval(int, int)

---

#### void setLeadSelectionIndex​(int index)

Set the lead selection index.

**Parameters:**
- index

- the lead selection index

**See Also:**
- getLeadSelectionIndex()

---

#### void clearSelection()

Change the selection to the empty set. If this represents
a change to the current selection then notify each ListSelectionListener.

**See Also:**
- addListSelectionListener(javax.swing.event.ListSelectionListener)

---

#### boolean isSelectionEmpty()

Returns true if no indices are selected.

**Returns:**
- true

if no indices are selected.

---

#### void insertIndexInterval​(int index,
int length,
boolean before)

Insert

length

indices beginning before/after

index

. This is typically
called to sync the selection model with a corresponding change
in the data model.

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

#### void removeIndexInterval​(int index0,
int index1)

Remove the indices in the interval

index0,index1

(inclusive) from
the selection model. This is typically called to sync the selection
model width a corresponding change in the data model.

**Parameters:**
- index0

- the beginning of the interval
- index1

- the end of the interval

---

#### void setValueIsAdjusting​(boolean valueIsAdjusting)

Sets the

valueIsAdjusting

property, which indicates whether
or not upcoming selection changes should be considered part of a single
change. The value of this property is used to initialize the

valueIsAdjusting

property of the

ListSelectionEvent

s that
are generated.

For example, if the selection is being updated in response to a user
drag, this property can be set to

true

when the drag is initiated
and set to

false

when the drag is finished. During the drag,
listeners receive events with a

valueIsAdjusting

property
set to

true

. At the end of the drag, when the change is
finalized, listeners receive an event with the value set to

false

.
Listeners can use this pattern if they wish to update only when a change
has been finalized.

Setting this property to

true

begins a series of changes that
is to be considered part of a single change. When the property is changed
back to

false

, an event is sent out characterizing the entire
selection change (if there was one), with the event's

valueIsAdjusting

property set to

false

.

**Parameters:**
- valueIsAdjusting

- the new value of the property

**See Also:**
- getValueIsAdjusting()

,

ListSelectionEvent.getValueIsAdjusting()

---

#### boolean getValueIsAdjusting()

Returns

true

if the selection is undergoing a series of changes.

**Returns:**
- true if the selection is undergoing a series of changes

**See Also:**
- setValueIsAdjusting(boolean)

---

#### void setSelectionMode​(int selectionMode)

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

**Parameters:**
- selectionMode

- the selection mode

**Throws:**
- IllegalArgumentException

- if the selection mode isn't
one of those allowed

**See Also:**
- getSelectionMode()

---

#### int getSelectionMode()

Returns the current selection mode.

**Returns:**
- the current selection mode

**See Also:**
- setSelectionMode(int)

---

#### void addListSelectionListener​(
ListSelectionListener
x)

Add a listener to the list that's notified each time a change
to the selection occurs.

**Parameters:**
- x

- the ListSelectionListener

**See Also:**
- removeListSelectionListener(javax.swing.event.ListSelectionListener)

,

setSelectionInterval(int, int)

,

addSelectionInterval(int, int)

,

removeSelectionInterval(int, int)

,

clearSelection()

,

insertIndexInterval(int, int, boolean)

,

removeIndexInterval(int, int)

---

#### void removeListSelectionListener​(
ListSelectionListener
x)

Remove a listener from the list that's notified each time a
change to the selection occurs.

**Parameters:**
- x

- the ListSelectionListener

**See Also:**
- addListSelectionListener(javax.swing.event.ListSelectionListener)

---

#### default int[] getSelectedIndices()

Returns an array of all of the selected indices in the selection model,
in increasing order.

**Returns:**
- all of the selected indices, in increasing order,
or an empty array if nothing is selected

**See Also:**
- removeSelectionInterval(int, int)

,

addListSelectionListener(javax.swing.event.ListSelectionListener)

**Since:**
- 11

**Implementation Requirements:**
- The default implementation iterates from minimum selected
index

getMinSelectionIndex()

to maximum selected index

getMaxSelectionIndex()

and returns the selected indices

isSelectedIndex(int)

in a newly allocated int array.

---

#### default int getSelectedItemsCount()

Returns the number of selected items.

**Returns:**
- the number of selected items, 0 if no items are selected

**Since:**
- 11

**Implementation Requirements:**
- The default implementation iterates from minimum selected
index

getMinSelectionIndex()

to maximum selected index

getMaxSelectionIndex()

and returns the number of selected indices

isSelectedIndex(int)

---

### Additional Sections

#### Interface ListSelectionModel

**All Known Implementing Classes:** DefaultListSelectionModel

```java
public interface
ListSelectionModel
```

This interface represents the current state of the
selection for any of the components that display a
list of values with stable indices. The selection is
modeled as a set of intervals, each interval represents
a contiguous range of selected list elements.
The methods for modifying the set of selected intervals
all take a pair of indices, index0 and index1, that represent
a closed interval, i.e. the interval includes both index0 and
index1.

**Since:** 1.2
**See Also:** DefaultListSelectionModel

public interface

ListSelectionModel

This interface represents the current state of the
selection for any of the components that display a
list of values with stable indices. The selection is
modeled as a set of intervals, each interval represents
a contiguous range of selected list elements.
The methods for modifying the set of selected intervals
all take a pair of indices, index0 and index1, that represent
a closed interval, i.e. the interval includes both index0 and
index1.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

MULTIPLE_INTERVAL_SELECTION

A value for the selectionMode property: select one or more
contiguous ranges of indices at a time.

static int

SINGLE_INTERVAL_SELECTION

A value for the selectionMode property: select one contiguous
range of indices at a time.

static int

SINGLE_SELECTION

A value for the selectionMode property: select one list index
at a time.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

void

addListSelectionListener

​(

ListSelectionListener

x)

Add a listener to the list that's notified each time a change
to the selection occurs.

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

void

clearSelection

()

Change the selection to the empty set.

int

getAnchorSelectionIndex

()

Return the first index argument from the most recent call to
setSelectionInterval(), addSelectionInterval() or removeSelectionInterval().

int

getLeadSelectionIndex

()

Return the second index argument from the most recent call to
setSelectionInterval(), addSelectionInterval() or removeSelectionInterval().

int

getMaxSelectionIndex

()

Returns the last selected index or -1 if the selection is empty.

int

getMinSelectionIndex

()

Returns the first selected index or -1 if the selection is empty.

default int[]

getSelectedIndices

()

Returns an array of all of the selected indices in the selection model,
in increasing order.

default int

getSelectedItemsCount

()

Returns the number of selected items.

int

getSelectionMode

()

Returns the current selection mode.

boolean

getValueIsAdjusting

()

Returns

true

if the selection is undergoing a series of changes.

void

insertIndexInterval

​(int index,
int length,
boolean before)

Insert

length

indices beginning before/after

index

.

boolean

isSelectedIndex

​(int index)

Returns true if the specified index is selected.

boolean

isSelectionEmpty

()

Returns true if no indices are selected.

void

removeIndexInterval

​(int index0,
int index1)

Remove the indices in the interval

index0,index1

(inclusive) from
the selection model.

void

removeListSelectionListener

​(

ListSelectionListener

x)

Remove a listener from the list that's notified each time a
change to the selection occurs.

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

​(int index)

Set the anchor selection index.

void

setLeadSelectionIndex

​(int index)

Set the lead selection index.

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

void

setValueIsAdjusting

​(boolean valueIsAdjusting)

Sets the

valueIsAdjusting

property, which indicates whether
or not upcoming selection changes should be considered part of a single
change.

Field Summary

Fields

Modifier and Type

Field

Description

static int

MULTIPLE_INTERVAL_SELECTION

A value for the selectionMode property: select one or more
contiguous ranges of indices at a time.

static int

SINGLE_INTERVAL_SELECTION

A value for the selectionMode property: select one contiguous
range of indices at a time.

static int

SINGLE_SELECTION

A value for the selectionMode property: select one list index
at a time.

---

#### Field Summary

A value for the selectionMode property: select one or more
contiguous ranges of indices at a time.

A value for the selectionMode property: select one contiguous
range of indices at a time.

A value for the selectionMode property: select one list index
at a time.

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

void

addListSelectionListener

​(

ListSelectionListener

x)

Add a listener to the list that's notified each time a change
to the selection occurs.

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

void

clearSelection

()

Change the selection to the empty set.

int

getAnchorSelectionIndex

()

Return the first index argument from the most recent call to
setSelectionInterval(), addSelectionInterval() or removeSelectionInterval().

int

getLeadSelectionIndex

()

Return the second index argument from the most recent call to
setSelectionInterval(), addSelectionInterval() or removeSelectionInterval().

int

getMaxSelectionIndex

()

Returns the last selected index or -1 if the selection is empty.

int

getMinSelectionIndex

()

Returns the first selected index or -1 if the selection is empty.

default int[]

getSelectedIndices

()

Returns an array of all of the selected indices in the selection model,
in increasing order.

default int

getSelectedItemsCount

()

Returns the number of selected items.

int

getSelectionMode

()

Returns the current selection mode.

boolean

getValueIsAdjusting

()

Returns

true

if the selection is undergoing a series of changes.

void

insertIndexInterval

​(int index,
int length,
boolean before)

Insert

length

indices beginning before/after

index

.

boolean

isSelectedIndex

​(int index)

Returns true if the specified index is selected.

boolean

isSelectionEmpty

()

Returns true if no indices are selected.

void

removeIndexInterval

​(int index0,
int index1)

Remove the indices in the interval

index0,index1

(inclusive) from
the selection model.

void

removeListSelectionListener

​(

ListSelectionListener

x)

Remove a listener from the list that's notified each time a
change to the selection occurs.

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

​(int index)

Set the anchor selection index.

void

setLeadSelectionIndex

​(int index)

Set the lead selection index.

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

void

setValueIsAdjusting

​(boolean valueIsAdjusting)

Sets the

valueIsAdjusting

property, which indicates whether
or not upcoming selection changes should be considered part of a single
change.

---

#### Method Summary

Add a listener to the list that's notified each time a change
to the selection occurs.

Changes the selection to be the set union of the current selection
and the indices between

index0

and

index1

inclusive.

Change the selection to the empty set.

Return the first index argument from the most recent call to
setSelectionInterval(), addSelectionInterval() or removeSelectionInterval().

Return the second index argument from the most recent call to
setSelectionInterval(), addSelectionInterval() or removeSelectionInterval().

Returns the last selected index or -1 if the selection is empty.

Returns the first selected index or -1 if the selection is empty.

Returns an array of all of the selected indices in the selection model,
in increasing order.

Returns the number of selected items.

Returns the current selection mode.

Returns

true

if the selection is undergoing a series of changes.

Insert

length

indices beginning before/after

index

.

Returns true if the specified index is selected.

Returns true if no indices are selected.

Remove the indices in the interval

index0,index1

(inclusive) from
the selection model.

Remove a listener from the list that's notified each time a
change to the selection occurs.

Changes the selection to be the set difference of the current selection
and the indices between

index0

and

index1

inclusive.

Set the anchor selection index.

Set the lead selection index.

Changes the selection to be between

index0

and

index1

inclusive.

Sets the selection mode.

Sets the

valueIsAdjusting

property, which indicates whether
or not upcoming selection changes should be considered part of a single
change.

============ FIELD DETAIL ===========

- Field Detail

- SINGLE_SELECTION

```java
static final int SINGLE_SELECTION
```

A value for the selectionMode property: select one list index
at a time.

**See Also:** setSelectionMode(int)

,

Constant Field Values

- SINGLE_INTERVAL_SELECTION

```java
static final int SINGLE_INTERVAL_SELECTION
```

A value for the selectionMode property: select one contiguous
range of indices at a time.

**See Also:** setSelectionMode(int)

,

Constant Field Values

- MULTIPLE_INTERVAL_SELECTION

```java
static final int MULTIPLE_INTERVAL_SELECTION
```

A value for the selectionMode property: select one or more
contiguous ranges of indices at a time.

**See Also:** setSelectionMode(int)

,

Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- setSelectionInterval

```java
void setSelectionInterval​(int index0,
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

**Parameters:** index0

- one end of the interval.
**Parameters:** index1

- other end of the interval
**See Also:** addListSelectionListener(javax.swing.event.ListSelectionListener)

- addSelectionInterval

```java
void addSelectionInterval​(int index0,
int index1)
```

Changes the selection to be the set union of the current selection
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
and can therefore be used to grow the selection.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

**Parameters:** index0

- one end of the interval.
**Parameters:** index1

- other end of the interval
**See Also:** addListSelectionListener(javax.swing.event.ListSelectionListener)

,

setSelectionInterval(int, int)

- removeSelectionInterval

```java
void removeSelectionInterval​(int index0,
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

**Parameters:** index0

- one end of the interval.
**Parameters:** index1

- other end of the interval
**See Also:** addListSelectionListener(javax.swing.event.ListSelectionListener)

- getMinSelectionIndex

```java
int getMinSelectionIndex()
```

Returns the first selected index or -1 if the selection is empty.

**Returns:** the first selected index or -1 if the selection is empty.

- getMaxSelectionIndex

```java
int getMaxSelectionIndex()
```

Returns the last selected index or -1 if the selection is empty.

**Returns:** the last selected index or -1 if the selection is empty.

- isSelectedIndex

```java
boolean isSelectedIndex​(int index)
```

Returns true if the specified index is selected.

**Parameters:** index

- an index
**Returns:** true

if the specified index is selected

- getAnchorSelectionIndex

```java
int getAnchorSelectionIndex()
```

Return the first index argument from the most recent call to
setSelectionInterval(), addSelectionInterval() or removeSelectionInterval().
The most recent index0 is considered the "anchor" and the most recent
index1 is considered the "lead". Some interfaces display these
indices specially, e.g. Windows95 displays the lead index with a
dotted yellow outline.

**Returns:** the anchor selection index
**See Also:** getLeadSelectionIndex()

,

setSelectionInterval(int, int)

,

addSelectionInterval(int, int)

- setAnchorSelectionIndex

```java
void setAnchorSelectionIndex​(int index)
```

Set the anchor selection index.

**Parameters:** index

- the anchor selection index
**See Also:** getAnchorSelectionIndex()

- getLeadSelectionIndex

```java
int getLeadSelectionIndex()
```

Return the second index argument from the most recent call to
setSelectionInterval(), addSelectionInterval() or removeSelectionInterval().

**Returns:** the lead selection index.
**See Also:** getAnchorSelectionIndex()

,

setSelectionInterval(int, int)

,

addSelectionInterval(int, int)

- setLeadSelectionIndex

```java
void setLeadSelectionIndex​(int index)
```

Set the lead selection index.

**Parameters:** index

- the lead selection index
**See Also:** getLeadSelectionIndex()

- clearSelection

```java
void clearSelection()
```

Change the selection to the empty set. If this represents
a change to the current selection then notify each ListSelectionListener.

**See Also:** addListSelectionListener(javax.swing.event.ListSelectionListener)

- isSelectionEmpty

```java
boolean isSelectionEmpty()
```

Returns true if no indices are selected.

**Returns:** true

if no indices are selected.

- insertIndexInterval

```java
void insertIndexInterval​(int index,
int length,
boolean before)
```

Insert

length

indices beginning before/after

index

. This is typically
called to sync the selection model with a corresponding change
in the data model.

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
void removeIndexInterval​(int index0,
int index1)
```

Remove the indices in the interval

index0,index1

(inclusive) from
the selection model. This is typically called to sync the selection
model width a corresponding change in the data model.

**Parameters:** index0

- the beginning of the interval
**Parameters:** index1

- the end of the interval

- setValueIsAdjusting

```java
void setValueIsAdjusting​(boolean valueIsAdjusting)
```

Sets the

valueIsAdjusting

property, which indicates whether
or not upcoming selection changes should be considered part of a single
change. The value of this property is used to initialize the

valueIsAdjusting

property of the

ListSelectionEvent

s that
are generated.

For example, if the selection is being updated in response to a user
drag, this property can be set to

true

when the drag is initiated
and set to

false

when the drag is finished. During the drag,
listeners receive events with a

valueIsAdjusting

property
set to

true

. At the end of the drag, when the change is
finalized, listeners receive an event with the value set to

false

.
Listeners can use this pattern if they wish to update only when a change
has been finalized.

Setting this property to

true

begins a series of changes that
is to be considered part of a single change. When the property is changed
back to

false

, an event is sent out characterizing the entire
selection change (if there was one), with the event's

valueIsAdjusting

property set to

false

.

**Parameters:** valueIsAdjusting

- the new value of the property
**See Also:** getValueIsAdjusting()

,

ListSelectionEvent.getValueIsAdjusting()

- getValueIsAdjusting

```java
boolean getValueIsAdjusting()
```

Returns

true

if the selection is undergoing a series of changes.

**Returns:** true if the selection is undergoing a series of changes
**See Also:** setValueIsAdjusting(boolean)

- setSelectionMode

```java
void setSelectionMode​(int selectionMode)
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

**Parameters:** selectionMode

- the selection mode
**Throws:** IllegalArgumentException

- if the selection mode isn't
one of those allowed
**See Also:** getSelectionMode()

- getSelectionMode

```java
int getSelectionMode()
```

Returns the current selection mode.

**Returns:** the current selection mode
**See Also:** setSelectionMode(int)

- addListSelectionListener

```java
void addListSelectionListener​(
ListSelectionListener
x)
```

Add a listener to the list that's notified each time a change
to the selection occurs.

**Parameters:** x

- the ListSelectionListener
**See Also:** removeListSelectionListener(javax.swing.event.ListSelectionListener)

,

setSelectionInterval(int, int)

,

addSelectionInterval(int, int)

,

removeSelectionInterval(int, int)

,

clearSelection()

,

insertIndexInterval(int, int, boolean)

,

removeIndexInterval(int, int)

- removeListSelectionListener

```java
void removeListSelectionListener​(
ListSelectionListener
x)
```

Remove a listener from the list that's notified each time a
change to the selection occurs.

**Parameters:** x

- the ListSelectionListener
**See Also:** addListSelectionListener(javax.swing.event.ListSelectionListener)

- getSelectedIndices

```java
default int[] getSelectedIndices()
```

Returns an array of all of the selected indices in the selection model,
in increasing order.

**Implementation Requirements:** The default implementation iterates from minimum selected
index

getMinSelectionIndex()

to maximum selected index

getMaxSelectionIndex()

and returns the selected indices

isSelectedIndex(int)

in a newly allocated int array.
**Returns:** all of the selected indices, in increasing order,
or an empty array if nothing is selected
**Since:** 11
**See Also:** removeSelectionInterval(int, int)

,

addListSelectionListener(javax.swing.event.ListSelectionListener)

- getSelectedItemsCount

```java
default int getSelectedItemsCount()
```

Returns the number of selected items.

**Implementation Requirements:** The default implementation iterates from minimum selected
index

getMinSelectionIndex()

to maximum selected index

getMaxSelectionIndex()

and returns the number of selected indices

isSelectedIndex(int)
**Returns:** the number of selected items, 0 if no items are selected
**Since:** 11

Field Detail

- SINGLE_SELECTION

```java
static final int SINGLE_SELECTION
```

A value for the selectionMode property: select one list index
at a time.

**See Also:** setSelectionMode(int)

,

Constant Field Values

- SINGLE_INTERVAL_SELECTION

```java
static final int SINGLE_INTERVAL_SELECTION
```

A value for the selectionMode property: select one contiguous
range of indices at a time.

**See Also:** setSelectionMode(int)

,

Constant Field Values

- MULTIPLE_INTERVAL_SELECTION

```java
static final int MULTIPLE_INTERVAL_SELECTION
```

A value for the selectionMode property: select one or more
contiguous ranges of indices at a time.

**See Also:** setSelectionMode(int)

,

Constant Field Values

---

#### Field Detail

SINGLE_SELECTION

```java
static final int SINGLE_SELECTION
```

A value for the selectionMode property: select one list index
at a time.

**See Also:** setSelectionMode(int)

,

Constant Field Values

---

#### SINGLE_SELECTION

static final int SINGLE_SELECTION

A value for the selectionMode property: select one list index
at a time.

SINGLE_INTERVAL_SELECTION

```java
static final int SINGLE_INTERVAL_SELECTION
```

A value for the selectionMode property: select one contiguous
range of indices at a time.

**See Also:** setSelectionMode(int)

,

Constant Field Values

---

#### SINGLE_INTERVAL_SELECTION

static final int SINGLE_INTERVAL_SELECTION

A value for the selectionMode property: select one contiguous
range of indices at a time.

MULTIPLE_INTERVAL_SELECTION

```java
static final int MULTIPLE_INTERVAL_SELECTION
```

A value for the selectionMode property: select one or more
contiguous ranges of indices at a time.

**See Also:** setSelectionMode(int)

,

Constant Field Values

---

#### MULTIPLE_INTERVAL_SELECTION

static final int MULTIPLE_INTERVAL_SELECTION

A value for the selectionMode property: select one or more
contiguous ranges of indices at a time.

Method Detail

- setSelectionInterval

```java
void setSelectionInterval​(int index0,
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

**Parameters:** index0

- one end of the interval.
**Parameters:** index1

- other end of the interval
**See Also:** addListSelectionListener(javax.swing.event.ListSelectionListener)

- addSelectionInterval

```java
void addSelectionInterval​(int index0,
int index1)
```

Changes the selection to be the set union of the current selection
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
and can therefore be used to grow the selection.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

**Parameters:** index0

- one end of the interval.
**Parameters:** index1

- other end of the interval
**See Also:** addListSelectionListener(javax.swing.event.ListSelectionListener)

,

setSelectionInterval(int, int)

- removeSelectionInterval

```java
void removeSelectionInterval​(int index0,
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

**Parameters:** index0

- one end of the interval.
**Parameters:** index1

- other end of the interval
**See Also:** addListSelectionListener(javax.swing.event.ListSelectionListener)

- getMinSelectionIndex

```java
int getMinSelectionIndex()
```

Returns the first selected index or -1 if the selection is empty.

**Returns:** the first selected index or -1 if the selection is empty.

- getMaxSelectionIndex

```java
int getMaxSelectionIndex()
```

Returns the last selected index or -1 if the selection is empty.

**Returns:** the last selected index or -1 if the selection is empty.

- isSelectedIndex

```java
boolean isSelectedIndex​(int index)
```

Returns true if the specified index is selected.

**Parameters:** index

- an index
**Returns:** true

if the specified index is selected

- getAnchorSelectionIndex

```java
int getAnchorSelectionIndex()
```

Return the first index argument from the most recent call to
setSelectionInterval(), addSelectionInterval() or removeSelectionInterval().
The most recent index0 is considered the "anchor" and the most recent
index1 is considered the "lead". Some interfaces display these
indices specially, e.g. Windows95 displays the lead index with a
dotted yellow outline.

**Returns:** the anchor selection index
**See Also:** getLeadSelectionIndex()

,

setSelectionInterval(int, int)

,

addSelectionInterval(int, int)

- setAnchorSelectionIndex

```java
void setAnchorSelectionIndex​(int index)
```

Set the anchor selection index.

**Parameters:** index

- the anchor selection index
**See Also:** getAnchorSelectionIndex()

- getLeadSelectionIndex

```java
int getLeadSelectionIndex()
```

Return the second index argument from the most recent call to
setSelectionInterval(), addSelectionInterval() or removeSelectionInterval().

**Returns:** the lead selection index.
**See Also:** getAnchorSelectionIndex()

,

setSelectionInterval(int, int)

,

addSelectionInterval(int, int)

- setLeadSelectionIndex

```java
void setLeadSelectionIndex​(int index)
```

Set the lead selection index.

**Parameters:** index

- the lead selection index
**See Also:** getLeadSelectionIndex()

- clearSelection

```java
void clearSelection()
```

Change the selection to the empty set. If this represents
a change to the current selection then notify each ListSelectionListener.

**See Also:** addListSelectionListener(javax.swing.event.ListSelectionListener)

- isSelectionEmpty

```java
boolean isSelectionEmpty()
```

Returns true if no indices are selected.

**Returns:** true

if no indices are selected.

- insertIndexInterval

```java
void insertIndexInterval​(int index,
int length,
boolean before)
```

Insert

length

indices beginning before/after

index

. This is typically
called to sync the selection model with a corresponding change
in the data model.

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
void removeIndexInterval​(int index0,
int index1)
```

Remove the indices in the interval

index0,index1

(inclusive) from
the selection model. This is typically called to sync the selection
model width a corresponding change in the data model.

**Parameters:** index0

- the beginning of the interval
**Parameters:** index1

- the end of the interval

- setValueIsAdjusting

```java
void setValueIsAdjusting​(boolean valueIsAdjusting)
```

Sets the

valueIsAdjusting

property, which indicates whether
or not upcoming selection changes should be considered part of a single
change. The value of this property is used to initialize the

valueIsAdjusting

property of the

ListSelectionEvent

s that
are generated.

For example, if the selection is being updated in response to a user
drag, this property can be set to

true

when the drag is initiated
and set to

false

when the drag is finished. During the drag,
listeners receive events with a

valueIsAdjusting

property
set to

true

. At the end of the drag, when the change is
finalized, listeners receive an event with the value set to

false

.
Listeners can use this pattern if they wish to update only when a change
has been finalized.

Setting this property to

true

begins a series of changes that
is to be considered part of a single change. When the property is changed
back to

false

, an event is sent out characterizing the entire
selection change (if there was one), with the event's

valueIsAdjusting

property set to

false

.

**Parameters:** valueIsAdjusting

- the new value of the property
**See Also:** getValueIsAdjusting()

,

ListSelectionEvent.getValueIsAdjusting()

- getValueIsAdjusting

```java
boolean getValueIsAdjusting()
```

Returns

true

if the selection is undergoing a series of changes.

**Returns:** true if the selection is undergoing a series of changes
**See Also:** setValueIsAdjusting(boolean)

- setSelectionMode

```java
void setSelectionMode​(int selectionMode)
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

**Parameters:** selectionMode

- the selection mode
**Throws:** IllegalArgumentException

- if the selection mode isn't
one of those allowed
**See Also:** getSelectionMode()

- getSelectionMode

```java
int getSelectionMode()
```

Returns the current selection mode.

**Returns:** the current selection mode
**See Also:** setSelectionMode(int)

- addListSelectionListener

```java
void addListSelectionListener​(
ListSelectionListener
x)
```

Add a listener to the list that's notified each time a change
to the selection occurs.

**Parameters:** x

- the ListSelectionListener
**See Also:** removeListSelectionListener(javax.swing.event.ListSelectionListener)

,

setSelectionInterval(int, int)

,

addSelectionInterval(int, int)

,

removeSelectionInterval(int, int)

,

clearSelection()

,

insertIndexInterval(int, int, boolean)

,

removeIndexInterval(int, int)

- removeListSelectionListener

```java
void removeListSelectionListener​(
ListSelectionListener
x)
```

Remove a listener from the list that's notified each time a
change to the selection occurs.

**Parameters:** x

- the ListSelectionListener
**See Also:** addListSelectionListener(javax.swing.event.ListSelectionListener)

- getSelectedIndices

```java
default int[] getSelectedIndices()
```

Returns an array of all of the selected indices in the selection model,
in increasing order.

**Implementation Requirements:** The default implementation iterates from minimum selected
index

getMinSelectionIndex()

to maximum selected index

getMaxSelectionIndex()

and returns the selected indices

isSelectedIndex(int)

in a newly allocated int array.
**Returns:** all of the selected indices, in increasing order,
or an empty array if nothing is selected
**Since:** 11
**See Also:** removeSelectionInterval(int, int)

,

addListSelectionListener(javax.swing.event.ListSelectionListener)

- getSelectedItemsCount

```java
default int getSelectedItemsCount()
```

Returns the number of selected items.

**Implementation Requirements:** The default implementation iterates from minimum selected
index

getMinSelectionIndex()

to maximum selected index

getMaxSelectionIndex()

and returns the number of selected indices

isSelectedIndex(int)
**Returns:** the number of selected items, 0 if no items are selected
**Since:** 11

---

#### Method Detail

setSelectionInterval

```java
void setSelectionInterval​(int index0,
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

**Parameters:** index0

- one end of the interval.
**Parameters:** index1

- other end of the interval
**See Also:** addListSelectionListener(javax.swing.event.ListSelectionListener)

---

#### setSelectionInterval

void setSelectionInterval​(int index0,
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

In

SINGLE_SELECTION

selection mode, only the second index
is used.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

addSelectionInterval

```java
void addSelectionInterval​(int index0,
int index1)
```

Changes the selection to be the set union of the current selection
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
and can therefore be used to grow the selection.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

**Parameters:** index0

- one end of the interval.
**Parameters:** index1

- other end of the interval
**See Also:** addListSelectionListener(javax.swing.event.ListSelectionListener)

,

setSelectionInterval(int, int)

---

#### addSelectionInterval

void addSelectionInterval​(int index0,
int index1)

Changes the selection to be the set union of the current selection
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
and can therefore be used to grow the selection.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

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
and can therefore be used to grow the selection.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

removeSelectionInterval

```java
void removeSelectionInterval​(int index0,
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

**Parameters:** index0

- one end of the interval.
**Parameters:** index1

- other end of the interval
**See Also:** addListSelectionListener(javax.swing.event.ListSelectionListener)

---

#### removeSelectionInterval

void removeSelectionInterval​(int index0,
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

If this represents a change to the current selection, then each

ListSelectionListener

is notified of the change.

getMinSelectionIndex

```java
int getMinSelectionIndex()
```

Returns the first selected index or -1 if the selection is empty.

**Returns:** the first selected index or -1 if the selection is empty.

---

#### getMinSelectionIndex

int getMinSelectionIndex()

Returns the first selected index or -1 if the selection is empty.

getMaxSelectionIndex

```java
int getMaxSelectionIndex()
```

Returns the last selected index or -1 if the selection is empty.

**Returns:** the last selected index or -1 if the selection is empty.

---

#### getMaxSelectionIndex

int getMaxSelectionIndex()

Returns the last selected index or -1 if the selection is empty.

isSelectedIndex

```java
boolean isSelectedIndex​(int index)
```

Returns true if the specified index is selected.

**Parameters:** index

- an index
**Returns:** true

if the specified index is selected

---

#### isSelectedIndex

boolean isSelectedIndex​(int index)

Returns true if the specified index is selected.

getAnchorSelectionIndex

```java
int getAnchorSelectionIndex()
```

Return the first index argument from the most recent call to
setSelectionInterval(), addSelectionInterval() or removeSelectionInterval().
The most recent index0 is considered the "anchor" and the most recent
index1 is considered the "lead". Some interfaces display these
indices specially, e.g. Windows95 displays the lead index with a
dotted yellow outline.

**Returns:** the anchor selection index
**See Also:** getLeadSelectionIndex()

,

setSelectionInterval(int, int)

,

addSelectionInterval(int, int)

---

#### getAnchorSelectionIndex

int getAnchorSelectionIndex()

Return the first index argument from the most recent call to
setSelectionInterval(), addSelectionInterval() or removeSelectionInterval().
The most recent index0 is considered the "anchor" and the most recent
index1 is considered the "lead". Some interfaces display these
indices specially, e.g. Windows95 displays the lead index with a
dotted yellow outline.

setAnchorSelectionIndex

```java
void setAnchorSelectionIndex​(int index)
```

Set the anchor selection index.

**Parameters:** index

- the anchor selection index
**See Also:** getAnchorSelectionIndex()

---

#### setAnchorSelectionIndex

void setAnchorSelectionIndex​(int index)

Set the anchor selection index.

getLeadSelectionIndex

```java
int getLeadSelectionIndex()
```

Return the second index argument from the most recent call to
setSelectionInterval(), addSelectionInterval() or removeSelectionInterval().

**Returns:** the lead selection index.
**See Also:** getAnchorSelectionIndex()

,

setSelectionInterval(int, int)

,

addSelectionInterval(int, int)

---

#### getLeadSelectionIndex

int getLeadSelectionIndex()

Return the second index argument from the most recent call to
setSelectionInterval(), addSelectionInterval() or removeSelectionInterval().

setLeadSelectionIndex

```java
void setLeadSelectionIndex​(int index)
```

Set the lead selection index.

**Parameters:** index

- the lead selection index
**See Also:** getLeadSelectionIndex()

---

#### setLeadSelectionIndex

void setLeadSelectionIndex​(int index)

Set the lead selection index.

clearSelection

```java
void clearSelection()
```

Change the selection to the empty set. If this represents
a change to the current selection then notify each ListSelectionListener.

**See Also:** addListSelectionListener(javax.swing.event.ListSelectionListener)

---

#### clearSelection

void clearSelection()

Change the selection to the empty set. If this represents
a change to the current selection then notify each ListSelectionListener.

isSelectionEmpty

```java
boolean isSelectionEmpty()
```

Returns true if no indices are selected.

**Returns:** true

if no indices are selected.

---

#### isSelectionEmpty

boolean isSelectionEmpty()

Returns true if no indices are selected.

insertIndexInterval

```java
void insertIndexInterval​(int index,
int length,
boolean before)
```

Insert

length

indices beginning before/after

index

. This is typically
called to sync the selection model with a corresponding change
in the data model.

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

void insertIndexInterval​(int index,
int length,
boolean before)

Insert

length

indices beginning before/after

index

. This is typically
called to sync the selection model with a corresponding change
in the data model.

removeIndexInterval

```java
void removeIndexInterval​(int index0,
int index1)
```

Remove the indices in the interval

index0,index1

(inclusive) from
the selection model. This is typically called to sync the selection
model width a corresponding change in the data model.

**Parameters:** index0

- the beginning of the interval
**Parameters:** index1

- the end of the interval

---

#### removeIndexInterval

void removeIndexInterval​(int index0,
int index1)

Remove the indices in the interval

index0,index1

(inclusive) from
the selection model. This is typically called to sync the selection
model width a corresponding change in the data model.

setValueIsAdjusting

```java
void setValueIsAdjusting​(boolean valueIsAdjusting)
```

Sets the

valueIsAdjusting

property, which indicates whether
or not upcoming selection changes should be considered part of a single
change. The value of this property is used to initialize the

valueIsAdjusting

property of the

ListSelectionEvent

s that
are generated.

For example, if the selection is being updated in response to a user
drag, this property can be set to

true

when the drag is initiated
and set to

false

when the drag is finished. During the drag,
listeners receive events with a

valueIsAdjusting

property
set to

true

. At the end of the drag, when the change is
finalized, listeners receive an event with the value set to

false

.
Listeners can use this pattern if they wish to update only when a change
has been finalized.

Setting this property to

true

begins a series of changes that
is to be considered part of a single change. When the property is changed
back to

false

, an event is sent out characterizing the entire
selection change (if there was one), with the event's

valueIsAdjusting

property set to

false

.

**Parameters:** valueIsAdjusting

- the new value of the property
**See Also:** getValueIsAdjusting()

,

ListSelectionEvent.getValueIsAdjusting()

---

#### setValueIsAdjusting

void setValueIsAdjusting​(boolean valueIsAdjusting)

Sets the

valueIsAdjusting

property, which indicates whether
or not upcoming selection changes should be considered part of a single
change. The value of this property is used to initialize the

valueIsAdjusting

property of the

ListSelectionEvent

s that
are generated.

For example, if the selection is being updated in response to a user
drag, this property can be set to

true

when the drag is initiated
and set to

false

when the drag is finished. During the drag,
listeners receive events with a

valueIsAdjusting

property
set to

true

. At the end of the drag, when the change is
finalized, listeners receive an event with the value set to

false

.
Listeners can use this pattern if they wish to update only when a change
has been finalized.

Setting this property to

true

begins a series of changes that
is to be considered part of a single change. When the property is changed
back to

false

, an event is sent out characterizing the entire
selection change (if there was one), with the event's

valueIsAdjusting

property set to

false

.

For example, if the selection is being updated in response to a user
drag, this property can be set to

true

when the drag is initiated
and set to

false

when the drag is finished. During the drag,
listeners receive events with a

valueIsAdjusting

property
set to

true

. At the end of the drag, when the change is
finalized, listeners receive an event with the value set to

false

.
Listeners can use this pattern if they wish to update only when a change
has been finalized.

Setting this property to

true

begins a series of changes that
is to be considered part of a single change. When the property is changed
back to

false

, an event is sent out characterizing the entire
selection change (if there was one), with the event's

valueIsAdjusting

property set to

false

.

Setting this property to

true

begins a series of changes that
is to be considered part of a single change. When the property is changed
back to

false

, an event is sent out characterizing the entire
selection change (if there was one), with the event's

valueIsAdjusting

property set to

false

.

getValueIsAdjusting

```java
boolean getValueIsAdjusting()
```

Returns

true

if the selection is undergoing a series of changes.

**Returns:** true if the selection is undergoing a series of changes
**See Also:** setValueIsAdjusting(boolean)

---

#### getValueIsAdjusting

boolean getValueIsAdjusting()

Returns

true

if the selection is undergoing a series of changes.

setSelectionMode

```java
void setSelectionMode​(int selectionMode)
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

**Parameters:** selectionMode

- the selection mode
**Throws:** IllegalArgumentException

- if the selection mode isn't
one of those allowed
**See Also:** getSelectionMode()

---

#### setSelectionMode

void setSelectionMode​(int selectionMode)

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

getSelectionMode

```java
int getSelectionMode()
```

Returns the current selection mode.

**Returns:** the current selection mode
**See Also:** setSelectionMode(int)

---

#### getSelectionMode

int getSelectionMode()

Returns the current selection mode.

addListSelectionListener

```java
void addListSelectionListener​(
ListSelectionListener
x)
```

Add a listener to the list that's notified each time a change
to the selection occurs.

**Parameters:** x

- the ListSelectionListener
**See Also:** removeListSelectionListener(javax.swing.event.ListSelectionListener)

,

setSelectionInterval(int, int)

,

addSelectionInterval(int, int)

,

removeSelectionInterval(int, int)

,

clearSelection()

,

insertIndexInterval(int, int, boolean)

,

removeIndexInterval(int, int)

---

#### addListSelectionListener

void addListSelectionListener​(

ListSelectionListener

x)

Add a listener to the list that's notified each time a change
to the selection occurs.

removeListSelectionListener

```java
void removeListSelectionListener​(
ListSelectionListener
x)
```

Remove a listener from the list that's notified each time a
change to the selection occurs.

**Parameters:** x

- the ListSelectionListener
**See Also:** addListSelectionListener(javax.swing.event.ListSelectionListener)

---

#### removeListSelectionListener

void removeListSelectionListener​(

ListSelectionListener

x)

Remove a listener from the list that's notified each time a
change to the selection occurs.

getSelectedIndices

```java
default int[] getSelectedIndices()
```

Returns an array of all of the selected indices in the selection model,
in increasing order.

**Implementation Requirements:** The default implementation iterates from minimum selected
index

getMinSelectionIndex()

to maximum selected index

getMaxSelectionIndex()

and returns the selected indices

isSelectedIndex(int)

in a newly allocated int array.
**Returns:** all of the selected indices, in increasing order,
or an empty array if nothing is selected
**Since:** 11
**See Also:** removeSelectionInterval(int, int)

,

addListSelectionListener(javax.swing.event.ListSelectionListener)

---

#### getSelectedIndices

default int[] getSelectedIndices()

Returns an array of all of the selected indices in the selection model,
in increasing order.

getSelectedItemsCount

```java
default int getSelectedItemsCount()
```

Returns the number of selected items.

**Implementation Requirements:** The default implementation iterates from minimum selected
index

getMinSelectionIndex()

to maximum selected index

getMaxSelectionIndex()

and returns the number of selected indices

isSelectedIndex(int)
**Returns:** the number of selected items, 0 if no items are selected
**Since:** 11

---

#### getSelectedItemsCount

default int getSelectedItemsCount()

Returns the number of selected items.

---

