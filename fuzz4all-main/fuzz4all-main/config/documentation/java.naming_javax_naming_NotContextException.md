# Class NotContextException

**Source:** `java.naming\javax\naming\NotContextException.html`

### Class Description

```java
public class
NotContextException

extends
NamingException
```

This exception is thrown when a naming operation proceeds to a point
where a context is required to continue the operation, but the
resolved object is not a context. For example, Context.destroy() requires
that the named object be a context. If it is not, NotContextException
is thrown. Another example is a non-context being encountered during
the resolution phase of the Context methods.

It is also thrown when a particular subtype of context is required,
such as a DirContext, and the resolved object is a context but not of
the required subtype.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public NotContextException​(
String
explanation)

Constructs a new instance of NotContextException using an
explanation. All other fields default to null.

**Parameters:**
- explanation

- Possibly null additional detail about this exception.

**See Also:**
- Throwable.getMessage()

---

#### public NotContextException()

Constructs a new instance of NotContextException.
All fields default to null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class NotContextException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.NotContextException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.NotContextException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.NotContextException

javax.naming.NamingException

- javax.naming.NotContextException

javax.naming.NotContextException

**All Implemented Interfaces:** Serializable

```java
public class
NotContextException

extends
NamingException
```

This exception is thrown when a naming operation proceeds to a point
where a context is required to continue the operation, but the
resolved object is not a context. For example, Context.destroy() requires
that the named object be a context. If it is not, NotContextException
is thrown. Another example is a non-context being encountered during
the resolution phase of the Context methods.

It is also thrown when a particular subtype of context is required,
such as a DirContext, and the resolved object is a context but not of
the required subtype.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Context.destroySubcontext(javax.naming.Name)

,

Serialized Form

public class

NotContextException

extends

NamingException

This exception is thrown when a naming operation proceeds to a point
where a context is required to continue the operation, but the
resolved object is not a context. For example, Context.destroy() requires
that the named object be a context. If it is not, NotContextException
is thrown. Another example is a non-context being encountered during
the resolution phase of the Context methods.

It is also thrown when a particular subtype of context is required,
such as a DirContext, and the resolved object is a context but not of
the required subtype.

Synchronization and serialization issues that apply to NamingException
apply directly here.

It is also thrown when a particular subtype of context is required,
such as a DirContext, and the resolved object is a context but not of
the required subtype.

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

NotContextException

()

Constructs a new instance of NotContextException.

NotContextException

​(

String

explanation)

Constructs a new instance of NotContextException using an
explanation.

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

NotContextException

()

Constructs a new instance of NotContextException.

NotContextException

​(

String

explanation)

Constructs a new instance of NotContextException using an
explanation.

---

#### Constructor Summary

Constructs a new instance of NotContextException.

Constructs a new instance of NotContextException using an
explanation.

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

- NotContextException

```java
public NotContextException​(
String
explanation)
```

Constructs a new instance of NotContextException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
**See Also:** Throwable.getMessage()

- NotContextException

```java
public NotContextException()
```

Constructs a new instance of NotContextException.
All fields default to null.

Constructor Detail

- NotContextException

```java
public NotContextException​(
String
explanation)
```

Constructs a new instance of NotContextException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
**See Also:** Throwable.getMessage()

- NotContextException

```java
public NotContextException()
```

Constructs a new instance of NotContextException.
All fields default to null.

---

#### Constructor Detail

NotContextException

```java
public NotContextException​(
String
explanation)
```

Constructs a new instance of NotContextException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
**See Also:** Throwable.getMessage()

---

#### NotContextException

public NotContextException​(

String

explanation)

Constructs a new instance of NotContextException using an
explanation. All other fields default to null.

NotContextException

```java
public NotContextException()
```

Constructs a new instance of NotContextException.
All fields default to null.

---

#### NotContextException

public NotContextException()

Constructs a new instance of NotContextException.
All fields default to null.

---

