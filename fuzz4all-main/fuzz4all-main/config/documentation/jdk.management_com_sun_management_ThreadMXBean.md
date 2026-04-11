# Interface ThreadMXBean

**Source:** `jdk.management\com\sun\management\ThreadMXBean.html`

### Class Description

```java
public interface
ThreadMXBean

extends
ThreadMXBean
```

Platform-specific management interface for the thread system
of the Java virtual machine.

This platform extension is only available to a thread
implementation that supports this extension.

**All Superinterfaces:** PlatformManagedObject

,

ThreadMXBean

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### long[] getThreadCpuTime​(long[] ids)

Returns the total CPU time for each thread whose ID is
in the input array

ids

in nanoseconds.
The returned values are of nanoseconds precision but
not necessarily nanoseconds accuracy.

This method is equivalent to calling the

ThreadMXBean.getThreadCpuTime(long)

method for each thread ID in the input array

ids

and setting the
returned value in the corresponding element of the returned array.

**Parameters:**
- ids

- an array of thread IDs.

**Returns:**
- an array of long values, each of which is the amount of CPU
time the thread whose ID is in the corresponding element of the input
array of IDs has used,
if the thread of a specified ID exists, the thread is alive,
and CPU time measurement is enabled;

-1

otherwise.

**Throws:**
- NullPointerException

- if

ids

is

null
- IllegalArgumentException

- if any element in the input array

ids

is

<=

0

.
- UnsupportedOperationException

- if the Java
virtual machine implementation does not support CPU time
measurement.

**See Also:**
- ThreadMXBean.getThreadCpuTime(long)

,

getThreadUserTime(long[])

,

ThreadMXBean.isThreadCpuTimeSupported()

,

ThreadMXBean.isThreadCpuTimeEnabled()

,

ThreadMXBean.setThreadCpuTimeEnabled(boolean)

---

#### long[] getThreadUserTime​(long[] ids)

Returns the CPU time that each thread whose ID is in the input array

ids

has executed in user mode in nanoseconds.
The returned values are of nanoseconds precision but
not necessarily nanoseconds accuracy.

This method is equivalent to calling the

ThreadMXBean.getThreadUserTime(long)

method for each thread ID in the input array

ids

and setting the
returned value in the corresponding element of the returned array.

**Parameters:**
- ids

- an array of thread IDs.

**Returns:**
- an array of long values, each of which is the amount of user
mode CPU time the thread whose ID is in the corresponding element of
the input array of IDs has used,
if the thread of a specified ID exists, the thread is alive,
and CPU time measurement is enabled;

-1

otherwise.

**Throws:**
- NullPointerException

- if

ids

is

null
- IllegalArgumentException

- if any element in the input array

ids

is

<=

0

.
- UnsupportedOperationException

- if the Java
virtual machine implementation does not support CPU time
measurement.

**See Also:**
- ThreadMXBean.getThreadUserTime(long)

,

getThreadCpuTime(long[])

,

ThreadMXBean.isThreadCpuTimeSupported()

,

ThreadMXBean.isThreadCpuTimeEnabled()

,

ThreadMXBean.setThreadCpuTimeEnabled(boolean)

---

#### default long getCurrentThreadAllocatedBytes()

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for the current thread.
The returned value is an approximation because some Java virtual machine
implementations may use object allocation mechanisms that result in a
delay between the time an object is allocated and the time its size is
recorded.

This is a convenience method for local management use and is
equivalent to calling:

```java
getThreadAllocatedBytes
(Thread.currentThread().getId());
```

**Returns:**
- an approximation of the total memory allocated, in bytes, in
heap memory for the current thread
if thread memory allocation measurement is enabled;

-1

otherwise.

**Throws:**
- UnsupportedOperationException

- if the Java virtual
machine implementation does not support thread memory allocation
measurement.

**See Also:**
- isThreadAllocatedMemorySupported()

,

isThreadAllocatedMemoryEnabled()

,

setThreadAllocatedMemoryEnabled(boolean)

**Since:**
- 11.0.10

---

#### long getThreadAllocatedBytes​(long id)

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for the thread with the specified ID.
The returned value is an approximation because some Java virtual machine
implementations may use object allocation mechanisms that result in a
delay between the time an object is allocated and the time its size is
recorded.

If the thread with the specified ID is not alive or does not exist,
this method returns

-1

. If thread memory allocation measurement
is disabled, this method returns

-1

.
A thread is alive if it has been started and has not yet died.

If thread memory allocation measurement is enabled after the thread has
started, the Java virtual machine implementation may choose any time up
to and including the time that the capability is enabled as the point
where thread memory allocation measurement starts.

**Parameters:**
- id

- the thread ID of a thread

**Returns:**
- an approximation of the total memory allocated, in bytes, in
heap memory for the thread with the specified ID
if the thread with the specified ID exists, the thread is alive,
and thread memory allocation measurement is enabled;

-1

otherwise.

