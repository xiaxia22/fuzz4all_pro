# Class DragSourceDropEvent

**Source:** `java.desktop\java\awt\dnd\DragSourceDropEvent.html`

### Class Description

```java
public class
DragSourceDropEvent

extends
DragSourceEvent
```

The

DragSourceDropEvent

is delivered
from the

DragSourceContextPeer

,
via the

DragSourceContext

, to the

dragDropEnd

method of

DragSourceListener

s registered with that

DragSourceContext

and with its associated

DragSource

.
It contains sufficient information for the
originator of the operation
to provide appropriate feedback to the end user
when the operation completes.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public DragSourceDropEvent​(
DragSourceContext
dsc,
int action,
boolean success)

Construct a

DragSourceDropEvent

for a drop,
given the

DragSourceContext

, the drop action,
and a

boolean

indicating if the drop was successful.
The coordinates for this

DragSourceDropEvent

are not specified, so

getLocation

will return

null

for this event.

The argument

action

should be one of

DnDConstants

that represents a single action.
This constructor does not throw any exception for invalid

action

.

**Parameters:**
- dsc

- the

DragSourceContext

associated with this

DragSourceDropEvent
- action

- the drop action
- success

- a boolean indicating if the drop was successful

**Throws:**
- IllegalArgumentException

- if

dsc

is

null

.

**See Also:**
- DragSourceEvent.getLocation()

---

#### public DragSourceDropEvent​(
DragSourceContext
dsc,
int action,
boolean success,
int x,
int y)

Construct a

DragSourceDropEvent

for a drop, given the

DragSourceContext

, the drop action, a

boolean

indicating if the drop was successful, and coordinates.

The argument

action

should be one of

DnDConstants

that represents a single action.
This constructor does not throw any exception for invalid

action

.

**Parameters:**
- dsc

- the

DragSourceContext

associated with this

DragSourceDropEvent
- action

- the drop action
- success

- a boolean indicating if the drop was successful
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

#### public DragSourceDropEvent​(
DragSourceContext
dsc)

Construct a

DragSourceDropEvent

for a drag that does not result in a drop.
The coordinates for this

DragSourceDropEvent

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
- DragSourceEvent.getLocation()

---

### Method Details

#### public boolean getDropSuccess()

This method returns a

boolean

indicating
if the drop was successful.

**Returns:**
- true

if the drop target accepted the drop and
successfully performed a drop action;

false

if the drop target rejected the drop or
if the drop target accepted the drop, but failed to perform
a drop action.

---

#### public int getDropAction()

This method returns an

int

representing
the action performed by the target on the subject of the drop.

**Returns:**
- the action performed by the target on the subject of the drop
if the drop target accepted the drop and the target drop action
is supported by the drag source; otherwise,

DnDConstants.ACTION_NONE

.

---

### Additional Sections

#### Class DragSourceDropEvent

java.lang.Object

- java.util.EventObject
- - java.awt.dnd.DragSourceEvent
- - java.awt.dnd.DragSourceDropEvent

java.util.EventObject

- java.awt.dnd.DragSourceEvent
- - java.awt.dnd.DragSourceDropEvent

java.awt.dnd.DragSourceEvent

- java.awt.dnd.DragSourceDropEvent

java.awt.dnd.DragSourceDropEvent

**All Implemented Interfaces:** Serializable

```java
public class
DragSourceDropEvent

extends
DragSourceEvent
```

The

DragSourceDropEvent

is delivered
from the

DragSourceContextPeer

,
via the

DragSourceContext

, to the

dragDropEnd

method of

DragSourceListener

s registered with that

DragSourceContext

and with its associated

DragSource

.
It contains sufficient information for the
originator of the operation
to provide appropriate feedback to the end user
when the operation completes.

**Since:** 1.2
**See Also:** Serialized Form

public class

DragSourceDropEvent

extends

DragSourceEvent

The

DragSourceDropEvent

is delivered
from the

DragSourceContextPeer

,
via the

