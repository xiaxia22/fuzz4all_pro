# Class UnknownObjectException

**Source:** `java.rmi\java\rmi\activation\UnknownObjectException.html`

### Class Description

```java
public class
UnknownObjectException

extends
ActivationException
```

An

UnknownObjectException

is thrown by methods of classes and
interfaces in the

java.rmi.activation

package when the

ActivationID

parameter to the method is determined to be
invalid. An

ActivationID

is invalid if it is not currently
known by the

ActivationSystem

. An

ActivationID

is obtained by the

ActivationSystem.registerObject

method.
An

ActivationID

is also obtained during the

Activatable.register

call.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public UnknownObjectException​(
String
s)

Constructs an

UnknownObjectException

with the specified
detail message.

**Parameters:**
- s

- the detail message

**Since:**
- 1.2

---

### Method Details

*No entries found.*

### Additional Sections

#### Class UnknownObjectException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.rmi.activation.ActivationException
- - java.rmi.activation.UnknownObjectException

java.lang.Throwable

- java.lang.Exception
- - java.rmi.activation.ActivationException
- - java.rmi.activation.UnknownObjectException

java.lang.Exception

- java.rmi.activation.ActivationException
- - java.rmi.activation.UnknownObjectException

java.rmi.activation.ActivationException

- java.rmi.activation.UnknownObjectException

java.rmi.activation.UnknownObjectException

**All Implemented Interfaces:** Serializable

```java
public class
UnknownObjectException

extends
ActivationException
```

An

UnknownObjectException

is thrown by methods of classes and
interfaces in the

java.rmi.activation

package when the

ActivationID

parameter to the method is determined to be
invalid. An

ActivationID

is invalid if it is not currently
known by the

ActivationSystem

. An

ActivationID

is obtained by the

ActivationSystem.registerObject

method.
An

ActivationID

is also obtained during the

Activatable.register

call.

**Since:** 1.2
**See Also:** Activatable

,

ActivationGroup

,

ActivationID

,

ActivationMonitor

,

ActivationSystem

,

Activator

,

Serialized Form

public class

UnknownObjectException

extends

ActivationException

An

UnknownObjectException

is thrown by methods of classes and
interfaces in the

java.rmi.activation

package when the

ActivationID

parameter to the method is determined to be
invalid. An

ActivationID

is invalid if it is not currently
known by the

ActivationSystem

. An

ActivationID

is obtained by the

ActivationSystem.registerObject

method.
An

ActivationID

is also obtained during the

Activatable.register

call.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.rmi.activation.

ActivationException

detail

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

UnknownObjectException

​(

String

s)

Constructs an

UnknownObjectException

with the specified
detail message.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.rmi.activation.

ActivationException

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

- Fields declared in class java.rmi.activation.

ActivationException

detail

---

#### Field Summary

Fields declared in class java.rmi.activation.

ActivationException

detail

---

#### Fields declared in class java.rmi.activation. ActivationException

Constructor Summary

Constructors

Constructor

Description

UnknownObjectException

​(

String

s)

Constructs an

UnknownObjectException

with the specified
detail message.

---

#### Constructor Summary

Constructs an

UnknownObjectException

with the specified
detail message.

Method Summary

- Methods declared in class java.rmi.activation.

ActivationException

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

Methods declared in class java.rmi.activation.

ActivationException

getCause

,

getMessage

---

#### Methods declared in class java.rmi.activation. ActivationException

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

- UnknownObjectException

```java
public UnknownObjectException​(
String
s)
```

Constructs an

UnknownObjectException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.2

Constructor Detail

- UnknownObjectException

```java
public UnknownObjectException​(
String
s)
```

Constructs an

UnknownObjectException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.2

---

#### Constructor Detail

UnknownObjectException

```java
public UnknownObjectException​(
String
s)
```

Constructs an

UnknownObjectException

with the specified
detail message.

**Parameters:** s

- the detail message
**Since:** 1.2

---

#### UnknownObjectException

public UnknownObjectException​(

String

s)

Constructs an

UnknownObjectException

with the specified
detail message.

---

