# Interface Locatable

**Source:** `jdk.jdi\com\sun\jdi\Locatable.html`

### Class Description

```java
public interface
Locatable
```

A mirror that has a

Location

.

**All Known Subinterfaces:** AccessWatchpointEvent

,

BreakpointEvent

,

BreakpointRequest

,

ExceptionEvent

,

LocatableEvent

,

Method

,

MethodEntryEvent

,

MethodExitEvent

,

ModificationWatchpointEvent

,

MonitorContendedEnteredEvent

,

MonitorContendedEnterEvent

,

MonitorWaitedEvent

,

MonitorWaitEvent

,

StackFrame

,

StepEvent

,

WatchpointEvent

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Location
location()

Returns the

Location

of this mirror, if there is
executable code associated with it. Note that both Java™
programming language methods and native methods have executable
code.
Returns null for abstract methods, since abstract methods
have no executable code.

**Returns:**
- the

Location

of this mirror, or null if
there is no executable code associated with it.

---

### Additional Sections

#### Interface Locatable

**All Known Subinterfaces:** AccessWatchpointEvent

,

BreakpointEvent

,

BreakpointRequest

,

ExceptionEvent

,

LocatableEvent

,

Method

,

MethodEntryEvent

,

MethodExitEvent

,

ModificationWatchpointEvent

,

MonitorContendedEnteredEvent

,

MonitorContendedEnterEvent

,

MonitorWaitedEvent

,

MonitorWaitEvent

,

StackFrame

,

StepEvent

,

WatchpointEvent

```java
public interface
Locatable
```

A mirror that has a

Location

.

**Since:** 1.3

public interface

Locatable

A mirror that has a

Location

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Location

location

()

Returns the

Location

of this mirror, if there is
executable code associated with it.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Location

location

()

Returns the

Location

of this mirror, if there is
executable code associated with it.

---

#### Method Summary

Returns the

Location

of this mirror, if there is
executable code associated with it.

============ METHOD DETAIL ==========

- Method Detail

- location

```java
Location
location()
```

Returns the

Location

of this mirror, if there is
executable code associated with it. Note that both Java™
programming language methods and native methods have executable
code.
Returns null for abstract methods, since abstract methods
have no executable code.

**Returns:** the

Location

of this mirror, or null if
there is no executable code associated with it.

Method Detail

- location

```java
Location
location()
```

Returns the

Location

of this mirror, if there is
executable code associated with it. Note that both Java™
programming language methods and native methods have executable
code.
Returns null for abstract methods, since abstract methods
have no executable code.

**Returns:** the

Location

of this mirror, or null if
there is no executable code associated with it.

---

#### Method Detail

location

```java
Location
location()
```

Returns the

Location

of this mirror, if there is
executable code associated with it. Note that both Java™
programming language methods and native methods have executable
code.
Returns null for abstract methods, since abstract methods
have no executable code.

**Returns:** the

Location

of this mirror, or null if
there is no executable code associated with it.

---

#### location

Location

location()

Returns the

Location

of this mirror, if there is
executable code associated with it. Note that both Java™
programming language methods and native methods have executable
code.
Returns null for abstract methods, since abstract methods
have no executable code.

---

