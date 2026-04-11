# Interface MonitorContendedEnterEvent

**Source:** `jdk.jdi\com\sun\jdi\event\MonitorContendedEnterEvent.html`

### Class Description

```java
public interface
MonitorContendedEnterEvent

extends
LocatableEvent
```

Notification that a thread in the target VM is attempting
to enter a monitor that is already acquired by another thread.

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

Returns the method that was entered.

**Returns:**
- an

ObjectReference

for the monitor.

---

### Additional Sections

#### Interface MonitorContendedEnterEvent

**All Superinterfaces:** Event

,

Locatable

,

LocatableEvent

,

Mirror

```java
public interface
MonitorContendedEnterEvent

extends
LocatableEvent
```

Notification that a thread in the target VM is attempting
to enter a monitor that is already acquired by another thread.

**Since:** 1.6
**See Also:** EventQueue

,

MonitorContendedEnteredEvent

public interface

MonitorContendedEnterEvent

extends

LocatableEvent

Notification that a thread in the target VM is attempting
to enter a monitor that is already acquired by another thread.

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

Returns the method that was entered.

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

ObjectReference

monitor

()

Returns the method that was entered.

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

Returns the method that was entered.

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

Returns the method that was entered.

**Returns:** an

ObjectReference

for the monitor.

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

Returns the method that was entered.

**Returns:** an

ObjectReference

for the monitor.

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

Returns the method that was entered.

**Returns:** an

ObjectReference

for the monitor.

---

#### monitor

ObjectReference

monitor()

Returns the method that was entered.

---

