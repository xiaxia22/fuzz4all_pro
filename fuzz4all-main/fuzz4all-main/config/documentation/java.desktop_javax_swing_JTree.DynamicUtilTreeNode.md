# Class JTree.DynamicUtilTreeNode

**Source:** `java.desktop\javax\swing\JTree.DynamicUtilTreeNode.html`

### Class Description

```java
public static class
JTree.DynamicUtilTreeNode

extends
DefaultMutableTreeNode
```

DynamicUtilTreeNode

can wrap
vectors/hashtables/arrays/strings and
create the appropriate children tree nodes as necessary. It is
dynamic in that it will only create the children as necessary.

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

,

Cloneable

,

MutableTreeNode

,

TreeNode

---

### Field Details

#### protected boolean hasChildren

Does the this

JTree

have children?
This property is currently not implemented.

---

#### protected
Object
childValue

Value to create children with.

---

#### protected boolean loadedChildren

Have the children been loaded yet?

---

### Constructor Details

#### public DynamicUtilTreeNode​(
Object
value,

Object
children)

Creates a node with the specified object as its value and
with the specified children. For the node to allow children,
the children-object must be an array of objects, a

Vector

, or a

Hashtable

-- even
if empty. Otherwise, the node is not
allowed to have children.

**Parameters:**
- value

- the

Object

that is the value for the
new node
- children

- an array of

Object

s, a

Vector

, or a

Hashtable

used to create the child nodes; if any other
object is specified, or if the value is

null

,
then the node is not allowed to have children

---

### Method Details

#### public static void createChildren​(
DefaultMutableTreeNode
parent,

Object
children)

Adds to parent all the children in

children

.
If

children

is an array or vector all of its
elements are added is children, otherwise if

children

is a hashtable all the key/value pairs are added in the order

Enumeration

returns them.

**Parameters:**
- parent

- the parent node
- children

- the children

---

#### public boolean isLeaf()

Returns true if this node allows children. Whether the node
allows children depends on how it was created.

**Specified by:**
- isLeaf

in interface

TreeNode

**Overrides:**
- isLeaf

in class

DefaultMutableTreeNode

**Returns:**
- true if this node allows children, false otherwise

**See Also:**
- JTree.DynamicUtilTreeNode

---

#### public int getChildCount()

Returns the number of child nodes.

**Specified by:**
- getChildCount

in interface

TreeNode

**Overrides:**
- getChildCount

in class

DefaultMutableTreeNode

**Returns:**
- the number of child nodes

---

#### protected void loadChildren()

Loads the children based on

childValue

.
If

childValue

is a

Vector

or array each element is added as a child,
if

childValue

is a

Hashtable

each key/value pair is added in the order that

Enumeration

returns the keys.

---

#### public
TreeNode
getChildAt​(int index)

Subclassed to load the children, if necessary.

**Specified by:**
- getChildAt

in interface

TreeNode

**Overrides:**
- getChildAt

in class

DefaultMutableTreeNode

**Parameters:**
- index

- an index into this node's child array

**Returns:**
- the TreeNode in this node's child array at the specified index

---

#### public
Enumeration
<
TreeNode
> children()

Subclassed to load the children, if necessary.

**Specified by:**
- children

in interface

TreeNode

**Overrides:**
- children

in class

DefaultMutableTreeNode

**Returns:**
- an Enumeration of this node's children

---

### Additional Sections

#### Class JTree.DynamicUtilTreeNode

java.lang.Object

- javax.swing.tree.DefaultMutableTreeNode
- - javax.swing.JTree.DynamicUtilTreeNode

javax.swing.tree.DefaultMutableTreeNode

- javax.swing.JTree.DynamicUtilTreeNode

javax.swing.JTree.DynamicUtilTreeNode

**All Implemented Interfaces:** Serializable

,

Cloneable

,

MutableTreeNode

,

TreeNode

**Enclosing class:** JTree

```java
public static class
JTree.DynamicUtilTreeNode

extends
DefaultMutableTreeNode
```

DynamicUtilTreeNode

can wrap
vectors/hashtables/arrays/strings and
create the appropriate children tree nodes as necessary. It is
dynamic in that it will only create the children as necessary.

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

