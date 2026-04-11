# Class HierarchyBoundsAdapter

**Source:** `java.desktop\java\awt\event\HierarchyBoundsAdapter.html`

### Class Description

```java
public abstract class
HierarchyBoundsAdapter

extends
Object

implements
HierarchyBoundsListener
```

An abstract adapter class for receiving ancestor moved and resized events.
The methods in this class are empty. This class exists as a
convenience for creating listener objects.

Extend this class and override the method for the event of interest. (If
you implement the

HierarchyBoundsListener

interface, you have
to define both methods in it. This abstract class defines null methods for
them both, so you only have to define the method for the event you care
about.)

Create a listener object using your class and then register it with a
Component using the Component's

addHierarchyBoundsListener

method. When the hierarchy to which the Component belongs changes by
resize or movement of an ancestor, the relevant method in the listener
object is invoked, and the

HierarchyEvent

is passed to it.

**All Implemented Interfaces:** HierarchyBoundsListener

,

EventListener

---

### Field Details

*No entries found.*

### Constructor Details

#### public HierarchyBoundsAdapter()

*No description found.*

---

### Method Details

#### public void ancestorMoved​(
HierarchyEvent
e)

Called when an ancestor of the source is moved.

**Specified by:**
- ancestorMoved

in interface

HierarchyBoundsListener

**Parameters:**
- e

- the event to be processed

---

#### public void ancestorResized​(
HierarchyEvent
e)

Called when an ancestor of the source is resized.

**Specified by:**
- ancestorResized

in interface

HierarchyBoundsListener

**Parameters:**
- e

- the event to be processed

---

### Additional Sections

#### Class HierarchyBoundsAdapter

java.lang.Object

- java.awt.event.HierarchyBoundsAdapter

java.awt.event.HierarchyBoundsAdapter

**All Implemented Interfaces:** HierarchyBoundsListener

,

EventListener

```java
public abstract class
HierarchyBoundsAdapter

extends
Object

implements
HierarchyBoundsListener
```

An abstract adapter class for receiving ancestor moved and resized events.
The methods in this class are empty. This class exists as a
convenience for creating listener objects.

Extend this class and override the method for the event of interest. (If
you implement the

HierarchyBoundsListener

interface, you have
to define both methods in it. This abstract class defines null methods for
them both, so you only have to define the method for the event you care
about.)

Create a listener object using your class and then register it with a
Component using the Component's

addHierarchyBoundsListener

method. When the hierarchy to which the Component belongs changes by
resize or movement of an ancestor, the relevant method in the listener
object is invoked, and the

HierarchyEvent

is passed to it.

**Since:** 1.3
**See Also:** HierarchyBoundsListener

,

HierarchyEvent

public abstract class

HierarchyBoundsAdapter

extends

Object

implements

HierarchyBoundsListener

An abstract adapter class for receiving ancestor moved and resized events.
The methods in this class are empty. This class exists as a
convenience for creating listener objects.

Extend this class and override the method for the event of interest. (If
you implement the

HierarchyBoundsListener

interface, you have
to define both methods in it. This abstract class defines null methods for
them both, so you only have to define the method for the event you care
about.)

Create a listener object using your class and then register it with a
Component using the Component's

addHierarchyBoundsListener

method. When the hierarchy to which the Component belongs changes by
resize or movement of an ancestor, the relevant method in the listener
object is invoked, and the

HierarchyEvent

is passed to it.

Extend this class and override the method for the event of interest. (If
you implement the

HierarchyBoundsListener

interface, you have
to define both methods in it. This abstract class defines null methods for
them both, so you only have to define the method for the event you care
about.)

Create a listener object using your class and then register it with a
Component using the Component's

addHierarchyBoundsListener

method. When the hierarchy to which the Component belongs changes by
resize or movement of an ancestor, the relevant method in the listener
object is invoked, and the

HierarchyEvent

is passed to it.

Create a listener object using your class and then register it with a
Component using the Component's

addHierarchyBoundsListener

method. When the hierarchy to which the Component belongs changes by
resize or movement of an ancestor, the relevant method in the listener
object is invoked, and the

HierarchyEvent

is passed to it.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

HierarchyBoundsAdapter

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

ancestorMoved

​(

HierarchyEvent

e)

Called when an ancestor of the source is moved.

void

ancestorResized

​(

HierarchyEvent

e)

Called when an ancestor of the source is resized.

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

Constructor Summary

Constructors

Constructor

Description

HierarchyBoundsAdapter

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

ancestorMoved

​(

HierarchyEvent

e)

Called when an ancestor of the source is moved.

void

ancestorResized

​(

HierarchyEvent

e)

Called when an ancestor of the source is resized.

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

---

#### Method Summary

Called when an ancestor of the source is moved.

Called when an ancestor of the source is resized.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- HierarchyBoundsAdapter

```java
public HierarchyBoundsAdapter()
```

============ METHOD DETAIL ==========

- Method Detail

- ancestorMoved

```java
public void ancestorMoved​(
HierarchyEvent
e)
```

Called when an ancestor of the source is moved.

**Specified by:** ancestorMoved

in interface

HierarchyBoundsListener
**Parameters:** e

- the event to be processed

- ancestorResized

```java
public void ancestorResized​(
HierarchyEvent
e)
```

Called when an ancestor of the source is resized.

**Specified by:** ancestorResized

in interface

HierarchyBoundsListener
**Parameters:** e

- the event to be processed

Constructor Detail

- HierarchyBoundsAdapter

```java
public HierarchyBoundsAdapter()
```

---

#### Constructor Detail

HierarchyBoundsAdapter

```java
public HierarchyBoundsAdapter()
```

---

#### HierarchyBoundsAdapter

public HierarchyBoundsAdapter()

Method Detail

- ancestorMoved

```java
public void ancestorMoved​(
HierarchyEvent
e)
```

Called when an ancestor of the source is moved.

**Specified by:** ancestorMoved

in interface

HierarchyBoundsListener
**Parameters:** e

- the event to be processed

- ancestorResized

```java
public void ancestorResized​(
HierarchyEvent
e)
```

Called when an ancestor of the source is resized.

**Specified by:** ancestorResized

in interface

HierarchyBoundsListener
**Parameters:** e

- the event to be processed

---

#### Method Detail

ancestorMoved

```java
public void ancestorMoved​(
HierarchyEvent
e)
```

Called when an ancestor of the source is moved.

**Specified by:** ancestorMoved

in interface

HierarchyBoundsListener
**Parameters:** e

- the event to be processed

---

#### ancestorMoved

public void ancestorMoved​(

HierarchyEvent

e)

Called when an ancestor of the source is moved.

ancestorResized

```java
public void ancestorResized​(
HierarchyEvent
e)
```

Called when an ancestor of the source is resized.

**Specified by:** ancestorResized

in interface

HierarchyBoundsListener
**Parameters:** e

- the event to be processed

---

#### ancestorResized

public void ancestorResized​(

HierarchyEvent

e)

Called when an ancestor of the source is resized.

---

