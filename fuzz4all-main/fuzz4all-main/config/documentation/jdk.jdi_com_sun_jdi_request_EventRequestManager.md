# Interface EventRequestManager

**Source:** `jdk.jdi\com\sun\jdi\request\EventRequestManager.html`

### Class Description

```java
public interface
EventRequestManager

extends
Mirror
```

Manages the creation and deletion of

EventRequest

s. A single
implementor of this interface exists in a particular VM and
is accessed through

VirtualMachine.eventRequestManager()

**All Superinterfaces:** Mirror

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ClassPrepareRequest
createClassPrepareRequest()

Creates a new disabled

ClassPrepareRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:**
- the created

ClassPrepareRequest

---

#### ClassUnloadRequest
createClassUnloadRequest()

Creates a new disabled

ClassUnloadRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:**
- the created

ClassUnloadRequest

---

#### ThreadStartRequest
createThreadStartRequest()

Creates a new disabled

ThreadStartRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:**
- the created

ThreadStartRequest

---

#### ThreadDeathRequest
createThreadDeathRequest()

Creates a new disabled

ThreadDeathRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:**
- the created

ThreadDeathRequest

---

#### ExceptionRequest
createExceptionRequest​(
ReferenceType
refType,
boolean notifyCaught,
boolean notifyUncaught)

Creates a new disabled

ExceptionRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

A specific exception type and its subclasses can be selected
for exception events. Caught exceptions, uncaught exceptions,
or both can be selected. Note, however, that
at the time an exception is thrown, it is not always
possible to determine whether it is truly caught. See

ExceptionEvent.catchLocation()

for
details.

**Parameters:**
- refType

- If non-null, specifies that exceptions which are
instances of refType will be reported. Note: this
will include instances of sub-types. If null,
all instances will be reported
- notifyCaught

- If true, caught exceptions will be reported.
- notifyUncaught

- If true, uncaught exceptions will be reported.

**Returns:**
- the created

ExceptionRequest

---

#### MethodEntryRequest
createMethodEntryRequest()

Creates a new disabled

MethodEntryRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:**
- the created

MethodEntryRequest

---

#### MethodExitRequest
createMethodExitRequest()

Creates a new disabled

MethodExitRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:**
- the created

MethodExitRequest

---

#### MonitorContendedEnterRequest
createMonitorContendedEnterRequest()

Creates a new disabled

MonitorContendedEnterRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestMonitorEvents()

to determine if the operation is supported.

**Returns:**
- the created

MonitorContendedEnterRequest

**Throws:**
- UnsupportedOperationException

- if
the target VM does not support this
operation.

**Since:**
- 1.6

---

#### MonitorContendedEnteredRequest
createMonitorContendedEnteredRequest()

Creates a new disabled

MonitorContendedEnteredRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestMonitorEvents()

to determine if the operation is supported.

**Returns:**
- the created

MonitorContendedEnteredRequest

**Throws:**
- UnsupportedOperationException

- if
the target VM does not support this
operation.

**Since:**
- 1.6

---

#### MonitorWaitRequest
createMonitorWaitRequest()

Creates a new disabled

MonitorWaitRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestMonitorEvents()

to determine if the operation is supported.

**Returns:**
- the created

MonitorWaitRequest

**Throws:**
- UnsupportedOperationException

- if
the target VM does not support this
operation.

**Since:**
- 1.6

---

#### MonitorWaitedRequest
createMonitorWaitedRequest()

Creates a new disabled

MonitorWaitedRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestMonitorEvents()

to determine if the operation is supported.

**Returns:**
- the created

MonitorWaitedRequest

**Throws:**
- UnsupportedOperationException

- if
the target VM does not support this
operation.

**Since:**
- 1.6

---

#### StepRequest
createStepRequest​(
ThreadReference
thread,
int size,
int depth)

Creates a new disabled

StepRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

The returned request will control stepping only in the specified

thread

; all other threads will be unaffected.
A

size

value of

StepRequest.STEP_MIN

will generate a
step event each time the code index changes. It represents the
smallest step size available and often maps to the instruction
level.
A

size

value of

StepRequest.STEP_LINE

will generate a
step event each time the source line changes unless line number information is not available,
in which case a STEP_MIN will be done instead. For example, no line number information is
available during the execution of a method that has been rendered obsolete by
by a

VirtualMachine.redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

operation.
A

depth

value of

StepRequest.STEP_INTO

will generate
step events in any called methods. A

depth

value
of

StepRequest.STEP_OVER

restricts step events to the current frame
or caller frames. A

depth

value of

StepRequest.STEP_OUT

restricts step events to caller frames only. All depth
restrictions are relative to the call stack immediately before the
step takes place.

Only one pending step request is allowed per thread.

Note that a typical debugger will want to cancel stepping
after the first step is detected. Thus a next line method
would do the following:

```java
EventRequestManager mgr = myVM.{@link VirtualMachine#eventRequestManager eventRequestManager}();
StepRequest request = mgr.createStepRequest(myThread,
StepRequest.{@link StepRequest#STEP_LINE STEP_LINE},
StepRequest.{@link StepRequest#STEP_OVER STEP_OVER});
request.{@link EventRequest#addCountFilter addCountFilter}(1); // next step only
request.enable();
myVM.{@link VirtualMachine#resume resume}();
```

**Parameters:**
- thread

- the thread in which to step
- depth

- the step depth
- size

- the step size

**Returns:**
- the created

StepRequest

**Throws:**
- DuplicateRequestException

- if there is already a pending
step request for the specified thread.
- IllegalArgumentException

- if the size or depth arguments
contain illegal values.

---

#### BreakpointRequest
createBreakpointRequest​(
Location
location)

Creates a new disabled

BreakpointRequest

.
The given

Location

must have a valid
(that is, non-negative) code index. The new
breakpoint is added to the list managed by this
EventRequestManager. Multiple breakpoints at the
same location are permitted. Use

EventRequest.enable()

to
activate this event request.

**Parameters:**
- location

- the location of the new breakpoint.

**Returns:**
- the created

BreakpointRequest

**Throws:**
- NativeMethodException

- if location is within a native method.

---

#### AccessWatchpointRequest
createAccessWatchpointRequest​(
Field
field)

Creates a new disabled watchpoint which watches accesses to the
specified field. The new
watchpoint is added to the list managed by this
EventRequestManager. Multiple watchpoints on the
same field are permitted.
Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canWatchFieldAccess()

to determine if the operation is supported.

**Parameters:**
- field

- the field to watch

**Returns:**
- the created watchpoint

**Throws:**
- UnsupportedOperationException

- if
the target virtual machine does not support this
operation.

---

#### ModificationWatchpointRequest
createModificationWatchpointRequest​(
Field
field)

Creates a new disabled watchpoint which watches accesses to the
specified field. The new
watchpoint is added to the list managed by this
EventRequestManager. Multiple watchpoints on the
same field are permitted.
Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canWatchFieldModification()

to determine if the operation is supported.

**Parameters:**
- field

- the field to watch

**Returns:**
- the created watchpoint

**Throws:**
- UnsupportedOperationException

- if
the target virtual machine does not support this
operation.

---

#### VMDeathRequest
createVMDeathRequest()

Creates a new disabled

VMDeathRequest

.
The new request is added to the list managed by this
EventRequestManager.
Use

EventRequest.enable()

to
activate this event request.

This request (if enabled) will cause a

VMDeathEvent

to be sent on termination of the target VM.

A VMDeathRequest with a suspend policy of

SUSPEND_ALL

can be used to assure processing of incoming

SUSPEND_NONE

or

SUSPEND_EVENT_THREAD

events before VM death. If all event processing is being
done in the same thread as event sets are being read,
enabling the request is all that is needed since the VM
will be suspended until the

EventSet

containing the

VMDeathEvent

is resumed.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestVMDeathEvent()

to determine if the operation is supported.

**Returns:**
- the created request

**Throws:**
- UnsupportedOperationException

- if
the target VM does not support this
operation.

**Since:**
- 1.4

---

#### void deleteEventRequest​(
EventRequest
eventRequest)

Removes an eventRequest. The eventRequest is disabled and
the removed from the requests managed by this
EventRequestManager. Once the eventRequest is deleted, no
operations (for example,

EventRequest.setEnabled(boolean)

)
are permitted - attempts to do so will generally cause an

InvalidRequestStateException

.
No other eventRequests are effected.

Because this method changes the underlying lists of event
requests, attempting to directly delete from a list returned
by a request accessor (e.g. below):

```java
Iterator iter = requestManager.stepRequests().iterator();
while (iter.hasNext()) {
requestManager.deleteEventRequest(iter.next());
}
```

may cause a

ConcurrentModificationException

.
Instead use

deleteEventRequests(List)

or copy the list before iterating.

**Parameters:**
- eventRequest

- the eventRequest to remove

---

#### void deleteEventRequests​(
List
<? extends
EventRequest
> eventRequests)

Removes a list of

EventRequest

s.

**Parameters:**
- eventRequests

- the list of eventRequests to remove

**See Also:**
- deleteEventRequest(EventRequest)

---

#### void deleteAllBreakpoints()

Remove all breakpoints managed by this EventRequestManager.

**See Also:**
- deleteEventRequest(EventRequest)

---

#### List
<
StepRequest
> stepRequests()

Return an unmodifiable list of the enabled and disabled step requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:**
- the all

StepRequest

objects.

---

#### List
<
ClassPrepareRequest
> classPrepareRequests()

Return an unmodifiable list of the enabled and disabled class prepare requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:**
- the all

ClassPrepareRequest

objects.

---

#### List
<
ClassUnloadRequest
> classUnloadRequests()

Return an unmodifiable list of the enabled and disabled class unload requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:**
- the all

