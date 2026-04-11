# Class TreePath

**Source:** `jdk.compiler\com\sun\source\util\TreePath.html`

### Class Description

```java
public class
TreePath

extends
Object

implements
Iterable
<
Tree
>
```

A path of tree nodes, typically used to represent the sequence of ancestor
nodes of a tree node up to the top level CompilationUnitTree node.

**All Implemented Interfaces:** Iterable

<

Tree

>

---

### Field Details

*No entries found.*

### Constructor Details

#### public TreePath​(
CompilationUnitTree
node)

Creates a TreePath for a root node.

**Parameters:**
- node

- the root node

---

#### public TreePath​(
TreePath
path,

Tree
tree)

Creates a TreePath for a child node.

**Parameters:**
- path

- the parent path
- tree

- the child node

---

### Method Details

#### public static
TreePath
getPath​(
CompilationUnitTree
unit,

Tree
target)

Returns a tree path for a tree node within a compilation unit,
or

null

if the node is not found.

**Parameters:**
- unit

- the compilation unit to search
- target

- the node to locate

**Returns:**
- the tree path

---

#### public static
TreePath
getPath​(
TreePath
path,

Tree
target)

Returns a tree path for a tree node within a subtree identified by a TreePath object.
Returns

null

if the node is not found.

**Parameters:**
- path

- the path in which to search
- target

- the node to locate

**Returns:**
- the tree path of the target node

---

#### public
CompilationUnitTree
getCompilationUnit()

Returns the compilation unit associated with this path.

**Returns:**
- the compilation unit

---

#### public
Tree
getLeaf()

Returns the leaf node for this path.

**Returns:**
- the leaf node

---

#### public
TreePath
getParentPath()

Returns the path for the enclosing node, or

null

if there is no enclosing node.

**Returns:**
- the path for the enclosing node

---

#### public
Iterator
<
Tree
> iterator()

Iterates from leaves to root.

**Specified by:**
- iterator

in interface

Iterable

<

Tree

>

**Returns:**
- an Iterator.

---

### Additional Sections

#### Class TreePath

java.lang.Object

- com.sun.source.util.TreePath

com.sun.source.util.TreePath

**All Implemented Interfaces:** Iterable

<

Tree

>

```java
public class
TreePath

extends
Object

implements
Iterable
<
Tree
>
```

A path of tree nodes, typically used to represent the sequence of ancestor
nodes of a tree node up to the top level CompilationUnitTree node.

**Since:** 1.6

public class

TreePath

extends

Object

implements

Iterable

<

Tree

>

A path of tree nodes, typically used to represent the sequence of ancestor
nodes of a tree node up to the top level CompilationUnitTree node.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TreePath

​(

CompilationUnitTree

node)

Creates a TreePath for a root node.

TreePath

​(

TreePath

path,

Tree

tree)

Creates a TreePath for a child node.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

CompilationUnitTree

getCompilationUnit

()

Returns the compilation unit associated with this path.

Tree

getLeaf

()

Returns the leaf node for this path.

TreePath

getParentPath

()

Returns the path for the enclosing node, or

null

if there is no enclosing node.

static

TreePath

getPath

​(

CompilationUnitTree

unit,

Tree

target)

Returns a tree path for a tree node within a compilation unit,
or

null

if the node is not found.

static

TreePath

getPath

​(

TreePath

path,

Tree

target)

Returns a tree path for a tree node within a subtree identified by a TreePath object.

Iterator

<

Tree

>

iterator

()

Iterates from leaves to root.

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

spliterator

Constructor Summary

Constructors

Constructor

Description

TreePath

​(

CompilationUnitTree

node)

Creates a TreePath for a root node.

TreePath

​(

TreePath

path,

Tree

tree)

Creates a TreePath for a child node.

---

#### Constructor Summary

Creates a TreePath for a root node.

Creates a TreePath for a child node.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

CompilationUnitTree

getCompilationUnit

()

Returns the compilation unit associated with this path.

Tree

getLeaf

()

Returns the leaf node for this path.

TreePath

getParentPath

()

Returns the path for the enclosing node, or

null

if there is no enclosing node.

static

TreePath

getPath

​(

CompilationUnitTree

unit,

Tree

target)

Returns a tree path for a tree node within a compilation unit,
or

null

if the node is not found.

static

TreePath

getPath

​(

TreePath

path,

Tree

target)

Returns a tree path for a tree node within a subtree identified by a TreePath object.

Iterator

<

Tree

>

iterator

()

Iterates from leaves to root.

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

spliterator

---

#### Method Summary

Returns the compilation unit associated with this path.

Returns the leaf node for this path.

Returns the path for the enclosing node, or

null

if there is no enclosing node.

Returns a tree path for a tree node within a compilation unit,
or

null

if the node is not found.

Returns a tree path for a tree node within a subtree identified by a TreePath object.

Iterates from leaves to root.

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

spliterator

---

#### Methods declared in interface java.lang. Iterable

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TreePath

```java
public TreePath​(
CompilationUnitTree
node)
```

Creates a TreePath for a root node.

**Parameters:** node

- the root node

- TreePath

```java
public TreePath​(
TreePath
path,

Tree
tree)
```

Creates a TreePath for a child node.

**Parameters:** path

- the parent path
**Parameters:** tree

- the child node

============ METHOD DETAIL ==========

- Method Detail

- getPath

```java
public static
TreePath
getPath​(
CompilationUnitTree
unit,

Tree
target)
```

Returns a tree path for a tree node within a compilation unit,
or

null

if the node is not found.

**Parameters:** unit

