# Class InternalFrameEvent

**Source:** `java.desktop\javax\swing\event\InternalFrameEvent.html`

### Class Description

```java
public class
InternalFrameEvent

extends
AWTEvent
```

An

AWTEvent

that adds support for

JInternalFrame

objects as the event source. This class has the
same event types as

WindowEvent

,
although different IDs are used.
Help on handling internal frame events
is in

How to Write an Internal Frame Listener

,
a section in

The Java Tutorial

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

#### public static final int INTERNAL_FRAME_FIRST

The first number in the range of IDs used for internal frame events.

**See Also:**
- Constant Field Values

---

#### public static final int INTERNAL_FRAME_LAST

The last number in the range of IDs used for internal frame events.

**See Also:**
- Constant Field Values

---

#### public static final int INTERNAL_FRAME_OPENED

The "window opened" event. This event is delivered only
the first time the internal frame is made visible.

**See Also:**
- JInternalFrame.show()

,

Constant Field Values

---

#### public static final int INTERNAL_FRAME_CLOSING

The "window is closing" event. This event is delivered when
the user attempts to close the internal frame, such as by
clicking the internal frame's close button,
or when a program attempts to close the internal frame
by invoking the

setClosed

method.

**See Also:**
- JInternalFrame.setDefaultCloseOperation(int)

,

JInternalFrame.doDefaultCloseAction()

,

JInternalFrame.setClosed(boolean)

,

Constant Field Values

---

#### public static final int INTERNAL_FRAME_CLOSED

The "window closed" event. This event is delivered after
the internal frame has been closed as the result of a call to
the

setClosed

or

dispose

method.

**See Also:**
- JInternalFrame.setClosed(boolean)

,

JInternalFrame.dispose()

,

Constant Field Values

---

#### public static final int INTERNAL_FRAME_ICONIFIED

The "window iconified" event.
This event indicates that the internal frame
was shrunk down to a small icon.

**See Also:**
- JInternalFrame.setIcon(boolean)

,

Constant Field Values

---

#### public static final int INTERNAL_FRAME_DEICONIFIED

The "window deiconified" event type. This event indicates that the
internal frame has been restored to its normal size.

**See Also:**
- JInternalFrame.setIcon(boolean)

,

Constant Field Values

---

#### public static final int INTERNAL_FRAME_ACTIVATED

The "window activated" event type. This event indicates that keystrokes
and mouse clicks are directed towards this internal frame.

**See Also:**
- JInternalFrame.show()

,

JInternalFrame.setSelected(boolean)

,

Constant Field Values

---

#### public static final int INTERNAL_FRAME_DEACTIVATED

The "window deactivated" event type. This event indicates that keystrokes
and mouse clicks are no longer directed to the internal frame.

**See Also:**
- JInternalFrame.setSelected(boolean)

,

Constant Field Values

---

### Constructor Details

#### public InternalFrameEvent​(
JInternalFrame
source,
int id)

Constructs an

InternalFrameEvent

object.

**Parameters:**
- source

- the

JInternalFrame

object that originated the event
- id

- an integer indicating the type of event

---

### Method Details

#### public
String
paramString()

Returns a parameter string identifying this event.
This method is useful for event logging and for debugging.

**Overrides:**
- paramString

in class

AWTEvent

**Returns:**
- a string identifying the event and its attributes

---

#### public
JInternalFrame
getInternalFrame()

Returns the originator of the event.

**Returns:**
- the

JInternalFrame

object that originated the event

**Since:**
- 1.3

---

### Additional Sections

#### Class InternalFrameEvent

java.lang.Object

- java.util.EventObject
- - java.awt.AWTEvent
- - javax.swing.event.InternalFrameEvent

java.util.EventObject

- java.awt.AWTEvent
- - javax.swing.event.InternalFrameEvent

java.awt.AWTEvent

- javax.swing.event.InternalFrameEvent

javax.swing.event.InternalFrameEvent

**All Implemented Interfaces:** Serializable

```java
public class
InternalFrameEvent

extends
AWTEvent
```