ClassUnloadRequest

objects.

---

#### List
<
ThreadStartRequest
> threadStartRequests()

Return an unmodifiable list of the enabled and disabled thread start requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:**
- the all

ThreadStartRequest

objects.

---

#### List
<
ThreadDeathRequest
> threadDeathRequests()

Return an unmodifiable list of the enabled and disabled thread death requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:**
- the all

ThreadDeathRequest

objects.

---

#### List
<
ExceptionRequest
> exceptionRequests()

Return an unmodifiable list of the enabled and disabled exception requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:**
- the all

ExceptionRequest

objects.

---

#### List
<
BreakpointRequest
> breakpointRequests()

Return an unmodifiable list of the enabled and disabled breakpoint requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:**
- the list of all

BreakpointRequest

objects.

---

#### List
<
AccessWatchpointRequest
> accessWatchpointRequests()

Return an unmodifiable list of the enabled and disabled access
watchpoint requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:**
- the all

AccessWatchpointRequest

objects.

---

#### List
<
ModificationWatchpointRequest
> modificationWatchpointRequests()

Return an unmodifiable list of the enabled and disabled modification
watchpoint requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:**
- the all

ModificationWatchpointRequest

objects.

---

#### List
<
MethodEntryRequest
> methodEntryRequests()

Return an unmodifiable list of the enabled and disabled method entry requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:**
- the list of all

MethodEntryRequest

objects.

---

#### List
<
MethodExitRequest
> methodExitRequests()

Return an unmodifiable list of the enabled and disabled method exit requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:**
- the list of all

MethodExitRequest

objects.

---

#### List
<
MonitorContendedEnterRequest
> monitorContendedEnterRequests()

Return an unmodifiable list of the enabled and disabled monitor contended enter requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:**
- the list of all

MonitorContendedEnterRequest

objects.

**Since:**
- 1.6

---

#### List
<
MonitorContendedEnteredRequest
> monitorContendedEnteredRequests()

Return an unmodifiable list of the enabled and disabled monitor contended entered requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:**
- the list of all

MonitorContendedEnteredRequest

objects.

**Since:**
- 1.6

---

#### List
<
MonitorWaitRequest
> monitorWaitRequests()

Return an unmodifiable list of the enabled and disabled monitor wait requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:**
- the list of all

MonitorWaitRequest

objects.

**Since:**
- 1.6

---

#### List
<
MonitorWaitedRequest
> monitorWaitedRequests()

Return an unmodifiable list of the enabled and disabled monitor waited requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:**
- the list of all

MonitorWaitedRequest

objects.

**Since:**
- 1.6

---

#### List
<
VMDeathRequest
> vmDeathRequests()

Return an unmodifiable list of the enabled and disabled VM death requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.
Note: the unsolicited VMDeathEvent does not have a
corresponding request.

**Returns:**
- the list of all

VMDeathRequest

objects.

**Since:**
- 1.4

---

### Additional Sections

#### Interface EventRequestManager

**All Superinterfaces:** Mirror

```java
public interface
EventRequestManager

extends
Mirror
```

Manages the creation and deletion of

EventRequest

s. A single
implementor of this interface exists in a particular VM and
is accessed through

VirtualMachine.eventRequestManager()

**Since:** 1.3
**See Also:** EventRequest

,

Event

,

BreakpointRequest

,

BreakpointEvent

,

VirtualMachine

public interface

EventRequestManager

extends

Mirror

Manages the creation and deletion of

EventRequest

s. A single
implementor of this interface exists in a particular VM and
is accessed through

VirtualMachine.eventRequestManager()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<

AccessWatchpointRequest

>

accessWatchpointRequests

()

Return an unmodifiable list of the enabled and disabled access
watchpoint requests.

List

<

BreakpointRequest

>

breakpointRequests

()

Return an unmodifiable list of the enabled and disabled breakpoint requests.

List

<

ClassPrepareRequest

>

classPrepareRequests

()

Return an unmodifiable list of the enabled and disabled class prepare requests.

List

<

ClassUnloadRequest

>

classUnloadRequests

()

Return an unmodifiable list of the enabled and disabled class unload requests.

AccessWatchpointRequest

createAccessWatchpointRequest

​(

Field

field)

Creates a new disabled watchpoint which watches accesses to the
specified field.

BreakpointRequest

createBreakpointRequest

​(

Location

location)

Creates a new disabled

BreakpointRequest

.

ClassPrepareRequest

createClassPrepareRequest

()

Creates a new disabled

ClassPrepareRequest

.

ClassUnloadRequest

createClassUnloadRequest

()

Creates a new disabled

ClassUnloadRequest

.

ExceptionRequest

createExceptionRequest

​(

ReferenceType

refType,
boolean notifyCaught,
boolean notifyUncaught)

Creates a new disabled

ExceptionRequest

.

MethodEntryRequest

createMethodEntryRequest

()

Creates a new disabled

MethodEntryRequest

.

MethodExitRequest

createMethodExitRequest

()

Creates a new disabled

MethodExitRequest

.

ModificationWatchpointRequest

createModificationWatchpointRequest

​(

Field

field)

Creates a new disabled watchpoint which watches accesses to the
specified field.

MonitorContendedEnteredRequest

createMonitorContendedEnteredRequest

()

Creates a new disabled

MonitorContendedEnteredRequest

.

MonitorContendedEnterRequest

createMonitorContendedEnterRequest

()

Creates a new disabled

MonitorContendedEnterRequest

.

MonitorWaitedRequest

createMonitorWaitedRequest

()

Creates a new disabled

MonitorWaitedRequest

.

MonitorWaitRequest

createMonitorWaitRequest

()

Creates a new disabled

MonitorWaitRequest

.

StepRequest

createStepRequest

​(

ThreadReference

thread,
int size,
int depth)

Creates a new disabled

StepRequest

.

ThreadDeathRequest

createThreadDeathRequest

()

Creates a new disabled

ThreadDeathRequest

.

ThreadStartRequest

createThreadStartRequest

()

Creates a new disabled

ThreadStartRequest

.

VMDeathRequest

createVMDeathRequest

()

Creates a new disabled

VMDeathRequest

.

void

deleteAllBreakpoints

()

Remove all breakpoints managed by this EventRequestManager.

void

deleteEventRequest

​(

EventRequest

eventRequest)

Removes an eventRequest.

void

deleteEventRequests

​(

List

<? extends

EventRequest

> eventRequests)

Removes a list of

EventRequest

s.

List

<

ExceptionRequest

>

exceptionRequests

()

Return an unmodifiable list of the enabled and disabled exception requests.

List

<

MethodEntryRequest

>

methodEntryRequests

()

Return an unmodifiable list of the enabled and disabled method entry requests.

List

<

MethodExitRequest

>

methodExitRequests

()

Return an unmodifiable list of the enabled and disabled method exit requests.

List

<

ModificationWatchpointRequest

>

modificationWatchpointRequests

()

Return an unmodifiable list of the enabled and disabled modification
watchpoint requests.

List

<

MonitorContendedEnteredRequest

>

monitorContendedEnteredRequests

()

Return an unmodifiable list of the enabled and disabled monitor contended entered requests.

List

<

MonitorContendedEnterRequest

>

monitorContendedEnterRequests

()

Return an unmodifiable list of the enabled and disabled monitor contended enter requests.

List

<

MonitorWaitedRequest

>

monitorWaitedRequests

()

Return an unmodifiable list of the enabled and disabled monitor waited requests.

List

<

MonitorWaitRequest

>

monitorWaitRequests

()

Return an unmodifiable list of the enabled and disabled monitor wait requests.

List

<

StepRequest

>

stepRequests

()

Return an unmodifiable list of the enabled and disabled step requests.

List

<

ThreadDeathRequest

>

threadDeathRequests

()

Return an unmodifiable list of the enabled and disabled thread death requests.

List

<

ThreadStartRequest

>

threadStartRequests

()

Return an unmodifiable list of the enabled and disabled thread start requests.

List

<

VMDeathRequest

>

vmDeathRequests

()

Return an unmodifiable list of the enabled and disabled VM death requests.

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

List

<

AccessWatchpointRequest

>

accessWatchpointRequests

()

Return an unmodifiable list of the enabled and disabled access
watchpoint requests.

List

<

BreakpointRequest

>

breakpointRequests

()

Return an unmodifiable list of the enabled and disabled breakpoint requests.

List

<

ClassPrepareRequest

>

classPrepareRequests

()

Return an unmodifiable list of the enabled and disabled class prepare requests.

List

<

ClassUnloadRequest

>

classUnloadRequests

()

Return an unmodifiable list of the enabled and disabled class unload requests.

AccessWatchpointRequest

createAccessWatchpointRequest

​(

Field

field)

Creates a new disabled watchpoint which watches accesses to the
specified field.

BreakpointRequest

createBreakpointRequest

​(

Location

location)

Creates a new disabled

BreakpointRequest

.

ClassPrepareRequest

createClassPrepareRequest

()

Creates a new disabled

ClassPrepareRequest

.

ClassUnloadRequest

createClassUnloadRequest

()

Creates a new disabled

ClassUnloadRequest

.

ExceptionRequest

createExceptionRequest

​(

ReferenceType

refType,
boolean notifyCaught,
boolean notifyUncaught)

Creates a new disabled

ExceptionRequest

.

MethodEntryRequest

createMethodEntryRequest

()

Creates a new disabled

MethodEntryRequest

.

MethodExitRequest

createMethodExitRequest

()

Creates a new disabled

MethodExitRequest

.

ModificationWatchpointRequest

createModificationWatchpointRequest

​(

Field

field)

