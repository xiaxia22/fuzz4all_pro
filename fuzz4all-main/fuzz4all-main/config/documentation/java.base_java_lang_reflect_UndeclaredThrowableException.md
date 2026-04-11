# Class UndeclaredThrowableException

**Source:** `java.base\java\lang\reflect\UndeclaredThrowableException.html`

### Class Description

```java
public class
UndeclaredThrowableException

extends
RuntimeException
```

Thrown by a method invocation on a proxy instance if its invocation
handler's

invoke

method throws a
checked exception (a

Throwable

that is not assignable
to

RuntimeException

or

Error

) that
is not assignable to any of the exception types declared in the

throws

clause of the method that was invoked on the
proxy instance and dispatched to the invocation handler.

An

UndeclaredThrowableException

instance contains
the undeclared checked exception that was thrown by the invocation
handler, and it can be retrieved with the

getUndeclaredThrowable()

method.

UndeclaredThrowableException

extends

RuntimeException

, so it is an unchecked exception
that wraps a checked exception.

As of release 1.4, this exception has been retrofitted to
conform to the general purpose exception-chaining mechanism. The
"undeclared checked exception that was thrown by the invocation
handler" that may be provided at construction time and accessed via
the

getUndeclaredThrowable()

method is now known as the

cause

, and may be accessed via the

Throwable.getCause()

method, as well as the aforementioned "legacy
method."

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public UndeclaredThrowableException​(
Throwable
undeclaredThrowable)

Constructs an

UndeclaredThrowableException

with the
specified

Throwable

.

**Parameters:**
- undeclaredThrowable

- the undeclared checked exception
that was thrown

---

#### public UndeclaredThrowableException​(
Throwable
undeclaredThrowable,

String
s)

Constructs an

UndeclaredThrowableException

with the
specified

Throwable

and a detail message.

**Parameters:**
- undeclaredThrowable

- the undeclared checked exception
that was thrown
- s

- the detail message

---

### Method Details

#### public
Throwable
getUndeclaredThrowable()

Returns the

Throwable

instance wrapped in this

UndeclaredThrowableException

, which may be

null

.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:**
- the undeclared checked exception that was thrown

---

#### public
Throwable
getCause()

