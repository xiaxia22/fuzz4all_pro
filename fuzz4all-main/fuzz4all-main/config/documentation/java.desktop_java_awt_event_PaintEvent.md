# Class PaintEvent

**Source:** `java.desktop\java\awt\event\PaintEvent.html`

### Class Description

```java
public class
PaintEvent

extends
ComponentEvent
```

The component-level paint event.
This event is a special type which is used to ensure that
paint/update method calls are serialized along with the other
events delivered from the event queue. This event is not
designed to be used with the Event Listener model; programs
should continue to override paint/update methods in order
render themselves properly.

An unspecified behavior will be caused if the

id

parameter
of any particular

PaintEvent

instance is not
in the range from

PAINT_FIRST

to

PAINT_LAST

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final int PAINT_FIRST

Marks the first integer id for the range of paint event ids.

**See Also:**
- Constant Field Values

---

#### public static final int PAINT_LAST

Marks the last integer id for the range of paint event ids.

**See Also:**
- Constant Field Values

---

#### public static final int PAINT

The paint event type.

**See Also:**
- Constant Field Values

---

#### public static final int UPDATE

The update event type.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public PaintEvent​(
Component
source,
int id,

Rectangle
updateRect)

Constructs a

PaintEvent

object with the specified
source component and type.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:**
- source

- The object where the event originated
- id

- The integer that identifies the event type.
For information on allowable values, see
the class description for

PaintEvent
- updateRect

- The rectangle area which needs to be repainted

**Throws:**
- IllegalArgumentException

- if

source

is null

**See Also:**
- EventObject.getSource()

,

AWTEvent.getID()

,

getUpdateRect()

---

### Method Details

#### public
Rectangle
getUpdateRect()

Returns the rectangle representing the area which needs to be
repainted in response to this event.

**Returns:**
- the rectangle representing the area which needs to be
repainted in response to this event

---

#### public void setUpdateRect​(
Rectangle
updateRect)

Sets the rectangle representing the area which needs to be
repainted in response to this event.

**Parameters:**
- updateRect

- the rectangle area which needs to be repainted

---

### Additional Sections

#### Class PaintEvent

java.lang.Object

- java.util.EventObject
- - java.awt.AWTEvent
- - java.awt.event.ComponentEvent
- - java.awt.event.PaintEvent

java.util.EventObject

- java.awt.AWTEvent
- - java.awt.event.ComponentEvent
- - java.awt.event.PaintEvent

java.awt.AWTEvent

- java.awt.event.ComponentEvent
- - java.awt.event.PaintEvent

java.awt.event.ComponentEvent

- java.awt.event.PaintEvent

java.awt.event.PaintEvent

**All Implemented Interfaces:** Serializable

```java
public class
PaintEvent

extends
ComponentEvent
```

The component-level paint event.
This event is a special type which is used to ensure that
paint/update method calls are serialized along with the other
events delivered from the event queue. This event is not
designed to be used with the Event Listener model; programs
should continue to override paint/update methods in order
render themselves properly.

An unspecified behavior will be caused if the

id

parameter
of any particular

PaintEvent

instance is not
in the range from

PAINT_FIRST

to

PAINT_LAST

.

**Since:** 1.1
**See Also:** Serialized Form

public class

PaintEvent

extends

ComponentEvent

The component-level paint event.
This event is a special type which is used to ensure that
paint/update method calls are serialized along with the other
events delivered from the event queue. This event is not
designed to be used with the Event Listener model; programs
should continue to override paint/update methods in order
render themselves properly.

An unspecified behavior will be caused if the

id

parameter
of any particular

PaintEvent

instance is not
in the range from

PAINT_FIRST

to

PAINT_LAST

.

An unspecified behavior will be caused if the

id

parameter
of any particular

PaintEvent

instance is not
in the range from

PAINT_FIRST

to

PAINT_LAST

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

PAINT

The paint event type.

static int

PAINT_FIRST

Marks the first integer id for the range of paint event ids.

static int

PAINT_LAST

Marks the last integer id for the range of paint event ids.

static int

UPDATE

The update event type.

- Fields declared in class java.awt.event.

ComponentEvent

COMPONENT_FIRST

,

COMPONENT_HIDDEN

,

