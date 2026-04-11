# Interface ThreadReference

**Source:** `jdk.jdi\com\sun\jdi\ThreadReference.html`

### Class Description

```java
public interface
ThreadReference

extends
ObjectReference
```

A thread object from the target VM.
A ThreadReference is an

ObjectReference

with additional
access to thread-specific information from the target VM.

**All Superinterfaces:** Mirror

,

ObjectReference

,

Value

---

### Field Details

#### static final int THREAD_STATUS_UNKNOWN

Thread status is unknown

**See Also:**
- Constant Field Values

---

#### static final int THREAD_STATUS_ZOMBIE

Thread has completed execution

**See Also:**
- Constant Field Values

---

#### static final int THREAD_STATUS_RUNNING

Thread is runnable

**See Also:**
- Constant Field Values

---

#### static final int THREAD_STATUS_SLEEPING

Thread is sleeping - Thread.sleep() or JVM_Sleep() was called

**See Also:**
- Constant Field Values

---

#### static final int THREAD_STATUS_MONITOR

Thread is waiting on a java monitor

**See Also:**
- Constant Field Values

---

#### static final int THREAD_STATUS_WAIT

Thread is waiting - Object.wait() or JVM_MonitorWait() was called

**See Also:**
- Constant Field Values

---

#### static final int THREAD_STATUS_NOT_STARTED

Thread has not yet been started

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### String
name()

Returns the name of this thread.

**Returns:**
- the string containing the thread name.

---

#### void suspend()

Suspends this thread. The thread can be resumed through

resume()

or resumed with other threads through

VirtualMachine.resume()

.

Unlike

Thread.suspend()

,
suspends of both the virtual machine and individual threads are
counted. Before a thread will run again, it must be resumed
(through

resume()

or

resume()

)
the same number of times it has been suspended.

Suspending single threads with this method has the same dangers
as

Thread.suspend()

. If the suspended thread
holds a monitor needed by another running thread, deadlock is
possible in the target VM (at least until the suspended thread
is resumed again).

The suspended thread is guaranteed to remain suspended until
resumed through one of the JDI resume methods mentioned above;
the application in the target VM cannot resume the suspended thread
through

Thread.resume()

.

**Throws:**
- VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

---

#### void resume()

Resumes this thread. If this thread was not previously suspended
through

suspend()

or through

VirtualMachine.suspend()

,
or because of a SUSPEND_ALL or SUSPEND_EVENT_THREAD event, then
invoking this method has no effect. Otherwise, the count of pending
suspends on this thread is decremented. If it is decremented to 0,
the thread will continue to execute.
Note: the normal way to resume from an event related suspension is
via

EventSet.resume()

.

**Throws:**
- VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

---

#### int suspendCount()

Returns the number of pending suspends for this thread. See

suspend()

for an explanation of counted suspends.

**Returns:**
- pending suspend count as an integer

---

#### void stop​(
ObjectReference
throwable)
throws
InvalidTypeException

Stops this thread with an asynchronous exception.
A debugger thread in the target VM will stop this thread
with the given

Throwable

object.

**Parameters:**
- throwable

- the asynchronous exception to throw.

**Throws:**
- InvalidTypeException

- if

throwable

is not
an instance of java.lang.Throwable in the target VM.
- VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

---

#### void interrupt()

Interrupts this thread unless the thread has been suspended by the
debugger.

**Throws:**
- VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

**See Also:**
- Thread.interrupt()

---

#### int status()

Returns the thread's status. If the thread is not suspended the
thread's current status is returned. If the thread is suspended, the
thread's status before the suspension is returned (or

THREAD_STATUS_UNKNOWN

if this information is not available.

isSuspended()

can be used to determine if the thread has been
suspended.

**Returns:**
- one of

THREAD_STATUS_UNKNOWN

,

THREAD_STATUS_ZOMBIE

,

THREAD_STATUS_RUNNING

,

THREAD_STATUS_SLEEPING

,

THREAD_STATUS_MONITOR

,

THREAD_STATUS_WAIT

,

THREAD_STATUS_NOT_STARTED

,

---

#### boolean isSuspended()

Determines whether the thread has been suspended by the
the debugger.

**Returns:**
- true

if the thread is currently suspended;

false

otherwise.

---

#### boolean isAtBreakpoint()

Determines whether the thread is suspended at a breakpoint.

**Returns:**
- true

if the thread is currently stopped at
a breakpoint;

false

otherwise.

---

#### ThreadGroupReference
threadGroup()

Returns this thread's thread group.

**Returns:**
- a

ThreadGroupReference

that mirrors this thread's
thread group in the target VM.

---

#### int frameCount()
throws
IncompatibleThreadStateException

Returns the number of stack frames in the thread's current
call stack.
The thread must be suspended (normally through an interruption
to the VM) to get this information, and
it is only valid until the thread is resumed again.

**Returns:**
- an integer frame count

**Throws:**
- IncompatibleThreadStateException

- if the thread is
not suspended in the target VM

---

#### List
<
StackFrame
> frames()
throws
IncompatibleThreadStateException

Returns a List containing each

StackFrame

in the
thread's current call stack.
The thread must be suspended (normally through an interruption
to the VM) to get this information, and
it is only valid until the thread is resumed again.

**Returns:**
- a List of

StackFrame

with the current frame first
followed by each caller's frame.

**Throws:**
- IncompatibleThreadStateException

- if the thread is
not suspended in the target VM

---

#### StackFrame
frame​(int index)
throws
IncompatibleThreadStateException

Returns the

StackFrame

at the given index in the
thread's current call stack. Index 0 retrieves the current
frame; higher indices retrieve caller frames.
The thread must be suspended (normally through an interruption
to the VM) to get this information, and
it is only valid until the thread is resumed again.

**Parameters:**
- index

- the desired frame

**Returns:**
- the requested

StackFrame

**Throws:**
- IncompatibleThreadStateException

- if the thread is
not suspended in the target VM
- IndexOutOfBoundsException

- if the index is greater than
or equal to

frameCount()

or is negative.

---

#### List
<
StackFrame
> frames​(int start,
int length)
throws
IncompatibleThreadStateException

Returns a List containing a range of

StackFrame

mirrors
from the thread's current call stack.
The thread must be suspended (normally through an interruption
to the VM) to get this information, and
it is only valid until the thread is resumed again.

**Parameters:**
- start

- the index of the first frame to retrieve.
Index 0 represents the current frame.
- length

- the number of frames to retrieve

**Returns:**
- a List of

StackFrame

with the current frame first
followed by each caller's frame.

**Throws:**
- IncompatibleThreadStateException

- if the thread is
not suspended in the target VM
- IndexOutOfBoundsException

- if the specified range is not
within the range of stack frame indicies.
That is, the exception is thrown if any of the following are true:

```java
start < 0
start >=
frameCount()

length < 0
(start+length) >
frameCount()
```

---

#### List
<
ObjectReference
> ownedMonitors()
throws
IncompatibleThreadStateException

Returns a List containing an

ObjectReference

for
each monitor owned by the thread.
A monitor is owned by a thread if it has been entered
(via the synchronized statement or entry into a synchronized
method) and has not been relinquished through

Object.wait()

.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetOwnedMonitorInfo()

to determine if the operation is supported.

**Returns:**
- a List of

ObjectReference

objects. The list
has zero length if no monitors are owned by this thread.

**Throws:**
- UnsupportedOperationException

- if
the target virtual machine does not support this
operation.
- IncompatibleThreadStateException

- if the thread is
not suspended in the target VM

---

#### List
<
MonitorInfo
> ownedMonitorsAndFrames()
throws
IncompatibleThreadStateException

Returns a List containing a

MonitorInfo

object for
each monitor owned by the thread.
A monitor is owned by a thread if it has been entered
(via the synchronized statement or entry into a synchronized
method) and has not been relinquished through

Object.wait()

.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetMonitorFrameInfo()

to determine if the operation is supported.

**Returns:**
- a List of

MonitorInfo

objects. The list
has zero length if no monitors are owned by this thread.

**Throws:**
- UnsupportedOperationException

- if
the target virtual machine does not support this
operation.
- IncompatibleThreadStateException

- if the thread is
not suspended in the target VM

**Since:**
- 1.6

---

#### ObjectReference
currentContendedMonitor()
throws
IncompatibleThreadStateException

Returns an

ObjectReference

for the monitor, if any,
for which this thread is currently waiting.
The thread can be waiting for a monitor through entry into a
synchronized method, the synchronized statement, or

Object.wait()

. The

status()

method can be used
to differentiate between the first two cases and the third.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetCurrentContendedMonitor()

to determine if the operation is supported.

**Returns:**
- the

ObjectReference

corresponding to the
contended monitor, or null if it is not waiting for a monitor.

**Throws:**
- UnsupportedOperationException

- if
the target virtual machine does not support this
operation.
- IncompatibleThreadStateException

- if the thread is
not suspended in the target VM

---

#### void popFrames​(
StackFrame
frame)
throws
IncompatibleThreadStateException

Pop stack frames.

All frames up to and including the

frame

are
popped off the stack.
The frame previous to the parameter

frame

will become the current frame.

After this operation, this thread will be
suspended at the invoke instruction of the target method
that created

frame

.
The

frame

's method can be reentered with a step into
the instruction.

The operand stack is restored, however, any changes
to the arguments that occurred in the called method, remain.
For example, if the method

foo

:

```java
void foo(int x) {
System.out.println("Foo: " + x);
x = 4;
System.out.println("pop here");
}
```

was called with

foo(7)

and

foo

is popped at the second

println

and resumed,
it will print:

Foo: 4

.

Locks acquired by a popped frame are released when it
is popped. This applies to synchronized methods that
are popped, and to any synchronized blocks within them.

Finally blocks are not executed.

No aspect of state, other than this thread's execution point and
locks, is affected by this call. Specifically, the values of
fields are unchanged, as are external resources such as
I/O streams. Additionally, the target program might be
placed in a state that is impossible with normal program flow;
for example, order of lock acquisition might be perturbed.
Thus the target program may
proceed differently than the user would expect.

The specified thread must be suspended.

All

StackFrame

objects for this thread are
invalidated.

No events are generated by this method.

None of the frames through and including the frame for the caller
of

