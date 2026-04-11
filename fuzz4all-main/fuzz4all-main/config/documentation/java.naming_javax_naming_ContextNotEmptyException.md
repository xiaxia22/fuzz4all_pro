# Class ContextNotEmptyException

**Source:** `java.naming\javax\naming\ContextNotEmptyException.html`

### Class Description

```java
public class
ContextNotEmptyException

extends
NamingException
```

This exception is thrown when attempting to destroy a context that
is not empty.

If the program wants to handle this exception in particular, it
should catch ContextNotEmptyException explicitly before attempting to
catch NamingException. For example, after catching ContextNotEmptyException,
the program might try to remove the contents of the context before
reattempting the destroy.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ContextNotEmptyException​(
String
explanation)

Constructs a new instance of ContextNotEmptyException using an
explanation. All other fields default to null.

**Parameters:**
- explanation

- Possibly null string containing
additional detail about this exception.

**See Also:**
- Throwable.getMessage()

---

#### public ContextNotEmptyException()

Constructs a new instance of ContextNotEmptyException with
all name resolution fields and explanation initialized to null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class ContextNotEmptyException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.ContextNotEmptyException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.ContextNotEmptyException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.ContextNotEmptyException

javax.naming.NamingException

- javax.naming.ContextNotEmptyException

javax.naming.ContextNotEmptyException

**All Implemented Interfaces:** Serializable

```java
public class
ContextNotEmptyException

extends
NamingException
```

This exception is thrown when attempting to destroy a context that
is not empty.

If the program wants to handle this exception in particular, it
should catch ContextNotEmptyException explicitly before attempting to
catch NamingException. For example, after catching ContextNotEmptyException,
the program might try to remove the contents of the context before
reattempting the destroy.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Context.destroySubcontext(javax.naming.Name)

,

Serialized Form

public class

ContextNotEmptyException

extends

NamingException

This exception is thrown when attempting to destroy a context that
is not empty.

If the program wants to handle this exception in particular, it
should catch ContextNotEmptyException explicitly before attempting to
catch NamingException. For example, after catching ContextNotEmptyException,
the program might try to remove the contents of the context before
reattempting the destroy.

Synchronization and serialization issues that apply to NamingException
apply directly here.

If the program wants to handle this exception in particular, it
should catch ContextNotEmptyException explicitly before attempting to
catch NamingException. For example, after catching ContextNotEmptyException,
the program might try to remove the contents of the context before
reattempting the destroy.

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

ContextNotEmptyException

()

Constructs a new instance of ContextNotEmptyException with
all name resolution fields and explanation initialized to null.

ContextNotEmptyException

​(

String

explanation)

Constructs a new instance of ContextNotEmptyException using an
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

ContextNotEmptyException

()

Constructs a new instance of ContextNotEmptyException with
all name resolution fields and explanation initialized to null.

ContextNotEmptyException

​(

String

explanation)

Constructs a new instance of ContextNotEmptyException using an
explanation.

---

#### Constructor Summary

Constructs a new instance of ContextNotEmptyException with
all name resolution fields and explanation initialized to null.

Constructs a new instance of ContextNotEmptyException using an
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

- ContextNotEmptyException

```java
public ContextNotEmptyException​(
String
explanation)
```

Constructs a new instance of ContextNotEmptyException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null string containing
additional detail about this exception.
**See Also:** Throwable.getMessage()

- ContextNotEmptyException

```java
public ContextNotEmptyException()
```

Constructs a new instance of ContextNotEmptyException with
all name resolution fields and explanation initialized to null.

Constructor Detail

- ContextNotEmptyException

```java
public ContextNotEmptyException​(
String
explanation)
```

Constructs a new instance of ContextNotEmptyException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null string containing
additional detail about this exception.
**See Also:** Throwable.getMessage()

- ContextNotEmptyException

```java
public ContextNotEmptyException()
```

Constructs a new instance of ContextNotEmptyException with
all name resolution fields and explanation initialized to null.

---

#### Constructor Detail

ContextNotEmptyException

```java
public ContextNotEmptyException​(
String
explanation)
```

Constructs a new instance of ContextNotEmptyException using an
explanation. All other fields default to null.

**Parameters:** explanation

- Possibly null string containing
additional detail about this exception.
**See Also:** Throwable.getMessage()

---

#### ContextNotEmptyException

public ContextNotEmptyException​(

String

explanation)

Constructs a new instance of ContextNotEmptyException using an
explanation. All other fields default to null.

ContextNotEmptyException

```java
public ContextNotEmptyException()
```

Constructs a new instance of ContextNotEmptyException with
all name resolution fields and explanation initialized to null.

---

#### ContextNotEmptyException

public ContextNotEmptyException()

Constructs a new instance of ContextNotEmptyException with
all name resolution fields and explanation initialized to null.

---

