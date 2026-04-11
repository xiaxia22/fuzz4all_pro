# Class UnexpectedException

**Source:** `java.rmi\java\rmi\UnexpectedException.html`

### Class Description

```java
public class
UnexpectedException

extends
RemoteException
```

An

UnexpectedException

is thrown if the client of a
remote method call receives, as a result of the call, a checked
exception that is not among the checked exception types declared in the

throws

clause of the method in the remote interface.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public UnexpectedException​(
String
s)

Constructs an

UnexpectedException

with the specified
detail message.

**Parameters:**
- s

- the detail message

**Since:**
- 1.1

---

#### public UnexpectedException​(
String
s,

Exception
ex)

Constructs a

UnexpectedException

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

#### Class UnexpectedException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.UnexpectedException

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.UnexpectedException

java.lang.Exception

- java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.UnexpectedException

java.io.IOException

- java.rmi.RemoteException
- - java.rmi.UnexpectedException

java.rmi.RemoteException

- java.rmi.UnexpectedException

java.rmi.UnexpectedException

**All Implemented Interfaces:** Serializable

```java
public class
UnexpectedException

extends
RemoteException
```

An

UnexpectedException

is thrown if the client of a
remote method call receives, as a result of the call, a checked
exception that is not among the checked exception types declared in the

throws

clause of the method in the remote interface.

**Since:** 1.1
**See Also:** Serialized Form

public class

UnexpectedException

extends

RemoteException

An

UnexpectedException

is thrown if the client of a
remote method call receives, as a result of the call, a checked
exception that is not among the checked exception types declared in the

throws

clause of the method in the remote interface.

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

UnexpectedException

​(

String

s)

Constructs an

UnexpectedException

with the specified
detail message.

UnexpectedException

​(

String

s,

Exception

ex)

Constructs a

UnexpectedException

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

UnexpectedException

​(

String

s)

Constructs an

UnexpectedException

with the specified
detail message.

UnexpectedException

​(

String

s,

Exception

ex)

Constructs a

UnexpectedException

with the specified
detail message and nested exception.

---

#### Constructor Summary

Constructs an

UnexpectedException

with the specified
detail message.

Constructs a

UnexpectedException

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

- UnexpectedException

```java
public UnexpectedException​(
String
s)
```

Constructs an

UnexpectedException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

- UnexpectedException

```java
public UnexpectedException​(
String
s,

Exception
ex)
```

Constructs a

UnexpectedException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

Constructor Detail

- UnexpectedException

```java
public UnexpectedException​(
String
s)
```

Constructs an

UnexpectedException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

- UnexpectedException

```java
public UnexpectedException​(
String
s,

Exception
ex)
```

Constructs a

UnexpectedException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

---

#### Constructor Detail

UnexpectedException

```java
public UnexpectedException​(
String
s)
```

Constructs an

UnexpectedException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.1

---

#### UnexpectedException

public UnexpectedException​(

String

s)

Constructs an

UnexpectedException

with the specified
detail message.

UnexpectedException

```java
public UnexpectedException​(
String
s,

Exception
ex)
```

Constructs a

UnexpectedException

with the specified
detail message and nested exception.

**Parameters:** s

- the detail message
**Parameters:** ex

- the nested exception
**Since:** 1.1

---

#### UnexpectedException

public UnexpectedException​(

String

s,

Exception

ex)

Constructs a

UnexpectedException

with the specified
detail message and nested exception.

---

