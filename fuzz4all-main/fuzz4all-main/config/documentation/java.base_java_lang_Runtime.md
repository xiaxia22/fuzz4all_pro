# Class Runtime

**Source:** `java.base\java\lang\Runtime.html`

### Class Description

```java
public class
Runtime

extends
Object
```

Every Java application has a single instance of class

Runtime

that allows the application to interface with
the environment in which the application is running. The current
runtime can be obtained from the

getRuntime

method.

An application cannot create its own instance of this class.

**Since:** 1.0
**See Also:** getRuntime()

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
Runtime
getRuntime()

Returns the runtime object associated with the current Java application.
Most of the methods of class

Runtime

are instance
methods and must be invoked with respect to the current runtime object.

**Returns:**
- the

Runtime

object associated with the current
Java application.

---

#### public void exit​(int status)

Terminates the currently running Java virtual machine by initiating its
shutdown sequence. This method never returns normally. The argument
serves as a status code; by convention, a nonzero status code indicates
abnormal termination.

All registered

shutdown hooks

, if any,
are started in some unspecified order and allowed to run concurrently
until they finish. Once this is done the virtual machine

halts

.

If this method is invoked after all shutdown hooks have already
been run and the status is nonzero then this method halts the
virtual machine with the given status code. Otherwise, this method
blocks indefinitely.

The

System.exit

method is the
conventional and convenient means of invoking this method.

**Parameters:**
- status

- Termination status. By convention, a nonzero status code
indicates abnormal termination.

**Throws:**
- SecurityException

- If a security manager is present and its

checkExit

method does not permit
exiting with the specified status

**See Also:**
- SecurityException

,

SecurityManager.checkExit(int)

,

addShutdownHook(java.lang.Thread)

,

removeShutdownHook(java.lang.Thread)

,

halt(int)

---

#### public void addShutdownHook​(
Thread
hook)

Registers a new virtual-machine shutdown hook.

The Java virtual machine

shuts down

in response to two kinds
of events:

- The program

exits

normally, when the last non-daemon
thread exits or when the

exit

(equivalently,

System.exit

) method is invoked, or

The virtual machine is

terminated

in response to a
user interrupt, such as typing

^C

, or a system-wide event,
such as user logoff or system shutdown.

A

shutdown hook

is simply an initialized but unstarted
thread. When the virtual machine begins its shutdown sequence it will
start all registered shutdown hooks in some unspecified order and let
them run concurrently. When all the hooks have finished it will then
halt. Note that daemon threads will continue to run during the shutdown
sequence, as will non-daemon threads if shutdown was initiated by
invoking the

exit

method.

Once the shutdown sequence has begun it can be stopped only by
invoking the

halt

method, which forcibly
terminates the virtual machine.

Once the shutdown sequence has begun it is impossible to register a
new shutdown hook or de-register a previously-registered hook.
Attempting either of these operations will cause an

IllegalStateException

to be thrown.

Shutdown hooks run at a delicate time in the life cycle of a virtual
machine and should therefore be coded defensively. They should, in
particular, be written to be thread-safe and to avoid deadlocks insofar
as possible. They should also not rely blindly upon services that may
have registered their own shutdown hooks and therefore may themselves in
the process of shutting down. Attempts to use other thread-based
services such as the AWT event-dispatch thread, for example, may lead to
deadlocks.

Shutdown hooks should also finish their work quickly. When a
program invokes

exit

the expectation is
that the virtual machine will promptly shut down and exit. When the
virtual machine is terminated due to user logoff or system shutdown the
underlying operating system may only allow a fixed amount of time in
which to shut down and exit. It is therefore inadvisable to attempt any
user interaction or to perform a long-running computation in a shutdown
hook.

Uncaught exceptions are handled in shutdown hooks just as in any
other thread, by invoking the

uncaughtException

method of the
thread's

ThreadGroup

object. The default implementation of this
method prints the exception's stack trace to

System.err

and
terminates the thread; it does not cause the virtual machine to exit or
halt.

In rare circumstances the virtual machine may

abort

, that is,
stop running without shutting down cleanly. This occurs when the
virtual machine is terminated externally, for example with the

SIGKILL

signal on Unix or the

TerminateProcess

call on
Microsoft Windows. The virtual machine may also abort if a native
method goes awry by, for example, corrupting internal data structures or
attempting to access nonexistent memory. If the virtual machine aborts
then no guarantee can be made about whether or not any shutdown hooks
will be run.

**Parameters:**
- hook

- An initialized but unstarted

Thread

object

**Throws:**
- IllegalArgumentException

- If the specified hook has already been registered,
or if it can be determined that the hook is already running or
has already been run
- IllegalStateException

- If the virtual machine is already in the process
of shutting down
- SecurityException

- If a security manager is present and it denies

RuntimePermission

("shutdownHooks")

**See Also:**
- removeShutdownHook(java.lang.Thread)

,

halt(int)

,

exit(int)

**Since:**
- 1.3

---

#### public boolean removeShutdownHook​(
Thread
hook)

De-registers a previously-registered virtual-machine shutdown hook.

**Parameters:**
- hook

- the hook to remove

**Returns:**
- true

if the specified hook had previously been
registered and was successfully de-registered,

false

otherwise.

**Throws:**
- IllegalStateException

- If the virtual machine is already in the process of shutting
down
- SecurityException

- If a security manager is present and it denies

RuntimePermission

("shutdownHooks")

**See Also:**
- addShutdownHook(java.lang.Thread)

,

exit(int)

**Since:**
- 1.3

---

#### public void halt​(int status)

Forcibly terminates the currently running Java virtual machine. This
method never returns normally.

This method should be used with extreme caution. Unlike the

exit

method, this method does not cause shutdown
hooks to be started. If the shutdown sequence has already been
initiated then this method does not wait for any running
shutdown hooks to finish their work.

**Parameters:**
- status

- Termination status. By convention, a nonzero status code
indicates abnormal termination. If the

exit

(equivalently,

System.exit

) method
has already been invoked then this status code
will override the status code passed to that method.

**Throws:**
- SecurityException

- If a security manager is present and its

checkExit

method
does not permit an exit with the specified status

**See Also:**
- exit(int)

,

addShutdownHook(java.lang.Thread)

,

removeShutdownHook(java.lang.Thread)

**Since:**
- 1.3

---

#### public
Process
exec​(
String
command)
throws
IOException

Executes the specified string command in a separate process.

This is a convenience method. An invocation of the form

exec(command)

behaves in exactly the same way as the invocation

exec

(command, null, null)

.

**Parameters:**
- command

- a specified system command.

**Returns:**
- A new

Process

object for managing the subprocess

**Throws:**
- SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
- IOException

- If an I/O error occurs
- NullPointerException

- If

command

is

null
- IllegalArgumentException

- If

command

is empty

**See Also:**
- exec(String[], String[], File)

,

ProcessBuilder

---

#### public
Process
exec​(
String
command,

String
[] envp)
throws
IOException

Executes the specified string command in a separate process with the
specified environment.

This is a convenience method. An invocation of the form

exec(command, envp)

behaves in exactly the same way as the invocation

exec

(command, envp, null)

.

**Parameters:**
- command

- a specified system command.
- envp

- array of strings, each element of which
has environment variable settings in the format

name

=

value

, or

null

if the subprocess should inherit
the environment of the current process.

**Returns:**
- A new

Process

object for managing the subprocess

**Throws:**
- SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
- IOException

- If an I/O error occurs
- NullPointerException

- If

command

is

null

,
or one of the elements of

envp

is

null
- IllegalArgumentException

- If

command

is empty

**See Also:**
- exec(String[], String[], File)

,

ProcessBuilder

---

#### public
Process
exec​(
String
command,

String
[] envp,

File
dir)
throws
IOException

Executes the specified string command in a separate process with the
specified environment and working directory.

This is a convenience method. An invocation of the form

exec(command, envp, dir)

behaves in exactly the same way as the invocation

exec

(cmdarray, envp, dir)

,
where

cmdarray

is an array of all the tokens in

command

.

More precisely, the

command

string is broken
into tokens using a

StringTokenizer

created by the call

new {@link StringTokenizer}(command)

with no
further modification of the character categories. The tokens
produced by the tokenizer are then placed in the new string
array

cmdarray

, in the same order.

**Parameters:**
- command

- a specified system command.
- envp

- array of strings, each element of which
has environment variable settings in the format

name

=

value

, or

null

if the subprocess should inherit
the environment of the current process.
- dir

- the working directory of the subprocess, or

null

if the subprocess should inherit
the working directory of the current process.

**Returns:**
- A new

Process

object for managing the subprocess

**Throws:**
- SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
- IOException

- If an I/O error occurs
- NullPointerException

- If

command

is

null

,
or one of the elements of

envp

is

null
- IllegalArgumentException

- If

command

is empty

**See Also:**
- ProcessBuilder

**Since:**
- 1.3

---

#### public
Process
exec​(
String
[] cmdarray)
throws
IOException

Executes the specified command and arguments in a separate process.

This is a convenience method. An invocation of the form

exec(cmdarray)

behaves in exactly the same way as the invocation

exec

(cmdarray, null, null)

.

**Parameters:**
- cmdarray

- array containing the command to call and
its arguments.

**Returns:**
- A new

Process

object for managing the subprocess

**Throws:**
- SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
- IOException

- If an I/O error occurs
- NullPointerException

- If

cmdarray

is

null

,
or one of the elements of

cmdarray

is

null
- IndexOutOfBoundsException

- If

cmdarray

is an empty array
(has length

0

)

**See Also:**
- ProcessBuilder

---

#### public
Process
exec​(
String
[] cmdarray,

String
[] envp)
throws
IOException

Executes the specified command and arguments in a separate process
with the specified environment.

This is a convenience method. An invocation of the form

exec(cmdarray, envp)

behaves in exactly the same way as the invocation

exec

(cmdarray, envp, null)

.

**Parameters:**
- cmdarray

- array containing the command to call and
its arguments.
- envp

- array of strings, each element of which
has environment variable settings in the format

name

=

value

, or

null

if the subprocess should inherit
the environment of the current process.

**Returns:**
- A new

Process

object for managing the subprocess

**Throws:**
- SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
- IOException

- If an I/O error occurs
- NullPointerException

- If

cmdarray

is

null

,
or one of the elements of

cmdarray

is

null

,
or one of the elements of

envp

is

null
- IndexOutOfBoundsException

- If

cmdarray

is an empty array
(has length

0

)

**See Also:**
- ProcessBuilder

---

#### public
Process
exec​(
String
[] cmdarray,

String
[] envp,

File
dir)
throws
IOException

Executes the specified command and arguments in a separate process with
the specified environment and working directory.

Given an array of strings

cmdarray

, representing the
tokens of a command line, and an array of strings

envp

,
representing "environment" variable settings, this method creates
a new process in which to execute the specified command.

This method checks that

cmdarray

is a valid operating
system command. Which commands are valid is system-dependent,
but at the very least the command must be a non-empty list of
non-null strings.

If

envp

is

null

, the subprocess inherits the
environment settings of the current process.

A minimal set of system dependent environment variables may
be required to start a process on some operating systems.
As a result, the subprocess may inherit additional environment variable
settings beyond those in the specified environment.

ProcessBuilder.start()

is now the preferred way to
start a process with a modified environment.

The working directory of the new subprocess is specified by

dir

.
If

dir

is

null

, the subprocess inherits the
current working directory of the current process.

If a security manager exists, its

checkExec

method is invoked with the first component of the array

cmdarray

as its argument. This may result in a

SecurityException

being thrown.

Starting an operating system process is highly system-dependent.
Among the many things that can go wrong are:

- The operating system program file was not found.

Access to the program file was denied.

The working directory does not exist.

In such cases an exception will be thrown. The exact nature
of the exception is system-dependent, but it will always be a
subclass of

IOException

.

If the operating system does not support the creation of
processes, an

UnsupportedOperationException

will be thrown.

**Parameters:**
- cmdarray

- array containing the command to call and
its arguments.
- envp

- array of strings, each element of which
has environment variable settings in the format

name

=

value

, or

null

if the subprocess should inherit
the environment of the current process.
- dir

- the working directory of the subprocess, or

null

if the subprocess should inherit
the working directory of the current process.

**Returns:**
- A new

Process

object for managing the subprocess

**Throws:**
- SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
- UnsupportedOperationException

- If the operating system does not support the creation of processes.
- IOException

- If an I/O error occurs
- NullPointerException

- If

cmdarray

is

null

,
or one of the elements of

cmdarray

is

null

,
or one of the elements of

envp

is

null
- IndexOutOfBoundsException

- If

cmdarray

is an empty array
(has length

0

)

**See Also:**
- ProcessBuilder

**Since:**
- 1.3

---

#### public int availableProcessors()

Returns the number of processors available to the Java virtual machine.

This value may change during a particular invocation of the virtual
machine. Applications that are sensitive to the number of available
processors should therefore occasionally poll this property and adjust
their resource usage appropriately.

**Returns:**
- the maximum number of processors available to the virtual
machine; never smaller than one

**Since:**
- 1.4

---

#### public long freeMemory()

Returns the amount of free memory in the Java Virtual Machine.
Calling the

gc

method may result in increasing the value returned
by

freeMemory.

**Returns:**
- an approximation to the total amount of memory currently
available for future allocated objects, measured in bytes.

---

#### public long totalMemory()

Returns the total amount of memory in the Java virtual machine.
The value returned by this method may vary over time, depending on
the host environment.

Note that the amount of memory required to hold an object of any
given type may be implementation-dependent.

**Returns:**
- the total amount of memory currently available for current
and future objects, measured in bytes.

---

#### public long maxMemory()

Returns the maximum amount of memory that the Java virtual machine
will attempt to use. If there is no inherent limit then the value

Long.MAX_VALUE

will be returned.

**Returns:**
- the maximum amount of memory that the virtual machine will
attempt to use, measured in bytes

**Since:**
- 1.4

---

#### public void gc()

Runs the garbage collector.
Calling this method suggests that the Java virtual machine expend
effort toward recycling unused objects in order to make the memory
they currently occupy available for quick reuse. When control
returns from the method call, the virtual machine has made
its best effort to recycle all discarded objects.

The name

gc

stands for "garbage
collector". The virtual machine performs this recycling
process automatically as needed, in a separate thread, even if the

gc

