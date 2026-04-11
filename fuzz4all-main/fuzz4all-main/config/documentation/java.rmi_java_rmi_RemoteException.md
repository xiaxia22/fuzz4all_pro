# Class RemoteException

**Source:** `java.rmi\java\rmi\RemoteException.html`

### Class Description

```java
public class
RemoteException

extends
IOException
```

A

RemoteException

is the common superclass for a number of
communication-related exceptions that may occur during the execution of a
remote method call. Each method of a remote interface, an interface that
extends

java.rmi.Remote

, must list

RemoteException

in its throws clause.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "wrapped remote
exception" that may be provided at construction time and accessed via
the public

detail

field is now known as the

cause

, and
may be accessed via the

Throwable.getCause()

method, as well as
the aforementioned "legacy field."

Invoking the method

Throwable.initCause(Throwable)

on an
instance of

RemoteException

always throws

IllegalStateException

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public
Throwable
detail

The cause of the remote exception.

This field predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

---

### Constructor Details

#### public RemoteException()

Constructs a

RemoteException

.

---

#### public RemoteException​(
String
s)

Constructs a

RemoteException

with the specified
detail message.

**Parameters:**
- s

- the detail message

---

#### public RemoteException​(
String
s,

Throwable
cause)

Constructs a

RemoteException

with the specified detail
message and cause. This constructor sets the

detail

field to the specified

Throwable

.

**Parameters:**
- s

- the detail message
- cause

- the cause

---

### Method Details

#### public
String
getMessage()

Returns the detail message, including the message from the cause, if
any, of this exception.

**Overrides:**
- getMessage

in class

Throwable

**Returns:**
- the detail message

---

#### public
Throwable
getCause()

Returns the cause of this exception. This method returns the value
of the

detail

field.

**Overrides:**
- getCause

in class

Throwable

**Returns:**
- the cause, which may be

null

.

**Since:**
- 1.4

---

### Additional Sections

#### Class RemoteException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.rmi.RemoteException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.rmi.RemoteException

java.lang.Exception

- java.io.IOException
- - java.rmi.RemoteException

java.io.IOException

- java.rmi.RemoteException

java.rmi.RemoteException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** AccessException

,

ActivateFailedException

,

ConnectException

,

ConnectIOException

,

ExportException

,

MarshalException

,

NoSuchObjectException

,

ServerError

,

ServerException

,

ServerRuntimeException

,

SkeletonMismatchException

,

SkeletonNotFoundException

,

StubNotFoundException

,

UnexpectedException

,

UnknownHostException

,

UnmarshalException

```java
public class
RemoteException

extends
IOException
```

A

RemoteException

is the common superclass for a number of
communication-related exceptions that may occur during the execution of a
remote method call. Each method of a remote interface, an interface that
extends

java.rmi.Remote

, must list

RemoteException

in its throws clause.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "wrapped remote
exception" that may be provided at construction time and accessed via
the public

detail

field is now known as the

cause

, and
may be accessed via the

Throwable.getCause()

method, as well as
the aforementioned "legacy field."

Invoking the method

Throwable.initCause(Throwable)

on an
instance of

RemoteException

always throws

IllegalStateException

.

**Since:** 1.1
**See Also:** Serialized Form

public class

RemoteException

extends

IOException

A

RemoteException

is the common superclass for a number of
communication-related exceptions that may occur during the execution of a
remote method call. Each method of a remote interface, an interface that
extends

java.rmi.Remote

, must list

RemoteException

in its throws clause.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "wrapped remote
exception" that may be provided at construction time and accessed via
the public

detail

field is now known as the

cause

, and
may be accessed via the

Throwable.getCause()

method, as well as
the aforementioned "legacy field."

Invoking the method

Throwable.initCause(Throwable)

on an
instance of

RemoteException

always throws

IllegalStateException

.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "wrapped remote
exception" that may be provided at construction time and accessed via
the public

detail

field is now known as the

cause

, and
may be accessed via the

Throwable.getCause()

method, as well as
the aforementioned "legacy field."

Invoking the method

Throwable.initCause(Throwable)

on an
instance of

RemoteException

always throws

IllegalStateException

.

Invoking the method

Throwable.initCause(Throwable)

on an
instance of

RemoteException

always throws

IllegalStateException

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

Throwable

detail

The cause of the remote exception.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RemoteException

()

Constructs a

RemoteException

.

RemoteException

​(

String

s)

Constructs a

RemoteException

with the specified
detail message.

RemoteException

​(

String

s,

Throwable

cause)

Constructs a

RemoteException

with the specified detail
message and cause.

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

Returns the cause of this exception.

String

getMessage

()

Returns the detail message, including the message from the cause, if
any, of this exception.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getLocalizedMessage

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

Field Summary

Fields

Modifier and Type

Field

Description

Throwable

detail

The cause of the remote exception.

---

#### Field Summary

The cause of the remote exception.

Constructor Summary

