# Class SaslException

**Source:** `java.security.sasl\javax\security\sasl\SaslException.html`

### Class Description

```java
public class
SaslException

extends
IOException
```

This class represents an error that has occurred when using SASL.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public SaslException()

Constructs a new instance of

SaslException

.
The root exception and the detailed message are null.

---

#### public SaslException​(
String
detail)

Constructs a new instance of

SaslException

with a detailed message.
The root exception is null.

**Parameters:**
- detail

- A possibly null string containing details of the exception.

**See Also:**
- Throwable.getMessage()

---

#### public SaslException​(
String
detail,

Throwable
ex)

Constructs a new instance of

SaslException

with a detailed message
and a root exception.
For example, a SaslException might result from a problem with
the callback handler, which might throw a NoSuchCallbackException if
it does not support the requested callback, or throw an IOException
if it had problems obtaining data for the callback. The
SaslException's root exception would be then be the exception thrown
by the callback handler.

**Parameters:**
- detail

- A possibly null string containing details of the exception.
- ex

- A possibly null root exception that caused this exception.

**See Also:**
- Throwable.getMessage()

,

Throwable.getCause()

---

### Method Details

#### public
String
toString()

Returns the string representation of this exception.
The string representation contains
this exception's class name, its detailed message, and if
it has a root exception, the string representation of the root
exception. This string representation
is meant for debugging and not meant to be interpreted
programmatically.

**Overrides:**
- toString

in class

Throwable

**Returns:**
- The non-null string representation of this exception.

**See Also:**
- Throwable.getMessage()

---

### Additional Sections

#### Class SaslException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - javax.security.sasl.SaslException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - javax.security.sasl.SaslException

java.lang.Exception

- java.io.IOException
- - javax.security.sasl.SaslException

java.io.IOException

- javax.security.sasl.SaslException

javax.security.sasl.SaslException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** AuthenticationException

```java
public class
SaslException

extends
IOException
```

This class represents an error that has occurred when using SASL.

**Since:** 1.5
**See Also:** Serialized Form

public class

SaslException

extends

IOException

This class represents an error that has occurred when using SASL.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SaslException

()

Constructs a new instance of

SaslException

.

SaslException

​(

String

detail)

Constructs a new instance of

SaslException

with a detailed message.

SaslException

​(

String

detail,

Throwable

ex)

Constructs a new instance of

SaslException

with a detailed message
and a root exception.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

toString

()

Returns the string representation of this exception.

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

SaslException

()

Constructs a new instance of

SaslException

.

SaslException

​(

String

detail)

Constructs a new instance of

SaslException

with a detailed message.

SaslException

​(

String

detail,

Throwable

ex)

Constructs a new instance of

SaslException

with a detailed message
and a root exception.

---

#### Constructor Summary

Constructs a new instance of

SaslException

.

Constructs a new instance of

SaslException

with a detailed message.

Constructs a new instance of

SaslException

with a detailed message
and a root exception.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

toString

()

Returns the string representation of this exception.

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

Returns the string representation of this exception.

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

- SaslException

```java
public SaslException()
```

Constructs a new instance of

SaslException

.
The root exception and the detailed message are null.

- SaslException

```java
public SaslException​(
String
detail)
```

Constructs a new instance of

SaslException

with a detailed message.
The root exception is null.

**Parameters:** detail

- A possibly null string containing details of the exception.
**See Also:** Throwable.getMessage()

- SaslException

```java
public SaslException​(
String
detail,

Throwable
ex)
```

Constructs a new instance of

SaslException

with a detailed message
and a root exception.
For example, a SaslException might result from a problem with
the callback handler, which might throw a NoSuchCallbackException if
it does not support the requested callback, or throw an IOException
if it had problems obtaining data for the callback. The
SaslException's root exception would be then be the exception thrown
by the callback handler.

**Parameters:** detail

- A possibly null string containing details of the exception.
**Parameters:** ex

- A possibly null root exception that caused this exception.
**See Also:** Throwable.getMessage()

,

Throwable.getCause()

============ METHOD DETAIL ==========

- Method Detail

- toString

```java
public
String
toString()
```

