# Interface TreeSelectionModel

**Source:** `java.desktop\javax\swing\tree\TreeSelectionModel.html`

### Class Description

```java
public interface
TreeSelectionModel
```

This interface represents the current state of the selection for
the tree component.
For information and examples of using tree selection models,
see

How to Use Trees

in

The Java Tutorial.

The state of the tree selection is characterized by
a set of TreePaths, and optionally a set of integers. The mapping
from TreePath to integer is done by way of an instance of RowMapper.
It is not necessary for a TreeSelectionModel to have a RowMapper to
correctly operate, but without a RowMapper

getSelectionRows

will return null.

A TreeSelectionModel can be configured to allow only one
path (

SINGLE_TREE_SELECTION

) a number of
contiguous paths (

CONTIGUOUS_TREE_SELECTION

) or a number of
discontiguous paths (

DISCONTIGUOUS_TREE_SELECTION

).
A

RowMapper

is used to determine if TreePaths are
contiguous.
In the absence of a RowMapper

CONTIGUOUS_TREE_SELECTION

and

DISCONTIGUOUS_TREE_SELECTION

behave the same, that is they
allow any number of paths to be contained in the TreeSelectionModel.

For a selection model of

CONTIGUOUS_TREE_SELECTION

any
time the paths are changed (

setSelectionPath

,

addSelectionPath

...) the TreePaths are again checked to
make they are contiguous. A check of the TreePaths can also be forced
by invoking

resetRowSelection

. How a set of discontiguous
TreePaths is mapped to a contiguous set is left to implementors of
this interface to enforce a particular policy.

Implementations should combine duplicate TreePaths that are
added to the selection. For example, the following code

```java
TreePath[] paths = new TreePath[] { treePath, treePath };
treeSelectionModel.setSelectionPaths(paths);
```

should result in only one path being selected:

treePath

, and
not two copies of

treePath

.

The lead TreePath is the last path that was added (or set). The lead
row is then the row that corresponds to the TreePath as determined
from the RowMapper.

**All Known Implementing Classes:** DefaultTreeSelectionModel

,

JTree.EmptySelectionModel

---

### Field Details

#### static final int SINGLE_TREE_SELECTION

Selection can only contain one path at a time.

**See Also:**
- Constant Field Values

---

#### static final int CONTIGUOUS_TREE_SELECTION

Selection can only be contiguous. This will only be enforced if
a RowMapper instance is provided. That is, if no RowMapper is set
this behaves the same as DISCONTIGUOUS_TREE_SELECTION.

**See Also:**
- Constant Field Values

---

#### static final int DISCONTIGUOUS_TREE_SELECTION

Selection can contain any number of items that are not necessarily
contiguous.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### void setSelectionMode​(int mode)

Sets the selection model, which must be one of SINGLE_TREE_SELECTION,
CONTIGUOUS_TREE_SELECTION or DISCONTIGUOUS_TREE_SELECTION.

This may change the selection if the current selection is not valid
for the new mode. For example, if three TreePaths are
selected when the mode is changed to

SINGLE_TREE_SELECTION

,
only one TreePath will remain selected. It is up to the particular
implementation to decide what TreePath remains selected.

**Parameters:**
- mode

- selection mode to be set

---

#### int getSelectionMode()

Returns the current selection mode, one of

SINGLE_TREE_SELECTION

,

CONTIGUOUS_TREE_SELECTION

or

DISCONTIGUOUS_TREE_SELECTION

.

**Returns:**
- the current selection mode

---

#### void setSelectionPath​(
TreePath
path)

Sets the selection to path. If this represents a change, then
the TreeSelectionListeners are notified. If

path

is
null, this has the same effect as invoking

clearSelection

.

**Parameters:**
- path

- new path to select

---

#### void setSelectionPaths​(
TreePath
[] paths)

Sets the selection to path. If this represents a change, then
the TreeSelectionListeners are notified. If

paths

is
null, this has the same effect as invoking

clearSelection

.

**Parameters:**
- paths

- new selection

---

#### void addSelectionPath​(
TreePath
path)

Adds path to the current selection. If path is not currently
in the selection the TreeSelectionListeners are notified. This has
no effect if

path

is null.

**Parameters:**
- path

- the new path to add to the current selection

---

#### void addSelectionPaths​(
TreePath
[] paths)

Adds paths to the current selection. If any of the paths in
paths are not currently in the selection the TreeSelectionListeners
are notified. This has
no effect if

paths

is null.

**Parameters:**
- paths

- the new paths to add to the current selection

---

#### void removeSelectionPath​(
TreePath
path)

Removes path from the selection. If path is in the selection
The TreeSelectionListeners are notified. This has no effect if

path

is null.

**Parameters:**
- path

- the path to remove from the selection

---

#### void removeSelectionPaths​(
TreePath
[] paths)

Removes paths from the selection. If any of the paths in

paths

are in the selection, the TreeSelectionListeners are notified.
This method has no effect if

paths

is null.

**Parameters:**
- paths

- the path to remove from the selection

---

#### TreePath
getSelectionPath()

Returns the first path in the selection. How first is defined is
up to implementors, and may not necessarily be the TreePath with
the smallest integer value as determined from the

RowMapper

.

**Returns:**
- the first path in the selection

---

#### TreePath
[] getSelectionPaths()

Returns the paths in the selection. This will return null (or an
empty array) if nothing is currently selected.

**Returns:**
- the paths in the selection

---

#### int getSelectionCount()

Returns the number of paths that are selected.

**Returns:**
- the number of paths that are selected

---

#### boolean isPathSelected​(
TreePath
path)

Returns true if the path,

path

, is in the current
selection.

**Parameters:**
- path

- the path to be loked for

**Returns:**
- whether the

path

is in the current selection

---

#### boolean isSelectionEmpty()

Returns true if the selection is currently empty.

**Returns:**
- whether the selection is currently empty

---

#### void clearSelection()

Empties the current selection. If this represents a change in the
current selection, the selection listeners are notified.

---

#### void setRowMapper​(
RowMapper
newMapper)

Sets the RowMapper instance. This instance is used to determine
the row for a particular TreePath.

