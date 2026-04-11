# Class DefaultTreeSelectionModel

**Source:** `java.desktop\javax\swing\tree\DefaultTreeSelectionModel.html`

### Class Description

```java
public class
DefaultTreeSelectionModel

extends
Object

implements
Cloneable
,
Serializable
,
TreeSelectionModel
```

Default implementation of TreeSelectionModel. Listeners are notified
whenever
the paths in the selection change, not the rows. In order
to be able to track row changes you may wish to become a listener
for expansion events on the tree and test for changes from there.

resetRowSelection is called from any of the methods that update
the selected paths. If you subclass any of these methods to
filter what is allowed to be selected, be sure and message

resetRowSelection

if you do not message super.

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

TreeSelectionModel

---

### Field Details

#### public static final
String
SELECTION_MODE_PROPERTY

Property name for selectionMode.

**See Also:**
- Constant Field Values

---

#### protected
SwingPropertyChangeSupport
changeSupport

Used to messaged registered listeners.

---

#### protected
TreePath
[] selection

Paths that are currently selected. Will be null if nothing is
currently selected.

---

#### protected
EventListenerList
listenerList

Event listener list.

---

#### protected transient
RowMapper
rowMapper

Provides a row for a given path.

---

#### protected
DefaultListSelectionModel
listSelectionModel

Handles maintaining the list selection model. The RowMapper is used
to map from a TreePath to a row, and the value is then placed here.

---

#### protected int selectionMode

Mode for the selection, will be either SINGLE_TREE_SELECTION,
CONTIGUOUS_TREE_SELECTION or DISCONTIGUOUS_TREE_SELECTION.

---

#### protected
TreePath
leadPath

Last path that was added.

---

#### protected int leadIndex

Index of the lead path in selection.

---

#### protected int leadRow

Lead row.

---

### Constructor Details

#### public DefaultTreeSelectionModel()

Creates a new instance of DefaultTreeSelectionModel that is
empty, with a selection mode of DISCONTIGUOUS_TREE_SELECTION.

---

### Method Details

#### public void setRowMapper​(
RowMapper
newMapper)

Sets the RowMapper instance. This instance is used to determine
the row for a particular TreePath.

**Specified by:**
- setRowMapper

in interface

TreeSelectionModel

**Parameters:**
- newMapper

- RowMapper to be set

---

#### public
RowMapper
getRowMapper()

Returns the RowMapper instance that is able to map a TreePath to a
row.

**Specified by:**
- getRowMapper

in interface

TreeSelectionModel

**Returns:**
- the RowMapper instance that is able to map a TreePath
to a row

---

#### public void setSelectionMode​(int mode)

Sets the selection model, which must be one of SINGLE_TREE_SELECTION,
CONTIGUOUS_TREE_SELECTION or DISCONTIGUOUS_TREE_SELECTION. If mode
is not one of the defined value,

DISCONTIGUOUS_TREE_SELECTION

is assumed.

This may change the selection if the current selection is not valid
for the new mode. For example, if three TreePaths are
selected when the mode is changed to

SINGLE_TREE_SELECTION

,
only one TreePath will remain selected. It is up to the particular
implementation to decide what TreePath remains selected.

Setting the mode to something other than the defined types will
result in the mode becoming

DISCONTIGUOUS_TREE_SELECTION

.

**Specified by:**
- setSelectionMode

in interface

TreeSelectionModel

**Parameters:**
- mode

- selection mode to be set

---

#### public int getSelectionMode()

Returns the selection mode, one of

SINGLE_TREE_SELECTION

,

DISCONTIGUOUS_TREE_SELECTION

or

CONTIGUOUS_TREE_SELECTION

.

**Specified by:**
- getSelectionMode

in interface

TreeSelectionModel

**Returns:**
- the current selection mode

---

#### public void setSelectionPath​(
TreePath
path)

Sets the selection to path. If this represents a change, then
the TreeSelectionListeners are notified. If

path

is
null, this has the same effect as invoking

clearSelection

.

**Specified by:**
- setSelectionPath

in interface

TreeSelectionModel

**Parameters:**
- path

- new path to select

---

#### public void setSelectionPaths​(
TreePath
[] pPaths)

Sets the selection. Whether the supplied paths are taken as the
new selection depends upon the selection mode. If the supplied
array is

null

, or empty, the selection is cleared. If
the selection mode is

SINGLE_TREE_SELECTION

, only the
first path in

pPaths

is used. If the selection
mode is

CONTIGUOUS_TREE_SELECTION

and the supplied paths
are not contiguous, then only the first path in

pPaths

is
used. If the selection mode is

DISCONTIGUOUS_TREE_SELECTION

, then all paths are used.

All

null

paths in

pPaths

are ignored.

If this represents a change, all registered

TreeSelectionListener

s are notified.

The lead path is set to the last unique path.

The paths returned from

getSelectionPaths

are in the same
order as those supplied to this method.

**Specified by:**
- setSelectionPaths

in interface

TreeSelectionModel

**Parameters:**
- pPaths

- the new selection

---

#### public void addSelectionPath​(
TreePath
path)

Adds path to the current selection. If path is not currently
in the selection the TreeSelectionListeners are notified. This has
no effect if

path

is null.

**Specified by:**
- addSelectionPath

in interface

TreeSelectionModel

**Parameters:**
- path

- the new path to add to the current selection

---

#### public void addSelectionPaths​(
TreePath
[] paths)

Adds paths to the current selection. If any of the paths in
paths are not currently in the selection the TreeSelectionListeners
are notified. This has
no effect if

paths

is null.

The lead path is set to the last element in

paths

.

If the selection mode is

CONTIGUOUS_TREE_SELECTION

,
and adding the new paths would make the selection discontiguous.
Then two things can result: if the TreePaths in

paths

are contiguous, then the selection becomes these TreePaths,
otherwise the TreePaths aren't contiguous and the selection becomes
the first TreePath in

paths

.

**Specified by:**
- addSelectionPaths

in interface

TreeSelectionModel

**Parameters:**
- paths

- the new path to add to the current selection

---

#### public void removeSelectionPath​(
TreePath
path)

Removes path from the selection. If path is in the selection
The TreeSelectionListeners are notified. This has no effect if

path

is null.

**Specified by:**
- removeSelectionPath

in interface

TreeSelectionModel

**Parameters:**
- path

- the path to remove from the selection

---

#### public void removeSelectionPaths​(
TreePath
[] paths)

Removes paths from the selection. If any of the paths in paths
are in the selection the TreeSelectionListeners are notified.
This has no effect if

paths

is null.

**Specified by:**
- removeSelectionPaths

in interface

TreeSelectionModel

**Parameters:**
- paths

- the paths to remove from the selection

---

#### public
TreePath
getSelectionPath()

Returns the first path in the selection. This is useful if there
if only one item currently selected.

**Specified by:**
- getSelectionPath

in interface

TreeSelectionModel

**Returns:**
- the first path in the selection

---

#### public
TreePath
[] getSelectionPaths()

Returns the selection.

**Specified by:**
- getSelectionPaths

in interface

TreeSelectionModel

**Returns:**
- the selection

---

#### public int getSelectionCount()

Returns the number of paths that are selected.

**Specified by:**
- getSelectionCount

in interface

TreeSelectionModel

**Returns:**
- the number of paths that are selected

---

#### public boolean isPathSelected​(
TreePath
path)

Returns true if the path,

path

,
is in the current selection.

**Specified by:**
- isPathSelected

in interface

TreeSelectionModel

**Parameters:**
- path

- the path to be loked for

**Returns:**
- whether the

path

is in the current selection

---

#### public boolean isSelectionEmpty()

Returns true if the selection is currently empty.

**Specified by:**
- isSelectionEmpty

in interface

TreeSelectionModel

**Returns:**
- whether the selection is currently empty

---

#### public void clearSelection()

Empties the current selection. If this represents a change in the
current selection, the selection listeners are notified.

**Specified by:**
- clearSelection

in interface

TreeSelectionModel

---

#### public void addTreeSelectionListener​(
TreeSelectionListener
x)

Adds x to the list of listeners that are notified each time the
set of selected TreePaths changes.

**Specified by:**
- addTreeSelectionListener

in interface

TreeSelectionModel

**Parameters:**
- x

- the new listener to be added

---

#### public void removeTreeSelectionListener​(
TreeSelectionListener
x)

Removes x from the list of listeners that are notified each time
the set of selected TreePaths changes.

**Specified by:**
- removeTreeSelectionListener

in interface

TreeSelectionModel

**Parameters:**
- x

- the listener to remove

---

#### public
TreeSelectionListener
[] getTreeSelectionListeners()

Returns an array of all the tree selection listeners
registered on this model.

**Returns:**
- all of this model's

TreeSelectionListener

s
or an empty
array if no tree selection listeners are currently registered

**See Also:**
- addTreeSelectionListener(javax.swing.event.TreeSelectionListener)

,

removeTreeSelectionListener(javax.swing.event.TreeSelectionListener)

**Since:**
- 1.4

---

#### protected void fireValueChanged​(
TreeSelectionEvent
e)

Notifies all listeners that are registered for
tree selection events on this object.

**Parameters:**
- e

- the event that characterizes the change

**See Also:**
- addTreeSelectionListener(javax.swing.event.TreeSelectionListener)

,

EventListenerList

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
upon this model.

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
with a class literal,
such as

Foo

Listener.class

.
For example, you can query a

DefaultTreeSelectionModel

m

for its tree selection listeners with the following code:

```java
TreeSelectionListener[] tsls = (TreeSelectionListener[])(m.getListeners(TreeSelectionListener.class));
```

If no such listeners exist, this method returns an empty array.

**Parameters:**
- listenerType

- the type of listeners requested

**Returns:**
- an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such
listeners have been added

**Throws:**
- ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener

**See Also:**
- getTreeSelectionListeners()

,

getPropertyChangeListeners()

**Since:**
- 1.3

**Type Parameters:**
- T

- the listener type

---

#### public int[] getSelectionRows()

Returns the selection in terms of rows. There is not
necessarily a one-to-one mapping between the

TreePath

s
returned from

getSelectionPaths

and this method. In
particular, if a

TreePath

is not viewable (the

RowMapper

returns

-1

for the row corresponding to the

TreePath

), then the corresponding row is not included
in the returned array. For example, if the selection consists
of two paths,

A

and

B

, with

A

at row

10

, and

B

not currently viewable, then this method
returns an array with the single entry

10

.

**Specified by:**
- getSelectionRows

in interface

TreeSelectionModel

**Returns:**
- the selection in terms of rows

---

#### public int getMinSelectionRow()

Returns the smallest value obtained from the RowMapper for the
current set of selected TreePaths. If nothing is selected,
or there is no RowMapper, this will return -1.

**Specified by:**
- getMinSelectionRow

in interface

TreeSelectionModel

**Returns:**
- the smallest value obtained from the RowMapper
for the current set of selected TreePaths

---

#### public int getMaxSelectionRow()

Returns the largest value obtained from the RowMapper for the
current set of selected TreePaths. If nothing is selected,
or there is no RowMapper, this will return -1.

**Specified by:**
- getMaxSelectionRow

in interface

TreeSelectionModel

**Returns:**
- the largest value obtained from the RowMapper
for the current set of selected TreePaths

---

#### public boolean isRowSelected​(int row)

Returns true if the row identified by

row

is selected.

**Specified by:**
- isRowSelected

in interface

TreeSelectionModel

**Parameters:**
- row

- row to check

**Returns:**
- whether the row is selected

---

#### public void resetRowSelection()

Updates this object's mapping from TreePath to rows. This should
be invoked when the mapping from TreePaths to integers has changed
(for example, a node has been expanded).

