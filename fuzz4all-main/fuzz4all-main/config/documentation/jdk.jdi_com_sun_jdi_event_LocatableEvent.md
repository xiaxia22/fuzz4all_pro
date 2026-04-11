# Interface LocatableEvent

**Source:** `jdk.jdi\com\sun\jdi\event\LocatableEvent.html`

### Class Description

```java
public interface
LocatableEvent

extends
Event
,
Locatable
```

Abstract superinterface of events which have both location
and thread.

**All Superinterfaces:** Event

,

Locatable

,

Mirror

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ThreadReference
thread()

Returns the thread in which this event has occurred.

**Returns:**
- a

ThreadReference

which mirrors the event's thread in
the target VM.

---

### Additional Sections

#### Interface LocatableEvent

**All Superinterfaces:** Event

,

Locatable

,

Mirror

**All Known Subinterfaces:** AccessWatchpointEvent

,

BreakpointEvent

,

ExceptionEvent

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

WatchpointEvent

```java
public interface
LocatableEvent

extends
Event
,
Locatable
```

Abstract superinterface of events which have both location
and thread.

**Since:** 1.3

public interface

LocatableEvent

extends

Event

,

Locatable

Abstract superinterface of events which have both location
and thread.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ThreadReference

thread

()

Returns the thread in which this event has occurred.

- Methods declared in interface com.sun.jdi.event.

Event

request

- Methods declared in interface com.sun.jdi.

Locatable

location

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

ThreadReference

thread

()

Returns the thread in which this event has occurred.

- Methods declared in interface com.sun.jdi.event.

Event

request

- Methods declared in interface com.sun.jdi.

Locatable

location

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Method Summary

Returns the thread in which this event has occurred.

Methods declared in interface com.sun.jdi.event.

Event

request

---

#### Methods declared in interface com.sun.jdi.event. Event

Methods declared in interface com.sun.jdi.

Locatable

location

---

#### Methods declared in interface com.sun.jdi. Locatable

Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Methods declared in interface com.sun.jdi. Mirror

============ METHOD DETAIL ==========

- Method Detail

- thread

```java
ThreadReference
thread()
```

Returns the thread in which this event has occurred.

**Returns:** a

ThreadReference

which mirrors the event's thread in
the target VM.

Method Detail

- thread

```java
ThreadReference
thread()
```

Returns the thread in which this event has occurred.

**Returns:** a

ThreadReference

which mirrors the event's thread in
the target VM.

---

#### Method Detail

thread

```java
ThreadReference
thread()
```

Returns the thread in which this event has occurred.

**Returns:** a

ThreadReference

which mirrors the event's thread in
the target VM.

---

#### thread

ThreadReference

thread()

Returns the thread in which this event has occurred.

---

