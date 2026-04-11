# Class InvocationTargetException

**Source:** `java.base\java\lang\reflect\InvocationTargetException.html`

### Class Description

```java
public class
InvocationTargetException

extends
ReflectiveOperationException
```

InvocationTargetException is a checked exception that wraps
an exception thrown by an invoked method or constructor.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "target exception"
that is provided at construction time and accessed via the

getTargetException()

method is now known as the

cause

,
and may be accessed via the

Throwable.getCause()

method,
as well as the aforementioned "legacy method."

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected InvocationTargetException()

Constructs an

InvocationTargetException

with

null

as the target exception.

---

#### public InvocationTargetException​(
Throwable
target)

Constructs a InvocationTargetException with a target exception.

**Parameters:**
- target

- the target exception

---

#### public InvocationTargetException​(
Throwable
target,

String
s)

Constructs a InvocationTargetException with a target exception
and a detail message.

**Parameters:**
- target

- the target exception
- s

- the detail message

---

### Method Details

#### public
Throwable
getTargetException()

Get the thrown target exception.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:**
- the thrown target exception (cause of this exception).

---

#### public
Throwable
getCause()

Returns the cause of this exception (the thrown target exception,
which may be

null

).

**Overrides:**
- getCause

in class

Throwable

**Returns:**
- the cause of this exception.

**Since:**
- 1.4

---

### Additional Sections

#### Class InvocationTargetException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.ReflectiveOperationException
- - java.lang.reflect.InvocationTargetException

java.lang.Throwable

- java.lang.Exception
- - java.lang.ReflectiveOperationException
- - java.lang.reflect.InvocationTargetException

java.lang.Exception

- java.lang.ReflectiveOperationException
- - java.lang.reflect.InvocationTargetException

java.lang.ReflectiveOperationException

- java.lang.reflect.InvocationTargetException

java.lang.reflect.InvocationTargetException

**All Implemented Interfaces:** Serializable

```java
public class
InvocationTargetException

extends
ReflectiveOperationException
```

InvocationTargetException is a checked exception that wraps
an exception thrown by an invoked method or constructor.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "target exception"
that is provided at construction time and accessed via the

getTargetException()

method is now known as the

cause

,
and may be accessed via the

Throwable.getCause()

method,
as well as the aforementioned "legacy method."

**Since:** 1.1
**See Also:** Method

,

Constructor

,

Serialized Form

public class

InvocationTargetException

extends

ReflectiveOperationException

InvocationTargetException is a checked exception that wraps
an exception thrown by an invoked method or constructor.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "target exception"
that is provided at construction time and accessed via the

getTargetException()

method is now known as the

cause

,
and may be accessed via the

Throwable.getCause()

method,
as well as the aforementioned "legacy method."

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "target exception"
that is provided at construction time and accessed via the

getTargetException()

method is now known as the

cause

,
and may be accessed via the

Throwable.getCause()

method,
as well as the aforementioned "legacy method."

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

InvocationTargetException

()

Constructs an

InvocationTargetException

with

null

as the target exception.

InvocationTargetException

​(

Throwable

target)

Constructs a InvocationTargetException with a target exception.

InvocationTargetException

​(

Throwable

target,

String

s)

Constructs a InvocationTargetException with a target exception
and a detail message.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Throwable

getCause

()

Returns the cause of this exception (the thrown target exception,
which may be

null

).

Throwable

getTargetException

()

Get the thrown target exception.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

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

Modifier

Constructor

Description

protected

InvocationTargetException

()

Constructs an

InvocationTargetException

with

null

as the target exception.

InvocationTargetException

​(

Throwable

target)

Constructs a InvocationTargetException with a target exception.

InvocationTargetException

​(

Throwable

target,

String

s)

Constructs a InvocationTargetException with a target exception
and a detail message.

---

#### Constructor Summary

Constructs an

InvocationTargetException

with

null

as the target exception.

Constructs a InvocationTargetException with a target exception.

Constructs a InvocationTargetException with a target exception
and a detail message.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Throwable

getCause

()

Returns the cause of this exception (the thrown target exception,
which may be

null

).

Throwable

getTargetException

()

Get the thrown target exception.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

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

Returns the cause of this exception (the thrown target exception,
which may be

null

).

Get the thrown target exception.

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

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

- InvocationTargetException

```java
protected InvocationTargetException()
```

Constructs an

InvocationTargetException

with

null

as the target exception.

- InvocationTargetException

```java
public InvocationTargetException​(
Throwable
target)
```

Constructs a InvocationTargetException with a target exception.

**Parameters:** target

- the target exception

- InvocationTargetException

```java
public InvocationTargetException​(
Throwable
target,

String
s)
```

Constructs a InvocationTargetException with a target exception
and a detail message.

**Parameters:** target

- the target exception
**Parameters:** s

- the detail message

============ METHOD DETAIL ==========

- Method Detail

- getTargetException

```java
public
Throwable
getTargetException()
```

Get the thrown target exception.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:** the thrown target exception (cause of this exception).

- getCause

```java
public
Throwable
getCause()
```

Returns the cause of this exception (the thrown target exception,
which may be

null

).

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this exception.
**Since:** 1.4

Constructor Detail

- InvocationTargetException

```java
protected InvocationTargetException()
```

Constructs an

InvocationTargetException

with

null

as the target exception.

- InvocationTargetException

```java
public InvocationTargetException​(
Throwable
target)
```

Constructs a InvocationTargetException with a target exception.

**Parameters:** target

- the target exception

- InvocationTargetException

```java
public InvocationTargetException​(
Throwable
target,

String
s)
```

Constructs a InvocationTargetException with a target exception
and a detail message.

**Parameters:** target

- the target exception
**Parameters:** s

- the detail message

---

#### Constructor Detail

InvocationTargetException

```java
protected InvocationTargetException()
```

Constructs an

InvocationTargetException

with

null

as the target exception.

---

#### InvocationTargetException

protected InvocationTargetException()

Constructs an

InvocationTargetException

with

null

as the target exception.

InvocationTargetException

```java
public InvocationTargetException​(
Throwable
target)
```

Constructs a InvocationTargetException with a target exception.

**Parameters:** target

- the target exception

---

#### InvocationTargetException

public InvocationTargetException​(

Throwable

target)

Constructs a InvocationTargetException with a target exception.

InvocationTargetException

```java
public InvocationTargetException​(
Throwable
target,

String
s)
```

Constructs a InvocationTargetException with a target exception
and a detail message.

**Parameters:** target

- the target exception
**Parameters:** s

- the detail message

---

#### InvocationTargetException

public InvocationTargetException​(

Throwable

target,

String

s)

Constructs a InvocationTargetException with a target exception
and a detail message.

Method Detail

- getTargetException

```java
public
Throwable
getTargetException()
```

Get the thrown target exception.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:** the thrown target exception (cause of this exception).

- getCause

```java
public
Throwable
getCause()
```

Returns the cause of this exception (the thrown target exception,
which may be

null

).

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this exception.
**Since:** 1.4

---

#### Method Detail

getTargetException

```java
public
Throwable
getTargetException()
```

Get the thrown target exception.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:** the thrown target exception (cause of this exception).

---

#### getTargetException

public

Throwable

getTargetException()

Get the thrown target exception.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

getCause

```java
public
Throwable
getCause()
```

Returns the cause of this exception (the thrown target exception,
which may be

null

).

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this exception.
**Since:** 1.4

---

#### getCause

public

Throwable

getCause()

Returns the cause of this exception (the thrown target exception,
which may be

null

).

---

