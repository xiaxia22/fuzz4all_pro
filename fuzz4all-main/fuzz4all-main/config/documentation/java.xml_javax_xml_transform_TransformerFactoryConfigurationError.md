# Class TransformerFactoryConfigurationError

**Source:** `java.xml\javax\xml\transform\TransformerFactoryConfigurationError.html`

### Class Description

```java
public class
TransformerFactoryConfigurationError

extends
Error
```

Thrown when a problem with configuration with the Transformer Factories
exists. This error will typically be thrown when the class of a
transformation factory specified in the system properties cannot be found
or instantiated.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public TransformerFactoryConfigurationError()

Create a new

TransformerFactoryConfigurationError

with no
detail message.

---

#### public TransformerFactoryConfigurationError​(
String
msg)

Create a new

TransformerFactoryConfigurationError

with
the

String

specified as an error message.

**Parameters:**
- msg

- The error message for the exception.

---

#### public TransformerFactoryConfigurationError​(
Exception
e)

Create a new

TransformerFactoryConfigurationError

with a
given

Exception

base cause of the error.

**Parameters:**
- e

- The exception to be encapsulated in a
TransformerFactoryConfigurationError.

---

#### public TransformerFactoryConfigurationError​(
Exception
e,

String
msg)

Create a new

TransformerFactoryConfigurationError

with the
given

Exception

base cause and detail message.

**Parameters:**
- e

- The exception to be encapsulated in a
TransformerFactoryConfigurationError
- msg

- The detail message.

---

### Method Details

#### public
String
getMessage()

Return the message (if any) for this error . If there is no
message for the exception and there is an encapsulated
exception then the message of that exception will be returned.

**Overrides:**
- getMessage

in class

Throwable

**Returns:**
- The error message.

---

#### public
Exception
getException()

Return the actual exception (if any) that caused this exception to
be raised.

**Returns:**
- The encapsulated exception, or null if there is none.

---

#### public
Throwable
getCause()

use the exception chaining mechanism of JDK1.4

**Overrides:**
- getCause

in class

Throwable

**Returns:**
- the cause of this throwable or

null

if the
cause is nonexistent or unknown.

---

### Additional Sections

#### Class TransformerFactoryConfigurationError

java.lang.Object

- java.lang.Throwable
- - java.lang.Error
- - javax.xml.transform.TransformerFactoryConfigurationError

java.lang.Throwable

- java.lang.Error
- - javax.xml.transform.TransformerFactoryConfigurationError

java.lang.Error

- javax.xml.transform.TransformerFactoryConfigurationError

javax.xml.transform.TransformerFactoryConfigurationError

**All Implemented Interfaces:** Serializable

```java
public class
TransformerFactoryConfigurationError

extends
Error
```

Thrown when a problem with configuration with the Transformer Factories
exists. This error will typically be thrown when the class of a
transformation factory specified in the system properties cannot be found
or instantiated.

**Since:** 1.4
**See Also:** Serialized Form

public class

TransformerFactoryConfigurationError

extends

Error

Thrown when a problem with configuration with the Transformer Factories
exists. This error will typically be thrown when the class of a
transformation factory specified in the system properties cannot be found
or instantiated.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TransformerFactoryConfigurationError

()

Create a new

TransformerFactoryConfigurationError

with no
detail message.

TransformerFactoryConfigurationError

​(

Exception

e)

Create a new

TransformerFactoryConfigurationError

with a
given

Exception

base cause of the error.

TransformerFactoryConfigurationError

​(

Exception

e,

String

msg)

Create a new

TransformerFactoryConfigurationError

with the
given

Exception

base cause and detail message.

TransformerFactoryConfigurationError

​(

String

msg)

Create a new

TransformerFactoryConfigurationError

with
the

String

specified as an error message.

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

use the exception chaining mechanism of JDK1.4

Exception

getException

()

Return the actual exception (if any) that caused this exception to
be raised.

