# Class TreeModelEvent

**Source:** `java.desktop\javax\swing\event\TreeModelEvent.html`

### Class Description

```java
public class
TreeModelEvent

extends
EventObject
```

Encapsulates information describing changes to a tree model, and
used to notify tree model listeners of the change.
For more information and examples see

How to Write a Tree Model Listener

,
a section in

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

#### protected
TreePath
path

Path to the parent of the nodes that have changed.

---

#### protected int[] childIndices

Indices identifying the position of where the children were.

---

#### protected
Object
[] children

Children that have been removed.

---

### Constructor Details

#### public TreeModelEvent​(
Object
source,

Object
[] path,
int[] childIndices,

Object
[] children)

Used to create an event when nodes have been changed, inserted, or
removed, identifying the path to the parent of the modified items as
an array of Objects. All of the modified objects are siblings which are
direct descendents (not grandchildren) of the specified parent.
The positions at which the inserts, deletes, or changes occurred are
specified by an array of

int

. The indexes in that array
must be in order, from lowest to highest.

For changes, the indexes in the model correspond exactly to the indexes
of items currently displayed in the UI. As a result, it is not really
critical if the indexes are not in their exact order. But after multiple
inserts or deletes, the items currently in the UI no longer correspond
to the items in the model. It is therefore critical to specify the
indexes properly for inserts and deletes.

For inserts, the indexes represent the

final

state of the tree,
after the inserts have occurred. Since the indexes must be specified in
order, the most natural processing methodology is to do the inserts
starting at the lowest index and working towards the highest. Accumulate
a Vector of

Integer

objects that specify the
insert-locations as you go, then convert the Vector to an
array of

int

to create the event. When the postition-index
equals zero, the node is inserted at the beginning of the list. When the
position index equals the size of the list, the node is "inserted" at
(appended to) the end of the list.

For deletes, the indexes represent the

initial

state of the tree,
before the deletes have occurred. Since the indexes must be specified in
order, the most natural processing methodology is to use a delete-counter.
Start by initializing the counter to zero and start work through the
list from lowest to highest. Every time you do a delete, add the current
value of the delete-counter to the index-position where the delete occurred,
and append the result to a Vector of delete-locations, using

addElement()

. Then increment the delete-counter. The index
positions stored in the Vector therefore reflect the effects of all previous
deletes, so they represent each object's position in the initial tree.
(You could also start at the highest index and working back towards the
lowest, accumulating a Vector of delete-locations as you go using the

insertElementAt(Integer, 0)

.) However you produce the Vector
of initial-positions, you then need to convert the Vector of

Integer

objects to an array of

int

to create the event.

Notes:

- Like the

insertNodeInto

method in the

DefaultTreeModel

class,

insertElementAt

appends to the

Vector

when the index matches the size
of the vector. So you can use

insertElementAt(Integer, 0)

even when the vector is empty.
- To create a node changed event for the root node, specify the parent
and the child indices as

null

.

**Parameters:**
- source

- the Object responsible for generating the event (typically
the creator of the event object passes

this

for its value)
- path

- an array of Object identifying the path to the
parent of the modified item(s), where the first element
of the array is the Object stored at the root node and
the last element is the Object stored at the parent node
- childIndices

- an array of

int

that specifies the
index values of the removed items. The indices must be
in sorted order, from lowest to highest
- children

- an array of Object containing the inserted, removed, or
changed objects

**See Also:**
- TreePath

---

#### public TreeModelEvent​(
Object
source,

TreePath
path,
int[] childIndices,

Object
[] children)

Used to create an event when nodes have been changed, inserted, or
removed, identifying the path to the parent of the modified items as
a TreePath object. For more information on how to specify the indexes
and objects, see

TreeModelEvent(Object,Object[],int[],Object[])

.

**Parameters:**
- source

- the Object responsible for generating the event (typically
the creator of the event object passes

this

for its value)
- path

- a TreePath object that identifies the path to the
parent of the modified item(s)
- childIndices

- an array of

int

that specifies the
index values of the modified items
- children

- an array of Object containing the inserted, removed, or
changed objects

**See Also:**
- TreeModelEvent(Object,Object[],int[],Object[])

---

#### public TreeModelEvent​(
Object
source,

Object
[] path)

Used to create an event when the node structure has changed in some way,
identifying the path to the root of a modified subtree as an array of
Objects. A structure change event might involve nodes swapping position,
for example, or it might encapsulate multiple inserts and deletes in the
subtree stemming from the node, where the changes may have taken place at
different levels of the subtree.

Note:

JTree collapses all nodes under the specified node, so that only its
immediate children are visible.

**Parameters:**
- source

- the Object responsible for generating the event (typically
the creator of the event object passes

this

for its value)
- path

- an array of Object identifying the path to the root of the
modified subtree, where the first element of the array is
the object stored at the root node and the last element
is the object stored at the changed node

**See Also:**
- TreePath

---

#### public TreeModelEvent​(
Object
source,

TreePath
path)

Used to create an event when the node structure has changed in some way,
identifying the path to the root of the modified subtree as a TreePath
object. For more information on this event specification, see

TreeModelEvent(Object,Object[])

.

**Parameters:**
- source

- the Object responsible for generating the event (typically
the creator of the event object passes

this

for its value)
- path

- a TreePath object that identifies the path to the
change. In the DefaultTreeModel,
this object contains an array of user-data objects,
but a subclass of TreePath could use some totally
different mechanism -- for example, a node ID number

