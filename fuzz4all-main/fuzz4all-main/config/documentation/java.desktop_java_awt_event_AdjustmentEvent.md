# Class AdjustmentEvent

**Source:** `java.desktop\java\awt\event\AdjustmentEvent.html`

### Class Description

```java
public class
AdjustmentEvent

extends
AWTEvent
```

The adjustment event emitted by Adjustable objects like

Scrollbar

and

ScrollPane

.
When the user changes the value of the scrolling component,
it receives an instance of

AdjustmentEvent

.

An unspecified behavior will be caused if the

id

parameter
of any particular

AdjustmentEvent

instance is not
in the range from

ADJUSTMENT_FIRST

to

ADJUSTMENT_LAST

.

The

type

of any

AdjustmentEvent

instance takes one of the following
values:

- UNIT_INCREMENT

UNIT_DECREMENT

BLOCK_INCREMENT

BLOCK_DECREMENT

TRACK

Assigning the value different from listed above will cause an unspecified behavior.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final int ADJUSTMENT_FIRST

Marks the first integer id for the range of adjustment event ids.

**See Also:**
- Constant Field Values

---

#### public static final int ADJUSTMENT_LAST

Marks the last integer id for the range of adjustment event ids.

**See Also:**
- Constant Field Values

---

#### public static final int ADJUSTMENT_VALUE_CHANGED

The adjustment value changed event.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int UNIT_INCREMENT

The unit increment adjustment type.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int UNIT_DECREMENT

The unit decrement adjustment type.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int BLOCK_DECREMENT

The block decrement adjustment type.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int BLOCK_INCREMENT

The block increment adjustment type.

**See Also:**
- Constant Field Values

---

#### @Native

public static final int TRACK

The absolute tracking adjustment type.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public AdjustmentEvent​(
Adjustable
source,
int id,
int type,
int value)

Constructs an

AdjustmentEvent

object with the
specified

Adjustable

source, event type,
adjustment type, and value.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:**
- source

- The

Adjustable

object where the
event originated
- id

- An integer indicating the type of event.
For information on allowable values, see
the class description for

AdjustmentEvent
- type

- An integer indicating the adjustment type.
For information on allowable values, see
the class description for

AdjustmentEvent
- value

- The current value of the adjustment

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

getAdjustmentType()

,

getValue()

---

#### public AdjustmentEvent​(
Adjustable
source,
int id,
int type,
int value,
boolean isAdjusting)

Constructs an

AdjustmentEvent

object with the
specified Adjustable source, event type, adjustment type, and value.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:**
- source

- The

Adjustable

object where the
event originated
- id

- An integer indicating the type of event.
For information on allowable values, see
the class description for

AdjustmentEvent
- type

- An integer indicating the adjustment type.
For information on allowable values, see
the class description for

AdjustmentEvent
- value

- The current value of the adjustment
- isAdjusting

- A boolean that equals

true

if the event is one
of a series of multiple adjusting events,
otherwise

false

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

getAdjustmentType()

,

getValue()

,

getValueIsAdjusting()

**Since:**
- 1.4

---

### Method Details

#### public
Adjustable
getAdjustable()

Returns the

Adjustable

object where this event originated.

**Returns:**
- the

Adjustable

object where this event originated

---

#### public int getValue()

Returns the current value in the adjustment event.

**Returns:**
- the current value in the adjustment event

---

#### public int getAdjustmentType()

Returns the type of adjustment which caused the value changed
event. It will have one of the following values:

- UNIT_INCREMENT

UNIT_DECREMENT

BLOCK_INCREMENT

BLOCK_DECREMENT

TRACK

**Returns:**
- one of the adjustment values listed above

---

#### public boolean getValueIsAdjusting()

Returns

true

if this is one of multiple
adjustment events.

**Returns:**
- true

if this is one of multiple
adjustment events, otherwise returns

false

**Since:**
- 1.4

---

### Additional Sections

#### Class AdjustmentEvent

java.lang.Object

- java.util.EventObject
- - java.awt.AWTEvent
- - java.awt.event.AdjustmentEvent

java.util.EventObject

