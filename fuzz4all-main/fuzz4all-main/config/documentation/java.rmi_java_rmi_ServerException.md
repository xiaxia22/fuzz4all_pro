# Class ServerException

**Source:** `java.rmi\java\rmi\ServerException.html`

### Class Description

```java
public class
ServerException

extends
RemoteException
```

A

ServerException

is thrown as a result of a remote method
invocation when a

RemoteException

is thrown while processing
the invocation on the server, either while unmarshalling the arguments or
executing the remote method itself.

A

ServerException

instance contains the original

RemoteException

that occurred as its cause.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ServerException​(
String
s)

Constructs a

ServerException

with the specified
detail message.

**Parameters:**
- s

- the detail message

**Since:**
- 1.1

---

#### public ServerException​(
String
s,

Exception
ex)

Constructs a

ServerException

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

#### Class ServerException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.ServerException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.ServerException

java.lang.Exception

- java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.ServerException

java.io.IOException

- java.rmi.RemoteException
- - java.rmi.ServerException

java.rmi.RemoteException

- java.rmi.ServerException

java.rmi.ServerException

**All Implemented Interfaces:** Serializable

```java
public class
ServerException

extends
RemoteException
```

A

ServerException

is thrown as a result of a remote method
invocation when a

RemoteException

is thrown while processing
the invocation on the server, either while unmarshalling the arguments or
executing the remote method itself.

A

ServerException

instance contains the original

RemoteException

that occurred as its cause.

**Since:** 1.1
**See Also:** Serialized Form

public class

ServerException

extends

RemoteException

A

ServerException

is thrown as a result of a remote method
invocation when a

RemoteException

is thrown while processing
the invocation on the server, either while unmarshalling the arguments or
executing the remote method itself.

A

ServerException

instance contains the original

RemoteException

that occurred as its cause.

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

ServerException

​(

String

s)

Constructs a

ServerException

with the specified
detail message.

ServerException

​(

String

s,

Exception

ex)

Constructs a

ServerException

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

ServerException

​(

String

s)

Constructs a

ServerException

with the specified
detail message.

ServerException

​(

String

s,

Exception

ex)

Constructs a

ServerException

with the specified
detail message and nested exception.

---

#### Constructor Summary

Constructs a

ServerException

with the specified
detail message.

Constructs a

ServerException

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

- ServerException

```java
public ServerException​(
String
s)
```

Constructs a

ServerException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

- ServerException

```java
public ServerException​(
String
s,

Exception
ex)
```

Constructs a

ServerException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

Constructor Detail

- ServerException

```java
public ServerException​(
String
s)
```

Constructs a

ServerException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

- ServerException

```java
public ServerException​(
String
s,

Exception
ex)
```

Constructs a

ServerException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

---

#### Constructor Detail

ServerException

```java
public ServerException​(
String
s)
```

Constructs a

ServerException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

---

#### ServerException

public ServerException​(

String

s)

Constructs a

ServerException

with the specified
detail message.

ServerException

```java
public ServerException​(
String
s,

Exception
ex)
```

Constructs a

ServerException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

---

#### ServerException

public ServerException​(

String

s,

Exception

ex)

Constructs a

ServerException

with the specified
detail message and nested exception.

---

