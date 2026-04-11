# Class TreePath

**Source:** `java.desktop\javax\swing\tree\TreePath.html`

### Class Description

```java
public class
TreePath

extends
Object

implements
Serializable
```

TreePath

represents an array of objects that uniquely
identify the path to a node in a tree. The elements of the array
are ordered with the root as the first element of the array. For
example, a file on the file system is uniquely identified based on
the array of parent directories and the name of the file. The path

/tmp/foo/bar

could be represented by a

TreePath

as

new TreePath(new Object[] {"tmp", "foo", "bar"})

.

TreePath

is used extensively by

JTree

and related classes.
For example,

JTree

represents the selection as an array of

TreePath

s. When used with

JTree

, the elements of the
path are the objects returned from the

TreeModel

. When

JTree

is paired with

DefaultTreeModel

, the elements of the
path are

TreeNode

s. The following example illustrates extracting
the user object from the selection of a

JTree

:

```java
DefaultMutableTreeNode root = ...;
DefaultTreeModel model = new DefaultTreeModel(root);
JTree tree = new JTree(model);
...
TreePath selectedPath = tree.getSelectionPath();
DefaultMutableTreeNode selectedNode =
((DefaultMutableTreeNode)selectedPath.getLastPathComponent()).
getUserObject();
```

Subclasses typically need override only

getLastPathComponent

, and

getParentPath

. As

JTree

internally creates

TreePath

s at various points, it's
generally not useful to subclass

TreePath

and use with

JTree

.

While

TreePath

is serializable, a

NotSerializableException

is thrown if any elements of the path are
not serializable.

For further information and examples of using tree paths,
see

How to Use Trees

in

The Java Tutorial.

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

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### @ConstructorProperties
("path")
public TreePath​(
Object
[] path)

Creates a

TreePath

from an array. The array uniquely
identifies the path to a node.

**Parameters:**
- path

- an array of objects representing the path to a node

**Throws:**
- IllegalArgumentException

- if

path

is

null

,
empty, or contains a

null

value

---

#### public TreePath​(
Object
lastPathComponent)

Creates a

TreePath

containing a single element. This is
used to construct a

TreePath

identifying the root.

**Parameters:**
- lastPathComponent

- the root

**Throws:**
- IllegalArgumentException

- if

lastPathComponent

is

null

**See Also:**
- TreePath(Object[])

---

#### protected TreePath​(
TreePath
parent,

Object
lastPathComponent)

Creates a

TreePath

with the specified parent and element.

**Parameters:**
- parent

- the path to the parent, or

null

to indicate
the root
- lastPathComponent

- the last path element

**Throws:**
- IllegalArgumentException

- if

lastPathComponent

is

null

---

#### protected TreePath​(
Object
[] path,
int length)

Creates a

TreePath

from an array. The returned

TreePath

represents the elements of the array from

0

to

length - 1

.

This constructor is used internally, and generally not useful outside
of subclasses.

**Parameters:**
- path

- the array to create the

TreePath

from
- length

- identifies the number of elements in

path

to
create the

TreePath

from

**Throws:**
- NullPointerException

- if

path

is

null
- ArrayIndexOutOfBoundsException

- if

length - 1

is
outside the range of the array
- IllegalArgumentException

- if any of the elements from

0

to

length - 1

are

null

---

#### protected TreePath()

Creates an empty

TreePath

. This is provided for
subclasses that represent paths in a different
manner. Subclasses that use this constructor must override

getLastPathComponent

, and

getParentPath

.

---

### Method Details

#### public
Object
[] getPath()

Returns an ordered array of the elements of this

TreePath

.
The first element is the root.

**Returns:**
- an array of the elements in this

TreePath

---

#### public
Object
getLastPathComponent()

Returns the last element of this path.

**Returns:**
- the last element in the path

---

#### public int getPathCount()

Returns the number of elements in the path.

**Returns:**
- the number of elements in the path

---

#### public
Object
getPathComponent​(int index)

Returns the path element at the specified index.

**Parameters:**
- index

- the index of the element requested

**Returns:**
- the element at the specified index

**Throws:**
- IllegalArgumentException

- if the index is outside the
range of this path

---

#### public boolean equals​(
Object
o)

Compares this

TreePath

to the specified object. This returns

true

if

o

is a

TreePath

with the exact
same elements (as determined by using

equals

on each
element of the path).

**Overrides:**
- equals

