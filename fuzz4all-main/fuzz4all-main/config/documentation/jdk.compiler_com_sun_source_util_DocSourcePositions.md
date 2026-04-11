# Interface DocSourcePositions

**Source:** `jdk.compiler\com\sun\source\util\DocSourcePositions.html`

### Class Description

```java
public interface
DocSourcePositions

extends
SourcePositions
```

Provides methods to obtain the position of a DocTree within a javadoc comment.
A position is defined as a simple character offset from the start of a
CompilationUnit where the first character is at offset 0.

**All Superinterfaces:** SourcePositions

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### long getStartPosition​(
CompilationUnitTree
file,

DocCommentTree
comment,

DocTree
tree)

Returns the starting position of the tree within the comment within the file. If tree is not found within
file, or if the starting position is not available,
return

Diagnostic.NOPOS

.
The given tree should be under the given comment tree, and the given documentation
comment tree should be returned from a

DocTrees.getDocCommentTree(com.sun.source.util.TreePath)

for a tree under the given file.
The returned position must be at the start of the yield of this tree, that
is for any sub-tree of this tree, the following must hold:

tree.getStartPosition() <= subtree.getStartPosition()

or

tree.getStartPosition() == NOPOS

or

subtree.getStartPosition() == NOPOS

**Parameters:**
- file

- CompilationUnit in which to find tree.
- comment

- the comment tree that encloses the tree for which the
position is being sought
- tree

- tree for which a position is sought.

**Returns:**
- the start position of tree.

---

#### long getEndPosition​(
CompilationUnitTree
file,

DocCommentTree
comment,

DocTree
tree)

Returns the ending position of the tree within the comment within the file. If tree is not found within
file, or if the ending position is not available,
return

Diagnostic.NOPOS

.
The given tree should be under the given comment tree, and the given documentation
comment tree should be returned from a

DocTrees.getDocCommentTree(com.sun.source.util.TreePath)

for a tree under the given file.
The returned position must be at the end of the yield of this tree,
that is for any sub-tree of this tree, the following must hold:

tree.getEndPosition() >= subtree.getEndPosition()

or

tree.getEndPosition() == NOPOS

or

subtree.getEndPosition() == NOPOS

In addition, the following must hold:

tree.getStartPosition() <= tree.getEndPosition()

or

tree.getStartPosition() == NOPOS

or

tree.getEndPosition() == NOPOS

**Parameters:**
- file

- CompilationUnit in which to find tree.
- comment

- the comment tree that encloses the tree for which the
position is being sought
- tree

- tree for which a position is sought.

**Returns:**
- the start position of tree.

---

### Additional Sections

#### Interface DocSourcePositions

**All Superinterfaces:** SourcePositions

```java
public interface
DocSourcePositions

extends
SourcePositions
```

Provides methods to obtain the position of a DocTree within a javadoc comment.
A position is defined as a simple character offset from the start of a
CompilationUnit where the first character is at offset 0.

**Since:** 1.8

public interface

DocSourcePositions

extends

SourcePositions

Provides methods to obtain the position of a DocTree within a javadoc comment.
A position is defined as a simple character offset from the start of a
CompilationUnit where the first character is at offset 0.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

long

getEndPosition

​(

CompilationUnitTree

file,

DocCommentTree

comment,

DocTree

tree)

Returns the ending position of the tree within the comment within the file.

long

getStartPosition

​(

CompilationUnitTree

file,

DocCommentTree

comment,

DocTree

tree)

Returns the starting position of the tree within the comment within the file.

- Methods declared in interface com.sun.source.util.

SourcePositions

getEndPosition

,

getStartPosition

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

long

getEndPosition

​(

CompilationUnitTree

file,

DocCommentTree

comment,

DocTree

tree)

Returns the ending position of the tree within the comment within the file.

long

getStartPosition

​(

CompilationUnitTree

file,

DocCommentTree

comment,

DocTree

tree)

Returns the starting position of the tree within the comment within the file.

- Methods declared in interface com.sun.source.util.

SourcePositions

getEndPosition

,

getStartPosition

---

#### Method Summary

Returns the ending position of the tree within the comment within the file.

Returns the starting position of the tree within the comment within the file.

Methods declared in interface com.sun.source.util.

SourcePositions

getEndPosition

,

getStartPosition

---

