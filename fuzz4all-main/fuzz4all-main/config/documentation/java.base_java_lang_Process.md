# Class Process

**Source:** `java.base\java\lang\Process.html`

### Class Description

```java
public abstract class
Process

extends
Object
```

Process

provides control of native processes started by
ProcessBuilder.start and Runtime.exec.
The class provides methods for performing input from the process, performing
output to the process, waiting for the process to complete,
checking the exit status of the process, and destroying (killing)
the process.
The

ProcessBuilder.start()

and

Runtime.exec

methods create a native process and return an instance of a
subclass of

Process

that can be used to control the process
and obtain information about it.

The methods that create processes may not work well for special
processes on certain native platforms, such as native windowing
processes, daemon processes, Win16/DOS processes on Microsoft
Windows, or shell scripts.

By default, the created process does not have its own terminal
or console. All its standard I/O (i.e. stdin, stdout, stderr)
operations will be redirected to the parent process, where they can
be accessed via the streams obtained using the methods

getOutputStream()

,

getInputStream()

, and

getErrorStream()

.
The parent process uses these streams to feed input to and get output
from the process. Because some native platforms only provide
limited buffer size for standard input and output streams, failure
to promptly write the input stream or read the output stream of
the process may cause the process to block, or even deadlock.

Where desired,

process I/O can also be redirected

using methods of the

ProcessBuilder

class.

The process is not killed when there are no more references to
the

Process

object, but rather the process
continues executing asynchronously.

There is no requirement that the process represented by a

Process

object execute asynchronously or concurrently with respect
to the Java process that owns the

Process

object.

As of 1.5,

ProcessBuilder.start()

is the preferred way
to create a

Process

.

Subclasses of Process should override the

onExit()

and

toHandle()

methods to provide a fully functional Process including the

process id

,

information about the process

,

direct children

, and

direct children plus descendants of those children

of the process.
Delegating to the underlying Process or ProcessHandle is typically
easiest and most efficient.

**Since:** 1.0

---

### Field Details

*No entries found.*

### Constructor Details

#### public Process()

Default constructor for Process.

---

### Method Details

#### public abstract
OutputStream
getOutputStream()

Returns the output stream connected to the normal input of the
process. Output to the stream is piped into the standard
input of the process represented by this

Process

object.

If the standard input of the process has been redirected using

ProcessBuilder.redirectInput

then this method will return a

null output stream

.

Implementation note: It is a good idea for the returned
output stream to be buffered.

**Returns:**
- the output stream connected to the normal input of the
process

---

#### public abstract
InputStream
getInputStream()

Returns the input stream connected to the normal output of the
process. The stream obtains data piped from the standard
output of the process represented by this

Process

object.

If the standard output of the process has been redirected using

ProcessBuilder.redirectOutput

then this method will return a

null input stream

.

Otherwise, if the standard error of the process has been
redirected using

ProcessBuilder.redirectErrorStream

then the input stream returned by this method will receive the
merged standard output and the standard error of the process.

Implementation note: It is a good idea for the returned
input stream to be buffered.

**Returns:**
- the input stream connected to the normal output of the
process

---

#### public abstract
InputStream
getErrorStream()

Returns the input stream connected to the error output of the
process. The stream obtains data piped from the error output
of the process represented by this

Process

object.

If the standard error of the process has been redirected using

ProcessBuilder.redirectError

or

ProcessBuilder.redirectErrorStream

then this method will return a

null input stream

.

Implementation note: It is a good idea for the returned
input stream to be buffered.

**Returns:**
- the input stream connected to the error output of
the process

---

#### public abstract int waitFor()
throws
InterruptedException

Causes the current thread to wait, if necessary, until the
process represented by this

Process

object has
terminated. This method returns immediately if the process
has already terminated. If the process has not yet
terminated, the calling thread will be blocked until the
process exits.

**Returns:**
- the exit value of the process represented by this

Process

object. By convention, the value

0

indicates normal termination.

**Throws:**
- InterruptedException

- if the current thread is

interrupted

by another
thread while it is waiting, then the wait is ended and
an

InterruptedException

is thrown.

---

#### public boolean waitFor​(long timeout,

TimeUnit
unit)
throws
InterruptedException

Causes the current thread to wait, if necessary, until the
process represented by this

Process

object has
terminated, or the specified waiting time elapses.

If the process has already terminated then this method returns
immediately with the value

true

. If the process has not
terminated and the timeout value is less than, or equal to, zero, then
this method returns immediately with the value

false

.

The default implementation of this methods polls the

exitValue

to check if the process has terminated. Concrete implementations of this
class are strongly encouraged to override this method with a more
efficient implementation.

**Parameters:**
- timeout

- the maximum time to wait
- unit

- the time unit of the

timeout

argument

**Returns:**
- true

if the process has exited and

false

if
the waiting time elapsed before the process has exited.

**Throws:**
- InterruptedException

- if the current thread is interrupted
while waiting.
- NullPointerException

- if unit is null

**Since:**
- 1.8

---

#### public abstract int exitValue()

Returns the exit value for the process.

**Returns:**
- the exit value of the process represented by this

Process

object. By convention, the value

0

indicates normal termination.

**Throws:**
- IllegalThreadStateException

- if the process represented
by this

Process

object has not yet terminated

---

#### public abstract void destroy()

Kills the process.
Whether the process represented by this

Process

object is

normally terminated

or not is
implementation dependent.
Forcible process destruction is defined as the immediate termination of a
process, whereas normal termination allows the process to shut down cleanly.
If the process is not alive, no action is taken.

The

CompletableFuture

from

onExit()

is

completed

when the process has terminated.

---

#### public
Process
destroyForcibly()

Kills the process forcibly. The process represented by this

Process

object is forcibly terminated.
Forcible process destruction is defined as the immediate termination of a
process, whereas normal termination allows the process to shut down cleanly.
If the process is not alive, no action is taken.

The

CompletableFuture

from

onExit()

is

completed

when the process has terminated.

Invoking this method on

Process

objects returned by

ProcessBuilder.start()

and

Runtime.exec(java.lang.String)

forcibly terminate
the process.

**Returns:**
- the

Process

object representing the
process forcibly destroyed

**Since:**
- 1.8

**API Note:**
- The process may not terminate immediately.
i.e.

isAlive()

may return true for a brief period
after

destroyForcibly()

is called. This method
may be chained to

waitFor()

if needed.

**Implementation Requirements:**
- The default implementation of this method invokes

destroy()

and so may not forcibly terminate the process.

**Implementation Note:**
- Concrete implementations of this class are strongly encouraged to override
this method with a compliant implementation.

---

#### public boolean supportsNormalTermination()

Returns

true

if the implementation of

destroy()

is to
normally terminate the process,
Returns

false

if the implementation of

destroy

forcibly and immediately terminates the process.

Invoking this method on

Process

objects returned by

ProcessBuilder.start()

and

Runtime.exec(java.lang.String)

return

true

or

false

depending on the platform implementation.

**Returns:**
- true

if the implementation of

destroy()

is to
normally terminate the process;
otherwise,

destroy()

forcibly terminates the process

**Throws:**
- UnsupportedOperationException

- if the Process implementation
does not support this operation

**Since:**
- 9

**Implementation Requirements:**
- This implementation throws an instance of

UnsupportedOperationException

and performs no other action.

---

#### public boolean isAlive()

Tests whether the process represented by this

Process

is
alive.

**Returns:**
- true

if the process represented by this

Process

object has not yet terminated.

**Since:**
- 1.8

---

#### public long pid()

Returns the native process ID of the process.
The native process ID is an identification number that the operating
system assigns to the process.

**Returns:**
- the native process id of the process

**Throws:**
- UnsupportedOperationException

- if the Process implementation
does not support this operation

**Since:**
- 9

**Implementation Requirements:**
- The implementation of this method returns the process id as:

toHandle().pid()

.

---

#### public
CompletableFuture
<
Process
> onExit()

Returns a

CompletableFuture<Process>

for the termination of the Process.
The

CompletableFuture

provides the ability
to trigger dependent functions or actions that may be run synchronously
or asynchronously upon process termination.
When the process has terminated the CompletableFuture is

completed

regardless
of the exit status of the process.

Calling

onExit().get()

waits for the process to terminate and returns
the Process. The future can be used to check if the process is

