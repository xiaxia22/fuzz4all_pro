# Interface VMDisconnectEvent

**Source:** `jdk.jdi\com\sun\jdi\event\VMDisconnectEvent.html`

### Class Description

```java
public interface
VMDisconnectEvent

extends
Event
```

Notification of disconnection from target VM.
May be caused by normal termination of a VM,
VM termination by uncaught exception or other error,
debugger action (

VirtualMachine.dispose()

or

VirtualMachine.exit(int)

) or by external events
(for example, target process termination by the
operating system, transport termination, etc).

If the target VM terminates before the disconnection, this event
will be preceded by a

VMDeathEvent

.

This event is always sent.
There is no corresponding

EventRequest

.
The enclosing singleton

EventSet

always has a
suspend policy of

EventRequest.SUSPEND_NONE

.

**All Superinterfaces:** Event

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

#### Interface VMDisconnectEvent

**All Superinterfaces:** Event

,

Mirror

```java
public interface
VMDisconnectEvent

extends
Event
```

Notification of disconnection from target VM.
May be caused by normal termination of a VM,
VM termination by uncaught exception or other error,
debugger action (

VirtualMachine.dispose()

or

VirtualMachine.exit(int)

) or by external events
(for example, target process termination by the
operating system, transport termination, etc).

If the target VM terminates before the disconnection, this event
will be preceded by a

VMDeathEvent

.

This event is always sent.
There is no corresponding

EventRequest

.
The enclosing singleton

EventSet

always has a
suspend policy of

EventRequest.SUSPEND_NONE

.

**Since:** 1.3
**See Also:** VMDeathEvent

,

EventQueue

,

VirtualMachine

public interface

VMDisconnectEvent

extends

Event

Notification of disconnection from target VM.
May be caused by normal termination of a VM,
VM termination by uncaught exception or other error,
debugger action (

VirtualMachine.dispose()

or

VirtualMachine.exit(int)

) or by external events
(for example, target process termination by the
operating system, transport termination, etc).

If the target VM terminates before the disconnection, this event
will be preceded by a

VMDeathEvent

.

This event is always sent.
There is no corresponding

EventRequest

.
The enclosing singleton

EventSet

always has a
suspend policy of

EventRequest.SUSPEND_NONE

.

If the target VM terminates before the disconnection, this event
will be preceded by a

VMDeathEvent

.

This event is always sent.
There is no corresponding

EventRequest

.
The enclosing singleton

EventSet

always has a
suspend policy of

EventRequest.SUSPEND_NONE

.

This event is always sent.
There is no corresponding

EventRequest

.
The enclosing singleton

EventSet

always has a
suspend policy of

EventRequest.SUSPEND_NONE

.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in interface com.sun.jdi.event.

Event

request

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

Mirror

toString

,

virtualMachine

---

