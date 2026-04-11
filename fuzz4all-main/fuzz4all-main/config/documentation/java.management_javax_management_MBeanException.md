# Class MBeanException

**Source:** `java.management\javax\management\MBeanException.html`

### Class Description

```java
public class
MBeanException

extends
JMException
```

Represents "user defined" exceptions thrown by MBean methods
in the agent. It "wraps" the actual "user defined" exception thrown.
This exception will be built by the MBeanServer when a call to an
MBean method results in an unknown exception.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public MBeanException​(
Exception
e)

Creates an

MBeanException

that wraps the actual

java.lang.Exception

.

**Parameters:**
- e

- the wrapped exception.

---

#### public MBeanException​(
Exception
e,

String
message)

Creates an

MBeanException

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

Return the actual

Exception

thrown.

**Returns:**
- the wrapped exception.

---

#### public
Throwable
getCause()

Return the actual

Exception

thrown.

**Overrides:**
- getCause

in class

Throwable

**Returns:**
- the wrapped exception.

---

### Additional Sections

#### Class MBeanException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.management.JMException
- - javax.management.MBeanException

java.lang.Throwable

- java.lang.Exception
- - javax.management.JMException
- - javax.management.MBeanException

java.lang.Exception

- javax.management.JMException
- - javax.management.MBeanException

javax.management.JMException

- javax.management.MBeanException

javax.management.MBeanException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** MBeanRegistrationException

```java
public class
MBeanException

extends
JMException
```

Represents "user defined" exceptions thrown by MBean methods
in the agent. It "wraps" the actual "user defined" exception thrown.
This exception will be built by the MBeanServer when a call to an
MBean method results in an unknown exception.

**Since:** 1.5
**See Also:** Serialized Form

public class

MBeanException

extends

JMException

Represents "user defined" exceptions thrown by MBean methods
in the agent. It "wraps" the actual "user defined" exception thrown.
This exception will be built by the MBeanServer when a call to an
MBean method results in an unknown exception.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MBeanException

​(

Exception

e)

Creates an

MBeanException

that wraps the actual

java.lang.Exception

.

MBeanException

​(

Exception

e,

String

message)

Creates an

MBeanException

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

Return the actual

Exception

thrown.

Exception

getTargetException

()

Return the actual

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

MBeanException

​(

Exception

e)

Creates an

MBeanException

that wraps the actual

java.lang.Exception

.

MBeanException

​(

Exception

e,

String

message)

Creates an

MBeanException

that wraps the actual

java.lang.Exception

with
a detail message.

---

#### Constructor Summary

Creates an

MBeanException

that wraps the actual

java.lang.Exception

.

Creates an

MBeanException

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

Return the actual

Exception

thrown.

Exception

getTargetException

()

Return the actual

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

Return the actual

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

- MBeanException

```java
public MBeanException​(
Exception
e)
```

Creates an

MBeanException

that wraps the actual

java.lang.Exception

.

**Parameters:** e

- the wrapped exception.

- MBeanException

```java
public MBeanException​(
Exception
e,

String
message)
```

Creates an

MBeanException

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

Return the actual

Exception

thrown.

**Returns:** the wrapped exception.

- getCause

```java
public
Throwable
getCause()
```

Return the actual

Exception

thrown.

**Overrides:** getCause

in class

Throwable
**Returns:** the wrapped exception.

Constructor Detail

- MBeanException

```java
public MBeanException​(
Exception
e)
```

Creates an

MBeanException

that wraps the actual

java.lang.Exception

.

**Parameters:** e

- the wrapped exception.

- MBeanException

```java
public MBeanException​(
Exception
e,

String
message)
```

Creates an

MBeanException

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

MBeanException

```java
public MBeanException​(
Exception
e)
```

Creates an

MBeanException

that wraps the actual

java.lang.Exception

.

**Parameters:** e

- the wrapped exception.

---

#### MBeanException

public MBeanException​(

Exception

e)

Creates an

MBeanException

that wraps the actual

java.lang.Exception

.

MBeanException

```java
public MBeanException​(
Exception
e,

String
message)
```

Creates an

MBeanException

that wraps the actual

java.lang.Exception

with
a detail message.

**Parameters:** e

- the wrapped exception.
**Parameters:** message

- the detail message.

---

#### MBeanException

public MBeanException​(

Exception

e,

String

message)

Creates an

MBeanException

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

Return the actual

Exception

thrown.

**Returns:** the wrapped exception.

- getCause

```java
public
Throwable
getCause()
```

Return the actual

Exception

thrown.

**Overrides:** getCause

in class

Throwable
**Returns:** the wrapped exception.

---

#### Method Detail

getTargetException

```java
public
Exception
getTargetException()
```

Return the actual

Exception

thrown.

**Returns:** the wrapped exception.

---

#### getTargetException

public

Exception

getTargetException()

Return the actual

Exception

thrown.

getCause

```java
public
Throwable
getCause()
```

Return the actual

Exception

thrown.

**Overrides:** getCause

in class

Throwable
**Returns:** the wrapped exception.

---

#### getCause

public

Throwable

getCause()

Return the actual

Exception

thrown.

---