Creates a new disabled watchpoint which watches accesses to the
specified field.

MonitorContendedEnteredRequest

createMonitorContendedEnteredRequest

()

Creates a new disabled

MonitorContendedEnteredRequest

.

MonitorContendedEnterRequest

createMonitorContendedEnterRequest

()

Creates a new disabled

MonitorContendedEnterRequest

.

MonitorWaitedRequest

createMonitorWaitedRequest

()

Creates a new disabled

MonitorWaitedRequest

.

MonitorWaitRequest

createMonitorWaitRequest

()

Creates a new disabled

MonitorWaitRequest

.

StepRequest

createStepRequest

​(

ThreadReference

thread,
int size,
int depth)

Creates a new disabled

StepRequest

.

ThreadDeathRequest

createThreadDeathRequest

()

Creates a new disabled

ThreadDeathRequest

.

ThreadStartRequest

createThreadStartRequest

()

Creates a new disabled

ThreadStartRequest

.

VMDeathRequest

createVMDeathRequest

()

Creates a new disabled

VMDeathRequest

.

void

deleteAllBreakpoints

()

Remove all breakpoints managed by this EventRequestManager.

void

deleteEventRequest

​(

EventRequest

eventRequest)

Removes an eventRequest.

void

deleteEventRequests

​(

List

<? extends

EventRequest

> eventRequests)

Removes a list of

EventRequest

s.

List

<

ExceptionRequest

>

exceptionRequests

()

Return an unmodifiable list of the enabled and disabled exception requests.

List

<

MethodEntryRequest

>

methodEntryRequests

()

Return an unmodifiable list of the enabled and disabled method entry requests.

List

<

MethodExitRequest

>

methodExitRequests

()

Return an unmodifiable list of the enabled and disabled method exit requests.

List

<

ModificationWatchpointRequest

>

modificationWatchpointRequests

()

Return an unmodifiable list of the enabled and disabled modification
watchpoint requests.

List

<

MonitorContendedEnteredRequest

>

monitorContendedEnteredRequests

()

Return an unmodifiable list of the enabled and disabled monitor contended entered requests.

List

<

MonitorContendedEnterRequest

>

monitorContendedEnterRequests

()

Return an unmodifiable list of the enabled and disabled monitor contended enter requests.

List

<

MonitorWaitedRequest

>

monitorWaitedRequests

()

Return an unmodifiable list of the enabled and disabled monitor waited requests.

List

<

MonitorWaitRequest

>

monitorWaitRequests

()

Return an unmodifiable list of the enabled and disabled monitor wait requests.

List

<

StepRequest

>

stepRequests

()

Return an unmodifiable list of the enabled and disabled step requests.

List

<

ThreadDeathRequest

>

threadDeathRequests

()

Return an unmodifiable list of the enabled and disabled thread death requests.

List

<

ThreadStartRequest

>

threadStartRequests

()

Return an unmodifiable list of the enabled and disabled thread start requests.

List

<

VMDeathRequest

>

vmDeathRequests

()

Return an unmodifiable list of the enabled and disabled VM death requests.

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Method Summary

Return an unmodifiable list of the enabled and disabled access
watchpoint requests.

Return an unmodifiable list of the enabled and disabled breakpoint requests.

Return an unmodifiable list of the enabled and disabled class prepare requests.

Return an unmodifiable list of the enabled and disabled class unload requests.

Creates a new disabled watchpoint which watches accesses to the
specified field.

Creates a new disabled

BreakpointRequest

.

Creates a new disabled

ClassPrepareRequest

.

Creates a new disabled

ClassUnloadRequest

.

Creates a new disabled

ExceptionRequest

.

Creates a new disabled

MethodEntryRequest

.

Creates a new disabled

MethodExitRequest

.

Creates a new disabled

MonitorContendedEnteredRequest

.

Creates a new disabled

MonitorContendedEnterRequest

.

Creates a new disabled

MonitorWaitedRequest

.

Creates a new disabled

MonitorWaitRequest

.

Creates a new disabled

StepRequest

.

Creates a new disabled

ThreadDeathRequest

.

Creates a new disabled

ThreadStartRequest

.

Creates a new disabled

VMDeathRequest

.

Remove all breakpoints managed by this EventRequestManager.

Removes an eventRequest.

Removes a list of

EventRequest

s.

Return an unmodifiable list of the enabled and disabled exception requests.

Return an unmodifiable list of the enabled and disabled method entry requests.

Return an unmodifiable list of the enabled and disabled method exit requests.

Return an unmodifiable list of the enabled and disabled modification
watchpoint requests.

Return an unmodifiable list of the enabled and disabled monitor contended entered requests.

Return an unmodifiable list of the enabled and disabled monitor contended enter requests.

Return an unmodifiable list of the enabled and disabled monitor waited requests.

Return an unmodifiable list of the enabled and disabled monitor wait requests.

Return an unmodifiable list of the enabled and disabled step requests.

Return an unmodifiable list of the enabled and disabled thread death requests.

Return an unmodifiable list of the enabled and disabled thread start requests.

Return an unmodifiable list of the enabled and disabled VM death requests.

Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Methods declared in interface com.sun.jdi. Mirror

============ METHOD DETAIL ==========

- Method Detail

- createClassPrepareRequest

```java
ClassPrepareRequest
createClassPrepareRequest()
```

Creates a new disabled

ClassPrepareRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:** the created

ClassPrepareRequest

- createClassUnloadRequest

```java
ClassUnloadRequest
createClassUnloadRequest()
```

Creates a new disabled

ClassUnloadRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:** the created

ClassUnloadRequest

- createThreadStartRequest

```java
ThreadStartRequest
createThreadStartRequest()
```

Creates a new disabled

ThreadStartRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:** the created

ThreadStartRequest

- createThreadDeathRequest

```java
ThreadDeathRequest
createThreadDeathRequest()
```

Creates a new disabled

ThreadDeathRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:** the created

ThreadDeathRequest

- createExceptionRequest

```java
ExceptionRequest
createExceptionRequest​(
ReferenceType
refType,
boolean notifyCaught,
boolean notifyUncaught)
```

Creates a new disabled

ExceptionRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

A specific exception type and its subclasses can be selected
for exception events. Caught exceptions, uncaught exceptions,
or both can be selected. Note, however, that
at the time an exception is thrown, it is not always
possible to determine whether it is truly caught. See

ExceptionEvent.catchLocation()

for
details.

**Parameters:** refType

- If non-null, specifies that exceptions which are
instances of refType will be reported. Note: this
will include instances of sub-types. If null,
all instances will be reported
**Parameters:** notifyCaught

- If true, caught exceptions will be reported.
**Parameters:** notifyUncaught

- If true, uncaught exceptions will be reported.
**Returns:** the created

ExceptionRequest

- createMethodEntryRequest

```java
MethodEntryRequest
createMethodEntryRequest()
```

Creates a new disabled

MethodEntryRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:** the created

MethodEntryRequest

- createMethodExitRequest

```java
MethodExitRequest
createMethodExitRequest()
```

Creates a new disabled

MethodExitRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:** the created

MethodExitRequest

- createMonitorContendedEnterRequest

```java
MonitorContendedEnterRequest
createMonitorContendedEnterRequest()
```

Creates a new disabled

MonitorContendedEnterRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestMonitorEvents()

to determine if the operation is supported.

**Returns:** the created

MonitorContendedEnterRequest
**Throws:** UnsupportedOperationException

- if
the target VM does not support this
operation.
**Since:** 1.6

- createMonitorContendedEnteredRequest

```java
MonitorContendedEnteredRequest
createMonitorContendedEnteredRequest()
```

Creates a new disabled

MonitorContendedEnteredRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestMonitorEvents()

to determine if the operation is supported.

**Returns:** the created

MonitorContendedEnteredRequest
**Throws:** UnsupportedOperationException

- if
the target VM does not support this
operation.
**Since:** 1.6

- createMonitorWaitRequest

```java
MonitorWaitRequest
createMonitorWaitRequest()
```

Creates a new disabled

MonitorWaitRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestMonitorEvents()

to determine if the operation is supported.

**Returns:** the created

MonitorWaitRequest
**Throws:** UnsupportedOperationException

- if
the target VM does not support this
operation.
**Since:** 1.6

- createMonitorWaitedRequest

```java
MonitorWaitedRequest
createMonitorWaitedRequest()
```

Creates a new disabled

MonitorWaitedRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestMonitorEvents()

to determine if the operation is supported.

**Returns:** the created

MonitorWaitedRequest
**Throws:** UnsupportedOperationException

- if
the target VM does not support this
operation.
**Since:** 1.6

- createStepRequest

```java
StepRequest
createStepRequest​(
ThreadReference
thread,
int size,
int depth)
```

Creates a new disabled

StepRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

The returned request will control stepping only in the specified

thread

; all other threads will be unaffected.
A

size

value of

StepRequest.STEP_MIN

will generate a
step event each time the code index changes. It represents the
smallest step size available and often maps to the instruction
level.
A

size

value of

StepRequest.STEP_LINE

will generate a
step event each time the source line changes unless line number information is not available,
in which case a STEP_MIN will be done instead. For example, no line number information is
available during the execution of a method that has been rendered obsolete by
by a

VirtualMachine.redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

operation.
A

depth

value of

StepRequest.STEP_INTO

will generate
step events in any called methods. A

depth

value
of

StepRequest.STEP_OVER

restricts step events to the current frame
or caller frames. A

depth

value of

StepRequest.STEP_OUT

restricts step events to caller frames only. All depth
restrictions are relative to the call stack immediately before the
step takes place.

Only one pending step request is allowed per thread.

Note that a typical debugger will want to cancel stepping
after the first step is detected. Thus a next line method
would do the following:

```java
EventRequestManager mgr = myVM.{@link VirtualMachine#eventRequestManager eventRequestManager}();
StepRequest request = mgr.createStepRequest(myThread,
StepRequest.{@link StepRequest#STEP_LINE STEP_LINE},
StepRequest.{@link StepRequest#STEP_OVER STEP_OVER});
request.{@link EventRequest#addCountFilter addCountFilter}(1); // next step only
request.enable();
myVM.{@link VirtualMachine#resume resume}();
```

**Parameters:** thread

- the thread in which to step
**Parameters:** depth

- the step depth
**Parameters:** size

- the step size
**Returns:** the created

StepRequest
**Throws:** DuplicateRequestException

- if there is already a pending
step request for the specified thread.
**Throws:** IllegalArgumentException

- if the size or depth arguments
contain illegal values.

- createBreakpointRequest

```java
BreakpointRequest
createBreakpointRequest​(
Location
location)
```

Creates a new disabled

BreakpointRequest

.
The given

Location

must have a valid
(that is, non-negative) code index. The new
breakpoint is added to the list managed by this
EventRequestManager. Multiple breakpoints at the
same location are permitted. Use

EventRequest.enable()

to
activate this event request.

**Parameters:** location

- the location of the new breakpoint.
**Returns:** the created

BreakpointRequest
**Throws:** NativeMethodException

- if location is within a native method.

- createAccessWatchpointRequest

```java
AccessWatchpointRequest
createAccessWatchpointRequest​(
Field
field)
```

Creates a new disabled watchpoint which watches accesses to the
specified field. The new
watchpoint is added to the list managed by this
EventRequestManager. Multiple watchpoints on the
same field are permitted.
Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canWatchFieldAccess()

to determine if the operation is supported.

**Parameters:** field

- the field to watch
**Returns:** the created watchpoint
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.

- createModificationWatchpointRequest

```java
ModificationWatchpointRequest
createModificationWatchpointRequest​(
Field
field)
```

Creates a new disabled watchpoint which watches accesses to the
specified field. The new
watchpoint is added to the list managed by this
EventRequestManager. Multiple watchpoints on the
same field are permitted.
Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canWatchFieldModification()

to determine if the operation is supported.

**Parameters:** field

- the field to watch
**Returns:** the created watchpoint
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.

- createVMDeathRequest

```java
VMDeathRequest
createVMDeathRequest()
```

Creates a new disabled

VMDeathRequest

.
The new request is added to the list managed by this
EventRequestManager.
Use

EventRequest.enable()

to
activate this event request.

This request (if enabled) will cause a

VMDeathEvent

to be sent on termination of the target VM.

A VMDeathRequest with a suspend policy of

SUSPEND_ALL

can be used to assure processing of incoming

SUSPEND_NONE

or

SUSPEND_EVENT_THREAD

events before VM death. If all event processing is being
done in the same thread as event sets are being read,
enabling the request is all that is needed since the VM
will be suspended until the

EventSet

containing the

VMDeathEvent

is resumed.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestVMDeathEvent()

to determine if the operation is supported.

**Returns:** the created request
**Throws:** UnsupportedOperationException

- if
the target VM does not support this
operation.
**Since:** 1.4

- deleteEventRequest

```java
void deleteEventRequest​(
EventRequest
eventRequest)
```

Removes an eventRequest. The eventRequest is disabled and
the removed from the requests managed by this
EventRequestManager. Once the eventRequest is deleted, no
operations (for example,

EventRequest.setEnabled(boolean)

)
are permitted - attempts to do so will generally cause an

InvalidRequestStateException

.
No other eventRequests are effected.

Because this method changes the underlying lists of event
requests, attempting to directly delete from a list returned
by a request accessor (e.g. below):

```java
Iterator iter = requestManager.stepRequests().iterator();
while (iter.hasNext()) {
requestManager.deleteEventRequest(iter.next());
}
```

may cause a

ConcurrentModificationException

.
Instead use

deleteEventRequests(List)

or copy the list before iterating.

**Parameters:** eventRequest

- the eventRequest to remove

- deleteEventRequests

```java
void deleteEventRequests​(
List
<? extends
EventRequest
> eventRequests)
```

Removes a list of

EventRequest

s.

**Parameters:** eventRequests

- the list of eventRequests to remove
**See Also:** deleteEventRequest(EventRequest)

- deleteAllBreakpoints

```java
void deleteAllBreakpoints()
```

Remove all breakpoints managed by this EventRequestManager.

**See Also:** deleteEventRequest(EventRequest)

- stepRequests

```java
List
<
StepRequest
> stepRequests()
```

Return an unmodifiable list of the enabled and disabled step requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

StepRequest

objects.

- classPrepareRequests

```java
List
<
ClassPrepareRequest
> classPrepareRequests()
```

Return an unmodifiable list of the enabled and disabled class prepare requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

ClassPrepareRequest

objects.

- classUnloadRequests

```java
List
<
ClassUnloadRequest
> classUnloadRequests()
```

Return an unmodifiable list of the enabled and disabled class unload requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

ClassUnloadRequest

objects.

- threadStartRequests

```java
List
<
ThreadStartRequest
> threadStartRequests()
```

Return an unmodifiable list of the enabled and disabled thread start requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

ThreadStartRequest

objects.

- threadDeathRequests

```java
List
<
ThreadDeathRequest
> threadDeathRequests()
```

Return an unmodifiable list of the enabled and disabled thread death requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

ThreadDeathRequest

objects.

- exceptionRequests

```java
List
<
ExceptionRequest
> exceptionRequests()
```

Return an unmodifiable list of the enabled and disabled exception requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

ExceptionRequest

objects.

- breakpointRequests

```java
List
<
BreakpointRequest
> breakpointRequests()
```

Return an unmodifiable list of the enabled and disabled breakpoint requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the list of all

BreakpointRequest

objects.

- accessWatchpointRequests

```java
List
<
AccessWatchpointRequest
> accessWatchpointRequests()
```

Return an unmodifiable list of the enabled and disabled access
watchpoint requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

AccessWatchpointRequest

objects.

- modificationWatchpointRequests

```java
List
<
ModificationWatchpointRequest
> modificationWatchpointRequests()
```

Return an unmodifiable list of the enabled and disabled modification
watchpoint requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

ModificationWatchpointRequest

objects.

- methodEntryRequests

```java
List
<
MethodEntryRequest
> methodEntryRequests()
```

Return an unmodifiable list of the enabled and disabled method entry requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the list of all

MethodEntryRequest

objects.

- methodExitRequests

```java
List
<
MethodExitRequest
> methodExitRequests()
```

Return an unmodifiable list of the enabled and disabled method exit requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the list of all

MethodExitRequest

objects.

- monitorContendedEnterRequests

```java
List
<
MonitorContendedEnterRequest
> monitorContendedEnterRequests()
```

Return an unmodifiable list of the enabled and disabled monitor contended enter requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the list of all

MonitorContendedEnterRequest

objects.
**Since:** 1.6

- monitorContendedEnteredRequests

```java
List
<
MonitorContendedEnteredRequest
> monitorContendedEnteredRequests()
```

Return an unmodifiable list of the enabled and disabled monitor contended entered requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the list of all

MonitorContendedEnteredRequest

objects.
**Since:** 1.6

- monitorWaitRequests

```java
List
<
MonitorWaitRequest
> monitorWaitRequests()
```

Return an unmodifiable list of the enabled and disabled monitor wait requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the list of all

MonitorWaitRequest

objects.
**Since:** 1.6

- monitorWaitedRequests

```java
List
<
MonitorWaitedRequest
> monitorWaitedRequests()
```

Return an unmodifiable list of the enabled and disabled monitor waited requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the list of all

MonitorWaitedRequest

objects.
**Since:** 1.6

- vmDeathRequests

```java
List
<
VMDeathRequest
> vmDeathRequests()
```

Return an unmodifiable list of the enabled and disabled VM death requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.
Note: the unsolicited VMDeathEvent does not have a
corresponding request.

**Returns:** the list of all

VMDeathRequest

objects.
**Since:** 1.4

Method Detail

- createClassPrepareRequest

```java
ClassPrepareRequest
createClassPrepareRequest()
```

Creates a new disabled

ClassPrepareRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:** the created

ClassPrepareRequest

- createClassUnloadRequest

```java
ClassUnloadRequest
createClassUnloadRequest()
```

Creates a new disabled

ClassUnloadRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:** the created

ClassUnloadRequest

- createThreadStartRequest

```java
ThreadStartRequest
createThreadStartRequest()
```

Creates a new disabled

ThreadStartRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:** the created

ThreadStartRequest

- createThreadDeathRequest

```java
ThreadDeathRequest
createThreadDeathRequest()
```

Creates a new disabled

ThreadDeathRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:** the created

ThreadDeathRequest

- createExceptionRequest

```java
ExceptionRequest
createExceptionRequest​(
ReferenceType
refType,
boolean notifyCaught,
boolean notifyUncaught)
```

Creates a new disabled

ExceptionRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

A specific exception type and its subclasses can be selected
for exception events. Caught exceptions, uncaught exceptions,
or both can be selected. Note, however, that
at the time an exception is thrown, it is not always
possible to determine whether it is truly caught. See

ExceptionEvent.catchLocation()

for
details.

**Parameters:** refType

- If non-null, specifies that exceptions which are
instances of refType will be reported. Note: this
will include instances of sub-types. If null,
all instances will be reported
**Parameters:** notifyCaught

- If true, caught exceptions will be reported.
**Parameters:** notifyUncaught

- If true, uncaught exceptions will be reported.
**Returns:** the created

ExceptionRequest

- createMethodEntryRequest

