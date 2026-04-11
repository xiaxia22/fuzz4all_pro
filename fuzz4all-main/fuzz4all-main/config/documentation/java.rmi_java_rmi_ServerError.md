# Class ServerError

**Source:** `java.rmi\java\rmi\ServerError.html`

### Class Description

```java
public class
ServerError

extends
RemoteException
```

A

ServerError

is thrown as a result of a remote method
invocation when an

Error

is thrown while processing
the invocation on the server, either while unmarshalling the arguments,
executing the remote method itself, or marshalling the return value.

A

ServerError

instance contains the original

Error

that occurred as its cause.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ServerError​(
String
s,

Error
err)

Constructs a

ServerError

with the specified
detail message and nested error.

**Parameters:**
- s

- the detail message
- err

- the nested error

**Since:**
- 1.1

---

### Method Details

*No entries found.*

### Additional Sections

#### Class ServerError

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.ServerError

java.lang.Throwable

- java.lang.Exception
- - java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.ServerError

java.lang.Exception

- java.io.IOException
- - java.rmi.RemoteException
- - java.rmi.ServerError

java.io.IOException

- java.rmi.RemoteException
- - java.rmi.ServerError

java.rmi.RemoteException

- java.rmi.ServerError

java.rmi.ServerError

**All Implemented Interfaces:** Serializable

```java
public class
ServerError

extends
RemoteException
```

A

ServerError

is thrown as a result of a remote method
invocation when an

Error

is thrown while processing
the invocation on the server, either while unmarshalling the arguments,
executing the remote method itself, or marshalling the return value.

A

ServerError

instance contains the original

Error

that occurred as its cause.

**Since:** 1.1
**See Also:** Serialized Form

public class

ServerError

extends

RemoteException

A

ServerError

is thrown as a result of a remote method
invocation when an

Error

is thrown while processing
the invocation on the server, either while unmarshalling the arguments,
executing the remote method itself, or marshalling the return value.

A

ServerError

instance contains the original

Error

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

ServerError

​(

String

s,

Error

err)

Constructs a

ServerError

with the specified
detail message and nested error.

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

ServerError

​(

String

s,

Error

err)

Constructs a

ServerError

with the specified
detail message and nested error.

---

#### Constructor Summary

Constructs a

ServerError

with the specified
detail message and nested error.

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

- ServerError

```java
public ServerError​(
String
s,

Error
err)
```

Constructs a

ServerError

with the specified
detail message and nested error.

**Parameters:** s

- the detail message
**Parameters:** err

- the nested error
**Since:** 1.1

Constructor Detail

- ServerError

```java
public ServerError​(
String
s,

Error
err)
```

Constructs a

ServerError

with the specified
detail message and nested error.

**Parameters:** s

- the detail message
**Parameters:** err

- the nested error
**Since:** 1.1

---

#### Constructor Detail

ServerError

```java
public ServerError​(
String
s,

Error
err)
```

Constructs a

ServerError

with the specified
detail message and nested error.

**Parameters:** s

- the detail message
**Parameters:** err

- the nested error
**Since:** 1.1

---

#### ServerError

public ServerError​(

String

s,

Error

err)

Constructs a

ServerError

with the specified
detail message and nested error.

---