**Parameters:**
- newMapper

- RowMapper to be set

---

#### RowMapper
getRowMapper()

Returns the RowMapper instance that is able to map a TreePath to a
row.

**Returns:**
- the RowMapper instance that is able to map a TreePath
to a row

---

#### int[] getSelectionRows()

Returns all of the currently selected rows. This will return
null (or an empty array) if there are no selected TreePaths or
a RowMapper has not been set.

**Returns:**
- all of the currently selected rows

---

#### int getMinSelectionRow()

Returns the smallest value obtained from the RowMapper for the
current set of selected TreePaths. If nothing is selected,
or there is no RowMapper, this will return -1.

**Returns:**
- the smallest value obtained from the RowMapper
for the current set of selected TreePaths

---

#### int getMaxSelectionRow()

Returns the largest value obtained from the RowMapper for the
current set of selected TreePaths. If nothing is selected,
or there is no RowMapper, this will return -1.

**Returns:**
- the largest value obtained from the RowMapper
for the current set of selected TreePaths

---

#### boolean isRowSelected​(int row)

Returns true if the row identified by

row

is selected.

**Parameters:**
- row

- row to check

**Returns:**
- whether the row is selected

---

#### void resetRowSelection()

Updates this object's mapping from TreePaths to rows. This should
be invoked when the mapping from TreePaths to integers has changed
(for example, a node has been expanded).

You do not normally have to call this; JTree and its associated
listeners will invoke this for you. If you are implementing your own
view class, then you will have to invoke this.

---

#### int getLeadSelectionRow()

Returns the lead selection index. That is the last index that was
added.

**Returns:**
- the lead selection index

---

#### TreePath
getLeadSelectionPath()

Returns the last path that was added. This may differ from the
leadSelectionPath property maintained by the JTree.

**Returns:**
- the last path that was added

---

#### void addPropertyChangeListener​(
PropertyChangeListener
listener)

Adds a PropertyChangeListener to the listener list.
The listener is registered for all properties.

A PropertyChangeEvent will get fired when the selection mode
changes.

**Parameters:**
- listener

- the PropertyChangeListener to be added

---

#### void removePropertyChangeListener​(
PropertyChangeListener
listener)

Removes a PropertyChangeListener from the listener list.
This removes a PropertyChangeListener that was registered
for all properties.

**Parameters:**
- listener

- the PropertyChangeListener to be removed

---

#### void addTreeSelectionListener​(
TreeSelectionListener
x)

Adds x to the list of listeners that are notified each time the
set of selected TreePaths changes.

**Parameters:**
- x

- the new listener to be added

---

#### void removeTreeSelectionListener​(
TreeSelectionListener
x)

Removes x from the list of listeners that are notified each time
the set of selected TreePaths changes.

**Parameters:**
- x

- the listener to remove

---

### Additional Sections

#### Interface TreeSelectionModel

**All Known Implementing Classes:** DefaultTreeSelectionModel

,

JTree.EmptySelectionModel

```java
public interface
TreeSelectionModel
```

This interface represents the current state of the selection for
the tree component.
For information and examples of using tree selection models,
see

How to Use Trees

in

The Java Tutorial.

The state of the tree selection is characterized by
a set of TreePaths, and optionally a set of integers. The mapping
from TreePath to integer is done by way of an instance of RowMapper.
It is not necessary for a TreeSelectionModel to have a RowMapper to
correctly operate, but without a RowMapper

getSelectionRows

will return null.

A TreeSelectionModel can be configured to allow only one
path (

SINGLE_TREE_SELECTION

) a number of
contiguous paths (

CONTIGUOUS_TREE_SELECTION

) or a number of
discontiguous paths (

DISCONTIGUOUS_TREE_SELECTION

).
A

RowMapper

is used to determine if TreePaths are
contiguous.
In the absence of a RowMapper

CONTIGUOUS_TREE_SELECTION

and

DISCONTIGUOUS_TREE_SELECTION

behave the same, that is they
allow any number of paths to be contained in the TreeSelectionModel.

For a selection model of

CONTIGUOUS_TREE_SELECTION

any
time the paths are changed (

setSelectionPath

,

addSelectionPath

...) the TreePaths are again checked to
make they are contiguous. A check of the TreePaths can also be forced
by invoking

resetRowSelection

. How a set of discontiguous
TreePaths is mapped to a contiguous set is left to implementors of
this interface to enforce a particular policy.

Implementations should combine duplicate TreePaths that are
added to the selection. For example, the following code

```java
TreePath[] paths = new TreePath[] { treePath, treePath };
treeSelectionModel.setSelectionPaths(paths);
```

should result in only one path being selected:

treePath

, and
not two copies of

treePath

.

The lead TreePath is the last path that was added (or set). The lead
row is then the row that corresponds to the TreePath as determined
from the RowMapper.

public interface

TreeSelectionModel

This interface represents the current state of the selection for
the tree component.
For information and examples of using tree selection models,
see

How to Use Trees

in

The Java Tutorial.

The state of the tree selection is characterized by
a set of TreePaths, and optionally a set of integers. The mapping
from TreePath to integer is done by way of an instance of RowMapper.
It is not necessary for a TreeSelectionModel to have a RowMapper to
correctly operate, but without a RowMapper

getSelectionRows

will return null.

A TreeSelectionModel can be configured to allow only one
path (

SINGLE_TREE_SELECTION

) a number of
contiguous paths (

CONTIGUOUS_TREE_SELECTION

) or a number of
discontiguous paths (

DISCONTIGUOUS_TREE_SELECTION

).
A

RowMapper

is used to determine if TreePaths are
contiguous.
In the absence of a RowMapper

CONTIGUOUS_TREE_SELECTION

and

DISCONTIGUOUS_TREE_SELECTION

behave the same, that is they
allow any number of paths to be contained in the TreeSelectionModel.

For a selection model of

CONTIGUOUS_TREE_SELECTION

any
time the paths are changed (

setSelectionPath

,

addSelectionPath

...) the TreePaths are again checked to
make they are contiguous. A check of the TreePaths can also be forced
by invoking

resetRowSelection