An

AWTEvent

that adds support for

JInternalFrame

objects as the event source. This class has the
same event types as

WindowEvent

,
although different IDs are used.
Help on handling internal frame events
is in

How to Write an Internal Frame Listener

,
a section in

The Java Tutorial

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

**See Also:** WindowEvent

,

WindowListener

,

JInternalFrame

,

InternalFrameListener

,

Serialized Form

public class

InternalFrameEvent

extends

AWTEvent

An

AWTEvent

that adds support for

JInternalFrame

objects as the event source. This class has the
same event types as

WindowEvent

,
although different IDs are used.
Help on handling internal frame events
is in

How to Write an Internal Frame Listener

,
a section in

The Java Tutorial

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

static int

INTERNAL_FRAME_ACTIVATED

The "window activated" event type.

static int

INTERNAL_FRAME_CLOSED

The "window closed" event.

static int

INTERNAL_FRAME_CLOSING

The "window is closing" event.

static int

INTERNAL_FRAME_DEACTIVATED

The "window deactivated" event type.

static int

INTERNAL_FRAME_DEICONIFIED

The "window deiconified" event type.

static int

INTERNAL_FRAME_FIRST

The first number in the range of IDs used for internal frame events.

static int

INTERNAL_FRAME_ICONIFIED

The "window iconified" event.

static int

INTERNAL_FRAME_LAST

The last number in the range of IDs used for internal frame events.

static int

INTERNAL_FRAME_OPENED

The "window opened" event.

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

InternalFrameEvent

​(

JInternalFrame

source,
int id)

Constructs an

InternalFrameEvent

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JInternalFrame

getInternalFrame

()

Returns the originator of the event.

String

paramString

()

Returns a parameter string identifying this event.

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

INTERNAL_FRAME_ACTIVATED

The "window activated" event type.

static int

INTERNAL_FRAME_CLOSED

The "window closed" event.

static int

INTERNAL_FRAME_CLOSING

The "window is closing" event.

static int

INTERNAL_FRAME_DEACTIVATED

The "window deactivated" event type.

static int

INTERNAL_FRAME_DEICONIFIED

The "window deiconified" event type.

static int

INTERNAL_FRAME_FIRST

The first number in the range of IDs used for internal frame events.

static int

INTERNAL_FRAME_ICONIFIED

The "window iconified" event.

static int

INTERNAL_FRAME_LAST

The last number in the range of IDs used for internal frame events.

static int

INTERNAL_FRAME_OPENED

The "window opened" event.

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

The "window activated" event type.

The "window closed" event.

The "window is closing" event.

The "window deactivated" event type.

The "window deiconified" event type.

The first number in the range of IDs used for internal frame events.

The "window iconified" event.

The last number in the range of IDs used for internal frame events.

The "window opened" event.

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

InternalFrameEvent

​(

JInternalFrame

source,
int id)

Constructs an

InternalFrameEvent

object.

---

#### Constructor Summary

Constructs an

InternalFrameEvent

object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JInternalFrame

getInternalFrame

()

Returns the originator of the event.

String

paramString

()

Returns a parameter string identifying this event.

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

Returns the originator of the event.

Returns a parameter string identifying this event.

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

- INTERNAL_FRAME_FIRST

```java
public static final int INTERNAL_FRAME_FIRST
```

The first number in the range of IDs used for internal frame events.

**See Also:** Constant Field Values

- INTERNAL_FRAME_LAST

```java
public static final int INTERNAL_FRAME_LAST
```

The last number in the range of IDs used for internal frame events.

**See Also:** Constant Field Values

- INTERNAL_FRAME_OPENED

```java
public static final int INTERNAL_FRAME_OPENED
```

The "window opened" event. This event is delivered only
the first time the internal frame is made visible.

**See Also:** JInternalFrame.show()

,

Constant Field Values

- INTERNAL_FRAME_CLOSING

```java
public static final int INTERNAL_FRAME_CLOSING
```