**Throws:**
- IllegalArgumentException

- if

id

<=

0

.
- UnsupportedOperationException

- if the Java virtual
machine implementation does not support thread memory allocation
measurement.

**See Also:**
- isThreadAllocatedMemorySupported()

,

isThreadAllocatedMemoryEnabled()

,

setThreadAllocatedMemoryEnabled(boolean)

---

#### long[] getThreadAllocatedBytes​(long[] ids)

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for each thread whose ID is in the input
array

ids

.
The returned values are approximations because some Java virtual machine
implementations may use object allocation mechanisms that result in a
delay between the time an object is allocated and the time its size is
recorded.

This method is equivalent to calling the

getThreadAllocatedBytes(long)

method for each thread ID in the input array

ids

and setting the
returned value in the corresponding element of the returned array.

**Parameters:**
- ids

- an array of thread IDs.

**Returns:**
- an array of long values, each of which is an approximation of
the total memory allocated, in bytes, in heap memory for the thread
whose ID is in the corresponding element of the input array of IDs.

**Throws:**
- NullPointerException

- if

ids

is

null
- IllegalArgumentException

- if any element in the input array

ids

is

<=

0

.
- UnsupportedOperationException

- if the Java virtual
machine implementation does not support thread memory allocation
measurement.

**See Also:**
- getThreadAllocatedBytes(long)

,

isThreadAllocatedMemorySupported()

,

isThreadAllocatedMemoryEnabled()

,

setThreadAllocatedMemoryEnabled(boolean)

---

#### boolean isThreadAllocatedMemorySupported()

Tests if the Java virtual machine implementation supports thread memory
allocation measurement.

**Returns:**
- true

if the Java virtual machine implementation supports thread memory
allocation measurement;

false

otherwise.

---

#### boolean isThreadAllocatedMemoryEnabled()

Tests if thread memory allocation measurement is enabled.

**Returns:**
- true

if thread memory allocation measurement is enabled;

false

otherwise.

**Throws:**
- UnsupportedOperationException

- if the Java virtual
machine does not support thread memory allocation measurement.

**See Also:**
- isThreadAllocatedMemorySupported()

---

#### void setThreadAllocatedMemoryEnabled​(boolean enable)

Enables or disables thread memory allocation measurement. The default
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

- if the Java virtual
machine does not support thread memory allocation measurement.
- SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("control").

**See Also:**
- isThreadAllocatedMemorySupported()

---

### Additional Sections

#### Interface ThreadMXBean

**All Superinterfaces:** PlatformManagedObject

,

ThreadMXBean

```java
public interface
ThreadMXBean

extends
ThreadMXBean
```

Platform-specific management interface for the thread system
of the Java virtual machine.

This platform extension is only available to a thread
implementation that supports this extension.

**Since:** 6u25

public interface

ThreadMXBean

extends

ThreadMXBean

Platform-specific management interface for the thread system
of the Java virtual machine.

This platform extension is only available to a thread
implementation that supports this extension.

This platform extension is only available to a thread
implementation that supports this extension.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default long

getCurrentThreadAllocatedBytes

()

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for the current thread.

long

getThreadAllocatedBytes

​(long id)

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for the thread with the specified ID.

long[]

getThreadAllocatedBytes

​(long[] ids)

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for each thread whose ID is in the input
array

ids

.

long[]

getThreadCpuTime

​(long[] ids)

Returns the total CPU time for each thread whose ID is
in the input array

ids

in nanoseconds.

long[]

getThreadUserTime

​(long[] ids)

Returns the CPU time that each thread whose ID is in the input array

ids

has executed in user mode in nanoseconds.

boolean

isThreadAllocatedMemoryEnabled

()

Tests if thread memory allocation measurement is enabled.

boolean

isThreadAllocatedMemorySupported

()

Tests if the Java virtual machine implementation supports thread memory
allocation measurement.

void

setThreadAllocatedMemoryEnabled

​(boolean enable)

Enables or disables thread memory allocation measurement.

- Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

- Methods declared in interface java.lang.management.

ThreadMXBean

dumpAllThreads

,

dumpAllThreads

,

findDeadlockedThreads

,

findMonitorDeadlockedThreads

,

getAllThreadIds

,

getCurrentThreadCpuTime

,

getCurrentThreadUserTime

,

getDaemonThreadCount

,

getPeakThreadCount

,

getThreadCount

,

getThreadCpuTime

,

getThreadInfo

,

getThreadInfo

,

getThreadInfo

,

getThreadInfo

,

getThreadInfo

,

getThreadInfo

,

getThreadUserTime

,

getTotalStartedThreadCount

,

isCurrentThreadCpuTimeSupported

,

isObjectMonitorUsageSupported

,

isSynchronizerUsageSupported

,

isThreadContentionMonitoringEnabled

,

isThreadContentionMonitoringSupported

,

isThreadCpuTimeEnabled

,

isThreadCpuTimeSupported

,

resetPeakThreadCount

