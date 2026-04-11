# Class LinkLoopException

**Source:** `java.naming\javax\naming\LinkLoopException.html`

### Class Description

```java
public class
LinkLoopException

extends
LinkException
```

This exception is thrown when
a loop was detected while attempting to resolve a link, or an implementation
specific limit on link counts has been reached.

Synchronization and serialization issues that apply to LinkException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public LinkLoopException​(
String
explanation)

Constructs a new instance of LinkLoopException with an explanation.
All the other fields are initialized to null.

**Parameters:**
- explanation

- A possibly null string containing additional
detail about this exception.

**See Also:**
- Throwable.getMessage()

---

#### public LinkLoopException()

Constructs a new instance of LinkLoopException.
All the non-link-related and link-related fields are initialized to null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class LinkLoopException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.LinkException
- - javax.naming.LinkLoopException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.LinkException
- - javax.naming.LinkLoopException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.LinkException
- - javax.naming.LinkLoopException

javax.naming.NamingException

- javax.naming.LinkException
- - javax.naming.LinkLoopException

javax.naming.LinkException

- javax.naming.LinkLoopException

javax.naming.LinkLoopException

**All Implemented Interfaces:** Serializable

```java
public class
LinkLoopException

extends
LinkException
```

This exception is thrown when
a loop was detected while attempting to resolve a link, or an implementation
specific limit on link counts has been reached.

Synchronization and serialization issues that apply to LinkException
apply directly here.

**Since:** 1.3
**See Also:** LinkRef

,

Serialized Form

public class

LinkLoopException

extends

LinkException

This exception is thrown when
a loop was detected while attempting to resolve a link, or an implementation
specific limit on link counts has been reached.

Synchronization and serialization issues that apply to LinkException
apply directly here.

Synchronization and serialization issues that apply to LinkException
apply directly here.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class javax.naming.

LinkException

linkExplanation

,

linkRemainingName

,

linkResolvedName

,

linkResolvedObj

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

LinkLoopException

()

Constructs a new instance of LinkLoopException.

LinkLoopException

​(

String

explanation)

Constructs a new instance of LinkLoopException with an explanation.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class javax.naming.

LinkException

getLinkExplanation

,

getLinkRemainingName

,

getLinkResolvedName

,

getLinkResolvedObj

,

setLinkExplanation

,

setLinkRemainingName

,

setLinkResolvedName

,

setLinkResolvedObj

,

toString

,

toString

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

LinkException

linkExplanation

,

linkRemainingName

,

linkResolvedName

,

linkResolvedObj

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

LinkException

linkExplanation

,

linkRemainingName

,

linkResolvedName

,

linkResolvedObj

---

#### Fields declared in class javax.naming. LinkException

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

LinkLoopException

()

Constructs a new instance of LinkLoopException.

LinkLoopException

​(

String

explanation)

Constructs a new instance of LinkLoopException with an explanation.

---

#### Constructor Summary

Constructs a new instance of LinkLoopException.

Constructs a new instance of LinkLoopException with an explanation.

Method Summary

- Methods declared in class javax.naming.

LinkException

getLinkExplanation

,

getLinkRemainingName

,

getLinkResolvedName

,

getLinkResolvedObj

,

setLinkExplanation

,

setLinkRemainingName

,

setLinkResolvedName

,

setLinkResolvedObj

,

toString

,

toString

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

LinkException

getLinkExplanation

,

getLinkRemainingName

,

getLinkResolvedName

,

getLinkResolvedObj

,

setLinkExplanation

,

setLinkRemainingName

,

setLinkResolvedName

,

setLinkResolvedObj

,

toString

,

toString

---

#### Methods declared in class javax.naming. LinkException

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

- LinkLoopException

```java
public LinkLoopException​(
String
explanation)
```

Constructs a new instance of LinkLoopException with an explanation.
All the other fields are initialized to null.

**Parameters:** explanation

- A possibly null string containing additional
detail about this exception.
**See Also:** Throwable.getMessage()

- LinkLoopException

```java
public LinkLoopException()
```

Constructs a new instance of LinkLoopException.
All the non-link-related and link-related fields are initialized to null.

Constructor Detail

- LinkLoopException

```java
public LinkLoopException​(
String
explanation)
```

Constructs a new instance of LinkLoopException with an explanation.
All the other fields are initialized to null.

**Parameters:** explanation

- A possibly null string containing additional
detail about this exception.
**See Also:** Throwable.getMessage()

- LinkLoopException

```java
public LinkLoopException()
```

Constructs a new instance of LinkLoopException.
All the non-link-related and link-related fields are initialized to null.

---

#### Constructor Detail

LinkLoopException

```java
public LinkLoopException​(
String
explanation)
```

Constructs a new instance of LinkLoopException with an explanation.
All the other fields are initialized to null.

**Parameters:** explanation

- A possibly null string containing additional
detail about this exception.
**See Also:** Throwable.getMessage()

---

#### LinkLoopException

public LinkLoopException​(

String

explanation)

Constructs a new instance of LinkLoopException with an explanation.
All the other fields are initialized to null.

LinkLoopException

```java
public LinkLoopException()
```

Constructs a new instance of LinkLoopException.
All the non-link-related and link-related fields are initialized to null.

---

#### LinkLoopException

public LinkLoopException()

Constructs a new instance of LinkLoopException.
All the non-link-related and link-related fields are initialized to null.

---