- java.awt.AWTEvent
- - java.awt.event.AdjustmentEvent

java.awt.AWTEvent

- java.awt.event.AdjustmentEvent

java.awt.event.AdjustmentEvent

**All Implemented Interfaces:** Serializable

```java
public class
AdjustmentEvent

extends
AWTEvent
```

The adjustment event emitted by Adjustable objects like

Scrollbar

and

ScrollPane

.
When the user changes the value of the scrolling component,
it receives an instance of

AdjustmentEvent

.

An unspecified behavior will be caused if the

id

parameter
of any particular

AdjustmentEvent

instance is not
in the range from

ADJUSTMENT_FIRST

to

ADJUSTMENT_LAST

.

The

type

of any

AdjustmentEvent

instance takes one of the following
values:

- UNIT_INCREMENT

UNIT_DECREMENT

BLOCK_INCREMENT

BLOCK_DECREMENT

TRACK

Assigning the value different from listed above will cause an unspecified behavior.

**Since:** 1.1
**See Also:** Adjustable

,

AdjustmentListener

,

Serialized Form

public class

AdjustmentEvent

extends

AWTEvent

The adjustment event emitted by Adjustable objects like

Scrollbar

and

ScrollPane

.
When the user changes the value of the scrolling component,
it receives an instance of

AdjustmentEvent

.

An unspecified behavior will be caused if the

id

parameter
of any particular

AdjustmentEvent

instance is not
in the range from

ADJUSTMENT_FIRST

to

ADJUSTMENT_LAST

.

The

type

of any

AdjustmentEvent

instance takes one of the following
values:

- UNIT_INCREMENT

UNIT_DECREMENT

BLOCK_INCREMENT

BLOCK_DECREMENT

TRACK

Assigning the value different from listed above will cause an unspecified behavior.

An unspecified behavior will be caused if the

id

parameter
of any particular

AdjustmentEvent

instance is not
in the range from

ADJUSTMENT_FIRST

to

ADJUSTMENT_LAST

.

The

type

of any

AdjustmentEvent

instance takes one of the following
values:

- UNIT_INCREMENT

UNIT_DECREMENT

BLOCK_INCREMENT

BLOCK_DECREMENT

TRACK

Assigning the value different from listed above will cause an unspecified behavior.

The

type

of any

AdjustmentEvent

instance takes one of the following
values:

- UNIT_INCREMENT

UNIT_DECREMENT

BLOCK_INCREMENT

BLOCK_DECREMENT

TRACK

Assigning the value different from listed above will cause an unspecified behavior.

UNIT_INCREMENT

UNIT_DECREMENT

BLOCK_INCREMENT

BLOCK_DECREMENT

TRACK

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ADJUSTMENT_FIRST

Marks the first integer id for the range of adjustment event ids.

static int

ADJUSTMENT_LAST

Marks the last integer id for the range of adjustment event ids.

static int

ADJUSTMENT_VALUE_CHANGED

The adjustment value changed event.

static int

BLOCK_DECREMENT

The block decrement adjustment type.

static int

BLOCK_INCREMENT

The block increment adjustment type.

static int

TRACK

The absolute tracking adjustment type.

static int

UNIT_DECREMENT

The unit decrement adjustment type.

static int

UNIT_INCREMENT

The unit increment adjustment type.

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

AdjustmentEvent

​(

Adjustable

source,
int id,
int type,
int value)

Constructs an

AdjustmentEvent

object with the
specified

Adjustable

source, event type,
adjustment type, and value.

AdjustmentEvent

​(

Adjustable

source,
int id,
int type,
int value,
boolean isAdjusting)

Constructs an

AdjustmentEvent

object with the
specified Adjustable source, event type, adjustment type, and value.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Adjustable

getAdjustable

()

Returns the

Adjustable

object where this event originated.

int

getAdjustmentType

()

Returns the type of adjustment which caused the value changed
event.

int

getValue

()

Returns the current value in the adjustment event.

boolean

getValueIsAdjusting

()

Returns

true

if this is one of multiple
adjustment events.

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

ADJUSTMENT_FIRST

