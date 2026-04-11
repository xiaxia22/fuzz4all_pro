# Interface ThreadMXBean

**Source:** `java.management\java\lang\management\ThreadMXBean.html`

### Class Description

```java
public interface
ThreadMXBean

extends
PlatformManagedObject
```

The management interface for the thread system of
the Java virtual machine.

A Java virtual machine has a single instance of the implementation
class of this interface. This instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getThreadMXBean()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
the thread system within an MBeanServer is:

java.lang:type=Threading

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

Thread ID

Thread ID is a positive long value returned by calling the

Thread.getId()

method for a thread.
The thread ID is unique during its lifetime. When a thread
is terminated, this thread ID may be reused.

Some methods in this interface take a thread ID or an array
of thread IDs as the input parameter and return per-thread information.

Thread CPU time

A Java virtual machine implementation may support measuring
the CPU time for the current thread, for any thread, or for no threads.

The

isThreadCpuTimeSupported()

method can be used to determine
if a Java virtual machine supports measuring of the CPU time for any
thread. The

isCurrentThreadCpuTimeSupported()

method can
be used to determine if a Java virtual machine supports measuring of
the CPU time for the current thread.
A Java virtual machine implementation that supports CPU time measurement
for any thread will also support that for the current thread.

The CPU time provided by this interface has nanosecond precision
but not necessarily nanosecond accuracy.

A Java virtual machine may disable CPU time measurement
by default.
The

isThreadCpuTimeEnabled()

and

setThreadCpuTimeEnabled(boolean)

methods can be used to test if CPU time measurement is enabled
and to enable/disable this support respectively.
Enabling thread CPU measurement could be expensive in some
Java virtual machine implementations.

Thread Contention Monitoring

Some Java virtual machines may support thread contention monitoring.
When thread contention monitoring is enabled, the accumulated elapsed
time that the thread has blocked for synchronization or waited for
notification will be collected and returned in the

ThreadInfo

object.

The

isThreadContentionMonitoringSupported()

method can be used to
determine if a Java virtual machine supports thread contention monitoring.
The thread contention monitoring is disabled by default. The

setThreadContentionMonitoringEnabled(boolean)

method can be used to enable
thread contention monitoring.

Synchronization Information and Deadlock Detection

Some Java virtual machines may support monitoring of

object monitor usage

and

ownable synchronizer usage

.
The

getThreadInfo(long[], boolean, boolean)

and

dumpAllThreads(boolean, boolean)

methods can be used to obtain the thread stack trace
and synchronization information including which

lock

a thread is blocked to
acquire or waiting on and which locks the thread currently owns.

The

ThreadMXBean

interface provides the

findMonitorDeadlockedThreads()

and

findDeadlockedThreads()

methods to find deadlocks in
the running application.

**All Superinterfaces:** PlatformManagedObject

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int getThreadCount()

Returns the current number of live threads including both
daemon and non-daemon threads.

**Returns:**
- the current number of live threads.

---

#### int getPeakThreadCount()

Returns the peak live thread count since the Java virtual machine
started or peak was reset.

**Returns:**
- the peak live thread count.

---

#### long getTotalStartedThreadCount()

Returns the total number of threads created and also started
since the Java virtual machine started.

**Returns:**
- the total number of threads started.

---

#### int getDaemonThreadCount()

Returns the current number of live daemon threads.

**Returns:**
- the current number of live daemon threads.

---

#### long[] getAllThreadIds()

Returns all live thread IDs.
Some threads included in the returned array
may have been terminated when this method returns.

**Returns:**
- an array of

long

, each is a thread ID.

**Throws:**
- SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").

---

#### ThreadInfo
getThreadInfo​(long id)

Returns the thread info for a thread of the specified

id

with no stack trace.
This method is equivalent to calling:

getThreadInfo(id, 0);

This method returns a

ThreadInfo

object representing
the thread information for the thread of the specified ID.
The stack trace, locked monitors, and locked synchronizers
in the returned

ThreadInfo

object will
be empty.

If a thread of the given ID is not alive or does not exist,
this method will return

null

. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

**Parameters:**
- id

- the thread ID of the thread. Must be positive.

**Returns:**
- a

ThreadInfo

object for the thread of the given ID
with no stack trace, no locked monitor and no synchronizer info;

null

if the thread of the given ID is not alive or
it does not exist.

**Throws:**
- IllegalArgumentException

- if

id <= 0

.
- SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").

---

#### ThreadInfo
[] getThreadInfo​(long[] ids)

Returns the thread info for each thread
whose ID is in the input array

ids

with no stack trace.
This method is equivalent to calling:

```java
getThreadInfo
(ids, 0);
```

This method returns an array of the

ThreadInfo

objects.
The stack trace, locked monitors, and locked synchronizers
in each

ThreadInfo

object will be empty.

If a thread of a given ID is not alive or does not exist,
the corresponding element in the returned array will
contain

null

. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

**Parameters:**
- ids

- an array of thread IDs.

**Returns:**
- an array of the

ThreadInfo

objects, each containing
information about a thread whose ID is in the corresponding
element of the input array of IDs
with no stack trace, no locked monitor and no synchronizer info.

**Throws:**
- IllegalArgumentException

- if any element in the input array

ids

is

<= 0

.
- SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").

---

#### ThreadInfo
getThreadInfo​(long id,
int maxDepth)

Returns a thread info for a thread of the specified

id

,
with stack trace of a specified number of stack trace elements.
The

maxDepth

parameter indicates the maximum number of

StackTraceElement

to be retrieved from the stack trace.
If

maxDepth == Integer.MAX_VALUE

, the entire stack trace of
the thread will be dumped.
If

maxDepth == 0

, no stack trace of the thread
will be dumped.
This method does not obtain the locked monitors and locked
synchronizers of the thread.

When the Java virtual machine has no stack trace information
about a thread or

maxDepth == 0

,
the stack trace in the

ThreadInfo

object will be an empty array of

StackTraceElement

.

If a thread of the given ID is not alive or does not exist,
this method will return

null

. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

**Parameters:**
- id

- the thread ID of the thread. Must be positive.
- maxDepth

- the maximum number of entries in the stack trace
to be dumped.

Integer.MAX_VALUE

could be used to request
the entire stack to be dumped.

**Returns:**
- a

ThreadInfo

of the thread of the given ID
with no locked monitor and synchronizer info.

null

if the thread of the given ID is not alive or
it does not exist.

**Throws:**
- IllegalArgumentException

- if

id <= 0

.
- IllegalArgumentException

- if

maxDepth is negative

.
- SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").

---

#### ThreadInfo
[] getThreadInfo​(long[] ids,
int maxDepth)

Returns the thread info for each thread
whose ID is in the input array

ids

,
with stack trace of a specified number of stack trace elements.
The

maxDepth

parameter indicates the maximum number of

StackTraceElement

to be retrieved from the stack trace.
If

maxDepth == Integer.MAX_VALUE

, the entire stack trace of
the thread will be dumped.
If

maxDepth == 0

, no stack trace of the thread
will be dumped.
This method does not obtain the locked monitors and locked
synchronizers of the threads.

When the Java virtual machine has no stack trace information
about a thread or

maxDepth == 0

,
the stack trace in the

ThreadInfo

object will be an empty array of

StackTraceElement

.

This method returns an array of the

ThreadInfo

objects,
each is the thread information about the thread with the same index
as in the

ids

array.
If a thread of the given ID is not alive or does not exist,

null

will be set in the corresponding element
in the returned array. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

**Parameters:**
- ids

- an array of thread IDs
- maxDepth

- the maximum number of entries in the stack trace
to be dumped.

Integer.MAX_VALUE

could be used to request
the entire stack to be dumped.

**Returns:**
- an array of the

ThreadInfo

objects, each containing
information about a thread whose ID is in the corresponding
element of the input array of IDs with no locked monitor and
synchronizer info.

**Throws:**
- IllegalArgumentException

- if

maxDepth is negative

.
- IllegalArgumentException

- if any element in the input array

ids

is

<= 0

.
- SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").

---

#### boolean isThreadContentionMonitoringSupported()

Tests if the Java virtual machine supports thread contention monitoring.

**Returns:**
- true

if the Java virtual machine supports thread contention monitoring;

false

otherwise.

---

#### boolean isThreadContentionMonitoringEnabled()

Tests if thread contention monitoring is enabled.

**Returns:**
- true

if thread contention monitoring is enabled;

false

otherwise.

**Throws:**
- UnsupportedOperationException

- if the Java virtual
machine does not support thread contention monitoring.

**See Also:**
- isThreadContentionMonitoringSupported()

---

#### void setThreadContentionMonitoringEnabled​(boolean enable)

Enables or disables thread contention monitoring.
Thread contention monitoring is disabled by default.

**Parameters:**
- enable

-

true

to enable;

false

to disable.

**Throws:**
- UnsupportedOperationException

- if the Java
virtual machine does not support thread contention monitoring.
- SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("control").

**See Also:**
- isThreadContentionMonitoringSupported()

---

#### long getCurrentThreadCpuTime()

Returns the total CPU time for the current thread in nanoseconds.
The returned value is of nanoseconds precision but
not necessarily nanoseconds accuracy.
If the implementation distinguishes between user mode time and system
mode time, the returned CPU time is the amount of time that
the current thread has executed in user mode or system mode.

This is a convenience method for local management use and is
equivalent to calling:

```java
getThreadCpuTime
(Thread.currentThread().getId());
```

**Returns:**
- the total CPU time for the current thread if CPU time
measurement is enabled;

-1

otherwise.

**Throws:**
- UnsupportedOperationException

- if the Java
virtual machine does not support CPU time measurement for
the current thread.

**See Also:**
- getCurrentThreadUserTime()

,

isCurrentThreadCpuTimeSupported()

,

isThreadCpuTimeEnabled()

,

setThreadCpuTimeEnabled(boolean)

---

#### long getCurrentThreadUserTime()

Returns the CPU time that the current thread has executed
in user mode in nanoseconds.
The returned value is of nanoseconds precision but
not necessarily nanoseconds accuracy.

This is a convenience method for local management use and is
equivalent to calling:

```java
getThreadUserTime
(Thread.currentThread().getId());
```

**Returns:**
- the user-level CPU time for the current thread if CPU time
measurement is enabled;

-1

otherwise.

**Throws:**
- UnsupportedOperationException

- if the Java
virtual machine does not support CPU time measurement for
the current thread.

**See Also:**
- getCurrentThreadCpuTime()

,

isCurrentThreadCpuTimeSupported()

,

isThreadCpuTimeEnabled()

,

setThreadCpuTimeEnabled(boolean)

---

#### long getThreadCpuTime​(long id)

Returns the total CPU time for a thread of the specified ID in nanoseconds.
The returned value is of nanoseconds precision but
not necessarily nanoseconds accuracy.
If the implementation distinguishes between user mode time and system
mode time, the returned CPU time is the amount of time that
the thread has executed in user mode or system mode.

If the thread of the specified ID is not alive or does not exist,
this method returns

-1

. If CPU time measurement
is disabled, this method returns

-1

.
A thread is alive if it has been started and has not yet died.

If CPU time measurement is enabled after the thread has started,
the Java virtual machine implementation may choose any time up to
and including the time that the capability is enabled as the point
where CPU time measurement starts.

**Parameters:**
- id

- the thread ID of a thread

**Returns:**
- the total CPU time for a thread of the specified ID
if the thread of the specified ID exists, the thread is alive,
and CPU time measurement is enabled;

-1

otherwise.

**Throws:**
- IllegalArgumentException

- if

id <= 0

.
- UnsupportedOperationException

- if the Java
virtual machine does not support CPU time measurement for
other threads.

**See Also:**
- getThreadUserTime(long)

,

isThreadCpuTimeSupported()

,

isThreadCpuTimeEnabled()

,

setThreadCpuTimeEnabled(boolean)

---

#### long getThreadUserTime​(long id)

Returns the CPU time that a thread of the specified ID
has executed in user mode in nanoseconds.
The returned value is of nanoseconds precision but
not necessarily nanoseconds accuracy.

If the thread of the specified ID is not alive or does not exist,
this method returns

-1

. If CPU time measurement
is disabled, this method returns

-1

.
A thread is alive if it has been started and has not yet died.

If CPU time measurement is enabled after the thread has started,
the Java virtual machine implementation may choose any time up to
and including the time that the capability is enabled as the point
where CPU time measurement starts.

**Parameters:**
- id

- the thread ID of a thread

**Returns:**
- the user-level CPU time for a thread of the specified ID
if the thread of the specified ID exists, the thread is alive,
and CPU time measurement is enabled;

-1

otherwise.

**Throws:**
- IllegalArgumentException

- if

id <= 0

.
- UnsupportedOperationException

- if the Java
virtual machine does not support CPU time measurement for
other threads.

**See Also:**
- getThreadCpuTime(long)

,

isThreadCpuTimeSupported()

,

isThreadCpuTimeEnabled()

,

setThreadCpuTimeEnabled(boolean)

---

#### boolean isThreadCpuTimeSupported()

Tests if the Java virtual machine implementation supports CPU time
measurement for any thread.
A Java virtual machine implementation that supports CPU time
measurement for any thread will also support CPU time
measurement for the current thread.

**Returns:**
- true

if the Java virtual machine supports CPU time
measurement for any thread;

false

otherwise.

---

#### boolean isCurrentThreadCpuTimeSupported()

Tests if the Java virtual machine supports CPU time
measurement for the current thread.
This method returns

true

if

isThreadCpuTimeSupported()

returns

true

.

**Returns:**
- true

if the Java virtual machine supports CPU time
measurement for current thread;

false

otherwise.

---

#### boolean isThreadCpuTimeEnabled()

Tests if thread CPU time measurement is enabled.

**Returns:**
- true

if thread CPU time measurement is enabled;

false

otherwise.

**Throws:**
- UnsupportedOperationException

- if the Java virtual
machine does not support CPU time measurement for other threads
nor for the current thread.

**See Also:**
- isThreadCpuTimeSupported()

,

isCurrentThreadCpuTimeSupported()

---

#### void setThreadCpuTimeEnabled​(boolean enable)

Enables or disables thread CPU time measurement. The default
is platform dependent.

**Parameters:**
- enable

-

true

to enable;

false

to disable.

**Throws:**
- UnsupportedOperationException

- if the Java
virtual machine does not support CPU time measurement for
any threads nor for the current thread.
- SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("control").

**See Also:**
- isThreadCpuTimeSupported()

,

isCurrentThreadCpuTimeSupported()

---

#### long[] findMonitorDeadlockedThreads()

Finds cycles of threads that are in deadlock waiting to acquire
object monitors. That is, threads that are blocked waiting to enter a
synchronization block or waiting to reenter a synchronization block
after an

Object.wait

call,
where each thread owns one monitor while
trying to obtain another monitor already held by another thread
in a cycle.

More formally, a thread is

monitor deadlocked

if it is
part of a cycle in the relation "is waiting for an object monitor
owned by". In the simplest case, thread A is blocked waiting
for a monitor owned by thread B, and thread B is blocked waiting
for a monitor owned by thread A.

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

This method finds deadlocks involving only object monitors.
To find deadlocks involving both object monitors and

ownable synchronizers

,
the

findDeadlockedThreads

method
should be used.

**Returns:**
- an array of IDs of the threads that are monitor
deadlocked, if any;

null

otherwise.

**Throws:**
- SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").

**See Also:**
- findDeadlockedThreads()

---

#### void resetPeakThreadCount()

Resets the peak thread count to the current number of
live threads.

**Throws:**
- SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("control").

**See Also:**
- getPeakThreadCount()

,

getThreadCount()

---

#### long[] findDeadlockedThreads()

Finds cycles of threads that are in deadlock waiting to acquire
object monitors or

ownable synchronizers

.

Threads are

deadlocked

in a cycle waiting for a lock of
these two types if each thread owns one lock while
trying to acquire another lock already held
by another thread in the cycle.

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

**Returns:**
- an array of IDs of the threads that are
deadlocked waiting for object monitors or ownable synchronizers, if any;

null

otherwise.

**Throws:**
- SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
- UnsupportedOperationException

- if the Java virtual
machine does not support monitoring of ownable synchronizer usage.

**See Also:**
- isSynchronizerUsageSupported()

,

