# Interface EventSet

**Source:** `jdk.jdi\com\sun\jdi\event\EventSet.html`

### Class Description

```java
public interface
EventSet

extends
Mirror
,
Set
<
Event
>
```

Several

Event

objects may be created at a given time by
the target

VirtualMachine

. For example, there may be
more than one

BreakpointRequest

for a given

Location

or you might single step to the same location as a
BreakpointRequest. These

Event

objects are delivered
together as an EventSet. For uniformity, an EventSet is always used
to deliver

Event

objects. EventSets are delivered by
the

EventQueue

.
EventSets are unmodifiable.

Associated with the issuance of an event set, suspensions may
have occurred in the target VM. These suspensions correspond
with the

suspend policy

.
To assure matching resumes occur, it is recommended,
where possible,
to complete the processing of an event set with

EventSet.resume()

.

The events that are grouped in an EventSet are restricted in the
following ways:

- Always singleton sets:

- VMStartEvent

VMDisconnectEvent

Only with other VMDeathEvents:

- VMDeathEvent

Only with other ThreadStartEvents for the same thread:

- ThreadStartEvent

Only with other ThreadDeathEvents for the same thread:

- ThreadDeathEvent

Only with other ClassPrepareEvents for the same class:

- ClassPrepareEvent

Only with other ClassUnloadEvents for the same class:

- ClassUnloadEvent

Only with other AccessWatchpointEvents for the same field access:

- AccessWatchpointEvent

Only with other ModificationWatchpointEvents for the same field
modification:

- ModificationWatchpointEvent

Only with other ExceptionEvents for the same exception occurrance:

- ExceptionEvent

Only with other MethodExitEvents for the same method exit:

- MethodExitEvent

Only with other Monitor contended enter events for the same monitor object:

- Monitor Contended Enter Event

Only with other Monitor contended entered events for the same monitor object:

- Monitor Contended Entered Event

Only with other Monitor wait events for the same monitor object:

- Monitor Wait Event

Only with other Monitor waited events for the same monitor object:

- Monitor Waited Event

Only with other members of this group, at the same location
and in the same thread:

- BreakpointEvent

StepEvent

MethodEntryEvent

**All Superinterfaces:** Collection

<

Event

>

,

Iterable

<

Event

>

,

Mirror

,

Set

<

Event

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int suspendPolicy()

Returns the policy used to suspend threads in the target VM
for this event set. This policy is selected from the suspend
policies for each event's request; the target VM chooses the
policy which suspends the most threads. The target VM suspends
threads according to that policy and that policy is returned here.
See

EventRequest

for the possible policy values.

In rare cases, the suspend policy may differ from the requested
value if a

ClassPrepareEvent

has occurred in a
debugger system thread. See

ClassPrepareEvent.thread()

for details.

**Returns:**
- the suspendPolicy which is either

SUSPEND_ALL

,

SUSPEND_EVENT_THREAD

or

SUSPEND_NONE

.

---

#### EventIterator
eventIterator()

Return an iterator specific to

Event

objects.

---

#### void resume()

Resumes threads suspended by this event set. If the

suspendPolicy()

is

EventRequest.SUSPEND_ALL

, a call to this method is equivalent to

VirtualMachine.resume()

. If the suspend policy is

EventRequest.SUSPEND_EVENT_THREAD

,
a call to this method is equivalent to

ThreadReference.resume()

for the event thread.
Otherwise, a call to this method is a no-op.

---

### Additional Sections

#### Interface EventSet

**All Superinterfaces:** Collection

<

Event

>

,

Iterable

<

Event

>

,

Mirror

,

Set

<

Event

>

```java
public interface
EventSet

extends
Mirror
,
Set
<
Event
>
```

Several

Event

objects may be created at a given time by
the target

VirtualMachine

. For example, there may be
more than one

BreakpointRequest

for a given

Location

or you might single step to the same location as a
BreakpointRequest. These