Marks the first integer id for the range of adjustment event ids.

static int

ADJUSTMENT_LAST

Marks the last integer id for the range of adjustment event ids.

static int

ADJUSTMENT_VALUE_CHANGED

The adjustment value changed event.

static int

BLOCK_DECREMENT

The block decrement adjustment type.

static int

BLOCK_INCREMENT

The block increment adjustment type.

static int

TRACK

The absolute tracking adjustment type.

static int

UNIT_DECREMENT

The unit decrement adjustment type.

static int

UNIT_INCREMENT

The unit increment adjustment type.

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

Marks the first integer id for the range of adjustment event ids.

Marks the last integer id for the range of adjustment event ids.

The adjustment value changed event.

The block decrement adjustment type.

The block increment adjustment type.

The absolute tracking adjustment type.

The unit decrement adjustment type.

The unit increment adjustment type.

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

AdjustmentEvent

​(

Adjustable

source,
int id,
int type,
int value)

Constructs an

AdjustmentEvent

object with the
specified

Adjustable

source, event type,
adjustment type, and value.

AdjustmentEvent

​(

Adjustable

source,
int id,
int type,
int value,
boolean isAdjusting)

Constructs an

AdjustmentEvent

object with the
specified Adjustable source, event type, adjustment type, and value.

---

#### Constructor Summary

Constructs an

AdjustmentEvent

object with the
specified

Adjustable

source, event type,
adjustment type, and value.

Constructs an

AdjustmentEvent

object with the
specified Adjustable source, event type, adjustment type, and value.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Adjustable

getAdjustable

()

Returns the

Adjustable

object where this event originated.

int

getAdjustmentType

()

Returns the type of adjustment which caused the value changed
event.

int

getValue

()

Returns the current value in the adjustment event.

boolean

getValueIsAdjusting

()

Returns

true

if this is one of multiple
adjustment events.

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

Returns the

Adjustable

object where this event originated.

Returns the type of adjustment which caused the value changed
event.

Returns the current value in the adjustment event.

Returns

true

if this is one of multiple
adjustment events.

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

- ADJUSTMENT_FIRST

```java
public static final int ADJUSTMENT_FIRST
```

Marks the first integer id for the range of adjustment event ids.

**See Also:** Constant Field Values

- ADJUSTMENT_LAST

```java
public static final int ADJUSTMENT_LAST
```

Marks the last integer id for the range of adjustment event ids.

**See Also:** Constant Field Values

- ADJUSTMENT_VALUE_CHANGED

```java
public static final int ADJUSTMENT_VALUE_CHANGED
```

The adjustment value changed event.

**See Also:** Constant Field Values

- UNIT_INCREMENT

```java
@Native

public static final int UNIT_INCREMENT
```

The unit increment adjustment type.

**See Also:** Constant Field Values

- UNIT_DECREMENT

```java
@Native

public static final int UNIT_DECREMENT
```

The unit decrement adjustment type.

**See Also:** Constant Field Values

- BLOCK_DECREMENT

```java
@Native

public static final int BLOCK_DECREMENT
```

The block decrement adjustment type.

**See Also:** Constant Field Values

- BLOCK_INCREMENT

```java
@Native

public static final int BLOCK_INCREMENT
```

The block increment adjustment type.

**See Also:** Constant Field Values

- TRACK

```java
@Native

public static final int TRACK
```

The absolute tracking adjustment type.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- AdjustmentEvent

```java
public AdjustmentEvent​(
Adjustable
source,
int id,
int type,
int value)
```

Constructs an

AdjustmentEvent

object with the
specified

Adjustable

source, event type,
adjustment type, and value.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- The

Adjustable

object where the
event originated
**Parameters:** id

- An integer indicating the type of event.
For information on allowable values, see
the class description for

AdjustmentEvent
**Parameters:** type

- An integer indicating the adjustment type.
For information on allowable values, see
the class description for

AdjustmentEvent
**Parameters:** value

- The current value of the adjustment
**Throws:** IllegalArgumentException

- if

source

is null
**See Also:** EventObject.getSource()

,

AWTEvent.getID()

,