```java
MethodEntryRequest
createMethodEntryRequest()
```

Creates a new disabled

MethodEntryRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:** the created

MethodEntryRequest

- createMethodExitRequest

```java
MethodExitRequest
createMethodExitRequest()
```

Creates a new disabled

MethodExitRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:** the created

MethodExitRequest

- createMonitorContendedEnterRequest

```java
MonitorContendedEnterRequest
createMonitorContendedEnterRequest()
```

Creates a new disabled

MonitorContendedEnterRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestMonitorEvents()

to determine if the operation is supported.

**Returns:** the created

MonitorContendedEnterRequest
**Throws:** UnsupportedOperationException

- if
the target VM does not support this
operation.
**Since:** 1.6

- createMonitorContendedEnteredRequest

```java
MonitorContendedEnteredRequest
createMonitorContendedEnteredRequest()
```

Creates a new disabled

MonitorContendedEnteredRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestMonitorEvents()

to determine if the operation is supported.

**Returns:** the created

MonitorContendedEnteredRequest
**Throws:** UnsupportedOperationException

- if
the target VM does not support this
operation.
**Since:** 1.6

- createMonitorWaitRequest

```java
MonitorWaitRequest
createMonitorWaitRequest()
```

Creates a new disabled

MonitorWaitRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestMonitorEvents()

to determine if the operation is supported.

**Returns:** the created

MonitorWaitRequest
**Throws:** UnsupportedOperationException

- if
the target VM does not support this
operation.
**Since:** 1.6

- createMonitorWaitedRequest

```java
MonitorWaitedRequest
createMonitorWaitedRequest()
```

Creates a new disabled

MonitorWaitedRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestMonitorEvents()

to determine if the operation is supported.

**Returns:** the created

MonitorWaitedRequest
**Throws:** UnsupportedOperationException

- if
the target VM does not support this
operation.
**Since:** 1.6

- createStepRequest

```java
StepRequest
createStepRequest​(
ThreadReference
thread,
int size,
int depth)
```

Creates a new disabled

StepRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

The returned request will control stepping only in the specified

thread

; all other threads will be unaffected.
A

size

value of

StepRequest.STEP_MIN

will generate a
step event each time the code index changes. It represents the
smallest step size available and often maps to the instruction
level.
A

size

value of

StepRequest.STEP_LINE

will generate a
step event each time the source line changes unless line number information is not available,
in which case a STEP_MIN will be done instead. For example, no line number information is
available during the execution of a method that has been rendered obsolete by
by a

VirtualMachine.redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

operation.
A

depth

value of

StepRequest.STEP_INTO

will generate
step events in any called methods. A

depth

value
of

StepRequest.STEP_OVER

restricts step events to the current frame
or caller frames. A

depth

value of

StepRequest.STEP_OUT

restricts step events to caller frames only. All depth
restrictions are relative to the call stack immediately before the
step takes place.

Only one pending step request is allowed per thread.

Note that a typical debugger will want to cancel stepping
after the first step is detected. Thus a next line method
would do the following:

```java
EventRequestManager mgr = myVM.{@link VirtualMachine#eventRequestManager eventRequestManager}();
StepRequest request = mgr.createStepRequest(myThread,
StepRequest.{@link StepRequest#STEP_LINE STEP_LINE},
StepRequest.{@link StepRequest#STEP_OVER STEP_OVER});
request.{@link EventRequest#addCountFilter addCountFilter}(1); // next step only
request.enable();
myVM.{@link VirtualMachine#resume resume}();
```

**Parameters:** thread

- the thread in which to step
**Parameters:** depth

- the step depth
**Parameters:** size

- the step size
**Returns:** the created

StepRequest
**Throws:** DuplicateRequestException

- if there is already a pending
step request for the specified thread.
**Throws:** IllegalArgumentException

- if the size or depth arguments
contain illegal values.

- createBreakpointRequest

```java
BreakpointRequest
createBreakpointRequest​(
Location
location)
```

Creates a new disabled

BreakpointRequest

.
The given

Location

must have a valid
(that is, non-negative) code index. The new
breakpoint is added to the list managed by this
EventRequestManager. Multiple breakpoints at the
same location are permitted. Use

EventRequest.enable()

to
activate this event request.

**Parameters:** location

- the location of the new breakpoint.
**Returns:** the created

BreakpointRequest
**Throws:** NativeMethodException

- if location is within a native method.

- createAccessWatchpointRequest

```java
AccessWatchpointRequest
createAccessWatchpointRequest​(
Field
field)
```

Creates a new disabled watchpoint which watches accesses to the
specified field. The new
watchpoint is added to the list managed by this
EventRequestManager. Multiple watchpoints on the
same field are permitted.
Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canWatchFieldAccess()

to determine if the operation is supported.

**Parameters:** field

- the field to watch
**Returns:** the created watchpoint
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.

- createModificationWatchpointRequest

```java
ModificationWatchpointRequest
createModificationWatchpointRequest​(
Field
field)
```

Creates a new disabled watchpoint which watches accesses to the
specified field. The new
watchpoint is added to the list managed by this
EventRequestManager. Multiple watchpoints on the
same field are permitted.
Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canWatchFieldModification()

to determine if the operation is supported.

**Parameters:** field

- the field to watch
**Returns:** the created watchpoint
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.

- createVMDeathRequest

```java
VMDeathRequest
createVMDeathRequest()
```

Creates a new disabled

VMDeathRequest

.
The new request is added to the list managed by this
EventRequestManager.
Use

EventRequest.enable()

to
activate this event request.

This request (if enabled) will cause a

VMDeathEvent

to be sent on termination of the target VM.

A VMDeathRequest with a suspend policy of

SUSPEND_ALL

can be used to assure processing of incoming

SUSPEND_NONE

or

SUSPEND_EVENT_THREAD

events before VM death. If all event processing is being
done in the same thread as event sets are being read,
enabling the request is all that is needed since the VM
will be suspended until the

EventSet

containing the

VMDeathEvent

is resumed.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestVMDeathEvent()

to determine if the operation is supported.

**Returns:** the created request
**Throws:** UnsupportedOperationException

- if
the target VM does not support this
operation.
**Since:** 1.4

- deleteEventRequest

```java
void deleteEventRequest​(
EventRequest
eventRequest)
```

Removes an eventRequest. The eventRequest is disabled and
the removed from the requests managed by this
EventRequestManager. Once the eventRequest is deleted, no
operations (for example,

EventRequest.setEnabled(boolean)

)
are permitted - attempts to do so will generally cause an

InvalidRequestStateException

.
No other eventRequests are effected.

Because this method changes the underlying lists of event
requests, attempting to directly delete from a list returned
by a request accessor (e.g. below):

```java
Iterator iter = requestManager.stepRequests().iterator();
while (iter.hasNext()) {
requestManager.deleteEventRequest(iter.next());
}
```

may cause a

ConcurrentModificationException

.
Instead use

deleteEventRequests(List)

or copy the list before iterating.

**Parameters:** eventRequest

- the eventRequest to remove

- deleteEventRequests

```java
void deleteEventRequests​(
List
<? extends
EventRequest
> eventRequests)
```

Removes a list of

EventRequest

s.

**Parameters:** eventRequests

- the list of eventRequests to remove
**See Also:** deleteEventRequest(EventRequest)

- deleteAllBreakpoints

```java
void deleteAllBreakpoints()
```

Remove all breakpoints managed by this EventRequestManager.

**See Also:** deleteEventRequest(EventRequest)

- stepRequests

```java
List
<
StepRequest
> stepRequests()
```

Return an unmodifiable list of the enabled and disabled step requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

StepRequest

objects.

- classPrepareRequests

```java
List
<
ClassPrepareRequest
> classPrepareRequests()
```

Return an unmodifiable list of the enabled and disabled class prepare requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

ClassPrepareRequest

objects.

- classUnloadRequests

```java
List
<
ClassUnloadRequest
> classUnloadRequests()
```

Return an unmodifiable list of the enabled and disabled class unload requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

ClassUnloadRequest

objects.

- threadStartRequests

```java
List
<
ThreadStartRequest
> threadStartRequests()
```

Return an unmodifiable list of the enabled and disabled thread start requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

ThreadStartRequest

objects.

- threadDeathRequests

```java
List
<
ThreadDeathRequest
> threadDeathRequests()
```

Return an unmodifiable list of the enabled and disabled thread death requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

ThreadDeathRequest

objects.

- exceptionRequests

```java
List
<
ExceptionRequest
> exceptionRequests()
```

Return an unmodifiable list of the enabled and disabled exception requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

ExceptionRequest

objects.

- breakpointRequests

```java
List
<
BreakpointRequest
> breakpointRequests()
```

Return an unmodifiable list of the enabled and disabled breakpoint requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the list of all

BreakpointRequest

objects.

- accessWatchpointRequests

```java
List
<
AccessWatchpointRequest
> accessWatchpointRequests()
```

Return an unmodifiable list of the enabled and disabled access
watchpoint requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

AccessWatchpointRequest

objects.

- modificationWatchpointRequests

```java
List
<
ModificationWatchpointRequest
> modificationWatchpointRequests()
```

Return an unmodifiable list of the enabled and disabled modification
watchpoint requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

ModificationWatchpointRequest

objects.

- methodEntryRequests

```java
List
<
MethodEntryRequest
> methodEntryRequests()
```

Return an unmodifiable list of the enabled and disabled method entry requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the list of all

MethodEntryRequest

objects.

- methodExitRequests

```java
List
<
MethodExitRequest
> methodExitRequests()
```

Return an unmodifiable list of the enabled and disabled method exit requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the list of all

MethodExitRequest

objects.

- monitorContendedEnterRequests