in class

Object

**Parameters:**
- o

- the object to compare

**Returns:**
- true

if this object is the same as the obj
argument;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Returns the hash code of this

TreePath

. The hash code of a

TreePath

is the hash code of the last element in the path.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- the hashCode for the object

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean isDescendant​(
TreePath
aTreePath)

Returns true if

aTreePath

is a
descendant of this

TreePath

. A

TreePath

P1

is a descendant of a

TreePath

P2

if

P1

contains all of the elements that make up

P2's

path.
For example, if this object has the path

[a, b]

,
and

aTreePath

has the path

[a, b, c]

,
then

aTreePath

is a descendant of this object.
However, if

aTreePath

has the path

[a]

,
then it is not a descendant of this object. By this definition
a

TreePath

is always considered a descendant of itself.
That is,

aTreePath.isDescendant(aTreePath)

returns

true

.

**Parameters:**
- aTreePath

- the

TreePath

to check

**Returns:**
- true if

aTreePath

is a descendant of this path

---

#### public
TreePath
pathByAddingChild​(
Object
child)

Returns a new path containing all the elements of this path
plus

child

.

child

is the last element
of the newly created

TreePath

.

**Parameters:**
- child

- the path element to add

**Returns:**
- a new path containing all the elements of this path
plus

child

**Throws:**
- NullPointerException

- if

child

is

null

---

#### public
TreePath
getParentPath()

Returns the

TreePath

of the parent. A return value of

null

indicates this is the root node.

**Returns:**
- the parent path

---

#### public
String
toString()

Returns a string that displays and identifies this
object's properties.

**Overrides:**
- toString

in class

Object

**Returns:**
- a String representation of this object

---

### Additional Sections

#### Class TreePath

java.lang.Object

- javax.swing.tree.TreePath

javax.swing.tree.TreePath

**All Implemented Interfaces:** Serializable

```java
public class
TreePath

extends
Object

implements
Serializable
```

TreePath

represents an array of objects that uniquely
identify the path to a node in a tree. The elements of the array
are ordered with the root as the first element of the array. For
example, a file on the file system is uniquely identified based on
the array of parent directories and the name of the file. The path

/tmp/foo/bar

could be represented by a

TreePath

as

new TreePath(new Object[] {"tmp", "foo", "bar"})

.

TreePath

is used extensively by

JTree

and related classes.
For example,

JTree

represents the selection as an array of

TreePath

s. When used with

JTree

, the elements of the
path are the objects returned from the

TreeModel

. When

JTree

is paired with

DefaultTreeModel

, the elements of the
path are

TreeNode

s. The following example illustrates extracting
the user object from the selection of a

JTree

:

```java
DefaultMutableTreeNode root = ...;
DefaultTreeModel model = new DefaultTreeModel(root);
JTree tree = new JTree(model);
...
TreePath selectedPath = tree.getSelectionPath();
DefaultMutableTreeNode selectedNode =
((DefaultMutableTreeNode)selectedPath.getLastPathComponent()).
getUserObject();
```

Subclasses typically need override only

getLastPathComponent

, and

getParentPath

. As

JTree

internally creates

TreePath

s at various points, it's
generally not useful to subclass

TreePath

and use with

JTree

.

While

TreePath

is serializable, a

NotSerializableException

is thrown if any elements of the path are
not serializable.

For further information and examples of using tree paths,
see

How to Use Trees

in

The Java Tutorial.

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

**See Also:** Serialized Form

public class

TreePath

extends

Object

implements

Serializable

TreePath

represents an array of objects that uniquely
identify the path to a node in a tree. The elements of the array
are ordered with the root as the first element of the array. For
example, a file on the file system is uniquely identified based on
the array of parent directories and the name of the file. The path

/tmp/foo/bar

could be represented by a

TreePath

as

new TreePath(new Object[] {"tmp", "foo", "bar"})

.

TreePath

is used extensively by

JTree

and related classes.
For example,

JTree

represents the selection as an array of

TreePath

s. When used with

JTree

, the elements of the
path are the objects returned from the

TreeModel

. When

JTree

is paired with

DefaultTreeModel

, the elements of the
path are

TreeNode

s. The following example illustrates extracting
the user object from the selection of a

JTree

:

```java
DefaultMutableTreeNode root = ...;
DefaultTreeModel model = new DefaultTreeModel(root);
JTree tree = new JTree(model);
...
TreePath selectedPath = tree.getSelectionPath();
DefaultMutableTreeNode selectedNode =
((DefaultMutableTreeNode)selectedPath.getLastPathComponent()).
getUserObject();
```

Subclasses typically need override only

getLastPathComponent

, and

getParentPath

. As

JTree

internally creates

TreePath

s at various points, it's
generally not useful to subclass

TreePath

and use with

JTree

.

While

TreePath

is serializable, a

NotSerializableException

is thrown if any elements of the path are
not serializable.

For further information and examples of using tree paths,
see

How to Use Trees

in

The Java Tutorial.

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

TreePath

is used extensively by

JTree

and related classes.
For example,

JTree

represents the selection as an array of

TreePath

s. When used with

JTree

, the elements of the
path are the objects returned from the

TreeModel

. When

JTree

is paired with

DefaultTreeModel

, the elements of the
path are

TreeNode

s. The following example illustrates extracting
the user object from the selection of a

JTree

:

```java
DefaultMutableTreeNode root = ...;
DefaultTreeModel model = new DefaultTreeModel(root);
JTree tree = new JTree(model);
...
TreePath selectedPath = tree.getSelectionPath();
DefaultMutableTreeNode selectedNode =
((DefaultMutableTreeNode)selectedPath.getLastPathComponent()).
getUserObject();
```

Subclasses typically need override only

getLastPathComponent

, and

getParentPath

. As

JTree

internally creates

TreePath

s at various points, it's
generally not useful to subclass

TreePath

and use with

JTree

.

While

TreePath

is serializable, a

NotSerializableException

is thrown if any elements of the path are
not serializable.

For further information and examples of using tree paths,
see

How to Use Trees

in

The Java Tutorial.

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

DefaultMutableTreeNode root = ...;
DefaultTreeModel model = new DefaultTreeModel(root);
JTree tree = new JTree(model);
...
TreePath selectedPath = tree.getSelectionPath();
DefaultMutableTreeNode selectedNode =
((DefaultMutableTreeNode)selectedPath.getLastPathComponent()).
getUserObject();

While

TreePath

is serializable, a

NotSerializableException

is thrown if any elements of the path are
not serializable.

For further information and examples of using tree paths,
see

How to Use Trees

in

The Java Tutorial.

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

For further information and examples of using tree paths,
see

How to Use Trees

in

The Java Tutorial.

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

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

TreePath

()

Creates an empty

TreePath

.

TreePath

​(

Object

lastPathComponent)

Creates a

TreePath

containing a single element.

TreePath

​(

Object

[] path)

Creates a

TreePath

from an array.

protected

TreePath

​(

Object

[] path,
int length)

Creates a

TreePath

from an array.

protected

TreePath

​(

TreePath

parent,

Object

lastPathComponent)

Creates a

TreePath

with the specified parent and element.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

o)

Compares this

TreePath

to the specified object.

Object

getLastPathComponent

()

Returns the last element of this path.

TreePath

getParentPath

()

Returns the

TreePath

of the parent.

Object

[]

getPath

()

Returns an ordered array of the elements of this

TreePath

.

Object

getPathComponent

​(int index)

Returns the path element at the specified index.

int

getPathCount

()

Returns the number of elements in the path.

int

hashCode

()

Returns the hash code of this

TreePath

.

boolean

isDescendant

​(

TreePath

aTreePath)

Returns true if

aTreePath

is a
descendant of this

TreePath

.

TreePath

pathByAddingChild

​(

Object

child)

Returns a new path containing all the elements of this path
plus

child

.

String

toString

()

Returns a string that displays and identifies this
object's properties.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

TreePath

()

Creates an empty

TreePath

.

TreePath

​(

Object

lastPathComponent)

Creates a

TreePath

containing a single element.

TreePath

​(

Object

[] path)

Creates a

TreePath

from an array.

protected

TreePath

​(

Object

[] path,
int length)

Creates a

TreePath

from an array.

protected

TreePath

​(

TreePath

parent,

Object

lastPathComponent)

Creates a

TreePath

with the specified parent and element.

---

#### Constructor Summary

Creates an empty

TreePath

.

Creates a

TreePath

containing a single element.

Creates a

TreePath

from an array.

Creates a

TreePath

with the specified parent and element.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

o)

Compares this

TreePath

to the specified object.

Object

getLastPathComponent

()

Returns the last element of this path.

TreePath

getParentPath