done

or to

wait

for it to terminate.

Cancelling

the CompletableFuture does not affect the Process.

Processes returned from

ProcessBuilder.start()

override the
default implementation to provide an efficient mechanism to wait
for process exit.

**Returns:**
- a new

CompletableFuture<Process>

for the Process

**Since:**
- 9

**API Note:**
- Using

onExit

is an alternative to

waitFor

that enables both additional concurrency
and convenient access to the result of the Process.
Lambda expressions can be used to evaluate the result of the Process
execution.
If there is other processing to be done before the value is used
then

onExit

is a convenient mechanism to
free the current thread and block only if and when the value is needed.

For example, launching a process to compare two files and get a boolean if they are identical:

```java
Process p = new ProcessBuilder("cmp", "f1", "f2").start();
Future<Boolean> identical = p.onExit().thenApply(p1 -> p1.exitValue() == 0);
...
if (identical.get()) { ... }
```

, The process may be observed to have terminated with

isAlive()

before the ComputableFuture is completed and dependent actions are invoked.

**Implementation Requirements:**
- This implementation executes

waitFor()

in a separate thread
repeatedly until it returns successfully. If the execution of

waitFor

is interrupted, the thread's interrupt status is preserved.

When

waitFor()

returns successfully the CompletableFuture is

completed

regardless
of the exit status of the process.

This implementation may consume a lot of memory for thread stacks if a
large number of processes are waited for concurrently.

External implementations should override this method and provide
a more efficient implementation. For example, to delegate to the underlying
process, it can do the following:

```java
public CompletableFuture<Process> onExit() {
return delegate.onExit().thenApply(p -> this);
}
```

---

#### public
ProcessHandle
toHandle()

Returns a ProcessHandle for the Process.

Process

objects returned by

ProcessBuilder.start()

and

Runtime.exec(java.lang.String)

implement

toHandle

as the equivalent of

ProcessHandle.of(pid)

including the
check for a SecurityManager and

RuntimePermission("manageProcess")

.

**Returns:**
- Returns a ProcessHandle for the Process

**Throws:**
- UnsupportedOperationException

- if the Process implementation
does not support this operation
- SecurityException

- if a security manager has been installed and
it denies RuntimePermission("manageProcess")

**Since:**
- 9

**Implementation Requirements:**
- This implementation throws an instance of

UnsupportedOperationException

and performs no other action.
Subclasses should override this method to provide a ProcessHandle for the
process. The methods

pid()

,

info()

,

children()

,
and

descendants()

, unless overridden, operate on the ProcessHandle.

---

#### public
ProcessHandle.Info
info()

Returns a snapshot of information about the process.

A

ProcessHandle.Info

instance has accessor methods
that return information about the process if it is available.

**Returns:**
- a snapshot of information about the process, always non-null

**Throws:**
- UnsupportedOperationException

- if the Process implementation
does not support this operation

**Since:**
- 9

**Implementation Requirements:**
- This implementation returns information about the process as:

toHandle().info()

.

---

#### public
Stream
<
ProcessHandle
> children()

Returns a snapshot of the direct children of the process.
The parent of a direct child process is the process.
Typically, a process that is

not alive

has no children.

Note that processes are created and terminate asynchronously.
There is no guarantee that a process is

alive

.

**Returns:**
- a sequential Stream of ProcessHandles for processes that are
direct children of the process

**Throws:**
- UnsupportedOperationException

- if the Process implementation
does not support this operation
- SecurityException

- if a security manager has been installed and
it denies RuntimePermission("manageProcess")

**Since:**
- 9

**Implementation Requirements:**
- This implementation returns the direct children as:

toHandle().children()

.

---

#### public
Stream
<
ProcessHandle
> descendants()

Returns a snapshot of the descendants of the process.
The descendants of a process are the children of the process
plus the descendants of those children, recursively.
Typically, a process that is

not alive

has no children.

Note that processes are created and terminate asynchronously.
There is no guarantee that a process is

alive

.

**Returns:**
- a sequential Stream of ProcessHandles for processes that
are descendants of the process

**Throws:**
- UnsupportedOperationException

- if the Process implementation
does not support this operation
- SecurityException

- if a security manager has been installed and
it denies RuntimePermission("manageProcess")

**Since:**
- 9

**Implementation Requirements:**
- This implementation returns all children as:

toHandle().descendants()

.

---

### Additional Sections

#### Class Process

java.lang.Object

- java.lang.Process

java.lang.Process

```java
public abstract class
Process

extends
Object
```

Process

provides control of native processes started by
ProcessBuilder.start and Runtime.exec.
The class provides methods for performing input from the process, performing
output to the process, waiting for the process to complete,
checking the exit status of the process, and destroying (killing)
the process.
The

ProcessBuilder.start()

and

Runtime.exec

methods create a native process and return an instance of a
subclass of

Process

that can be used to control the process
and obtain information about it.

The methods that create processes may not work well for special
processes on certain native platforms, such as native windowing
processes, daemon processes, Win16/DOS processes on Microsoft
Windows, or shell scripts.

By default, the created process does not have its own terminal
or console. All its standard I/O (i.e. stdin, stdout, stderr)
operations will be redirected to the parent process, where they can
be accessed via the streams obtained using the methods

getOutputStream()

,

getInputStream()

, and

getErrorStream()

.
The parent process uses these streams to feed input to and get output
from the process. Because some native platforms only provide
limited buffer size for standard input and output streams, failure
to promptly write the input stream or read the output stream of
the process may cause the process to block, or even deadlock.

Where desired,

process I/O can also be redirected

using methods of the

ProcessBuilder

class.

The process is not killed when there are no more references to
the

Process

object, but rather the process
continues executing asynchronously.

There is no requirement that the process represented by a

Process

object execute asynchronously or concurrently with respect
to the Java process that owns the

Process

object.

As of 1.5,

ProcessBuilder.start()

is the preferred way
to create a

Process

.

Subclasses of Process should override the

onExit()

and

toHandle()

methods to provide a fully functional Process including the

process id

,

information about the process

,

direct children

, and

direct children plus descendants of those children

of the process.
Delegating to the underlying Process or ProcessHandle is typically
easiest and most efficient.

**Since:** 1.0

public abstract class

Process

extends

Object

Process

provides control of native processes started by
ProcessBuilder.start and Runtime.exec.
The class provides methods for performing input from the process, performing
output to the process, waiting for the process to complete,
checking the exit status of the process, and destroying (killing)
the process.
The

ProcessBuilder.start()

and

Runtime.exec

methods create a native process and return an instance of a
subclass of

Process

that can be used to control the process
and obtain information about it.

The methods that create processes may not work well for special
processes on certain native platforms, such as native windowing
processes, daemon processes, Win16/DOS processes on Microsoft
Windows, or shell scripts.

By default, the created process does not have its own terminal
or console. All its standard I/O (i.e. stdin, stdout, stderr)
operations will be redirected to the parent process, where they can
be accessed via the streams obtained using the methods

getOutputStream()

,

getInputStream()

, and

getErrorStream()

.
The parent process uses these streams to feed input to and get output
from the process. Because some native platforms only provide
limited buffer size for standard input and output streams, failure
to promptly write the input stream or read the output stream of
the process may cause the process to block, or even deadlock.

Where desired,

process I/O can also be redirected

using methods of the

ProcessBuilder

class.

The process is not killed when there are no more references to
the

Process

object, but rather the process
continues executing asynchronously.

There is no requirement that the process represented by a

Process

object execute asynchronously or concurrently with respect
to the Java process that owns the

Process

object.

As of 1.5,

ProcessBuilder.start()

is the preferred way
to create a

Process

.

Subclasses of Process should override the

onExit()

and

toHandle()

methods to provide a fully functional Process including the

process id

,

information about the process

,

direct children

, and

direct children plus descendants of those children

of the process.
Delegating to the underlying Process or ProcessHandle is typically
easiest and most efficient.

The methods that create processes may not work well for special
processes on certain native platforms, such as native windowing
processes, daemon processes, Win16/DOS processes on Microsoft
Windows, or shell scripts.

By default, the created process does not have its own terminal
or console. All its standard I/O (i.e. stdin, stdout, stderr)
operations will be redirected to the parent process, where they can
be accessed via the streams obtained using the methods

getOutputStream()

,

getInputStream()

