# Class DragSourceEvent

**Source:** `java.desktop\java\awt\dnd\DragSourceEvent.html`

### Class Description

```java
public class
DragSourceEvent

extends
EventObject
```

This class is the base class for

DragSourceDragEvent

and

DragSourceDropEvent

.

DragSourceEvent

s are generated whenever the drag enters, moves
over, or exits a drop site, when the drop action changes, and when the drag
ends. The location for the generated

DragSourceEvent

specifies
the mouse cursor location in screen coordinates at the moment this event
occurred.

In a multi-screen environment without a virtual device, the cursor location is
specified in the coordinate system of the

initiator

GraphicsConfiguration

. The

initiator

GraphicsConfiguration

is the

GraphicsConfiguration

of the

Component

on which the drag gesture for the current drag
operation was recognized. If the cursor location is outside the bounds of
the initiator

GraphicsConfiguration

, the reported coordinates are
clipped to fit within the bounds of that

GraphicsConfiguration

.

In a multi-screen environment with a virtual device, the location is specified
in the corresponding virtual coordinate system. If the cursor location is
outside the bounds of the virtual device the reported coordinates are
clipped to fit within the bounds of the virtual device.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public DragSourceEvent​(
DragSourceContext
dsc)

Construct a

DragSourceEvent

given a specified

DragSourceContext

.
The coordinates for this

DragSourceEvent

are not specified, so

getLocation

will return

null

for this event.

**Parameters:**
- dsc

- the

DragSourceContext

**Throws:**
- IllegalArgumentException

- if

dsc

is

null

.

**See Also:**
- getLocation()

---

#### public DragSourceEvent​(
DragSourceContext
dsc,
int x,
int y)

Construct a

DragSourceEvent

given a specified

DragSourceContext

, and coordinates of the cursor
location.

**Parameters:**
- dsc

- the

DragSourceContext
- x

- the horizontal coordinate for the cursor location
- y

- the vertical coordinate for the cursor location

**Throws:**
- IllegalArgumentException

- if

dsc

is

null

.

**Since:**
- 1.4

---

### Method Details

#### public
DragSourceContext
getDragSourceContext()

This method returns the

DragSourceContext

that
originated the event.

**Returns:**
- the

DragSourceContext

that originated the event

---

#### public
Point
getLocation()

This method returns a

Point

indicating the cursor
location in screen coordinates at the moment this event occurred, or

null

if the cursor location is not specified for this
event.

**Returns:**
- the

Point

indicating the cursor location
or

null

if the cursor location is not specified

**Since:**
- 1.4

---

#### public int getX()

This method returns the horizontal coordinate of the cursor location in
screen coordinates at the moment this event occurred, or zero if the
cursor location is not specified for this event.

**Returns:**
- an integer indicating the horizontal coordinate of the cursor
location or zero if the cursor location is not specified

**Since:**
- 1.4

---

#### public int getY()

This method returns the vertical coordinate of the cursor location in
screen coordinates at the moment this event occurred, or zero if the
cursor location is not specified for this event.

**Returns:**
- an integer indicating the vertical coordinate of the cursor
location or zero if the cursor location is not specified

**Since:**
- 1.4

---

### Additional Sections

#### Class DragSourceEvent

java.lang.Object

- java.util.EventObject
- - java.awt.dnd.DragSourceEvent

java.util.EventObject

- java.awt.dnd.DragSourceEvent

java.awt.dnd.DragSourceEvent

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** DragSourceDragEvent

,

DragSourceDropEvent

```java
public class
DragSourceEvent

extends
EventObject
```

This class is the base class for

DragSourceDragEvent

and

DragSourceDropEvent

.

DragSourceEvent

s are generated whenever the drag enters, moves
over, or exits a drop site, when the drop action changes, and when the drag
ends. The location for the generated

DragSourceEvent

specifies
the mouse cursor location in screen coordinates at the moment this event
occurred.

In a multi-screen environment without a virtual device, the cursor location is
specified in the coordinate system of the

initiator

GraphicsConfiguration

. The

initiator

GraphicsConfiguration

is the

GraphicsConfiguration

of the

Component

on which the drag gesture for the current drag
operation was recognized. If the cursor location is outside the bounds of
the initiator

GraphicsConfiguration

, the reported coordinates are
clipped to fit within the bounds of that

GraphicsConfiguration

.