You do not normally have to call this, JTree and its associated
Listeners will invoke this for you. If you are implementing your own
View class, then you will have to invoke this.

This will invoke

insureRowContinuity

to make sure
the currently selected TreePaths are still valid based on the
selection mode.

**Specified by:**
- resetRowSelection

in interface

TreeSelectionModel

---

#### public int getLeadSelectionRow()

Returns the lead selection index. That is the last index that was
added.

**Specified by:**
- getLeadSelectionRow

in interface

TreeSelectionModel

**Returns:**
- the lead selection index

---

#### public
TreePath
getLeadSelectionPath()

Returns the last path that was added. This may differ from the
leadSelectionPath property maintained by the JTree.

**Specified by:**
- getLeadSelectionPath

in interface

TreeSelectionModel

**Returns:**
- the last path that was added

---

#### public void addPropertyChangeListener​(
PropertyChangeListener
listener)

Adds a PropertyChangeListener to the listener list.
The listener is registered for all properties.

A PropertyChangeEvent will get fired when the selection mode
changes.

**Specified by:**
- addPropertyChangeListener

in interface

TreeSelectionModel

**Parameters:**
- listener

- the PropertyChangeListener to be added

---

#### public void removePropertyChangeListener​(
PropertyChangeListener
listener)

Removes a PropertyChangeListener from the listener list.
This removes a PropertyChangeListener that was registered
for all properties.

**Specified by:**
- removePropertyChangeListener

in interface

TreeSelectionModel

**Parameters:**
- listener

- the PropertyChangeListener to be removed

---

#### public
PropertyChangeListener
[] getPropertyChangeListeners()

Returns an array of all the property change listeners
registered on this

DefaultTreeSelectionModel

.

**Returns:**
- all of this model's

PropertyChangeListener

s
or an empty
array if no property change listeners are currently registered

**See Also:**
- addPropertyChangeListener(java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

**Since:**
- 1.4

---

#### protected void insureRowContinuity()

Makes sure the currently selected

TreePath

s are valid
for the current selection mode.
If the selection mode is

CONTIGUOUS_TREE_SELECTION

and a

RowMapper

exists, this will make sure all
the rows are contiguous, that is, when sorted all the rows are
in order with no gaps.
If the selection isn't contiguous, the selection is
reset to contain the first set, when sorted, of contiguous rows.

If the selection mode is

SINGLE_TREE_SELECTION

and
more than one TreePath is selected, the selection is reset to
contain the first path currently selected.

---

#### protected boolean arePathsContiguous​(
TreePath
[] paths)

Returns true if the paths are contiguous,
or this object has no RowMapper.

**Parameters:**
- paths

- array of paths to check

**Returns:**
- whether the paths are contiguous, or this object has no RowMapper

---

#### protected boolean canPathsBeAdded​(
TreePath
[] paths)

Used to test if a particular set of

TreePath

s can
be added. This will return true if

paths

is null (or
empty), or this object has no RowMapper, or nothing is currently selected,
or the selection mode is

DISCONTIGUOUS_TREE_SELECTION

, or
adding the paths to the current selection still results in a
contiguous set of

TreePath

s.

**Parameters:**
- paths

- array of

TreePaths

to check

**Returns:**
- whether the particular set of

TreePaths

can be added

---

#### protected boolean canPathsBeRemoved​(
TreePath
[] paths)

Returns true if the paths can be removed without breaking the
continuity of the model.
This is rather expensive.

**Parameters:**
- paths

- array of

TreePath

to check

**Returns:**
- whether the paths can be removed without breaking the
continuity of the model

---

#### @Deprecated

protected void notifyPathChange​(
Vector
<?> changedPaths,

TreePath
oldLeadSelection)

Notifies listeners of a change in path. changePaths should contain
instances of PathPlaceHolder.

**Parameters:**
- changedPaths

- the vector of the changed paths
- oldLeadSelection

- the old selection path

---

#### protected void updateLeadIndex()

Updates the leadIndex instance variable.

---

#### protected void insureUniqueness()

This method is obsolete and its implementation is now a noop. It's
still called by setSelectionPaths and addSelectionPaths, but only
for backwards compatibility.

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
- a String representation of this object

---

#### public
Object
clone()
throws
CloneNotSupportedException

Returns a clone of this object with the same selection.
This method does not duplicate
selection listeners and property listeners.

**Overrides:**
- clone

in class

Object

**Returns:**
- a clone of this instance.

**Throws:**
- CloneNotSupportedException

- never thrown by instances of
this class

**See Also:**
- Cloneable

---

### Additional Sections

#### Class DefaultTreeSelectionModel

java.lang.Object

- javax.swing.tree.DefaultTreeSelectionModel

javax.swing.tree.DefaultTreeSelectionModel

**All Implemented Interfaces:** Serializable

,

Cloneable

,

TreeSelectionModel

**Direct Known Subclasses:** JTree.EmptySelectionModel

```java
public class
DefaultTreeSelectionModel

extends
Object

implements
Cloneable
,
Serializable
,
TreeSelectionModel
```

Default implementation of TreeSelectionModel. Listeners are notified
whenever
the paths in the selection change, not the rows. In order
to be able to track row changes you may wish to become a listener
for expansion events on the tree and test for changes from there.

resetRowSelection is called from any of the methods that update
the selected paths. If you subclass any of these methods to
filter what is allowed to be selected, be sure and message

resetRowSelection

if you do not message super.

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

**See Also:** JTree

,

Serialized Form

public class

DefaultTreeSelectionModel

extends

Object

implements

Cloneable

,

Serializable

,

TreeSelectionModel

Default implementation of TreeSelectionModel. Listeners are notified
whenever
the paths in the selection change, not the rows. In order
to be able to track row changes you may wish to become a listener
for expansion events on the tree and test for changes from there.

resetRowSelection is called from any of the methods that update
the selected paths. If you subclass any of these methods to
filter what is allowed to be selected, be sure and message

resetRowSelection

if you do not message super.

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

resetRowSelection is called from any of the methods that update
the selected paths. If you subclass any of these methods to
filter what is allowed to be selected, be sure and message

resetRowSelection

if you do not message super.

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

protected

SwingPropertyChangeSupport

changeSupport

Used to messaged registered listeners.

protected int

leadIndex

Index of the lead path in selection.

protected

TreePath

leadPath

Last path that was added.

protected int

leadRow

Lead row.

protected

EventListenerList

listenerList

Event listener list.

protected

DefaultListSelectionModel

listSelectionModel

Handles maintaining the list selection model.

protected

RowMapper

rowMapper

Provides a row for a given path.

protected

TreePath

[]

selection

Paths that are currently selected.

static

String

SELECTION_MODE_PROPERTY

Property name for selectionMode.

protected int

selectionMode

Mode for the selection, will be either SINGLE_TREE_SELECTION,
CONTIGUOUS_TREE_SELECTION or DISCONTIGUOUS_TREE_SELECTION.

- Fields declared in interface javax.swing.tree.

TreeSelectionModel

CONTIGUOUS_TREE_SELECTION

,

DISCONTIGUOUS_TREE_SELECTION

,

SINGLE_TREE_SELECTION

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DefaultTreeSelectionModel

()

Creates a new instance of DefaultTreeSelectionModel that is
empty, with a selection mode of DISCONTIGUOUS_TREE_SELECTION.

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

addPropertyChangeListener

​(

PropertyChangeListener

listener)

Adds a PropertyChangeListener to the listener list.

void

addSelectionPath

​(

TreePath

path)

Adds path to the current selection.

void

addSelectionPaths

​(

TreePath

[] paths)

Adds paths to the current selection.

void

addTreeSelectionListener

​(

TreeSelectionListener

x)

Adds x to the list of listeners that are notified each time the
set of selected TreePaths changes.

protected boolean

arePathsContiguous

​(

TreePath

[] paths)

Returns true if the paths are contiguous,
or this object has no RowMapper.

protected boolean

canPathsBeAdded

​(

TreePath

[] paths)

Used to test if a particular set of

TreePath

s can
be added.

protected boolean

canPathsBeRemoved

​(

TreePath

[] paths)

Returns true if the paths can be removed without breaking the
continuity of the model.

void

clearSelection

()

Empties the current selection.

Object

clone

()

Returns a clone of this object with the same selection.

protected void

fireValueChanged

​(

TreeSelectionEvent

e)

Notifies all listeners that are registered for
tree selection events on this object.

TreePath

getLeadSelectionPath

()

Returns the last path that was added.

int

getLeadSelectionRow

()

Returns the lead selection index.

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
upon this model.

int

getMaxSelectionRow

()

Returns the largest value obtained from the RowMapper for the
current set of selected TreePaths.

int

getMinSelectionRow

()

Returns the smallest value obtained from the RowMapper for the
current set of selected TreePaths.

PropertyChangeListener

[]

getPropertyChangeListeners

()

Returns an array of all the property change listeners
registered on this

DefaultTreeSelectionModel

.

RowMapper

getRowMapper

()

Returns the RowMapper instance that is able to map a TreePath to a
row.

int

getSelectionCount

()

Returns the number of paths that are selected.

int

getSelectionMode

()

Returns the selection mode, one of

SINGLE_TREE_SELECTION

,

DISCONTIGUOUS_TREE_SELECTION

or

CONTIGUOUS_TREE_SELECTION

.

TreePath

getSelectionPath

()

Returns the first path in the selection.

TreePath

[]

getSelectionPaths

()

Returns the selection.

int[]

getSelectionRows

()

Returns the selection in terms of rows.

TreeSelectionListener

[]

getTreeSelectionListeners

()

Returns an array of all the tree selection listeners
registered on this model.

protected void

insureRowContinuity

()

Makes sure the currently selected

TreePath

s are valid
for the current selection mode.

protected void

insureUniqueness

()

This method is obsolete and its implementation is now a noop.

boolean

isPathSelected

​(

TreePath

path)

Returns true if the path,

path

,
is in the current selection.

boolean

isRowSelected

​(int row)

Returns true if the row identified by

row

is selected.

boolean

isSelectionEmpty

()

Returns true if the selection is currently empty.

protected void

notifyPathChange

​(

Vector

<?> changedPaths,

TreePath

oldLeadSelection)

Deprecated.

As of JDK version 1.7

void

removePropertyChangeListener

​(

PropertyChangeListener

listener)

Removes a PropertyChangeListener from the listener list.

void

removeSelectionPath

​(

TreePath

path)

Removes path from the selection.

void

removeSelectionPaths

​(

TreePath

[] paths)

Removes paths from the selection.

void

removeTreeSelectionListener

​(

TreeSelectionListener

x)

Removes x from the list of listeners that are notified each time
the set of selected TreePaths changes.

void

resetRowSelection

()

Updates this object's mapping from TreePath to rows.

void

setRowMapper

​(

RowMapper

newMapper)

Sets the RowMapper instance.

void

setSelectionMode

​(int mode)

Sets the selection model, which must be one of SINGLE_TREE_SELECTION,
CONTIGUOUS_TREE_SELECTION or DISCONTIGUOUS_TREE_SELECTION.

void

setSelectionPath

​(

TreePath

path)

Sets the selection to path.

void

setSelectionPaths

​(

TreePath

[] pPaths)

Sets the selection.

String

toString

()

Returns a string that displays and identifies this
object's properties.

protected void

updateLeadIndex

()

Updates the leadIndex instance variable.

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

Field Summary

Fields

Modifier and Type

Field

Description

protected

SwingPropertyChangeSupport

changeSupport

Used to messaged registered listeners.

protected int

leadIndex

Index of the lead path in selection.

protected

TreePath

leadPath

Last path that was added.

protected int

leadRow

Lead row.

protected

EventListenerList

listenerList

Event listener list.

protected

