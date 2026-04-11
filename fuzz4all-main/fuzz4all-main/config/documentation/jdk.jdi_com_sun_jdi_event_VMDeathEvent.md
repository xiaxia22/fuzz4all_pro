# Interface VMDeathEvent

**Source:** `jdk.jdi\com\sun\jdi\event\VMDeathEvent.html`

### Class Description

```java
public interface
VMDeathEvent

extends
Event
```

Notification of target VM termination.
This event occurs if the target VM terminates before the
VM disconnects (

VMDisconnectEvent

).
Thus, this event will NOT occur if external forces terminate
the connection (e.g. a crash) or if the connection is intentionally
terminated with

VirtualMachine.dispose()

On VM termination, a single unsolicited VMDeathEvent will always be sent with a

suspend policy

of

SUSPEND_NONE

.
Additional VMDeathEvents will be sent in the same event set if they are
requested with a

VMDeathRequest

.

The VM is still intact and can be queried at the point this
event was initiated but immediately thereafter it is not
considered intact and cannot be queried.
Note: If the enclosing

EventSet

has a

suspend policy

other than

SUSPEND_ALL

the initiating point may be long past.

All VMDeathEvents will be in a single

EventSet

,
no other events will be in the event set. A resume
must occur to continue execution after any event set which
performs suspensions - in this case to allow proper shutdown.

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

#### Interface VMDeathEvent

**All Superinterfaces:** Event

,

Mirror

```java
public interface
VMDeathEvent

extends
Event
```

Notification of target VM termination.
This event occurs if the target VM terminates before the
VM disconnects (

VMDisconnectEvent

).
Thus, this event will NOT occur if external forces terminate
the connection (e.g. a crash) or if the connection is intentionally
terminated with

VirtualMachine.dispose()

On VM termination, a single unsolicited VMDeathEvent will always be sent with a

suspend policy

of

SUSPEND_NONE

.
Additional VMDeathEvents will be sent in the same event set if they are
requested with a

VMDeathRequest

.

The VM is still intact and can be queried at the point this
event was initiated but immediately thereafter it is not
considered intact and cannot be queried.
Note: If the enclosing

EventSet

has a

suspend policy

other than

SUSPEND_ALL

the initiating point may be long past.

All VMDeathEvents will be in a single

EventSet

,
no other events will be in the event set. A resume
must occur to continue execution after any event set which
performs suspensions - in this case to allow proper shutdown.

**Since:** 1.3
**See Also:** VMDisconnectEvent

,

EventRequestManager.createVMDeathRequest()

,

VMDeathRequest

,

EventQueue

,

VirtualMachine

public interface

VMDeathEvent

extends

Event

Notification of target VM termination.
This event occurs if the target VM terminates before the
VM disconnects (

VMDisconnectEvent

).
Thus, this event will NOT occur if external forces terminate
the connection (e.g. a crash) or if the connection is intentionally
terminated with

VirtualMachine.dispose()

On VM termination, a single unsolicited VMDeathEvent will always be sent with a

suspend policy

of

SUSPEND_NONE

.
Additional VMDeathEvents will be sent in the same event set if they are
requested with a

VMDeathRequest

.

The VM is still intact and can be queried at the point this
event was initiated but immediately thereafter it is not
considered intact and cannot be queried.
Note: If the enclosing

EventSet

has a

suspend policy

other than

SUSPEND_ALL

the initiating point may be long past.

All VMDeathEvents will be in a single

EventSet

,
no other events will be in the event set. A resume
must occur to continue execution after any event set which
performs suspensions - in this case to allow proper shutdown.

On VM termination, a single unsolicited VMDeathEvent will always be sent with a

suspend policy

of

SUSPEND_NONE

.
Additional VMDeathEvents will be sent in the same event set if they are
requested with a

VMDeathRequest

.

The VM is still intact and can be queried at the point this
event was initiated but immediately thereafter it is not
considered intact and cannot be queried.
Note: If the enclosing

EventSet

has a

suspend policy

other than

SUSPEND_ALL

the initiating point may be long past.

All VMDeathEvents will be in a single

EventSet

,
no other events will be in the event set. A resume
must occur to continue execution after any event set which
performs suspensions - in this case to allow proper shutdown.

The VM is still intact and can be queried at the point this
event was initiated but immediately thereafter it is not
considered intact and cannot be queried.
Note: If the enclosing

EventSet

has a

suspend policy

other than

SUSPEND_ALL

the initiating point may be long past.

All VMDeathEvents will be in a single

EventSet

,
no other events will be in the event set. A resume
must occur to continue execution after any event set which
performs suspensions - in this case to allow proper shutdown.

All VMDeathEvents will be in a single

EventSet

,
no other events will be in the event set. A resume
must occur to continue execution after any event set which
performs suspensions - in this case to allow proper shutdown.

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