**See Also:**
- TreeModelEvent(Object,Object[])

---

### Method Details

#### public
TreePath
getTreePath()

For all events, except treeStructureChanged,
returns the parent of the changed nodes.
For treeStructureChanged events, returns the ancestor of the
structure that has changed. This and

getChildIndices

are used to get a list of the effected
nodes.

The one exception to this is a treeNodesChanged event that is to
identify the root, in which case this will return the root
and

getChildIndices

will return null.

**Returns:**
- the TreePath used in identifying the changed nodes.

**See Also:**
- TreePath.getLastPathComponent()

---

#### public
Object
[] getPath()

Convenience method to get the array of objects from the TreePath
instance that this event wraps.

**Returns:**
- an array of Objects, where the first Object is the one
stored at the root and the last object is the one
stored at the node identified by the path

---

#### public
Object
[] getChildren()

Returns the objects that are children of the node identified by

getPath

at the locations specified by

getChildIndices

. If this is a removal event the
returned objects are no longer children of the parent node.

**Returns:**
- an array of Object containing the children specified by
the event

**See Also:**
- getPath()

,

getChildIndices()

---

#### public int[] getChildIndices()

Returns the values of the child indexes. If this is a removal event
the indexes point to locations in the initial list where items
were removed. If it is an insert, the indices point to locations
in the final list where the items were added. For node changes,
the indices point to the locations of the modified nodes.

**Returns:**
- an array of

int

containing index locations for
the children specified by the event

---

#### public
String
toString()

Returns a string that displays and identifies this object's
properties.

**Overrides:**
- toString

in class

EventObject

**Returns:**
- a String representation of this object

---

### Additional Sections

#### Class TreeModelEvent

java.lang.Object

- java.util.EventObject
- - javax.swing.event.TreeModelEvent

java.util.EventObject

- javax.swing.event.TreeModelEvent

javax.swing.event.TreeModelEvent

**All Implemented Interfaces:** Serializable

```java
public class
TreeModelEvent

extends
EventObject
```

Encapsulates information describing changes to a tree model, and
used to notify tree model listeners of the change.
For more information and examples see

How to Write a Tree Model Listener

,
a section in

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

TreeModelEvent

extends

EventObject

Encapsulates information describing changes to a tree model, and
used to notify tree model listeners of the change.
For more information and examples see

How to Write a Tree Model Listener

,
a section in

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

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected int[]

childIndices

Indices identifying the position of where the children were.

protected

Object

[]

children

Children that have been removed.

protected

TreePath

path

Path to the parent of the nodes that have changed.

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TreeModelEvent

​(

Object

source,

Object

[] path)

Used to create an event when the node structure has changed in some way,
identifying the path to the root of a modified subtree as an array of
Objects.

TreeModelEvent

​(

Object

source,

Object

[] path,
int[] childIndices,

Object

[] children)

Used to create an event when nodes have been changed, inserted, or
removed, identifying the path to the parent of the modified items as
an array of Objects.

TreeModelEvent

​(

Object

source,

TreePath

path)

Used to create an event when the node structure has changed in some way,
identifying the path to the root of the modified subtree as a TreePath
object.

TreeModelEvent

​(

Object

source,

TreePath

path,
int[] childIndices,

Object

[] children)

Used to create an event when nodes have been changed, inserted, or
removed, identifying the path to the parent of the modified items as
a TreePath object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int[]

getChildIndices

()

Returns the values of the child indexes.

Object

[]

getChildren

()

Returns the objects that are children of the node identified by

getPath

at the locations specified by

getChildIndices

.

Object

[]

getPath

()

Convenience method to get the array of objects from the TreePath
instance that this event wraps.

TreePath

getTreePath

()

For all events, except treeStructureChanged,
returns the parent of the changed nodes.

String

toString

()

Returns a string that displays and identifies this object's
properties.

- Methods declared in class java.util.

EventObject

getSource

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

protected int[]

childIndices

Indices identifying the position of where the children were.

protected

Object

[]

children

Children that have been removed.

protected

TreePath

path

Path to the parent of the nodes that have changed.

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

Indices identifying the position of where the children were.

Children that have been removed.

Path to the parent of the nodes that have changed.

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

TreeModelEvent

​(

Object

source,

Object

[] path)

Used to create an event when the node structure has changed in some way,
identifying the path to the root of a modified subtree as an array of
Objects.

TreeModelEvent

​(

Object

source,

Object

[] path,
int[] childIndices,

Object

[] children)

Used to create an event when nodes have been changed, inserted, or
removed, identifying the path to the parent of the modified items as
an array of Objects.

TreeModelEvent

​(

Object

source,

TreePath

path)

Used to create an event when the node structure has changed in some way,
identifying the path to the root of the modified subtree as a TreePath
object.

TreeModelEvent

​(

Object

source,

TreePath

path,
int[] childIndices,

Object

[] children)

Used to create an event when nodes have been changed, inserted, or
removed, identifying the path to the parent of the modified items as
a TreePath object.

---

#### Constructor Summary

Used to create an event when the node structure has changed in some way,
identifying the path to the root of a modified subtree as an array of
Objects.

Used to create an event when nodes have been changed, inserted, or
removed, identifying the path to the parent of the modified items as
an array of Objects.

Used to create an event when the node structure has changed in some way,
identifying the path to the root of the modified subtree as a TreePath
object.