- the compilation unit to search
**Parameters:** target

- the node to locate
**Returns:** the tree path

- getPath

```java
public static
TreePath
getPath​(
TreePath
path,

Tree
target)
```

Returns a tree path for a tree node within a subtree identified by a TreePath object.
Returns

null

if the node is not found.

**Parameters:** path

- the path in which to search
**Parameters:** target

- the node to locate
**Returns:** the tree path of the target node

- getCompilationUnit

```java
public
CompilationUnitTree
getCompilationUnit()
```

Returns the compilation unit associated with this path.

**Returns:** the compilation unit

- getLeaf

```java
public
Tree
getLeaf()
```

Returns the leaf node for this path.

**Returns:** the leaf node

- getParentPath

```java
public
TreePath
getParentPath()
```

Returns the path for the enclosing node, or

null

if there is no enclosing node.

**Returns:** the path for the enclosing node

- iterator

```java
public
Iterator
<
Tree
> iterator()
```

Iterates from leaves to root.

**Specified by:** iterator

in interface

Iterable

<

Tree

>
**Returns:** an Iterator.

Constructor Detail

- TreePath

```java
public TreePath​(
CompilationUnitTree
node)
```

Creates a TreePath for a root node.

**Parameters:** node

- the root node

- TreePath

```java
public TreePath​(
TreePath
path,

Tree
tree)
```

Creates a TreePath for a child node.

**Parameters:** path

- the parent path
**Parameters:** tree

- the child node

---

#### Constructor Detail

TreePath

```java
public TreePath​(
CompilationUnitTree
node)
```

Creates a TreePath for a root node.

**Parameters:** node

- the root node

---

#### TreePath

public TreePath​(

CompilationUnitTree

node)

Creates a TreePath for a root node.

TreePath

```java
public TreePath​(
TreePath
path,

Tree
tree)
```

Creates a TreePath for a child node.

**Parameters:** path

- the parent path
**Parameters:** tree

- the child node

---

#### TreePath

public TreePath​(

TreePath

path,

Tree

tree)

Creates a TreePath for a child node.

Method Detail

- getPath

```java
public static
TreePath
getPath​(
CompilationUnitTree
unit,

Tree
target)
```

Returns a tree path for a tree node within a compilation unit,
or

null

if the node is not found.

**Parameters:** unit

- the compilation unit to search
**Parameters:** target

- the node to locate
**Returns:** the tree path

- getPath

```java
public static
TreePath
getPath​(
TreePath
path,

Tree
target)
```

Returns a tree path for a tree node within a subtree identified by a TreePath object.
Returns

null

if the node is not found.

**Parameters:** path

- the path in which to search
**Parameters:** target

- the node to locate
**Returns:** the tree path of the target node

- getCompilationUnit

```java
public
CompilationUnitTree
getCompilationUnit()
```

Returns the compilation unit associated with this path.

**Returns:** the compilation unit

- getLeaf

```java
public
Tree
getLeaf()
```

Returns the leaf node for this path.

**Returns:** the leaf node

- getParentPath

```java
public
TreePath
getParentPath()
```

Returns the path for the enclosing node, or

null

if there is no enclosing node.

**Returns:** the path for the enclosing node

- iterator

```java
public
Iterator
<
Tree
> iterator()
```

Iterates from leaves to root.

**Specified by:** iterator

in interface

Iterable

<

Tree

>
**Returns:** an Iterator.

---

#### Method Detail

getPath

```java
public static
TreePath
getPath​(
CompilationUnitTree
unit,

Tree
target)
```

Returns a tree path for a tree node within a compilation unit,
or

null

if the node is not found.

**Parameters:** unit

- the compilation unit to search
**Parameters:** target

- the node to locate
**Returns:** the tree path

---

#### getPath

public static

TreePath

getPath​(

CompilationUnitTree

unit,

Tree

target)

Returns a tree path for a tree node within a compilation unit,
or

null

if the node is not found.

getPath

```java
public static
TreePath
getPath​(
TreePath
path,

Tree
target)
```

Returns a tree path for a tree node within a subtree identified by a TreePath object.
Returns

null

if the node is not found.

**Parameters:** path

- the path in which to search
**Parameters:** target

- the node to locate
**Returns:** the tree path of the target node

---

#### getPath

public static

TreePath

getPath​(

TreePath

path,

Tree

target)

Returns a tree path for a tree node within a subtree identified by a TreePath object.
Returns

null

if the node is not found.

getCompilationUnit

```java
public
CompilationUnitTree
getCompilationUnit()
```

Returns the compilation unit associated with this path.

**Returns:** the compilation unit

---

#### getCompilationUnit

public

CompilationUnitTree

getCompilationUnit()

Returns the compilation unit associated with this path.

getLeaf

```java
public
Tree
getLeaf()
```

Returns the leaf node for this path.

**Returns:** the leaf node

---

#### getLeaf

public

Tree

getLeaf()

Returns the leaf node for this path.

getParentPath

```java
public
TreePath
getParentPath()
```

Returns the path for the enclosing node, or

null

if there is no enclosing node.

**Returns:** the path for the enclosing node

---

#### getParentPath

public

TreePath

getParentPath()

Returns the path for the enclosing node, or

null

if there is no enclosing node.

iterator

```java
public
Iterator
<
Tree
> iterator()
```

Iterates from leaves to root.

**Specified by:** iterator

in interface

Iterable

<

Tree

>
**Returns:** an Iterator.

---

#### iterator

public

Iterator

<

Tree

> iterator()

Iterates from leaves to root.

---

