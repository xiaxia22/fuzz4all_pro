# Interface MonitorWaitedEvent

**Source:** `jdk.jdi\com\sun\jdi\event\MonitorWaitedEvent.html`

### Class Description

```java
public interface
MonitorWaitedEvent

extends
LocatableEvent
```

Notification that a thread in the target VM has finished
waiting on an monitor object.

**All Superinterfaces:** Event

,

Locatable

,

LocatableEvent

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

**Specified by:**
- thread

in interface

LocatableEvent

**Returns:**
- a

ThreadReference

which mirrors the event's thread in
the target VM.

---

#### ObjectReference
monitor()

Returns the monitor object this thread waited on.

**Returns:**
- an

ObjectReference

for the monitor.

---

#### boolean timedout()

Returns whether the wait has timed out or been interrupted.

**Returns:**
- true

if the wait is timed out.

---

### Additional Sections

#### Interface MonitorWaitedEvent

**All Superinterfaces:** Event

,

Locatable

,

LocatableEvent

,

Mirror

```java
public interface
MonitorWaitedEvent

extends
LocatableEvent
```

Notification that a thread in the target VM has finished
waiting on an monitor object.

**Since:** 1.6
**See Also:** EventQueue

,

MonitorWaitEvent

public interface

MonitorWaitedEvent

extends

LocatableEvent

Notification that a thread in the target VM has finished
waiting on an monitor object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ObjectReference

monitor

()

Returns the monitor object this thread waited on.

ThreadReference

thread

()

Returns the thread in which this event has occurred.

boolean

timedout

()

Returns whether the wait has timed out or been interrupted.

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

ObjectReference

monitor

()

Returns the monitor object this thread waited on.

ThreadReference

thread

()

Returns the thread in which this event has occurred.

boolean

timedout

()

Returns whether the wait has timed out or been interrupted.

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

Returns the monitor object this thread waited on.

Returns the thread in which this event has occurred.

Returns whether the wait has timed out or been interrupted.

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

**Specified by:** thread

in interface

LocatableEvent
**Returns:** a

ThreadReference

which mirrors the event's thread in
the target VM.

- monitor

```java
ObjectReference
monitor()
```

Returns the monitor object this thread waited on.

**Returns:** an

ObjectReference

for the monitor.

- timedout

```java
boolean timedout()
```

Returns whether the wait has timed out or been interrupted.

**Returns:** true

if the wait is timed out.

Method Detail

- thread

```java
ThreadReference
thread()
```

Returns the thread in which this event has occurred.

**Specified by:** thread

in interface

LocatableEvent
**Returns:** a

ThreadReference

which mirrors the event's thread in
the target VM.

- monitor

```java
ObjectReference
monitor()
```

Returns the monitor object this thread waited on.

**Returns:** an

ObjectReference

for the monitor.

- timedout

```java
boolean timedout()
```

Returns whether the wait has timed out or been interrupted.

**Returns:** true

if the wait is timed out.

---

#### Method Detail

thread

```java
ThreadReference
thread()
```

Returns the thread in which this event has occurred.

**Specified by:** thread

in interface

LocatableEvent
**Returns:** a

ThreadReference

which mirrors the event's thread in
the target VM.

---

#### thread

ThreadReference

thread()

Returns the thread in which this event has occurred.

monitor

```java
ObjectReference
monitor()
```

Returns the monitor object this thread waited on.

**Returns:** an

ObjectReference

for the monitor.

---

#### monitor

ObjectReference

monitor()

Returns the monitor object this thread waited on.

timedout

```java
boolean timedout()
```

Returns whether the wait has timed out or been interrupted.

**Returns:** true

if the wait is timed out.

---

#### timedout

boolean timedout()

Returns whether the wait has timed out or been interrupted.

---

