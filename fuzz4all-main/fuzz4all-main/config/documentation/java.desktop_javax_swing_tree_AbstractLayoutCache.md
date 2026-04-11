# Class AbstractLayoutCache

**Source:** `java.desktop\javax\swing\tree\AbstractLayoutCache.html`

### Class Description

```java
public abstract class
AbstractLayoutCache

extends
Object

implements
RowMapper
```

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

#### protected
AbstractLayoutCache.NodeDimensions
nodeDimensions

Object responsible for getting the size of a node.

---

#### protected
TreeModel
treeModel

Model providing information.

---

#### protected
TreeSelectionModel
treeSelectionModel

Selection model.

---

#### protected boolean rootVisible

True if the root node is displayed, false if its children are
the highest visible nodes.

---

#### protected int rowHeight

Height to use for each row. If this is <= 0 the renderer will be
used to determine the height for each row.

---

### Constructor Details

#### public AbstractLayoutCache()

*No description found.*

---

### Method Details

#### public void setNodeDimensions​(
AbstractLayoutCache.NodeDimensions
nd)

Sets the renderer that is responsible for drawing nodes in the tree
and which is therefore responsible for calculating the dimensions of
individual nodes.

**Parameters:**
- nd

- a

NodeDimensions

object

---

#### public
AbstractLayoutCache.NodeDimensions
getNodeDimensions()

Returns the object that renders nodes in the tree, and which is
responsible for calculating the dimensions of individual nodes.

**Returns:**
- the

NodeDimensions

object

---

#### public void setModel​(
TreeModel
newModel)

Sets the

TreeModel

that will provide the data.

**Parameters:**
- newModel

- the

TreeModel

that is to
provide the data

---

#### public
TreeModel
getModel()

Returns the

TreeModel

that is providing the data.

**Returns:**
- the

TreeModel

that is providing the data

---

#### @BeanProperty
(
description
="Whether or not the root node from the TreeModel is visible.")
public void setRootVisible​(boolean rootVisible)

Determines whether or not the root node from
the

TreeModel

is visible.

**Parameters:**
- rootVisible

- true if the root node of the tree is to be displayed

**See Also:**
- rootVisible

---

#### public boolean isRootVisible()

Returns true if the root node of the tree is displayed.

**Returns:**
- true if the root node of the tree is displayed

**See Also:**
- rootVisible

---

#### @BeanProperty
(
description
="The height of each cell.")
public void setRowHeight​(int rowHeight)

Sets the height of each cell. If the specified value
is less than or equal to zero the current cell renderer is
queried for each row's height.

**Parameters:**
- rowHeight

- the height of each cell, in pixels

---

#### public int getRowHeight()

Returns the height of each row. If the returned value is less than
or equal to 0 the height for each row is determined by the
renderer.

**Returns:**
- the height of each row

---

#### public void setSelectionModel​(
TreeSelectionModel
newLSM)

Sets the

TreeSelectionModel

used to manage the
selection to new LSM.

**Parameters:**
- newLSM

- the new

TreeSelectionModel

---

#### public
TreeSelectionModel
getSelectionModel()

Returns the model used to maintain the selection.

**Returns:**
- the

treeSelectionModel

---

#### public int getPreferredHeight()

Returns the preferred height.

**Returns:**
- the preferred height

---

#### public int getPreferredWidth​(
Rectangle
bounds)

Returns the preferred width for the passed in region.
The region is defined by the path closest to

(bounds.x, bounds.y)

and
ends at

bounds.height + bounds.y

.
If

bounds

is

null

,
the preferred width for all the nodes
will be returned (and this may be a VERY expensive
computation).

**Parameters:**
- bounds

- the region being queried

**Returns:**
- the preferred width for the passed in region

---

#### public abstract boolean isExpanded​(
TreePath
path)

Returns true if the value identified by row is currently expanded.

**Parameters:**
- path

- TreePath to check

**Returns:**
- whether TreePath is expanded

---

#### public abstract
Rectangle
getBounds​(
TreePath
path,

Rectangle
placeIn)

Returns a rectangle giving the bounds needed to draw path.

**Parameters:**
- path

- a

TreePath

specifying a node
- placeIn

- a

Rectangle

object giving the
available space

**Returns:**
- a

Rectangle

object specifying the space to be used

---

#### public abstract
TreePath
getPathForRow​(int row)

Returns the path for passed in row. If row is not visible

null

is returned.

**Parameters:**
- row

- the row being queried

**Returns:**
- the

TreePath

for the given row

---

#### public abstract int getRowForPath​(
TreePath
path)

Returns the row that the last item identified in path is visible
at. Will return -1 if any of the elements in path are not
currently visible.

**Parameters:**
- path

- the

TreePath

being queried

**Returns:**
- the row where the last item in path is visible or -1
if any elements in path aren't currently visible

---

#### public abstract
TreePath
getPathClosestTo​(int x,
int y)

Returns the path to the node that is closest to x,y. If
there is nothing currently visible this will return

null

,
otherwise it'll always return a valid path.
If you need to test if the
returned object is exactly at x, y you should get the bounds for
the returned path and test x, y against that.

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

#### public abstract
Enumeration
<
TreePath
> getVisiblePathsFrom​(
TreePath
path)

Returns an

Enumerator

that increments over the visible
paths starting at the passed in location. The ordering of the
enumeration is based on how the paths are displayed.
The first element of the returned enumeration will be path,
unless it isn't visible,
in which case

null

will be returned.

**Parameters:**
- path

- the starting location for the enumeration

**Returns:**
- the

Enumerator

starting at the desired location

---

#### public abstract int getVisibleChildCount​(
TreePath
path)

Returns the number of visible children for row.

**Parameters:**
- path

- the path being queried

**Returns:**
- the number of visible children for the specified path

---

#### public abstract void setExpandedState​(
TreePath
path,
boolean isExpanded)

Marks the path

path

expanded state to

isExpanded

.

**Parameters:**
- path

- the path being expanded or collapsed
- isExpanded

- true if the path should be expanded, false otherwise

---

#### public abstract boolean getExpandedState​(
TreePath
path)

Returns true if the path is expanded, and visible.

**Parameters:**
- path

- the path being queried

**Returns:**
- true if the path is expanded and visible, false otherwise

---

#### public abstract int getRowCount()

Number of rows being displayed.

**Returns:**
- the number of rows being displayed

---

#### public abstract void invalidateSizes()

Informs the

TreeState

that it needs to recalculate
all the sizes it is referencing.

---

#### public abstract void invalidatePathBounds​(
TreePath
path)

Instructs the

LayoutCache

that the bounds for

path

are invalid, and need to be updated.

**Parameters:**
- path

- the path being updated

---

#### public abstract void treeNodesChanged​(
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

**Parameters:**
- e

- the

TreeModelEvent

---

#### public abstract void treeNodesInserted​(
TreeModelEvent
e)

Invoked after nodes have been inserted into the tree.

e.path() returns the parent of the new nodes

