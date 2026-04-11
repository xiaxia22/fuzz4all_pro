# Class InputEvent

**Source:** `java.desktop\java\awt\event\InputEvent.html`

### Class Description

```java
public abstract class
InputEvent

extends
ComponentEvent
```

The root event class for all component-level input events.

Input events are delivered to listeners before they are
processed normally by the source where they originated.
This allows listeners and component subclasses to "consume"
the event so that the source will not process them in their
default manner. For example, consuming mousePressed events
on a Button component will prevent the Button from being
activated.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### @Deprecated
(
since
="9")
public static final int SHIFT_MASK

The Shift key modifier constant.

**See Also:**
- Constant Field Values

---

#### @Deprecated
(
since
="9")
public static final int CTRL_MASK

The Control key modifier constant.

**See Also:**
- Constant Field Values

---

#### @Deprecated
(
since
="9")
public static final int META_MASK

The Meta key modifier constant.

**See Also:**
- Constant Field Values

---

#### @Deprecated
(
since
="9")
public static final int ALT_MASK

The Alt key modifier constant.

**See Also:**
- Constant Field Values

---

#### @Deprecated
(
since
="9")
public static final int ALT_GRAPH_MASK

The AltGraph key modifier constant.

**See Also:**
- Constant Field Values

---

#### @Deprecated
(
since
="9")
public static final int BUTTON1_MASK

The Mouse Button1 modifier constant.

**See Also:**
- Constant Field Values

---

#### @Deprecated
(
since
="9")
public static final int BUTTON2_MASK

The Mouse Button2 modifier constant.

**See Also:**
- Constant Field Values

---

#### @Deprecated
(
since
="9")
public static final int BUTTON3_MASK

The Mouse Button3 modifier constant.

**See Also:**
- Constant Field Values

---

#### public static final int SHIFT_DOWN_MASK

The Shift key extended modifier constant.

**See Also:**
- Constant Field Values

**Since:**
- 1.4

---

#### public static final int CTRL_DOWN_MASK

The Control key extended modifier constant.

**See Also:**
- Constant Field Values

**Since:**
- 1.4

---

#### public static final int META_DOWN_MASK

The Meta key extended modifier constant.

**See Also:**
- Constant Field Values

**Since:**
- 1.4

---

#### public static final int ALT_DOWN_MASK

The Alt key extended modifier constant.

**See Also:**
- Constant Field Values

**Since:**
- 1.4

---

#### public static final int BUTTON1_DOWN_MASK

The Mouse Button1 extended modifier constant.

**See Also:**
- Constant Field Values

**Since:**
- 1.4

---

#### public static final int BUTTON2_DOWN_MASK

The Mouse Button2 extended modifier constant.

**See Also:**
- Constant Field Values

**Since:**
- 1.4

---

#### public static final int BUTTON3_DOWN_MASK

The Mouse Button3 extended modifier constant.

**See Also:**
- Constant Field Values

**Since:**
- 1.4

---

#### public static final int ALT_GRAPH_DOWN_MASK

The AltGraph key extended modifier constant.

**See Also:**
- Constant Field Values

**Since:**
- 1.4

---

### Constructor Details

*No entries found.*

### Method Details

#### public static int getMaskForButton​(int button)

A method to obtain a mask for any existing mouse button.
The returned mask may be used for different purposes. Following are some of them:

- mousePress(buttons)

and

mouseRelease(buttons)

as a

modifiers

parameter when creating a new

MouseEvent

instance

to check

modifiersEx

of existing

MouseEvent

**Parameters:**
- button

- is a number to represent a button starting from 1.
For example,

```java
int button = InputEvent.getMaskForButton(1);
```

will have the same meaning as

```java
int button = InputEvent.getMaskForButton(MouseEvent.BUTTON1);
```

because

MouseEvent.BUTTON1

equals to 1.
If a mouse has three enabled buttons(see

MouseInfo.getNumberOfButtons()

)
then the values from the left column passed into the method will return
corresponding values from the right column:

```java
button

returned mask

BUTTON1

BUTTON1_DOWN_MASK

BUTTON2

BUTTON2_DOWN_MASK

BUTTON3

BUTTON3_DOWN_MASK
```

If a mouse has more than three enabled buttons then more values
are admissible (4, 5, etc.). There is no assigned constants for these extended buttons.
The button masks for the extra buttons returned by this method have no assigned names like the
first three button masks.

This method has the following implementation restriction.
It returns masks for a limited number of buttons only. The maximum number is
implementation dependent and may vary.
This limit is defined by the relevant number
of buttons that may hypothetically exist on the mouse but it is greater than the

MouseInfo.getNumberOfButtons()

.

**Returns:**
- a mask for an existing mouse button.

**Throws:**
- IllegalArgumentException

- if

button

is less than zero or greater than the number
of button masks reserved for buttons

**See Also:**
- MouseInfo.getNumberOfButtons()

,

Toolkit.areExtraMouseButtonsEnabled()

,

getModifiers()

,

getModifiersEx()

**Since:**
- 1.7

---

#### public boolean isShiftDown()

Returns whether or not the Shift modifier is down on this event.

**Returns:**
- whether or not the Shift modifier is down on this event

---

#### public boolean isControlDown()

Returns whether or not the Control modifier is down on this event.

**Returns:**
- whether or not the Control modifier is down on this event

---

#### public boolean isMetaDown()

Returns whether or not the Meta modifier is down on this event.

**Returns:**
- whether or not the Meta modifier is down on this event

---

#### public boolean isAltDown()

Returns whether or not the Alt modifier is down on this event.

**Returns:**
- whether or not the Alt modifier is down on this event

---

#### public boolean isAltGraphDown()

Returns whether or not the AltGraph modifier is down on this event.

**Returns:**
- whether or not the AltGraph modifier is down on this event

---

#### public long getWhen()

Returns the difference in milliseconds between the timestamp of when this event occurred and
midnight, January 1, 1970 UTC.

**Returns:**
- the difference in milliseconds between the timestamp and midnight, January 1, 1970 UTC

---

#### @Deprecated
(
since
="9")
public int getModifiers()

Returns the modifier mask for this event.

**Returns:**
- the modifier mask for this event

---

#### public int getModifiersEx()

Returns the extended modifier mask for this event.

Extended modifiers are the modifiers that ends with the _DOWN_MASK suffix,
such as ALT_DOWN_MASK, BUTTON1_DOWN_MASK, and others.

Extended modifiers represent the state of all modal keys,
such as ALT, CTRL, META, and the mouse buttons just after
the event occurred.

For example, if the user presses

button 1

followed by

button 2

, and then releases them in the same order,
the following sequence of events is generated:

```java
MOUSE_PRESSED
:
BUTTON1_DOWN_MASK

MOUSE_PRESSED
:
BUTTON1_DOWN_MASK | BUTTON2_DOWN_MASK

MOUSE_RELEASED
:
BUTTON2_DOWN_MASK

MOUSE_CLICKED
:
BUTTON2_DOWN_MASK

MOUSE_RELEASED
:

MOUSE_CLICKED
:
```

It is not recommended to compare the return value of this method
using

==

