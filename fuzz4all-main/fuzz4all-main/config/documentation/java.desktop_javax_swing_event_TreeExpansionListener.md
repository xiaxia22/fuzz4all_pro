# Interface TreeExpansionListener

**Source:** `java.desktop\javax\swing\event\TreeExpansionListener.html`

### Class Description

```java
public interface
TreeExpansionListener

extends
EventListener
```

The listener that's notified when a tree expands or collapses
a node.
For further documentation and examples see

How to Write a Tree Expansion Listener

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

#### void treeExpanded​(
TreeExpansionEvent
event)

Called whenever an item in the tree has been expanded.

**Parameters:**
- event

- a

TreeExpansionEvent

containing a

TreePath

object for the expanded node

---

#### void treeCollapsed​(
TreeExpansionEvent
event)

Called whenever an item in the tree has been collapsed.

**Parameters:**
- event

- a

TreeExpansionEvent

containing a

TreePath

object for the collapsed node

---

### Additional Sections

#### Interface TreeExpansionListener

**All Superinterfaces:** EventListener

**All Known Implementing Classes:** BasicTreeUI.TreeExpansionHandler

,

JTree.AccessibleJTree

```java
public interface
TreeExpansionListener

extends
EventListener
```

The listener that's notified when a tree expands or collapses
a node.
For further documentation and examples see

How to Write a Tree Expansion Listener

,
a section in

The Java Tutorial.

public interface

TreeExpansionListener

extends

EventListener

The listener that's notified when a tree expands or collapses
a node.
For further documentation and examples see

How to Write a Tree Expansion Listener

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

treeCollapsed

​(

TreeExpansionEvent

event)

Called whenever an item in the tree has been collapsed.

void

treeExpanded

​(

TreeExpansionEvent

event)

Called whenever an item in the tree has been expanded.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

treeCollapsed

​(

TreeExpansionEvent

event)

Called whenever an item in the tree has been collapsed.

void

treeExpanded

​(

TreeExpansionEvent

event)

Called whenever an item in the tree has been expanded.

---

#### Method Summary

Called whenever an item in the tree has been collapsed.

Called whenever an item in the tree has been expanded.

============ METHOD DETAIL ==========

- Method Detail

- treeExpanded

```java
void treeExpanded​(
TreeExpansionEvent
event)
```

Called whenever an item in the tree has been expanded.

**Parameters:** event

- a

TreeExpansionEvent

containing a

TreePath

object for the expanded node

- treeCollapsed

```java
void treeCollapsed​(
TreeExpansionEvent
event)
```

Called whenever an item in the tree has been collapsed.

**Parameters:** event

- a

TreeExpansionEvent

containing a

TreePath

object for the collapsed node

Method Detail

- treeExpanded

```java
void treeExpanded​(
TreeExpansionEvent
event)
```

Called whenever an item in the tree has been expanded.

**Parameters:** event

- a

TreeExpansionEvent

containing a

TreePath

object for the expanded node

- treeCollapsed

```java
void treeCollapsed​(
TreeExpansionEvent
event)
```

Called whenever an item in the tree has been collapsed.

**Parameters:** event

- a

TreeExpansionEvent

containing a

TreePath

object for the collapsed node

---

#### Method Detail

treeExpanded

```java
void treeExpanded​(
TreeExpansionEvent
event)
```

Called whenever an item in the tree has been expanded.

**Parameters:** event

- a

TreeExpansionEvent

containing a

TreePath

object for the expanded node

---

#### treeExpanded

void treeExpanded​(

TreeExpansionEvent

event)

Called whenever an item in the tree has been expanded.

treeCollapsed

```java
void treeCollapsed​(
TreeExpansionEvent
event)
```

Called whenever an item in the tree has been collapsed.

**Parameters:** event

- a

TreeExpansionEvent

containing a

TreePath

object for the collapsed node

---

#### treeCollapsed

void treeCollapsed​(

TreeExpansionEvent

event)

Called whenever an item in the tree has been collapsed.

---