DefaultListSelectionModel

listSelectionModel

Handles maintaining the list selection model.

protected

RowMapper

rowMapper

Provides a row for a given path.

protected

TreePath

[]

selection

Paths that are currently selected.

static

String

SELECTION_MODE_PROPERTY

Property name for selectionMode.

protected int

selectionMode

Mode for the selection, will be either SINGLE_TREE_SELECTION,
CONTIGUOUS_TREE_SELECTION or DISCONTIGUOUS_TREE_SELECTION.

- Fields declared in interface javax.swing.tree.

TreeSelectionModel

CONTIGUOUS_TREE_SELECTION

,

DISCONTIGUOUS_TREE_SELECTION

,

SINGLE_TREE_SELECTION

---

#### Field Summary

Used to messaged registered listeners.

Index of the lead path in selection.

Last path that was added.

Lead row.

Event listener list.

Handles maintaining the list selection model.

Provides a row for a given path.

Paths that are currently selected.

Property name for selectionMode.

Mode for the selection, will be either SINGLE_TREE_SELECTION,
CONTIGUOUS_TREE_SELECTION or DISCONTIGUOUS_TREE_SELECTION.

Fields declared in interface javax.swing.tree.

TreeSelectionModel

CONTIGUOUS_TREE_SELECTION

,

DISCONTIGUOUS_TREE_SELECTION

,

SINGLE_TREE_SELECTION

---

#### Fields declared in interface javax.swing.tree. TreeSelectionModel

Constructor Summary

Constructors

Constructor

Description

DefaultTreeSelectionModel

()

Creates a new instance of DefaultTreeSelectionModel that is
empty, with a selection mode of DISCONTIGUOUS_TREE_SELECTION.

---

#### Constructor Summary

Creates a new instance of DefaultTreeSelectionModel that is
empty, with a selection mode of DISCONTIGUOUS_TREE_SELECTION.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

addPropertyChangeListener

​(

PropertyChangeListener

listener)

Adds a PropertyChangeListener to the listener list.

void

addSelectionPath

​(

TreePath

path)

Adds path to the current selection.

void

addSelectionPaths

​(

TreePath

[] paths)

Adds paths to the current selection.

void

addTreeSelectionListener

​(

TreeSelectionListener

x)

Adds x to the list of listeners that are notified each time the
set of selected TreePaths changes.

protected boolean

arePathsContiguous

​(

TreePath

[] paths)

Returns true if the paths are contiguous,
or this object has no RowMapper.

protected boolean

canPathsBeAdded

​(

TreePath

[] paths)

Used to test if a particular set of

TreePath

s can
be added.

protected boolean

canPathsBeRemoved

​(

TreePath

[] paths)

Returns true if the paths can be removed without breaking the
continuity of the model.

void

clearSelection

()

Empties the current selection.

Object

clone

()

Returns a clone of this object with the same selection.

protected void

fireValueChanged

​(

TreeSelectionEvent

e)

Notifies all listeners that are registered for
tree selection events on this object.

TreePath

getLeadSelectionPath

()

Returns the last path that was added.

int

getLeadSelectionRow

()

Returns the lead selection index.

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
upon this model.

int

getMaxSelectionRow

()

Returns the largest value obtained from the RowMapper for the
current set of selected TreePaths.

int

getMinSelectionRow

()

Returns the smallest value obtained from the RowMapper for the
current set of selected TreePaths.

PropertyChangeListener

[]

getPropertyChangeListeners

()

Returns an array of all the property change listeners
registered on this

DefaultTreeSelectionModel

.

RowMapper

getRowMapper

()

Returns the RowMapper instance that is able to map a TreePath to a
row.

int

getSelectionCount

()

Returns the number of paths that are selected.

int

getSelectionMode

()

Returns the selection mode, one of

SINGLE_TREE_SELECTION

,

DISCONTIGUOUS_TREE_SELECTION

or

CONTIGUOUS_TREE_SELECTION

.

TreePath

getSelectionPath

()

Returns the first path in the selection.

TreePath

[]

getSelectionPaths

()

Returns the selection.

int[]

getSelectionRows

()

Returns the selection in terms of rows.

TreeSelectionListener

[]

getTreeSelectionListeners

()

Returns an array of all the tree selection listeners
registered on this model.

protected void

insureRowContinuity

()

Makes sure the currently selected

TreePath

s are valid
for the current selection mode.

protected void

insureUniqueness

()

This method is obsolete and its implementation is now a noop.

boolean

isPathSelected

​(

TreePath

path)

Returns true if the path,

path

,
is in the current selection.

boolean

isRowSelected

​(int row)

Returns true if the row identified by

row

is selected.

boolean

isSelectionEmpty

()

Returns true if the selection is currently empty.

protected void

notifyPathChange

​(

Vector

<?> changedPaths,

TreePath

oldLeadSelection)

Deprecated.

As of JDK version 1.7

void

removePropertyChangeListener

​(

PropertyChangeListener

listener)

Removes a PropertyChangeListener from the listener list.

void

removeSelectionPath

​(

TreePath

path)

Removes path from the selection.

void

removeSelectionPaths

​(

TreePath

[] paths)

Removes paths from the selection.

void

removeTreeSelectionListener

​(

TreeSelectionListener

x)

Removes x from the list of listeners that are notified each time
the set of selected TreePaths changes.

void

resetRowSelection

()

Updates this object's mapping from TreePath to rows.

void

setRowMapper

​(

RowMapper

newMapper)

Sets the RowMapper instance.

void

setSelectionMode

​(int mode)

Sets the selection model, which must be one of SINGLE_TREE_SELECTION,
CONTIGUOUS_TREE_SELECTION or DISCONTIGUOUS_TREE_SELECTION.

void

setSelectionPath

​(

TreePath

path)

Sets the selection to path.

void

setSelectionPaths

​(

TreePath

[] pPaths)

Sets the selection.

String

toString

()

Returns a string that displays and identifies this
object's properties.

protected void

updateLeadIndex

()

Updates the leadIndex instance variable.

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

---

#### Method Summary

Adds a PropertyChangeListener to the listener list.

Adds path to the current selection.

Adds paths to the current selection.

Adds x to the list of listeners that are notified each time the
set of selected TreePaths changes.

Returns true if the paths are contiguous,
or this object has no RowMapper.

Used to test if a particular set of

TreePath

s can
be added.

Returns true if the paths can be removed without breaking the
continuity of the model.

Empties the current selection.

Returns a clone of this object with the same selection.

Notifies all listeners that are registered for
tree selection events on this object.

Returns the last path that was added.

Returns the lead selection index.

Returns an array of all the objects currently registered
as

Foo

Listener

s
upon this model.

Returns the largest value obtained from the RowMapper for the
current set of selected TreePaths.

Returns the smallest value obtained from the RowMapper for the
current set of selected TreePaths.

Returns an array of all the property change listeners
registered on this

DefaultTreeSelectionModel

.

Returns the RowMapper instance that is able to map a TreePath to a
row.

Returns the number of paths that are selected.

Returns the selection mode, one of

SINGLE_TREE_SELECTION

,

DISCONTIGUOUS_TREE_SELECTION

or

CONTIGUOUS_TREE_SELECTION

.

Returns the first path in the selection.

Returns the selection.

Returns the selection in terms of rows.

Returns an array of all the tree selection listeners
registered on this model.

Makes sure the currently selected

TreePath

s are valid
for the current selection mode.

This method is obsolete and its implementation is now a noop.

Returns true if the path,

path

,
is in the current selection.

Returns true if the row identified by

row

is selected.

Returns true if the selection is currently empty.

Deprecated.

As of JDK version 1.7

Removes a PropertyChangeListener from the listener list.

Removes path from the selection.

Removes paths from the selection.

Removes x from the list of listeners that are notified each time
the set of selected TreePaths changes.

Updates this object's mapping from TreePath to rows.

Sets the RowMapper instance.

Sets the selection model, which must be one of SINGLE_TREE_SELECTION,
CONTIGUOUS_TREE_SELECTION or DISCONTIGUOUS_TREE_SELECTION.

Sets the selection to path.

Sets the selection.

Returns a string that displays and identifies this
object's properties.

Updates the leadIndex instance variable.

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

============ FIELD DETAIL ===========

- Field Detail

- SELECTION_MODE_PROPERTY

```java
public static final
String
SELECTION_MODE_PROPERTY
```

Property name for selectionMode.

**See Also:** Constant Field Values

- changeSupport

```java
protected
SwingPropertyChangeSupport
changeSupport
```

Used to messaged registered listeners.

- selection

```java
protected
TreePath
[] selection
```

Paths that are currently selected. Will be null if nothing is
currently selected.

- listenerList

```java
protected
EventListenerList
listenerList
```

Event listener list.

- rowMapper

```java
protected transient
RowMapper
rowMapper
```

Provides a row for a given path.

- listSelectionModel

```java
protected
DefaultListSelectionModel
listSelectionModel
```

Handles maintaining the list selection model. The RowMapper is used
to map from a TreePath to a row, and the value is then placed here.

- selectionMode

```java
protected int selectionMode
```

Mode for the selection, will be either SINGLE_TREE_SELECTION,
CONTIGUOUS_TREE_SELECTION or DISCONTIGUOUS_TREE_SELECTION.

- leadPath

```java
protected
TreePath
leadPath
```

Last path that was added.

- leadIndex

```java
protected int leadIndex
```

Index of the lead path in selection.

- leadRow

```java
protected int leadRow
```

Lead row.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DefaultTreeSelectionModel

```java
public DefaultTreeSelectionModel()
```

Creates a new instance of DefaultTreeSelectionModel that is
empty, with a selection mode of DISCONTIGUOUS_TREE_SELECTION.

============ METHOD DETAIL ==========

- Method Detail

- setRowMapper

```java
public void setRowMapper​(
RowMapper
newMapper)
```

Sets the RowMapper instance. This instance is used to determine
the row for a particular TreePath.

**Specified by:** setRowMapper

in interface

TreeSelectionModel
**Parameters:** newMapper

- RowMapper to be set

- getRowMapper

```java
public
RowMapper
getRowMapper()
```

Returns the RowMapper instance that is able to map a TreePath to a
row.

**Specified by:** getRowMapper

in interface

TreeSelectionModel
**Returns:** the RowMapper instance that is able to map a TreePath
to a row

- setSelectionMode

```java
public void setSelectionMode​(int mode)
```

Sets the selection model, which must be one of SINGLE_TREE_SELECTION,
CONTIGUOUS_TREE_SELECTION or DISCONTIGUOUS_TREE_SELECTION. If mode
is not one of the defined value,

DISCONTIGUOUS_TREE_SELECTION

is assumed.

This may change the selection if the current selection is not valid
for the new mode. For example, if three TreePaths are
selected when the mode is changed to

SINGLE_TREE_SELECTION

,
only one TreePath will remain selected. It is up to the particular
implementation to decide what TreePath remains selected.

Setting the mode to something other than the defined types will
result in the mode becoming

DISCONTIGUOUS_TREE_SELECTION

.

**Specified by:** setSelectionMode

in interface

TreeSelectionModel
**Parameters:** mode

- selection mode to be set

- getSelectionMode

```java
public int getSelectionMode()
```

Returns the selection mode, one of

SINGLE_TREE_SELECTION

,

DISCONTIGUOUS_TREE_SELECTION

or

CONTIGUOUS_TREE_SELECTION

.

**Specified by:** getSelectionMode

in interface

TreeSelectionModel
**Returns:** the current selection mode

- setSelectionPath

```java
public void setSelectionPath​(
TreePath
path)
```

Sets the selection to path. If this represents a change, then
the TreeSelectionListeners are notified. If

path

is
null, this has the same effect as invoking

clearSelection

