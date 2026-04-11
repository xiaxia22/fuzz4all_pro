# Interface TreeModelListener

**Source:** `java.desktop\javax\swing\event\TreeModelListener.html`

### Class Description

```java
public interface
TreeModelListener

extends
EventListener
```

Defines the interface for an object that listens
to changes in a TreeModel.
For further information and examples see

How to Write a Tree Model Listener

,
a section in

The Java Tutorial.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void treeNodesChanged​(
TreeModelEvent
e)

Invoked after a node (or a set of siblings) has changed in some
way. The node(s) have not changed locations in the tree or
altered their children arrays, but other attributes have
changed and may affect presentation. Example: the name of a
file has changed, but it is in the same location in the file
system.

To indicate the root has changed, childIndices and children
will be null.

Use

e.getPath()

to get the parent of the changed node(s).

e.getChildIndices()

returns the index(es) of the changed node(s).

**Parameters:**
- e

- a

TreeModelEvent

describing changes to a tree model

---

#### void treeNodesInserted​(
TreeModelEvent
e)

Invoked after nodes have been inserted into the tree.

Use

e.getPath()

to get the parent of the new node(s).

e.getChildIndices()

returns the index(es) of the new node(s)
in ascending order.

**Parameters:**
- e

- a

TreeModelEvent

describing changes to a tree model

---

#### void treeNodesRemoved​(
TreeModelEvent
e)

Invoked after nodes have been removed from the tree. Note that
if a subtree is removed from the tree, this method may only be
invoked once for the root of the removed subtree, not once for
each individual set of siblings removed.

Use

e.getPath()

to get the former parent of the deleted
node(s).

e.getChildIndices()

returns, in ascending order, the
index(es) the node(s) had before being deleted.

**Parameters:**
- e

- a

TreeModelEvent

describing changes to a tree model

---

#### void treeStructureChanged​(
TreeModelEvent
e)

Invoked after the tree has drastically changed structure from a
given node down. If the path returned by e.getPath() is of length
one and the first element does not identify the current root node
the first element should become the new root of the tree.

Use

e.getPath()

to get the path to the node.

e.getChildIndices()

returns null.

**Parameters:**
- e

- a

TreeModelEvent

describing changes to a tree model

---

### Additional Sections

#### Interface TreeModelListener

**All Superinterfaces:** EventListener

**All Known Implementing Classes:** BasicTreeUI.TreeModelHandler

,

JTree.AccessibleJTree

,

JTree.TreeModelHandler

```java
public interface
TreeModelListener

extends
EventListener
```

Defines the interface for an object that listens
to changes in a TreeModel.
For further information and examples see

How to Write a Tree Model Listener

,
a section in

The Java Tutorial.

public interface

TreeModelListener

extends

EventListener

Defines the interface for an object that listens
to changes in a TreeModel.
For further information and examples see

How to Write a Tree Model Listener

,
a section in

The Java Tutorial.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

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

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

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

---

#### Method Summary

Invoked after a node (or a set of siblings) has changed in some
way.

Invoked after nodes have been inserted into the tree.

Invoked after nodes have been removed from the tree.

Invoked after the tree has drastically changed structure from a
given node down.

============ METHOD DETAIL ==========

- Method Detail

- treeNodesChanged

```java
void treeNodesChanged​(
TreeModelEvent
e)
```

Invoked after a node (or a set of siblings) has changed in some
way. The node(s) have not changed locations in the tree or
altered their children arrays, but other attributes have
changed and may affect presentation. Example: the name of a
file has changed, but it is in the same location in the file
system.

To indicate the root has changed, childIndices and children
will be null.

Use

e.getPath()

to get the parent of the changed node(s).

e.getChildIndices()

returns the index(es) of the changed node(s).

**Parameters:** e

- a

TreeModelEvent

describing changes to a tree model

- treeNodesInserted

```java
void treeNodesInserted​(
TreeModelEvent
e)
```

Invoked after nodes have been inserted into the tree.

Use

e.getPath()

to get the parent of the new node(s).

e.getChildIndices()

returns the index(es) of the new node(s)
in ascending order.

**Parameters:** e

- a

TreeModelEvent

describing changes to a tree model

- treeNodesRemoved

```java
void treeNodesRemoved​(
TreeModelEvent
e)
```

Invoked after nodes have been removed from the tree. Note that
if a subtree is removed from the tree, this method may only be
invoked once for the root of the removed subtree, not once for
each individual set of siblings removed.

Use

e.getPath()

to get the former parent of the deleted
node(s).

e.getChildIndices()

returns, in ascending order, the
index(es) the node(s) had before being deleted.

**Parameters:** e

- a

TreeModelEvent

describing changes to a tree model

- treeStructureChanged

```java
void treeStructureChanged​(
TreeModelEvent
e)
```

Invoked after the tree has drastically changed structure from a
given node down. If the path returned by e.getPath() is of length
one and the first element does not identify the current root node
the first element should become the new root of the tree.

Use

e.getPath()

to get the path to the node.

e.getChildIndices()

returns null.

**Parameters:** e

- a

TreeModelEvent

describing changes to a tree model

Method Detail

- treeNodesChanged

```java
void treeNodesChanged​(
TreeModelEvent
e)
```

Invoked after a node (or a set of siblings) has changed in some
way. The node(s) have not changed locations in the tree or
altered their children arrays, but other attributes have
changed and may affect presentation. Example: the name of a
file has changed, but it is in the same location in the file
system.

To indicate the root has changed, childIndices and children
will be null.

Use

e.getPath()

to get the parent of the changed node(s).

e.getChildIndices()

returns the index(es) of the changed node(s).

**Parameters:** e

- a

TreeModelEvent

describing changes to a tree model

