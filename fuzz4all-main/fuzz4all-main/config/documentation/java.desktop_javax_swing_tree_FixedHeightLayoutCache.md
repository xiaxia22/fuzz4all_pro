# Class FixedHeightLayoutCache

**Source:** `java.desktop\javax\swing\tree\FixedHeightLayoutCache.html`

### Class Description

```java
public class
FixedHeightLayoutCache

extends
AbstractLayoutCache
```

NOTE: This will become more open in a future release.

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

**All Implemented Interfaces:** RowMapper

---

### Field Details

*No entries found.*

### Constructor Details

#### public FixedHeightLayoutCache()

Constructs a

FixedHeightLayoutCache

.

---

### Method Details

#### public void setModel​(
TreeModel
newModel)

Sets the TreeModel that will provide the data.

**Overrides:**
- setModel

in class

AbstractLayoutCache

**Parameters:**
- newModel

- the TreeModel that is to provide the data

---

#### public void setRootVisible​(boolean rootVisible)

Determines whether or not the root node from
the TreeModel is visible.

**Overrides:**
- setRootVisible

in class

AbstractLayoutCache

**Parameters:**
- rootVisible

- true if the root node of the tree is to be displayed

**See Also:**
- AbstractLayoutCache.rootVisible

---

#### public void setRowHeight​(int rowHeight)

Sets the height of each cell. If rowHeight is less than or equal to
0 this will throw an IllegalArgumentException.

**Overrides:**
- setRowHeight

in class

AbstractLayoutCache

**Parameters:**
- rowHeight

- the height of each cell, in pixels

---

#### public int getRowCount()

Returns the number of visible rows.

**Specified by:**
- getRowCount

in class

AbstractLayoutCache

**Returns:**
- the number of rows being displayed

---

#### public void invalidatePathBounds​(
TreePath
path)

Does nothing, FixedHeightLayoutCache doesn't cache width, and that
is all that could change.

**Specified by:**
- invalidatePathBounds

in class

AbstractLayoutCache

**Parameters:**
- path

- the path being updated

---

#### public void invalidateSizes()

Informs the TreeState that it needs to recalculate all the sizes
it is referencing.

**Specified by:**
- invalidateSizes

in class

AbstractLayoutCache

---

#### public boolean isExpanded​(
TreePath
path)

Returns true if the value identified by row is currently expanded.

**Specified by:**
- isExpanded

in class

AbstractLayoutCache

**Parameters:**
- path

- TreePath to check

**Returns:**
- whether TreePath is expanded

---

#### public
Rectangle
getBounds​(
TreePath
path,

Rectangle
placeIn)

Returns a rectangle giving the bounds needed to draw path.

**Specified by:**
- getBounds

in class

AbstractLayoutCache

**Parameters:**
- path

- a TreePath specifying a node
- placeIn

- a Rectangle object giving the available space

**Returns:**
- a Rectangle object specifying the space to be used

---

#### public
TreePath
getPathForRow​(int row)

Returns the path for passed in row. If row is not visible
null is returned.

**Specified by:**
- getPathForRow

in class

AbstractLayoutCache

**Parameters:**
- row

- the row being queried

**Returns:**
- the

TreePath

for the given row

---

#### public int getRowForPath​(
TreePath
path)

Returns the row that the last item identified in path is visible
at. Will return -1 if any of the elements in path are not
currently visible.

**Specified by:**
- getRowForPath

in class

AbstractLayoutCache

**Parameters:**
- path

- the

TreePath

being queried

**Returns:**
- the row where the last item in path is visible or -1
if any elements in path aren't currently visible

---

#### public
TreePath
getPathClosestTo​(int x,
int y)

Returns the path to the node that is closest to x,y. If
there is nothing currently visible this will return null, otherwise
it'll always return a valid path. If you need to test if the
returned object is exactly at x, y you should get the bounds for
the returned path and test x, y against that.

**Specified by:**
- getPathClosestTo

in class

AbstractLayoutCache

**Parameters:**
- x

- the horizontal component of the desired location
- y

- the vertical component of the desired location

**Returns:**
- the

TreePath

closest to the specified point

---

#### public int getVisibleChildCount​(
TreePath
path)

Returns the number of visible children for row.

**Specified by:**
- getVisibleChildCount

in class

AbstractLayoutCache

**Parameters:**
- path

- the path being queried

**Returns:**
- the number of visible children for the specified path

---

#### public
Enumeration
<
TreePath
> getVisiblePathsFrom​(
TreePath
path)

Returns an Enumerator that increments over the visible paths
starting at the passed in location. The ordering of the enumeration
is based on how the paths are displayed.

**Specified by:**
- getVisiblePathsFrom

in class

AbstractLayoutCache

**Parameters:**
- path

- the starting location for the enumeration

**Returns:**
- the

Enumerator

starting at the desired location

---

#### public void setExpandedState​(
TreePath
path,
boolean isExpanded)

Marks the path

path

expanded state to

isExpanded

.

**Specified by:**
- setExpandedState

in class

AbstractLayoutCache

**Parameters:**
- path

- the path being expanded or collapsed
- isExpanded

- true if the path should be expanded, false otherwise

---

#### public boolean getExpandedState​(
TreePath
path)

Returns true if the path is expanded, and visible.