()

Returns the

TreePath

of the parent.

Object

[]

getPath

()

Returns an ordered array of the elements of this

TreePath

.

Object

getPathComponent

​(int index)

Returns the path element at the specified index.

int

getPathCount

()

Returns the number of elements in the path.

int

hashCode

()

Returns the hash code of this

TreePath

.

boolean

isDescendant

​(

TreePath

aTreePath)

Returns true if

aTreePath

is a
descendant of this

TreePath

.

TreePath

pathByAddingChild

​(

Object

child)

Returns a new path containing all the elements of this path
plus

child

.

String

toString

()

Returns a string that displays and identifies this
object's properties.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Compares this

TreePath

to the specified object.

Returns the last element of this path.

Returns the

TreePath

of the parent.

Returns an ordered array of the elements of this

TreePath

.

Returns the path element at the specified index.

Returns the number of elements in the path.

Returns the hash code of this

TreePath

.

Returns true if

aTreePath

is a
descendant of this

TreePath

.

Returns a new path containing all the elements of this path
plus

child

.

Returns a string that displays and identifies this
object's properties.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

,

notify

,

notifyAll

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

- TreePath

```java
@ConstructorProperties
("path")
public TreePath​(
Object
[] path)
```

Creates a

TreePath

from an array. The array uniquely
identifies the path to a node.

**Parameters:** path

- an array of objects representing the path to a node
**Throws:** IllegalArgumentException

- if

path

is

null

,
empty, or contains a

null

value

- TreePath

```java
public TreePath​(
Object
lastPathComponent)
```

Creates a

TreePath

containing a single element. This is
used to construct a

TreePath

identifying the root.

**Parameters:** lastPathComponent

- the root
**Throws:** IllegalArgumentException

- if

lastPathComponent

is

null
**See Also:** TreePath(Object[])

- TreePath

```java
protected TreePath​(
TreePath
parent,

Object
lastPathComponent)
```

Creates a

TreePath

with the specified parent and element.

**Parameters:** parent

- the path to the parent, or

null

to indicate
the root
**Parameters:** lastPathComponent

- the last path element
**Throws:** IllegalArgumentException

- if

lastPathComponent

is

null

- TreePath

```java
protected TreePath​(
Object
[] path,
int length)
```

Creates a

TreePath

from an array. The returned

TreePath

represents the elements of the array from

0

to

length - 1

.

This constructor is used internally, and generally not useful outside
of subclasses.

**Parameters:** path

- the array to create the

TreePath

from
**Parameters:** length

- identifies the number of elements in

path

to
create the

TreePath

from
**Throws:** NullPointerException

- if

path

is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

length - 1

is
outside the range of the array
**Throws:** IllegalArgumentException

- if any of the elements from

0

to

length - 1

are

null

- TreePath

```java
protected TreePath()
```

Creates an empty

TreePath

. This is provided for
subclasses that represent paths in a different
manner. Subclasses that use this constructor must override

getLastPathComponent

, and

getParentPath

.

============ METHOD DETAIL ==========

- Method Detail

- getPath

```java
public
Object
[] getPath()
```

Returns an ordered array of the elements of this

TreePath

.
The first element is the root.

**Returns:** an array of the elements in this

TreePath

- getLastPathComponent

```java
public
Object
getLastPathComponent()
```

Returns the last element of this path.

**Returns:** the last element in the path

- getPathCount

```java
public int getPathCount()
```

Returns the number of elements in the path.

**Returns:** the number of elements in the path

- getPathComponent

```java
public
Object
getPathComponent​(int index)
```

Returns the path element at the specified index.

**Parameters:** index

- the index of the element requested
**Returns:** the element at the specified index
**Throws:** IllegalArgumentException

- if the index is outside the
range of this path

- equals

```java
public boolean equals​(
Object
o)
```

Compares this

TreePath

to the specified object. This returns

true

if

o

is a

TreePath

with the exact
same elements (as determined by using

equals

on each
element of the path).

**Overrides:** equals

in class

Object
**Parameters:** o

- the object to compare
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code of this

TreePath

. The hash code of a

TreePath

is the hash code of the last element in the path.

**Overrides:** hashCode

in class

Object
**Returns:** the hashCode for the object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- isDescendant

```java
public boolean isDescendant​(
TreePath
aTreePath)
```

Returns true if

aTreePath

is a
descendant of this

TreePath

. A

TreePath

