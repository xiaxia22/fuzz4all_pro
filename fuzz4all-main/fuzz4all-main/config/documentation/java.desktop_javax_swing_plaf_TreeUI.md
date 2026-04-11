# Class TreeUI

**Source:** `java.desktop\javax\swing\plaf\TreeUI.html`

### Class Description

```java
public abstract class
TreeUI

extends
ComponentUI
```

Pluggable look and feel interface for JTree.

**Direct Known Subclasses:** BasicTreeUI

,

MultiTreeUI

---

### Field Details

*No entries found.*

### Constructor Details

#### public TreeUI()

*No description found.*

---

### Method Details

#### public abstract
Rectangle
getPathBounds​(
JTree
tree,

TreePath
path)

Returns the Rectangle enclosing the label portion that the
last item in path will be drawn into. Will return null if
any component in path is currently valid.

**Parameters:**
- tree

- the

JTree

for

path
- path

- the

TreePath

identifying the node

**Returns:**
- the

Rectangle

enclosing the label portion that the
last item in path will be drawn into,

null

if any
component in path is currently valid.

---

#### public abstract
TreePath
getPathForRow​(
JTree
tree,
int row)

Returns the path for passed in row. If row is not visible
null is returned.

**Parameters:**
- tree

- a

JTree

object
- row

- an integer specifying a row

**Returns:**
- the

path

for

row

or

null

if

row

is not visible

---

#### public abstract int getRowForPath​(
JTree
tree,

TreePath
path)

Returns the row that the last item identified in path is visible
at. Will return -1 if any of the elements in path are not
currently visible.

**Parameters:**
- tree

- the

JTree

for

path
- path

- the

TreePath

object to look in

**Returns:**
- an integer specifying the row at which the last item
identified is visible, -1 if any of the elements in

path

are not currently visible

---

#### public abstract int getRowCount​(
JTree
tree)

Returns the number of rows that are being displayed.

**Parameters:**
- tree

- the

JTree

for which to count rows

**Returns:**
- an integer specifying the number of row being displayed

---

#### public abstract
TreePath
getClosestPathForLocation​(
JTree
tree,
int x,
int y)

Returns the path to the node that is closest to x,y. If
there is nothing currently visible this will return null, otherwise
it'll always return a valid path. If you need to test if the
returned object is exactly at x, y you should get the bounds for
the returned path and test x, y against that.

**Parameters:**
- tree

- a

JTree

object
- x

- an integer giving the number of pixels horizontally from the
left edge of the display area
- y

- an integer giving the number of pixels vertically from the top
of the display area, minus any top margin

**Returns:**
- the

TreePath

node closest to

x,y

or

null

if there is nothing currently visible

---

#### public abstract boolean isEditing​(
JTree
tree)

Returns true if the tree is being edited. The item that is being
edited can be returned by getEditingPath().

**Parameters:**
- tree

- a

JTree

object

**Returns:**
- true if

tree

is being edited

---

#### public abstract boolean stopEditing​(
JTree
tree)

Stops the current editing session. This has no effect if the
tree isn't being edited. Returns true if the editor allows the
editing session to stop.

**Parameters:**
- tree

- a

JTree

object

**Returns:**
- true if the editor allows the editing session to stop

---

#### public abstract void cancelEditing​(
JTree
tree)

Cancels the current editing session. This has no effect if the
tree isn't being edited.

**Parameters:**
- tree

- a

JTree

object

---

#### public abstract void startEditingAtPath​(
JTree
tree,

TreePath
path)

Selects the last item in path and tries to edit it. Editing will
fail if the CellEditor won't allow it for the selected item.

**Parameters:**
- tree

- the

JTree

being edited
- path

- the

TreePath

to be edited

---

#### public abstract
TreePath
getEditingPath​(
JTree
tree)

Returns the path to the element that is being edited.

**Parameters:**
- tree

- the

JTree

for which to return a path

**Returns:**
- a

TreePath

containing the path to

tree

---

### Additional Sections

#### Class TreeUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.TreeUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.TreeUI

