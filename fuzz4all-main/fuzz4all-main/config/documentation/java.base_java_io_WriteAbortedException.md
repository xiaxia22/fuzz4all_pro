# Class WriteAbortedException

**Source:** `java.base\java\io\WriteAbortedException.html`

### Class Description

```java
public class
WriteAbortedException

extends
ObjectStreamException
```

Signals that one of the ObjectStreamExceptions was thrown during a
write operation. Thrown during a read operation when one of the
ObjectStreamExceptions was thrown during a write operation. The
exception that terminated the write can be found in the detail
field. The stream is reset to it's initial state and all references
to objects already deserialized are discarded.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "exception causing
the abort" that is provided at construction time and
accessed via the public

detail

field is now known as the

cause

, and may be accessed via the

Throwable.getCause()

method, as well as the aforementioned "legacy field."

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public
Exception
detail

Exception that was caught while writing the ObjectStream.

This field predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

---

### Constructor Details

#### public WriteAbortedException​(
String
s,

Exception
ex)

Constructs a WriteAbortedException with a string describing
the exception and the exception causing the abort.

**Parameters:**
- s

- String describing the exception.
- ex

- Exception causing the abort.

---

### Method Details

#### public
String
getMessage()

Produce the message and include the message from the nested
exception, if there is one.

**Overrides:**
- getMessage

in class

Throwable

**Returns:**
- the detail message string of this

Throwable

instance
(which may be

null

).

---

#### public
Throwable
getCause()

Returns the exception that terminated the operation (the

cause

).

**Overrides:**
- getCause

in class

Throwable

**Returns:**
- the exception that terminated the operation (the

cause

),
which may be null.

**Since:**
- 1.4

---

### Additional Sections

#### Class WriteAbortedException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.io.ObjectStreamException
- - java.io.WriteAbortedException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.io.ObjectStreamException
- - java.io.WriteAbortedException

java.lang.Exception

- java.io.IOException
- - java.io.ObjectStreamException
- - java.io.WriteAbortedException

java.io.IOException

- java.io.ObjectStreamException
- - java.io.WriteAbortedException

java.io.ObjectStreamException

- java.io.WriteAbortedException

java.io.WriteAbortedException

**All Implemented Interfaces:** Serializable

```java
public class
WriteAbortedException

extends
ObjectStreamException
```

Signals that one of the ObjectStreamExceptions was thrown during a
write operation. Thrown during a read operation when one of the
ObjectStreamExceptions was thrown during a write operation. The
exception that terminated the write can be found in the detail
field. The stream is reset to it's initial state and all references
to objects already deserialized are discarded.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "exception causing
the abort" that is provided at construction time and
accessed via the public

detail

field is now known as the

cause

, and may be accessed via the

Throwable.getCause()

method, as well as the aforementioned "legacy field."

**Since:** 1.1
**See Also:** Serialized Form

public class

WriteAbortedException

extends

ObjectStreamException

Signals that one of the ObjectStreamExceptions was thrown during a
write operation. Thrown during a read operation when one of the
ObjectStreamExceptions was thrown during a write operation. The
exception that terminated the write can be found in the detail
field. The stream is reset to it's initial state and all references
to objects already deserialized are discarded.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "exception causing
the abort" that is provided at construction time and
accessed via the public

detail

field is now known as the

cause

, and may be accessed via the

Throwable.getCause()

method, as well as the aforementioned "legacy field."

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "exception causing
the abort" that is provided at construction time and
accessed via the public

detail

field is now known as the

cause

, and may be accessed via the

Throwable.getCause()

method, as well as the aforementioned "legacy field."

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

Exception

detail

Exception that was caught while writing the ObjectStream.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

WriteAbortedException

​(

String

s,

Exception

ex)

Constructs a WriteAbortedException with a string describing
the exception and the exception causing the abort.

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

Returns the exception that terminated the operation (the

cause

).

String

getMessage