findMonitorDeadlockedThreads()

**Since:**
- 1.6

---

#### boolean isObjectMonitorUsageSupported()

Tests if the Java virtual machine supports monitoring of
object monitor usage.

**Returns:**
- true

if the Java virtual machine supports monitoring of
object monitor usage;

false

otherwise.

**See Also:**
- dumpAllThreads(boolean, boolean)

**Since:**
- 1.6

---

#### boolean isSynchronizerUsageSupported()

Tests if the Java virtual machine supports monitoring of

ownable synchronizer

usage.

**Returns:**
- true

if the Java virtual machine supports monitoring of ownable
synchronizer usage;

false

otherwise.

**See Also:**
- dumpAllThreads(boolean, boolean)

**Since:**
- 1.6

---

#### ThreadInfo
[] getThreadInfo​(long[] ids,
boolean lockedMonitors,
boolean lockedSynchronizers)

Returns the thread info for each thread
whose ID is in the input array

ids

,
with stack trace and synchronization information.
This is equivalent to calling:

getThreadInfo(ids, lockedMonitors, lockedSynchronizers, Integer.MAX_VALUE)

**Parameters:**
- ids

- an array of thread IDs.
- lockedMonitors

- if

true

, retrieves all locked monitors.
- lockedSynchronizers

- if

true

, retrieves all locked
ownable synchronizers.

**Returns:**
- an array of the

ThreadInfo

objects, each containing
information about a thread whose ID is in the corresponding
element of the input array of IDs.

**Throws:**
- SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
- UnsupportedOperationException

-

- if

lockedMonitors

is

true

but
the Java virtual machine does not support monitoring
of

object monitor usage

; or
- if

lockedSynchronizers

is

true

but
the Java virtual machine does not support monitoring
of

ownable synchronizer usage

.

**See Also:**
- isObjectMonitorUsageSupported()

,

isSynchronizerUsageSupported()

**Since:**
- 1.6

---

#### default
ThreadInfo
[] getThreadInfo​(long[] ids,
boolean lockedMonitors,
boolean lockedSynchronizers,
int maxDepth)

Returns the thread info for each thread whose ID
is in the input array

ids

,
with stack trace of the specified maximum number of elements
and synchronization information.
If

maxDepth == 0

, no stack trace of the thread
will be dumped.

This method obtains a snapshot of the thread information
for each thread including:

- stack trace of the specified maximum number of elements,
- the object monitors currently locked by the thread
if

lockedMonitors

is

true

, and
- the

ownable synchronizers

currently locked by the thread
if

lockedSynchronizers

is

true

.

This method returns an array of the

ThreadInfo

objects,
each is the thread information about the thread with the same index
as in the

ids

array.
If a thread of the given ID is not alive or does not exist,

null

will be set in the corresponding element
in the returned array. A thread is alive if
it has been started and has not yet died.

If a thread does not lock any object monitor or

lockedMonitors

is

false

, the returned

ThreadInfo

object will have an
empty

MonitorInfo

array. Similarly, if a thread does not
lock any synchronizer or

lockedSynchronizers

is

false

,
the returned

ThreadInfo

object
will have an empty

LockInfo

array.

When both

lockedMonitors

and

lockedSynchronizers

parameters are

false

, it is equivalent to calling:

```java
getThreadInfo(ids, maxDepth)
```

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

**Parameters:**
- ids

- an array of thread IDs.
- lockedMonitors

- if

true

, retrieves all locked monitors.
- lockedSynchronizers

- if

true

, retrieves all locked
ownable synchronizers.
- maxDepth

- indicates the maximum number of

StackTraceElement

to be retrieved from the stack trace.

**Returns:**
- an array of the

ThreadInfo

objects, each containing
information about a thread whose ID is in the corresponding
element of the input array of IDs.

**Throws:**
- IllegalArgumentException

- if

maxDepth

is negative.
- SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
- UnsupportedOperationException

-

- if

lockedMonitors

is

true

but
the Java virtual machine does not support monitoring
of

object monitor usage

; or
- if

lockedSynchronizers

is

true

but
the Java virtual machine does not support monitoring
of

ownable synchronizer usage

.

**See Also:**
- isObjectMonitorUsageSupported()

,

isSynchronizerUsageSupported()

**Since:**
- 10

**Implementation Requirements:**
- The default implementation throws

UnsupportedOperationException

.

---

#### ThreadInfo
[] dumpAllThreads​(boolean lockedMonitors,
boolean lockedSynchronizers)

Returns the thread info for all live threads with stack trace
and synchronization information.
This is equivalent to calling:

dumpAllThreads(lockedMonitors, lockedSynchronizers, Integer.MAX_VALUE)

**Parameters:**
- lockedMonitors

- if

true

, dump all locked monitors.
- lockedSynchronizers

- if

true

, dump all locked
ownable synchronizers.

**Returns:**
- an array of

ThreadInfo

for all live threads.

**Throws:**
- SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
- UnsupportedOperationException

-

- if

lockedMonitors

is

true

but
the Java virtual machine does not support monitoring
of

object monitor usage

; or
- if

lockedSynchronizers

is

true

but
the Java virtual machine does not support monitoring
of

ownable synchronizer usage

.

**See Also:**
- isObjectMonitorUsageSupported()

,

isSynchronizerUsageSupported()

**Since:**
- 1.6

---

#### default
ThreadInfo
[] dumpAllThreads​(boolean lockedMonitors,
boolean lockedSynchronizers,
int maxDepth)

Returns the thread info for all live threads
with stack trace of the specified maximum number of elements
and synchronization information.
if

maxDepth == 0

, no stack trace of the thread
will be dumped.
Some threads included in the returned array
may have been terminated when this method returns.

This method returns an array of

ThreadInfo

objects
as specified in the

getThreadInfo(long[], boolean, boolean, int)

method.

**Parameters:**
- lockedMonitors

- if

true

, dump all locked monitors.
- lockedSynchronizers

- if

true

, dump all locked
ownable synchronizers.
- maxDepth

- indicates the maximum number of

StackTraceElement

to be retrieved from the stack trace.

**Returns:**
- an array of

ThreadInfo

for all live threads.

**Throws:**
- IllegalArgumentException

- if

maxDepth

is negative.
- SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
- UnsupportedOperationException

-

- if

lockedMonitors

is

true

but
the Java virtual machine does not support monitoring
of

object monitor usage

; or
- if

lockedSynchronizers

is

true

but
the Java virtual machine does not support monitoring
of

ownable synchronizer usage

.

**See Also:**
- isObjectMonitorUsageSupported()

,

isSynchronizerUsageSupported()

**Since:**
- 10

**Implementation Requirements:**
- The default implementation throws

UnsupportedOperationException

.

---

### Additional Sections

#### Interface ThreadMXBean

**All Superinterfaces:** PlatformManagedObject

**All Known Subinterfaces:** ThreadMXBean

```java
public interface
ThreadMXBean

extends
PlatformManagedObject
```

The management interface for the thread system of
the Java virtual machine.

A Java virtual machine has a single instance of the implementation
class of this interface. This instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getThreadMXBean()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
the thread system within an MBeanServer is:

java.lang:type=Threading

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

Thread ID

Thread ID is a positive long value returned by calling the

Thread.getId()

method for a thread.
The thread ID is unique during its lifetime. When a thread
is terminated, this thread ID may be reused.

Some methods in this interface take a thread ID or an array
of thread IDs as the input parameter and return per-thread information.

Thread CPU time

A Java virtual machine implementation may support measuring
the CPU time for the current thread, for any thread, or for no threads.

The

isThreadCpuTimeSupported()

method can be used to determine
if a Java virtual machine supports measuring of the CPU time for any
thread. The

isCurrentThreadCpuTimeSupported()

method can
be used to determine if a Java virtual machine supports measuring of
the CPU time for the current thread.
A Java virtual machine implementation that supports CPU time measurement
for any thread will also support that for the current thread.

The CPU time provided by this interface has nanosecond precision
but not necessarily nanosecond accuracy.

A Java virtual machine may disable CPU time measurement
by default.
The

isThreadCpuTimeEnabled()

and

setThreadCpuTimeEnabled(boolean)

methods can be used to test if CPU time measurement is enabled
and to enable/disable this support respectively.
Enabling thread CPU measurement could be expensive in some
Java virtual machine implementations.

Thread Contention Monitoring

Some Java virtual machines may support thread contention monitoring.
When thread contention monitoring is enabled, the accumulated elapsed
time that the thread has blocked for synchronization or waited for
notification will be collected and returned in the

ThreadInfo

object.

The

isThreadContentionMonitoringSupported()

method can be used to
determine if a Java virtual machine supports thread contention monitoring.
The thread contention monitoring is disabled by default. The

setThreadContentionMonitoringEnabled(boolean)

method can be used to enable
thread contention monitoring.

Synchronization Information and Deadlock Detection

Some Java virtual machines may support monitoring of

object monitor usage

and

ownable synchronizer usage

.
The

getThreadInfo(long[], boolean, boolean)

and

dumpAllThreads(boolean, boolean)

methods can be used to obtain the thread stack trace
and synchronization information including which

lock

a thread is blocked to
acquire or waiting on and which locks the thread currently owns.

The

ThreadMXBean

interface provides the

findMonitorDeadlockedThreads()

and

findDeadlockedThreads()

methods to find deadlocks in
the running application.

**Since:** 1.5
**See Also:** ManagementFactory.getPlatformMXBeans(Class)

,

JMX Specification.

,

Ways to Access MXBeans

public interface

ThreadMXBean

extends

PlatformManagedObject

The management interface for the thread system of
the Java virtual machine.

A Java virtual machine has a single instance of the implementation
class of this interface. This instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getThreadMXBean()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
the thread system within an MBeanServer is:

java.lang:type=Threading

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

Thread ID

Thread ID is a positive long value returned by calling the

Thread.getId()

method for a thread.
The thread ID is unique during its lifetime. When a thread
is terminated, this thread ID may be reused.

Some methods in this interface take a thread ID or an array
of thread IDs as the input parameter and return per-thread information.

Thread CPU time

A Java virtual machine implementation may support measuring
the CPU time for the current thread, for any thread, or for no threads.

The

isThreadCpuTimeSupported()

method can be used to determine
if a Java virtual machine supports measuring of the CPU time for any
thread. The

isCurrentThreadCpuTimeSupported()

method can
be used to determine if a Java virtual machine supports measuring of
the CPU time for the current thread.
A Java virtual machine implementation that supports CPU time measurement
for any thread will also support that for the current thread.

The CPU time provided by this interface has nanosecond precision
but not necessarily nanosecond accuracy.

A Java virtual machine may disable CPU time measurement
by default.
The

isThreadCpuTimeEnabled()

and

setThreadCpuTimeEnabled(boolean)

methods can be used to test if CPU time measurement is enabled
and to enable/disable this support respectively.
Enabling thread CPU measurement could be expensive in some
Java virtual machine implementations.

Thread Contention Monitoring

Some Java virtual machines may support thread contention monitoring.
When thread contention monitoring is enabled, the accumulated elapsed
time that the thread has blocked for synchronization or waited for
notification will be collected and returned in the

ThreadInfo

object.

The

isThreadContentionMonitoringSupported()

method can be used to
determine if a Java virtual machine supports thread contention monitoring.
The thread contention monitoring is disabled by default. The

setThreadContentionMonitoringEnabled(boolean)

method can be used to enable
thread contention monitoring.

Synchronization Information and Deadlock Detection

Some Java virtual machines may support monitoring of

object monitor usage

and

ownable synchronizer usage

.
The

getThreadInfo(long[], boolean, boolean)

and

dumpAllThreads(boolean, boolean)

methods can be used to obtain the thread stack trace
and synchronization information including which

lock

a thread is blocked to
acquire or waiting on and which locks the thread currently owns.

The

ThreadMXBean

interface provides the

findMonitorDeadlockedThreads()

and

findDeadlockedThreads()

methods to find deadlocks in
the running application.

A Java virtual machine has a single instance of the implementation
class of this interface. This instance implementing this interface is
an

MXBean

that can be obtained by calling
the

ManagementFactory.getThreadMXBean()

method or
from the

platform MBeanServer

method.

The

ObjectName

for uniquely identifying the MXBean for
the thread system within an MBeanServer is:

java.lang:type=Threading

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

Thread ID

Thread ID is a positive long value returned by calling the

Thread.getId()

method for a thread.
The thread ID is unique during its lifetime. When a thread
is terminated, this thread ID may be reused.

Some methods in this interface take a thread ID or an array
of thread IDs as the input parameter and return per-thread information.

Thread CPU time

A Java virtual machine implementation may support measuring
the CPU time for the current thread, for any thread, or for no threads.

The

isThreadCpuTimeSupported()

method can be used to determine
if a Java virtual machine supports measuring of the CPU time for any
thread. The

isCurrentThreadCpuTimeSupported()

method can
be used to determine if a Java virtual machine supports measuring of
the CPU time for the current thread.
A Java virtual machine implementation that supports CPU time measurement
for any thread will also support that for the current thread.

The CPU time provided by this interface has nanosecond precision
but not necessarily nanosecond accuracy.

A Java virtual machine may disable CPU time measurement
by default.
The

isThreadCpuTimeEnabled()

and

setThreadCpuTimeEnabled(boolean)

methods can be used to test if CPU time measurement is enabled
and to enable/disable this support respectively.
Enabling thread CPU measurement could be expensive in some
Java virtual machine implementations.

Thread Contention Monitoring

Some Java virtual machines may support thread contention monitoring.
When thread contention monitoring is enabled, the accumulated elapsed
time that the thread has blocked for synchronization or waited for
notification will be collected and returned in the

ThreadInfo

object.

The

isThreadContentionMonitoringSupported()

method can be used to
determine if a Java virtual machine supports thread contention monitoring.
The thread contention monitoring is disabled by default. The

setThreadContentionMonitoringEnabled(boolean)

method can be used to enable
thread contention monitoring.

Synchronization Information and Deadlock Detection

Some Java virtual machines may support monitoring of

object monitor usage

and

ownable synchronizer usage

.
The

getThreadInfo(long[], boolean, boolean)

and

dumpAllThreads(boolean, boolean)

methods can be used to obtain the thread stack trace
and synchronization information including which

lock

a thread is blocked to
acquire or waiting on and which locks the thread currently owns.

The

ThreadMXBean

interface provides the

findMonitorDeadlockedThreads()

and

findDeadlockedThreads()

methods to find deadlocks in
the running application.

The

ObjectName

for uniquely identifying the MXBean for
the thread system within an MBeanServer is:

java.lang:type=Threading

It can be obtained by calling the

PlatformManagedObject.getObjectName()

method.

Thread ID

Thread ID is a positive long value returned by calling the

Thread.getId()

method for a thread.
The thread ID is unique during its lifetime. When a thread
is terminated, this thread ID may be reused.

Some methods in this interface take a thread ID or an array
of thread IDs as the input parameter and return per-thread information.

Thread CPU time

A Java virtual machine implementation may support measuring
the CPU time for the current thread, for any thread, or for no threads.

The

isThreadCpuTimeSupported()

method can be used to determine
if a Java virtual machine supports measuring of the CPU time for any
thread. The

isCurrentThreadCpuTimeSupported()

method can
be used to determine if a Java virtual machine supports measuring of
the CPU time for the current thread.
A Java virtual machine implementation that supports CPU time measurement
for any thread will also support that for the current thread.

The CPU time provided by this interface has nanosecond precision
but not necessarily nanosecond accuracy.

A Java virtual machine may disable CPU time measurement
by default.
The

isThreadCpuTimeEnabled()

and

setThreadCpuTimeEnabled(boolean)

methods can be used to test if CPU time measurement is enabled
and to enable/disable this support respectively.
Enabling thread CPU measurement could be expensive in some
Java virtual machine implementations.

Thread Contention Monitoring

Some Java virtual machines may support thread contention monitoring.
When thread contention monitoring is enabled, the accumulated elapsed
time that the thread has blocked for synchronization or waited for
notification will be collected and returned in the

ThreadInfo

object.

The

isThreadContentionMonitoringSupported()

method can be used to
determine if a Java virtual machine supports thread contention monitoring.
The thread contention monitoring is disabled by default. The

setThreadContentionMonitoringEnabled(boolean)