String

getMessage

()

Return the message (if any) for this error .

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

Constructor Summary

Constructors

Constructor

Description

TransformerFactoryConfigurationError

()

Create a new

TransformerFactoryConfigurationError

with no
detail message.

TransformerFactoryConfigurationError

​(

Exception

e)

Create a new

TransformerFactoryConfigurationError

with a
given

Exception

base cause of the error.

TransformerFactoryConfigurationError

​(

Exception

e,

String

msg)

Create a new

TransformerFactoryConfigurationError

with the
given

Exception

base cause and detail message.

TransformerFactoryConfigurationError

​(

String

msg)

Create a new

TransformerFactoryConfigurationError

with
the

String

specified as an error message.

---

#### Constructor Summary

Create a new

TransformerFactoryConfigurationError

with no
detail message.

Create a new

TransformerFactoryConfigurationError

with a
given

Exception

base cause of the error.

Create a new

TransformerFactoryConfigurationError

with the
given

Exception

base cause and detail message.

Create a new

TransformerFactoryConfigurationError

with
the

String

specified as an error message.

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

use the exception chaining mechanism of JDK1.4

Exception

getException

()

Return the actual exception (if any) that caused this exception to
be raised.

String

getMessage

()

Return the message (if any) for this error .

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

use the exception chaining mechanism of JDK1.4

Return the actual exception (if any) that caused this exception to
be raised.

Return the message (if any) for this error .

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- TransformerFactoryConfigurationError

```java
public TransformerFactoryConfigurationError()
```

Create a new

TransformerFactoryConfigurationError

with no
detail message.

- TransformerFactoryConfigurationError

```java
public TransformerFactoryConfigurationError​(
String
msg)
```

Create a new

TransformerFactoryConfigurationError

with
the

String

specified as an error message.

**Parameters:** msg

- The error message for the exception.

- TransformerFactoryConfigurationError

```java
public TransformerFactoryConfigurationError​(
Exception
e)
```

Create a new

TransformerFactoryConfigurationError

with a
given

Exception

base cause of the error.

**Parameters:** e

- The exception to be encapsulated in a
TransformerFactoryConfigurationError.

- TransformerFactoryConfigurationError

```java
public TransformerFactoryConfigurationError​(
Exception
e,

String
msg)
```

Create a new

TransformerFactoryConfigurationError

with the
given

Exception

base cause and detail message.

**Parameters:** e

- The exception to be encapsulated in a
TransformerFactoryConfigurationError
**Parameters:** msg

- The detail message.

============ METHOD DETAIL ==========

- Method Detail

- getMessage

```java
public
String
getMessage()
```

Return the message (if any) for this error . If there is no
message for the exception and there is an encapsulated
exception then the message of that exception will be returned.

**Overrides:** getMessage

in class

Throwable
**Returns:** The error message.

- getException

```java
public
Exception
getException()
```

Return the actual exception (if any) that caused this exception to
be raised.

**Returns:** The encapsulated exception, or null if there is none.

- getCause

```java
public
Throwable
getCause()
```

use the exception chaining mechanism of JDK1.4

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this throwable or

null

if the
cause is nonexistent or unknown.

Constructor Detail

- TransformerFactoryConfigurationError

```java
public TransformerFactoryConfigurationError()
```

Create a new

TransformerFactoryConfigurationError

with no
detail message.

- TransformerFactoryConfigurationError

```java
public TransformerFactoryConfigurationError​(
String
msg)
```

Create a new

TransformerFactoryConfigurationError

with
the

String

specified as an error message.

**Parameters:** msg

- The error message for the exception.

- TransformerFactoryConfigurationError

```java
public TransformerFactoryConfigurationError​(
Exception
e)
```

Create a new

TransformerFactoryConfigurationError

with a
given

Exception

base cause of the error.

**Parameters:** e

- The exception to be encapsulated in a
TransformerFactoryConfigurationError.