Used to create an event when nodes have been changed, inserted, or
removed, identifying the path to the parent of the modified items as
a TreePath object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int[]

getChildIndices

()

Returns the values of the child indexes.

Object

[]

getChildren

()

Returns the objects that are children of the node identified by

getPath

at the locations specified by

getChildIndices

.

Object

[]

getPath

()

Convenience method to get the array of objects from the TreePath
instance that this event wraps.

TreePath

getTreePath

()

For all events, except treeStructureChanged,
returns the parent of the changed nodes.

String

toString

()

Returns a string that displays and identifies this object's
properties.

- Methods declared in class java.util.

EventObject

getSource

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

wait

,

wait

,

wait

---

#### Method Summary

Returns the values of the child indexes.

Returns the objects that are children of the node identified by

getPath

at the locations specified by

getChildIndices

.

Convenience method to get the array of objects from the TreePath
instance that this event wraps.

For all events, except treeStructureChanged,
returns the parent of the changed nodes.

Returns a string that displays and identifies this object's
properties.

Methods declared in class java.util.

EventObject

getSource

---

#### Methods declared in class java.util. EventObject

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- path

```java
protected
TreePath
path
```

Path to the parent of the nodes that have changed.

- childIndices

```java
protected int[] childIndices
```

Indices identifying the position of where the children were.

- children

```java
protected
Object
[] children
```

Children that have been removed.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TreeModelEvent

```java
public TreeModelEvent​(
Object
source,

Object
[] path,
int[] childIndices,

Object
[] children)
```

Used to create an event when nodes have been changed, inserted, or
removed, identifying the path to the parent of the modified items as
an array of Objects. All of the modified objects are siblings which are
direct descendents (not grandchildren) of the specified parent.
The positions at which the inserts, deletes, or changes occurred are
specified by an array of

int

. The indexes in that array
must be in order, from lowest to highest.

For changes, the indexes in the model correspond exactly to the indexes
of items currently displayed in the UI. As a result, it is not really
critical if the indexes are not in their exact order. But after multiple
inserts or deletes, the items currently in the UI no longer correspond
to the items in the model. It is therefore critical to specify the
indexes properly for inserts and deletes.

For inserts, the indexes represent the

final

state of the tree,
after the inserts have occurred. Since the indexes must be specified in
order, the most natural processing methodology is to do the inserts
starting at the lowest index and working towards the highest. Accumulate
a Vector of

Integer

objects that specify the
insert-locations as you go, then convert the Vector to an
array of

int

to create the event. When the postition-index
equals zero, the node is inserted at the beginning of the list. When the
position index equals the size of the list, the node is "inserted" at
(appended to) the end of the list.

For deletes, the indexes represent the

initial

state of the tree,
before the deletes have occurred. Since the indexes must be specified in
order, the most natural processing methodology is to use a delete-counter.
Start by initializing the counter to zero and start work through the
list from lowest to highest. Every time you do a delete, add the current
value of the delete-counter to the index-position where the delete occurred,
and append the result to a Vector of delete-locations, using

addElement()

. Then increment the delete-counter. The index
positions stored in the Vector therefore reflect the effects of all previous
deletes, so they represent each object's position in the initial tree.
(You could also start at the highest index and working back towards the
lowest, accumulating a Vector of delete-locations as you go using the

insertElementAt(Integer, 0)

.) However you produce the Vector
of initial-positions, you then need to convert the Vector of

Integer

objects to an array of

int

to create the event.

Notes:

- Like the

insertNodeInto

method in the

DefaultTreeModel

class,

insertElementAt

appends to the

Vector

when the index matches the size
of the vector. So you can use

insertElementAt(Integer, 0)

even when the vector is empty.
- To create a node changed event for the root node, specify the parent
and the child indices as

null

.

**Parameters:** source

- the Object responsible for generating the event (typically
the creator of the event object passes

this

for its value)
**Parameters:** path

- an array of Object identifying the path to the
parent of the modified item(s), where the first element
of the array is the Object stored at the root node and
the last element is the Object stored at the parent node
**Parameters:** childIndices

- an array of

int

that specifies the
index values of the removed items. The indices must be
in sorted order, from lowest to highest
**Parameters:** children

- an array of Object containing the inserted, removed, or
changed objects
**See Also:** TreePath

- TreeModelEvent

```java
public TreeModelEvent​(
Object
source,

TreePath
path,
int[] childIndices,

Object
[] children)
```

Used to create an event when nodes have been changed, inserted, or
removed, identifying the path to the parent of the modified items as
a TreePath object. For more information on how to specify the indexes
and objects, see

TreeModelEvent(Object,Object[],int[],Object[])

.

**Parameters:** source

- the Object responsible for generating the event (typically
the creator of the event object passes

this

for its value)
**Parameters:** path

- a TreePath object that identifies the path to the
parent of the modified item(s)
**Parameters:** childIndices

- an array of

int

that specifies the
index values of the modified items
**Parameters:** children

- an array of Object containing the inserted, removed, or
changed objects
**See Also:** TreeModelEvent(Object,Object[],int[],Object[])

- TreeModelEvent

```java
public TreeModelEvent​(
Object
source,

Object
[] path)
```

Used to create an event when the node structure has changed in some way,
identifying the path to the root of a modified subtree as an array of
Objects. A structure change event might involve nodes swapping position,
for example, or it might encapsulate multiple inserts and deletes in the
subtree stemming from the node, where the changes may have taken place at
different levels of the subtree.

