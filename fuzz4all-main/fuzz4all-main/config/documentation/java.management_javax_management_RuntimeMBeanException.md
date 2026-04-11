# Class RuntimeMBeanException

**Source:** `java.management\javax\management\RuntimeMBeanException.html`

### Class Description

```java
public class
RuntimeMBeanException

extends
JMRuntimeException
```

Represents runtime exceptions thrown by MBean methods in
the agent. It "wraps" the actual

java.lang.RuntimeException

exception thrown.
This exception will be built by the MBeanServer when a call to an
MBean method throws a runtime exception.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public RuntimeMBeanException​(
RuntimeException
e)

Creates a

RuntimeMBeanException

that wraps the actual

java.lang.RuntimeException

.

**Parameters:**
- e

- the wrapped exception.

---

#### public RuntimeMBeanException​(
RuntimeException
e,

String
message)

Creates a

RuntimeMBeanException

that wraps the actual

java.lang.RuntimeException

with
a detailed message.

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

#### Class RuntimeMBeanException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - javax.management.JMRuntimeException
- - javax.management.RuntimeMBeanException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - javax.management.JMRuntimeException
- - javax.management.RuntimeMBeanException

java.lang.Exception

- java.lang.RuntimeException
- - javax.management.JMRuntimeException
- - javax.management.RuntimeMBeanException

java.lang.RuntimeException

- javax.management.JMRuntimeException
- - javax.management.RuntimeMBeanException

javax.management.JMRuntimeException

- javax.management.RuntimeMBeanException

javax.management.RuntimeMBeanException

**All Implemented Interfaces:** Serializable

```java
public class
RuntimeMBeanException

extends
JMRuntimeException
```

Represents runtime exceptions thrown by MBean methods in
the agent. It "wraps" the actual

java.lang.RuntimeException

exception thrown.
This exception will be built by the MBeanServer when a call to an
MBean method throws a runtime exception.

**Since:** 1.5
**See Also:** Serialized Form

public class

RuntimeMBeanException

extends

JMRuntimeException

Represents runtime exceptions thrown by MBean methods in
the agent. It "wraps" the actual

java.lang.RuntimeException

exception thrown.
This exception will be built by the MBeanServer when a call to an
MBean method throws a runtime exception.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RuntimeMBeanException

​(

RuntimeException

e)

Creates a

RuntimeMBeanException

that wraps the actual

java.lang.RuntimeException

.

RuntimeMBeanException

​(

RuntimeException

e,

String

message)

Creates a

RuntimeMBeanException

that wraps the actual

java.lang.RuntimeException

with
a detailed message.

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

RuntimeMBeanException

​(

RuntimeException

e)

Creates a

RuntimeMBeanException

that wraps the actual

java.lang.RuntimeException

.

RuntimeMBeanException

​(

RuntimeException

e,

String

message)

Creates a

RuntimeMBeanException

that wraps the actual

java.lang.RuntimeException

with
a detailed message.

---

#### Constructor Summary

Creates a

RuntimeMBeanException

that wraps the actual

java.lang.RuntimeException

.

Creates a

RuntimeMBeanException

that wraps the actual

java.lang.RuntimeException

with
a detailed message.

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

- RuntimeMBeanException

```java
public RuntimeMBeanException​(
RuntimeException
e)
```

Creates a

RuntimeMBeanException

that wraps the actual

java.lang.RuntimeException

.

**Parameters:** e

- the wrapped exception.

- RuntimeMBeanException

```java
public RuntimeMBeanException​(
RuntimeException
e,

String
message)
```

Creates a

RuntimeMBeanException

that wraps the actual

java.lang.RuntimeException

with
a detailed message.

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

- RuntimeMBeanException

```java
public RuntimeMBeanException​(
RuntimeException
e)
```

Creates a

RuntimeMBeanException

that wraps the actual

java.lang.RuntimeException

.

**Parameters:** e

- the wrapped exception.

- RuntimeMBeanException

```java
public RuntimeMBeanException​(
RuntimeException
e,

String
message)
```

Creates a

RuntimeMBeanException

that wraps the actual

java.lang.RuntimeException

with
a detailed message.

**Parameters:** e

- the wrapped exception.
**Parameters:** message

- the detail message.

---

#### Constructor Detail

RuntimeMBeanException

```java
public RuntimeMBeanException​(
RuntimeException
e)
```

Creates a

RuntimeMBeanException

that wraps the actual

java.lang.RuntimeException

.

**Parameters:** e

- the wrapped exception.

---

#### RuntimeMBeanException

public RuntimeMBeanException​(

RuntimeException

e)

Creates a

RuntimeMBeanException

that wraps the actual

java.lang.RuntimeException

.

RuntimeMBeanException

```java
public RuntimeMBeanException​(
RuntimeException
e,

String
message)
```

Creates a

RuntimeMBeanException

that wraps the actual

java.lang.RuntimeException

with
a detailed message.

**Parameters:** e

- the wrapped exception.
**Parameters:** message

- the detail message.

---

#### RuntimeMBeanException

public RuntimeMBeanException​(

RuntimeException

e,

String

message)

Creates a

RuntimeMBeanException

that wraps the actual

java.lang.RuntimeException

with
a detailed message.

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