**Specified by:**
- getExpandedState

in class

AbstractLayoutCache

**Parameters:**
- path

- the path being queried

**Returns:**
- true if the path is expanded and visible, false otherwise

---

#### public void treeNodesChanged​(
TreeModelEvent
e)

Invoked after a node (or a set of siblings) has changed in some
way. The node(s) have not changed locations in the tree or
altered their children arrays, but other attributes have
changed and may affect presentation. Example: the name of a
file has changed, but it is in the same location in the file
system.

e.path() returns the path the parent of the changed node(s).

e.childIndices() returns the index(es) of the changed node(s).

**Specified by:**
- treeNodesChanged

in class

AbstractLayoutCache

**Parameters:**
- e

- the

TreeModelEvent

---

#### public void treeNodesInserted​(
TreeModelEvent
e)

Invoked after nodes have been inserted into the tree.

e.path() returns the parent of the new nodes

e.childIndices() returns the indices of the new nodes in
ascending order.

**Specified by:**
- treeNodesInserted

in class

AbstractLayoutCache

**Parameters:**
- e

- the

TreeModelEvent

---

#### public void treeNodesRemoved​(
TreeModelEvent
e)

Invoked after nodes have been removed from the tree. Note that
if a subtree is removed from the tree, this method may only be
invoked once for the root of the removed subtree, not once for
each individual set of siblings removed.

e.path() returns the former parent of the deleted nodes.

e.childIndices() returns the indices the nodes had before they were deleted in ascending order.

**Specified by:**
- treeNodesRemoved

in class

AbstractLayoutCache

**Parameters:**
- e

- the

TreeModelEvent

---

#### public void treeStructureChanged​(
TreeModelEvent
e)

Invoked after the tree has drastically changed structure from a
given node down. If the path returned by e.getPath() is of length
one and the first element does not identify the current root node
the first element should become the new root of the tree.

e.path() holds the path to the node.

e.childIndices() returns null.

**Specified by:**
- treeStructureChanged

in class

AbstractLayoutCache

**Parameters:**
- e

- the

TreeModelEvent

---

### Additional Sections

#### Class FixedHeightLayoutCache

java.lang.Object

- javax.swing.tree.AbstractLayoutCache
- - javax.swing.tree.FixedHeightLayoutCache

javax.swing.tree.AbstractLayoutCache

- javax.swing.tree.FixedHeightLayoutCache

javax.swing.tree.FixedHeightLayoutCache

**All Implemented Interfaces:** RowMapper

```java
public class
FixedHeightLayoutCache

extends
AbstractLayoutCache
```

NOTE: This will become more open in a future release.

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

public class

FixedHeightLayoutCache

extends

AbstractLayoutCache

NOTE: This will become more open in a future release.

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

- Nested classes/interfaces declared in class javax.swing.tree.

AbstractLayoutCache

AbstractLayoutCache.NodeDimensions

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.swing.tree.

AbstractLayoutCache

nodeDimensions

,

rootVisible

,

rowHeight

,

treeModel

,

treeSelectionModel

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FixedHeightLayoutCache

()

Constructs a

FixedHeightLayoutCache

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Rectangle

getBounds

​(

TreePath

path,

Rectangle

placeIn)

Returns a rectangle giving the bounds needed to draw path.

boolean

getExpandedState

​(

TreePath

path)

Returns true if the path is expanded, and visible.

TreePath

getPathClosestTo

​(int x,
int y)

Returns the path to the node that is closest to x,y.

TreePath

getPathForRow

​(int row)

Returns the path for passed in row.

int

getRowCount

()

Returns the number of visible rows.

int

getRowForPath

​(

TreePath

path)

Returns the row that the last item identified in path is visible
at.

int

getVisibleChildCount

​(

TreePath

path)

Returns the number of visible children for row.

Enumeration

<

TreePath

>

getVisiblePathsFrom

​(

TreePath

path)

Returns an Enumerator that increments over the visible paths
starting at the passed in location.

void

invalidatePathBounds

​(

TreePath

path)

Does nothing, FixedHeightLayoutCache doesn't cache width, and that
is all that could change.

void

invalidateSizes

()

Informs the TreeState that it needs to recalculate all the sizes
it is referencing.

boolean

isExpanded

​(

TreePath

path)

Returns true if the value identified by row is currently expanded.

void

setExpandedState

​(

TreePath

path,
boolean isExpanded)

Marks the path

path

expanded state to

isExpanded

.

void

setModel

​(

TreeModel

newModel)

Sets the TreeModel that will provide the data.

void

setRootVisible

​(boolean rootVisible)

Determines whether or not the root node from
the TreeModel is visible.

void

setRowHeight

​(int rowHeight)

Sets the height of each cell.

void

treeNodesChanged

​(

TreeModelEvent

e)

Invoked after a node (or a set of siblings) has changed in some
way.

void

treeNodesInserted

​(

TreeModelEvent

e)

Invoked after nodes have been inserted into the tree.

void

treeNodesRemoved

​(

TreeModelEvent

e)

Invoked after nodes have been removed from the tree.

void

treeStructureChanged

​(

TreeModelEvent

e)

Invoked after the tree has drastically changed structure from a
given node down.

- Methods declared in class javax.swing.tree.