COMPONENT_LAST

,

COMPONENT_MOVED

,

COMPONENT_RESIZED

,

COMPONENT_SHOWN

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

PaintEvent

​(

Component

source,
int id,

Rectangle

updateRect)

Constructs a

PaintEvent

object with the specified
source component and type.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Rectangle

getUpdateRect

()

Returns the rectangle representing the area which needs to be
repainted in response to this event.

void

setUpdateRect

​(

Rectangle

updateRect)

Sets the rectangle representing the area which needs to be
repainted in response to this event.

- Methods declared in class java.awt.event.

ComponentEvent

getComponent

,

paramString

- Methods declared in class java.awt.

AWTEvent

consume

,

getID

,

isConsumed

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

PAINT

The paint event type.

static int

PAINT_FIRST

Marks the first integer id for the range of paint event ids.

static int

PAINT_LAST

Marks the last integer id for the range of paint event ids.

static int

UPDATE

The update event type.

- Fields declared in class java.awt.event.

ComponentEvent

COMPONENT_FIRST

,

COMPONENT_HIDDEN

,

COMPONENT_LAST

,

COMPONENT_MOVED

,

COMPONENT_RESIZED

,

COMPONENT_SHOWN

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

The paint event type.

Marks the first integer id for the range of paint event ids.

Marks the last integer id for the range of paint event ids.

The update event type.

Fields declared in class java.awt.event.

ComponentEvent

COMPONENT_FIRST

,

COMPONENT_HIDDEN

,

COMPONENT_LAST

,

COMPONENT_MOVED

,

COMPONENT_RESIZED

,

COMPONENT_SHOWN

---

#### Fields declared in class java.awt.event. ComponentEvent

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

PaintEvent

​(

Component

source,
int id,

Rectangle

updateRect)

Constructs a

PaintEvent

object with the specified
source component and type.

---

#### Constructor Summary

Constructs a

PaintEvent

object with the specified
source component and type.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Rectangle

getUpdateRect

()

Returns the rectangle representing the area which needs to be
repainted in response to this event.

void

setUpdateRect

​(

Rectangle

updateRect)

Sets the rectangle representing the area which needs to be
repainted in response to this event.

- Methods declared in class java.awt.event.

ComponentEvent

getComponent

,

paramString

- Methods declared in class java.awt.

AWTEvent

consume

,

getID

,

isConsumed

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

Returns the rectangle representing the area which needs to be
repainted in response to this event.

Sets the rectangle representing the area which needs to be
repainted in response to this event.

Methods declared in class java.awt.event.

ComponentEvent

getComponent

,

paramString

---

#### Methods declared in class java.awt.event. ComponentEvent

Methods declared in class java.awt.

AWTEvent

consume

,

getID

,

isConsumed

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

- PAINT_FIRST

```java
public static final int PAINT_FIRST
```

Marks the first integer id for the range of paint event ids.

**See Also:** Constant Field Values

- PAINT_LAST

```java
public static final int PAINT_LAST
```

Marks the last integer id for the range of paint event ids.

**See Also:** Constant Field Values

- PAINT

```java
public static final int PAINT
```

The paint event type.

**See Also:** Constant Field Values

- UPDATE

```java
public static final int UPDATE
```

The update event type.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- PaintEvent

```java
public PaintEvent​(
Component
source,
int id,

Rectangle
updateRect)
```

Constructs a

PaintEvent

object with the specified
source component and type.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- The object where the event originated
**Parameters:** id

- The integer that identifies the event type.
For information on allowable values, see
the class description for

PaintEvent
**Parameters:** updateRect

- The rectangle area which needs to be repainted
**Throws:** IllegalArgumentException

- if

source

is null
**See Also:** EventObject.getSource()

,

AWTEvent.getID()

,

getUpdateRect()

============ METHOD DETAIL ==========

- Method Detail

- getUpdateRect

```java
public
Rectangle
getUpdateRect()
```

Returns the rectangle representing the area which needs to be
repainted in response to this event.

**Returns:** the rectangle representing the area which needs to be
repainted in response to this event

- setUpdateRect

```java
public void setUpdateRect​(
Rectangle
updateRect)
```

Sets the rectangle representing the area which needs to be
repainted in response to this event.

