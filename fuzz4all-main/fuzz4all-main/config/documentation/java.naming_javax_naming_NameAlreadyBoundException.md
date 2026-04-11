# Class NameAlreadyBoundException

**Source:** `java.naming\javax\naming\NameAlreadyBoundException.html`

### Class Description

```java
public class
NameAlreadyBoundException

extends
NamingException
```

This exception is thrown by methods to indicate that
a binding cannot be added because the name is already bound to
another object.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public NameAlreadyBoundException​(
String
explanation)

Constructs a new instance of NameAlreadyBoundException using the
explanation supplied. All other fields default to null.

**Parameters:**
- explanation

- Possibly null additional detail about this exception.

**See Also:**
- Throwable.getMessage()

---

#### public NameAlreadyBoundException()

Constructs a new instance of NameAlreadyBoundException.
All fields are set to null;

---

### Method Details

*No entries found.*

### Additional Sections

#### Class NameAlreadyBoundException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.NameAlreadyBoundException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.NameAlreadyBoundException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.NameAlreadyBoundException

javax.naming.NamingException

- javax.naming.NameAlreadyBoundException

javax.naming.NameAlreadyBoundException

**All Implemented Interfaces:** Serializable

```java
public class
NameAlreadyBoundException

extends
NamingException
```

This exception is thrown by methods to indicate that
a binding cannot be added because the name is already bound to
another object.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Context.bind(javax.naming.Name, java.lang.Object)

,

Context.rebind(javax.naming.Name, java.lang.Object)

,

Context.createSubcontext(javax.naming.Name)

,

DirContext.bind(javax.naming.Name, java.lang.Object, javax.naming.directory.Attributes)

,

DirContext.rebind(javax.naming.Name, java.lang.Object, javax.naming.directory.Attributes)

,

DirContext.createSubcontext(javax.naming.Name, javax.naming.directory.Attributes)

,

Serialized Form

public class

NameAlreadyBoundException

extends

NamingException

This exception is thrown by methods to indicate that
a binding cannot be added because the name is already bound to
another object.

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

NameAlreadyBoundException

()

Constructs a new instance of NameAlreadyBoundException.

NameAlreadyBoundException

​(

String

explanation)

Constructs a new instance of NameAlreadyBoundException using the
explanation supplied.

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

NameAlreadyBoundException

()

Constructs a new instance of NameAlreadyBoundException.

NameAlreadyBoundException

​(

String

explanation)

Constructs a new instance of NameAlreadyBoundException using the
explanation supplied.

---

#### Constructor Summary

Constructs a new instance of NameAlreadyBoundException.

Constructs a new instance of NameAlreadyBoundException using the
explanation supplied.

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

- NameAlreadyBoundException

```java
public NameAlreadyBoundException​(
String
explanation)
```

Constructs a new instance of NameAlreadyBoundException using the
explanation supplied. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
**See Also:** Throwable.getMessage()

- NameAlreadyBoundException

```java
public NameAlreadyBoundException()
```

Constructs a new instance of NameAlreadyBoundException.
All fields are set to null;

Constructor Detail

- NameAlreadyBoundException

```java
public NameAlreadyBoundException​(
String
explanation)
```

Constructs a new instance of NameAlreadyBoundException using the
explanation supplied. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
**See Also:** Throwable.getMessage()

- NameAlreadyBoundException

```java
public NameAlreadyBoundException()
```

Constructs a new instance of NameAlreadyBoundException.
All fields are set to null;

---

#### Constructor Detail

NameAlreadyBoundException

```java
public NameAlreadyBoundException​(
String
explanation)
```

Constructs a new instance of NameAlreadyBoundException using the
explanation supplied. All other fields default to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
**See Also:** Throwable.getMessage()

---

#### NameAlreadyBoundException

public NameAlreadyBoundException​(

String

explanation)

Constructs a new instance of NameAlreadyBoundException using the
explanation supplied. All other fields default to null.

NameAlreadyBoundException

```java
public NameAlreadyBoundException()
```

Constructs a new instance of NameAlreadyBoundException.
All fields are set to null;

---

#### NameAlreadyBoundException

public NameAlreadyBoundException()

Constructs a new instance of NameAlreadyBoundException.
All fields are set to null;

---

