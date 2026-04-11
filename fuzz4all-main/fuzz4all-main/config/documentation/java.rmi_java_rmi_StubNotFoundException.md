# Class StubNotFoundException

**Source:** `java.rmi\java\rmi\StubNotFoundException.html`

### Class Description

```java
public class
StubNotFoundException

extends
RemoteException
```

A

StubNotFoundException

is thrown if a valid stub class
could not be found for a remote object when it is exported.
A

StubNotFoundException

may also be
thrown when an activatable object is registered via the

java.rmi.activation.Activatable.register

method.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public StubNotFoundException​(
String
s)

Constructs a

StubNotFoundException

with the specified
detail message.

**Parameters:**
- s

- the detail message

**Since:**
- 1.1

---

#### public StubNotFoundException​(
String
s,

Exception
ex)

Constructs a

StubNotFoundException

with the specified
detail message and nested exception.

**Parameters:**
- s

- the detail message
- ex

- the nested exception

**Since:**
- 1.1

---

### Method Details

*No entries found.*

### Additional Sections

#### Class StubNotFoundException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.StubNotFoundException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.StubNotFoundException

java.lang.Exception

- java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.StubNotFoundException

java.io.IOException

- java.rmi.RemoteException
- - java.rmi.StubNotFoundException

java.rmi.RemoteException

- java.rmi.StubNotFoundException

java.rmi.StubNotFoundException

**All Implemented Interfaces:** Serializable

```java
public class
StubNotFoundException

extends
RemoteException
```

A

StubNotFoundException

is thrown if a valid stub class
could not be found for a remote object when it is exported.
A

StubNotFoundException

may also be
thrown when an activatable object is registered via the

java.rmi.activation.Activatable.register

method.

**Since:** 1.1
**See Also:** UnicastRemoteObject

,

Activatable

,

Serialized Form

public class

StubNotFoundException

extends

RemoteException

A

StubNotFoundException

is thrown if a valid stub class
could not be found for a remote object when it is exported.
A

StubNotFoundException

may also be
thrown when an activatable object is registered via the

java.rmi.activation.Activatable.register

method.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.rmi.

RemoteException

detail

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

StubNotFoundException

​(

String

s)

Constructs a

StubNotFoundException

with the specified
detail message.

StubNotFoundException

​(

String

s,

Exception

ex)

Constructs a

StubNotFoundException

with the specified
detail message and nested exception.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.rmi.

RemoteException

getCause

,

getMessage

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

Field Summary

- Fields declared in class java.rmi.

RemoteException

detail

---

#### Field Summary

Fields declared in class java.rmi.

RemoteException

detail

---

#### Fields declared in class java.rmi. RemoteException

Constructor Summary

Constructors

Constructor

Description

StubNotFoundException

​(

String

s)

Constructs a

StubNotFoundException

with the specified
detail message.

StubNotFoundException

​(

String

s,

Exception

ex)

Constructs a

StubNotFoundException

with the specified
detail message and nested exception.

---

#### Constructor Summary

Constructs a

StubNotFoundException

with the specified
detail message.

Constructs a

StubNotFoundException

with the specified
detail message and nested exception.

Method Summary

- Methods declared in class java.rmi.

RemoteException

getCause

,

getMessage

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

Methods declared in class java.rmi.

RemoteException

getCause

,

getMessage

---

#### Methods declared in class java.rmi. RemoteException

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

- StubNotFoundException

```java
public StubNotFoundException​(
String
s)
```

Constructs a

StubNotFoundException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

- StubNotFoundException

```java
public StubNotFoundException​(
String
s,

Exception
ex)
```

Constructs a

StubNotFoundException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

Constructor Detail

- StubNotFoundException

```java
public StubNotFoundException​(
String
s)
```

Constructs a

StubNotFoundException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

- StubNotFoundException

```java
public StubNotFoundException​(
String
s,

Exception
ex)
```

Constructs a

StubNotFoundException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

---

#### Constructor Detail

StubNotFoundException

```java
public StubNotFoundException​(
String
s)
```

Constructs a

StubNotFoundException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

---

#### StubNotFoundException

public StubNotFoundException​(

String

s)

Constructs a

StubNotFoundException

with the specified
detail message.

StubNotFoundException

```java
public StubNotFoundException​(
String
s,

Exception
ex)
```

Constructs a

StubNotFoundException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

---

#### StubNotFoundException

public StubNotFoundException​(

String

s,

Exception

ex)

Constructs a

StubNotFoundException

with the specified
detail message and nested exception.

---