method can be used to enable
thread contention monitoring.

Synchronization Information and Deadlock Detection

Some Java virtual machines may support monitoring of

object monitor usage

and

ownable synchronizer usage

.
The

getThreadInfo(long[], boolean, boolean)

and

dumpAllThreads(boolean, boolean)

methods can be used to obtain the thread stack trace
and synchronization information including which

lock

a thread is blocked to
acquire or waiting on and which locks the thread currently owns.

The

ThreadMXBean

interface provides the

findMonitorDeadlockedThreads()

and

findDeadlockedThreads()

methods to find deadlocks in
the running application.

---

#### Thread ID

Some methods in this interface take a thread ID or an array
of thread IDs as the input parameter and return per-thread information.

Thread CPU time

A Java virtual machine implementation may support measuring
the CPU time for the current thread, for any thread, or for no threads.

The

isThreadCpuTimeSupported()

method can be used to determine
if a Java virtual machine supports measuring of the CPU time for any
thread. The

isCurrentThreadCpuTimeSupported()

method can
be used to determine if a Java virtual machine supports measuring of
the CPU time for the current thread.
A Java virtual machine implementation that supports CPU time measurement
for any thread will also support that for the current thread.

The CPU time provided by this interface has nanosecond precision
but not necessarily nanosecond accuracy.

A Java virtual machine may disable CPU time measurement
by default.
The

isThreadCpuTimeEnabled()

and

setThreadCpuTimeEnabled(boolean)

methods can be used to test if CPU time measurement is enabled
and to enable/disable this support respectively.
Enabling thread CPU measurement could be expensive in some
Java virtual machine implementations.

Thread Contention Monitoring

Some Java virtual machines may support thread contention monitoring.
When thread contention monitoring is enabled, the accumulated elapsed
time that the thread has blocked for synchronization or waited for
notification will be collected and returned in the

ThreadInfo

object.

The

isThreadContentionMonitoringSupported()

method can be used to
determine if a Java virtual machine supports thread contention monitoring.
The thread contention monitoring is disabled by default. The

setThreadContentionMonitoringEnabled(boolean)

method can be used to enable
thread contention monitoring.

Synchronization Information and Deadlock Detection

Some Java virtual machines may support monitoring of

object monitor usage

and

ownable synchronizer usage

.
The

getThreadInfo(long[], boolean, boolean)

and

dumpAllThreads(boolean, boolean)

methods can be used to obtain the thread stack trace
and synchronization information including which

lock

a thread is blocked to
acquire or waiting on and which locks the thread currently owns.

The

ThreadMXBean

interface provides the

findMonitorDeadlockedThreads()

and

findDeadlockedThreads()

methods to find deadlocks in
the running application.

---

#### Thread CPU time

The

isThreadCpuTimeSupported()

method can be used to determine
if a Java virtual machine supports measuring of the CPU time for any
thread. The

isCurrentThreadCpuTimeSupported()

method can
be used to determine if a Java virtual machine supports measuring of
the CPU time for the current thread.
A Java virtual machine implementation that supports CPU time measurement
for any thread will also support that for the current thread.

The CPU time provided by this interface has nanosecond precision
but not necessarily nanosecond accuracy.

A Java virtual machine may disable CPU time measurement
by default.
The

isThreadCpuTimeEnabled()

and

setThreadCpuTimeEnabled(boolean)

methods can be used to test if CPU time measurement is enabled
and to enable/disable this support respectively.
Enabling thread CPU measurement could be expensive in some
Java virtual machine implementations.

Thread Contention Monitoring

Some Java virtual machines may support thread contention monitoring.
When thread contention monitoring is enabled, the accumulated elapsed
time that the thread has blocked for synchronization or waited for
notification will be collected and returned in the

ThreadInfo

object.

The

isThreadContentionMonitoringSupported()

method can be used to
determine if a Java virtual machine supports thread contention monitoring.
The thread contention monitoring is disabled by default. The

setThreadContentionMonitoringEnabled(boolean)

method can be used to enable
thread contention monitoring.

Synchronization Information and Deadlock Detection

Some Java virtual machines may support monitoring of

object monitor usage

and

ownable synchronizer usage

.
The

getThreadInfo(long[], boolean, boolean)

and

dumpAllThreads(boolean, boolean)

methods can be used to obtain the thread stack trace
and synchronization information including which

lock

a thread is blocked to
acquire or waiting on and which locks the thread currently owns.

The

ThreadMXBean

interface provides the

findMonitorDeadlockedThreads()

and

findDeadlockedThreads()

methods to find deadlocks in
the running application.

The CPU time provided by this interface has nanosecond precision
but not necessarily nanosecond accuracy.

A Java virtual machine may disable CPU time measurement
by default.
The

isThreadCpuTimeEnabled()

and

setThreadCpuTimeEnabled(boolean)

methods can be used to test if CPU time measurement is enabled
and to enable/disable this support respectively.
Enabling thread CPU measurement could be expensive in some
Java virtual machine implementations.

Thread Contention Monitoring

Some Java virtual machines may support thread contention monitoring.
When thread contention monitoring is enabled, the accumulated elapsed
time that the thread has blocked for synchronization or waited for
notification will be collected and returned in the

ThreadInfo

object.

The

isThreadContentionMonitoringSupported()

method can be used to
determine if a Java virtual machine supports thread contention monitoring.
The thread contention monitoring is disabled by default. The

setThreadContentionMonitoringEnabled(boolean)

method can be used to enable
thread contention monitoring.

Synchronization Information and Deadlock Detection

Some Java virtual machines may support monitoring of

object monitor usage

and

ownable synchronizer usage

.
The

getThreadInfo(long[], boolean, boolean)

and

dumpAllThreads(boolean, boolean)

methods can be used to obtain the thread stack trace
and synchronization information including which

lock

a thread is blocked to
acquire or waiting on and which locks the thread currently owns.

The

ThreadMXBean

interface provides the

findMonitorDeadlockedThreads()

and

findDeadlockedThreads()

methods to find deadlocks in
the running application.

A Java virtual machine may disable CPU time measurement
by default.
The

isThreadCpuTimeEnabled()

and

setThreadCpuTimeEnabled(boolean)

methods can be used to test if CPU time measurement is enabled
and to enable/disable this support respectively.
Enabling thread CPU measurement could be expensive in some
Java virtual machine implementations.

Thread Contention Monitoring

Some Java virtual machines may support thread contention monitoring.
When thread contention monitoring is enabled, the accumulated elapsed
time that the thread has blocked for synchronization or waited for
notification will be collected and returned in the

ThreadInfo

object.

The

isThreadContentionMonitoringSupported()

method can be used to
determine if a Java virtual machine supports thread contention monitoring.
The thread contention monitoring is disabled by default. The

setThreadContentionMonitoringEnabled(boolean)

method can be used to enable
thread contention monitoring.

Synchronization Information and Deadlock Detection

Some Java virtual machines may support monitoring of

object monitor usage

and

ownable synchronizer usage

.
The

getThreadInfo(long[], boolean, boolean)

and

dumpAllThreads(boolean, boolean)

methods can be used to obtain the thread stack trace
and synchronization information including which

lock

a thread is blocked to
acquire or waiting on and which locks the thread currently owns.

The

ThreadMXBean

interface provides the

findMonitorDeadlockedThreads()

and

findDeadlockedThreads()

methods to find deadlocks in
the running application.

---

#### Thread Contention Monitoring

The

isThreadContentionMonitoringSupported()

method can be used to
determine if a Java virtual machine supports thread contention monitoring.
The thread contention monitoring is disabled by default. The

setThreadContentionMonitoringEnabled(boolean)

method can be used to enable
thread contention monitoring.

Synchronization Information and Deadlock Detection

Some Java virtual machines may support monitoring of

object monitor usage

and

ownable synchronizer usage

.
The

getThreadInfo(long[], boolean, boolean)

and

dumpAllThreads(boolean, boolean)

methods can be used to obtain the thread stack trace
and synchronization information including which

lock

a thread is blocked to
acquire or waiting on and which locks the thread currently owns.

The

ThreadMXBean

interface provides the

findMonitorDeadlockedThreads()

and

findDeadlockedThreads()

methods to find deadlocks in
the running application.

---

#### Synchronization Information and Deadlock Detection

The

ThreadMXBean

interface provides the

findMonitorDeadlockedThreads()

and

findDeadlockedThreads()

methods to find deadlocks in
the running application.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

ThreadInfo

[]

dumpAllThreads

​(boolean lockedMonitors,
boolean lockedSynchronizers)

Returns the thread info for all live threads with stack trace
and synchronization information.

default

ThreadInfo

[]

dumpAllThreads

​(boolean lockedMonitors,
boolean lockedSynchronizers,
int maxDepth)

Returns the thread info for all live threads
with stack trace of the specified maximum number of elements
and synchronization information.

long[]

findDeadlockedThreads

()

Finds cycles of threads that are in deadlock waiting to acquire
object monitors or

ownable synchronizers

.

long[]

findMonitorDeadlockedThreads

()

Finds cycles of threads that are in deadlock waiting to acquire
object monitors.

long[]

getAllThreadIds

()

Returns all live thread IDs.

long

getCurrentThreadCpuTime

()

Returns the total CPU time for the current thread in nanoseconds.

long

getCurrentThreadUserTime

()

Returns the CPU time that the current thread has executed
in user mode in nanoseconds.

int

getDaemonThreadCount

()

Returns the current number of live daemon threads.

int

getPeakThreadCount

()

Returns the peak live thread count since the Java virtual machine
started or peak was reset.

int

getThreadCount

()

Returns the current number of live threads including both
daemon and non-daemon threads.

long

getThreadCpuTime

​(long id)

Returns the total CPU time for a thread of the specified ID in nanoseconds.

ThreadInfo

getThreadInfo

​(long id)

Returns the thread info for a thread of the specified

id

with no stack trace.

ThreadInfo

[]

getThreadInfo

​(long[] ids)

Returns the thread info for each thread
whose ID is in the input array

ids

with no stack trace.

ThreadInfo

[]

getThreadInfo

​(long[] ids,
boolean lockedMonitors,
boolean lockedSynchronizers)

Returns the thread info for each thread
whose ID is in the input array

ids

,
with stack trace and synchronization information.

default

ThreadInfo

[]

getThreadInfo

​(long[] ids,
boolean lockedMonitors,
boolean lockedSynchronizers,
int maxDepth)

Returns the thread info for each thread whose ID
is in the input array

ids

,
with stack trace of the specified maximum number of elements
and synchronization information.

ThreadInfo

[]

getThreadInfo

​(long[] ids,
int maxDepth)

Returns the thread info for each thread
whose ID is in the input array

ids

,
with stack trace of a specified number of stack trace elements.

ThreadInfo

getThreadInfo

​(long id,
int maxDepth)

Returns a thread info for a thread of the specified

id

,
with stack trace of a specified number of stack trace elements.

long

getThreadUserTime

​(long id)

Returns the CPU time that a thread of the specified ID
has executed in user mode in nanoseconds.

long

getTotalStartedThreadCount

()

Returns the total number of threads created and also started
since the Java virtual machine started.

boolean

isCurrentThreadCpuTimeSupported

()

Tests if the Java virtual machine supports CPU time
measurement for the current thread.

boolean

isObjectMonitorUsageSupported

()

Tests if the Java virtual machine supports monitoring of
object monitor usage.

boolean

isSynchronizerUsageSupported

()

Tests if the Java virtual machine supports monitoring of

ownable synchronizer

usage.

boolean

isThreadContentionMonitoringEnabled

()

Tests if thread contention monitoring is enabled.

boolean

isThreadContentionMonitoringSupported

()

Tests if the Java virtual machine supports thread contention monitoring.

boolean

isThreadCpuTimeEnabled

()

Tests if thread CPU time measurement is enabled.

boolean

isThreadCpuTimeSupported

()

Tests if the Java virtual machine implementation supports CPU time
measurement for any thread.

void

resetPeakThreadCount

()

Resets the peak thread count to the current number of
live threads.

void

setThreadContentionMonitoringEnabled

​(boolean enable)

Enables or disables thread contention monitoring.

void

setThreadCpuTimeEnabled

​(boolean enable)

Enables or disables thread CPU time measurement.

- Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

ThreadInfo

[]

dumpAllThreads

​(boolean lockedMonitors,
boolean lockedSynchronizers)

Returns the thread info for all live threads with stack trace
and synchronization information.

default

ThreadInfo

[]

dumpAllThreads

​(boolean lockedMonitors,
boolean lockedSynchronizers,
int maxDepth)

Returns the thread info for all live threads
with stack trace of the specified maximum number of elements
and synchronization information.

long[]

findDeadlockedThreads

()

Finds cycles of threads that are in deadlock waiting to acquire
object monitors or

ownable synchronizers

.

long[]

findMonitorDeadlockedThreads

()

Finds cycles of threads that are in deadlock waiting to acquire
object monitors.

long[]

getAllThreadIds

()

Returns all live thread IDs.

long

getCurrentThreadCpuTime

()

Returns the total CPU time for the current thread in nanoseconds.

long

getCurrentThreadUserTime

()

Returns the CPU time that the current thread has executed
in user mode in nanoseconds.

int

getDaemonThreadCount

()

Returns the current number of live daemon threads.

int

getPeakThreadCount

()

Returns the peak live thread count since the Java virtual machine
started or peak was reset.

int

getThreadCount

()

Returns the current number of live threads including both
daemon and non-daemon threads.

long

getThreadCpuTime

​(long id)

Returns the total CPU time for a thread of the specified ID in nanoseconds.

ThreadInfo

getThreadInfo

​(long id)

Returns the thread info for a thread of the specified

id

with no stack trace.

ThreadInfo

[]

getThreadInfo

​(long[] ids)

Returns the thread info for each thread
whose ID is in the input array

ids

with no stack trace.

ThreadInfo

[]

getThreadInfo

​(long[] ids,
boolean lockedMonitors,
boolean lockedSynchronizers)

Returns the thread info for each thread
whose ID is in the input array

ids

,
with stack trace and synchronization information.

default

ThreadInfo

[]

getThreadInfo

​(long[] ids,
boolean lockedMonitors,
boolean lockedSynchronizers,
int maxDepth)

Returns the thread info for each thread whose ID
is in the input array

ids

,
with stack trace of the specified maximum number of elements
and synchronization information.

ThreadInfo

[]

getThreadInfo

​(long[] ids,
int maxDepth)

Returns the thread info for each thread
whose ID is in the input array

ids

,
with stack trace of a specified number of stack trace elements.

ThreadInfo

getThreadInfo

​(long id,
int maxDepth)

Returns a thread info for a thread of the specified

id

,
with stack trace of a specified number of stack trace elements.

long

getThreadUserTime

​(long id)

Returns the CPU time that a thread of the specified ID
has executed in user mode in nanoseconds.

long

getTotalStartedThreadCount

()

Returns the total number of threads created and also started
since the Java virtual machine started.

boolean

isCurrentThreadCpuTimeSupported

()

Tests if the Java virtual machine supports CPU time
measurement for the current thread.

boolean

isObjectMonitorUsageSupported

()

Tests if the Java virtual machine supports monitoring of
object monitor usage.

boolean

isSynchronizerUsageSupported

()

Tests if the Java virtual machine supports monitoring of

ownable synchronizer

usage.

boolean

isThreadContentionMonitoringEnabled

()

Tests if thread contention monitoring is enabled.

boolean

isThreadContentionMonitoringSupported

()

Tests if the Java virtual machine supports thread contention monitoring.

boolean

isThreadCpuTimeEnabled

()

Tests if thread CPU time measurement is enabled.

boolean

isThreadCpuTimeSupported

()

Tests if the Java virtual machine implementation supports CPU time
measurement for any thread.

void

resetPeakThreadCount

()

Resets the peak thread count to the current number of
live threads.

void

setThreadContentionMonitoringEnabled

​(boolean enable)

Enables or disables thread contention monitoring.

void

setThreadCpuTimeEnabled

​(boolean enable)

Enables or disables thread CPU time measurement.

- Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

---

#### Method Summary

Returns the thread info for all live threads with stack trace
and synchronization information.

Returns the thread info for all live threads
with stack trace of the specified maximum number of elements
and synchronization information.