javax.swing.plaf.TreeUI

**Direct Known Subclasses:** BasicTreeUI

,

MultiTreeUI

```java
public abstract class
TreeUI

extends
ComponentUI
```

Pluggable look and feel interface for JTree.

public abstract class

TreeUI

extends

ComponentUI

Pluggable look and feel interface for JTree.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TreeUI

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract void

cancelEditing

​(

JTree

tree)

Cancels the current editing session.

abstract

TreePath

getClosestPathForLocation

​(

JTree

tree,
int x,
int y)

Returns the path to the node that is closest to x,y.

abstract

TreePath

getEditingPath

​(

JTree

tree)

Returns the path to the element that is being edited.

abstract

Rectangle

getPathBounds

​(

JTree

tree,

TreePath

path)

Returns the Rectangle enclosing the label portion that the
last item in path will be drawn into.

abstract

TreePath

getPathForRow

​(

JTree

tree,
int row)

Returns the path for passed in row.

abstract int

getRowCount

​(

JTree

tree)

Returns the number of rows that are being displayed.

abstract int

getRowForPath

​(

JTree

tree,

TreePath

path)

Returns the row that the last item identified in path is visible
at.

abstract boolean

isEditing

​(

JTree

tree)

Returns true if the tree is being edited.

abstract void

startEditingAtPath

​(

JTree

tree,

TreePath

path)

Selects the last item in path and tries to edit it.

abstract boolean

stopEditing

​(

JTree

tree)

Stops the current editing session.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

createUI

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

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

Constructor Summary

Constructors

Constructor

Description

TreeUI

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract void

cancelEditing

​(

JTree

tree)

Cancels the current editing session.

abstract

TreePath

getClosestPathForLocation

​(

JTree

tree,
int x,
int y)

Returns the path to the node that is closest to x,y.

abstract

TreePath

getEditingPath

​(

JTree

tree)

Returns the path to the element that is being edited.

abstract

Rectangle

getPathBounds

​(

JTree

tree,

TreePath

path)

Returns the Rectangle enclosing the label portion that the
last item in path will be drawn into.

abstract

TreePath

getPathForRow

​(

JTree

tree,
int row)

Returns the path for passed in row.

abstract int

getRowCount

​(

JTree

tree)

Returns the number of rows that are being displayed.

abstract int

getRowForPath

​(

JTree

tree,

TreePath

path)

Returns the row that the last item identified in path is visible
at.

abstract boolean

isEditing

​(

JTree

tree)

Returns true if the tree is being edited.

abstract void

startEditingAtPath

​(

JTree

tree,

TreePath

path)

Selects the last item in path and tries to edit it.

abstract boolean

stopEditing

​(

JTree

tree)

Stops the current editing session.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

createUI

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

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

Cancels the current editing session.

Returns the path to the node that is closest to x,y.

Returns the path to the element that is being edited.

Returns the Rectangle enclosing the label portion that the
last item in path will be drawn into.

Returns the path for passed in row.

Returns the number of rows that are being displayed.

Returns the row that the last item identified in path is visible
at.

Returns true if the tree is being edited.

Selects the last item in path and tries to edit it.

Stops the current editing session.

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

createUI

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

---

#### Methods declared in class javax.swing.plaf. ComponentUI

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

- TreeUI

```java
public TreeUI()
```

============ METHOD DETAIL ==========

- Method Detail

- getPathBounds

```java
public abstract
Rectangle
getPathBounds​(
JTree
tree,

TreePath
path)
```

Returns the Rectangle enclosing the label portion that the
last item in path will be drawn into. Will return null if
any component in path is currently valid.

**Parameters:** tree

- the

JTree

for

path
**Parameters:** path

- the

TreePath

identifying the node
**Returns:** the

Rectangle

enclosing the label portion that the
last item in path will be drawn into,

null

if any
component in path is currently valid.

- getPathForRow

```java
public abstract
TreePath
getPathForRow​(
JTree
tree,
int row)
```

Returns the path for passed in row. If row is not visible
null is returned.

**Parameters:** tree

- a

JTree

