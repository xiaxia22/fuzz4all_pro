# Class NodeChangeEvent

**Source:** `java.prefs\java\util\prefs\NodeChangeEvent.html`

### Class Description

```java
public class
NodeChangeEvent

extends
EventObject
```

An event emitted by a

Preferences

node to indicate that
a child of that node has been added or removed.

Note, that although NodeChangeEvent inherits Serializable interface from
java.util.EventObject, it is not intended to be Serializable. Appropriate
serialization methods are implemented to throw NotSerializableException.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public NodeChangeEvent​(
Preferences
parent,

Preferences
child)

Constructs a new

NodeChangeEvent

instance.

**Parameters:**
- parent

- The parent of the node that was added or removed.
- child

- The node that was added or removed.

---

### Method Details

#### public
Preferences
getParent()

Returns the parent of the node that was added or removed.

**Returns:**
- The parent Preferences node whose child was added or removed

---

#### public
Preferences
getChild()

Returns the node that was added or removed.

**Returns:**
- The node that was added or removed.

---

### Additional Sections

#### Class NodeChangeEvent

java.lang.Object

- java.util.EventObject
- - java.util.prefs.NodeChangeEvent

java.util.EventObject

- java.util.prefs.NodeChangeEvent

java.util.prefs.NodeChangeEvent

**All Implemented Interfaces:** Serializable

```java
public class
NodeChangeEvent

extends
EventObject
```

An event emitted by a

Preferences

node to indicate that
a child of that node has been added or removed.

Note, that although NodeChangeEvent inherits Serializable interface from
java.util.EventObject, it is not intended to be Serializable. Appropriate
serialization methods are implemented to throw NotSerializableException.

**Since:** 1.4
**See Also:** Preferences

,

NodeChangeListener

,

PreferenceChangeEvent

public class

NodeChangeEvent

extends

EventObject

An event emitted by a

Preferences

node to indicate that
a child of that node has been added or removed.

Note, that although NodeChangeEvent inherits Serializable interface from
java.util.EventObject, it is not intended to be Serializable. Appropriate
serialization methods are implemented to throw NotSerializableException.

Note, that although NodeChangeEvent inherits Serializable interface from
java.util.EventObject, it is not intended to be Serializable. Appropriate
serialization methods are implemented to throw NotSerializableException.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

NodeChangeEvent

​(

Preferences

parent,

Preferences

child)

Constructs a new

NodeChangeEvent

instance.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Preferences

getChild

()

Returns the node that was added or removed.

Preferences

getParent

()

Returns the parent of the node that was added or removed.

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

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

NodeChangeEvent

​(

Preferences

parent,

Preferences

child)

Constructs a new

NodeChangeEvent

instance.

---

#### Constructor Summary

Constructs a new

NodeChangeEvent

instance.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Preferences

getChild

()

Returns the node that was added or removed.

Preferences

getParent

()

Returns the parent of the node that was added or removed.

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

Returns the node that was added or removed.

Returns the parent of the node that was added or removed.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- NodeChangeEvent

```java
public NodeChangeEvent​(
Preferences
parent,

Preferences
child)
```

Constructs a new

NodeChangeEvent

instance.

**Parameters:** parent

- The parent of the node that was added or removed.
**Parameters:** child

- The node that was added or removed.

============ METHOD DETAIL ==========

- Method Detail

- getParent

```java
public
Preferences
getParent()
```

Returns the parent of the node that was added or removed.

**Returns:** The parent Preferences node whose child was added or removed

- getChild

```java
public
Preferences
getChild()
```

Returns the node that was added or removed.

**Returns:** The node that was added or removed.

Constructor Detail

- NodeChangeEvent

```java
public NodeChangeEvent​(
Preferences
parent,

Preferences
child)
```

Constructs a new

NodeChangeEvent

instance.

**Parameters:** parent

- The parent of the node that was added or removed.
**Parameters:** child

- The node that was added or removed.

---

#### Constructor Detail

NodeChangeEvent

```java
public NodeChangeEvent​(
Preferences
parent,

Preferences
child)
```

Constructs a new

NodeChangeEvent

instance.

**Parameters:** parent

- The parent of the node that was added or removed.
**Parameters:** child

- The node that was added or removed.

---

#### NodeChangeEvent

public NodeChangeEvent​(

Preferences

parent,

Preferences

child)

Constructs a new

NodeChangeEvent

instance.

Method Detail

- getParent

```java
public
Preferences
getParent()
```

Returns the parent of the node that was added or removed.

**Returns:** The parent Preferences node whose child was added or removed

- getChild

```java
public
Preferences
getChild()
```

Returns the node that was added or removed.

**Returns:** The node that was added or removed.

---

#### Method Detail

getParent

```java
public
Preferences
getParent()
```

Returns the parent of the node that was added or removed.

**Returns:** The parent Preferences node whose child was added or removed

---

#### getParent

public

Preferences

getParent()

Returns the parent of the node that was added or removed.

getChild

```java
public
Preferences
getChild()
```

Returns the node that was added or removed.

**Returns:** The node that was added or removed.

---

#### getChild

public

Preferences

getChild()

Returns the node that was added or removed.

---