getAdjustmentType()

,

getValue()

- AdjustmentEvent

```java
public AdjustmentEvent​(
Adjustable
source,
int id,
int type,
int value,
boolean isAdjusting)
```

Constructs an

AdjustmentEvent

object with the
specified Adjustable source, event type, adjustment type, and value.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- The

Adjustable

object where the
event originated
**Parameters:** id

- An integer indicating the type of event.
For information on allowable values, see
the class description for

AdjustmentEvent
**Parameters:** type

- An integer indicating the adjustment type.
For information on allowable values, see
the class description for

AdjustmentEvent
**Parameters:** value

- The current value of the adjustment
**Parameters:** isAdjusting

- A boolean that equals

true

if the event is one
of a series of multiple adjusting events,
otherwise

false
**Throws:** IllegalArgumentException

- if

source

is null
**Since:** 1.4
**See Also:** EventObject.getSource()

,

AWTEvent.getID()

,

getAdjustmentType()

,

getValue()

,

getValueIsAdjusting()

============ METHOD DETAIL ==========

- Method Detail

- getAdjustable

```java
public
Adjustable
getAdjustable()
```

Returns the

Adjustable

object where this event originated.

**Returns:** the

Adjustable

object where this event originated

- getValue

```java
public int getValue()
```

Returns the current value in the adjustment event.

**Returns:** the current value in the adjustment event

- getAdjustmentType

```java
public int getAdjustmentType()
```

Returns the type of adjustment which caused the value changed
event. It will have one of the following values:

- UNIT_INCREMENT

UNIT_DECREMENT

BLOCK_INCREMENT

BLOCK_DECREMENT

TRACK

**Returns:** one of the adjustment values listed above

- getValueIsAdjusting

```java
public boolean getValueIsAdjusting()
```

Returns

true

if this is one of multiple
adjustment events.

**Returns:** true

if this is one of multiple
adjustment events, otherwise returns

false
**Since:** 1.4

Field Detail

- ADJUSTMENT_FIRST

```java
public static final int ADJUSTMENT_FIRST
```

Marks the first integer id for the range of adjustment event ids.

**See Also:** Constant Field Values

- ADJUSTMENT_LAST

```java
public static final int ADJUSTMENT_LAST
```

Marks the last integer id for the range of adjustment event ids.

**See Also:** Constant Field Values

- ADJUSTMENT_VALUE_CHANGED

```java
public static final int ADJUSTMENT_VALUE_CHANGED
```

The adjustment value changed event.

**See Also:** Constant Field Values

- UNIT_INCREMENT

```java
@Native

public static final int UNIT_INCREMENT
```

The unit increment adjustment type.

**See Also:** Constant Field Values

- UNIT_DECREMENT

```java
@Native

public static final int UNIT_DECREMENT
```

The unit decrement adjustment type.

**See Also:** Constant Field Values

- BLOCK_DECREMENT

```java
@Native

public static final int BLOCK_DECREMENT
```

The block decrement adjustment type.

**See Also:** Constant Field Values

- BLOCK_INCREMENT

```java
@Native

public static final int BLOCK_INCREMENT
```

The block increment adjustment type.

**See Also:** Constant Field Values

- TRACK

```java
@Native

public static final int TRACK
```

The absolute tracking adjustment type.

**See Also:** Constant Field Values

---

#### Field Detail

ADJUSTMENT_FIRST

```java
public static final int ADJUSTMENT_FIRST
```

Marks the first integer id for the range of adjustment event ids.

**See Also:** Constant Field Values

---

#### ADJUSTMENT_FIRST

public static final int ADJUSTMENT_FIRST

Marks the first integer id for the range of adjustment event ids.

ADJUSTMENT_LAST

```java
public static final int ADJUSTMENT_LAST
```

Marks the last integer id for the range of adjustment event ids.

**See Also:** Constant Field Values

---

#### ADJUSTMENT_LAST

public static final int ADJUSTMENT_LAST

Marks the last integer id for the range of adjustment event ids.

ADJUSTMENT_VALUE_CHANGED

```java
public static final int ADJUSTMENT_VALUE_CHANGED
```