frame

may be native.

Not all target virtual machines support this operation.
Use

VirtualMachine.canPopFrames()

to determine if the operation is supported.

**Parameters:**
- frame

- Stack frame to pop.

frame

is on this
thread's call stack.

**Throws:**
- UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

VirtualMachine.canPopFrames()

.
- IncompatibleThreadStateException

- if this
thread is not suspended.
- IllegalArgumentException

- if

frame

is not on this thread's call stack.
- NativeMethodException

- if one of the frames that would be
popped is that of a native method or if the frame previous to

frame

is native.
- InvalidStackFrameException

- if

frame

has become
invalid. Once this thread is resumed, the stack frame is
no longer valid. This exception is also thrown if there are no
more frames.
- VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

**Since:**
- 1.4

---

#### void forceEarlyReturn​(
Value
value)
throws
InvalidTypeException
,

ClassNotLoadedException
,

IncompatibleThreadStateException

Force a method to return before it reaches a return
statement.

The method which will return early is referred to as the
called method. The called method is the current method (as
defined by the Frames section in the Java Virtual Machine
Specification) for the specified thread at the time this
method is called.

The thread must be suspended.
The return occurs when execution of Java programming
language code is resumed on this thread. Between the call to
this method and resumption of thread execution, the
state of the stack is undefined.

No further instructions are executed in the called
method. Specifically, finally blocks are not executed. Note:
this can cause inconsistent states in the application.

A lock acquired by calling the called method (if it is a
synchronized method) and locks acquired by entering
synchronized blocks within the called method are
released. Note: this does not apply to native locks or
java.util.concurrent.locks locks.

Events, such as MethodExit, are generated as they would be in
a normal return.

The called method must be a non-native Java programming
language method. Forcing return on a thread with only one
frame on the stack causes the thread to exit when resumed.

The

value

argument is the value that the
method is to return.
If the return type of the method is void, then value must
be a

VoidValue