,

setThreadContentionMonitoringEnabled

,

setThreadCpuTimeEnabled

Method Summary

All Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

default long

getCurrentThreadAllocatedBytes

()

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for the current thread.

long

getThreadAllocatedBytes

​(long id)

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for the thread with the specified ID.

long[]

getThreadAllocatedBytes

​(long[] ids)

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for each thread whose ID is in the input
array

ids

.

long[]

getThreadCpuTime

​(long[] ids)

Returns the total CPU time for each thread whose ID is
in the input array

ids

in nanoseconds.

long[]

getThreadUserTime

​(long[] ids)

Returns the CPU time that each thread whose ID is in the input array

ids

has executed in user mode in nanoseconds.

boolean

isThreadAllocatedMemoryEnabled

()

Tests if thread memory allocation measurement is enabled.

boolean

isThreadAllocatedMemorySupported

()

Tests if the Java virtual machine implementation supports thread memory
allocation measurement.

void

setThreadAllocatedMemoryEnabled

​(boolean enable)

Enables or disables thread memory allocation measurement.

- Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

- Methods declared in interface java.lang.management.

ThreadMXBean

dumpAllThreads

,

dumpAllThreads

,

findDeadlockedThreads

,

findMonitorDeadlockedThreads

,

getAllThreadIds

,

getCurrentThreadCpuTime

,

getCurrentThreadUserTime

,

getDaemonThreadCount

,

getPeakThreadCount

,

getThreadCount

,

getThreadCpuTime

,

getThreadInfo

,

getThreadInfo

,

getThreadInfo

,

getThreadInfo

,

getThreadInfo

,

getThreadInfo

,

getThreadUserTime

,

getTotalStartedThreadCount

,

isCurrentThreadCpuTimeSupported

,

isObjectMonitorUsageSupported

,

isSynchronizerUsageSupported

,

isThreadContentionMonitoringEnabled

,

isThreadContentionMonitoringSupported

,

isThreadCpuTimeEnabled

,

isThreadCpuTimeSupported

,

resetPeakThreadCount

,

setThreadContentionMonitoringEnabled

,

setThreadCpuTimeEnabled

---

#### Method Summary

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for the current thread.

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for the thread with the specified ID.

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for each thread whose ID is in the input
array

ids

.

Returns the total CPU time for each thread whose ID is
in the input array

ids

in nanoseconds.

Returns the CPU time that each thread whose ID is in the input array

ids

has executed in user mode in nanoseconds.

Tests if thread memory allocation measurement is enabled.

Tests if the Java virtual machine implementation supports thread memory
allocation measurement.

Enables or disables thread memory allocation measurement.

Methods declared in interface java.lang.management.

PlatformManagedObject

getObjectName

---

#### Methods declared in interface java.lang.management. PlatformManagedObject

Methods declared in interface java.lang.management.

ThreadMXBean

dumpAllThreads

,

dumpAllThreads

,

findDeadlockedThreads

,

findMonitorDeadlockedThreads

,

getAllThreadIds

,

getCurrentThreadCpuTime

,

getCurrentThreadUserTime

,

getDaemonThreadCount

,

getPeakThreadCount

,

getThreadCount

,

getThreadCpuTime

,

getThreadInfo

,

getThreadInfo

,

getThreadInfo

,

getThreadInfo

,

getThreadInfo

,

getThreadInfo

,

getThreadUserTime

,

getTotalStartedThreadCount

,

isCurrentThreadCpuTimeSupported

,

isObjectMonitorUsageSupported

,

isSynchronizerUsageSupported

,

isThreadContentionMonitoringEnabled

,

isThreadContentionMonitoringSupported

,

isThreadCpuTimeEnabled

,

isThreadCpuTimeSupported

,

resetPeakThreadCount

,

setThreadContentionMonitoringEnabled

,

setThreadCpuTimeEnabled

---

#### Methods declared in interface java.lang.management. ThreadMXBean

============ METHOD DETAIL ==========

- Method Detail

- getThreadCpuTime

```java
long[] getThreadCpuTime​(long[] ids)
```

Returns the total CPU time for each thread whose ID is
in the input array

ids

in nanoseconds.
The returned values are of nanoseconds precision but
not necessarily nanoseconds accuracy.

This method is equivalent to calling the

ThreadMXBean.getThreadCpuTime(long)

method for each thread ID in the input array

ids

and setting the
returned value in the corresponding element of the returned array.

**Parameters:** ids

- an array of thread IDs.
**Returns:** an array of long values, each of which is the amount of CPU
time the thread whose ID is in the corresponding element of the input
array of IDs has used,
if the thread of a specified ID exists, the thread is alive,
and CPU time measurement is enabled;

-1

otherwise.
**Throws:** NullPointerException

- if

ids

is

null
**Throws:** IllegalArgumentException

- if any element in the input array

ids

is

<=

0

.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine implementation does not support CPU time
measurement.
**See Also:** ThreadMXBean.getThreadCpuTime(long)