object
**Parameters:** row

- an integer specifying a row
**Returns:** the

path

for

row

or

null

if

row

is not visible

- getRowForPath

```java
public abstract int getRowForPath​(
JTree
tree,

TreePath
path)
```

Returns the row that the last item identified in path is visible
at. Will return -1 if any of the elements in path are not
currently visible.

**Parameters:** tree

- the

JTree

for

path
**Parameters:** path

- the

TreePath

object to look in
**Returns:** an integer specifying the row at which the last item
identified is visible, -1 if any of the elements in

path

are not currently visible

- getRowCount

```java
public abstract int getRowCount​(
JTree
tree)
```

Returns the number of rows that are being displayed.

**Parameters:** tree

- the

JTree

for which to count rows
**Returns:** an integer specifying the number of row being displayed

- getClosestPathForLocation

```java
public abstract
TreePath
getClosestPathForLocation​(
JTree
tree,
int x,
int y)
```

Returns the path to the node that is closest to x,y. If
there is nothing currently visible this will return null, otherwise
it'll always return a valid path. If you need to test if the
returned object is exactly at x, y you should get the bounds for
the returned path and test x, y against that.

**Parameters:** tree

- a

JTree

object
**Parameters:** x

- an integer giving the number of pixels horizontally from the
left edge of the display area
**Parameters:** y

- an integer giving the number of pixels vertically from the top
of the display area, minus any top margin
**Returns:** the

TreePath

node closest to

x,y

or

null

if there is nothing currently visible

- isEditing

```java
public abstract boolean isEditing​(
JTree
tree)
```

Returns true if the tree is being edited. The item that is being
edited can be returned by getEditingPath().

**Parameters:** tree

- a

JTree

object
**Returns:** true if

tree

is being edited

- stopEditing

```java
public abstract boolean stopEditing​(
JTree
tree)
```

Stops the current editing session. This has no effect if the
tree isn't being edited. Returns true if the editor allows the
editing session to stop.

**Parameters:** tree

- a

JTree

object
**Returns:** true if the editor allows the editing session to stop

- cancelEditing

```java
public abstract void cancelEditing​(
JTree
tree)
```

Cancels the current editing session. This has no effect if the
tree isn't being edited.

**Parameters:** tree

- a

JTree

object

- startEditingAtPath

```java
public abstract void startEditingAtPath​(
JTree
tree,

TreePath
path)
```

Selects the last item in path and tries to edit it. Editing will
fail if the CellEditor won't allow it for the selected item.

**Parameters:** tree

- the

JTree

being edited
**Parameters:** path

- the

TreePath

to be edited

- getEditingPath

```java
public abstract
TreePath
getEditingPath​(
JTree
tree)
```

Returns the path to the element that is being edited.

**Parameters:** tree

- the

JTree

for which to return a path
**Returns:** a

TreePath

containing the path to

tree

Constructor Detail

- TreeUI

```java
public TreeUI()
```

---

#### Constructor Detail

TreeUI

```java
public TreeUI()
```

---

#### TreeUI

public TreeUI()

Method Detail

- getPathBounds

```java
public abstract
Rectangle
getPathBounds​(
JTree
tree,

TreePath
path)
```

Returns the Rectangle enclosing the label portion that the
last item in path will be drawn into. Will return null if
any component in path is currently valid.

**Parameters:** tree

- the

JTree

for

path
**Parameters:** path

- the

TreePath

identifying the node
**Returns:** the

Rectangle

enclosing the label portion that the
last item in path will be drawn into,

null

if any
component in path is currently valid.

- getPathForRow

```java
public abstract
TreePath
getPathForRow​(
JTree
tree,
int row)
```

Returns the path for passed in row. If row is not visible
null is returned.

**Parameters:** tree

- a

JTree

object
**Parameters:** row

- an integer specifying a row
**Returns:** the

path

for

row

or

null

if

row

is not visible

- getRowForPath

```java
public abstract int getRowForPath​(
JTree
tree,

TreePath
path)
```

