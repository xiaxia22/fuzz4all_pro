# Class UnmarshalException

**Source:** `java.rmi\java\rmi\UnmarshalException.html`

### Class Description

```java
public class
UnmarshalException

extends
RemoteException
```

An

UnmarshalException

can be thrown while unmarshalling the
parameters or results of a remote method call if any of the following
conditions occur:

- if an exception occurs while unmarshalling the call header

if the protocol for the return value is invalid

if a

java.io.IOException

occurs unmarshalling
parameters (on the server side) or the return value (on the client side).

if a

java.lang.ClassNotFoundException

occurs during
unmarshalling parameters or return values

if no skeleton can be loaded on the server-side; note that skeletons
are required in the 1.1 stub protocol, but not in the 1.2 stub protocol.

if the method hash is invalid (i.e., missing method).

if there is a failure to create a remote reference object for
a remote object's stub when it is unmarshalled.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public UnmarshalException​(
String
s)

Constructs an

UnmarshalException

with the specified
detail message.

**Parameters:**
- s

- the detail message

**Since:**
- 1.1

---

#### public UnmarshalException​(
String
s,

Exception
ex)

Constructs an

UnmarshalException

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

#### Class UnmarshalException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.UnmarshalException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.UnmarshalException

java.lang.Exception

- java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.UnmarshalException

java.io.IOException

- java.rmi.RemoteException
- - java.rmi.UnmarshalException

java.rmi.RemoteException

- java.rmi.UnmarshalException

java.rmi.UnmarshalException

**All Implemented Interfaces:** Serializable

```java
public class
UnmarshalException

extends
RemoteException
```

An

UnmarshalException

can be thrown while unmarshalling the
parameters or results of a remote method call if any of the following
conditions occur:

- if an exception occurs while unmarshalling the call header

if the protocol for the return value is invalid

if a

java.io.IOException

occurs unmarshalling
parameters (on the server side) or the return value (on the client side).

if a

java.lang.ClassNotFoundException

occurs during
unmarshalling parameters or return values

if no skeleton can be loaded on the server-side; note that skeletons
are required in the 1.1 stub protocol, but not in the 1.2 stub protocol.

if the method hash is invalid (i.e., missing method).

if there is a failure to create a remote reference object for
a remote object's stub when it is unmarshalled.

**Since:** 1.1
**See Also:** Serialized Form

public class

UnmarshalException

extends

RemoteException

An

UnmarshalException

can be thrown while unmarshalling the
parameters or results of a remote method call if any of the following
conditions occur:

- if an exception occurs while unmarshalling the call header

if the protocol for the return value is invalid

if a

java.io.IOException

occurs unmarshalling
parameters (on the server side) or the return value (on the client side).

if a

java.lang.ClassNotFoundException

occurs during
unmarshalling parameters or return values

if no skeleton can be loaded on the server-side; note that skeletons
are required in the 1.1 stub protocol, but not in the 1.2 stub protocol.

if the method hash is invalid (i.e., missing method).

if there is a failure to create a remote reference object for
a remote object's stub when it is unmarshalled.

if an exception occurs while unmarshalling the call header

if the protocol for the return value is invalid

if a

java.io.IOException

occurs unmarshalling
parameters (on the server side) or the return value (on the client side).

if a

java.lang.ClassNotFoundException

occurs during
unmarshalling parameters or return values

if no skeleton can be loaded on the server-side; note that skeletons
are required in the 1.1 stub protocol, but not in the 1.2 stub protocol.

if the method hash is invalid (i.e., missing method).

if there is a failure to create a remote reference object for
a remote object's stub when it is unmarshalled.

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

UnmarshalException

​(

String

s)

Constructs an

UnmarshalException

with the specified
detail message.

UnmarshalException

​(

String

s,

Exception

ex)

Constructs an

UnmarshalException

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

UnmarshalException

​(

String

s)

Constructs an

UnmarshalException

with the specified
detail message.

UnmarshalException

​(

String

s,

Exception

ex)

Constructs an

UnmarshalException

with the specified
detail message and nested exception.

---

#### Constructor Summary

Constructs an

UnmarshalException

with the specified
detail message.

Constructs an

UnmarshalException

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

- UnmarshalException

```java
public UnmarshalException​(
String
s)
```

Constructs an

UnmarshalException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

- UnmarshalException

```java
public UnmarshalException​(
String
s,

Exception
ex)
```

Constructs an

UnmarshalException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

Constructor Detail

- UnmarshalException

```java
public UnmarshalException​(
String
s)
```

Constructs an

UnmarshalException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

- UnmarshalException

```java
public UnmarshalException​(
String
s,

Exception
ex)
```

Constructs an

UnmarshalException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

---

#### Constructor Detail

UnmarshalException

```java
public UnmarshalException​(
String
s)
```

Constructs an

UnmarshalException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

---

#### UnmarshalException

public UnmarshalException​(

String

s)

Constructs an

UnmarshalException

with the specified
detail message.

UnmarshalException

```java
public UnmarshalException​(
String
s,

Exception
ex)
```

Constructs an

UnmarshalException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

---

#### UnmarshalException

public UnmarshalException​(

String

s,

Exception

ex)

Constructs an

UnmarshalException

with the specified
detail message and nested exception.

---

