# Interface WatchpointEvent

**Source:** `jdk.jdi\com\sun\jdi\event\WatchpointEvent.html`

### Class Description

```java
public interface
WatchpointEvent

extends
LocatableEvent
```

Notification of a field triggered event encountered by a thread in the
target VM.

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

#### Field
field()

Returns the field that is about to be accessed/modified.

**Returns:**
- a

Field

which mirrors the field
in the target VM.

**Throws:**
- ObjectCollectedException

- may be thrown if class
has been garbage collected.

---

#### ObjectReference
object()

Returns the object whose field is about to be accessed/modified.
Return null is the access is to a static field.

**Returns:**
- a

ObjectReference

which mirrors the event's
object in the target VM.

---

#### Value
valueCurrent()

Current value of the field.

**Throws:**
- ObjectCollectedException

- if object or class have been
garbage collected.

---

### Additional Sections

#### Interface WatchpointEvent

**All Superinterfaces:** Event

,

Locatable

,

LocatableEvent

,

Mirror

**All Known Subinterfaces:** AccessWatchpointEvent

,

ModificationWatchpointEvent

```java
public interface
WatchpointEvent

extends
LocatableEvent
```

Notification of a field triggered event encountered by a thread in the
target VM.

**Since:** 1.3
**See Also:** EventQueue

,

VirtualMachine

public interface

WatchpointEvent

extends

LocatableEvent

Notification of a field triggered event encountered by a thread in the
target VM.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Field

field

()

Returns the field that is about to be accessed/modified.

ObjectReference

object

()

Returns the object whose field is about to be accessed/modified.

Value

valueCurrent

()

Current value of the field.

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

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Field

field

()

Returns the field that is about to be accessed/modified.

ObjectReference

object

()

Returns the object whose field is about to be accessed/modified.

Value

valueCurrent

()

Current value of the field.

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

Returns the field that is about to be accessed/modified.

Returns the object whose field is about to be accessed/modified.

Current value of the field.

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

============ METHOD DETAIL ==========

- Method Detail

- field

```java
Field
field()
```

Returns the field that is about to be accessed/modified.

**Returns:** a

Field

which mirrors the field
in the target VM.
**Throws:** ObjectCollectedException

- may be thrown if class
has been garbage collected.

- object

```java
ObjectReference
object()
```

Returns the object whose field is about to be accessed/modified.
Return null is the access is to a static field.

**Returns:** a

ObjectReference

which mirrors the event's
object in the target VM.

- valueCurrent

```java
Value
valueCurrent()
```

Current value of the field.

**Throws:** ObjectCollectedException

- if object or class have been
garbage collected.

Method Detail

- field

```java
Field
field()
```

Returns the field that is about to be accessed/modified.

**Returns:** a

Field

which mirrors the field
in the target VM.
**Throws:** ObjectCollectedException

- may be thrown if class
has been garbage collected.

- object

```java
ObjectReference
object()
```

Returns the object whose field is about to be accessed/modified.
Return null is the access is to a static field.

**Returns:** a

ObjectReference

which mirrors the event's
object in the target VM.

- valueCurrent

```java
Value
valueCurrent()
```

Current value of the field.

**Throws:** ObjectCollectedException

- if object or class have been
garbage collected.

---

#### Method Detail

field

```java
Field
field()
```

Returns the field that is about to be accessed/modified.

**Returns:** a

Field

which mirrors the field
in the target VM.
**Throws:** ObjectCollectedException

- may be thrown if class
has been garbage collected.

---

#### field

Field

field()

Returns the field that is about to be accessed/modified.

object

```java
ObjectReference
object()
```

Returns the object whose field is about to be accessed/modified.
Return null is the access is to a static field.

**Returns:** a

ObjectReference

which mirrors the event's
object in the target VM.

---

#### object

ObjectReference

object()

Returns the object whose field is about to be accessed/modified.
Return null is the access is to a static field.

valueCurrent

```java
Value
valueCurrent()
```

Current value of the field.

**Throws:** ObjectCollectedException

- if object or class have been
garbage collected.

---

#### valueCurrent

Value

valueCurrent()

Current value of the field.

---