, and

getErrorStream()

.
The parent process uses these streams to feed input to and get output
from the process. Because some native platforms only provide
limited buffer size for standard input and output streams, failure
to promptly write the input stream or read the output stream of
the process may cause the process to block, or even deadlock.

Where desired,

process I/O can also be redirected

using methods of the

ProcessBuilder

class.

The process is not killed when there are no more references to
the

Process

object, but rather the process
continues executing asynchronously.

There is no requirement that the process represented by a

Process

object execute asynchronously or concurrently with respect
to the Java process that owns the

Process

object.

As of 1.5,

ProcessBuilder.start()

is the preferred way
to create a

Process

.

Subclasses of Process should override the

onExit()

and

toHandle()

methods to provide a fully functional Process including the

process id

,

information about the process

,

direct children

, and

direct children plus descendants of those children

of the process.
Delegating to the underlying Process or ProcessHandle is typically
easiest and most efficient.

By default, the created process does not have its own terminal
or console. All its standard I/O (i.e. stdin, stdout, stderr)
operations will be redirected to the parent process, where they can
be accessed via the streams obtained using the methods

getOutputStream()

,

getInputStream()

, and

getErrorStream()

.
The parent process uses these streams to feed input to and get output
from the process. Because some native platforms only provide
limited buffer size for standard input and output streams, failure
to promptly write the input stream or read the output stream of
the process may cause the process to block, or even deadlock.

Where desired,

process I/O can also be redirected

using methods of the

ProcessBuilder

class.

The process is not killed when there are no more references to
the

Process

object, but rather the process
continues executing asynchronously.

There is no requirement that the process represented by a

Process

object execute asynchronously or concurrently with respect
to the Java process that owns the

Process

object.

As of 1.5,

ProcessBuilder.start()

is the preferred way
to create a

Process

.

Subclasses of Process should override the

onExit()

and

toHandle()

methods to provide a fully functional Process including the

process id

,

information about the process

,

direct children

, and

direct children plus descendants of those children

of the process.
Delegating to the underlying Process or ProcessHandle is typically
easiest and most efficient.

Where desired,

process I/O can also be redirected

using methods of the

ProcessBuilder

class.

The process is not killed when there are no more references to
the

Process

object, but rather the process
continues executing asynchronously.

There is no requirement that the process represented by a

Process

object execute asynchronously or concurrently with respect
to the Java process that owns the

Process

object.

As of 1.5,

ProcessBuilder.start()

is the preferred way
to create a

Process

.

Subclasses of Process should override the

onExit()

and

toHandle()

methods to provide a fully functional Process including the

process id

,

information about the process

,

direct children

, and

direct children plus descendants of those children

of the process.
Delegating to the underlying Process or ProcessHandle is typically
easiest and most efficient.

The process is not killed when there are no more references to
the

Process

object, but rather the process
continues executing asynchronously.

There is no requirement that the process represented by a

Process

object execute asynchronously or concurrently with respect
to the Java process that owns the

Process

object.

As of 1.5,

ProcessBuilder.start()

is the preferred way
to create a

Process

.

Subclasses of Process should override the

onExit()

and

toHandle()

methods to provide a fully functional Process including the

process id

,

information about the process

,

direct children

, and

direct children plus descendants of those children

of the process.
Delegating to the underlying Process or ProcessHandle is typically
easiest and most efficient.

There is no requirement that the process represented by a

Process

object execute asynchronously or concurrently with respect
to the Java process that owns the

Process

object.

As of 1.5,

ProcessBuilder.start()

is the preferred way
to create a

Process

.

Subclasses of Process should override the

onExit()

and

toHandle()

methods to provide a fully functional Process including the

process id

,

information about the process

,

direct children

, and

direct children plus descendants of those children

of the process.
Delegating to the underlying Process or ProcessHandle is typically
easiest and most efficient.

As of 1.5,

ProcessBuilder.start()

is the preferred way
to create a

Process

.

Subclasses of Process should override the

onExit()

and

toHandle()

methods to provide a fully functional Process including the

process id

,

information about the process

,

direct children

, and

direct children plus descendants of those children

of the process.
Delegating to the underlying Process or ProcessHandle is typically
easiest and most efficient.

Subclasses of Process should override the

onExit()

and

toHandle()

methods to provide a fully functional Process including the

process id

,

information about the process

,

direct children

, and

direct children plus descendants of those children

of the process.
Delegating to the underlying Process or ProcessHandle is typically
easiest and most efficient.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Process

()

Default constructor for Process.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

Stream

<

ProcessHandle

>

children

()

Returns a snapshot of the direct children of the process.

Stream

<

ProcessHandle

>

descendants

()

Returns a snapshot of the descendants of the process.

abstract void

destroy

()

Kills the process.

Process

destroyForcibly

()

Kills the process forcibly.

abstract int

exitValue

()

Returns the exit value for the process.

abstract

InputStream

getErrorStream

()

Returns the input stream connected to the error output of the
process.

abstract

InputStream

getInputStream

()

Returns the input stream connected to the normal output of the
process.

abstract

OutputStream

getOutputStream

()

Returns the output stream connected to the normal input of the
process.

ProcessHandle.Info

info

()

Returns a snapshot of information about the process.

boolean

isAlive

()

Tests whether the process represented by this

Process

is
alive.

CompletableFuture

<

Process

>

onExit

()

Returns a

CompletableFuture<Process>

for the termination of the Process.

long

pid

()

Returns the native process ID of the process.

boolean

supportsNormalTermination

()

Returns

true

if the implementation of

destroy()

is to
normally terminate the process,
Returns

false

if the implementation of

destroy

forcibly and immediately terminates the process.

ProcessHandle

toHandle

()

Returns a ProcessHandle for the Process.

abstract int

waitFor

()

Causes the current thread to wait, if necessary, until the
process represented by this

Process

object has
terminated.

boolean

waitFor

​(long timeout,

TimeUnit

unit)

Causes the current thread to wait, if necessary, until the
process represented by this

Process

object has
terminated, or the specified waiting time elapses.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

Process

()

Default constructor for Process.

---

#### Constructor Summary

Default constructor for Process.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

Stream

<

ProcessHandle

>

children

()

Returns a snapshot of the direct children of the process.

Stream

<

ProcessHandle

>

descendants

()

Returns a snapshot of the descendants of the process.

abstract void

destroy

()

Kills the process.

Process

destroyForcibly

()

Kills the process forcibly.

abstract int

exitValue

()

Returns the exit value for the process.

abstract

InputStream

getErrorStream

()

Returns the input stream connected to the error output of the
process.

abstract

InputStream

getInputStream

()

Returns the input stream connected to the normal output of the
process.

abstract

OutputStream

getOutputStream

()

Returns the output stream connected to the normal input of the
process.

ProcessHandle.Info

info

()

Returns a snapshot of information about the process.

boolean

isAlive

()

Tests whether the process represented by this

Process

is
alive.

CompletableFuture

<

Process

>

onExit

()

Returns a

CompletableFuture<Process>

for the termination of the Process.

long

pid

()

Returns the native process ID of the process.

boolean

supportsNormalTermination

()

Returns

true

if the implementation of

destroy()

is to
normally terminate the process,
Returns

false

if the implementation of

destroy

forcibly and immediately terminates the process.

ProcessHandle

toHandle

()

Returns a ProcessHandle for the Process.

abstract int

waitFor

()

Causes the current thread to wait, if necessary, until the
process represented by this

Process

object has
terminated.

boolean

waitFor

​(long timeout,

TimeUnit

unit)

Causes the current thread to wait, if necessary, until the
process represented by this

Process

object has
terminated, or the specified waiting time elapses.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns a snapshot of the direct children of the process.

Returns a snapshot of the descendants of the process.

Kills the process.

Kills the process forcibly.

Returns the exit value for the process.

Returns the input stream connected to the error output of the
process.

Returns the input stream connected to the normal output of the
process.

Returns the output stream connected to the normal input of the
process.

Returns a snapshot of information about the process.

Tests whether the process represented by this

Process

is
alive.

Returns a

CompletableFuture<Process>

for the termination of the Process.

Returns the native process ID of the process.

Returns

true

if the implementation of

destroy()

is to
normally terminate the process,
Returns

false

if the implementation of

destroy

forcibly and immediately terminates the process.