Event

objects are delivered
together as an EventSet. For uniformity, an EventSet is always used
to deliver

Event

objects. EventSets are delivered by
the

EventQueue

.
EventSets are unmodifiable.

Associated with the issuance of an event set, suspensions may
have occurred in the target VM. These suspensions correspond
with the

suspend policy

.
To assure matching resumes occur, it is recommended,
where possible,
to complete the processing of an event set with

EventSet.resume()

.

The events that are grouped in an EventSet are restricted in the
following ways:

- Always singleton sets:

- VMStartEvent

VMDisconnectEvent

Only with other VMDeathEvents:

- VMDeathEvent

Only with other ThreadStartEvents for the same thread:

- ThreadStartEvent

Only with other ThreadDeathEvents for the same thread:

- ThreadDeathEvent

Only with other ClassPrepareEvents for the same class:

- ClassPrepareEvent

Only with other ClassUnloadEvents for the same class:

- ClassUnloadEvent

Only with other AccessWatchpointEvents for the same field access:

- AccessWatchpointEvent

Only with other ModificationWatchpointEvents for the same field
modification:

- ModificationWatchpointEvent

Only with other ExceptionEvents for the same exception occurrance:

- ExceptionEvent

Only with other MethodExitEvents for the same method exit:

- MethodExitEvent

Only with other Monitor contended enter events for the same monitor object:

- Monitor Contended Enter Event

Only with other Monitor contended entered events for the same monitor object:

- Monitor Contended Entered Event

Only with other Monitor wait events for the same monitor object:

- Monitor Wait Event

Only with other Monitor waited events for the same monitor object:

- Monitor Waited Event

Only with other members of this group, at the same location
and in the same thread:

- BreakpointEvent

StepEvent

MethodEntryEvent

**Since:** 1.3
**See Also:** Event

,

EventQueue

public interface

EventSet

extends

Mirror

,

Set

<

Event

>

Several

Event

objects may be created at a given time by
the target

VirtualMachine

. For example, there may be
more than one

BreakpointRequest

for a given

Location

or you might single step to the same location as a
BreakpointRequest. These

Event

objects are delivered
together as an EventSet. For uniformity, an EventSet is always used
to deliver

Event

objects. EventSets are delivered by
the

EventQueue

.
EventSets are unmodifiable.

Associated with the issuance of an event set, suspensions may
have occurred in the target VM. These suspensions correspond
with the

suspend policy

.
To assure matching resumes occur, it is recommended,
where possible,
to complete the processing of an event set with

EventSet.resume()

.

The events that are grouped in an EventSet are restricted in the
following ways:

- Always singleton sets:

- VMStartEvent

VMDisconnectEvent

Only with other VMDeathEvents:

- VMDeathEvent

Only with other ThreadStartEvents for the same thread:

- ThreadStartEvent

Only with other ThreadDeathEvents for the same thread:

- ThreadDeathEvent

Only with other ClassPrepareEvents for the same class:

- ClassPrepareEvent

Only with other ClassUnloadEvents for the same class:

- ClassUnloadEvent

Only with other AccessWatchpointEvents for the same field access:

- AccessWatchpointEvent

Only with other ModificationWatchpointEvents for the same field
modification:

- ModificationWatchpointEvent

Only with other ExceptionEvents for the same exception occurrance:

- ExceptionEvent

Only with other MethodExitEvents for the same method exit:

- MethodExitEvent

Only with other Monitor contended enter events for the same monitor object:

- Monitor Contended Enter Event

Only with other Monitor contended entered events for the same monitor object:

- Monitor Contended Entered Event

Only with other Monitor wait events for the same monitor object:

- Monitor Wait Event

Only with other Monitor waited events for the same monitor object:

- Monitor Waited Event

Only with other members of this group, at the same location
and in the same thread:

- BreakpointEvent

StepEvent

MethodEntryEvent

