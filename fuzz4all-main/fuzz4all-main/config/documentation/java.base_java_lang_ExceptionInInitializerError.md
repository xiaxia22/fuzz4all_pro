# Class ExceptionInInitializerError

**Source:** `java.base\java\lang\ExceptionInInitializerError.html`

### Class Description

```java
public class
ExceptionInInitializerError

extends
LinkageError
```

Signals that an unexpected exception has occurred in a static initializer.
An

ExceptionInInitializerError

is thrown to indicate that an
exception occurred during evaluation of a static initializer or the
initializer for a static variable.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "saved throwable
object" that may be provided at construction time and accessed via
the

getException()

method is now known as the

cause

,
and may be accessed via the

Throwable.getCause()

method, as well
as the aforementioned "legacy method."

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ExceptionInInitializerError()

Constructs an

ExceptionInInitializerError

with

null

as its detail message string and with no saved
throwable object.
A detail message is a String that describes this particular exception.

---

#### public ExceptionInInitializerError​(
Throwable
thrown)

Constructs a new

ExceptionInInitializerError

class by
saving a reference to the

Throwable

object thrown for
later retrieval by the

getException()

method. The detail
message string is set to

null

.

**Parameters:**
- thrown

- The exception thrown

---

#### public ExceptionInInitializerError​(
String
s)

Constructs an ExceptionInInitializerError with the specified detail
message string. A detail message is a String that describes this
particular exception. The detail message string is saved for later
retrieval by the

Throwable.getMessage()

method. There is no
saved throwable object.

**Parameters:**
- s

- the detail message

---

### Method Details

#### public
Throwable
getException()

Returns the exception that occurred during a static initialization that
caused this error to be created.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:**
- the saved throwable object of this

ExceptionInInitializerError

, or

null

if this

ExceptionInInitializerError

has no saved
throwable object.

---

#### public
Throwable
getCause()

Returns the cause of this error (the exception that occurred
during a static initialization that caused this error to be created).

**Overrides:**
- getCause

in class

Throwable

**Returns:**
- the cause of this error or

null

if the
cause is nonexistent or unknown.

**Since:**
- 1.4

---

### Additional Sections

#### Class ExceptionInInitializerError

java.lang.Object

- java.lang.Throwable
- - java.lang.Error
- - java.lang.LinkageError
- - java.lang.ExceptionInInitializerError

java.lang.Throwable

- java.lang.Error
- - java.lang.LinkageError
- - java.lang.ExceptionInInitializerError

java.lang.Error

- java.lang.LinkageError
- - java.lang.ExceptionInInitializerError

java.lang.LinkageError

- java.lang.ExceptionInInitializerError

java.lang.ExceptionInInitializerError

**All Implemented Interfaces:** Serializable

```java
public class
ExceptionInInitializerError

extends
LinkageError
```

Signals that an unexpected exception has occurred in a static initializer.
An

ExceptionInInitializerError

is thrown to indicate that an
exception occurred during evaluation of a static initializer or the
initializer for a static variable.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "saved throwable
object" that may be provided at construction time and accessed via
the

getException()

method is now known as the

cause

,
and may be accessed via the

Throwable.getCause()

method, as well
as the aforementioned "legacy method."

**Since:** 1.1
**See Also:** Serialized Form

public class

ExceptionInInitializerError

extends

LinkageError

Signals that an unexpected exception has occurred in a static initializer.
An

ExceptionInInitializerError

is thrown to indicate that an
exception occurred during evaluation of a static initializer or the
initializer for a static variable.

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "saved throwable
object" that may be provided at construction time and accessed via
the

getException()

method is now known as the

cause

,
and may be accessed via the

Throwable.getCause()

method, as well
as the aforementioned "legacy method."

As of release 1.4, this exception has been retrofitted to conform to
the general purpose exception-chaining mechanism. The "saved throwable
object" that may be provided at construction time and accessed via
the

getException()

method is now known as the

cause

,
and may be accessed via the

Throwable.getCause()

method, as well
as the aforementioned "legacy method."

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ExceptionInInitializerError

()

Constructs an

ExceptionInInitializerError

with

null

as its detail message string and with no saved
throwable object.

ExceptionInInitializerError

​(

String

s)

Constructs an ExceptionInInitializerError with the specified detail
message string.

ExceptionInInitializerError

​(

Throwable

thrown)

Constructs a new

ExceptionInInitializerError

class by
saving a reference to the

Throwable

object thrown for
later retrieval by the

getException()

method.

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

Returns the cause of this error (the exception that occurred
during a static initialization that caused this error to be created).

Throwable

getException

()

Returns the exception that occurred during a static initialization that
caused this error to be created.

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

ExceptionInInitializerError

()

Constructs an

ExceptionInInitializerError

with

null

as its detail message string and with no saved
throwable object.

ExceptionInInitializerError

​(

String

s)

Constructs an ExceptionInInitializerError with the specified detail
message string.

ExceptionInInitializerError

​(

Throwable

thrown)

Constructs a new

ExceptionInInitializerError

class by
saving a reference to the

Throwable

object thrown for
later retrieval by the

getException()

method.

---

#### Constructor Summary

Constructs an

ExceptionInInitializerError

with

null

as its detail message string and with no saved
throwable object.

Constructs an ExceptionInInitializerError with the specified detail
message string.

Constructs a new

ExceptionInInitializerError

class by
saving a reference to the

Throwable

object thrown for
later retrieval by the

getException()

method.

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

Returns the cause of this error (the exception that occurred
during a static initialization that caused this error to be created).

Throwable

getException

()

Returns the exception that occurred during a static initialization that
caused this error to be created.

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

