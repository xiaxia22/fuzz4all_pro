# Class AccessException

**Source:** `java.rmi\java\rmi\AccessException.html`

### Class Description

```java
public class
AccessException

extends
RemoteException
```

An

AccessException

is thrown by certain methods of the

java.rmi.Naming

class (specifically

bind

,

rebind

, and

unbind

) and methods of the

java.rmi.activation.ActivationSystem

interface to
indicate that the caller does not have permission to perform the action
requested by the method call. If the method was invoked from a non-local
host, then an

AccessException

is thrown.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public AccessException​(
String
s)

Constructs an

AccessException

with the specified
detail message.

**Parameters:**
- s

- the detail message

**Since:**
- 1.1

---

#### public AccessException​(
String
s,

Exception
ex)

Constructs an

AccessException

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

#### Class AccessException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.AccessException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.AccessException

java.lang.Exception

- java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.AccessException

java.io.IOException

- java.rmi.RemoteException
- - java.rmi.AccessException

java.rmi.RemoteException

- java.rmi.AccessException

java.rmi.AccessException

**All Implemented Interfaces:** Serializable

```java
public class
AccessException

extends
RemoteException
```

An

AccessException

is thrown by certain methods of the

java.rmi.Naming

class (specifically

bind

,

rebind

, and

unbind

) and methods of the

java.rmi.activation.ActivationSystem

interface to
indicate that the caller does not have permission to perform the action
requested by the method call. If the method was invoked from a non-local
host, then an

AccessException

is thrown.

**Since:** 1.1
**See Also:** Naming

,

ActivationSystem

,

Serialized Form

public class

AccessException

extends

RemoteException

An

AccessException

is thrown by certain methods of the

java.rmi.Naming

class (specifically

bind

,

rebind

, and

unbind

) and methods of the

java.rmi.activation.ActivationSystem

interface to
indicate that the caller does not have permission to perform the action
requested by the method call. If the method was invoked from a non-local
host, then an

AccessException

is thrown.

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

AccessException

​(

String

s)

Constructs an

AccessException

with the specified
detail message.

AccessException

​(

String

s,

Exception

ex)

Constructs an

AccessException

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

AccessException

​(

String

s)

Constructs an

AccessException

with the specified
detail message.

AccessException

​(

String

s,

Exception

ex)

Constructs an

AccessException

with the specified
detail message and nested exception.

---

#### Constructor Summary

Constructs an

AccessException

with the specified
detail message.

Constructs an

AccessException

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

- AccessException

```java
public AccessException​(
String
s)
```

Constructs an

AccessException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

- AccessException

```java
public AccessException​(
String
s,

Exception
ex)
```

Constructs an

AccessException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

Constructor Detail

- AccessException

```java
public AccessException​(
String
s)
```

Constructs an

AccessException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

- AccessException

```java
public AccessException​(
String
s,

Exception
ex)
```

Constructs an

AccessException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

---

#### Constructor Detail

AccessException

```java
public AccessException​(
String
s)
```

Constructs an

AccessException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

---

#### AccessException

public AccessException​(

String

s)

Constructs an

AccessException

with the specified
detail message.

AccessException

```java
public AccessException​(
String
s,

Exception
ex)
```

Constructs an

AccessException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

---

#### AccessException

public AccessException​(

String

s,

Exception

ex)

Constructs an

AccessException

with the specified
detail message and nested exception.

---