**Parameters:** updateRect

- the rectangle area which needs to be repainted

Field Detail

- PAINT_FIRST

```java
public static final int PAINT_FIRST
```

Marks the first integer id for the range of paint event ids.

**See Also:** Constant Field Values

- PAINT_LAST

```java
public static final int PAINT_LAST
```

Marks the last integer id for the range of paint event ids.

**See Also:** Constant Field Values

- PAINT

```java
public static final int PAINT
```

The paint event type.

**See Also:** Constant Field Values

- UPDATE

```java
public static final int UPDATE
```

The update event type.

**See Also:** Constant Field Values

---

#### Field Detail

PAINT_FIRST

```java
public static final int PAINT_FIRST
```

Marks the first integer id for the range of paint event ids.

**See Also:** Constant Field Values

---

#### PAINT_FIRST

public static final int PAINT_FIRST

Marks the first integer id for the range of paint event ids.

PAINT_LAST

```java
public static final int PAINT_LAST
```

Marks the last integer id for the range of paint event ids.

**See Also:** Constant Field Values

---

#### PAINT_LAST

public static final int PAINT_LAST

Marks the last integer id for the range of paint event ids.

PAINT

```java
public static final int PAINT
```

The paint event type.

**See Also:** Constant Field Values

---

#### PAINT

public static final int PAINT

The paint event type.

UPDATE

```java
public static final int UPDATE
```

The update event type.

**See Also:** Constant Field Values

---

#### UPDATE

public static final int UPDATE

The update event type.

Constructor Detail

- PaintEvent

```java
public PaintEvent​(
Component
source,
int id,

Rectangle
updateRect)
```

Constructs a

PaintEvent

object with the specified
source component and type.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- The object where the event originated
**Parameters:** id

- The integer that identifies the event type.
For information on allowable values, see
the class description for

PaintEvent
**Parameters:** updateRect

- The rectangle area which needs to be repainted
**Throws:** IllegalArgumentException

- if

source

is null
**See Also:** EventObject.getSource()

,

AWTEvent.getID()

,

getUpdateRect()

---

#### Constructor Detail

PaintEvent

```java
public PaintEvent​(
Component
source,
int id,

Rectangle
updateRect)
```

Constructs a

PaintEvent

object with the specified
source component and type.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- The object where the event originated
**Parameters:** id

- The integer that identifies the event type.
For information on allowable values, see
the class description for

PaintEvent
**Parameters:** updateRect

- The rectangle area which needs to be repainted
**Throws:** IllegalArgumentException

- if

source

is null
**See Also:** EventObject.getSource()

,

AWTEvent.getID()

,

getUpdateRect()

---

#### PaintEvent

public PaintEvent​(

Component

source,
int id,

Rectangle

updateRect)

Constructs a

PaintEvent

object with the specified
source component and type.

This method throws an

IllegalArgumentException

if

source

is

null

.

This method throws an

IllegalArgumentException

if

source

is

null

.

Method Detail

- getUpdateRect

```java
public
Rectangle
getUpdateRect()
```

Returns the rectangle representing the area which needs to be
repainted in response to this event.

**Returns:** the rectangle representing the area which needs to be
repainted in response to this event

- setUpdateRect

```java
public void setUpdateRect​(
Rectangle
updateRect)
```

Sets the rectangle representing the area which needs to be
repainted in response to this event.

**Parameters:** updateRect

- the rectangle area which needs to be repainted

---

#### Method Detail

getUpdateRect

```java
public
Rectangle
getUpdateRect()
```

Returns the rectangle representing the area which needs to be
repainted in response to this event.

**Returns:** the rectangle representing the area which needs to be
repainted in response to this event

---

#### getUpdateRect

public

Rectangle

getUpdateRect()

Returns the rectangle representing the area which needs to be
repainted in response to this event.

setUpdateRect

```java
public void setUpdateRect​(
Rectangle
updateRect)
```

Sets the rectangle representing the area which needs to be
repainted in response to this event.

**Parameters:** updateRect

- the rectangle area which needs to be repainted

---

#### setUpdateRect

public void setUpdateRect​(

Rectangle

updateRect)

Sets the rectangle representing the area which needs to be
repainted in response to this event.

---

