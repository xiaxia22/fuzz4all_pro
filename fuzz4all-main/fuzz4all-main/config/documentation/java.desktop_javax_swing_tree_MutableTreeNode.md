# Interface MutableTreeNode

**Source:** `java.desktop\javax\swing\tree\MutableTreeNode.html`

### Class Description

```java
public interface
MutableTreeNode

extends
TreeNode
```

Defines the requirements for a tree node object that can change --
by adding or removing child nodes, or by changing the contents
of a user object stored in the node.

**All Superinterfaces:** TreeNode

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void insert​(
MutableTreeNode
child,
int index)

Adds

child

to the receiver at

index

.

child

will be messaged with

setParent

.

**Parameters:**
- child

- node to be added
- index

- index of the receiver

---

#### void remove​(int index)

Removes the child at

index

from the receiver.

**Parameters:**
- index

- index of child to be removed

---

#### void remove​(
MutableTreeNode
node)

Removes

node

from the receiver.

setParent

will be messaged on

node

.

**Parameters:**
- node

- node to be removed from the receiver

---

#### void setUserObject​(
Object
object)

Resets the user object of the receiver to

object

.

**Parameters:**
- object

- object to be set as a receiver

---

#### void removeFromParent()

Removes the receiver from its parent.

---

#### void setParent​(
MutableTreeNode
newParent)

Sets the parent of the receiver to

newParent

.

**Parameters:**
- newParent

- node to be set as parent of the receiver

---

### Additional Sections

#### Interface MutableTreeNode

**All Superinterfaces:** TreeNode

**All Known Implementing Classes:** DefaultMutableTreeNode

,

JTree.DynamicUtilTreeNode

```java
public interface
MutableTreeNode

extends
TreeNode
```

Defines the requirements for a tree node object that can change --
by adding or removing child nodes, or by changing the contents
of a user object stored in the node.

**See Also:** DefaultMutableTreeNode

,

JTree

public interface

MutableTreeNode

extends

TreeNode

Defines the requirements for a tree node object that can change --
by adding or removing child nodes, or by changing the contents
of a user object stored in the node.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

insert

​(

MutableTreeNode

child,
int index)

Adds

child

to the receiver at

index

.

void

remove

​(int index)

Removes the child at

index

from the receiver.

void

remove

​(

MutableTreeNode

node)

Removes

node

from the receiver.

void

removeFromParent

()

Removes the receiver from its parent.

void

setParent

​(

MutableTreeNode

newParent)

Sets the parent of the receiver to

newParent

.

void

setUserObject

​(

Object

object)

Resets the user object of the receiver to

object

.

- Methods declared in interface javax.swing.tree.

TreeNode

children

,

getAllowsChildren

,

getChildAt

,

getChildCount

,

getIndex

,

getParent

,

isLeaf

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

insert

​(

MutableTreeNode

child,
int index)

Adds

child

to the receiver at

index

.

void

remove

​(int index)

Removes the child at

index

from the receiver.

void

remove

​(

MutableTreeNode

node)

Removes

node

from the receiver.

void

removeFromParent

()

Removes the receiver from its parent.

void

setParent

​(

MutableTreeNode

newParent)

Sets the parent of the receiver to

newParent

.

void

setUserObject

​(

Object

object)

Resets the user object of the receiver to

object

.

- Methods declared in interface javax.swing.tree.

TreeNode

children

,

getAllowsChildren

,

getChildAt

,

getChildCount

,

getIndex

,

getParent

,

isLeaf

---

#### Method Summary

Adds

child

to the receiver at

index

.

Removes the child at

index

from the receiver.

Removes

node

from the receiver.

Removes the receiver from its parent.

Sets the parent of the receiver to

newParent

.

Resets the user object of the receiver to

object

.

Methods declared in interface javax.swing.tree.

TreeNode

children

,

getAllowsChildren

,

getChildAt

,

getChildCount