because new modifiers can be added in the future.
For example, the appropriate way to check that SHIFT and BUTTON1 are
down, but CTRL is up is demonstrated by the following code:

```java
int onmask = SHIFT_DOWN_MASK | BUTTON1_DOWN_MASK;
int offmask = CTRL_DOWN_MASK;
if ((event.getModifiersEx() & (onmask | offmask)) == onmask) {
...
}
```

The above code will work even if new modifiers are added.

**Returns:**
- the extended modifier mask for this event

**Since:**
- 1.4

---

#### public void consume()

Consumes this event so that it will not be processed
in the default manner by the source which originated it.

**Overrides:**
- consume

in class

AWTEvent

---

#### public boolean isConsumed()

Returns whether or not this event has been consumed.

**Overrides:**
- isConsumed

in class

AWTEvent

**Returns:**
- whether or not this event has been consumed

**See Also:**
- consume()

---

#### public static
String
getModifiersExText​(int modifiers)

Returns a String describing the extended modifier keys and
mouse buttons, such as "Shift", "Button1", or "Ctrl+Shift".
These strings can be localized by changing the

awt.properties

file.

Note that passing negative parameter is incorrect,
and will cause the returning an unspecified string.
Zero parameter means that no modifiers were passed and will
cause the returning an empty string.

**Parameters:**
- modifiers

- a modifier mask describing the extended
modifier keys and mouse buttons for the event

**Returns:**
- a String describing the extended modifier keys and
mouse buttons

**Since:**
- 1.4

---

### Additional Sections

#### Class InputEvent

java.lang.Object

- java.util.EventObject
- - java.awt.AWTEvent
- - java.awt.event.ComponentEvent
- - java.awt.event.InputEvent

java.util.EventObject

- java.awt.AWTEvent
- - java.awt.event.ComponentEvent
- - java.awt.event.InputEvent

java.awt.AWTEvent

- java.awt.event.ComponentEvent
- - java.awt.event.InputEvent

java.awt.event.ComponentEvent

- java.awt.event.InputEvent

java.awt.event.InputEvent

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** KeyEvent

,

MouseEvent

```java
public abstract class
InputEvent

extends
ComponentEvent
```

The root event class for all component-level input events.

Input events are delivered to listeners before they are
processed normally by the source where they originated.
This allows listeners and component subclasses to "consume"
the event so that the source will not process them in their
default manner. For example, consuming mousePressed events
on a Button component will prevent the Button from being
activated.

**Since:** 1.1
**See Also:** KeyEvent

,

KeyAdapter

,

MouseEvent

,

MouseAdapter

,

MouseMotionAdapter

,

Serialized Form

public abstract class

InputEvent

extends

ComponentEvent

The root event class for all component-level input events.

Input events are delivered to listeners before they are
processed normally by the source where they originated.
This allows listeners and component subclasses to "consume"
the event so that the source will not process them in their
default manner. For example, consuming mousePressed events
on a Button component will prevent the Button from being
activated.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ALT_DOWN_MASK

The Alt key extended modifier constant.

static int

ALT_GRAPH_DOWN_MASK

The AltGraph key extended modifier constant.

static int

ALT_GRAPH_MASK

Deprecated.

It is recommended that ALT_GRAPH_DOWN_MASK and

getModifiersEx()

be used instead

static int

ALT_MASK

Deprecated.

It is recommended that ALT_DOWN_MASK and

getModifiersEx()

be used instead

static int

BUTTON1_DOWN_MASK

The Mouse Button1 extended modifier constant.

static int

BUTTON1_MASK

Deprecated.

It is recommended that BUTTON1_DOWN_MASK and

getModifiersEx()

be used instead

static int

BUTTON2_DOWN_MASK

The Mouse Button2 extended modifier constant.

static int

BUTTON2_MASK

Deprecated.

It is recommended that BUTTON2_DOWN_MASK and

getModifiersEx()

be used instead.

static int

BUTTON3_DOWN_MASK

The Mouse Button3 extended modifier constant.

static int

BUTTON3_MASK

Deprecated.

It is recommended that BUTTON3_DOWN_MASK and

getModifiersEx()

be used instead.

static int

CTRL_DOWN_MASK

The Control key extended modifier constant.

static int

CTRL_MASK

Deprecated.

It is recommended that CTRL_DOWN_MASK and

getModifiersEx()

be used instead

static int

META_DOWN_MASK

The Meta key extended modifier constant.

static int

META_MASK

Deprecated.

It is recommended that META_DOWN_MASK and

getModifiersEx()

be used instead

static int

SHIFT_DOWN_MASK

The Shift key extended modifier constant.

static int

SHIFT_MASK

Deprecated.

It is recommended that SHIFT_DOWN_MASK and

getModifiersEx()

be used instead

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

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

consume

()

Consumes this event so that it will not be processed
in the default manner by the source which originated it.

static int

getMaskForButton

​(int button)

A method to obtain a mask for any existing mouse button.

int

getModifiers

()

Deprecated.

It is recommended that extended modifier keys and

getModifiersEx()

be used instead

int

getModifiersEx

()

Returns the extended modifier mask for this event.

static

String

getModifiersExText

​(int modifiers)

Returns a String describing the extended modifier keys and
mouse buttons, such as "Shift", "Button1", or "Ctrl+Shift".

long

getWhen

()

Returns the difference in milliseconds between the timestamp of when this event occurred and
midnight, January 1, 1970 UTC.

boolean

isAltDown

()

Returns whether or not the Alt modifier is down on this event.

boolean

isAltGraphDown

()

Returns whether or not the AltGraph modifier is down on this event.

boolean

isConsumed

()

Returns whether or not this event has been consumed.

boolean

isControlDown

()

Returns whether or not the Control modifier is down on this event.

boolean

isMetaDown

()

Returns whether or not the Meta modifier is down on this event.

boolean

isShiftDown

()

Returns whether or not the Shift modifier is down on this event.

- Methods declared in class java.awt.event.

ComponentEvent

getComponent

,

paramString

- Methods declared in class java.awt.

AWTEvent

getID

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

ALT_DOWN_MASK

The Alt key extended modifier constant.

static int

ALT_GRAPH_DOWN_MASK

The AltGraph key extended modifier constant.

static int

ALT_GRAPH_MASK

Deprecated.

It is recommended that ALT_GRAPH_DOWN_MASK and

getModifiersEx()

be used instead

static int

ALT_MASK

Deprecated.

It is recommended that ALT_DOWN_MASK and

getModifiersEx()

be used instead

static int

BUTTON1_DOWN_MASK

The Mouse Button1 extended modifier constant.

static int

BUTTON1_MASK

Deprecated.

It is recommended that BUTTON1_DOWN_MASK and

getModifiersEx()

be used instead

static int

BUTTON2_DOWN_MASK

The Mouse Button2 extended modifier constant.

static int

BUTTON2_MASK

Deprecated.

It is recommended that BUTTON2_DOWN_MASK and

getModifiersEx()

be used instead.

static int

BUTTON3_DOWN_MASK

The Mouse Button3 extended modifier constant.

static int

BUTTON3_MASK