. How a set of discontiguous
TreePaths is mapped to a contiguous set is left to implementors of
this interface to enforce a particular policy.

Implementations should combine duplicate TreePaths that are
added to the selection. For example, the following code

```java
TreePath[] paths = new TreePath[] { treePath, treePath };
treeSelectionModel.setSelectionPaths(paths);
```

should result in only one path being selected:

treePath

, and
not two copies of

treePath

.

The lead TreePath is the last path that was added (or set). The lead
row is then the row that corresponds to the TreePath as determined
from the RowMapper.

The state of the tree selection is characterized by
a set of TreePaths, and optionally a set of integers. The mapping
from TreePath to integer is done by way of an instance of RowMapper.
It is not necessary for a TreeSelectionModel to have a RowMapper to
correctly operate, but without a RowMapper

getSelectionRows

will return null.

A TreeSelectionModel can be configured to allow only one
path (

SINGLE_TREE_SELECTION

) a number of
contiguous paths (

CONTIGUOUS_TREE_SELECTION

) or a number of
discontiguous paths (

DISCONTIGUOUS_TREE_SELECTION

).
A

RowMapper

is used to determine if TreePaths are
contiguous.
In the absence of a RowMapper

CONTIGUOUS_TREE_SELECTION

and

DISCONTIGUOUS_TREE_SELECTION

behave the same, that is they
allow any number of paths to be contained in the TreeSelectionModel.

For a selection model of

CONTIGUOUS_TREE_SELECTION

any
time the paths are changed (

setSelectionPath

,

addSelectionPath

...) the TreePaths are again checked to
make they are contiguous. A check of the TreePaths can also be forced
by invoking

resetRowSelection

. How a set of discontiguous
TreePaths is mapped to a contiguous set is left to implementors of
this interface to enforce a particular policy.

Implementations should combine duplicate TreePaths that are
added to the selection. For example, the following code

```java
TreePath[] paths = new TreePath[] { treePath, treePath };
treeSelectionModel.setSelectionPaths(paths);
```

should result in only one path being selected:

treePath

, and
not two copies of

treePath

.

The lead TreePath is the last path that was added (or set). The lead
row is then the row that corresponds to the TreePath as determined
from the RowMapper.

A TreeSelectionModel can be configured to allow only one
path (

SINGLE_TREE_SELECTION

) a number of
contiguous paths (

CONTIGUOUS_TREE_SELECTION

) or a number of
discontiguous paths (

DISCONTIGUOUS_TREE_SELECTION

).
A

RowMapper

is used to determine if TreePaths are
contiguous.
In the absence of a RowMapper

CONTIGUOUS_TREE_SELECTION

and

DISCONTIGUOUS_TREE_SELECTION

behave the same, that is they
allow any number of paths to be contained in the TreeSelectionModel.

For a selection model of

CONTIGUOUS_TREE_SELECTION

any
time the paths are changed (

setSelectionPath

,

addSelectionPath

...) the TreePaths are again checked to
make they are contiguous. A check of the TreePaths can also be forced
by invoking

resetRowSelection

. How a set of discontiguous
TreePaths is mapped to a contiguous set is left to implementors of
this interface to enforce a particular policy.

Implementations should combine duplicate TreePaths that are
added to the selection. For example, the following code

```java
TreePath[] paths = new TreePath[] { treePath, treePath };
treeSelectionModel.setSelectionPaths(paths);
```

should result in only one path being selected:

treePath

, and
not two copies of

treePath

.

The lead TreePath is the last path that was added (or set). The lead
row is then the row that corresponds to the TreePath as determined
from the RowMapper.

For a selection model of

CONTIGUOUS_TREE_SELECTION

any
time the paths are changed (

setSelectionPath

,

addSelectionPath

...) the TreePaths are again checked to
make they are contiguous. A check of the TreePaths can also be forced
by invoking

resetRowSelection

. How a set of discontiguous
TreePaths is mapped to a contiguous set is left to implementors of
this interface to enforce a particular policy.

Implementations should combine duplicate TreePaths that are
added to the selection. For example, the following code

```java
TreePath[] paths = new TreePath[] { treePath, treePath };
treeSelectionModel.setSelectionPaths(paths);
```

should result in only one path being selected:

treePath

, and
not two copies of

treePath

.

The lead TreePath is the last path that was added (or set). The lead
row is then the row that corresponds to the TreePath as determined
from the RowMapper.

Implementations should combine duplicate TreePaths that are
added to the selection. For example, the following code

```java
TreePath[] paths = new TreePath[] { treePath, treePath };
treeSelectionModel.setSelectionPaths(paths);
```

should result in only one path being selected:

treePath

, and
not two copies of

treePath

.

The lead TreePath is the last path that was added (or set). The lead
row is then the row that corresponds to the TreePath as determined
from the RowMapper.

TreePath[] paths = new TreePath[] { treePath, treePath };
treeSelectionModel.setSelectionPaths(paths);

The lead TreePath is the last path that was added (or set). The lead
row is then the row that corresponds to the TreePath as determined
from the RowMapper.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

CONTIGUOUS_TREE_SELECTION

Selection can only be contiguous.

static int

DISCONTIGUOUS_TREE_SELECTION

Selection can contain any number of items that are not necessarily
contiguous.

static int

SINGLE_TREE_SELECTION

Selection can only contain one path at a time.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

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

void

clearSelection

()

Empties the current selection.

TreePath

getLeadSelectionPath

()

Returns the last path that was added.

int

getLeadSelectionRow

()

Returns the lead selection index.

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

Returns the current selection mode, one of

SINGLE_TREE_SELECTION

,

CONTIGUOUS_TREE_SELECTION

or

DISCONTIGUOUS_TREE_SELECTION

.

TreePath

getSelectionPath

()

Returns the first path in the selection.

TreePath

[]

getSelectionPaths

()

Returns the paths in the selection.

int[]

getSelectionRows

()

Returns all of the currently selected rows.

boolean

isPathSelected

​(

TreePath

path)

Returns true if the path,

path

, is in the current
selection.

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

Updates this object's mapping from TreePaths to rows.

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

[] paths)

Sets the selection to path.

