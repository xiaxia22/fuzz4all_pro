# Class ServerCloneException

**Source:** `java.rmi\java\rmi\server\ServerCloneException.html`

### Class Description

```java
public class
ServerCloneException

extends
CloneNotSupportedException
```

A

ServerCloneException

is thrown if a remote exception occurs
during the cloning of a

UnicastRemoteObject

.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "nested exception"
that may be provided at construction time and accessed via the public

detail

field is now known as the

cause

, and may be
accessed via the

Throwable.getCause()

method, as well as
the aforementioned "legacy field."

Invoking the method

Throwable.initCause(Throwable)

on an
instance of

ServerCloneException

always throws

IllegalStateException

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public
Exception
detail

The cause of the exception.

This field predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

---

### Constructor Details

#### public ServerCloneException​(
String
s)

Constructs a

ServerCloneException

with the specified
detail message.

**Parameters:**
- s

- the detail message.

---

#### public ServerCloneException​(
String
s,

Exception
cause)

Constructs a

ServerCloneException

with the specified
detail message and cause.

**Parameters:**
- s

- the detail message.
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

#### Class ServerCloneException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.CloneNotSupportedException
- - java.rmi.server.ServerCloneException

java.lang.Throwable

- java.lang.Exception
- - java.lang.CloneNotSupportedException
- - java.rmi.server.ServerCloneException

java.lang.Exception

- java.lang.CloneNotSupportedException
- - java.rmi.server.ServerCloneException

java.lang.CloneNotSupportedException

- java.rmi.server.ServerCloneException

java.rmi.server.ServerCloneException

**All Implemented Interfaces:** Serializable

```java
public class
ServerCloneException

extends
CloneNotSupportedException
```

A

ServerCloneException

is thrown if a remote exception occurs
during the cloning of a

UnicastRemoteObject

.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "nested exception"
that may be provided at construction time and accessed via the public

detail

field is now known as the

cause

, and may be
accessed via the

Throwable.getCause()

method, as well as
the aforementioned "legacy field."

Invoking the method

Throwable.initCause(Throwable)

on an
instance of

ServerCloneException

always throws

IllegalStateException

.

**Since:** 1.1
**See Also:** UnicastRemoteObject.clone()

,

Serialized Form

public class

ServerCloneException

extends

CloneNotSupportedException

A

ServerCloneException

is thrown if a remote exception occurs
during the cloning of a

UnicastRemoteObject

.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "nested exception"
that may be provided at construction time and accessed via the public

detail

field is now known as the

cause

, and may be
accessed via the

Throwable.getCause()

method, as well as
the aforementioned "legacy field."

Invoking the method

Throwable.initCause(Throwable)

on an
instance of

ServerCloneException

always throws

IllegalStateException

.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "nested exception"
that may be provided at construction time and accessed via the public

detail

field is now known as the

cause

, and may be
accessed via the

Throwable.getCause()

method, as well as
the aforementioned "legacy field."

Invoking the method

Throwable.initCause(Throwable)

on an
instance of

ServerCloneException

always throws

IllegalStateException

.

Invoking the method

Throwable.initCause(Throwable)

on an
instance of

ServerCloneException

always throws

IllegalStateException

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

Exception

detail

The cause of the exception.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ServerCloneException

​(

String

s)

Constructs a

ServerCloneException

with the specified
detail message.

ServerCloneException

​(

String

s,

Exception

cause)

Constructs a

ServerCloneException

with the specified
detail message and cause.

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

Exception

detail

The cause of the exception.

---

#### Field Summary

The cause of the exception.

Constructor Summary

Constructors

Constructor

Description

ServerCloneException

​(

String

s)

Constructs a

ServerCloneException

with the specified
detail message.

ServerCloneException

​(

String

s,

Exception

cause)

Constructs a

ServerCloneException

with the specified
detail message and cause.

---

#### Constructor Summary

Constructs a

ServerCloneException

with the specified
detail message.

Constructs a

ServerCloneException

with the specified
detail message and cause.

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
Exception
detail
```

The cause of the exception.

This field predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ServerCloneException

```java
public ServerCloneException​(
String
s)
```

Constructs a

ServerCloneException

with the specified
detail message.

**Parameters:** s

- the detail message.

- ServerCloneException

```java
public ServerCloneException​(
String
s,

Exception
cause)
```

Constructs a

ServerCloneException

with the specified
detail message and cause.

**Parameters:** s

- the detail message.
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
Exception
detail
```

The cause of the exception.

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
Exception
detail
```

The cause of the exception.

This field predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

---

#### detail

public

Exception

detail

The cause of the exception.

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

- ServerCloneException

```java
public ServerCloneException​(
String
s)
```

Constructs a

ServerCloneException

with the specified
detail message.

**Parameters:** s

- the detail message.

- ServerCloneException

```java
public ServerCloneException​(
String
s,

Exception
cause)
```

Constructs a

ServerCloneException

with the specified
detail message and cause.

**Parameters:** s

- the detail message.
**Parameters:** cause

- the cause

---

#### Constructor Detail

ServerCloneException

```java
public ServerCloneException​(
String
s)
```

Constructs a

ServerCloneException

with the specified
detail message.

**Parameters:** s

- the detail message.

---

#### ServerCloneException

public ServerCloneException​(

String

s)

Constructs a

ServerCloneException

with the specified
detail message.

ServerCloneException

```java
public ServerCloneException​(
String
s,

Exception
cause)
```

Constructs a

ServerCloneException

with the specified
detail message and cause.

**Parameters:** s

- the detail message.
**Parameters:** cause

- the cause

---

#### ServerCloneException

public ServerCloneException​(

String

s,

Exception

cause)

Constructs a

ServerCloneException

with the specified
detail message and cause.

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