Associated with the issuance of an event set, suspensions may
have occurred in the target VM. These suspensions correspond
with the

suspend policy

.
To assure matching resumes occur, it is recommended,
where possible,
to complete the processing of an event set with

EventSet.resume()

.

The events that are grouped in an EventSet are restricted in the
following ways:

- Always singleton sets:

- VMStartEvent

VMDisconnectEvent

Only with other VMDeathEvents:

- VMDeathEvent

Only with other ThreadStartEvents for the same thread:

- ThreadStartEvent

Only with other ThreadDeathEvents for the same thread:

- ThreadDeathEvent

Only with other ClassPrepareEvents for the same class:

- ClassPrepareEvent

Only with other ClassUnloadEvents for the same class:

- ClassUnloadEvent

Only with other AccessWatchpointEvents for the same field access:

- AccessWatchpointEvent

Only with other ModificationWatchpointEvents for the same field
modification:

- ModificationWatchpointEvent

Only with other ExceptionEvents for the same exception occurrance:

- ExceptionEvent

Only with other MethodExitEvents for the same method exit:

- MethodExitEvent

Only with other Monitor contended enter events for the same monitor object:

- Monitor Contended Enter Event

Only with other Monitor contended entered events for the same monitor object:

- Monitor Contended Entered Event

Only with other Monitor wait events for the same monitor object:

- Monitor Wait Event

Only with other Monitor waited events for the same monitor object:

- Monitor Waited Event

Only with other members of this group, at the same location
and in the same thread:

- BreakpointEvent

StepEvent

MethodEntryEvent

The events that are grouped in an EventSet are restricted in the
following ways:

- Always singleton sets:

- VMStartEvent

VMDisconnectEvent

Only with other VMDeathEvents:

- VMDeathEvent

Only with other ThreadStartEvents for the same thread:

- ThreadStartEvent

Only with other ThreadDeathEvents for the same thread:

- ThreadDeathEvent

Only with other ClassPrepareEvents for the same class:

- ClassPrepareEvent

Only with other ClassUnloadEvents for the same class:

- ClassUnloadEvent

Only with other AccessWatchpointEvents for the same field access:

- AccessWatchpointEvent

Only with other ModificationWatchpointEvents for the same field
modification:

- ModificationWatchpointEvent

Only with other ExceptionEvents for the same exception occurrance:

- ExceptionEvent

Only with other MethodExitEvents for the same method exit:

- MethodExitEvent

Only with other Monitor contended enter events for the same monitor object:

- Monitor Contended Enter Event

Only with other Monitor contended entered events for the same monitor object:

- Monitor Contended Entered Event

Only with other Monitor wait events for the same monitor object:

- Monitor Wait Event

Only with other Monitor waited events for the same monitor object:

- Monitor Waited Event

Only with other members of this group, at the same location
and in the same thread:

- BreakpointEvent

StepEvent

MethodEntryEvent

Always singleton sets:

- VMStartEvent

VMDisconnectEvent

Only with other VMDeathEvents:

- VMDeathEvent

Only with other ThreadStartEvents for the same thread:

- ThreadStartEvent

Only with other ThreadDeathEvents for the same thread:

- ThreadDeathEvent

Only with other ClassPrepareEvents for the same class:

- ClassPrepareEvent

Only with other ClassUnloadEvents for the same class:

- ClassUnloadEvent

Only with other AccessWatchpointEvents for the same field access:

- AccessWatchpointEvent

Only with other ModificationWatchpointEvents for the same field
modification:

- ModificationWatchpointEvent

Only with other ExceptionEvents for the same exception occurrance:

- ExceptionEvent

Only with other MethodExitEvents for the same method exit:

- MethodExitEvent

Only with other Monitor contended enter events for the same monitor object:

- Monitor Contended Enter Event

Only with other Monitor contended entered events for the same monitor object:

- Monitor Contended Entered Event