- TransformerFactoryConfigurationError

```java
public TransformerFactoryConfigurationError​(
Exception
e,

String
msg)
```

Create a new

TransformerFactoryConfigurationError

with the
given

Exception

base cause and detail message.

**Parameters:** e

- The exception to be encapsulated in a
TransformerFactoryConfigurationError
**Parameters:** msg

- The detail message.

---

#### Constructor Detail

TransformerFactoryConfigurationError

```java
public TransformerFactoryConfigurationError()
```

Create a new

TransformerFactoryConfigurationError

with no
detail message.

---

#### TransformerFactoryConfigurationError

public TransformerFactoryConfigurationError()

Create a new

TransformerFactoryConfigurationError

with no
detail message.

TransformerFactoryConfigurationError

```java
public TransformerFactoryConfigurationError​(
String
msg)
```

Create a new

TransformerFactoryConfigurationError

with
the

String

specified as an error message.

**Parameters:** msg

- The error message for the exception.

---

#### TransformerFactoryConfigurationError

public TransformerFactoryConfigurationError​(

String

msg)

Create a new

TransformerFactoryConfigurationError

with
the

String

specified as an error message.

TransformerFactoryConfigurationError

```java
public TransformerFactoryConfigurationError​(
Exception
e)
```

Create a new

TransformerFactoryConfigurationError

with a
given

Exception

base cause of the error.

**Parameters:** e

- The exception to be encapsulated in a
TransformerFactoryConfigurationError.

---

#### TransformerFactoryConfigurationError

public TransformerFactoryConfigurationError​(

Exception

e)

Create a new

TransformerFactoryConfigurationError

with a
given

Exception

base cause of the error.

TransformerFactoryConfigurationError

```java
public TransformerFactoryConfigurationError​(
Exception
e,

String
msg)
```

Create a new

TransformerFactoryConfigurationError

with the
given

Exception

base cause and detail message.

**Parameters:** e

- The exception to be encapsulated in a
TransformerFactoryConfigurationError
**Parameters:** msg

- The detail message.

---

#### TransformerFactoryConfigurationError

public TransformerFactoryConfigurationError​(

Exception

e,

String

msg)

Create a new

TransformerFactoryConfigurationError

with the
given

Exception

base cause and detail message.

Method Detail

- getMessage

```java
public
String
getMessage()
```

Return the message (if any) for this error . If there is no
message for the exception and there is an encapsulated
exception then the message of that exception will be returned.

**Overrides:** getMessage

in class

Throwable
**Returns:** The error message.

- getException

```java
public
Exception
getException()
```

Return the actual exception (if any) that caused this exception to
be raised.

**Returns:** The encapsulated exception, or null if there is none.

- getCause

```java
public
Throwable
getCause()
```

use the exception chaining mechanism of JDK1.4

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this throwable or

null

if the
cause is nonexistent or unknown.

---

#### Method Detail

getMessage

```java
public
String
getMessage()
```

Return the message (if any) for this error . If there is no
message for the exception and there is an encapsulated
exception then the message of that exception will be returned.

**Overrides:** getMessage

in class

Throwable
**Returns:** The error message.

---

#### getMessage

public

String

getMessage()

Return the message (if any) for this error . If there is no
message for the exception and there is an encapsulated
exception then the message of that exception will be returned.

getException

```java
public
Exception
getException()
```

Return the actual exception (if any) that caused this exception to
be raised.

**Returns:** The encapsulated exception, or null if there is none.

---

#### getException

public

Exception

getException()

Return the actual exception (if any) that caused this exception to
be raised.

getCause

```java
public
Throwable
getCause()
```

use the exception chaining mechanism of JDK1.4

**Overrides:** getCause

in class

Throwable
**Returns:** the cause of this throwable or

null

if the
cause is nonexistent or unknown.

---

#### getCause

public

Throwable

getCause()

use the exception chaining mechanism of JDK1.4

---