.

**Specified by:** setSelectionPath

in interface

TreeSelectionModel
**Parameters:** path

- new path to select

- setSelectionPaths

```java
public void setSelectionPaths​(
TreePath
[] pPaths)
```

Sets the selection. Whether the supplied paths are taken as the
new selection depends upon the selection mode. If the supplied
array is

null

, or empty, the selection is cleared. If
the selection mode is

SINGLE_TREE_SELECTION

, only the
first path in

pPaths

is used. If the selection
mode is

CONTIGUOUS_TREE_SELECTION

and the supplied paths
are not contiguous, then only the first path in

pPaths

is
used. If the selection mode is

DISCONTIGUOUS_TREE_SELECTION

, then all paths are used.

All

null

paths in

pPaths

are ignored.

If this represents a change, all registered

TreeSelectionListener

s are notified.

The lead path is set to the last unique path.

The paths returned from

getSelectionPaths

are in the same
order as those supplied to this method.

**Specified by:** setSelectionPaths

in interface

TreeSelectionModel
**Parameters:** pPaths

- the new selection

- addSelectionPath

```java
public void addSelectionPath​(
TreePath
path)
```

Adds path to the current selection. If path is not currently
in the selection the TreeSelectionListeners are notified. This has
no effect if

path

is null.

**Specified by:** addSelectionPath

in interface

TreeSelectionModel
**Parameters:** path

- the new path to add to the current selection

- addSelectionPaths

```java
public void addSelectionPaths​(
TreePath
[] paths)
```

Adds paths to the current selection. If any of the paths in
paths are not currently in the selection the TreeSelectionListeners
are notified. This has
no effect if

paths

is null.

The lead path is set to the last element in

paths

.

If the selection mode is

CONTIGUOUS_TREE_SELECTION

,
and adding the new paths would make the selection discontiguous.
Then two things can result: if the TreePaths in

paths

are contiguous, then the selection becomes these TreePaths,
otherwise the TreePaths aren't contiguous and the selection becomes
the first TreePath in

paths

.

**Specified by:** addSelectionPaths

in interface

TreeSelectionModel
**Parameters:** paths

- the new path to add to the current selection

- removeSelectionPath

```java
public void removeSelectionPath​(
TreePath
path)
```

Removes path from the selection. If path is in the selection
The TreeSelectionListeners are notified. This has no effect if

path

is null.

**Specified by:** removeSelectionPath

in interface

TreeSelectionModel
**Parameters:** path

- the path to remove from the selection

- removeSelectionPaths

```java
public void removeSelectionPaths​(
TreePath
[] paths)
```

Removes paths from the selection. If any of the paths in paths
are in the selection the TreeSelectionListeners are notified.
This has no effect if

paths

is null.

**Specified by:** removeSelectionPaths

in interface

TreeSelectionModel
**Parameters:** paths

- the paths to remove from the selection

- getSelectionPath

```java
public
TreePath
getSelectionPath()
```

Returns the first path in the selection. This is useful if there
if only one item currently selected.

**Specified by:** getSelectionPath

in interface

TreeSelectionModel
**Returns:** the first path in the selection

- getSelectionPaths

```java
public
TreePath
[] getSelectionPaths()
```

Returns the selection.

**Specified by:** getSelectionPaths

in interface

TreeSelectionModel
**Returns:** the selection

- getSelectionCount

```java
public int getSelectionCount()
```

Returns the number of paths that are selected.

**Specified by:** getSelectionCount

in interface

TreeSelectionModel
**Returns:** the number of paths that are selected

- isPathSelected

```java
public boolean isPathSelected​(
TreePath
path)
```

Returns true if the path,

path

,
is in the current selection.

**Specified by:** isPathSelected

in interface

TreeSelectionModel
**Parameters:** path

- the path to be loked for
**Returns:** whether the

path

is in the current selection

- isSelectionEmpty

```java
public boolean isSelectionEmpty()
```

Returns true if the selection is currently empty.

**Specified by:** isSelectionEmpty

in interface

TreeSelectionModel
**Returns:** whether the selection is currently empty

- clearSelection

```java
public void clearSelection()
```

Empties the current selection. If this represents a change in the
current selection, the selection listeners are notified.

**Specified by:** clearSelection

in interface

TreeSelectionModel

- addTreeSelectionListener

```java
public void addTreeSelectionListener​(
TreeSelectionListener
x)
```

Adds x to the list of listeners that are notified each time the
set of selected TreePaths changes.

**Specified by:** addTreeSelectionListener

in interface

TreeSelectionModel
**Parameters:** x

- the new listener to be added

- removeTreeSelectionListener

```java
public void removeTreeSelectionListener​(
TreeSelectionListener
x)
```

Removes x from the list of listeners that are notified each time
the set of selected TreePaths changes.

**Specified by:** removeTreeSelectionListener

in interface

TreeSelectionModel
**Parameters:** x

- the listener to remove

- getTreeSelectionListeners

```java
public
TreeSelectionListener
[] getTreeSelectionListeners()
```

Returns an array of all the tree selection listeners
registered on this model.

**Returns:** all of this model's

TreeSelectionListener

s
or an empty
array if no tree selection listeners are currently registered
**Since:** 1.4
**See Also:** addTreeSelectionListener(javax.swing.event.TreeSelectionListener)

,

removeTreeSelectionListener(javax.swing.event.TreeSelectionListener)

- fireValueChanged

```java
protected void fireValueChanged​(
TreeSelectionEvent
e)
```

Notifies all listeners that are registered for
tree selection events on this object.

**Parameters:** e

- the event that characterizes the change
**See Also:** addTreeSelectionListener(javax.swing.event.TreeSelectionListener)

,

EventListenerList

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
upon this model.

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
with a class literal,
such as

Foo

Listener.class

.
For example, you can query a

DefaultTreeSelectionModel

m

for its tree selection listeners with the following code:

```java
TreeSelectionListener[] tsls = (TreeSelectionListener[])(m.getListeners(TreeSelectionListener.class));
```

If no such listeners exist, this method returns an empty array.

**Type Parameters:** T

- the listener type
**Parameters:** listenerType

- the type of listeners requested
**Returns:** an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getTreeSelectionListeners()

,

getPropertyChangeListeners()

- getSelectionRows

```java
public int[] getSelectionRows()
```

Returns the selection in terms of rows. There is not
necessarily a one-to-one mapping between the

TreePath

s
returned from

getSelectionPaths

and this method. In
particular, if a

TreePath

is not viewable (the

RowMapper

returns

-1

for the row corresponding to the

TreePath

), then the corresponding row is not included
in the returned array. For example, if the selection consists
of two paths,

A

and

B

, with

A

at row

10

, and

B

not currently viewable, then this method
returns an array with the single entry

10

.

**Specified by:** getSelectionRows

in interface

TreeSelectionModel
**Returns:** the selection in terms of rows

- getMinSelectionRow

```java
public int getMinSelectionRow()
```

Returns the smallest value obtained from the RowMapper for the
current set of selected TreePaths. If nothing is selected,
or there is no RowMapper, this will return -1.

**Specified by:** getMinSelectionRow

in interface

TreeSelectionModel
**Returns:** the smallest value obtained from the RowMapper
for the current set of selected TreePaths

- getMaxSelectionRow

```java
public int getMaxSelectionRow()
```

Returns the largest value obtained from the RowMapper for the
current set of selected TreePaths. If nothing is selected,
or there is no RowMapper, this will return -1.

**Specified by:** getMaxSelectionRow

in interface

TreeSelectionModel
**Returns:** the largest value obtained from the RowMapper
for the current set of selected TreePaths

- isRowSelected

```java
public boolean isRowSelected​(int row)
```

Returns true if the row identified by

row

is selected.

**Specified by:** isRowSelected

in interface

TreeSelectionModel
**Parameters:** row

- row to check
**Returns:** whether the row is selected

- resetRowSelection

```java
public void resetRowSelection()
```

Updates this object's mapping from TreePath to rows. This should
be invoked when the mapping from TreePaths to integers has changed
(for example, a node has been expanded).

You do not normally have to call this, JTree and its associated
Listeners will invoke this for you. If you are implementing your own
View class, then you will have to invoke this.

This will invoke

insureRowContinuity

to make sure
the currently selected TreePaths are still valid based on the
selection mode.

**Specified by:** resetRowSelection

in interface

TreeSelectionModel

- getLeadSelectionRow

```java
public int getLeadSelectionRow()
```

Returns the lead selection index. That is the last index that was
added.

**Specified by:** getLeadSelectionRow

in interface

TreeSelectionModel
**Returns:** the lead selection index

- getLeadSelectionPath

```java
public
TreePath
getLeadSelectionPath()
```

Returns the last path that was added. This may differ from the
leadSelectionPath property maintained by the JTree.

**Specified by:** getLeadSelectionPath

in interface

TreeSelectionModel
**Returns:** the last path that was added

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list.
The listener is registered for all properties.

A PropertyChangeEvent will get fired when the selection mode
changes.

**Specified by:** addPropertyChangeListener

in interface

TreeSelectionModel
**Parameters:** listener

- the PropertyChangeListener to be added

- removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a PropertyChangeListener from the listener list.
This removes a PropertyChangeListener that was registered
for all properties.

**Specified by:** removePropertyChangeListener

in interface

TreeSelectionModel
**Parameters:** listener

- the PropertyChangeListener to be removed

- getPropertyChangeListeners

```java
public
PropertyChangeListener
[] getPropertyChangeListeners()
```

Returns an array of all the property change listeners
registered on this

DefaultTreeSelectionModel

.

**Returns:** all of this model's

PropertyChangeListener

s
or an empty
array if no property change listeners are currently registered
**Since:** 1.4
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

- insureRowContinuity

```java
protected void insureRowContinuity()
```

Makes sure the currently selected

TreePath

s are valid
for the current selection mode.
If the selection mode is

CONTIGUOUS_TREE_SELECTION

and a

RowMapper

exists, this will make sure all
the rows are contiguous, that is, when sorted all the rows are
in order with no gaps.
If the selection isn't contiguous, the selection is
reset to contain the first set, when sorted, of contiguous rows.

If the selection mode is

SINGLE_TREE_SELECTION

and
more than one TreePath is selected, the selection is reset to
contain the first path currently selected.

- arePathsContiguous

```java
protected boolean arePathsContiguous​(
TreePath
[] paths)
```

Returns true if the paths are contiguous,
or this object has no RowMapper.

**Parameters:** paths

- array of paths to check
**Returns:** whether the paths are contiguous, or this object has no RowMapper

- canPathsBeAdded

```java
protected boolean canPathsBeAdded​(
TreePath
[] paths)
```

Used to test if a particular set of

TreePath

s can
be added. This will return true if

paths

is null (or
empty), or this object has no RowMapper, or nothing is currently selected,
or the selection mode is

DISCONTIGUOUS_TREE_SELECTION

, or
adding the paths to the current selection still results in a
contiguous set of

TreePath

s.

**Parameters:** paths

- array of

TreePaths

to check
**Returns:** whether the particular set of

TreePaths

can be added

- canPathsBeRemoved

```java
protected boolean canPathsBeRemoved​(
TreePath
[] paths)
```

Returns true if the paths can be removed without breaking the
continuity of the model.
This is rather expensive.

**Parameters:** paths

- array of

TreePath

to check
**Returns:** whether the paths can be removed without breaking the
continuity of the model

- notifyPathChange

```java
@Deprecated

protected void notifyPathChange​(
Vector
<?> changedPaths,

TreePath
oldLeadSelection)
```

Deprecated.

As of JDK version 1.7

Notifies listeners of a change in path. changePaths should contain
instances of PathPlaceHolder.

**Parameters:** changedPaths

