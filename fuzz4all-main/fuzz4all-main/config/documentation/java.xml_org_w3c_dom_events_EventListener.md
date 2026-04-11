# Interface EventListener

**Source:** `java.xml\org\w3c\dom\events\EventListener.html`

### Class Description

```java
public interface
EventListener
```

The

EventListener

interface is the primary method for
handling events. Users implement the

EventListener

interface
and register their listener on an

EventTarget

using the

AddEventListener

method. The users should also remove their

EventListener

from its

EventTarget

after they
have completed using the listener.

When a

Node

is copied using the

cloneNode

method the

EventListener

s attached to the source

Node

are not attached to the copied

Node

. If
the user wishes the same

EventListener

s to be added to the
newly created copy the user must add them manually.

See also the

Document Object Model (DOM) Level 2 Events Specification

.

**Since:** 1.5, DOM Level 2

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void handleEvent​(
Event
evt)

This method is called whenever an event occurs of the type for which
the

EventListener

interface was registered.

**Parameters:**
- evt

- The

Event

contains contextual information
about the event. It also contains the

stopPropagation

and

preventDefault

methods which are used in
determining the event's flow and default action.

---

### Additional Sections

#### Interface EventListener

```java
public interface
EventListener
```

The

EventListener

interface is the primary method for
handling events. Users implement the

EventListener

interface
and register their listener on an

EventTarget

using the

AddEventListener

method. The users should also remove their

EventListener

from its

EventTarget

after they
have completed using the listener.

When a

Node

is copied using the

cloneNode

method the

EventListener

s attached to the source

Node

are not attached to the copied

Node

. If
the user wishes the same

EventListener

s to be added to the
newly created copy the user must add them manually.

See also the

Document Object Model (DOM) Level 2 Events Specification

.

**Since:** 1.5, DOM Level 2

public interface

EventListener

The

EventListener

interface is the primary method for
handling events. Users implement the

EventListener

interface
and register their listener on an

EventTarget

using the

AddEventListener

method. The users should also remove their

EventListener

from its

EventTarget

after they
have completed using the listener.

When a

Node

is copied using the

cloneNode

method the

EventListener

s attached to the source

Node

are not attached to the copied

Node

. If
the user wishes the same

EventListener

s to be added to the
newly created copy the user must add them manually.

See also the

Document Object Model (DOM) Level 2 Events Specification

.

When a

Node

is copied using the

cloneNode

method the

EventListener

s attached to the source

Node

are not attached to the copied

Node

. If
the user wishes the same

EventListener

s to be added to the
newly created copy the user must add them manually.

See also the

Document Object Model (DOM) Level 2 Events Specification

.

See also the

Document Object Model (DOM) Level 2 Events Specification

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

handleEvent

​(

Event

evt)

This method is called whenever an event occurs of the type for which
the

EventListener

interface was registered.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

handleEvent

​(

Event

evt)

This method is called whenever an event occurs of the type for which
the

EventListener

interface was registered.

---

#### Method Summary

This method is called whenever an event occurs of the type for which
the

EventListener

interface was registered.

============ METHOD DETAIL ==========

- Method Detail

- handleEvent

```java
void handleEvent​(
Event
evt)
```

This method is called whenever an event occurs of the type for which
the

EventListener

interface was registered.

**Parameters:** evt

- The

Event

contains contextual information
about the event. It also contains the

stopPropagation

and

preventDefault

methods which are used in
determining the event's flow and default action.

Method Detail

- handleEvent

```java
void handleEvent​(
Event
evt)
```

This method is called whenever an event occurs of the type for which
the

EventListener

interface was registered.

**Parameters:** evt

- The

Event

contains contextual information
about the event. It also contains the

stopPropagation

and

preventDefault

methods which are used in
determining the event's flow and default action.

---

#### Method Detail

handleEvent

```java
void handleEvent​(
Event
evt)
```

This method is called whenever an event occurs of the type for which
the

EventListener

interface was registered.

**Parameters:** evt

- The

Event

contains contextual information
about the event. It also contains the

stopPropagation

and

preventDefault

methods which are used in
determining the event's flow and default action.

---

#### handleEvent

void handleEvent​(

Event

evt)

This method is called whenever an event occurs of the type for which
the

EventListener

interface was registered.

---