,

getThreadUserTime(long[])

,

ThreadMXBean.isThreadCpuTimeSupported()

,

ThreadMXBean.isThreadCpuTimeEnabled()

,

ThreadMXBean.setThreadCpuTimeEnabled(boolean)

- getThreadUserTime

```java
long[] getThreadUserTime​(long[] ids)
```

Returns the CPU time that each thread whose ID is in the input array

ids

has executed in user mode in nanoseconds.
The returned values are of nanoseconds precision but
not necessarily nanoseconds accuracy.

This method is equivalent to calling the

ThreadMXBean.getThreadUserTime(long)

method for each thread ID in the input array

ids

and setting the
returned value in the corresponding element of the returned array.

**Parameters:** ids

- an array of thread IDs.
**Returns:** an array of long values, each of which is the amount of user
mode CPU time the thread whose ID is in the corresponding element of
the input array of IDs has used,
if the thread of a specified ID exists, the thread is alive,
and CPU time measurement is enabled;

-1

otherwise.
**Throws:** NullPointerException

- if

ids

is

null
**Throws:** IllegalArgumentException

- if any element in the input array

ids

is

<=

0

.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine implementation does not support CPU time
measurement.
**See Also:** ThreadMXBean.getThreadUserTime(long)

,

getThreadCpuTime(long[])

,

ThreadMXBean.isThreadCpuTimeSupported()

,

ThreadMXBean.isThreadCpuTimeEnabled()

,

ThreadMXBean.setThreadCpuTimeEnabled(boolean)

- getCurrentThreadAllocatedBytes

```java
default long getCurrentThreadAllocatedBytes()
```

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for the current thread.
The returned value is an approximation because some Java virtual machine
implementations may use object allocation mechanisms that result in a
delay between the time an object is allocated and the time its size is
recorded.

This is a convenience method for local management use and is
equivalent to calling:

```java
getThreadAllocatedBytes
(Thread.currentThread().getId());
```

**Returns:** an approximation of the total memory allocated, in bytes, in
heap memory for the current thread
if thread memory allocation measurement is enabled;

-1

otherwise.
**Throws:** UnsupportedOperationException

- if the Java virtual
machine implementation does not support thread memory allocation
measurement.
**Since:** 11.0.10
**See Also:** isThreadAllocatedMemorySupported()

,

isThreadAllocatedMemoryEnabled()

,

setThreadAllocatedMemoryEnabled(boolean)

- getThreadAllocatedBytes

```java
long getThreadAllocatedBytes​(long id)
```

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for the thread with the specified ID.
The returned value is an approximation because some Java virtual machine
implementations may use object allocation mechanisms that result in a
delay between the time an object is allocated and the time its size is
recorded.

If the thread with the specified ID is not alive or does not exist,
this method returns

-1

. If thread memory allocation measurement
is disabled, this method returns

-1

.
A thread is alive if it has been started and has not yet died.

If thread memory allocation measurement is enabled after the thread has
started, the Java virtual machine implementation may choose any time up
to and including the time that the capability is enabled as the point
where thread memory allocation measurement starts.

**Parameters:** id

- the thread ID of a thread
**Returns:** an approximation of the total memory allocated, in bytes, in
heap memory for the thread with the specified ID
if the thread with the specified ID exists, the thread is alive,
and thread memory allocation measurement is enabled;

-1

otherwise.
**Throws:** IllegalArgumentException

- if

id

<=

0

.
**Throws:** UnsupportedOperationException

- if the Java virtual
machine implementation does not support thread memory allocation
measurement.
**See Also:** isThreadAllocatedMemorySupported()

,

isThreadAllocatedMemoryEnabled()

,

setThreadAllocatedMemoryEnabled(boolean)

- getThreadAllocatedBytes

```java
long[] getThreadAllocatedBytes​(long[] ids)
```

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for each thread whose ID is in the input
array

ids

.
The returned values are approximations because some Java virtual machine
implementations may use object allocation mechanisms that result in a
delay between the time an object is allocated and the time its size is
recorded.

This method is equivalent to calling the

getThreadAllocatedBytes(long)

method for each thread ID in the input array

ids

and setting the
returned value in the corresponding element of the returned array.

**Parameters:** ids

- an array of thread IDs.
**Returns:** an array of long values, each of which is an approximation of
the total memory allocated, in bytes, in heap memory for the thread
whose ID is in the corresponding element of the input array of IDs.
**Throws:** NullPointerException

- if

ids

is

null
**Throws:** IllegalArgumentException

- if any element in the input array

ids

is

<=

0

.
**Throws:** UnsupportedOperationException

- if the Java virtual
machine implementation does not support thread memory allocation
measurement.
**See Also:** getThreadAllocatedBytes(long)

,

isThreadAllocatedMemorySupported()

,

isThreadAllocatedMemoryEnabled()

,

setThreadAllocatedMemoryEnabled(boolean)