#### Methods declared in interface com.sun.source.util. SourcePositions

============ METHOD DETAIL ==========

- Method Detail

- getStartPosition

```java
long getStartPosition​(
CompilationUnitTree
file,

DocCommentTree
comment,

DocTree
tree)
```

Returns the starting position of the tree within the comment within the file. If tree is not found within
file, or if the starting position is not available,
return

Diagnostic.NOPOS

.
The given tree should be under the given comment tree, and the given documentation
comment tree should be returned from a

DocTrees.getDocCommentTree(com.sun.source.util.TreePath)

for a tree under the given file.
The returned position must be at the start of the yield of this tree, that
is for any sub-tree of this tree, the following must hold:

tree.getStartPosition() <= subtree.getStartPosition()

or

tree.getStartPosition() == NOPOS

or

subtree.getStartPosition() == NOPOS

**Parameters:** file

- CompilationUnit in which to find tree.
**Parameters:** comment

- the comment tree that encloses the tree for which the
position is being sought
**Parameters:** tree

- tree for which a position is sought.
**Returns:** the start position of tree.

- getEndPosition

```java
long getEndPosition​(
CompilationUnitTree
file,

DocCommentTree
comment,

DocTree
tree)
```

Returns the ending position of the tree within the comment within the file. If tree is not found within
file, or if the ending position is not available,
return

Diagnostic.NOPOS

.
The given tree should be under the given comment tree, and the given documentation
comment tree should be returned from a

DocTrees.getDocCommentTree(com.sun.source.util.TreePath)

for a tree under the given file.
The returned position must be at the end of the yield of this tree,
that is for any sub-tree of this tree, the following must hold:

tree.getEndPosition() >= subtree.getEndPosition()

or

tree.getEndPosition() == NOPOS

or

subtree.getEndPosition() == NOPOS

In addition, the following must hold:

tree.getStartPosition() <= tree.getEndPosition()

or

tree.getStartPosition() == NOPOS

or

tree.getEndPosition() == NOPOS

**Parameters:** file

- CompilationUnit in which to find tree.
**Parameters:** comment

- the comment tree that encloses the tree for which the
position is being sought
**Parameters:** tree

- tree for which a position is sought.
**Returns:** the start position of tree.

Method Detail

- getStartPosition

```java
long getStartPosition​(
CompilationUnitTree
file,

DocCommentTree
comment,

DocTree
tree)
```

Returns the starting position of the tree within the comment within the file. If tree is not found within
file, or if the starting position is not available,
return

Diagnostic.NOPOS

.
The given tree should be under the given comment tree, and the given documentation
comment tree should be returned from a

DocTrees.getDocCommentTree(com.sun.source.util.TreePath)

for a tree under the given file.
The returned position must be at the start of the yield of this tree, that
is for any sub-tree of this tree, the following must hold:

tree.getStartPosition() <= subtree.getStartPosition()

or

tree.getStartPosition() == NOPOS

or

subtree.getStartPosition() == NOPOS

**Parameters:** file

- CompilationUnit in which to find tree.
**Parameters:** comment

- the comment tree that encloses the tree for which the
position is being sought
**Parameters:** tree

- tree for which a position is sought.
**Returns:** the start position of tree.

- getEndPosition

```java
long getEndPosition​(
CompilationUnitTree
file,

DocCommentTree
comment,

DocTree
tree)
```

Returns the ending position of the tree within the comment within the file. If tree is not found within
file, or if the ending position is not available,
return

Diagnostic.NOPOS

.
The given tree should be under the given comment tree, and the given documentation
comment tree should be returned from a

DocTrees.getDocCommentTree(com.sun.source.util.TreePath)

for a tree under the given file.
The returned position must be at the end of the yield of this tree,
that is for any sub-tree of this tree, the following must hold:

tree.getEndPosition() >= subtree.getEndPosition()

or

tree.getEndPosition() == NOPOS

or

subtree.getEndPosition() == NOPOS

In addition, the following must hold:

tree.getStartPosition() <= tree.getEndPosition()

or

tree.getStartPosition() == NOPOS

or

tree.getEndPosition() == NOPOS

**Parameters:** file

- CompilationUnit in which to find tree.
**Parameters:** comment

- the comment tree that encloses the tree for which the
position is being sought
**Parameters:** tree