P1

is a descendant of a

TreePath

P2

if

P1

contains all of the elements that make up

P2's

path.
For example, if this object has the path

[a, b]

,
and

aTreePath

has the path

[a, b, c]

,
then

aTreePath

is a descendant of this object.
However, if

aTreePath

has the path

[a]

,
then it is not a descendant of this object. By this definition
a

TreePath

is always considered a descendant of itself.
That is,

aTreePath.isDescendant(aTreePath)

returns

true

.

**Parameters:** aTreePath

- the

TreePath

to check
**Returns:** true if

aTreePath

is a descendant of this path

- pathByAddingChild

```java
public
TreePath
pathByAddingChild​(
Object
child)
```

Returns a new path containing all the elements of this path
plus

child

.

child

is the last element
of the newly created

TreePath

.

**Parameters:** child

- the path element to add
**Returns:** a new path containing all the elements of this path
plus

child
**Throws:** NullPointerException

- if

child

is

null

- getParentPath

```java
public
TreePath
getParentPath()
```

Returns the

TreePath

of the parent. A return value of

null

indicates this is the root node.

**Returns:** the parent path

- toString

```java
public
String
toString()
```

Returns a string that displays and identifies this
object's properties.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this object

Constructor Detail

- TreePath

```java
@ConstructorProperties
("path")
public TreePath​(
Object
[] path)
```

Creates a

TreePath

from an array. The array uniquely
identifies the path to a node.

**Parameters:** path

- an array of objects representing the path to a node
**Throws:** IllegalArgumentException

- if

path

is

null

,
empty, or contains a

null

value

- TreePath

```java
public TreePath​(
Object
lastPathComponent)
```

Creates a

TreePath

containing a single element. This is
used to construct a

TreePath

identifying the root.

**Parameters:** lastPathComponent

- the root
**Throws:** IllegalArgumentException

- if

lastPathComponent

is

null
**See Also:** TreePath(Object[])

- TreePath

```java
protected TreePath​(
TreePath
parent,

Object
lastPathComponent)
```

Creates a

TreePath

with the specified parent and element.

**Parameters:** parent

- the path to the parent, or

null

to indicate
the root
**Parameters:** lastPathComponent

- the last path element
**Throws:** IllegalArgumentException

- if

lastPathComponent

is

null

- TreePath

```java
protected TreePath​(
Object
[] path,
int length)
```

Creates a

TreePath

from an array. The returned

TreePath

represents the elements of the array from

0

to

length - 1

.

This constructor is used internally, and generally not useful outside
of subclasses.

**Parameters:** path

- the array to create the

TreePath

from
**Parameters:** length

- identifies the number of elements in

path

to
create the

TreePath

from
**Throws:** NullPointerException

- if

path

is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

length - 1

is
outside the range of the array
**Throws:** IllegalArgumentException

- if any of the elements from

0

to

length - 1

are

null

- TreePath

```java
protected TreePath()
```

Creates an empty

TreePath

. This is provided for
subclasses that represent paths in a different
manner. Subclasses that use this constructor must override

getLastPathComponent

, and

getParentPath

.

---

#### Constructor Detail

TreePath

```java
@ConstructorProperties
("path")
public TreePath​(
Object
[] path)
```

Creates a

TreePath

from an array. The array uniquely
identifies the path to a node.

**Parameters:** path

- an array of objects representing the path to a node
**Throws:** IllegalArgumentException

- if

path

is

null

,
empty, or contains a

null

value

---

#### TreePath

@ConstructorProperties

("path")
public TreePath​(

Object

[] path)

Creates a

TreePath

from an array. The array uniquely
identifies the path to a node.

TreePath

```java
public TreePath​(
Object
lastPathComponent)
```

Creates a

TreePath

containing a single element. This is
used to construct a

TreePath

identifying the root.

**Parameters:** lastPathComponent

- the root
**Throws:** IllegalArgumentException

- if

lastPathComponent

is

null
**See Also:** TreePath(Object[])

---

#### TreePath

public TreePath​(

Object

lastPathComponent)

Creates a

TreePath

containing a single element. This is
used to construct a

TreePath

identifying the root.

TreePath

```java
protected TreePath​(
TreePath
parent,

Object
lastPathComponent)
```

Creates a

TreePath

with the specified parent and element.

**Parameters:** parent

- the path to the parent, or

null

to indicate
the root
**Parameters:** lastPathComponent

