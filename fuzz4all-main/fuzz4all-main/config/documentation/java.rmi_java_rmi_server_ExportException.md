# Class ExportException

**Source:** `java.rmi\java\rmi\server\ExportException.html`

### Class Description

```java
public class
ExportException

extends
RemoteException
```

An

ExportException

is a

RemoteException

thrown if an attempt to export a remote object fails. A remote object is
exported via the constructors and

exportObject

methods of

java.rmi.server.UnicastRemoteObject

and

java.rmi.activation.Activatable

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ExportException​(
String
s)

Constructs an

ExportException

with the specified
detail message.

**Parameters:**
- s

- the detail message

**Since:**
- 1.1

---

#### public ExportException​(
String
s,

Exception
ex)

Constructs an

ExportException

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

#### Class ExportException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.server.ExportException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.server.ExportException

java.lang.Exception

- java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.server.ExportException

java.io.IOException

- java.rmi.RemoteException
- - java.rmi.server.ExportException

java.rmi.RemoteException

- java.rmi.server.ExportException

java.rmi.server.ExportException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** SocketSecurityException

```java
public class
ExportException

extends
RemoteException
```

An

ExportException

is a

RemoteException

thrown if an attempt to export a remote object fails. A remote object is
exported via the constructors and

exportObject

methods of

java.rmi.server.UnicastRemoteObject

and

java.rmi.activation.Activatable

.

**Since:** 1.1
**See Also:** UnicastRemoteObject

,

Activatable

,

Serialized Form

public class

ExportException

extends

RemoteException

An

ExportException

is a

RemoteException

thrown if an attempt to export a remote object fails. A remote object is
exported via the constructors and

exportObject

methods of

java.rmi.server.UnicastRemoteObject

and

java.rmi.activation.Activatable

.

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

ExportException

​(

String

s)

Constructs an

ExportException

with the specified
detail message.

ExportException

​(

String

s,

Exception

ex)

Constructs an

ExportException

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

ExportException

​(

String

s)

Constructs an

ExportException

with the specified
detail message.

ExportException

​(

String

s,

Exception

ex)

Constructs an

ExportException

with the specified
detail message and nested exception.

---

#### Constructor Summary

Constructs an

ExportException

with the specified
detail message.

Constructs an

ExportException

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

- ExportException

```java
public ExportException​(
String
s)
```

Constructs an

ExportException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

- ExportException

```java
public ExportException​(
String
s,

Exception
ex)
```

Constructs an

ExportException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

Constructor Detail

- ExportException

```java
public ExportException​(
String
s)
```

Constructs an

ExportException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

- ExportException

```java
public ExportException​(
String
s,

Exception
ex)
```

Constructs an

ExportException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

---

#### Constructor Detail

ExportException

```java
public ExportException​(
String
s)
```

Constructs an

ExportException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

---

#### ExportException

public ExportException​(

String

s)

Constructs an

ExportException

with the specified
detail message.

ExportException

```java
public ExportException​(
String
s,

Exception
ex)
```

Constructs an

ExportException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

---

#### ExportException

public ExportException​(

String

s,

Exception

ex)

Constructs an

ExportException

with the specified
detail message and nested exception.

---