AbstractLayoutCache

getModel

,

getNodeDimensions

,

getNodeDimensions

,

getPreferredHeight

,

getPreferredWidth

,

getRowHeight

,

getRowsForPaths

,

getSelectionModel

,

isFixedRowHeight

,

isRootVisible

,

setNodeDimensions

,

setSelectionModel

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

toString

,

wait

,

wait

,

wait

Nested Class Summary

- Nested classes/interfaces declared in class javax.swing.tree.

AbstractLayoutCache

AbstractLayoutCache.NodeDimensions

---

#### Nested Class Summary

Nested classes/interfaces declared in class javax.swing.tree.

AbstractLayoutCache

AbstractLayoutCache.NodeDimensions

---

#### Nested classes/interfaces declared in class javax.swing.tree. AbstractLayoutCache

Field Summary

- Fields declared in class javax.swing.tree.

AbstractLayoutCache

nodeDimensions

,

rootVisible

,

rowHeight

,

treeModel

,

treeSelectionModel

---

#### Field Summary

Fields declared in class javax.swing.tree.

AbstractLayoutCache

nodeDimensions

,

rootVisible

,

rowHeight

,

treeModel

,

treeSelectionModel

---

#### Fields declared in class javax.swing.tree. AbstractLayoutCache

Constructor Summary

Constructors

Constructor

Description

FixedHeightLayoutCache

()

Constructs a

FixedHeightLayoutCache

.

---

#### Constructor Summary

Constructs a

FixedHeightLayoutCache

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Rectangle

getBounds

​(

TreePath

path,

Rectangle

placeIn)

Returns a rectangle giving the bounds needed to draw path.

boolean

getExpandedState

​(

TreePath

path)

Returns true if the path is expanded, and visible.

TreePath

getPathClosestTo

​(int x,
int y)

Returns the path to the node that is closest to x,y.

TreePath

getPathForRow

​(int row)

Returns the path for passed in row.

int

getRowCount

()

Returns the number of visible rows.

int

getRowForPath

​(

TreePath

path)

Returns the row that the last item identified in path is visible
at.

int

getVisibleChildCount

​(

TreePath

path)

Returns the number of visible children for row.

Enumeration

<

TreePath

>

getVisiblePathsFrom

​(

TreePath

path)

Returns an Enumerator that increments over the visible paths
starting at the passed in location.

void

invalidatePathBounds

​(

TreePath

path)

Does nothing, FixedHeightLayoutCache doesn't cache width, and that
is all that could change.

void

invalidateSizes

()

Informs the TreeState that it needs to recalculate all the sizes
it is referencing.

boolean

isExpanded

​(

TreePath

path)

Returns true if the value identified by row is currently expanded.

void

setExpandedState

​(

TreePath

path,
boolean isExpanded)

Marks the path

path

expanded state to

isExpanded

.

void

setModel

​(

TreeModel

newModel)

Sets the TreeModel that will provide the data.

void

setRootVisible

​(boolean rootVisible)

Determines whether or not the root node from
the TreeModel is visible.

void

setRowHeight

​(int rowHeight)

Sets the height of each cell.

void

treeNodesChanged

​(

TreeModelEvent

e)

Invoked after a node (or a set of siblings) has changed in some
way.

void

treeNodesInserted

​(

TreeModelEvent

e)

Invoked after nodes have been inserted into the tree.

void

treeNodesRemoved

​(

TreeModelEvent

e)

Invoked after nodes have been removed from the tree.

void

treeStructureChanged

​(

TreeModelEvent

e)

Invoked after the tree has drastically changed structure from a
given node down.

- Methods declared in class javax.swing.tree.

AbstractLayoutCache

getModel

,

getNodeDimensions

,

getNodeDimensions

,

getPreferredHeight

,

getPreferredWidth

,

getRowHeight

,

getRowsForPaths

,

getSelectionModel

,

isFixedRowHeight

,

isRootVisible

,

setNodeDimensions

,

setSelectionModel

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns a rectangle giving the bounds needed to draw path.

Returns true if the path is expanded, and visible.

Returns the path to the node that is closest to x,y.

Returns the path for passed in row.

Returns the number of visible rows.

Returns the row that the last item identified in path is visible
at.

Returns the number of visible children for row.

Returns an Enumerator that increments over the visible paths
starting at the passed in location.

Does nothing, FixedHeightLayoutCache doesn't cache width, and that
is all that could change.

Informs the TreeState that it needs to recalculate all the sizes
it is referencing.

Returns true if the value identified by row is currently expanded.

Marks the path

path

expanded state to

isExpanded

.

Sets the TreeModel that will provide the data.

Determines whether or not the root node from
the TreeModel is visible.

Sets the height of each cell.

Invoked after a node (or a set of siblings) has changed in some
way.

Invoked after nodes have been inserted into the tree.

Invoked after nodes have been removed from the tree.

Invoked after the tree has drastically changed structure from a
given node down.

Methods declared in class javax.swing.tree.

AbstractLayoutCache

getModel

,

getNodeDimensions

,

getNodeDimensions

,

getPreferredHeight

,

getPreferredWidth

,

getRowHeight

,

getRowsForPaths

,

getSelectionModel

,

isFixedRowHeight

,

isRootVisible

,

setNodeDimensions