- isThreadAllocatedMemorySupported

```java
boolean isThreadAllocatedMemorySupported()
```

Tests if the Java virtual machine implementation supports thread memory
allocation measurement.

**Returns:** true

if the Java virtual machine implementation supports thread memory
allocation measurement;

false

otherwise.

- isThreadAllocatedMemoryEnabled

```java
boolean isThreadAllocatedMemoryEnabled()
```

Tests if thread memory allocation measurement is enabled.

**Returns:** true

if thread memory allocation measurement is enabled;

false

otherwise.
**Throws:** UnsupportedOperationException

- if the Java virtual
machine does not support thread memory allocation measurement.
**See Also:** isThreadAllocatedMemorySupported()

- setThreadAllocatedMemoryEnabled

```java
void setThreadAllocatedMemoryEnabled​(boolean enable)
```

Enables or disables thread memory allocation measurement. The default
is platform dependent.

**Parameters:** enable

-

true

to enable;

false

to disable.
**Throws:** UnsupportedOperationException

- if the Java virtual
machine does not support thread memory allocation measurement.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("control").
**See Also:** isThreadAllocatedMemorySupported()

Method Detail

- getThreadCpuTime

```java
long[] getThreadCpuTime​(long[] ids)
```

Returns the total CPU time for each thread whose ID is
in the input array

ids

in nanoseconds.
The returned values are of nanoseconds precision but
not necessarily nanoseconds accuracy.

This method is equivalent to calling the

ThreadMXBean.getThreadCpuTime(long)

method for each thread ID in the input array

ids

and setting the
returned value in the corresponding element of the returned array.

**Parameters:** ids

- an array of thread IDs.
**Returns:** an array of long values, each of which is the amount of CPU
time the thread whose ID is in the corresponding element of the input
array of IDs has used,
if the thread of a specified ID exists, the thread is alive,
and CPU time measurement is enabled;

-1

otherwise.
**Throws:** NullPointerException

- if

ids

is

null
**Throws:** IllegalArgumentException

- if any element in the input array

ids

is

<=

0

.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine implementation does not support CPU time
measurement.
**See Also:** ThreadMXBean.getThreadCpuTime(long)

,

getThreadUserTime(long[])

,

ThreadMXBean.isThreadCpuTimeSupported()

,

ThreadMXBean.isThreadCpuTimeEnabled()

,

ThreadMXBean.setThreadCpuTimeEnabled(boolean)

- getThreadUserTime

```java
long[] getThreadUserTime​(long[] ids)
```

Returns the CPU time that each thread whose ID is in the input array

ids

has executed in user mode in nanoseconds.
The returned values are of nanoseconds precision but
not necessarily nanoseconds accuracy.

This method is equivalent to calling the

ThreadMXBean.getThreadUserTime(long)

method for each thread ID in the input array

ids

and setting the
returned value in the corresponding element of the returned array.

**Parameters:** ids

- an array of thread IDs.
**Returns:** an array of long values, each of which is the amount of user
mode CPU time the thread whose ID is in the corresponding element of
the input array of IDs has used,
if the thread of a specified ID exists, the thread is alive,
and CPU time measurement is enabled;

-1

otherwise.
**Throws:** NullPointerException

- if

ids

is

null
**Throws:** IllegalArgumentException

- if any element in the input array

ids

is

<=

0

.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine implementation does not support CPU time
measurement.
**See Also:** ThreadMXBean.getThreadUserTime(long)

,

getThreadCpuTime(long[])

,

ThreadMXBean.isThreadCpuTimeSupported()

,

ThreadMXBean.isThreadCpuTimeEnabled()

,

ThreadMXBean.setThreadCpuTimeEnabled(boolean)

- getCurrentThreadAllocatedBytes

```java
default long getCurrentThreadAllocatedBytes()
```

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for the current thread.
The returned value is an approximation because some Java virtual machine
implementations may use object allocation mechanisms that result in a
delay between the time an object is allocated and the time its size is
recorded.

This is a convenience method for local management use and is
equivalent to calling:

```java
getThreadAllocatedBytes
(Thread.currentThread().getId());
```

**Returns:** an approximation of the total memory allocated, in bytes, in
heap memory for the current thread
if thread memory allocation measurement is enabled;

-1

otherwise.
**Throws:** UnsupportedOperationException

- if the Java virtual
machine implementation does not support thread memory allocation
measurement.
**Since:** 11.0.10
**See Also:** isThreadAllocatedMemorySupported()

,

isThreadAllocatedMemoryEnabled()

,

setThreadAllocatedMemoryEnabled(boolean)

- getThreadAllocatedBytes

```java
long getThreadAllocatedBytes​(long id)
```

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for the thread with the specified ID.
The returned value is an approximation because some Java virtual machine
implementations may use object allocation mechanisms that result in a
delay between the time an object is allocated and the time its size is
recorded.

If the thread with the specified ID is not alive or does not exist,
this method returns