public static class

JTree.DynamicUtilTreeNode

extends

DefaultMutableTreeNode

DynamicUtilTreeNode

can wrap
vectors/hashtables/arrays/strings and
create the appropriate children tree nodes as necessary. It is
dynamic in that it will only create the children as necessary.

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

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

Object

childValue

Value to create children with.

protected boolean

hasChildren

Does the this

JTree

have children?

protected boolean

loadedChildren

Have the children been loaded yet?

- Fields declared in class javax.swing.tree.

DefaultMutableTreeNode

allowsChildren

,

children

,

EMPTY_ENUMERATION

,

parent

,

userObject

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DynamicUtilTreeNode

​(

Object

value,

Object

children)

Creates a node with the specified object as its value and
with the specified children.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Enumeration

<

TreeNode

>

children

()

Subclassed to load the children, if necessary.

static void

createChildren

​(

DefaultMutableTreeNode

parent,

Object

children)

Adds to parent all the children in

children

.

TreeNode

getChildAt

​(int index)

Subclassed to load the children, if necessary.

int

getChildCount

()

Returns the number of child nodes.

boolean

isLeaf

()

Returns true if this node allows children.

protected void

loadChildren

()

Loads the children based on

childValue

.

- Methods declared in class javax.swing.tree.

DefaultMutableTreeNode

add

,

breadthFirstEnumeration

,

clone

,

depthFirstEnumeration

,

getAllowsChildren

,

getChildAfter

,

getChildBefore

,

getDepth

,

getFirstChild

,

getFirstLeaf

,

getIndex

,

getLastChild

,

getLastLeaf

,

getLeafCount

,

getLevel

,

getNextLeaf

,

getNextNode

,

getNextSibling

,

getParent

,

getPath

,

getPathToRoot

,

getPreviousLeaf

,

getPreviousNode

,

getPreviousSibling

,

getRoot

,

getSharedAncestor

,

getSiblingCount

,

getUserObject

,

getUserObjectPath

,

insert

,

isNodeAncestor

,

isNodeChild

,

isNodeDescendant

,

isNodeRelated

,

isNodeSibling

,

isRoot

,

pathFromAncestorEnumeration

,

postorderEnumeration

,

preorderEnumeration

,

remove

,

remove

,

removeAllChildren

,

removeFromParent

,

setAllowsChildren

,

setParent

,

setUserObject

,

toString

- Methods declared in class java.lang.

Object

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

wait

,

wait

,

wait

Field Summary

Fields

Modifier and Type

Field

Description

protected

Object

childValue

Value to create children with.

protected boolean

hasChildren

Does the this

JTree

have children?

protected boolean

loadedChildren

Have the children been loaded yet?

- Fields declared in class javax.swing.tree.

DefaultMutableTreeNode

allowsChildren

,

children

,

EMPTY_ENUMERATION

,

parent

,

userObject

---

#### Field Summary

Value to create children with.

Does the this

JTree

have children?

Have the children been loaded yet?

Fields declared in class javax.swing.tree.

DefaultMutableTreeNode

allowsChildren

,

children

,

EMPTY_ENUMERATION

,

parent

,

userObject

---

#### Fields declared in class javax.swing.tree. DefaultMutableTreeNode

Constructor Summary

Constructors

Constructor

Description

DynamicUtilTreeNode

​(

Object

value,

Object

children)

Creates a node with the specified object as its value and
with the specified children.

---

#### Constructor Summary

Creates a node with the specified object as its value and
with the specified children.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Enumeration

<

TreeNode

>

children

()

Subclassed to load the children, if necessary.

static void

createChildren

​(

DefaultMutableTreeNode

parent,

Object

children)

Adds to parent all the children in

children

.

TreeNode

getChildAt

​(int index)

Subclassed to load the children, if necessary.

int

getChildCount

()

Returns the number of child nodes.

boolean

isLeaf

()

Returns true if this node allows children.

protected void

loadChildren

()

Loads the children based on

childValue

.

- Methods declared in class javax.swing.tree.

DefaultMutableTreeNode

add

,

breadthFirstEnumeration

,

clone

,

depthFirstEnumeration