Only with other Monitor wait events for the same monitor object:

- Monitor Wait Event

Only with other Monitor waited events for the same monitor object:

- Monitor Waited Event

Only with other members of this group, at the same location
and in the same thread:

- BreakpointEvent

StepEvent

MethodEntryEvent

VMStartEvent

VMDisconnectEvent

VMDeathEvent

ThreadStartEvent

ThreadDeathEvent

ClassPrepareEvent

ClassUnloadEvent

AccessWatchpointEvent

ModificationWatchpointEvent

ExceptionEvent

MethodExitEvent

Monitor Contended Enter Event

Monitor Contended Entered Event

Monitor Wait Event

Monitor Waited Event

BreakpointEvent

StepEvent

MethodEntryEvent

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

EventIterator

eventIterator

()

Return an iterator specific to

Event

objects.

void

resume

()

Resumes threads suspended by this event set.

int

suspendPolicy

()

Returns the policy used to suspend threads in the target VM
for this event set.

- Methods declared in interface java.util.

Collection

parallelStream

,

removeIf

,

stream

,

toArray

- Methods declared in interface java.lang.

Iterable

forEach

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

- Methods declared in interface java.util.

Set

add

,

addAll

,

clear

,

contains

,

containsAll

,

equals

,

hashCode

,

isEmpty

,

iterator

,

remove

,

removeAll

,

retainAll

,

size

,

spliterator

,

toArray

,

toArray

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

EventIterator

eventIterator

()

Return an iterator specific to

Event

objects.

void

resume

()

Resumes threads suspended by this event set.

int

suspendPolicy

()

Returns the policy used to suspend threads in the target VM
for this event set.

- Methods declared in interface java.util.

Collection

parallelStream

,

removeIf

,

stream

,

toArray

- Methods declared in interface java.lang.

Iterable

forEach

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

- Methods declared in interface java.util.

Set

add

,

addAll

,

clear

,

contains

,

containsAll

,

equals

,

hashCode

,

isEmpty

,

iterator

,

remove

,

removeAll

,

retainAll

,

size

,

spliterator

,

toArray

,

toArray

---

#### Method Summary

Return an iterator specific to

Event

objects.

Resumes threads suspended by this event set.

Returns the policy used to suspend threads in the target VM
for this event set.

Methods declared in interface java.util.

Collection

parallelStream

,

removeIf

,

stream

,

toArray

---

#### Methods declared in interface java.util. Collection

Methods declared in interface java.lang.

Iterable

forEach

---

#### Methods declared in interface java.lang. Iterable

Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Methods declared in interface com.sun.jdi. Mirror

Methods declared in interface java.util.

Set

add

,

addAll

,

clear

,

contains

,

containsAll

,

equals

,

hashCode

,

isEmpty

,

iterator

,

remove

,

removeAll

,

retainAll

,

size

,

spliterator

,

toArray

,

toArray

---

#### Methods declared in interface java.util. Set

============ METHOD DETAIL ==========

- Method Detail

- suspendPolicy

```java
int suspendPolicy()
```

Returns the policy used to suspend threads in the target VM
for this event set. This policy is selected from the suspend
policies for each event's request; the target VM chooses the
policy which suspends the most threads. The target VM suspends
threads according to that policy and that policy is returned here.
See

EventRequest

for the possible policy values.

In rare cases, the suspend policy may differ from the requested
value if a

ClassPrepareEvent

has occurred in a
debugger system thread. See

ClassPrepareEvent.thread()

for details.

**Returns:** the suspendPolicy which is either

SUSPEND_ALL

,

SUSPEND_EVENT_THREAD

or

SUSPEND_NONE

.

- eventIterator

```java
EventIterator
eventIterator()
```

Return an iterator specific to

Event

objects.

- resume

```java
void resume()
```

Resumes threads suspended by this event set. If the

suspendPolicy()

is

EventRequest.SUSPEND_ALL

