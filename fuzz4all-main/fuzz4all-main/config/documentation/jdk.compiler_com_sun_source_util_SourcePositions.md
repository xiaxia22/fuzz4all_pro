# Interface SourcePositions

**Source:** `jdk.compiler\com\sun\source\util\SourcePositions.html`

### Class Description

```java
public interface
SourcePositions
```

Provides methods to obtain the position of a Tree within a CompilationUnit.
A position is defined as a simple character offset from the start of a
CompilationUnit where the first character is at offset 0.

**All Known Subinterfaces:** DocSourcePositions

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### long getStartPosition​(
CompilationUnitTree
file,

Tree
tree)

Returns the starting position of tree within file. If tree is not found within
file, or if the starting position is not available,
return

Diagnostic.NOPOS

.
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
- tree

- tree for which a position is sought.

**Returns:**
- the start position of tree.

---

#### long getEndPosition​(
CompilationUnitTree
file,

Tree
tree)

Returns the ending position of tree within file. If tree is not found within
file, or if the ending position is not available,
return

Diagnostic.NOPOS

.
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
- tree

- tree for which a position is sought.

**Returns:**
- the end position of tree.

---

### Additional Sections

#### Interface SourcePositions

**All Known Subinterfaces:** DocSourcePositions

```java
public interface
SourcePositions
```

Provides methods to obtain the position of a Tree within a CompilationUnit.
A position is defined as a simple character offset from the start of a
CompilationUnit where the first character is at offset 0.

**Since:** 1.6

public interface

SourcePositions

Provides methods to obtain the position of a Tree within a CompilationUnit.
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

Tree

tree)

Returns the ending position of tree within file.

long

getStartPosition

​(

CompilationUnitTree

file,

Tree

tree)

Returns the starting position of tree within file.

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

Tree

tree)

Returns the ending position of tree within file.

long

getStartPosition

​(

CompilationUnitTree

file,

Tree

tree)

Returns the starting position of tree within file.

---

#### Method Summary

Returns the ending position of tree within file.

Returns the starting position of tree within file.

============ METHOD DETAIL ==========

- Method Detail

- getStartPosition

```java
long getStartPosition​(
CompilationUnitTree
file,

Tree
tree)
```

Returns the starting position of tree within file. If tree is not found within
file, or if the starting position is not available,
return

Diagnostic.NOPOS

.
The returned position must be at the start of the yield of this tree, that
is for any sub-tree of this tree, the following must hold:

tree.getStartPosition() <= subtree.getStartPosition()

or

tree.getStartPosition() == NOPOS

or

subtree.getStartPosition() == NOPOS

**Parameters:** file

- CompilationUnit in which to find tree.
**Parameters:** tree

- tree for which a position is sought.
**Returns:** the start position of tree.

- getEndPosition

```java
long getEndPosition​(
CompilationUnitTree
file,

Tree
tree)
```

Returns the ending position of tree within file. If tree is not found within
file, or if the ending position is not available,
return

Diagnostic.NOPOS

.
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
**Parameters:** tree

- tree for which a position is sought.
**Returns:** the end position of tree.

Method Detail

- getStartPosition

```java
long getStartPosition​(
CompilationUnitTree
file,

Tree
tree)
```

Returns the starting position of tree within file. If tree is not found within
file, or if the starting position is not available,
return

Diagnostic.NOPOS

.
The returned position must be at the start of the yield of this tree, that
is for any sub-tree of this tree, the following must hold:

tree.getStartPosition() <= subtree.getStartPosition()

or

tree.getStartPosition() == NOPOS

or

subtree.getStartPosition() == NOPOS

**Parameters:** file

- CompilationUnit in which to find tree.
**Parameters:** tree

- tree for which a position is sought.
**Returns:** the start position of tree.

- getEndPosition

```java
long getEndPosition​(
CompilationUnitTree
file,

Tree
tree)
```

Returns the ending position of tree within file. If tree is not found within
file, or if the ending position is not available,
return

Diagnostic.NOPOS

.
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
**Parameters:** tree

- tree for which a position is sought.
**Returns:** the end position of tree.

---

#### Method Detail

getStartPosition

```java
long getStartPosition​(
CompilationUnitTree
file,

Tree
tree)
```

Returns the starting position of tree within file. If tree is not found within
file, or if the starting position is not available,
return

Diagnostic.NOPOS

.
The returned position must be at the start of the yield of this tree, that
is for any sub-tree of this tree, the following must hold:

tree.getStartPosition() <= subtree.getStartPosition()

or

tree.getStartPosition() == NOPOS

or

subtree.getStartPosition() == NOPOS

**Parameters:** file

- CompilationUnit in which to find tree.
**Parameters:** tree

- tree for which a position is sought.
**Returns:** the start position of tree.

---

#### getStartPosition

long getStartPosition​(

CompilationUnitTree

file,

Tree

tree)

Returns the starting position of tree within file. If tree is not found within
file, or if the starting position is not available,
return

Diagnostic.NOPOS

.
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

Tree
tree)
```

Returns the ending position of tree within file. If tree is not found within
file, or if the ending position is not available,
return

Diagnostic.NOPOS

.
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
**Parameters:** tree

- tree for which a position is sought.
**Returns:** the end position of tree.

---

#### getEndPosition

long getEndPosition​(

CompilationUnitTree

file,

Tree

tree)

Returns the ending position of tree within file. If tree is not found within
file, or if the ending position is not available,
return

Diagnostic.NOPOS

.
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

