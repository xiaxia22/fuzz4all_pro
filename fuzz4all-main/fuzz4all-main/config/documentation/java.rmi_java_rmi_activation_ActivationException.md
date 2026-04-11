# Class ActivationException

**Source:** `java.rmi\java\rmi\activation\ActivationException.html`

### Class Description

```java
public class
ActivationException

extends
Exception
```

General exception used by the activation interfaces.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "detail exception"
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

ActivationException

always throws

IllegalStateException

.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public
Throwable
detail

The cause of the activation exception.

This field predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

---

### Constructor Details

#### public ActivationException()

Constructs an

ActivationException

.

---

#### public ActivationException​(
String
s)

Constructs an

ActivationException

with the specified
detail message.

**Parameters:**
- s

- the detail message

---

#### public ActivationException​(
String
s,

Throwable
cause)

Constructs an

ActivationException

with the specified
detail message and cause. This constructor sets the

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

#### Class ActivationException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.rmi.activation.ActivationException

java.lang.Throwable

- java.lang.Exception
- - java.rmi.activation.ActivationException

java.lang.Exception

- java.rmi.activation.ActivationException

java.rmi.activation.ActivationException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** UnknownGroupException

,

UnknownObjectException

```java
public class
ActivationException

extends
Exception
```

General exception used by the activation interfaces.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "detail exception"
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

ActivationException

always throws

IllegalStateException

.

**Since:** 1.2
**See Also:** Serialized Form

public class

ActivationException

extends

Exception

General exception used by the activation interfaces.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "detail exception"
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

ActivationException

always throws

IllegalStateException

.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "detail exception"
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

ActivationException

always throws

IllegalStateException

.

Invoking the method

Throwable.initCause(Throwable)

on an
instance of

ActivationException

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

The cause of the activation exception.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ActivationException

()

Constructs an

ActivationException

.

ActivationException

​(

String

s)

Constructs an

ActivationException

with the specified
detail message.

ActivationException

​(

String

s,

Throwable

cause)

Constructs an

ActivationException

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

Throwable

detail

The cause of the activation exception.

---

#### Field Summary

The cause of the activation exception.

Constructor Summary

Constructors

Constructor

Description

ActivationException

()

Constructs an

ActivationException

.

ActivationException

​(

String

s)

Constructs an

ActivationException

with the specified
detail message.

ActivationException

​(

String

s,

Throwable

cause)

Constructs an

ActivationException

with the specified
detail message and cause.

---

#### Constructor Summary

Constructs an

ActivationException

.

Constructs an

ActivationException

with the specified
detail message.

Constructs an

ActivationException

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
Throwable
detail
```

The cause of the activation exception.

This field predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ActivationException

```java
public ActivationException()
```

Constructs an

ActivationException

.

- ActivationException

```java
public ActivationException​(
String
s)
```

Constructs an

ActivationException

with the specified
detail message.

**Parameters:** s

- the detail message

- ActivationException

```java
public ActivationException​(
String
s,

Throwable
cause)
```

Constructs an

ActivationException

with the specified
detail message and cause. This constructor sets the

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

The cause of the activation exception.

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

The cause of the activation exception.

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

The cause of the activation exception.

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

- ActivationException

```java
public ActivationException()
```

Constructs an

ActivationException

.

- ActivationException

```java
public ActivationException​(
String
s)
```

Constructs an

ActivationException

with the specified
detail message.

**Parameters:** s

- the detail message

- ActivationException

```java
public ActivationException​(
String
s,

Throwable
cause)
```

Constructs an

ActivationException

with the specified
detail message and cause. This constructor sets the

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

ActivationException

```java
public ActivationException()
```

Constructs an

ActivationException

.

---

#### ActivationException

public ActivationException()

Constructs an

ActivationException

.

ActivationException

```java
public ActivationException​(
String
s)
```

Constructs an

ActivationException

with the specified
detail message.

**Parameters:** s

- the detail message

---

#### ActivationException

public ActivationException​(

String

s)

Constructs an

ActivationException

with the specified
detail message.

ActivationException

```java
public ActivationException​(
String
s,

Throwable
cause)
```

Constructs an

ActivationException

with the specified
detail message and cause. This constructor sets the

detail

field to the specified

Throwable

.

**Parameters:** s

- the detail message
**Parameters:** cause

- the cause

---

#### ActivationException

public ActivationException​(

String

s,

Throwable

cause)

Constructs an

ActivationException

with the specified
detail message and cause. This constructor sets the

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

