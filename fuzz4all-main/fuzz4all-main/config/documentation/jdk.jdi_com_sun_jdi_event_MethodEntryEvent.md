# Interface MethodEntryEvent

**Source:** `jdk.jdi\com\sun\jdi\event\MethodEntryEvent.html`

### Class Description

```java
public interface
MethodEntryEvent

extends
LocatableEvent
```

Notification of a method invocation in the target VM. This event
occurs after entry into the invoked method and before any
code has executed.
Method entry events are generated for both native and non-native
methods.

In some VMs method entry events can occur for a particular thread
before its

ThreadStartEvent

occurs if methods are called
as part of the thread's initialization.

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

#### Method
method()

Returns the method that was entered.

**Returns:**
- a

Method

which mirrors the method that was entered.

---

### Additional Sections

#### Interface MethodEntryEvent

**All Superinterfaces:** Event

,

Locatable

,

LocatableEvent

,

Mirror

```java
public interface
MethodEntryEvent

extends
LocatableEvent
```

Notification of a method invocation in the target VM. This event
occurs after entry into the invoked method and before any
code has executed.
Method entry events are generated for both native and non-native
methods.

In some VMs method entry events can occur for a particular thread
before its

ThreadStartEvent

occurs if methods are called
as part of the thread's initialization.

**Since:** 1.3
**See Also:** EventQueue

public interface

MethodEntryEvent

extends

LocatableEvent

Notification of a method invocation in the target VM. This event
occurs after entry into the invoked method and before any
code has executed.
Method entry events are generated for both native and non-native
methods.

In some VMs method entry events can occur for a particular thread
before its

ThreadStartEvent

occurs if methods are called
as part of the thread's initialization.

In some VMs method entry events can occur for a particular thread
before its

ThreadStartEvent

occurs if methods are called
as part of the thread's initialization.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Method

method

()

Returns the method that was entered.

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

Method

method

()

Returns the method that was entered.

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

Returns the method that was entered.

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

- method

```java
Method
method()
```

Returns the method that was entered.

**Returns:** a

Method

which mirrors the method that was entered.

Method Detail

- method

```java
Method
method()
```

Returns the method that was entered.

**Returns:** a

Method

which mirrors the method that was entered.

---

#### Method Detail

method

```java
Method
method()
```

Returns the method that was entered.

**Returns:** a

Method

which mirrors the method that was entered.

---

#### method

Method

method()

Returns the method that was entered.

---

