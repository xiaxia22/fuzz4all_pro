# Interface StepEvent

**Source:** `jdk.jdi\com\sun\jdi\event\StepEvent.html`

### Class Description

```java
public interface
StepEvent

extends
LocatableEvent
```

Notification of step completion in the target VM.
The step event is generated immediately before the code at its location
is executed. Thus, if the step is entering a new method (as might occur
with

StepRequest.STEP_INTO

)
the location of the event is the first instruction of the method.
When a step leaves a method, the location of the event will be the
first instruction after the call in the calling method; note that
this location may not be at a line boundary, even if

StepRequest.STEP_LINE

was used.

**All Superinterfaces:** Event

,

Locatable

,

LocatableEvent

,

Mirror

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Interface StepEvent

**All Superinterfaces:** Event

,

Locatable

,

LocatableEvent

,

Mirror

```java
public interface
StepEvent

extends
LocatableEvent
```

Notification of step completion in the target VM.
The step event is generated immediately before the code at its location
is executed. Thus, if the step is entering a new method (as might occur
with

StepRequest.STEP_INTO

)
the location of the event is the first instruction of the method.
When a step leaves a method, the location of the event will be the
first instruction after the call in the calling method; note that
this location may not be at a line boundary, even if

StepRequest.STEP_LINE

was used.

**Since:** 1.3
**See Also:** StepRequest

,

EventQueue

public interface

StepEvent

extends

LocatableEvent

Notification of step completion in the target VM.
The step event is generated immediately before the code at its location
is executed. Thus, if the step is entering a new method (as might occur
with

StepRequest.STEP_INTO

)
the location of the event is the first instruction of the method.
When a step leaves a method, the location of the event will be the
first instruction after the call in the calling method; note that
this location may not be at a line boundary, even if

StepRequest.STEP_LINE

was used.

========== METHOD SUMMARY ===========

- Method Summary

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

Method Summary

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

---

#### Method Summary

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