Note:

JTree collapses all nodes under the specified node, so that only its
immediate children are visible.

**Parameters:** source

- the Object responsible for generating the event (typically
the creator of the event object passes

this

for its value)
**Parameters:** path

- an array of Object identifying the path to the root of the
modified subtree, where the first element of the array is
the object stored at the root node and the last element
is the object stored at the changed node
**See Also:** TreePath

- TreeModelEvent

```java
public TreeModelEvent​(
Object
source,

TreePath
path)
```

Used to create an event when the node structure has changed in some way,
identifying the path to the root of the modified subtree as a TreePath
object. For more information on this event specification, see

TreeModelEvent(Object,Object[])

.

**Parameters:** source

- the Object responsible for generating the event (typically
the creator of the event object passes

this

for its value)
**Parameters:** path

- a TreePath object that identifies the path to the
change. In the DefaultTreeModel,
this object contains an array of user-data objects,
but a subclass of TreePath could use some totally
different mechanism -- for example, a node ID number
**See Also:** TreeModelEvent(Object,Object[])

============ METHOD DETAIL ==========

- Method Detail

- getTreePath

```java
public
TreePath
getTreePath()
```

For all events, except treeStructureChanged,
returns the parent of the changed nodes.
For treeStructureChanged events, returns the ancestor of the
structure that has changed. This and

getChildIndices

are used to get a list of the effected
nodes.

The one exception to this is a treeNodesChanged event that is to
identify the root, in which case this will return the root
and

getChildIndices

will return null.

**Returns:** the TreePath used in identifying the changed nodes.
**See Also:** TreePath.getLastPathComponent()

- getPath

```java
public
Object
[] getPath()
```

Convenience method to get the array of objects from the TreePath
instance that this event wraps.

**Returns:** an array of Objects, where the first Object is the one
stored at the root and the last object is the one
stored at the node identified by the path

- getChildren

```java
public
Object
[] getChildren()
```

Returns the objects that are children of the node identified by

getPath

at the locations specified by

getChildIndices

. If this is a removal event the
returned objects are no longer children of the parent node.

**Returns:** an array of Object containing the children specified by
the event
**See Also:** getPath()

,

getChildIndices()

- getChildIndices

```java
public int[] getChildIndices()
```

Returns the values of the child indexes. If this is a removal event
the indexes point to locations in the initial list where items
were removed. If it is an insert, the indices point to locations
in the final list where the items were added. For node changes,
the indices point to the locations of the modified nodes.

**Returns:** an array of

int

containing index locations for
the children specified by the event

- toString

```java
public
String
toString()
```

Returns a string that displays and identifies this object's
properties.

**Overrides:** toString

in class

EventObject
**Returns:** a String representation of this object

Field Detail

- path

```java
protected
TreePath
path
```

Path to the parent of the nodes that have changed.

- childIndices

```java
protected int[] childIndices
```

Indices identifying the position of where the children were.

- children

```java
protected
Object
[] children
```

Children that have been removed.

---

#### Field Detail

path

```java
protected
TreePath
path
```

Path to the parent of the nodes that have changed.

---

#### path

protected

TreePath

path

Path to the parent of the nodes that have changed.

childIndices

```java
protected int[] childIndices
```

Indices identifying the position of where the children were.

---

#### childIndices

protected int[] childIndices

Indices identifying the position of where the children were.

children

```java
protected
Object
[] children
```

Children that have been removed.

---

#### children

protected

Object

[] children

Children that have been removed.

Constructor Detail

- TreeModelEvent

```java
public TreeModelEvent​(
Object
source,

Object
[] path,
int[] childIndices,

Object
[] children)
```

Used to create an event when nodes have been changed, inserted, or
removed, identifying the path to the parent of the modified items as
an array of Objects. All of the modified objects are siblings which are
direct descendents (not grandchildren) of the specified parent.
The positions at which the inserts, deletes, or changes occurred are
specified by an array of

int

. The indexes in that array
must be in order, from lowest to highest.

For changes, the indexes in the model correspond exactly to the indexes
of items currently displayed in the UI. As a result, it is not really
critical if the indexes are not in their exact order. But after multiple
inserts or deletes, the items currently in the UI no longer correspond
to the items in the model. It is therefore critical to specify the
indexes properly for inserts and deletes.

For inserts, the indexes represent the

final

state of the tree,
after the inserts have occurred. Since the indexes must be specified in
order, the most natural processing methodology is to do the inserts
starting at the lowest index and working towards the highest. Accumulate
a Vector of

Integer

objects that specify the
insert-locations as you go, then convert the Vector to an
array of

int

to create the event. When the postition-index
equals zero, the node is inserted at the beginning of the list. When the
position index equals the size of the list, the node is "inserted" at
(appended to) the end of the list.

For deletes, the indexes represent the

initial

state of the tree,
before the deletes have occurred. Since the indexes must be specified in
order, the most natural processing methodology is to use a delete-counter.
Start by initializing the counter to zero and start work through the
list from lowest to highest. Every time you do a delete, add the current
value of the delete-counter to the index-position where the delete occurred,
and append the result to a Vector of delete-locations, using

addElement()

