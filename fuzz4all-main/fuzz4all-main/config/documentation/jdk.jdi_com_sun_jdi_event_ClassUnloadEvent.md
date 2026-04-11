# Interface ClassUnloadEvent

**Source:** `jdk.jdi\com\sun\jdi\event\ClassUnloadEvent.html`

### Class Description

```java
public interface
ClassUnloadEvent

extends
Event
```

Notification of a class unload in the target VM.

There are severe constraints on the debugger back-end during
garbage collection, so unload information is greatly limited.

**All Superinterfaces:** Event

,

Mirror

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
className()

Returns the name of the class that has been unloaded.

---

#### String
classSignature()

Returns the JNI-style signature of the class that has been unloaded.

---

### Additional Sections

#### Interface ClassUnloadEvent

**All Superinterfaces:** Event

,

Mirror

```java
public interface
ClassUnloadEvent

extends
Event
```

Notification of a class unload in the target VM.

There are severe constraints on the debugger back-end during
garbage collection, so unload information is greatly limited.

**Since:** 1.3
**See Also:** EventQueue

,

VirtualMachine

public interface

ClassUnloadEvent

extends

Event

Notification of a class unload in the target VM.

There are severe constraints on the debugger back-end during
garbage collection, so unload information is greatly limited.

There are severe constraints on the debugger back-end during
garbage collection, so unload information is greatly limited.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

className

()

Returns the name of the class that has been unloaded.

String

classSignature

()

Returns the JNI-style signature of the class that has been unloaded.

- Methods declared in interface com.sun.jdi.event.

Event

request

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

String

className

()

Returns the name of the class that has been unloaded.

String

classSignature

()

Returns the JNI-style signature of the class that has been unloaded.

- Methods declared in interface com.sun.jdi.event.

Event

request

- Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Method Summary

Returns the name of the class that has been unloaded.

Returns the JNI-style signature of the class that has been unloaded.

Methods declared in interface com.sun.jdi.event.

Event

request

---

#### Methods declared in interface com.sun.jdi.event. Event

Methods declared in interface com.sun.jdi.

Mirror

toString

,

virtualMachine

---

#### Methods declared in interface com.sun.jdi. Mirror

============ METHOD DETAIL ==========

- Method Detail

- className

```java
String
className()
```

Returns the name of the class that has been unloaded.

- classSignature

```java
String
classSignature()
```

Returns the JNI-style signature of the class that has been unloaded.

Method Detail

- className

```java
String
className()
```

Returns the name of the class that has been unloaded.

- classSignature

```java
String
classSignature()
```

Returns the JNI-style signature of the class that has been unloaded.

---

#### Method Detail

className

```java
String
className()
```

Returns the name of the class that has been unloaded.

---

#### className

String

className()

Returns the name of the class that has been unloaded.

classSignature

```java
String
classSignature()
```

Returns the JNI-style signature of the class that has been unloaded.

---

#### classSignature

String

classSignature()

Returns the JNI-style signature of the class that has been unloaded.

---

