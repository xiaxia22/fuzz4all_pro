# Class ReflectionException

**Source:** `java.management\javax\management\ReflectionException.html`

### Class Description

```java
public class
ReflectionException

extends
JMException
```

Represents exceptions thrown in the MBean server when using the
java.lang.reflect classes to invoke methods on MBeans. It "wraps" the
actual java.lang.Exception thrown.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ReflectionException​(
Exception
e)

Creates a

ReflectionException

that wraps the actual

java.lang.Exception

.

**Parameters:**
- e

- the wrapped exception.

---

#### public ReflectionException​(
Exception
e,

String
message)

Creates a

ReflectionException

that wraps the actual

java.lang.Exception

with
a detail message.

**Parameters:**
- e

- the wrapped exception.
- message

- the detail message.

---

### Method Details

#### public
Exception
getTargetException()

Returns the actual

Exception

thrown.

**Returns:**
- the wrapped

Exception

.

---

#### public
Throwable
getCause()

Returns the actual

Exception

thrown.

**Overrides:**
- getCause

in class

Throwable

**Returns:**
- the wrapped

Exception

.

---

### Additional Sections

#### Class ReflectionException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.management.JMException
- - javax.management.ReflectionException

java.lang.Throwable

- java.lang.Exception
- - javax.management.JMException
- - javax.management.ReflectionException

java.lang.Exception

- javax.management.JMException
- - javax.management.ReflectionException

javax.management.JMException

- javax.management.ReflectionException

javax.management.ReflectionException

**All Implemented Interfaces:** Serializable

```java
public class
ReflectionException

extends
JMException
```

Represents exceptions thrown in the MBean server when using the
java.lang.reflect classes to invoke methods on MBeans. It "wraps" the
actual java.lang.Exception thrown.

**Since:** 1.5
**See Also:** Serialized Form

public class

ReflectionException

extends

JMException

Represents exceptions thrown in the MBean server when using the
java.lang.reflect classes to invoke methods on MBeans. It "wraps" the
actual java.lang.Exception thrown.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ReflectionException

​(

Exception

e)

Creates a

ReflectionException

that wraps the actual

java.lang.Exception

.

ReflectionException

​(

Exception

e,

String

message)

Creates a

ReflectionException

that wraps the actual

java.lang.Exception

with
a detail message.

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

Exception

thrown.

Exception

getTargetException

()

Returns the actual

Exception

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

ReflectionException

​(

Exception

e)

Creates a

ReflectionException

that wraps the actual

java.lang.Exception

.

ReflectionException

​(

Exception

e,

String

message)

Creates a

ReflectionException

that wraps the actual

java.lang.Exception

with
a detail message.

---

#### Constructor Summary

Creates a

ReflectionException

that wraps the actual

java.lang.Exception

.

Creates a

ReflectionException

that wraps the actual

java.lang.Exception

with
a detail message.

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

Exception

thrown.

Exception

getTargetException

()

Returns the actual

Exception

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

Exception

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

- ReflectionException

```java
public ReflectionException​(
Exception
e)
```

Creates a

ReflectionException

that wraps the actual

java.lang.Exception

.

**Parameters:** e

- the wrapped exception.

- ReflectionException

```java
public ReflectionException​(
Exception
e,

String
message)
```

Creates a

ReflectionException

that wraps the actual

java.lang.Exception

with
a detail message.

**Parameters:** e

- the wrapped exception.
**Parameters:** message

- the detail message.

============ METHOD DETAIL ==========

- Method Detail

- getTargetException

```java
public
Exception
getTargetException()
```

Returns the actual

Exception

thrown.

**Returns:** the wrapped

Exception

.

- getCause

```java
public
Throwable
getCause()
```

Returns the actual

Exception

thrown.

**Overrides:** getCause

in class

Throwable
**Returns:** the wrapped

Exception

.

Constructor Detail

- ReflectionException

```java
public ReflectionException​(
Exception
e)
```

Creates a

ReflectionException

that wraps the actual

java.lang.Exception

.

**Parameters:** e

- the wrapped exception.

- ReflectionException

```java
public ReflectionException​(
Exception
e,

String
message)
```

Creates a

ReflectionException

that wraps the actual

java.lang.Exception

with
a detail message.

**Parameters:** e

- the wrapped exception.
**Parameters:** message

- the detail message.

---

#### Constructor Detail

ReflectionException

```java
public ReflectionException​(
Exception
e)
```

Creates a

ReflectionException

that wraps the actual

java.lang.Exception

.

**Parameters:** e

- the wrapped exception.

---

#### ReflectionException

public ReflectionException​(

Exception

e)

Creates a

ReflectionException

that wraps the actual

java.lang.Exception

.

ReflectionException

```java
public ReflectionException​(
Exception
e,

String
message)
```

Creates a

ReflectionException

that wraps the actual

java.lang.Exception

with
a detail message.

**Parameters:** e

- the wrapped exception.
**Parameters:** message

- the detail message.

---

#### ReflectionException

public ReflectionException​(

Exception

e,

String

message)

Creates a

ReflectionException

that wraps the actual

java.lang.Exception

with
a detail message.

Method Detail

- getTargetException

```java
public
Exception
getTargetException()
```

Returns the actual

Exception

thrown.

**Returns:** the wrapped

Exception

.

- getCause

```java
public
Throwable
getCause()
```

Returns the actual

Exception

thrown.

**Overrides:** getCause

in class

Throwable
**Returns:** the wrapped

Exception

.

---

#### Method Detail

getTargetException

```java
public
Exception
getTargetException()
```

Returns the actual

Exception

thrown.

**Returns:** the wrapped

Exception

.

---

#### getTargetException

public

Exception

getTargetException()

Returns the actual

Exception

thrown.

getCause

```java
public
Throwable
getCause()
```

Returns the actual

Exception

thrown.

**Overrides:** getCause

in class

Throwable
**Returns:** the wrapped

Exception

.

---

#### getCause

public

Throwable

getCause()

Returns the actual

Exception

thrown.

---