```java
List
<
MonitorContendedEnterRequest
> monitorContendedEnterRequests()
```

Return an unmodifiable list of the enabled and disabled monitor contended enter requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the list of all

MonitorContendedEnterRequest

objects.
**Since:** 1.6

- monitorContendedEnteredRequests

```java
List
<
MonitorContendedEnteredRequest
> monitorContendedEnteredRequests()
```

Return an unmodifiable list of the enabled and disabled monitor contended entered requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the list of all

MonitorContendedEnteredRequest

objects.
**Since:** 1.6

- monitorWaitRequests

```java
List
<
MonitorWaitRequest
> monitorWaitRequests()
```

Return an unmodifiable list of the enabled and disabled monitor wait requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the list of all

MonitorWaitRequest

objects.
**Since:** 1.6

- monitorWaitedRequests

```java
List
<
MonitorWaitedRequest
> monitorWaitedRequests()
```

Return an unmodifiable list of the enabled and disabled monitor waited requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the list of all

MonitorWaitedRequest

objects.
**Since:** 1.6

- vmDeathRequests

```java
List
<
VMDeathRequest
> vmDeathRequests()
```

Return an unmodifiable list of the enabled and disabled VM death requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.
Note: the unsolicited VMDeathEvent does not have a
corresponding request.

**Returns:** the list of all

VMDeathRequest

objects.
**Since:** 1.4

---

#### Method Detail

createClassPrepareRequest

```java
ClassPrepareRequest
createClassPrepareRequest()
```

Creates a new disabled

ClassPrepareRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:** the created

ClassPrepareRequest

---

#### createClassPrepareRequest

ClassPrepareRequest

createClassPrepareRequest()

Creates a new disabled

ClassPrepareRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

createClassUnloadRequest

```java
ClassUnloadRequest
createClassUnloadRequest()
```

Creates a new disabled

ClassUnloadRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:** the created

ClassUnloadRequest

---

#### createClassUnloadRequest

ClassUnloadRequest

createClassUnloadRequest()

Creates a new disabled

ClassUnloadRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

createThreadStartRequest

```java
ThreadStartRequest
createThreadStartRequest()
```

Creates a new disabled

ThreadStartRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:** the created

ThreadStartRequest

---

#### createThreadStartRequest

ThreadStartRequest

createThreadStartRequest()

Creates a new disabled

ThreadStartRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

createThreadDeathRequest

```java
ThreadDeathRequest
createThreadDeathRequest()
```

Creates a new disabled

ThreadDeathRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:** the created

ThreadDeathRequest

---

#### createThreadDeathRequest

ThreadDeathRequest

createThreadDeathRequest()

Creates a new disabled

ThreadDeathRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

createExceptionRequest

```java
ExceptionRequest
createExceptionRequest​(
ReferenceType
refType,
boolean notifyCaught,
boolean notifyUncaught)
```

Creates a new disabled

ExceptionRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

A specific exception type and its subclasses can be selected
for exception events. Caught exceptions, uncaught exceptions,
or both can be selected. Note, however, that
at the time an exception is thrown, it is not always
possible to determine whether it is truly caught. See

ExceptionEvent.catchLocation()

for
details.

**Parameters:** refType

- If non-null, specifies that exceptions which are
instances of refType will be reported. Note: this
will include instances of sub-types. If null,
all instances will be reported
**Parameters:** notifyCaught

- If true, caught exceptions will be reported.
**Parameters:** notifyUncaught

- If true, uncaught exceptions will be reported.
**Returns:** the created

ExceptionRequest

---

#### createExceptionRequest

ExceptionRequest

createExceptionRequest​(

ReferenceType

refType,
boolean notifyCaught,
boolean notifyUncaught)

Creates a new disabled

ExceptionRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

A specific exception type and its subclasses can be selected
for exception events. Caught exceptions, uncaught exceptions,
or both can be selected. Note, however, that
at the time an exception is thrown, it is not always
possible to determine whether it is truly caught. See

ExceptionEvent.catchLocation()

for
details.

A specific exception type and its subclasses can be selected
for exception events. Caught exceptions, uncaught exceptions,
or both can be selected. Note, however, that
at the time an exception is thrown, it is not always
possible to determine whether it is truly caught. See

ExceptionEvent.catchLocation()

for
details.

createMethodEntryRequest

```java
MethodEntryRequest
createMethodEntryRequest()
```

Creates a new disabled

MethodEntryRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:** the created

MethodEntryRequest

---

#### createMethodEntryRequest

MethodEntryRequest

createMethodEntryRequest()

Creates a new disabled

MethodEntryRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

createMethodExitRequest

```java
MethodExitRequest
createMethodExitRequest()
```

Creates a new disabled

MethodExitRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

**Returns:** the created

MethodExitRequest

---

#### createMethodExitRequest

MethodExitRequest

createMethodExitRequest()

Creates a new disabled

MethodExitRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

createMonitorContendedEnterRequest

```java
MonitorContendedEnterRequest
createMonitorContendedEnterRequest()
```

Creates a new disabled

MonitorContendedEnterRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestMonitorEvents()

to determine if the operation is supported.

**Returns:** the created

MonitorContendedEnterRequest
**Throws:** UnsupportedOperationException

- if
the target VM does not support this
operation.
**Since:** 1.6

---

#### createMonitorContendedEnterRequest

MonitorContendedEnterRequest

createMonitorContendedEnterRequest()

Creates a new disabled

MonitorContendedEnterRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestMonitorEvents()

to determine if the operation is supported.

createMonitorContendedEnteredRequest

```java
MonitorContendedEnteredRequest
createMonitorContendedEnteredRequest()
```

Creates a new disabled

MonitorContendedEnteredRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestMonitorEvents()

to determine if the operation is supported.

**Returns:** the created

MonitorContendedEnteredRequest
**Throws:** UnsupportedOperationException

- if
the target VM does not support this
operation.
**Since:** 1.6

---

#### createMonitorContendedEnteredRequest

MonitorContendedEnteredRequest

createMonitorContendedEnteredRequest()

Creates a new disabled

MonitorContendedEnteredRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestMonitorEvents()

to determine if the operation is supported.

createMonitorWaitRequest

```java
MonitorWaitRequest
createMonitorWaitRequest()
```

Creates a new disabled

MonitorWaitRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestMonitorEvents()

to determine if the operation is supported.

**Returns:** the created

MonitorWaitRequest
**Throws:** UnsupportedOperationException

- if
the target VM does not support this
operation.
**Since:** 1.6

---

#### createMonitorWaitRequest

MonitorWaitRequest

createMonitorWaitRequest()

Creates a new disabled

MonitorWaitRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestMonitorEvents()

to determine if the operation is supported.

createMonitorWaitedRequest

```java
MonitorWaitedRequest
createMonitorWaitedRequest()
```

Creates a new disabled

MonitorWaitedRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestMonitorEvents()

to determine if the operation is supported.

**Returns:** the created

MonitorWaitedRequest
**Throws:** UnsupportedOperationException

- if
the target VM does not support this
operation.
**Since:** 1.6

---

#### createMonitorWaitedRequest

MonitorWaitedRequest

createMonitorWaitedRequest()

Creates a new disabled

MonitorWaitedRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestMonitorEvents()

to determine if the operation is supported.

createStepRequest

```java
StepRequest
createStepRequest​(
ThreadReference
thread,
int size,
int depth)
```

Creates a new disabled

StepRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

The returned request will control stepping only in the specified

thread

; all other threads will be unaffected.
A

size

value of

StepRequest.STEP_MIN

will generate a
step event each time the code index changes. It represents the
smallest step size available and often maps to the instruction
level.
A

size

value of

StepRequest.STEP_LINE

will generate a
step event each time the source line changes unless line number information is not available,
in which case a STEP_MIN will be done instead. For example, no line number information is
available during the execution of a method that has been rendered obsolete by
by a

VirtualMachine.redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

operation.
A

depth

value of

StepRequest.STEP_INTO

will generate
step events in any called methods. A

depth

value
of

StepRequest.STEP_OVER

restricts step events to the current frame
or caller frames. A

depth

value of

StepRequest.STEP_OUT

restricts step events to caller frames only. All depth
restrictions are relative to the call stack immediately before the
step takes place.

Only one pending step request is allowed per thread.

Note that a typical debugger will want to cancel stepping
after the first step is detected. Thus a next line method
would do the following:

```java
EventRequestManager mgr = myVM.{@link VirtualMachine#eventRequestManager eventRequestManager}();
StepRequest request = mgr.createStepRequest(myThread,
StepRequest.{@link StepRequest#STEP_LINE STEP_LINE},
StepRequest.{@link StepRequest#STEP_OVER STEP_OVER});
request.{@link EventRequest#addCountFilter addCountFilter}(1); // next step only
request.enable();
myVM.{@link VirtualMachine#resume resume}();
```

**Parameters:** thread

- the thread in which to step
**Parameters:** depth

- the step depth
**Parameters:** size

- the step size
**Returns:** the created

StepRequest
**Throws:** DuplicateRequestException

- if there is already a pending
step request for the specified thread.
**Throws:** IllegalArgumentException

- if the size or depth arguments
contain illegal values.

---

#### createStepRequest

StepRequest

createStepRequest​(

ThreadReference

thread,
int size,
int depth)

Creates a new disabled

StepRequest

.
The new event request is added to the list managed by this
EventRequestManager. Use

EventRequest.enable()

to
activate this event request.

The returned request will control stepping only in the specified

thread

; all other threads will be unaffected.
A

size

value of

StepRequest.STEP_MIN

will generate a
step event each time the code index changes. It represents the
smallest step size available and often maps to the instruction
level.
A

size

