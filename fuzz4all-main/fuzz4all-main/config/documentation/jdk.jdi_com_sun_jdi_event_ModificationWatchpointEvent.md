# Interface ModificationWatchpointEvent

**Source:** `jdk.jdi\com\sun\jdi\event\ModificationWatchpointEvent.html`

### Class Description

```java
public interface
ModificationWatchpointEvent

extends
WatchpointEvent
```

Notification of a field modification in the
target VM.

**All Superinterfaces:** Event

,

Locatable

,

LocatableEvent

,

Mirror

,

WatchpointEvent

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Value
valueToBe()

Value that will be assigned to the field when the instruction
completes.

---

### Additional Sections

#### Interface ModificationWatchpointEvent

**All Superinterfaces:** Event

,

Locatable

,

LocatableEvent

,

Mirror

,

WatchpointEvent

```java
public interface
ModificationWatchpointEvent

extends
WatchpointEvent
```

Notification of a field modification in the
target VM.

**Since:** 1.3
**See Also:** EventQueue

,

VirtualMachine

,

ModificationWatchpointRequest

public interface

ModificationWatchpointEvent

extends

WatchpointEvent

Notification of a field modification in the
target VM.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Value

valueToBe

()

Value that will be assigned to the field when the instruction
completes.

- Methods declared in interface com.sun.jdi.event.

Event

request

- Methods declared in interface com.sun.jdi.

Locatable

location

- Methods declared in interface com.sun.jdi.event.

LocatableEvent

thread

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

- Methods declared in interface com.sun.jdi.event.

WatchpointEvent

field

,

object

,

valueCurrent

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Value

valueToBe

()

Value that will be assigned to the field when the instruction
completes.

- Methods declared in interface com.sun.jdi.event.

Event

request

- Methods declared in interface com.sun.jdi.

Locatable

location

- Methods declared in interface com.sun.jdi.event.

LocatableEvent

thread

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

- Methods declared in interface com.sun.jdi.event.

WatchpointEvent

field

,

object

,

valueCurrent

---

#### Method Summary

Value that will be assigned to the field when the instruction
completes.

Methods declared in interface com.sun.jdi.event.

Event

request

---

#### Methods declared in interface com.sun.jdi.event. Event

Methods declared in interface com.sun.jdi.

Locatable

location

---

#### Methods declared in interface com.sun.jdi. Locatable

Methods declared in interface com.sun.jdi.event.

LocatableEvent

thread

---

#### Methods declared in interface com.sun.jdi.event. LocatableEvent

Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Methods declared in interface com.sun.jdi. Mirror

Methods declared in interface com.sun.jdi.event.

WatchpointEvent

field

,

object

,

valueCurrent

---

#### Methods declared in interface com.sun.jdi.event. WatchpointEvent

============ METHOD DETAIL ==========

- Method Detail

- valueToBe

```java
Value
valueToBe()
```

Value that will be assigned to the field when the instruction
completes.

Method Detail

- valueToBe

```java
Value
valueToBe()
```

Value that will be assigned to the field when the instruction
completes.

---

#### Method Detail

valueToBe

```java
Value
valueToBe()
```

Value that will be assigned to the field when the instruction
completes.

---

#### valueToBe

Value

valueToBe()

Value that will be assigned to the field when the instruction
completes.

---

