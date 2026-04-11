# Class AncestorEvent

**Source:** `java.desktop\javax\swing\event\AncestorEvent.html`

### Class Description

```java
public class
AncestorEvent

extends
AWTEvent
```

An event reported to a child component that originated from an
ancestor in the component hierarchy.

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

#### public static final int ANCESTOR_ADDED

An ancestor-component was added to the hierarchy of
visible objects (made visible), and is currently being displayed.

**See Also:**
- Constant Field Values

---

#### public static final int ANCESTOR_REMOVED

An ancestor-component was removed from the hierarchy
of visible objects (hidden) and is no longer being displayed.

**See Also:**
- Constant Field Values

---

#### public static final int ANCESTOR_MOVED

An ancestor-component changed its position on the screen.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public AncestorEvent​(
JComponent
source,
int id,

Container
ancestor,

Container
ancestorParent)

Constructs an AncestorEvent object to identify a change
in an ancestor-component's display-status.

**Parameters:**
- source

- the JComponent that originated the event
(typically

this

)
- id

- an int specifying

ANCESTOR_ADDED

,

ANCESTOR_REMOVED

or

ANCESTOR_MOVED
- ancestor

- a Container object specifying the ancestor-component
whose display-status changed
- ancestorParent

- a Container object specifying the ancestor's parent

---

### Method Details

#### public
Container
getAncestor()

Returns the ancestor that the event actually occurred on.

**Returns:**
- the

Container

object specifying the ancestor component

---

#### public
Container
getAncestorParent()

Returns the parent of the ancestor the event actually occurred on.
This is most interesting in an ANCESTOR_REMOVED event, as
the ancestor may no longer be in the component hierarchy.

**Returns:**
- the

Container

object specifying the ancestor's parent

---

#### public
JComponent
getComponent()

Returns the component that the listener was added to.

**Returns:**
- the

JComponent

on which the event occurred

---

### Additional Sections

#### Class AncestorEvent

java.lang.Object

- java.util.EventObject
- - java.awt.AWTEvent
- - javax.swing.event.AncestorEvent

java.util.EventObject

- java.awt.AWTEvent
- - javax.swing.event.AncestorEvent

java.awt.AWTEvent

- javax.swing.event.AncestorEvent

javax.swing.event.AncestorEvent

**All Implemented Interfaces:** Serializable

```java
public class
AncestorEvent

extends
AWTEvent
```

An event reported to a child component that originated from an
ancestor in the component hierarchy.

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

AncestorEvent

extends

AWTEvent

An event reported to a child component that originated from an
ancestor in the component hierarchy.

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

static int

ANCESTOR_ADDED

An ancestor-component was added to the hierarchy of
visible objects (made visible), and is currently being displayed.

static int

ANCESTOR_MOVED

An ancestor-component changed its position on the screen.

static int

ANCESTOR_REMOVED

An ancestor-component was removed from the hierarchy
of visible objects (hidden) and is no longer being displayed.

- Fields declared in class java.awt.

AWTEvent

ACTION_EVENT_MASK

,

ADJUSTMENT_EVENT_MASK

,

COMPONENT_EVENT_MASK

,

consumed

,

CONTAINER_EVENT_MASK

,

FOCUS_EVENT_MASK

,

HIERARCHY_BOUNDS_EVENT_MASK

,

HIERARCHY_EVENT_MASK

,

id

,

INPUT_METHOD_EVENT_MASK

,

INVOCATION_EVENT_MASK

,

ITEM_EVENT_MASK

,

KEY_EVENT_MASK

,

MOUSE_EVENT_MASK

,

MOUSE_MOTION_EVENT_MASK

,

MOUSE_WHEEL_EVENT_MASK

,

PAINT_EVENT_MASK

,

RESERVED_ID_MAX

,

TEXT_EVENT_MASK

,

WINDOW_EVENT_MASK

,

WINDOW_FOCUS_EVENT_MASK

,

WINDOW_STATE_EVENT_MASK

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AncestorEvent

​(

JComponent

source,
int id,

Container

ancestor,

Container

ancestorParent)

Constructs an AncestorEvent object to identify a change
in an ancestor-component's display-status.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Container

getAncestor

()

Returns the ancestor that the event actually occurred on.

Container

getAncestorParent

()

Returns the parent of the ancestor the event actually occurred on.

JComponent

getComponent

()

Returns the component that the listener was added to.

- Methods declared in class java.awt.

AWTEvent

consume

,

getID

,

isConsumed

,

paramString

,

setSource

,

toString

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

static int

ANCESTOR_ADDED

An ancestor-component was added to the hierarchy of
visible objects (made visible), and is currently being displayed.

static int

ANCESTOR_MOVED

An ancestor-component changed its position on the screen.

static int

ANCESTOR_REMOVED

An ancestor-component was removed from the hierarchy
of visible objects (hidden) and is no longer being displayed.

- Fields declared in class java.awt.

AWTEvent

ACTION_EVENT_MASK

,

ADJUSTMENT_EVENT_MASK

