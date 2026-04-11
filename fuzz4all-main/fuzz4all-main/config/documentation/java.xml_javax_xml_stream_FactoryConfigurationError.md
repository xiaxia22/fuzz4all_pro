# Class FactoryConfigurationError

**Source:** `java.xml\javax\xml\stream\FactoryConfigurationError.html`

### Class Description

```java
public class
FactoryConfigurationError

extends
Error
```

An error class for reporting factory configuration errors.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public FactoryConfigurationError()

Default constructor

---

#### public FactoryConfigurationError​(
Exception
e)

Construct an exception with a nested inner exception

**Parameters:**
- e

- the exception to nest

---

#### public FactoryConfigurationError​(
Exception
e,

String
msg)

Construct an exception with a nested inner exception
and a message

**Parameters:**
- e

- the exception to nest
- msg

- the message to report

---

#### public FactoryConfigurationError​(
String
msg,

Exception
e)

Construct an exception with a nested inner exception
and a message

**Parameters:**
- msg

- the message to report
- e

- the exception to nest

---

#### public FactoryConfigurationError​(
String
msg)

Construct an exception with associated message

**Parameters:**
- msg

- the message to report

---

### Method Details

#### public
Exception
getException()

Return the nested exception (if any)

**Returns:**
- the nested exception or null

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

#### public
String
getMessage()

Report the message associated with this error

**Overrides:**
- getMessage

in class

Throwable

**Returns:**
- the string value of the message

---

### Additional Sections

#### Class FactoryConfigurationError

java.lang.Object

- java.lang.Throwable
- - java.lang.Error
- - javax.xml.stream.FactoryConfigurationError

java.lang.Throwable

- java.lang.Error
- - javax.xml.stream.FactoryConfigurationError

java.lang.Error

- javax.xml.stream.FactoryConfigurationError

javax.xml.stream.FactoryConfigurationError

**All Implemented Interfaces:** Serializable

```java
public class
FactoryConfigurationError

extends
Error
```

An error class for reporting factory configuration errors.

**Since:** 1.6
**See Also:** Serialized Form

public class

FactoryConfigurationError

extends

Error

An error class for reporting factory configuration errors.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FactoryConfigurationError

()

Default constructor

FactoryConfigurationError

​(

Exception

e)

Construct an exception with a nested inner exception

FactoryConfigurationError

​(

Exception

e,

String

msg)

Construct an exception with a nested inner exception
and a message

FactoryConfigurationError

​(

String

msg)

Construct an exception with associated message

FactoryConfigurationError

​(

String

msg,

Exception

e)

Construct an exception with a nested inner exception
and a message

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

Return the nested exception (if any)

String

getMessage

()

Report the message associated with this error

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

FactoryConfigurationError

()

Default constructor

FactoryConfigurationError

​(

Exception

e)

Construct an exception with a nested inner exception

FactoryConfigurationError

​(

Exception

e,

String

msg)

Construct an exception with a nested inner exception
and a message

FactoryConfigurationError

​(

String

msg)

Construct an exception with associated message

FactoryConfigurationError

​(

String

msg,

Exception

e)

Construct an exception with a nested inner exception
and a message

---

#### Constructor Summary

Default constructor

Construct an exception with a nested inner exception

Construct an exception with a nested inner exception
and a message

Construct an exception with associated message

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

Return the nested exception (if any)

String

getMessage

()

Report the message associated with this error

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

Return the nested exception (if any)

Report the message associated with this error

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

- FactoryConfigurationError

```java
public FactoryConfigurationError()
```

Default constructor

- FactoryConfigurationError

```java
public FactoryConfigurationError​(
Exception
e)
```

Construct an exception with a nested inner exception

**Parameters:** e

- the exception to nest

- FactoryConfigurationError

```java
public FactoryConfigurationError​(
Exception
e,

String
msg)
```

Construct an exception with a nested inner exception
and a message

**Parameters:** e

- the exception to nest
**Parameters:** msg

- the message to report