method is not invoked explicitly.

The method

System.gc()

is the conventional and convenient
means of invoking this method.

---

#### public void runFinalization()

Runs the finalization methods of any objects pending finalization.
Calling this method suggests that the Java virtual machine expend
effort toward running the

finalize

methods of objects
that have been found to be discarded but whose

finalize

methods have not yet been run. When control returns from the
method call, the virtual machine has made a best effort to
complete all outstanding finalizations.

The virtual machine performs the finalization process
automatically as needed, in a separate thread, if the

runFinalization

method is not invoked explicitly.

The method

System.runFinalization()

is the conventional
and convenient means of invoking this method.

**See Also:**
- Object.finalize()

---

#### @Deprecated
(
since
="9",

forRemoval
=true)
public void traceInstructions​(boolean on)

Not implemented, does nothing.

**Parameters:**
- on

- ignored

---

#### @Deprecated
(
since
="9",

forRemoval
=true)
public void traceMethodCalls​(boolean on)

Not implemented, does nothing.

**Parameters:**
- on

- ignored

---

#### public void load​(
String
filename)

Loads the native library specified by the filename argument. The filename
argument must be an absolute path name.
(for example

Runtime.getRuntime().load("/home/avh/lib/libX11.so");

).

If the filename argument, when stripped of any platform-specific library
prefix, path, and file extension, indicates a library whose name is,
for example, L, and a native library called L is statically linked
with the VM, then the JNI_OnLoad_L function exported by the library
is invoked rather than attempting to load a dynamic library.
A filename matching the argument does not have to exist in the file
system.
See the

JNI Specification

for more details.

Otherwise, the filename argument is mapped to a native library image in
an implementation-dependent manner.

First, if there is a security manager, its

checkLink

method is called with the

filename

as its argument.
This may result in a security exception.

This is similar to the method

loadLibrary(String)

, but it
accepts a general file name as an argument rather than just a library
name, allowing any file of native code to be loaded.

The method

System.load(String)

is the conventional and
convenient means of invoking this method.

**Parameters:**
- filename

- the file to load.

**Throws:**
- SecurityException

- if a security manager exists and its

checkLink

method doesn't allow
loading of the specified dynamic library
- UnsatisfiedLinkError

- if either the filename is not an
absolute path name, the native library is not statically
linked with the VM, or the library cannot be mapped to
a native library image by the host system.
- NullPointerException

- if

filename

is

null

**See Also:**
- getRuntime()

,

SecurityException

,

SecurityManager.checkLink(java.lang.String)

---

#### public void loadLibrary​(
String
libname)

Loads the native library specified by the

libname

argument. The

libname

argument must not contain any platform
specific prefix, file extension or path. If a native library
called

libname

is statically linked with the VM, then the
JNI_OnLoad_

libname

function exported by the library is invoked.
See the

JNI Specification

for more details.

Otherwise, the libname argument is loaded from a system library
location and mapped to a native library image in an implementation-
dependent manner.

First, if there is a security manager, its

checkLink

method is called with the

libname

as its argument.
This may result in a security exception.

The method

System.loadLibrary(String)

is the conventional
and convenient means of invoking this method. If native
methods are to be used in the implementation of a class, a standard
strategy is to put the native code in a library file (call it

LibFile

) and then to put a static initializer:

```java
static { System.loadLibrary("LibFile"); }
```

within the class declaration. When the class is loaded and
initialized, the necessary native code implementation for the native
methods will then be loaded as well.

If this method is called more than once with the same library
name, the second and subsequent calls are ignored.

**Parameters:**
- libname

- the name of the library.

**Throws:**
- SecurityException

- if a security manager exists and its

checkLink

method doesn't allow
loading of the specified dynamic library
- UnsatisfiedLinkError

- if either the libname argument
contains a file path, the native library is not statically
linked with the VM, or the library cannot be mapped to a
native library image by the host system.
- NullPointerException

- if

libname

is

null

**See Also:**
- SecurityException

,

SecurityManager.checkLink(java.lang.String)

---

#### public static
Runtime.Version
version()

Returns the version of the Java Runtime Environment as a

Runtime.Version

.

**Returns:**
- the

Runtime.Version

of the Java Runtime Environment

**Since:**
- 9

---

### Additional Sections

#### Class Runtime

java.lang.Object

- java.lang.Runtime

java.lang.Runtime

```java
public class
Runtime

extends
Object
```

Every Java application has a single instance of class

Runtime

that allows the application to interface with
the environment in which the application is running. The current
runtime can be obtained from the

getRuntime

method.

An application cannot create its own instance of this class.

**Since:** 1.0
**See Also:** getRuntime()

public class

Runtime

extends

Object

Every Java application has a single instance of class

Runtime

that allows the application to interface with
the environment in which the application is running. The current
runtime can be obtained from the

getRuntime

method.

An application cannot create its own instance of this class.

An application cannot create its own instance of this class.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Runtime.Version

A representation of a version string for an implementation of the
Java SE Platform.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

addShutdownHook

​(

Thread

hook)

Registers a new virtual-machine shutdown hook.

int

availableProcessors

()

Returns the number of processors available to the Java virtual machine.

Process

exec

​(

String

command)

Executes the specified string command in a separate process.

Process

exec

​(

String

[] cmdarray)

Executes the specified command and arguments in a separate process.

Process

exec

​(

String

[] cmdarray,

String

[] envp)

Executes the specified command and arguments in a separate process
with the specified environment.

Process

exec

​(

String

[] cmdarray,

String

[] envp,

File

dir)

Executes the specified command and arguments in a separate process with
the specified environment and working directory.

Process

exec

​(

String

command,

String

[] envp)

Executes the specified string command in a separate process with the
specified environment.

Process

exec

​(

String

command,

String

[] envp,

File

dir)

Executes the specified string command in a separate process with the
specified environment and working directory.

void

exit

​(int status)

Terminates the currently running Java virtual machine by initiating its
shutdown sequence.

long

freeMemory

()

Returns the amount of free memory in the Java Virtual Machine.

void

gc

()

Runs the garbage collector.

static

Runtime

getRuntime

()

Returns the runtime object associated with the current Java application.

void

halt

​(int status)

Forcibly terminates the currently running Java virtual machine.

void

load

​(

String

filename)

Loads the native library specified by the filename argument.

void

loadLibrary

​(

String

libname)

Loads the native library specified by the

libname

argument.

long

maxMemory

()

Returns the maximum amount of memory that the Java virtual machine
will attempt to use.

boolean

removeShutdownHook

​(

Thread

hook)

De-registers a previously-registered virtual-machine shutdown hook.

void

runFinalization

()

Runs the finalization methods of any objects pending finalization.

long

totalMemory

()

Returns the total amount of memory in the Java virtual machine.

void

traceInstructions

​(boolean on)

Deprecated, for removal: This API element is subject to removal in a future version.

This method was intended to control instruction tracing.

void

traceMethodCalls

​(boolean on)

Deprecated, for removal: This API element is subject to removal in a future version.

This method was intended to control method call tracing.

static

Runtime.Version

version

()

Returns the version of the Java Runtime Environment as a

Runtime.Version

.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Runtime.Version

A representation of a version string for an implementation of the
Java SE Platform.

---

#### Nested Class Summary

A representation of a version string for an implementation of the
Java SE Platform.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

void

addShutdownHook

​(

Thread

hook)

Registers a new virtual-machine shutdown hook.

int

availableProcessors

()

Returns the number of processors available to the Java virtual machine.

Process

exec

​(

String

command)

Executes the specified string command in a separate process.

Process

exec

​(

String

[] cmdarray)

Executes the specified command and arguments in a separate process.

Process

exec

​(

String

[] cmdarray,

String

[] envp)

Executes the specified command and arguments in a separate process
with the specified environment.

Process

exec

​(

String

[] cmdarray,

String

[] envp,

File

dir)

Executes the specified command and arguments in a separate process with
the specified environment and working directory.

Process

exec

​(

String

command,

String

[] envp)

Executes the specified string command in a separate process with the
specified environment.

Process

exec

​(

String

command,

String

[] envp,

File

dir)

Executes the specified string command in a separate process with the
specified environment and working directory.

void

exit

​(int status)

Terminates the currently running Java virtual machine by initiating its
shutdown sequence.

long

freeMemory

()

Returns the amount of free memory in the Java Virtual Machine.

void

gc

()

Runs the garbage collector.

static

Runtime

getRuntime

()

Returns the runtime object associated with the current Java application.

void

halt

​(int status)

Forcibly terminates the currently running Java virtual machine.

void

load

​(

String

filename)

Loads the native library specified by the filename argument.

void

loadLibrary

​(

String

libname)

Loads the native library specified by the

libname

argument.

long

maxMemory

()

Returns the maximum amount of memory that the Java virtual machine
will attempt to use.

boolean

removeShutdownHook

​(

Thread

hook)

De-registers a previously-registered virtual-machine shutdown hook.

void

runFinalization

()

Runs the finalization methods of any objects pending finalization.

long

totalMemory

()

Returns the total amount of memory in the Java virtual machine.

void

traceInstructions

​(boolean on)

Deprecated, for removal: This API element is subject to removal in a future version.

This method was intended to control instruction tracing.

void

traceMethodCalls

​(boolean on)

Deprecated, for removal: This API element is subject to removal in a future version.

This method was intended to control method call tracing.

static

Runtime.Version

version

()

Returns the version of the Java Runtime Environment as a

Runtime.Version

.

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

Registers a new virtual-machine shutdown hook.

Returns the number of processors available to the Java virtual machine.

Executes the specified string command in a separate process.

Executes the specified command and arguments in a separate process.

Executes the specified command and arguments in a separate process
with the specified environment.

Executes the specified command and arguments in a separate process with
the specified environment and working directory.

Executes the specified string command in a separate process with the
specified environment.

Executes the specified string command in a separate process with the
specified environment and working directory.

Terminates the currently running Java virtual machine by initiating its
shutdown sequence.

Returns the amount of free memory in the Java Virtual Machine.

Runs the garbage collector.

Returns the runtime object associated with the current Java application.

Forcibly terminates the currently running Java virtual machine.

Loads the native library specified by the filename argument.

Loads the native library specified by the

libname

argument.

Returns the maximum amount of memory that the Java virtual machine
will attempt to use.

De-registers a previously-registered virtual-machine shutdown hook.

Runs the finalization methods of any objects pending finalization.

Returns the total amount of memory in the Java virtual machine.

Deprecated, for removal: This API element is subject to removal in a future version.

This method was intended to control instruction tracing.

Deprecated, for removal: This API element is subject to removal in a future version.

This method was intended to control method call tracing.

Returns the version of the Java Runtime Environment as a

Runtime.Version

.

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

============ METHOD DETAIL ==========

- Method Detail

- getRuntime

```java
public static
Runtime
getRuntime()
```

Returns the runtime object associated with the current Java application.
Most of the methods of class

Runtime

are instance
methods and must be invoked with respect to the current runtime object.

**Returns:** the

Runtime

object associated with the current
Java application.

- exit

```java
public void exit​(int status)
```

Terminates the currently running Java virtual machine by initiating its
shutdown sequence. This method never returns normally. The argument
serves as a status code; by convention, a nonzero status code indicates
abnormal termination.

All registered

shutdown hooks

, if any,
are started in some unspecified order and allowed to run concurrently
until they finish. Once this is done the virtual machine

halts

.

If this method is invoked after all shutdown hooks have already
been run and the status is nonzero then this method halts the
virtual machine with the given status code. Otherwise, this method
blocks indefinitely.

The

System.exit

method is the
conventional and convenient means of invoking this method.

**Parameters:** status

- Termination status. By convention, a nonzero status code
indicates abnormal termination.
**Throws:** SecurityException

- If a security manager is present and its

checkExit

method does not permit
exiting with the specified status
**See Also:** SecurityException

,

SecurityManager.checkExit(int)

,

addShutdownHook(java.lang.Thread)

,

removeShutdownHook(java.lang.Thread)

,

halt(int)

- addShutdownHook

```java
public void addShutdownHook​(
Thread
hook)
```

Registers a new virtual-machine shutdown hook.

The Java virtual machine

shuts down

in response to two kinds
of events:

- The program

exits

normally, when the last non-daemon
thread exits or when the

exit

(equivalently,

System.exit

) method is invoked, or

The virtual machine is

terminated

in response to a
user interrupt, such as typing

^C

, or a system-wide event,
such as user logoff or system shutdown.

A

shutdown hook

is simply an initialized but unstarted
thread. When the virtual machine begins its shutdown sequence it will
start all registered shutdown hooks in some unspecified order and let
them run concurrently. When all the hooks have finished it will then
halt. Note that daemon threads will continue to run during the shutdown
sequence, as will non-daemon threads if shutdown was initiated by
invoking the

exit

method.

Once the shutdown sequence has begun it can be stopped only by
invoking the

halt

method, which forcibly
terminates the virtual machine.

Once the shutdown sequence has begun it is impossible to register a
new shutdown hook or de-register a previously-registered hook.
Attempting either of these operations will cause an

IllegalStateException

to be thrown.

Shutdown hooks run at a delicate time in the life cycle of a virtual
machine and should therefore be coded defensively. They should, in
particular, be written to be thread-safe and to avoid deadlocks insofar
as possible. They should also not rely blindly upon services that may
have registered their own shutdown hooks and therefore may themselves in
the process of shutting down. Attempts to use other thread-based
services such as the AWT event-dispatch thread, for example, may lead to
deadlocks.

Shutdown hooks should also finish their work quickly. When a
program invokes

exit

the expectation is
that the virtual machine will promptly shut down and exit. When the
virtual machine is terminated due to user logoff or system shutdown the
underlying operating system may only allow a fixed amount of time in
which to shut down and exit. It is therefore inadvisable to attempt any
user interaction or to perform a long-running computation in a shutdown
hook.

Uncaught exceptions are handled in shutdown hooks just as in any
other thread, by invoking the

uncaughtException

method of the
thread's

ThreadGroup

object. The default implementation of this
method prints the exception's stack trace to

System.err

and
terminates the thread; it does not cause the virtual machine to exit or
halt.

In rare circumstances the virtual machine may

abort

, that is,
stop running without shutting down cleanly. This occurs when the
virtual machine is terminated externally, for example with the

SIGKILL

signal on Unix or the

TerminateProcess