Returns the cause of this exception (the

Throwable

instance wrapped in this

UndeclaredThrowableException

,
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

#### Class UndeclaredThrowableException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.reflect.UndeclaredThrowableException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - java.lang.reflect.UndeclaredThrowableException

java.lang.Exception

- java.lang.RuntimeException
- - java.lang.reflect.UndeclaredThrowableException

java.lang.RuntimeException

- java.lang.reflect.UndeclaredThrowableException

java.lang.reflect.UndeclaredThrowableException

**All Implemented Interfaces:** Serializable

```java
public class
UndeclaredThrowableException

extends
RuntimeException
```

Thrown by a method invocation on a proxy instance if its invocation
handler's

invoke

method throws a
checked exception (a

Throwable

that is not assignable
to

RuntimeException

or

Error

) that
is not assignable to any of the exception types declared in the

throws

clause of the method that was invoked on the
proxy instance and dispatched to the invocation handler.

An

UndeclaredThrowableException

instance contains
the undeclared checked exception that was thrown by the invocation
handler, and it can be retrieved with the

getUndeclaredThrowable()

method.

UndeclaredThrowableException

extends

RuntimeException

, so it is an unchecked exception
that wraps a checked exception.

As of release 1.4, this exception has been retrofitted to
conform to the general purpose exception-chaining mechanism. The
"undeclared checked exception that was thrown by the invocation
handler" that may be provided at construction time and accessed via
the

getUndeclaredThrowable()

method is now known as the

cause

, and may be accessed via the

Throwable.getCause()

method, as well as the aforementioned "legacy
method."

**Since:** 1.3
**See Also:** InvocationHandler

,

Serialized Form

public class

UndeclaredThrowableException

extends

RuntimeException

Thrown by a method invocation on a proxy instance if its invocation
handler's

invoke

method throws a
checked exception (a

Throwable

that is not assignable
to

RuntimeException

or

Error

) that
is not assignable to any of the exception types declared in the

throws

clause of the method that was invoked on the
proxy instance and dispatched to the invocation handler.

An

UndeclaredThrowableException

instance contains
the undeclared checked exception that was thrown by the invocation
handler, and it can be retrieved with the

getUndeclaredThrowable()

method.

UndeclaredThrowableException

extends

RuntimeException

, so it is an unchecked exception
that wraps a checked exception.

As of release 1.4, this exception has been retrofitted to
conform to the general purpose exception-chaining mechanism. The
"undeclared checked exception that was thrown by the invocation
handler" that may be provided at construction time and accessed via
the

getUndeclaredThrowable()

method is now known as the

cause

, and may be accessed via the

Throwable.getCause()

method, as well as the aforementioned "legacy
method."

An

UndeclaredThrowableException

instance contains
the undeclared checked exception that was thrown by the invocation
handler, and it can be retrieved with the

getUndeclaredThrowable()

method.

UndeclaredThrowableException

extends

RuntimeException

, so it is an unchecked exception
that wraps a checked exception.

As of release 1.4, this exception has been retrofitted to
conform to the general purpose exception-chaining mechanism. The
"undeclared checked exception that was thrown by the invocation
handler" that may be provided at construction time and accessed via
the

getUndeclaredThrowable()

method is now known as the

cause

, and may be accessed via the

Throwable.getCause()

method, as well as the aforementioned "legacy
method."

As of release 1.4, this exception has been retrofitted to
conform to the general purpose exception-chaining mechanism. The
"undeclared checked exception that was thrown by the invocation
handler" that may be provided at construction time and accessed via
the

getUndeclaredThrowable()

method is now known as the

cause

, and may be accessed via the

Throwable.getCause()

method, as well as the aforementioned "legacy
method."

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

UndeclaredThrowableException

​(

Throwable

undeclaredThrowable)

Constructs an

UndeclaredThrowableException

with the
specified

Throwable

.

UndeclaredThrowableException

​(

Throwable

undeclaredThrowable,

String

s)

Constructs an

UndeclaredThrowableException

with the
specified

Throwable

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

Returns the cause of this exception (the

Throwable

instance wrapped in this

UndeclaredThrowableException

,
which may be

null

).

Throwable

getUndeclaredThrowable

()

Returns the

Throwable

instance wrapped in this

UndeclaredThrowableException

, which may be

null

.

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

Constructor

Description

UndeclaredThrowableException

​(

Throwable

undeclaredThrowable)

Constructs an

UndeclaredThrowableException

with the
specified

Throwable

.

UndeclaredThrowableException

​(

Throwable

undeclaredThrowable,

String

s)

Constructs an

UndeclaredThrowableException

with the
specified

Throwable

and a detail message.

---

#### Constructor Summary

Constructs an

UndeclaredThrowableException

with the
specified

Throwable

.

Constructs an

UndeclaredThrowableException

with the
specified

Throwable

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

Returns the cause of this exception (the

Throwable

instance wrapped in this

UndeclaredThrowableException

,
which may be

null

).

Throwable

getUndeclaredThrowable

()

Returns the

Throwable

instance wrapped in this

UndeclaredThrowableException

, which may be

null

.

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

Returns the cause of this exception (the

Throwable

instance wrapped in this

UndeclaredThrowableException

,
which may be

null

).

Returns the

Throwable

instance wrapped in this

UndeclaredThrowableException

, which may be

null

.

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

- UndeclaredThrowableException

```java
public UndeclaredThrowableException​(
Throwable
undeclaredThrowable)
```

Constructs an

UndeclaredThrowableException

with the
specified

Throwable

.

**Parameters:** undeclaredThrowable

- the undeclared checked exception
that was thrown

- UndeclaredThrowableException

```java
public UndeclaredThrowableException​(
Throwable
undeclaredThrowable,

String
s)
```

Constructs an

UndeclaredThrowableException

with the
specified

Throwable

and a detail message.

**Parameters:** undeclaredThrowable

- the undeclared checked exception
that was thrown
**Parameters:** s

- the detail message

============ METHOD DETAIL ==========

- Method Detail

- getUndeclaredThrowable

```java
public
Throwable
getUndeclaredThrowable()
```

Returns the

Throwable

instance wrapped in this

UndeclaredThrowableException

, which may be

null

.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:** the undeclared checked exception that was thrown

- getCause

```java
public
Throwable
getCause()
```

Returns the cause of this exception (the

Throwable

instance wrapped in this

UndeclaredThrowableException

,
which may be

null

).

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this exception.
**Since:** 1.4

Constructor Detail

- UndeclaredThrowableException

```java
public UndeclaredThrowableException​(
Throwable
undeclaredThrowable)
```

Constructs an

UndeclaredThrowableException

with the
specified

Throwable

.

**Parameters:** undeclaredThrowable

- the undeclared checked exception
that was thrown

- UndeclaredThrowableException

```java
public UndeclaredThrowableException​(
Throwable
undeclaredThrowable,

String
s)
```

Constructs an

UndeclaredThrowableException

with the
specified

Throwable

and a detail message.

**Parameters:** undeclaredThrowable

- the undeclared checked exception
that was thrown
**Parameters:** s

- the detail message

---

#### Constructor Detail

UndeclaredThrowableException

```java
public UndeclaredThrowableException​(
Throwable
undeclaredThrowable)
```

Constructs an

UndeclaredThrowableException

with the
specified

Throwable

.

**Parameters:** undeclaredThrowable

- the undeclared checked exception
that was thrown

---

#### UndeclaredThrowableException

public UndeclaredThrowableException​(

Throwable

undeclaredThrowable)

Constructs an

UndeclaredThrowableException

with the
specified

Throwable

.

UndeclaredThrowableException

```java
public UndeclaredThrowableException​(
Throwable
undeclaredThrowable,

String
s)
```

Constructs an

UndeclaredThrowableException

with the
specified

Throwable

and a detail message.

**Parameters:** undeclaredThrowable

- the undeclared checked exception
that was thrown
**Parameters:** s

- the detail message

---

#### UndeclaredThrowableException

public UndeclaredThrowableException​(

Throwable

undeclaredThrowable,

String

s)

Constructs an

UndeclaredThrowableException

with the
specified

Throwable

and a detail message.

Method Detail

- getUndeclaredThrowable

```java
public
Throwable
getUndeclaredThrowable()
```

Returns the

Throwable

instance wrapped in this

UndeclaredThrowableException

, which may be

null

.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:** the undeclared checked exception that was thrown

- getCause

```java
public
Throwable
getCause()
```

Returns the cause of this exception (the

Throwable

instance wrapped in this

UndeclaredThrowableException

,
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

getUndeclaredThrowable

```java
public
Throwable
getUndeclaredThrowable()
```

Returns the

Throwable

instance wrapped in this

UndeclaredThrowableException

, which may be

null

.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:** the undeclared checked exception that was thrown

---

#### getUndeclaredThrowable

public

Throwable

getUndeclaredThrowable()

Returns the

Throwable

instance wrapped in this

UndeclaredThrowableException

, which may be

null

.

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

Returns the cause of this exception (the

Throwable

instance wrapped in this

UndeclaredThrowableException

,
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

Returns the cause of this exception (the

Throwable

instance wrapped in this

UndeclaredThrowableException

,
which may be

null

).

---

