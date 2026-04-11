# Interface BreakpointEvent

**Source:** `jdk.jdi\com\sun\jdi\event\BreakpointEvent.html`

### Class Description

```java
public interface
BreakpointEvent

extends
LocatableEvent
```

Notification of a breakpoint in the target VM.

The breakpoint event is generated before the code at its location
is executed. When a location is reached which satisfies a currently enabled

breakpoint request

, an

event set

containing an instance of this class will be added to the VM's event queue.

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

*No entries found.*

### Additional Sections

#### Interface BreakpointEvent

**All Superinterfaces:** Event

,

Locatable

,

LocatableEvent

,

Mirror

```java
public interface
BreakpointEvent

extends
LocatableEvent
```

Notification of a breakpoint in the target VM.

The breakpoint event is generated before the code at its location
is executed. When a location is reached which satisfies a currently enabled

breakpoint request

, an

event set

containing an instance of this class will be added to the VM's event queue.

**Since:** 1.3
**See Also:** EventQueue

,

VirtualMachine

,

BreakpointRequest

public interface

BreakpointEvent

extends

LocatableEvent

Notification of a breakpoint in the target VM.

The breakpoint event is generated before the code at its location
is executed. When a location is reached which satisfies a currently enabled

breakpoint request

, an

event set

containing an instance of this class will be added to the VM's event queue.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in interface com.sun.jdi.event.

Event

request

- Methods declared in interface com.sun.jdi.

Locatable

location

- Methods declared in interface com.sun.jdi.event.

LocatableEvent

thread

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

Method Summary

- Methods declared in interface com.sun.jdi.event.

Event

request

- Methods declared in interface com.sun.jdi.

Locatable

location

- Methods declared in interface com.sun.jdi.event.

LocatableEvent

thread

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Method Summary

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

Methods declared in interface com.sun.jdi.event.

LocatableEvent

thread

---

#### Methods declared in interface com.sun.jdi.event. LocatableEvent

Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