,

setSelectionModel

---

#### Methods declared in class javax.swing.tree. AbstractLayoutCache

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

toString

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

- FixedHeightLayoutCache

```java
public FixedHeightLayoutCache()
```

Constructs a

FixedHeightLayoutCache

.

============ METHOD DETAIL ==========

- Method Detail

- setModel

```java
public void setModel​(
TreeModel
newModel)
```

Sets the TreeModel that will provide the data.

**Overrides:** setModel

in class

AbstractLayoutCache
**Parameters:** newModel

- the TreeModel that is to provide the data

- setRootVisible

```java
public void setRootVisible​(boolean rootVisible)
```

Determines whether or not the root node from
the TreeModel is visible.

**Overrides:** setRootVisible

in class

AbstractLayoutCache
**Parameters:** rootVisible

- true if the root node of the tree is to be displayed
**See Also:** AbstractLayoutCache.rootVisible

- setRowHeight

```java
public void setRowHeight​(int rowHeight)
```

Sets the height of each cell. If rowHeight is less than or equal to
0 this will throw an IllegalArgumentException.

**Overrides:** setRowHeight

in class

AbstractLayoutCache
**Parameters:** rowHeight

- the height of each cell, in pixels

- getRowCount

```java
public int getRowCount()
```

Returns the number of visible rows.

**Specified by:** getRowCount

in class

AbstractLayoutCache
**Returns:** the number of rows being displayed

- invalidatePathBounds

```java
public void invalidatePathBounds​(
TreePath
path)
```

Does nothing, FixedHeightLayoutCache doesn't cache width, and that
is all that could change.

**Specified by:** invalidatePathBounds

in class

AbstractLayoutCache
**Parameters:** path

- the path being updated

- invalidateSizes

```java
public void invalidateSizes()
```

Informs the TreeState that it needs to recalculate all the sizes
it is referencing.

**Specified by:** invalidateSizes

in class

AbstractLayoutCache

- isExpanded

```java
public boolean isExpanded​(
TreePath
path)
```

Returns true if the value identified by row is currently expanded.

**Specified by:** isExpanded

in class

AbstractLayoutCache
**Parameters:** path

- TreePath to check
**Returns:** whether TreePath is expanded

- getBounds

```java
public
Rectangle
getBounds​(
TreePath
path,

Rectangle
placeIn)
```

Returns a rectangle giving the bounds needed to draw path.

**Specified by:** getBounds

in class

AbstractLayoutCache
**Parameters:** path

- a TreePath specifying a node
**Parameters:** placeIn

- a Rectangle object giving the available space
**Returns:** a Rectangle object specifying the space to be used

- getPathForRow

```java
public
TreePath
getPathForRow​(int row)
```

Returns the path for passed in row. If row is not visible
null is returned.

**Specified by:** getPathForRow

in class

AbstractLayoutCache
**Parameters:** row

- the row being queried
**Returns:** the

TreePath

for the given row

- getRowForPath

```java
public int getRowForPath​(
TreePath
path)
```

Returns the row that the last item identified in path is visible
at. Will return -1 if any of the elements in path are not
currently visible.

**Specified by:** getRowForPath

in class

AbstractLayoutCache
**Parameters:** path

- the

TreePath

being queried
**Returns:** the row where the last item in path is visible or -1
if any elements in path aren't currently visible

- getPathClosestTo

```java
public
TreePath
getPathClosestTo​(int x,
int y)
```

Returns the path to the node that is closest to x,y. If
there is nothing currently visible this will return null, otherwise
it'll always return a valid path. If you need to test if the
returned object is exactly at x, y you should get the bounds for
the returned path and test x, y against that.

**Specified by:** getPathClosestTo

in class

AbstractLayoutCache
**Parameters:** x

- the horizontal component of the desired location
**Parameters:** y

- the vertical component of the desired location
**Returns:** the

TreePath

closest to the specified point

- getVisibleChildCount

```java
public int getVisibleChildCount​(
TreePath
path)
```

Returns the number of visible children for row.

**Specified by:** getVisibleChildCount

in class

AbstractLayoutCache
**Parameters:** path

- the path being queried
**Returns:** the number of visible children for the specified path

- getVisiblePathsFrom

```java
public
Enumeration
<
TreePath
> getVisiblePathsFrom​(
TreePath
path)
```

Returns an Enumerator that increments over the visible paths
starting at the passed in location. The ordering of the enumeration
is based on how the paths are displayed.

**Specified by:** getVisiblePathsFrom

in class

AbstractLayoutCache
**Parameters:** path

- the starting location for the enumeration
**Returns:** the

Enumerator

starting at the desired location

- setExpandedState

```java
public void setExpandedState​(
TreePath
path,
boolean isExpanded)
```

Marks the path

path

expanded state to

isExpanded

.

**Specified by:** setExpandedState

in class

AbstractLayoutCache
**Parameters:** path

- the path being expanded or collapsed
**Parameters:** isExpanded

- true if the path should be expanded, false otherwise

- getExpandedState

```java
public boolean getExpandedState​(
TreePath
path)
```

Returns true if the path is expanded, and visible.

**Specified by:** getExpandedState

in class

AbstractLayoutCache
**Parameters:** path

- the path being queried
**Returns:** true if the path is expanded and visible, false otherwise

