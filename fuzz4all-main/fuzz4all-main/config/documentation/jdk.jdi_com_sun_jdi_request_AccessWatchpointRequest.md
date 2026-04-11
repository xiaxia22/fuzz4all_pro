# Interface AccessWatchpointRequest

**Source:** `jdk.jdi\com\sun\jdi\request\AccessWatchpointRequest.html`

### Class Description

```java
public interface
AccessWatchpointRequest

extends
WatchpointRequest
```

Request for notification when the contents of a field are accessed
in the target VM.
This event will be triggered when the specified field is accessed
by Java™ programming language code or by a
Java Native Interface (JNI) get function (

Get<Type>Field,
GetStatic<Type>Field

).
Access by JDI does not trigger this event.
When an enabled AccessWatchpointRequest is satisfied, an

event set

containing an

AccessWatchpointEvent

will be placed
on the

EventQueue

.
The collection of existing ExceptionRequests is
managed by the

EventRequestManager

The collection of existing watchpoints is
managed by the

EventRequestManager

.

Note that the modification
of a Field is not considered an access.

**All Superinterfaces:** EventRequest

,

Mirror

,

WatchpointRequest

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Interface AccessWatchpointRequest

**All Superinterfaces:** EventRequest

,

Mirror

,

WatchpointRequest

```java
public interface
AccessWatchpointRequest

extends
WatchpointRequest
```

Request for notification when the contents of a field are accessed
in the target VM.
This event will be triggered when the specified field is accessed
by Java™ programming language code or by a
Java Native Interface (JNI) get function (

Get<Type>Field,
GetStatic<Type>Field

).
Access by JDI does not trigger this event.
When an enabled AccessWatchpointRequest is satisfied, an

event set

containing an

AccessWatchpointEvent

will be placed
on the

EventQueue

.
The collection of existing ExceptionRequests is
managed by the

EventRequestManager

The collection of existing watchpoints is
managed by the

EventRequestManager

.

Note that the modification
of a Field is not considered an access.

**Since:** 1.3
**See Also:** ModificationWatchpointRequest

,

EventQueue

,

EventRequestManager

public interface

AccessWatchpointRequest

extends

WatchpointRequest

Request for notification when the contents of a field are accessed
in the target VM.
This event will be triggered when the specified field is accessed
by Java™ programming language code or by a
Java Native Interface (JNI) get function (

Get<Type>Field,
GetStatic<Type>Field

).
Access by JDI does not trigger this event.
When an enabled AccessWatchpointRequest is satisfied, an

event set

containing an

AccessWatchpointEvent

will be placed
on the

EventQueue

.
The collection of existing ExceptionRequests is
managed by the

EventRequestManager

The collection of existing watchpoints is
managed by the

EventRequestManager

.

Note that the modification
of a Field is not considered an access.

Note that the modification
of a Field is not considered an access.

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

- Methods declared in interface com.sun.jdi.request.

WatchpointRequest

addClassExclusionFilter

,

addClassFilter

,

addClassFilter

,

addInstanceFilter

,

addThreadFilter

,

field

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

- Methods declared in interface com.sun.jdi.request.

WatchpointRequest

addClassExclusionFilter

,

addClassFilter

,

addClassFilter

,

addInstanceFilter

,

addThreadFilter

,

field

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

#### Methods declared in interface com.sun.jdi. Mirror

Methods declared in interface com.sun.jdi.request.

WatchpointRequest

addClassExclusionFilter

,

addClassFilter

,

addClassFilter

,

addInstanceFilter

,

addThreadFilter

,

field

---

