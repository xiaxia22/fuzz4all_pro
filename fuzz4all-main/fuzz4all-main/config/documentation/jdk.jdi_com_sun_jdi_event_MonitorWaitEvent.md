# Interface MonitorWaitEvent

**Source:** `jdk.jdi\com\sun\jdi\event\MonitorWaitEvent.html`

### Class Description

```java
public interface
MonitorWaitEvent

extends
LocatableEvent
```

Notification that a thread in the target VM is about to
wait on a monitor object.

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

Returns the thread in which monitor wait event has occurred.

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

Returns the monitor object that the thread about to wait.

**Returns:**
- an

ObjectReference

for the monitor.

---

#### long timeout()

Returns the number of millisecond the thread will wait.

**Returns:**
- a

jlong

containing monitor wait time in milliseconds.

---

### Additional Sections

#### Interface MonitorWaitEvent

**All Superinterfaces:** Event

,

Locatable

,

LocatableEvent

,

Mirror

```java
public interface
MonitorWaitEvent

extends
LocatableEvent
```

Notification that a thread in the target VM is about to
wait on a monitor object.

**Since:** 1.6
**See Also:** EventQueue

,

MonitorWaitedEvent

public interface

MonitorWaitEvent

extends

LocatableEvent

Notification that a thread in the target VM is about to
wait on a monitor object.

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

Returns the monitor object that the thread about to wait.

ThreadReference

thread

()

Returns the thread in which monitor wait event has occurred.

long

timeout

()

Returns the number of millisecond the thread will wait.

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

Returns the monitor object that the thread about to wait.

ThreadReference

thread

()

Returns the thread in which monitor wait event has occurred.

long

timeout

()

Returns the number of millisecond the thread will wait.

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

Returns the monitor object that the thread about to wait.

Returns the thread in which monitor wait event has occurred.

Returns the number of millisecond the thread will wait.

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

Returns the thread in which monitor wait event has occurred.

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

Returns the monitor object that the thread about to wait.

**Returns:** an

ObjectReference

for the monitor.

- timeout

```java
long timeout()
```

Returns the number of millisecond the thread will wait.

**Returns:** a

jlong

containing monitor wait time in milliseconds.

Method Detail

- thread

```java
ThreadReference
thread()
```

Returns the thread in which monitor wait event has occurred.

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

Returns the monitor object that the thread about to wait.

**Returns:** an

ObjectReference

for the monitor.

- timeout

```java
long timeout()
```

Returns the number of millisecond the thread will wait.

**Returns:** a

jlong

containing monitor wait time in milliseconds.

---

#### Method Detail

thread

```java
ThreadReference
thread()
```

Returns the thread in which monitor wait event has occurred.

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

Returns the thread in which monitor wait event has occurred.

monitor

```java
ObjectReference
monitor()
```

Returns the monitor object that the thread about to wait.

**Returns:** an

ObjectReference

for the monitor.

---

#### monitor

ObjectReference

monitor()

Returns the monitor object that the thread about to wait.

timeout

```java
long timeout()
```

Returns the number of millisecond the thread will wait.

**Returns:** a

jlong

containing monitor wait time in milliseconds.

---

#### timeout

long timeout()

Returns the number of millisecond the thread will wait.

---