- treeNodesChanged

```java
public void treeNodesChanged​(
TreeModelEvent
e)
```

Invoked after a node (or a set of siblings) has changed in some
way. The node(s) have not changed locations in the tree or
altered their children arrays, but other attributes have
changed and may affect presentation. Example: the name of a
file has changed, but it is in the same location in the file
system.

e.path() returns the path the parent of the changed node(s).

e.childIndices() returns the index(es) of the changed node(s).

**Specified by:** treeNodesChanged

in class

AbstractLayoutCache
**Parameters:** e

- the

TreeModelEvent

- treeNodesInserted

```java
public void treeNodesInserted​(
TreeModelEvent
e)
```

Invoked after nodes have been inserted into the tree.

e.path() returns the parent of the new nodes

e.childIndices() returns the indices of the new nodes in
ascending order.

**Specified by:** treeNodesInserted

in class

AbstractLayoutCache
**Parameters:** e

- the

TreeModelEvent

- treeNodesRemoved

```java
public void treeNodesRemoved​(
TreeModelEvent
e)
```

Invoked after nodes have been removed from the tree. Note that
if a subtree is removed from the tree, this method may only be
invoked once for the root of the removed subtree, not once for
each individual set of siblings removed.

e.path() returns the former parent of the deleted nodes.

e.childIndices() returns the indices the nodes had before they were deleted in ascending order.

**Specified by:** treeNodesRemoved

in class

AbstractLayoutCache
**Parameters:** e

- the

TreeModelEvent

- treeStructureChanged

```java
public void treeStructureChanged​(
TreeModelEvent
e)
```

Invoked after the tree has drastically changed structure from a
given node down. If the path returned by e.getPath() is of length
one and the first element does not identify the current root node
the first element should become the new root of the tree.

e.path() holds the path to the node.

e.childIndices() returns null.

**Specified by:** treeStructureChanged

in class

AbstractLayoutCache
**Parameters:** e

- the

TreeModelEvent

Constructor Detail

- FixedHeightLayoutCache

```java
public FixedHeightLayoutCache()
```

Constructs a

FixedHeightLayoutCache

.

---

#### Constructor Detail

FixedHeightLayoutCache

```java
public FixedHeightLayoutCache()
```

Constructs a

FixedHeightLayoutCache

.

---

#### FixedHeightLayoutCache

public FixedHeightLayoutCache()

Constructs a

FixedHeightLayoutCache

.

Method Detail

- setModel

```java
public void setModel​(
TreeModel
newModel)
```

Sets the TreeModel that will provide the data.

**Overrides:** setModel

in class

AbstractLayoutCache
**Parameters:** newModel

- the TreeModel that is to provide the data

- setRootVisible

```java
public void setRootVisible​(boolean rootVisible)
```

Determines whether or not the root node from
the TreeModel is visible.

**Overrides:** setRootVisible

in class

AbstractLayoutCache
**Parameters:** rootVisible

- true if the root node of the tree is to be displayed
**See Also:** AbstractLayoutCache.rootVisible

- setRowHeight

```java
public void setRowHeight​(int rowHeight)
```

Sets the height of each cell. If rowHeight is less than or equal to
0 this will throw an IllegalArgumentException.

**Overrides:** setRowHeight

in class

AbstractLayoutCache
**Parameters:** rowHeight

- the height of each cell, in pixels

- getRowCount

```java
public int getRowCount()
```

Returns the number of visible rows.

**Specified by:** getRowCount

in class

AbstractLayoutCache
**Returns:** the number of rows being displayed

- invalidatePathBounds

```java
public void invalidatePathBounds​(
TreePath
path)
```

Does nothing, FixedHeightLayoutCache doesn't cache width, and that
is all that could change.

**Specified by:** invalidatePathBounds

in class

AbstractLayoutCache
**Parameters:** path

- the path being updated

- invalidateSizes

```java
public void invalidateSizes()
```

Informs the TreeState that it needs to recalculate all the sizes
it is referencing.

**Specified by:** invalidateSizes

in class

AbstractLayoutCache

- isExpanded

```java
public boolean isExpanded​(
TreePath
path)
```

Returns true if the value identified by row is currently expanded.

**Specified by:** isExpanded

in class

AbstractLayoutCache
**Parameters:** path

- TreePath to check
**Returns:** whether TreePath is expanded

- getBounds

```java
public
Rectangle
getBounds​(
TreePath
path,

Rectangle
placeIn)
```

Returns a rectangle giving the bounds needed to draw path.

**Specified by:** getBounds

in class

AbstractLayoutCache
**Parameters:** path

- a TreePath specifying a node
**Parameters:** placeIn

- a Rectangle object giving the available space
**Returns:** a Rectangle object specifying the space to be used

- getPathForRow

```java
public
TreePath
getPathForRow​(int row)
```

Returns the path for passed in row. If row is not visible
null is returned.

**Specified by:** getPathForRow

in class

AbstractLayoutCache
**Parameters:** row

- the row being queried
**Returns:** the

TreePath

for the given row

- getRowForPath

```java
public int getRowForPath​(
TreePath
path)
```

Returns the row that the last item identified in path is visible
at. Will return -1 if any of the elements in path are not
currently visible.

**Specified by:** getRowForPath