Field Summary

Fields

Modifier and Type

Field

Description

static int

CONTIGUOUS_TREE_SELECTION

Selection can only be contiguous.

static int

DISCONTIGUOUS_TREE_SELECTION

Selection can contain any number of items that are not necessarily
contiguous.

static int

SINGLE_TREE_SELECTION

Selection can only contain one path at a time.

---

#### Field Summary

Selection can only be contiguous.

Selection can contain any number of items that are not necessarily
contiguous.

Selection can only contain one path at a time.

Method Summary

All Methods

Instance Methods

Abstract Methods

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

void

clearSelection

()

Empties the current selection.

TreePath

getLeadSelectionPath

()

Returns the last path that was added.

int

getLeadSelectionRow

()

Returns the lead selection index.

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

Returns the current selection mode, one of

SINGLE_TREE_SELECTION

,

CONTIGUOUS_TREE_SELECTION

or

DISCONTIGUOUS_TREE_SELECTION

.

TreePath

getSelectionPath

()

Returns the first path in the selection.

TreePath

[]

getSelectionPaths

()

Returns the paths in the selection.

int[]

getSelectionRows

()

Returns all of the currently selected rows.

boolean

isPathSelected

​(

TreePath

path)

Returns true if the path,

path

, is in the current
selection.

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

Updates this object's mapping from TreePaths to rows.

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

[] paths)

Sets the selection to path.

---

#### Method Summary

Adds a PropertyChangeListener to the listener list.

Adds path to the current selection.

Adds paths to the current selection.

Adds x to the list of listeners that are notified each time the
set of selected TreePaths changes.

Empties the current selection.

Returns the last path that was added.

Returns the lead selection index.

Returns the largest value obtained from the RowMapper for the
current set of selected TreePaths.

Returns the smallest value obtained from the RowMapper for the
current set of selected TreePaths.

Returns the RowMapper instance that is able to map a TreePath to a
row.

Returns the number of paths that are selected.

Returns the current selection mode, one of

SINGLE_TREE_SELECTION

,

CONTIGUOUS_TREE_SELECTION

or

DISCONTIGUOUS_TREE_SELECTION

.

Returns the first path in the selection.

Returns the paths in the selection.

Returns all of the currently selected rows.

Returns true if the path,

path

, is in the current
selection.

Returns true if the row identified by

row

is selected.

Returns true if the selection is currently empty.

Removes a PropertyChangeListener from the listener list.

Removes path from the selection.

Removes paths from the selection.

Removes x from the list of listeners that are notified each time
the set of selected TreePaths changes.

Updates this object's mapping from TreePaths to rows.

Sets the RowMapper instance.

Sets the selection model, which must be one of SINGLE_TREE_SELECTION,
CONTIGUOUS_TREE_SELECTION or DISCONTIGUOUS_TREE_SELECTION.

Sets the selection to path.

============ FIELD DETAIL ===========

- Field Detail

- SINGLE_TREE_SELECTION

```java
static final int SINGLE_TREE_SELECTION
```

Selection can only contain one path at a time.

**See Also:** Constant Field Values

- CONTIGUOUS_TREE_SELECTION

```java
static final int CONTIGUOUS_TREE_SELECTION
```

Selection can only be contiguous. This will only be enforced if
a RowMapper instance is provided. That is, if no RowMapper is set
this behaves the same as DISCONTIGUOUS_TREE_SELECTION.

**See Also:** Constant Field Values

- DISCONTIGUOUS_TREE_SELECTION

```java
static final int DISCONTIGUOUS_TREE_SELECTION
```

Selection can contain any number of items that are not necessarily
contiguous.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- setSelectionMode

```java
void setSelectionMode​(int mode)
```

Sets the selection model, which must be one of SINGLE_TREE_SELECTION,
CONTIGUOUS_TREE_SELECTION or DISCONTIGUOUS_TREE_SELECTION.

This may change the selection if the current selection is not valid
for the new mode. For example, if three TreePaths are
selected when the mode is changed to

SINGLE_TREE_SELECTION

,
only one TreePath will remain selected. It is up to the particular
implementation to decide what TreePath remains selected.

**Parameters:** mode

- selection mode to be set

- getSelectionMode

```java
int getSelectionMode()
```

Returns the current selection mode, one of

SINGLE_TREE_SELECTION

,

CONTIGUOUS_TREE_SELECTION

or

DISCONTIGUOUS_TREE_SELECTION

.

**Returns:** the current selection mode

- setSelectionPath