Finds cycles of threads that are in deadlock waiting to acquire
object monitors or

ownable synchronizers

.

Finds cycles of threads that are in deadlock waiting to acquire
object monitors.

Returns all live thread IDs.

Returns the total CPU time for the current thread in nanoseconds.

Returns the CPU time that the current thread has executed
in user mode in nanoseconds.

Returns the current number of live daemon threads.

Returns the peak live thread count since the Java virtual machine
started or peak was reset.

Returns the current number of live threads including both
daemon and non-daemon threads.

Returns the total CPU time for a thread of the specified ID in nanoseconds.

Returns the thread info for a thread of the specified

id

with no stack trace.

Returns the thread info for each thread
whose ID is in the input array

ids

with no stack trace.

Returns the thread info for each thread
whose ID is in the input array

ids

,
with stack trace and synchronization information.

Returns the thread info for each thread whose ID
is in the input array

ids

,
with stack trace of the specified maximum number of elements
and synchronization information.

Returns the thread info for each thread
whose ID is in the input array

ids

,
with stack trace of a specified number of stack trace elements.

Returns a thread info for a thread of the specified

id

,
with stack trace of a specified number of stack trace elements.

Returns the CPU time that a thread of the specified ID
has executed in user mode in nanoseconds.

Returns the total number of threads created and also started
since the Java virtual machine started.

Tests if the Java virtual machine supports CPU time
measurement for the current thread.

Tests if the Java virtual machine supports monitoring of
object monitor usage.

Tests if the Java virtual machine supports monitoring of

ownable synchronizer

usage.

Tests if thread contention monitoring is enabled.

Tests if the Java virtual machine supports thread contention monitoring.

Tests if thread CPU time measurement is enabled.

Tests if the Java virtual machine implementation supports CPU time
measurement for any thread.

Resets the peak thread count to the current number of
live threads.

Enables or disables thread contention monitoring.

Enables or disables thread CPU time measurement.

Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

---

#### Methods declared in interface java.lang.management. PlatformManagedObject

============ METHOD DETAIL ==========

- Method Detail

- getThreadCount

```java
int getThreadCount()
```

Returns the current number of live threads including both
daemon and non-daemon threads.

**Returns:** the current number of live threads.

- getPeakThreadCount

```java
int getPeakThreadCount()
```

Returns the peak live thread count since the Java virtual machine
started or peak was reset.

**Returns:** the peak live thread count.

- getTotalStartedThreadCount

```java
long getTotalStartedThreadCount()
```

Returns the total number of threads created and also started
since the Java virtual machine started.

**Returns:** the total number of threads started.

- getDaemonThreadCount

```java
int getDaemonThreadCount()
```

Returns the current number of live daemon threads.

**Returns:** the current number of live daemon threads.

- getAllThreadIds

```java
long[] getAllThreadIds()
```

Returns all live thread IDs.
Some threads included in the returned array
may have been terminated when this method returns.

**Returns:** an array of

long

, each is a thread ID.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").

- getThreadInfo

```java
ThreadInfo
getThreadInfo​(long id)
```

Returns the thread info for a thread of the specified

id

with no stack trace.
This method is equivalent to calling:

getThreadInfo(id, 0);

This method returns a

ThreadInfo

object representing
the thread information for the thread of the specified ID.
The stack trace, locked monitors, and locked synchronizers
in the returned

ThreadInfo

object will
be empty.

If a thread of the given ID is not alive or does not exist,
this method will return

null

. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

**Parameters:** id

- the thread ID of the thread. Must be positive.
**Returns:** a

ThreadInfo

object for the thread of the given ID
with no stack trace, no locked monitor and no synchronizer info;

null

if the thread of the given ID is not alive or
it does not exist.
**Throws:** IllegalArgumentException

- if

id <= 0

.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").

- getThreadInfo

```java
ThreadInfo
[] getThreadInfo​(long[] ids)
```

Returns the thread info for each thread
whose ID is in the input array

ids

with no stack trace.
This method is equivalent to calling:

```java
getThreadInfo
(ids, 0);
```

This method returns an array of the

ThreadInfo

objects.
The stack trace, locked monitors, and locked synchronizers
in each

ThreadInfo

object will be empty.

If a thread of a given ID is not alive or does not exist,
the corresponding element in the returned array will
contain

null

. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

**Parameters:** ids

- an array of thread IDs.
**Returns:** an array of the

ThreadInfo

objects, each containing
information about a thread whose ID is in the corresponding
element of the input array of IDs
with no stack trace, no locked monitor and no synchronizer info.
**Throws:** IllegalArgumentException

- if any element in the input array

ids

is

<= 0

.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").

- getThreadInfo

```java
ThreadInfo
getThreadInfo​(long id,
int maxDepth)
```

Returns a thread info for a thread of the specified

id

,
with stack trace of a specified number of stack trace elements.
The

maxDepth

parameter indicates the maximum number of

StackTraceElement

to be retrieved from the stack trace.
If

maxDepth == Integer.MAX_VALUE

, the entire stack trace of
the thread will be dumped.
If

maxDepth == 0

, no stack trace of the thread
will be dumped.
This method does not obtain the locked monitors and locked
synchronizers of the thread.

When the Java virtual machine has no stack trace information
about a thread or

maxDepth == 0

,
the stack trace in the

ThreadInfo

object will be an empty array of

StackTraceElement

.

If a thread of the given ID is not alive or does not exist,
this method will return

null

. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

**Parameters:** id

- the thread ID of the thread. Must be positive.
**Parameters:** maxDepth

- the maximum number of entries in the stack trace
to be dumped.

Integer.MAX_VALUE

could be used to request
the entire stack to be dumped.
**Returns:** a

ThreadInfo

of the thread of the given ID
with no locked monitor and synchronizer info.

null

if the thread of the given ID is not alive or
it does not exist.
**Throws:** IllegalArgumentException

- if

id <= 0

.
**Throws:** IllegalArgumentException

- if

maxDepth is negative

.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").

- getThreadInfo

```java
ThreadInfo
[] getThreadInfo​(long[] ids,
int maxDepth)
```

Returns the thread info for each thread
whose ID is in the input array

ids

,
with stack trace of a specified number of stack trace elements.
The

maxDepth

parameter indicates the maximum number of

StackTraceElement

to be retrieved from the stack trace.
If

maxDepth == Integer.MAX_VALUE

, the entire stack trace of
the thread will be dumped.
If

maxDepth == 0

, no stack trace of the thread
will be dumped.
This method does not obtain the locked monitors and locked
synchronizers of the threads.

When the Java virtual machine has no stack trace information
about a thread or

maxDepth == 0

,
the stack trace in the

ThreadInfo

object will be an empty array of

StackTraceElement

.

This method returns an array of the

ThreadInfo

objects,
each is the thread information about the thread with the same index
as in the

ids

array.
If a thread of the given ID is not alive or does not exist,

null

will be set in the corresponding element
in the returned array. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

**Parameters:** ids

- an array of thread IDs
**Parameters:** maxDepth

- the maximum number of entries in the stack trace
to be dumped.

Integer.MAX_VALUE

could be used to request
the entire stack to be dumped.
**Returns:** an array of the

ThreadInfo

objects, each containing
information about a thread whose ID is in the corresponding
element of the input array of IDs with no locked monitor and
synchronizer info.
**Throws:** IllegalArgumentException

- if

maxDepth is negative

.
**Throws:** IllegalArgumentException

- if any element in the input array

ids

is

<= 0

.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").

- isThreadContentionMonitoringSupported

```java
boolean isThreadContentionMonitoringSupported()
```

Tests if the Java virtual machine supports thread contention monitoring.

**Returns:** true

if the Java virtual machine supports thread contention monitoring;

false

otherwise.

- isThreadContentionMonitoringEnabled

```java
boolean isThreadContentionMonitoringEnabled()
```

Tests if thread contention monitoring is enabled.

**Returns:** true

if thread contention monitoring is enabled;

false

otherwise.
**Throws:** UnsupportedOperationException

- if the Java virtual
machine does not support thread contention monitoring.
**See Also:** isThreadContentionMonitoringSupported()

- setThreadContentionMonitoringEnabled

```java
void setThreadContentionMonitoringEnabled​(boolean enable)
```

Enables or disables thread contention monitoring.
Thread contention monitoring is disabled by default.

**Parameters:** enable

-

true

to enable;

false

to disable.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine does not support thread contention monitoring.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("control").
**See Also:** isThreadContentionMonitoringSupported()

- getCurrentThreadCpuTime

```java
long getCurrentThreadCpuTime()
```

Returns the total CPU time for the current thread in nanoseconds.
The returned value is of nanoseconds precision but
not necessarily nanoseconds accuracy.
If the implementation distinguishes between user mode time and system
mode time, the returned CPU time is the amount of time that
the current thread has executed in user mode or system mode.

This is a convenience method for local management use and is
equivalent to calling:

```java
getThreadCpuTime
(Thread.currentThread().getId());
```

**Returns:** the total CPU time for the current thread if CPU time
measurement is enabled;

-1

otherwise.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine does not support CPU time measurement for
the current thread.
**See Also:** getCurrentThreadUserTime()

,

isCurrentThreadCpuTimeSupported()

,

isThreadCpuTimeEnabled()

,

setThreadCpuTimeEnabled(boolean)

- getCurrentThreadUserTime

```java
long getCurrentThreadUserTime()
```

Returns the CPU time that the current thread has executed
in user mode in nanoseconds.
The returned value is of nanoseconds precision but
not necessarily nanoseconds accuracy.

This is a convenience method for local management use and is
equivalent to calling:

```java
getThreadUserTime
(Thread.currentThread().getId());
```

**Returns:** the user-level CPU time for the current thread if CPU time
measurement is enabled;

-1

otherwise.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine does not support CPU time measurement for
the current thread.
**See Also:** getCurrentThreadCpuTime()

,

isCurrentThreadCpuTimeSupported()

,

isThreadCpuTimeEnabled()

,

setThreadCpuTimeEnabled(boolean)

- getThreadCpuTime

```java
long getThreadCpuTime​(long id)
```

Returns the total CPU time for a thread of the specified ID in nanoseconds.
The returned value is of nanoseconds precision but
not necessarily nanoseconds accuracy.
If the implementation distinguishes between user mode time and system
mode time, the returned CPU time is the amount of time that
the thread has executed in user mode or system mode.

If the thread of the specified ID is not alive or does not exist,
this method returns

-1

. If CPU time measurement
is disabled, this method returns

-1

.
A thread is alive if it has been started and has not yet died.

If CPU time measurement is enabled after the thread has started,
the Java virtual machine implementation may choose any time up to
and including the time that the capability is enabled as the point
where CPU time measurement starts.

**Parameters:** id

- the thread ID of a thread
**Returns:** the total CPU time for a thread of the specified ID
if the thread of the specified ID exists, the thread is alive,
and CPU time measurement is enabled;

-1

otherwise.
**Throws:** IllegalArgumentException

- if

id <= 0

.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine does not support CPU time measurement for
other threads.
**See Also:** getThreadUserTime(long)

,

isThreadCpuTimeSupported()

,

isThreadCpuTimeEnabled()

,

setThreadCpuTimeEnabled(boolean)

- getThreadUserTime

```java
long getThreadUserTime​(long id)
```

Returns the CPU time that a thread of the specified ID
has executed in user mode in nanoseconds.
The returned value is of nanoseconds precision but
not necessarily nanoseconds accuracy.

If the thread of the specified ID is not alive or does not exist,
this method returns

-1

. If CPU time measurement
is disabled, this method returns

-1

.
A thread is alive if it has been started and has not yet died.

If CPU time measurement is enabled after the thread has started,
the Java virtual machine implementation may choose any time up to
and including the time that the capability is enabled as the point
where CPU time measurement starts.

**Parameters:** id

- the thread ID of a thread
**Returns:** the user-level CPU time for a thread of the specified ID
if the thread of the specified ID exists, the thread is alive,
and CPU time measurement is enabled;

-1

otherwise.
**Throws:** IllegalArgumentException

- if

id <= 0

.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine does not support CPU time measurement for
other threads.
**See Also:** getThreadCpuTime(long)

,

isThreadCpuTimeSupported()

,

isThreadCpuTimeEnabled()

,

setThreadCpuTimeEnabled(boolean)

- isThreadCpuTimeSupported

```java
boolean isThreadCpuTimeSupported()
```

Tests if the Java virtual machine implementation supports CPU time
measurement for any thread.
A Java virtual machine implementation that supports CPU time
measurement for any thread will also support CPU time
measurement for the current thread.

**Returns:** true

if the Java virtual machine supports CPU time
measurement for any thread;

false

otherwise.

- isCurrentThreadCpuTimeSupported

```java
boolean isCurrentThreadCpuTimeSupported()
```

Tests if the Java virtual machine supports CPU time
measurement for the current thread.
This method returns

true

if

isThreadCpuTimeSupported()

returns

true

.

**Returns:** true

if the Java virtual machine supports CPU time
measurement for current thread;

false

otherwise.

- isThreadCpuTimeEnabled

```java
boolean isThreadCpuTimeEnabled()
```

Tests if thread CPU time measurement is enabled.

**Returns:** true

if thread CPU time measurement is enabled;

false

otherwise.
**Throws:** UnsupportedOperationException

- if the Java virtual
machine does not support CPU time measurement for other threads
nor for the current thread.
**See Also:** isThreadCpuTimeSupported()

,

isCurrentThreadCpuTimeSupported()

- setThreadCpuTimeEnabled

```java
void setThreadCpuTimeEnabled​(boolean enable)
```

Enables or disables thread CPU time measurement. The default
is platform dependent.

**Parameters:** enable

-

true

to enable;

false

to disable.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine does not support CPU time measurement for
any threads nor for the current thread.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("control").
**See Also:** isThreadCpuTimeSupported()

,

isCurrentThreadCpuTimeSupported()

- findMonitorDeadlockedThreads

```java
long[] findMonitorDeadlockedThreads()
```

Finds cycles of threads that are in deadlock waiting to acquire
object monitors. That is, threads that are blocked waiting to enter a
synchronization block or waiting to reenter a synchronization block
after an

Object.wait

call,
where each thread owns one monitor while
trying to obtain another monitor already held by another thread
in a cycle.

More formally, a thread is

monitor deadlocked

if it is
part of a cycle in the relation "is waiting for an object monitor
owned by". In the simplest case, thread A is blocked waiting
for a monitor owned by thread B, and thread B is blocked waiting
for a monitor owned by thread A.

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

This method finds deadlocks involving only object monitors.
To find deadlocks involving both object monitors and

ownable synchronizers

,
the

findDeadlockedThreads

method
should be used.

**Returns:** an array of IDs of the threads that are monitor
deadlocked, if any;

null

otherwise.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
**See Also:** findDeadlockedThreads()

- resetPeakThreadCount

```java
void resetPeakThreadCount()
```

Resets the peak thread count to the current number of
live threads.

**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("control").
**See Also:** getPeakThreadCount()

,

getThreadCount()

- findDeadlockedThreads

```java
long[] findDeadlockedThreads()
```

Finds cycles of threads that are in deadlock waiting to acquire
object monitors or

ownable synchronizers

.

Threads are

deadlocked

in a cycle waiting for a lock of
these two types if each thread owns one lock while
trying to acquire another lock already held
by another thread in the cycle.

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

**Returns:** an array of IDs of the threads that are
deadlocked waiting for object monitors or ownable synchronizers, if any;

null

otherwise.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
**Throws:** UnsupportedOperationException

- if the Java virtual
machine does not support monitoring of ownable synchronizer usage.
**Since:** 1.6
**See Also:** isSynchronizerUsageSupported()

,

findMonitorDeadlockedThreads()

- isObjectMonitorUsageSupported

```java
boolean isObjectMonitorUsageSupported()
```

Tests if the Java virtual machine supports monitoring of
object monitor usage.

**Returns:** true

if the Java virtual machine supports monitoring of
object monitor usage;

false

otherwise.
**Since:** 1.6
**See Also:** dumpAllThreads(boolean, boolean)

- isSynchronizerUsageSupported

```java
boolean isSynchronizerUsageSupported()
```

Tests if the Java virtual machine supports monitoring of

ownable synchronizer

usage.

**Returns:** true