- the vector of the changed paths
**Parameters:** oldLeadSelection

- the old selection path

- updateLeadIndex

```java
protected void updateLeadIndex()
```

Updates the leadIndex instance variable.

- insureUniqueness

```java
protected void insureUniqueness()
```

This method is obsolete and its implementation is now a noop. It's
still called by setSelectionPaths and addSelectionPaths, but only
for backwards compatibility.

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
**Returns:** a String representation of this object

- clone

```java
public
Object
clone()
throws
CloneNotSupportedException
```

Returns a clone of this object with the same selection.
This method does not duplicate
selection listeners and property listeners.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** CloneNotSupportedException

- never thrown by instances of
this class
**See Also:** Cloneable

Field Detail

- SELECTION_MODE_PROPERTY

```java
public static final
String
SELECTION_MODE_PROPERTY
```

Property name for selectionMode.

**See Also:** Constant Field Values

- changeSupport

```java
protected
SwingPropertyChangeSupport
changeSupport
```

Used to messaged registered listeners.

- selection

```java
protected
TreePath
[] selection
```

Paths that are currently selected. Will be null if nothing is
currently selected.

- listenerList

```java
protected
EventListenerList
listenerList
```

Event listener list.

- rowMapper

```java
protected transient
RowMapper
rowMapper
```

Provides a row for a given path.

- listSelectionModel

```java
protected
DefaultListSelectionModel
listSelectionModel
```

Handles maintaining the list selection model. The RowMapper is used
to map from a TreePath to a row, and the value is then placed here.

- selectionMode

```java
protected int selectionMode
```

Mode for the selection, will be either SINGLE_TREE_SELECTION,
CONTIGUOUS_TREE_SELECTION or DISCONTIGUOUS_TREE_SELECTION.

- leadPath

```java
protected
TreePath
leadPath
```

Last path that was added.

- leadIndex

```java
protected int leadIndex
```

Index of the lead path in selection.

- leadRow

```java
protected int leadRow
```

Lead row.

---

#### Field Detail

SELECTION_MODE_PROPERTY

```java
public static final
String
SELECTION_MODE_PROPERTY
```

Property name for selectionMode.

**See Also:** Constant Field Values

---

#### SELECTION_MODE_PROPERTY

public static final

String

SELECTION_MODE_PROPERTY

Property name for selectionMode.

changeSupport

```java
protected
SwingPropertyChangeSupport
changeSupport
```

Used to messaged registered listeners.

---

#### changeSupport

protected

SwingPropertyChangeSupport

changeSupport

Used to messaged registered listeners.

selection

```java
protected
TreePath
[] selection
```

Paths that are currently selected. Will be null if nothing is
currently selected.

---

#### selection

protected

TreePath

[] selection

Paths that are currently selected. Will be null if nothing is
currently selected.

listenerList

```java
protected
EventListenerList
listenerList
```

Event listener list.

---

#### listenerList

protected

EventListenerList

listenerList

Event listener list.

rowMapper

```java
protected transient
RowMapper
rowMapper
```

Provides a row for a given path.

---

#### rowMapper

protected transient

RowMapper

rowMapper

Provides a row for a given path.

listSelectionModel

```java
protected
DefaultListSelectionModel
listSelectionModel
```

Handles maintaining the list selection model. The RowMapper is used
to map from a TreePath to a row, and the value is then placed here.

---

#### listSelectionModel

protected

DefaultListSelectionModel

listSelectionModel

Handles maintaining the list selection model. The RowMapper is used
to map from a TreePath to a row, and the value is then placed here.

selectionMode

```java
protected int selectionMode
```

Mode for the selection, will be either SINGLE_TREE_SELECTION,
CONTIGUOUS_TREE_SELECTION or DISCONTIGUOUS_TREE_SELECTION.

---

#### selectionMode

protected int selectionMode

Mode for the selection, will be either SINGLE_TREE_SELECTION,
CONTIGUOUS_TREE_SELECTION or DISCONTIGUOUS_TREE_SELECTION.

leadPath

```java
protected
TreePath
leadPath
```

Last path that was added.

---

#### leadPath

protected

TreePath

leadPath

Last path that was added.

leadIndex

```java
protected int leadIndex
```

Index of the lead path in selection.

---

#### leadIndex

protected int leadIndex

Index of the lead path in selection.

leadRow

```java
protected int leadRow
```

Lead row.

---

#### leadRow

protected int leadRow

Lead row.

Constructor Detail

- DefaultTreeSelectionModel

```java
public DefaultTreeSelectionModel()
```

Creates a new instance of DefaultTreeSelectionModel that is
empty, with a selection mode of DISCONTIGUOUS_TREE_SELECTION.

---

#### Constructor Detail

DefaultTreeSelectionModel

```java
public DefaultTreeSelectionModel()
```

Creates a new instance of DefaultTreeSelectionModel that is
empty, with a selection mode of DISCONTIGUOUS_TREE_SELECTION.

---

#### DefaultTreeSelectionModel

public DefaultTreeSelectionModel()

Creates a new instance of DefaultTreeSelectionModel that is
empty, with a selection mode of DISCONTIGUOUS_TREE_SELECTION.

Method Detail

- setRowMapper

```java
public void setRowMapper​(
RowMapper
newMapper)
```

Sets the RowMapper instance. This instance is used to determine
the row for a particular TreePath.

**Specified by:** setRowMapper

in interface

TreeSelectionModel
**Parameters:** newMapper

- RowMapper to be set

- getRowMapper

```java
public
RowMapper
getRowMapper()
```

Returns the RowMapper instance that is able to map a TreePath to a
row.

**Specified by:** getRowMapper

in interface

TreeSelectionModel
**Returns:** the RowMapper instance that is able to map a TreePath
to a row

- setSelectionMode

```java
public void setSelectionMode​(int mode)
```

Sets the selection model, which must be one of SINGLE_TREE_SELECTION,
CONTIGUOUS_TREE_SELECTION or DISCONTIGUOUS_TREE_SELECTION. If mode
is not one of the defined value,

DISCONTIGUOUS_TREE_SELECTION

is assumed.

This may change the selection if the current selection is not valid
for the new mode. For example, if three TreePaths are
selected when the mode is changed to

SINGLE_TREE_SELECTION

,
only one TreePath will remain selected. It is up to the particular
implementation to decide what TreePath remains selected.

Setting the mode to something other than the defined types will
result in the mode becoming

DISCONTIGUOUS_TREE_SELECTION

.

**Specified by:** setSelectionMode

in interface

TreeSelectionModel
**Parameters:** mode

- selection mode to be set

- getSelectionMode

```java
public int getSelectionMode()
```

Returns the selection mode, one of

SINGLE_TREE_SELECTION

,

DISCONTIGUOUS_TREE_SELECTION

or

CONTIGUOUS_TREE_SELECTION

.

**Specified by:** getSelectionMode

in interface

TreeSelectionModel
**Returns:** the current selection mode

- setSelectionPath

```java
public void setSelectionPath​(
TreePath
path)
```

Sets the selection to path. If this represents a change, then
the TreeSelectionListeners are notified. If

path

is
null, this has the same effect as invoking

clearSelection

.

**Specified by:** setSelectionPath

in interface

TreeSelectionModel
**Parameters:** path

- new path to select

- setSelectionPaths

```java
public void setSelectionPaths​(
TreePath
[] pPaths)
```

Sets the selection. Whether the supplied paths are taken as the
new selection depends upon the selection mode. If the supplied
array is

null

, or empty, the selection is cleared. If
the selection mode is

SINGLE_TREE_SELECTION

, only the
first path in

pPaths

is used. If the selection
mode is

CONTIGUOUS_TREE_SELECTION

and the supplied paths
are not contiguous, then only the first path in

pPaths

is
used. If the selection mode is

DISCONTIGUOUS_TREE_SELECTION

, then all paths are used.

All

null

paths in

pPaths

are ignored.

If this represents a change, all registered

TreeSelectionListener

s are notified.

The lead path is set to the last unique path.

The paths returned from

getSelectionPaths

are in the same
order as those supplied to this method.

**Specified by:** setSelectionPaths

in interface

TreeSelectionModel
**Parameters:** pPaths

- the new selection

- addSelectionPath

```java
public void addSelectionPath​(
TreePath
path)
```

Adds path to the current selection. If path is not currently
in the selection the TreeSelectionListeners are notified. This has
no effect if

path

is null.

**Specified by:** addSelectionPath

in interface

TreeSelectionModel
**Parameters:** path

- the new path to add to the current selection

- addSelectionPaths

```java
public void addSelectionPaths​(
TreePath
[] paths)
```

Adds paths to the current selection. If any of the paths in
paths are not currently in the selection the TreeSelectionListeners
are notified. This has
no effect if

paths

is null.

The lead path is set to the last element in

paths

.

If the selection mode is

CONTIGUOUS_TREE_SELECTION

,
and adding the new paths would make the selection discontiguous.
Then two things can result: if the TreePaths in

paths

are contiguous, then the selection becomes these TreePaths,
otherwise the TreePaths aren't contiguous and the selection becomes
the first TreePath in

paths

.

**Specified by:** addSelectionPaths

in interface

TreeSelectionModel
**Parameters:** paths

- the new path to add to the current selection

- removeSelectionPath

```java
public void removeSelectionPath​(
TreePath
path)
```

Removes path from the selection. If path is in the selection
The TreeSelectionListeners are notified. This has no effect if

path

is null.

**Specified by:** removeSelectionPath

in interface

TreeSelectionModel
**Parameters:** path

- the path to remove from the selection

- removeSelectionPaths

```java
public void removeSelectionPaths​(
TreePath
[] paths)
```

Removes paths from the selection. If any of the paths in paths
are in the selection the TreeSelectionListeners are notified.
This has no effect if

paths

is null.

**Specified by:** removeSelectionPaths

in interface

TreeSelectionModel
**Parameters:** paths

- the paths to remove from the selection

- getSelectionPath

```java
public
TreePath
getSelectionPath()
```

Returns the first path in the selection. This is useful if there
if only one item currently selected.

**Specified by:** getSelectionPath

in interface

TreeSelectionModel
**Returns:** the first path in the selection

- getSelectionPaths

```java
public
TreePath
[] getSelectionPaths()
```

Returns the selection.

**Specified by:** getSelectionPaths

in interface

TreeSelectionModel
**Returns:** the selection

- getSelectionCount

```java
public int getSelectionCount()
```

Returns the number of paths that are selected.

**Specified by:** getSelectionCount

in interface

TreeSelectionModel
**Returns:** the number of paths that are selected

- isPathSelected

```java
public boolean isPathSelected​(
TreePath
path)
```

Returns true if the path,

path

,
is in the current selection.

**Specified by:** isPathSelected

in interface

TreeSelectionModel
**Parameters:** path

- the path to be loked for
**Returns:** whether the

path

is in the current selection

- isSelectionEmpty

```java
public boolean isSelectionEmpty()
```

Returns true if the selection is currently empty.

**Specified by:** isSelectionEmpty

in interface

TreeSelectionModel
**Returns:** whether the selection is currently empty

- clearSelection

```java
public void clearSelection()
```

Empties the current selection. If this represents a change in the
current selection, the selection listeners are notified.

**Specified by:** clearSelection

in interface

TreeSelectionModel

- addTreeSelectionListener

```java
public void addTreeSelectionListener​(
TreeSelectionListener
x)
```

Adds x to the list of listeners that are notified each time the
set of selected TreePaths changes.

**Specified by:** addTreeSelectionListener

in interface

TreeSelectionModel
**Parameters:** x

- the new listener to be added

- removeTreeSelectionListener

```java
public void removeTreeSelectionListener​(
TreeSelectionListener
x)
```