-1

. If thread memory allocation measurement
is disabled, this method returns

-1

.
A thread is alive if it has been started and has not yet died.

If thread memory allocation measurement is enabled after the thread has
started, the Java virtual machine implementation may choose any time up
to and including the time that the capability is enabled as the point
where thread memory allocation measurement starts.

**Parameters:** id

- the thread ID of a thread
**Returns:** an approximation of the total memory allocated, in bytes, in
heap memory for the thread with the specified ID
if the thread with the specified ID exists, the thread is alive,
and thread memory allocation measurement is enabled;

-1

otherwise.
**Throws:** IllegalArgumentException

- if

id

<=

0

.
**Throws:** UnsupportedOperationException

- if the Java virtual
machine implementation does not support thread memory allocation
measurement.
**See Also:** isThreadAllocatedMemorySupported()

,

isThreadAllocatedMemoryEnabled()

,

setThreadAllocatedMemoryEnabled(boolean)

- getThreadAllocatedBytes

```java
long[] getThreadAllocatedBytes​(long[] ids)
```

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for each thread whose ID is in the input
array

ids

.
The returned values are approximations because some Java virtual machine
implementations may use object allocation mechanisms that result in a
delay between the time an object is allocated and the time its size is
recorded.

This method is equivalent to calling the

getThreadAllocatedBytes(long)

method for each thread ID in the input array

ids

and setting the
returned value in the corresponding element of the returned array.

**Parameters:** ids

- an array of thread IDs.
**Returns:** an array of long values, each of which is an approximation of
the total memory allocated, in bytes, in heap memory for the thread
whose ID is in the corresponding element of the input array of IDs.
**Throws:** NullPointerException

- if

ids

is

null
**Throws:** IllegalArgumentException

- if any element in the input array

ids

is

<=

0

.
**Throws:** UnsupportedOperationException

- if the Java virtual
machine implementation does not support thread memory allocation
measurement.
**See Also:** getThreadAllocatedBytes(long)

,

isThreadAllocatedMemorySupported()

,

isThreadAllocatedMemoryEnabled()

,

setThreadAllocatedMemoryEnabled(boolean)

- isThreadAllocatedMemorySupported

```java
boolean isThreadAllocatedMemorySupported()
```

Tests if the Java virtual machine implementation supports thread memory
allocation measurement.

**Returns:** true

if the Java virtual machine implementation supports thread memory
allocation measurement;

false

otherwise.

- isThreadAllocatedMemoryEnabled

```java
boolean isThreadAllocatedMemoryEnabled()
```

Tests if thread memory allocation measurement is enabled.

**Returns:** true

if thread memory allocation measurement is enabled;

false

otherwise.
**Throws:** UnsupportedOperationException

- if the Java virtual
machine does not support thread memory allocation measurement.
**See Also:** isThreadAllocatedMemorySupported()

- setThreadAllocatedMemoryEnabled

```java
void setThreadAllocatedMemoryEnabled​(boolean enable)
```

Enables or disables thread memory allocation measurement. The default
is platform dependent.

**Parameters:** enable

-

true

to enable;

false

to disable.
**Throws:** UnsupportedOperationException

- if the Java virtual
machine does not support thread memory allocation measurement.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("control").
**See Also:** isThreadAllocatedMemorySupported()

---

#### Method Detail

getThreadCpuTime

```java
long[] getThreadCpuTime​(long[] ids)
```

Returns the total CPU time for each thread whose ID is
in the input array

ids

in nanoseconds.
The returned values are of nanoseconds precision but
not necessarily nanoseconds accuracy.

This method is equivalent to calling the

ThreadMXBean.getThreadCpuTime(long)

method for each thread ID in the input array

ids

and setting the
returned value in the corresponding element of the returned array.

**Parameters:** ids

- an array of thread IDs.
**Returns:** an array of long values, each of which is the amount of CPU
time the thread whose ID is in the corresponding element of the input
array of IDs has used,
if the thread of a specified ID exists, the thread is alive,
and CPU time measurement is enabled;

-1

otherwise.
**Throws:** NullPointerException

- if

ids

is

null
**Throws:** IllegalArgumentException

- if any element in the input array

ids

is

<=

0

.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine implementation does not support CPU time
measurement.
**See Also:** ThreadMXBean.getThreadCpuTime(long)

,

getThreadUserTime(long[])

,

ThreadMXBean.isThreadCpuTimeSupported()

,

ThreadMXBean.isThreadCpuTimeEnabled()

,

ThreadMXBean.setThreadCpuTimeEnabled(boolean)

---

#### getThreadCpuTime

long[] getThreadCpuTime​(long[] ids)

Returns the total CPU time for each thread whose ID is
in the input array

ids

in nanoseconds.
The returned values are of nanoseconds precision but
not necessarily nanoseconds accuracy.

This method is equivalent to calling the

ThreadMXBean.getThreadCpuTime(long)

method for each thread ID in the input array