call on
Microsoft Windows. The virtual machine may also abort if a native
method goes awry by, for example, corrupting internal data structures or
attempting to access nonexistent memory. If the virtual machine aborts
then no guarantee can be made about whether or not any shutdown hooks
will be run.

**Parameters:** hook

- An initialized but unstarted

Thread

object
**Throws:** IllegalArgumentException

- If the specified hook has already been registered,
or if it can be determined that the hook is already running or
has already been run
**Throws:** IllegalStateException

- If the virtual machine is already in the process
of shutting down
**Throws:** SecurityException

- If a security manager is present and it denies

RuntimePermission

("shutdownHooks")
**Since:** 1.3
**See Also:** removeShutdownHook(java.lang.Thread)

,

halt(int)

,

exit(int)

- removeShutdownHook

```java
public boolean removeShutdownHook​(
Thread
hook)
```

De-registers a previously-registered virtual-machine shutdown hook.

**Parameters:** hook

- the hook to remove
**Returns:** true

if the specified hook had previously been
registered and was successfully de-registered,

false

otherwise.
**Throws:** IllegalStateException

- If the virtual machine is already in the process of shutting
down
**Throws:** SecurityException

- If a security manager is present and it denies

RuntimePermission

("shutdownHooks")
**Since:** 1.3
**See Also:** addShutdownHook(java.lang.Thread)

,

exit(int)

- halt

```java
public void halt​(int status)
```

Forcibly terminates the currently running Java virtual machine. This
method never returns normally.

This method should be used with extreme caution. Unlike the

exit

method, this method does not cause shutdown
hooks to be started. If the shutdown sequence has already been
initiated then this method does not wait for any running
shutdown hooks to finish their work.

**Parameters:** status

- Termination status. By convention, a nonzero status code
indicates abnormal termination. If the

exit

(equivalently,

System.exit

) method
has already been invoked then this status code
will override the status code passed to that method.
**Throws:** SecurityException

- If a security manager is present and its

checkExit

method
does not permit an exit with the specified status
**Since:** 1.3
**See Also:** exit(int)

,

addShutdownHook(java.lang.Thread)

,

removeShutdownHook(java.lang.Thread)

- exec

```java
public
Process
exec​(
String
command)
throws
IOException
```

Executes the specified string command in a separate process.

This is a convenience method. An invocation of the form

exec(command)

behaves in exactly the same way as the invocation

exec

(command, null, null)

.

**Parameters:** command

- a specified system command.
**Returns:** A new

Process

object for managing the subprocess
**Throws:** SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

command

is

null
**Throws:** IllegalArgumentException

- If

command

is empty
**See Also:** exec(String[], String[], File)

,

ProcessBuilder

- exec

```java
public
Process
exec​(
String
command,

String
[] envp)
throws
IOException
```

Executes the specified string command in a separate process with the
specified environment.

This is a convenience method. An invocation of the form

exec(command, envp)

behaves in exactly the same way as the invocation

exec

(command, envp, null)

.

**Parameters:** command

- a specified system command.
**Parameters:** envp

- array of strings, each element of which
has environment variable settings in the format

name

=

value

, or

null

if the subprocess should inherit
the environment of the current process.
**Returns:** A new

Process

object for managing the subprocess
**Throws:** SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

command

is

null

,
or one of the elements of

envp

is

null
**Throws:** IllegalArgumentException

- If

command

is empty
**See Also:** exec(String[], String[], File)

,

ProcessBuilder

- exec

```java
public
Process
exec​(
String
command,

String
[] envp,

File
dir)
throws
IOException
```

Executes the specified string command in a separate process with the
specified environment and working directory.

This is a convenience method. An invocation of the form

exec(command, envp, dir)

behaves in exactly the same way as the invocation

exec

(cmdarray, envp, dir)

,
where

cmdarray

is an array of all the tokens in

command

.

More precisely, the

command

string is broken
into tokens using a

StringTokenizer

created by the call

new {@link StringTokenizer}(command)

with no
further modification of the character categories. The tokens
produced by the tokenizer are then placed in the new string
array

cmdarray

, in the same order.

**Parameters:** command

- a specified system command.
**Parameters:** envp

- array of strings, each element of which
has environment variable settings in the format

name

=

value

, or

null

if the subprocess should inherit
the environment of the current process.
**Parameters:** dir

- the working directory of the subprocess, or

null

if the subprocess should inherit
the working directory of the current process.
**Returns:** A new

Process

object for managing the subprocess
**Throws:** SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

command

is

null

,
or one of the elements of

envp

is

null
**Throws:** IllegalArgumentException

- If

command

is empty
**Since:** 1.3
**See Also:** ProcessBuilder

- exec

```java
public
Process
exec​(
String
[] cmdarray)
throws
IOException
```

Executes the specified command and arguments in a separate process.

This is a convenience method. An invocation of the form

exec(cmdarray)

behaves in exactly the same way as the invocation

exec

(cmdarray, null, null)

.

**Parameters:** cmdarray

- array containing the command to call and
its arguments.
**Returns:** A new

Process

object for managing the subprocess
**Throws:** SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

cmdarray

is

null

,
or one of the elements of

cmdarray

is

null
**Throws:** IndexOutOfBoundsException

- If

cmdarray

is an empty array
(has length

0

)
**See Also:** ProcessBuilder

- exec

```java
public
Process
exec​(
String
[] cmdarray,

String
[] envp)
throws
IOException
```

Executes the specified command and arguments in a separate process
with the specified environment.

This is a convenience method. An invocation of the form

exec(cmdarray, envp)

behaves in exactly the same way as the invocation

exec

(cmdarray, envp, null)

.

**Parameters:** cmdarray

- array containing the command to call and
its arguments.
**Parameters:** envp

- array of strings, each element of which
has environment variable settings in the format

name

=

value

, or

null

if the subprocess should inherit
the environment of the current process.
**Returns:** A new

Process

object for managing the subprocess
**Throws:** SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

cmdarray

is

null

,
or one of the elements of

cmdarray

is

null

,
or one of the elements of

envp

is

null
**Throws:** IndexOutOfBoundsException

- If

cmdarray

is an empty array
(has length

0

)
**See Also:** ProcessBuilder

- exec

```java
public
Process
exec​(
String
[] cmdarray,

String
[] envp,

File
dir)
throws
IOException
```

Executes the specified command and arguments in a separate process with
the specified environment and working directory.

Given an array of strings

cmdarray

, representing the
tokens of a command line, and an array of strings

envp

,
representing "environment" variable settings, this method creates
a new process in which to execute the specified command.

This method checks that

cmdarray

is a valid operating
system command. Which commands are valid is system-dependent,
but at the very least the command must be a non-empty list of
non-null strings.

If

envp

is

null

, the subprocess inherits the
environment settings of the current process.

A minimal set of system dependent environment variables may
be required to start a process on some operating systems.
As a result, the subprocess may inherit additional environment variable
settings beyond those in the specified environment.

ProcessBuilder.start()

is now the preferred way to
start a process with a modified environment.

The working directory of the new subprocess is specified by

dir

.
If

dir

is

null

, the subprocess inherits the
current working directory of the current process.

If a security manager exists, its

checkExec

method is invoked with the first component of the array

cmdarray

as its argument. This may result in a

SecurityException

being thrown.

Starting an operating system process is highly system-dependent.
Among the many things that can go wrong are:

- The operating system program file was not found.

Access to the program file was denied.

The working directory does not exist.

In such cases an exception will be thrown. The exact nature
of the exception is system-dependent, but it will always be a
subclass of

IOException

.

If the operating system does not support the creation of
processes, an

UnsupportedOperationException

will be thrown.

**Parameters:** cmdarray

- array containing the command to call and
its arguments.
**Parameters:** envp

- array of strings, each element of which
has environment variable settings in the format

name

=

value

, or

null

if the subprocess should inherit
the environment of the current process.
**Parameters:** dir

- the working directory of the subprocess, or

null

if the subprocess should inherit
the working directory of the current process.
**Returns:** A new

Process

object for managing the subprocess
**Throws:** SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
**Throws:** UnsupportedOperationException

- If the operating system does not support the creation of processes.
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

cmdarray

is

null

,
or one of the elements of

cmdarray

is

null

,
or one of the elements of

envp

is

null
**Throws:** IndexOutOfBoundsException

- If

cmdarray

is an empty array
(has length

0

)
**Since:** 1.3
**See Also:** ProcessBuilder

- availableProcessors

```java
public int availableProcessors()
```

Returns the number of processors available to the Java virtual machine.

This value may change during a particular invocation of the virtual
machine. Applications that are sensitive to the number of available
processors should therefore occasionally poll this property and adjust
their resource usage appropriately.

**Returns:** the maximum number of processors available to the virtual
machine; never smaller than one
**Since:** 1.4

- freeMemory

```java
public long freeMemory()
```

Returns the amount of free memory in the Java Virtual Machine.
Calling the

gc

method may result in increasing the value returned
by

freeMemory.

**Returns:** an approximation to the total amount of memory currently
available for future allocated objects, measured in bytes.

- totalMemory

```java
public long totalMemory()
```

Returns the total amount of memory in the Java virtual machine.
The value returned by this method may vary over time, depending on
the host environment.

Note that the amount of memory required to hold an object of any
given type may be implementation-dependent.

**Returns:** the total amount of memory currently available for current
and future objects, measured in bytes.

- maxMemory

```java
public long maxMemory()
```

Returns the maximum amount of memory that the Java virtual machine
will attempt to use. If there is no inherent limit then the value

Long.MAX_VALUE

will be returned.

**Returns:** the maximum amount of memory that the virtual machine will
attempt to use, measured in bytes
**Since:** 1.4

- gc

```java
public void gc()
```

Runs the garbage collector.
Calling this method suggests that the Java virtual machine expend
effort toward recycling unused objects in order to make the memory
they currently occupy available for quick reuse. When control
returns from the method call, the virtual machine has made
its best effort to recycle all discarded objects.

The name

gc

stands for "garbage
collector". The virtual machine performs this recycling
process automatically as needed, in a separate thread, even if the

gc

method is not invoked explicitly.

The method

System.gc()

is the conventional and convenient
means of invoking this method.

- runFinalization

```java
public void runFinalization()
```

Runs the finalization methods of any objects pending finalization.
Calling this method suggests that the Java virtual machine expend
effort toward running the

finalize

methods of objects
that have been found to be discarded but whose

finalize

methods have not yet been run. When control returns from the
method call, the virtual machine has made a best effort to
complete all outstanding finalizations.

The virtual machine performs the finalization process
automatically as needed, in a separate thread, if the

runFinalization

method is not invoked explicitly.

The method

System.runFinalization()

is the conventional
and convenient means of invoking this method.

**See Also:** Object.finalize()

- traceInstructions

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public void traceInstructions​(boolean on)
```

Deprecated, for removal: This API element is subject to removal in a future version.

This method was intended to control instruction tracing.
It has been superseded by JVM-specific tracing mechanisms.
This method is subject to removal in a future version of Java SE.

Not implemented, does nothing.

**Parameters:** on

- ignored

- traceMethodCalls

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public void traceMethodCalls​(boolean on)
```

Deprecated, for removal: This API element is subject to removal in a future version.

This method was intended to control method call tracing.
It has been superseded by JVM-specific tracing mechanisms.
This method is subject to removal in a future version of Java SE.

Not implemented, does nothing.

**Parameters:** on

- ignored

- load

```java
public void load​(
String
filename)
```

Loads the native library specified by the filename argument. The filename
argument must be an absolute path name.
(for example

Runtime.getRuntime().load("/home/avh/lib/libX11.so");

).

If the filename argument, when stripped of any platform-specific library
prefix, path, and file extension, indicates a library whose name is,
for example, L, and a native library called L is statically linked
with the VM, then the JNI_OnLoad_L function exported by the library
is invoked rather than attempting to load a dynamic library.
A filename matching the argument does not have to exist in the file
system.
See the

JNI Specification

for more details.

Otherwise, the filename argument is mapped to a native library image in
an implementation-dependent manner.

First, if there is a security manager, its

checkLink

method is called with the

filename

as its argument.
This may result in a security exception.

This is similar to the method

loadLibrary(String)

, but it
accepts a general file name as an argument rather than just a library
name, allowing any file of native code to be loaded.

The method

System.load(String)

is the conventional and
convenient means of invoking this method.

**Parameters:** filename

- the file to load.
**Throws:** SecurityException

- if a security manager exists and its

checkLink

method doesn't allow
loading of the specified dynamic library
**Throws:** UnsatisfiedLinkError

- if either the filename is not an
absolute path name, the native library is not statically
linked with the VM, or the library cannot be mapped to
a native library image by the host system.
**Throws:** NullPointerException

- if

filename

is

null
**See Also:** getRuntime()

,

SecurityException

,

SecurityManager.checkLink(java.lang.String)

- loadLibrary

```java
public void loadLibrary​(
String
libname)
```

Loads the native library specified by the

libname

argument. The

libname

argument must not contain any platform
specific prefix, file extension or path. If a native library
called

libname

is statically linked with the VM, then the
JNI_OnLoad_

libname

function exported by the library is invoked.
See the

JNI Specification

for more details.

Otherwise, the libname argument is loaded from a system library
location and mapped to a native library image in an implementation-
dependent manner.

First, if there is a security manager, its

checkLink

method is called with the

libname

as its argument.
This may result in a security exception.

The method

System.loadLibrary(String)

is the conventional
and convenient means of invoking this method. If native
methods are to be used in the implementation of a class, a standard
strategy is to put the native code in a library file (call it

LibFile

) and then to put a static initializer:

```java
static { System.loadLibrary("LibFile"); }
```

within the class declaration. When the class is loaded and
initialized, the necessary native code implementation for the native
methods will then be loaded as well.

If this method is called more than once with the same library
name, the second and subsequent calls are ignored.

**Parameters:** libname

- the name of the library.
**Throws:** SecurityException

- if a security manager exists and its

checkLink

method doesn't allow
loading of the specified dynamic library
**Throws:** UnsatisfiedLinkError

- if either the libname argument
contains a file path, the native library is not statically
linked with the VM, or the library cannot be mapped to a
native library image by the host system.
**Throws:** NullPointerException

- if

libname

is

null
**See Also:** SecurityException

,

SecurityManager.checkLink(java.lang.String)

- version

