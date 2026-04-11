# Class PartialResultException

**Source:** `java.naming\javax\naming\PartialResultException.html`

### Class Description

```java
public class
PartialResultException

extends
NamingException
```

This exception is thrown to indicate that the result being returned
or returned so far is partial, and that the operation cannot
be completed. For example, when listing a context, this exception
indicates that returned results only represents some of the bindings
in the context.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public PartialResultException​(
String
explanation)

Constructs a new instance of the exception using the explanation
message specified. All other fields default to null.

**Parameters:**
- explanation

- Possibly null detail explaining the exception.

---

#### public PartialResultException()

Constructs a new instance of PartialResultException.
All fields default to null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class PartialResultException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.PartialResultException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.PartialResultException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.PartialResultException

javax.naming.NamingException

- javax.naming.PartialResultException

javax.naming.PartialResultException

**All Implemented Interfaces:** Serializable

```java
public class
PartialResultException

extends
NamingException
```

This exception is thrown to indicate that the result being returned
or returned so far is partial, and that the operation cannot
be completed. For example, when listing a context, this exception
indicates that returned results only represents some of the bindings
in the context.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Serialized Form

public class

PartialResultException

extends

NamingException

This exception is thrown to indicate that the result being returned
or returned so far is partial, and that the operation cannot
be completed. For example, when listing a context, this exception
indicates that returned results only represents some of the bindings
in the context.

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

PartialResultException

()

Constructs a new instance of PartialResultException.

PartialResultException

​(

String

explanation)

Constructs a new instance of the exception using the explanation
message specified.

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

PartialResultException

()

Constructs a new instance of PartialResultException.

PartialResultException

​(

String

explanation)

Constructs a new instance of the exception using the explanation
message specified.

---

#### Constructor Summary

Constructs a new instance of PartialResultException.

Constructs a new instance of the exception using the explanation
message specified.

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

- PartialResultException

```java
public PartialResultException​(
String
explanation)
```

Constructs a new instance of the exception using the explanation
message specified. All other fields default to null.

**Parameters:** explanation

- Possibly null detail explaining the exception.

- PartialResultException

```java
public PartialResultException()
```

Constructs a new instance of PartialResultException.
All fields default to null.

Constructor Detail

- PartialResultException

```java
public PartialResultException​(
String
explanation)
```

Constructs a new instance of the exception using the explanation
message specified. All other fields default to null.

**Parameters:** explanation

- Possibly null detail explaining the exception.

- PartialResultException

```java
public PartialResultException()
```

Constructs a new instance of PartialResultException.
All fields default to null.

---

#### Constructor Detail

PartialResultException

```java
public PartialResultException​(
String
explanation)
```

Constructs a new instance of the exception using the explanation
message specified. All other fields default to null.

**Parameters:** explanation

- Possibly null detail explaining the exception.

---

#### PartialResultException

public PartialResultException​(

String

explanation)

Constructs a new instance of the exception using the explanation
message specified. All other fields default to null.

PartialResultException

```java
public PartialResultException()
```

Constructs a new instance of PartialResultException.
All fields default to null.

---

#### PartialResultException

public PartialResultException()

Constructs a new instance of PartialResultException.
All fields default to null.

---