. Then increment the delete-counter. The index
positions stored in the Vector therefore reflect the effects of all previous
deletes, so they represent each object's position in the initial tree.
(You could also start at the highest index and working back towards the
lowest, accumulating a Vector of delete-locations as you go using the

insertElementAt(Integer, 0)

.) However you produce the Vector
of initial-positions, you then need to convert the Vector of

Integer

objects to an array of

int

to create the event.

Notes:

- Like the

insertNodeInto

method in the

DefaultTreeModel

class,

insertElementAt

appends to the

Vector

when the index matches the size
of the vector. So you can use

insertElementAt(Integer, 0)

even when the vector is empty.
- To create a node changed event for the root node, specify the parent
and the child indices as

null

.

**Parameters:** source

- the Object responsible for generating the event (typically
the creator of the event object passes

this

for its value)
**Parameters:** path

- an array of Object identifying the path to the
parent of the modified item(s), where the first element
of the array is the Object stored at the root node and
the last element is the Object stored at the parent node
**Parameters:** childIndices

- an array of

int

that specifies the
index values of the removed items. The indices must be
in sorted order, from lowest to highest
**Parameters:** children

- an array of Object containing the inserted, removed, or
changed objects
**See Also:** TreePath

- TreeModelEvent

```java
public TreeModelEvent​(
Object
source,

TreePath
path,
int[] childIndices,

Object
[] children)
```

Used to create an event when nodes have been changed, inserted, or
removed, identifying the path to the parent of the modified items as
a TreePath object. For more information on how to specify the indexes
and objects, see

TreeModelEvent(Object,Object[],int[],Object[])

.

**Parameters:** source

- the Object responsible for generating the event (typically
the creator of the event object passes

this

for its value)
**Parameters:** path

- a TreePath object that identifies the path to the
parent of the modified item(s)
**Parameters:** childIndices

- an array of

int

that specifies the
index values of the modified items
**Parameters:** children

- an array of Object containing the inserted, removed, or
changed objects
**See Also:** TreeModelEvent(Object,Object[],int[],Object[])

- TreeModelEvent

```java
public TreeModelEvent​(
Object
source,

Object
[] path)
```

Used to create an event when the node structure has changed in some way,
identifying the path to the root of a modified subtree as an array of
Objects. A structure change event might involve nodes swapping position,
for example, or it might encapsulate multiple inserts and deletes in the
subtree stemming from the node, where the changes may have taken place at
different levels of the subtree.

Note:

JTree collapses all nodes under the specified node, so that only its
immediate children are visible.

**Parameters:** source

- the Object responsible for generating the event (typically
the creator of the event object passes

this

for its value)
**Parameters:** path

- an array of Object identifying the path to the root of the
modified subtree, where the first element of the array is
the object stored at the root node and the last element
is the object stored at the changed node
**See Also:** TreePath

- TreeModelEvent

```java
public TreeModelEvent​(
Object
source,

TreePath
path)
```

Used to create an event when the node structure has changed in some way,
identifying the path to the root of the modified subtree as a TreePath
object. For more information on this event specification, see

TreeModelEvent(Object,Object[])

.

**Parameters:** source

- the Object responsible for generating the event (typically
the creator of the event object passes

this

for its value)
**Parameters:** path

- a TreePath object that identifies the path to the
change. In the DefaultTreeModel,
this object contains an array of user-data objects,
but a subclass of TreePath could use some totally
different mechanism -- for example, a node ID number
**See Also:** TreeModelEvent(Object,Object[])

---

#### Constructor Detail

TreeModelEvent

```java
public TreeModelEvent​(
Object
source,

Object
[] path,
int[] childIndices,

Object
[] children)
```

Used to create an event when nodes have been changed, inserted, or
removed, identifying the path to the parent of the modified items as
an array of Objects. All of the modified objects are siblings which are
direct descendents (not grandchildren) of the specified parent.
The positions at which the inserts, deletes, or changes occurred are
specified by an array of

int

. The indexes in that array
must be in order, from lowest to highest.

For changes, the indexes in the model correspond exactly to the indexes
of items currently displayed in the UI. As a result, it is not really
critical if the indexes are not in their exact order. But after multiple
inserts or deletes, the items currently in the UI no longer correspond
to the items in the model. It is therefore critical to specify the
indexes properly for inserts and deletes.

For inserts, the indexes represent the

final

state of the tree,
after the inserts have occurred. Since the indexes must be specified in
order, the most natural processing methodology is to do the inserts
starting at the lowest index and working towards the highest. Accumulate
a Vector of

Integer

objects that specify the
insert-locations as you go, then convert the Vector to an
array of

int

to create the event. When the postition-index
equals zero, the node is inserted at the beginning of the list. When the
position index equals the size of the list, the node is "inserted" at
(appended to) the end of the list.

For deletes, the indexes represent the

initial

state of the tree,
before the deletes have occurred. Since the indexes must be specified in
order, the most natural processing methodology is to use a delete-counter.
Start by initializing the counter to zero and start work through the
list from lowest to highest. Every time you do a delete, add the current
value of the delete-counter to the index-position where the delete occurred,
and append the result to a Vector of delete-locations, using

addElement()

. Then increment the delete-counter. The index
positions stored in the Vector therefore reflect the effects of all previous
deletes, so they represent each object's position in the initial tree.
(You could also start at the highest index and working back towards the
lowest, accumulating a Vector of delete-locations as you go using the

insertElementAt(Integer, 0)

.) However you produce the Vector
of initial-positions, you then need to convert the Vector of

Integer

objects to an array of

int

to create the event.

