# Interface ThreadGroupReference

**Source:** `jdk.jdi\com\sun\jdi\ThreadGroupReference.html`

### Class Description

```java
public interface
ThreadGroupReference

extends
ObjectReference
```

A thread group object from the target VM.
A ThreadGroupReference is an

ObjectReference

with additional
access to threadgroup-specific information from the target VM.

**All Superinterfaces:** Mirror

,

ObjectReference

,

Value

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
name()

Returns the name of this thread group.

**Returns:**
- the string containing the thread group name.

---

#### ThreadGroupReference
parent()

Returns the parent of this thread group.

**Returns:**
- a

ThreadGroupReference

mirroring the parent of this
thread group in the target VM, or null if this is a top-level
thread group.

---

#### void suspend()

Suspends all threads in this thread group. Each thread
in this group and in all of its subgroups will be
suspended as described in

ThreadReference.suspend()

.
This is not guaranteed to be an atomic
operation; if the target VM is not interrupted at the time
this method is
called, it is possible that new threads will be created
between the time that threads are enumerated and all of them
have been suspended.

**Throws:**
- VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

---

#### void resume()

Resumes all threads in this thread group. Each thread
in this group and in all of its subgroups will be
resumed as described in

ThreadReference.resume()

.

**Throws:**
- VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

---

#### List
<
ThreadReference
> threads()

Returns a List containing a

ThreadReference

for each live thread
in this thread group. Only the live threads in this immediate thread group
(and not its subgroups) are returned. A thread is alive if it
has been started and has not yet been stopped.

**Returns:**
- a List of

ThreadReference

objects mirroring the
live threads from this thread group in the target VM.

---

#### List
<
ThreadGroupReference
> threadGroups()

Returns a List containing each active

ThreadGroupReference

in this
thread group. Only the active thread groups in this immediate thread group
(and not its subgroups) are returned.
See

ThreadGroup

for information about 'active' ThreadGroups.

**Returns:**
- a List of

ThreadGroupReference

objects mirroring the
active thread groups from this thread group in the target VM.

---

### Additional Sections

#### Interface ThreadGroupReference

**All Superinterfaces:** Mirror

,

ObjectReference

,

Value

```java
public interface
ThreadGroupReference

extends
ObjectReference
```

A thread group object from the target VM.
A ThreadGroupReference is an

ObjectReference

with additional
access to threadgroup-specific information from the target VM.

**Since:** 1.3

public interface

ThreadGroupReference

extends

ObjectReference

A thread group object from the target VM.
A ThreadGroupReference is an

ObjectReference

with additional
access to threadgroup-specific information from the target VM.

=========== FIELD SUMMARY ===========

- Field Summary

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

String

name

()

Returns the name of this thread group.

ThreadGroupReference

parent

()

Returns the parent of this thread group.

void

resume

()

Resumes all threads in this thread group.

void

suspend

()

Suspends all threads in this thread group.

List

<

ThreadGroupReference

>

threadGroups

()

Returns a List containing each active

ThreadGroupReference

in this
thread group.

List

<

ThreadReference

>

threads

()

Returns a List containing a

ThreadReference

for each live thread
in this thread group.

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

- Fields declared in interface com.sun.jdi.

ObjectReference

INVOKE_NONVIRTUAL

,

INVOKE_SINGLE_THREADED

---

#### Field Summary

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

String

name

()

Returns the name of this thread group.

ThreadGroupReference

parent

()

Returns the parent of this thread group.

void

resume

()

Resumes all threads in this thread group.

void

suspend

()

Suspends all threads in this thread group.

List

<

ThreadGroupReference

>

threadGroups

()

Returns a List containing each active

ThreadGroupReference

in this
thread group.

List

<

ThreadReference

>

threads

()

Returns a List containing a

ThreadReference

for each live thread
in this thread group.

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

Returns the name of this thread group.

Returns the parent of this thread group.

Resumes all threads in this thread group.

Suspends all threads in this thread group.

Returns a List containing each active

ThreadGroupReference

in this
thread group.

Returns a List containing a

ThreadReference

for each live thread
in this thread group.

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

============ METHOD DETAIL ==========

- Method Detail

- name

```java
String
name()
```

Returns the name of this thread group.

**Returns:** the string containing the thread group name.

- parent

```java
ThreadGroupReference
parent()
```

Returns the parent of this thread group.

**Returns:** a

ThreadGroupReference

mirroring the parent of this
thread group in the target VM, or null if this is a top-level
thread group.

- suspend

```java
void suspend()
```

Suspends all threads in this thread group. Each thread
in this group and in all of its subgroups will be
suspended as described in

ThreadReference.suspend()

.
This is not guaranteed to be an atomic
operation; if the target VM is not interrupted at the time
this method is
called, it is possible that new threads will be created
between the time that threads are enumerated and all of them
have been suspended.

**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

- resume

```java
void resume()
```

Resumes all threads in this thread group. Each thread
in this group and in all of its subgroups will be
resumed as described in

ThreadReference.resume()

.

**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

- threads

```java
List
<
ThreadReference
> threads()
```

Returns a List containing a

ThreadReference

for each live thread
in this thread group. Only the live threads in this immediate thread group
(and not its subgroups) are returned. A thread is alive if it
has been started and has not yet been stopped.