Removes x from the list of listeners that are notified each time
the set of selected TreePaths changes.

**Specified by:** removeTreeSelectionListener

in interface

TreeSelectionModel
**Parameters:** x

- the listener to remove

- getTreeSelectionListeners

```java
public
TreeSelectionListener
[] getTreeSelectionListeners()
```

Returns an array of all the tree selection listeners
registered on this model.

**Returns:** all of this model's

TreeSelectionListener

s
or an empty
array if no tree selection listeners are currently registered
**Since:** 1.4
**See Also:** addTreeSelectionListener(javax.swing.event.TreeSelectionListener)

,

removeTreeSelectionListener(javax.swing.event.TreeSelectionListener)

- fireValueChanged

```java
protected void fireValueChanged​(
TreeSelectionEvent
e)
```

Notifies all listeners that are registered for
tree selection events on this object.

**Parameters:** e

- the event that characterizes the change
**See Also:** addTreeSelectionListener(javax.swing.event.TreeSelectionListener)

,

EventListenerList

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
upon this model.

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
with a class literal,
such as

Foo

Listener.class

.
For example, you can query a

DefaultTreeSelectionModel

m

for its tree selection listeners with the following code:

```java
TreeSelectionListener[] tsls = (TreeSelectionListener[])(m.getListeners(TreeSelectionListener.class));
```

If no such listeners exist, this method returns an empty array.

**Type Parameters:** T

- the listener type
**Parameters:** listenerType

- the type of listeners requested
**Returns:** an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getTreeSelectionListeners()

,

getPropertyChangeListeners()

- getSelectionRows

```java
public int[] getSelectionRows()
```

Returns the selection in terms of rows. There is not
necessarily a one-to-one mapping between the

TreePath

s
returned from

getSelectionPaths

and this method. In
particular, if a

TreePath

is not viewable (the

RowMapper

returns

-1

for the row corresponding to the

TreePath

), then the corresponding row is not included
in the returned array. For example, if the selection consists
of two paths,

A

and

B

, with

A

at row

10

, and

B

not currently viewable, then this method
returns an array with the single entry

10

.

**Specified by:** getSelectionRows

in interface

TreeSelectionModel
**Returns:** the selection in terms of rows

- getMinSelectionRow

```java
public int getMinSelectionRow()
```

Returns the smallest value obtained from the RowMapper for the
current set of selected TreePaths. If nothing is selected,
or there is no RowMapper, this will return -1.

**Specified by:** getMinSelectionRow

in interface

TreeSelectionModel
**Returns:** the smallest value obtained from the RowMapper
for the current set of selected TreePaths

- getMaxSelectionRow

```java
public int getMaxSelectionRow()
```

Returns the largest value obtained from the RowMapper for the
current set of selected TreePaths. If nothing is selected,
or there is no RowMapper, this will return -1.

**Specified by:** getMaxSelectionRow

in interface

TreeSelectionModel
**Returns:** the largest value obtained from the RowMapper
for the current set of selected TreePaths

- isRowSelected

```java
public boolean isRowSelected​(int row)
```

Returns true if the row identified by

row

is selected.

**Specified by:** isRowSelected

in interface

TreeSelectionModel
**Parameters:** row

- row to check
**Returns:** whether the row is selected

- resetRowSelection

```java
public void resetRowSelection()
```

Updates this object's mapping from TreePath to rows. This should
be invoked when the mapping from TreePaths to integers has changed
(for example, a node has been expanded).

You do not normally have to call this, JTree and its associated
Listeners will invoke this for you. If you are implementing your own
View class, then you will have to invoke this.

This will invoke

insureRowContinuity

to make sure
the currently selected TreePaths are still valid based on the
selection mode.

**Specified by:** resetRowSelection

in interface

TreeSelectionModel

- getLeadSelectionRow

```java
public int getLeadSelectionRow()
```

Returns the lead selection index. That is the last index that was
added.

**Specified by:** getLeadSelectionRow

in interface

TreeSelectionModel
**Returns:** the lead selection index

- getLeadSelectionPath

```java
public
TreePath
getLeadSelectionPath()
```

Returns the last path that was added. This may differ from the
leadSelectionPath property maintained by the JTree.

**Specified by:** getLeadSelectionPath

in interface

TreeSelectionModel
**Returns:** the last path that was added

- addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list.
The listener is registered for all properties.

A PropertyChangeEvent will get fired when the selection mode
changes.

**Specified by:** addPropertyChangeListener

in interface

TreeSelectionModel
**Parameters:** listener

- the PropertyChangeListener to be added

- removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a PropertyChangeListener from the listener list.
This removes a PropertyChangeListener that was registered
for all properties.

**Specified by:** removePropertyChangeListener

in interface

TreeSelectionModel
**Parameters:** listener

- the PropertyChangeListener to be removed

- getPropertyChangeListeners

```java
public
PropertyChangeListener
[] getPropertyChangeListeners()
```

Returns an array of all the property change listeners
registered on this

DefaultTreeSelectionModel

.

**Returns:** all of this model's

PropertyChangeListener

s
or an empty
array if no property change listeners are currently registered
**Since:** 1.4
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

- insureRowContinuity

```java
protected void insureRowContinuity()
```

Makes sure the currently selected

TreePath

s are valid
for the current selection mode.
If the selection mode is

CONTIGUOUS_TREE_SELECTION

and a

RowMapper

exists, this will make sure all
the rows are contiguous, that is, when sorted all the rows are
in order with no gaps.
If the selection isn't contiguous, the selection is
reset to contain the first set, when sorted, of contiguous rows.

If the selection mode is

SINGLE_TREE_SELECTION

and
more than one TreePath is selected, the selection is reset to
contain the first path currently selected.

- arePathsContiguous

```java
protected boolean arePathsContiguous​(
TreePath
[] paths)
```

Returns true if the paths are contiguous,
or this object has no RowMapper.

**Parameters:** paths

- array of paths to check
**Returns:** whether the paths are contiguous, or this object has no RowMapper

- canPathsBeAdded

```java
protected boolean canPathsBeAdded​(
TreePath
[] paths)
```

Used to test if a particular set of

TreePath

s can
be added. This will return true if

paths

is null (or
empty), or this object has no RowMapper, or nothing is currently selected,
or the selection mode is

DISCONTIGUOUS_TREE_SELECTION

, or
adding the paths to the current selection still results in a
contiguous set of

TreePath

s.

**Parameters:** paths

- array of

TreePaths

to check
**Returns:** whether the particular set of

TreePaths

can be added

- canPathsBeRemoved

```java
protected boolean canPathsBeRemoved​(
TreePath
[] paths)
```

Returns true if the paths can be removed without breaking the
continuity of the model.
This is rather expensive.

**Parameters:** paths

- array of

TreePath

to check
**Returns:** whether the paths can be removed without breaking the
continuity of the model

- notifyPathChange

```java
@Deprecated

protected void notifyPathChange​(
Vector
<?> changedPaths,

TreePath
oldLeadSelection)
```

Deprecated.

As of JDK version 1.7

Notifies listeners of a change in path. changePaths should contain
instances of PathPlaceHolder.

**Parameters:** changedPaths

- the vector of the changed paths
**Parameters:** oldLeadSelection

- the old selection path

- updateLeadIndex

```java
protected void updateLeadIndex()
```

Updates the leadIndex instance variable.

- insureUniqueness

```java
protected void insureUniqueness()
```

This method is obsolete and its implementation is now a noop. It's
still called by setSelectionPaths and addSelectionPaths, but only
for backwards compatibility.

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
**Returns:** a String representation of this object

- clone

```java
public
Object
clone()
throws
CloneNotSupportedException
```

Returns a clone of this object with the same selection.
This method does not duplicate
selection listeners and property listeners.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** CloneNotSupportedException

- never thrown by instances of
this class
**See Also:** Cloneable

---

#### Method Detail

setRowMapper

```java
public void setRowMapper​(
RowMapper
newMapper)
```

Sets the RowMapper instance. This instance is used to determine
the row for a particular TreePath.

**Specified by:** setRowMapper

in interface

TreeSelectionModel
**Parameters:** newMapper

- RowMapper to be set

---

#### setRowMapper

public void setRowMapper​(

RowMapper

newMapper)

Sets the RowMapper instance. This instance is used to determine
the row for a particular TreePath.

getRowMapper

```java
public
RowMapper
getRowMapper()
```

Returns the RowMapper instance that is able to map a TreePath to a
row.

**Specified by:** getRowMapper

in interface

TreeSelectionModel
**Returns:** the RowMapper instance that is able to map a TreePath
to a row

---

#### getRowMapper

public

RowMapper

getRowMapper()

Returns the RowMapper instance that is able to map a TreePath to a
row.

setSelectionMode

```java
public void setSelectionMode​(int mode)
```

Sets the selection model, which must be one of SINGLE_TREE_SELECTION,
CONTIGUOUS_TREE_SELECTION or DISCONTIGUOUS_TREE_SELECTION. If mode
is not one of the defined value,

DISCONTIGUOUS_TREE_SELECTION

is assumed.

This may change the selection if the current selection is not valid
for the new mode. For example, if three TreePaths are
selected when the mode is changed to

SINGLE_TREE_SELECTION

,
only one TreePath will remain selected. It is up to the particular
implementation to decide what TreePath remains selected.

Setting the mode to something other than the defined types will
result in the mode becoming

DISCONTIGUOUS_TREE_SELECTION

.

**Specified by:** setSelectionMode

in interface

TreeSelectionModel
**Parameters:** mode

- selection mode to be set

---

#### setSelectionMode

public void setSelectionMode​(int mode)

Sets the selection model, which must be one of SINGLE_TREE_SELECTION,
CONTIGUOUS_TREE_SELECTION or DISCONTIGUOUS_TREE_SELECTION. If mode
is not one of the defined value,

DISCONTIGUOUS_TREE_SELECTION

is assumed.

This may change the selection if the current selection is not valid
for the new mode. For example, if three TreePaths are
selected when the mode is changed to

SINGLE_TREE_SELECTION

,
only one TreePath will remain selected. It is up to the particular
implementation to decide what TreePath remains selected.

Setting the mode to something other than the defined types will
result in the mode becoming

DISCONTIGUOUS_TREE_SELECTION

.

This may change the selection if the current selection is not valid
for the new mode. For example, if three TreePaths are
selected when the mode is changed to

SINGLE_TREE_SELECTION

,
only one TreePath will remain selected. It is up to the particular
implementation to decide what TreePath remains selected.

Setting the mode to something other than the defined types will
result in the mode becoming

DISCONTIGUOUS_TREE_SELECTION

.

Setting the mode to something other than the defined types will
result in the mode becoming

DISCONTIGUOUS_TREE_SELECTION

.

getSelectionMode

```java
public int getSelectionMode()
```

Returns the selection mode, one of

SINGLE_TREE_SELECTION

,

DISCONTIGUOUS_TREE_SELECTION

or

CONTIGUOUS_TREE_SELECTION

.

**Specified by:** getSelectionMode

in interface

TreeSelectionModel
**Returns:** the current selection mode

---

#### getSelectionMode

public int getSelectionMode()

Returns the selection mode, one of

SINGLE_TREE_SELECTION

,

DISCONTIGUOUS_TREE_SELECTION

or

CONTIGUOUS_TREE_SELECTION

.

setSelectionPath

```java
public void setSelectionPath​(
TreePath
path)
```

Sets the selection to path. If this represents a change, then
the TreeSelectionListeners are notified. If

path

is
null, this has the same effect as invoking

clearSelection

.

**Specified by:** setSelectionPath

in interface

TreeSelectionModel
**Parameters:** path

- new path to select

---

#### setSelectionPath

public void setSelectionPath​(

TreePath

path)