- treeNodesInserted

```java
void treeNodesInserted​(
TreeModelEvent
e)
```

Invoked after nodes have been inserted into the tree.

Use

e.getPath()

to get the parent of the new node(s).

e.getChildIndices()

returns the index(es) of the new node(s)
in ascending order.

**Parameters:** e

- a

TreeModelEvent

describing changes to a tree model

- treeNodesRemoved

```java
void treeNodesRemoved​(
TreeModelEvent
e)
```

Invoked after nodes have been removed from the tree. Note that
if a subtree is removed from the tree, this method may only be
invoked once for the root of the removed subtree, not once for
each individual set of siblings removed.

Use

e.getPath()

to get the former parent of the deleted
node(s).

e.getChildIndices()

returns, in ascending order, the
index(es) the node(s) had before being deleted.

**Parameters:** e

- a

TreeModelEvent

describing changes to a tree model

- treeStructureChanged

```java
void treeStructureChanged​(
TreeModelEvent
e)
```

Invoked after the tree has drastically changed structure from a
given node down. If the path returned by e.getPath() is of length
one and the first element does not identify the current root node
the first element should become the new root of the tree.

Use

e.getPath()

to get the path to the node.

e.getChildIndices()

returns null.

**Parameters:** e

- a

TreeModelEvent

describing changes to a tree model

---

#### Method Detail

treeNodesChanged

```java
void treeNodesChanged​(
TreeModelEvent
e)
```

Invoked after a node (or a set of siblings) has changed in some
way. The node(s) have not changed locations in the tree or
altered their children arrays, but other attributes have
changed and may affect presentation. Example: the name of a
file has changed, but it is in the same location in the file
system.

To indicate the root has changed, childIndices and children
will be null.

Use

e.getPath()

to get the parent of the changed node(s).

e.getChildIndices()

returns the index(es) of the changed node(s).

**Parameters:** e

- a

TreeModelEvent

describing changes to a tree model

---

#### treeNodesChanged

void treeNodesChanged​(

TreeModelEvent

e)

Invoked after a node (or a set of siblings) has changed in some
way. The node(s) have not changed locations in the tree or
altered their children arrays, but other attributes have
changed and may affect presentation. Example: the name of a
file has changed, but it is in the same location in the file
system.

To indicate the root has changed, childIndices and children
will be null.

Use

e.getPath()

to get the parent of the changed node(s).

e.getChildIndices()

returns the index(es) of the changed node(s).

To indicate the root has changed, childIndices and children
will be null.

Use

e.getPath()

to get the parent of the changed node(s).

e.getChildIndices()

returns the index(es) of the changed node(s).

Use

e.getPath()

to get the parent of the changed node(s).

e.getChildIndices()

returns the index(es) of the changed node(s).

treeNodesInserted

```java
void treeNodesInserted​(
TreeModelEvent
e)
```

Invoked after nodes have been inserted into the tree.

Use

e.getPath()

to get the parent of the new node(s).

e.getChildIndices()

returns the index(es) of the new node(s)
in ascending order.

**Parameters:** e

- a

TreeModelEvent

describing changes to a tree model

---

#### treeNodesInserted

void treeNodesInserted​(

TreeModelEvent

e)

Invoked after nodes have been inserted into the tree.

Use

e.getPath()

to get the parent of the new node(s).

e.getChildIndices()

returns the index(es) of the new node(s)
in ascending order.

Invoked after nodes have been inserted into the tree.

Use

e.getPath()

to get the parent of the new node(s).

e.getChildIndices()

returns the index(es) of the new node(s)
in ascending order.

treeNodesRemoved

```java
void treeNodesRemoved​(
TreeModelEvent
e)
```

Invoked after nodes have been removed from the tree. Note that
if a subtree is removed from the tree, this method may only be
invoked once for the root of the removed subtree, not once for
each individual set of siblings removed.

Use

e.getPath()

to get the former parent of the deleted
node(s).

e.getChildIndices()

returns, in ascending order, the
index(es) the node(s) had before being deleted.

**Parameters:** e

- a

TreeModelEvent

describing changes to a tree model

---

#### treeNodesRemoved

void treeNodesRemoved​(

TreeModelEvent

e)

Invoked after nodes have been removed from the tree. Note that
if a subtree is removed from the tree, this method may only be
invoked once for the root of the removed subtree, not once for
each individual set of siblings removed.

Use

e.getPath()

to get the former parent of the deleted
node(s).

e.getChildIndices()

returns, in ascending order, the
index(es) the node(s) had before being deleted.

Invoked after nodes have been removed from the tree. Note that
if a subtree is removed from the tree, this method may only be
invoked once for the root of the removed subtree, not once for
each individual set of siblings removed.

Use

e.getPath()

to get the former parent of the deleted
node(s).

e.getChildIndices()

returns, in ascending order, the
index(es) the node(s) had before being deleted.

treeStructureChanged

```java
void treeStructureChanged​(
TreeModelEvent
e)
```

Invoked after the tree has drastically changed structure from a
given node down. If the path returned by e.getPath() is of length
one and the first element does not identify the current root node
the first element should become the new root of the tree.

Use

e.getPath()

to get the path to the node.

e.getChildIndices()

returns null.

**Parameters:** e

- a

TreeModelEvent

describing changes to a tree model

---

#### treeStructureChanged

void treeStructureChanged​(

TreeModelEvent

e)

Invoked after the tree has drastically changed structure from a
given node down. If the path returned by e.getPath() is of length
one and the first element does not identify the current root node
the first element should become the new root of the tree.

Use

e.getPath()

to get the path to the node.

e.getChildIndices()

returns null.

Use

e.getPath()

to get the path to the node.

e.getChildIndices()

returns null.

---