in class

AbstractLayoutCache
**Parameters:** path

- the

TreePath

being queried
**Returns:** the row where the last item in path is visible or -1
if any elements in path aren't currently visible

- getPathClosestTo

```java
public
TreePath
getPathClosestTo​(int x,
int y)
```

Returns the path to the node that is closest to x,y. If
there is nothing currently visible this will return null, otherwise
it'll always return a valid path. If you need to test if the
returned object is exactly at x, y you should get the bounds for
the returned path and test x, y against that.

**Specified by:** getPathClosestTo

in class

AbstractLayoutCache
**Parameters:** x

- the horizontal component of the desired location
**Parameters:** y

- the vertical component of the desired location
**Returns:** the

TreePath

closest to the specified point

- getVisibleChildCount

```java
public int getVisibleChildCount​(
TreePath
path)
```

Returns the number of visible children for row.

**Specified by:** getVisibleChildCount

in class

AbstractLayoutCache
**Parameters:** path

- the path being queried
**Returns:** the number of visible children for the specified path

- getVisiblePathsFrom

```java
public
Enumeration
<
TreePath
> getVisiblePathsFrom​(
TreePath
path)
```

Returns an Enumerator that increments over the visible paths
starting at the passed in location. The ordering of the enumeration
is based on how the paths are displayed.

**Specified by:** getVisiblePathsFrom

in class

AbstractLayoutCache
**Parameters:** path

- the starting location for the enumeration
**Returns:** the

Enumerator

starting at the desired location

- setExpandedState

```java
public void setExpandedState​(
TreePath
path,
boolean isExpanded)
```

Marks the path

path

expanded state to

isExpanded

.

**Specified by:** setExpandedState

in class

AbstractLayoutCache
**Parameters:** path

- the path being expanded or collapsed
**Parameters:** isExpanded

- true if the path should be expanded, false otherwise

- getExpandedState

```java
public boolean getExpandedState​(
TreePath
path)
```

Returns true if the path is expanded, and visible.

**Specified by:** getExpandedState

in class

AbstractLayoutCache
**Parameters:** path

- the path being queried
**Returns:** true if the path is expanded and visible, false otherwise

- treeNodesChanged

```java
public void treeNodesChanged​(
TreeModelEvent
e)
```

Invoked after a node (or a set of siblings) has changed in some
way. The node(s) have not changed locations in the tree or
altered their children arrays, but other attributes have
changed and may affect presentation. Example: the name of a
file has changed, but it is in the same location in the file
system.

e.path() returns the path the parent of the changed node(s).

e.childIndices() returns the index(es) of the changed node(s).

**Specified by:** treeNodesChanged

in class

AbstractLayoutCache
**Parameters:** e

- the

TreeModelEvent

- treeNodesInserted

```java
public void treeNodesInserted​(
TreeModelEvent
e)
```

Invoked after nodes have been inserted into the tree.

e.path() returns the parent of the new nodes

e.childIndices() returns the indices of the new nodes in
ascending order.

**Specified by:** treeNodesInserted

in class

AbstractLayoutCache
**Parameters:** e

- the

TreeModelEvent

- treeNodesRemoved

```java
public void treeNodesRemoved​(
TreeModelEvent
e)
```

Invoked after nodes have been removed from the tree. Note that
if a subtree is removed from the tree, this method may only be
invoked once for the root of the removed subtree, not once for
each individual set of siblings removed.

e.path() returns the former parent of the deleted nodes.

e.childIndices() returns the indices the nodes had before they were deleted in ascending order.

**Specified by:** treeNodesRemoved

in class

AbstractLayoutCache
**Parameters:** e

- the

TreeModelEvent

- treeStructureChanged

```java
public void treeStructureChanged​(
TreeModelEvent
e)
```

Invoked after the tree has drastically changed structure from a
given node down. If the path returned by e.getPath() is of length
one and the first element does not identify the current root node
the first element should become the new root of the tree.

e.path() holds the path to the node.

e.childIndices() returns null.

**Specified by:** treeStructureChanged

in class

AbstractLayoutCache
**Parameters:** e

- the

TreeModelEvent

---

#### Method Detail

setModel

```java
public void setModel​(
TreeModel
newModel)
```

Sets the TreeModel that will provide the data.

**Overrides:** setModel

in class

AbstractLayoutCache
**Parameters:** newModel

- the TreeModel that is to provide the data

---

#### setModel

public void setModel​(

TreeModel

newModel)

Sets the TreeModel that will provide the data.

setRootVisible

```java
public void setRootVisible​(boolean rootVisible)
```

Determines whether or not the root node from
the TreeModel is visible.

**Overrides:** setRootVisible

in class

AbstractLayoutCache
**Parameters:** rootVisible

- true if the root node of the tree is to be displayed
**See Also:** AbstractLayoutCache.rootVisible

---

#### setRootVisible

public void setRootVisible​(boolean rootVisible)

Determines whether or not the root node from
the TreeModel is visible.

setRowHeight

```java
public void setRowHeight​(int rowHeight)
```

Sets the height of each cell. If rowHeight is less than or equal to
0 this will throw an IllegalArgumentException.

**Overrides:** setRowHeight

in class

AbstractLayoutCache
**Parameters:** rowHeight