The adjustment value changed event.

**See Also:** Constant Field Values

---

#### ADJUSTMENT_VALUE_CHANGED

public static final int ADJUSTMENT_VALUE_CHANGED

The adjustment value changed event.

UNIT_INCREMENT

```java
@Native

public static final int UNIT_INCREMENT
```

The unit increment adjustment type.

**See Also:** Constant Field Values

---

#### UNIT_INCREMENT

@Native

public static final int UNIT_INCREMENT

The unit increment adjustment type.

UNIT_DECREMENT

```java
@Native

public static final int UNIT_DECREMENT
```

The unit decrement adjustment type.

**See Also:** Constant Field Values

---

#### UNIT_DECREMENT

@Native

public static final int UNIT_DECREMENT

The unit decrement adjustment type.

BLOCK_DECREMENT

```java
@Native

public static final int BLOCK_DECREMENT
```

The block decrement adjustment type.

**See Also:** Constant Field Values

---

#### BLOCK_DECREMENT

@Native

public static final int BLOCK_DECREMENT

The block decrement adjustment type.

BLOCK_INCREMENT

```java
@Native

public static final int BLOCK_INCREMENT
```

The block increment adjustment type.

**See Also:** Constant Field Values

---

#### BLOCK_INCREMENT

@Native

public static final int BLOCK_INCREMENT

The block increment adjustment type.

TRACK

```java
@Native

public static final int TRACK
```

The absolute tracking adjustment type.

**See Also:** Constant Field Values

---

#### TRACK

@Native

public static final int TRACK

The absolute tracking adjustment type.

Constructor Detail

- AdjustmentEvent

```java
public AdjustmentEvent​(
Adjustable
source,
int id,
int type,
int value)
```

Constructs an

AdjustmentEvent

object with the
specified

Adjustable

source, event type,
adjustment type, and value.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- The

Adjustable

object where the
event originated
**Parameters:** id

- An integer indicating the type of event.
For information on allowable values, see
the class description for

AdjustmentEvent
**Parameters:** type

- An integer indicating the adjustment type.
For information on allowable values, see
the class description for

AdjustmentEvent
**Parameters:** value

- The current value of the adjustment
**Throws:** IllegalArgumentException

- if

source

is null
**See Also:** EventObject.getSource()

,

AWTEvent.getID()

,

getAdjustmentType()

,

getValue()

- AdjustmentEvent

```java
public AdjustmentEvent​(
Adjustable
source,
int id,
int type,
int value,
boolean isAdjusting)
```

Constructs an

AdjustmentEvent

object with the
specified Adjustable source, event type, adjustment type, and value.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- The

Adjustable

object where the
event originated
**Parameters:** id

- An integer indicating the type of event.
For information on allowable values, see
the class description for

AdjustmentEvent
**Parameters:** type

- An integer indicating the adjustment type.
For information on allowable values, see
the class description for

AdjustmentEvent
**Parameters:** value

- The current value of the adjustment
**Parameters:** isAdjusting

- A boolean that equals

true

if the event is one
of a series of multiple adjusting events,
otherwise

false
**Throws:** IllegalArgumentException

- if

source

is null
**Since:** 1.4
**See Also:** EventObject.getSource()

,

AWTEvent.getID()

,

getAdjustmentType()

,

getValue()

,

getValueIsAdjusting()

---

#### Constructor Detail

AdjustmentEvent

```java
public AdjustmentEvent​(
Adjustable
source,
int id,
int type,
int value)
```

Constructs an

AdjustmentEvent

object with the
specified

Adjustable

source, event type,
adjustment type, and value.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- The

Adjustable

object where the
event originated
**Parameters:** id

- An integer indicating the type of event.
For information on allowable values, see
the class description for

AdjustmentEvent
**Parameters:** type

- An integer indicating the adjustment type.
For information on allowable values, see
the class description for

AdjustmentEvent
**Parameters:** value

- The current value of the adjustment
**Throws:** IllegalArgumentException

- if

source

is null
**See Also:** EventObject.getSource()

,

AWTEvent.getID()

,