Deprecated.

It is recommended that BUTTON3_DOWN_MASK and

getModifiersEx()

be used instead.

static int

CTRL_DOWN_MASK

The Control key extended modifier constant.

static int

CTRL_MASK

Deprecated.

It is recommended that CTRL_DOWN_MASK and

getModifiersEx()

be used instead

static int

META_DOWN_MASK

The Meta key extended modifier constant.

static int

META_MASK

Deprecated.

It is recommended that META_DOWN_MASK and

getModifiersEx()

be used instead

static int

SHIFT_DOWN_MASK

The Shift key extended modifier constant.

static int

SHIFT_MASK

Deprecated.

It is recommended that SHIFT_DOWN_MASK and

getModifiersEx()

be used instead

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

The Alt key extended modifier constant.

The AltGraph key extended modifier constant.

Deprecated.

It is recommended that ALT_GRAPH_DOWN_MASK and

getModifiersEx()

be used instead

Deprecated.

It is recommended that ALT_DOWN_MASK and

getModifiersEx()

be used instead

The Mouse Button1 extended modifier constant.

Deprecated.

It is recommended that BUTTON1_DOWN_MASK and

getModifiersEx()

be used instead

The Mouse Button2 extended modifier constant.

Deprecated.

It is recommended that BUTTON2_DOWN_MASK and

getModifiersEx()

be used instead.

The Mouse Button3 extended modifier constant.

Deprecated.

It is recommended that BUTTON3_DOWN_MASK and

getModifiersEx()

be used instead.

The Control key extended modifier constant.

Deprecated.

It is recommended that CTRL_DOWN_MASK and

getModifiersEx()

be used instead

The Meta key extended modifier constant.

Deprecated.

It is recommended that META_DOWN_MASK and

getModifiersEx()

be used instead

The Shift key extended modifier constant.

Deprecated.

It is recommended that SHIFT_DOWN_MASK and

getModifiersEx()

be used instead

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

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

consume

()

Consumes this event so that it will not be processed
in the default manner by the source which originated it.

static int

getMaskForButton

​(int button)

A method to obtain a mask for any existing mouse button.

int

getModifiers

()

Deprecated.

It is recommended that extended modifier keys and

getModifiersEx()

be used instead

int

getModifiersEx

()

Returns the extended modifier mask for this event.

static

String

getModifiersExText

​(int modifiers)

Returns a String describing the extended modifier keys and
mouse buttons, such as "Shift", "Button1", or "Ctrl+Shift".

long

getWhen

()

Returns the difference in milliseconds between the timestamp of when this event occurred and
midnight, January 1, 1970 UTC.

boolean

isAltDown

()

Returns whether or not the Alt modifier is down on this event.

boolean

isAltGraphDown

()

Returns whether or not the AltGraph modifier is down on this event.

boolean

isConsumed

()

Returns whether or not this event has been consumed.

boolean

isControlDown

()

Returns whether or not the Control modifier is down on this event.

boolean

isMetaDown

()

Returns whether or not the Meta modifier is down on this event.

boolean

isShiftDown

()

Returns whether or not the Shift modifier is down on this event.

- Methods declared in class java.awt.event.

ComponentEvent

getComponent

,

paramString

- Methods declared in class java.awt.

AWTEvent

getID

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

Consumes this event so that it will not be processed
in the default manner by the source which originated it.

A method to obtain a mask for any existing mouse button.

Deprecated.

It is recommended that extended modifier keys and

getModifiersEx()

be used instead

Returns the extended modifier mask for this event.

Returns a String describing the extended modifier keys and
mouse buttons, such as "Shift", "Button1", or "Ctrl+Shift".

Returns the difference in milliseconds between the timestamp of when this event occurred and
midnight, January 1, 1970 UTC.

Returns whether or not the Alt modifier is down on this event.

Returns whether or not the AltGraph modifier is down on this event.

Returns whether or not this event has been consumed.

Returns whether or not the Control modifier is down on this event.

Returns whether or not the Meta modifier is down on this event.

Returns whether or not the Shift modifier is down on this event.

Methods declared in class java.awt.event.

ComponentEvent

getComponent

,

paramString

---

#### Methods declared in class java.awt.event. ComponentEvent

Methods declared in class java.awt.

AWTEvent

getID

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

- SHIFT_MASK

```java
@Deprecated
(
since
="9")
public static final int SHIFT_MASK
```

Deprecated.

It is recommended that SHIFT_DOWN_MASK and

getModifiersEx()

be used instead

The Shift key modifier constant.

**See Also:** Constant Field Values

- CTRL_MASK

```java
@Deprecated
(
since
="9")
public static final int CTRL_MASK
```

Deprecated.

It is recommended that CTRL_DOWN_MASK and

getModifiersEx()

be used instead

The Control key modifier constant.

**See Also:** Constant Field Values

- META_MASK

```java
@Deprecated
(
since
="9")
public static final int META_MASK
```

Deprecated.

It is recommended that META_DOWN_MASK and

getModifiersEx()

be used instead

The Meta key modifier constant.

**See Also:** Constant Field Values

- ALT_MASK

```java
@Deprecated
(
since
="9")
public static final int ALT_MASK
```

Deprecated.

It is recommended that ALT_DOWN_MASK and

getModifiersEx()

be used instead

The Alt key modifier constant.

**See Also:** Constant Field Values

- ALT_GRAPH_MASK

```java
@Deprecated
(
since
="9")
public static final int ALT_GRAPH_MASK
```

Deprecated.

It is recommended that ALT_GRAPH_DOWN_MASK and

getModifiersEx()

be used instead

The AltGraph key modifier constant.

**See Also:** Constant Field Values

- BUTTON1_MASK

```java
@Deprecated
(
since
="9")
public static final int BUTTON1_MASK
```

Deprecated.

It is recommended that BUTTON1_DOWN_MASK and

getModifiersEx()

be used instead

The Mouse Button1 modifier constant.

**See Also:** Constant Field Values

- BUTTON2_MASK

```java
@Deprecated
(
since
="9")
public static final int BUTTON2_MASK
```

Deprecated.

It is recommended that BUTTON2_DOWN_MASK and

getModifiersEx()

be used instead. Note that
BUTTON2_MASK has the same value as ALT_MASK.

The Mouse Button2 modifier constant.

**See Also:** Constant Field Values

- BUTTON3_MASK

```java
@Deprecated
(
since
="9")
public static final int BUTTON3_MASK
```

Deprecated.

It is recommended that BUTTON3_DOWN_MASK and

getModifiersEx()

be used instead. Note that
BUTTON3_MASK has the same value as META_MASK.

The Mouse Button3 modifier constant.

**See Also:** Constant Field Values

- SHIFT_DOWN_MASK

```java
public static final int SHIFT_DOWN_MASK
```

The Shift key extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

- CTRL_DOWN_MASK

```java
public static final int CTRL_DOWN_MASK
```

The Control key extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

- META_DOWN_MASK

```java
public static final int META_DOWN_MASK
```

The Meta key extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

- ALT_DOWN_MASK

```java
public static final int ALT_DOWN_MASK
```

The Alt key extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