e.childIndices() returns the indices of the new nodes in
ascending order.

**Parameters:**
- e

- the

TreeModelEvent

---

#### public abstract void treeNodesRemoved​(
TreeModelEvent
e)

Invoked after nodes have been removed from the tree. Note that
if a subtree is removed from the tree, this method may only be
invoked once for the root of the removed subtree, not once for
each individual set of siblings removed.

e.path() returns the former parent of the deleted nodes.

e.childIndices() returns the indices the nodes had before they were deleted in ascending order.

**Parameters:**
- e

- the

TreeModelEvent

---

#### public abstract void treeStructureChanged​(
TreeModelEvent
e)

Invoked after the tree has drastically changed structure from a
given node down. If the path returned by

e.getPath()

is of length one and the first element does not identify the
current root node the first element should become the new root
of the tree.

e.path() holds the path to the node.

e.childIndices() returns null.

**Parameters:**
- e

- the

TreeModelEvent

---

#### public int[] getRowsForPaths​(
TreePath
[] paths)

Returns the rows that the

TreePath

instances in

path

are being displayed at.
This method should return an array of the same length as that passed
in, and if one of the

TreePaths

in

path

is not valid its entry in the array should
be set to -1.

**Specified by:**
- getRowsForPaths

in interface

RowMapper

**Parameters:**
- paths

- the array of

TreePath

s being queried

**Returns:**
- an array of the same length that is passed in containing
the rows that each corresponding where each

TreePath

is displayed; if

paths

is

null

,

null

is returned

---

#### protected
Rectangle
getNodeDimensions​(
Object
value,
int row,
int depth,
boolean expanded,

Rectangle
placeIn)

Returns, by reference in

placeIn

,
the size needed to represent

value

.
If

inPlace

is

null

, a newly created

Rectangle

should be returned, otherwise the value
should be placed in

inPlace

and returned. This will
return

null

if there is no renderer.

**Parameters:**
- value

- the

value

to be represented
- row

- row being queried
- depth

- the depth of the row
- expanded

- true if row is expanded, false otherwise
- placeIn

- a

Rectangle

containing the size needed
to represent

value

**Returns:**
- a

Rectangle

containing the node dimensions,
or

null

if node has no dimension

---

#### protected boolean isFixedRowHeight()

Returns true if the height of each row is a fixed size.

**Returns:**
- whether the height of each row is a fixed size

---

### Additional Sections

#### Class AbstractLayoutCache

java.lang.Object

- javax.swing.tree.AbstractLayoutCache

javax.swing.tree.AbstractLayoutCache

**All Implemented Interfaces:** RowMapper

**Direct Known Subclasses:** FixedHeightLayoutCache

,

VariableHeightLayoutCache

```java
public abstract class
AbstractLayoutCache

extends
Object

implements
RowMapper
```

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

public abstract class

AbstractLayoutCache

extends

Object

implements

RowMapper

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

static class

AbstractLayoutCache.NodeDimensions

Used by

AbstractLayoutCache

to determine the size
and x origin of a particular node.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

AbstractLayoutCache.NodeDimensions

nodeDimensions

Object responsible for getting the size of a node.

protected boolean

rootVisible

True if the root node is displayed, false if its children are
the highest visible nodes.

protected int

rowHeight

Height to use for each row.

protected

TreeModel

treeModel

Model providing information.

protected

TreeSelectionModel

treeSelectionModel

Selection model.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AbstractLayoutCache

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

Rectangle

getBounds

​(

TreePath

path,

Rectangle

placeIn)

Returns a rectangle giving the bounds needed to draw path.

abstract boolean

getExpandedState

​(

TreePath

path)

Returns true if the path is expanded, and visible.

TreeModel

getModel

()

Returns the

TreeModel

that is providing the data.

AbstractLayoutCache.NodeDimensions

getNodeDimensions

()

Returns the object that renders nodes in the tree, and which is
responsible for calculating the dimensions of individual nodes.

protected

Rectangle

getNodeDimensions

​(

Object

value,
int row,
int depth,
boolean expanded,

Rectangle

placeIn)

Returns, by reference in

placeIn

,
the size needed to represent

value

.

abstract

TreePath

getPathClosestTo

​(int x,
int y)

Returns the path to the node that is closest to x,y.

abstract

TreePath

getPathForRow

​(int row)

Returns the path for passed in row.

int

getPreferredHeight

()

Returns the preferred height.

int

getPreferredWidth

​(

Rectangle

bounds)

Returns the preferred width for the passed in region.

abstract int

getRowCount

()

Number of rows being displayed.

abstract int

getRowForPath

​(

TreePath

path)

Returns the row that the last item identified in path is visible
at.

int

getRowHeight

()

Returns the height of each row.

int[]

getRowsForPaths

​(

TreePath

[] paths)

Returns the rows that the

TreePath

instances in

path

are being displayed at.

TreeSelectionModel

getSelectionModel

()

Returns the model used to maintain the selection.

abstract int

getVisibleChildCount

​(

TreePath

path)

Returns the number of visible children for row.

abstract

Enumeration

<

TreePath

>

getVisiblePathsFrom

​(

TreePath

path)

Returns an

Enumerator

that increments over the visible
paths starting at the passed in location.

abstract void

invalidatePathBounds

​(

TreePath

path)

Instructs the

LayoutCache

that the bounds for

path

are invalid, and need to be updated.

abstract void

invalidateSizes

()

Informs the

TreeState

that it needs to recalculate
all the sizes it is referencing.

abstract boolean

isExpanded

​(

TreePath

path)

Returns true if the value identified by row is currently expanded.

protected boolean

isFixedRowHeight

()

Returns true if the height of each row is a fixed size.

boolean

isRootVisible

()

Returns true if the root node of the tree is displayed.

abstract void

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

Sets the

TreeModel

that will provide the data.

void

setNodeDimensions

​(

AbstractLayoutCache.NodeDimensions

nd)

Sets the renderer that is responsible for drawing nodes in the tree
and which is therefore responsible for calculating the dimensions of
individual nodes.

void

setRootVisible

​(boolean rootVisible)

Determines whether or not the root node from
the

TreeModel

is visible.

void

setRowHeight

​(int rowHeight)

Sets the height of each cell.

void

setSelectionModel

​(

TreeSelectionModel

newLSM)

Sets the

TreeSelectionModel

used to manage the
selection to new LSM.

abstract void

treeNodesChanged

​(

TreeModelEvent

e)

Invoked after a node (or a set of siblings) has changed in some
way.

abstract void

treeNodesInserted

​(

TreeModelEvent

e)

Invoked after nodes have been inserted into the tree.

abstract void

treeNodesRemoved

​(

TreeModelEvent

e)

Invoked after nodes have been removed from the tree.

abstract void

treeStructureChanged

​(

TreeModelEvent

e)

Invoked after the tree has drastically changed structure from a
given node down.

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

Nested Classes

Modifier and Type

Class

Description

static class

AbstractLayoutCache.NodeDimensions

Used by

AbstractLayoutCache