if the Java virtual machine supports monitoring of ownable
synchronizer usage;

false

otherwise.
**Since:** 1.6
**See Also:** dumpAllThreads(boolean, boolean)

- getThreadInfo

```java
ThreadInfo
[] getThreadInfo​(long[] ids,
boolean lockedMonitors,
boolean lockedSynchronizers)
```

Returns the thread info for each thread
whose ID is in the input array

ids

,
with stack trace and synchronization information.
This is equivalent to calling:

getThreadInfo(ids, lockedMonitors, lockedSynchronizers, Integer.MAX_VALUE)

**Parameters:** ids

- an array of thread IDs.
**Parameters:** lockedMonitors

- if

true

, retrieves all locked monitors.
**Parameters:** lockedSynchronizers

- if

true

, retrieves all locked
ownable synchronizers.
**Returns:** an array of the

ThreadInfo

objects, each containing
information about a thread whose ID is in the corresponding
element of the input array of IDs.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
**Throws:** UnsupportedOperationException

-

- if

lockedMonitors

is

true

but
the Java virtual machine does not support monitoring
of

object monitor usage

; or
- if

lockedSynchronizers

is

true

but
the Java virtual machine does not support monitoring
of

ownable synchronizer usage

.
**Since:** 1.6
**See Also:** isObjectMonitorUsageSupported()

,

isSynchronizerUsageSupported()

- getThreadInfo

```java
default
ThreadInfo
[] getThreadInfo​(long[] ids,
boolean lockedMonitors,
boolean lockedSynchronizers,
int maxDepth)
```

Returns the thread info for each thread whose ID
is in the input array

ids

,
with stack trace of the specified maximum number of elements
and synchronization information.
If

maxDepth == 0

, no stack trace of the thread
will be dumped.

This method obtains a snapshot of the thread information
for each thread including:

- stack trace of the specified maximum number of elements,
- the object monitors currently locked by the thread
if

lockedMonitors

is

true

, and
- the

ownable synchronizers

currently locked by the thread
if

lockedSynchronizers

is

true

.

This method returns an array of the

ThreadInfo

objects,
each is the thread information about the thread with the same index
as in the

ids

array.
If a thread of the given ID is not alive or does not exist,

null

will be set in the corresponding element
in the returned array. A thread is alive if
it has been started and has not yet died.

If a thread does not lock any object monitor or

lockedMonitors

is

false

, the returned

ThreadInfo

object will have an
empty

MonitorInfo

array. Similarly, if a thread does not
lock any synchronizer or

lockedSynchronizers

is

false

,
the returned

ThreadInfo

object
will have an empty

LockInfo

array.

When both

lockedMonitors

and

lockedSynchronizers

parameters are

false

, it is equivalent to calling:

```java
getThreadInfo(ids, maxDepth)
```

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

.
**Parameters:** ids

- an array of thread IDs.
**Parameters:** lockedMonitors

- if

true

, retrieves all locked monitors.
**Parameters:** lockedSynchronizers

- if

true

, retrieves all locked
ownable synchronizers.
**Parameters:** maxDepth

- indicates the maximum number of

StackTraceElement

to be retrieved from the stack trace.
**Returns:** an array of the

ThreadInfo

objects, each containing
information about a thread whose ID is in the corresponding
element of the input array of IDs.
**Throws:** IllegalArgumentException

- if

maxDepth

is negative.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
**Throws:** UnsupportedOperationException

-

- if

lockedMonitors

is

true

but
the Java virtual machine does not support monitoring
of

object monitor usage

; or
- if

lockedSynchronizers

is

true

but
the Java virtual machine does not support monitoring
of

ownable synchronizer usage

.
**Since:** 10
**See Also:** isObjectMonitorUsageSupported()

,

isSynchronizerUsageSupported()

- dumpAllThreads

```java
ThreadInfo
[] dumpAllThreads​(boolean lockedMonitors,
boolean lockedSynchronizers)
```

Returns the thread info for all live threads with stack trace
and synchronization information.
This is equivalent to calling:

dumpAllThreads(lockedMonitors, lockedSynchronizers, Integer.MAX_VALUE)

**Parameters:** lockedMonitors

- if

true

, dump all locked monitors.
**Parameters:** lockedSynchronizers

- if

true

, dump all locked
ownable synchronizers.
**Returns:** an array of

ThreadInfo

for all live threads.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
**Throws:** UnsupportedOperationException

-

- if

lockedMonitors

is

true

but
the Java virtual machine does not support monitoring
of

object monitor usage

; or
- if

lockedSynchronizers

is

true

but
the Java virtual machine does not support monitoring
of

ownable synchronizer usage

.
**Since:** 1.6
**See Also:** isObjectMonitorUsageSupported()

,

isSynchronizerUsageSupported()

- dumpAllThreads

```java
default
ThreadInfo
[] dumpAllThreads​(boolean lockedMonitors,
boolean lockedSynchronizers,
int maxDepth)
```

Returns the thread info for all live threads
with stack trace of the specified maximum number of elements
and synchronization information.
if

maxDepth == 0

, no stack trace of the thread
will be dumped.
Some threads included in the returned array
may have been terminated when this method returns.

This method returns an array of

ThreadInfo

objects
as specified in the

getThreadInfo(long[], boolean, boolean, int)

method.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

.
**Parameters:** lockedMonitors

- if

true

, dump all locked monitors.
**Parameters:** lockedSynchronizers

- if

true

, dump all locked
ownable synchronizers.
**Parameters:** maxDepth

- indicates the maximum number of

StackTraceElement

to be retrieved from the stack trace.
**Returns:** an array of

ThreadInfo

for all live threads.
**Throws:** IllegalArgumentException

- if

maxDepth

is negative.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
**Throws:** UnsupportedOperationException

-

- if

lockedMonitors

is

true

but
the Java virtual machine does not support monitoring
of

object monitor usage

; or
- if

lockedSynchronizers

is

true

but
the Java virtual machine does not support monitoring
of

ownable synchronizer usage

.
**Since:** 10
**See Also:** isObjectMonitorUsageSupported()

,

isSynchronizerUsageSupported()

Method Detail

- getThreadCount

```java
int getThreadCount()
```

Returns the current number of live threads including both
daemon and non-daemon threads.

**Returns:** the current number of live threads.

- getPeakThreadCount

```java
int getPeakThreadCount()
```

Returns the peak live thread count since the Java virtual machine
started or peak was reset.

**Returns:** the peak live thread count.

- getTotalStartedThreadCount

```java
long getTotalStartedThreadCount()
```

Returns the total number of threads created and also started
since the Java virtual machine started.

**Returns:** the total number of threads started.

- getDaemonThreadCount

```java
int getDaemonThreadCount()
```

Returns the current number of live daemon threads.

**Returns:** the current number of live daemon threads.

- getAllThreadIds

```java
long[] getAllThreadIds()
```

Returns all live thread IDs.
Some threads included in the returned array
may have been terminated when this method returns.

**Returns:** an array of

long

, each is a thread ID.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").

- getThreadInfo

```java
ThreadInfo
getThreadInfo​(long id)
```

Returns the thread info for a thread of the specified

id

with no stack trace.
This method is equivalent to calling:

getThreadInfo(id, 0);

This method returns a

ThreadInfo

object representing
the thread information for the thread of the specified ID.
The stack trace, locked monitors, and locked synchronizers
in the returned

ThreadInfo

object will
be empty.

If a thread of the given ID is not alive or does not exist,
this method will return

null

. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

**Parameters:** id

- the thread ID of the thread. Must be positive.
**Returns:** a

ThreadInfo

object for the thread of the given ID
with no stack trace, no locked monitor and no synchronizer info;

null

if the thread of the given ID is not alive or
it does not exist.
**Throws:** IllegalArgumentException

- if

id <= 0

.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").

- getThreadInfo

```java
ThreadInfo
[] getThreadInfo​(long[] ids)
```

Returns the thread info for each thread
whose ID is in the input array

ids

with no stack trace.
This method is equivalent to calling:

```java
getThreadInfo
(ids, 0);
```

This method returns an array of the

ThreadInfo

objects.
The stack trace, locked monitors, and locked synchronizers
in each

ThreadInfo

object will be empty.

If a thread of a given ID is not alive or does not exist,
the corresponding element in the returned array will
contain

null

. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

**Parameters:** ids

- an array of thread IDs.
**Returns:** an array of the

ThreadInfo

objects, each containing
information about a thread whose ID is in the corresponding
element of the input array of IDs
with no stack trace, no locked monitor and no synchronizer info.
**Throws:** IllegalArgumentException

- if any element in the input array

ids

is

<= 0

.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").

- getThreadInfo

```java
ThreadInfo
getThreadInfo​(long id,
int maxDepth)
```

Returns a thread info for a thread of the specified

id

,
with stack trace of a specified number of stack trace elements.
The

maxDepth

parameter indicates the maximum number of

StackTraceElement

to be retrieved from the stack trace.
If

maxDepth == Integer.MAX_VALUE

, the entire stack trace of
the thread will be dumped.
If

maxDepth == 0

, no stack trace of the thread
will be dumped.
This method does not obtain the locked monitors and locked
synchronizers of the thread.

When the Java virtual machine has no stack trace information
about a thread or

maxDepth == 0

,
the stack trace in the

ThreadInfo

object will be an empty array of

StackTraceElement

.

If a thread of the given ID is not alive or does not exist,
this method will return

null

. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

**Parameters:** id

- the thread ID of the thread. Must be positive.
**Parameters:** maxDepth

- the maximum number of entries in the stack trace
to be dumped.

Integer.MAX_VALUE

could be used to request
the entire stack to be dumped.
**Returns:** a

ThreadInfo

of the thread of the given ID
with no locked monitor and synchronizer info.

null

if the thread of the given ID is not alive or
it does not exist.
**Throws:** IllegalArgumentException

- if

id <= 0

.
**Throws:** IllegalArgumentException

- if

maxDepth is negative

.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").

- getThreadInfo

```java
ThreadInfo
[] getThreadInfo​(long[] ids,
int maxDepth)
```

Returns the thread info for each thread
whose ID is in the input array

ids

,
with stack trace of a specified number of stack trace elements.
The

maxDepth

parameter indicates the maximum number of

StackTraceElement

to be retrieved from the stack trace.
If

maxDepth == Integer.MAX_VALUE

, the entire stack trace of
the thread will be dumped.
If

maxDepth == 0

, no stack trace of the thread
will be dumped.
This method does not obtain the locked monitors and locked
synchronizers of the threads.

When the Java virtual machine has no stack trace information
about a thread or

maxDepth == 0

,
the stack trace in the

ThreadInfo

object will be an empty array of

StackTraceElement

.

This method returns an array of the

ThreadInfo

objects,
each is the thread information about the thread with the same index
as in the

ids

array.
If a thread of the given ID is not alive or does not exist,

null

will be set in the corresponding element
in the returned array. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

**Parameters:** ids

- an array of thread IDs
**Parameters:** maxDepth

- the maximum number of entries in the stack trace
to be dumped.

Integer.MAX_VALUE

could be used to request
the entire stack to be dumped.
**Returns:** an array of the

ThreadInfo

objects, each containing
information about a thread whose ID is in the corresponding
element of the input array of IDs with no locked monitor and
synchronizer info.
**Throws:** IllegalArgumentException

- if

maxDepth is negative

.
**Throws:** IllegalArgumentException

- if any element in the input array

ids

is

<= 0

.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").

- isThreadContentionMonitoringSupported

```java
boolean isThreadContentionMonitoringSupported()
```

Tests if the Java virtual machine supports thread contention monitoring.

**Returns:** true

if the Java virtual machine supports thread contention monitoring;

false

otherwise.

- isThreadContentionMonitoringEnabled

```java
boolean isThreadContentionMonitoringEnabled()
```

Tests if thread contention monitoring is enabled.

**Returns:** true

if thread contention monitoring is enabled;

false

otherwise.
**Throws:** UnsupportedOperationException

- if the Java virtual
machine does not support thread contention monitoring.
**See Also:** isThreadContentionMonitoringSupported()

- setThreadContentionMonitoringEnabled

```java
void setThreadContentionMonitoringEnabled​(boolean enable)
```

Enables or disables thread contention monitoring.
Thread contention monitoring is disabled by default.

**Parameters:** enable

-

true

to enable;

false

to disable.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine does not support thread contention monitoring.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("control").
**See Also:** isThreadContentionMonitoringSupported()

- getCurrentThreadCpuTime

```java
long getCurrentThreadCpuTime()
```

Returns the total CPU time for the current thread in nanoseconds.
The returned value is of nanoseconds precision but
not necessarily nanoseconds accuracy.
If the implementation distinguishes between user mode time and system
mode time, the returned CPU time is the amount of time that
the current thread has executed in user mode or system mode.

This is a convenience method for local management use and is
equivalent to calling:

```java
getThreadCpuTime
(Thread.currentThread().getId());
```

**Returns:** the total CPU time for the current thread if CPU time
measurement is enabled;

-1

otherwise.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine does not support CPU time measurement for
the current thread.
**See Also:** getCurrentThreadUserTime()

,

isCurrentThreadCpuTimeSupported()

,

isThreadCpuTimeEnabled()

,

setThreadCpuTimeEnabled(boolean)

- getCurrentThreadUserTime

```java
long getCurrentThreadUserTime()
```

Returns the CPU time that the current thread has executed
in user mode in nanoseconds.
The returned value is of nanoseconds precision but
not necessarily nanoseconds accuracy.

This is a convenience method for local management use and is
equivalent to calling:

```java
getThreadUserTime
(Thread.currentThread().getId());
```

**Returns:** the user-level CPU time for the current thread if CPU time
measurement is enabled;

-1

otherwise.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine does not support CPU time measurement for
the current thread.
**See Also:** getCurrentThreadCpuTime()

,

isCurrentThreadCpuTimeSupported()

,

isThreadCpuTimeEnabled()

,

setThreadCpuTimeEnabled(boolean)

- getThreadCpuTime

```java
long getThreadCpuTime​(long id)
```

Returns the total CPU time for a thread of the specified ID in nanoseconds.
The returned value is of nanoseconds precision but
not necessarily nanoseconds accuracy.
If the implementation distinguishes between user mode time and system
mode time, the returned CPU time is the amount of time that
the thread has executed in user mode or system mode.

If the thread of the specified ID is not alive or does not exist,
this method returns

-1

. If CPU time measurement
is disabled, this method returns

-1

.
A thread is alive if it has been started and has not yet died.

If CPU time measurement is enabled after the thread has started,
the Java virtual machine implementation may choose any time up to
and including the time that the capability is enabled as the point
where CPU time measurement starts.

**Parameters:** id

- the thread ID of a thread
**Returns:** the total CPU time for a thread of the specified ID
if the thread of the specified ID exists, the thread is alive,
and CPU time measurement is enabled;

-1

otherwise.
**Throws:** IllegalArgumentException

- if

id <= 0

.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine does not support CPU time measurement for
other threads.
**See Also:** getThreadUserTime(long)

,

isThreadCpuTimeSupported()

,

isThreadCpuTimeEnabled()

,

setThreadCpuTimeEnabled(boolean)

- getThreadUserTime

```java
long getThreadUserTime​(long id)
```

Returns the CPU time that a thread of the specified ID
has executed in user mode in nanoseconds.
The returned value is of nanoseconds precision but
not necessarily nanoseconds accuracy.

If the thread of the specified ID is not alive or does not exist,
this method returns

-1

. If CPU time measurement
is disabled, this method returns

-1

.
A thread is alive if it has been started and has not yet died.

If CPU time measurement is enabled after the thread has started,
the Java virtual machine implementation may choose any time up to
and including the time that the capability is enabled as the point
where CPU time measurement starts.

**Parameters:** id

- the thread ID of a thread
**Returns:** the user-level CPU time for a thread of the specified ID
if the thread of the specified ID exists, the thread is alive,
and CPU time measurement is enabled;

-1

otherwise.
**Throws:** IllegalArgumentException

- if

id <= 0

.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine does not support CPU time measurement for
other threads.
**See Also:** getThreadCpuTime(long)

,

isThreadCpuTimeSupported()

,

isThreadCpuTimeEnabled()

,

setThreadCpuTimeEnabled(boolean)

- isThreadCpuTimeSupported