,

getAllowsChildren

,

getChildAfter

,

getChildBefore

,

getDepth

,

getFirstChild

,

getFirstLeaf

,

getIndex

,

getLastChild

,

getLastLeaf

,

getLeafCount

,

getLevel

,

getNextLeaf

,

getNextNode

,

getNextSibling

,

getParent

,

getPath

,

getPathToRoot

,

getPreviousLeaf

,

getPreviousNode

,

getPreviousSibling

,

getRoot

,

getSharedAncestor

,

getSiblingCount

,

getUserObject

,

getUserObjectPath

,

insert

,

isNodeAncestor

,

isNodeChild

,

isNodeDescendant

,

isNodeRelated

,

isNodeSibling

,

isRoot

,

pathFromAncestorEnumeration

,

postorderEnumeration

,

preorderEnumeration

,

remove

,

remove

,

removeAllChildren

,

removeFromParent

,

setAllowsChildren

,

setParent

,

setUserObject

,

toString

- Methods declared in class java.lang.

Object

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

wait

,

wait

,

wait

---

#### Method Summary

Subclassed to load the children, if necessary.

Adds to parent all the children in

children

.

Returns the number of child nodes.

Returns true if this node allows children.

Loads the children based on

childValue

.

Methods declared in class javax.swing.tree.

DefaultMutableTreeNode

add

,

breadthFirstEnumeration

,

clone

,

depthFirstEnumeration

,

getAllowsChildren

,

getChildAfter

,

getChildBefore

,

getDepth

,

getFirstChild

,

getFirstLeaf

,

getIndex

,

getLastChild

,

getLastLeaf

,

getLeafCount

,

getLevel

,

getNextLeaf

,

getNextNode

,

getNextSibling

,

getParent

,

getPath

,

getPathToRoot

,

getPreviousLeaf

,

getPreviousNode

,

getPreviousSibling

,

getRoot

,

getSharedAncestor

,

getSiblingCount

,

getUserObject

,

getUserObjectPath

,

insert

,

isNodeAncestor

,

isNodeChild

,

isNodeDescendant

,

isNodeRelated

,

isNodeSibling

,

isRoot

,

pathFromAncestorEnumeration

,

postorderEnumeration

,

preorderEnumeration

,

remove

,

remove

,

removeAllChildren

,

removeFromParent

,

setAllowsChildren

,

setParent

,

setUserObject

,

toString

---

#### Methods declared in class javax.swing.tree. DefaultMutableTreeNode

Methods declared in class java.lang.

Object

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- hasChildren

```java
protected boolean hasChildren
```

Does the this

JTree

have children?
This property is currently not implemented.

- childValue

```java
protected
Object
childValue
```

Value to create children with.

- loadedChildren

```java
protected boolean loadedChildren
```

Have the children been loaded yet?

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- DynamicUtilTreeNode

```java
public DynamicUtilTreeNode​(
Object
value,

Object
children)
```

Creates a node with the specified object as its value and
with the specified children. For the node to allow children,
the children-object must be an array of objects, a

Vector

, or a

Hashtable

-- even
if empty. Otherwise, the node is not
allowed to have children.

**Parameters:** value

- the

Object

that is the value for the
new node
**Parameters:** children

- an array of

Object

s, a

Vector

, or a

Hashtable

used to create the child nodes; if any other
object is specified, or if the value is

null

,
then the node is not allowed to have children

============ METHOD DETAIL ==========

- Method Detail

- createChildren

```java
public static void createChildren​(
DefaultMutableTreeNode
parent,

Object
children)
```

Adds to parent all the children in

children

.
If

children

is an array or vector all of its
elements are added is children, otherwise if

children

is a hashtable all the key/value pairs are added in the order

Enumeration

returns them.

**Parameters:** parent

- the parent node
**Parameters:** children

- the children

- isLeaf

```java
public boolean isLeaf()
```

Returns true if this node allows children. Whether the node
allows children depends on how it was created.

**Specified by:** isLeaf

in interface

TreeNode
**Overrides:** isLeaf

in class

DefaultMutableTreeNode
**Returns:** true if this node allows children, false otherwise
**See Also:** JTree.DynamicUtilTreeNode