- FactoryConfigurationError

```java
public FactoryConfigurationError​(
String
msg,

Exception
e)
```

Construct an exception with a nested inner exception
and a message

**Parameters:** msg

- the message to report
**Parameters:** e

- the exception to nest

- FactoryConfigurationError

```java
public FactoryConfigurationError​(
String
msg)
```

Construct an exception with associated message

**Parameters:** msg

- the message to report

============ METHOD DETAIL ==========

- Method Detail

- getException

```java
public
Exception
getException()
```

Return the nested exception (if any)

**Returns:** the nested exception or null

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

- getMessage

```java
public
String
getMessage()
```

Report the message associated with this error

**Overrides:** getMessage

in class

Throwable
**Returns:** the string value of the message

Constructor Detail

- FactoryConfigurationError

```java
public FactoryConfigurationError()
```

Default constructor

- FactoryConfigurationError

```java
public FactoryConfigurationError​(
Exception
e)
```

Construct an exception with a nested inner exception

**Parameters:** e

- the exception to nest

- FactoryConfigurationError

```java
public FactoryConfigurationError​(
Exception
e,

String
msg)
```

Construct an exception with a nested inner exception
and a message

**Parameters:** e

- the exception to nest
**Parameters:** msg

- the message to report

- FactoryConfigurationError

```java
public FactoryConfigurationError​(
String
msg,

Exception
e)
```

Construct an exception with a nested inner exception
and a message

**Parameters:** msg

- the message to report
**Parameters:** e

- the exception to nest

- FactoryConfigurationError

```java
public FactoryConfigurationError​(
String
msg)
```

Construct an exception with associated message

**Parameters:** msg

- the message to report

---

#### Constructor Detail

FactoryConfigurationError

```java
public FactoryConfigurationError()
```

Default constructor

---

#### FactoryConfigurationError

public FactoryConfigurationError()

Default constructor

FactoryConfigurationError

```java
public FactoryConfigurationError​(
Exception
e)
```

Construct an exception with a nested inner exception

**Parameters:** e

- the exception to nest

---

#### FactoryConfigurationError

public FactoryConfigurationError​(

Exception

e)

Construct an exception with a nested inner exception

FactoryConfigurationError

```java
public FactoryConfigurationError​(
Exception
e,

String
msg)
```

Construct an exception with a nested inner exception
and a message

**Parameters:** e

- the exception to nest
**Parameters:** msg

- the message to report

---

#### FactoryConfigurationError

public FactoryConfigurationError​(

Exception

e,

String

msg)

Construct an exception with a nested inner exception
and a message

FactoryConfigurationError

```java
public FactoryConfigurationError​(
String
msg,

Exception
e)
```

Construct an exception with a nested inner exception
and a message

**Parameters:** msg

- the message to report
**Parameters:** e

- the exception to nest

---

#### FactoryConfigurationError

public FactoryConfigurationError​(

String

msg,

Exception

e)

Construct an exception with a nested inner exception
and a message

FactoryConfigurationError

```java
public FactoryConfigurationError​(
String
msg)
```

Construct an exception with associated message

**Parameters:** msg

- the message to report

---

#### FactoryConfigurationError

public FactoryConfigurationError​(

String

msg)

Construct an exception with associated message

Method Detail

- getException

```java
public
Exception
getException()
```

Return the nested exception (if any)

**Returns:** the nested exception or null

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

- getMessage

```java
public
String
getMessage()
```

Report the message associated with this error

**Overrides:** getMessage

in class

Throwable
**Returns:** the string value of the message

---

#### Method Detail

getException

```java
public
Exception
getException()
```

Return the nested exception (if any)

**Returns:** the nested exception or null

---

#### getException

public

Exception

getException()

Return the nested exception (if any)

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

getMessage

```java
public
String
getMessage()
```

Report the message associated with this error

**Overrides:** getMessage

in class

Throwable
**Returns:** the string value of the message

---

#### getMessage

public

String

getMessage()

Report the message associated with this error

---