DragSourceContext

, to the

dragDropEnd

method of

DragSourceListener

s registered with that

DragSourceContext

and with its associated

DragSource

.
It contains sufficient information for the
originator of the operation
to provide appropriate feedback to the end user
when the operation completes.

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

DragSourceDropEvent

​(

DragSourceContext

dsc)

Construct a

DragSourceDropEvent

for a drag that does not result in a drop.

DragSourceDropEvent

​(

DragSourceContext

dsc,
int action,
boolean success)

Construct a

DragSourceDropEvent

for a drop,
given the

DragSourceContext

, the drop action,
and a

boolean

indicating if the drop was successful.

DragSourceDropEvent

​(

DragSourceContext

dsc,
int action,
boolean success,
int x,
int y)

Construct a

DragSourceDropEvent

for a drop, given the

DragSourceContext

, the drop action, a

boolean

indicating if the drop was successful, and coordinates.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getDropAction

()

This method returns an

int

representing
the action performed by the target on the subject of the drop.

boolean

getDropSuccess

()

This method returns a

boolean

indicating
if the drop was successful.

- Methods declared in class java.awt.dnd.

DragSourceEvent

getDragSourceContext

,

getLocation

,

getX

,

getY

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

DragSourceDropEvent

​(

DragSourceContext

dsc)

Construct a

DragSourceDropEvent

for a drag that does not result in a drop.

DragSourceDropEvent

​(

DragSourceContext

dsc,
int action,
boolean success)

Construct a

DragSourceDropEvent

for a drop,
given the

DragSourceContext

, the drop action,
and a

boolean

indicating if the drop was successful.

DragSourceDropEvent

​(

DragSourceContext

dsc,
int action,
boolean success,
int x,
int y)

Construct a

DragSourceDropEvent

for a drop, given the

DragSourceContext

, the drop action, a

boolean

indicating if the drop was successful, and coordinates.

---

#### Constructor Summary

Construct a

DragSourceDropEvent

for a drag that does not result in a drop.

Construct a

DragSourceDropEvent

for a drop,
given the

DragSourceContext

, the drop action,
and a

boolean

indicating if the drop was successful.

Construct a

DragSourceDropEvent

for a drop, given the

DragSourceContext

, the drop action, a

boolean

indicating if the drop was successful, and coordinates.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getDropAction

()

This method returns an

int

representing
the action performed by the target on the subject of the drop.

boolean

getDropSuccess

()

This method returns a

boolean

indicating
if the drop was successful.

- Methods declared in class java.awt.dnd.

DragSourceEvent

getDragSourceContext

,

getLocation

,

getX

,

getY

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

This method returns an

int

representing
the action performed by the target on the subject of the drop.

This method returns a

boolean

indicating
if the drop was successful.

Methods declared in class java.awt.dnd.

DragSourceEvent

getDragSourceContext

,

getLocation

,

getX

,

getY

---

#### Methods declared in class java.awt.dnd. DragSourceEvent

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

- DragSourceDropEvent

```java
public DragSourceDropEvent​(
DragSourceContext
dsc,
int action,
boolean success)
```

Construct a

DragSourceDropEvent

for a drop,
given the

DragSourceContext

, the drop action,
and a

boolean

indicating if the drop was successful.
The coordinates for this

DragSourceDropEvent

are not specified, so

getLocation

will return

null

for this event.

The argument

action

should be one of

DnDConstants

that represents a single action.
This constructor does not throw any exception for invalid

action

.

**Parameters:** dsc

- the

DragSourceContext

associated with this

DragSourceDropEvent
**Parameters:** action

- the drop action
**Parameters:** success

- a boolean indicating if the drop was successful
**Throws:** IllegalArgumentException

- if

dsc

is

null

.
**See Also:** DragSourceEvent.getLocation()

- DragSourceDropEvent

```java
public DragSourceDropEvent​(
DragSourceContext
dsc,
int action,
boolean success,
int x,
int y)
```

Construct a