```java
public static
Runtime.Version
version()
```

Returns the version of the Java Runtime Environment as a

Runtime.Version

.

**Returns:** the

Runtime.Version

of the Java Runtime Environment
**Since:** 9

Method Detail

- getRuntime

```java
public static
Runtime
getRuntime()
```

Returns the runtime object associated with the current Java application.
Most of the methods of class

Runtime

are instance
methods and must be invoked with respect to the current runtime object.

**Returns:** the

Runtime

object associated with the current
Java application.

- exit

```java
public void exit​(int status)
```

Terminates the currently running Java virtual machine by initiating its
shutdown sequence. This method never returns normally. The argument
serves as a status code; by convention, a nonzero status code indicates
abnormal termination.

All registered

shutdown hooks

, if any,
are started in some unspecified order and allowed to run concurrently
until they finish. Once this is done the virtual machine

halts

.

If this method is invoked after all shutdown hooks have already
been run and the status is nonzero then this method halts the
virtual machine with the given status code. Otherwise, this method
blocks indefinitely.

The

System.exit

method is the
conventional and convenient means of invoking this method.

**Parameters:** status

- Termination status. By convention, a nonzero status code
indicates abnormal termination.
**Throws:** SecurityException

- If a security manager is present and its

checkExit

method does not permit
exiting with the specified status
**See Also:** SecurityException

,

SecurityManager.checkExit(int)

,

addShutdownHook(java.lang.Thread)

,

removeShutdownHook(java.lang.Thread)

,

halt(int)

- addShutdownHook

```java
public void addShutdownHook​(
Thread
hook)
```

Registers a new virtual-machine shutdown hook.

The Java virtual machine

shuts down

in response to two kinds
of events:

- The program

exits

normally, when the last non-daemon
thread exits or when the

exit

(equivalently,

System.exit

) method is invoked, or

The virtual machine is

terminated

in response to a
user interrupt, such as typing

^C

, or a system-wide event,
such as user logoff or system shutdown.

A

shutdown hook

is simply an initialized but unstarted
thread. When the virtual machine begins its shutdown sequence it will
start all registered shutdown hooks in some unspecified order and let
them run concurrently. When all the hooks have finished it will then
halt. Note that daemon threads will continue to run during the shutdown
sequence, as will non-daemon threads if shutdown was initiated by
invoking the

exit

method.

Once the shutdown sequence has begun it can be stopped only by
invoking the

halt

method, which forcibly
terminates the virtual machine.

Once the shutdown sequence has begun it is impossible to register a
new shutdown hook or de-register a previously-registered hook.
Attempting either of these operations will cause an

IllegalStateException

to be thrown.

Shutdown hooks run at a delicate time in the life cycle of a virtual
machine and should therefore be coded defensively. They should, in
particular, be written to be thread-safe and to avoid deadlocks insofar
as possible. They should also not rely blindly upon services that may
have registered their own shutdown hooks and therefore may themselves in
the process of shutting down. Attempts to use other thread-based
services such as the AWT event-dispatch thread, for example, may lead to
deadlocks.

Shutdown hooks should also finish their work quickly. When a
program invokes

exit

the expectation is
that the virtual machine will promptly shut down and exit. When the
virtual machine is terminated due to user logoff or system shutdown the
underlying operating system may only allow a fixed amount of time in
which to shut down and exit. It is therefore inadvisable to attempt any
user interaction or to perform a long-running computation in a shutdown
hook.

Uncaught exceptions are handled in shutdown hooks just as in any
other thread, by invoking the

uncaughtException

method of the
thread's

ThreadGroup

object. The default implementation of this
method prints the exception's stack trace to

System.err

and
terminates the thread; it does not cause the virtual machine to exit or
halt.

In rare circumstances the virtual machine may

abort

, that is,
stop running without shutting down cleanly. This occurs when the
virtual machine is terminated externally, for example with the

SIGKILL

signal on Unix or the

TerminateProcess

call on
Microsoft Windows. The virtual machine may also abort if a native
method goes awry by, for example, corrupting internal data structures or
attempting to access nonexistent memory. If the virtual machine aborts
then no guarantee can be made about whether or not any shutdown hooks
will be run.

**Parameters:** hook

- An initialized but unstarted

Thread

object
**Throws:** IllegalArgumentException

- If the specified hook has already been registered,
or if it can be determined that the hook is already running or
has already been run
**Throws:** IllegalStateException

- If the virtual machine is already in the process
of shutting down
**Throws:** SecurityException

- If a security manager is present and it denies

RuntimePermission

("shutdownHooks")
**Since:** 1.3
**See Also:** removeShutdownHook(java.lang.Thread)

,

halt(int)

,

exit(int)

- removeShutdownHook

```java
public boolean removeShutdownHook​(
Thread
hook)
```

De-registers a previously-registered virtual-machine shutdown hook.

**Parameters:** hook

- the hook to remove
**Returns:** true

if the specified hook had previously been
registered and was successfully de-registered,

false

otherwise.
**Throws:** IllegalStateException

- If the virtual machine is already in the process of shutting
down
**Throws:** SecurityException

- If a security manager is present and it denies

RuntimePermission

("shutdownHooks")
**Since:** 1.3
**See Also:** addShutdownHook(java.lang.Thread)

,

exit(int)

- halt

```java
public void halt​(int status)
```

Forcibly terminates the currently running Java virtual machine. This
method never returns normally.

This method should be used with extreme caution. Unlike the

exit

method, this method does not cause shutdown
hooks to be started. If the shutdown sequence has already been
initiated then this method does not wait for any running
shutdown hooks to finish their work.

**Parameters:** status

- Termination status. By convention, a nonzero status code
indicates abnormal termination. If the

exit

(equivalently,

System.exit

) method
has already been invoked then this status code
will override the status code passed to that method.
**Throws:** SecurityException

- If a security manager is present and its

checkExit

method
does not permit an exit with the specified status
**Since:** 1.3
**See Also:** exit(int)

,

addShutdownHook(java.lang.Thread)

,

removeShutdownHook(java.lang.Thread)

- exec

```java
public
Process
exec​(
String
command)
throws
IOException
```

Executes the specified string command in a separate process.

This is a convenience method. An invocation of the form

exec(command)

behaves in exactly the same way as the invocation

exec

(command, null, null)

.

**Parameters:** command

- a specified system command.
**Returns:** A new

Process

object for managing the subprocess
**Throws:** SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

command

is

null
**Throws:** IllegalArgumentException

- If

command

is empty
**See Also:** exec(String[], String[], File)

,

ProcessBuilder

- exec

```java
public
Process
exec​(
String
command,

String
[] envp)
throws
IOException
```

Executes the specified string command in a separate process with the
specified environment.

This is a convenience method. An invocation of the form

exec(command, envp)

behaves in exactly the same way as the invocation

exec

(command, envp, null)

.

**Parameters:** command

- a specified system command.
**Parameters:** envp

- array of strings, each element of which
has environment variable settings in the format

name

=

value

, or

null

if the subprocess should inherit
the environment of the current process.
**Returns:** A new

Process

object for managing the subprocess
**Throws:** SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

command

is

null

,
or one of the elements of

envp

is

null
**Throws:** IllegalArgumentException

- If

command

is empty
**See Also:** exec(String[], String[], File)

,

ProcessBuilder

- exec

```java
public
Process
exec​(
String
command,

String
[] envp,

File
dir)
throws
IOException
```

Executes the specified string command in a separate process with the
specified environment and working directory.

This is a convenience method. An invocation of the form

exec(command, envp, dir)

behaves in exactly the same way as the invocation

exec

(cmdarray, envp, dir)

,
where

cmdarray

is an array of all the tokens in

command

.

More precisely, the

command

string is broken
into tokens using a

StringTokenizer

created by the call

new {@link StringTokenizer}(command)

with no
further modification of the character categories. The tokens
produced by the tokenizer are then placed in the new string
array

cmdarray

, in the same order.

**Parameters:** command

- a specified system command.
**Parameters:** envp

- array of strings, each element of which
has environment variable settings in the format

name

=

value

, or

null

if the subprocess should inherit
the environment of the current process.
**Parameters:** dir

- the working directory of the subprocess, or

null

if the subprocess should inherit
the working directory of the current process.
**Returns:** A new

Process

object for managing the subprocess
**Throws:** SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

command

is

null

,
or one of the elements of

envp

is

null
**Throws:** IllegalArgumentException

- If

command

is empty
**Since:** 1.3
**See Also:** ProcessBuilder

- exec

```java
public
Process
exec​(
String
[] cmdarray)
throws
IOException
```

Executes the specified command and arguments in a separate process.

This is a convenience method. An invocation of the form

exec(cmdarray)

behaves in exactly the same way as the invocation

exec

(cmdarray, null, null)

.

**Parameters:** cmdarray

- array containing the command to call and
its arguments.
**Returns:** A new

Process

object for managing the subprocess
**Throws:** SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

cmdarray

is

null

,
or one of the elements of

cmdarray

is

null
**Throws:** IndexOutOfBoundsException

- If

cmdarray

is an empty array
(has length

0

)
**See Also:** ProcessBuilder

- exec

```java
public
Process
exec​(
String
[] cmdarray,

String
[] envp)
throws
IOException
```

Executes the specified command and arguments in a separate process
with the specified environment.

This is a convenience method. An invocation of the form

exec(cmdarray, envp)

behaves in exactly the same way as the invocation

exec

(cmdarray, envp, null)

.

**Parameters:** cmdarray

- array containing the command to call and
its arguments.
**Parameters:** envp

- array of strings, each element of which
has environment variable settings in the format

name

=

value

, or

null

if the subprocess should inherit
the environment of the current process.
**Returns:** A new

Process

object for managing the subprocess
**Throws:** SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

cmdarray

is

null

,
or one of the elements of

cmdarray

is

null

,
or one of the elements of

envp

is

null
**Throws:** IndexOutOfBoundsException

- If

cmdarray

is an empty array
(has length

0

)
**See Also:** ProcessBuilder

- exec

```java
public
Process
exec​(
String
[] cmdarray,

String
[] envp,

File
dir)
throws
IOException
```

Executes the specified command and arguments in a separate process with
the specified environment and working directory.

Given an array of strings

cmdarray

, representing the
tokens of a command line, and an array of strings

envp

,
representing "environment" variable settings, this method creates
a new process in which to execute the specified command.

This method checks that

cmdarray

is a valid operating
system command. Which commands are valid is system-dependent,
but at the very least the command must be a non-empty list of
non-null strings.

If

envp

is

null

, the subprocess inherits the
environment settings of the current process.

A minimal set of system dependent environment variables may
be required to start a process on some operating systems.
As a result, the subprocess may inherit additional environment variable
settings beyond those in the specified environment.

ProcessBuilder.start()

is now the preferred way to
start a process with a modified environment.

The working directory of the new subprocess is specified by

dir

.
If

dir

is

null

, the subprocess inherits the
current working directory of the current process.

If a security manager exists, its

checkExec

method is invoked with the first component of the array

cmdarray

as its argument. This may result in a

SecurityException

being thrown.

Starting an operating system process is highly system-dependent.
Among the many things that can go wrong are:

- The operating system program file was not found.

Access to the program file was denied.

The working directory does not exist.

In such cases an exception will be thrown. The exact nature
of the exception is system-dependent, but it will always be a
subclass of

IOException

.

If the operating system does not support the creation of
processes, an

UnsupportedOperationException

will be thrown.

**Parameters:** cmdarray

- array containing the command to call and
its arguments.
**Parameters:** envp

- array of strings, each element of which
has environment variable settings in the format

name

=

value

, or

null

if the subprocess should inherit
the environment of the current process.
**Parameters:** dir

- the working directory of the subprocess, or

null

if the subprocess should inherit
the working directory of the current process.
**Returns:** A new

Process

object for managing the subprocess
**Throws:** SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
**Throws:** UnsupportedOperationException

- If the operating system does not support the creation of processes.
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

cmdarray

is

null

,
or one of the elements of

cmdarray

is

null

,
or one of the elements of

envp

is

null
**Throws:** IndexOutOfBoundsException

- If

cmdarray

is an empty array
(has length

0

)
**Since:** 1.3
**See Also:** ProcessBuilder

- availableProcessors

```java
public int availableProcessors()
```

Returns the number of processors available to the Java virtual machine.

This value may change during a particular invocation of the virtual
machine. Applications that are sensitive to the number of available
processors should therefore occasionally poll this property and adjust
their resource usage appropriately.

**Returns:** the maximum number of processors available to the virtual
machine; never smaller than one
**Since:** 1.4

- freeMemory

```java
public long freeMemory()
```

Returns the amount of free memory in the Java Virtual Machine.
Calling the

gc

method may result in increasing the value returned
by

freeMemory.

**Returns:** an approximation to the total amount of memory currently
available for future allocated objects, measured in bytes.

- totalMemory

```java
public long totalMemory()
```

Returns the total amount of memory in the Java virtual machine.
The value returned by this method may vary over time, depending on
the host environment.

Note that the amount of memory required to hold an object of any
given type may be implementation-dependent.

**Returns:** the total amount of memory currently available for current
and future objects, measured in bytes.

- maxMemory

```java
public long maxMemory()
```

Returns the maximum amount of memory that the Java virtual machine
will attempt to use. If there is no inherent limit then the value

Long.MAX_VALUE

will be returned.

**Returns:** the maximum amount of memory that the virtual machine will
attempt to use, measured in bytes
**Since:** 1.4

- gc

```java
public void gc()
```

Runs the garbage collector.
Calling this method suggests that the Java virtual machine expend
effort toward recycling unused objects in order to make the memory
they currently occupy available for quick reuse. When control
returns from the method call, the virtual machine has made
its best effort to recycle all discarded objects.

The name

gc

stands for "garbage
collector". The virtual machine performs this recycling
process automatically as needed, in a separate thread, even if the

gc

method is not invoked explicitly.

The method

System.gc()

is the conventional and convenient
means of invoking this method.

- runFinalization

```java
public void runFinalization()
```

Runs the finalization methods of any objects pending finalization.
Calling this method suggests that the Java virtual machine expend
effort toward running the

finalize

methods of objects
that have been found to be discarded but whose

finalize

methods have not yet been run. When control returns from the
method call, the virtual machine has made a best effort to
complete all outstanding finalizations.

The virtual machine performs the finalization process
automatically as needed, in a separate thread, if the