- getChildCount

```java
public int getChildCount()
```

Returns the number of child nodes.

**Specified by:** getChildCount

in interface

TreeNode
**Overrides:** getChildCount

in class

DefaultMutableTreeNode
**Returns:** the number of child nodes

- loadChildren

```java
protected void loadChildren()
```

Loads the children based on

childValue

.
If

childValue

is a

Vector

or array each element is added as a child,
if

childValue

is a

Hashtable

each key/value pair is added in the order that

Enumeration

returns the keys.

- getChildAt

```java
public
TreeNode
getChildAt​(int index)
```

Subclassed to load the children, if necessary.

**Specified by:** getChildAt

in interface

TreeNode
**Overrides:** getChildAt

in class

DefaultMutableTreeNode
**Parameters:** index

- an index into this node's child array
**Returns:** the TreeNode in this node's child array at the specified index

- children

```java
public
Enumeration
<
TreeNode
> children()
```

Subclassed to load the children, if necessary.

**Specified by:** children

in interface

TreeNode
**Overrides:** children

in class

DefaultMutableTreeNode
**Returns:** an Enumeration of this node's children

Field Detail

- hasChildren

```java
protected boolean hasChildren
```

Does the this

JTree

have children?
This property is currently not implemented.

- childValue

```java
protected
Object
childValue
```

Value to create children with.

- loadedChildren

```java
protected boolean loadedChildren
```

Have the children been loaded yet?

---

#### Field Detail

hasChildren

```java
protected boolean hasChildren
```

Does the this

JTree

have children?
This property is currently not implemented.

---

#### hasChildren

protected boolean hasChildren

Does the this

JTree

have children?
This property is currently not implemented.

childValue

```java
protected
Object
childValue
```

Value to create children with.

---

#### childValue

protected

Object

childValue

Value to create children with.

loadedChildren

```java
protected boolean loadedChildren
```

Have the children been loaded yet?

---

#### loadedChildren

protected boolean loadedChildren

Have the children been loaded yet?

Constructor Detail

- DynamicUtilTreeNode

```java
public DynamicUtilTreeNode​(
Object
value,

Object
children)
```

Creates a node with the specified object as its value and
with the specified children. For the node to allow children,
the children-object must be an array of objects, a

Vector

, or a

Hashtable

-- even
if empty. Otherwise, the node is not
allowed to have children.

**Parameters:** value

- the

Object

that is the value for the
new node
**Parameters:** children

- an array of

Object

s, a

Vector

, or a

Hashtable

used to create the child nodes; if any other
object is specified, or if the value is

null

,
then the node is not allowed to have children

---

#### Constructor Detail

DynamicUtilTreeNode

```java
public DynamicUtilTreeNode​(
Object
value,

Object
children)
```

Creates a node with the specified object as its value and
with the specified children. For the node to allow children,
the children-object must be an array of objects, a

Vector

, or a

Hashtable

-- even
if empty. Otherwise, the node is not
allowed to have children.

**Parameters:** value

- the

Object

that is the value for the
new node
**Parameters:** children

- an array of

Object

s, a

Vector

, or a

Hashtable

used to create the child nodes; if any other
object is specified, or if the value is

null

,
then the node is not allowed to have children

---

#### DynamicUtilTreeNode

public DynamicUtilTreeNode​(

Object

value,

Object

children)

Creates a node with the specified object as its value and
with the specified children. For the node to allow children,
the children-object must be an array of objects, a

Vector

, or a

Hashtable

-- even
if empty. Otherwise, the node is not
allowed to have children.

Method Detail

- createChildren

```java
public static void createChildren​(
DefaultMutableTreeNode
parent,

Object
children)
```

Adds to parent all the children in

children

.
If

children

is an array or vector all of its
elements are added is children, otherwise if

children

is a hashtable all the key/value pairs are added in the order

Enumeration

returns them.

**Parameters:** parent

- the parent node
**Parameters:** children

- the children

- isLeaf

```java
public boolean isLeaf()
```

Returns true if this node allows children. Whether the node
allows children depends on how it was created.

**Specified by:** isLeaf

in interface

TreeNode
**Overrides:** isLeaf