Returns a ProcessHandle for the Process.

Causes the current thread to wait, if necessary, until the
process represented by this

Process

object has
terminated.

Causes the current thread to wait, if necessary, until the
process represented by this

Process

object has
terminated, or the specified waiting time elapses.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Process

```java
public Process()
```

Default constructor for Process.

============ METHOD DETAIL ==========

- Method Detail

- getOutputStream

```java
public abstract
OutputStream
getOutputStream()
```

Returns the output stream connected to the normal input of the
process. Output to the stream is piped into the standard
input of the process represented by this

Process

object.

If the standard input of the process has been redirected using

ProcessBuilder.redirectInput

then this method will return a

null output stream

.

Implementation note: It is a good idea for the returned
output stream to be buffered.

**Returns:** the output stream connected to the normal input of the
process

- getInputStream

```java
public abstract
InputStream
getInputStream()
```

Returns the input stream connected to the normal output of the
process. The stream obtains data piped from the standard
output of the process represented by this

Process

object.

If the standard output of the process has been redirected using

ProcessBuilder.redirectOutput

then this method will return a

null input stream

.

Otherwise, if the standard error of the process has been
redirected using

ProcessBuilder.redirectErrorStream

then the input stream returned by this method will receive the
merged standard output and the standard error of the process.

Implementation note: It is a good idea for the returned
input stream to be buffered.

**Returns:** the input stream connected to the normal output of the
process

- getErrorStream

```java
public abstract
InputStream
getErrorStream()
```

Returns the input stream connected to the error output of the
process. The stream obtains data piped from the error output
of the process represented by this

Process

object.

If the standard error of the process has been redirected using

ProcessBuilder.redirectError

or

ProcessBuilder.redirectErrorStream

then this method will return a

null input stream

.

Implementation note: It is a good idea for the returned
input stream to be buffered.

**Returns:** the input stream connected to the error output of
the process

- waitFor

```java
public abstract int waitFor()
throws
InterruptedException
```

Causes the current thread to wait, if necessary, until the
process represented by this

Process

object has
terminated. This method returns immediately if the process
has already terminated. If the process has not yet
terminated, the calling thread will be blocked until the
process exits.

**Returns:** the exit value of the process represented by this

Process

object. By convention, the value

0

indicates normal termination.
**Throws:** InterruptedException

- if the current thread is

interrupted

by another
thread while it is waiting, then the wait is ended and
an

InterruptedException

is thrown.

- waitFor