runFinalization

method is not invoked explicitly.

The method

System.runFinalization()

is the conventional
and convenient means of invoking this method.

**See Also:** Object.finalize()

- traceInstructions

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public void traceInstructions​(boolean on)
```

Deprecated, for removal: This API element is subject to removal in a future version.

This method was intended to control instruction tracing.
It has been superseded by JVM-specific tracing mechanisms.
This method is subject to removal in a future version of Java SE.

Not implemented, does nothing.

**Parameters:** on

- ignored

- traceMethodCalls

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public void traceMethodCalls​(boolean on)
```

Deprecated, for removal: This API element is subject to removal in a future version.

This method was intended to control method call tracing.
It has been superseded by JVM-specific tracing mechanisms.
This method is subject to removal in a future version of Java SE.

Not implemented, does nothing.

**Parameters:** on

- ignored

- load

```java
public void load​(
String
filename)
```

Loads the native library specified by the filename argument. The filename
argument must be an absolute path name.
(for example

Runtime.getRuntime().load("/home/avh/lib/libX11.so");

).

If the filename argument, when stripped of any platform-specific library
prefix, path, and file extension, indicates a library whose name is,
for example, L, and a native library called L is statically linked
with the VM, then the JNI_OnLoad_L function exported by the library
is invoked rather than attempting to load a dynamic library.
A filename matching the argument does not have to exist in the file
system.
See the

JNI Specification

for more details.

Otherwise, the filename argument is mapped to a native library image in
an implementation-dependent manner.

First, if there is a security manager, its

checkLink

method is called with the

filename

as its argument.
This may result in a security exception.

This is similar to the method

loadLibrary(String)

, but it
accepts a general file name as an argument rather than just a library
name, allowing any file of native code to be loaded.

The method

System.load(String)

is the conventional and
convenient means of invoking this method.

**Parameters:** filename

- the file to load.
**Throws:** SecurityException

- if a security manager exists and its

checkLink

method doesn't allow
loading of the specified dynamic library
**Throws:** UnsatisfiedLinkError

- if either the filename is not an
absolute path name, the native library is not statically
linked with the VM, or the library cannot be mapped to
a native library image by the host system.
**Throws:** NullPointerException

- if

filename

is

null
**See Also:** getRuntime()

,

SecurityException

,

SecurityManager.checkLink(java.lang.String)

- loadLibrary

```java
public void loadLibrary​(
String
libname)
```

Loads the native library specified by the

libname

argument. The

libname

argument must not contain any platform
specific prefix, file extension or path. If a native library
called

libname

is statically linked with the VM, then the
JNI_OnLoad_

libname

function exported by the library is invoked.
See the

JNI Specification

for more details.

Otherwise, the libname argument is loaded from a system library
location and mapped to a native library image in an implementation-
dependent manner.

First, if there is a security manager, its

checkLink

method is called with the

libname

as its argument.
This may result in a security exception.

The method

System.loadLibrary(String)

is the conventional
and convenient means of invoking this method. If native
methods are to be used in the implementation of a class, a standard
strategy is to put the native code in a library file (call it

LibFile

) and then to put a static initializer:

```java
static { System.loadLibrary("LibFile"); }
```

within the class declaration. When the class is loaded and
initialized, the necessary native code implementation for the native
methods will then be loaded as well.

If this method is called more than once with the same library
name, the second and subsequent calls are ignored.

**Parameters:** libname

- the name of the library.
**Throws:** SecurityException

- if a security manager exists and its

checkLink

method doesn't allow
loading of the specified dynamic library
**Throws:** UnsatisfiedLinkError

- if either the libname argument
contains a file path, the native library is not statically
linked with the VM, or the library cannot be mapped to a
native library image by the host system.
**Throws:** NullPointerException

- if

libname

is

null
**See Also:** SecurityException

,

SecurityManager.checkLink(java.lang.String)

- version

```java
public static
Runtime.Version
version()
```

Returns the version of the Java Runtime Environment as a

Runtime.Version

.

**Returns:** the

Runtime.Version

of the Java Runtime Environment
**Since:** 9

---

#### Method Detail

getRuntime

```java
public static
Runtime
getRuntime()
```

Returns the runtime object associated with the current Java application.
Most of the methods of class

Runtime

are instance
methods and must be invoked with respect to the current runtime object.

**Returns:** the

Runtime

object associated with the current
Java application.

---

#### getRuntime

public static

Runtime

getRuntime()

Returns the runtime object associated with the current Java application.
Most of the methods of class

Runtime

are instance
methods and must be invoked with respect to the current runtime object.

exit

```java
public void exit​(int status)
```

Terminates the currently running Java virtual machine by initiating its
shutdown sequence. This method never returns normally. The argument
serves as a status code; by convention, a nonzero status code indicates
abnormal termination.

All registered

shutdown hooks

, if any,
are started in some unspecified order and allowed to run concurrently
until they finish. Once this is done the virtual machine

halts

.

If this method is invoked after all shutdown hooks have already
been run and the status is nonzero then this method halts the
virtual machine with the given status code. Otherwise, this method
blocks indefinitely.

The

System.exit

method is the
conventional and convenient means of invoking this method.

**Parameters:** status

- Termination status. By convention, a nonzero status code
indicates abnormal termination.
**Throws:** SecurityException

- If a security manager is present and its

checkExit

method does not permit
exiting with the specified status
**See Also:** SecurityException

,

SecurityManager.checkExit(int)

,

addShutdownHook(java.lang.Thread)

,

removeShutdownHook(java.lang.Thread)

,

halt(int)

---

#### exit

public void exit​(int status)

Terminates the currently running Java virtual machine by initiating its
shutdown sequence. This method never returns normally. The argument
serves as a status code; by convention, a nonzero status code indicates
abnormal termination.

All registered

shutdown hooks

, if any,
are started in some unspecified order and allowed to run concurrently
until they finish. Once this is done the virtual machine

halts

.

If this method is invoked after all shutdown hooks have already
been run and the status is nonzero then this method halts the
virtual machine with the given status code. Otherwise, this method
blocks indefinitely.

The

System.exit

method is the
conventional and convenient means of invoking this method.

All registered

shutdown hooks

, if any,
are started in some unspecified order and allowed to run concurrently
until they finish. Once this is done the virtual machine

halts

.

If this method is invoked after all shutdown hooks have already
been run and the status is nonzero then this method halts the
virtual machine with the given status code. Otherwise, this method
blocks indefinitely.

The

System.exit

method is the
conventional and convenient means of invoking this method.

If this method is invoked after all shutdown hooks have already
been run and the status is nonzero then this method halts the
virtual machine with the given status code. Otherwise, this method
blocks indefinitely.

The

System.exit

method is the
conventional and convenient means of invoking this method.

The

System.exit

method is the
conventional and convenient means of invoking this method.

addShutdownHook

```java
public void addShutdownHook​(
Thread
hook)
```

Registers a new virtual-machine shutdown hook.

The Java virtual machine

shuts down

in response to two kinds
of events:

- The program

exits

normally, when the last non-daemon
thread exits or when the

exit

(equivalently,

System.exit

) method is invoked, or

The virtual machine is

terminated

in response to a
user interrupt, such as typing

^C

, or a system-wide event,
such as user logoff or system shutdown.

A

shutdown hook

is simply an initialized but unstarted
thread. When the virtual machine begins its shutdown sequence it will
start all registered shutdown hooks in some unspecified order and let
them run concurrently. When all the hooks have finished it will then
halt. Note that daemon threads will continue to run during the shutdown
sequence, as will non-daemon threads if shutdown was initiated by
invoking the

exit

method.

Once the shutdown sequence has begun it can be stopped only by
invoking the

halt

method, which forcibly
terminates the virtual machine.

Once the shutdown sequence has begun it is impossible to register a
new shutdown hook or de-register a previously-registered hook.
Attempting either of these operations will cause an

IllegalStateException

to be thrown.

Shutdown hooks run at a delicate time in the life cycle of a virtual
machine and should therefore be coded defensively. They should, in
particular, be written to be thread-safe and to avoid deadlocks insofar
as possible. They should also not rely blindly upon services that may
have registered their own shutdown hooks and therefore may themselves in
the process of shutting down. Attempts to use other thread-based
services such as the AWT event-dispatch thread, for example, may lead to
deadlocks.

Shutdown hooks should also finish their work quickly. When a
program invokes

exit

the expectation is
that the virtual machine will promptly shut down and exit. When the
virtual machine is terminated due to user logoff or system shutdown the
underlying operating system may only allow a fixed amount of time in
which to shut down and exit. It is therefore inadvisable to attempt any
user interaction or to perform a long-running computation in a shutdown
hook.

Uncaught exceptions are handled in shutdown hooks just as in any
other thread, by invoking the

uncaughtException

method of the
thread's

ThreadGroup

object. The default implementation of this
method prints the exception's stack trace to

System.err

and
terminates the thread; it does not cause the virtual machine to exit or
halt.

In rare circumstances the virtual machine may

abort

, that is,
stop running without shutting down cleanly. This occurs when the
virtual machine is terminated externally, for example with the

SIGKILL

signal on Unix or the

TerminateProcess

call on
Microsoft Windows. The virtual machine may also abort if a native
method goes awry by, for example, corrupting internal data structures or
attempting to access nonexistent memory. If the virtual machine aborts
then no guarantee can be made about whether or not any shutdown hooks
will be run.

**Parameters:** hook

- An initialized but unstarted

Thread

object
**Throws:** IllegalArgumentException

- If the specified hook has already been registered,
or if it can be determined that the hook is already running or
has already been run
**Throws:** IllegalStateException

- If the virtual machine is already in the process
of shutting down
**Throws:** SecurityException

- If a security manager is present and it denies

RuntimePermission

("shutdownHooks")
**Since:** 1.3
**See Also:** removeShutdownHook(java.lang.Thread)

,

halt(int)

,

exit(int)

---

#### addShutdownHook

public void addShutdownHook​(

Thread

hook)

Registers a new virtual-machine shutdown hook.

The Java virtual machine

shuts down

in response to two kinds
of events:

- The program

exits

normally, when the last non-daemon
thread exits or when the

exit

(equivalently,

System.exit

) method is invoked, or

The virtual machine is

terminated

in response to a
user interrupt, such as typing

^C

, or a system-wide event,
such as user logoff or system shutdown.

A

shutdown hook

is simply an initialized but unstarted
thread. When the virtual machine begins its shutdown sequence it will
start all registered shutdown hooks in some unspecified order and let
them run concurrently. When all the hooks have finished it will then
halt. Note that daemon threads will continue to run during the shutdown
sequence, as will non-daemon threads if shutdown was initiated by
invoking the

exit

method.

Once the shutdown sequence has begun it can be stopped only by
invoking the

halt

method, which forcibly
terminates the virtual machine.

Once the shutdown sequence has begun it is impossible to register a
new shutdown hook or de-register a previously-registered hook.
Attempting either of these operations will cause an

IllegalStateException

to be thrown.

Shutdown hooks run at a delicate time in the life cycle of a virtual
machine and should therefore be coded defensively. They should, in
particular, be written to be thread-safe and to avoid deadlocks insofar
as possible. They should also not rely blindly upon services that may
have registered their own shutdown hooks and therefore may themselves in
the process of shutting down. Attempts to use other thread-based
services such as the AWT event-dispatch thread, for example, may lead to
deadlocks.

Shutdown hooks should also finish their work quickly. When a
program invokes

exit

the expectation is
that the virtual machine will promptly shut down and exit. When the
virtual machine is terminated due to user logoff or system shutdown the
underlying operating system may only allow a fixed amount of time in
which to shut down and exit. It is therefore inadvisable to attempt any
user interaction or to perform a long-running computation in a shutdown
hook.

Uncaught exceptions are handled in shutdown hooks just as in any
other thread, by invoking the

uncaughtException

method of the
thread's

ThreadGroup

object. The default implementation of this
method prints the exception's stack trace to

System.err

and
terminates the thread; it does not cause the virtual machine to exit or
halt.

In rare circumstances the virtual machine may

abort

, that is,
stop running without shutting down cleanly. This occurs when the
virtual machine is terminated externally, for example with the

SIGKILL

signal on Unix or the

TerminateProcess

call on
Microsoft Windows. The virtual machine may also abort if a native
method goes awry by, for example, corrupting internal data structures or
attempting to access nonexistent memory. If the virtual machine aborts
then no guarantee can be made about whether or not any shutdown hooks
will be run.

The Java virtual machine

shuts down

in response to two kinds
of events:

- The program

exits

normally, when the last non-daemon
thread exits or when the

exit

(equivalently,

System.exit

) method is invoked, or

The virtual machine is

terminated

in response to a
user interrupt, such as typing

^C

, or a system-wide event,
such as user logoff or system shutdown.

A

shutdown hook

is simply an initialized but unstarted
thread. When the virtual machine begins its shutdown sequence it will
start all registered shutdown hooks in some unspecified order and let
them run concurrently. When all the hooks have finished it will then
halt. Note that daemon threads will continue to run during the shutdown
sequence, as will non-daemon threads if shutdown was initiated by
invoking the

exit

method.

Once the shutdown sequence has begun it can be stopped only by
invoking the

halt

method, which forcibly
terminates the virtual machine.

Once the shutdown sequence has begun it is impossible to register a
new shutdown hook or de-register a previously-registered hook.
Attempting either of these operations will cause an

IllegalStateException

to be thrown.

Shutdown hooks run at a delicate time in the life cycle of a virtual
machine and should therefore be coded defensively. They should, in
particular, be written to be thread-safe and to avoid deadlocks insofar
as possible. They should also not rely blindly upon services that may
have registered their own shutdown hooks and therefore may themselves in
the process of shutting down. Attempts to use other thread-based
services such as the AWT event-dispatch thread, for example, may lead to
deadlocks.

Shutdown hooks should also finish their work quickly. When a
program invokes

exit

the expectation is
that the virtual machine will promptly shut down and exit. When the
virtual machine is terminated due to user logoff or system shutdown the
underlying operating system may only allow a fixed amount of time in
which to shut down and exit. It is therefore inadvisable to attempt any
user interaction or to perform a long-running computation in a shutdown
hook.

Uncaught exceptions are handled in shutdown hooks just as in any
other thread, by invoking the

uncaughtException

method of the
thread's