DragSourceDropEvent

for a drop, given the

DragSourceContext

, the drop action, a

boolean

indicating if the drop was successful, and coordinates.

The argument

action

should be one of

DnDConstants

that represents a single action.
This constructor does not throw any exception for invalid

action

.

**Parameters:** dsc

- the

DragSourceContext

associated with this

DragSourceDropEvent
**Parameters:** action

- the drop action
**Parameters:** success

- a boolean indicating if the drop was successful
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

- DragSourceDropEvent

```java
public DragSourceDropEvent​(
DragSourceContext
dsc)
```

Construct a

DragSourceDropEvent

for a drag that does not result in a drop.
The coordinates for this

DragSourceDropEvent

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
**See Also:** DragSourceEvent.getLocation()

============ METHOD DETAIL ==========

- Method Detail

- getDropSuccess

```java
public boolean getDropSuccess()
```

This method returns a

boolean

indicating
if the drop was successful.

**Returns:** true

if the drop target accepted the drop and
successfully performed a drop action;

false

if the drop target rejected the drop or
if the drop target accepted the drop, but failed to perform
a drop action.

- getDropAction

```java
public int getDropAction()
```

This method returns an

int

representing
the action performed by the target on the subject of the drop.

**Returns:** the action performed by the target on the subject of the drop
if the drop target accepted the drop and the target drop action
is supported by the drag source; otherwise,

DnDConstants.ACTION_NONE

.

Constructor Detail

- DragSourceDropEvent

```java
public DragSourceDropEvent​(
DragSourceContext
dsc,
int action,
boolean success)
```

Construct a

DragSourceDropEvent

for a drop,
given the

DragSourceContext

, the drop action,
and a

boolean

indicating if the drop was successful.
The coordinates for this

DragSourceDropEvent

are not specified, so

getLocation

will return

null

for this event.

The argument

action

should be one of

DnDConstants

that represents a single action.
This constructor does not throw any exception for invalid

action

.

**Parameters:** dsc

- the

DragSourceContext

associated with this

DragSourceDropEvent
**Parameters:** action

- the drop action
**Parameters:** success

- a boolean indicating if the drop was successful
**Throws:** IllegalArgumentException

- if

dsc

is

null

.
**See Also:** DragSourceEvent.getLocation()

- DragSourceDropEvent

```java
public DragSourceDropEvent​(
DragSourceContext
dsc,
int action,
boolean success,
int x,
int y)
```

Construct a

DragSourceDropEvent

for a drop, given the

DragSourceContext

, the drop action, a

boolean

indicating if the drop was successful, and coordinates.

The argument

action

should be one of

DnDConstants

that represents a single action.
This constructor does not throw any exception for invalid

action

.

**Parameters:** dsc

- the

DragSourceContext

associated with this

DragSourceDropEvent
**Parameters:** action

- the drop action
**Parameters:** success

- a boolean indicating if the drop was successful
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

- DragSourceDropEvent

```java
public DragSourceDropEvent​(
DragSourceContext
dsc)
```

Construct a

DragSourceDropEvent

for a drag that does not result in a drop.
The coordinates for this

DragSourceDropEvent

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
**See Also:** DragSourceEvent.getLocation()

---

#### Constructor Detail

DragSourceDropEvent

```java
public DragSourceDropEvent​(
DragSourceContext
dsc,
int action,
boolean success)
```

Construct a

DragSourceDropEvent

for a drop,
given the

DragSourceContext

, the drop action,
and a

boolean

indicating if the drop was successful.
The coordinates for this

DragSourceDropEvent

are not specified, so

getLocation

will return

null

for this event.

The argument

action

should be one of

DnDConstants

that represents a single action.
This constructor does not throw any exception for invalid

action

.

**Parameters:** dsc

- the

DragSourceContext

associated with this

DragSourceDropEvent
**Parameters:** action

- the drop action
**Parameters:** success

- a boolean indicating if the drop was successful
**Throws:** IllegalArgumentException