In a multi-screen environment with a virtual device, the location is specified
in the corresponding virtual coordinate system. If the cursor location is
outside the bounds of the virtual device the reported coordinates are
clipped to fit within the bounds of the virtual device.

**Since:** 1.2
**See Also:** Serialized Form

public class

DragSourceEvent

extends

EventObject

This class is the base class for

DragSourceDragEvent

and

DragSourceDropEvent

.

DragSourceEvent

s are generated whenever the drag enters, moves
over, or exits a drop site, when the drop action changes, and when the drag
ends. The location for the generated

DragSourceEvent

specifies
the mouse cursor location in screen coordinates at the moment this event
occurred.

In a multi-screen environment without a virtual device, the cursor location is
specified in the coordinate system of the

initiator

GraphicsConfiguration

. The

initiator

GraphicsConfiguration

is the

GraphicsConfiguration

of the

Component

on which the drag gesture for the current drag
operation was recognized. If the cursor location is outside the bounds of
the initiator

GraphicsConfiguration

, the reported coordinates are
clipped to fit within the bounds of that

GraphicsConfiguration

.

In a multi-screen environment with a virtual device, the location is specified
in the corresponding virtual coordinate system. If the cursor location is
outside the bounds of the virtual device the reported coordinates are
clipped to fit within the bounds of the virtual device.

DragSourceEvent

s are generated whenever the drag enters, moves
over, or exits a drop site, when the drop action changes, and when the drag
ends. The location for the generated

DragSourceEvent

specifies
the mouse cursor location in screen coordinates at the moment this event
occurred.

In a multi-screen environment without a virtual device, the cursor location is
specified in the coordinate system of the

initiator

GraphicsConfiguration

. The

initiator

GraphicsConfiguration

is the

GraphicsConfiguration

of the

Component

on which the drag gesture for the current drag
operation was recognized. If the cursor location is outside the bounds of
the initiator

GraphicsConfiguration

, the reported coordinates are
clipped to fit within the bounds of that

GraphicsConfiguration

.

In a multi-screen environment with a virtual device, the location is specified
in the corresponding virtual coordinate system. If the cursor location is
outside the bounds of the virtual device the reported coordinates are
clipped to fit within the bounds of the virtual device.

In a multi-screen environment without a virtual device, the cursor location is
specified in the coordinate system of the

initiator

GraphicsConfiguration

. The

initiator

GraphicsConfiguration

is the

GraphicsConfiguration

of the

Component

on which the drag gesture for the current drag
operation was recognized. If the cursor location is outside the bounds of
the initiator

GraphicsConfiguration

, the reported coordinates are
clipped to fit within the bounds of that

GraphicsConfiguration

.

In a multi-screen environment with a virtual device, the location is specified
in the corresponding virtual coordinate system. If the cursor location is
outside the bounds of the virtual device the reported coordinates are
clipped to fit within the bounds of the virtual device.

In a multi-screen environment with a virtual device, the location is specified
in the corresponding virtual coordinate system. If the cursor location is
outside the bounds of the virtual device the reported coordinates are
clipped to fit within the bounds of the virtual device.

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

DragSourceEvent

​(

DragSourceContext

dsc)

Construct a

DragSourceEvent

given a specified

DragSourceContext

.

DragSourceEvent

​(

DragSourceContext

dsc,
int x,
int y)

Construct a

DragSourceEvent

given a specified

DragSourceContext

, and coordinates of the cursor
location.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

DragSourceContext

getDragSourceContext

()

This method returns the

DragSourceContext

that
originated the event.

Point

getLocation

()

This method returns a

Point

indicating the cursor
location in screen coordinates at the moment this event occurred, or

null

if the cursor location is not specified for this
event.

int

getX

()

This method returns the horizontal coordinate of the cursor location in
screen coordinates at the moment this event occurred, or zero if the
cursor location is not specified for this event.

int

getY

()

This method returns the vertical coordinate of the cursor location in
screen coordinates at the moment this event occurred, or zero if the
cursor location is not specified for this event.

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

DragSourceEvent

​(

DragSourceContext

dsc)

Construct a

DragSourceEvent

given a specified

DragSourceContext

.

DragSourceEvent

​(

DragSourceContext

dsc,
int x,
int y)

Construct a

DragSourceEvent

given a specified

DragSourceContext

, and coordinates of the cursor
location.

---

#### Constructor Summary

