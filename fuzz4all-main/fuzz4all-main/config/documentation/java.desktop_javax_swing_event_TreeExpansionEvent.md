# Class TreeExpansionEvent

**Source:** `java.desktop\javax\swing\event\TreeExpansionEvent.html`

### Class Description

```java
public class
TreeExpansionEvent

extends
EventObject
```

An event used to identify a single path in a tree. The source
returned by

getSource

will be an instance of JTree.

For further documentation and examples see
the following sections in

The Java Tutorial

:

How to Write a Tree Expansion Listener

and

How to Write a Tree-Will-Expand Listener

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

**All Implemented Interfaces:** Serializable

---

### Field Details

#### protected
TreePath
path

Path to the value this event represents.

---

### Constructor Details

#### public TreeExpansionEvent​(
Object
source,

TreePath
path)

Constructs a TreeExpansionEvent object.

**Parameters:**
- source

- the Object that originated the event
(typically

this

)
- path

- a TreePath object identifying the newly expanded
node

---

### Method Details

#### public
TreePath
getPath()

Returns the path to the value that has been expanded/collapsed.

**Returns:**
- this event's

TreePath

object

---

### Additional Sections

#### Class TreeExpansionEvent

java.lang.Object

- java.util.EventObject
- - javax.swing.event.TreeExpansionEvent

java.util.EventObject

- javax.swing.event.TreeExpansionEvent

javax.swing.event.TreeExpansionEvent

**All Implemented Interfaces:** Serializable

```java
public class
TreeExpansionEvent

extends
EventObject
```

An event used to identify a single path in a tree. The source
returned by

getSource

will be an instance of JTree.

For further documentation and examples see
the following sections in

The Java Tutorial

:

How to Write a Tree Expansion Listener

and

How to Write a Tree-Will-Expand Listener

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

**See Also:** Serialized Form

public class

TreeExpansionEvent

extends

EventObject

An event used to identify a single path in a tree. The source
returned by

getSource

will be an instance of JTree.

For further documentation and examples see
the following sections in

The Java Tutorial

:

How to Write a Tree Expansion Listener

and

How to Write a Tree-Will-Expand Listener

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

For further documentation and examples see
the following sections in

The Java Tutorial

:

How to Write a Tree Expansion Listener

and

How to Write a Tree-Will-Expand Listener

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

TreePath

path

Path to the value this event represents.

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TreeExpansionEvent

​(

Object

source,

TreePath

path)

Constructs a TreeExpansionEvent object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

TreePath

getPath

()

Returns the path to the value that has been expanded/collapsed.

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

protected

TreePath

path

Path to the value this event represents.

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

Path to the value this event represents.

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

TreeExpansionEvent

​(

Object

source,

TreePath

path)

Constructs a TreeExpansionEvent object.

---

#### Constructor Summary

Constructs a TreeExpansionEvent object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

TreePath

getPath

()

Returns the path to the value that has been expanded/collapsed.

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

Returns the path to the value that has been expanded/collapsed.

Methods declared in class java.util.

EventObject

getSource

,

toString

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

Path to the value this event represents.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TreeExpansionEvent

```java
public TreeExpansionEvent​(
Object
source,

TreePath
path)
```

Constructs a TreeExpansionEvent object.

**Parameters:** source

- the Object that originated the event
(typically

this

)
**Parameters:** path

- a TreePath object identifying the newly expanded
node

============ METHOD DETAIL ==========

- Method Detail

- getPath

```java
public
TreePath
getPath()
```

Returns the path to the value that has been expanded/collapsed.

**Returns:** this event's

TreePath

object

Field Detail

- path

```java
protected
TreePath
path
```

Path to the value this event represents.

---

#### Field Detail

path

```java
protected
TreePath
path
```

Path to the value this event represents.

---

#### path

protected

TreePath

path

Path to the value this event represents.

Constructor Detail

- TreeExpansionEvent

```java
public TreeExpansionEvent​(
Object
source,

TreePath
path)
```

Constructs a TreeExpansionEvent object.

**Parameters:** source

- the Object that originated the event
(typically

this

)
**Parameters:** path

- a TreePath object identifying the newly expanded
node

---

#### Constructor Detail

TreeExpansionEvent

```java
public TreeExpansionEvent​(
Object
source,

TreePath
path)
```

Constructs a TreeExpansionEvent object.

**Parameters:** source

- the Object that originated the event
(typically

this

)
**Parameters:** path

- a TreePath object identifying the newly expanded
node

---

#### TreeExpansionEvent

public TreeExpansionEvent​(

Object

source,

TreePath

path)

Constructs a TreeExpansionEvent object.

Method Detail

- getPath

```java
public
TreePath
getPath()
```

Returns the path to the value that has been expanded/collapsed.

**Returns:** this event's

TreePath

object

---

#### Method Detail

getPath

```java
public
TreePath
getPath()
```

Returns the path to the value that has been expanded/collapsed.

**Returns:** this event's

TreePath

object

---

#### getPath

public

TreePath

getPath()

Returns the path to the value that has been expanded/collapsed.

---

