# Class WrongMethodTypeException

**Source:** `java.base\java\lang\invoke\WrongMethodTypeException.html`

### Class Description

```java
public class
WrongMethodTypeException

extends
RuntimeException
```

Thrown to indicate that code has attempted to call a method handle
via the wrong method type. As with the bytecode representation of
normal Java method calls, method handle calls are strongly typed
to a specific type descriptor associated with a call site.

This exception may also be thrown when two method handles are
composed, and the system detects that their types cannot be
matched up correctly. This amounts to an early evaluation
of the type mismatch, at method handle construction time,
instead of when the mismatched method handle is called.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public WrongMethodTypeException()

Constructs a

WrongMethodTypeException

with no detail message.

---

#### public WrongMethodTypeException​(
String
s)

Constructs a

WrongMethodTypeException

with the specified
detail message.

**Parameters:**
- s

- the detail message.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class WrongMethodTypeException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.invoke.WrongMethodTypeException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.invoke.WrongMethodTypeException

java.lang.Exception

- java.lang.RuntimeException
- - java.lang.invoke.WrongMethodTypeException

java.lang.RuntimeException

- java.lang.invoke.WrongMethodTypeException

java.lang.invoke.WrongMethodTypeException

**All Implemented Interfaces:** Serializable

```java
public class
WrongMethodTypeException

extends
RuntimeException
```

Thrown to indicate that code has attempted to call a method handle
via the wrong method type. As with the bytecode representation of
normal Java method calls, method handle calls are strongly typed
to a specific type descriptor associated with a call site.

This exception may also be thrown when two method handles are
composed, and the system detects that their types cannot be
matched up correctly. This amounts to an early evaluation
of the type mismatch, at method handle construction time,
instead of when the mismatched method handle is called.

**Since:** 1.7
**See Also:** Serialized Form

public class

WrongMethodTypeException

extends

RuntimeException

Thrown to indicate that code has attempted to call a method handle
via the wrong method type. As with the bytecode representation of
normal Java method calls, method handle calls are strongly typed
to a specific type descriptor associated with a call site.

This exception may also be thrown when two method handles are
composed, and the system detects that their types cannot be
matched up correctly. This amounts to an early evaluation
of the type mismatch, at method handle construction time,
instead of when the mismatched method handle is called.

This exception may also be thrown when two method handles are
composed, and the system detects that their types cannot be
matched up correctly. This amounts to an early evaluation
of the type mismatch, at method handle construction time,
instead of when the mismatched method handle is called.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

WrongMethodTypeException

()

Constructs a

WrongMethodTypeException

with no detail message.

WrongMethodTypeException

​(

String

s)

Constructs a

WrongMethodTypeException

with the specified
detail message.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

WrongMethodTypeException

()

Constructs a

WrongMethodTypeException

with no detail message.

WrongMethodTypeException

​(

String

s)

Constructs a

WrongMethodTypeException

with the specified
detail message.

---

#### Constructor Summary

Constructs a

WrongMethodTypeException

with no detail message.

Constructs a

WrongMethodTypeException

with the specified
detail message.

Method Summary

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

wait

,

wait

,

wait

---

#### Method Summary

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

---

#### Methods declared in class java.lang. Throwable

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- WrongMethodTypeException

```java
public WrongMethodTypeException()
```

Constructs a

WrongMethodTypeException

with no detail message.

- WrongMethodTypeException

```java
public WrongMethodTypeException​(
String
s)
```

Constructs a

WrongMethodTypeException

with the specified
detail message.

**Parameters:** s

- the detail message.

Constructor Detail

- WrongMethodTypeException

```java
public WrongMethodTypeException()
```

Constructs a

WrongMethodTypeException

with no detail message.

- WrongMethodTypeException

```java
public WrongMethodTypeException​(
String
s)
```

Constructs a

WrongMethodTypeException

with the specified
detail message.

**Parameters:** s

- the detail message.

---

#### Constructor Detail

WrongMethodTypeException

```java
public WrongMethodTypeException()
```

Constructs a

WrongMethodTypeException

with no detail message.

---

#### WrongMethodTypeException

public WrongMethodTypeException()

Constructs a

WrongMethodTypeException

with no detail message.

WrongMethodTypeException

```java
public WrongMethodTypeException​(
String
s)
```

Constructs a

WrongMethodTypeException

with the specified
detail message.

**Parameters:** s

- the detail message.

---

#### WrongMethodTypeException

public WrongMethodTypeException​(

String

s)

Constructs a

WrongMethodTypeException

with the specified
detail message.

---