```java
boolean isThreadCpuTimeSupported()
```

Tests if the Java virtual machine implementation supports CPU time
measurement for any thread.
A Java virtual machine implementation that supports CPU time
measurement for any thread will also support CPU time
measurement for the current thread.

**Returns:** true

if the Java virtual machine supports CPU time
measurement for any thread;

false

otherwise.

- isCurrentThreadCpuTimeSupported

```java
boolean isCurrentThreadCpuTimeSupported()
```

Tests if the Java virtual machine supports CPU time
measurement for the current thread.
This method returns

true

if

isThreadCpuTimeSupported()

returns

true

.

**Returns:** true

if the Java virtual machine supports CPU time
measurement for current thread;

false

otherwise.

- isThreadCpuTimeEnabled

```java
boolean isThreadCpuTimeEnabled()
```

Tests if thread CPU time measurement is enabled.

**Returns:** true

if thread CPU time measurement is enabled;

false

otherwise.
**Throws:** UnsupportedOperationException

- if the Java virtual
machine does not support CPU time measurement for other threads
nor for the current thread.
**See Also:** isThreadCpuTimeSupported()

,

isCurrentThreadCpuTimeSupported()

- setThreadCpuTimeEnabled

```java
void setThreadCpuTimeEnabled​(boolean enable)
```

Enables or disables thread CPU time measurement. The default
is platform dependent.

**Parameters:** enable

-

true

to enable;

false

to disable.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine does not support CPU time measurement for
any threads nor for the current thread.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("control").
**See Also:** isThreadCpuTimeSupported()

,

isCurrentThreadCpuTimeSupported()

- findMonitorDeadlockedThreads

```java
long[] findMonitorDeadlockedThreads()
```

Finds cycles of threads that are in deadlock waiting to acquire
object monitors. That is, threads that are blocked waiting to enter a
synchronization block or waiting to reenter a synchronization block
after an

Object.wait

call,
where each thread owns one monitor while
trying to obtain another monitor already held by another thread
in a cycle.

More formally, a thread is

monitor deadlocked

if it is
part of a cycle in the relation "is waiting for an object monitor
owned by". In the simplest case, thread A is blocked waiting
for a monitor owned by thread B, and thread B is blocked waiting
for a monitor owned by thread A.

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

This method finds deadlocks involving only object monitors.
To find deadlocks involving both object monitors and

ownable synchronizers

,
the

findDeadlockedThreads

method
should be used.

**Returns:** an array of IDs of the threads that are monitor
deadlocked, if any;

null

otherwise.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
**See Also:** findDeadlockedThreads()

- resetPeakThreadCount

```java
void resetPeakThreadCount()
```

Resets the peak thread count to the current number of
live threads.

**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("control").
**See Also:** getPeakThreadCount()

,

getThreadCount()

- findDeadlockedThreads

```java
long[] findDeadlockedThreads()
```

Finds cycles of threads that are in deadlock waiting to acquire
object monitors or

ownable synchronizers

.

Threads are

deadlocked

in a cycle waiting for a lock of
these two types if each thread owns one lock while
trying to acquire another lock already held
by another thread in the cycle.

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

**Returns:** an array of IDs of the threads that are
deadlocked waiting for object monitors or ownable synchronizers, if any;

null

otherwise.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
**Throws:** UnsupportedOperationException

- if the Java virtual
machine does not support monitoring of ownable synchronizer usage.
**Since:** 1.6
**See Also:** isSynchronizerUsageSupported()

,

findMonitorDeadlockedThreads()

- isObjectMonitorUsageSupported

```java
boolean isObjectMonitorUsageSupported()
```

Tests if the Java virtual machine supports monitoring of
object monitor usage.

**Returns:** true

if the Java virtual machine supports monitoring of
object monitor usage;

false

otherwise.
**Since:** 1.6
**See Also:** dumpAllThreads(boolean, boolean)

- isSynchronizerUsageSupported

```java
boolean isSynchronizerUsageSupported()
```

Tests if the Java virtual machine supports monitoring of

ownable synchronizer

usage.

**Returns:** true

if the Java virtual machine supports monitoring of ownable
synchronizer usage;

false

otherwise.
**Since:** 1.6
**See Also:** dumpAllThreads(boolean, boolean)

- getThreadInfo

```java
ThreadInfo
[] getThreadInfo​(long[] ids,
boolean lockedMonitors,
boolean lockedSynchronizers)
```

Returns the thread info for each thread
whose ID is in the input array

ids

,
with stack trace and synchronization information.
This is equivalent to calling:

getThreadInfo(ids, lockedMonitors, lockedSynchronizers, Integer.MAX_VALUE)

**Parameters:** ids

- an array of thread IDs.
**Parameters:** lockedMonitors

- if

true

, retrieves all locked monitors.
**Parameters:** lockedSynchronizers

- if

true

, retrieves all locked
ownable synchronizers.
**Returns:** an array of the

ThreadInfo

objects, each containing
information about a thread whose ID is in the corresponding
element of the input array of IDs.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
**Throws:** UnsupportedOperationException

-

- if

lockedMonitors

is

true

but
the Java virtual machine does not support monitoring
of

object monitor usage

; or
- if

lockedSynchronizers

is

true

but
the Java virtual machine does not support monitoring
of

ownable synchronizer usage

.
**Since:** 1.6
**See Also:** isObjectMonitorUsageSupported()

,

isSynchronizerUsageSupported()

- getThreadInfo

```java
default
ThreadInfo
[] getThreadInfo​(long[] ids,
boolean lockedMonitors,
boolean lockedSynchronizers,
int maxDepth)
```

Returns the thread info for each thread whose ID
is in the input array

ids

,
with stack trace of the specified maximum number of elements
and synchronization information.
If

maxDepth == 0

, no stack trace of the thread
will be dumped.

This method obtains a snapshot of the thread information
for each thread including:

- stack trace of the specified maximum number of elements,
- the object monitors currently locked by the thread
if

lockedMonitors

is

true

, and
- the

ownable synchronizers

currently locked by the thread
if

lockedSynchronizers

is

true

.

This method returns an array of the

ThreadInfo

objects,
each is the thread information about the thread with the same index
as in the

ids

array.
If a thread of the given ID is not alive or does not exist,

null

will be set in the corresponding element
in the returned array. A thread is alive if
it has been started and has not yet died.

If a thread does not lock any object monitor or

lockedMonitors

is

false

, the returned

ThreadInfo

object will have an
empty

MonitorInfo

array. Similarly, if a thread does not
lock any synchronizer or

lockedSynchronizers

is

false

,
the returned

ThreadInfo

object
will have an empty

LockInfo

array.

When both

lockedMonitors

and

lockedSynchronizers

parameters are

false

, it is equivalent to calling:

```java
getThreadInfo(ids, maxDepth)
```

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

.
**Parameters:** ids

- an array of thread IDs.
**Parameters:** lockedMonitors

- if

true

, retrieves all locked monitors.
**Parameters:** lockedSynchronizers

- if

true

, retrieves all locked
ownable synchronizers.
**Parameters:** maxDepth

- indicates the maximum number of

StackTraceElement

to be retrieved from the stack trace.
**Returns:** an array of the

ThreadInfo

objects, each containing
information about a thread whose ID is in the corresponding
element of the input array of IDs.
**Throws:** IllegalArgumentException

- if

maxDepth

is negative.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
**Throws:** UnsupportedOperationException

-

- if

lockedMonitors

is

true

but
the Java virtual machine does not support monitoring
of

object monitor usage

; or
- if

lockedSynchronizers

is

true

but
the Java virtual machine does not support monitoring
of

ownable synchronizer usage

.
**Since:** 10
**See Also:** isObjectMonitorUsageSupported()

,

isSynchronizerUsageSupported()

- dumpAllThreads

```java
ThreadInfo
[] dumpAllThreads​(boolean lockedMonitors,
boolean lockedSynchronizers)
```

Returns the thread info for all live threads with stack trace
and synchronization information.
This is equivalent to calling:

dumpAllThreads(lockedMonitors, lockedSynchronizers, Integer.MAX_VALUE)

**Parameters:** lockedMonitors

- if

true

, dump all locked monitors.
**Parameters:** lockedSynchronizers

- if

true

, dump all locked
ownable synchronizers.
**Returns:** an array of

ThreadInfo

for all live threads.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
**Throws:** UnsupportedOperationException

-

- if

lockedMonitors

is

true

but
the Java virtual machine does not support monitoring
of

object monitor usage

; or
- if

lockedSynchronizers

is

true

but
the Java virtual machine does not support monitoring
of

ownable synchronizer usage

.
**Since:** 1.6
**See Also:** isObjectMonitorUsageSupported()

,

isSynchronizerUsageSupported()

- dumpAllThreads

```java
default
ThreadInfo
[] dumpAllThreads​(boolean lockedMonitors,
boolean lockedSynchronizers,
int maxDepth)
```

Returns the thread info for all live threads
with stack trace of the specified maximum number of elements
and synchronization information.
if

maxDepth == 0

, no stack trace of the thread
will be dumped.
Some threads included in the returned array
may have been terminated when this method returns.

This method returns an array of

ThreadInfo

objects
as specified in the

getThreadInfo(long[], boolean, boolean, int)

method.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

.
**Parameters:** lockedMonitors

- if

true

, dump all locked monitors.
**Parameters:** lockedSynchronizers

- if

true

, dump all locked
ownable synchronizers.
**Parameters:** maxDepth

- indicates the maximum number of

StackTraceElement

to be retrieved from the stack trace.
**Returns:** an array of

ThreadInfo

for all live threads.
**Throws:** IllegalArgumentException

- if

maxDepth

is negative.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
**Throws:** UnsupportedOperationException

-

- if

lockedMonitors

is

true

but
the Java virtual machine does not support monitoring
of

object monitor usage

; or
- if

lockedSynchronizers

is

true

but
the Java virtual machine does not support monitoring
of

ownable synchronizer usage

.
**Since:** 10
**See Also:** isObjectMonitorUsageSupported()

,

isSynchronizerUsageSupported()

---

#### Method Detail

getThreadCount

```java
int getThreadCount()
```

Returns the current number of live threads including both
daemon and non-daemon threads.

**Returns:** the current number of live threads.

---

#### getThreadCount

int getThreadCount()

Returns the current number of live threads including both
daemon and non-daemon threads.

getPeakThreadCount

```java
int getPeakThreadCount()
```

Returns the peak live thread count since the Java virtual machine
started or peak was reset.

**Returns:** the peak live thread count.

---

#### getPeakThreadCount

int getPeakThreadCount()

Returns the peak live thread count since the Java virtual machine
started or peak was reset.

getTotalStartedThreadCount

```java
long getTotalStartedThreadCount()
```

Returns the total number of threads created and also started
since the Java virtual machine started.

**Returns:** the total number of threads started.

---

#### getTotalStartedThreadCount

long getTotalStartedThreadCount()

Returns the total number of threads created and also started
since the Java virtual machine started.

getDaemonThreadCount

```java
int getDaemonThreadCount()
```

Returns the current number of live daemon threads.

**Returns:** the current number of live daemon threads.

---

#### getDaemonThreadCount

int getDaemonThreadCount()

Returns the current number of live daemon threads.

getAllThreadIds

```java
long[] getAllThreadIds()
```

Returns all live thread IDs.
Some threads included in the returned array
may have been terminated when this method returns.

**Returns:** an array of

long

, each is a thread ID.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").

---

#### getAllThreadIds

long[] getAllThreadIds()

Returns all live thread IDs.
Some threads included in the returned array
may have been terminated when this method returns.

getThreadInfo

```java
ThreadInfo
getThreadInfo​(long id)
```

Returns the thread info for a thread of the specified

id

with no stack trace.
This method is equivalent to calling:

getThreadInfo(id, 0);

This method returns a

ThreadInfo

object representing
the thread information for the thread of the specified ID.
The stack trace, locked monitors, and locked synchronizers
in the returned

ThreadInfo

object will
be empty.

If a thread of the given ID is not alive or does not exist,
this method will return

null

. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

**Parameters:** id

- the thread ID of the thread. Must be positive.
**Returns:** a

ThreadInfo

object for the thread of the given ID
with no stack trace, no locked monitor and no synchronizer info;

null

if the thread of the given ID is not alive or
it does not exist.
**Throws:** IllegalArgumentException

- if

id <= 0

.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").

---

#### getThreadInfo

ThreadInfo

getThreadInfo​(long id)

Returns the thread info for a thread of the specified

id

with no stack trace.
This method is equivalent to calling:

getThreadInfo(id, 0);

This method returns a

ThreadInfo

object representing
the thread information for the thread of the specified ID.
The stack trace, locked monitors, and locked synchronizers
in the returned

ThreadInfo

object will
be empty.

If a thread of the given ID is not alive or does not exist,
this method will return

null

. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

This method returns a

ThreadInfo

object representing
the thread information for the thread of the specified ID.
The stack trace, locked monitors, and locked synchronizers
in the returned

ThreadInfo

object will
be empty.

If a thread of the given ID is not alive or does not exist,
this method will return

null

. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

getThreadInfo

```java
ThreadInfo
[] getThreadInfo​(long[] ids)
```

Returns the thread info for each thread
whose ID is in the input array

ids

with no stack trace.
This method is equivalent to calling:

```java
getThreadInfo
(ids, 0);
```

This method returns an array of the

ThreadInfo

objects.
The stack trace, locked monitors, and locked synchronizers
in each

ThreadInfo

object will be empty.

If a thread of a given ID is not alive or does not exist,
the corresponding element in the returned array will
contain

null

. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

**Parameters:** ids

- an array of thread IDs.
**Returns:** an array of the

ThreadInfo

objects, each containing
information about a thread whose ID is in the corresponding
element of the input array of IDs
with no stack trace, no locked monitor and no synchronizer info.
**Throws:** IllegalArgumentException

- if any element in the input array

ids

is

<= 0

.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").

---

#### getThreadInfo

ThreadInfo

[] getThreadInfo​(long[] ids)

Returns the thread info for each thread
whose ID is in the input array

ids

with no stack trace.
This method is equivalent to calling:

```java
getThreadInfo
(ids, 0);
```

This method returns an array of the

ThreadInfo

objects.
The stack trace, locked monitors, and locked synchronizers
in each

ThreadInfo

object will be empty.

If a thread of a given ID is not alive or does not exist,
the corresponding element in the returned array will
contain

null

. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

getThreadInfo

(ids, 0);

This method returns an array of the

ThreadInfo

objects.
The stack trace, locked monitors, and locked synchronizers
in each

ThreadInfo

object will be empty.

If a thread of a given ID is not alive or does not exist,
the corresponding element in the returned array will
contain

null

. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

getThreadInfo

```java
ThreadInfo
getThreadInfo​(long id,
int maxDepth)
```

Returns a thread info for a thread of the specified

id

,
with stack trace of a specified number of stack trace elements.
The

maxDepth

parameter indicates the maximum number of

StackTraceElement

to be retrieved from the stack trace.
If

maxDepth == Integer.MAX_VALUE

, the entire stack trace of
the thread will be dumped.
If

maxDepth == 0

, no stack trace of the thread
will be dumped.
This method does not obtain the locked monitors and locked
synchronizers of the thread.

When the Java virtual machine has no stack trace information
about a thread or

maxDepth == 0

,
the stack trace in the

ThreadInfo

object will be an empty array of

StackTraceElement

.

If a thread of the given ID is not alive or does not exist,
this method will return

null

. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

**Parameters:** id

- the thread ID of the thread. Must be positive.
**Parameters:** maxDepth

- the maximum number of entries in the stack trace
to be dumped.

Integer.MAX_VALUE

could be used to request
the entire stack to be dumped.
**Returns:** a

ThreadInfo

of the thread of the given ID
with no locked monitor and synchronizer info.

null

if the thread of the given ID is not alive or
it does not exist.
**Throws:** IllegalArgumentException

- if

id <= 0

.
**Throws:** IllegalArgumentException

- if

maxDepth is negative

.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").

---

#### getThreadInfo

ThreadInfo

getThreadInfo​(long id,
int maxDepth)

Returns a thread info for a thread of the specified

id

,
with stack trace of a specified number of stack trace elements.
The

maxDepth

parameter indicates the maximum number of

StackTraceElement