- the last path element
**Throws:** IllegalArgumentException

- if

lastPathComponent

is

null

---

#### TreePath

protected TreePath​(

TreePath

parent,

Object

lastPathComponent)

Creates a

TreePath

with the specified parent and element.

TreePath

```java
protected TreePath​(
Object
[] path,
int length)
```

Creates a

TreePath

from an array. The returned

TreePath

represents the elements of the array from

0

to

length - 1

.

This constructor is used internally, and generally not useful outside
of subclasses.

**Parameters:** path

- the array to create the

TreePath

from
**Parameters:** length

- identifies the number of elements in

path

to
create the

TreePath

from
**Throws:** NullPointerException

- if

path

is

null
**Throws:** ArrayIndexOutOfBoundsException

- if

length - 1

is
outside the range of the array
**Throws:** IllegalArgumentException

- if any of the elements from

0

to

length - 1

are

null

---

#### TreePath

protected TreePath​(

Object

[] path,
int length)

Creates a

TreePath

from an array. The returned

TreePath

represents the elements of the array from

0

to

length - 1

.

This constructor is used internally, and generally not useful outside
of subclasses.

This constructor is used internally, and generally not useful outside
of subclasses.

TreePath

```java
protected TreePath()
```

Creates an empty

TreePath

. This is provided for
subclasses that represent paths in a different
manner. Subclasses that use this constructor must override

getLastPathComponent

, and

getParentPath

.

---

#### TreePath

protected TreePath()

Creates an empty

TreePath

. This is provided for
subclasses that represent paths in a different
manner. Subclasses that use this constructor must override

getLastPathComponent

, and

getParentPath

.

Method Detail

- getPath

```java
public
Object
[] getPath()
```

Returns an ordered array of the elements of this

TreePath

.
The first element is the root.

**Returns:** an array of the elements in this

TreePath

- getLastPathComponent

```java
public
Object
getLastPathComponent()
```

Returns the last element of this path.

**Returns:** the last element in the path

- getPathCount

```java
public int getPathCount()
```

Returns the number of elements in the path.

**Returns:** the number of elements in the path

- getPathComponent

```java
public
Object
getPathComponent​(int index)
```

Returns the path element at the specified index.

**Parameters:** index

- the index of the element requested
**Returns:** the element at the specified index
**Throws:** IllegalArgumentException

- if the index is outside the
range of this path

- equals

```java
public boolean equals​(
Object
o)
```

Compares this

TreePath

to the specified object. This returns

true

if

o

is a

TreePath

with the exact
same elements (as determined by using

equals

on each
element of the path).

**Overrides:** equals

in class

Object
**Parameters:** o

- the object to compare
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Returns the hash code of this

TreePath

. The hash code of a

TreePath

is the hash code of the last element in the path.

**Overrides:** hashCode

in class

Object
**Returns:** the hashCode for the object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- isDescendant

```java
public boolean isDescendant​(
TreePath
aTreePath)
```

Returns true if

aTreePath

is a
descendant of this

TreePath

. A

TreePath

P1

is a descendant of a

TreePath

P2

if

P1

contains all of the elements that make up

P2's

path.
For example, if this object has the path

[a, b]

,
and

aTreePath

has the path

[a, b, c]

,
then

aTreePath

is a descendant of this object.
However, if

aTreePath

has the path

[a]

,
then it is not a descendant of this object. By this definition
a

TreePath

is always considered a descendant of itself.
That is,

aTreePath.isDescendant(aTreePath)

returns

true

.

**Parameters:** aTreePath

- the

TreePath

to check
**Returns:** true if

aTreePath

is a descendant of this path

- pathByAddingChild

```java
public
TreePath
pathByAddingChild​(
Object
child)
```

Returns a new path containing all the elements of this path
plus

child

.

child

is the last element
of the newly created

TreePath

.

**Parameters:** child

- the path element to add
**Returns:** a new path containing all the elements of this path
plus

child
**Throws:** NullPointerException

- if

child

is

null

- getParentPath

```java
public
TreePath
getParentPath()
```

Returns the

TreePath

of the parent. A return value of

null

indicates this is the root node.

**Returns:** the parent path

- toString

```java
public
String
toString()
```

Returns a string that displays and identifies this
object's properties.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this object

---

#### Method Detail

getPath

```java
public
Object
[] getPath()
```

Returns an ordered array of the elements of this

TreePath

