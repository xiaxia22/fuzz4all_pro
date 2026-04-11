# Class ServerRuntimeException

**Source:** `java.rmi\java\rmi\ServerRuntimeException.html`

### Class Description

```java
@Deprecated

public class
ServerRuntimeException

extends
RemoteException
```

From a server executing on JDK 1.1, a

ServerRuntimeException

is thrown as a result of a
remote method invocation when a

RuntimeException

is
thrown while processing the invocation on the server, either while
unmarshalling the arguments, executing the remote method itself, or
marshalling the return value.

A

ServerRuntimeException

instance contains the original

RuntimeException

that occurred as its cause.

A

ServerRuntimeException

is not thrown from servers
executing on the Java 2 platform v1.2 or later versions.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### @Deprecated

public ServerRuntimeException​(
String
s,

Exception
ex)

Constructs a

ServerRuntimeException

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

#### Class ServerRuntimeException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.ServerRuntimeException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.ServerRuntimeException

java.lang.Exception

- java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.ServerRuntimeException

java.io.IOException

- java.rmi.RemoteException
- - java.rmi.ServerRuntimeException

java.rmi.RemoteException

- java.rmi.ServerRuntimeException

java.rmi.ServerRuntimeException

**All Implemented Interfaces:** Serializable

```java
@Deprecated

public class
ServerRuntimeException

extends
RemoteException
```

Deprecated.

no replacement

From a server executing on JDK 1.1, a

ServerRuntimeException

is thrown as a result of a
remote method invocation when a

RuntimeException

is
thrown while processing the invocation on the server, either while
unmarshalling the arguments, executing the remote method itself, or
marshalling the return value.

A

ServerRuntimeException

instance contains the original

RuntimeException

that occurred as its cause.

A

ServerRuntimeException

is not thrown from servers
executing on the Java 2 platform v1.2 or later versions.

**Since:** 1.1
**See Also:** Serialized Form

@Deprecated

public class

ServerRuntimeException

extends

RemoteException

From a server executing on JDK 1.1, a

ServerRuntimeException

is thrown as a result of a
remote method invocation when a

RuntimeException

is
thrown while processing the invocation on the server, either while
unmarshalling the arguments, executing the remote method itself, or
marshalling the return value.

A

ServerRuntimeException

instance contains the original

RuntimeException

that occurred as its cause.

A

ServerRuntimeException

is not thrown from servers
executing on the Java 2 platform v1.2 or later versions.

A

ServerRuntimeException

is not thrown from servers
executing on the Java 2 platform v1.2 or later versions.

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

ServerRuntimeException

​(

String

s,

Exception

ex)

Deprecated.

no replacement

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

ServerRuntimeException

​(

String

s,

Exception

ex)

Deprecated.

no replacement

---

#### Constructor Summary

Deprecated.

no replacement

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

- ServerRuntimeException

```java
@Deprecated

public ServerRuntimeException​(
String
s,

Exception
ex)
```

Deprecated.

no replacement

Constructs a

ServerRuntimeException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

Constructor Detail

- ServerRuntimeException

```java
@Deprecated

public ServerRuntimeException​(
String
s,

Exception
ex)
```

Deprecated.

no replacement

Constructs a

ServerRuntimeException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

---

#### Constructor Detail

ServerRuntimeException

```java
@Deprecated

public ServerRuntimeException​(
String
s,

Exception
ex)
```

Deprecated.

no replacement

Constructs a

ServerRuntimeException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

---

#### ServerRuntimeException

@Deprecated

public ServerRuntimeException​(

String

s,

Exception

ex)

Constructs a

ServerRuntimeException

with the specified
detail message and nested exception.

---