The "window is closing" event. This event is delivered when
the user attempts to close the internal frame, such as by
clicking the internal frame's close button,
or when a program attempts to close the internal frame
by invoking the

setClosed

method.

**See Also:** JInternalFrame.setDefaultCloseOperation(int)

,

JInternalFrame.doDefaultCloseAction()

,

JInternalFrame.setClosed(boolean)

,

Constant Field Values

- INTERNAL_FRAME_CLOSED

```java
public static final int INTERNAL_FRAME_CLOSED
```

The "window closed" event. This event is delivered after
the internal frame has been closed as the result of a call to
the

setClosed

or

dispose

method.

**See Also:** JInternalFrame.setClosed(boolean)

,

JInternalFrame.dispose()

,

Constant Field Values

- INTERNAL_FRAME_ICONIFIED

```java
public static final int INTERNAL_FRAME_ICONIFIED
```

The "window iconified" event.
This event indicates that the internal frame
was shrunk down to a small icon.

**See Also:** JInternalFrame.setIcon(boolean)

,

Constant Field Values

- INTERNAL_FRAME_DEICONIFIED

```java
public static final int INTERNAL_FRAME_DEICONIFIED
```

The "window deiconified" event type. This event indicates that the
internal frame has been restored to its normal size.

**See Also:** JInternalFrame.setIcon(boolean)

,

Constant Field Values

- INTERNAL_FRAME_ACTIVATED

```java
public static final int INTERNAL_FRAME_ACTIVATED
```

The "window activated" event type. This event indicates that keystrokes
and mouse clicks are directed towards this internal frame.

**See Also:** JInternalFrame.show()

,

JInternalFrame.setSelected(boolean)

,

Constant Field Values

- INTERNAL_FRAME_DEACTIVATED

```java
public static final int INTERNAL_FRAME_DEACTIVATED
```

The "window deactivated" event type. This event indicates that keystrokes
and mouse clicks are no longer directed to the internal frame.

**See Also:** JInternalFrame.setSelected(boolean)

,

Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- InternalFrameEvent

```java
public InternalFrameEvent​(
JInternalFrame
source,
int id)
```

Constructs an

InternalFrameEvent

object.

**Parameters:** source

- the

JInternalFrame

object that originated the event
**Parameters:** id

- an integer indicating the type of event

============ METHOD DETAIL ==========

- Method Detail

- paramString

```java
public
String
paramString()
```

Returns a parameter string identifying this event.
This method is useful for event logging and for debugging.

**Overrides:** paramString

in class

AWTEvent
**Returns:** a string identifying the event and its attributes

- getInternalFrame

```java
public
JInternalFrame
getInternalFrame()
```

Returns the originator of the event.

**Returns:** the

JInternalFrame

object that originated the event
**Since:** 1.3

Field Detail

- INTERNAL_FRAME_FIRST

```java
public static final int INTERNAL_FRAME_FIRST
```

The first number in the range of IDs used for internal frame events.

**See Also:** Constant Field Values

- INTERNAL_FRAME_LAST

```java
public static final int INTERNAL_FRAME_LAST
```

The last number in the range of IDs used for internal frame events.

**See Also:** Constant Field Values

- INTERNAL_FRAME_OPENED

```java
public static final int INTERNAL_FRAME_OPENED
```

The "window opened" event. This event is delivered only
the first time the internal frame is made visible.

**See Also:** JInternalFrame.show()

,

Constant Field Values

- INTERNAL_FRAME_CLOSING

```java
public static final int INTERNAL_FRAME_CLOSING
```

The "window is closing" event. This event is delivered when
the user attempts to close the internal frame, such as by
clicking the internal frame's close button,
or when a program attempts to close the internal frame
by invoking the

setClosed

method.

**See Also:** JInternalFrame.setDefaultCloseOperation(int)

,

JInternalFrame.doDefaultCloseAction()

,

JInternalFrame.setClosed(boolean)

,

Constant Field Values

- INTERNAL_FRAME_CLOSED

```java
public static final int INTERNAL_FRAME_CLOSED
```