Notes:

- Like the

insertNodeInto

method in the

DefaultTreeModel

class,

insertElementAt

appends to the

Vector

when the index matches the size
of the vector. So you can use

insertElementAt(Integer, 0)

even when the vector is empty.
- To create a node changed event for the root node, specify the parent
and the child indices as

null

.

**Parameters:** source

- the Object responsible for generating the event (typically
the creator of the event object passes

this

for its value)
**Parameters:** path

- an array of Object identifying the path to the
parent of the modified item(s), where the first element
of the array is the Object stored at the root node and
the last element is the Object stored at the parent node
**Parameters:** childIndices

- an array of

int

that specifies the
index values of the removed items. The indices must be
in sorted order, from lowest to highest
**Parameters:** children

- an array of Object containing the inserted, removed, or
changed objects
**See Also:** TreePath

---

#### TreeModelEvent

public TreeModelEvent​(

Object

source,

Object

[] path,
int[] childIndices,

Object

[] children)

Used to create an event when nodes have been changed, inserted, or
removed, identifying the path to the parent of the modified items as
an array of Objects. All of the modified objects are siblings which are
direct descendents (not grandchildren) of the specified parent.
The positions at which the inserts, deletes, or changes occurred are
specified by an array of

int

. The indexes in that array
must be in order, from lowest to highest.

For changes, the indexes in the model correspond exactly to the indexes
of items currently displayed in the UI. As a result, it is not really
critical if the indexes are not in their exact order. But after multiple
inserts or deletes, the items currently in the UI no longer correspond
to the items in the model. It is therefore critical to specify the
indexes properly for inserts and deletes.

For inserts, the indexes represent the

final

state of the tree,
after the inserts have occurred. Since the indexes must be specified in
order, the most natural processing methodology is to do the inserts
starting at the lowest index and working towards the highest. Accumulate
a Vector of

Integer

objects that specify the
insert-locations as you go, then convert the Vector to an
array of

int

to create the event. When the postition-index
equals zero, the node is inserted at the beginning of the list. When the
position index equals the size of the list, the node is "inserted" at
(appended to) the end of the list.

For deletes, the indexes represent the

initial

state of the tree,
before the deletes have occurred. Since the indexes must be specified in
order, the most natural processing methodology is to use a delete-counter.
Start by initializing the counter to zero and start work through the
list from lowest to highest. Every time you do a delete, add the current
value of the delete-counter to the index-position where the delete occurred,
and append the result to a Vector of delete-locations, using

addElement()

. Then increment the delete-counter. The index
positions stored in the Vector therefore reflect the effects of all previous
deletes, so they represent each object's position in the initial tree.
(You could also start at the highest index and working back towards the
lowest, accumulating a Vector of delete-locations as you go using the

insertElementAt(Integer, 0)

.) However you produce the Vector
of initial-positions, you then need to convert the Vector of

Integer

objects to an array of

int

to create the event.

Notes:

- Like the

insertNodeInto

method in the

DefaultTreeModel

class,

insertElementAt

appends to the

Vector

when the index matches the size
of the vector. So you can use

insertElementAt(Integer, 0)

even when the vector is empty.
- To create a node changed event for the root node, specify the parent
and the child indices as

null

.

For changes, the indexes in the model correspond exactly to the indexes
of items currently displayed in the UI. As a result, it is not really
critical if the indexes are not in their exact order. But after multiple
inserts or deletes, the items currently in the UI no longer correspond
to the items in the model. It is therefore critical to specify the
indexes properly for inserts and deletes.

For inserts, the indexes represent the

final

state of the tree,
after the inserts have occurred. Since the indexes must be specified in
order, the most natural processing methodology is to do the inserts
starting at the lowest index and working towards the highest. Accumulate
a Vector of

Integer

objects that specify the
insert-locations as you go, then convert the Vector to an
array of

int

to create the event. When the postition-index
equals zero, the node is inserted at the beginning of the list. When the
position index equals the size of the list, the node is "inserted" at
(appended to) the end of the list.

For deletes, the indexes represent the

initial

state of the tree,
before the deletes have occurred. Since the indexes must be specified in
order, the most natural processing methodology is to use a delete-counter.
Start by initializing the counter to zero and start work through the
list from lowest to highest. Every time you do a delete, add the current
value of the delete-counter to the index-position where the delete occurred,
and append the result to a Vector of delete-locations, using

addElement()

. Then increment the delete-counter. The index
positions stored in the Vector therefore reflect the effects of all previous
deletes, so they represent each object's position in the initial tree.
(You could also start at the highest index and working back towards the
lowest, accumulating a Vector of delete-locations as you go using the

insertElementAt(Integer, 0)

.) However you produce the Vector
of initial-positions, you then need to convert the Vector of

Integer

objects to an array of

int

to create the event.

Notes:

- Like the

insertNodeInto

method in the

DefaultTreeModel

class,

insertElementAt

appends to the

Vector

when the index matches the size
of the vector. So you can use

insertElementAt(Integer, 0)

even when the vector is empty.
- To create a node changed event for the root node, specify the parent
and the child indices as

null

.

For inserts, the indexes represent the

final

state of the tree,
after the inserts have occurred. Since the indexes must be specified in
order, the most natural processing methodology is to do the inserts
starting at the lowest index and working towards the highest. Accumulate
a Vector of

Integer

objects that specify the
insert-locations as you go, then convert the Vector to an
array of

