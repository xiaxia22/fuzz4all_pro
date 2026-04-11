# Class PrivilegedActionException

**Source:** `java.base\java\security\PrivilegedActionException.html`

### Class Description

```java
public class
PrivilegedActionException

extends
Exception
```

This exception is thrown by

doPrivileged(PrivilegedExceptionAction)

and

doPrivileged(PrivilegedExceptionAction,
AccessControlContext context)

to indicate
that the action being performed threw a checked exception. The exception
thrown by the action can be obtained by calling the

getException

method. In effect, an

PrivilegedActionException

is a "wrapper"
for an exception thrown by a privileged action.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "exception thrown
by the privileged computation" that is provided at construction time and
accessed via the

getException()

method is now known as the

cause

, and may be accessed via the

Throwable.getCause()

method, as well as the aforementioned "legacy method."

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public PrivilegedActionException​(
Exception
exception)

Constructs a new PrivilegedActionException "wrapping"
the specific Exception.

**Parameters:**
- exception

- The exception thrown

---

### Method Details

#### public
Exception
getException()

Returns the exception thrown by the privileged computation that
resulted in this

PrivilegedActionException

.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:**
- the exception thrown by the privileged computation that
resulted in this

PrivilegedActionException

.

**See Also:**
- PrivilegedExceptionAction

,

AccessController.doPrivileged(PrivilegedExceptionAction)

,

AccessController.doPrivileged(PrivilegedExceptionAction,
AccessControlContext)

---

#### public
Throwable
getCause()

Returns the cause of this exception (the exception thrown by
the privileged computation that resulted in this

PrivilegedActionException

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

#### Class PrivilegedActionException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.security.PrivilegedActionException

java.lang.Throwable

- java.lang.Exception
- - java.security.PrivilegedActionException

java.lang.Exception

- java.security.PrivilegedActionException

java.security.PrivilegedActionException

**All Implemented Interfaces:** Serializable

```java
public class
PrivilegedActionException

extends
Exception
```

This exception is thrown by

doPrivileged(PrivilegedExceptionAction)

and

doPrivileged(PrivilegedExceptionAction,
AccessControlContext context)

to indicate
that the action being performed threw a checked exception. The exception
thrown by the action can be obtained by calling the

getException

method. In effect, an

PrivilegedActionException

is a "wrapper"
for an exception thrown by a privileged action.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "exception thrown
by the privileged computation" that is provided at construction time and
accessed via the

getException()

method is now known as the

cause

, and may be accessed via the

Throwable.getCause()

method, as well as the aforementioned "legacy method."

**Since:** 1.2
**See Also:** PrivilegedExceptionAction

,

AccessController.doPrivileged(PrivilegedExceptionAction)

,

AccessController.doPrivileged(PrivilegedExceptionAction,AccessControlContext)

,

Serialized Form

public class

PrivilegedActionException

extends

Exception

This exception is thrown by

doPrivileged(PrivilegedExceptionAction)

and

doPrivileged(PrivilegedExceptionAction,
AccessControlContext context)

to indicate
that the action being performed threw a checked exception. The exception
thrown by the action can be obtained by calling the

getException

method. In effect, an

PrivilegedActionException

is a "wrapper"
for an exception thrown by a privileged action.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "exception thrown
by the privileged computation" that is provided at construction time and
accessed via the

getException()

method is now known as the

cause

, and may be accessed via the

Throwable.getCause()

method, as well as the aforementioned "legacy method."

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "exception thrown
by the privileged computation" that is provided at construction time and
accessed via the

getException()

method is now known as the

cause

, and may be accessed via the

Throwable.getCause()

method, as well as the aforementioned "legacy method."

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PrivilegedActionException

​(

Exception

exception)

Constructs a new PrivilegedActionException "wrapping"
the specific Exception.

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

Returns the cause of this exception (the exception thrown by
the privileged computation that resulted in this

PrivilegedActionException

).

Exception

getException

()

Returns the exception thrown by the privileged computation that
resulted in this

PrivilegedActionException

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

PrivilegedActionException

​(

Exception

exception)

Constructs a new PrivilegedActionException "wrapping"
the specific Exception.

---

#### Constructor Summary

Constructs a new PrivilegedActionException "wrapping"
the specific Exception.

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

Returns the cause of this exception (the exception thrown by
the privileged computation that resulted in this

PrivilegedActionException

).

Exception

getException

()

Returns the exception thrown by the privileged computation that
resulted in this

PrivilegedActionException

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

Returns the cause of this exception (the exception thrown by
the privileged computation that resulted in this

PrivilegedActionException

).

Returns the exception thrown by the privileged computation that
resulted in this

PrivilegedActionException

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

- PrivilegedActionException

```java
public PrivilegedActionException​(
Exception
exception)
```

Constructs a new PrivilegedActionException "wrapping"
the specific Exception.

**Parameters:** exception

- The exception thrown

============ METHOD DETAIL ==========

- Method Detail

- getException

```java
public
Exception
getException()
```

Returns the exception thrown by the privileged computation that
resulted in this

PrivilegedActionException

.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:** the exception thrown by the privileged computation that
resulted in this

PrivilegedActionException

.
**See Also:** PrivilegedExceptionAction

,

AccessController.doPrivileged(PrivilegedExceptionAction)

,

AccessController.doPrivileged(PrivilegedExceptionAction,
AccessControlContext)

- getCause

```java
public
Throwable
getCause()
```

Returns the cause of this exception (the exception thrown by
the privileged computation that resulted in this

PrivilegedActionException

).

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this exception.
**Since:** 1.4

Constructor Detail

- PrivilegedActionException

```java
public PrivilegedActionException​(
Exception
exception)
```

Constructs a new PrivilegedActionException "wrapping"
the specific Exception.

**Parameters:** exception

- The exception thrown

---

#### Constructor Detail

PrivilegedActionException

```java
public PrivilegedActionException​(
Exception
exception)
```

Constructs a new PrivilegedActionException "wrapping"
the specific Exception.

**Parameters:** exception

- The exception thrown

---

#### PrivilegedActionException

public PrivilegedActionException​(

Exception

exception)

Constructs a new PrivilegedActionException "wrapping"
the specific Exception.

Method Detail

- getException

```java
public
Exception
getException()
```

Returns the exception thrown by the privileged computation that
resulted in this

PrivilegedActionException

.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:** the exception thrown by the privileged computation that
resulted in this

PrivilegedActionException

.
**See Also:** PrivilegedExceptionAction

,

AccessController.doPrivileged(PrivilegedExceptionAction)

,

AccessController.doPrivileged(PrivilegedExceptionAction,
AccessControlContext)

- getCause

```java
public
Throwable
getCause()
```

Returns the cause of this exception (the exception thrown by
the privileged computation that resulted in this

PrivilegedActionException

).

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this exception.
**Since:** 1.4

---

#### Method Detail

getException

```java
public
Exception
getException()
```

Returns the exception thrown by the privileged computation that
resulted in this

PrivilegedActionException

.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:** the exception thrown by the privileged computation that
resulted in this

PrivilegedActionException

.
**See Also:** PrivilegedExceptionAction

,

AccessController.doPrivileged(PrivilegedExceptionAction)

,

AccessController.doPrivileged(PrivilegedExceptionAction,
AccessControlContext)

---

#### getException

public

Exception

getException()

Returns the exception thrown by the privileged computation that
resulted in this

PrivilegedActionException

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

Returns the cause of this exception (the exception thrown by
the privileged computation that resulted in this

PrivilegedActionException

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

Returns the cause of this exception (the exception thrown by
the privileged computation that resulted in this

PrivilegedActionException

).

---