,

COMPONENT_EVENT_MASK

,

consumed

,

CONTAINER_EVENT_MASK

,

FOCUS_EVENT_MASK

,

HIERARCHY_BOUNDS_EVENT_MASK

,

HIERARCHY_EVENT_MASK

,

id

,

INPUT_METHOD_EVENT_MASK

,

INVOCATION_EVENT_MASK

,

ITEM_EVENT_MASK

,

KEY_EVENT_MASK

,

MOUSE_EVENT_MASK

,

MOUSE_MOTION_EVENT_MASK

,

MOUSE_WHEEL_EVENT_MASK

,

PAINT_EVENT_MASK

,

RESERVED_ID_MAX

,

TEXT_EVENT_MASK

,

WINDOW_EVENT_MASK

,

WINDOW_FOCUS_EVENT_MASK

,

WINDOW_STATE_EVENT_MASK

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

An ancestor-component was added to the hierarchy of
visible objects (made visible), and is currently being displayed.

An ancestor-component changed its position on the screen.

An ancestor-component was removed from the hierarchy
of visible objects (hidden) and is no longer being displayed.

Fields declared in class java.awt.

AWTEvent

ACTION_EVENT_MASK

,

ADJUSTMENT_EVENT_MASK

,

COMPONENT_EVENT_MASK

,

consumed

,

CONTAINER_EVENT_MASK

,

FOCUS_EVENT_MASK

,

HIERARCHY_BOUNDS_EVENT_MASK

,

HIERARCHY_EVENT_MASK

,

id

,

INPUT_METHOD_EVENT_MASK

,

INVOCATION_EVENT_MASK

,

ITEM_EVENT_MASK

,

KEY_EVENT_MASK

,

MOUSE_EVENT_MASK

,

MOUSE_MOTION_EVENT_MASK

,

MOUSE_WHEEL_EVENT_MASK

,

PAINT_EVENT_MASK

,

RESERVED_ID_MAX

,

TEXT_EVENT_MASK

,

WINDOW_EVENT_MASK

,

WINDOW_FOCUS_EVENT_MASK

,

WINDOW_STATE_EVENT_MASK

---

#### Fields declared in class java.awt. AWTEvent

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

AncestorEvent

​(

JComponent

source,
int id,

Container

ancestor,

Container

ancestorParent)

Constructs an AncestorEvent object to identify a change
in an ancestor-component's display-status.

---

#### Constructor Summary

Constructs an AncestorEvent object to identify a change
in an ancestor-component's display-status.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Container

getAncestor

()

Returns the ancestor that the event actually occurred on.

Container

getAncestorParent

()

Returns the parent of the ancestor the event actually occurred on.

JComponent

getComponent

()

Returns the component that the listener was added to.

- Methods declared in class java.awt.

AWTEvent

consume

,

getID

,

isConsumed

,

paramString

,

setSource

,

toString

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

Returns the ancestor that the event actually occurred on.

Returns the parent of the ancestor the event actually occurred on.

Returns the component that the listener was added to.

Methods declared in class java.awt.

AWTEvent

consume

,

getID

,

isConsumed

,

paramString

,

setSource

,

toString

---

#### Methods declared in class java.awt. AWTEvent

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

- ANCESTOR_ADDED

```java
public static final int ANCESTOR_ADDED
```

An ancestor-component was added to the hierarchy of
visible objects (made visible), and is currently being displayed.

**See Also:** Constant Field Values

- ANCESTOR_REMOVED

```java
public static final int ANCESTOR_REMOVED
```

An ancestor-component was removed from the hierarchy
of visible objects (hidden) and is no longer being displayed.

**See Also:** Constant Field Values

- ANCESTOR_MOVED

```java
public static final int ANCESTOR_MOVED
```

An ancestor-component changed its position on the screen.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AncestorEvent

```java
public AncestorEvent​(
JComponent
source,
int id,

Container
ancestor,

Container
ancestorParent)
```

Constructs an AncestorEvent object to identify a change
in an ancestor-component's display-status.

**Parameters:** source

- the JComponent that originated the event
(typically

this

)
**Parameters:** id

- an int specifying

ANCESTOR_ADDED

,

ANCESTOR_REMOVED

or

ANCESTOR_MOVED
**Parameters:** ancestor

- a Container object specifying the ancestor-component
whose display-status changed
**Parameters:** ancestorParent

- a Container object specifying the ancestor's parent

============ METHOD DETAIL ==========

- Method Detail

- getAncestor

```java
public
Container
getAncestor()
```

Returns the ancestor that the event actually occurred on.

**Returns:** the

Container

object specifying the ancestor component

- getAncestorParent

```java
public
Container
getAncestorParent()
```

Returns the parent of the ancestor the event actually occurred on.
This is most interesting in an ANCESTOR_REMOVED event, as
the ancestor may no longer be in the component hierarchy.

**Returns:** the

Container

object specifying the ancestor's parent

- getComponent

```java
public
JComponent
getComponent()
```

Returns the component that the listener was added to.