.
Object values must be assignment compatible with the method return type
(This implies that the method return type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the method return type or must be
convertible to the variable type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

Not all target virtual machines support this operation.
Use

VirtualMachine.canForceEarlyReturn()

to determine if the operation is supported.

**Parameters:**
- value

- the value the method is to return.

**Throws:**
- UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canForceEarlyReturn()
- IncompatibleThreadStateException

- if this
thread is not suspended.
- NativeMethodException

- if the frame to be returned from
is that of a native method.
- InvalidStackFrameException

- if there are no frames.
- InvalidTypeException

- if the value's type does not match
the method's return type.
- ClassNotLoadedException

- if the method's return type has not yet
been loaded through the appropriate class loader.
- VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

**Since:**
- 1.6

---

### Additional Sections

#### Interface ThreadReference

**All Superinterfaces:** Mirror

,

ObjectReference

,

Value

```java
public interface
ThreadReference

extends
ObjectReference
```

A thread object from the target VM.
A ThreadReference is an

ObjectReference

with additional
access to thread-specific information from the target VM.

**Since:** 1.3

public interface

ThreadReference

extends

ObjectReference

A thread object from the target VM.
A ThreadReference is an

ObjectReference

with additional
access to thread-specific information from the target VM.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

THREAD_STATUS_MONITOR

Thread is waiting on a java monitor

static int

THREAD_STATUS_NOT_STARTED

Thread has not yet been started

static int

THREAD_STATUS_RUNNING

Thread is runnable

static int

THREAD_STATUS_SLEEPING

Thread is sleeping - Thread.sleep() or JVM_Sleep() was called

static int

THREAD_STATUS_UNKNOWN

Thread status is unknown

static int

THREAD_STATUS_WAIT

Thread is waiting - Object.wait() or JVM_MonitorWait() was called

static int

THREAD_STATUS_ZOMBIE

Thread has completed execution

- Fields declared in interface com.sun.jdi.

ObjectReference

INVOKE_NONVIRTUAL

,

INVOKE_SINGLE_THREADED

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ObjectReference

currentContendedMonitor

()

Returns an

ObjectReference

for the monitor, if any,
for which this thread is currently waiting.

void

forceEarlyReturn

​(

Value

value)

Force a method to return before it reaches a return
statement.

StackFrame

frame

​(int index)

Returns the

StackFrame

at the given index in the
thread's current call stack.

int

frameCount

()

Returns the number of stack frames in the thread's current
call stack.

List

<

StackFrame

>

frames

()

Returns a List containing each

StackFrame

in the
thread's current call stack.

List

<

StackFrame

>

frames

​(int start,
int length)

Returns a List containing a range of

StackFrame

mirrors
from the thread's current call stack.

void

interrupt

()

Interrupts this thread unless the thread has been suspended by the
debugger.

boolean

isAtBreakpoint

()

Determines whether the thread is suspended at a breakpoint.

boolean

isSuspended

()

Determines whether the thread has been suspended by the
the debugger.

String

name

()

Returns the name of this thread.

List

<

ObjectReference

>

ownedMonitors

()

Returns a List containing an

ObjectReference

for
each monitor owned by the thread.

List

<

MonitorInfo

>

ownedMonitorsAndFrames

()

Returns a List containing a

MonitorInfo

object for
each monitor owned by the thread.

void

popFrames

​(

StackFrame

frame)

Pop stack frames.

void

resume

()

Resumes this thread.

int

status

()

Returns the thread's status.

void

stop

​(

ObjectReference

throwable)

Stops this thread with an asynchronous exception.

void

suspend

()

Suspends this thread.

int

suspendCount

()

Returns the number of pending suspends for this thread.

ThreadGroupReference

threadGroup

()

Returns this thread's thread group.

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

- Methods declared in interface com.sun.jdi.

ObjectReference

disableCollection

,

enableCollection

,

entryCount

,

equals

,

getValue

,

getValues

,

hashCode

,

invokeMethod

,

isCollected

,

owningThread

,

referenceType

,

referringObjects

,

setValue

,

uniqueID

,

waitingThreads

- Methods declared in interface com.sun.jdi.

Value

type

Field Summary

Fields

Modifier and Type

Field

Description

static int

THREAD_STATUS_MONITOR

Thread is waiting on a java monitor

static int

THREAD_STATUS_NOT_STARTED

Thread has not yet been started

static int

THREAD_STATUS_RUNNING

Thread is runnable

static int

THREAD_STATUS_SLEEPING

Thread is sleeping - Thread.sleep() or JVM_Sleep() was called

static int

THREAD_STATUS_UNKNOWN

Thread status is unknown

static int

THREAD_STATUS_WAIT

Thread is waiting - Object.wait() or JVM_MonitorWait() was called

static int

THREAD_STATUS_ZOMBIE

Thread has completed execution

- Fields declared in interface com.sun.jdi.

ObjectReference

INVOKE_NONVIRTUAL

,

INVOKE_SINGLE_THREADED

---

#### Field Summary

Thread is waiting on a java monitor

Thread has not yet been started

Thread is runnable

Thread is sleeping - Thread.sleep() or JVM_Sleep() was called

Thread status is unknown

Thread is waiting - Object.wait() or JVM_MonitorWait() was called

Thread has completed execution

Fields declared in interface com.sun.jdi.

ObjectReference

INVOKE_NONVIRTUAL

,

INVOKE_SINGLE_THREADED

---

#### Fields declared in interface com.sun.jdi. ObjectReference

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ObjectReference

currentContendedMonitor

()

Returns an

ObjectReference

for the monitor, if any,
for which this thread is currently waiting.

void

forceEarlyReturn

​(

Value

value)

Force a method to return before it reaches a return
statement.

StackFrame

frame

​(int index)

Returns the

StackFrame

at the given index in the
thread's current call stack.

int

frameCount

()

Returns the number of stack frames in the thread's current
call stack.

List

<

StackFrame

>

frames

()

Returns a List containing each

StackFrame

in the
thread's current call stack.

List

<

StackFrame

>

frames

​(int start,
int length)

Returns a List containing a range of

StackFrame

mirrors
from the thread's current call stack.

void

interrupt

()

Interrupts this thread unless the thread has been suspended by the
debugger.

boolean

isAtBreakpoint

()

Determines whether the thread is suspended at a breakpoint.

boolean

isSuspended

()

Determines whether the thread has been suspended by the
the debugger.

String

name

()

Returns the name of this thread.

List

<

ObjectReference

>

ownedMonitors

()

Returns a List containing an

ObjectReference

for
each monitor owned by the thread.

List

<

MonitorInfo

>

ownedMonitorsAndFrames

()

Returns a List containing a

MonitorInfo

object for
each monitor owned by the thread.

void

popFrames

​(

StackFrame

frame)

Pop stack frames.

void

resume

()

Resumes this thread.

int

status

()

Returns the thread's status.

void

stop

​(

ObjectReference

throwable)

Stops this thread with an asynchronous exception.

void

suspend

()

Suspends this thread.

int

suspendCount

()

Returns the number of pending suspends for this thread.

ThreadGroupReference

threadGroup

()

Returns this thread's thread group.

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

- Methods declared in interface com.sun.jdi.

ObjectReference

disableCollection

,

enableCollection

,

entryCount

,

equals

,

getValue

,

getValues

,

hashCode

,

invokeMethod

,

isCollected

,

owningThread

,

referenceType

,

referringObjects

,

setValue

,

uniqueID

,

waitingThreads

- Methods declared in interface com.sun.jdi.

Value

type

---

#### Method Summary

Returns an

ObjectReference

for the monitor, if any,
for which this thread is currently waiting.

Force a method to return before it reaches a return
statement.

Returns the

StackFrame

at the given index in the
thread's current call stack.

Returns the number of stack frames in the thread's current
call stack.

Returns a List containing each

StackFrame

in the
thread's current call stack.

Returns a List containing a range of

StackFrame

mirrors
from the thread's current call stack.

Interrupts this thread unless the thread has been suspended by the
debugger.

Determines whether the thread is suspended at a breakpoint.

Determines whether the thread has been suspended by the
the debugger.

Returns the name of this thread.

Returns a List containing an

ObjectReference

for
each monitor owned by the thread.

Returns a List containing a

MonitorInfo

object for
each monitor owned by the thread.

Pop stack frames.

Resumes this thread.

Returns the thread's status.

Stops this thread with an asynchronous exception.

Suspends this thread.

Returns the number of pending suspends for this thread.

Returns this thread's thread group.

Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Methods declared in interface com.sun.jdi. Mirror

Methods declared in interface com.sun.jdi.

ObjectReference

disableCollection

,

enableCollection

,

entryCount

,

equals

,

getValue

,

getValues

,

hashCode

,

invokeMethod

,

isCollected

,

owningThread

,

referenceType

,

referringObjects

,

setValue

,

uniqueID

,

waitingThreads

---

#### Methods declared in interface com.sun.jdi. ObjectReference

Methods declared in interface com.sun.jdi.

Value

type

---

#### Methods declared in interface com.sun.jdi. Value

============ FIELD DETAIL ===========

- Field Detail

- THREAD_STATUS_UNKNOWN

```java
static final int THREAD_STATUS_UNKNOWN
```

Thread status is unknown

**See Also:** Constant Field Values

- THREAD_STATUS_ZOMBIE

```java
static final int THREAD_STATUS_ZOMBIE
```

Thread has completed execution

**See Also:** Constant Field Values

- THREAD_STATUS_RUNNING

```java
static final int THREAD_STATUS_RUNNING
```

Thread is runnable

**See Also:** Constant Field Values

- THREAD_STATUS_SLEEPING

```java
static final int THREAD_STATUS_SLEEPING
```

Thread is sleeping - Thread.sleep() or JVM_Sleep() was called

**See Also:** Constant Field Values

- THREAD_STATUS_MONITOR

```java
static final int THREAD_STATUS_MONITOR
```

Thread is waiting on a java monitor

**See Also:** Constant Field Values

- THREAD_STATUS_WAIT

```java
static final int THREAD_STATUS_WAIT
```

Thread is waiting - Object.wait() or JVM_MonitorWait() was called

**See Also:** Constant Field Values

- THREAD_STATUS_NOT_STARTED

```java
static final int THREAD_STATUS_NOT_STARTED
```

Thread has not yet been started

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- name

```java
String
name()
```

Returns the name of this thread.

**Returns:** the string containing the thread name.

- suspend

```java
void suspend()
```

Suspends this thread. The thread can be resumed through

resume()

or resumed with other threads through

VirtualMachine.resume()

.

Unlike

Thread.suspend()

,
suspends of both the virtual machine and individual threads are
counted. Before a thread will run again, it must be resumed
(through

resume()

or

resume()

)
the same number of times it has been suspended.

Suspending single threads with this method has the same dangers
as

Thread.suspend()

. If the suspended thread
holds a monitor needed by another running thread, deadlock is
possible in the target VM (at least until the suspended thread
is resumed again).

The suspended thread is guaranteed to remain suspended until
resumed through one of the JDI resume methods mentioned above;
the application in the target VM cannot resume the suspended thread
through

Thread.resume()

.

**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

- resume

```java
void resume()
```

Resumes this thread. If this thread was not previously suspended
through

suspend()

or through

VirtualMachine.suspend()

,
or because of a SUSPEND_ALL or SUSPEND_EVENT_THREAD event, then
invoking this method has no effect. Otherwise, the count of pending
suspends on this thread is decremented. If it is decremented to 0,
the thread will continue to execute.
Note: the normal way to resume from an event related suspension is
via

EventSet.resume()

.

**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

- suspendCount

```java
int suspendCount()
```

Returns the number of pending suspends for this thread. See

suspend()

for an explanation of counted suspends.

**Returns:** pending suspend count as an integer

- stop

```java
void stop​(
ObjectReference
throwable)
throws
InvalidTypeException
```

Stops this thread with an asynchronous exception.
A debugger thread in the target VM will stop this thread
with the given

Throwable

object.

**Parameters:** throwable

- the asynchronous exception to throw.
**Throws:** InvalidTypeException

- if

throwable

is not
an instance of java.lang.Throwable in the target VM.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

- interrupt

```java
void interrupt()
```

Interrupts this thread unless the thread has been suspended by the
debugger.

**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.
**See Also:** Thread.interrupt()

- status

```java
int status()
```

Returns the thread's status. If the thread is not suspended the
thread's current status is returned. If the thread is suspended, the
thread's status before the suspension is returned (or

THREAD_STATUS_UNKNOWN

if this information is not available.

isSuspended()

can be used to determine if the thread has been
suspended.

**Returns:** one of

THREAD_STATUS_UNKNOWN

,

THREAD_STATUS_ZOMBIE

,

THREAD_STATUS_RUNNING

,

THREAD_STATUS_SLEEPING

,

THREAD_STATUS_MONITOR

,

THREAD_STATUS_WAIT

,

THREAD_STATUS_NOT_STARTED

,

- isSuspended

```java
boolean isSuspended()
```

Determines whether the thread has been suspended by the
the debugger.

**Returns:** true

if the thread is currently suspended;

false

otherwise.

- isAtBreakpoint

```java
boolean isAtBreakpoint()
```

Determines whether the thread is suspended at a breakpoint.

**Returns:** true

if the thread is currently stopped at
a breakpoint;

false

otherwise.

- threadGroup

```java
ThreadGroupReference
threadGroup()
```

Returns this thread's thread group.

**Returns:** a

ThreadGroupReference

that mirrors this thread's
thread group in the target VM.

- frameCount

```java
int frameCount()
throws
IncompatibleThreadStateException
```

Returns the number of stack frames in the thread's current
call stack.
The thread must be suspended (normally through an interruption
to the VM) to get this information, and
it is only valid until the thread is resumed again.

**Returns:** an integer frame count
**Throws:** IncompatibleThreadStateException

- if the thread is
not suspended in the target VM

- frames

```java
List
<
StackFrame
> frames()
throws
IncompatibleThreadStateException
```

Returns a List containing each

StackFrame

in the
thread's current call stack.
The thread must be suspended (normally through an interruption
to the VM) to get this information, and
it is only valid until the thread is resumed again.

**Returns:** a List of

StackFrame

with the current frame first
followed by each caller's frame.
**Throws:** IncompatibleThreadStateException

- if the thread is
not suspended in the target VM

- frame

```java
StackFrame
frame​(int index)
throws
IncompatibleThreadStateException
```

Returns the

StackFrame

at the given index in the
thread's current call stack. Index 0 retrieves the current
frame; higher indices retrieve caller frames.
The thread must be suspended (normally through an interruption
to the VM) to get this information, and
it is only valid until the thread is resumed again.

**Parameters:** index

- the desired frame
**Returns:** the requested

StackFrame
**Throws:** IncompatibleThreadStateException

- if the thread is
not suspended in the target VM
**Throws:** IndexOutOfBoundsException

- if the index is greater than
or equal to

frameCount()

or is negative.

- frames

```java
List
<
StackFrame
> frames​(int start,
int length)
throws
IncompatibleThreadStateException
```

Returns a List containing a range of

StackFrame

mirrors
from the thread's current call stack.
The thread must be suspended (normally through an interruption
to the VM) to get this information, and
it is only valid until the thread is resumed again.

**Parameters:** start

- the index of the first frame to retrieve.
Index 0 represents the current frame.
**Parameters:** length

- the number of frames to retrieve
**Returns:** a List of

StackFrame

with the current frame first
followed by each caller's frame.
**Throws:** IncompatibleThreadStateException

- if the thread is
not suspended in the target VM
**Throws:** IndexOutOfBoundsException

- if the specified range is not
within the range of stack frame indicies.
That is, the exception is thrown if any of the following are true:

```java
start < 0
start >=
frameCount()

length < 0
(start+length) >
frameCount()
```

- ownedMonitors

```java
List
<
ObjectReference
> ownedMonitors()
throws
IncompatibleThreadStateException
```

Returns a List containing an

ObjectReference

for
each monitor owned by the thread.
A monitor is owned by a thread if it has been entered
(via the synchronized statement or entry into a synchronized
method) and has not been relinquished through

Object.wait()

.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetOwnedMonitorInfo()

to determine if the operation is supported.

**Returns:** a List of

ObjectReference

objects. The list
has zero length if no monitors are owned by this thread.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.
**Throws:** IncompatibleThreadStateException

- if the thread is
not suspended in the target VM

- ownedMonitorsAndFrames

```java
List
<
MonitorInfo
> ownedMonitorsAndFrames()
throws
IncompatibleThreadStateException
```

Returns a List containing a

MonitorInfo

object for
each monitor owned by the thread.
A monitor is owned by a thread if it has been entered
(via the synchronized statement or entry into a synchronized
method) and has not been relinquished through

Object.wait()

.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetMonitorFrameInfo()

to determine if the operation is supported.

**Returns:** a List of

MonitorInfo

objects. The list
has zero length if no monitors are owned by this thread.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.
**Throws:** IncompatibleThreadStateException

- if the thread is
not suspended in the target VM
**Since:** 1.6

- currentContendedMonitor

```java
ObjectReference
currentContendedMonitor()
throws
IncompatibleThreadStateException
```

Returns an

ObjectReference

for the monitor, if any,
for which this thread is currently waiting.
The thread can be waiting for a monitor through entry into a
synchronized method, the synchronized statement, or

Object.wait()

. The

status()

method can be used
to differentiate between the first two cases and the third.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetCurrentContendedMonitor()

to determine if the operation is supported.

**Returns:** the

ObjectReference

corresponding to the
contended monitor, or null if it is not waiting for a monitor.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.
**Throws:** IncompatibleThreadStateException

- if the thread is
not suspended in the target VM

- popFrames

```java
void popFrames​(
StackFrame
frame)
throws
IncompatibleThreadStateException
```

Pop stack frames.

All frames up to and including the

frame

are
popped off the stack.
The frame previous to the parameter

frame

will become the current frame.

After this operation, this thread will be
suspended at the invoke instruction of the target method
that created

frame

.
The

frame

's method can be reentered with a step into
the instruction.

The operand stack is restored, however, any changes
to the arguments that occurred in the called method, remain.
For example, if the method

foo

:

```java
void foo(int x) {
System.out.println("Foo: " + x);
x = 4;
System.out.println("pop here");
}
```

was called with

foo(7)

and

foo

is popped at the second

println

and resumed,
it will print:

Foo: 4

.

Locks acquired by a popped frame are released when it
is popped. This applies to synchronized methods that
are popped, and to any synchronized blocks within them.

Finally blocks are not executed.

No aspect of state, other than this thread's execution point and
locks, is affected by this call. Specifically, the values of
fields are unchanged, as are external resources such as
I/O streams. Additionally, the target program might be
placed in a state that is impossible with normal program flow;
for example, order of lock acquisition might be perturbed.
Thus the target program may
proceed differently than the user would expect.

The specified thread must be suspended.

All

StackFrame

objects for this thread are
invalidated.

No events are generated by this method.

None of the frames through and including the frame for the caller
of

frame

may be native.

Not all target virtual machines support this operation.
Use

VirtualMachine.canPopFrames()

to determine if the operation is supported.

**Parameters:** frame

- Stack frame to pop.

frame

is on this
thread's call stack.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

VirtualMachine.canPopFrames()

.
**Throws:** IncompatibleThreadStateException

- if this
thread is not suspended.
**Throws:** IllegalArgumentException

- if

frame

is not on this thread's call stack.
**Throws:** NativeMethodException

- if one of the frames that would be
popped is that of a native method or if the frame previous to

frame

is native.
**Throws:** InvalidStackFrameException

- if

frame

has become
invalid. Once this thread is resumed, the stack frame is
no longer valid. This exception is also thrown if there are no
more frames.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.
**Since:** 1.4

- forceEarlyReturn

```java
void forceEarlyReturn​(
Value
value)
throws
InvalidTypeException
,

ClassNotLoadedException
,

IncompatibleThreadStateException
```

Force a method to return before it reaches a return
statement.

The method which will return early is referred to as the
called method. The called method is the current method (as
defined by the Frames section in the Java Virtual Machine
Specification) for the specified thread at the time this
method is called.

The thread must be suspended.
The return occurs when execution of Java programming
language code is resumed on this thread. Between the call to
this method and resumption of thread execution, the
state of the stack is undefined.

No further instructions are executed in the called
method. Specifically, finally blocks are not executed. Note:
this can cause inconsistent states in the application.

A lock acquired by calling the called method (if it is a
synchronized method) and locks acquired by entering
synchronized blocks within the called method are
released. Note: this does not apply to native locks or
java.util.concurrent.locks locks.

Events, such as MethodExit, are generated as they would be in
a normal return.

The called method must be a non-native Java programming
language method. Forcing return on a thread with only one
frame on the stack causes the thread to exit when resumed.

The

value

argument is the value that the
method is to return.
If the return type of the method is void, then value must
be a

VoidValue

.
Object values must be assignment compatible with the method return type
(This implies that the method return type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the method return type or must be
convertible to the variable type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

Not all target virtual machines support this operation.
Use

VirtualMachine.canForceEarlyReturn()

to determine if the operation is supported.

**Parameters:** value

- the value the method is to return.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canForceEarlyReturn()
**Throws:** IncompatibleThreadStateException

- if this
thread is not suspended.
**Throws:** NativeMethodException

- if the frame to be returned from
is that of a native method.
**Throws:** InvalidStackFrameException

- if there are no frames.
**Throws:** InvalidTypeException

- if the value's type does not match
the method's return type.
**Throws:** ClassNotLoadedException

- if the method's return type has not yet
been loaded through the appropriate class loader.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.
**Since:** 1.6

Field Detail

- THREAD_STATUS_UNKNOWN

```java
static final int THREAD_STATUS_UNKNOWN
```

Thread status is unknown

**See Also:** Constant Field Values

- THREAD_STATUS_ZOMBIE

```java
static final int THREAD_STATUS_ZOMBIE
```

Thread has completed execution

**See Also:** Constant Field Values

- THREAD_STATUS_RUNNING

```java
static final int THREAD_STATUS_RUNNING
```

Thread is runnable

**See Also:** Constant Field Values

- THREAD_STATUS_SLEEPING

```java
static final int THREAD_STATUS_SLEEPING
```

Thread is sleeping - Thread.sleep() or JVM_Sleep() was called

**See Also:** Constant Field Values

- THREAD_STATUS_MONITOR

```java
static final int THREAD_STATUS_MONITOR
```

Thread is waiting on a java monitor

**See Also:** Constant Field Values

- THREAD_STATUS_WAIT

```java
static final int THREAD_STATUS_WAIT
```

Thread is waiting - Object.wait() or JVM_MonitorWait() was called

**See Also:** Constant Field Values

- THREAD_STATUS_NOT_STARTED

```java
static final int THREAD_STATUS_NOT_STARTED
```

Thread has not yet been started

**See Also:** Constant Field Values

---

#### Field Detail

THREAD_STATUS_UNKNOWN

```java
static final int THREAD_STATUS_UNKNOWN
```

Thread status is unknown

**See Also:** Constant Field Values

---

#### THREAD_STATUS_UNKNOWN

static final int THREAD_STATUS_UNKNOWN

Thread status is unknown

THREAD_STATUS_ZOMBIE

```java
static final int THREAD_STATUS_ZOMBIE
```

Thread has completed execution

**See Also:** Constant Field Values

---

#### THREAD_STATUS_ZOMBIE

static final int THREAD_STATUS_ZOMBIE

Thread has completed execution

THREAD_STATUS_RUNNING

```java
static final int THREAD_STATUS_RUNNING
```

Thread is runnable

**See Also:** Constant Field Values

---

#### THREAD_STATUS_RUNNING

static final int THREAD_STATUS_RUNNING

Thread is runnable

THREAD_STATUS_SLEEPING

```java
static final int THREAD_STATUS_SLEEPING
```

Thread is sleeping - Thread.sleep() or JVM_Sleep() was called

**See Also:** Constant Field Values

---

#### THREAD_STATUS_SLEEPING

static final int THREAD_STATUS_SLEEPING

Thread is sleeping - Thread.sleep() or JVM_Sleep() was called

THREAD_STATUS_MONITOR

```java
static final int THREAD_STATUS_MONITOR
```

Thread is waiting on a java monitor

**See Also:** Constant Field Values

---

#### THREAD_STATUS_MONITOR

static final int THREAD_STATUS_MONITOR

Thread is waiting on a java monitor

THREAD_STATUS_WAIT

```java
static final int THREAD_STATUS_WAIT
```

Thread is waiting - Object.wait() or JVM_MonitorWait() was called

**See Also:** Constant Field Values

---

#### THREAD_STATUS_WAIT

static final int THREAD_STATUS_WAIT

Thread is waiting - Object.wait() or JVM_MonitorWait() was called

THREAD_STATUS_NOT_STARTED

```java
static final int THREAD_STATUS_NOT_STARTED
```

Thread has not yet been started

**See Also:** Constant Field Values

---

#### THREAD_STATUS_NOT_STARTED

static final int THREAD_STATUS_NOT_STARTED

Thread has not yet been started

Method Detail

- name

```java
String
name()
```

Returns the name of this thread.

**Returns:** the string containing the thread name.

- suspend

```java
void suspend()
```

Suspends this thread. The thread can be resumed through

resume()

or resumed with other threads through

VirtualMachine.resume()

.

Unlike

Thread.suspend()

,
suspends of both the virtual machine and individual threads are
counted. Before a thread will run again, it must be resumed
(through

resume()

or

resume()

)
the same number of times it has been suspended.

Suspending single threads with this method has the same dangers
as

Thread.suspend()

. If the suspended thread
holds a monitor needed by another running thread, deadlock is
possible in the target VM (at least until the suspended thread
is resumed again).

The suspended thread is guaranteed to remain suspended until
resumed through one of the JDI resume methods mentioned above;
the application in the target VM cannot resume the suspended thread
through

Thread.resume()

.

**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

- resume

```java
void resume()
```

Resumes this thread. If this thread was not previously suspended
through

suspend()

or through

VirtualMachine.suspend()

,
or because of a SUSPEND_ALL or SUSPEND_EVENT_THREAD event, then
invoking this method has no effect. Otherwise, the count of pending
suspends on this thread is decremented. If it is decremented to 0,
the thread will continue to execute.
Note: the normal way to resume from an event related suspension is
via

EventSet.resume()

.

**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

- suspendCount

```java
int suspendCount()
```

Returns the number of pending suspends for this thread. See

suspend()

for an explanation of counted suspends.

**Returns:** pending suspend count as an integer

- stop

```java
void stop​(
ObjectReference
throwable)
throws
InvalidTypeException
```

Stops this thread with an asynchronous exception.
A debugger thread in the target VM will stop this thread
with the given

Throwable

object.

**Parameters:** throwable

- the asynchronous exception to throw.
**Throws:** InvalidTypeException

- if

throwable

is not
an instance of java.lang.Throwable in the target VM.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

- interrupt

```java
void interrupt()
```

Interrupts this thread unless the thread has been suspended by the
debugger.

**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.
**See Also:** Thread.interrupt()

- status

```java
int status()
```

Returns the thread's status. If the thread is not suspended the
thread's current status is returned. If the thread is suspended, the
thread's status before the suspension is returned (or

THREAD_STATUS_UNKNOWN

if this information is not available.

isSuspended()

can be used to determine if the thread has been
suspended.

**Returns:** one of

THREAD_STATUS_UNKNOWN

,

THREAD_STATUS_ZOMBIE

,

THREAD_STATUS_RUNNING

,

THREAD_STATUS_SLEEPING

,

THREAD_STATUS_MONITOR

,

THREAD_STATUS_WAIT

,

THREAD_STATUS_NOT_STARTED

,

- isSuspended

```java
boolean isSuspended()
```

Determines whether the thread has been suspended by the
the debugger.

**Returns:** true

if the thread is currently suspended;

false

otherwise.

- isAtBreakpoint

```java
boolean isAtBreakpoint()
```

Determines whether the thread is suspended at a breakpoint.

**Returns:** true

if the thread is currently stopped at
a breakpoint;

false

otherwise.

- threadGroup

```java
ThreadGroupReference
threadGroup()
```

Returns this thread's thread group.

**Returns:** a

ThreadGroupReference

that mirrors this thread's
thread group in the target VM.

- frameCount

```java
int frameCount()
throws
IncompatibleThreadStateException
```

Returns the number of stack frames in the thread's current
call stack.
The thread must be suspended (normally through an interruption
to the VM) to get this information, and
it is only valid until the thread is resumed again.

**Returns:** an integer frame count
**Throws:** IncompatibleThreadStateException

- if the thread is
not suspended in the target VM

- frames

```java
List
<
StackFrame
> frames()
throws
IncompatibleThreadStateException
```

Returns a List containing each

StackFrame

in the
thread's current call stack.
The thread must be suspended (normally through an interruption
to the VM) to get this information, and
it is only valid until the thread is resumed again.

**Returns:** a List of

StackFrame

with the current frame first
followed by each caller's frame.
**Throws:** IncompatibleThreadStateException

- if the thread is
not suspended in the target VM

- frame

```java
StackFrame
frame​(int index)
throws
IncompatibleThreadStateException
```

Returns the

StackFrame

at the given index in the
thread's current call stack. Index 0 retrieves the current
frame; higher indices retrieve caller frames.
The thread must be suspended (normally through an interruption
to the VM) to get this information, and
it is only valid until the thread is resumed again.

**Parameters:** index

- the desired frame
**Returns:** the requested

StackFrame
**Throws:** IncompatibleThreadStateException

- if the thread is
not suspended in the target VM
**Throws:** IndexOutOfBoundsException

- if the index is greater than
or equal to

frameCount()

or is negative.

- frames

```java
List
<
StackFrame
> frames​(int start,
int length)
throws
IncompatibleThreadStateException
```

Returns a List containing a range of

StackFrame

mirrors
from the thread's current call stack.
The thread must be suspended (normally through an interruption
to the VM) to get this information, and
it is only valid until the thread is resumed again.

**Parameters:** start

- the index of the first frame to retrieve.
Index 0 represents the current frame.
**Parameters:** length

- the number of frames to retrieve
**Returns:** a List of

StackFrame

with the current frame first
followed by each caller's frame.
**Throws:** IncompatibleThreadStateException

- if the thread is
not suspended in the target VM
**Throws:** IndexOutOfBoundsException

- if the specified range is not
within the range of stack frame indicies.
That is, the exception is thrown if any of the following are true:

```java
start < 0
start >=
frameCount()

length < 0
(start+length) >
frameCount()
```

- ownedMonitors

```java
List
<
ObjectReference
> ownedMonitors()
throws
IncompatibleThreadStateException
```

Returns a List containing an

ObjectReference

for
each monitor owned by the thread.
A monitor is owned by a thread if it has been entered
(via the synchronized statement or entry into a synchronized
method) and has not been relinquished through

Object.wait()

.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetOwnedMonitorInfo()

to determine if the operation is supported.

**Returns:** a List of

ObjectReference

objects. The list
has zero length if no monitors are owned by this thread.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.
**Throws:** IncompatibleThreadStateException

- if the thread is
not suspended in the target VM

- ownedMonitorsAndFrames

```java
List
<
MonitorInfo
> ownedMonitorsAndFrames()
throws
IncompatibleThreadStateException
```

Returns a List containing a

MonitorInfo

object for
each monitor owned by the thread.
A monitor is owned by a thread if it has been entered
(via the synchronized statement or entry into a synchronized
method) and has not been relinquished through

Object.wait()

.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetMonitorFrameInfo()

to determine if the operation is supported.

**Returns:** a List of

MonitorInfo

objects. The list
has zero length if no monitors are owned by this thread.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.
**Throws:** IncompatibleThreadStateException

- if the thread is
not suspended in the target VM
**Since:** 1.6

- currentContendedMonitor

```java
ObjectReference
currentContendedMonitor()
throws
IncompatibleThreadStateException
```

Returns an

ObjectReference

for the monitor, if any,
for which this thread is currently waiting.
The thread can be waiting for a monitor through entry into a
synchronized method, the synchronized statement, or

Object.wait()

. The

status()

method can be used
to differentiate between the first two cases and the third.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetCurrentContendedMonitor()

to determine if the operation is supported.

**Returns:** the

ObjectReference

corresponding to the
contended monitor, or null if it is not waiting for a monitor.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.
**Throws:** IncompatibleThreadStateException

- if the thread is
not suspended in the target VM

- popFrames

```java
void popFrames​(
StackFrame
frame)
throws
IncompatibleThreadStateException
```

Pop stack frames.

All frames up to and including the

frame

are
popped off the stack.
The frame previous to the parameter

frame

will become the current frame.

After this operation, this thread will be
suspended at the invoke instruction of the target method
that created

frame

.
The

frame

's method can be reentered with a step into
the instruction.

The operand stack is restored, however, any changes
to the arguments that occurred in the called method, remain.
For example, if the method

foo

:

```java
void foo(int x) {
System.out.println("Foo: " + x);
x = 4;
System.out.println("pop here");
}
```

was called with

foo(7)

and

foo

is popped at the second

println

and resumed,
it will print:

Foo: 4

.

Locks acquired by a popped frame are released when it
is popped. This applies to synchronized methods that
are popped, and to any synchronized blocks within them.

Finally blocks are not executed.

No aspect of state, other than this thread's execution point and
locks, is affected by this call. Specifically, the values of
fields are unchanged, as are external resources such as
I/O streams. Additionally, the target program might be
placed in a state that is impossible with normal program flow;
for example, order of lock acquisition might be perturbed.
Thus the target program may
proceed differently than the user would expect.

The specified thread must be suspended.

All

StackFrame

objects for this thread are
invalidated.

No events are generated by this method.

None of the frames through and including the frame for the caller
of

frame

may be native.

Not all target virtual machines support this operation.
Use

VirtualMachine.canPopFrames()

to determine if the operation is supported.

**Parameters:** frame

- Stack frame to pop.

frame

is on this
thread's call stack.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

VirtualMachine.canPopFrames()

.
**Throws:** IncompatibleThreadStateException

- if this
thread is not suspended.
**Throws:** IllegalArgumentException

- if

frame

is not on this thread's call stack.
**Throws:** NativeMethodException

- if one of the frames that would be
popped is that of a native method or if the frame previous to

frame

is native.
**Throws:** InvalidStackFrameException

- if

frame

has become
invalid. Once this thread is resumed, the stack frame is
no longer valid. This exception is also thrown if there are no
more frames.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.
**Since:** 1.4

- forceEarlyReturn

```java
void forceEarlyReturn​(
Value
value)
throws
InvalidTypeException
,

ClassNotLoadedException
,

IncompatibleThreadStateException
```

Force a method to return before it reaches a return
statement.

The method which will return early is referred to as the
called method. The called method is the current method (as
defined by the Frames section in the Java Virtual Machine
Specification) for the specified thread at the time this
method is called.

The thread must be suspended.
The return occurs when execution of Java programming
language code is resumed on this thread. Between the call to
this method and resumption of thread execution, the
state of the stack is undefined.

No further instructions are executed in the called
method. Specifically, finally blocks are not executed. Note:
this can cause inconsistent states in the application.

A lock acquired by calling the called method (if it is a
synchronized method) and locks acquired by entering
synchronized blocks within the called method are
released. Note: this does not apply to native locks or
java.util.concurrent.locks locks.

Events, such as MethodExit, are generated as they would be in
a normal return.

The called method must be a non-native Java programming
language method. Forcing return on a thread with only one
frame on the stack causes the thread to exit when resumed.

The

value

argument is the value that the
method is to return.
If the return type of the method is void, then value must
be a

VoidValue

.
Object values must be assignment compatible with the method return type
(This implies that the method return type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the method return type or must be
convertible to the variable type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

Not all target virtual machines support this operation.
Use

VirtualMachine.canForceEarlyReturn()

to determine if the operation is supported.

**Parameters:** value

- the value the method is to return.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canForceEarlyReturn()
**Throws:** IncompatibleThreadStateException

- if this
thread is not suspended.
**Throws:** NativeMethodException

- if the frame to be returned from
is that of a native method.
**Throws:** InvalidStackFrameException

- if there are no frames.
**Throws:** InvalidTypeException

- if the value's type does not match
the method's return type.
**Throws:** ClassNotLoadedException

- if the method's return type has not yet
been loaded through the appropriate class loader.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.
**Since:** 1.6

---

#### Method Detail

name

```java
String
name()
```

Returns the name of this thread.

**Returns:** the string containing the thread name.

---

#### name

String

name()

Returns the name of this thread.

suspend

```java
void suspend()
```

Suspends this thread. The thread can be resumed through

resume()

or resumed with other threads through

VirtualMachine.resume()

.

Unlike

Thread.suspend()

,
suspends of both the virtual machine and individual threads are
counted. Before a thread will run again, it must be resumed
(through

resume()

or

resume()

)
the same number of times it has been suspended.

Suspending single threads with this method has the same dangers
as

Thread.suspend()

. If the suspended thread
holds a monitor needed by another running thread, deadlock is
possible in the target VM (at least until the suspended thread
is resumed again).

The suspended thread is guaranteed to remain suspended until
resumed through one of the JDI resume methods mentioned above;
the application in the target VM cannot resume the suspended thread
through

Thread.resume()

.

**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

---

#### suspend

void suspend()

Suspends this thread. The thread can be resumed through

resume()

or resumed with other threads through

VirtualMachine.resume()

.

Unlike

Thread.suspend()

,
suspends of both the virtual machine and individual threads are
counted. Before a thread will run again, it must be resumed
(through

resume()

or

resume()

)
the same number of times it has been suspended.

Suspending single threads with this method has the same dangers
as

Thread.suspend()

. If the suspended thread
holds a monitor needed by another running thread, deadlock is
possible in the target VM (at least until the suspended thread
is resumed again).

The suspended thread is guaranteed to remain suspended until
resumed through one of the JDI resume methods mentioned above;
the application in the target VM cannot resume the suspended thread
through

Thread.resume()

.

Unlike

Thread.suspend()

,
suspends of both the virtual machine and individual threads are
counted. Before a thread will run again, it must be resumed
(through

resume()

or

resume()

)
the same number of times it has been suspended.

Suspending single threads with this method has the same dangers
as

Thread.suspend()

. If the suspended thread
holds a monitor needed by another running thread, deadlock is
possible in the target VM (at least until the suspended thread
is resumed again).

The suspended thread is guaranteed to remain suspended until
resumed through one of the JDI resume methods mentioned above;
the application in the target VM cannot resume the suspended thread
through

Thread.resume()

.

Suspending single threads with this method has the same dangers
as

Thread.suspend()

. If the suspended thread
holds a monitor needed by another running thread, deadlock is
possible in the target VM (at least until the suspended thread
is resumed again).

The suspended thread is guaranteed to remain suspended until
resumed through one of the JDI resume methods mentioned above;
the application in the target VM cannot resume the suspended thread
through

Thread.resume()

.

The suspended thread is guaranteed to remain suspended until
resumed through one of the JDI resume methods mentioned above;
the application in the target VM cannot resume the suspended thread
through

Thread.resume()

.

resume

```java
void resume()
```

Resumes this thread. If this thread was not previously suspended
through

suspend()

or through

VirtualMachine.suspend()

,
or because of a SUSPEND_ALL or SUSPEND_EVENT_THREAD event, then
invoking this method has no effect. Otherwise, the count of pending
suspends on this thread is decremented. If it is decremented to 0,
the thread will continue to execute.
Note: the normal way to resume from an event related suspension is
via

EventSet.resume()

.

**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

---

#### resume

void resume()

Resumes this thread. If this thread was not previously suspended
through

suspend()

or through

VirtualMachine.suspend()

,
or because of a SUSPEND_ALL or SUSPEND_EVENT_THREAD event, then
invoking this method has no effect. Otherwise, the count of pending
suspends on this thread is decremented. If it is decremented to 0,
the thread will continue to execute.
Note: the normal way to resume from an event related suspension is
via

EventSet.resume()

.

suspendCount

```java
int suspendCount()
```

Returns the number of pending suspends for this thread. See

suspend()

for an explanation of counted suspends.

**Returns:** pending suspend count as an integer

---

#### suspendCount

int suspendCount()

Returns the number of pending suspends for this thread. See

suspend()

for an explanation of counted suspends.

stop

```java
void stop​(
ObjectReference
throwable)
throws
InvalidTypeException
```

Stops this thread with an asynchronous exception.
A debugger thread in the target VM will stop this thread
with the given

Throwable

object.

**Parameters:** throwable

- the asynchronous exception to throw.
**Throws:** InvalidTypeException

- if

throwable

is not
an instance of java.lang.Throwable in the target VM.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

---

#### stop

void stop​(

ObjectReference

throwable)
throws

InvalidTypeException

Stops this thread with an asynchronous exception.
A debugger thread in the target VM will stop this thread
with the given

Throwable

object.

interrupt

```java
void interrupt()
```

Interrupts this thread unless the thread has been suspended by the
debugger.

**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.
**See Also:** Thread.interrupt()

---

#### interrupt

void interrupt()

Interrupts this thread unless the thread has been suspended by the
debugger.

status

```java
int status()
```

Returns the thread's status. If the thread is not suspended the
thread's current status is returned. If the thread is suspended, the
thread's status before the suspension is returned (or

THREAD_STATUS_UNKNOWN

if this information is not available.

isSuspended()

can be used to determine if the thread has been
suspended.

**Returns:** one of

THREAD_STATUS_UNKNOWN

,

THREAD_STATUS_ZOMBIE

,

THREAD_STATUS_RUNNING

,

THREAD_STATUS_SLEEPING

,

THREAD_STATUS_MONITOR

,

THREAD_STATUS_WAIT

,

THREAD_STATUS_NOT_STARTED

,

---

#### status

int status()

Returns the thread's status. If the thread is not suspended the
thread's current status is returned. If the thread is suspended, the
thread's status before the suspension is returned (or

THREAD_STATUS_UNKNOWN

if this information is not available.

isSuspended()

can be used to determine if the thread has been
suspended.

isSuspended

```java
boolean isSuspended()
```

Determines whether the thread has been suspended by the
the debugger.

**Returns:** true

if the thread is currently suspended;

false

otherwise.

---

#### isSuspended

boolean isSuspended()

Determines whether the thread has been suspended by the
the debugger.

isAtBreakpoint

```java
boolean isAtBreakpoint()
```

Determines whether the thread is suspended at a breakpoint.

**Returns:** true

if the thread is currently stopped at
a breakpoint;

false

otherwise.

---

#### isAtBreakpoint

boolean isAtBreakpoint()

Determines whether the thread is suspended at a breakpoint.

threadGroup

```java
ThreadGroupReference
threadGroup()
```

Returns this thread's thread group.

**Returns:** a

ThreadGroupReference

that mirrors this thread's
thread group in the target VM.

---

#### threadGroup

ThreadGroupReference

threadGroup()

Returns this thread's thread group.

frameCount

```java
int frameCount()
throws
IncompatibleThreadStateException
```

Returns the number of stack frames in the thread's current
call stack.
The thread must be suspended (normally through an interruption
to the VM) to get this information, and
it is only valid until the thread is resumed again.

**Returns:** an integer frame count
**Throws:** IncompatibleThreadStateException

- if the thread is
not suspended in the target VM

---

#### frameCount

int frameCount()
throws

IncompatibleThreadStateException

Returns the number of stack frames in the thread's current
call stack.
The thread must be suspended (normally through an interruption
to the VM) to get this information, and
it is only valid until the thread is resumed again.

frames

```java
List
<
StackFrame
> frames()
throws
IncompatibleThreadStateException
```

Returns a List containing each

StackFrame

in the
thread's current call stack.
The thread must be suspended (normally through an interruption
to the VM) to get this information, and
it is only valid until the thread is resumed again.

**Returns:** a List of

StackFrame

with the current frame first
followed by each caller's frame.
**Throws:** IncompatibleThreadStateException

- if the thread is
not suspended in the target VM

---

#### frames

List

<

StackFrame

> frames()
throws

IncompatibleThreadStateException

Returns a List containing each

StackFrame

in the
thread's current call stack.
The thread must be suspended (normally through an interruption
to the VM) to get this information, and
it is only valid until the thread is resumed again.

frame

```java
StackFrame
frame​(int index)
throws
IncompatibleThreadStateException
```

Returns the

StackFrame

at the given index in the
thread's current call stack. Index 0 retrieves the current
frame; higher indices retrieve caller frames.
The thread must be suspended (normally through an interruption
to the VM) to get this information, and
it is only valid until the thread is resumed again.

**Parameters:** index

- the desired frame
**Returns:** the requested

StackFrame
**Throws:** IncompatibleThreadStateException

- if the thread is
not suspended in the target VM
**Throws:** IndexOutOfBoundsException

- if the index is greater than
or equal to

frameCount()

or is negative.

---

#### frame

StackFrame

frame​(int index)
throws

IncompatibleThreadStateException

Returns the

StackFrame

at the given index in the
thread's current call stack. Index 0 retrieves the current
frame; higher indices retrieve caller frames.
The thread must be suspended (normally through an interruption
to the VM) to get this information, and
it is only valid until the thread is resumed again.

frames

```java
List
<
StackFrame
> frames​(int start,
int length)
throws
IncompatibleThreadStateException
```

Returns a List containing a range of

StackFrame

mirrors
from the thread's current call stack.
The thread must be suspended (normally through an interruption
to the VM) to get this information, and
it is only valid until the thread is resumed again.

**Parameters:** start

- the index of the first frame to retrieve.
Index 0 represents the current frame.
**Parameters:** length

- the number of frames to retrieve
**Returns:** a List of

StackFrame

with the current frame first
followed by each caller's frame.
**Throws:** IncompatibleThreadStateException

- if the thread is
not suspended in the target VM
**Throws:** IndexOutOfBoundsException

- if the specified range is not
within the range of stack frame indicies.
That is, the exception is thrown if any of the following are true:

```java
start < 0
start >=
frameCount()

length < 0
(start+length) >
frameCount()
```

---

#### frames

List

<

StackFrame

> frames​(int start,
int length)
throws

IncompatibleThreadStateException

Returns a List containing a range of

StackFrame

mirrors
from the thread's current call stack.
The thread must be suspended (normally through an interruption
to the VM) to get this information, and
it is only valid until the thread is resumed again.

start < 0
start >=

frameCount()

length < 0
(start+length) >

frameCount()

ownedMonitors

```java
List
<
ObjectReference
> ownedMonitors()
throws
IncompatibleThreadStateException
```

Returns a List containing an

ObjectReference

for
each monitor owned by the thread.
A monitor is owned by a thread if it has been entered
(via the synchronized statement or entry into a synchronized
method) and has not been relinquished through

Object.wait()

.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetOwnedMonitorInfo()

to determine if the operation is supported.

**Returns:** a List of

ObjectReference

objects. The list
has zero length if no monitors are owned by this thread.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.
**Throws:** IncompatibleThreadStateException

- if the thread is
not suspended in the target VM

---

#### ownedMonitors

List

<

ObjectReference

> ownedMonitors()
throws

IncompatibleThreadStateException

Returns a List containing an

ObjectReference

for
each monitor owned by the thread.
A monitor is owned by a thread if it has been entered
(via the synchronized statement or entry into a synchronized
method) and has not been relinquished through

Object.wait()

.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetOwnedMonitorInfo()

to determine if the operation is supported.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetOwnedMonitorInfo()

to determine if the operation is supported.

ownedMonitorsAndFrames

```java
List
<
MonitorInfo
> ownedMonitorsAndFrames()
throws
IncompatibleThreadStateException
```

Returns a List containing a

MonitorInfo

object for
each monitor owned by the thread.
A monitor is owned by a thread if it has been entered
(via the synchronized statement or entry into a synchronized
method) and has not been relinquished through

Object.wait()

.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetMonitorFrameInfo()

to determine if the operation is supported.

**Returns:** a List of

MonitorInfo

objects. The list
has zero length if no monitors are owned by this thread.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.
**Throws:** IncompatibleThreadStateException

- if the thread is
not suspended in the target VM
**Since:** 1.6

---

#### ownedMonitorsAndFrames

List

<

MonitorInfo

> ownedMonitorsAndFrames()
throws

IncompatibleThreadStateException

Returns a List containing a

MonitorInfo

object for
each monitor owned by the thread.
A monitor is owned by a thread if it has been entered
(via the synchronized statement or entry into a synchronized
method) and has not been relinquished through

Object.wait()

.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetMonitorFrameInfo()

to determine if the operation is supported.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetMonitorFrameInfo()

to determine if the operation is supported.

currentContendedMonitor

```java
ObjectReference
currentContendedMonitor()
throws
IncompatibleThreadStateException
```

Returns an

ObjectReference

for the monitor, if any,
for which this thread is currently waiting.
The thread can be waiting for a monitor through entry into a
synchronized method, the synchronized statement, or

Object.wait()

. The

status()

method can be used
to differentiate between the first two cases and the third.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetCurrentContendedMonitor()

to determine if the operation is supported.

**Returns:** the

ObjectReference

corresponding to the
contended monitor, or null if it is not waiting for a monitor.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation.
**Throws:** IncompatibleThreadStateException

- if the thread is
not suspended in the target VM

---

#### currentContendedMonitor

ObjectReference

currentContendedMonitor()
throws

IncompatibleThreadStateException

Returns an

ObjectReference

for the monitor, if any,
for which this thread is currently waiting.
The thread can be waiting for a monitor through entry into a
synchronized method, the synchronized statement, or

Object.wait()

. The

status()

method can be used
to differentiate between the first two cases and the third.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetCurrentContendedMonitor()

to determine if the operation is supported.

Not all target virtual machines support this operation.
Use

VirtualMachine.canGetCurrentContendedMonitor()

to determine if the operation is supported.

popFrames

```java
void popFrames​(
StackFrame
frame)
throws
IncompatibleThreadStateException
```

Pop stack frames.

All frames up to and including the

frame

are
popped off the stack.
The frame previous to the parameter

frame

will become the current frame.

After this operation, this thread will be
suspended at the invoke instruction of the target method
that created

frame

.
The

frame

's method can be reentered with a step into
the instruction.

The operand stack is restored, however, any changes
to the arguments that occurred in the called method, remain.
For example, if the method

foo

:

```java
void foo(int x) {
System.out.println("Foo: " + x);
x = 4;
System.out.println("pop here");
}
```

was called with

foo(7)

and

foo

is popped at the second

println

and resumed,
it will print:

Foo: 4

.

Locks acquired by a popped frame are released when it
is popped. This applies to synchronized methods that
are popped, and to any synchronized blocks within them.

Finally blocks are not executed.

No aspect of state, other than this thread's execution point and
locks, is affected by this call. Specifically, the values of
fields are unchanged, as are external resources such as
I/O streams. Additionally, the target program might be
placed in a state that is impossible with normal program flow;
for example, order of lock acquisition might be perturbed.
Thus the target program may
proceed differently than the user would expect.

The specified thread must be suspended.

All

StackFrame

objects for this thread are
invalidated.

No events are generated by this method.

None of the frames through and including the frame for the caller
of

frame

may be native.

Not all target virtual machines support this operation.
Use

VirtualMachine.canPopFrames()

to determine if the operation is supported.

**Parameters:** frame

- Stack frame to pop.

frame

is on this
thread's call stack.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

VirtualMachine.canPopFrames()

.
**Throws:** IncompatibleThreadStateException

- if this
thread is not suspended.
**Throws:** IllegalArgumentException

- if

frame

is not on this thread's call stack.
**Throws:** NativeMethodException

- if one of the frames that would be
popped is that of a native method or if the frame previous to

frame

is native.
**Throws:** InvalidStackFrameException

- if

frame

has become
invalid. Once this thread is resumed, the stack frame is
no longer valid. This exception is also thrown if there are no
more frames.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.
**Since:** 1.4

---

#### popFrames

void popFrames​(

StackFrame

frame)
throws

IncompatibleThreadStateException

Pop stack frames.

All frames up to and including the

frame

are
popped off the stack.
The frame previous to the parameter

frame

will become the current frame.

After this operation, this thread will be
suspended at the invoke instruction of the target method
that created

frame

.
The

frame

's method can be reentered with a step into
the instruction.

The operand stack is restored, however, any changes
to the arguments that occurred in the called method, remain.
For example, if the method

foo

:

```java
void foo(int x) {
System.out.println("Foo: " + x);
x = 4;
System.out.println("pop here");
}
```

was called with

foo(7)

and

foo

is popped at the second

println

and resumed,
it will print:

Foo: 4

.

Locks acquired by a popped frame are released when it
is popped. This applies to synchronized methods that
are popped, and to any synchronized blocks within them.

Finally blocks are not executed.

No aspect of state, other than this thread's execution point and
locks, is affected by this call. Specifically, the values of
fields are unchanged, as are external resources such as
I/O streams. Additionally, the target program might be
placed in a state that is impossible with normal program flow;
for example, order of lock acquisition might be perturbed.
Thus the target program may
proceed differently than the user would expect.

The specified thread must be suspended.

All

StackFrame

objects for this thread are
invalidated.

No events are generated by this method.

None of the frames through and including the frame for the caller
of

frame

may be native.

Not all target virtual machines support this operation.
Use

VirtualMachine.canPopFrames()

to determine if the operation is supported.

All frames up to and including the

frame

are
popped off the stack.
The frame previous to the parameter

frame

will become the current frame.

After this operation, this thread will be
suspended at the invoke instruction of the target method
that created

frame

.
The

frame

's method can be reentered with a step into
the instruction.

The operand stack is restored, however, any changes
to the arguments that occurred in the called method, remain.
For example, if the method

foo

:

```java
void foo(int x) {
System.out.println("Foo: " + x);
x = 4;
System.out.println("pop here");
}
```

was called with

foo(7)

and

foo

is popped at the second

println

and resumed,
it will print:

Foo: 4

.

Locks acquired by a popped frame are released when it
is popped. This applies to synchronized methods that
are popped, and to any synchronized blocks within them.

Finally blocks are not executed.

No aspect of state, other than this thread's execution point and
locks, is affected by this call. Specifically, the values of
fields are unchanged, as are external resources such as
I/O streams. Additionally, the target program might be
placed in a state that is impossible with normal program flow;
for example, order of lock acquisition might be perturbed.
Thus the target program may
proceed differently than the user would expect.

The specified thread must be suspended.

All

StackFrame

objects for this thread are
invalidated.

No events are generated by this method.

None of the frames through and including the frame for the caller
of

frame

may be native.

Not all target virtual machines support this operation.
Use

VirtualMachine.canPopFrames()

to determine if the operation is supported.

After this operation, this thread will be
suspended at the invoke instruction of the target method
that created

frame

.
The

frame

's method can be reentered with a step into
the instruction.

The operand stack is restored, however, any changes
to the arguments that occurred in the called method, remain.
For example, if the method

foo

:

```java
void foo(int x) {
System.out.println("Foo: " + x);
x = 4;
System.out.println("pop here");
}
```

was called with

foo(7)

and

foo

is popped at the second

println

and resumed,
it will print:

Foo: 4

.

Locks acquired by a popped frame are released when it
is popped. This applies to synchronized methods that
are popped, and to any synchronized blocks within them.

Finally blocks are not executed.

No aspect of state, other than this thread's execution point and
locks, is affected by this call. Specifically, the values of
fields are unchanged, as are external resources such as
I/O streams. Additionally, the target program might be
placed in a state that is impossible with normal program flow;
for example, order of lock acquisition might be perturbed.
Thus the target program may
proceed differently than the user would expect.

The specified thread must be suspended.

All

StackFrame

objects for this thread are
invalidated.

No events are generated by this method.

None of the frames through and including the frame for the caller
of

frame

may be native.

Not all target virtual machines support this operation.
Use

VirtualMachine.canPopFrames()

to determine if the operation is supported.

The operand stack is restored, however, any changes
to the arguments that occurred in the called method, remain.
For example, if the method

foo

:

```java
void foo(int x) {
System.out.println("Foo: " + x);
x = 4;
System.out.println("pop here");
}
```

was called with

foo(7)

and

foo

is popped at the second

println

and resumed,
it will print:

Foo: 4

.

Locks acquired by a popped frame are released when it
is popped. This applies to synchronized methods that
are popped, and to any synchronized blocks within them.

Finally blocks are not executed.

No aspect of state, other than this thread's execution point and
locks, is affected by this call. Specifically, the values of
fields are unchanged, as are external resources such as
I/O streams. Additionally, the target program might be
placed in a state that is impossible with normal program flow;
for example, order of lock acquisition might be perturbed.
Thus the target program may
proceed differently than the user would expect.

The specified thread must be suspended.

All

StackFrame

objects for this thread are
invalidated.

No events are generated by this method.

None of the frames through and including the frame for the caller
of

frame

may be native.

Not all target virtual machines support this operation.
Use

VirtualMachine.canPopFrames()

to determine if the operation is supported.

void foo(int x) {
System.out.println("Foo: " + x);
x = 4;
System.out.println("pop here");
}

Locks acquired by a popped frame are released when it
is popped. This applies to synchronized methods that
are popped, and to any synchronized blocks within them.

Finally blocks are not executed.

No aspect of state, other than this thread's execution point and
locks, is affected by this call. Specifically, the values of
fields are unchanged, as are external resources such as
I/O streams. Additionally, the target program might be
placed in a state that is impossible with normal program flow;
for example, order of lock acquisition might be perturbed.
Thus the target program may
proceed differently than the user would expect.

The specified thread must be suspended.

All

StackFrame

objects for this thread are
invalidated.

No events are generated by this method.

None of the frames through and including the frame for the caller
of

frame

may be native.

Not all target virtual machines support this operation.
Use

VirtualMachine.canPopFrames()

to determine if the operation is supported.

Finally blocks are not executed.

No aspect of state, other than this thread's execution point and
locks, is affected by this call. Specifically, the values of
fields are unchanged, as are external resources such as
I/O streams. Additionally, the target program might be
placed in a state that is impossible with normal program flow;
for example, order of lock acquisition might be perturbed.
Thus the target program may
proceed differently than the user would expect.

The specified thread must be suspended.

All

StackFrame

objects for this thread are
invalidated.

No events are generated by this method.

None of the frames through and including the frame for the caller
of

frame

may be native.

Not all target virtual machines support this operation.
Use

VirtualMachine.canPopFrames()

to determine if the operation is supported.

No aspect of state, other than this thread's execution point and
locks, is affected by this call. Specifically, the values of
fields are unchanged, as are external resources such as
I/O streams. Additionally, the target program might be
placed in a state that is impossible with normal program flow;
for example, order of lock acquisition might be perturbed.
Thus the target program may
proceed differently than the user would expect.

The specified thread must be suspended.

All

StackFrame

objects for this thread are
invalidated.

No events are generated by this method.

None of the frames through and including the frame for the caller
of

frame

may be native.

Not all target virtual machines support this operation.
Use

VirtualMachine.canPopFrames()

to determine if the operation is supported.

The specified thread must be suspended.

All

StackFrame

objects for this thread are
invalidated.

No events are generated by this method.

None of the frames through and including the frame for the caller
of

frame

may be native.

Not all target virtual machines support this operation.
Use

VirtualMachine.canPopFrames()

to determine if the operation is supported.

All

StackFrame

objects for this thread are
invalidated.

No events are generated by this method.

None of the frames through and including the frame for the caller
of

frame

may be native.

Not all target virtual machines support this operation.
Use

VirtualMachine.canPopFrames()

to determine if the operation is supported.

No events are generated by this method.

None of the frames through and including the frame for the caller
of

frame

may be native.

Not all target virtual machines support this operation.
Use

VirtualMachine.canPopFrames()

to determine if the operation is supported.

None of the frames through and including the frame for the caller
of

frame

may be native.

Not all target virtual machines support this operation.
Use

VirtualMachine.canPopFrames()

to determine if the operation is supported.

Not all target virtual machines support this operation.
Use

VirtualMachine.canPopFrames()

to determine if the operation is supported.

forceEarlyReturn

```java
void forceEarlyReturn​(
Value
value)
throws
InvalidTypeException
,

ClassNotLoadedException
,

IncompatibleThreadStateException
```

Force a method to return before it reaches a return
statement.

The method which will return early is referred to as the
called method. The called method is the current method (as
defined by the Frames section in the Java Virtual Machine
Specification) for the specified thread at the time this
method is called.

The thread must be suspended.
The return occurs when execution of Java programming
language code is resumed on this thread. Between the call to
this method and resumption of thread execution, the
state of the stack is undefined.

No further instructions are executed in the called
method. Specifically, finally blocks are not executed. Note:
this can cause inconsistent states in the application.

A lock acquired by calling the called method (if it is a
synchronized method) and locks acquired by entering
synchronized blocks within the called method are
released. Note: this does not apply to native locks or
java.util.concurrent.locks locks.

Events, such as MethodExit, are generated as they would be in
a normal return.

The called method must be a non-native Java programming
language method. Forcing return on a thread with only one
frame on the stack causes the thread to exit when resumed.

The

value

argument is the value that the
method is to return.
If the return type of the method is void, then value must
be a

VoidValue

.
Object values must be assignment compatible with the method return type
(This implies that the method return type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the method return type or must be
convertible to the variable type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

Not all target virtual machines support this operation.
Use

VirtualMachine.canForceEarlyReturn()

to determine if the operation is supported.

**Parameters:** value

- the value the method is to return.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canForceEarlyReturn()
**Throws:** IncompatibleThreadStateException

- if this
thread is not suspended.
**Throws:** NativeMethodException

- if the frame to be returned from
is that of a native method.
**Throws:** InvalidStackFrameException

- if there are no frames.
**Throws:** InvalidTypeException

- if the value's type does not match
the method's return type.
**Throws:** ClassNotLoadedException

- if the method's return type has not yet
been loaded through the appropriate class loader.
**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.
**Since:** 1.6

---

#### forceEarlyReturn

void forceEarlyReturn​(

Value

value)
throws

InvalidTypeException

,

ClassNotLoadedException

,

IncompatibleThreadStateException

Force a method to return before it reaches a return
statement.

The method which will return early is referred to as the
called method. The called method is the current method (as
defined by the Frames section in the Java Virtual Machine
Specification) for the specified thread at the time this
method is called.

The thread must be suspended.
The return occurs when execution of Java programming
language code is resumed on this thread. Between the call to
this method and resumption of thread execution, the
state of the stack is undefined.

No further instructions are executed in the called
method. Specifically, finally blocks are not executed. Note:
this can cause inconsistent states in the application.

A lock acquired by calling the called method (if it is a
synchronized method) and locks acquired by entering
synchronized blocks within the called method are
released. Note: this does not apply to native locks or
java.util.concurrent.locks locks.

Events, such as MethodExit, are generated as they would be in
a normal return.

The called method must be a non-native Java programming
language method. Forcing return on a thread with only one
frame on the stack causes the thread to exit when resumed.

The

value

argument is the value that the
method is to return.
If the return type of the method is void, then value must
be a

VoidValue

.
Object values must be assignment compatible with the method return type
(This implies that the method return type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the method return type or must be
convertible to the variable type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

Not all target virtual machines support this operation.
Use

VirtualMachine.canForceEarlyReturn()

to determine if the operation is supported.

The method which will return early is referred to as the
called method. The called method is the current method (as
defined by the Frames section in the Java Virtual Machine
Specification) for the specified thread at the time this
method is called.

The thread must be suspended.
The return occurs when execution of Java programming
language code is resumed on this thread. Between the call to
this method and resumption of thread execution, the
state of the stack is undefined.

No further instructions are executed in the called
method. Specifically, finally blocks are not executed. Note:
this can cause inconsistent states in the application.

A lock acquired by calling the called method (if it is a
synchronized method) and locks acquired by entering
synchronized blocks within the called method are
released. Note: this does not apply to native locks or
java.util.concurrent.locks locks.

Events, such as MethodExit, are generated as they would be in
a normal return.

The called method must be a non-native Java programming
language method. Forcing return on a thread with only one
frame on the stack causes the thread to exit when resumed.

The

value

argument is the value that the
method is to return.
If the return type of the method is void, then value must
be a

VoidValue

.
Object values must be assignment compatible with the method return type
(This implies that the method return type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the method return type or must be
convertible to the variable type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

Not all target virtual machines support this operation.
Use

VirtualMachine.canForceEarlyReturn()

to determine if the operation is supported.

The thread must be suspended.
The return occurs when execution of Java programming
language code is resumed on this thread. Between the call to
this method and resumption of thread execution, the
state of the stack is undefined.

No further instructions are executed in the called
method. Specifically, finally blocks are not executed. Note:
this can cause inconsistent states in the application.

A lock acquired by calling the called method (if it is a
synchronized method) and locks acquired by entering
synchronized blocks within the called method are
released. Note: this does not apply to native locks or
java.util.concurrent.locks locks.

Events, such as MethodExit, are generated as they would be in
a normal return.

The called method must be a non-native Java programming
language method. Forcing return on a thread with only one
frame on the stack causes the thread to exit when resumed.

The

value

argument is the value that the
method is to return.
If the return type of the method is void, then value must
be a

VoidValue

.
Object values must be assignment compatible with the method return type
(This implies that the method return type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the method return type or must be
convertible to the variable type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

Not all target virtual machines support this operation.
Use

VirtualMachine.canForceEarlyReturn()

to determine if the operation is supported.

No further instructions are executed in the called
method. Specifically, finally blocks are not executed. Note:
this can cause inconsistent states in the application.

A lock acquired by calling the called method (if it is a
synchronized method) and locks acquired by entering
synchronized blocks within the called method are
released. Note: this does not apply to native locks or
java.util.concurrent.locks locks.

Events, such as MethodExit, are generated as they would be in
a normal return.

The called method must be a non-native Java programming
language method. Forcing return on a thread with only one
frame on the stack causes the thread to exit when resumed.

The

value

argument is the value that the
method is to return.
If the return type of the method is void, then value must
be a

VoidValue

.
Object values must be assignment compatible with the method return type
(This implies that the method return type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the method return type or must be
convertible to the variable type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

Not all target virtual machines support this operation.
Use

VirtualMachine.canForceEarlyReturn()

to determine if the operation is supported.

A lock acquired by calling the called method (if it is a
synchronized method) and locks acquired by entering
synchronized blocks within the called method are
released. Note: this does not apply to native locks or
java.util.concurrent.locks locks.

Events, such as MethodExit, are generated as they would be in
a normal return.

The called method must be a non-native Java programming
language method. Forcing return on a thread with only one
frame on the stack causes the thread to exit when resumed.

The

value

argument is the value that the
method is to return.
If the return type of the method is void, then value must
be a

VoidValue

.
Object values must be assignment compatible with the method return type
(This implies that the method return type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the method return type or must be
convertible to the variable type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

Not all target virtual machines support this operation.
Use

VirtualMachine.canForceEarlyReturn()

to determine if the operation is supported.

Events, such as MethodExit, are generated as they would be in
a normal return.

The called method must be a non-native Java programming
language method. Forcing return on a thread with only one
frame on the stack causes the thread to exit when resumed.

The

value

argument is the value that the
method is to return.
If the return type of the method is void, then value must
be a

VoidValue

.
Object values must be assignment compatible with the method return type
(This implies that the method return type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the method return type or must be
convertible to the variable type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

Not all target virtual machines support this operation.
Use

VirtualMachine.canForceEarlyReturn()

to determine if the operation is supported.

The called method must be a non-native Java programming
language method. Forcing return on a thread with only one
frame on the stack causes the thread to exit when resumed.

The

value

argument is the value that the
method is to return.
If the return type of the method is void, then value must
be a

VoidValue

.
Object values must be assignment compatible with the method return type
(This implies that the method return type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the method return type or must be
convertible to the variable type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

Not all target virtual machines support this operation.
Use

VirtualMachine.canForceEarlyReturn()

to determine if the operation is supported.

The

value

argument is the value that the
method is to return.
If the return type of the method is void, then value must
be a

VoidValue

.
Object values must be assignment compatible with the method return type
(This implies that the method return type must be loaded through the
enclosing class's class loader). Primitive values must be
either assignment compatible with the method return type or must be
convertible to the variable type without loss of information.
See JLS section 5.2 for more information on assignment
compatibility.

Not all target virtual machines support this operation.
Use

VirtualMachine.canForceEarlyReturn()

to determine if the operation is supported.

Not all target virtual machines support this operation.
Use

VirtualMachine.canForceEarlyReturn()

to determine if the operation is supported.

---