Returns the string representation of this exception.
The string representation contains
this exception's class name, its detailed message, and if
it has a root exception, the string representation of the root
exception. This string representation
is meant for debugging and not meant to be interpreted
programmatically.

**Overrides:** toString

in class

Throwable
**Returns:** The non-null string representation of this exception.
**See Also:** Throwable.getMessage()

Constructor Detail

- SaslException

```java
public SaslException()
```

Constructs a new instance of

SaslException

.
The root exception and the detailed message are null.

- SaslException

```java
public SaslException​(
String
detail)
```

Constructs a new instance of

SaslException

with a detailed message.
The root exception is null.

**Parameters:** detail

- A possibly null string containing details of the exception.
**See Also:** Throwable.getMessage()

- SaslException

```java
public SaslException​(
String
detail,

Throwable
ex)
```

Constructs a new instance of

SaslException

with a detailed message
and a root exception.
For example, a SaslException might result from a problem with
the callback handler, which might throw a NoSuchCallbackException if
it does not support the requested callback, or throw an IOException
if it had problems obtaining data for the callback. The
SaslException's root exception would be then be the exception thrown
by the callback handler.

**Parameters:** detail

- A possibly null string containing details of the exception.
**Parameters:** ex

- A possibly null root exception that caused this exception.
**See Also:** Throwable.getMessage()

,

Throwable.getCause()

---

#### Constructor Detail

SaslException

```java
public SaslException()
```

Constructs a new instance of

SaslException

.
The root exception and the detailed message are null.

---

#### SaslException

public SaslException()

Constructs a new instance of

SaslException

.
The root exception and the detailed message are null.

SaslException

```java
public SaslException​(
String
detail)
```

Constructs a new instance of

SaslException

with a detailed message.
The root exception is null.

**Parameters:** detail

- A possibly null string containing details of the exception.
**See Also:** Throwable.getMessage()

---

#### SaslException

public SaslException​(

String

detail)

Constructs a new instance of

SaslException

with a detailed message.
The root exception is null.

SaslException

```java
public SaslException​(
String
detail,

Throwable
ex)
```

Constructs a new instance of

SaslException

with a detailed message
and a root exception.
For example, a SaslException might result from a problem with
the callback handler, which might throw a NoSuchCallbackException if
it does not support the requested callback, or throw an IOException
if it had problems obtaining data for the callback. The
SaslException's root exception would be then be the exception thrown
by the callback handler.

**Parameters:** detail

- A possibly null string containing details of the exception.
**Parameters:** ex

- A possibly null root exception that caused this exception.
**See Also:** Throwable.getMessage()

,

Throwable.getCause()

---

#### SaslException

public SaslException​(

String

detail,

Throwable

ex)

Constructs a new instance of

SaslException

with a detailed message
and a root exception.
For example, a SaslException might result from a problem with
the callback handler, which might throw a NoSuchCallbackException if
it does not support the requested callback, or throw an IOException
if it had problems obtaining data for the callback. The
SaslException's root exception would be then be the exception thrown
by the callback handler.

Method Detail

- toString

```java
public
String
toString()
```

Returns the string representation of this exception.
The string representation contains
this exception's class name, its detailed message, and if
it has a root exception, the string representation of the root
exception. This string representation
is meant for debugging and not meant to be interpreted
programmatically.

**Overrides:** toString

in class

Throwable
**Returns:** The non-null string representation of this exception.
**See Also:** Throwable.getMessage()

---

#### Method Detail

toString

```java
public
String
toString()
```

Returns the string representation of this exception.
The string representation contains
this exception's class name, its detailed message, and if
it has a root exception, the string representation of the root
exception. This string representation
is meant for debugging and not meant to be interpreted
programmatically.

**Overrides:** toString

in class

Throwable
**Returns:** The non-null string representation of this exception.
**See Also:** Throwable.getMessage()

---

#### toString

public

String

toString()

Returns the string representation of this exception.
The string representation contains
this exception's class name, its detailed message, and if
it has a root exception, the string representation of the root
exception. This string representation
is meant for debugging and not meant to be interpreted
programmatically.

---