```java
public boolean waitFor​(long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Causes the current thread to wait, if necessary, until the
process represented by this

Process

object has
terminated, or the specified waiting time elapses.

If the process has already terminated then this method returns
immediately with the value

true

. If the process has not
terminated and the timeout value is less than, or equal to, zero, then
this method returns immediately with the value

false

.

The default implementation of this methods polls the

exitValue

to check if the process has terminated. Concrete implementations of this
class are strongly encouraged to override this method with a more
efficient implementation.

**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the

timeout

argument
**Returns:** true

if the process has exited and

false

if
the waiting time elapsed before the process has exited.
**Throws:** InterruptedException

- if the current thread is interrupted
while waiting.
**Throws:** NullPointerException

- if unit is null
**Since:** 1.8

- exitValue

```java
public abstract int exitValue()
```

Returns the exit value for the process.

**Returns:** the exit value of the process represented by this

Process

object. By convention, the value

0

indicates normal termination.
**Throws:** IllegalThreadStateException

- if the process represented
by this

Process

object has not yet terminated

- destroy

```java
public abstract void destroy()
```

Kills the process.
Whether the process represented by this

Process

object is

normally terminated

or not is
implementation dependent.
Forcible process destruction is defined as the immediate termination of a
process, whereas normal termination allows the process to shut down cleanly.
If the process is not alive, no action is taken.

The

CompletableFuture

from

onExit()

is

completed

when the process has terminated.

- destroyForcibly

```java
public
Process
destroyForcibly()
```

Kills the process forcibly. The process represented by this

Process

object is forcibly terminated.
Forcible process destruction is defined as the immediate termination of a
process, whereas normal termination allows the process to shut down cleanly.
If the process is not alive, no action is taken.

The

CompletableFuture

from

onExit()

is

completed

when the process has terminated.

Invoking this method on

Process

objects returned by

ProcessBuilder.start()

and

Runtime.exec(java.lang.String)

forcibly terminate
the process.

**API Note:** The process may not terminate immediately.
i.e.

isAlive()

may return true for a brief period
after

destroyForcibly()

is called. This method
may be chained to

waitFor()

if needed.
**Implementation Requirements:** The default implementation of this method invokes

destroy()

and so may not forcibly terminate the process.
**Implementation Note:** Concrete implementations of this class are strongly encouraged to override
this method with a compliant implementation.
**Returns:** the

Process

object representing the
process forcibly destroyed
**Since:** 1.8

- supportsNormalTermination

```java
public boolean supportsNormalTermination()
```

Returns

true

if the implementation of

destroy()

is to
normally terminate the process,
Returns

false

if the implementation of

destroy

forcibly and immediately terminates the process.

Invoking this method on

Process

objects returned by

ProcessBuilder.start()

and

Runtime.exec(java.lang.String)

return

true

or

false

depending on the platform implementation.

**Implementation Requirements:** This implementation throws an instance of

UnsupportedOperationException

and performs no other action.
**Returns:** true

if the implementation of

destroy()

is to
normally terminate the process;
otherwise,

destroy()

forcibly terminates the process
**Throws:** UnsupportedOperationException

- if the Process implementation
does not support this operation
**Since:** 9

- isAlive

```java
public boolean isAlive()
```

Tests whether the process represented by this

Process

is
alive.

**Returns:** true

if the process represented by this

Process

object has not yet terminated.
**Since:** 1.8

- pid

```java
public long pid()
```

Returns the native process ID of the process.
The native process ID is an identification number that the operating
system assigns to the process.

**Implementation Requirements:** The implementation of this method returns the process id as:

toHandle().pid()

.
**Returns:** the native process id of the process
**Throws:** UnsupportedOperationException

- if the Process implementation
does not support this operation
**Since:** 9

- onExit

```java
public
CompletableFuture
<
Process
> onExit()
```

Returns a

CompletableFuture<Process>

for the termination of the Process.
The

CompletableFuture

provides the ability
to trigger dependent functions or actions that may be run synchronously
or asynchronously upon process termination.
When the process has terminated the CompletableFuture is

completed

regardless
of the exit status of the process.

Calling

onExit().get()

waits for the process to terminate and returns
the Process. The future can be used to check if the process is

done

or to

wait

for it to terminate.

Cancelling

the CompletableFuture does not affect the Process.

Processes returned from

ProcessBuilder.start()

override the
default implementation to provide an efficient mechanism to wait
for process exit.

**API Note:** Using

onExit

is an alternative to

waitFor

that enables both additional concurrency
and convenient access to the result of the Process.
Lambda expressions can be used to evaluate the result of the Process
execution.
If there is other processing to be done before the value is used
then

onExit

is a convenient mechanism to
free the current thread and block only if and when the value is needed.

For example, launching a process to compare two files and get a boolean if they are identical:

```java
Process p = new ProcessBuilder("cmp", "f1", "f2").start();
Future<Boolean> identical = p.onExit().thenApply(p1 -> p1.exitValue() == 0);
...
if (identical.get()) { ... }
```

, The process may be observed to have terminated with

isAlive()

before the ComputableFuture is completed and dependent actions are invoked.
**Implementation Requirements:** This implementation executes

waitFor()

in a separate thread
repeatedly until it returns successfully. If the execution of

waitFor

is interrupted, the thread's interrupt status is preserved.

When

waitFor()

returns successfully the CompletableFuture is

completed

regardless
of the exit status of the process.

This implementation may consume a lot of memory for thread stacks if a
large number of processes are waited for concurrently.

External implementations should override this method and provide
a more efficient implementation. For example, to delegate to the underlying
process, it can do the following:

```java
public CompletableFuture<Process> onExit() {
return delegate.onExit().thenApply(p -> this);
}
```
**Returns:** a new

CompletableFuture<Process>

for the Process
**Since:** 9

- toHandle

```java
public
ProcessHandle
toHandle()
```

Returns a ProcessHandle for the Process.

Process

objects returned by

ProcessBuilder.start()

and

Runtime.exec(java.lang.String)

implement

toHandle

as the equivalent of

ProcessHandle.of(pid)

including the
check for a SecurityManager and

RuntimePermission("manageProcess")

.

**Implementation Requirements:** This implementation throws an instance of

UnsupportedOperationException

and performs no other action.
Subclasses should override this method to provide a ProcessHandle for the
process. The methods

pid()

,

info()

,

children()

,
and

descendants()

, unless overridden, operate on the ProcessHandle.
**Returns:** Returns a ProcessHandle for the Process
**Throws:** UnsupportedOperationException

- if the Process implementation
does not support this operation
**Throws:** SecurityException

- if a security manager has been installed and
it denies RuntimePermission("manageProcess")
**Since:** 9

- info

```java
public
ProcessHandle.Info
info()
```

Returns a snapshot of information about the process.

A

ProcessHandle.Info

instance has accessor methods
that return information about the process if it is available.

**Implementation Requirements:** This implementation returns information about the process as:

toHandle().info()

.
**Returns:** a snapshot of information about the process, always non-null
**Throws:** UnsupportedOperationException

- if the Process implementation
does not support this operation
**Since:** 9

- children

```java
public
Stream
<
ProcessHandle
> children()
```

Returns a snapshot of the direct children of the process.
The parent of a direct child process is the process.
Typically, a process that is

not alive

has no children.

Note that processes are created and terminate asynchronously.
There is no guarantee that a process is

alive

.

**Implementation Requirements:** This implementation returns the direct children as:

toHandle().children()

.
**Returns:** a sequential Stream of ProcessHandles for processes that are
direct children of the process
**Throws:** UnsupportedOperationException

- if the Process implementation
does not support this operation
**Throws:** SecurityException

- if a security manager has been installed and
it denies RuntimePermission("manageProcess")
**Since:** 9

- descendants

```java
public
Stream
<
ProcessHandle
> descendants()
```

Returns a snapshot of the descendants of the process.
The descendants of a process are the children of the process
plus the descendants of those children, recursively.
Typically, a process that is

not alive

has no children.

Note that processes are created and terminate asynchronously.
There is no guarantee that a process is

alive

.

**Implementation Requirements:** This implementation returns all children as:

toHandle().descendants()

.
**Returns:** a sequential Stream of ProcessHandles for processes that
are descendants of the process
**Throws:** UnsupportedOperationException

- if the Process implementation
does not support this operation
**Throws:** SecurityException

- if a security manager has been installed and
it denies RuntimePermission("manageProcess")
**Since:** 9

Constructor Detail

- Process

```java
public Process()
```

Default constructor for Process.

---

#### Constructor Detail

Process

```java
public Process()
```

Default constructor for Process.

---

#### Process

public Process()

Default constructor for Process.

Method Detail

- getOutputStream

```java
public abstract
OutputStream
getOutputStream()
```

Returns the output stream connected to the normal input of the
process. Output to the stream is piped into the standard
input of the process represented by this

Process

object.

If the standard input of the process has been redirected using

ProcessBuilder.redirectInput

then this method will return a

null output stream

.

Implementation note: It is a good idea for the returned
output stream to be buffered.

**Returns:** the output stream connected to the normal input of the
process

- getInputStream

```java
public abstract
InputStream
getInputStream()
```

Returns the input stream connected to the normal output of the
process. The stream obtains data piped from the standard
output of the process represented by this

Process

object.

If the standard output of the process has been redirected using

ProcessBuilder.redirectOutput

then this method will return a

null input stream

.

Otherwise, if the standard error of the process has been
redirected using

ProcessBuilder.redirectErrorStream

then the input stream returned by this method will receive the
merged standard output and the standard error of the process.

Implementation note: It is a good idea for the returned
input stream to be buffered.

**Returns:** the input stream connected to the normal output of the
process

- getErrorStream

```java
public abstract
InputStream
getErrorStream()
```

Returns the input stream connected to the error output of the
process. The stream obtains data piped from the error output
of the process represented by this

Process

object.

If the standard error of the process has been redirected using

ProcessBuilder.redirectError

or

ProcessBuilder.redirectErrorStream

then this method will return a

null input stream

.

Implementation note: It is a good idea for the returned
input stream to be buffered.

**Returns:** the input stream connected to the error output of
the process

- waitFor

```java
public abstract int waitFor()
throws
InterruptedException
```

Causes the current thread to wait, if necessary, until the
process represented by this

Process

object has
terminated. This method returns immediately if the process
has already terminated. If the process has not yet
terminated, the calling thread will be blocked until the
process exits.

**Returns:** the exit value of the process represented by this

Process

object. By convention, the value

0

indicates normal termination.
**Throws:** InterruptedException

- if the current thread is

interrupted

by another
thread while it is waiting, then the wait is ended and
an

InterruptedException

is thrown.

- waitFor

```java
public boolean waitFor​(long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Causes the current thread to wait, if necessary, until the
process represented by this

Process

object has
terminated, or the specified waiting time elapses.

If the process has already terminated then this method returns
immediately with the value

true

. If the process has not
terminated and the timeout value is less than, or equal to, zero, then
this method returns immediately with the value

false

.

The default implementation of this methods polls the

exitValue

to check if the process has terminated. Concrete implementations of this
class are strongly encouraged to override this method with a more
efficient implementation.

**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the

timeout

argument
**Returns:** true

if the process has exited and

false

if
the waiting time elapsed before the process has exited.
**Throws:** InterruptedException

- if the current thread is interrupted
while waiting.
**Throws:** NullPointerException

- if unit is null
**Since:** 1.8

- exitValue

```java
public abstract int exitValue()
```

Returns the exit value for the process.

**Returns:** the exit value of the process represented by this

Process

object. By convention, the value

0

indicates normal termination.
**Throws:** IllegalThreadStateException

- if the process represented
by this

Process

object has not yet terminated

- destroy

```java
public abstract void destroy()
```

Kills the process.
Whether the process represented by this

Process

object is

normally terminated

or not is
implementation dependent.
Forcible process destruction is defined as the immediate termination of a
process, whereas normal termination allows the process to shut down cleanly.
If the process is not alive, no action is taken.

The

CompletableFuture

from

onExit()

is

completed

when the process has terminated.

- destroyForcibly

```java
public
Process
destroyForcibly()
```

Kills the process forcibly. The process represented by this

Process

object is forcibly terminated.
Forcible process destruction is defined as the immediate termination of a
process, whereas normal termination allows the process to shut down cleanly.
If the process is not alive, no action is taken.

The

CompletableFuture

from

onExit()

is

completed

when the process has terminated.

Invoking this method on

Process

objects returned by

ProcessBuilder.start()

and

Runtime.exec(java.lang.String)

forcibly terminate
the process.

**API Note:** The process may not terminate immediately.
i.e.

isAlive()

may return true for a brief period
after

destroyForcibly()

is called. This method
may be chained to

waitFor()

if needed.
**Implementation Requirements:** The default implementation of this method invokes

destroy()

and so may not forcibly terminate the process.
**Implementation Note:** Concrete implementations of this class are strongly encouraged to override
this method with a compliant implementation.
**Returns:** the

Process

object representing the
process forcibly destroyed
**Since:** 1.8

- supportsNormalTermination

```java
public boolean supportsNormalTermination()
```

Returns

true

if the implementation of

destroy()

is to
normally terminate the process,
Returns

false

if the implementation of

destroy

forcibly and immediately terminates the process.

Invoking this method on

Process

objects returned by

ProcessBuilder.start()

and

Runtime.exec(java.lang.String)

return

true

or

false

depending on the platform implementation.

**Implementation Requirements:** This implementation throws an instance of

UnsupportedOperationException

and performs no other action.
**Returns:** true

if the implementation of

destroy()

is to
normally terminate the process;
otherwise,

destroy()

forcibly terminates the process
**Throws:** UnsupportedOperationException

- if the Process implementation
does not support this operation
**Since:** 9

- isAlive

```java
public boolean isAlive()
```

Tests whether the process represented by this

Process

is
alive.

**Returns:** true

if the process represented by this

Process

object has not yet terminated.
**Since:** 1.8

- pid

```java
public long pid()
```

Returns the native process ID of the process.
The native process ID is an identification number that the operating
system assigns to the process.

**Implementation Requirements:** The implementation of this method returns the process id as:

toHandle().pid()

.
**Returns:** the native process id of the process
**Throws:** UnsupportedOperationException

- if the Process implementation
does not support this operation
**Since:** 9

- onExit

```java
public
CompletableFuture
<
Process
> onExit()
```

Returns a

CompletableFuture<Process>

for the termination of the Process.
The

CompletableFuture

provides the ability
to trigger dependent functions or actions that may be run synchronously
or asynchronously upon process termination.
When the process has terminated the CompletableFuture is

completed

regardless
of the exit status of the process.

Calling

onExit().get()

waits for the process to terminate and returns
the Process. The future can be used to check if the process is

done

or to

wait

for it to terminate.

Cancelling

the CompletableFuture does not affect the Process.

Processes returned from

ProcessBuilder.start()

override the
default implementation to provide an efficient mechanism to wait
for process exit.

**API Note:** Using

onExit

is an alternative to

waitFor

that enables both additional concurrency
and convenient access to the result of the Process.
Lambda expressions can be used to evaluate the result of the Process
execution.
If there is other processing to be done before the value is used
then

onExit

is a convenient mechanism to
free the current thread and block only if and when the value is needed.

For example, launching a process to compare two files and get a boolean if they are identical:

```java
Process p = new ProcessBuilder("cmp", "f1", "f2").start();
Future<Boolean> identical = p.onExit().thenApply(p1 -> p1.exitValue() == 0);
...
if (identical.get()) { ... }
```

, The process may be observed to have terminated with

isAlive()

before the ComputableFuture is completed and dependent actions are invoked.
**Implementation Requirements:** This implementation executes

waitFor()

in a separate thread
repeatedly until it returns successfully. If the execution of

waitFor

is interrupted, the thread's interrupt status is preserved.

When

waitFor()

returns successfully the CompletableFuture is

completed

regardless
of the exit status of the process.

This implementation may consume a lot of memory for thread stacks if a
large number of processes are waited for concurrently.

External implementations should override this method and provide
a more efficient implementation. For example, to delegate to the underlying
process, it can do the following:

```java
public CompletableFuture<Process> onExit() {
return delegate.onExit().thenApply(p -> this);
}
```
**Returns:** a new

CompletableFuture<Process>

for the Process
**Since:** 9

- toHandle

```java
public
ProcessHandle
toHandle()
```

Returns a ProcessHandle for the Process.

Process

objects returned by

ProcessBuilder.start()

and

Runtime.exec(java.lang.String)

implement

toHandle

as the equivalent of

ProcessHandle.of(pid)

including the
check for a SecurityManager and

RuntimePermission("manageProcess")

.

**Implementation Requirements:** This implementation throws an instance of

UnsupportedOperationException

and performs no other action.
Subclasses should override this method to provide a ProcessHandle for the
process. The methods

pid()

,

info()

,

children()

,
and

descendants()

, unless overridden, operate on the ProcessHandle.
**Returns:** Returns a ProcessHandle for the Process
**Throws:** UnsupportedOperationException

- if the Process implementation
does not support this operation
**Throws:** SecurityException

- if a security manager has been installed and
it denies RuntimePermission("manageProcess")
**Since:** 9

- info

```java
public
ProcessHandle.Info
info()
```

Returns a snapshot of information about the process.

A

ProcessHandle.Info

instance has accessor methods
that return information about the process if it is available.

**Implementation Requirements:** This implementation returns information about the process as:

toHandle().info()

.
**Returns:** a snapshot of information about the process, always non-null
**Throws:** UnsupportedOperationException

- if the Process implementation
does not support this operation
**Since:** 9

- children

```java
public
Stream
<
ProcessHandle
> children()
```

Returns a snapshot of the direct children of the process.
The parent of a direct child process is the process.
Typically, a process that is

not alive

has no children.

Note that processes are created and terminate asynchronously.
There is no guarantee that a process is

alive

.

**Implementation Requirements:** This implementation returns the direct children as:

toHandle().children()

.
**Returns:** a sequential Stream of ProcessHandles for processes that are
direct children of the process
**Throws:** UnsupportedOperationException

- if the Process implementation
does not support this operation
**Throws:** SecurityException

- if a security manager has been installed and
it denies RuntimePermission("manageProcess")
**Since:** 9

- descendants

```java
public
Stream
<
ProcessHandle
> descendants()
```

Returns a snapshot of the descendants of the process.
The descendants of a process are the children of the process
plus the descendants of those children, recursively.
Typically, a process that is

not alive

has no children.

Note that processes are created and terminate asynchronously.
There is no guarantee that a process is

alive

.

**Implementation Requirements:** This implementation returns all children as:

toHandle().descendants()

.
**Returns:** a sequential Stream of ProcessHandles for processes that
are descendants of the process
**Throws:** UnsupportedOperationException

- if the Process implementation
does not support this operation
**Throws:** SecurityException

- if a security manager has been installed and
it denies RuntimePermission("manageProcess")
**Since:** 9

---

#### Method Detail

getOutputStream

```java
public abstract
OutputStream
getOutputStream()
```

Returns the output stream connected to the normal input of the
process. Output to the stream is piped into the standard
input of the process represented by this

Process

object.

If the standard input of the process has been redirected using

ProcessBuilder.redirectInput

then this method will return a

null output stream

.

Implementation note: It is a good idea for the returned
output stream to be buffered.

**Returns:** the output stream connected to the normal input of the
process

---

#### getOutputStream

public abstract

OutputStream

getOutputStream()

Returns the output stream connected to the normal input of the
process. Output to the stream is piped into the standard
input of the process represented by this

Process

object.

If the standard input of the process has been redirected using

ProcessBuilder.redirectInput

then this method will return a

null output stream

.

Implementation note: It is a good idea for the returned
output stream to be buffered.

If the standard input of the process has been redirected using

ProcessBuilder.redirectInput

then this method will return a

null output stream

.

Implementation note: It is a good idea for the returned
output stream to be buffered.

Implementation note: It is a good idea for the returned
output stream to be buffered.

getInputStream

```java
public abstract
InputStream
getInputStream()
```

Returns the input stream connected to the normal output of the
process. The stream obtains data piped from the standard
output of the process represented by this

Process

object.

If the standard output of the process has been redirected using

ProcessBuilder.redirectOutput

then this method will return a

null input stream

.

Otherwise, if the standard error of the process has been
redirected using

ProcessBuilder.redirectErrorStream

then the input stream returned by this method will receive the
merged standard output and the standard error of the process.

Implementation note: It is a good idea for the returned
input stream to be buffered.

**Returns:** the input stream connected to the normal output of the
process

---

#### getInputStream

public abstract

InputStream

getInputStream()

Returns the input stream connected to the normal output of the
process. The stream obtains data piped from the standard
output of the process represented by this

Process

object.

If the standard output of the process has been redirected using

ProcessBuilder.redirectOutput

then this method will return a

null input stream

.

Otherwise, if the standard error of the process has been
redirected using

ProcessBuilder.redirectErrorStream

then the input stream returned by this method will receive the
merged standard output and the standard error of the process.

Implementation note: It is a good idea for the returned
input stream to be buffered.

If the standard output of the process has been redirected using

ProcessBuilder.redirectOutput

then this method will return a

null input stream

.

Otherwise, if the standard error of the process has been
redirected using

ProcessBuilder.redirectErrorStream

then the input stream returned by this method will receive the
merged standard output and the standard error of the process.

Implementation note: It is a good idea for the returned
input stream to be buffered.

Otherwise, if the standard error of the process has been
redirected using

ProcessBuilder.redirectErrorStream

then the input stream returned by this method will receive the
merged standard output and the standard error of the process.

Implementation note: It is a good idea for the returned
input stream to be buffered.

Implementation note: It is a good idea for the returned
input stream to be buffered.

getErrorStream

```java
public abstract
InputStream
getErrorStream()
```

Returns the input stream connected to the error output of the
process. The stream obtains data piped from the error output
of the process represented by this

Process

object.

If the standard error of the process has been redirected using

ProcessBuilder.redirectError

or

ProcessBuilder.redirectErrorStream

then this method will return a

null input stream

.

Implementation note: It is a good idea for the returned
input stream to be buffered.

**Returns:** the input stream connected to the error output of
the process

---

#### getErrorStream

public abstract

InputStream

getErrorStream()

Returns the input stream connected to the error output of the
process. The stream obtains data piped from the error output
of the process represented by this

Process

object.

If the standard error of the process has been redirected using

ProcessBuilder.redirectError

or

ProcessBuilder.redirectErrorStream

then this method will return a

null input stream

.

Implementation note: It is a good idea for the returned
input stream to be buffered.

If the standard error of the process has been redirected using

ProcessBuilder.redirectError

or

ProcessBuilder.redirectErrorStream

then this method will return a

null input stream

.

Implementation note: It is a good idea for the returned
input stream to be buffered.

Implementation note: It is a good idea for the returned
input stream to be buffered.

waitFor

```java
public abstract int waitFor()
throws
InterruptedException
```

Causes the current thread to wait, if necessary, until the
process represented by this

Process

object has
terminated. This method returns immediately if the process
has already terminated. If the process has not yet
terminated, the calling thread will be blocked until the
process exits.

**Returns:** the exit value of the process represented by this

Process

object. By convention, the value

0

indicates normal termination.
**Throws:** InterruptedException

- if the current thread is

interrupted

by another
thread while it is waiting, then the wait is ended and
an

InterruptedException

is thrown.

---

#### waitFor

public abstract int waitFor()
throws

InterruptedException

Causes the current thread to wait, if necessary, until the
process represented by this

Process

object has
terminated. This method returns immediately if the process
has already terminated. If the process has not yet
terminated, the calling thread will be blocked until the
process exits.

waitFor

```java
public boolean waitFor​(long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Causes the current thread to wait, if necessary, until the
process represented by this

Process

object has
terminated, or the specified waiting time elapses.

If the process has already terminated then this method returns
immediately with the value

true

. If the process has not
terminated and the timeout value is less than, or equal to, zero, then
this method returns immediately with the value

false

.

The default implementation of this methods polls the

exitValue

to check if the process has terminated. Concrete implementations of this
class are strongly encouraged to override this method with a more
efficient implementation.

**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the

timeout

argument
**Returns:** true

if the process has exited and

false

if
the waiting time elapsed before the process has exited.
**Throws:** InterruptedException

- if the current thread is interrupted
while waiting.
**Throws:** NullPointerException

- if unit is null
**Since:** 1.8

---

#### waitFor

public boolean waitFor​(long timeout,

TimeUnit

unit)
throws

InterruptedException

Causes the current thread to wait, if necessary, until the
process represented by this

Process

object has
terminated, or the specified waiting time elapses.

If the process has already terminated then this method returns
immediately with the value

true

. If the process has not
terminated and the timeout value is less than, or equal to, zero, then
this method returns immediately with the value

false

.

The default implementation of this methods polls the

exitValue

to check if the process has terminated. Concrete implementations of this
class are strongly encouraged to override this method with a more
efficient implementation.

If the process has already terminated then this method returns
immediately with the value

true

. If the process has not
terminated and the timeout value is less than, or equal to, zero, then
this method returns immediately with the value

false

.

The default implementation of this methods polls the

exitValue

to check if the process has terminated. Concrete implementations of this
class are strongly encouraged to override this method with a more
efficient implementation.

The default implementation of this methods polls the

exitValue

to check if the process has terminated. Concrete implementations of this
class are strongly encouraged to override this method with a more
efficient implementation.

exitValue

```java
public abstract int exitValue()
```

Returns the exit value for the process.

**Returns:** the exit value of the process represented by this

Process

object. By convention, the value

0

indicates normal termination.
**Throws:** IllegalThreadStateException

- if the process represented
by this

Process

object has not yet terminated

---

#### exitValue

public abstract int exitValue()

Returns the exit value for the process.

destroy

```java
public abstract void destroy()
```

Kills the process.
Whether the process represented by this

Process

object is

normally terminated

or not is
implementation dependent.
Forcible process destruction is defined as the immediate termination of a
process, whereas normal termination allows the process to shut down cleanly.
If the process is not alive, no action is taken.

The

CompletableFuture

from

onExit()

is

completed

when the process has terminated.

---

#### destroy

public abstract void destroy()

Kills the process.
Whether the process represented by this

Process

object is

normally terminated

or not is
implementation dependent.
Forcible process destruction is defined as the immediate termination of a
process, whereas normal termination allows the process to shut down cleanly.
If the process is not alive, no action is taken.

The

CompletableFuture

from

onExit()

is

completed

when the process has terminated.

The

CompletableFuture

from

onExit()

is

completed

when the process has terminated.

destroyForcibly

```java
public
Process
destroyForcibly()
```

Kills the process forcibly. The process represented by this

Process

object is forcibly terminated.
Forcible process destruction is defined as the immediate termination of a
process, whereas normal termination allows the process to shut down cleanly.
If the process is not alive, no action is taken.

The

CompletableFuture

from

onExit()

is

completed

when the process has terminated.

Invoking this method on

Process

objects returned by

ProcessBuilder.start()

and

Runtime.exec(java.lang.String)

forcibly terminate
the process.

**API Note:** The process may not terminate immediately.
i.e.

isAlive()

may return true for a brief period
after

destroyForcibly()

is called. This method
may be chained to

waitFor()

if needed.
**Implementation Requirements:** The default implementation of this method invokes

destroy()

and so may not forcibly terminate the process.
**Implementation Note:** Concrete implementations of this class are strongly encouraged to override
this method with a compliant implementation.
**Returns:** the

Process

object representing the
process forcibly destroyed
**Since:** 1.8

---

#### destroyForcibly

public

Process

destroyForcibly()

Kills the process forcibly. The process represented by this

Process

object is forcibly terminated.
Forcible process destruction is defined as the immediate termination of a
process, whereas normal termination allows the process to shut down cleanly.
If the process is not alive, no action is taken.

The

CompletableFuture

from

onExit()

is

completed

when the process has terminated.

Invoking this method on

Process

objects returned by

ProcessBuilder.start()

and

Runtime.exec(java.lang.String)

forcibly terminate
the process.

The

CompletableFuture

from

onExit()

is

completed

when the process has terminated.

Invoking this method on

Process

objects returned by

ProcessBuilder.start()

and

Runtime.exec(java.lang.String)

forcibly terminate
the process.

Invoking this method on

Process

objects returned by

ProcessBuilder.start()

and

Runtime.exec(java.lang.String)

forcibly terminate
the process.

supportsNormalTermination

```java
public boolean supportsNormalTermination()
```

Returns

true

if the implementation of

destroy()

is to
normally terminate the process,
Returns

false

if the implementation of

destroy

forcibly and immediately terminates the process.

Invoking this method on

Process

objects returned by

ProcessBuilder.start()

and

Runtime.exec(java.lang.String)

return

true

or

false

depending on the platform implementation.

**Implementation Requirements:** This implementation throws an instance of

UnsupportedOperationException

and performs no other action.
**Returns:** true

if the implementation of

destroy()

is to
normally terminate the process;
otherwise,

destroy()

forcibly terminates the process
**Throws:** UnsupportedOperationException

- if the Process implementation
does not support this operation
**Since:** 9

---

#### supportsNormalTermination

public boolean supportsNormalTermination()

Returns

true

if the implementation of

destroy()

is to
normally terminate the process,
Returns

false

if the implementation of

destroy

forcibly and immediately terminates the process.

Invoking this method on

Process

objects returned by

ProcessBuilder.start()

and

Runtime.exec(java.lang.String)

return

true

or

false

depending on the platform implementation.

Invoking this method on

Process

objects returned by

ProcessBuilder.start()

and

Runtime.exec(java.lang.String)

return

true

or

false

depending on the platform implementation.

isAlive

```java
public boolean isAlive()
```

Tests whether the process represented by this

Process

is
alive.

**Returns:** true

if the process represented by this

Process

object has not yet terminated.
**Since:** 1.8

---

#### isAlive

public boolean isAlive()

Tests whether the process represented by this

Process

is
alive.

pid

```java
public long pid()
```

Returns the native process ID of the process.
The native process ID is an identification number that the operating
system assigns to the process.

**Implementation Requirements:** The implementation of this method returns the process id as:

toHandle().pid()

.
**Returns:** the native process id of the process
**Throws:** UnsupportedOperationException

- if the Process implementation
does not support this operation
**Since:** 9

---

#### pid

public long pid()

Returns the native process ID of the process.
The native process ID is an identification number that the operating
system assigns to the process.

onExit

```java
public
CompletableFuture
<
Process
> onExit()
```

Returns a

CompletableFuture<Process>

for the termination of the Process.
The

CompletableFuture

provides the ability
to trigger dependent functions or actions that may be run synchronously
or asynchronously upon process termination.
When the process has terminated the CompletableFuture is

completed

regardless
of the exit status of the process.

Calling

onExit().get()

waits for the process to terminate and returns
the Process. The future can be used to check if the process is

done

or to

wait

for it to terminate.

Cancelling

the CompletableFuture does not affect the Process.

Processes returned from

ProcessBuilder.start()

override the
default implementation to provide an efficient mechanism to wait
for process exit.

**API Note:** Using

onExit

is an alternative to

waitFor

that enables both additional concurrency
and convenient access to the result of the Process.
Lambda expressions can be used to evaluate the result of the Process
execution.
If there is other processing to be done before the value is used
then

onExit

is a convenient mechanism to
free the current thread and block only if and when the value is needed.

For example, launching a process to compare two files and get a boolean if they are identical:

```java
Process p = new ProcessBuilder("cmp", "f1", "f2").start();
Future<Boolean> identical = p.onExit().thenApply(p1 -> p1.exitValue() == 0);
...
if (identical.get()) { ... }
```

, The process may be observed to have terminated with

isAlive()

before the ComputableFuture is completed and dependent actions are invoked.
**Implementation Requirements:** This implementation executes

waitFor()

in a separate thread
repeatedly until it returns successfully. If the execution of

waitFor

is interrupted, the thread's interrupt status is preserved.

When

waitFor()

returns successfully the CompletableFuture is

completed

regardless
of the exit status of the process.

This implementation may consume a lot of memory for thread stacks if a
large number of processes are waited for concurrently.

External implementations should override this method and provide
a more efficient implementation. For example, to delegate to the underlying
process, it can do the following:

```java
public CompletableFuture<Process> onExit() {
return delegate.onExit().thenApply(p -> this);
}
```
**Returns:** a new

CompletableFuture<Process>

for the Process
**Since:** 9

---

#### onExit

public

CompletableFuture

<

Process

> onExit()

Returns a

CompletableFuture<Process>

for the termination of the Process.
The

CompletableFuture

provides the ability
to trigger dependent functions or actions that may be run synchronously
or asynchronously upon process termination.
When the process has terminated the CompletableFuture is

completed

regardless
of the exit status of the process.

Calling

onExit().get()

waits for the process to terminate and returns
the Process. The future can be used to check if the process is

done

or to

wait

for it to terminate.

Cancelling

the CompletableFuture does not affect the Process.

Processes returned from

ProcessBuilder.start()

override the
default implementation to provide an efficient mechanism to wait
for process exit.

Calling

onExit().get()

waits for the process to terminate and returns
the Process. The future can be used to check if the process is

done

or to

wait

for it to terminate.

Cancelling

the CompletableFuture does not affect the Process.

Processes returned from

ProcessBuilder.start()

override the
default implementation to provide an efficient mechanism to wait
for process exit.

Processes returned from

ProcessBuilder.start()

override the
default implementation to provide an efficient mechanism to wait
for process exit.

Process p = new ProcessBuilder("cmp", "f1", "f2").start();
Future<Boolean> identical = p.onExit().thenApply(p1 -> p1.exitValue() == 0);
...
if (identical.get()) { ... }

When

waitFor()

returns successfully the CompletableFuture is

completed

regardless
of the exit status of the process.

This implementation may consume a lot of memory for thread stacks if a
large number of processes are waited for concurrently.

External implementations should override this method and provide
a more efficient implementation. For example, to delegate to the underlying
process, it can do the following:

```java
public CompletableFuture<Process> onExit() {
return delegate.onExit().thenApply(p -> this);
}
```

External implementations should override this method and provide
a more efficient implementation. For example, to delegate to the underlying
process, it can do the following:

```java
public CompletableFuture<Process> onExit() {
return delegate.onExit().thenApply(p -> this);
}
```

public CompletableFuture<Process> onExit() {
return delegate.onExit().thenApply(p -> this);
}

toHandle

```java
public
ProcessHandle
toHandle()
```

Returns a ProcessHandle for the Process.

Process

objects returned by

ProcessBuilder.start()

and

Runtime.exec(java.lang.String)

implement

toHandle

as the equivalent of

ProcessHandle.of(pid)

including the
check for a SecurityManager and

RuntimePermission("manageProcess")

.

**Implementation Requirements:** This implementation throws an instance of

UnsupportedOperationException

and performs no other action.
Subclasses should override this method to provide a ProcessHandle for the
process. The methods

pid()

,

info()

,

children()

,
and

descendants()

, unless overridden, operate on the ProcessHandle.
**Returns:** Returns a ProcessHandle for the Process
**Throws:** UnsupportedOperationException

- if the Process implementation
does not support this operation
**Throws:** SecurityException

- if a security manager has been installed and
it denies RuntimePermission("manageProcess")
**Since:** 9

---

#### toHandle

public

ProcessHandle

toHandle()

Returns a ProcessHandle for the Process.

Process

objects returned by

ProcessBuilder.start()

and

Runtime.exec(java.lang.String)

implement

toHandle

as the equivalent of

ProcessHandle.of(pid)

including the
check for a SecurityManager and

RuntimePermission("manageProcess")

.

info

```java
public
ProcessHandle.Info
info()
```

Returns a snapshot of information about the process.

A

ProcessHandle.Info

instance has accessor methods
that return information about the process if it is available.

**Implementation Requirements:** This implementation returns information about the process as:

toHandle().info()

.
**Returns:** a snapshot of information about the process, always non-null
**Throws:** UnsupportedOperationException

- if the Process implementation
does not support this operation
**Since:** 9

---

#### info

public

ProcessHandle.Info

info()

Returns a snapshot of information about the process.

A

ProcessHandle.Info

instance has accessor methods
that return information about the process if it is available.

A

ProcessHandle.Info

instance has accessor methods
that return information about the process if it is available.

children

```java
public
Stream
<
ProcessHandle
> children()
```

Returns a snapshot of the direct children of the process.
The parent of a direct child process is the process.
Typically, a process that is

not alive

has no children.

Note that processes are created and terminate asynchronously.
There is no guarantee that a process is

alive

.

**Implementation Requirements:** This implementation returns the direct children as:

toHandle().children()

.
**Returns:** a sequential Stream of ProcessHandles for processes that are
direct children of the process
**Throws:** UnsupportedOperationException

- if the Process implementation
does not support this operation
**Throws:** SecurityException

- if a security manager has been installed and
it denies RuntimePermission("manageProcess")
**Since:** 9

---

#### children

public

Stream

<

ProcessHandle

> children()

Returns a snapshot of the direct children of the process.
The parent of a direct child process is the process.
Typically, a process that is

not alive

has no children.

Note that processes are created and terminate asynchronously.
There is no guarantee that a process is

alive

.

Note that processes are created and terminate asynchronously.
There is no guarantee that a process is

alive

.

descendants

```java
public
Stream
<
ProcessHandle
> descendants()
```

Returns a snapshot of the descendants of the process.
The descendants of a process are the children of the process
plus the descendants of those children, recursively.
Typically, a process that is

not alive

has no children.

Note that processes are created and terminate asynchronously.
There is no guarantee that a process is

alive

.

**Implementation Requirements:** This implementation returns all children as:

toHandle().descendants()

.
**Returns:** a sequential Stream of ProcessHandles for processes that
are descendants of the process
**Throws:** UnsupportedOperationException

- if the Process implementation
does not support this operation
**Throws:** SecurityException

- if a security manager has been installed and
it denies RuntimePermission("manageProcess")
**Since:** 9

---

#### descendants

public

Stream

<

ProcessHandle

> descendants()

Returns a snapshot of the descendants of the process.
The descendants of a process are the children of the process
plus the descendants of those children, recursively.
Typically, a process that is

not alive

has no children.

Note that processes are created and terminate asynchronously.
There is no guarantee that a process is

alive

.

Note that processes are created and terminate asynchronously.
There is no guarantee that a process is

alive

.

---

