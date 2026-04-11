# Interface MethodExitEvent

**Source:** `jdk.jdi\com\sun\jdi\event\MethodExitEvent.html`

### Class Description

```java
public interface
MethodExitEvent

extends
LocatableEvent
```

Notification of a method return in the target VM. This event
is generated after all code in the method has executed, but the
location of this event is the last executed location in the method.
Method exit events are generated for both native and non-native
methods. Method exit events are not generated if the method terminates
with a thrown exception.

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

Returns the method that was exited.

**Returns:**
- a

Method

which mirrors the method that was exited.

**Throws:**
- ObjectCollectedException

- may be thrown if class
has been garbage collected.

---

#### Value
returnValue()

Returns the value that the method will return.

Not all target virtual machines support this operation.
Use

canGetMethodReturnValues()

to determine if this operation is supported.

**Returns:**
- a

Value

which mirrors the value to be returned.

**Throws:**
- UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetMethodReturnValues()

**Since:**
- 1.6

---

### Additional Sections

#### Interface MethodExitEvent

**All Superinterfaces:** Event

,

Locatable

,

LocatableEvent

,

Mirror

```java
public interface
MethodExitEvent

extends
LocatableEvent
```

Notification of a method return in the target VM. This event
is generated after all code in the method has executed, but the
location of this event is the last executed location in the method.
Method exit events are generated for both native and non-native
methods. Method exit events are not generated if the method terminates
with a thrown exception.

**Since:** 1.3
**See Also:** EventQueue

public interface

MethodExitEvent

extends

LocatableEvent

Notification of a method return in the target VM. This event
is generated after all code in the method has executed, but the
location of this event is the last executed location in the method.
Method exit events are generated for both native and non-native
methods. Method exit events are not generated if the method terminates
with a thrown exception.

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

Returns the method that was exited.

Value

returnValue

()

Returns the value that the method will return.

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

Returns the method that was exited.

Value

returnValue

()

Returns the value that the method will return.

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

Returns the method that was exited.

Returns the value that the method will return.

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

Returns the method that was exited.

**Returns:** a

Method

which mirrors the method that was exited.
**Throws:** ObjectCollectedException

- may be thrown if class
has been garbage collected.

- returnValue

```java
Value
returnValue()
```

Returns the value that the method will return.

Not all target virtual machines support this operation.
Use

canGetMethodReturnValues()

to determine if this operation is supported.

**Returns:** a

Value

which mirrors the value to be returned.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetMethodReturnValues()
**Since:** 1.6

Method Detail

- method

```java
Method
method()
```

Returns the method that was exited.

**Returns:** a

Method

which mirrors the method that was exited.
**Throws:** ObjectCollectedException

- may be thrown if class
has been garbage collected.

- returnValue

```java
Value
returnValue()
```

Returns the value that the method will return.

Not all target virtual machines support this operation.
Use

canGetMethodReturnValues()

to determine if this operation is supported.

**Returns:** a

Value

which mirrors the value to be returned.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetMethodReturnValues()
**Since:** 1.6

---

#### Method Detail

method

```java
Method
method()
```

Returns the method that was exited.

**Returns:** a

Method

which mirrors the method that was exited.
**Throws:** ObjectCollectedException

- may be thrown if class
has been garbage collected.

---

#### method

Method

method()

Returns the method that was exited.

returnValue

```java
Value
returnValue()
```

Returns the value that the method will return.

Not all target virtual machines support this operation.
Use

canGetMethodReturnValues()

to determine if this operation is supported.

**Returns:** a

Value

which mirrors the value to be returned.
**Throws:** UnsupportedOperationException

- if
the target virtual machine does not support this
operation - see

canGetMethodReturnValues()
**Since:** 1.6

---

#### returnValue

Value

returnValue()

Returns the value that the method will return.

Not all target virtual machines support this operation.
Use

canGetMethodReturnValues()

to determine if this operation is supported.

---