**Returns:** the

JComponent

on which the event occurred

Field Detail

- ANCESTOR_ADDED

```java
public static final int ANCESTOR_ADDED
```

An ancestor-component was added to the hierarchy of
visible objects (made visible), and is currently being displayed.

**See Also:** Constant Field Values

- ANCESTOR_REMOVED

```java
public static final int ANCESTOR_REMOVED
```

An ancestor-component was removed from the hierarchy
of visible objects (hidden) and is no longer being displayed.

**See Also:** Constant Field Values

- ANCESTOR_MOVED

```java
public static final int ANCESTOR_MOVED
```

An ancestor-component changed its position on the screen.

**See Also:** Constant Field Values

---

#### Field Detail

ANCESTOR_ADDED

```java
public static final int ANCESTOR_ADDED
```

An ancestor-component was added to the hierarchy of
visible objects (made visible), and is currently being displayed.

**See Also:** Constant Field Values

---

#### ANCESTOR_ADDED

public static final int ANCESTOR_ADDED

An ancestor-component was added to the hierarchy of
visible objects (made visible), and is currently being displayed.

ANCESTOR_REMOVED

```java
public static final int ANCESTOR_REMOVED
```

An ancestor-component was removed from the hierarchy
of visible objects (hidden) and is no longer being displayed.

**See Also:** Constant Field Values

---

#### ANCESTOR_REMOVED

public static final int ANCESTOR_REMOVED

An ancestor-component was removed from the hierarchy
of visible objects (hidden) and is no longer being displayed.

ANCESTOR_MOVED

```java
public static final int ANCESTOR_MOVED
```

An ancestor-component changed its position on the screen.

**See Also:** Constant Field Values

---

#### ANCESTOR_MOVED

public static final int ANCESTOR_MOVED

An ancestor-component changed its position on the screen.

Constructor Detail

- AncestorEvent

```java
public AncestorEvent​(
JComponent
source,
int id,

Container
ancestor,

Container
ancestorParent)
```

Constructs an AncestorEvent object to identify a change
in an ancestor-component's display-status.

**Parameters:** source

- the JComponent that originated the event
(typically

this

)
**Parameters:** id

- an int specifying

ANCESTOR_ADDED

,

ANCESTOR_REMOVED

or

ANCESTOR_MOVED
**Parameters:** ancestor

- a Container object specifying the ancestor-component
whose display-status changed
**Parameters:** ancestorParent

- a Container object specifying the ancestor's parent

---

#### Constructor Detail

AncestorEvent

```java
public AncestorEvent​(
JComponent
source,
int id,

Container
ancestor,

Container
ancestorParent)
```

Constructs an AncestorEvent object to identify a change
in an ancestor-component's display-status.

**Parameters:** source

- the JComponent that originated the event
(typically

this

)
**Parameters:** id

- an int specifying

ANCESTOR_ADDED

,

ANCESTOR_REMOVED

or

ANCESTOR_MOVED
**Parameters:** ancestor

- a Container object specifying the ancestor-component
whose display-status changed
**Parameters:** ancestorParent

- a Container object specifying the ancestor's parent

---

#### AncestorEvent

public AncestorEvent​(

JComponent

source,
int id,

Container

ancestor,

Container

ancestorParent)

Constructs an AncestorEvent object to identify a change
in an ancestor-component's display-status.

Method Detail

- getAncestor

```java
public
Container
getAncestor()
```

Returns the ancestor that the event actually occurred on.

**Returns:** the

Container

object specifying the ancestor component

- getAncestorParent

```java
public
Container
getAncestorParent()
```

Returns the parent of the ancestor the event actually occurred on.
This is most interesting in an ANCESTOR_REMOVED event, as
the ancestor may no longer be in the component hierarchy.

**Returns:** the

Container

object specifying the ancestor's parent

- getComponent

```java
public
JComponent
getComponent()
```

Returns the component that the listener was added to.

**Returns:** the

JComponent

on which the event occurred

---

#### Method Detail

getAncestor

```java
public
Container
getAncestor()
```

Returns the ancestor that the event actually occurred on.

**Returns:** the

Container

object specifying the ancestor component

---

#### getAncestor

public

Container

getAncestor()

Returns the ancestor that the event actually occurred on.

getAncestorParent

```java
public
Container
getAncestorParent()
```

Returns the parent of the ancestor the event actually occurred on.
This is most interesting in an ANCESTOR_REMOVED event, as
the ancestor may no longer be in the component hierarchy.

**Returns:** the

Container

object specifying the ancestor's parent

---

#### getAncestorParent

public

Container

getAncestorParent()

Returns the parent of the ancestor the event actually occurred on.
This is most interesting in an ANCESTOR_REMOVED event, as
the ancestor may no longer be in the component hierarchy.

getComponent

```java
public
JComponent
getComponent()
```

Returns the component that the listener was added to.

**Returns:** the

JComponent

on which the event occurred

---

#### getComponent

public

JComponent

getComponent()

Returns the component that the listener was added to.

---

