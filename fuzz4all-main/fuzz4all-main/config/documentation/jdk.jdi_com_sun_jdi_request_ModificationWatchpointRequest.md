# Interface ModificationWatchpointRequest

**Source:** `jdk.jdi\com\sun\jdi\request\ModificationWatchpointRequest.html`

### Class Description

```java
public interface
ModificationWatchpointRequest

extends
WatchpointRequest
```

Request for notification when a field is set.
This event will be triggered when a value is assigned to the specified
field with a Java™ programming
language statement (assignment, increment, etc) or by a
Java Native Interface (JNI) set function (

Set<Type>Field,
SetStatic<Type>Field

).
Setting a field to a value which is the same as the previous value
still triggers this event.
Modification by JDI does not trigger this event.
When an enabled ModificationWatchpointRequest is satisfied, an

event set

containing a

ModificationWatchpointEvent

will be placed on the

EventQueue

.
The collection of existing watchpoints is
managed by the

EventRequestManager

.

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

#### Interface ModificationWatchpointRequest

**All Superinterfaces:** EventRequest

,

Mirror

,

WatchpointRequest

```java
public interface
ModificationWatchpointRequest

extends
WatchpointRequest
```

Request for notification when a field is set.
This event will be triggered when a value is assigned to the specified
field with a Java™ programming
language statement (assignment, increment, etc) or by a
Java Native Interface (JNI) set function (

Set<Type>Field,
SetStatic<Type>Field

).
Setting a field to a value which is the same as the previous value
still triggers this event.
Modification by JDI does not trigger this event.
When an enabled ModificationWatchpointRequest is satisfied, an

event set

containing a

ModificationWatchpointEvent

will be placed on the

EventQueue

.
The collection of existing watchpoints is
managed by the

EventRequestManager

.

**Since:** 1.3
**See Also:** ModificationWatchpointEvent

,

AccessWatchpointRequest

,

EventQueue

,

EventRequestManager

public interface

ModificationWatchpointRequest

extends

WatchpointRequest

Request for notification when a field is set.
This event will be triggered when a value is assigned to the specified
field with a Java™ programming
language statement (assignment, increment, etc) or by a
Java Native Interface (JNI) set function (

Set<Type>Field,
SetStatic<Type>Field

).
Setting a field to a value which is the same as the previous value
still triggers this event.
Modification by JDI does not trigger this event.
When an enabled ModificationWatchpointRequest is satisfied, an

event set

containing a

ModificationWatchpointEvent

will be placed on the

EventQueue

.
The collection of existing watchpoints is
managed by the

EventRequestManager

.

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