int

to create the event. When the postition-index
equals zero, the node is inserted at the beginning of the list. When the
position index equals the size of the list, the node is "inserted" at
(appended to) the end of the list.

For deletes, the indexes represent the

initial

state of the tree,
before the deletes have occurred. Since the indexes must be specified in
order, the most natural processing methodology is to use a delete-counter.
Start by initializing the counter to zero and start work through the
list from lowest to highest. Every time you do a delete, add the current
value of the delete-counter to the index-position where the delete occurred,
and append the result to a Vector of delete-locations, using

addElement()

. Then increment the delete-counter. The index
positions stored in the Vector therefore reflect the effects of all previous
deletes, so they represent each object's position in the initial tree.
(You could also start at the highest index and working back towards the
lowest, accumulating a Vector of delete-locations as you go using the

insertElementAt(Integer, 0)

.) However you produce the Vector
of initial-positions, you then need to convert the Vector of

Integer

objects to an array of

int

to create the event.

Notes:

- Like the

insertNodeInto

method in the

DefaultTreeModel

class,

insertElementAt

appends to the

Vector

when the index matches the size
of the vector. So you can use

insertElementAt(Integer, 0)

even when the vector is empty.
- To create a node changed event for the root node, specify the parent
and the child indices as

null

.

For deletes, the indexes represent the

initial

state of the tree,
before the deletes have occurred. Since the indexes must be specified in
order, the most natural processing methodology is to use a delete-counter.
Start by initializing the counter to zero and start work through the
list from lowest to highest. Every time you do a delete, add the current
value of the delete-counter to the index-position where the delete occurred,
and append the result to a Vector of delete-locations, using

addElement()

. Then increment the delete-counter. The index
positions stored in the Vector therefore reflect the effects of all previous
deletes, so they represent each object's position in the initial tree.
(You could also start at the highest index and working back towards the
lowest, accumulating a Vector of delete-locations as you go using the

insertElementAt(Integer, 0)

.) However you produce the Vector
of initial-positions, you then need to convert the Vector of

Integer

objects to an array of

int

to create the event.

Notes:

- Like the

insertNodeInto

method in the

DefaultTreeModel

class,

insertElementAt

appends to the

Vector

when the index matches the size
of the vector. So you can use

insertElementAt(Integer, 0)

even when the vector is empty.
- To create a node changed event for the root node, specify the parent
and the child indices as

null

.

Notes:

- Like the

insertNodeInto

method in the

DefaultTreeModel

class,

insertElementAt

appends to the

Vector

when the index matches the size
of the vector. So you can use

insertElementAt(Integer, 0)

even when the vector is empty.
- To create a node changed event for the root node, specify the parent
and the child indices as

null

.

Like the

insertNodeInto

method in the

DefaultTreeModel

class,

insertElementAt

appends to the

Vector

when the index matches the size
of the vector. So you can use

insertElementAt(Integer, 0)

even when the vector is empty.

To create a node changed event for the root node, specify the parent
and the child indices as

null

.

TreeModelEvent

```java
public TreeModelEvent​(
Object
source,

TreePath
path,
int[] childIndices,

Object
[] children)
```

Used to create an event when nodes have been changed, inserted, or
removed, identifying the path to the parent of the modified items as
a TreePath object. For more information on how to specify the indexes
and objects, see

TreeModelEvent(Object,Object[],int[],Object[])

.

**Parameters:** source

- the Object responsible for generating the event (typically
the creator of the event object passes

this

for its value)
**Parameters:** path

- a TreePath object that identifies the path to the
parent of the modified item(s)
**Parameters:** childIndices

- an array of

int

that specifies the
index values of the modified items
**Parameters:** children

- an array of Object containing the inserted, removed, or
changed objects
**See Also:** TreeModelEvent(Object,Object[],int[],Object[])

---

#### TreeModelEvent

public TreeModelEvent​(

Object

source,

TreePath

path,
int[] childIndices,

Object

[] children)

Used to create an event when nodes have been changed, inserted, or
removed, identifying the path to the parent of the modified items as
a TreePath object. For more information on how to specify the indexes
and objects, see

TreeModelEvent(Object,Object[],int[],Object[])

.

TreeModelEvent

```java
public TreeModelEvent​(
Object
source,

Object
[] path)
```

Used to create an event when the node structure has changed in some way,
identifying the path to the root of a modified subtree as an array of
Objects. A structure change event might involve nodes swapping position,
for example, or it might encapsulate multiple inserts and deletes in the
subtree stemming from the node, where the changes may have taken place at
different levels of the subtree.

Note:

JTree collapses all nodes under the specified node, so that only its
immediate children are visible.

**Parameters:** source

- the Object responsible for generating the event (typically
the creator of the event object passes

this

for its value)
**Parameters:** path

- an array of Object identifying the path to the root of the
modified subtree, where the first element of the array is
the object stored at the root node and the last element
is the object stored at the changed node
**See Also:** TreePath

---

#### TreeModelEvent

public TreeModelEvent​(

Object

source,

Object

[] path)

Used to create an event when the node structure has changed in some way,
identifying the path to the root of a modified subtree as an array of
Objects. A structure change event might involve nodes swapping position,
for example, or it might encapsulate multiple inserts and deletes in the
subtree stemming from the node, where the changes may have taken place at
different levels of the subtree.

Note:

JTree collapses all nodes under the specified node, so that only its
immediate children are visible.