- BUTTON1_DOWN_MASK

```java
public static final int BUTTON1_DOWN_MASK
```

The Mouse Button1 extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

- BUTTON2_DOWN_MASK

```java
public static final int BUTTON2_DOWN_MASK
```

The Mouse Button2 extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

- BUTTON3_DOWN_MASK

```java
public static final int BUTTON3_DOWN_MASK
```

The Mouse Button3 extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

- ALT_GRAPH_DOWN_MASK

```java
public static final int ALT_GRAPH_DOWN_MASK
```

The AltGraph key extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getMaskForButton

```java
public static int getMaskForButton​(int button)
```

A method to obtain a mask for any existing mouse button.
The returned mask may be used for different purposes. Following are some of them:

- mousePress(buttons)

and

mouseRelease(buttons)

as a

modifiers

parameter when creating a new

MouseEvent

instance

to check

modifiersEx

of existing

MouseEvent

**Parameters:** button

- is a number to represent a button starting from 1.
For example,

```java
int button = InputEvent.getMaskForButton(1);
```

will have the same meaning as

```java
int button = InputEvent.getMaskForButton(MouseEvent.BUTTON1);
```

because

MouseEvent.BUTTON1

equals to 1.
If a mouse has three enabled buttons(see

MouseInfo.getNumberOfButtons()

)
then the values from the left column passed into the method will return
corresponding values from the right column:

```java
button

returned mask

BUTTON1

BUTTON1_DOWN_MASK

BUTTON2

BUTTON2_DOWN_MASK

BUTTON3

BUTTON3_DOWN_MASK
```

If a mouse has more than three enabled buttons then more values
are admissible (4, 5, etc.). There is no assigned constants for these extended buttons.
The button masks for the extra buttons returned by this method have no assigned names like the
first three button masks.

This method has the following implementation restriction.
It returns masks for a limited number of buttons only. The maximum number is
implementation dependent and may vary.
This limit is defined by the relevant number
of buttons that may hypothetically exist on the mouse but it is greater than the

MouseInfo.getNumberOfButtons()

.
**Returns:** a mask for an existing mouse button.
**Throws:** IllegalArgumentException

- if

button

is less than zero or greater than the number
of button masks reserved for buttons
**Since:** 1.7
**See Also:** MouseInfo.getNumberOfButtons()

,

Toolkit.areExtraMouseButtonsEnabled()

,

getModifiers()

,

getModifiersEx()

- isShiftDown

```java
public boolean isShiftDown()
```

Returns whether or not the Shift modifier is down on this event.

**Returns:** whether or not the Shift modifier is down on this event

- isControlDown

```java
public boolean isControlDown()
```

Returns whether or not the Control modifier is down on this event.

**Returns:** whether or not the Control modifier is down on this event

- isMetaDown

```java
public boolean isMetaDown()
```

Returns whether or not the Meta modifier is down on this event.

**Returns:** whether or not the Meta modifier is down on this event

- isAltDown

```java
public boolean isAltDown()
```

Returns whether or not the Alt modifier is down on this event.

**Returns:** whether or not the Alt modifier is down on this event

- isAltGraphDown

```java
public boolean isAltGraphDown()
```

Returns whether or not the AltGraph modifier is down on this event.

**Returns:** whether or not the AltGraph modifier is down on this event

- getWhen

```java
public long getWhen()
```

Returns the difference in milliseconds between the timestamp of when this event occurred and
midnight, January 1, 1970 UTC.

**Returns:** the difference in milliseconds between the timestamp and midnight, January 1, 1970 UTC

- getModifiers

```java
@Deprecated
(
since
="9")
public int getModifiers()
```

Deprecated.

It is recommended that extended modifier keys and

getModifiersEx()

be used instead

Returns the modifier mask for this event.

**Returns:** the modifier mask for this event

- getModifiersEx

```java
public int getModifiersEx()
```

Returns the extended modifier mask for this event.

Extended modifiers are the modifiers that ends with the _DOWN_MASK suffix,
such as ALT_DOWN_MASK, BUTTON1_DOWN_MASK, and others.

Extended modifiers represent the state of all modal keys,
such as ALT, CTRL, META, and the mouse buttons just after
the event occurred.

For example, if the user presses

button 1

followed by

button 2

, and then releases them in the same order,
the following sequence of events is generated:

```java
MOUSE_PRESSED
:
BUTTON1_DOWN_MASK

MOUSE_PRESSED
:
BUTTON1_DOWN_MASK | BUTTON2_DOWN_MASK

MOUSE_RELEASED
:
BUTTON2_DOWN_MASK

MOUSE_CLICKED
:
BUTTON2_DOWN_MASK

MOUSE_RELEASED
:

MOUSE_CLICKED
:
```

It is not recommended to compare the return value of this method
using

==

because new modifiers can be added in the future.
For example, the appropriate way to check that SHIFT and BUTTON1 are
down, but CTRL is up is demonstrated by the following code:

```java
int onmask = SHIFT_DOWN_MASK | BUTTON1_DOWN_MASK;
int offmask = CTRL_DOWN_MASK;
if ((event.getModifiersEx() & (onmask | offmask)) == onmask) {
...
}
```

The above code will work even if new modifiers are added.

**Returns:** the extended modifier mask for this event
**Since:** 1.4

- consume

```java
public void consume()
```

Consumes this event so that it will not be processed
in the default manner by the source which originated it.

**Overrides:** consume

in class

AWTEvent

- isConsumed

```java
public boolean isConsumed()
```

Returns whether or not this event has been consumed.

**Overrides:** isConsumed

in class

AWTEvent
**Returns:** whether or not this event has been consumed
**See Also:** consume()

- getModifiersExText

```java
public static
String
getModifiersExText​(int modifiers)
```

Returns a String describing the extended modifier keys and
mouse buttons, such as "Shift", "Button1", or "Ctrl+Shift".
These strings can be localized by changing the

awt.properties

file.

Note that passing negative parameter is incorrect,
and will cause the returning an unspecified string.
Zero parameter means that no modifiers were passed and will
cause the returning an empty string.

**Parameters:** modifiers

- a modifier mask describing the extended
modifier keys and mouse buttons for the event
**Returns:** a String describing the extended modifier keys and
mouse buttons
**Since:** 1.4

Field Detail

- SHIFT_MASK

```java
@Deprecated
(
since
="9")
public static final int SHIFT_MASK
```

Deprecated.

It is recommended that SHIFT_DOWN_MASK and

getModifiersEx()

be used instead

The Shift key modifier constant.

**See Also:** Constant Field Values

- CTRL_MASK

```java
@Deprecated
(
since
="9")
public static final int CTRL_MASK
```

Deprecated.

It is recommended that CTRL_DOWN_MASK and

getModifiersEx()

be used instead

The Control key modifier constant.

**See Also:** Constant Field Values

- META_MASK

```java
@Deprecated
(
since
="9")
public static final int META_MASK
```

Deprecated.

It is recommended that META_DOWN_MASK and

getModifiersEx()

be used instead

The Meta key modifier constant.

**See Also:** Constant Field Values

- ALT_MASK

