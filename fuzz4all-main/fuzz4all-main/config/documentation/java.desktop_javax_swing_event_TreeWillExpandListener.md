# Interface TreeWillExpandListener

**Source:** `java.desktop\javax\swing\event\TreeWillExpandListener.html`

### Class Description

```java
public interface
TreeWillExpandListener

extends
EventListener
```

The listener that's notified when a tree expands or collapses
a node.
For further information and examples see

How to Write a Tree-Will-Expand Listener

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

#### void treeWillExpand​(
TreeExpansionEvent
event)
throws
ExpandVetoException

Invoked whenever a node in the tree is about to be expanded.

**Parameters:**
- event

- a

TreeExpansionEvent

containing a

TreePath

object for the node

**Throws:**
- ExpandVetoException

- to signify expansion has been canceled

---

#### void treeWillCollapse​(
TreeExpansionEvent
event)
throws
ExpandVetoException

Invoked whenever a node in the tree is about to be collapsed.

**Parameters:**
- event

- a

TreeExpansionEvent

containing a

TreePath

object for the node

**Throws:**
- ExpandVetoException

- to signify collapse has been canceled

---

### Additional Sections

#### Interface TreeWillExpandListener

**All Superinterfaces:** EventListener

```java
public interface
TreeWillExpandListener

extends
EventListener
```

The listener that's notified when a tree expands or collapses
a node.
For further information and examples see

How to Write a Tree-Will-Expand Listener

,
a section in

The Java Tutorial.

public interface

TreeWillExpandListener

extends

EventListener

The listener that's notified when a tree expands or collapses
a node.
For further information and examples see

How to Write a Tree-Will-Expand Listener

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

treeWillCollapse

​(

TreeExpansionEvent

event)

Invoked whenever a node in the tree is about to be collapsed.

void

treeWillExpand

​(

TreeExpansionEvent

event)

Invoked whenever a node in the tree is about to be expanded.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

treeWillCollapse

​(

TreeExpansionEvent

event)

Invoked whenever a node in the tree is about to be collapsed.

void

treeWillExpand

​(

TreeExpansionEvent

event)

Invoked whenever a node in the tree is about to be expanded.

---

#### Method Summary

Invoked whenever a node in the tree is about to be collapsed.

Invoked whenever a node in the tree is about to be expanded.

============ METHOD DETAIL ==========

- Method Detail

- treeWillExpand

```java
void treeWillExpand​(
TreeExpansionEvent
event)
throws
ExpandVetoException
```

Invoked whenever a node in the tree is about to be expanded.

**Parameters:** event

- a

TreeExpansionEvent

containing a

TreePath

object for the node
**Throws:** ExpandVetoException

- to signify expansion has been canceled

- treeWillCollapse

```java
void treeWillCollapse​(
TreeExpansionEvent
event)
throws
ExpandVetoException
```

Invoked whenever a node in the tree is about to be collapsed.

**Parameters:** event

- a

TreeExpansionEvent

containing a

TreePath

object for the node
**Throws:** ExpandVetoException

- to signify collapse has been canceled

Method Detail

- treeWillExpand

```java
void treeWillExpand​(
TreeExpansionEvent
event)
throws
ExpandVetoException
```

Invoked whenever a node in the tree is about to be expanded.

**Parameters:** event

- a

TreeExpansionEvent

containing a

TreePath

object for the node
**Throws:** ExpandVetoException

- to signify expansion has been canceled

- treeWillCollapse

```java
void treeWillCollapse​(
TreeExpansionEvent
event)
throws
ExpandVetoException
```

Invoked whenever a node in the tree is about to be collapsed.

**Parameters:** event

- a

TreeExpansionEvent

containing a

TreePath

object for the node
**Throws:** ExpandVetoException

- to signify collapse has been canceled

---

#### Method Detail

treeWillExpand

```java
void treeWillExpand​(
TreeExpansionEvent
event)
throws
ExpandVetoException
```

Invoked whenever a node in the tree is about to be expanded.

**Parameters:** event

- a

TreeExpansionEvent

containing a

TreePath

object for the node
**Throws:** ExpandVetoException

- to signify expansion has been canceled

---

#### treeWillExpand

void treeWillExpand​(

TreeExpansionEvent

event)
throws

ExpandVetoException

Invoked whenever a node in the tree is about to be expanded.

treeWillCollapse

```java
void treeWillCollapse​(
TreeExpansionEvent
event)
throws
ExpandVetoException
```

Invoked whenever a node in the tree is about to be collapsed.

**Parameters:** event

- a

TreeExpansionEvent

containing a

TreePath

object for the node
**Throws:** ExpandVetoException

- to signify collapse has been canceled

---

#### treeWillCollapse

void treeWillCollapse​(

TreeExpansionEvent

event)
throws

ExpandVetoException

Invoked whenever a node in the tree is about to be collapsed.

---

