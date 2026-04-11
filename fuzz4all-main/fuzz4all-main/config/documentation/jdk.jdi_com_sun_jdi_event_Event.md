# Interface Event

**Source:** `jdk.jdi\com\sun\jdi\event\Event.html`

### Class Description

```java
public interface
Event

extends
Mirror
```

An occurrence in a target VM that is of interest to a debugger. Event is
the common superinterface for all events (examples include

BreakpointEvent

,

ExceptionEvent

,

ClassPrepareEvent

).
When an event occurs, an instance of Event as a component of
an

EventSet

is enqueued in the

VirtualMachine

's

EventQueue

.

**All Superinterfaces:** Mirror

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### EventRequest
request()

**Returns:**
- The

EventRequest

that requested this event.
Some events (eg.

VMDeathEvent

) may not have
a cooresponding request and thus will return null.

---

### Additional Sections

#### Interface Event

**All Superinterfaces:** Mirror

**All Known Subinterfaces:** AccessWatchpointEvent

,

BreakpointEvent

,

ClassPrepareEvent

,

ClassUnloadEvent

,

ExceptionEvent

,

LocatableEvent

,

MethodEntryEvent

,

MethodExitEvent

,

ModificationWatchpointEvent

,

MonitorContendedEnteredEvent

,

MonitorContendedEnterEvent

,

MonitorWaitedEvent

,

MonitorWaitEvent

,

StepEvent

,

ThreadDeathEvent

,

ThreadStartEvent

,

VMDeathEvent

,

VMDisconnectEvent

,

VMStartEvent

,

WatchpointEvent

```java
public interface
Event

extends
Mirror
```

An occurrence in a target VM that is of interest to a debugger. Event is
the common superinterface for all events (examples include

BreakpointEvent

,

ExceptionEvent

,

ClassPrepareEvent

).
When an event occurs, an instance of Event as a component of
an

EventSet

is enqueued in the

VirtualMachine

's

EventQueue

.

**Since:** 1.3
**See Also:** EventSet

,

EventQueue

public interface

Event

extends

Mirror

An occurrence in a target VM that is of interest to a debugger. Event is
the common superinterface for all events (examples include

BreakpointEvent

,

ExceptionEvent

,

ClassPrepareEvent

).
When an event occurs, an instance of Event as a component of
an

EventSet

is enqueued in the

VirtualMachine

's

EventQueue

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

EventRequest

request

()

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

EventRequest

request

()

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Method Summary

Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Methods declared in interface com.sun.jdi. Mirror

============ METHOD DETAIL ==========

- Method Detail

- request

```java
EventRequest
request()
```

**Returns:** The

EventRequest

that requested this event.
Some events (eg.

VMDeathEvent

) may not have
a cooresponding request and thus will return null.

Method Detail

- request

```java
EventRequest
request()
```

**Returns:** The

EventRequest

that requested this event.
Some events (eg.

VMDeathEvent

) may not have
a cooresponding request and thus will return null.

---

#### Method Detail

request

```java
EventRequest
request()
```

**Returns:** The

EventRequest

that requested this event.
Some events (eg.

VMDeathEvent

) may not have
a cooresponding request and thus will return null.

---

#### request

EventRequest

request()

---