Returns the cause of this error (the exception that occurred
during a static initialization that caused this error to be created).

Returns the exception that occurred during a static initialization that
caused this error to be created.

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

- ExceptionInInitializerError

```java
public ExceptionInInitializerError()
```

Constructs an

ExceptionInInitializerError

with

null

as its detail message string and with no saved
throwable object.
A detail message is a String that describes this particular exception.

- ExceptionInInitializerError

```java
public ExceptionInInitializerError​(
Throwable
thrown)
```

Constructs a new

ExceptionInInitializerError

class by
saving a reference to the

Throwable

object thrown for
later retrieval by the

getException()

method. The detail
message string is set to

null

.

**Parameters:** thrown

- The exception thrown

- ExceptionInInitializerError

```java
public ExceptionInInitializerError​(
String
s)
```

Constructs an ExceptionInInitializerError with the specified detail
message string. A detail message is a String that describes this
particular exception. The detail message string is saved for later
retrieval by the

Throwable.getMessage()

method. There is no
saved throwable object.

**Parameters:** s

- the detail message

============ METHOD DETAIL ==========

- Method Detail

- getException

```java
public
Throwable
getException()
```

Returns the exception that occurred during a static initialization that
caused this error to be created.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:** the saved throwable object of this

ExceptionInInitializerError

, or

null

if this

ExceptionInInitializerError

has no saved
throwable object.

- getCause

```java
public
Throwable
getCause()
```

Returns the cause of this error (the exception that occurred
during a static initialization that caused this error to be created).

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this error or

null

if the
cause is nonexistent or unknown.
**Since:** 1.4

Constructor Detail

- ExceptionInInitializerError

```java
public ExceptionInInitializerError()
```

Constructs an

ExceptionInInitializerError

with

null

as its detail message string and with no saved
throwable object.
A detail message is a String that describes this particular exception.

- ExceptionInInitializerError

```java
public ExceptionInInitializerError​(
Throwable
thrown)
```

Constructs a new

ExceptionInInitializerError

class by
saving a reference to the

Throwable

object thrown for
later retrieval by the

getException()

method. The detail
message string is set to

null

.

**Parameters:** thrown

- The exception thrown

- ExceptionInInitializerError

```java
public ExceptionInInitializerError​(
String
s)
```

Constructs an ExceptionInInitializerError with the specified detail
message string. A detail message is a String that describes this
particular exception. The detail message string is saved for later
retrieval by the

Throwable.getMessage()

method. There is no
saved throwable object.

**Parameters:** s

- the detail message

---

#### Constructor Detail

ExceptionInInitializerError

```java
public ExceptionInInitializerError()
```

Constructs an

ExceptionInInitializerError

with

null

as its detail message string and with no saved
throwable object.
A detail message is a String that describes this particular exception.

---

#### ExceptionInInitializerError

public ExceptionInInitializerError()

Constructs an

ExceptionInInitializerError

with

null

as its detail message string and with no saved
throwable object.
A detail message is a String that describes this particular exception.

ExceptionInInitializerError

```java
public ExceptionInInitializerError​(
Throwable
thrown)
```

Constructs a new

ExceptionInInitializerError

class by
saving a reference to the

Throwable

object thrown for
later retrieval by the

getException()

method. The detail
message string is set to

null

.

**Parameters:** thrown

- The exception thrown

---

#### ExceptionInInitializerError

public ExceptionInInitializerError​(

Throwable

thrown)

Constructs a new

ExceptionInInitializerError

class by
saving a reference to the

Throwable

object thrown for
later retrieval by the

getException()

method. The detail
message string is set to

null

.

ExceptionInInitializerError

```java
public ExceptionInInitializerError​(
String
s)
```

Constructs an ExceptionInInitializerError with the specified detail
message string. A detail message is a String that describes this
particular exception. The detail message string is saved for later
retrieval by the

Throwable.getMessage()

method. There is no
saved throwable object.

**Parameters:** s

- the detail message

---

#### ExceptionInInitializerError

public ExceptionInInitializerError​(

String

s)

Constructs an ExceptionInInitializerError with the specified detail
message string. A detail message is a String that describes this
particular exception. The detail message string is saved for later
retrieval by the

Throwable.getMessage()

method. There is no
saved throwable object.

Method Detail

- getException

```java
public
Throwable
getException()
```

Returns the exception that occurred during a static initialization that
caused this error to be created.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:** the saved throwable object of this

ExceptionInInitializerError

, or

null

if this

ExceptionInInitializerError

has no saved
throwable object.

- getCause

```java
public
Throwable
getCause()
```

Returns the cause of this error (the exception that occurred
during a static initialization that caused this error to be created).

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this error or

null

if the
cause is nonexistent or unknown.
**Since:** 1.4

---

#### Method Detail

getException

```java
public
Throwable
getException()
```

Returns the exception that occurred during a static initialization that
caused this error to be created.

This method predates the general-purpose exception chaining facility.
The

Throwable.getCause()

method is now the preferred means of
obtaining this information.

**Returns:** the saved throwable object of this

ExceptionInInitializerError

, or

null

if this

ExceptionInInitializerError

has no saved
throwable object.

---

#### getException

public

Throwable

getException()

Returns the exception that occurred during a static initialization that
caused this error to be created.

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

Returns the cause of this error (the exception that occurred
during a static initialization that caused this error to be created).

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this error or

null

if the
cause is nonexistent or unknown.
**Since:** 1.4

---

#### getCause

public

Throwable

getCause()

Returns the cause of this error (the exception that occurred
during a static initialization that caused this error to be created).

---