ids

and setting the
returned value in the corresponding element of the returned array.

This method is equivalent to calling the

ThreadMXBean.getThreadCpuTime(long)

method for each thread ID in the input array

ids

and setting the
returned value in the corresponding element of the returned array.

getThreadUserTime

```java
long[] getThreadUserTime​(long[] ids)
```

Returns the CPU time that each thread whose ID is in the input array

ids

has executed in user mode in nanoseconds.
The returned values are of nanoseconds precision but
not necessarily nanoseconds accuracy.

This method is equivalent to calling the

ThreadMXBean.getThreadUserTime(long)

method for each thread ID in the input array

ids

and setting the
returned value in the corresponding element of the returned array.

**Parameters:** ids

- an array of thread IDs.
**Returns:** an array of long values, each of which is the amount of user
mode CPU time the thread whose ID is in the corresponding element of
the input array of IDs has used,
if the thread of a specified ID exists, the thread is alive,
and CPU time measurement is enabled;

-1

otherwise.
**Throws:** NullPointerException

- if

ids

is

null
**Throws:** IllegalArgumentException

- if any element in the input array

ids

is

<=

0

.
**Throws:** UnsupportedOperationException

- if the Java
virtual machine implementation does not support CPU time
measurement.
**See Also:** ThreadMXBean.getThreadUserTime(long)

,

getThreadCpuTime(long[])

,

ThreadMXBean.isThreadCpuTimeSupported()

,

ThreadMXBean.isThreadCpuTimeEnabled()

,

ThreadMXBean.setThreadCpuTimeEnabled(boolean)

---

#### getThreadUserTime

long[] getThreadUserTime​(long[] ids)

Returns the CPU time that each thread whose ID is in the input array

ids

has executed in user mode in nanoseconds.
The returned values are of nanoseconds precision but
not necessarily nanoseconds accuracy.

This method is equivalent to calling the

ThreadMXBean.getThreadUserTime(long)

method for each thread ID in the input array

ids

and setting the
returned value in the corresponding element of the returned array.

This method is equivalent to calling the

ThreadMXBean.getThreadUserTime(long)

method for each thread ID in the input array

ids

and setting the
returned value in the corresponding element of the returned array.

getCurrentThreadAllocatedBytes

```java
default long getCurrentThreadAllocatedBytes()
```

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for the current thread.
The returned value is an approximation because some Java virtual machine
implementations may use object allocation mechanisms that result in a
delay between the time an object is allocated and the time its size is
recorded.

This is a convenience method for local management use and is
equivalent to calling:

```java
getThreadAllocatedBytes
(Thread.currentThread().getId());
```

**Returns:** an approximation of the total memory allocated, in bytes, in
heap memory for the current thread
if thread memory allocation measurement is enabled;

-1

otherwise.
**Throws:** UnsupportedOperationException

- if the Java virtual
machine implementation does not support thread memory allocation
measurement.
**Since:** 11.0.10
**See Also:** isThreadAllocatedMemorySupported()

,

isThreadAllocatedMemoryEnabled()

,

setThreadAllocatedMemoryEnabled(boolean)

---

#### getCurrentThreadAllocatedBytes

default long getCurrentThreadAllocatedBytes()

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for the current thread.
The returned value is an approximation because some Java virtual machine
implementations may use object allocation mechanisms that result in a
delay between the time an object is allocated and the time its size is
recorded.

This is a convenience method for local management use and is
equivalent to calling:

```java
getThreadAllocatedBytes
(Thread.currentThread().getId());
```

This is a convenience method for local management use and is
equivalent to calling:

```java
getThreadAllocatedBytes
(Thread.currentThread().getId());
```

getThreadAllocatedBytes

(Thread.currentThread().getId());

getThreadAllocatedBytes

```java
long getThreadAllocatedBytes​(long id)
```

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for the thread with the specified ID.
The returned value is an approximation because some Java virtual machine
implementations may use object allocation mechanisms that result in a
delay between the time an object is allocated and the time its size is
recorded.

If the thread with the specified ID is not alive or does not exist,
this method returns

-1

. If thread memory allocation measurement
is disabled, this method returns

-1

.
A thread is alive if it has been started and has not yet died.

If thread memory allocation measurement is enabled after the thread has
started, the Java virtual machine implementation may choose any time up
to and including the time that the capability is enabled as the point
where thread memory allocation measurement starts.

**Parameters:** id

- the thread ID of a thread
**Returns:** an approximation of the total memory allocated, in bytes, in
heap memory for the thread with the specified ID
if the thread with the specified ID exists, the thread is alive,
and thread memory allocation measurement is enabled;

-1

otherwise.
**Throws:** IllegalArgumentException

- if

id

<=

0

.
**Throws:** UnsupportedOperationException

- if the Java virtual
machine implementation does not support thread memory allocation
measurement.
**See Also:** isThreadAllocatedMemorySupported()

,

isThreadAllocatedMemoryEnabled()