ThreadGroup

object. The default implementation of this
method prints the exception's stack trace to

System.err

and
terminates the thread; it does not cause the virtual machine to exit or
halt.

In rare circumstances the virtual machine may

abort

, that is,
stop running without shutting down cleanly. This occurs when the
virtual machine is terminated externally, for example with the

SIGKILL

signal on Unix or the

TerminateProcess

call on
Microsoft Windows. The virtual machine may also abort if a native
method goes awry by, for example, corrupting internal data structures or
attempting to access nonexistent memory. If the virtual machine aborts
then no guarantee can be made about whether or not any shutdown hooks
will be run.

The program

exits

normally, when the last non-daemon
thread exits or when the

exit

(equivalently,

System.exit

) method is invoked, or

The virtual machine is

terminated

in response to a
user interrupt, such as typing

^C

, or a system-wide event,
such as user logoff or system shutdown.

A

shutdown hook

is simply an initialized but unstarted
thread. When the virtual machine begins its shutdown sequence it will
start all registered shutdown hooks in some unspecified order and let
them run concurrently. When all the hooks have finished it will then
halt. Note that daemon threads will continue to run during the shutdown
sequence, as will non-daemon threads if shutdown was initiated by
invoking the

exit

method.

Once the shutdown sequence has begun it can be stopped only by
invoking the

halt

method, which forcibly
terminates the virtual machine.

Once the shutdown sequence has begun it is impossible to register a
new shutdown hook or de-register a previously-registered hook.
Attempting either of these operations will cause an

IllegalStateException

to be thrown.

Shutdown hooks run at a delicate time in the life cycle of a virtual
machine and should therefore be coded defensively. They should, in
particular, be written to be thread-safe and to avoid deadlocks insofar
as possible. They should also not rely blindly upon services that may
have registered their own shutdown hooks and therefore may themselves in
the process of shutting down. Attempts to use other thread-based
services such as the AWT event-dispatch thread, for example, may lead to
deadlocks.

Shutdown hooks should also finish their work quickly. When a
program invokes

exit

the expectation is
that the virtual machine will promptly shut down and exit. When the
virtual machine is terminated due to user logoff or system shutdown the
underlying operating system may only allow a fixed amount of time in
which to shut down and exit. It is therefore inadvisable to attempt any
user interaction or to perform a long-running computation in a shutdown
hook.

Uncaught exceptions are handled in shutdown hooks just as in any
other thread, by invoking the

uncaughtException

method of the
thread's

ThreadGroup

object. The default implementation of this
method prints the exception's stack trace to

System.err

and
terminates the thread; it does not cause the virtual machine to exit or
halt.

In rare circumstances the virtual machine may

abort

, that is,
stop running without shutting down cleanly. This occurs when the
virtual machine is terminated externally, for example with the

SIGKILL

signal on Unix or the

TerminateProcess

call on
Microsoft Windows. The virtual machine may also abort if a native
method goes awry by, for example, corrupting internal data structures or
attempting to access nonexistent memory. If the virtual machine aborts
then no guarantee can be made about whether or not any shutdown hooks
will be run.

Once the shutdown sequence has begun it can be stopped only by
invoking the

halt

method, which forcibly
terminates the virtual machine.

Once the shutdown sequence has begun it is impossible to register a
new shutdown hook or de-register a previously-registered hook.
Attempting either of these operations will cause an

IllegalStateException

to be thrown.

Shutdown hooks run at a delicate time in the life cycle of a virtual
machine and should therefore be coded defensively. They should, in
particular, be written to be thread-safe and to avoid deadlocks insofar
as possible. They should also not rely blindly upon services that may
have registered their own shutdown hooks and therefore may themselves in
the process of shutting down. Attempts to use other thread-based
services such as the AWT event-dispatch thread, for example, may lead to
deadlocks.

Shutdown hooks should also finish their work quickly. When a
program invokes

exit

the expectation is
that the virtual machine will promptly shut down and exit. When the
virtual machine is terminated due to user logoff or system shutdown the
underlying operating system may only allow a fixed amount of time in
which to shut down and exit. It is therefore inadvisable to attempt any
user interaction or to perform a long-running computation in a shutdown
hook.

Uncaught exceptions are handled in shutdown hooks just as in any
other thread, by invoking the

uncaughtException

method of the
thread's

ThreadGroup

object. The default implementation of this
method prints the exception's stack trace to

System.err

and
terminates the thread; it does not cause the virtual machine to exit or
halt.

In rare circumstances the virtual machine may

abort

, that is,
stop running without shutting down cleanly. This occurs when the
virtual machine is terminated externally, for example with the

SIGKILL

signal on Unix or the

TerminateProcess

call on
Microsoft Windows. The virtual machine may also abort if a native
method goes awry by, for example, corrupting internal data structures or
attempting to access nonexistent memory. If the virtual machine aborts
then no guarantee can be made about whether or not any shutdown hooks
will be run.

Once the shutdown sequence has begun it is impossible to register a
new shutdown hook or de-register a previously-registered hook.
Attempting either of these operations will cause an

IllegalStateException

to be thrown.

Shutdown hooks run at a delicate time in the life cycle of a virtual
machine and should therefore be coded defensively. They should, in
particular, be written to be thread-safe and to avoid deadlocks insofar
as possible. They should also not rely blindly upon services that may
have registered their own shutdown hooks and therefore may themselves in
the process of shutting down. Attempts to use other thread-based
services such as the AWT event-dispatch thread, for example, may lead to
deadlocks.

Shutdown hooks should also finish their work quickly. When a
program invokes

exit

the expectation is
that the virtual machine will promptly shut down and exit. When the
virtual machine is terminated due to user logoff or system shutdown the
underlying operating system may only allow a fixed amount of time in
which to shut down and exit. It is therefore inadvisable to attempt any
user interaction or to perform a long-running computation in a shutdown
hook.

Uncaught exceptions are handled in shutdown hooks just as in any
other thread, by invoking the

uncaughtException

method of the
thread's

ThreadGroup

object. The default implementation of this
method prints the exception's stack trace to

System.err

and
terminates the thread; it does not cause the virtual machine to exit or
halt.

In rare circumstances the virtual machine may

abort

, that is,
stop running without shutting down cleanly. This occurs when the
virtual machine is terminated externally, for example with the

SIGKILL

signal on Unix or the

TerminateProcess

call on
Microsoft Windows. The virtual machine may also abort if a native
method goes awry by, for example, corrupting internal data structures or
attempting to access nonexistent memory. If the virtual machine aborts
then no guarantee can be made about whether or not any shutdown hooks
will be run.

Shutdown hooks run at a delicate time in the life cycle of a virtual
machine and should therefore be coded defensively. They should, in
particular, be written to be thread-safe and to avoid deadlocks insofar
as possible. They should also not rely blindly upon services that may
have registered their own shutdown hooks and therefore may themselves in
the process of shutting down. Attempts to use other thread-based
services such as the AWT event-dispatch thread, for example, may lead to
deadlocks.

Shutdown hooks should also finish their work quickly. When a
program invokes

exit

the expectation is
that the virtual machine will promptly shut down and exit. When the
virtual machine is terminated due to user logoff or system shutdown the
underlying operating system may only allow a fixed amount of time in
which to shut down and exit. It is therefore inadvisable to attempt any
user interaction or to perform a long-running computation in a shutdown
hook.

Uncaught exceptions are handled in shutdown hooks just as in any
other thread, by invoking the

uncaughtException

method of the
thread's

ThreadGroup

object. The default implementation of this
method prints the exception's stack trace to

System.err

and
terminates the thread; it does not cause the virtual machine to exit or
halt.

In rare circumstances the virtual machine may

abort

, that is,
stop running without shutting down cleanly. This occurs when the
virtual machine is terminated externally, for example with the

SIGKILL

signal on Unix or the

TerminateProcess

call on
Microsoft Windows. The virtual machine may also abort if a native
method goes awry by, for example, corrupting internal data structures or
attempting to access nonexistent memory. If the virtual machine aborts
then no guarantee can be made about whether or not any shutdown hooks
will be run.

Shutdown hooks should also finish their work quickly. When a
program invokes

exit

the expectation is
that the virtual machine will promptly shut down and exit. When the
virtual machine is terminated due to user logoff or system shutdown the
underlying operating system may only allow a fixed amount of time in
which to shut down and exit. It is therefore inadvisable to attempt any
user interaction or to perform a long-running computation in a shutdown
hook.

Uncaught exceptions are handled in shutdown hooks just as in any
other thread, by invoking the

uncaughtException

method of the
thread's

ThreadGroup

object. The default implementation of this
method prints the exception's stack trace to

System.err

and
terminates the thread; it does not cause the virtual machine to exit or
halt.

In rare circumstances the virtual machine may

abort

, that is,
stop running without shutting down cleanly. This occurs when the
virtual machine is terminated externally, for example with the

SIGKILL

signal on Unix or the

TerminateProcess

call on
Microsoft Windows. The virtual machine may also abort if a native
method goes awry by, for example, corrupting internal data structures or
attempting to access nonexistent memory. If the virtual machine aborts
then no guarantee can be made about whether or not any shutdown hooks
will be run.

Uncaught exceptions are handled in shutdown hooks just as in any
other thread, by invoking the

uncaughtException

method of the
thread's

ThreadGroup

object. The default implementation of this
method prints the exception's stack trace to

System.err

and
terminates the thread; it does not cause the virtual machine to exit or
halt.

In rare circumstances the virtual machine may

abort

, that is,
stop running without shutting down cleanly. This occurs when the
virtual machine is terminated externally, for example with the

SIGKILL

signal on Unix or the

TerminateProcess

call on
Microsoft Windows. The virtual machine may also abort if a native
method goes awry by, for example, corrupting internal data structures or
attempting to access nonexistent memory. If the virtual machine aborts
then no guarantee can be made about whether or not any shutdown hooks
will be run.

In rare circumstances the virtual machine may

abort

, that is,
stop running without shutting down cleanly. This occurs when the
virtual machine is terminated externally, for example with the

SIGKILL

signal on Unix or the

TerminateProcess

call on
Microsoft Windows. The virtual machine may also abort if a native
method goes awry by, for example, corrupting internal data structures or
attempting to access nonexistent memory. If the virtual machine aborts
then no guarantee can be made about whether or not any shutdown hooks
will be run.

removeShutdownHook

```java
public boolean removeShutdownHook​(
Thread
hook)
```

De-registers a previously-registered virtual-machine shutdown hook.

**Parameters:** hook

- the hook to remove
**Returns:** true

if the specified hook had previously been
registered and was successfully de-registered,

false

otherwise.
**Throws:** IllegalStateException

- If the virtual machine is already in the process of shutting
down
**Throws:** SecurityException

- If a security manager is present and it denies

RuntimePermission

("shutdownHooks")
**Since:** 1.3
**See Also:** addShutdownHook(java.lang.Thread)

,

exit(int)

---

#### removeShutdownHook

public boolean removeShutdownHook​(

Thread

hook)

De-registers a previously-registered virtual-machine shutdown hook.

halt

```java
public void halt​(int status)
```

Forcibly terminates the currently running Java virtual machine. This
method never returns normally.

This method should be used with extreme caution. Unlike the

exit

method, this method does not cause shutdown
hooks to be started. If the shutdown sequence has already been
initiated then this method does not wait for any running
shutdown hooks to finish their work.

**Parameters:** status

- Termination status. By convention, a nonzero status code
indicates abnormal termination. If the

exit

(equivalently,

System.exit

) method
has already been invoked then this status code
will override the status code passed to that method.
**Throws:** SecurityException

- If a security manager is present and its

checkExit

method
does not permit an exit with the specified status
**Since:** 1.3
**See Also:** exit(int)

,

addShutdownHook(java.lang.Thread)

,

removeShutdownHook(java.lang.Thread)

---

#### halt

public void halt​(int status)

Forcibly terminates the currently running Java virtual machine. This
method never returns normally.

This method should be used with extreme caution. Unlike the

exit

method, this method does not cause shutdown
hooks to be started. If the shutdown sequence has already been
initiated then this method does not wait for any running
shutdown hooks to finish their work.

This method should be used with extreme caution. Unlike the

exit

method, this method does not cause shutdown
hooks to be started. If the shutdown sequence has already been
initiated then this method does not wait for any running
shutdown hooks to finish their work.

exec

```java
public
Process
exec​(
String
command)
throws
IOException
```

Executes the specified string command in a separate process.

This is a convenience method. An invocation of the form

exec(command)

behaves in exactly the same way as the invocation

exec

(command, null, null)

.

**Parameters:** command

- a specified system command.
**Returns:** A new

Process

object for managing the subprocess
**Throws:** SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

command

is

null
**Throws:** IllegalArgumentException

- If

command

is empty
**See Also:** exec(String[], String[], File)

,

ProcessBuilder

---

#### exec

public

Process

exec​(

String

command)
throws

IOException

Executes the specified string command in a separate process.

This is a convenience method. An invocation of the form

exec(command)

behaves in exactly the same way as the invocation

exec

(command, null, null)

.

This is a convenience method. An invocation of the form

exec(command)

behaves in exactly the same way as the invocation

exec

(command, null, null)

.

exec

```java
public
Process
exec​(
String
command,

String
[] envp)
throws
IOException
```

Executes the specified string command in a separate process with the
specified environment.

This is a convenience method. An invocation of the form

exec(command, envp)

behaves in exactly the same way as the invocation

exec

(command, envp, null)

.

**Parameters:** command

- a specified system command.
**Parameters:** envp

- array of strings, each element of which
has environment variable settings in the format

name

=

value

, or

null

if the subprocess should inherit
the environment of the current process.
**Returns:** A new

Process

object for managing the subprocess
**Throws:** SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

command

is

null

,
or one of the elements of

envp

is

null
**Throws:** IllegalArgumentException

- If

command

is empty
**See Also:** exec(String[], String[], File)

,

ProcessBuilder

---

#### exec

public

Process

exec​(

String

command,

String

[] envp)
throws

IOException

Executes the specified string command in a separate process with the
specified environment.

This is a convenience method. An invocation of the form

exec(command, envp)

behaves in exactly the same way as the invocation

exec

(command, envp, null)

.

This is a convenience method. An invocation of the form

exec(command, envp)

behaves in exactly the same way as the invocation

exec

(command, envp, null)

.

