# Class RuntimeErrorException

**Source:** `java.management\javax\management\RuntimeErrorException.html`

### Class Description

```java
public class
RuntimeErrorException

extends
JMRuntimeException
```

When a

java.lang.Error

occurs in the agent it should be caught and
re-thrown as a

RuntimeErrorException

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public RuntimeErrorException​(
Error
e)

Default constructor.

**Parameters:**
- e

- the wrapped error.

---

#### public RuntimeErrorException​(
Error
e,

String
message)

Constructor that allows a specific error message to be specified.

**Parameters:**
- e

- the wrapped error.
- message

- the detail message.

---

### Method Details

#### public
Error
getTargetError()

Returns the actual

Error

thrown.

**Returns:**
- the wrapped

Error

.

---

#### public
Throwable
getCause()

Returns the actual

Error

thrown.

**Overrides:**
- getCause

in class

Throwable

**Returns:**
- the wrapped

Error

.

---

### Additional Sections

#### Class RuntimeErrorException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - javax.management.JMRuntimeException
- - javax.management.RuntimeErrorException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - javax.management.JMRuntimeException
- - javax.management.RuntimeErrorException

java.lang.Exception

- java.lang.RuntimeException
- - javax.management.JMRuntimeException
- - javax.management.RuntimeErrorException

java.lang.RuntimeException

- javax.management.JMRuntimeException
- - javax.management.RuntimeErrorException

javax.management.JMRuntimeException

- javax.management.RuntimeErrorException

javax.management.RuntimeErrorException

**All Implemented Interfaces:** Serializable

```java
public class
RuntimeErrorException

extends
JMRuntimeException
```

When a

java.lang.Error

occurs in the agent it should be caught and
re-thrown as a

RuntimeErrorException

.

**Since:** 1.5
**See Also:** Serialized Form

public class

RuntimeErrorException

extends

JMRuntimeException

When a

java.lang.Error

occurs in the agent it should be caught and
re-thrown as a

RuntimeErrorException

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RuntimeErrorException

​(

Error

e)

Default constructor.

RuntimeErrorException

​(

Error

e,

String

message)

Constructor that allows a specific error message to be specified.

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

Returns the actual

Error

thrown.

Error

getTargetError

()

Returns the actual

Error

thrown.

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

RuntimeErrorException

​(

Error

e)

Default constructor.

RuntimeErrorException

​(

Error

e,

String

message)

Constructor that allows a specific error message to be specified.

---

#### Constructor Summary

Default constructor.

Constructor that allows a specific error message to be specified.

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

Returns the actual

Error

thrown.

Error

getTargetError

()

Returns the actual

Error

thrown.

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

Returns the actual

Error

thrown.

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

- RuntimeErrorException

```java
public RuntimeErrorException​(
Error
e)
```

Default constructor.

**Parameters:** e

- the wrapped error.

- RuntimeErrorException

```java
public RuntimeErrorException​(
Error
e,

String
message)
```

Constructor that allows a specific error message to be specified.

**Parameters:** e

- the wrapped error.
**Parameters:** message

- the detail message.

============ METHOD DETAIL ==========

- Method Detail

- getTargetError

```java
public
Error
getTargetError()
```

Returns the actual

Error

thrown.

**Returns:** the wrapped

Error

.

- getCause

```java
public
Throwable
getCause()
```

Returns the actual

Error

thrown.

**Overrides:** getCause

in class

Throwable
**Returns:** the wrapped

Error

.

Constructor Detail

- RuntimeErrorException

```java
public RuntimeErrorException​(
Error
e)
```

Default constructor.

**Parameters:** e

- the wrapped error.

- RuntimeErrorException

```java
public RuntimeErrorException​(
Error
e,

String
message)
```

Constructor that allows a specific error message to be specified.

**Parameters:** e

- the wrapped error.
**Parameters:** message

- the detail message.

---

#### Constructor Detail

RuntimeErrorException

```java
public RuntimeErrorException​(
Error
e)
```

Default constructor.

**Parameters:** e

- the wrapped error.

---

#### RuntimeErrorException

public RuntimeErrorException​(

Error

e)

Default constructor.

RuntimeErrorException

```java
public RuntimeErrorException​(
Error
e,

String
message)
```

Constructor that allows a specific error message to be specified.

**Parameters:** e

- the wrapped error.
**Parameters:** message

- the detail message.

---

#### RuntimeErrorException

public RuntimeErrorException​(

Error

e,

String

message)

Constructor that allows a specific error message to be specified.

Method Detail

- getTargetError

```java
public
Error
getTargetError()
```

Returns the actual

Error

thrown.

**Returns:** the wrapped

Error

.

- getCause

```java
public
Throwable
getCause()
```

Returns the actual

Error

thrown.

**Overrides:** getCause

in class

Throwable
**Returns:** the wrapped

Error

.

---

#### Method Detail

getTargetError

```java
public
Error
getTargetError()
```

Returns the actual

Error

thrown.

**Returns:** the wrapped

Error

.

---

#### getTargetError

public

Error

getTargetError()

Returns the actual

Error

thrown.

getCause

```java
public
Throwable
getCause()
```

Returns the actual

Error

thrown.

**Overrides:** getCause

in class

Throwable
**Returns:** the wrapped

Error

.

---

#### getCause

public

Throwable

getCause()

Returns the actual

Error

thrown.

---