- tree for which a position is sought.
**Returns:** the start position of tree.

---

#### Method Detail

getStartPosition

```java
long getStartPosition​(
CompilationUnitTree
file,

DocCommentTree
comment,

DocTree
tree)
```

Returns the starting position of the tree within the comment within the file. If tree is not found within
file, or if the starting position is not available,
return

Diagnostic.NOPOS

.
The given tree should be under the given comment tree, and the given documentation
comment tree should be returned from a

DocTrees.getDocCommentTree(com.sun.source.util.TreePath)

for a tree under the given file.
The returned position must be at the start of the yield of this tree, that
is for any sub-tree of this tree, the following must hold:

tree.getStartPosition() <= subtree.getStartPosition()

or

tree.getStartPosition() == NOPOS

or

subtree.getStartPosition() == NOPOS

**Parameters:** file

- CompilationUnit in which to find tree.
**Parameters:** comment

- the comment tree that encloses the tree for which the
position is being sought
**Parameters:** tree

- tree for which a position is sought.
**Returns:** the start position of tree.

---

#### getStartPosition

long getStartPosition​(

CompilationUnitTree

file,

DocCommentTree

comment,

DocTree

tree)

Returns the starting position of the tree within the comment within the file. If tree is not found within
file, or if the starting position is not available,
return

Diagnostic.NOPOS

.
The given tree should be under the given comment tree, and the given documentation
comment tree should be returned from a

DocTrees.getDocCommentTree(com.sun.source.util.TreePath)

for a tree under the given file.
The returned position must be at the start of the yield of this tree, that
is for any sub-tree of this tree, the following must hold:

tree.getStartPosition() <= subtree.getStartPosition()

or

tree.getStartPosition() == NOPOS

or

subtree.getStartPosition() == NOPOS

tree.getStartPosition() <= subtree.getStartPosition()

or

tree.getStartPosition() == NOPOS

or

subtree.getStartPosition() == NOPOS

getEndPosition

```java
long getEndPosition​(
CompilationUnitTree
file,

DocCommentTree
comment,

DocTree
tree)
```

Returns the ending position of the tree within the comment within the file. If tree is not found within
file, or if the ending position is not available,
return

Diagnostic.NOPOS

.
The given tree should be under the given comment tree, and the given documentation
comment tree should be returned from a

DocTrees.getDocCommentTree(com.sun.source.util.TreePath)

for a tree under the given file.
The returned position must be at the end of the yield of this tree,
that is for any sub-tree of this tree, the following must hold:

tree.getEndPosition() >= subtree.getEndPosition()

or

tree.getEndPosition() == NOPOS

or

subtree.getEndPosition() == NOPOS

In addition, the following must hold:

tree.getStartPosition() <= tree.getEndPosition()

or

tree.getStartPosition() == NOPOS

or

tree.getEndPosition() == NOPOS

**Parameters:** file

- CompilationUnit in which to find tree.
**Parameters:** comment

- the comment tree that encloses the tree for which the
position is being sought
**Parameters:** tree

- tree for which a position is sought.
**Returns:** the start position of tree.

---

#### getEndPosition

long getEndPosition​(

CompilationUnitTree

file,

DocCommentTree

comment,

DocTree

tree)

Returns the ending position of the tree within the comment within the file. If tree is not found within
file, or if the ending position is not available,
return

Diagnostic.NOPOS

.
The given tree should be under the given comment tree, and the given documentation
comment tree should be returned from a

DocTrees.getDocCommentTree(com.sun.source.util.TreePath)

for a tree under the given file.
The returned position must be at the end of the yield of this tree,
that is for any sub-tree of this tree, the following must hold:

tree.getEndPosition() >= subtree.getEndPosition()

or

tree.getEndPosition() == NOPOS

or

subtree.getEndPosition() == NOPOS

In addition, the following must hold:

tree.getStartPosition() <= tree.getEndPosition()

or

tree.getStartPosition() == NOPOS

or

tree.getEndPosition() == NOPOS

tree.getEndPosition() >= subtree.getEndPosition()

or

tree.getEndPosition() == NOPOS

or

subtree.getEndPosition() == NOPOS

tree.getStartPosition() <= tree.getEndPosition()

or

tree.getStartPosition() == NOPOS

or

tree.getEndPosition() == NOPOS

---

