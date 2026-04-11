# Class RuntimeOperationsException

**Source:** `java.management\javax\management\RuntimeOperationsException.html`

### Class Description

```java
public class
RuntimeOperationsException

extends
JMRuntimeException
```

Represents runtime exceptions thrown in the agent when performing operations on MBeans.
It wraps the actual

java.lang.RuntimeException

thrown.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public RuntimeOperationsException​(
RuntimeException
e)

Creates a

RuntimeOperationsException

that wraps the actual

java.lang.RuntimeException

.

**Parameters:**
- e

- the wrapped exception.

---

#### public RuntimeOperationsException​(
RuntimeException
e,

String
message)

Creates a

RuntimeOperationsException

that wraps the actual

java.lang.RuntimeException

with a detailed message.

**Parameters:**
- e

- the wrapped exception.
- message

- the detail message.

---

### Method Details

#### public
RuntimeException
getTargetException()

Returns the actual

RuntimeException

thrown.

**Returns:**
- the wrapped

RuntimeException

.

---

#### public
Throwable
getCause()

Returns the actual

RuntimeException

thrown.

**Overrides:**
- getCause

in class

Throwable

**Returns:**
- the wrapped

RuntimeException

.

---

### Additional Sections

#### Class RuntimeOperationsException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - javax.management.JMRuntimeException
- - javax.management.RuntimeOperationsException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - javax.management.JMRuntimeException
- - javax.management.RuntimeOperationsException

java.lang.Exception

- java.lang.RuntimeException
- - javax.management.JMRuntimeException
- - javax.management.RuntimeOperationsException

java.lang.RuntimeException

- javax.management.JMRuntimeException
- - javax.management.RuntimeOperationsException

javax.management.JMRuntimeException

- javax.management.RuntimeOperationsException

javax.management.RuntimeOperationsException

**All Implemented Interfaces:** Serializable

```java
public class
RuntimeOperationsException

extends
JMRuntimeException
```

Represents runtime exceptions thrown in the agent when performing operations on MBeans.
It wraps the actual

java.lang.RuntimeException

thrown.

**Since:** 1.5
**See Also:** Serialized Form

public class

RuntimeOperationsException

extends

JMRuntimeException

Represents runtime exceptions thrown in the agent when performing operations on MBeans.
It wraps the actual

java.lang.RuntimeException

thrown.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RuntimeOperationsException

​(

RuntimeException

e)

Creates a

RuntimeOperationsException

that wraps the actual

java.lang.RuntimeException

.

RuntimeOperationsException

​(

RuntimeException

e,

String

message)

Creates a

RuntimeOperationsException

that wraps the actual

java.lang.RuntimeException

with a detailed message.

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

RuntimeException

thrown.

RuntimeException

getTargetException

()

Returns the actual

RuntimeException

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

RuntimeOperationsException

​(

RuntimeException

e)

Creates a

RuntimeOperationsException

that wraps the actual

java.lang.RuntimeException

.

RuntimeOperationsException

​(

RuntimeException

e,

String

message)

Creates a

RuntimeOperationsException

that wraps the actual

java.lang.RuntimeException

with a detailed message.

---

#### Constructor Summary

Creates a

RuntimeOperationsException

that wraps the actual

java.lang.RuntimeException

.

Creates a

RuntimeOperationsException

that wraps the actual

java.lang.RuntimeException

with a detailed message.

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

RuntimeException

thrown.

RuntimeException

getTargetException

()

Returns the actual

RuntimeException

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

RuntimeException

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

- RuntimeOperationsException

```java
public RuntimeOperationsException​(
RuntimeException
e)
```

Creates a

RuntimeOperationsException

that wraps the actual

java.lang.RuntimeException

.

**Parameters:** e

- the wrapped exception.

- RuntimeOperationsException

```java
public RuntimeOperationsException​(
RuntimeException
e,

String
message)
```

Creates a

RuntimeOperationsException

that wraps the actual

java.lang.RuntimeException

with a detailed message.

**Parameters:** e

- the wrapped exception.
**Parameters:** message

- the detail message.

============ METHOD DETAIL ==========

- Method Detail

- getTargetException

```java
public
RuntimeException
getTargetException()
```

Returns the actual

RuntimeException

thrown.

**Returns:** the wrapped

RuntimeException

.

- getCause

```java
public
Throwable
getCause()
```

Returns the actual

RuntimeException

thrown.

**Overrides:** getCause

in class

Throwable
**Returns:** the wrapped

RuntimeException

.

Constructor Detail

- RuntimeOperationsException

```java
public RuntimeOperationsException​(
RuntimeException
e)
```

Creates a

RuntimeOperationsException

that wraps the actual

java.lang.RuntimeException

.

**Parameters:** e

- the wrapped exception.

- RuntimeOperationsException

```java
public RuntimeOperationsException​(
RuntimeException
e,

String
message)
```

Creates a

RuntimeOperationsException

that wraps the actual

java.lang.RuntimeException

with a detailed message.

**Parameters:** e

- the wrapped exception.
**Parameters:** message

- the detail message.

---

#### Constructor Detail

RuntimeOperationsException

```java
public RuntimeOperationsException​(
RuntimeException
e)
```

Creates a

RuntimeOperationsException

that wraps the actual

java.lang.RuntimeException

.

**Parameters:** e

- the wrapped exception.

---

#### RuntimeOperationsException

public RuntimeOperationsException​(

RuntimeException

e)

Creates a

RuntimeOperationsException

that wraps the actual

java.lang.RuntimeException

.

RuntimeOperationsException

```java
public RuntimeOperationsException​(
RuntimeException
e,

String
message)
```

Creates a

RuntimeOperationsException

that wraps the actual

java.lang.RuntimeException

with a detailed message.

**Parameters:** e

- the wrapped exception.
**Parameters:** message

- the detail message.

---

#### RuntimeOperationsException

public RuntimeOperationsException​(

RuntimeException

e,

String

message)

Creates a

RuntimeOperationsException

that wraps the actual

java.lang.RuntimeException

with a detailed message.

Method Detail

- getTargetException

```java
public
RuntimeException
getTargetException()
```

Returns the actual

RuntimeException

thrown.

**Returns:** the wrapped

RuntimeException

.

- getCause

```java
public
Throwable
getCause()
```

Returns the actual

RuntimeException

thrown.

**Overrides:** getCause

in class

Throwable
**Returns:** the wrapped

RuntimeException

.

---

#### Method Detail

getTargetException

```java
public
RuntimeException
getTargetException()
```

Returns the actual

RuntimeException

thrown.

**Returns:** the wrapped

RuntimeException

.

---

#### getTargetException

public

RuntimeException

getTargetException()

Returns the actual

RuntimeException

thrown.

getCause

```java
public
Throwable
getCause()
```

Returns the actual

RuntimeException

thrown.

**Overrides:** getCause

in class

Throwable
**Returns:** the wrapped

RuntimeException

.

---

#### getCause

public

Throwable

getCause()

Returns the actual

RuntimeException

thrown.

---

