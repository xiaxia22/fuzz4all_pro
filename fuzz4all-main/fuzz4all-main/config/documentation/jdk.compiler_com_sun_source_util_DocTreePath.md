# Class DocTreePath

**Source:** `jdk.compiler\com\sun\source\util\DocTreePath.html`

### Class Description

```java
public class
DocTreePath

extends
Object

implements
Iterable
<
DocTree
>
```

A path of tree nodes, typically used to represent the sequence of ancestor
nodes of a tree node up to the top level DocCommentTree node.

**All Implemented Interfaces:** Iterable

<

DocTree

>

---

### Field Details

*No entries found.*

### Constructor Details

#### public DocTreePath​(
TreePath
treePath,

DocCommentTree
t)

Creates a DocTreePath for a root node.

**Parameters:**
- treePath

- the TreePath from which the root node was created.
- t

- the DocCommentTree to create the path for.

---

#### public DocTreePath​(
DocTreePath
p,

DocTree
t)

Creates a DocTreePath for a child node.

**Parameters:**
- p

- the parent node
- t

- the child node

---

### Method Details

#### public static
DocTreePath
getPath​(
TreePath
treePath,

DocCommentTree
doc,

DocTree
target)

Returns a documentation tree path for a tree node within a compilation unit,
or

null

if the node is not found.

**Parameters:**
- treePath

- the path for the node with which the doc comment is associated
- doc

- the doc comment associated with the node
- target

- a node within the doc comment

**Returns:**
- a path identifying the target within the tree

---

#### public static
DocTreePath
getPath​(
DocTreePath
path,

DocTree
target)

Returns a documentation tree path for a tree node within a subtree
identified by a DocTreePath object, or

null

if the node is not found.

**Parameters:**
- path

- a path identifying a node within a doc comment tree
- target

- a node to be located within the given node

**Returns:**
- a path identifying the target node

---

#### public
TreePath
getTreePath()

Returns the TreePath associated with this path.

**Returns:**
- the TreePath for this DocTreePath

---

#### public
DocCommentTree
getDocComment()

Returns the DocCommentTree associated with this path.

**Returns:**
- the DocCommentTree for this DocTreePath

---

#### public
DocTree
getLeaf()

Returns the leaf node for this path.

**Returns:**
- the DocTree for this DocTreePath

---

#### public
DocTreePath
getParentPath()

Returns the path for the enclosing node, or

null

if there is no enclosing node.

**Returns:**
- DocTreePath of parent

---

### Additional Sections

#### Class DocTreePath

java.lang.Object

- com.sun.source.util.DocTreePath

com.sun.source.util.DocTreePath

**All Implemented Interfaces:** Iterable

<

DocTree

>

```java
public class
DocTreePath

extends
Object

implements
Iterable
<
DocTree
>
```

A path of tree nodes, typically used to represent the sequence of ancestor
nodes of a tree node up to the top level DocCommentTree node.

**Since:** 1.8

public class

DocTreePath

extends

Object

implements

Iterable

<

DocTree

>

A path of tree nodes, typically used to represent the sequence of ancestor
nodes of a tree node up to the top level DocCommentTree node.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DocTreePath

​(

DocTreePath

p,

DocTree

t)

Creates a DocTreePath for a child node.

DocTreePath

​(

TreePath

treePath,

DocCommentTree

t)

Creates a DocTreePath for a root node.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

DocCommentTree

getDocComment

()

Returns the DocCommentTree associated with this path.

DocTree

getLeaf

()

Returns the leaf node for this path.

DocTreePath

getParentPath

()

Returns the path for the enclosing node, or

null

if there is no enclosing node.

static

DocTreePath

getPath

​(

DocTreePath

path,

DocTree

target)

Returns a documentation tree path for a tree node within a subtree
identified by a DocTreePath object, or

null

if the node is not found.

static

DocTreePath

getPath

​(

TreePath

treePath,

DocCommentTree

doc,

DocTree

target)

Returns a documentation tree path for a tree node within a compilation unit,
or

null

if the node is not found.

TreePath

getTreePath

()

Returns the TreePath associated with this path.

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

- Methods declared in interface java.lang.

Iterable

forEach

,

iterator

,

spliterator

Constructor Summary

Constructors

Constructor

Description

DocTreePath

​(

DocTreePath

p,

DocTree

t)

Creates a DocTreePath for a child node.

DocTreePath

​(

TreePath

treePath,

DocCommentTree

t)