, a call to this method is equivalent to

VirtualMachine.resume()

. If the suspend policy is

EventRequest.SUSPEND_EVENT_THREAD

,
a call to this method is equivalent to

ThreadReference.resume()

for the event thread.
Otherwise, a call to this method is a no-op.

Method Detail

- suspendPolicy

```java
int suspendPolicy()
```

Returns the policy used to suspend threads in the target VM
for this event set. This policy is selected from the suspend
policies for each event's request; the target VM chooses the
policy which suspends the most threads. The target VM suspends
threads according to that policy and that policy is returned here.
See

EventRequest

for the possible policy values.

In rare cases, the suspend policy may differ from the requested
value if a

ClassPrepareEvent

has occurred in a
debugger system thread. See

ClassPrepareEvent.thread()

for details.

**Returns:** the suspendPolicy which is either

SUSPEND_ALL

,

SUSPEND_EVENT_THREAD

or

SUSPEND_NONE

.

- eventIterator

```java
EventIterator
eventIterator()
```

Return an iterator specific to

Event

objects.

- resume

```java
void resume()
```

Resumes threads suspended by this event set. If the

suspendPolicy()

is

EventRequest.SUSPEND_ALL

, a call to this method is equivalent to

VirtualMachine.resume()

. If the suspend policy is

EventRequest.SUSPEND_EVENT_THREAD

,
a call to this method is equivalent to

ThreadReference.resume()

for the event thread.
Otherwise, a call to this method is a no-op.

---

#### Method Detail

suspendPolicy

```java
int suspendPolicy()
```

Returns the policy used to suspend threads in the target VM
for this event set. This policy is selected from the suspend
policies for each event's request; the target VM chooses the
policy which suspends the most threads. The target VM suspends
threads according to that policy and that policy is returned here.
See

EventRequest

for the possible policy values.

In rare cases, the suspend policy may differ from the requested
value if a

ClassPrepareEvent

has occurred in a
debugger system thread. See

ClassPrepareEvent.thread()

for details.

**Returns:** the suspendPolicy which is either

SUSPEND_ALL

,

SUSPEND_EVENT_THREAD

or

SUSPEND_NONE

.

---

#### suspendPolicy

int suspendPolicy()

Returns the policy used to suspend threads in the target VM
for this event set. This policy is selected from the suspend
policies for each event's request; the target VM chooses the
policy which suspends the most threads. The target VM suspends
threads according to that policy and that policy is returned here.
See

EventRequest

for the possible policy values.

In rare cases, the suspend policy may differ from the requested
value if a

ClassPrepareEvent

has occurred in a
debugger system thread. See

ClassPrepareEvent.thread()

for details.

In rare cases, the suspend policy may differ from the requested
value if a

ClassPrepareEvent

has occurred in a
debugger system thread. See

ClassPrepareEvent.thread()

for details.

eventIterator

```java
EventIterator
eventIterator()
```

Return an iterator specific to

Event

objects.

---

#### eventIterator

EventIterator

eventIterator()

Return an iterator specific to

Event

objects.

resume

```java
void resume()
```

Resumes threads suspended by this event set. If the

suspendPolicy()

is

EventRequest.SUSPEND_ALL

, a call to this method is equivalent to

VirtualMachine.resume()

. If the suspend policy is

EventRequest.SUSPEND_EVENT_THREAD

,
a call to this method is equivalent to

ThreadReference.resume()

for the event thread.
Otherwise, a call to this method is a no-op.

---

#### resume

void resume()

Resumes threads suspended by this event set. If the

suspendPolicy()

is

EventRequest.SUSPEND_ALL

, a call to this method is equivalent to

VirtualMachine.resume()

. If the suspend policy is

EventRequest.SUSPEND_EVENT_THREAD

,
a call to this method is equivalent to

ThreadReference.resume()

for the event thread.
Otherwise, a call to this method is a no-op.

---