.
The first element is the root.

**Returns:** an array of the elements in this

TreePath

---

#### getPath

public

Object

[] getPath()

Returns an ordered array of the elements of this

TreePath

.
The first element is the root.

getLastPathComponent

```java
public
Object
getLastPathComponent()
```

Returns the last element of this path.

**Returns:** the last element in the path

---

#### getLastPathComponent

public

Object

getLastPathComponent()

Returns the last element of this path.

getPathCount

```java
public int getPathCount()
```

Returns the number of elements in the path.

**Returns:** the number of elements in the path

---

#### getPathCount

public int getPathCount()

Returns the number of elements in the path.

getPathComponent

```java
public
Object
getPathComponent​(int index)
```

Returns the path element at the specified index.

**Parameters:** index

- the index of the element requested
**Returns:** the element at the specified index
**Throws:** IllegalArgumentException

- if the index is outside the
range of this path

---

#### getPathComponent

public

Object

getPathComponent​(int index)

Returns the path element at the specified index.

equals

```java
public boolean equals​(
Object
o)
```

Compares this

TreePath

to the specified object. This returns

true

if

o

is a

TreePath

with the exact
same elements (as determined by using

equals

on each
element of the path).

**Overrides:** equals

in class

Object
**Parameters:** o

- the object to compare
**Returns:** true

if this object is the same as the obj
argument;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

o)

Compares this

TreePath

to the specified object. This returns

true

if

o

is a

TreePath

with the exact
same elements (as determined by using

equals

on each
element of the path).

hashCode

```java
public int hashCode()
```

Returns the hash code of this

TreePath

. The hash code of a

TreePath

is the hash code of the last element in the path.

**Overrides:** hashCode

in class

Object
**Returns:** the hashCode for the object
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns the hash code of this

TreePath

. The hash code of a

TreePath

is the hash code of the last element in the path.

isDescendant

```java
public boolean isDescendant​(
TreePath
aTreePath)
```

Returns true if

aTreePath

is a
descendant of this

TreePath

. A

TreePath

P1

is a descendant of a

TreePath

P2

if

P1

contains all of the elements that make up

P2's

path.
For example, if this object has the path

[a, b]

,
and

aTreePath

has the path

[a, b, c]

,
then

aTreePath

is a descendant of this object.
However, if

aTreePath

has the path

[a]

,
then it is not a descendant of this object. By this definition
a

TreePath

is always considered a descendant of itself.
That is,

aTreePath.isDescendant(aTreePath)

returns

true

.

**Parameters:** aTreePath

- the

TreePath

to check
**Returns:** true if

aTreePath

is a descendant of this path

---

#### isDescendant

public boolean isDescendant​(

TreePath

aTreePath)

Returns true if

aTreePath

is a
descendant of this

TreePath

. A

TreePath

P1

is a descendant of a

TreePath

P2

if

P1

contains all of the elements that make up

P2's

path.
For example, if this object has the path

[a, b]

,
and

aTreePath

has the path

[a, b, c]

,
then

aTreePath

is a descendant of this object.
However, if

aTreePath

has the path

[a]

,
then it is not a descendant of this object. By this definition
a

TreePath

is always considered a descendant of itself.
That is,

aTreePath.isDescendant(aTreePath)

returns

true

.

pathByAddingChild

```java
public
TreePath
pathByAddingChild​(
Object
child)
```

Returns a new path containing all the elements of this path
plus

child

.

child

is the last element
of the newly created

TreePath

.

**Parameters:** child

- the path element to add
**Returns:** a new path containing all the elements of this path
plus

child
**Throws:** NullPointerException

- if

child

is

null

---

#### pathByAddingChild

public

TreePath

pathByAddingChild​(

Object

child)

Returns a new path containing all the elements of this path
plus

child

.

child

is the last element
of the newly created

TreePath

.

getParentPath

```java
public
TreePath
getParentPath()
```

Returns the

TreePath

of the parent. A return value of

null

indicates this is the root node.

**Returns:** the parent path

---

#### getParentPath

public

TreePath

getParentPath()

Returns the

TreePath

of the parent. A return value of

null

indicates this is the root node.

toString

```java
public
String
toString()
```

Returns a string that displays and identifies this
object's properties.

**Overrides:** toString

in class

Object
**Returns:** a String representation of this object

---

#### toString

public

String

toString()

Returns a string that displays and identifies this
object's properties.

---