TreeModelEvent

```java
public TreeModelEvent​(
Object
source,

TreePath
path)
```

Used to create an event when the node structure has changed in some way,
identifying the path to the root of the modified subtree as a TreePath
object. For more information on this event specification, see

TreeModelEvent(Object,Object[])

.

**Parameters:** source

- the Object responsible for generating the event (typically
the creator of the event object passes

this

for its value)
**Parameters:** path

- a TreePath object that identifies the path to the
change. In the DefaultTreeModel,
this object contains an array of user-data objects,
but a subclass of TreePath could use some totally
different mechanism -- for example, a node ID number
**See Also:** TreeModelEvent(Object,Object[])

---

#### TreeModelEvent

public TreeModelEvent​(

Object

source,

TreePath

path)

Used to create an event when the node structure has changed in some way,
identifying the path to the root of the modified subtree as a TreePath
object. For more information on this event specification, see

TreeModelEvent(Object,Object[])

.

Method Detail

- getTreePath

```java
public
TreePath
getTreePath()
```

For all events, except treeStructureChanged,
returns the parent of the changed nodes.
For treeStructureChanged events, returns the ancestor of the
structure that has changed. This and

getChildIndices

are used to get a list of the effected
nodes.

The one exception to this is a treeNodesChanged event that is to
identify the root, in which case this will return the root
and

getChildIndices

will return null.

**Returns:** the TreePath used in identifying the changed nodes.
**See Also:** TreePath.getLastPathComponent()

- getPath

```java
public
Object
[] getPath()
```

Convenience method to get the array of objects from the TreePath
instance that this event wraps.

**Returns:** an array of Objects, where the first Object is the one
stored at the root and the last object is the one
stored at the node identified by the path

- getChildren

```java
public
Object
[] getChildren()
```

Returns the objects that are children of the node identified by

getPath

at the locations specified by

getChildIndices

. If this is a removal event the
returned objects are no longer children of the parent node.

**Returns:** an array of Object containing the children specified by
the event
**See Also:** getPath()

,

getChildIndices()

- getChildIndices

```java
public int[] getChildIndices()
```

Returns the values of the child indexes. If this is a removal event
the indexes point to locations in the initial list where items
were removed. If it is an insert, the indices point to locations
in the final list where the items were added. For node changes,
the indices point to the locations of the modified nodes.

**Returns:** an array of

int

containing index locations for
the children specified by the event

- toString

```java
public
String
toString()
```

Returns a string that displays and identifies this object's
properties.

**Overrides:** toString

in class

EventObject
**Returns:** a String representation of this object

---

#### Method Detail

getTreePath

```java
public
TreePath
getTreePath()
```

For all events, except treeStructureChanged,
returns the parent of the changed nodes.
For treeStructureChanged events, returns the ancestor of the
structure that has changed. This and

getChildIndices

are used to get a list of the effected
nodes.

The one exception to this is a treeNodesChanged event that is to
identify the root, in which case this will return the root
and

getChildIndices

will return null.

**Returns:** the TreePath used in identifying the changed nodes.
**See Also:** TreePath.getLastPathComponent()

---

#### getTreePath

public

TreePath

getTreePath()

For all events, except treeStructureChanged,
returns the parent of the changed nodes.
For treeStructureChanged events, returns the ancestor of the
structure that has changed. This and

getChildIndices

are used to get a list of the effected
nodes.

The one exception to this is a treeNodesChanged event that is to
identify the root, in which case this will return the root
and

getChildIndices

will return null.

The one exception to this is a treeNodesChanged event that is to
identify the root, in which case this will return the root
and

getChildIndices

will return null.

getPath

```java
public
Object
[] getPath()
```

Convenience method to get the array of objects from the TreePath
instance that this event wraps.

**Returns:** an array of Objects, where the first Object is the one
stored at the root and the last object is the one
stored at the node identified by the path

---

#### getPath

public

Object

[] getPath()

Convenience method to get the array of objects from the TreePath
instance that this event wraps.

getChildren

```java
public
Object
[] getChildren()
```

Returns the objects that are children of the node identified by

getPath

at the locations specified by

getChildIndices

. If this is a removal event the
returned objects are no longer children of the parent node.

**Returns:** an array of Object containing the children specified by
the event
**See Also:** getPath()

,

getChildIndices()

---

#### getChildren

public

Object

[] getChildren()

Returns the objects that are children of the node identified by

getPath

at the locations specified by

getChildIndices

. If this is a removal event the
returned objects are no longer children of the parent node.

getChildIndices

```java
public int[] getChildIndices()
```

Returns the values of the child indexes. If this is a removal event
the indexes point to locations in the initial list where items
were removed. If it is an insert, the indices point to locations
in the final list where the items were added. For node changes,
the indices point to the locations of the modified nodes.

**Returns:** an array of

int

containing index locations for
the children specified by the event

---

#### getChildIndices

public int[] getChildIndices()

Returns the values of the child indexes. If this is a removal event
the indexes point to locations in the initial list where items
were removed. If it is an insert, the indices point to locations
in the final list where the items were added. For node changes,
the indices point to the locations of the modified nodes.

toString

```java
public
String
toString()
```

Returns a string that displays and identifies this object's
properties.

**Overrides:** toString

in class

EventObject
**Returns:** a String representation of this object

---

#### toString

public

String

toString()

Returns a string that displays and identifies this object's
properties.

---