Creates a DocTreePath for a root node.

---

#### Constructor Summary

Creates a DocTreePath for a child node.

Creates a DocTreePath for a root node.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

DocCommentTree

getDocComment

()

Returns the DocCommentTree associated with this path.

DocTree

getLeaf

()

Returns the leaf node for this path.

DocTreePath

getParentPath

()

Returns the path for the enclosing node, or

null

if there is no enclosing node.

static

DocTreePath

getPath

​(

DocTreePath

path,

DocTree

target)

Returns a documentation tree path for a tree node within a subtree
identified by a DocTreePath object, or

null

if the node is not found.

static

DocTreePath

getPath

​(

TreePath

treePath,

DocCommentTree

doc,

DocTree

target)

Returns a documentation tree path for a tree node within a compilation unit,
or

null

if the node is not found.

TreePath

getTreePath

()

Returns the TreePath associated with this path.

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

- Methods declared in interface java.lang.

Iterable

forEach

,

iterator

,

spliterator

---

#### Method Summary

Returns the DocCommentTree associated with this path.

Returns the leaf node for this path.

Returns the path for the enclosing node, or

null

if there is no enclosing node.

Returns a documentation tree path for a tree node within a subtree
identified by a DocTreePath object, or

null

if the node is not found.

Returns a documentation tree path for a tree node within a compilation unit,
or

null

if the node is not found.

Returns the TreePath associated with this path.

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

Methods declared in interface java.lang.

Iterable

forEach

,

iterator

,

spliterator

---

#### Methods declared in interface java.lang. Iterable

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DocTreePath

```java
public DocTreePath​(
TreePath
treePath,

DocCommentTree
t)
```

Creates a DocTreePath for a root node.

**Parameters:** treePath

- the TreePath from which the root node was created.
**Parameters:** t

- the DocCommentTree to create the path for.

- DocTreePath

```java
public DocTreePath​(
DocTreePath
p,

DocTree
t)
```

Creates a DocTreePath for a child node.

**Parameters:** p

- the parent node
**Parameters:** t

- the child node

============ METHOD DETAIL ==========

- Method Detail

- getPath

```java
public static
DocTreePath
getPath​(
TreePath
treePath,

DocCommentTree
doc,

DocTree
target)
```

Returns a documentation tree path for a tree node within a compilation unit,
or

null

if the node is not found.

**Parameters:** treePath

- the path for the node with which the doc comment is associated
**Parameters:** doc

- the doc comment associated with the node
**Parameters:** target

- a node within the doc comment
**Returns:** a path identifying the target within the tree

- getPath

```java
public static
DocTreePath
getPath​(
DocTreePath
path,

DocTree
target)
```

Returns a documentation tree path for a tree node within a subtree
identified by a DocTreePath object, or

null

if the node is not found.

**Parameters:** path

- a path identifying a node within a doc comment tree
**Parameters:** target

- a node to be located within the given node
**Returns:** a path identifying the target node

- getTreePath

```java
public
TreePath
getTreePath()
```

Returns the TreePath associated with this path.

**Returns:** the TreePath for this DocTreePath

- getDocComment

```java
public
DocCommentTree
getDocComment()
```

Returns the DocCommentTree associated with this path.

**Returns:** the DocCommentTree for this DocTreePath

- getLeaf

```java
public
DocTree
getLeaf()
```

Returns the leaf node for this path.

**Returns:** the DocTree for this DocTreePath

- getParentPath

```java
public
DocTreePath
getParentPath()
```

Returns the path for the enclosing node, or

null

if there is no enclosing node.

**Returns:** DocTreePath of parent

Constructor Detail

- DocTreePath

```java
public DocTreePath​(
TreePath
treePath,

DocCommentTree
t)
```

Creates a DocTreePath for a root node.

**Parameters:** treePath

- the TreePath from which the root node was created.
**Parameters:** t

- the DocCommentTree to create the path for.

- DocTreePath

```java
public DocTreePath​(
DocTreePath
p,

DocTree
t)
```

Creates a DocTreePath for a child node.

**Parameters:** p

- the parent node
**Parameters:** t

- the child node

---

#### Constructor Detail

DocTreePath

```java
public DocTreePath​(
TreePath
treePath,

DocCommentTree
t)
```

Creates a DocTreePath for a root node.

**Parameters:** treePath

- the TreePath from which the root node was created.
**Parameters:** t

