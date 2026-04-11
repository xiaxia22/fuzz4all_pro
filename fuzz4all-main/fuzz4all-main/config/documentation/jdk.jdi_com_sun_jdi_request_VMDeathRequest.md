# Interface VMDeathRequest

**Source:** `jdk.jdi\com\sun\jdi\request\VMDeathRequest.html`

### Class Description

```java
public interface
VMDeathRequest

extends
EventRequest
```

Request for notification when the target VM terminates.
When an enabled VMDeathRequest is satisfied, an

event set

containing a

VMDeathEvent

will be placed on the

EventQueue

.
The collection of existing VMDeathRequests is
managed by the

EventRequestManager

Even without creating a VMDeathRequest, a single
unsolicited VMDeathEvent will be sent with a

suspend policy

of

SUSPEND_NONE

.
This request would typically be created so that a
VMDeathEvent with a suspend policy of

SUSPEND_ALL

will be sent. This event can be used to assure
completion of any processing which requires the VM
to be alive (e.g. event processing). Note: the
unsolicited VMDeathEvent will still be sent.

**All Superinterfaces:** EventRequest

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

#### Interface VMDeathRequest

**All Superinterfaces:** EventRequest

,

Mirror

```java
public interface
VMDeathRequest

extends
EventRequest
```

Request for notification when the target VM terminates.
When an enabled VMDeathRequest is satisfied, an

event set

containing a

VMDeathEvent

will be placed on the

EventQueue

.
The collection of existing VMDeathRequests is
managed by the

EventRequestManager

Even without creating a VMDeathRequest, a single
unsolicited VMDeathEvent will be sent with a

suspend policy

of

SUSPEND_NONE

.
This request would typically be created so that a
VMDeathEvent with a suspend policy of

SUSPEND_ALL

will be sent. This event can be used to assure
completion of any processing which requires the VM
to be alive (e.g. event processing). Note: the
unsolicited VMDeathEvent will still be sent.

**Since:** 1.4
**See Also:** VMDeathEvent

,

EventQueue

,

EventRequestManager

public interface

VMDeathRequest

extends

EventRequest

Request for notification when the target VM terminates.
When an enabled VMDeathRequest is satisfied, an

event set

containing a

VMDeathEvent

will be placed on the

EventQueue

.
The collection of existing VMDeathRequests is
managed by the

EventRequestManager

Even without creating a VMDeathRequest, a single
unsolicited VMDeathEvent will be sent with a

suspend policy

of

SUSPEND_NONE

.
This request would typically be created so that a
VMDeathEvent with a suspend policy of

SUSPEND_ALL

will be sent. This event can be used to assure
completion of any processing which requires the VM
to be alive (e.g. event processing). Note: the
unsolicited VMDeathEvent will still be sent.

Even without creating a VMDeathRequest, a single
unsolicited VMDeathEvent will be sent with a

suspend policy

of

SUSPEND_NONE

.
This request would typically be created so that a
VMDeathEvent with a suspend policy of

SUSPEND_ALL

will be sent. This event can be used to assure
completion of any processing which requires the VM
to be alive (e.g. event processing). Note: the
unsolicited VMDeathEvent will still be sent.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface com.sun.jdi.request.

EventRequest

SUSPEND_ALL

,

SUSPEND_EVENT_THREAD

,

SUSPEND_NONE

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in interface com.sun.jdi.request.

EventRequest

addCountFilter

,

disable

,

enable

,

getProperty

,

isEnabled

,

putProperty

,

setEnabled

,

setSuspendPolicy

,

suspendPolicy

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

Field Summary

- Fields declared in interface com.sun.jdi.request.

EventRequest

SUSPEND_ALL

,

SUSPEND_EVENT_THREAD

,

SUSPEND_NONE

---

#### Field Summary

Fields declared in interface com.sun.jdi.request.

EventRequest

SUSPEND_ALL

,

SUSPEND_EVENT_THREAD

,

SUSPEND_NONE

---

#### Fields declared in interface com.sun.jdi.request. EventRequest

Method Summary

- Methods declared in interface com.sun.jdi.request.

EventRequest

addCountFilter

,

disable

,

enable

,

getProperty

,

isEnabled

,

putProperty

,

setEnabled

,

setSuspendPolicy

,

suspendPolicy

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Method Summary

Methods declared in interface com.sun.jdi.request.

EventRequest

addCountFilter

,

disable

,

enable

,

getProperty

,

isEnabled

,

putProperty

,

setEnabled

,

setSuspendPolicy

,

suspendPolicy

---

#### Methods declared in interface com.sun.jdi.request. EventRequest

Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