The "window closed" event. This event is delivered after
the internal frame has been closed as the result of a call to
the

setClosed

or

dispose

method.

**See Also:** JInternalFrame.setClosed(boolean)

,

JInternalFrame.dispose()

,

Constant Field Values

- INTERNAL_FRAME_ICONIFIED

```java
public static final int INTERNAL_FRAME_ICONIFIED
```

The "window iconified" event.
This event indicates that the internal frame
was shrunk down to a small icon.

**See Also:** JInternalFrame.setIcon(boolean)

,

Constant Field Values

- INTERNAL_FRAME_DEICONIFIED

```java
public static final int INTERNAL_FRAME_DEICONIFIED
```

The "window deiconified" event type. This event indicates that the
internal frame has been restored to its normal size.

**See Also:** JInternalFrame.setIcon(boolean)

,

Constant Field Values

- INTERNAL_FRAME_ACTIVATED

```java
public static final int INTERNAL_FRAME_ACTIVATED
```

The "window activated" event type. This event indicates that keystrokes
and mouse clicks are directed towards this internal frame.

**See Also:** JInternalFrame.show()

,

JInternalFrame.setSelected(boolean)

,

Constant Field Values

- INTERNAL_FRAME_DEACTIVATED

```java
public static final int INTERNAL_FRAME_DEACTIVATED
```

The "window deactivated" event type. This event indicates that keystrokes
and mouse clicks are no longer directed to the internal frame.

**See Also:** JInternalFrame.setSelected(boolean)

,

Constant Field Values

---

#### Field Detail

INTERNAL_FRAME_FIRST

```java
public static final int INTERNAL_FRAME_FIRST
```

The first number in the range of IDs used for internal frame events.

**See Also:** Constant Field Values

---

#### INTERNAL_FRAME_FIRST

public static final int INTERNAL_FRAME_FIRST

The first number in the range of IDs used for internal frame events.

INTERNAL_FRAME_LAST

```java
public static final int INTERNAL_FRAME_LAST
```

The last number in the range of IDs used for internal frame events.

**See Also:** Constant Field Values

---

#### INTERNAL_FRAME_LAST

public static final int INTERNAL_FRAME_LAST

The last number in the range of IDs used for internal frame events.

INTERNAL_FRAME_OPENED

```java
public static final int INTERNAL_FRAME_OPENED
```

The "window opened" event. This event is delivered only
the first time the internal frame is made visible.

**See Also:** JInternalFrame.show()

,

Constant Field Values

---

#### INTERNAL_FRAME_OPENED

public static final int INTERNAL_FRAME_OPENED

The "window opened" event. This event is delivered only
the first time the internal frame is made visible.

INTERNAL_FRAME_CLOSING

```java
public static final int INTERNAL_FRAME_CLOSING
```

The "window is closing" event. This event is delivered when
the user attempts to close the internal frame, such as by
clicking the internal frame's close button,
or when a program attempts to close the internal frame
by invoking the

setClosed

method.

**See Also:** JInternalFrame.setDefaultCloseOperation(int)

,

JInternalFrame.doDefaultCloseAction()

,

JInternalFrame.setClosed(boolean)

,

Constant Field Values

---

#### INTERNAL_FRAME_CLOSING

public static final int INTERNAL_FRAME_CLOSING

The "window is closing" event. This event is delivered when
the user attempts to close the internal frame, such as by
clicking the internal frame's close button,
or when a program attempts to close the internal frame
by invoking the

setClosed

method.

INTERNAL_FRAME_CLOSED

```java
public static final int INTERNAL_FRAME_CLOSED
```

The "window closed" event. This event is delivered after
the internal frame has been closed as the result of a call to
the

setClosed

or

dispose

method.

**See Also:** JInternalFrame.setClosed(boolean)

,

JInternalFrame.dispose()

,

Constant Field Values

---

#### INTERNAL_FRAME_CLOSED

public static final int INTERNAL_FRAME_CLOSED

The "window closed" event. This event is delivered after
the internal frame has been closed as the result of a call to
the

setClosed

or

dispose