Sets the selection to path. If this represents a change, then
the TreeSelectionListeners are notified. If

path

is
null, this has the same effect as invoking

clearSelection

.

setSelectionPaths

```java
public void setSelectionPaths​(
TreePath
[] pPaths)
```

Sets the selection. Whether the supplied paths are taken as the
new selection depends upon the selection mode. If the supplied
array is

null

, or empty, the selection is cleared. If
the selection mode is

SINGLE_TREE_SELECTION

, only the
first path in

pPaths

is used. If the selection
mode is

CONTIGUOUS_TREE_SELECTION

and the supplied paths
are not contiguous, then only the first path in

pPaths

is
used. If the selection mode is

DISCONTIGUOUS_TREE_SELECTION

, then all paths are used.

All

null

paths in

pPaths

are ignored.

If this represents a change, all registered

TreeSelectionListener

s are notified.

The lead path is set to the last unique path.

The paths returned from

getSelectionPaths

are in the same
order as those supplied to this method.

**Specified by:** setSelectionPaths

in interface

TreeSelectionModel
**Parameters:** pPaths

- the new selection

---

#### setSelectionPaths

public void setSelectionPaths​(

TreePath

[] pPaths)

Sets the selection. Whether the supplied paths are taken as the
new selection depends upon the selection mode. If the supplied
array is

null

, or empty, the selection is cleared. If
the selection mode is

SINGLE_TREE_SELECTION

, only the
first path in

pPaths

is used. If the selection
mode is

CONTIGUOUS_TREE_SELECTION

and the supplied paths
are not contiguous, then only the first path in

pPaths

is
used. If the selection mode is

DISCONTIGUOUS_TREE_SELECTION

, then all paths are used.

All

null

paths in

pPaths

are ignored.

If this represents a change, all registered

TreeSelectionListener

s are notified.

The lead path is set to the last unique path.

The paths returned from

getSelectionPaths

are in the same
order as those supplied to this method.

All

null

paths in

pPaths

are ignored.

If this represents a change, all registered

TreeSelectionListener

s are notified.

The lead path is set to the last unique path.

The paths returned from

getSelectionPaths

are in the same
order as those supplied to this method.

If this represents a change, all registered

TreeSelectionListener

s are notified.

The lead path is set to the last unique path.

The paths returned from

getSelectionPaths

are in the same
order as those supplied to this method.

The lead path is set to the last unique path.

The paths returned from

getSelectionPaths

are in the same
order as those supplied to this method.

The paths returned from

getSelectionPaths

are in the same
order as those supplied to this method.

addSelectionPath

```java
public void addSelectionPath​(
TreePath
path)
```

Adds path to the current selection. If path is not currently
in the selection the TreeSelectionListeners are notified. This has
no effect if

path

is null.

**Specified by:** addSelectionPath

in interface

TreeSelectionModel
**Parameters:** path

- the new path to add to the current selection

---

#### addSelectionPath

public void addSelectionPath​(

TreePath

path)

Adds path to the current selection. If path is not currently
in the selection the TreeSelectionListeners are notified. This has
no effect if

path

is null.

addSelectionPaths

```java
public void addSelectionPaths​(
TreePath
[] paths)
```

Adds paths to the current selection. If any of the paths in
paths are not currently in the selection the TreeSelectionListeners
are notified. This has
no effect if

paths

is null.

The lead path is set to the last element in

paths

.

If the selection mode is

CONTIGUOUS_TREE_SELECTION

,
and adding the new paths would make the selection discontiguous.
Then two things can result: if the TreePaths in

paths

are contiguous, then the selection becomes these TreePaths,
otherwise the TreePaths aren't contiguous and the selection becomes
the first TreePath in

paths

.

**Specified by:** addSelectionPaths

in interface

TreeSelectionModel
**Parameters:** paths

- the new path to add to the current selection

---

#### addSelectionPaths

public void addSelectionPaths​(

TreePath

[] paths)

Adds paths to the current selection. If any of the paths in
paths are not currently in the selection the TreeSelectionListeners
are notified. This has
no effect if

paths

is null.

The lead path is set to the last element in

paths

.

If the selection mode is

CONTIGUOUS_TREE_SELECTION

,
and adding the new paths would make the selection discontiguous.
Then two things can result: if the TreePaths in

paths

are contiguous, then the selection becomes these TreePaths,
otherwise the TreePaths aren't contiguous and the selection becomes
the first TreePath in

paths

.

The lead path is set to the last element in

paths

.

If the selection mode is

CONTIGUOUS_TREE_SELECTION

,
and adding the new paths would make the selection discontiguous.
Then two things can result: if the TreePaths in

paths

are contiguous, then the selection becomes these TreePaths,
otherwise the TreePaths aren't contiguous and the selection becomes
the first TreePath in

paths

.

If the selection mode is

CONTIGUOUS_TREE_SELECTION

,
and adding the new paths would make the selection discontiguous.
Then two things can result: if the TreePaths in

paths

are contiguous, then the selection becomes these TreePaths,
otherwise the TreePaths aren't contiguous and the selection becomes
the first TreePath in

paths

.

removeSelectionPath

```java
public void removeSelectionPath​(
TreePath
path)
```

Removes path from the selection. If path is in the selection
The TreeSelectionListeners are notified. This has no effect if

path

is null.

**Specified by:** removeSelectionPath

in interface

TreeSelectionModel
**Parameters:** path

- the path to remove from the selection

---

#### removeSelectionPath

public void removeSelectionPath​(

TreePath

path)

Removes path from the selection. If path is in the selection
The TreeSelectionListeners are notified. This has no effect if

path

is null.

removeSelectionPaths

```java
public void removeSelectionPaths​(
TreePath
[] paths)
```

Removes paths from the selection. If any of the paths in paths
are in the selection the TreeSelectionListeners are notified.
This has no effect if

paths

is null.

**Specified by:** removeSelectionPaths

in interface

TreeSelectionModel
**Parameters:** paths

- the paths to remove from the selection

---

#### removeSelectionPaths

public void removeSelectionPaths​(

TreePath

[] paths)

Removes paths from the selection. If any of the paths in paths
are in the selection the TreeSelectionListeners are notified.
This has no effect if

paths

is null.

getSelectionPath

```java
public
TreePath
getSelectionPath()
```

Returns the first path in the selection. This is useful if there
if only one item currently selected.

**Specified by:** getSelectionPath

in interface

TreeSelectionModel
**Returns:** the first path in the selection

---

#### getSelectionPath

public

TreePath

getSelectionPath()

Returns the first path in the selection. This is useful if there
if only one item currently selected.

getSelectionPaths

```java
public
TreePath
[] getSelectionPaths()
```

Returns the selection.

**Specified by:** getSelectionPaths

in interface

TreeSelectionModel
**Returns:** the selection

---

#### getSelectionPaths

public

TreePath

[] getSelectionPaths()

Returns the selection.

getSelectionCount

```java
public int getSelectionCount()
```

Returns the number of paths that are selected.

**Specified by:** getSelectionCount

in interface

TreeSelectionModel
**Returns:** the number of paths that are selected

---

#### getSelectionCount

public int getSelectionCount()

Returns the number of paths that are selected.

isPathSelected

```java
public boolean isPathSelected​(
TreePath
path)
```

Returns true if the path,

path

,
is in the current selection.

**Specified by:** isPathSelected

in interface

TreeSelectionModel
**Parameters:** path

- the path to be loked for
**Returns:** whether the

path

is in the current selection

---

#### isPathSelected

public boolean isPathSelected​(

TreePath

path)

Returns true if the path,

path

,
is in the current selection.

isSelectionEmpty

```java
public boolean isSelectionEmpty()
```

Returns true if the selection is currently empty.

**Specified by:** isSelectionEmpty

in interface

TreeSelectionModel
**Returns:** whether the selection is currently empty

---

#### isSelectionEmpty

public boolean isSelectionEmpty()

Returns true if the selection is currently empty.

clearSelection

```java
public void clearSelection()
```

Empties the current selection. If this represents a change in the
current selection, the selection listeners are notified.

**Specified by:** clearSelection

in interface

TreeSelectionModel

---

#### clearSelection

public void clearSelection()

Empties the current selection. If this represents a change in the
current selection, the selection listeners are notified.

addTreeSelectionListener

```java
public void addTreeSelectionListener​(
TreeSelectionListener
x)
```

Adds x to the list of listeners that are notified each time the
set of selected TreePaths changes.

**Specified by:** addTreeSelectionListener

in interface

TreeSelectionModel
**Parameters:** x

- the new listener to be added

---

#### addTreeSelectionListener

public void addTreeSelectionListener​(

TreeSelectionListener

x)

Adds x to the list of listeners that are notified each time the
set of selected TreePaths changes.

removeTreeSelectionListener

```java
public void removeTreeSelectionListener​(
TreeSelectionListener
x)
```

Removes x from the list of listeners that are notified each time
the set of selected TreePaths changes.

**Specified by:** removeTreeSelectionListener

in interface

TreeSelectionModel
**Parameters:** x

- the listener to remove

---

#### removeTreeSelectionListener

public void removeTreeSelectionListener​(

TreeSelectionListener

x)

Removes x from the list of listeners that are notified each time
the set of selected TreePaths changes.

getTreeSelectionListeners

```java
public
TreeSelectionListener
[] getTreeSelectionListeners()
```

Returns an array of all the tree selection listeners
registered on this model.

**Returns:** all of this model's

TreeSelectionListener

s
or an empty
array if no tree selection listeners are currently registered
**Since:** 1.4
**See Also:** addTreeSelectionListener(javax.swing.event.TreeSelectionListener)

,

removeTreeSelectionListener(javax.swing.event.TreeSelectionListener)

---

#### getTreeSelectionListeners

public

TreeSelectionListener

[] getTreeSelectionListeners()

Returns an array of all the tree selection listeners
registered on this model.

fireValueChanged

```java
protected void fireValueChanged​(
TreeSelectionEvent
e)
```

Notifies all listeners that are registered for
tree selection events on this object.

**Parameters:** e

- the event that characterizes the change
**See Also:** addTreeSelectionListener(javax.swing.event.TreeSelectionListener)

,

EventListenerList

---

#### fireValueChanged

protected void fireValueChanged​(

TreeSelectionEvent

e)

Notifies all listeners that are registered for
tree selection events on this object.

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
upon this model.

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
with a class literal,
such as

Foo

Listener.class

.
For example, you can query a

DefaultTreeSelectionModel

m

for its tree selection listeners with the following code:

```java
TreeSelectionListener[] tsls = (TreeSelectionListener[])(m.getListeners(TreeSelectionListener.class));
```

If no such listeners exist, this method returns an empty array.

**Type Parameters:** T

- the listener type
**Parameters:** listenerType

- the type of listeners requested
**Returns:** an array of all objects registered as

Foo

Listener

s on this component,
or an empty array if no such
listeners have been added
**Throws:** ClassCastException

- if

listenerType

doesn't specify a class or interface that implements

java.util.EventListener
**Since:** 1.3
**See Also:** getTreeSelectionListeners()

,

getPropertyChangeListeners()

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
upon this model.

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
with a class literal,
such as

Foo

Listener.class

.
For example, you can query a

DefaultTreeSelectionModel

m

for its tree selection listeners with the following code:

```java
TreeSelectionListener[] tsls = (TreeSelectionListener[])(m.getListeners(TreeSelectionListener.class));
```

If no such listeners exist, this method returns an empty array.

You can specify the

listenerType

argument
with a class literal,
such as

Foo

Listener.class

.
For example, you can query a

DefaultTreeSelectionModel

m

for its tree selection listeners with the following code:

