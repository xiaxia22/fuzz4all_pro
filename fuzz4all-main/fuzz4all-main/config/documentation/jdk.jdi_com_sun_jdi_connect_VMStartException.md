# Class VMStartException

**Source:** `jdk.jdi\com\sun\jdi\connect\VMStartException.html`

### Class Description

```java
public class
VMStartException

extends
Exception
```

A target VM was successfully launched, but terminated with an
error before a connection could be established. This exception
provides the

Process

object for the launched
target to help in diagnosing the problem.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public VMStartException​(
Process
process)

*No description found.*

---

#### public VMStartException​(
String
message,

Process
process)

*No description found.*

---

### Method Details

#### public
Process
process()

*No description found.*

---

### Additional Sections

#### Class VMStartException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - com.sun.jdi.connect.VMStartException

java.lang.Throwable

- java.lang.Exception
- - com.sun.jdi.connect.VMStartException

java.lang.Exception

- com.sun.jdi.connect.VMStartException

com.sun.jdi.connect.VMStartException

**All Implemented Interfaces:** Serializable

```java
public class
VMStartException

extends
Exception
```

A target VM was successfully launched, but terminated with an
error before a connection could be established. This exception
provides the

Process

object for the launched
target to help in diagnosing the problem.

**Since:** 1.3
**See Also:** Serialized Form

public class

VMStartException

extends

Exception

A target VM was successfully launched, but terminated with an
error before a connection could be established. This exception
provides the

Process

object for the launched
target to help in diagnosing the problem.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

VMStartException

​(

Process

process)

VMStartException

​(

String

message,

Process

process)

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Process

process

()

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

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

Constructor Summary

Constructors

Constructor

Description

VMStartException

​(

Process

process)

VMStartException

​(

String

message,

Process

process)

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

Process

process

()

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

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

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

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

- VMStartException

```java
public VMStartException​(
Process
process)
```

- VMStartException

```java
public VMStartException​(
String
message,

Process
process)
```

============ METHOD DETAIL ==========

- Method Detail

- process

```java
public
Process
process()
```

Constructor Detail

- VMStartException

```java
public VMStartException​(
Process
process)
```

- VMStartException

```java
public VMStartException​(
String
message,

Process
process)
```

---

#### Constructor Detail

VMStartException

```java
public VMStartException​(
Process
process)
```

---

#### VMStartException

public VMStartException​(

Process

process)

VMStartException

```java
public VMStartException​(
String
message,

Process
process)
```

---

#### VMStartException

public VMStartException​(

String

message,

Process

process)

Method Detail

- process

```java
public
Process
process()
```

---

#### Method Detail

process

```java
public
Process
process()
```

---

#### process

public

Process

process()

---