method.

INTERNAL_FRAME_ICONIFIED

```java
public static final int INTERNAL_FRAME_ICONIFIED
```

The "window iconified" event.
This event indicates that the internal frame
was shrunk down to a small icon.

**See Also:** JInternalFrame.setIcon(boolean)

,

Constant Field Values

---

#### INTERNAL_FRAME_ICONIFIED

public static final int INTERNAL_FRAME_ICONIFIED

The "window iconified" event.
This event indicates that the internal frame
was shrunk down to a small icon.

INTERNAL_FRAME_DEICONIFIED

```java
public static final int INTERNAL_FRAME_DEICONIFIED
```

The "window deiconified" event type. This event indicates that the
internal frame has been restored to its normal size.

**See Also:** JInternalFrame.setIcon(boolean)

,

Constant Field Values

---

#### INTERNAL_FRAME_DEICONIFIED

public static final int INTERNAL_FRAME_DEICONIFIED

The "window deiconified" event type. This event indicates that the
internal frame has been restored to its normal size.

INTERNAL_FRAME_ACTIVATED

```java
public static final int INTERNAL_FRAME_ACTIVATED
```

The "window activated" event type. This event indicates that keystrokes
and mouse clicks are directed towards this internal frame.

**See Also:** JInternalFrame.show()

,

JInternalFrame.setSelected(boolean)

,

Constant Field Values

---

#### INTERNAL_FRAME_ACTIVATED

public static final int INTERNAL_FRAME_ACTIVATED

The "window activated" event type. This event indicates that keystrokes
and mouse clicks are directed towards this internal frame.

INTERNAL_FRAME_DEACTIVATED

```java
public static final int INTERNAL_FRAME_DEACTIVATED
```

The "window deactivated" event type. This event indicates that keystrokes
and mouse clicks are no longer directed to the internal frame.

**See Also:** JInternalFrame.setSelected(boolean)

,

Constant Field Values

---

#### INTERNAL_FRAME_DEACTIVATED

public static final int INTERNAL_FRAME_DEACTIVATED

The "window deactivated" event type. This event indicates that keystrokes
and mouse clicks are no longer directed to the internal frame.

Constructor Detail

- InternalFrameEvent

```java
public InternalFrameEvent​(
JInternalFrame
source,
int id)
```

Constructs an

InternalFrameEvent

object.

**Parameters:** source

- the

JInternalFrame

object that originated the event
**Parameters:** id

- an integer indicating the type of event

---

#### Constructor Detail

InternalFrameEvent

```java
public InternalFrameEvent​(
JInternalFrame
source,
int id)
```

Constructs an

InternalFrameEvent

object.

**Parameters:** source

- the

JInternalFrame

object that originated the event
**Parameters:** id

- an integer indicating the type of event

---

#### InternalFrameEvent

public InternalFrameEvent​(

JInternalFrame

source,
int id)

Constructs an

InternalFrameEvent

object.

Method Detail

- paramString

```java
public
String
paramString()
```

Returns a parameter string identifying this event.
This method is useful for event logging and for debugging.

**Overrides:** paramString

in class

AWTEvent
**Returns:** a string identifying the event and its attributes

- getInternalFrame

```java
public
JInternalFrame
getInternalFrame()
```

Returns the originator of the event.

**Returns:** the

JInternalFrame

object that originated the event
**Since:** 1.3

---

#### Method Detail

paramString

```java
public
String
paramString()
```

Returns a parameter string identifying this event.
This method is useful for event logging and for debugging.

**Overrides:** paramString

in class

AWTEvent
**Returns:** a string identifying the event and its attributes

---

#### paramString

public

String

paramString()

Returns a parameter string identifying this event.
This method is useful for event logging and for debugging.

getInternalFrame

```java
public
JInternalFrame
getInternalFrame()
```

Returns the originator of the event.

**Returns:** the

JInternalFrame

object that originated the event
**Since:** 1.3

---

#### getInternalFrame

public

JInternalFrame

getInternalFrame()

Returns the originator of the event.

---