Constructors

Constructor

Description

RemoteException

()

Constructs a

RemoteException

.

RemoteException

​(

String

s)

Constructs a

RemoteException

with the specified
detail message.

RemoteException

​(

String

s,

Throwable

cause)

Constructs a

RemoteException

with the specified detail
message and cause.

---

#### Constructor Summary

Constructs a

RemoteException

.

Constructs a

RemoteException

with the specified
detail message.

Constructs a

RemoteException

with the specified detail
message and cause.

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

Returns the cause of this exception.

String

getMessage

()

Returns the detail message, including the message from the cause, if
any, of this exception.

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getLocalizedMessage

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

Returns the cause of this exception.

Returns the detail message, including the message from the cause, if
any, of this exception.

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getLocalizedMessage

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

============ FIELD DETAIL ===========

- Field Detail

- detail

```java
public
Throwable
detail
```

The cause of the remote exception.

This field predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- RemoteException

```java
public RemoteException()
```

Constructs a

RemoteException

.

- RemoteException

```java
public RemoteException​(
String
s)
```

Constructs a

RemoteException

with the specified
detail message.

**Parameters:** s

- the detail message

- RemoteException

```java
public RemoteException​(
String
s,

Throwable
cause)
```

Constructs a

RemoteException

with the specified detail
message and cause. This constructor sets the

detail

field to the specified

Throwable

.

**Parameters:** s

- the detail message
**Parameters:** cause

- the cause

============ METHOD DETAIL ==========

- Method Detail

- getMessage

```java
public
String
getMessage()
```

Returns the detail message, including the message from the cause, if
any, of this exception.

**Overrides:** getMessage

in class

Throwable
**Returns:** the detail message

- getCause

```java
public
Throwable
getCause()
```

Returns the cause of this exception. This method returns the value
of the

detail

field.

**Overrides:** getCause

in class

Throwable
**Returns:** the cause, which may be

null

.
**Since:** 1.4

Field Detail

- detail

```java
public
Throwable
detail
```

The cause of the remote exception.

This field predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

---

#### Field Detail

detail

```java
public
Throwable
detail
```

The cause of the remote exception.

This field predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

---

#### detail

public

Throwable

detail

The cause of the remote exception.

This field predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

This field predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

Constructor Detail

- RemoteException

```java
public RemoteException()
```

Constructs a

RemoteException

.

- RemoteException

```java
public RemoteException​(
String
s)
```

Constructs a

RemoteException

with the specified
detail message.

**Parameters:** s

- the detail message

- RemoteException

```java
public RemoteException​(
String
s,

Throwable
cause)
```

Constructs a

RemoteException

with the specified detail
message and cause. This constructor sets the

detail

field to the specified

Throwable

.

**Parameters:** s

- the detail message
**Parameters:** cause

- the cause

---

#### Constructor Detail

RemoteException

```java
public RemoteException()
```

Constructs a

RemoteException

.

---

#### RemoteException

public RemoteException()

Constructs a

RemoteException

.

RemoteException

```java
public RemoteException​(
String
s)
```

Constructs a

RemoteException

with the specified
detail message.

**Parameters:** s

- the detail message

---

#### RemoteException

public RemoteException​(

String

s)

Constructs a

RemoteException

with the specified
detail message.

RemoteException

```java
public RemoteException​(
String
s,

Throwable
cause)
```

Constructs a

RemoteException

with the specified detail
message and cause. This constructor sets the

detail

field to the specified

Throwable

.

**Parameters:** s

- the detail message
**Parameters:** cause

- the cause

---

#### RemoteException

public RemoteException​(

String

s,

Throwable

cause)

Constructs a

RemoteException

with the specified detail
message and cause. This constructor sets the

detail

field to the specified

Throwable

.

Method Detail

- getMessage

```java
public
String
getMessage()
```

Returns the detail message, including the message from the cause, if
any, of this exception.

**Overrides:** getMessage

in class

Throwable
**Returns:** the detail message

- getCause

```java
public
Throwable
getCause()
```

Returns the cause of this exception. This method returns the value
of the

detail

field.

**Overrides:** getCause

in class

Throwable
**Returns:** the cause, which may be

null

.
**Since:** 1.4

---

#### Method Detail

getMessage

```java
public
String
getMessage()
```

Returns the detail message, including the message from the cause, if
any, of this exception.

**Overrides:** getMessage

in class

Throwable
**Returns:** the detail message

---

#### getMessage

public

String

getMessage()

Returns the detail message, including the message from the cause, if
any, of this exception.

getCause

```java
public
Throwable
getCause()
```

Returns the cause of this exception. This method returns the value
of the

detail

field.

**Overrides:** getCause

in class

Throwable
**Returns:** the cause, which may be

null

.
**Since:** 1.4

---

#### getCause

public

Throwable

getCause()

Returns the cause of this exception. This method returns the value
of the

detail

field.

---