exec

```java
public
Process
exec​(
String
command,

String
[] envp,

File
dir)
throws
IOException
```

Executes the specified string command in a separate process with the
specified environment and working directory.

This is a convenience method. An invocation of the form

exec(command, envp, dir)

behaves in exactly the same way as the invocation

exec

(cmdarray, envp, dir)

,
where

cmdarray

is an array of all the tokens in

command

.

More precisely, the

command

string is broken
into tokens using a

StringTokenizer

created by the call

new {@link StringTokenizer}(command)

with no
further modification of the character categories. The tokens
produced by the tokenizer are then placed in the new string
array

cmdarray

, in the same order.

**Parameters:** command

- a specified system command.
**Parameters:** envp

- array of strings, each element of which
has environment variable settings in the format

name

=

value

, or

null

if the subprocess should inherit
the environment of the current process.
**Parameters:** dir

- the working directory of the subprocess, or

null

if the subprocess should inherit
the working directory of the current process.
**Returns:** A new

Process

object for managing the subprocess
**Throws:** SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

command

is

null

,
or one of the elements of

envp

is

null
**Throws:** IllegalArgumentException

- If

command

is empty
**Since:** 1.3
**See Also:** ProcessBuilder

---

#### exec

public

Process

exec​(

String

command,

String

[] envp,

File

dir)
throws

IOException

Executes the specified string command in a separate process with the
specified environment and working directory.

This is a convenience method. An invocation of the form

exec(command, envp, dir)

behaves in exactly the same way as the invocation

exec

(cmdarray, envp, dir)

,
where

cmdarray

is an array of all the tokens in

command

.

More precisely, the

command

string is broken
into tokens using a

StringTokenizer

created by the call

new {@link StringTokenizer}(command)

with no
further modification of the character categories. The tokens
produced by the tokenizer are then placed in the new string
array

cmdarray

, in the same order.

This is a convenience method. An invocation of the form

exec(command, envp, dir)

behaves in exactly the same way as the invocation

exec

(cmdarray, envp, dir)

,
where

cmdarray

is an array of all the tokens in

command

.

More precisely, the

command

string is broken
into tokens using a

StringTokenizer

created by the call

new {@link StringTokenizer}(command)

with no
further modification of the character categories. The tokens
produced by the tokenizer are then placed in the new string
array

cmdarray

, in the same order.

More precisely, the

command

string is broken
into tokens using a

StringTokenizer

created by the call

new {@link StringTokenizer}(command)

with no
further modification of the character categories. The tokens
produced by the tokenizer are then placed in the new string
array

cmdarray

, in the same order.

exec

```java
public
Process
exec​(
String
[] cmdarray)
throws
IOException
```

Executes the specified command and arguments in a separate process.

This is a convenience method. An invocation of the form

exec(cmdarray)

behaves in exactly the same way as the invocation

exec

(cmdarray, null, null)

.

**Parameters:** cmdarray

- array containing the command to call and
its arguments.
**Returns:** A new

Process

object for managing the subprocess
**Throws:** SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

cmdarray

is

null

,
or one of the elements of

cmdarray

is

null
**Throws:** IndexOutOfBoundsException

- If

cmdarray

is an empty array
(has length

0

)
**See Also:** ProcessBuilder

---

#### exec

public

Process

exec​(

String

[] cmdarray)
throws

IOException

Executes the specified command and arguments in a separate process.

This is a convenience method. An invocation of the form

exec(cmdarray)

behaves in exactly the same way as the invocation

exec

(cmdarray, null, null)

.

This is a convenience method. An invocation of the form

exec(cmdarray)

behaves in exactly the same way as the invocation

exec

(cmdarray, null, null)

.

exec

```java
public
Process
exec​(
String
[] cmdarray,

String
[] envp)
throws
IOException
```

Executes the specified command and arguments in a separate process
with the specified environment.

This is a convenience method. An invocation of the form

exec(cmdarray, envp)

behaves in exactly the same way as the invocation

exec

(cmdarray, envp, null)

.

**Parameters:** cmdarray

- array containing the command to call and
its arguments.
**Parameters:** envp

- array of strings, each element of which
has environment variable settings in the format

name

=

value

, or

null

if the subprocess should inherit
the environment of the current process.
**Returns:** A new

Process

object for managing the subprocess
**Throws:** SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

cmdarray

is

null

,
or one of the elements of

cmdarray

is

null

,
or one of the elements of

envp

is

null
**Throws:** IndexOutOfBoundsException

- If

cmdarray

is an empty array
(has length

0

)
**See Also:** ProcessBuilder

---

#### exec

public

Process

exec​(

String

[] cmdarray,

String

[] envp)
throws

IOException

Executes the specified command and arguments in a separate process
with the specified environment.

This is a convenience method. An invocation of the form

exec(cmdarray, envp)

behaves in exactly the same way as the invocation

exec

(cmdarray, envp, null)

.

This is a convenience method. An invocation of the form

exec(cmdarray, envp)

behaves in exactly the same way as the invocation

exec

(cmdarray, envp, null)

.

exec

```java
public
Process
exec​(
String
[] cmdarray,

String
[] envp,

File
dir)
throws
IOException
```

Executes the specified command and arguments in a separate process with
the specified environment and working directory.

Given an array of strings

cmdarray

, representing the
tokens of a command line, and an array of strings

envp

,
representing "environment" variable settings, this method creates
a new process in which to execute the specified command.

This method checks that

cmdarray

is a valid operating
system command. Which commands are valid is system-dependent,
but at the very least the command must be a non-empty list of
non-null strings.

If

envp

is

null

, the subprocess inherits the
environment settings of the current process.

A minimal set of system dependent environment variables may
be required to start a process on some operating systems.
As a result, the subprocess may inherit additional environment variable
settings beyond those in the specified environment.

ProcessBuilder.start()

is now the preferred way to
start a process with a modified environment.

The working directory of the new subprocess is specified by

dir

.
If

dir

is

null

, the subprocess inherits the
current working directory of the current process.

If a security manager exists, its

checkExec

method is invoked with the first component of the array

cmdarray

as its argument. This may result in a

SecurityException

being thrown.

Starting an operating system process is highly system-dependent.
Among the many things that can go wrong are:

- The operating system program file was not found.

Access to the program file was denied.

The working directory does not exist.

In such cases an exception will be thrown. The exact nature
of the exception is system-dependent, but it will always be a
subclass of

IOException

.

If the operating system does not support the creation of
processes, an

UnsupportedOperationException

will be thrown.

**Parameters:** cmdarray

- array containing the command to call and
its arguments.
**Parameters:** envp

- array of strings, each element of which
has environment variable settings in the format

name

=

value

, or

null

if the subprocess should inherit
the environment of the current process.
**Parameters:** dir

- the working directory of the subprocess, or

null

if the subprocess should inherit
the working directory of the current process.
**Returns:** A new

Process

object for managing the subprocess
**Throws:** SecurityException

- If a security manager exists and its

checkExec

method doesn't allow creation of the subprocess
**Throws:** UnsupportedOperationException

- If the operating system does not support the creation of processes.
**Throws:** IOException

- If an I/O error occurs
**Throws:** NullPointerException

- If

cmdarray

is

null

,
or one of the elements of

cmdarray

is

null

,
or one of the elements of

envp

is

null
**Throws:** IndexOutOfBoundsException

- If

cmdarray

is an empty array
(has length

0

)
**Since:** 1.3
**See Also:** ProcessBuilder

---

#### exec

public

Process

exec​(

String

[] cmdarray,

String

[] envp,

File

dir)
throws

IOException

Executes the specified command and arguments in a separate process with
the specified environment and working directory.

Given an array of strings

cmdarray

, representing the
tokens of a command line, and an array of strings

envp

,
representing "environment" variable settings, this method creates
a new process in which to execute the specified command.

This method checks that

cmdarray

is a valid operating
system command. Which commands are valid is system-dependent,
but at the very least the command must be a non-empty list of
non-null strings.

If

envp

is

null

, the subprocess inherits the
environment settings of the current process.

A minimal set of system dependent environment variables may
be required to start a process on some operating systems.
As a result, the subprocess may inherit additional environment variable
settings beyond those in the specified environment.

ProcessBuilder.start()

is now the preferred way to
start a process with a modified environment.

The working directory of the new subprocess is specified by

dir

.
If

dir

is

null

, the subprocess inherits the
current working directory of the current process.

If a security manager exists, its

checkExec

method is invoked with the first component of the array

cmdarray

as its argument. This may result in a

SecurityException

being thrown.

Starting an operating system process is highly system-dependent.
Among the many things that can go wrong are:

- The operating system program file was not found.

Access to the program file was denied.

The working directory does not exist.

In such cases an exception will be thrown. The exact nature
of the exception is system-dependent, but it will always be a
subclass of

IOException

.

If the operating system does not support the creation of
processes, an

UnsupportedOperationException

will be thrown.

Given an array of strings

cmdarray

, representing the
tokens of a command line, and an array of strings

envp

,
representing "environment" variable settings, this method creates
a new process in which to execute the specified command.

This method checks that

cmdarray

is a valid operating
system command. Which commands are valid is system-dependent,
but at the very least the command must be a non-empty list of
non-null strings.

If

envp

is

null

, the subprocess inherits the
environment settings of the current process.

A minimal set of system dependent environment variables may
be required to start a process on some operating systems.
As a result, the subprocess may inherit additional environment variable
settings beyond those in the specified environment.

ProcessBuilder.start()

is now the preferred way to
start a process with a modified environment.

The working directory of the new subprocess is specified by

dir

.
If

dir

is

null

, the subprocess inherits the
current working directory of the current process.

If a security manager exists, its

checkExec

method is invoked with the first component of the array

cmdarray

as its argument. This may result in a

SecurityException

being thrown.

Starting an operating system process is highly system-dependent.
Among the many things that can go wrong are:

- The operating system program file was not found.

Access to the program file was denied.

The working directory does not exist.

In such cases an exception will be thrown. The exact nature
of the exception is system-dependent, but it will always be a
subclass of

IOException

.

If the operating system does not support the creation of
processes, an

UnsupportedOperationException

will be thrown.

This method checks that

cmdarray

is a valid operating
system command. Which commands are valid is system-dependent,
but at the very least the command must be a non-empty list of
non-null strings.

If

envp

is

null

, the subprocess inherits the
environment settings of the current process.

A minimal set of system dependent environment variables may
be required to start a process on some operating systems.
As a result, the subprocess may inherit additional environment variable
settings beyond those in the specified environment.

ProcessBuilder.start()

is now the preferred way to
start a process with a modified environment.

The working directory of the new subprocess is specified by

dir

.
If

dir

is

null

, the subprocess inherits the
current working directory of the current process.

If a security manager exists, its

checkExec

method is invoked with the first component of the array

cmdarray

as its argument. This may result in a

SecurityException

being thrown.

Starting an operating system process is highly system-dependent.
Among the many things that can go wrong are:

- The operating system program file was not found.

Access to the program file was denied.

The working directory does not exist.

In such cases an exception will be thrown. The exact nature
of the exception is system-dependent, but it will always be a
subclass of

IOException

.

If the operating system does not support the creation of
processes, an

UnsupportedOperationException

will be thrown.

If

envp

is

null

, the subprocess inherits the
environment settings of the current process.

A minimal set of system dependent environment variables may
be required to start a process on some operating systems.
As a result, the subprocess may inherit additional environment variable
settings beyond those in the specified environment.

ProcessBuilder.start()

is now the preferred way to
start a process with a modified environment.

The working directory of the new subprocess is specified by

dir

.
If

dir

is

null

, the subprocess inherits the
current working directory of the current process.

If a security manager exists, its

checkExec

method is invoked with the first component of the array

cmdarray

as its argument. This may result in a

SecurityException

being thrown.

Starting an operating system process is highly system-dependent.
Among the many things that can go wrong are:

- The operating system program file was not found.

Access to the program file was denied.

The working directory does not exist.

In such cases an exception will be thrown. The exact nature
of the exception is system-dependent, but it will always be a
subclass of

IOException

.

If the operating system does not support the creation of
processes, an

UnsupportedOperationException

will be thrown.

A minimal set of system dependent environment variables may
be required to start a process on some operating systems.
As a result, the subprocess may inherit additional environment variable
settings beyond those in the specified environment.

ProcessBuilder.start()

is now the preferred way to
start a process with a modified environment.

The working directory of the new subprocess is specified by

dir

.
If

dir

is

null

, the subprocess inherits the
current working directory of the current process.

If a security manager exists, its

checkExec

method is invoked with the first component of the array

cmdarray

as its argument. This may result in a

SecurityException

being thrown.

Starting an operating system process is highly system-dependent.
Among the many things that can go wrong are:

- The operating system program file was not found.

Access to the program file was denied.

The working directory does not exist.

In such cases an exception will be thrown. The exact nature
of the exception is system-dependent, but it will always be a
subclass of

IOException

.

If the operating system does not support the creation of
processes, an

UnsupportedOperationException

will be thrown.

ProcessBuilder.start()

is now the preferred way to
start a process with a modified environment.

The working directory of the new subprocess is specified by

dir

.
If

dir

is

null

, the subprocess inherits the
current working directory of the current process.

If a security manager exists, its

checkExec

method is invoked with the first component of the array

cmdarray

as its argument. This may result in a

SecurityException

being thrown.

Starting an operating system process is highly system-dependent.
Among the many things that can go wrong are:

- The operating system program file was not found.

Access to the program file was denied.

The working directory does not exist.

In such cases an exception will be thrown. The exact nature
of the exception is system-dependent, but it will always be a
subclass of

IOException

.

If the operating system does not support the creation of
processes, an

UnsupportedOperationException

will be thrown.

The working directory of the new subprocess is specified by

dir

.
If

dir

is

null

, the subprocess inherits the
current working directory of the current process.

If a security manager exists, its

checkExec

method is invoked with the first component of the array

cmdarray

as its argument. This may result in a

SecurityException

being thrown.

Starting an operating system process is highly system-dependent.
Among the many things that can go wrong are:

- The operating system program file was not found.

Access to the program file was denied.

The working directory does not exist.

In such cases an exception will be thrown. The exact nature
of the exception is system-dependent, but it will always be a
subclass of

IOException

.

If the operating system does not support the creation of
processes, an

UnsupportedOperationException

will be thrown.

