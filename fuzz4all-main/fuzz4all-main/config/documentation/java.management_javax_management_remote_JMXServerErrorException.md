# Class JMXServerErrorException

**Source:** `java.management\javax\management\remote\JMXServerErrorException.html`

### Class Description

```java
public class
JMXServerErrorException

extends
IOException
```

Exception thrown as the result of a remote

MBeanServer

method invocation when an

Error

is thrown while
processing the invocation in the remote MBean server. A

JMXServerErrorException

instance contains the original

Error

that occurred as its cause.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public JMXServerErrorException​(
String
s,

Error
err)

Constructs a

JMXServerErrorException

with the specified
detail message and nested error.

**Parameters:**
- s

- the detail message.
- err

- the nested error. An instance of this class can be
constructed where this parameter is null, but the standard
connectors will never do so.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class JMXServerErrorException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - javax.management.remote.JMXServerErrorException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - javax.management.remote.JMXServerErrorException

java.lang.Exception

- java.io.IOException
- - javax.management.remote.JMXServerErrorException

java.io.IOException

- javax.management.remote.JMXServerErrorException

javax.management.remote.JMXServerErrorException

**All Implemented Interfaces:** Serializable

```java
public class
JMXServerErrorException

extends
IOException
```

Exception thrown as the result of a remote

MBeanServer

method invocation when an

Error

is thrown while
processing the invocation in the remote MBean server. A

JMXServerErrorException

instance contains the original

Error

that occurred as its cause.

**Since:** 1.5
**See Also:** ServerError

,

Serialized Form

public class

JMXServerErrorException

extends

IOException

Exception thrown as the result of a remote

MBeanServer

method invocation when an

Error

is thrown while
processing the invocation in the remote MBean server. A

JMXServerErrorException

instance contains the original

Error

that occurred as its cause.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

JMXServerErrorException

​(

String

s,

Error

err)

Constructs a

JMXServerErrorException

with the specified
detail message and nested error.

========== METHOD SUMMARY ===========

- Method Summary

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

JMXServerErrorException

​(

String

s,

Error

err)

Constructs a

JMXServerErrorException

with the specified
detail message and nested error.

---

#### Constructor Summary

Constructs a

JMXServerErrorException

with the specified
detail message and nested error.

Method Summary

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

- JMXServerErrorException

```java
public JMXServerErrorException​(
String
s,

Error
err)
```

Constructs a

JMXServerErrorException

with the specified
detail message and nested error.

**Parameters:** s

- the detail message.
**Parameters:** err

- the nested error. An instance of this class can be
constructed where this parameter is null, but the standard
connectors will never do so.

Constructor Detail

- JMXServerErrorException

```java
public JMXServerErrorException​(
String
s,

Error
err)
```

Constructs a

JMXServerErrorException

with the specified
detail message and nested error.

**Parameters:** s

- the detail message.
**Parameters:** err

- the nested error. An instance of this class can be
constructed where this parameter is null, but the standard
connectors will never do so.

---

#### Constructor Detail

JMXServerErrorException

```java
public JMXServerErrorException​(
String
s,

Error
err)
```

Constructs a

JMXServerErrorException

with the specified
detail message and nested error.

**Parameters:** s

- the detail message.
**Parameters:** err

- the nested error. An instance of this class can be
constructed where this parameter is null, but the standard
connectors will never do so.

---

#### JMXServerErrorException

public JMXServerErrorException​(

String

s,

Error

err)

Constructs a

JMXServerErrorException

with the specified
detail message and nested error.

---