to be retrieved from the stack trace.
If

maxDepth == Integer.MAX_VALUE

, the entire stack trace of
the thread will be dumped.
If

maxDepth == 0

, no stack trace of the thread
will be dumped.
This method does not obtain the locked monitors and locked
synchronizers of the thread.

When the Java virtual machine has no stack trace information
about a thread or

maxDepth == 0

,
the stack trace in the

ThreadInfo

object will be an empty array of

StackTraceElement

.

If a thread of the given ID is not alive or does not exist,
this method will return

null

. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

When the Java virtual machine has no stack trace information
about a thread or

maxDepth == 0

,
the stack trace in the

ThreadInfo

object will be an empty array of

StackTraceElement

.

If a thread of the given ID is not alive or does not exist,
this method will return

null

. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

If a thread of the given ID is not alive or does not exist,
this method will return

null

. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

getThreadInfo

```java
ThreadInfo
[] getThreadInfo​(long[] ids,
int maxDepth)
```

Returns the thread info for each thread
whose ID is in the input array

ids

,
with stack trace of a specified number of stack trace elements.
The

maxDepth

parameter indicates the maximum number of

StackTraceElement

to be retrieved from the stack trace.
If

maxDepth == Integer.MAX_VALUE

, the entire stack trace of
the thread will be dumped.
If

maxDepth == 0

, no stack trace of the thread
will be dumped.
This method does not obtain the locked monitors and locked
synchronizers of the threads.

When the Java virtual machine has no stack trace information
about a thread or

maxDepth == 0

,
the stack trace in the

ThreadInfo

object will be an empty array of

StackTraceElement

.

This method returns an array of the

ThreadInfo

objects,
each is the thread information about the thread with the same index
as in the

ids

array.
If a thread of the given ID is not alive or does not exist,

null

will be set in the corresponding element
in the returned array. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

**Parameters:** ids

- an array of thread IDs
**Parameters:** maxDepth

- the maximum number of entries in the stack trace
to be dumped.

Integer.MAX_VALUE

could be used to request
the entire stack to be dumped.
**Returns:** an array of the

ThreadInfo

objects, each containing
information about a thread whose ID is in the corresponding
element of the input array of IDs with no locked monitor and
synchronizer info.
**Throws:** IllegalArgumentException

- if

maxDepth is negative

.
**Throws:** IllegalArgumentException

- if any element in the input array

ids

is

<= 0

.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").

---

#### getThreadInfo

ThreadInfo

[] getThreadInfo​(long[] ids,
int maxDepth)

Returns the thread info for each thread
whose ID is in the input array

ids

,
with stack trace of a specified number of stack trace elements.
The

maxDepth

parameter indicates the maximum number of

StackTraceElement

to be retrieved from the stack trace.
If

maxDepth == Integer.MAX_VALUE

, the entire stack trace of
the thread will be dumped.
If

maxDepth == 0

, no stack trace of the thread
will be dumped.
This method does not obtain the locked monitors and locked
synchronizers of the threads.

When the Java virtual machine has no stack trace information
about a thread or

maxDepth == 0

,
the stack trace in the

ThreadInfo

object will be an empty array of

StackTraceElement

.

This method returns an array of the

ThreadInfo

objects,
each is the thread information about the thread with the same index
as in the

ids

array.
If a thread of the given ID is not alive or does not exist,

null

will be set in the corresponding element
in the returned array. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

When the Java virtual machine has no stack trace information
about a thread or

maxDepth == 0

,
the stack trace in the

ThreadInfo

object will be an empty array of

StackTraceElement

.

This method returns an array of the

ThreadInfo

objects,
each is the thread information about the thread with the same index
as in the

ids

array.
If a thread of the given ID is not alive or does not exist,

null

will be set in the corresponding element
in the returned array. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

This method returns an array of the

ThreadInfo

objects,
each is the thread information about the thread with the same index
as in the

ids

array.
If a thread of the given ID is not alive or does not exist,

null

will be set in the corresponding element
in the returned array. A thread is alive if
it has been started and has not yet died.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

isThreadContentionMonitoringSupported

```java
boolean isThreadContentionMonitoringSupported()
```

Tests if the Java virtual machine supports thread contention monitoring.

**Returns:** true

if the Java virtual machine supports thread contention monitoring;

false

otherwise.

---

#### isThreadContentionMonitoringSupported

boolean isThreadContentionMonitoringSupported()

Tests if the Java virtual machine supports thread contention monitoring.

isThreadContentionMonitoringEnabled

```java
boolean isThreadContentionMonitoringEnabled()
```

Tests if thread contention monitoring is enabled.

**Returns:** true

if thread contention monitoring is enabled;

false

otherwise.
**Throws:** UnsupportedOperationException

- if the Java virtual
machine does not support thread contention monitoring.
**See Also:** isThreadContentionMonitoringSupported()

---

#### isThreadContentionMonitoringEnabled

boolean isThreadContentionMonitoringEnabled()

Tests if thread contention monitoring is enabled.

setThreadContentionMonitoringEnabled

```java
void setThreadContentionMonitoringEnabled​(boolean enable)
```

Enables or disables thread contention monitoring.
Thread contention monitoring is disabled by default.

**Parameters:** enable

-

true

to enable;

false

to disable.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine does not support thread contention monitoring.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("control").
**See Also:** isThreadContentionMonitoringSupported()

---

#### setThreadContentionMonitoringEnabled

void setThreadContentionMonitoringEnabled​(boolean enable)

Enables or disables thread contention monitoring.
Thread contention monitoring is disabled by default.

getCurrentThreadCpuTime

```java
long getCurrentThreadCpuTime()
```

Returns the total CPU time for the current thread in nanoseconds.
The returned value is of nanoseconds precision but
not necessarily nanoseconds accuracy.
If the implementation distinguishes between user mode time and system
mode time, the returned CPU time is the amount of time that
the current thread has executed in user mode or system mode.

This is a convenience method for local management use and is
equivalent to calling:

```java
getThreadCpuTime
(Thread.currentThread().getId());
```

**Returns:** the total CPU time for the current thread if CPU time
measurement is enabled;

-1

otherwise.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine does not support CPU time measurement for
the current thread.
**See Also:** getCurrentThreadUserTime()

,

isCurrentThreadCpuTimeSupported()

,

isThreadCpuTimeEnabled()

,

setThreadCpuTimeEnabled(boolean)

---

#### getCurrentThreadCpuTime

long getCurrentThreadCpuTime()

Returns the total CPU time for the current thread in nanoseconds.
The returned value is of nanoseconds precision but
not necessarily nanoseconds accuracy.
If the implementation distinguishes between user mode time and system
mode time, the returned CPU time is the amount of time that
the current thread has executed in user mode or system mode.

This is a convenience method for local management use and is
equivalent to calling:

```java
getThreadCpuTime
(Thread.currentThread().getId());
```

This is a convenience method for local management use and is
equivalent to calling:

```java
getThreadCpuTime
(Thread.currentThread().getId());
```

getThreadCpuTime

(Thread.currentThread().getId());

getCurrentThreadUserTime

```java
long getCurrentThreadUserTime()
```

Returns the CPU time that the current thread has executed
in user mode in nanoseconds.
The returned value is of nanoseconds precision but
not necessarily nanoseconds accuracy.

This is a convenience method for local management use and is
equivalent to calling:

```java
getThreadUserTime
(Thread.currentThread().getId());
```

**Returns:** the user-level CPU time for the current thread if CPU time
measurement is enabled;

-1

otherwise.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine does not support CPU time measurement for
the current thread.
**See Also:** getCurrentThreadCpuTime()

,

isCurrentThreadCpuTimeSupported()

,

isThreadCpuTimeEnabled()

,

setThreadCpuTimeEnabled(boolean)

---

#### getCurrentThreadUserTime

long getCurrentThreadUserTime()

Returns the CPU time that the current thread has executed
in user mode in nanoseconds.
The returned value is of nanoseconds precision but
not necessarily nanoseconds accuracy.

This is a convenience method for local management use and is
equivalent to calling:

```java
getThreadUserTime
(Thread.currentThread().getId());
```

This is a convenience method for local management use and is
equivalent to calling:

```java
getThreadUserTime
(Thread.currentThread().getId());
```

getThreadUserTime

(Thread.currentThread().getId());

getThreadCpuTime

```java
long getThreadCpuTime​(long id)
```

Returns the total CPU time for a thread of the specified ID in nanoseconds.
The returned value is of nanoseconds precision but
not necessarily nanoseconds accuracy.
If the implementation distinguishes between user mode time and system
mode time, the returned CPU time is the amount of time that
the thread has executed in user mode or system mode.

If the thread of the specified ID is not alive or does not exist,
this method returns

-1

. If CPU time measurement
is disabled, this method returns

-1

.
A thread is alive if it has been started and has not yet died.

If CPU time measurement is enabled after the thread has started,
the Java virtual machine implementation may choose any time up to
and including the time that the capability is enabled as the point
where CPU time measurement starts.

**Parameters:** id

- the thread ID of a thread
**Returns:** the total CPU time for a thread of the specified ID
if the thread of the specified ID exists, the thread is alive,
and CPU time measurement is enabled;

-1

otherwise.
**Throws:** IllegalArgumentException

- if

id <= 0

.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine does not support CPU time measurement for
other threads.
**See Also:** getThreadUserTime(long)

,

isThreadCpuTimeSupported()

,

isThreadCpuTimeEnabled()

,

setThreadCpuTimeEnabled(boolean)

---

#### getThreadCpuTime

long getThreadCpuTime​(long id)

Returns the total CPU time for a thread of the specified ID in nanoseconds.
The returned value is of nanoseconds precision but
not necessarily nanoseconds accuracy.
If the implementation distinguishes between user mode time and system
mode time, the returned CPU time is the amount of time that
the thread has executed in user mode or system mode.

If the thread of the specified ID is not alive or does not exist,
this method returns

-1

. If CPU time measurement
is disabled, this method returns

-1

.
A thread is alive if it has been started and has not yet died.

If CPU time measurement is enabled after the thread has started,
the Java virtual machine implementation may choose any time up to
and including the time that the capability is enabled as the point
where CPU time measurement starts.

If the thread of the specified ID is not alive or does not exist,
this method returns

-1

. If CPU time measurement
is disabled, this method returns

-1

.
A thread is alive if it has been started and has not yet died.

If CPU time measurement is enabled after the thread has started,
the Java virtual machine implementation may choose any time up to
and including the time that the capability is enabled as the point
where CPU time measurement starts.

If CPU time measurement is enabled after the thread has started,
the Java virtual machine implementation may choose any time up to
and including the time that the capability is enabled as the point
where CPU time measurement starts.

getThreadUserTime

```java
long getThreadUserTime​(long id)
```

Returns the CPU time that a thread of the specified ID
has executed in user mode in nanoseconds.
The returned value is of nanoseconds precision but
not necessarily nanoseconds accuracy.

If the thread of the specified ID is not alive or does not exist,
this method returns

-1

. If CPU time measurement
is disabled, this method returns

-1

.
A thread is alive if it has been started and has not yet died.

If CPU time measurement is enabled after the thread has started,
the Java virtual machine implementation may choose any time up to
and including the time that the capability is enabled as the point
where CPU time measurement starts.

**Parameters:** id

- the thread ID of a thread
**Returns:** the user-level CPU time for a thread of the specified ID
if the thread of the specified ID exists, the thread is alive,
and CPU time measurement is enabled;

-1

otherwise.
**Throws:** IllegalArgumentException

- if

id <= 0

.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine does not support CPU time measurement for
other threads.
**See Also:** getThreadCpuTime(long)

,

isThreadCpuTimeSupported()

,

isThreadCpuTimeEnabled()

,

setThreadCpuTimeEnabled(boolean)

---

#### getThreadUserTime

long getThreadUserTime​(long id)

Returns the CPU time that a thread of the specified ID
has executed in user mode in nanoseconds.
The returned value is of nanoseconds precision but
not necessarily nanoseconds accuracy.

If the thread of the specified ID is not alive or does not exist,
this method returns

-1

. If CPU time measurement
is disabled, this method returns

-1

.
A thread is alive if it has been started and has not yet died.

If CPU time measurement is enabled after the thread has started,
the Java virtual machine implementation may choose any time up to
and including the time that the capability is enabled as the point
where CPU time measurement starts.

If the thread of the specified ID is not alive or does not exist,
this method returns

-1

. If CPU time measurement
is disabled, this method returns

-1

.
A thread is alive if it has been started and has not yet died.

If CPU time measurement is enabled after the thread has started,
the Java virtual machine implementation may choose any time up to
and including the time that the capability is enabled as the point
where CPU time measurement starts.

If CPU time measurement is enabled after the thread has started,
the Java virtual machine implementation may choose any time up to
and including the time that the capability is enabled as the point
where CPU time measurement starts.

isThreadCpuTimeSupported

```java
boolean isThreadCpuTimeSupported()
```

Tests if the Java virtual machine implementation supports CPU time
measurement for any thread.
A Java virtual machine implementation that supports CPU time
measurement for any thread will also support CPU time
measurement for the current thread.

**Returns:** true

if the Java virtual machine supports CPU time
measurement for any thread;

false

otherwise.

---

#### isThreadCpuTimeSupported

boolean isThreadCpuTimeSupported()

Tests if the Java virtual machine implementation supports CPU time
measurement for any thread.
A Java virtual machine implementation that supports CPU time
measurement for any thread will also support CPU time
measurement for the current thread.

isCurrentThreadCpuTimeSupported

```java
boolean isCurrentThreadCpuTimeSupported()
```

Tests if the Java virtual machine supports CPU time
measurement for the current thread.
This method returns

true

if

isThreadCpuTimeSupported()

returns

true

.

**Returns:** true

if the Java virtual machine supports CPU time
measurement for current thread;

false

otherwise.

---

#### isCurrentThreadCpuTimeSupported

boolean isCurrentThreadCpuTimeSupported()

Tests if the Java virtual machine supports CPU time
measurement for the current thread.
This method returns

true

if

isThreadCpuTimeSupported()

returns

true

.

isThreadCpuTimeEnabled

```java
boolean isThreadCpuTimeEnabled()
```

Tests if thread CPU time measurement is enabled.

**Returns:** true

if thread CPU time measurement is enabled;

false

otherwise.
**Throws:** UnsupportedOperationException

- if the Java virtual
machine does not support CPU time measurement for other threads
nor for the current thread.
**See Also:** isThreadCpuTimeSupported()

,

isCurrentThreadCpuTimeSupported()

---

#### isThreadCpuTimeEnabled

boolean isThreadCpuTimeEnabled()

Tests if thread CPU time measurement is enabled.

setThreadCpuTimeEnabled

```java
void setThreadCpuTimeEnabled​(boolean enable)
```

Enables or disables thread CPU time measurement. The default
is platform dependent.

**Parameters:** enable

-

true

to enable;

false

to disable.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine does not support CPU time measurement for
any threads nor for the current thread.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("control").
**See Also:** isThreadCpuTimeSupported()

,

isCurrentThreadCpuTimeSupported()

---

#### setThreadCpuTimeEnabled

void setThreadCpuTimeEnabled​(boolean enable)

Enables or disables thread CPU time measurement. The default
is platform dependent.

findMonitorDeadlockedThreads

```java
long[] findMonitorDeadlockedThreads()
```

Finds cycles of threads that are in deadlock waiting to acquire
object monitors. That is, threads that are blocked waiting to enter a
synchronization block or waiting to reenter a synchronization block
after an

Object.wait

call,
where each thread owns one monitor while
trying to obtain another monitor already held by another thread
in a cycle.

More formally, a thread is

monitor deadlocked

if it is
part of a cycle in the relation "is waiting for an object monitor
owned by". In the simplest case, thread A is blocked waiting
for a monitor owned by thread B, and thread B is blocked waiting
for a monitor owned by thread A.

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

This method finds deadlocks involving only object monitors.
To find deadlocks involving both object monitors and

ownable synchronizers

,
the

findDeadlockedThreads

method
should be used.

**Returns:** an array of IDs of the threads that are monitor
deadlocked, if any;

null

otherwise.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
**See Also:** findDeadlockedThreads()

---

#### findMonitorDeadlockedThreads

long[] findMonitorDeadlockedThreads()