Returns the row that the last item identified in path is visible
at. Will return -1 if any of the elements in path are not
currently visible.

**Parameters:** tree

- the

JTree

for

path
**Parameters:** path

- the

TreePath

object to look in
**Returns:** an integer specifying the row at which the last item
identified is visible, -1 if any of the elements in

path

are not currently visible

- getRowCount

```java
public abstract int getRowCount​(
JTree
tree)
```

Returns the number of rows that are being displayed.

**Parameters:** tree

- the

JTree

for which to count rows
**Returns:** an integer specifying the number of row being displayed

- getClosestPathForLocation

```java
public abstract
TreePath
getClosestPathForLocation​(
JTree
tree,
int x,
int y)
```

Returns the path to the node that is closest to x,y. If
there is nothing currently visible this will return null, otherwise
it'll always return a valid path. If you need to test if the
returned object is exactly at x, y you should get the bounds for
the returned path and test x, y against that.

**Parameters:** tree

- a

JTree

object
**Parameters:** x

- an integer giving the number of pixels horizontally from the
left edge of the display area
**Parameters:** y

- an integer giving the number of pixels vertically from the top
of the display area, minus any top margin
**Returns:** the

TreePath

node closest to

x,y

or

null

if there is nothing currently visible

- isEditing

```java
public abstract boolean isEditing​(
JTree
tree)
```

Returns true if the tree is being edited. The item that is being
edited can be returned by getEditingPath().

**Parameters:** tree

- a

JTree

object
**Returns:** true if

tree

is being edited

- stopEditing

```java
public abstract boolean stopEditing​(
JTree
tree)
```

Stops the current editing session. This has no effect if the
tree isn't being edited. Returns true if the editor allows the
editing session to stop.

**Parameters:** tree

- a

JTree

object
**Returns:** true if the editor allows the editing session to stop

- cancelEditing

```java
public abstract void cancelEditing​(
JTree
tree)
```

Cancels the current editing session. This has no effect if the
tree isn't being edited.

**Parameters:** tree

- a

JTree

object

- startEditingAtPath

```java
public abstract void startEditingAtPath​(
JTree
tree,

TreePath
path)
```

Selects the last item in path and tries to edit it. Editing will
fail if the CellEditor won't allow it for the selected item.

**Parameters:** tree

- the

JTree

being edited
**Parameters:** path

- the

TreePath

to be edited

- getEditingPath

```java
public abstract
TreePath
getEditingPath​(
JTree
tree)
```

Returns the path to the element that is being edited.

**Parameters:** tree

- the

JTree

for which to return a path
**Returns:** a

TreePath

containing the path to

tree

---

#### Method Detail

getPathBounds

```java
public abstract
Rectangle
getPathBounds​(
JTree
tree,

TreePath
path)
```

Returns the Rectangle enclosing the label portion that the
last item in path will be drawn into. Will return null if
any component in path is currently valid.

**Parameters:** tree

- the

JTree

for

path
**Parameters:** path

- the

TreePath

identifying the node
**Returns:** the

Rectangle

enclosing the label portion that the
last item in path will be drawn into,

null

if any
component in path is currently valid.

---

#### getPathBounds

public abstract

Rectangle

getPathBounds​(

JTree

tree,

TreePath

path)

Returns the Rectangle enclosing the label portion that the
last item in path will be drawn into. Will return null if
any component in path is currently valid.

getPathForRow

```java
public abstract
TreePath
getPathForRow​(
JTree
tree,
int row)
```

Returns the path for passed in row. If row is not visible
null is returned.

**Parameters:** tree

- a

JTree

object
**Parameters:** row

- an integer specifying a row
**Returns:** the

path

for

row

or

null

if

row

is not visible

---

#### getPathForRow

public abstract

TreePath

getPathForRow​(

JTree

tree,
int row)

Returns the path for passed in row. If row is not visible
null is returned.

getRowForPath

```java
public abstract int getRowForPath​(
JTree
tree,

TreePath
path)
```

Returns the row that the last item identified in path is visible
at. Will return -1 if any of the elements in path are not
currently visible.

**Parameters:** tree