,

getIndex

,

getParent

,

isLeaf

---

#### Methods declared in interface javax.swing.tree. TreeNode

============ METHOD DETAIL ==========

- Method Detail

- insert

```java
void insert​(
MutableTreeNode
child,
int index)
```

Adds

child

to the receiver at

index

.

child

will be messaged with

setParent

.

**Parameters:** child

- node to be added
**Parameters:** index

- index of the receiver

- remove

```java
void remove​(int index)
```

Removes the child at

index

from the receiver.

**Parameters:** index

- index of child to be removed

- remove

```java
void remove​(
MutableTreeNode
node)
```

Removes

node

from the receiver.

setParent

will be messaged on

node

.

**Parameters:** node

- node to be removed from the receiver

- setUserObject

```java
void setUserObject​(
Object
object)
```

Resets the user object of the receiver to

object

.

**Parameters:** object

- object to be set as a receiver

- removeFromParent

```java
void removeFromParent()
```

Removes the receiver from its parent.

- setParent

```java
void setParent​(
MutableTreeNode
newParent)
```

Sets the parent of the receiver to

newParent

.

**Parameters:** newParent

- node to be set as parent of the receiver

Method Detail

- insert

```java
void insert​(
MutableTreeNode
child,
int index)
```

Adds

child

to the receiver at

index

.

child

will be messaged with

setParent

.

**Parameters:** child

- node to be added
**Parameters:** index

- index of the receiver

- remove

```java
void remove​(int index)
```

Removes the child at

index

from the receiver.

**Parameters:** index

- index of child to be removed

- remove

```java
void remove​(
MutableTreeNode
node)
```

Removes

node

from the receiver.

setParent

will be messaged on

node

.

**Parameters:** node

- node to be removed from the receiver

- setUserObject

```java
void setUserObject​(
Object
object)
```

Resets the user object of the receiver to

object

.

**Parameters:** object

- object to be set as a receiver

- removeFromParent

```java
void removeFromParent()
```

Removes the receiver from its parent.

- setParent

```java
void setParent​(
MutableTreeNode
newParent)
```

Sets the parent of the receiver to

newParent

.

**Parameters:** newParent

- node to be set as parent of the receiver

---

#### Method Detail

insert

```java
void insert​(
MutableTreeNode
child,
int index)
```

Adds

child

to the receiver at

index

.

child

will be messaged with

setParent

.

**Parameters:** child

- node to be added
**Parameters:** index

- index of the receiver

---

#### insert

void insert​(

MutableTreeNode

child,
int index)

Adds

child

to the receiver at

index

.

child

will be messaged with

setParent

.

remove

```java
void remove​(int index)
```

Removes the child at

index

from the receiver.

**Parameters:** index

- index of child to be removed

---

#### remove

void remove​(int index)

Removes the child at

index

from the receiver.

remove

```java
void remove​(
MutableTreeNode
node)
```

Removes

node

from the receiver.

setParent

will be messaged on

node

.

**Parameters:** node

- node to be removed from the receiver

---

#### remove

void remove​(

MutableTreeNode

node)

Removes

node

from the receiver.

setParent

will be messaged on

node

.

setUserObject

```java
void setUserObject​(
Object
object)
```

Resets the user object of the receiver to

object

.

**Parameters:** object

- object to be set as a receiver

---

#### setUserObject

void setUserObject​(

Object

object)

Resets the user object of the receiver to

object

.

removeFromParent

```java
void removeFromParent()
```

Removes the receiver from its parent.

---

#### removeFromParent

void removeFromParent()

Removes the receiver from its parent.

setParent

```java
void setParent​(
MutableTreeNode
newParent)
```

Sets the parent of the receiver to

newParent

.

**Parameters:** newParent

- node to be set as parent of the receiver

---

#### setParent

void setParent​(

MutableTreeNode

newParent)

Sets the parent of the receiver to

newParent

.

---