Finds cycles of threads that are in deadlock waiting to acquire
object monitors. That is, threads that are blocked waiting to enter a
synchronization block or waiting to reenter a synchronization block
after an

Object.wait

call,
where each thread owns one monitor while
trying to obtain another monitor already held by another thread
in a cycle.

More formally, a thread is

monitor deadlocked

if it is
part of a cycle in the relation "is waiting for an object monitor
owned by". In the simplest case, thread A is blocked waiting
for a monitor owned by thread B, and thread B is blocked waiting
for a monitor owned by thread A.

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

This method finds deadlocks involving only object monitors.
To find deadlocks involving both object monitors and

ownable synchronizers

,
the

findDeadlockedThreads

method
should be used.

More formally, a thread is

monitor deadlocked

if it is
part of a cycle in the relation "is waiting for an object monitor
owned by". In the simplest case, thread A is blocked waiting
for a monitor owned by thread B, and thread B is blocked waiting
for a monitor owned by thread A.

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

This method finds deadlocks involving only object monitors.
To find deadlocks involving both object monitors and

ownable synchronizers

,
the

findDeadlockedThreads

method
should be used.

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

This method finds deadlocks involving only object monitors.
To find deadlocks involving both object monitors and

ownable synchronizers

,
the

findDeadlockedThreads

method
should be used.

This method finds deadlocks involving only object monitors.
To find deadlocks involving both object monitors and

ownable synchronizers

,
the

findDeadlockedThreads

method
should be used.

resetPeakThreadCount

```java
void resetPeakThreadCount()
```

Resets the peak thread count to the current number of
live threads.

**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("control").
**See Also:** getPeakThreadCount()

,

getThreadCount()

---

#### resetPeakThreadCount

void resetPeakThreadCount()

Resets the peak thread count to the current number of
live threads.

findDeadlockedThreads

```java
long[] findDeadlockedThreads()
```

Finds cycles of threads that are in deadlock waiting to acquire
object monitors or

ownable synchronizers

.

Threads are

deadlocked

in a cycle waiting for a lock of
these two types if each thread owns one lock while
trying to acquire another lock already held
by another thread in the cycle.

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

**Returns:** an array of IDs of the threads that are
deadlocked waiting for object monitors or ownable synchronizers, if any;

null

otherwise.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
**Throws:** UnsupportedOperationException

- if the Java virtual
machine does not support monitoring of ownable synchronizer usage.
**Since:** 1.6
**See Also:** isSynchronizerUsageSupported()

,

findMonitorDeadlockedThreads()

---

#### findDeadlockedThreads

long[] findDeadlockedThreads()

Finds cycles of threads that are in deadlock waiting to acquire
object monitors or

ownable synchronizers

.

Threads are

deadlocked

in a cycle waiting for a lock of
these two types if each thread owns one lock while
trying to acquire another lock already held
by another thread in the cycle.

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

isObjectMonitorUsageSupported

```java
boolean isObjectMonitorUsageSupported()
```

Tests if the Java virtual machine supports monitoring of
object monitor usage.

**Returns:** true

if the Java virtual machine supports monitoring of
object monitor usage;

false

otherwise.
**Since:** 1.6
**See Also:** dumpAllThreads(boolean, boolean)

---

#### isObjectMonitorUsageSupported

boolean isObjectMonitorUsageSupported()

Tests if the Java virtual machine supports monitoring of
object monitor usage.

isSynchronizerUsageSupported

```java
boolean isSynchronizerUsageSupported()
```

Tests if the Java virtual machine supports monitoring of

ownable synchronizer

usage.

**Returns:** true

if the Java virtual machine supports monitoring of ownable
synchronizer usage;

false

otherwise.
**Since:** 1.6
**See Also:** dumpAllThreads(boolean, boolean)

---

#### isSynchronizerUsageSupported

boolean isSynchronizerUsageSupported()

Tests if the Java virtual machine supports monitoring of

ownable synchronizer

usage.

getThreadInfo

```java
ThreadInfo
[] getThreadInfo​(long[] ids,
boolean lockedMonitors,
boolean lockedSynchronizers)
```

Returns the thread info for each thread
whose ID is in the input array

ids

,
with stack trace and synchronization information.
This is equivalent to calling:

getThreadInfo(ids, lockedMonitors, lockedSynchronizers, Integer.MAX_VALUE)

**Parameters:** ids

- an array of thread IDs.
**Parameters:** lockedMonitors

- if

true

, retrieves all locked monitors.
**Parameters:** lockedSynchronizers

- if

true

, retrieves all locked
ownable synchronizers.
**Returns:** an array of the

ThreadInfo

objects, each containing
information about a thread whose ID is in the corresponding
element of the input array of IDs.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
**Throws:** UnsupportedOperationException

-

- if

lockedMonitors

is

true

but
the Java virtual machine does not support monitoring
of

object monitor usage

; or
- if

lockedSynchronizers

is

true

but
the Java virtual machine does not support monitoring
of

ownable synchronizer usage

.
**Since:** 1.6
**See Also:** isObjectMonitorUsageSupported()

,

isSynchronizerUsageSupported()

---

#### getThreadInfo

ThreadInfo

[] getThreadInfo​(long[] ids,
boolean lockedMonitors,
boolean lockedSynchronizers)

Returns the thread info for each thread
whose ID is in the input array

ids

,
with stack trace and synchronization information.
This is equivalent to calling:

getThreadInfo(ids, lockedMonitors, lockedSynchronizers, Integer.MAX_VALUE)

if

lockedMonitors

is

true

but
the Java virtual machine does not support monitoring
of

object monitor usage

; or

if

lockedSynchronizers

is

true

but
the Java virtual machine does not support monitoring
of

ownable synchronizer usage

.

getThreadInfo

```java
default
ThreadInfo
[] getThreadInfo​(long[] ids,
boolean lockedMonitors,
boolean lockedSynchronizers,
int maxDepth)
```

Returns the thread info for each thread whose ID
is in the input array

ids

,
with stack trace of the specified maximum number of elements
and synchronization information.
If

maxDepth == 0

, no stack trace of the thread
will be dumped.

This method obtains a snapshot of the thread information
for each thread including:

- stack trace of the specified maximum number of elements,
- the object monitors currently locked by the thread
if

lockedMonitors

is

true

, and
- the

ownable synchronizers

currently locked by the thread
if

lockedSynchronizers

is

true

.

This method returns an array of the

ThreadInfo

objects,
each is the thread information about the thread with the same index
as in the

ids

array.
If a thread of the given ID is not alive or does not exist,

null

will be set in the corresponding element
in the returned array. A thread is alive if
it has been started and has not yet died.

If a thread does not lock any object monitor or

lockedMonitors

is

false

, the returned

ThreadInfo

object will have an
empty

MonitorInfo

array. Similarly, if a thread does not
lock any synchronizer or

lockedSynchronizers

is

false

,
the returned

ThreadInfo

object
will have an empty

LockInfo

array.

When both

lockedMonitors

and

lockedSynchronizers

parameters are

false

, it is equivalent to calling:

```java
getThreadInfo(ids, maxDepth)
```

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

.
**Parameters:** ids

- an array of thread IDs.
**Parameters:** lockedMonitors

- if

true

, retrieves all locked monitors.
**Parameters:** lockedSynchronizers

- if

true

, retrieves all locked
ownable synchronizers.
**Parameters:** maxDepth

- indicates the maximum number of

StackTraceElement

to be retrieved from the stack trace.
**Returns:** an array of the

ThreadInfo

objects, each containing
information about a thread whose ID is in the corresponding
element of the input array of IDs.
**Throws:** IllegalArgumentException

- if

maxDepth

is negative.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
**Throws:** UnsupportedOperationException

-

- if

lockedMonitors

is

true

but
the Java virtual machine does not support monitoring
of

object monitor usage

; or
- if

lockedSynchronizers

is

true

but
the Java virtual machine does not support monitoring
of

ownable synchronizer usage

.
**Since:** 10
**See Also:** isObjectMonitorUsageSupported()

,

isSynchronizerUsageSupported()

---

#### getThreadInfo

default

ThreadInfo

[] getThreadInfo​(long[] ids,
boolean lockedMonitors,
boolean lockedSynchronizers,
int maxDepth)

Returns the thread info for each thread whose ID
is in the input array

ids

,
with stack trace of the specified maximum number of elements
and synchronization information.
If

maxDepth == 0

, no stack trace of the thread
will be dumped.

This method obtains a snapshot of the thread information
for each thread including:

- stack trace of the specified maximum number of elements,
- the object monitors currently locked by the thread
if

lockedMonitors

is

true

, and
- the

ownable synchronizers

currently locked by the thread
if

lockedSynchronizers

is

true

.

This method returns an array of the

ThreadInfo

objects,
each is the thread information about the thread with the same index
as in the

ids

array.
If a thread of the given ID is not alive or does not exist,

null

will be set in the corresponding element
in the returned array. A thread is alive if
it has been started and has not yet died.

If a thread does not lock any object monitor or

lockedMonitors

is

false

, the returned

ThreadInfo

object will have an
empty

MonitorInfo

array. Similarly, if a thread does not
lock any synchronizer or

lockedSynchronizers

is

false

,
the returned

ThreadInfo

object
will have an empty

LockInfo

array.

When both

lockedMonitors

and

lockedSynchronizers

parameters are

false

, it is equivalent to calling:

```java
getThreadInfo(ids, maxDepth)
```

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

This method obtains a snapshot of the thread information
for each thread including:

- stack trace of the specified maximum number of elements,
- the object monitors currently locked by the thread
if

lockedMonitors

is

true

, and
- the

ownable synchronizers

currently locked by the thread
if

lockedSynchronizers

is

true

.

This method returns an array of the

ThreadInfo

objects,
each is the thread information about the thread with the same index
as in the

ids

array.
If a thread of the given ID is not alive or does not exist,

null

will be set in the corresponding element
in the returned array. A thread is alive if
it has been started and has not yet died.

If a thread does not lock any object monitor or

lockedMonitors

is

false

, the returned

ThreadInfo

object will have an
empty

MonitorInfo

array. Similarly, if a thread does not
lock any synchronizer or

lockedSynchronizers

is

false

,
the returned

ThreadInfo

object
will have an empty

LockInfo

array.

When both

lockedMonitors

and

lockedSynchronizers

parameters are

false

, it is equivalent to calling:

```java
getThreadInfo(ids, maxDepth)
```

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

stack trace of the specified maximum number of elements,

the object monitors currently locked by the thread
if

lockedMonitors

is

true

, and

the

ownable synchronizers

currently locked by the thread
if

lockedSynchronizers

is

true

.

This method returns an array of the

ThreadInfo

objects,
each is the thread information about the thread with the same index
as in the

ids

array.
If a thread of the given ID is not alive or does not exist,

null

will be set in the corresponding element
in the returned array. A thread is alive if
it has been started and has not yet died.

If a thread does not lock any object monitor or

lockedMonitors

is

false

, the returned

ThreadInfo

object will have an
empty

MonitorInfo

array. Similarly, if a thread does not
lock any synchronizer or

lockedSynchronizers

is

false

,
the returned

ThreadInfo

object
will have an empty

LockInfo

array.

When both

lockedMonitors

and

lockedSynchronizers

parameters are

false

, it is equivalent to calling:

```java
getThreadInfo(ids, maxDepth)
```

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

If a thread does not lock any object monitor or

lockedMonitors

is

false

, the returned

ThreadInfo

object will have an
empty

MonitorInfo

array. Similarly, if a thread does not
lock any synchronizer or

lockedSynchronizers

is

false

,
the returned

ThreadInfo

object
will have an empty

LockInfo

array.

When both

lockedMonitors

and

lockedSynchronizers

parameters are

false

, it is equivalent to calling:

```java
getThreadInfo(ids, maxDepth)
```

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

When both

lockedMonitors

and

lockedSynchronizers

parameters are

false

, it is equivalent to calling:

```java
getThreadInfo(ids, maxDepth)
```

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

getThreadInfo(ids, maxDepth)

This method is designed for troubleshooting use, but not for
synchronization control. It might be an expensive operation.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

MBeanServer access

:

The mapped type of

ThreadInfo

is

CompositeData

with attributes as specified in the

ThreadInfo.from

method.

if

lockedMonitors

is

true

but
the Java virtual machine does not support monitoring
of

object monitor usage

; or

if

lockedSynchronizers

is

true

but
the Java virtual machine does not support monitoring
of

ownable synchronizer usage

.

dumpAllThreads

```java
ThreadInfo
[] dumpAllThreads​(boolean lockedMonitors,
boolean lockedSynchronizers)
```

Returns the thread info for all live threads with stack trace
and synchronization information.
This is equivalent to calling:

dumpAllThreads(lockedMonitors, lockedSynchronizers, Integer.MAX_VALUE)

**Parameters:** lockedMonitors

- if

true

, dump all locked monitors.
**Parameters:** lockedSynchronizers

- if

true

, dump all locked
ownable synchronizers.
**Returns:** an array of

ThreadInfo

for all live threads.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
**Throws:** UnsupportedOperationException

-

- if

lockedMonitors

is

true

but
the Java virtual machine does not support monitoring
of

object monitor usage

; or
- if

lockedSynchronizers

is

true

but
the Java virtual machine does not support monitoring
of

ownable synchronizer usage

.
**Since:** 1.6
**See Also:** isObjectMonitorUsageSupported()

,

isSynchronizerUsageSupported()

---

#### dumpAllThreads

ThreadInfo

[] dumpAllThreads​(boolean lockedMonitors,
boolean lockedSynchronizers)

Returns the thread info for all live threads with stack trace
and synchronization information.
This is equivalent to calling:

dumpAllThreads(lockedMonitors, lockedSynchronizers, Integer.MAX_VALUE)

if

lockedMonitors

is

true

but
the Java virtual machine does not support monitoring
of

object monitor usage

; or

if

lockedSynchronizers

is

true

but
the Java virtual machine does not support monitoring
of

ownable synchronizer usage

.

dumpAllThreads

```java
default
ThreadInfo
[] dumpAllThreads​(boolean lockedMonitors,
boolean lockedSynchronizers,
int maxDepth)
```

Returns the thread info for all live threads
with stack trace of the specified maximum number of elements
and synchronization information.
if

maxDepth == 0

, no stack trace of the thread
will be dumped.
Some threads included in the returned array
may have been terminated when this method returns.

This method returns an array of

ThreadInfo

objects
as specified in the

getThreadInfo(long[], boolean, boolean, int)

method.

**Implementation Requirements:** The default implementation throws

UnsupportedOperationException

.
**Parameters:** lockedMonitors

- if

true

, dump all locked monitors.
**Parameters:** lockedSynchronizers

- if

true

, dump all locked
ownable synchronizers.
**Parameters:** maxDepth

- indicates the maximum number of

StackTraceElement

to be retrieved from the stack trace.
**Returns:** an array of

ThreadInfo

for all live threads.
**Throws:** IllegalArgumentException

- if

maxDepth

is negative.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("monitor").
**Throws:** UnsupportedOperationException

-

- if

lockedMonitors

is

true

but
the Java virtual machine does not support monitoring
of

object monitor usage

; or
- if

lockedSynchronizers

is

true

but
the Java virtual machine does not support monitoring
of

ownable synchronizer usage

.
**Since:** 10
**See Also:** isObjectMonitorUsageSupported()

,

isSynchronizerUsageSupported()

---

#### dumpAllThreads

default

ThreadInfo

[] dumpAllThreads​(boolean lockedMonitors,
boolean lockedSynchronizers,
int maxDepth)

Returns the thread info for all live threads
with stack trace of the specified maximum number of elements
and synchronization information.
if

maxDepth == 0

, no stack trace of the thread
will be dumped.
Some threads included in the returned array
may have been terminated when this method returns.

This method returns an array of

ThreadInfo

objects
as specified in the

getThreadInfo(long[], boolean, boolean, int)

method.

This method returns an array of

ThreadInfo

objects
as specified in the

getThreadInfo(long[], boolean, boolean, int)

method.

if

lockedMonitors

is

true

but
the Java virtual machine does not support monitoring
of

object monitor usage

; or

if

lockedSynchronizers

is

true

but
the Java virtual machine does not support monitoring
of

ownable synchronizer usage

.

---