If a security manager exists, its

checkExec

method is invoked with the first component of the array

cmdarray

as its argument. This may result in a

SecurityException

being thrown.

Starting an operating system process is highly system-dependent.
Among the many things that can go wrong are:

- The operating system program file was not found.

Access to the program file was denied.

The working directory does not exist.

In such cases an exception will be thrown. The exact nature
of the exception is system-dependent, but it will always be a
subclass of

IOException

.

If the operating system does not support the creation of
processes, an

UnsupportedOperationException

will be thrown.

Starting an operating system process is highly system-dependent.
Among the many things that can go wrong are:

- The operating system program file was not found.

Access to the program file was denied.

The working directory does not exist.

In such cases an exception will be thrown. The exact nature
of the exception is system-dependent, but it will always be a
subclass of

IOException

.

If the operating system does not support the creation of
processes, an

UnsupportedOperationException

will be thrown.

The operating system program file was not found.

Access to the program file was denied.

The working directory does not exist.

In such cases an exception will be thrown. The exact nature
of the exception is system-dependent, but it will always be a
subclass of

IOException

.

If the operating system does not support the creation of
processes, an

UnsupportedOperationException

will be thrown.

If the operating system does not support the creation of
processes, an

UnsupportedOperationException

will be thrown.

availableProcessors

```java
public int availableProcessors()
```

Returns the number of processors available to the Java virtual machine.

This value may change during a particular invocation of the virtual
machine. Applications that are sensitive to the number of available
processors should therefore occasionally poll this property and adjust
their resource usage appropriately.

**Returns:** the maximum number of processors available to the virtual
machine; never smaller than one
**Since:** 1.4

---

#### availableProcessors

public int availableProcessors()

Returns the number of processors available to the Java virtual machine.

This value may change during a particular invocation of the virtual
machine. Applications that are sensitive to the number of available
processors should therefore occasionally poll this property and adjust
their resource usage appropriately.

This value may change during a particular invocation of the virtual
machine. Applications that are sensitive to the number of available
processors should therefore occasionally poll this property and adjust
their resource usage appropriately.

freeMemory

```java
public long freeMemory()
```

Returns the amount of free memory in the Java Virtual Machine.
Calling the

gc

method may result in increasing the value returned
by

freeMemory.

**Returns:** an approximation to the total amount of memory currently
available for future allocated objects, measured in bytes.

---

#### freeMemory

public long freeMemory()

Returns the amount of free memory in the Java Virtual Machine.
Calling the

gc

method may result in increasing the value returned
by

freeMemory.

totalMemory

```java
public long totalMemory()
```

Returns the total amount of memory in the Java virtual machine.
The value returned by this method may vary over time, depending on
the host environment.

Note that the amount of memory required to hold an object of any
given type may be implementation-dependent.

**Returns:** the total amount of memory currently available for current
and future objects, measured in bytes.

---

#### totalMemory

public long totalMemory()

Returns the total amount of memory in the Java virtual machine.
The value returned by this method may vary over time, depending on
the host environment.

Note that the amount of memory required to hold an object of any
given type may be implementation-dependent.

Note that the amount of memory required to hold an object of any
given type may be implementation-dependent.

maxMemory

```java
public long maxMemory()
```

Returns the maximum amount of memory that the Java virtual machine
will attempt to use. If there is no inherent limit then the value

Long.MAX_VALUE

will be returned.

**Returns:** the maximum amount of memory that the virtual machine will
attempt to use, measured in bytes
**Since:** 1.4

---

#### maxMemory

public long maxMemory()

Returns the maximum amount of memory that the Java virtual machine
will attempt to use. If there is no inherent limit then the value

Long.MAX_VALUE

will be returned.

gc

```java
public void gc()
```

Runs the garbage collector.
Calling this method suggests that the Java virtual machine expend
effort toward recycling unused objects in order to make the memory
they currently occupy available for quick reuse. When control
returns from the method call, the virtual machine has made
its best effort to recycle all discarded objects.

The name

gc

stands for "garbage
collector". The virtual machine performs this recycling
process automatically as needed, in a separate thread, even if the

gc

method is not invoked explicitly.

The method

System.gc()

is the conventional and convenient
means of invoking this method.

---

#### gc

public void gc()

Runs the garbage collector.
Calling this method suggests that the Java virtual machine expend
effort toward recycling unused objects in order to make the memory
they currently occupy available for quick reuse. When control
returns from the method call, the virtual machine has made
its best effort to recycle all discarded objects.

The name

gc

stands for "garbage
collector". The virtual machine performs this recycling
process automatically as needed, in a separate thread, even if the

gc

method is not invoked explicitly.

The method

System.gc()

is the conventional and convenient
means of invoking this method.

The name

gc

stands for "garbage
collector". The virtual machine performs this recycling
process automatically as needed, in a separate thread, even if the

gc

method is not invoked explicitly.

The method

System.gc()

is the conventional and convenient
means of invoking this method.

The method

System.gc()

is the conventional and convenient
means of invoking this method.

runFinalization

```java
public void runFinalization()
```

Runs the finalization methods of any objects pending finalization.
Calling this method suggests that the Java virtual machine expend
effort toward running the

finalize

methods of objects
that have been found to be discarded but whose

finalize

methods have not yet been run. When control returns from the
method call, the virtual machine has made a best effort to
complete all outstanding finalizations.

The virtual machine performs the finalization process
automatically as needed, in a separate thread, if the

runFinalization

method is not invoked explicitly.

The method

System.runFinalization()

is the conventional
and convenient means of invoking this method.

**See Also:** Object.finalize()

---

#### runFinalization

public void runFinalization()

Runs the finalization methods of any objects pending finalization.
Calling this method suggests that the Java virtual machine expend
effort toward running the

finalize

methods of objects
that have been found to be discarded but whose

finalize

methods have not yet been run. When control returns from the
method call, the virtual machine has made a best effort to
complete all outstanding finalizations.

The virtual machine performs the finalization process
automatically as needed, in a separate thread, if the

runFinalization

method is not invoked explicitly.

The method

System.runFinalization()

is the conventional
and convenient means of invoking this method.

The virtual machine performs the finalization process
automatically as needed, in a separate thread, if the

runFinalization

method is not invoked explicitly.

The method

System.runFinalization()

is the conventional
and convenient means of invoking this method.

The method

System.runFinalization()

is the conventional
and convenient means of invoking this method.

traceInstructions

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public void traceInstructions​(boolean on)
```

Deprecated, for removal: This API element is subject to removal in a future version.

This method was intended to control instruction tracing.
It has been superseded by JVM-specific tracing mechanisms.
This method is subject to removal in a future version of Java SE.

Not implemented, does nothing.

**Parameters:** on

- ignored

---

#### traceInstructions

@Deprecated

(

since

="9",

forRemoval

=true)
public void traceInstructions​(boolean on)

Not implemented, does nothing.

traceMethodCalls

```java
@Deprecated
(
since
="9",

forRemoval
=true)
public void traceMethodCalls​(boolean on)
```

Deprecated, for removal: This API element is subject to removal in a future version.

This method was intended to control method call tracing.
It has been superseded by JVM-specific tracing mechanisms.
This method is subject to removal in a future version of Java SE.

Not implemented, does nothing.

**Parameters:** on

- ignored

---

#### traceMethodCalls

@Deprecated

(

since

="9",

forRemoval

=true)
public void traceMethodCalls​(boolean on)

Not implemented, does nothing.

load

```java
public void load​(
String
filename)
```

Loads the native library specified by the filename argument. The filename
argument must be an absolute path name.
(for example

Runtime.getRuntime().load("/home/avh/lib/libX11.so");

).

If the filename argument, when stripped of any platform-specific library
prefix, path, and file extension, indicates a library whose name is,
for example, L, and a native library called L is statically linked
with the VM, then the JNI_OnLoad_L function exported by the library
is invoked rather than attempting to load a dynamic library.
A filename matching the argument does not have to exist in the file
system.
See the

JNI Specification

for more details.

Otherwise, the filename argument is mapped to a native library image in
an implementation-dependent manner.

First, if there is a security manager, its

checkLink

method is called with the

filename

as its argument.
This may result in a security exception.

This is similar to the method

loadLibrary(String)

, but it
accepts a general file name as an argument rather than just a library
name, allowing any file of native code to be loaded.

The method

System.load(String)

is the conventional and
convenient means of invoking this method.

**Parameters:** filename

- the file to load.
**Throws:** SecurityException

- if a security manager exists and its

checkLink

method doesn't allow
loading of the specified dynamic library
**Throws:** UnsatisfiedLinkError

- if either the filename is not an
absolute path name, the native library is not statically
linked with the VM, or the library cannot be mapped to
a native library image by the host system.
**Throws:** NullPointerException

- if

filename

is

null
**See Also:** getRuntime()

,

SecurityException

,

SecurityManager.checkLink(java.lang.String)

---

#### load

public void load​(

String

filename)

Loads the native library specified by the filename argument. The filename
argument must be an absolute path name.
(for example

Runtime.getRuntime().load("/home/avh/lib/libX11.so");

).

If the filename argument, when stripped of any platform-specific library
prefix, path, and file extension, indicates a library whose name is,
for example, L, and a native library called L is statically linked
with the VM, then the JNI_OnLoad_L function exported by the library
is invoked rather than attempting to load a dynamic library.
A filename matching the argument does not have to exist in the file
system.
See the

JNI Specification

for more details.

Otherwise, the filename argument is mapped to a native library image in
an implementation-dependent manner.

First, if there is a security manager, its

checkLink

method is called with the

filename

as its argument.
This may result in a security exception.

This is similar to the method

loadLibrary(String)

, but it
accepts a general file name as an argument rather than just a library
name, allowing any file of native code to be loaded.

The method

System.load(String)

is the conventional and
convenient means of invoking this method.

First, if there is a security manager, its

checkLink

method is called with the

filename

as its argument.
This may result in a security exception.

This is similar to the method

loadLibrary(String)

, but it
accepts a general file name as an argument rather than just a library
name, allowing any file of native code to be loaded.

The method

System.load(String)

is the conventional and
convenient means of invoking this method.

This is similar to the method

loadLibrary(String)

, but it
accepts a general file name as an argument rather than just a library
name, allowing any file of native code to be loaded.

The method

System.load(String)

is the conventional and
convenient means of invoking this method.

The method

System.load(String)

is the conventional and
convenient means of invoking this method.

loadLibrary

```java
public void loadLibrary​(
String
libname)
```

Loads the native library specified by the

libname

argument. The

libname

argument must not contain any platform
specific prefix, file extension or path. If a native library
called

libname

is statically linked with the VM, then the
JNI_OnLoad_

libname

function exported by the library is invoked.
See the

JNI Specification

for more details.

Otherwise, the libname argument is loaded from a system library
location and mapped to a native library image in an implementation-
dependent manner.

First, if there is a security manager, its

checkLink

method is called with the

libname

as its argument.
This may result in a security exception.

The method

System.loadLibrary(String)

is the conventional
and convenient means of invoking this method. If native
methods are to be used in the implementation of a class, a standard
strategy is to put the native code in a library file (call it

LibFile

) and then to put a static initializer:

```java
static { System.loadLibrary("LibFile"); }
```

within the class declaration. When the class is loaded and
initialized, the necessary native code implementation for the native
methods will then be loaded as well.

If this method is called more than once with the same library
name, the second and subsequent calls are ignored.

**Parameters:** libname

- the name of the library.
**Throws:** SecurityException

- if a security manager exists and its

checkLink

method doesn't allow
loading of the specified dynamic library
**Throws:** UnsatisfiedLinkError

- if either the libname argument
contains a file path, the native library is not statically
linked with the VM, or the library cannot be mapped to a
native library image by the host system.
**Throws:** NullPointerException

- if

libname

is

null
**See Also:** SecurityException

,

SecurityManager.checkLink(java.lang.String)

---

#### loadLibrary

public void loadLibrary​(

String

libname)

Loads the native library specified by the

libname

argument. The

libname

argument must not contain any platform
specific prefix, file extension or path. If a native library
called

libname

is statically linked with the VM, then the
JNI_OnLoad_

libname

function exported by the library is invoked.
See the

JNI Specification

for more details.

Otherwise, the libname argument is loaded from a system library
location and mapped to a native library image in an implementation-
dependent manner.

First, if there is a security manager, its

checkLink

method is called with the

libname

as its argument.
This may result in a security exception.

The method

System.loadLibrary(String)

is the conventional
and convenient means of invoking this method. If native
methods are to be used in the implementation of a class, a standard
strategy is to put the native code in a library file (call it

LibFile

) and then to put a static initializer:

```java
static { System.loadLibrary("LibFile"); }
```

within the class declaration. When the class is loaded and
initialized, the necessary native code implementation for the native
methods will then be loaded as well.

If this method is called more than once with the same library
name, the second and subsequent calls are ignored.

First, if there is a security manager, its

checkLink

method is called with the

libname

as its argument.
This may result in a security exception.

The method

System.loadLibrary(String)

is the conventional
and convenient means of invoking this method. If native
methods are to be used in the implementation of a class, a standard
strategy is to put the native code in a library file (call it

LibFile

) and then to put a static initializer:

```java
static { System.loadLibrary("LibFile"); }
```

within the class declaration. When the class is loaded and
initialized, the necessary native code implementation for the native
methods will then be loaded as well.

If this method is called more than once with the same library
name, the second and subsequent calls are ignored.

The method

System.loadLibrary(String)

is the conventional
and convenient means of invoking this method. If native
methods are to be used in the implementation of a class, a standard
strategy is to put the native code in a library file (call it

LibFile

) and then to put a static initializer:

```java
static { System.loadLibrary("LibFile"); }
```

within the class declaration. When the class is loaded and
initialized, the necessary native code implementation for the native
methods will then be loaded as well.

If this method is called more than once with the same library
name, the second and subsequent calls are ignored.

static { System.loadLibrary("LibFile"); }

If this method is called more than once with the same library
name, the second and subsequent calls are ignored.

version

```java
public static
Runtime.Version
version()
```

Returns the version of the Java Runtime Environment as a

Runtime.Version

.

**Returns:** the

Runtime.Version

of the Java Runtime Environment
**Since:** 9

---

#### version

public static

Runtime.Version

version()

Returns the version of the Java Runtime Environment as a

Runtime.Version

.

---