()

Produce the message and include the message from the nested
exception, if there is one.

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

Exception that was caught while writing the ObjectStream.

---

#### Field Summary

Exception that was caught while writing the ObjectStream.

Constructor Summary

Constructors

Constructor

Description

WriteAbortedException

​(

String

s,

Exception

ex)

Constructs a WriteAbortedException with a string describing
the exception and the exception causing the abort.

---

#### Constructor Summary

Constructs a WriteAbortedException with a string describing
the exception and the exception causing the abort.

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

Returns the exception that terminated the operation (the

cause

).

String

getMessage

()

Produce the message and include the message from the nested
exception, if there is one.

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

Returns the exception that terminated the operation (the

cause

).

Produce the message and include the message from the nested
exception, if there is one.

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

Exception that was caught while writing the ObjectStream.

This field predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- WriteAbortedException

```java
public WriteAbortedException​(
String
s,

Exception
ex)
```

Constructs a WriteAbortedException with a string describing
the exception and the exception causing the abort.

**Parameters:** s

- String describing the exception.
**Parameters:** ex

- Exception causing the abort.

============ METHOD DETAIL ==========

- Method Detail

- getMessage

```java
public
String
getMessage()
```

Produce the message and include the message from the nested
exception, if there is one.

**Overrides:** getMessage

in class

Throwable
**Returns:** the detail message string of this

Throwable

instance
(which may be

null

).

- getCause

```java
public
Throwable
getCause()
```

Returns the exception that terminated the operation (the

cause

).

**Overrides:** getCause

in class

Throwable
**Returns:** the exception that terminated the operation (the

cause

),
which may be null.
**Since:** 1.4

Field Detail

- detail

```java
public
Exception
detail
```

Exception that was caught while writing the ObjectStream.

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

Exception that was caught while writing the ObjectStream.

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

Exception that was caught while writing the ObjectStream.

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

- WriteAbortedException

```java
public WriteAbortedException​(
String
s,

Exception
ex)
```

Constructs a WriteAbortedException with a string describing
the exception and the exception causing the abort.

**Parameters:** s

- String describing the exception.
**Parameters:** ex

- Exception causing the abort.

---

#### Constructor Detail

WriteAbortedException

```java
public WriteAbortedException​(
String
s,

Exception
ex)
```

Constructs a WriteAbortedException with a string describing
the exception and the exception causing the abort.

**Parameters:** s

- String describing the exception.
**Parameters:** ex

- Exception causing the abort.

---

#### WriteAbortedException

public WriteAbortedException​(

String

s,

Exception

ex)

Constructs a WriteAbortedException with a string describing
the exception and the exception causing the abort.

Method Detail

- getMessage

```java
public
String
getMessage()
```

Produce the message and include the message from the nested
exception, if there is one.

**Overrides:** getMessage

in class

Throwable
**Returns:** the detail message string of this

Throwable

instance
(which may be

null

).

- getCause

```java
public
Throwable
getCause()
```

Returns the exception that terminated the operation (the

cause

).

**Overrides:** getCause

in class

Throwable
**Returns:** the exception that terminated the operation (the

cause

),
which may be null.
**Since:** 1.4

---

#### Method Detail

getMessage

```java
public
String
getMessage()
```

Produce the message and include the message from the nested
exception, if there is one.

**Overrides:** getMessage

in class

Throwable
**Returns:** the detail message string of this

Throwable

instance
(which may be

null

).

---

#### getMessage

public

String

getMessage()

Produce the message and include the message from the nested
exception, if there is one.

getCause

```java
public
Throwable
getCause()
```

Returns the exception that terminated the operation (the

cause

).

**Overrides:** getCause

in class

Throwable
**Returns:** the exception that terminated the operation (the

cause

),
which may be null.
**Since:** 1.4

---

#### getCause

public

Throwable

getCause()

Returns the exception that terminated the operation (the

cause

).

---