```java
@Deprecated
(
since
="9")
public static final int ALT_MASK
```

Deprecated.

It is recommended that ALT_DOWN_MASK and

getModifiersEx()

be used instead

The Alt key modifier constant.

**See Also:** Constant Field Values

- ALT_GRAPH_MASK

```java
@Deprecated
(
since
="9")
public static final int ALT_GRAPH_MASK
```

Deprecated.

It is recommended that ALT_GRAPH_DOWN_MASK and

getModifiersEx()

be used instead

The AltGraph key modifier constant.

**See Also:** Constant Field Values

- BUTTON1_MASK

```java
@Deprecated
(
since
="9")
public static final int BUTTON1_MASK
```

Deprecated.

It is recommended that BUTTON1_DOWN_MASK and

getModifiersEx()

be used instead

The Mouse Button1 modifier constant.

**See Also:** Constant Field Values

- BUTTON2_MASK

```java
@Deprecated
(
since
="9")
public static final int BUTTON2_MASK
```

Deprecated.

It is recommended that BUTTON2_DOWN_MASK and

getModifiersEx()

be used instead. Note that
BUTTON2_MASK has the same value as ALT_MASK.

The Mouse Button2 modifier constant.

**See Also:** Constant Field Values

- BUTTON3_MASK

```java
@Deprecated
(
since
="9")
public static final int BUTTON3_MASK
```

Deprecated.

It is recommended that BUTTON3_DOWN_MASK and

getModifiersEx()

be used instead. Note that
BUTTON3_MASK has the same value as META_MASK.

The Mouse Button3 modifier constant.

**See Also:** Constant Field Values

- SHIFT_DOWN_MASK

```java
public static final int SHIFT_DOWN_MASK
```

The Shift key extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

- CTRL_DOWN_MASK

```java
public static final int CTRL_DOWN_MASK
```

The Control key extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

- META_DOWN_MASK

```java
public static final int META_DOWN_MASK
```

The Meta key extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

- ALT_DOWN_MASK

```java
public static final int ALT_DOWN_MASK
```

The Alt key extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

- BUTTON1_DOWN_MASK

```java
public static final int BUTTON1_DOWN_MASK
```

The Mouse Button1 extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

- BUTTON2_DOWN_MASK

```java
public static final int BUTTON2_DOWN_MASK
```

The Mouse Button2 extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

- BUTTON3_DOWN_MASK

```java
public static final int BUTTON3_DOWN_MASK
```

The Mouse Button3 extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

- ALT_GRAPH_DOWN_MASK

```java
public static final int ALT_GRAPH_DOWN_MASK
```

The AltGraph key extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

---

#### Field Detail

SHIFT_MASK

```java
@Deprecated
(
since
="9")
public static final int SHIFT_MASK
```

Deprecated.

It is recommended that SHIFT_DOWN_MASK and

getModifiersEx()

be used instead

The Shift key modifier constant.

**See Also:** Constant Field Values

---

#### SHIFT_MASK

@Deprecated

(

since

="9")
public static final int SHIFT_MASK

The Shift key modifier constant.

CTRL_MASK

```java
@Deprecated
(
since
="9")
public static final int CTRL_MASK
```

Deprecated.

It is recommended that CTRL_DOWN_MASK and

getModifiersEx()

be used instead

The Control key modifier constant.

**See Also:** Constant Field Values

---

#### CTRL_MASK

@Deprecated

(

since

="9")
public static final int CTRL_MASK

The Control key modifier constant.

META_MASK

```java
@Deprecated
(
since
="9")
public static final int META_MASK
```

Deprecated.

It is recommended that META_DOWN_MASK and

getModifiersEx()

be used instead

The Meta key modifier constant.

**See Also:** Constant Field Values

---

#### META_MASK

@Deprecated

(

since

="9")
public static final int META_MASK

The Meta key modifier constant.

ALT_MASK

```java
@Deprecated
(
since
="9")
public static final int ALT_MASK
```

Deprecated.

It is recommended that ALT_DOWN_MASK and

getModifiersEx()

be used instead

The Alt key modifier constant.

**See Also:** Constant Field Values

---

#### ALT_MASK

@Deprecated

(

since

="9")
public static final int ALT_MASK

The Alt key modifier constant.

ALT_GRAPH_MASK

```java
@Deprecated
(
since
="9")
public static final int ALT_GRAPH_MASK
```

Deprecated.

It is recommended that ALT_GRAPH_DOWN_MASK and

getModifiersEx()

be used instead

The AltGraph key modifier constant.

**See Also:** Constant Field Values

---

#### ALT_GRAPH_MASK

@Deprecated

(

since

="9")
public static final int ALT_GRAPH_MASK

The AltGraph key modifier constant.

BUTTON1_MASK

```java
@Deprecated
(
since
="9")
public static final int BUTTON1_MASK
```

Deprecated.

It is recommended that BUTTON1_DOWN_MASK and

getModifiersEx()

be used instead

The Mouse Button1 modifier constant.

**See Also:** Constant Field Values

---

#### BUTTON1_MASK

@Deprecated

(

since

="9")
public static final int BUTTON1_MASK

The Mouse Button1 modifier constant.

BUTTON2_MASK

```java
@Deprecated
(
since
="9")
public static final int BUTTON2_MASK
```

Deprecated.

It is recommended that BUTTON2_DOWN_MASK and

getModifiersEx()

be used instead. Note that
BUTTON2_MASK has the same value as ALT_MASK.

The Mouse Button2 modifier constant.

**See Also:** Constant Field Values

---

#### BUTTON2_MASK

@Deprecated

(

since

="9")
public static final int BUTTON2_MASK

The Mouse Button2 modifier constant.

BUTTON3_MASK

```java
@Deprecated
(
since
="9")
public static final int BUTTON3_MASK
```

Deprecated.

It is recommended that BUTTON3_DOWN_MASK and

getModifiersEx()

be used instead. Note that
BUTTON3_MASK has the same value as META_MASK.

The Mouse Button3 modifier constant.

**See Also:** Constant Field Values

---

#### BUTTON3_MASK

@Deprecated

(

since

="9")
public static final int BUTTON3_MASK

The Mouse Button3 modifier constant.

SHIFT_DOWN_MASK

```java
public static final int SHIFT_DOWN_MASK
```

The Shift key extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

---

#### SHIFT_DOWN_MASK

public static final int SHIFT_DOWN_MASK

The Shift key extended modifier constant.

CTRL_DOWN_MASK

```java
public static final int CTRL_DOWN_MASK
```

The Control key extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

---

#### CTRL_DOWN_MASK

public static final int CTRL_DOWN_MASK

The Control key extended modifier constant.

META_DOWN_MASK

```java
public static final int META_DOWN_MASK
```

The Meta key extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

---

#### META_DOWN_MASK

public static final int META_DOWN_MASK

The Meta key extended modifier constant.

ALT_DOWN_MASK

```java
public static final int ALT_DOWN_MASK
```

The Alt key extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

---

#### ALT_DOWN_MASK

public static final int ALT_DOWN_MASK

The Alt key extended modifier constant.