- if

dsc

is

null

.
**See Also:** DragSourceEvent.getLocation()

---

#### DragSourceDropEvent

public DragSourceDropEvent​(

DragSourceContext

dsc,
int action,
boolean success)

Construct a

DragSourceDropEvent

for a drop,
given the

DragSourceContext

, the drop action,
and a

boolean

indicating if the drop was successful.
The coordinates for this

DragSourceDropEvent

are not specified, so

getLocation

will return

null

for this event.

The argument

action

should be one of

DnDConstants

that represents a single action.
This constructor does not throw any exception for invalid

action

.

The argument

action

should be one of

DnDConstants

that represents a single action.
This constructor does not throw any exception for invalid

action

.

DragSourceDropEvent

```java
public DragSourceDropEvent​(
DragSourceContext
dsc,
int action,
boolean success,
int x,
int y)
```

Construct a

DragSourceDropEvent

for a drop, given the

DragSourceContext

, the drop action, a

boolean

indicating if the drop was successful, and coordinates.

The argument

action

should be one of

DnDConstants

that represents a single action.
This constructor does not throw any exception for invalid

action

.

**Parameters:** dsc

- the

DragSourceContext

associated with this

DragSourceDropEvent
**Parameters:** action

- the drop action
**Parameters:** success

- a boolean indicating if the drop was successful
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

#### DragSourceDropEvent

public DragSourceDropEvent​(

DragSourceContext

dsc,
int action,
boolean success,
int x,
int y)

Construct a

DragSourceDropEvent

for a drop, given the

DragSourceContext

, the drop action, a

boolean

indicating if the drop was successful, and coordinates.

The argument

action

should be one of

DnDConstants

that represents a single action.
This constructor does not throw any exception for invalid

action

.

The argument

action

should be one of

DnDConstants

that represents a single action.
This constructor does not throw any exception for invalid

action

.

DragSourceDropEvent

```java
public DragSourceDropEvent​(
DragSourceContext
dsc)
```

Construct a

DragSourceDropEvent

for a drag that does not result in a drop.
The coordinates for this

DragSourceDropEvent

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
**See Also:** DragSourceEvent.getLocation()

---

#### DragSourceDropEvent

public DragSourceDropEvent​(

DragSourceContext

dsc)

Construct a

DragSourceDropEvent

for a drag that does not result in a drop.
The coordinates for this

DragSourceDropEvent

are not specified, so

getLocation

will return

null

for this event.

Method Detail

- getDropSuccess

```java
public boolean getDropSuccess()
```

This method returns a

boolean

indicating
if the drop was successful.

**Returns:** true

if the drop target accepted the drop and
successfully performed a drop action;

false

if the drop target rejected the drop or
if the drop target accepted the drop, but failed to perform
a drop action.

- getDropAction

```java
public int getDropAction()
```

This method returns an

int

representing
the action performed by the target on the subject of the drop.

**Returns:** the action performed by the target on the subject of the drop
if the drop target accepted the drop and the target drop action
is supported by the drag source; otherwise,

DnDConstants.ACTION_NONE

.

---

#### Method Detail

getDropSuccess

```java
public boolean getDropSuccess()
```

This method returns a

boolean

indicating
if the drop was successful.

**Returns:** true

if the drop target accepted the drop and
successfully performed a drop action;

false

if the drop target rejected the drop or
if the drop target accepted the drop, but failed to perform
a drop action.

---

#### getDropSuccess

public boolean getDropSuccess()

This method returns a

boolean

indicating
if the drop was successful.

getDropAction

```java
public int getDropAction()
```

This method returns an

int

representing
the action performed by the target on the subject of the drop.

**Returns:** the action performed by the target on the subject of the drop
if the drop target accepted the drop and the target drop action
is supported by the drag source; otherwise,

DnDConstants.ACTION_NONE

.

---

#### getDropAction

public int getDropAction()

This method returns an

int

representing
the action performed by the target on the subject of the drop.

---