,

setThreadAllocatedMemoryEnabled(boolean)

---

#### getThreadAllocatedBytes

long getThreadAllocatedBytes​(long id)

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for the thread with the specified ID.
The returned value is an approximation because some Java virtual machine
implementations may use object allocation mechanisms that result in a
delay between the time an object is allocated and the time its size is
recorded.

If the thread with the specified ID is not alive or does not exist,
this method returns

-1

. If thread memory allocation measurement
is disabled, this method returns

-1

.
A thread is alive if it has been started and has not yet died.

If thread memory allocation measurement is enabled after the thread has
started, the Java virtual machine implementation may choose any time up
to and including the time that the capability is enabled as the point
where thread memory allocation measurement starts.

If the thread with the specified ID is not alive or does not exist,
this method returns

-1

. If thread memory allocation measurement
is disabled, this method returns

-1

.
A thread is alive if it has been started and has not yet died.

If thread memory allocation measurement is enabled after the thread has
started, the Java virtual machine implementation may choose any time up
to and including the time that the capability is enabled as the point
where thread memory allocation measurement starts.

If thread memory allocation measurement is enabled after the thread has
started, the Java virtual machine implementation may choose any time up
to and including the time that the capability is enabled as the point
where thread memory allocation measurement starts.

getThreadAllocatedBytes

```java
long[] getThreadAllocatedBytes​(long[] ids)
```

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for each thread whose ID is in the input
array

ids

.
The returned values are approximations because some Java virtual machine
implementations may use object allocation mechanisms that result in a
delay between the time an object is allocated and the time its size is
recorded.

This method is equivalent to calling the

getThreadAllocatedBytes(long)

method for each thread ID in the input array

ids

and setting the
returned value in the corresponding element of the returned array.

**Parameters:** ids

- an array of thread IDs.
**Returns:** an array of long values, each of which is an approximation of
the total memory allocated, in bytes, in heap memory for the thread
whose ID is in the corresponding element of the input array of IDs.
**Throws:** NullPointerException

- if

ids

is

null
**Throws:** IllegalArgumentException

- if any element in the input array

ids

is

<=

0

.
**Throws:** UnsupportedOperationException

- if the Java virtual
machine implementation does not support thread memory allocation
measurement.
**See Also:** getThreadAllocatedBytes(long)

,

isThreadAllocatedMemorySupported()

,

isThreadAllocatedMemoryEnabled()

,

setThreadAllocatedMemoryEnabled(boolean)

---

#### getThreadAllocatedBytes

long[] getThreadAllocatedBytes​(long[] ids)

Returns an approximation of the total amount of memory, in bytes,
allocated in heap memory for each thread whose ID is in the input
array

ids

.
The returned values are approximations because some Java virtual machine
implementations may use object allocation mechanisms that result in a
delay between the time an object is allocated and the time its size is
recorded.

This method is equivalent to calling the

getThreadAllocatedBytes(long)

method for each thread ID in the input array

ids

and setting the
returned value in the corresponding element of the returned array.

This method is equivalent to calling the

getThreadAllocatedBytes(long)

method for each thread ID in the input array

ids

and setting the
returned value in the corresponding element of the returned array.

isThreadAllocatedMemorySupported

```java
boolean isThreadAllocatedMemorySupported()
```

Tests if the Java virtual machine implementation supports thread memory
allocation measurement.

**Returns:** true

if the Java virtual machine implementation supports thread memory
allocation measurement;

false

otherwise.

---

#### isThreadAllocatedMemorySupported

boolean isThreadAllocatedMemorySupported()

Tests if the Java virtual machine implementation supports thread memory
allocation measurement.

isThreadAllocatedMemoryEnabled

```java
boolean isThreadAllocatedMemoryEnabled()
```

Tests if thread memory allocation measurement is enabled.

**Returns:** true

if thread memory allocation measurement is enabled;

false

otherwise.
**Throws:** UnsupportedOperationException

- if the Java virtual
machine does not support thread memory allocation measurement.
**See Also:** isThreadAllocatedMemorySupported()

---

#### isThreadAllocatedMemoryEnabled

boolean isThreadAllocatedMemoryEnabled()

Tests if thread memory allocation measurement is enabled.

setThreadAllocatedMemoryEnabled

```java
void setThreadAllocatedMemoryEnabled​(boolean enable)
```

Enables or disables thread memory allocation measurement. The default
is platform dependent.

**Parameters:** enable

-

true

to enable;

false

to disable.
**Throws:** UnsupportedOperationException

- if the Java virtual
machine does not support thread memory allocation measurement.
**Throws:** SecurityException

- if a security manager
exists and the caller does not have
ManagementPermission("control").
**See Also:** isThreadAllocatedMemorySupported()

---

#### setThreadAllocatedMemoryEnabled

void setThreadAllocatedMemoryEnabled​(boolean enable)

Enables or disables thread memory allocation measurement. The default
is platform dependent.

---