BUTTON1_DOWN_MASK

```java
public static final int BUTTON1_DOWN_MASK
```

The Mouse Button1 extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

---

#### BUTTON1_DOWN_MASK

public static final int BUTTON1_DOWN_MASK

The Mouse Button1 extended modifier constant.

BUTTON2_DOWN_MASK

```java
public static final int BUTTON2_DOWN_MASK
```

The Mouse Button2 extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

---

#### BUTTON2_DOWN_MASK

public static final int BUTTON2_DOWN_MASK

The Mouse Button2 extended modifier constant.

BUTTON3_DOWN_MASK

```java
public static final int BUTTON3_DOWN_MASK
```

The Mouse Button3 extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

---

#### BUTTON3_DOWN_MASK

public static final int BUTTON3_DOWN_MASK

The Mouse Button3 extended modifier constant.

ALT_GRAPH_DOWN_MASK

```java
public static final int ALT_GRAPH_DOWN_MASK
```

The AltGraph key extended modifier constant.

**Since:** 1.4
**See Also:** Constant Field Values

---

#### ALT_GRAPH_DOWN_MASK

public static final int ALT_GRAPH_DOWN_MASK

The AltGraph key extended modifier constant.

Method Detail

- getMaskForButton

```java
public static int getMaskForButton​(int button)
```

A method to obtain a mask for any existing mouse button.
The returned mask may be used for different purposes. Following are some of them:

- mousePress(buttons)

and

mouseRelease(buttons)

as a

modifiers

parameter when creating a new

MouseEvent

instance

to check

modifiersEx

of existing

MouseEvent

**Parameters:** button

- is a number to represent a button starting from 1.
For example,

```java
int button = InputEvent.getMaskForButton(1);
```

will have the same meaning as

```java
int button = InputEvent.getMaskForButton(MouseEvent.BUTTON1);
```

because

MouseEvent.BUTTON1

equals to 1.
If a mouse has three enabled buttons(see

MouseInfo.getNumberOfButtons()

)
then the values from the left column passed into the method will return
corresponding values from the right column:

```java
button

returned mask

BUTTON1

BUTTON1_DOWN_MASK

BUTTON2

BUTTON2_DOWN_MASK

BUTTON3

BUTTON3_DOWN_MASK
```

If a mouse has more than three enabled buttons then more values
are admissible (4, 5, etc.). There is no assigned constants for these extended buttons.
The button masks for the extra buttons returned by this method have no assigned names like the
first three button masks.

This method has the following implementation restriction.
It returns masks for a limited number of buttons only. The maximum number is
implementation dependent and may vary.
This limit is defined by the relevant number
of buttons that may hypothetically exist on the mouse but it is greater than the

MouseInfo.getNumberOfButtons()

.
**Returns:** a mask for an existing mouse button.
**Throws:** IllegalArgumentException

- if

button

is less than zero or greater than the number
of button masks reserved for buttons
**Since:** 1.7
**See Also:** MouseInfo.getNumberOfButtons()

,

Toolkit.areExtraMouseButtonsEnabled()

,

getModifiers()

,

getModifiersEx()

- isShiftDown

```java
public boolean isShiftDown()
```

Returns whether or not the Shift modifier is down on this event.

**Returns:** whether or not the Shift modifier is down on this event

- isControlDown

```java
public boolean isControlDown()
```

Returns whether or not the Control modifier is down on this event.

**Returns:** whether or not the Control modifier is down on this event

- isMetaDown

```java
public boolean isMetaDown()
```

Returns whether or not the Meta modifier is down on this event.

**Returns:** whether or not the Meta modifier is down on this event

- isAltDown

```java
public boolean isAltDown()
```

Returns whether or not the Alt modifier is down on this event.

**Returns:** whether or not the Alt modifier is down on this event

- isAltGraphDown

```java
public boolean isAltGraphDown()
```

Returns whether or not the AltGraph modifier is down on this event.

**Returns:** whether or not the AltGraph modifier is down on this event

- getWhen

```java
public long getWhen()
```

Returns the difference in milliseconds between the timestamp of when this event occurred and
midnight, January 1, 1970 UTC.

**Returns:** the difference in milliseconds between the timestamp and midnight, January 1, 1970 UTC

- getModifiers

```java
@Deprecated
(
since
="9")
public int getModifiers()
```

Deprecated.

It is recommended that extended modifier keys and

getModifiersEx()

be used instead

Returns the modifier mask for this event.

**Returns:** the modifier mask for this event

- getModifiersEx

```java
public int getModifiersEx()
```

Returns the extended modifier mask for this event.

Extended modifiers are the modifiers that ends with the _DOWN_MASK suffix,
such as ALT_DOWN_MASK, BUTTON1_DOWN_MASK, and others.

Extended modifiers represent the state of all modal keys,
such as ALT, CTRL, META, and the mouse buttons just after
the event occurred.

For example, if the user presses

button 1

followed by

button 2

, and then releases them in the same order,
the following sequence of events is generated:

```java
MOUSE_PRESSED
:
BUTTON1_DOWN_MASK

MOUSE_PRESSED
:
BUTTON1_DOWN_MASK | BUTTON2_DOWN_MASK

MOUSE_RELEASED
:
BUTTON2_DOWN_MASK

MOUSE_CLICKED
:
BUTTON2_DOWN_MASK

MOUSE_RELEASED
:

MOUSE_CLICKED
:
```

It is not recommended to compare the return value of this method
using

==

because new modifiers can be added in the future.
For example, the appropriate way to check that SHIFT and BUTTON1 are
down, but CTRL is up is demonstrated by the following code:

```java
int onmask = SHIFT_DOWN_MASK | BUTTON1_DOWN_MASK;
int offmask = CTRL_DOWN_MASK;
if ((event.getModifiersEx() & (onmask | offmask)) == onmask) {
...
}
```

The above code will work even if new modifiers are added.

**Returns:** the extended modifier mask for this event
**Since:** 1.4

- consume

```java
public void consume()
```

Consumes this event so that it will not be processed
in the default manner by the source which originated it.

**Overrides:** consume

in class

AWTEvent

- isConsumed

```java
public boolean isConsumed()
```

Returns whether or not this event has been consumed.

**Overrides:** isConsumed

in class

AWTEvent
**Returns:** whether or not this event has been consumed
**See Also:** consume()

- getModifiersExText

```java
public static
String
getModifiersExText​(int modifiers)
```

Returns a String describing the extended modifier keys and
mouse buttons, such as "Shift", "Button1", or "Ctrl+Shift".
These strings can be localized by changing the

awt.properties

file.

Note that passing negative parameter is incorrect,
and will cause the returning an unspecified string.
Zero parameter means that no modifiers were passed and will
cause the returning an empty string.

**Parameters:** modifiers

- a modifier mask describing the extended
modifier keys and mouse buttons for the event
**Returns:** a String describing the extended modifier keys and
mouse buttons
**Since:** 1.4

---

#### Method Detail

getMaskForButton

```java
public static int getMaskForButton​(int button)
```

A method to obtain a mask for any existing mouse button.
The returned mask may be used for different purposes. Following are some of them:

- mousePress(buttons)

and

mouseRelease(buttons)

as a

modifiers

parameter when creating a new

MouseEvent

instance

to check

modifiersEx

of existing

MouseEvent

**Parameters:** button

- is a number to represent a button starting from 1.
For example,

```java
int button = InputEvent.getMaskForButton(1);
```

will have the same meaning as

```java
int button = InputEvent.getMaskForButton(MouseEvent.BUTTON1);
```

because

MouseEvent.BUTTON1

equals to 1.
If a mouse has three enabled buttons(see

MouseInfo.getNumberOfButtons()

)
then the values from the left column passed into the method will return
corresponding values from the right column:

```java
button

returned mask

BUTTON1

BUTTON1_DOWN_MASK

BUTTON2

BUTTON2_DOWN_MASK

BUTTON3

BUTTON3_DOWN_MASK
```

If a mouse has more than three enabled buttons then more values
are admissible (4, 5, etc.). There is no assigned constants for these extended buttons.
The button masks for the extra buttons returned by this method have no assigned names like the
first three button masks.

This method has the following implementation restriction.
It returns masks for a limited number of buttons only. The maximum number is
implementation dependent and may vary.
This limit is defined by the relevant number
of buttons that may hypothetically exist on the mouse but it is greater than the

MouseInfo.getNumberOfButtons()

.
**Returns:** a mask for an existing mouse button.
**Throws:** IllegalArgumentException

- if

button

is less than zero or greater than the number
of button masks reserved for buttons
**Since:** 1.7
**See Also:** MouseInfo.getNumberOfButtons()

,

Toolkit.areExtraMouseButtonsEnabled()

,

getModifiers()

,

getModifiersEx()

---

#### getMaskForButton

public static int getMaskForButton​(int button)

A method to obtain a mask for any existing mouse button.
The returned mask may be used for different purposes. Following are some of them:

- mousePress(buttons)

and

mouseRelease(buttons)

as a

modifiers

parameter when creating a new

MouseEvent

instance

to check

modifiersEx

of existing

MouseEvent

mousePress(buttons)

and

mouseRelease(buttons)

as a

modifiers

parameter when creating a new

MouseEvent

instance

to check

modifiersEx

of existing

MouseEvent

int button = InputEvent.getMaskForButton(1);

int button = InputEvent.getMaskForButton(MouseEvent.BUTTON1);

button

returned mask

BUTTON1

BUTTON1_DOWN_MASK

BUTTON2

BUTTON2_DOWN_MASK

BUTTON3

BUTTON3_DOWN_MASK

This method has the following implementation restriction.
It returns masks for a limited number of buttons only. The maximum number is
implementation dependent and may vary.
This limit is defined by the relevant number
of buttons that may hypothetically exist on the mouse but it is greater than the

MouseInfo.getNumberOfButtons()

.

isShiftDown

```java
public boolean isShiftDown()
```

Returns whether or not the Shift modifier is down on this event.

**Returns:** whether or not the Shift modifier is down on this event

---

#### isShiftDown

public boolean isShiftDown()

Returns whether or not the Shift modifier is down on this event.

isControlDown

```java
public boolean isControlDown()
```

Returns whether or not the Control modifier is down on this event.

**Returns:** whether or not the Control modifier is down on this event

---

#### isControlDown

public boolean isControlDown()

Returns whether or not the Control modifier is down on this event.

isMetaDown

```java
public boolean isMetaDown()
```

Returns whether or not the Meta modifier is down on this event.

**Returns:** whether or not the Meta modifier is down on this event

---

#### isMetaDown

public boolean isMetaDown()

Returns whether or not the Meta modifier is down on this event.

isAltDown

```java
public boolean isAltDown()
```

Returns whether or not the Alt modifier is down on this event.

**Returns:** whether or not the Alt modifier is down on this event

---

#### isAltDown

public boolean isAltDown()

Returns whether or not the Alt modifier is down on this event.

isAltGraphDown

```java
public boolean isAltGraphDown()
```

Returns whether or not the AltGraph modifier is down on this event.

**Returns:** whether or not the AltGraph modifier is down on this event

---

#### isAltGraphDown

public boolean isAltGraphDown()

Returns whether or not the AltGraph modifier is down on this event.

getWhen

```java
public long getWhen()
```

Returns the difference in milliseconds between the timestamp of when this event occurred and
midnight, January 1, 1970 UTC.

**Returns:** the difference in milliseconds between the timestamp and midnight, January 1, 1970 UTC

---

#### getWhen

public long getWhen()

Returns the difference in milliseconds between the timestamp of when this event occurred and
midnight, January 1, 1970 UTC.

getModifiers

```java
@Deprecated
(
since
="9")
public int getModifiers()
```

Deprecated.

It is recommended that extended modifier keys and

getModifiersEx()

be used instead

Returns the modifier mask for this event.

**Returns:** the modifier mask for this event

---

#### getModifiers

@Deprecated

(

since

="9")
public int getModifiers()

Returns the modifier mask for this event.

getModifiersEx

```java
public int getModifiersEx()
```

Returns the extended modifier mask for this event.

Extended modifiers are the modifiers that ends with the _DOWN_MASK suffix,
such as ALT_DOWN_MASK, BUTTON1_DOWN_MASK, and others.

Extended modifiers represent the state of all modal keys,
such as ALT, CTRL, META, and the mouse buttons just after
the event occurred.

For example, if the user presses

button 1

followed by

button 2

, and then releases them in the same order,
the following sequence of events is generated:

```java
MOUSE_PRESSED
:
BUTTON1_DOWN_MASK

MOUSE_PRESSED
:
BUTTON1_DOWN_MASK | BUTTON2_DOWN_MASK

MOUSE_RELEASED
:
BUTTON2_DOWN_MASK

MOUSE_CLICKED
:
BUTTON2_DOWN_MASK

MOUSE_RELEASED
:

MOUSE_CLICKED
:
```

It is not recommended to compare the return value of this method
using

==

because new modifiers can be added in the future.
For example, the appropriate way to check that SHIFT and BUTTON1 are
down, but CTRL is up is demonstrated by the following code:

```java
int onmask = SHIFT_DOWN_MASK | BUTTON1_DOWN_MASK;
int offmask = CTRL_DOWN_MASK;
if ((event.getModifiersEx() & (onmask | offmask)) == onmask) {
...
}
```

The above code will work even if new modifiers are added.

**Returns:** the extended modifier mask for this event
**Since:** 1.4

---

#### getModifiersEx

public int getModifiersEx()

Returns the extended modifier mask for this event.

Extended modifiers are the modifiers that ends with the _DOWN_MASK suffix,
such as ALT_DOWN_MASK, BUTTON1_DOWN_MASK, and others.

Extended modifiers represent the state of all modal keys,
such as ALT, CTRL, META, and the mouse buttons just after
the event occurred.

For example, if the user presses

button 1

followed by

button 2

, and then releases them in the same order,
the following sequence of events is generated:

```java
MOUSE_PRESSED
:
BUTTON1_DOWN_MASK

MOUSE_PRESSED
:
BUTTON1_DOWN_MASK | BUTTON2_DOWN_MASK

MOUSE_RELEASED
:
BUTTON2_DOWN_MASK

MOUSE_CLICKED
:
BUTTON2_DOWN_MASK

MOUSE_RELEASED
:

MOUSE_CLICKED
:
```

It is not recommended to compare the return value of this method
using

==

because new modifiers can be added in the future.
For example, the appropriate way to check that SHIFT and BUTTON1 are
down, but CTRL is up is demonstrated by the following code:

```java
int onmask = SHIFT_DOWN_MASK | BUTTON1_DOWN_MASK;
int offmask = CTRL_DOWN_MASK;
if ((event.getModifiersEx() & (onmask | offmask)) == onmask) {
...
}
```

The above code will work even if new modifiers are added.

Extended modifiers are the modifiers that ends with the _DOWN_MASK suffix,
such as ALT_DOWN_MASK, BUTTON1_DOWN_MASK, and others.

Extended modifiers represent the state of all modal keys,
such as ALT, CTRL, META, and the mouse buttons just after
the event occurred.

For example, if the user presses

button 1

followed by

button 2

, and then releases them in the same order,
the following sequence of events is generated:

```java
MOUSE_PRESSED
:
BUTTON1_DOWN_MASK

MOUSE_PRESSED
:
BUTTON1_DOWN_MASK | BUTTON2_DOWN_MASK

MOUSE_RELEASED
:
BUTTON2_DOWN_MASK

MOUSE_CLICKED
:
BUTTON2_DOWN_MASK

MOUSE_RELEASED
:

MOUSE_CLICKED
:
```

It is not recommended to compare the return value of this method
using

==

because new modifiers can be added in the future.
For example, the appropriate way to check that SHIFT and BUTTON1 are
down, but CTRL is up is demonstrated by the following code:

```java
int onmask = SHIFT_DOWN_MASK | BUTTON1_DOWN_MASK;
int offmask = CTRL_DOWN_MASK;
if ((event.getModifiersEx() & (onmask | offmask)) == onmask) {
...
}
```

The above code will work even if new modifiers are added.

Extended modifiers represent the state of all modal keys,
such as ALT, CTRL, META, and the mouse buttons just after
the event occurred.

For example, if the user presses

button 1

followed by

button 2

, and then releases them in the same order,
the following sequence of events is generated:

```java
MOUSE_PRESSED
:
BUTTON1_DOWN_MASK

MOUSE_PRESSED
:
BUTTON1_DOWN_MASK | BUTTON2_DOWN_MASK

MOUSE_RELEASED
:
BUTTON2_DOWN_MASK

MOUSE_CLICKED
:
BUTTON2_DOWN_MASK

MOUSE_RELEASED
:

MOUSE_CLICKED
:
```

It is not recommended to compare the return value of this method
using

==

because new modifiers can be added in the future.
For example, the appropriate way to check that SHIFT and BUTTON1 are
down, but CTRL is up is demonstrated by the following code:

```java
int onmask = SHIFT_DOWN_MASK | BUTTON1_DOWN_MASK;
int offmask = CTRL_DOWN_MASK;
if ((event.getModifiersEx() & (onmask | offmask)) == onmask) {
...
}
```

The above code will work even if new modifiers are added.

For example, if the user presses

button 1

followed by

button 2

, and then releases them in the same order,
the following sequence of events is generated:

```java
MOUSE_PRESSED
:
BUTTON1_DOWN_MASK

MOUSE_PRESSED
:
BUTTON1_DOWN_MASK | BUTTON2_DOWN_MASK

MOUSE_RELEASED
:
BUTTON2_DOWN_MASK

MOUSE_CLICKED
:
BUTTON2_DOWN_MASK

MOUSE_RELEASED
:

MOUSE_CLICKED
:
```

It is not recommended to compare the return value of this method
using

==

because new modifiers can be added in the future.
For example, the appropriate way to check that SHIFT and BUTTON1 are
down, but CTRL is up is demonstrated by the following code:

```java
int onmask = SHIFT_DOWN_MASK | BUTTON1_DOWN_MASK;
int offmask = CTRL_DOWN_MASK;
if ((event.getModifiersEx() & (onmask | offmask)) == onmask) {
...
}
```

The above code will work even if new modifiers are added.

MOUSE_PRESSED

:

BUTTON1_DOWN_MASK

MOUSE_PRESSED

:

BUTTON1_DOWN_MASK | BUTTON2_DOWN_MASK

MOUSE_RELEASED

:

BUTTON2_DOWN_MASK

MOUSE_CLICKED

:

BUTTON2_DOWN_MASK

MOUSE_RELEASED

:

MOUSE_CLICKED

:

It is not recommended to compare the return value of this method
using

==

because new modifiers can be added in the future.
For example, the appropriate way to check that SHIFT and BUTTON1 are
down, but CTRL is up is demonstrated by the following code:

```java
int onmask = SHIFT_DOWN_MASK | BUTTON1_DOWN_MASK;
int offmask = CTRL_DOWN_MASK;
if ((event.getModifiersEx() & (onmask | offmask)) == onmask) {
...
}
```

The above code will work even if new modifiers are added.

int onmask = SHIFT_DOWN_MASK | BUTTON1_DOWN_MASK;
int offmask = CTRL_DOWN_MASK;
if ((event.getModifiersEx() & (onmask | offmask)) == onmask) {
...
}

consume

```java
public void consume()
```

Consumes this event so that it will not be processed
in the default manner by the source which originated it.

**Overrides:** consume

in class

AWTEvent

---

#### consume

public void consume()

Consumes this event so that it will not be processed
in the default manner by the source which originated it.

isConsumed

```java
public boolean isConsumed()
```

Returns whether or not this event has been consumed.

**Overrides:** isConsumed

in class

AWTEvent
**Returns:** whether or not this event has been consumed
**See Also:** consume()

---

#### isConsumed

public boolean isConsumed()

Returns whether or not this event has been consumed.

getModifiersExText

```java
public static
String
getModifiersExText​(int modifiers)
```

Returns a String describing the extended modifier keys and
mouse buttons, such as "Shift", "Button1", or "Ctrl+Shift".
These strings can be localized by changing the

awt.properties

file.

Note that passing negative parameter is incorrect,
and will cause the returning an unspecified string.
Zero parameter means that no modifiers were passed and will
cause the returning an empty string.

**Parameters:** modifiers

- a modifier mask describing the extended
modifier keys and mouse buttons for the event
**Returns:** a String describing the extended modifier keys and
mouse buttons
**Since:** 1.4

---

#### getModifiersExText

public static

String

getModifiersExText​(int modifiers)

Returns a String describing the extended modifier keys and
mouse buttons, such as "Shift", "Button1", or "Ctrl+Shift".
These strings can be localized by changing the

awt.properties

file.

Note that passing negative parameter is incorrect,
and will cause the returning an unspecified string.
Zero parameter means that no modifiers were passed and will
cause the returning an empty string.

Note that passing negative parameter is incorrect,
and will cause the returning an unspecified string.
Zero parameter means that no modifiers were passed and will
cause the returning an empty string.

---

