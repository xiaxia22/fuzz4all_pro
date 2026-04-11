# Class InterruptedNamingException

**Source:** `java.naming\javax\naming\InterruptedNamingException.html`

### Class Description

```java
public class
InterruptedNamingException

extends
NamingException
```

This exception is thrown when the naming operation
being invoked has been interrupted. For example, an application
might interrupt a thread that is performing a search. If the
search supports being interrupted, it will throw
InterruptedNamingException. Whether an operation is interruptible
and when depends on its implementation (as provided by the
service providers). Different implementations have different ways
of protecting their resources and objects from being damaged
due to unexpected interrupts.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public InterruptedNamingException​(
String
explanation)

Constructs an instance of InterruptedNamingException using an
explanation of the problem.
All name resolution-related fields are initialized to null.

**Parameters:**
- explanation

- A possibly null message explaining the problem.

**See Also:**
- Throwable.getMessage()

---

#### public InterruptedNamingException()

Constructs an instance of InterruptedNamingException with
all name resolution fields and explanation initialized to null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class InterruptedNamingException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.InterruptedNamingException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.InterruptedNamingException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.InterruptedNamingException

javax.naming.NamingException

- javax.naming.InterruptedNamingException

javax.naming.InterruptedNamingException

**All Implemented Interfaces:** Serializable

```java
public class
InterruptedNamingException

extends
NamingException
```

This exception is thrown when the naming operation
being invoked has been interrupted. For example, an application
might interrupt a thread that is performing a search. If the
search supports being interrupted, it will throw
InterruptedNamingException. Whether an operation is interruptible
and when depends on its implementation (as provided by the
service providers). Different implementations have different ways
of protecting their resources and objects from being damaged
due to unexpected interrupts.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Context

,

DirContext

,

Thread.interrupt()

,

InterruptedException

,

Serialized Form

public class

InterruptedNamingException

extends

NamingException

This exception is thrown when the naming operation
being invoked has been interrupted. For example, an application
might interrupt a thread that is performing a search. If the
search supports being interrupted, it will throw
InterruptedNamingException. Whether an operation is interruptible
and when depends on its implementation (as provided by the
service providers). Different implementations have different ways
of protecting their resources and objects from being damaged
due to unexpected interrupts.

Synchronization and serialization issues that apply to NamingException
apply directly here.

Synchronization and serialization issues that apply to NamingException
apply directly here.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.naming.

NamingException

remainingName

,

resolvedName

,

resolvedObj

,

rootException

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

InterruptedNamingException

()

Constructs an instance of InterruptedNamingException with
all name resolution fields and explanation initialized to null.

InterruptedNamingException

​(

String

explanation)

Constructs an instance of InterruptedNamingException using an
explanation of the problem.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class javax.naming.

NamingException

appendRemainingComponent

,

appendRemainingName

,

getCause

,

getExplanation

,

getRemainingName

,

getResolvedName

,

getResolvedObj

,

getRootCause

,

initCause

,

setRemainingName

,

setResolvedName

,

setResolvedObj

,

setRootCause

,

toString

,

toString

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

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

- Fields declared in class javax.naming.

NamingException

remainingName

,

resolvedName

,

resolvedObj

,

rootException

---

#### Field Summary

Fields declared in class javax.naming.

NamingException

remainingName

,

resolvedName

,

resolvedObj

,

rootException

---

#### Fields declared in class javax.naming. NamingException

Constructor Summary

Constructors

Constructor

Description

InterruptedNamingException

()

Constructs an instance of InterruptedNamingException with
all name resolution fields and explanation initialized to null.

InterruptedNamingException

​(

String

explanation)

Constructs an instance of InterruptedNamingException using an
explanation of the problem.

---

#### Constructor Summary

Constructs an instance of InterruptedNamingException with
all name resolution fields and explanation initialized to null.

Constructs an instance of InterruptedNamingException using an
explanation of the problem.

Method Summary

- Methods declared in class javax.naming.

NamingException

appendRemainingComponent

,

appendRemainingName

,

getCause

,

getExplanation

,

getRemainingName

,

getResolvedName

,

getResolvedObj

,

getRootCause

,

initCause

,

setRemainingName

,

setResolvedName

,

setResolvedObj

,

setRootCause

,

toString

,

toString

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

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

Methods declared in class javax.naming.

NamingException

appendRemainingComponent

,

appendRemainingName

,

getCause

,

getExplanation

,

getRemainingName

,

getResolvedName

,

getResolvedObj

,

getRootCause

,

initCause

,

setRemainingName

,

setResolvedName

,

setResolvedObj

,

setRootCause

,

toString

,

toString

---

#### Methods declared in class javax.naming. NamingException

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

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

- InterruptedNamingException

```java
public InterruptedNamingException​(
String
explanation)
```

Constructs an instance of InterruptedNamingException using an
explanation of the problem.
All name resolution-related fields are initialized to null.

**Parameters:** explanation

- A possibly null message explaining the problem.
**See Also:** Throwable.getMessage()

- InterruptedNamingException

```java
public InterruptedNamingException()
```

Constructs an instance of InterruptedNamingException with
all name resolution fields and explanation initialized to null.

Constructor Detail

- InterruptedNamingException

```java
public InterruptedNamingException​(
String
explanation)
```

Constructs an instance of InterruptedNamingException using an
explanation of the problem.
All name resolution-related fields are initialized to null.

**Parameters:** explanation

- A possibly null message explaining the problem.
**See Also:** Throwable.getMessage()

- InterruptedNamingException

```java
public InterruptedNamingException()
```

Constructs an instance of InterruptedNamingException with
all name resolution fields and explanation initialized to null.

---

#### Constructor Detail

InterruptedNamingException

```java
public InterruptedNamingException​(
String
explanation)
```

Constructs an instance of InterruptedNamingException using an
explanation of the problem.
All name resolution-related fields are initialized to null.

**Parameters:** explanation

- A possibly null message explaining the problem.
**See Also:** Throwable.getMessage()

---

#### InterruptedNamingException

public InterruptedNamingException​(

String

explanation)

Constructs an instance of InterruptedNamingException using an
explanation of the problem.
All name resolution-related fields are initialized to null.

InterruptedNamingException

```java
public InterruptedNamingException()
```

Constructs an instance of InterruptedNamingException with
all name resolution fields and explanation initialized to null.

---

#### InterruptedNamingException

public InterruptedNamingException()

Constructs an instance of InterruptedNamingException with
all name resolution fields and explanation initialized to null.

---