**Returns:** a List of

ThreadReference

objects mirroring the
live threads from this thread group in the target VM.

- threadGroups

```java
List
<
ThreadGroupReference
> threadGroups()
```

Returns a List containing each active

ThreadGroupReference

in this
thread group. Only the active thread groups in this immediate thread group
(and not its subgroups) are returned.
See

ThreadGroup

for information about 'active' ThreadGroups.

**Returns:** a List of

ThreadGroupReference

objects mirroring the
active thread groups from this thread group in the target VM.

Method Detail

- name

```java
String
name()
```

Returns the name of this thread group.

**Returns:** the string containing the thread group name.

- parent

```java
ThreadGroupReference
parent()
```

Returns the parent of this thread group.

**Returns:** a

ThreadGroupReference

mirroring the parent of this
thread group in the target VM, or null if this is a top-level
thread group.

- suspend

```java
void suspend()
```

Suspends all threads in this thread group. Each thread
in this group and in all of its subgroups will be
suspended as described in

ThreadReference.suspend()

.
This is not guaranteed to be an atomic
operation; if the target VM is not interrupted at the time
this method is
called, it is possible that new threads will be created
between the time that threads are enumerated and all of them
have been suspended.

**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

- resume

```java
void resume()
```

Resumes all threads in this thread group. Each thread
in this group and in all of its subgroups will be
resumed as described in

ThreadReference.resume()

.

**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

- threads

```java
List
<
ThreadReference
> threads()
```

Returns a List containing a

ThreadReference

for each live thread
in this thread group. Only the live threads in this immediate thread group
(and not its subgroups) are returned. A thread is alive if it
has been started and has not yet been stopped.

**Returns:** a List of

ThreadReference

objects mirroring the
live threads from this thread group in the target VM.

- threadGroups

```java
List
<
ThreadGroupReference
> threadGroups()
```

Returns a List containing each active

ThreadGroupReference

in this
thread group. Only the active thread groups in this immediate thread group
(and not its subgroups) are returned.
See

ThreadGroup

for information about 'active' ThreadGroups.

**Returns:** a List of

ThreadGroupReference

objects mirroring the
active thread groups from this thread group in the target VM.

---

#### Method Detail

name

```java
String
name()
```

Returns the name of this thread group.

**Returns:** the string containing the thread group name.

---

#### name

String

name()

Returns the name of this thread group.

parent

```java
ThreadGroupReference
parent()
```

Returns the parent of this thread group.

**Returns:** a

ThreadGroupReference

mirroring the parent of this
thread group in the target VM, or null if this is a top-level
thread group.

---

#### parent

ThreadGroupReference

parent()

Returns the parent of this thread group.

suspend

```java
void suspend()
```

Suspends all threads in this thread group. Each thread
in this group and in all of its subgroups will be
suspended as described in

ThreadReference.suspend()

.
This is not guaranteed to be an atomic
operation; if the target VM is not interrupted at the time
this method is
called, it is possible that new threads will be created
between the time that threads are enumerated and all of them
have been suspended.

**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

---

#### suspend

void suspend()

Suspends all threads in this thread group. Each thread
in this group and in all of its subgroups will be
suspended as described in

ThreadReference.suspend()

.
This is not guaranteed to be an atomic
operation; if the target VM is not interrupted at the time
this method is
called, it is possible that new threads will be created
between the time that threads are enumerated and all of them
have been suspended.

resume

```java
void resume()
```

Resumes all threads in this thread group. Each thread
in this group and in all of its subgroups will be
resumed as described in

ThreadReference.resume()

.

**Throws:** VMCannotBeModifiedException

- if the VirtualMachine is read-only - see

VirtualMachine.canBeModified()

.

---

#### resume

void resume()

Resumes all threads in this thread group. Each thread
in this group and in all of its subgroups will be
resumed as described in

ThreadReference.resume()

.

threads

```java
List
<
ThreadReference
> threads()
```

Returns a List containing a

ThreadReference

for each live thread
in this thread group. Only the live threads in this immediate thread group
(and not its subgroups) are returned. A thread is alive if it
has been started and has not yet been stopped.

**Returns:** a List of

ThreadReference

objects mirroring the
live threads from this thread group in the target VM.

---

#### threads

List

<

ThreadReference

> threads()

Returns a List containing a

ThreadReference

for each live thread
in this thread group. Only the live threads in this immediate thread group
(and not its subgroups) are returned. A thread is alive if it
has been started and has not yet been stopped.

threadGroups

```java
List
<
ThreadGroupReference
> threadGroups()
```

Returns a List containing each active

ThreadGroupReference

in this
thread group. Only the active thread groups in this immediate thread group
(and not its subgroups) are returned.
See

ThreadGroup

for information about 'active' ThreadGroups.

**Returns:** a List of

ThreadGroupReference

objects mirroring the
active thread groups from this thread group in the target VM.

---

#### threadGroups

List

<

ThreadGroupReference

> threadGroups()

Returns a List containing each active

ThreadGroupReference

in this
thread group. Only the active thread groups in this immediate thread group
(and not its subgroups) are returned.
See

ThreadGroup

for information about 'active' ThreadGroups.

---

