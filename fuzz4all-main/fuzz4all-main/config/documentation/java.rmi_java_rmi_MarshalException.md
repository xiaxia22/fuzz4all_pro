# Class MarshalException

**Source:** `java.rmi\java\rmi\MarshalException.html`

### Class Description

```java
public class
MarshalException

extends
RemoteException
```

A

MarshalException

is thrown if a

java.io.IOException

occurs while marshalling the remote call
header, arguments or return value for a remote method call. A

MarshalException

is also thrown if the receiver does not
support the protocol version of the sender.

If a

MarshalException

occurs during a remote method call,
the call may or may not have reached the server. If the call did reach the
server, parameters may have been deserialized. A call may not be
retransmitted after a

MarshalException

and reliably preserve
"at most once" call semantics.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public MarshalException​(
String
s)

Constructs a

MarshalException

with the specified
detail message.

**Parameters:**
- s

- the detail message

**Since:**
- 1.1

---

#### public MarshalException​(
String
s,

Exception
ex)

Constructs a

MarshalException

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

#### Class MarshalException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.MarshalException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.MarshalException

java.lang.Exception

- java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.MarshalException

java.io.IOException

- java.rmi.RemoteException
- - java.rmi.MarshalException

java.rmi.RemoteException

- java.rmi.MarshalException

java.rmi.MarshalException

**All Implemented Interfaces:** Serializable

```java
public class
MarshalException

extends
RemoteException
```

A

MarshalException

is thrown if a

java.io.IOException

occurs while marshalling the remote call
header, arguments or return value for a remote method call. A

MarshalException

is also thrown if the receiver does not
support the protocol version of the sender.

If a

MarshalException

occurs during a remote method call,
the call may or may not have reached the server. If the call did reach the
server, parameters may have been deserialized. A call may not be
retransmitted after a

MarshalException

and reliably preserve
"at most once" call semantics.

**Since:** 1.1
**See Also:** Serialized Form

public class

MarshalException

extends

RemoteException

A

MarshalException

is thrown if a

java.io.IOException

occurs while marshalling the remote call
header, arguments or return value for a remote method call. A

MarshalException

is also thrown if the receiver does not
support the protocol version of the sender.

If a

MarshalException

occurs during a remote method call,
the call may or may not have reached the server. If the call did reach the
server, parameters may have been deserialized. A call may not be
retransmitted after a

MarshalException

and reliably preserve
"at most once" call semantics.

If a

MarshalException

occurs during a remote method call,
the call may or may not have reached the server. If the call did reach the
server, parameters may have been deserialized. A call may not be
retransmitted after a

MarshalException

and reliably preserve
"at most once" call semantics.

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

MarshalException

​(

String

s)

Constructs a

MarshalException

with the specified
detail message.

MarshalException

​(

String

s,

Exception

ex)

Constructs a

MarshalException

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

MarshalException

​(

String

s)

Constructs a

MarshalException

with the specified
detail message.

MarshalException

​(

String

s,

Exception

ex)

Constructs a

MarshalException

with the specified
detail message and nested exception.

---

#### Constructor Summary

Constructs a

MarshalException

with the specified
detail message.

Constructs a

MarshalException

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

- MarshalException

```java
public MarshalException​(
String
s)
```

Constructs a

MarshalException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

- MarshalException

```java
public MarshalException​(
String
s,

Exception
ex)
```

Constructs a

MarshalException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

Constructor Detail

- MarshalException

```java
public MarshalException​(
String
s)
```

Constructs a

MarshalException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

- MarshalException

```java
public MarshalException​(
String
s,

Exception
ex)
```

Constructs a

MarshalException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

---

#### Constructor Detail

MarshalException

```java
public MarshalException​(
String
s)
```

Constructs a

MarshalException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

---

#### MarshalException

public MarshalException​(

String

s)

Constructs a

MarshalException

with the specified
detail message.

MarshalException

```java
public MarshalException​(
String
s,

Exception
ex)
```

Constructs a

MarshalException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

---

#### MarshalException

public MarshalException​(

String

s,

Exception

ex)

Constructs a

MarshalException

with the specified
detail message and nested exception.

---