- the DocCommentTree to create the path for.

---

#### DocTreePath

public DocTreePath​(

TreePath

treePath,

DocCommentTree

t)

Creates a DocTreePath for a root node.

DocTreePath

```java
public DocTreePath​(
DocTreePath
p,

DocTree
t)
```

Creates a DocTreePath for a child node.

**Parameters:** p

- the parent node
**Parameters:** t

- the child node

---

#### DocTreePath

public DocTreePath​(

DocTreePath

p,

DocTree

t)

Creates a DocTreePath for a child node.

Method Detail

- getPath

```java
public static
DocTreePath
getPath​(
TreePath
treePath,

DocCommentTree
doc,

DocTree
target)
```

Returns a documentation tree path for a tree node within a compilation unit,
or

null

if the node is not found.

**Parameters:** treePath

- the path for the node with which the doc comment is associated
**Parameters:** doc

- the doc comment associated with the node
**Parameters:** target

- a node within the doc comment
**Returns:** a path identifying the target within the tree

- getPath

```java
public static
DocTreePath
getPath​(
DocTreePath
path,

DocTree
target)
```

Returns a documentation tree path for a tree node within a subtree
identified by a DocTreePath object, or

null

if the node is not found.

**Parameters:** path

- a path identifying a node within a doc comment tree
**Parameters:** target

- a node to be located within the given node
**Returns:** a path identifying the target node

- getTreePath

```java
public
TreePath
getTreePath()
```

Returns the TreePath associated with this path.

**Returns:** the TreePath for this DocTreePath

- getDocComment

```java
public
DocCommentTree
getDocComment()
```

Returns the DocCommentTree associated with this path.

**Returns:** the DocCommentTree for this DocTreePath

- getLeaf

```java
public
DocTree
getLeaf()
```

Returns the leaf node for this path.

**Returns:** the DocTree for this DocTreePath

- getParentPath

```java
public
DocTreePath
getParentPath()
```

Returns the path for the enclosing node, or

null

if there is no enclosing node.

**Returns:** DocTreePath of parent

---

#### Method Detail

getPath

```java
public static
DocTreePath
getPath​(
TreePath
treePath,

DocCommentTree
doc,

DocTree
target)
```

Returns a documentation tree path for a tree node within a compilation unit,
or

null

if the node is not found.

**Parameters:** treePath

- the path for the node with which the doc comment is associated
**Parameters:** doc

- the doc comment associated with the node
**Parameters:** target

- a node within the doc comment
**Returns:** a path identifying the target within the tree

---

#### getPath

public static

DocTreePath

getPath​(

TreePath

treePath,

DocCommentTree

doc,

DocTree

target)

Returns a documentation tree path for a tree node within a compilation unit,
or

null

if the node is not found.

getPath

```java
public static
DocTreePath
getPath​(
DocTreePath
path,

DocTree
target)
```

Returns a documentation tree path for a tree node within a subtree
identified by a DocTreePath object, or

null

if the node is not found.

**Parameters:** path

- a path identifying a node within a doc comment tree
**Parameters:** target

- a node to be located within the given node
**Returns:** a path identifying the target node

---

#### getPath

public static

DocTreePath

getPath​(

DocTreePath

path,

DocTree

target)

Returns a documentation tree path for a tree node within a subtree
identified by a DocTreePath object, or

null

if the node is not found.

getTreePath

```java
public
TreePath
getTreePath()
```

Returns the TreePath associated with this path.

**Returns:** the TreePath for this DocTreePath

---

#### getTreePath

public

TreePath

getTreePath()

Returns the TreePath associated with this path.

getDocComment

```java
public
DocCommentTree
getDocComment()
```

Returns the DocCommentTree associated with this path.

**Returns:** the DocCommentTree for this DocTreePath

---

#### getDocComment

public

DocCommentTree

getDocComment()

Returns the DocCommentTree associated with this path.

getLeaf

```java
public
DocTree
getLeaf()
```

Returns the leaf node for this path.

**Returns:** the DocTree for this DocTreePath

---

#### getLeaf

public

DocTree

getLeaf()

Returns the leaf node for this path.

getParentPath

```java
public
DocTreePath
getParentPath()
```

Returns the path for the enclosing node, or

null

if there is no enclosing node.

**Returns:** DocTreePath of parent

---

#### getParentPath

public

DocTreePath

getParentPath()

Returns the path for the enclosing node, or

null

if there is no enclosing node.

---