Construct a

DragSourceEvent

given a specified

DragSourceContext

.

Construct a

DragSourceEvent

given a specified

DragSourceContext

, and coordinates of the cursor
location.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

DragSourceContext

getDragSourceContext

()

This method returns the

DragSourceContext

that
originated the event.

Point

getLocation

()

This method returns a

Point

indicating the cursor
location in screen coordinates at the moment this event occurred, or

null

if the cursor location is not specified for this
event.

int

getX

()

This method returns the horizontal coordinate of the cursor location in
screen coordinates at the moment this event occurred, or zero if the
cursor location is not specified for this event.

int

getY

()

This method returns the vertical coordinate of the cursor location in
screen coordinates at the moment this event occurred, or zero if the
cursor location is not specified for this event.

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

This method returns the

DragSourceContext

that
originated the event.

This method returns a

Point

indicating the cursor
location in screen coordinates at the moment this event occurred, or

null

if the cursor location is not specified for this
event.

This method returns the horizontal coordinate of the cursor location in
screen coordinates at the moment this event occurred, or zero if the
cursor location is not specified for this event.

This method returns the vertical coordinate of the cursor location in
screen coordinates at the moment this event occurred, or zero if the
cursor location is not specified for this event.

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

- DragSourceEvent

```java
public DragSourceEvent​(
DragSourceContext
dsc)
```

Construct a

DragSourceEvent

given a specified

DragSourceContext

.
The coordinates for this

DragSourceEvent

are not specified, so

getLocation

will return

null

for this event.

**Parameters:** dsc

- the

DragSourceContext
**Throws:** IllegalArgumentException

- if

dsc

is

null

.
**See Also:** getLocation()

- DragSourceEvent

```java
public DragSourceEvent​(
DragSourceContext
dsc,
int x,
int y)
```

Construct a

DragSourceEvent

given a specified

DragSourceContext

, and coordinates of the cursor
location.

**Parameters:** dsc

- the

DragSourceContext
**Parameters:** x

- the horizontal coordinate for the cursor location
**Parameters:** y

- the vertical coordinate for the cursor location
**Throws:** IllegalArgumentException

- if

dsc

is

null

.
**Since:** 1.4

============ METHOD DETAIL ==========

- Method Detail

- getDragSourceContext

```java
public
DragSourceContext
getDragSourceContext()
```

This method returns the

DragSourceContext

that
originated the event.

**Returns:** the

DragSourceContext

that originated the event

- getLocation

```java
public
Point
getLocation()
```

This method returns a

Point

indicating the cursor
location in screen coordinates at the moment this event occurred, or

null

if the cursor location is not specified for this
event.

**Returns:** the

Point

indicating the cursor location
or

null

if the cursor location is not specified
**Since:** 1.4

- getX

```java
public int getX()
```

This method returns the horizontal coordinate of the cursor location in
screen coordinates at the moment this event occurred, or zero if the
cursor location is not specified for this event.

**Returns:** an integer indicating the horizontal coordinate of the cursor
location or zero if the cursor location is not specified
**Since:** 1.4

- getY

```java
public int getY()
```

This method returns the vertical coordinate of the cursor location in
screen coordinates at the moment this event occurred, or zero if the
cursor location is not specified for this event.

**Returns:** an integer indicating the vertical coordinate of the cursor
location or zero if the cursor location is not specified
**Since:** 1.4

Constructor Detail

- DragSourceEvent

```java
public DragSourceEvent​(
DragSourceContext
dsc)
```

Construct a

DragSourceEvent

given a specified

DragSourceContext

.
The coordinates for this

DragSourceEvent

are not specified, so

getLocation

will return

null

for this event.

**Parameters:** dsc

- the

DragSourceContext
**Throws:** IllegalArgumentException

- if

dsc

is

null

.
**See Also:** getLocation()

- DragSourceEvent

```java
public DragSourceEvent​(
DragSourceContext
dsc,
int x,
int y)
```

Construct a

DragSourceEvent

given a specified

DragSourceContext

, and coordinates of the cursor
location.

**Parameters:** dsc

- the

DragSourceContext
**Parameters:** x

- the horizontal coordinate for the cursor location
**Parameters:** y

- the vertical coordinate for the cursor location
**Throws:** IllegalArgumentException

- if

dsc

is

null

.
**Since:** 1.4

---

#### Constructor Detail

DragSourceEvent