- the

JTree

for

path
**Parameters:** path

- the

TreePath

object to look in
**Returns:** an integer specifying the row at which the last item
identified is visible, -1 if any of the elements in

path

are not currently visible

---

#### getRowForPath

public abstract int getRowForPath​(

JTree

tree,

TreePath

path)

Returns the row that the last item identified in path is visible
at. Will return -1 if any of the elements in path are not
currently visible.

getRowCount

```java
public abstract int getRowCount​(
JTree
tree)
```

Returns the number of rows that are being displayed.

**Parameters:** tree

- the

JTree

for which to count rows
**Returns:** an integer specifying the number of row being displayed

---

#### getRowCount

public abstract int getRowCount​(

JTree

tree)

Returns the number of rows that are being displayed.

getClosestPathForLocation

```java
public abstract
TreePath
getClosestPathForLocation​(
JTree
tree,
int x,
int y)
```

Returns the path to the node that is closest to x,y. If
there is nothing currently visible this will return null, otherwise
it'll always return a valid path. If you need to test if the
returned object is exactly at x, y you should get the bounds for
the returned path and test x, y against that.

**Parameters:** tree

- a

JTree

object
**Parameters:** x

- an integer giving the number of pixels horizontally from the
left edge of the display area
**Parameters:** y

- an integer giving the number of pixels vertically from the top
of the display area, minus any top margin
**Returns:** the

TreePath

node closest to

x,y

or

null

if there is nothing currently visible

---

#### getClosestPathForLocation

public abstract

TreePath

getClosestPathForLocation​(

JTree

tree,
int x,
int y)

Returns the path to the node that is closest to x,y. If
there is nothing currently visible this will return null, otherwise
it'll always return a valid path. If you need to test if the
returned object is exactly at x, y you should get the bounds for
the returned path and test x, y against that.

isEditing

```java
public abstract boolean isEditing​(
JTree
tree)
```

Returns true if the tree is being edited. The item that is being
edited can be returned by getEditingPath().

**Parameters:** tree

- a

JTree

object
**Returns:** true if

tree

is being edited

---

#### isEditing

public abstract boolean isEditing​(

JTree

tree)

Returns true if the tree is being edited. The item that is being
edited can be returned by getEditingPath().

stopEditing

```java
public abstract boolean stopEditing​(
JTree
tree)
```

Stops the current editing session. This has no effect if the
tree isn't being edited. Returns true if the editor allows the
editing session to stop.

**Parameters:** tree

- a

JTree

object
**Returns:** true if the editor allows the editing session to stop

---

#### stopEditing

public abstract boolean stopEditing​(

JTree

tree)

Stops the current editing session. This has no effect if the
tree isn't being edited. Returns true if the editor allows the
editing session to stop.

cancelEditing

```java
public abstract void cancelEditing​(
JTree
tree)
```

Cancels the current editing session. This has no effect if the
tree isn't being edited.

**Parameters:** tree

- a

JTree

object

---

#### cancelEditing

public abstract void cancelEditing​(

JTree

tree)

Cancels the current editing session. This has no effect if the
tree isn't being edited.

startEditingAtPath

```java
public abstract void startEditingAtPath​(
JTree
tree,

TreePath
path)
```

Selects the last item in path and tries to edit it. Editing will
fail if the CellEditor won't allow it for the selected item.

**Parameters:** tree

- the

JTree

being edited
**Parameters:** path

- the

TreePath

to be edited

---

#### startEditingAtPath

public abstract void startEditingAtPath​(

JTree

tree,

TreePath

path)

Selects the last item in path and tries to edit it. Editing will
fail if the CellEditor won't allow it for the selected item.

getEditingPath

```java
public abstract
TreePath
getEditingPath​(
JTree
tree)
```

Returns the path to the element that is being edited.

**Parameters:** tree

- the

JTree

for which to return a path
**Returns:** a

TreePath

containing the path to

tree

---

#### getEditingPath

public abstract

TreePath

getEditingPath​(

JTree

tree)

Returns the path to the element that is being edited.

---