to determine the size
and x origin of a particular node.

---

#### Nested Class Summary

Used by

AbstractLayoutCache

to determine the size
and x origin of a particular node.

Field Summary

Fields

Modifier and Type

Field

Description

protected

AbstractLayoutCache.NodeDimensions

nodeDimensions

Object responsible for getting the size of a node.

protected boolean

rootVisible

True if the root node is displayed, false if its children are
the highest visible nodes.

protected int

rowHeight

Height to use for each row.

protected

TreeModel

treeModel

Model providing information.

protected

TreeSelectionModel

treeSelectionModel

Selection model.

---

#### Field Summary

Object responsible for getting the size of a node.

True if the root node is displayed, false if its children are
the highest visible nodes.

Height to use for each row.

Model providing information.

Selection model.

Constructor Summary

Constructors

Constructor

Description

AbstractLayoutCache

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

Rectangle

getBounds

​(

TreePath

path,

Rectangle

placeIn)

Returns a rectangle giving the bounds needed to draw path.

abstract boolean

getExpandedState

​(

TreePath

path)

Returns true if the path is expanded, and visible.

TreeModel

getModel

()

Returns the

TreeModel

that is providing the data.

AbstractLayoutCache.NodeDimensions

getNodeDimensions

()

Returns the object that renders nodes in the tree, and which is
responsible for calculating the dimensions of individual nodes.

protected

Rectangle

getNodeDimensions

​(

Object

value,
int row,
int depth,
boolean expanded,

Rectangle

placeIn)

Returns, by reference in

placeIn

,
the size needed to represent

value

.

abstract

TreePath

getPathClosestTo

​(int x,
int y)

Returns the path to the node that is closest to x,y.

abstract

TreePath

getPathForRow

​(int row)

Returns the path for passed in row.

int

getPreferredHeight

()

Returns the preferred height.

int

getPreferredWidth

​(

Rectangle

bounds)

Returns the preferred width for the passed in region.

abstract int

getRowCount

()

Number of rows being displayed.

abstract int

getRowForPath

​(

TreePath

path)

Returns the row that the last item identified in path is visible
at.

int

getRowHeight

()

Returns the height of each row.

int[]

getRowsForPaths

​(

TreePath

[] paths)

Returns the rows that the

TreePath

instances in

path

are being displayed at.

TreeSelectionModel

getSelectionModel

()

Returns the model used to maintain the selection.

abstract int

getVisibleChildCount

​(

TreePath

path)

Returns the number of visible children for row.

abstract

Enumeration

<

TreePath

>

getVisiblePathsFrom

​(

TreePath

path)

Returns an

Enumerator

that increments over the visible
paths starting at the passed in location.

abstract void

invalidatePathBounds

​(

TreePath

path)

Instructs the

LayoutCache

that the bounds for

path

are invalid, and need to be updated.

abstract void

invalidateSizes

()

Informs the

TreeState

that it needs to recalculate
all the sizes it is referencing.

abstract boolean

isExpanded

​(

TreePath

path)

Returns true if the value identified by row is currently expanded.

protected boolean

isFixedRowHeight

()

Returns true if the height of each row is a fixed size.

boolean

isRootVisible

()

Returns true if the root node of the tree is displayed.

abstract void

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

Sets the

TreeModel

that will provide the data.

void

setNodeDimensions

​(

AbstractLayoutCache.NodeDimensions

nd)

Sets the renderer that is responsible for drawing nodes in the tree
and which is therefore responsible for calculating the dimensions of
individual nodes.

void

setRootVisible

​(boolean rootVisible)

Determines whether or not the root node from
the

TreeModel

is visible.

void

setRowHeight

​(int rowHeight)

Sets the height of each cell.

void

setSelectionModel

​(

TreeSelectionModel

newLSM)

Sets the

TreeSelectionModel

used to manage the
selection to new LSM.

abstract void

treeNodesChanged

​(

TreeModelEvent

e)

Invoked after a node (or a set of siblings) has changed in some
way.

abstract void

treeNodesInserted

​(

TreeModelEvent

e)

Invoked after nodes have been inserted into the tree.

abstract void

treeNodesRemoved

​(

TreeModelEvent

e)

Invoked after nodes have been removed from the tree.

abstract void

treeStructureChanged

​(

TreeModelEvent

e)

Invoked after the tree has drastically changed structure from a
given node down.

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

Returns the

TreeModel

that is providing the data.

Returns the object that renders nodes in the tree, and which is
responsible for calculating the dimensions of individual nodes.

Returns, by reference in

placeIn

,
the size needed to represent

value

.

Returns the path to the node that is closest to x,y.

Returns the path for passed in row.

Returns the preferred height.

Returns the preferred width for the passed in region.

Number of rows being displayed.

Returns the row that the last item identified in path is visible
at.

Returns the height of each row.

Returns the rows that the

TreePath

instances in

path

are being displayed at.

Returns the model used to maintain the selection.

Returns the number of visible children for row.

Returns an

Enumerator

that increments over the visible
paths starting at the passed in location.

Instructs the

LayoutCache

that the bounds for

path

are invalid, and need to be updated.

Informs the

TreeState

that it needs to recalculate
all the sizes it is referencing.

Returns true if the value identified by row is currently expanded.

Returns true if the height of each row is a fixed size.

Returns true if the root node of the tree is displayed.

Marks the path

path

expanded state to

isExpanded

.

Sets the

TreeModel

that will provide the data.

Sets the renderer that is responsible for drawing nodes in the tree
and which is therefore responsible for calculating the dimensions of
individual nodes.

Determines whether or not the root node from
the

TreeModel

is visible.

Sets the height of each cell.

Sets the

TreeSelectionModel

used to manage the
selection to new LSM.

Invoked after a node (or a set of siblings) has changed in some
way.

Invoked after nodes have been inserted into the tree.

Invoked after nodes have been removed from the tree.

Invoked after the tree has drastically changed structure from a
given node down.

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

============ FIELD DETAIL ===========

- Field Detail

- nodeDimensions

```java
protected
AbstractLayoutCache.NodeDimensions
nodeDimensions
```

Object responsible for getting the size of a node.

- treeModel

```java
protected
TreeModel
treeModel
```

Model providing information.

- treeSelectionModel

```java
protected
TreeSelectionModel
treeSelectionModel
```

Selection model.

- rootVisible

```java
protected boolean rootVisible
```

True if the root node is displayed, false if its children are
the highest visible nodes.

- rowHeight

```java
protected int rowHeight
```

Height to use for each row. If this is <= 0 the renderer will be
used to determine the height for each row.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AbstractLayoutCache

```java
public AbstractLayoutCache()
```

============ METHOD DETAIL ==========

- Method Detail

- setNodeDimensions

```java
public void setNodeDimensions​(
AbstractLayoutCache.NodeDimensions
nd)
```

Sets the renderer that is responsible for drawing nodes in the tree
and which is therefore responsible for calculating the dimensions of
individual nodes.

**Parameters:** nd

- a

