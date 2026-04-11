# Interface MonitorInfo

**Source:** `jdk.jdi\com\sun\jdi\MonitorInfo.html`

### Class Description

```java
public interface
MonitorInfo

extends
Mirror
```

Information about a monitor owned by a thread.

**All Superinterfaces:** Mirror

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ObjectReference
monitor()

Returns the

ObjectReference

object for the monitor.

**Returns:**
- the

ObjectReference

object for the monitor.

**Throws:**
- InvalidStackFrameException

- if the associated stack
frame has become invalid. Once the frame's thread is resumed,
the stack frame is no longer valid.

**See Also:**
- ThreadReference.ownedMonitorsAndFrames()

**Since:**
- 1.6

---

#### int stackDepth()

Returns the stack depth at which this monitor was
acquired by the owning thread. Returns -1 if the
implementation cannot determine the stack depth
(e.g., for monitors acquired by JNI MonitorEnter).

**Returns:**
- the stack depth at which this monitor was
acquired by the owning thread.

**Throws:**
- InvalidStackFrameException

- if the associated stack
frame has become invalid. Once the frame's thread is resumed,
the stack frame is no longer valid.

**See Also:**
- ThreadReference.ownedMonitorsAndFrames()

---

#### ThreadReference
thread()

Returns a

ThreadReference

object for the thread that
owns the monitor.

**Returns:**
- a

ThreadReference

object for the thread that
owns the monitor.

**Throws:**
- InvalidStackFrameException

- if the associated stack
frame has become invalid. Once the frame's thread is resumed,
the stack frame is no longer valid.

**See Also:**
- ThreadReference.frame(int)

---

### Additional Sections

#### Interface MonitorInfo

**All Superinterfaces:** Mirror

```java
public interface
MonitorInfo

extends
Mirror
```

Information about a monitor owned by a thread.

**Since:** 1.6

public interface

MonitorInfo

extends

Mirror

Information about a monitor owned by a thread.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ObjectReference

monitor

()

Returns the

ObjectReference

object for the monitor.

int

stackDepth

()

Returns the stack depth at which this monitor was
acquired by the owning thread.

ThreadReference

thread

()

Returns a

ThreadReference

object for the thread that
owns the monitor.

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

ObjectReference

monitor

()

Returns the

ObjectReference

object for the monitor.

int

stackDepth

()

Returns the stack depth at which this monitor was
acquired by the owning thread.

ThreadReference

thread

()

Returns a

ThreadReference

object for the thread that
owns the monitor.

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Method Summary

Returns the

ObjectReference

object for the monitor.

Returns the stack depth at which this monitor was
acquired by the owning thread.

Returns a

ThreadReference

object for the thread that
owns the monitor.

Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Methods declared in interface com.sun.jdi. Mirror

============ METHOD DETAIL ==========

- Method Detail

- monitor

```java
ObjectReference
monitor()
```

Returns the

ObjectReference

object for the monitor.

**Returns:** the

ObjectReference

object for the monitor.
**Throws:** InvalidStackFrameException

- if the associated stack
frame has become invalid. Once the frame's thread is resumed,
the stack frame is no longer valid.
**Since:** 1.6
**See Also:** ThreadReference.ownedMonitorsAndFrames()

- stackDepth

```java
int stackDepth()
```

Returns the stack depth at which this monitor was
acquired by the owning thread. Returns -1 if the
implementation cannot determine the stack depth
(e.g., for monitors acquired by JNI MonitorEnter).

**Returns:** the stack depth at which this monitor was
acquired by the owning thread.
**Throws:** InvalidStackFrameException

- if the associated stack
frame has become invalid. Once the frame's thread is resumed,
the stack frame is no longer valid.
**See Also:** ThreadReference.ownedMonitorsAndFrames()

- thread

```java
ThreadReference
thread()
```

Returns a

ThreadReference

object for the thread that
owns the monitor.

**Returns:** a

ThreadReference

object for the thread that
owns the monitor.
**Throws:** InvalidStackFrameException

- if the associated stack
frame has become invalid. Once the frame's thread is resumed,
the stack frame is no longer valid.
**See Also:** ThreadReference.frame(int)

Method Detail

- monitor

```java
ObjectReference
monitor()
```

Returns the

ObjectReference

object for the monitor.

**Returns:** the

ObjectReference

object for the monitor.
**Throws:** InvalidStackFrameException

- if the associated stack
frame has become invalid. Once the frame's thread is resumed,
the stack frame is no longer valid.
**Since:** 1.6
**See Also:** ThreadReference.ownedMonitorsAndFrames()

- stackDepth

```java
int stackDepth()
```

Returns the stack depth at which this monitor was
acquired by the owning thread. Returns -1 if the
implementation cannot determine the stack depth
(e.g., for monitors acquired by JNI MonitorEnter).

**Returns:** the stack depth at which this monitor was
acquired by the owning thread.
**Throws:** InvalidStackFrameException

- if the associated stack
frame has become invalid. Once the frame's thread is resumed,
the stack frame is no longer valid.
**See Also:** ThreadReference.ownedMonitorsAndFrames()

- thread

```java
ThreadReference
thread()
```

Returns a

ThreadReference

object for the thread that
owns the monitor.

**Returns:** a

ThreadReference

object for the thread that
owns the monitor.
**Throws:** InvalidStackFrameException

- if the associated stack
frame has become invalid. Once the frame's thread is resumed,
the stack frame is no longer valid.
**See Also:** ThreadReference.frame(int)

---

#### Method Detail

monitor

```java
ObjectReference
monitor()
```

Returns the

ObjectReference

object for the monitor.

**Returns:** the

ObjectReference

object for the monitor.
**Throws:** InvalidStackFrameException

- if the associated stack
frame has become invalid. Once the frame's thread is resumed,
the stack frame is no longer valid.
**Since:** 1.6
**See Also:** ThreadReference.ownedMonitorsAndFrames()

---

#### monitor

ObjectReference

monitor()

Returns the

ObjectReference

object for the monitor.

stackDepth

```java
int stackDepth()
```

Returns the stack depth at which this monitor was
acquired by the owning thread. Returns -1 if the
implementation cannot determine the stack depth
(e.g., for monitors acquired by JNI MonitorEnter).

**Returns:** the stack depth at which this monitor was
acquired by the owning thread.
**Throws:** InvalidStackFrameException

- if the associated stack
frame has become invalid. Once the frame's thread is resumed,
the stack frame is no longer valid.
**See Also:** ThreadReference.ownedMonitorsAndFrames()

---

#### stackDepth

int stackDepth()

Returns the stack depth at which this monitor was
acquired by the owning thread. Returns -1 if the
implementation cannot determine the stack depth
(e.g., for monitors acquired by JNI MonitorEnter).

thread

```java
ThreadReference
thread()
```

Returns a

ThreadReference

object for the thread that
owns the monitor.

**Returns:** a

ThreadReference

object for the thread that
owns the monitor.
**Throws:** InvalidStackFrameException

- if the associated stack
frame has become invalid. Once the frame's thread is resumed,
the stack frame is no longer valid.
**See Also:** ThreadReference.frame(int)

---

#### thread

ThreadReference

thread()

Returns a

ThreadReference

object for the thread that
owns the monitor.

---