value of

StepRequest.STEP_LINE

will generate a
step event each time the source line changes unless line number information is not available,
in which case a STEP_MIN will be done instead. For example, no line number information is
available during the execution of a method that has been rendered obsolete by
by a

VirtualMachine.redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

operation.
A

depth

value of

StepRequest.STEP_INTO

will generate
step events in any called methods. A

depth

value
of

StepRequest.STEP_OVER

restricts step events to the current frame
or caller frames. A

depth

value of

StepRequest.STEP_OUT

restricts step events to caller frames only. All depth
restrictions are relative to the call stack immediately before the
step takes place.

Only one pending step request is allowed per thread.

Note that a typical debugger will want to cancel stepping
after the first step is detected. Thus a next line method
would do the following:

```java
EventRequestManager mgr = myVM.{@link VirtualMachine#eventRequestManager eventRequestManager}();
StepRequest request = mgr.createStepRequest(myThread,
StepRequest.{@link StepRequest#STEP_LINE STEP_LINE},
StepRequest.{@link StepRequest#STEP_OVER STEP_OVER});
request.{@link EventRequest#addCountFilter addCountFilter}(1); // next step only
request.enable();
myVM.{@link VirtualMachine#resume resume}();
```

The returned request will control stepping only in the specified

thread

; all other threads will be unaffected.
A

size

value of

StepRequest.STEP_MIN

will generate a
step event each time the code index changes. It represents the
smallest step size available and often maps to the instruction
level.
A

size

value of

StepRequest.STEP_LINE

will generate a
step event each time the source line changes unless line number information is not available,
in which case a STEP_MIN will be done instead. For example, no line number information is
available during the execution of a method that has been rendered obsolete by
by a

VirtualMachine.redefineClasses(java.util.Map<? extends com.sun.jdi.ReferenceType, byte[]>)

operation.
A

depth

value of

StepRequest.STEP_INTO

will generate
step events in any called methods. A

depth

value
of

StepRequest.STEP_OVER

restricts step events to the current frame
or caller frames. A

depth

value of

StepRequest.STEP_OUT

restricts step events to caller frames only. All depth
restrictions are relative to the call stack immediately before the
step takes place.

Only one pending step request is allowed per thread.

Note that a typical debugger will want to cancel stepping
after the first step is detected. Thus a next line method
would do the following:

```java
EventRequestManager mgr = myVM.{@link VirtualMachine#eventRequestManager eventRequestManager}();
StepRequest request = mgr.createStepRequest(myThread,
StepRequest.{@link StepRequest#STEP_LINE STEP_LINE},
StepRequest.{@link StepRequest#STEP_OVER STEP_OVER});
request.{@link EventRequest#addCountFilter addCountFilter}(1); // next step only
request.enable();
myVM.{@link VirtualMachine#resume resume}();
```

Only one pending step request is allowed per thread.

Note that a typical debugger will want to cancel stepping
after the first step is detected. Thus a next line method
would do the following:

```java
EventRequestManager mgr = myVM.{@link VirtualMachine#eventRequestManager eventRequestManager}();
StepRequest request = mgr.createStepRequest(myThread,
StepRequest.{@link StepRequest#STEP_LINE STEP_LINE},
StepRequest.{@link StepRequest#STEP_OVER STEP_OVER});
request.{@link EventRequest#addCountFilter addCountFilter}(1); // next step only
request.enable();
myVM.{@link VirtualMachine#resume resume}();
```

Note that a typical debugger will want to cancel stepping
after the first step is detected. Thus a next line method
would do the following:

```java
EventRequestManager mgr = myVM.{@link VirtualMachine#eventRequestManager eventRequestManager}();
StepRequest request = mgr.createStepRequest(myThread,
StepRequest.{@link StepRequest#STEP_LINE STEP_LINE},
StepRequest.{@link StepRequest#STEP_OVER STEP_OVER});
request.{@link EventRequest#addCountFilter addCountFilter}(1); // next step only
request.enable();
myVM.{@link VirtualMachine#resume resume}();
```