NodeDimensions

object

- getNodeDimensions

```java
public
AbstractLayoutCache.NodeDimensions
getNodeDimensions()
```

Returns the object that renders nodes in the tree, and which is
responsible for calculating the dimensions of individual nodes.

**Returns:** the

NodeDimensions

object

- setModel

```java
public void setModel​(
TreeModel
newModel)
```

Sets the

TreeModel

that will provide the data.

**Parameters:** newModel

- the

TreeModel

that is to
provide the data

- getModel

```java
public
TreeModel
getModel()
```

Returns the

TreeModel

that is providing the data.

**Returns:** the

TreeModel

that is providing the data

- setRootVisible

```java
@BeanProperty
(
description
="Whether or not the root node from the TreeModel is visible.")
public void setRootVisible​(boolean rootVisible)
```

Determines whether or not the root node from
the

TreeModel

is visible.

**Parameters:** rootVisible

- true if the root node of the tree is to be displayed
**See Also:** rootVisible

- isRootVisible

```java
public boolean isRootVisible()
```

Returns true if the root node of the tree is displayed.

**Returns:** true if the root node of the tree is displayed
**See Also:** rootVisible

- setRowHeight

```java
@BeanProperty
(
description
="The height of each cell.")
public void setRowHeight​(int rowHeight)
```

Sets the height of each cell. If the specified value
is less than or equal to zero the current cell renderer is
queried for each row's height.

**Parameters:** rowHeight

- the height of each cell, in pixels

- getRowHeight

```java
public int getRowHeight()
```

Returns the height of each row. If the returned value is less than
or equal to 0 the height for each row is determined by the
renderer.

**Returns:** the height of each row

- setSelectionModel

```java
public void setSelectionModel​(
TreeSelectionModel
newLSM)
```

Sets the

TreeSelectionModel

used to manage the
selection to new LSM.

**Parameters:** newLSM

- the new

TreeSelectionModel

- getSelectionModel

```java
public
TreeSelectionModel
getSelectionModel()
```

Returns the model used to maintain the selection.

**Returns:** the

treeSelectionModel

- getPreferredHeight

```java
public int getPreferredHeight()
```

Returns the preferred height.

**Returns:** the preferred height

- getPreferredWidth

```java
public int getPreferredWidth​(
Rectangle
bounds)
```

Returns the preferred width for the passed in region.
The region is defined by the path closest to

(bounds.x, bounds.y)

and
ends at

bounds.height + bounds.y

.
If

bounds

is

null

,
the preferred width for all the nodes
will be returned (and this may be a VERY expensive
computation).

**Parameters:** bounds

- the region being queried
**Returns:** the preferred width for the passed in region

- isExpanded

```java
public abstract boolean isExpanded​(
TreePath
path)
```

Returns true if the value identified by row is currently expanded.

**Parameters:** path

- TreePath to check
**Returns:** whether TreePath is expanded

- getBounds

```java
public abstract
Rectangle
getBounds​(
TreePath
path,

Rectangle
placeIn)
```

Returns a rectangle giving the bounds needed to draw path.

**Parameters:** path

- a

TreePath

specifying a node
**Parameters:** placeIn

- a

Rectangle

object giving the
available space
**Returns:** a

Rectangle

object specifying the space to be used

- getPathForRow

```java
public abstract
TreePath
getPathForRow​(int row)
```

Returns the path for passed in row. If row is not visible

null

is returned.

**Parameters:** row

- the row being queried
**Returns:** the

TreePath

for the given row

- getRowForPath

```java
public abstract int getRowForPath​(
TreePath
path)
```

Returns the row that the last item identified in path is visible
at. Will return -1 if any of the elements in path are not
currently visible.

**Parameters:** path

- the

TreePath

being queried
**Returns:** the row where the last item in path is visible or -1
if any elements in path aren't currently visible

- getPathClosestTo

```java
public abstract
TreePath
getPathClosestTo​(int x,
int y)
```

Returns the path to the node that is closest to x,y. If
there is nothing currently visible this will return

null

,
otherwise it'll always return a valid path.
If you need to test if the
returned object is exactly at x, y you should get the bounds for
the returned path and test x, y against that.

**Parameters:** x

- the horizontal component of the desired location
**Parameters:** y

- the vertical component of the desired location
**Returns:** the

TreePath

closest to the specified point

- getVisiblePathsFrom

```java
public abstract
Enumeration
<
TreePath
> getVisiblePathsFrom​(
TreePath
path)
```

Returns an

Enumerator

that increments over the visible
paths starting at the passed in location. The ordering of the
enumeration is based on how the paths are displayed.
The first element of the returned enumeration will be path,
unless it isn't visible,
in which case

null

will be returned.

**Parameters:** path

- the starting location for the enumeration
**Returns:** the

Enumerator

starting at the desired location

- getVisibleChildCount

```java
public abstract int getVisibleChildCount​(
TreePath
path)
```

Returns the number of visible children for row.

**Parameters:** path

- the path being queried
**Returns:** the number of visible children for the specified path

- setExpandedState

```java
public abstract void setExpandedState​(
TreePath
path,
boolean isExpanded)
```

Marks the path

path

expanded state to

isExpanded

.

**Parameters:** path

- the path being expanded or collapsed
**Parameters:** isExpanded

- true if the path should be expanded, false otherwise

- getExpandedState

```java
public abstract boolean getExpandedState​(
TreePath
path)
```

Returns true if the path is expanded, and visible.

**Parameters:** path

- the path being queried
**Returns:** true if the path is expanded and visible, false otherwise

- getRowCount

```java
public abstract int getRowCount()
```

Number of rows being displayed.

**Returns:** the number of rows being displayed

- invalidateSizes

```java
public abstract void invalidateSizes()
```

Informs the

TreeState

that it needs to recalculate
all the sizes it is referencing.

- invalidatePathBounds

```java
public abstract void invalidatePathBounds​(
TreePath
path)
```

Instructs the

LayoutCache

that the bounds for

path

are invalid, and need to be updated.

**Parameters:** path

- the path being updated

- treeNodesChanged