- the height of each cell, in pixels

---

#### setRowHeight

public void setRowHeight​(int rowHeight)

Sets the height of each cell. If rowHeight is less than or equal to
0 this will throw an IllegalArgumentException.

getRowCount

```java
public int getRowCount()
```

Returns the number of visible rows.

**Specified by:** getRowCount

in class

AbstractLayoutCache
**Returns:** the number of rows being displayed

---

#### getRowCount

public int getRowCount()

Returns the number of visible rows.

invalidatePathBounds

```java
public void invalidatePathBounds​(
TreePath
path)
```

Does nothing, FixedHeightLayoutCache doesn't cache width, and that
is all that could change.

**Specified by:** invalidatePathBounds

in class

AbstractLayoutCache
**Parameters:** path

- the path being updated

---

#### invalidatePathBounds

public void invalidatePathBounds​(

TreePath

path)

Does nothing, FixedHeightLayoutCache doesn't cache width, and that
is all that could change.

invalidateSizes

```java
public void invalidateSizes()
```

Informs the TreeState that it needs to recalculate all the sizes
it is referencing.

**Specified by:** invalidateSizes

in class

AbstractLayoutCache

---

#### invalidateSizes

public void invalidateSizes()

Informs the TreeState that it needs to recalculate all the sizes
it is referencing.

isExpanded

```java
public boolean isExpanded​(
TreePath
path)
```

Returns true if the value identified by row is currently expanded.

**Specified by:** isExpanded

in class

AbstractLayoutCache
**Parameters:** path

- TreePath to check
**Returns:** whether TreePath is expanded

---

#### isExpanded

public boolean isExpanded​(

TreePath

path)

Returns true if the value identified by row is currently expanded.

getBounds

```java
public
Rectangle
getBounds​(
TreePath
path,

Rectangle
placeIn)
```

Returns a rectangle giving the bounds needed to draw path.

**Specified by:** getBounds

in class

AbstractLayoutCache
**Parameters:** path

- a TreePath specifying a node
**Parameters:** placeIn

- a Rectangle object giving the available space
**Returns:** a Rectangle object specifying the space to be used

---

#### getBounds

public

Rectangle

getBounds​(

TreePath

path,

Rectangle

placeIn)

Returns a rectangle giving the bounds needed to draw path.

getPathForRow

```java
public
TreePath
getPathForRow​(int row)
```

Returns the path for passed in row. If row is not visible
null is returned.

**Specified by:** getPathForRow

in class

AbstractLayoutCache
**Parameters:** row

- the row being queried
**Returns:** the

TreePath

for the given row

---

#### getPathForRow

public

TreePath

getPathForRow​(int row)

Returns the path for passed in row. If row is not visible
null is returned.

getRowForPath

```java
public int getRowForPath​(
TreePath
path)
```

Returns the row that the last item identified in path is visible
at. Will return -1 if any of the elements in path are not
currently visible.

**Specified by:** getRowForPath

in class

AbstractLayoutCache
**Parameters:** path

- the

TreePath

being queried
**Returns:** the row where the last item in path is visible or -1
if any elements in path aren't currently visible

---

#### getRowForPath

public int getRowForPath​(

TreePath

path)

Returns the row that the last item identified in path is visible
at. Will return -1 if any of the elements in path are not
currently visible.

getPathClosestTo

```java
public
TreePath
getPathClosestTo​(int x,
int y)
```

Returns the path to the node that is closest to x,y. If
there is nothing currently visible this will return null, otherwise
it'll always return a valid path. If you need to test if the
returned object is exactly at x, y you should get the bounds for
the returned path and test x, y against that.

**Specified by:** getPathClosestTo

in class

AbstractLayoutCache
**Parameters:** x

- the horizontal component of the desired location
**Parameters:** y

- the vertical component of the desired location
**Returns:** the

TreePath

closest to the specified point

---

#### getPathClosestTo

public

TreePath

getPathClosestTo​(int x,
int y)

Returns the path to the node that is closest to x,y. If
there is nothing currently visible this will return null, otherwise
it'll always return a valid path. If you need to test if the
returned object is exactly at x, y you should get the bounds for
the returned path and test x, y against that.

getVisibleChildCount

```java
public int getVisibleChildCount​(
TreePath
path)
```

Returns the number of visible children for row.

**Specified by:** getVisibleChildCount

in class

AbstractLayoutCache
**Parameters:** path

- the path being queried
**Returns:** the number of visible children for the specified path

---

#### getVisibleChildCount

public int getVisibleChildCount​(

TreePath

path)

Returns the number of visible children for row.

getVisiblePathsFrom

```java
public
Enumeration
<
TreePath
> getVisiblePathsFrom​(
TreePath
path)
```

Returns an Enumerator that increments over the visible paths
starting at the passed in location. The ordering of the enumeration
is based on how the paths are displayed.

**Specified by:** getVisiblePathsFrom

in class

AbstractLayoutCache
**Parameters:** path

- the starting location for the enumeration
**Returns:** the

Enumerator

starting at the desired location

---

#### getVisiblePathsFrom

public

Enumeration

<

TreePath

> getVisiblePathsFrom​(

TreePath

path)

Returns an Enumerator that increments over the visible paths
starting at the passed in location. The ordering of the enumeration
is based on how the paths are displayed.