in class

DefaultMutableTreeNode
**Returns:** true if this node allows children, false otherwise
**See Also:** JTree.DynamicUtilTreeNode

- getChildCount

```java
public int getChildCount()
```

Returns the number of child nodes.

**Specified by:** getChildCount

in interface

TreeNode
**Overrides:** getChildCount

in class

DefaultMutableTreeNode
**Returns:** the number of child nodes

- loadChildren

```java
protected void loadChildren()
```

Loads the children based on

childValue

.
If

childValue

is a

Vector

or array each element is added as a child,
if

childValue

is a

Hashtable

each key/value pair is added in the order that

Enumeration

returns the keys.

- getChildAt

```java
public
TreeNode
getChildAt​(int index)
```

Subclassed to load the children, if necessary.

**Specified by:** getChildAt

in interface

TreeNode
**Overrides:** getChildAt

in class

DefaultMutableTreeNode
**Parameters:** index

- an index into this node's child array
**Returns:** the TreeNode in this node's child array at the specified index

- children

```java
public
Enumeration
<
TreeNode
> children()
```

Subclassed to load the children, if necessary.

**Specified by:** children

in interface

TreeNode
**Overrides:** children

in class

DefaultMutableTreeNode
**Returns:** an Enumeration of this node's children

---

#### Method Detail

createChildren

```java
public static void createChildren​(
DefaultMutableTreeNode
parent,

Object
children)
```

Adds to parent all the children in

children

.
If

children

is an array or vector all of its
elements are added is children, otherwise if

children

is a hashtable all the key/value pairs are added in the order

Enumeration

returns them.

**Parameters:** parent

- the parent node
**Parameters:** children

- the children

---

#### createChildren

public static void createChildren​(

DefaultMutableTreeNode

parent,

Object

children)

Adds to parent all the children in

children

.
If

children

is an array or vector all of its
elements are added is children, otherwise if

children

is a hashtable all the key/value pairs are added in the order

Enumeration

returns them.

isLeaf

```java
public boolean isLeaf()
```

Returns true if this node allows children. Whether the node
allows children depends on how it was created.

**Specified by:** isLeaf

in interface

TreeNode
**Overrides:** isLeaf

in class

DefaultMutableTreeNode
**Returns:** true if this node allows children, false otherwise
**See Also:** JTree.DynamicUtilTreeNode

---

#### isLeaf

public boolean isLeaf()

Returns true if this node allows children. Whether the node
allows children depends on how it was created.

getChildCount

```java
public int getChildCount()
```

Returns the number of child nodes.

**Specified by:** getChildCount

in interface

TreeNode
**Overrides:** getChildCount

in class

DefaultMutableTreeNode
**Returns:** the number of child nodes

---

#### getChildCount

public int getChildCount()

Returns the number of child nodes.

loadChildren

```java
protected void loadChildren()
```

Loads the children based on

childValue

.
If

childValue

is a

Vector

or array each element is added as a child,
if

childValue

is a

Hashtable

each key/value pair is added in the order that

Enumeration

returns the keys.

---

#### loadChildren

protected void loadChildren()

Loads the children based on

childValue

.
If

childValue

is a

Vector

or array each element is added as a child,
if

childValue

is a

Hashtable

each key/value pair is added in the order that

Enumeration

returns the keys.

getChildAt

```java
public
TreeNode
getChildAt​(int index)
```

Subclassed to load the children, if necessary.

**Specified by:** getChildAt

in interface

TreeNode
**Overrides:** getChildAt

in class

DefaultMutableTreeNode
**Parameters:** index

- an index into this node's child array
**Returns:** the TreeNode in this node's child array at the specified index

---

#### getChildAt

public

TreeNode

getChildAt​(int index)

Subclassed to load the children, if necessary.

children

```java
public
Enumeration
<
TreeNode
> children()
```

Subclassed to load the children, if necessary.

**Specified by:** children

in interface

TreeNode
**Overrides:** children

in class

DefaultMutableTreeNode
**Returns:** an Enumeration of this node's children

---

#### children

public

Enumeration

<

TreeNode

> children()

Subclassed to load the children, if necessary.

---