getAdjustmentType()

,

getValue()

---

#### AdjustmentEvent

public AdjustmentEvent​(

Adjustable

source,
int id,
int type,
int value)

Constructs an

AdjustmentEvent

object with the
specified

Adjustable

source, event type,
adjustment type, and value.

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

AdjustmentEvent

```java
public AdjustmentEvent​(
Adjustable
source,
int id,
int type,
int value,
boolean isAdjusting)
```

Constructs an

AdjustmentEvent

object with the
specified Adjustable source, event type, adjustment type, and value.

This method throws an

IllegalArgumentException

if

source

is

null

.

**Parameters:** source

- The

Adjustable

object where the
event originated
**Parameters:** id

- An integer indicating the type of event.
For information on allowable values, see
the class description for

AdjustmentEvent
**Parameters:** type

- An integer indicating the adjustment type.
For information on allowable values, see
the class description for

AdjustmentEvent
**Parameters:** value

- The current value of the adjustment
**Parameters:** isAdjusting

- A boolean that equals

true

if the event is one
of a series of multiple adjusting events,
otherwise

false
**Throws:** IllegalArgumentException

- if

source

is null
**Since:** 1.4
**See Also:** EventObject.getSource()

,

AWTEvent.getID()

,

getAdjustmentType()

,

getValue()

,

getValueIsAdjusting()

---

#### AdjustmentEvent

public AdjustmentEvent​(

Adjustable

source,
int id,
int type,
int value,
boolean isAdjusting)

Constructs an

AdjustmentEvent

object with the
specified Adjustable source, event type, adjustment type, and value.

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

- getAdjustable

```java
public
Adjustable
getAdjustable()
```

Returns the

Adjustable

object where this event originated.

**Returns:** the

Adjustable

object where this event originated

- getValue

```java
public int getValue()
```

Returns the current value in the adjustment event.

**Returns:** the current value in the adjustment event

- getAdjustmentType

```java
public int getAdjustmentType()
```

Returns the type of adjustment which caused the value changed
event. It will have one of the following values:

- UNIT_INCREMENT

UNIT_DECREMENT

BLOCK_INCREMENT

BLOCK_DECREMENT

TRACK

**Returns:** one of the adjustment values listed above

- getValueIsAdjusting

```java
public boolean getValueIsAdjusting()
```

Returns

true

if this is one of multiple
adjustment events.

**Returns:** true

if this is one of multiple
adjustment events, otherwise returns

false
**Since:** 1.4

---

#### Method Detail

getAdjustable

```java
public
Adjustable
getAdjustable()
```

Returns the

Adjustable

object where this event originated.

**Returns:** the

Adjustable

object where this event originated

---

#### getAdjustable

public

Adjustable

getAdjustable()

Returns the

Adjustable

object where this event originated.

getValue

```java
public int getValue()
```

Returns the current value in the adjustment event.

**Returns:** the current value in the adjustment event

---

#### getValue

public int getValue()

Returns the current value in the adjustment event.

getAdjustmentType

```java
public int getAdjustmentType()
```

Returns the type of adjustment which caused the value changed
event. It will have one of the following values:

- UNIT_INCREMENT

UNIT_DECREMENT

BLOCK_INCREMENT

BLOCK_DECREMENT

TRACK

**Returns:** one of the adjustment values listed above

---

#### getAdjustmentType

public int getAdjustmentType()

Returns the type of adjustment which caused the value changed
event. It will have one of the following values:

- UNIT_INCREMENT

UNIT_DECREMENT

BLOCK_INCREMENT

BLOCK_DECREMENT

TRACK

UNIT_INCREMENT

UNIT_DECREMENT

BLOCK_INCREMENT

BLOCK_DECREMENT

TRACK

getValueIsAdjusting

```java
public boolean getValueIsAdjusting()
```

Returns

true

if this is one of multiple
adjustment events.

**Returns:** true

if this is one of multiple
adjustment events, otherwise returns

false
**Since:** 1.4

---

#### getValueIsAdjusting

public boolean getValueIsAdjusting()

Returns

true

if this is one of multiple
adjustment events.

---