setExpandedState

```java
public void setExpandedState​(
TreePath
path,
boolean isExpanded)
```

Marks the path

path

expanded state to

isExpanded

.

**Specified by:** setExpandedState

in class

AbstractLayoutCache
**Parameters:** path

- the path being expanded or collapsed
**Parameters:** isExpanded

- true if the path should be expanded, false otherwise

---

#### setExpandedState

public void setExpandedState​(

TreePath

path,
boolean isExpanded)

Marks the path

path

expanded state to

isExpanded

.

getExpandedState

```java
public boolean getExpandedState​(
TreePath
path)
```

Returns true if the path is expanded, and visible.

**Specified by:** getExpandedState

in class

AbstractLayoutCache
**Parameters:** path

- the path being queried
**Returns:** true if the path is expanded and visible, false otherwise

---

#### getExpandedState

public boolean getExpandedState​(

TreePath

path)

Returns true if the path is expanded, and visible.

treeNodesChanged

```java
public void treeNodesChanged​(
TreeModelEvent
e)
```

Invoked after a node (or a set of siblings) has changed in some
way. The node(s) have not changed locations in the tree or
altered their children arrays, but other attributes have
changed and may affect presentation. Example: the name of a
file has changed, but it is in the same location in the file
system.

e.path() returns the path the parent of the changed node(s).

e.childIndices() returns the index(es) of the changed node(s).

**Specified by:** treeNodesChanged

in class

AbstractLayoutCache
**Parameters:** e

- the

TreeModelEvent

---

#### treeNodesChanged

public void treeNodesChanged​(

TreeModelEvent

e)

Invoked after a node (or a set of siblings) has changed in some
way. The node(s) have not changed locations in the tree or
altered their children arrays, but other attributes have
changed and may affect presentation. Example: the name of a
file has changed, but it is in the same location in the file
system.

e.path() returns the path the parent of the changed node(s).

e.childIndices() returns the index(es) of the changed node(s).

Invoked after a node (or a set of siblings) has changed in some
way. The node(s) have not changed locations in the tree or
altered their children arrays, but other attributes have
changed and may affect presentation. Example: the name of a
file has changed, but it is in the same location in the file
system.

e.path() returns the path the parent of the changed node(s).

e.childIndices() returns the index(es) of the changed node(s).

treeNodesInserted

```java
public void treeNodesInserted​(
TreeModelEvent
e)
```

Invoked after nodes have been inserted into the tree.

e.path() returns the parent of the new nodes

e.childIndices() returns the indices of the new nodes in
ascending order.

**Specified by:** treeNodesInserted

in class

AbstractLayoutCache
**Parameters:** e

- the

TreeModelEvent

---

#### treeNodesInserted

public void treeNodesInserted​(

TreeModelEvent

e)

Invoked after nodes have been inserted into the tree.

e.path() returns the parent of the new nodes

e.childIndices() returns the indices of the new nodes in
ascending order.

Invoked after nodes have been inserted into the tree.

e.path() returns the parent of the new nodes

e.childIndices() returns the indices of the new nodes in
ascending order.

e.childIndices() returns the indices of the new nodes in
ascending order.

treeNodesRemoved

```java
public void treeNodesRemoved​(
TreeModelEvent
e)
```

Invoked after nodes have been removed from the tree. Note that
if a subtree is removed from the tree, this method may only be
invoked once for the root of the removed subtree, not once for
each individual set of siblings removed.

e.path() returns the former parent of the deleted nodes.

e.childIndices() returns the indices the nodes had before they were deleted in ascending order.

**Specified by:** treeNodesRemoved

in class

AbstractLayoutCache
**Parameters:** e

- the

TreeModelEvent

---

#### treeNodesRemoved

public void treeNodesRemoved​(

TreeModelEvent

e)

Invoked after nodes have been removed from the tree. Note that
if a subtree is removed from the tree, this method may only be
invoked once for the root of the removed subtree, not once for
each individual set of siblings removed.

e.path() returns the former parent of the deleted nodes.

e.childIndices() returns the indices the nodes had before they were deleted in ascending order.

Invoked after nodes have been removed from the tree. Note that
if a subtree is removed from the tree, this method may only be
invoked once for the root of the removed subtree, not once for
each individual set of siblings removed.

e.path() returns the former parent of the deleted nodes.

e.childIndices() returns the indices the nodes had before they were deleted in ascending order.

treeStructureChanged

```java
public void treeStructureChanged​(
TreeModelEvent
e)
```

Invoked after the tree has drastically changed structure from a
given node down. If the path returned by e.getPath() is of length
one and the first element does not identify the current root node
the first element should become the new root of the tree.

e.path() holds the path to the node.

e.childIndices() returns null.

**Specified by:** treeStructureChanged

in class

AbstractLayoutCache
**Parameters:** e

- the

TreeModelEvent

---

#### treeStructureChanged

public void treeStructureChanged​(

TreeModelEvent

e)

Invoked after the tree has drastically changed structure from a
given node down. If the path returned by e.getPath() is of length
one and the first element does not identify the current root node
the first element should become the new root of the tree.

e.path() holds the path to the node.

e.childIndices() returns null.

e.path() holds the path to the node.

e.childIndices() returns null.

---