EventRequestManager mgr = myVM.{@link VirtualMachine#eventRequestManager eventRequestManager}();
StepRequest request = mgr.createStepRequest(myThread,
StepRequest.{@link StepRequest#STEP_LINE STEP_LINE},
StepRequest.{@link StepRequest#STEP_OVER STEP_OVER});
request.{@link EventRequest#addCountFilter addCountFilter}(1); // next step only
request.enable();
myVM.{@link VirtualMachine#resume resume}();

createBreakpointRequest

```java
BreakpointRequest
createBreakpointRequest​(
Location
location)
```

Creates a new disabled

BreakpointRequest

.
The given

Location

must have a valid
(that is, non-negative) code index. The new
breakpoint is added to the list managed by this
EventRequestManager. Multiple breakpoints at the
same location are permitted. Use

EventRequest.enable()

to
activate this event request.

**Parameters:** location

- the location of the new breakpoint.
**Returns:** the created

BreakpointRequest
**Throws:** NativeMethodException

- if location is within a native method.

---

#### createBreakpointRequest

BreakpointRequest

createBreakpointRequest​(

Location

location)

Creates a new disabled

BreakpointRequest

.
The given

Location

must have a valid
(that is, non-negative) code index. The new
breakpoint is added to the list managed by this
EventRequestManager. Multiple breakpoints at the
same location are permitted. Use

EventRequest.enable()

to
activate this event request.

createAccessWatchpointRequest

```java
AccessWatchpointRequest
createAccessWatchpointRequest​(
Field
field)
```

Creates a new disabled watchpoint which watches accesses to the
specified field. The new
watchpoint is added to the list managed by this
EventRequestManager. Multiple watchpoints on the
same field are permitted.
Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canWatchFieldAccess()

to determine if the operation is supported.

**Parameters:** field

- the field to watch
**Returns:** the created watchpoint
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.

---

#### createAccessWatchpointRequest

AccessWatchpointRequest

createAccessWatchpointRequest​(

Field

field)

Creates a new disabled watchpoint which watches accesses to the
specified field. The new
watchpoint is added to the list managed by this
EventRequestManager. Multiple watchpoints on the
same field are permitted.
Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canWatchFieldAccess()

to determine if the operation is supported.

Not all target virtual machines support this operation.
Use

VirtualMachine.canWatchFieldAccess()

to determine if the operation is supported.

createModificationWatchpointRequest

```java
ModificationWatchpointRequest
createModificationWatchpointRequest​(
Field
field)
```

Creates a new disabled watchpoint which watches accesses to the
specified field. The new
watchpoint is added to the list managed by this
EventRequestManager. Multiple watchpoints on the
same field are permitted.
Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canWatchFieldModification()

to determine if the operation is supported.

**Parameters:** field

- the field to watch
**Returns:** the created watchpoint
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.

---

#### createModificationWatchpointRequest

ModificationWatchpointRequest

createModificationWatchpointRequest​(

Field

field)

Creates a new disabled watchpoint which watches accesses to the
specified field. The new
watchpoint is added to the list managed by this
EventRequestManager. Multiple watchpoints on the
same field are permitted.
Use

EventRequest.enable()

to
activate this event request.

Not all target virtual machines support this operation.
Use

VirtualMachine.canWatchFieldModification()

to determine if the operation is supported.

Not all target virtual machines support this operation.
Use

VirtualMachine.canWatchFieldModification()

to determine if the operation is supported.

createVMDeathRequest

```java
VMDeathRequest
createVMDeathRequest()
```

Creates a new disabled

VMDeathRequest

.
The new request is added to the list managed by this
EventRequestManager.
Use

EventRequest.enable()

to
activate this event request.

This request (if enabled) will cause a

VMDeathEvent

to be sent on termination of the target VM.

A VMDeathRequest with a suspend policy of

SUSPEND_ALL

can be used to assure processing of incoming

SUSPEND_NONE

or

SUSPEND_EVENT_THREAD

events before VM death. If all event processing is being
done in the same thread as event sets are being read,
enabling the request is all that is needed since the VM
will be suspended until the

EventSet

containing the

VMDeathEvent

is resumed.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestVMDeathEvent()

to determine if the operation is supported.

**Returns:** the created request
**Throws:** UnsupportedOperationException

- if
the target VM does not support this
operation.
**Since:** 1.4

---

#### createVMDeathRequest

VMDeathRequest

createVMDeathRequest()

Creates a new disabled

VMDeathRequest

.
The new request is added to the list managed by this
EventRequestManager.
Use

EventRequest.enable()

to
activate this event request.

This request (if enabled) will cause a

VMDeathEvent

to be sent on termination of the target VM.

A VMDeathRequest with a suspend policy of

SUSPEND_ALL

can be used to assure processing of incoming

SUSPEND_NONE

or

SUSPEND_EVENT_THREAD

events before VM death. If all event processing is being
done in the same thread as event sets are being read,
enabling the request is all that is needed since the VM
will be suspended until the

EventSet

containing the

VMDeathEvent

is resumed.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestVMDeathEvent()

to determine if the operation is supported.

This request (if enabled) will cause a

VMDeathEvent

to be sent on termination of the target VM.

A VMDeathRequest with a suspend policy of

SUSPEND_ALL

can be used to assure processing of incoming

SUSPEND_NONE

or

SUSPEND_EVENT_THREAD

events before VM death. If all event processing is being
done in the same thread as event sets are being read,
enabling the request is all that is needed since the VM
will be suspended until the

EventSet

containing the

VMDeathEvent

is resumed.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestVMDeathEvent()

to determine if the operation is supported.

A VMDeathRequest with a suspend policy of

SUSPEND_ALL

can be used to assure processing of incoming

SUSPEND_NONE

or

SUSPEND_EVENT_THREAD

events before VM death. If all event processing is being
done in the same thread as event sets are being read,
enabling the request is all that is needed since the VM
will be suspended until the

EventSet

containing the

VMDeathEvent

is resumed.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestVMDeathEvent()

to determine if the operation is supported.

Not all target virtual machines support this operation.
Use

VirtualMachine.canRequestVMDeathEvent()

to determine if the operation is supported.

deleteEventRequest

```java
void deleteEventRequest​(
EventRequest
eventRequest)
```

Removes an eventRequest. The eventRequest is disabled and
the removed from the requests managed by this
EventRequestManager. Once the eventRequest is deleted, no
operations (for example,

EventRequest.setEnabled(boolean)

)
are permitted - attempts to do so will generally cause an

InvalidRequestStateException

.
No other eventRequests are effected.

Because this method changes the underlying lists of event
requests, attempting to directly delete from a list returned
by a request accessor (e.g. below):

```java
Iterator iter = requestManager.stepRequests().iterator();
while (iter.hasNext()) {
requestManager.deleteEventRequest(iter.next());
}
```

may cause a

ConcurrentModificationException

.
Instead use

deleteEventRequests(List)

or copy the list before iterating.

**Parameters:** eventRequest

- the eventRequest to remove

---

#### deleteEventRequest

void deleteEventRequest​(

EventRequest

eventRequest)

Removes an eventRequest. The eventRequest is disabled and
the removed from the requests managed by this
EventRequestManager. Once the eventRequest is deleted, no
operations (for example,

EventRequest.setEnabled(boolean)

)
are permitted - attempts to do so will generally cause an

InvalidRequestStateException

.
No other eventRequests are effected.

Because this method changes the underlying lists of event
requests, attempting to directly delete from a list returned
by a request accessor (e.g. below):

```java
Iterator iter = requestManager.stepRequests().iterator();
while (iter.hasNext()) {
requestManager.deleteEventRequest(iter.next());
}
```

may cause a

ConcurrentModificationException

.
Instead use

deleteEventRequests(List)

or copy the list before iterating.

Because this method changes the underlying lists of event
requests, attempting to directly delete from a list returned
by a request accessor (e.g. below):

```java
Iterator iter = requestManager.stepRequests().iterator();
while (iter.hasNext()) {
requestManager.deleteEventRequest(iter.next());
}
```

may cause a

ConcurrentModificationException

.
Instead use

deleteEventRequests(List)

or copy the list before iterating.

Iterator iter = requestManager.stepRequests().iterator();
while (iter.hasNext()) {
requestManager.deleteEventRequest(iter.next());
}

deleteEventRequests

```java
void deleteEventRequests​(
List
<? extends
EventRequest
> eventRequests)
```

Removes a list of

EventRequest

s.

**Parameters:** eventRequests

- the list of eventRequests to remove
**See Also:** deleteEventRequest(EventRequest)

---

#### deleteEventRequests

void deleteEventRequests​(

List

<? extends

EventRequest

> eventRequests)

Removes a list of

EventRequest

s.

deleteAllBreakpoints

```java
void deleteAllBreakpoints()
```

Remove all breakpoints managed by this EventRequestManager.

**See Also:** deleteEventRequest(EventRequest)

---

#### deleteAllBreakpoints

void deleteAllBreakpoints()

Remove all breakpoints managed by this EventRequestManager.

stepRequests

```java
List
<
StepRequest
> stepRequests()
```

Return an unmodifiable list of the enabled and disabled step requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

StepRequest

objects.

---

#### stepRequests

List

<

StepRequest

> stepRequests()

Return an unmodifiable list of the enabled and disabled step requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

classPrepareRequests

```java
List
<
ClassPrepareRequest
> classPrepareRequests()
```

Return an unmodifiable list of the enabled and disabled class prepare requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

ClassPrepareRequest

objects.

---

#### classPrepareRequests

List

<

ClassPrepareRequest

> classPrepareRequests()

Return an unmodifiable list of the enabled and disabled class prepare requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

classUnloadRequests

```java
List
<
ClassUnloadRequest
> classUnloadRequests()
```

Return an unmodifiable list of the enabled and disabled class unload requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

ClassUnloadRequest

objects.

---

#### classUnloadRequests

List

<

ClassUnloadRequest

> classUnloadRequests()

Return an unmodifiable list of the enabled and disabled class unload requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

threadStartRequests

```java
List
<
ThreadStartRequest
> threadStartRequests()
```

Return an unmodifiable list of the enabled and disabled thread start requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

ThreadStartRequest

objects.

---

#### threadStartRequests

List

<

ThreadStartRequest

> threadStartRequests()

Return an unmodifiable list of the enabled and disabled thread start requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

threadDeathRequests

```java
List
<
ThreadDeathRequest
> threadDeathRequests()
```

Return an unmodifiable list of the enabled and disabled thread death requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

ThreadDeathRequest

objects.

---

#### threadDeathRequests

List

<

ThreadDeathRequest

> threadDeathRequests()

Return an unmodifiable list of the enabled and disabled thread death requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

exceptionRequests

```java
List
<
ExceptionRequest
> exceptionRequests()
```

Return an unmodifiable list of the enabled and disabled exception requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

ExceptionRequest

objects.

---

#### exceptionRequests

List

<

ExceptionRequest

> exceptionRequests()

Return an unmodifiable list of the enabled and disabled exception requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

breakpointRequests

```java
List
<
BreakpointRequest
> breakpointRequests()
```

Return an unmodifiable list of the enabled and disabled breakpoint requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the list of all

BreakpointRequest

objects.

---

#### breakpointRequests

List

<

BreakpointRequest

> breakpointRequests()

Return an unmodifiable list of the enabled and disabled breakpoint requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

accessWatchpointRequests

```java
List
<
AccessWatchpointRequest
> accessWatchpointRequests()
```

Return an unmodifiable list of the enabled and disabled access
watchpoint requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

AccessWatchpointRequest

objects.

---

#### accessWatchpointRequests

List

<

AccessWatchpointRequest

> accessWatchpointRequests()

Return an unmodifiable list of the enabled and disabled access
watchpoint requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

modificationWatchpointRequests

```java
List
<
ModificationWatchpointRequest
> modificationWatchpointRequests()
```

Return an unmodifiable list of the enabled and disabled modification
watchpoint requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the all

ModificationWatchpointRequest

objects.

---

#### modificationWatchpointRequests

List

<

ModificationWatchpointRequest

> modificationWatchpointRequests()

Return an unmodifiable list of the enabled and disabled modification
watchpoint requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

methodEntryRequests

```java
List
<
MethodEntryRequest
> methodEntryRequests()
```

Return an unmodifiable list of the enabled and disabled method entry requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the list of all

MethodEntryRequest

objects.

---

#### methodEntryRequests

List

<

MethodEntryRequest

> methodEntryRequests()

Return an unmodifiable list of the enabled and disabled method entry requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

methodExitRequests

```java
List
<
MethodExitRequest
> methodExitRequests()
```

Return an unmodifiable list of the enabled and disabled method exit requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the list of all

MethodExitRequest

objects.

---

#### methodExitRequests

List

<

MethodExitRequest

> methodExitRequests()

Return an unmodifiable list of the enabled and disabled method exit requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

monitorContendedEnterRequests

```java
List
<
MonitorContendedEnterRequest
> monitorContendedEnterRequests()
```

Return an unmodifiable list of the enabled and disabled monitor contended enter requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the list of all

MonitorContendedEnterRequest

objects.
**Since:** 1.6

---

#### monitorContendedEnterRequests

List

<

MonitorContendedEnterRequest

> monitorContendedEnterRequests()

Return an unmodifiable list of the enabled and disabled monitor contended enter requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

monitorContendedEnteredRequests

```java
List
<
MonitorContendedEnteredRequest
> monitorContendedEnteredRequests()
```

Return an unmodifiable list of the enabled and disabled monitor contended entered requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the list of all

MonitorContendedEnteredRequest

objects.
**Since:** 1.6

---

#### monitorContendedEnteredRequests

List

<

MonitorContendedEnteredRequest

> monitorContendedEnteredRequests()

Return an unmodifiable list of the enabled and disabled monitor contended entered requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

monitorWaitRequests

```java
List
<
MonitorWaitRequest
> monitorWaitRequests()
```

Return an unmodifiable list of the enabled and disabled monitor wait requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the list of all

MonitorWaitRequest

objects.
**Since:** 1.6

---

#### monitorWaitRequests

List

<

MonitorWaitRequest

> monitorWaitRequests()

Return an unmodifiable list of the enabled and disabled monitor wait requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

monitorWaitedRequests

```java
List
<
MonitorWaitedRequest
> monitorWaitedRequests()
```

Return an unmodifiable list of the enabled and disabled monitor waited requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

**Returns:** the list of all

MonitorWaitedRequest

objects.
**Since:** 1.6

---

#### monitorWaitedRequests

List

<

MonitorWaitedRequest

> monitorWaitedRequests()

Return an unmodifiable list of the enabled and disabled monitor waited requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.

vmDeathRequests

```java
List
<
VMDeathRequest
> vmDeathRequests()
```

Return an unmodifiable list of the enabled and disabled VM death requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.
Note: the unsolicited VMDeathEvent does not have a
corresponding request.

**Returns:** the list of all

VMDeathRequest

objects.
**Since:** 1.4

---

#### vmDeathRequests

List

<

VMDeathRequest

> vmDeathRequests()

Return an unmodifiable list of the enabled and disabled VM death requests.
This list is a live view of these requests and thus changes as requests
are added and deleted.
Note: the unsolicited VMDeathEvent does not have a
corresponding request.

---

