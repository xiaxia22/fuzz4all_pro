# Class NoInitialContextException

**Source:** `java.naming\javax\naming\NoInitialContextException.html`

### Class Description

```java
public class
NoInitialContextException

extends
NamingException
```

This exception is thrown when no initial context implementation
can be created. The policy of how an initial context implementation
is selected is described in the documentation of the InitialContext class.

This exception can be thrown during any interaction with the
InitialContext, not only when the InitialContext is constructed.
For example, the implementation of the initial context might lazily
retrieve the context only when actual methods are invoked on it.
The application should not have any dependency on when the existence
of an initial context is determined.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public NoInitialContextException()

Constructs an instance of NoInitialContextException.
All fields are initialized to null.

---

#### public NoInitialContextException​(
String
explanation)

Constructs an instance of NoInitialContextException with an
explanation. All other fields are initialized to null.

**Parameters:**
- explanation

- Possibly null additional detail about this exception.

**See Also:**
- Throwable.getMessage()

---

### Method Details

*No entries found.*

### Additional Sections

#### Class NoInitialContextException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.NoInitialContextException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.NoInitialContextException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.NoInitialContextException

javax.naming.NamingException

- javax.naming.NoInitialContextException

javax.naming.NoInitialContextException

**All Implemented Interfaces:** Serializable

```java
public class
NoInitialContextException

extends
NamingException
```

This exception is thrown when no initial context implementation
can be created. The policy of how an initial context implementation
is selected is described in the documentation of the InitialContext class.

This exception can be thrown during any interaction with the
InitialContext, not only when the InitialContext is constructed.
For example, the implementation of the initial context might lazily
retrieve the context only when actual methods are invoked on it.
The application should not have any dependency on when the existence
of an initial context is determined.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** InitialContext

,

InitialDirContext

,

NamingManager.getInitialContext(java.util.Hashtable<?, ?>)

,

NamingManager.setInitialContextFactoryBuilder(javax.naming.spi.InitialContextFactoryBuilder)

,

Serialized Form

public class

NoInitialContextException

extends

NamingException

This exception is thrown when no initial context implementation
can be created. The policy of how an initial context implementation
is selected is described in the documentation of the InitialContext class.

This exception can be thrown during any interaction with the
InitialContext, not only when the InitialContext is constructed.
For example, the implementation of the initial context might lazily
retrieve the context only when actual methods are invoked on it.
The application should not have any dependency on when the existence
of an initial context is determined.

Synchronization and serialization issues that apply to NamingException
apply directly here.

This exception can be thrown during any interaction with the
InitialContext, not only when the InitialContext is constructed.
For example, the implementation of the initial context might lazily
retrieve the context only when actual methods are invoked on it.
The application should not have any dependency on when the existence
of an initial context is determined.

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

NoInitialContextException

()

Constructs an instance of NoInitialContextException.

NoInitialContextException

​(

String

explanation)

Constructs an instance of NoInitialContextException with an
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

NoInitialContextException

()

Constructs an instance of NoInitialContextException.

NoInitialContextException

​(

String

explanation)

Constructs an instance of NoInitialContextException with an
explanation.

---

#### Constructor Summary

Constructs an instance of NoInitialContextException.

Constructs an instance of NoInitialContextException with an
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

- NoInitialContextException

```java
public NoInitialContextException()
```

Constructs an instance of NoInitialContextException.
All fields are initialized to null.

- NoInitialContextException

```java
public NoInitialContextException​(
String
explanation)
```

Constructs an instance of NoInitialContextException with an
explanation. All other fields are initialized to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
**See Also:** Throwable.getMessage()

Constructor Detail

- NoInitialContextException

```java
public NoInitialContextException()
```

Constructs an instance of NoInitialContextException.
All fields are initialized to null.

- NoInitialContextException

```java
public NoInitialContextException​(
String
explanation)
```

Constructs an instance of NoInitialContextException with an
explanation. All other fields are initialized to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
**See Also:** Throwable.getMessage()

---

#### Constructor Detail

NoInitialContextException

```java
public NoInitialContextException()
```

Constructs an instance of NoInitialContextException.
All fields are initialized to null.

---

#### NoInitialContextException

public NoInitialContextException()

Constructs an instance of NoInitialContextException.
All fields are initialized to null.

NoInitialContextException

```java
public NoInitialContextException​(
String
explanation)
```

Constructs an instance of NoInitialContextException with an
explanation. All other fields are initialized to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
**See Also:** Throwable.getMessage()

---

#### NoInitialContextException

public NoInitialContextException​(

String

explanation)

Constructs an instance of NoInitialContextException with an
explanation. All other fields are initialized to null.

---

