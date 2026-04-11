# Class NoSuchObjectException

**Source:** `java.rmi\java\rmi\NoSuchObjectException.html`

### Class Description

```java
public class
NoSuchObjectException

extends
RemoteException
```

A

NoSuchObjectException

is thrown if an attempt is made to
invoke a method on an object that no longer exists in the remote virtual
machine. If a

NoSuchObjectException

occurs attempting to
invoke a method on a remote object, the call may be retransmitted and still
preserve RMI's "at most once" call semantics.

A

NoSuchObjectException

is also thrown by the method

java.rmi.server.RemoteObject.toStub

and by the

unexportObject

methods of

java.rmi.server.UnicastRemoteObject

and

java.rmi.activation.Activatable

and

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public NoSuchObjectException​(
String
s)

Constructs a

NoSuchObjectException

with the specified
detail message.

**Parameters:**
- s

- the detail message

**Since:**
- 1.1

---

### Method Details

*No entries found.*

### Additional Sections

#### Class NoSuchObjectException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.NoSuchObjectException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.NoSuchObjectException

java.lang.Exception

- java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.NoSuchObjectException

java.io.IOException

- java.rmi.RemoteException
- - java.rmi.NoSuchObjectException

java.rmi.RemoteException

- java.rmi.NoSuchObjectException

java.rmi.NoSuchObjectException

**All Implemented Interfaces:** Serializable

```java
public class
NoSuchObjectException

extends
RemoteException
```

A

NoSuchObjectException

is thrown if an attempt is made to
invoke a method on an object that no longer exists in the remote virtual
machine. If a

NoSuchObjectException

occurs attempting to
invoke a method on a remote object, the call may be retransmitted and still
preserve RMI's "at most once" call semantics.

A

NoSuchObjectException

is also thrown by the method

java.rmi.server.RemoteObject.toStub

and by the

unexportObject

methods of

java.rmi.server.UnicastRemoteObject

and

java.rmi.activation.Activatable

and

**Since:** 1.1
**See Also:** RemoteObject.toStub(Remote)

,

UnicastRemoteObject.unexportObject(Remote,boolean)

,

Activatable.unexportObject(Remote,boolean)

,

Serialized Form

public class

NoSuchObjectException

extends

RemoteException

A

NoSuchObjectException

is thrown if an attempt is made to
invoke a method on an object that no longer exists in the remote virtual
machine. If a

NoSuchObjectException

occurs attempting to
invoke a method on a remote object, the call may be retransmitted and still
preserve RMI's "at most once" call semantics.

A

NoSuchObjectException

is also thrown by the method

java.rmi.server.RemoteObject.toStub

and by the

unexportObject

methods of

java.rmi.server.UnicastRemoteObject

and

java.rmi.activation.Activatable

and

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

NoSuchObjectException

​(

String

s)

Constructs a

NoSuchObjectException

with the specified
detail message.

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

NoSuchObjectException

​(

String

s)

Constructs a

NoSuchObjectException

with the specified
detail message.

---

#### Constructor Summary

Constructs a

NoSuchObjectException

with the specified
detail message.

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

- NoSuchObjectException

```java
public NoSuchObjectException​(
String
s)
```

Constructs a

NoSuchObjectException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

Constructor Detail

- NoSuchObjectException

```java
public NoSuchObjectException​(
String
s)
```

Constructs a

NoSuchObjectException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

---

#### Constructor Detail

NoSuchObjectException

```java
public NoSuchObjectException​(
String
s)
```

Constructs a

NoSuchObjectException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

---

#### NoSuchObjectException

public NoSuchObjectException​(

String

s)

Constructs a

NoSuchObjectException

with the specified
detail message.

---