```java
TreeSelectionListener[] tsls = (TreeSelectionListener[])(m.getListeners(TreeSelectionListener.class));
```

If no such listeners exist, this method returns an empty array.

TreeSelectionListener[] tsls = (TreeSelectionListener[])(m.getListeners(TreeSelectionListener.class));

getSelectionRows

```java
public int[] getSelectionRows()
```

Returns the selection in terms of rows. There is not
necessarily a one-to-one mapping between the

TreePath

s
returned from

getSelectionPaths

and this method. In
particular, if a

TreePath

is not viewable (the

RowMapper

returns

-1

for the row corresponding to the

TreePath

), then the corresponding row is not included
in the returned array. For example, if the selection consists
of two paths,

A

and

B

, with

A

at row

10

, and

B

not currently viewable, then this method
returns an array with the single entry

10

.

**Specified by:** getSelectionRows

in interface

TreeSelectionModel
**Returns:** the selection in terms of rows

---

#### getSelectionRows

public int[] getSelectionRows()

Returns the selection in terms of rows. There is not
necessarily a one-to-one mapping between the

TreePath

s
returned from

getSelectionPaths

and this method. In
particular, if a

TreePath

is not viewable (the

RowMapper

returns

-1

for the row corresponding to the

TreePath

), then the corresponding row is not included
in the returned array. For example, if the selection consists
of two paths,

A

and

B

, with

A

at row

10

, and

B

not currently viewable, then this method
returns an array with the single entry

10

.

getMinSelectionRow

```java
public int getMinSelectionRow()
```

Returns the smallest value obtained from the RowMapper for the
current set of selected TreePaths. If nothing is selected,
or there is no RowMapper, this will return -1.

**Specified by:** getMinSelectionRow

in interface

TreeSelectionModel
**Returns:** the smallest value obtained from the RowMapper
for the current set of selected TreePaths

---

#### getMinSelectionRow

public int getMinSelectionRow()

Returns the smallest value obtained from the RowMapper for the
current set of selected TreePaths. If nothing is selected,
or there is no RowMapper, this will return -1.

getMaxSelectionRow

```java
public int getMaxSelectionRow()
```

Returns the largest value obtained from the RowMapper for the
current set of selected TreePaths. If nothing is selected,
or there is no RowMapper, this will return -1.

**Specified by:** getMaxSelectionRow

in interface

TreeSelectionModel
**Returns:** the largest value obtained from the RowMapper
for the current set of selected TreePaths

---

#### getMaxSelectionRow

public int getMaxSelectionRow()

Returns the largest value obtained from the RowMapper for the
current set of selected TreePaths. If nothing is selected,
or there is no RowMapper, this will return -1.

isRowSelected

```java
public boolean isRowSelected​(int row)
```

Returns true if the row identified by

row

is selected.

**Specified by:** isRowSelected

in interface

TreeSelectionModel
**Parameters:** row

- row to check
**Returns:** whether the row is selected

---

#### isRowSelected

public boolean isRowSelected​(int row)

Returns true if the row identified by

row

is selected.

resetRowSelection

```java
public void resetRowSelection()
```

Updates this object's mapping from TreePath to rows. This should
be invoked when the mapping from TreePaths to integers has changed
(for example, a node has been expanded).

You do not normally have to call this, JTree and its associated
Listeners will invoke this for you. If you are implementing your own
View class, then you will have to invoke this.

This will invoke

insureRowContinuity

to make sure
the currently selected TreePaths are still valid based on the
selection mode.

**Specified by:** resetRowSelection

in interface

TreeSelectionModel

---

#### resetRowSelection

public void resetRowSelection()

Updates this object's mapping from TreePath to rows. This should
be invoked when the mapping from TreePaths to integers has changed
(for example, a node has been expanded).

You do not normally have to call this, JTree and its associated
Listeners will invoke this for you. If you are implementing your own
View class, then you will have to invoke this.

This will invoke

insureRowContinuity

to make sure
the currently selected TreePaths are still valid based on the
selection mode.

You do not normally have to call this, JTree and its associated
Listeners will invoke this for you. If you are implementing your own
View class, then you will have to invoke this.

This will invoke

insureRowContinuity

to make sure
the currently selected TreePaths are still valid based on the
selection mode.

This will invoke

insureRowContinuity

to make sure
the currently selected TreePaths are still valid based on the
selection mode.

getLeadSelectionRow

```java
public int getLeadSelectionRow()
```

Returns the lead selection index. That is the last index that was
added.

**Specified by:** getLeadSelectionRow

in interface

TreeSelectionModel
**Returns:** the lead selection index

---

#### getLeadSelectionRow

public int getLeadSelectionRow()

Returns the lead selection index. That is the last index that was
added.

getLeadSelectionPath

```java
public
TreePath
getLeadSelectionPath()
```

Returns the last path that was added. This may differ from the
leadSelectionPath property maintained by the JTree.

**Specified by:** getLeadSelectionPath

in interface

TreeSelectionModel
**Returns:** the last path that was added

---

#### getLeadSelectionPath

public

TreePath

getLeadSelectionPath()

Returns the last path that was added. This may differ from the
leadSelectionPath property maintained by the JTree.

addPropertyChangeListener

```java
public void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list.
The listener is registered for all properties.

A PropertyChangeEvent will get fired when the selection mode
changes.

**Specified by:** addPropertyChangeListener

in interface

TreeSelectionModel
**Parameters:** listener

- the PropertyChangeListener to be added

---

#### addPropertyChangeListener

public void addPropertyChangeListener​(

PropertyChangeListener

listener)

Adds a PropertyChangeListener to the listener list.
The listener is registered for all properties.

A PropertyChangeEvent will get fired when the selection mode
changes.

A PropertyChangeEvent will get fired when the selection mode
changes.

removePropertyChangeListener

```java
public void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a PropertyChangeListener from the listener list.
This removes a PropertyChangeListener that was registered
for all properties.

**Specified by:** removePropertyChangeListener

in interface

TreeSelectionModel
**Parameters:** listener

- the PropertyChangeListener to be removed

---

#### removePropertyChangeListener

public void removePropertyChangeListener​(

PropertyChangeListener

listener)

Removes a PropertyChangeListener from the listener list.
This removes a PropertyChangeListener that was registered
for all properties.

getPropertyChangeListeners

```java
public
PropertyChangeListener
[] getPropertyChangeListeners()
```

Returns an array of all the property change listeners
registered on this

DefaultTreeSelectionModel

.

**Returns:** all of this model's

PropertyChangeListener

s
or an empty
array if no property change listeners are currently registered
**Since:** 1.4
**See Also:** addPropertyChangeListener(java.beans.PropertyChangeListener)

,

removePropertyChangeListener(java.beans.PropertyChangeListener)

---

#### getPropertyChangeListeners

public

PropertyChangeListener

[] getPropertyChangeListeners()

Returns an array of all the property change listeners
registered on this

DefaultTreeSelectionModel

.

insureRowContinuity

```java
protected void insureRowContinuity()
```

Makes sure the currently selected

TreePath

s are valid
for the current selection mode.
If the selection mode is

CONTIGUOUS_TREE_SELECTION

and a

RowMapper

exists, this will make sure all
the rows are contiguous, that is, when sorted all the rows are
in order with no gaps.
If the selection isn't contiguous, the selection is
reset to contain the first set, when sorted, of contiguous rows.

If the selection mode is

SINGLE_TREE_SELECTION

and
more than one TreePath is selected, the selection is reset to
contain the first path currently selected.

---

#### insureRowContinuity

protected void insureRowContinuity()

Makes sure the currently selected

TreePath

s are valid
for the current selection mode.
If the selection mode is

CONTIGUOUS_TREE_SELECTION

and a

RowMapper

exists, this will make sure all
the rows are contiguous, that is, when sorted all the rows are
in order with no gaps.
If the selection isn't contiguous, the selection is
reset to contain the first set, when sorted, of contiguous rows.

If the selection mode is

SINGLE_TREE_SELECTION

and
more than one TreePath is selected, the selection is reset to
contain the first path currently selected.

If the selection mode is

SINGLE_TREE_SELECTION

and
more than one TreePath is selected, the selection is reset to
contain the first path currently selected.

arePathsContiguous

```java
protected boolean arePathsContiguous​(
TreePath
[] paths)
```

Returns true if the paths are contiguous,
or this object has no RowMapper.

**Parameters:** paths

- array of paths to check
**Returns:** whether the paths are contiguous, or this object has no RowMapper

---

#### arePathsContiguous

protected boolean arePathsContiguous​(

TreePath

[] paths)

Returns true if the paths are contiguous,
or this object has no RowMapper.

canPathsBeAdded

```java
protected boolean canPathsBeAdded​(
TreePath
[] paths)
```

Used to test if a particular set of

TreePath

s can
be added. This will return true if

paths

is null (or
empty), or this object has no RowMapper, or nothing is currently selected,
or the selection mode is

DISCONTIGUOUS_TREE_SELECTION

, or
adding the paths to the current selection still results in a
contiguous set of

TreePath

s.

**Parameters:** paths

- array of

TreePaths

to check
**Returns:** whether the particular set of

TreePaths

can be added

---

#### canPathsBeAdded

protected boolean canPathsBeAdded​(

TreePath

[] paths)

Used to test if a particular set of

TreePath

s can
be added. This will return true if

paths

is null (or
empty), or this object has no RowMapper, or nothing is currently selected,
or the selection mode is

DISCONTIGUOUS_TREE_SELECTION

, or
adding the paths to the current selection still results in a
contiguous set of

TreePath

s.

canPathsBeRemoved

```java
protected boolean canPathsBeRemoved​(
TreePath
[] paths)
```

Returns true if the paths can be removed without breaking the
continuity of the model.
This is rather expensive.

**Parameters:** paths

- array of

TreePath

to check
**Returns:** whether the paths can be removed without breaking the
continuity of the model

---

#### canPathsBeRemoved

protected boolean canPathsBeRemoved​(

TreePath

[] paths)

Returns true if the paths can be removed without breaking the
continuity of the model.
This is rather expensive.

notifyPathChange

```java
@Deprecated

protected void notifyPathChange​(
Vector
<?> changedPaths,

TreePath
oldLeadSelection)
```

Deprecated.

As of JDK version 1.7

Notifies listeners of a change in path. changePaths should contain
instances of PathPlaceHolder.

**Parameters:** changedPaths

- the vector of the changed paths
**Parameters:** oldLeadSelection

- the old selection path

---

#### notifyPathChange

@Deprecated

protected void notifyPathChange​(

Vector

<?> changedPaths,

TreePath

oldLeadSelection)

Notifies listeners of a change in path. changePaths should contain
instances of PathPlaceHolder.

updateLeadIndex

```java
protected void updateLeadIndex()
```

Updates the leadIndex instance variable.

---

#### updateLeadIndex

protected void updateLeadIndex()

Updates the leadIndex instance variable.

insureUniqueness

```java
protected void insureUniqueness()
```

This method is obsolete and its implementation is now a noop. It's
still called by setSelectionPaths and addSelectionPaths, but only
for backwards compatibility.

---

#### insureUniqueness

protected void insureUniqueness()

This method is obsolete and its implementation is now a noop. It's
still called by setSelectionPaths and addSelectionPaths, but only
for backwards compatibility.

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
**Returns:** a String representation of this object

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

Returns a clone of this object with the same selection.
This method does not duplicate
selection listeners and property listeners.

**Overrides:** clone

in class

Object
**Returns:** a clone of this instance.
**Throws:** CloneNotSupportedException

- never thrown by instances of
this class
**See Also:** Cloneable

---

#### clone

public

Object

clone()
throws

CloneNotSupportedException

Returns a clone of this object with the same selection.
This method does not duplicate
selection listeners and property listeners.

---