```java
public abstract void treeNodesChanged​(
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

**Parameters:** e

- the

TreeModelEvent

- treeNodesInserted

```java
public abstract void treeNodesInserted​(
TreeModelEvent
e)
```

Invoked after nodes have been inserted into the tree.

e.path() returns the parent of the new nodes

e.childIndices() returns the indices of the new nodes in
ascending order.

**Parameters:** e

- the

TreeModelEvent

- treeNodesRemoved

```java
public abstract void treeNodesRemoved​(
TreeModelEvent
e)
```

Invoked after nodes have been removed from the tree. Note that
if a subtree is removed from the tree, this method may only be
invoked once for the root of the removed subtree, not once for
each individual set of siblings removed.

e.path() returns the former parent of the deleted nodes.

e.childIndices() returns the indices the nodes had before they were deleted in ascending order.

**Parameters:** e

- the

TreeModelEvent

- treeStructureChanged

```java
public abstract void treeStructureChanged​(
TreeModelEvent
e)
```

Invoked after the tree has drastically changed structure from a
given node down. If the path returned by

e.getPath()

is of length one and the first element does not identify the
current root node the first element should become the new root
of the tree.

e.path() holds the path to the node.

e.childIndices() returns null.

**Parameters:** e

- the

TreeModelEvent

- getRowsForPaths

```java
public int[] getRowsForPaths​(
TreePath
[] paths)
```

Returns the rows that the

TreePath

instances in

path

are being displayed at.
This method should return an array of the same length as that passed
in, and if one of the

TreePaths

in

path

is not valid its entry in the array should
be set to -1.

**Specified by:** getRowsForPaths

in interface

RowMapper
**Parameters:** paths

- the array of

TreePath

s being queried
**Returns:** an array of the same length that is passed in containing
the rows that each corresponding where each

TreePath

is displayed; if

paths

is

null

,

null

is returned

- getNodeDimensions

```java
protected
Rectangle
getNodeDimensions​(
Object
value,
int row,
int depth,
boolean expanded,

Rectangle
placeIn)
```

Returns, by reference in

placeIn

,
the size needed to represent

value

.
If

inPlace

is

null

, a newly created

Rectangle

should be returned, otherwise the value
should be placed in

inPlace

and returned. This will
return

null

if there is no renderer.

**Parameters:** value

- the

value

to be represented
**Parameters:** row

- row being queried
**Parameters:** depth

- the depth of the row
**Parameters:** expanded

- true if row is expanded, false otherwise
**Parameters:** placeIn

- a

Rectangle

containing the size needed
to represent

value
**Returns:** a

Rectangle

containing the node dimensions,
or

null

if node has no dimension

- isFixedRowHeight

```java
protected boolean isFixedRowHeight()
```

Returns true if the height of each row is a fixed size.

**Returns:** whether the height of each row is a fixed size

Field Detail

- nodeDimensions

```java
protected
AbstractLayoutCache.NodeDimensions
nodeDimensions
```

Object responsible for getting the size of a node.

- treeModel

```java
protected
TreeModel
treeModel
```

Model providing information.

- treeSelectionModel

```java
protected
TreeSelectionModel
treeSelectionModel
```

Selection model.

- rootVisible

```java
protected boolean rootVisible
```

True if the root node is displayed, false if its children are
the highest visible nodes.

- rowHeight

```java
protected int rowHeight
```

Height to use for each row. If this is <= 0 the renderer will be
used to determine the height for each row.

---

#### Field Detail

nodeDimensions

```java
protected
AbstractLayoutCache.NodeDimensions
nodeDimensions
```

Object responsible for getting the size of a node.

---

#### nodeDimensions

protected

AbstractLayoutCache.NodeDimensions

nodeDimensions

Object responsible for getting the size of a node.

treeModel

```java
protected
TreeModel
treeModel
```

Model providing information.

---

#### treeModel

protected

TreeModel

treeModel

Model providing information.

treeSelectionModel

```java
protected
TreeSelectionModel
treeSelectionModel
```

Selection model.

---

#### treeSelectionModel

protected

TreeSelectionModel

treeSelectionModel

Selection model.

rootVisible

```java
protected boolean rootVisible
```

True if the root node is displayed, false if its children are
the highest visible nodes.

---

#### rootVisible

protected boolean rootVisible

True if the root node is displayed, false if its children are
the highest visible nodes.

rowHeight

```java
protected int rowHeight
```

Height to use for each row. If this is <= 0 the renderer will be
used to determine the height for each row.

---

#### rowHeight

protected int rowHeight

Height to use for each row. If this is <= 0 the renderer will be
used to determine the height for each row.

Constructor Detail

- AbstractLayoutCache

```java
public AbstractLayoutCache()
```

---

#### Constructor Detail

AbstractLayoutCache

```java
public AbstractLayoutCache()
```

---

#### AbstractLayoutCache

public AbstractLayoutCache()

Method Detail

- setNodeDimensions

```java
public void setNodeDimensions​(
AbstractLayoutCache.NodeDimensions
nd)
```

Sets the renderer that is responsible for drawing nodes in the tree
and which is therefore responsible for calculating the dimensions of
individual nodes.

**Parameters:** nd

- a

NodeDimensions

object

- getNodeDimensions

```java
public
AbstractLayoutCache.NodeDimensions
getNodeDimensions()
```

Returns the object that renders nodes in the tree, and which is
responsible for calculating the dimensions of individual nodes.

**Returns:** the

NodeDimensions

object

- setModel

```java
public void setModel​(
TreeModel
newModel)
```

Sets the

TreeModel

that will provide the data.

**Parameters:** newModel

- the

TreeModel

that is to
provide the data

- getModel

```java
public
TreeModel
getModel()
```

Returns the

TreeModel

that is providing the data.

**Returns:** the

TreeModel

that is providing the data

- setRootVisible

```java
@BeanProperty
(
description
="Whether or not the root node from the TreeModel is visible.")
public void setRootVisible​(boolean rootVisible)
```

Determines whether or not the root node from
the

TreeModel

is visible.

**Parameters:** rootVisible

- true if the root node of the tree is to be displayed
**See Also:** rootVisible

- isRootVisible

```java
public boolean isRootVisible()
```

Returns true if the root node of the tree is displayed.

**Returns:** true if the root node of the tree is displayed
**See Also:** rootVisible

- setRowHeight

```java
@BeanProperty
(
description
="The height of each cell.")
public void setRowHeight​(int rowHeight)
```

Sets the height of each cell. If the specified value
is less than or equal to zero the current cell renderer is
queried for each row's height.

**Parameters:** rowHeight

- the height of each cell, in pixels

- getRowHeight

```java
public int getRowHeight()
```

Returns the height of each row. If the returned value is less than
or equal to 0 the height for each row is determined by the
renderer.

**Returns:** the height of each row

- setSelectionModel

```java
public void setSelectionModel​(
TreeSelectionModel
newLSM)
```

Sets the

TreeSelectionModel

used to manage the
selection to new LSM.

**Parameters:** newLSM

- the new

TreeSelectionModel

- getSelectionModel

```java
public
TreeSelectionModel
getSelectionModel()
```

Returns the model used to maintain the selection.

**Returns:** the

treeSelectionModel

- getPreferredHeight

```java
public int getPreferredHeight()
```

Returns the preferred height.

**Returns:** the preferred height

- getPreferredWidth

```java
public int getPreferredWidth​(
Rectangle
bounds)
```

Returns the preferred width for the passed in region.
The region is defined by the path closest to

(bounds.x, bounds.y)

and
ends at

bounds.height + bounds.y

.
If

bounds

is

null

,
the preferred width for all the nodes
will be returned (and this may be a VERY expensive
computation).

**Parameters:** bounds

- the region being queried
**Returns:** the preferred width for the passed in region

- isExpanded

```java
public abstract boolean isExpanded​(
TreePath
path)
```

Returns true if the value identified by row is currently expanded.

**Parameters:** path

- TreePath to check
**Returns:** whether TreePath is expanded

- getBounds

```java
public abstract
Rectangle
getBounds​(
TreePath
path,

Rectangle
placeIn)
```

Returns a rectangle giving the bounds needed to draw path.

**Parameters:** path

- a

TreePath

specifying a node
**Parameters:** placeIn

- a

Rectangle

object giving the
available space
**Returns:** a

Rectangle

object specifying the space to be used

- getPathForRow

```java
public abstract
TreePath
getPathForRow​(int row)
```

Returns the path for passed in row. If row is not visible

null

is returned.

**Parameters:** row

- the row being queried
**Returns:** the

TreePath

for the given row

- getRowForPath

```java
public abstract int getRowForPath​(
TreePath
path)
```

Returns the row that the last item identified in path is visible
at. Will return -1 if any of the elements in path are not
currently visible.

**Parameters:** path

- the

TreePath

being queried
**Returns:** the row where the last item in path is visible or -1
if any elements in path aren't currently visible

- getPathClosestTo

```java
public abstract
TreePath
getPathClosestTo​(int x,
int y)
```

Returns the path to the node that is closest to x,y. If
there is nothing currently visible this will return

null

,
otherwise it'll always return a valid path.
If you need to test if the
returned object is exactly at x, y you should get the bounds for
the returned path and test x, y against that.

**Parameters:** x

- the horizontal component of the desired location
**Parameters:** y

- the vertical component of the desired location
**Returns:** the

TreePath

closest to the specified point

- getVisiblePathsFrom

```java
public abstract
Enumeration
<
TreePath
> getVisiblePathsFrom​(
TreePath
path)
```

Returns an

Enumerator

that increments over the visible
paths starting at the passed in location. The ordering of the
enumeration is based on how the paths are displayed.
The first element of the returned enumeration will be path,
unless it isn't visible,
in which case

null

will be returned.

**Parameters:** path

- the starting location for the enumeration
**Returns:** the

Enumerator

starting at the desired location

- getVisibleChildCount

```java
public abstract int getVisibleChildCount​(
TreePath
path)
```

Returns the number of visible children for row.

**Parameters:** path

- the path being queried
**Returns:** the number of visible children for the specified path

- setExpandedState

```java
public abstract void setExpandedState​(
TreePath
path,
boolean isExpanded)
```

Marks the path

path

expanded state to

isExpanded

.

**Parameters:** path

- the path being expanded or collapsed
**Parameters:** isExpanded

- true if the path should be expanded, false otherwise

- getExpandedState

```java
public abstract boolean getExpandedState​(
TreePath
path)
```

Returns true if the path is expanded, and visible.

**Parameters:** path

- the path being queried
**Returns:** true if the path is expanded and visible, false otherwise

- getRowCount

```java
public abstract int getRowCount()
```

Number of rows being displayed.

**Returns:** the number of rows being displayed

- invalidateSizes

```java
public abstract void invalidateSizes()
```

Informs the

TreeState

that it needs to recalculate
all the sizes it is referencing.

- invalidatePathBounds

```java
public abstract void invalidatePathBounds​(
TreePath
path)
```

Instructs the

LayoutCache

that the bounds for

path

are invalid, and need to be updated.

**Parameters:** path

- the path being updated

- treeNodesChanged

```java
public abstract void treeNodesChanged​(
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

**Parameters:** e

- the

TreeModelEvent

- treeNodesInserted

```java
public abstract void treeNodesInserted​(
TreeModelEvent
e)
```

Invoked after nodes have been inserted into the tree.

e.path() returns the parent of the new nodes

e.childIndices() returns the indices of the new nodes in
ascending order.

**Parameters:** e

- the

TreeModelEvent

- treeNodesRemoved

```java
public abstract void treeNodesRemoved​(
TreeModelEvent
e)
```

Invoked after nodes have been removed from the tree. Note that
if a subtree is removed from the tree, this method may only be
invoked once for the root of the removed subtree, not once for
each individual set of siblings removed.

e.path() returns the former parent of the deleted nodes.

e.childIndices() returns the indices the nodes had before they were deleted in ascending order.

**Parameters:** e

- the

TreeModelEvent

- treeStructureChanged

```java
public abstract void treeStructureChanged​(
TreeModelEvent
e)
```

Invoked after the tree has drastically changed structure from a
given node down. If the path returned by

e.getPath()

is of length one and the first element does not identify the
current root node the first element should become the new root
of the tree.

e.path() holds the path to the node.

e.childIndices() returns null.

**Parameters:** e

- the

TreeModelEvent

- getRowsForPaths

```java
public int[] getRowsForPaths​(
TreePath
[] paths)
```

Returns the rows that the

TreePath

instances in

path

are being displayed at.
This method should return an array of the same length as that passed
in, and if one of the

TreePaths

in

path

is not valid its entry in the array should
be set to -1.

**Specified by:** getRowsForPaths

in interface

RowMapper
**Parameters:** paths

- the array of

TreePath

s being queried
**Returns:** an array of the same length that is passed in containing
the rows that each corresponding where each

TreePath

is displayed; if

paths

is

null

,

null

is returned

- getNodeDimensions

```java
protected
Rectangle
getNodeDimensions​(
Object
value,
int row,
int depth,
boolean expanded,

Rectangle
placeIn)
```

Returns, by reference in

placeIn

,
the size needed to represent

value

.
If

inPlace

is

null

, a newly created

Rectangle

should be returned, otherwise the value
should be placed in

inPlace

and returned. This will
return

null

if there is no renderer.

**Parameters:** value

- the

value

to be represented
**Parameters:** row

- row being queried
**Parameters:** depth

- the depth of the row
**Parameters:** expanded

- true if row is expanded, false otherwise
**Parameters:** placeIn

- a

Rectangle

containing the size needed
to represent

value
**Returns:** a

Rectangle

containing the node dimensions,
or

null

if node has no dimension

- isFixedRowHeight

```java
protected boolean isFixedRowHeight()
```

Returns true if the height of each row is a fixed size.

**Returns:** whether the height of each row is a fixed size

---

#### Method Detail

setNodeDimensions

```java
public void setNodeDimensions​(
AbstractLayoutCache.NodeDimensions
nd)
```

Sets the renderer that is responsible for drawing nodes in the tree
and which is therefore responsible for calculating the dimensions of
individual nodes.

**Parameters:** nd

- a

NodeDimensions

object

---

#### setNodeDimensions

public void setNodeDimensions​(

AbstractLayoutCache.NodeDimensions

nd)

Sets the renderer that is responsible for drawing nodes in the tree
and which is therefore responsible for calculating the dimensions of
individual nodes.

getNodeDimensions

```java
public
AbstractLayoutCache.NodeDimensions
getNodeDimensions()
```

Returns the object that renders nodes in the tree, and which is
responsible for calculating the dimensions of individual nodes.

**Returns:** the

NodeDimensions

object

---

#### getNodeDimensions

public

AbstractLayoutCache.NodeDimensions

getNodeDimensions()

Returns the object that renders nodes in the tree, and which is
responsible for calculating the dimensions of individual nodes.

setModel

```java
public void setModel​(
TreeModel
newModel)
```

Sets the

TreeModel

that will provide the data.

**Parameters:** newModel

- the

TreeModel

that is to
provide the data

---

#### setModel

public void setModel​(

TreeModel

newModel)

Sets the

TreeModel

that will provide the data.

getModel

```java
public
TreeModel
getModel()
```

Returns the

TreeModel

that is providing the data.

**Returns:** the

TreeModel

that is providing the data

---

#### getModel

public

TreeModel

getModel()

Returns the

TreeModel

that is providing the data.

setRootVisible

```java
@BeanProperty
(
description
="Whether or not the root node from the TreeModel is visible.")
public void setRootVisible​(boolean rootVisible)
```

Determines whether or not the root node from
the

TreeModel

is visible.

**Parameters:** rootVisible

- true if the root node of the tree is to be displayed
**See Also:** rootVisible

---

#### setRootVisible

@BeanProperty

(

description

="Whether or not the root node from the TreeModel is visible.")
public void setRootVisible​(boolean rootVisible)

Determines whether or not the root node from
the

TreeModel

is visible.

isRootVisible

```java
public boolean isRootVisible()
```

Returns true if the root node of the tree is displayed.

**Returns:** true if the root node of the tree is displayed
**See Also:** rootVisible

---

#### isRootVisible

public boolean isRootVisible()

Returns true if the root node of the tree is displayed.

setRowHeight

```java
@BeanProperty
(
description
="The height of each cell.")
public void setRowHeight​(int rowHeight)
```

Sets the height of each cell. If the specified value
is less than or equal to zero the current cell renderer is
queried for each row's height.

**Parameters:** rowHeight

- the height of each cell, in pixels

---

#### setRowHeight

@BeanProperty

(

description

="The height of each cell.")
public void setRowHeight​(int rowHeight)

Sets the height of each cell. If the specified value
is less than or equal to zero the current cell renderer is
queried for each row's height.

getRowHeight

```java
public int getRowHeight()
```

Returns the height of each row. If the returned value is less than
or equal to 0 the height for each row is determined by the
renderer.

**Returns:** the height of each row

---

#### getRowHeight

public int getRowHeight()

Returns the height of each row. If the returned value is less than
or equal to 0 the height for each row is determined by the
renderer.

setSelectionModel

```java
public void setSelectionModel​(
TreeSelectionModel
newLSM)
```

Sets the

TreeSelectionModel

used to manage the
selection to new LSM.

**Parameters:** newLSM

- the new

TreeSelectionModel

---

#### setSelectionModel

public void setSelectionModel​(

TreeSelectionModel

newLSM)

Sets the

TreeSelectionModel

used to manage the
selection to new LSM.

getSelectionModel

```java
public
TreeSelectionModel
getSelectionModel()
```

Returns the model used to maintain the selection.

**Returns:** the

treeSelectionModel

---

#### getSelectionModel

public

TreeSelectionModel

getSelectionModel()

Returns the model used to maintain the selection.

getPreferredHeight

```java
public int getPreferredHeight()
```

Returns the preferred height.

**Returns:** the preferred height

---

#### getPreferredHeight

public int getPreferredHeight()

Returns the preferred height.

getPreferredWidth

```java
public int getPreferredWidth​(
Rectangle
bounds)
```

Returns the preferred width for the passed in region.
The region is defined by the path closest to

(bounds.x, bounds.y)

and
ends at

bounds.height + bounds.y

.
If

bounds

is

null

,
the preferred width for all the nodes
will be returned (and this may be a VERY expensive
computation).

**Parameters:** bounds

- the region being queried
**Returns:** the preferred width for the passed in region

---

#### getPreferredWidth

public int getPreferredWidth​(

Rectangle

bounds)

Returns the preferred width for the passed in region.
The region is defined by the path closest to

(bounds.x, bounds.y)

and
ends at

bounds.height + bounds.y

.
If

bounds

is

null

,
the preferred width for all the nodes
will be returned (and this may be a VERY expensive
computation).

isExpanded

```java
public abstract boolean isExpanded​(
TreePath
path)
```

Returns true if the value identified by row is currently expanded.

**Parameters:** path

- TreePath to check
**Returns:** whether TreePath is expanded

---

#### isExpanded

public abstract boolean isExpanded​(

TreePath

path)

Returns true if the value identified by row is currently expanded.

getBounds

```java
public abstract
Rectangle
getBounds​(
TreePath
path,

Rectangle
placeIn)
```

Returns a rectangle giving the bounds needed to draw path.

**Parameters:** path

- a

TreePath

specifying a node
**Parameters:** placeIn

- a

Rectangle

object giving the
available space
**Returns:** a

Rectangle

object specifying the space to be used

---

#### getBounds

public abstract

Rectangle

getBounds​(

TreePath

path,

Rectangle

placeIn)

Returns a rectangle giving the bounds needed to draw path.

getPathForRow

```java
public abstract
TreePath
getPathForRow​(int row)
```

Returns the path for passed in row. If row is not visible

null

is returned.

**Parameters:** row

- the row being queried
**Returns:** the

TreePath

for the given row

---

#### getPathForRow

public abstract

TreePath

getPathForRow​(int row)

Returns the path for passed in row. If row is not visible

null

is returned.

getRowForPath

```java
public abstract int getRowForPath​(
TreePath
path)
```

Returns the row that the last item identified in path is visible
at. Will return -1 if any of the elements in path are not
currently visible.

**Parameters:** path

- the

TreePath

being queried
**Returns:** the row where the last item in path is visible or -1
if any elements in path aren't currently visible

---

#### getRowForPath

public abstract int getRowForPath​(

TreePath

path)

Returns the row that the last item identified in path is visible
at. Will return -1 if any of the elements in path are not
currently visible.

getPathClosestTo

```java
public abstract
TreePath
getPathClosestTo​(int x,
int y)
```

Returns the path to the node that is closest to x,y. If
there is nothing currently visible this will return

null

,
otherwise it'll always return a valid path.
If you need to test if the
returned object is exactly at x, y you should get the bounds for
the returned path and test x, y against that.

**Parameters:** x

- the horizontal component of the desired location
**Parameters:** y

- the vertical component of the desired location
**Returns:** the

TreePath

closest to the specified point

---

#### getPathClosestTo

public abstract

TreePath

getPathClosestTo​(int x,
int y)

Returns the path to the node that is closest to x,y. If
there is nothing currently visible this will return

null

,
otherwise it'll always return a valid path.
If you need to test if the
returned object is exactly at x, y you should get the bounds for
the returned path and test x, y against that.

getVisiblePathsFrom

```java
public abstract
Enumeration
<
TreePath
> getVisiblePathsFrom​(
TreePath
path)
```

Returns an

Enumerator

that increments over the visible
paths starting at the passed in location. The ordering of the
enumeration is based on how the paths are displayed.
The first element of the returned enumeration will be path,
unless it isn't visible,
in which case

null

will be returned.

**Parameters:** path

- the starting location for the enumeration
**Returns:** the

Enumerator

starting at the desired location

---

#### getVisiblePathsFrom

public abstract

Enumeration

<

TreePath

> getVisiblePathsFrom​(

TreePath

path)

Returns an

Enumerator

that increments over the visible
paths starting at the passed in location. The ordering of the
enumeration is based on how the paths are displayed.
The first element of the returned enumeration will be path,
unless it isn't visible,
in which case

null

will be returned.

getVisibleChildCount

```java
public abstract int getVisibleChildCount​(
TreePath
path)
```

Returns the number of visible children for row.

**Parameters:** path

- the path being queried
**Returns:** the number of visible children for the specified path

---

#### getVisibleChildCount

public abstract int getVisibleChildCount​(

TreePath

path)

Returns the number of visible children for row.

setExpandedState

```java
public abstract void setExpandedState​(
TreePath
path,
boolean isExpanded)
```

Marks the path

path

expanded state to

isExpanded

.

**Parameters:** path

- the path being expanded or collapsed
**Parameters:** isExpanded

- true if the path should be expanded, false otherwise

---

#### setExpandedState

public abstract void setExpandedState​(

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
public abstract boolean getExpandedState​(
TreePath
path)
```

Returns true if the path is expanded, and visible.

**Parameters:** path

- the path being queried
**Returns:** true if the path is expanded and visible, false otherwise

---

#### getExpandedState

public abstract boolean getExpandedState​(

TreePath

path)

Returns true if the path is expanded, and visible.

getRowCount

```java
public abstract int getRowCount()
```

Number of rows being displayed.

**Returns:** the number of rows being displayed

---

#### getRowCount

public abstract int getRowCount()

Number of rows being displayed.

invalidateSizes

```java
public abstract void invalidateSizes()
```

Informs the

TreeState

that it needs to recalculate
all the sizes it is referencing.

---

#### invalidateSizes

public abstract void invalidateSizes()

Informs the

TreeState

that it needs to recalculate
all the sizes it is referencing.

invalidatePathBounds

```java
public abstract void invalidatePathBounds​(
TreePath
path)
```

Instructs the

LayoutCache

that the bounds for

path

are invalid, and need to be updated.

**Parameters:** path

- the path being updated

---

#### invalidatePathBounds

public abstract void invalidatePathBounds​(

TreePath

path)

Instructs the

LayoutCache

that the bounds for

path

are invalid, and need to be updated.

treeNodesChanged

```java
public abstract void treeNodesChanged​(
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

**Parameters:** e

- the

TreeModelEvent

---

#### treeNodesChanged

public abstract void treeNodesChanged​(

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
public abstract void treeNodesInserted​(
TreeModelEvent
e)
```

Invoked after nodes have been inserted into the tree.

e.path() returns the parent of the new nodes

e.childIndices() returns the indices of the new nodes in
ascending order.

**Parameters:** e

- the

TreeModelEvent

---

#### treeNodesInserted

public abstract void treeNodesInserted​(

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

treeNodesRemoved

```java
public abstract void treeNodesRemoved​(
TreeModelEvent
e)
```

Invoked after nodes have been removed from the tree. Note that
if a subtree is removed from the tree, this method may only be
invoked once for the root of the removed subtree, not once for
each individual set of siblings removed.

e.path() returns the former parent of the deleted nodes.

e.childIndices() returns the indices the nodes had before they were deleted in ascending order.

**Parameters:** e

- the

TreeModelEvent

---

#### treeNodesRemoved

public abstract void treeNodesRemoved​(

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
public abstract void treeStructureChanged​(
TreeModelEvent
e)
```

Invoked after the tree has drastically changed structure from a
given node down. If the path returned by

e.getPath()

is of length one and the first element does not identify the
current root node the first element should become the new root
of the tree.

e.path() holds the path to the node.

e.childIndices() returns null.

**Parameters:** e

- the

TreeModelEvent

---

#### treeStructureChanged

public abstract void treeStructureChanged​(

TreeModelEvent

e)

Invoked after the tree has drastically changed structure from a
given node down. If the path returned by

e.getPath()

is of length one and the first element does not identify the
current root node the first element should become the new root
of the tree.

e.path() holds the path to the node.

e.childIndices() returns null.

Invoked after the tree has drastically changed structure from a
given node down. If the path returned by

e.getPath()

is of length one and the first element does not identify the
current root node the first element should become the new root
of the tree.

e.path() holds the path to the node.

e.childIndices() returns null.

getRowsForPaths

```java
public int[] getRowsForPaths​(
TreePath
[] paths)
```

Returns the rows that the

TreePath

instances in

path

are being displayed at.
This method should return an array of the same length as that passed
in, and if one of the

TreePaths

in

path

is not valid its entry in the array should
be set to -1.

**Specified by:** getRowsForPaths

in interface

RowMapper
**Parameters:** paths

- the array of

TreePath

s being queried
**Returns:** an array of the same length that is passed in containing
the rows that each corresponding where each

TreePath

is displayed; if

paths

is

null

,

null

is returned

---

#### getRowsForPaths

public int[] getRowsForPaths​(

TreePath

[] paths)

Returns the rows that the

TreePath

instances in

path

are being displayed at.
This method should return an array of the same length as that passed
in, and if one of the

TreePaths

in

path

is not valid its entry in the array should
be set to -1.

getNodeDimensions

```java
protected
Rectangle
getNodeDimensions​(
Object
value,
int row,
int depth,
boolean expanded,

Rectangle
placeIn)
```

Returns, by reference in

placeIn

,
the size needed to represent

value

.
If

inPlace

is

null

, a newly created

Rectangle

should be returned, otherwise the value
should be placed in

inPlace

and returned. This will
return

null

if there is no renderer.

**Parameters:** value

- the

value

to be represented
**Parameters:** row

- row being queried
**Parameters:** depth

- the depth of the row
**Parameters:** expanded

- true if row is expanded, false otherwise
**Parameters:** placeIn

- a

Rectangle

containing the size needed
to represent

value
**Returns:** a

Rectangle

containing the node dimensions,
or

null

if node has no dimension

---

#### getNodeDimensions

protected

Rectangle

getNodeDimensions​(

Object

value,
int row,
int depth,
boolean expanded,

Rectangle

placeIn)

Returns, by reference in

placeIn

,
the size needed to represent

value

.
If

inPlace

is

null

, a newly created

Rectangle

should be returned, otherwise the value
should be placed in

inPlace

and returned. This will
return

null

if there is no renderer.

isFixedRowHeight

```java
protected boolean isFixedRowHeight()
```

Returns true if the height of each row is a fixed size.

**Returns:** whether the height of each row is a fixed size

---

#### isFixedRowHeight

protected boolean isFixedRowHeight()

Returns true if the height of each row is a fixed size.

---