```java
void setSelectionPath​(
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

**Parameters:** path

- new path to select

- setSelectionPaths

```java
void setSelectionPaths​(
TreePath
[] paths)
```

Sets the selection to path. If this represents a change, then
the TreeSelectionListeners are notified. If

paths

is
null, this has the same effect as invoking

clearSelection

.

**Parameters:** paths

- new selection

- addSelectionPath

```java
void addSelectionPath​(
TreePath
path)
```

Adds path to the current selection. If path is not currently
in the selection the TreeSelectionListeners are notified. This has
no effect if

path

is null.

**Parameters:** path

- the new path to add to the current selection

- addSelectionPaths

```java
void addSelectionPaths​(
TreePath
[] paths)
```

Adds paths to the current selection. If any of the paths in
paths are not currently in the selection the TreeSelectionListeners
are notified. This has
no effect if

paths

is null.

**Parameters:** paths

- the new paths to add to the current selection

- removeSelectionPath

```java
void removeSelectionPath​(
TreePath
path)
```

Removes path from the selection. If path is in the selection
The TreeSelectionListeners are notified. This has no effect if

path

is null.

**Parameters:** path

- the path to remove from the selection

- removeSelectionPaths

```java
void removeSelectionPaths​(
TreePath
[] paths)
```

Removes paths from the selection. If any of the paths in

paths

are in the selection, the TreeSelectionListeners are notified.
This method has no effect if

paths

is null.

**Parameters:** paths

- the path to remove from the selection

- getSelectionPath

```java
TreePath
getSelectionPath()
```

Returns the first path in the selection. How first is defined is
up to implementors, and may not necessarily be the TreePath with
the smallest integer value as determined from the

RowMapper

.

**Returns:** the first path in the selection

- getSelectionPaths

```java
TreePath
[] getSelectionPaths()
```

Returns the paths in the selection. This will return null (or an
empty array) if nothing is currently selected.

**Returns:** the paths in the selection

- getSelectionCount

```java
int getSelectionCount()
```

Returns the number of paths that are selected.

**Returns:** the number of paths that are selected

- isPathSelected

```java
boolean isPathSelected​(
TreePath
path)
```

Returns true if the path,

path

, is in the current
selection.

**Parameters:** path

- the path to be loked for
**Returns:** whether the

path

is in the current selection

- isSelectionEmpty

```java
boolean isSelectionEmpty()
```

Returns true if the selection is currently empty.

**Returns:** whether the selection is currently empty

- clearSelection

```java
void clearSelection()
```

Empties the current selection. If this represents a change in the
current selection, the selection listeners are notified.

- setRowMapper

```java
void setRowMapper​(
RowMapper
newMapper)
```

Sets the RowMapper instance. This instance is used to determine
the row for a particular TreePath.

**Parameters:** newMapper

- RowMapper to be set

- getRowMapper

```java
RowMapper
getRowMapper()
```

Returns the RowMapper instance that is able to map a TreePath to a
row.

**Returns:** the RowMapper instance that is able to map a TreePath
to a row

- getSelectionRows

```java
int[] getSelectionRows()
```

Returns all of the currently selected rows. This will return
null (or an empty array) if there are no selected TreePaths or
a RowMapper has not been set.

**Returns:** all of the currently selected rows

- getMinSelectionRow

```java
int getMinSelectionRow()
```

Returns the smallest value obtained from the RowMapper for the
current set of selected TreePaths. If nothing is selected,
or there is no RowMapper, this will return -1.

**Returns:** the smallest value obtained from the RowMapper
for the current set of selected TreePaths

- getMaxSelectionRow

```java
int getMaxSelectionRow()
```

Returns the largest value obtained from the RowMapper for the
current set of selected TreePaths. If nothing is selected,
or there is no RowMapper, this will return -1.

**Returns:** the largest value obtained from the RowMapper
for the current set of selected TreePaths

- isRowSelected

```java
boolean isRowSelected​(int row)
```

Returns true if the row identified by

row

is selected.

**Parameters:** row

- row to check
**Returns:** whether the row is selected

- resetRowSelection

```java
void resetRowSelection()
```

Updates this object's mapping from TreePaths to rows. This should
be invoked when the mapping from TreePaths to integers has changed
(for example, a node has been expanded).

You do not normally have to call this; JTree and its associated
listeners will invoke this for you. If you are implementing your own
view class, then you will have to invoke this.

- getLeadSelectionRow

```java
int getLeadSelectionRow()
```

Returns the lead selection index. That is the last index that was
added.

**Returns:** the lead selection index

- getLeadSelectionPath

```java
TreePath
getLeadSelectionPath()
```

Returns the last path that was added. This may differ from the
leadSelectionPath property maintained by the JTree.

**Returns:** the last path that was added

- addPropertyChangeListener

```java
void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list.
The listener is registered for all properties.

A PropertyChangeEvent will get fired when the selection mode
changes.

**Parameters:** listener

- the PropertyChangeListener to be added

- removePropertyChangeListener