```java
public DragSourceEvent​(
DragSourceContext
dsc)
```

Construct a

DragSourceEvent

given a specified

DragSourceContext

.
The coordinates for this

DragSourceEvent

are not specified, so

getLocation

will return

null

for this event.

**Parameters:** dsc

- the

DragSourceContext
**Throws:** IllegalArgumentException

- if

dsc

is

null

.
**See Also:** getLocation()

---

#### DragSourceEvent

public DragSourceEvent​(

DragSourceContext

dsc)

Construct a

DragSourceEvent

given a specified

DragSourceContext

.
The coordinates for this

DragSourceEvent

are not specified, so

getLocation

will return

null

for this event.

DragSourceEvent

```java
public DragSourceEvent​(
DragSourceContext
dsc,
int x,
int y)
```

Construct a

DragSourceEvent

given a specified

DragSourceContext

, and coordinates of the cursor
location.

**Parameters:** dsc

- the

DragSourceContext
**Parameters:** x

- the horizontal coordinate for the cursor location
**Parameters:** y

- the vertical coordinate for the cursor location
**Throws:** IllegalArgumentException

- if

dsc

is

null

.
**Since:** 1.4

---

#### DragSourceEvent

public DragSourceEvent​(

DragSourceContext

dsc,
int x,
int y)

Construct a

DragSourceEvent

given a specified

DragSourceContext

, and coordinates of the cursor
location.

Method Detail

- getDragSourceContext

```java
public
DragSourceContext
getDragSourceContext()
```

This method returns the

DragSourceContext

that
originated the event.

**Returns:** the

DragSourceContext

that originated the event

- getLocation

```java
public
Point
getLocation()
```

This method returns a

Point

indicating the cursor
location in screen coordinates at the moment this event occurred, or

null

if the cursor location is not specified for this
event.

**Returns:** the

Point

indicating the cursor location
or

null

if the cursor location is not specified
**Since:** 1.4

- getX

```java
public int getX()
```

This method returns the horizontal coordinate of the cursor location in
screen coordinates at the moment this event occurred, or zero if the
cursor location is not specified for this event.

**Returns:** an integer indicating the horizontal coordinate of the cursor
location or zero if the cursor location is not specified
**Since:** 1.4

- getY

```java
public int getY()
```

This method returns the vertical coordinate of the cursor location in
screen coordinates at the moment this event occurred, or zero if the
cursor location is not specified for this event.

**Returns:** an integer indicating the vertical coordinate of the cursor
location or zero if the cursor location is not specified
**Since:** 1.4

---

#### Method Detail

getDragSourceContext

```java
public
DragSourceContext
getDragSourceContext()
```

This method returns the

DragSourceContext

that
originated the event.

**Returns:** the

DragSourceContext

that originated the event

---

#### getDragSourceContext

public

DragSourceContext

getDragSourceContext()

This method returns the

DragSourceContext

that
originated the event.

getLocation

```java
public
Point
getLocation()
```

This method returns a

Point

indicating the cursor
location in screen coordinates at the moment this event occurred, or

null

if the cursor location is not specified for this
event.

**Returns:** the

Point

indicating the cursor location
or

null

if the cursor location is not specified
**Since:** 1.4

---

#### getLocation

public

Point

getLocation()

This method returns a

Point

indicating the cursor
location in screen coordinates at the moment this event occurred, or

null

if the cursor location is not specified for this
event.

getX

```java
public int getX()
```

This method returns the horizontal coordinate of the cursor location in
screen coordinates at the moment this event occurred, or zero if the
cursor location is not specified for this event.

**Returns:** an integer indicating the horizontal coordinate of the cursor
location or zero if the cursor location is not specified
**Since:** 1.4

---

#### getX

public int getX()

This method returns the horizontal coordinate of the cursor location in
screen coordinates at the moment this event occurred, or zero if the
cursor location is not specified for this event.

getY

```java
public int getY()
```

This method returns the vertical coordinate of the cursor location in
screen coordinates at the moment this event occurred, or zero if the
cursor location is not specified for this event.

**Returns:** an integer indicating the vertical coordinate of the cursor
location or zero if the cursor location is not specified
**Since:** 1.4

---

#### getY

public int getY()

This method returns the vertical coordinate of the cursor location in
screen coordinates at the moment this event occurred, or zero if the
cursor location is not specified for this event.

---