```java
void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a PropertyChangeListener from the listener list.
This removes a PropertyChangeListener that was registered
for all properties.

**Parameters:** listener

- the PropertyChangeListener to be removed

- addTreeSelectionListener

```java
void addTreeSelectionListener​(
TreeSelectionListener
x)
```

Adds x to the list of listeners that are notified each time the
set of selected TreePaths changes.

**Parameters:** x

- the new listener to be added

- removeTreeSelectionListener

```java
void removeTreeSelectionListener​(
TreeSelectionListener
x)
```

Removes x from the list of listeners that are notified each time
the set of selected TreePaths changes.

**Parameters:** x

- the listener to remove

Field Detail

- SINGLE_TREE_SELECTION

```java
static final int SINGLE_TREE_SELECTION
```

Selection can only contain one path at a time.

**See Also:** Constant Field Values

- CONTIGUOUS_TREE_SELECTION

```java
static final int CONTIGUOUS_TREE_SELECTION
```

Selection can only be contiguous. This will only be enforced if
a RowMapper instance is provided. That is, if no RowMapper is set
this behaves the same as DISCONTIGUOUS_TREE_SELECTION.

**See Also:** Constant Field Values

- DISCONTIGUOUS_TREE_SELECTION

```java
static final int DISCONTIGUOUS_TREE_SELECTION
```

Selection can contain any number of items that are not necessarily
contiguous.

**See Also:** Constant Field Values

---

#### Field Detail

SINGLE_TREE_SELECTION

```java
static final int SINGLE_TREE_SELECTION
```

Selection can only contain one path at a time.

**See Also:** Constant Field Values

---

#### SINGLE_TREE_SELECTION

static final int SINGLE_TREE_SELECTION

Selection can only contain one path at a time.

CONTIGUOUS_TREE_SELECTION

```java
static final int CONTIGUOUS_TREE_SELECTION
```

Selection can only be contiguous. This will only be enforced if
a RowMapper instance is provided. That is, if no RowMapper is set
this behaves the same as DISCONTIGUOUS_TREE_SELECTION.

**See Also:** Constant Field Values

---

#### CONTIGUOUS_TREE_SELECTION

static final int CONTIGUOUS_TREE_SELECTION

Selection can only be contiguous. This will only be enforced if
a RowMapper instance is provided. That is, if no RowMapper is set
this behaves the same as DISCONTIGUOUS_TREE_SELECTION.

DISCONTIGUOUS_TREE_SELECTION

```java
static final int DISCONTIGUOUS_TREE_SELECTION
```

Selection can contain any number of items that are not necessarily
contiguous.

**See Also:** Constant Field Values

---

#### DISCONTIGUOUS_TREE_SELECTION

static final int DISCONTIGUOUS_TREE_SELECTION

Selection can contain any number of items that are not necessarily
contiguous.

Method Detail

- setSelectionMode

```java
void setSelectionMode​(int mode)
```

Sets the selection model, which must be one of SINGLE_TREE_SELECTION,
CONTIGUOUS_TREE_SELECTION or DISCONTIGUOUS_TREE_SELECTION.

This may change the selection if the current selection is not valid
for the new mode. For example, if three TreePaths are
selected when the mode is changed to

SINGLE_TREE_SELECTION

,
only one TreePath will remain selected. It is up to the particular
implementation to decide what TreePath remains selected.

**Parameters:** mode

- selection mode to be set

- getSelectionMode

```java
int getSelectionMode()
```

Returns the current selection mode, one of

SINGLE_TREE_SELECTION

,

CONTIGUOUS_TREE_SELECTION

or

DISCONTIGUOUS_TREE_SELECTION

.

**Returns:** the current selection mode

- setSelectionPath

```java
void setSelectionPath​(
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

**Parameters:** path

- new path to select

- setSelectionPaths

```java
void setSelectionPaths​(
TreePath
[] paths)
```

Sets the selection to path. If this represents a change, then
the TreeSelectionListeners are notified. If

paths

is
null, this has the same effect as invoking

clearSelection

.

**Parameters:** paths

- new selection

- addSelectionPath

```java
void addSelectionPath​(
TreePath
path)
```

Adds path to the current selection. If path is not currently
in the selection the TreeSelectionListeners are notified. This has
no effect if

path

is null.

**Parameters:** path

- the new path to add to the current selection

- addSelectionPaths

```java
void addSelectionPaths​(
TreePath
[] paths)
```

Adds paths to the current selection. If any of the paths in
paths are not currently in the selection the TreeSelectionListeners
are notified. This has
no effect if

paths

is null.

**Parameters:** paths

- the new paths to add to the current selection

- removeSelectionPath

```java
void removeSelectionPath​(
TreePath
path)
```

Removes path from the selection. If path is in the selection
The TreeSelectionListeners are notified. This has no effect if

path

is null.

**Parameters:** path

- the path to remove from the selection

- removeSelectionPaths

```java
void removeSelectionPaths​(
TreePath
[] paths)
```

Removes paths from the selection. If any of the paths in

paths

are in the selection, the TreeSelectionListeners are notified.
This method has no effect if

paths

is null.

**Parameters:** paths

- the path to remove from the selection

- getSelectionPath

```java
TreePath
getSelectionPath()
```

Returns the first path in the selection. How first is defined is
up to implementors, and may not necessarily be the TreePath with
the smallest integer value as determined from the

RowMapper

.

**Returns:** the first path in the selection

- getSelectionPaths

```java
TreePath
[] getSelectionPaths()
```

Returns the paths in the selection. This will return null (or an
empty array) if nothing is currently selected.

**Returns:** the paths in the selection

- getSelectionCount

```java
int getSelectionCount()
```

Returns the number of paths that are selected.

**Returns:** the number of paths that are selected

- isPathSelected

```java
boolean isPathSelected​(
TreePath
path)
```

Returns true if the path,

path

, is in the current
selection.

**Parameters:** path

- the path to be loked for
**Returns:** whether the

path

is in the current selection

- isSelectionEmpty

```java
boolean isSelectionEmpty()
```

Returns true if the selection is currently empty.

**Returns:** whether the selection is currently empty

- clearSelection

```java
void clearSelection()
```

Empties the current selection. If this represents a change in the
current selection, the selection listeners are notified.

- setRowMapper

```java
void setRowMapper​(
RowMapper
newMapper)
```

Sets the RowMapper instance. This instance is used to determine
the row for a particular TreePath.

**Parameters:** newMapper

- RowMapper to be set

- getRowMapper

```java
RowMapper
getRowMapper()
```

Returns the RowMapper instance that is able to map a TreePath to a
row.

**Returns:** the RowMapper instance that is able to map a TreePath
to a row

- getSelectionRows

```java
int[] getSelectionRows()
```

Returns all of the currently selected rows. This will return
null (or an empty array) if there are no selected TreePaths or
a RowMapper has not been set.

**Returns:** all of the currently selected rows

- getMinSelectionRow

```java
int getMinSelectionRow()
```

Returns the smallest value obtained from the RowMapper for the
current set of selected TreePaths. If nothing is selected,
or there is no RowMapper, this will return -1.

**Returns:** the smallest value obtained from the RowMapper
for the current set of selected TreePaths

- getMaxSelectionRow

```java
int getMaxSelectionRow()
```

Returns the largest value obtained from the RowMapper for the
current set of selected TreePaths. If nothing is selected,
or there is no RowMapper, this will return -1.

**Returns:** the largest value obtained from the RowMapper
for the current set of selected TreePaths

- isRowSelected

```java
boolean isRowSelected​(int row)
```

Returns true if the row identified by

row

is selected.

**Parameters:** row

- row to check
**Returns:** whether the row is selected

- resetRowSelection

```java
void resetRowSelection()
```

Updates this object's mapping from TreePaths to rows. This should
be invoked when the mapping from TreePaths to integers has changed
(for example, a node has been expanded).

You do not normally have to call this; JTree and its associated
listeners will invoke this for you. If you are implementing your own
view class, then you will have to invoke this.

- getLeadSelectionRow

```java
int getLeadSelectionRow()
```

Returns the lead selection index. That is the last index that was
added.

**Returns:** the lead selection index

- getLeadSelectionPath

```java
TreePath
getLeadSelectionPath()
```

Returns the last path that was added. This may differ from the
leadSelectionPath property maintained by the JTree.

**Returns:** the last path that was added

- addPropertyChangeListener

```java
void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list.
The listener is registered for all properties.

A PropertyChangeEvent will get fired when the selection mode
changes.

**Parameters:** listener

- the PropertyChangeListener to be added

- removePropertyChangeListener

```java
void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a PropertyChangeListener from the listener list.
This removes a PropertyChangeListener that was registered
for all properties.

**Parameters:** listener

- the PropertyChangeListener to be removed

- addTreeSelectionListener

```java
void addTreeSelectionListener​(
TreeSelectionListener
x)
```

Adds x to the list of listeners that are notified each time the
set of selected TreePaths changes.

**Parameters:** x

- the new listener to be added

- removeTreeSelectionListener

```java
void removeTreeSelectionListener​(
TreeSelectionListener
x)
```

Removes x from the list of listeners that are notified each time
the set of selected TreePaths changes.

**Parameters:** x

- the listener to remove

---

#### Method Detail

setSelectionMode

```java
void setSelectionMode​(int mode)
```

Sets the selection model, which must be one of SINGLE_TREE_SELECTION,
CONTIGUOUS_TREE_SELECTION or DISCONTIGUOUS_TREE_SELECTION.

This may change the selection if the current selection is not valid
for the new mode. For example, if three TreePaths are
selected when the mode is changed to

SINGLE_TREE_SELECTION

,
only one TreePath will remain selected. It is up to the particular
implementation to decide what TreePath remains selected.

**Parameters:** mode

- selection mode to be set

---

#### setSelectionMode

void setSelectionMode​(int mode)

Sets the selection model, which must be one of SINGLE_TREE_SELECTION,
CONTIGUOUS_TREE_SELECTION or DISCONTIGUOUS_TREE_SELECTION.

This may change the selection if the current selection is not valid
for the new mode. For example, if three TreePaths are
selected when the mode is changed to

SINGLE_TREE_SELECTION

,
only one TreePath will remain selected. It is up to the particular
implementation to decide what TreePath remains selected.

This may change the selection if the current selection is not valid
for the new mode. For example, if three TreePaths are
selected when the mode is changed to

SINGLE_TREE_SELECTION

,
only one TreePath will remain selected. It is up to the particular
implementation to decide what TreePath remains selected.

getSelectionMode

```java
int getSelectionMode()
```

Returns the current selection mode, one of

SINGLE_TREE_SELECTION

,

CONTIGUOUS_TREE_SELECTION

or

DISCONTIGUOUS_TREE_SELECTION

.

**Returns:** the current selection mode

---

#### getSelectionMode

int getSelectionMode()

Returns the current selection mode, one of

SINGLE_TREE_SELECTION

,

CONTIGUOUS_TREE_SELECTION

or

DISCONTIGUOUS_TREE_SELECTION

.

setSelectionPath

```java
void setSelectionPath​(
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

**Parameters:** path

- new path to select

---

#### setSelectionPath

void setSelectionPath​(

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
void setSelectionPaths​(
TreePath
[] paths)
```

Sets the selection to path. If this represents a change, then
the TreeSelectionListeners are notified. If

paths

is
null, this has the same effect as invoking

clearSelection

.

**Parameters:** paths

- new selection

---

#### setSelectionPaths

void setSelectionPaths​(

TreePath

[] paths)

Sets the selection to path. If this represents a change, then
the TreeSelectionListeners are notified. If

paths

is
null, this has the same effect as invoking

clearSelection

.

addSelectionPath

```java
void addSelectionPath​(
TreePath
path)
```

Adds path to the current selection. If path is not currently
in the selection the TreeSelectionListeners are notified. This has
no effect if

path

is null.

**Parameters:** path

- the new path to add to the current selection

---

#### addSelectionPath

void addSelectionPath​(

TreePath

path)

Adds path to the current selection. If path is not currently
in the selection the TreeSelectionListeners are notified. This has
no effect if

path

is null.

addSelectionPaths

```java
void addSelectionPaths​(
TreePath
[] paths)
```

Adds paths to the current selection. If any of the paths in
paths are not currently in the selection the TreeSelectionListeners
are notified. This has
no effect if

paths

is null.

**Parameters:** paths

- the new paths to add to the current selection

---

#### addSelectionPaths

void addSelectionPaths​(

TreePath

[] paths)

Adds paths to the current selection. If any of the paths in
paths are not currently in the selection the TreeSelectionListeners
are notified. This has
no effect if

paths

is null.

removeSelectionPath

```java
void removeSelectionPath​(
TreePath
path)
```

Removes path from the selection. If path is in the selection
The TreeSelectionListeners are notified. This has no effect if

path

is null.

**Parameters:** path

- the path to remove from the selection

---

#### removeSelectionPath

void removeSelectionPath​(

TreePath

path)

Removes path from the selection. If path is in the selection
The TreeSelectionListeners are notified. This has no effect if

path

is null.

removeSelectionPaths

```java
void removeSelectionPaths​(
TreePath
[] paths)
```

Removes paths from the selection. If any of the paths in

paths

are in the selection, the TreeSelectionListeners are notified.
This method has no effect if

paths

is null.

**Parameters:** paths

- the path to remove from the selection

---

#### removeSelectionPaths

void removeSelectionPaths​(

TreePath

[] paths)

Removes paths from the selection. If any of the paths in

paths

are in the selection, the TreeSelectionListeners are notified.
This method has no effect if

paths

is null.

getSelectionPath

```java
TreePath
getSelectionPath()
```

Returns the first path in the selection. How first is defined is
up to implementors, and may not necessarily be the TreePath with
the smallest integer value as determined from the

RowMapper

.

**Returns:** the first path in the selection

---

#### getSelectionPath

TreePath

getSelectionPath()

Returns the first path in the selection. How first is defined is
up to implementors, and may not necessarily be the TreePath with
the smallest integer value as determined from the

RowMapper

.

getSelectionPaths

```java
TreePath
[] getSelectionPaths()
```

Returns the paths in the selection. This will return null (or an
empty array) if nothing is currently selected.

**Returns:** the paths in the selection

---

#### getSelectionPaths

TreePath

[] getSelectionPaths()

Returns the paths in the selection. This will return null (or an
empty array) if nothing is currently selected.

getSelectionCount

```java
int getSelectionCount()
```

Returns the number of paths that are selected.

**Returns:** the number of paths that are selected

---

#### getSelectionCount

int getSelectionCount()

Returns the number of paths that are selected.

isPathSelected

```java
boolean isPathSelected​(
TreePath
path)
```

Returns true if the path,

path

, is in the current
selection.

**Parameters:** path

- the path to be loked for
**Returns:** whether the

path

is in the current selection

---

#### isPathSelected

boolean isPathSelected​(

TreePath

path)

Returns true if the path,

path

, is in the current
selection.

isSelectionEmpty

```java
boolean isSelectionEmpty()
```

Returns true if the selection is currently empty.

**Returns:** whether the selection is currently empty

---

#### isSelectionEmpty

boolean isSelectionEmpty()

Returns true if the selection is currently empty.

clearSelection

```java
void clearSelection()
```

Empties the current selection. If this represents a change in the
current selection, the selection listeners are notified.

---

#### clearSelection

void clearSelection()

Empties the current selection. If this represents a change in the
current selection, the selection listeners are notified.

setRowMapper

```java
void setRowMapper​(
RowMapper
newMapper)
```

Sets the RowMapper instance. This instance is used to determine
the row for a particular TreePath.

**Parameters:** newMapper

- RowMapper to be set

---

#### setRowMapper

void setRowMapper​(

RowMapper

newMapper)

Sets the RowMapper instance. This instance is used to determine
the row for a particular TreePath.

getRowMapper

```java
RowMapper
getRowMapper()
```

Returns the RowMapper instance that is able to map a TreePath to a
row.

**Returns:** the RowMapper instance that is able to map a TreePath
to a row

---

#### getRowMapper

RowMapper

getRowMapper()

Returns the RowMapper instance that is able to map a TreePath to a
row.

getSelectionRows

```java
int[] getSelectionRows()
```

Returns all of the currently selected rows. This will return
null (or an empty array) if there are no selected TreePaths or
a RowMapper has not been set.

**Returns:** all of the currently selected rows

---

#### getSelectionRows

int[] getSelectionRows()

Returns all of the currently selected rows. This will return
null (or an empty array) if there are no selected TreePaths or
a RowMapper has not been set.

getMinSelectionRow

```java
int getMinSelectionRow()
```

Returns the smallest value obtained from the RowMapper for the
current set of selected TreePaths. If nothing is selected,
or there is no RowMapper, this will return -1.

**Returns:** the smallest value obtained from the RowMapper
for the current set of selected TreePaths

---

#### getMinSelectionRow

int getMinSelectionRow()

Returns the smallest value obtained from the RowMapper for the
current set of selected TreePaths. If nothing is selected,
or there is no RowMapper, this will return -1.

getMaxSelectionRow

```java
int getMaxSelectionRow()
```

Returns the largest value obtained from the RowMapper for the
current set of selected TreePaths. If nothing is selected,
or there is no RowMapper, this will return -1.

**Returns:** the largest value obtained from the RowMapper
for the current set of selected TreePaths

---

#### getMaxSelectionRow

int getMaxSelectionRow()

Returns the largest value obtained from the RowMapper for the
current set of selected TreePaths. If nothing is selected,
or there is no RowMapper, this will return -1.

isRowSelected

```java
boolean isRowSelected​(int row)
```

Returns true if the row identified by

row

is selected.

**Parameters:** row

- row to check
**Returns:** whether the row is selected

---

#### isRowSelected

boolean isRowSelected​(int row)

Returns true if the row identified by

row

is selected.

resetRowSelection

```java
void resetRowSelection()
```

Updates this object's mapping from TreePaths to rows. This should
be invoked when the mapping from TreePaths to integers has changed
(for example, a node has been expanded).

You do not normally have to call this; JTree and its associated
listeners will invoke this for you. If you are implementing your own
view class, then you will have to invoke this.

---

#### resetRowSelection

void resetRowSelection()

Updates this object's mapping from TreePaths to rows. This should
be invoked when the mapping from TreePaths to integers has changed
(for example, a node has been expanded).

You do not normally have to call this; JTree and its associated
listeners will invoke this for you. If you are implementing your own
view class, then you will have to invoke this.

You do not normally have to call this; JTree and its associated
listeners will invoke this for you. If you are implementing your own
view class, then you will have to invoke this.

getLeadSelectionRow

```java
int getLeadSelectionRow()
```

Returns the lead selection index. That is the last index that was
added.

**Returns:** the lead selection index

---

#### getLeadSelectionRow

int getLeadSelectionRow()

Returns the lead selection index. That is the last index that was
added.

getLeadSelectionPath

```java
TreePath
getLeadSelectionPath()
```

Returns the last path that was added. This may differ from the
leadSelectionPath property maintained by the JTree.

**Returns:** the last path that was added

---

#### getLeadSelectionPath

TreePath

getLeadSelectionPath()

Returns the last path that was added. This may differ from the
leadSelectionPath property maintained by the JTree.

addPropertyChangeListener

```java
void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a PropertyChangeListener to the listener list.
The listener is registered for all properties.

A PropertyChangeEvent will get fired when the selection mode
changes.

**Parameters:** listener

- the PropertyChangeListener to be added

---

#### addPropertyChangeListener

void addPropertyChangeListener​(

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
void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a PropertyChangeListener from the listener list.
This removes a PropertyChangeListener that was registered
for all properties.

**Parameters:** listener

- the PropertyChangeListener to be removed

---

#### removePropertyChangeListener

void removePropertyChangeListener​(

PropertyChangeListener

listener)

Removes a PropertyChangeListener from the listener list.
This removes a PropertyChangeListener that was registered
for all properties.

addTreeSelectionListener

```java
void addTreeSelectionListener​(
TreeSelectionListener
x)
```

Adds x to the list of listeners that are notified each time the
set of selected TreePaths changes.

**Parameters:** x

- the new listener to be added

---

#### addTreeSelectionListener

void addTreeSelectionListener​(

TreeSelectionListener

x)

Adds x to the list of listeners that are notified each time the
set of selected TreePaths changes.

removeTreeSelectionListener

```java
void removeTreeSelectionListener​(
TreeSelectionListener
x)
```

Removes x from the list of listeners that are notified each time
the set of selected TreePaths changes.

**Parameters:** x

- the listener to remove

---

#### removeTreeSelectionListener

void removeTreeSelectionListener​(

TreeSelectionListener

x)

Removes x from the list of listeners that are notified each time
the set of selected TreePaths changes.

---

