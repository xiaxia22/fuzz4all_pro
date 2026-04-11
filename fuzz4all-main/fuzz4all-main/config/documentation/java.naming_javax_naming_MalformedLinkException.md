# Class MalformedLinkException

**Source:** `java.naming\javax\naming\MalformedLinkException.html`

### Class Description

```java
public class
MalformedLinkException

extends
LinkException
```

This exception is thrown when a malformed link was encountered while
resolving or constructing a link.

Synchronization and serialization issues that apply to LinkException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public MalformedLinkException​(
String
explanation)

Constructs a new instance of MalformedLinkException with an explanation.
All the other fields are initialized to null.

**Parameters:**
- explanation

- A possibly null string containing additional
detail about this exception.

---

#### public MalformedLinkException()

Constructs a new instance of Malformed LinkException.
All fields are initialized to null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class MalformedLinkException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.LinkException
- - javax.naming.MalformedLinkException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.LinkException
- - javax.naming.MalformedLinkException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.LinkException
- - javax.naming.MalformedLinkException

javax.naming.NamingException

- javax.naming.LinkException
- - javax.naming.MalformedLinkException

javax.naming.LinkException

- javax.naming.MalformedLinkException

javax.naming.MalformedLinkException

**All Implemented Interfaces:** Serializable

```java
public class
MalformedLinkException

extends
LinkException
```

This exception is thrown when a malformed link was encountered while
resolving or constructing a link.

Synchronization and serialization issues that apply to LinkException
apply directly here.

**Since:** 1.3
**See Also:** LinkRef.getLinkName()

,

LinkRef

,

Serialized Form

public class

MalformedLinkException

extends

LinkException

This exception is thrown when a malformed link was encountered while
resolving or constructing a link.

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

MalformedLinkException

()

Constructs a new instance of Malformed LinkException.

MalformedLinkException

​(

String

explanation)

Constructs a new instance of MalformedLinkException with an explanation.

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

MalformedLinkException

()

Constructs a new instance of Malformed LinkException.

MalformedLinkException

​(

String

explanation)

Constructs a new instance of MalformedLinkException with an explanation.

---

#### Constructor Summary

Constructs a new instance of Malformed LinkException.

Constructs a new instance of MalformedLinkException with an explanation.

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

- MalformedLinkException

```java
public MalformedLinkException​(
String
explanation)
```

Constructs a new instance of MalformedLinkException with an explanation.
All the other fields are initialized to null.

**Parameters:** explanation

- A possibly null string containing additional
detail about this exception.

- MalformedLinkException

```java
public MalformedLinkException()
```

Constructs a new instance of Malformed LinkException.
All fields are initialized to null.

Constructor Detail

- MalformedLinkException

```java
public MalformedLinkException​(
String
explanation)
```

Constructs a new instance of MalformedLinkException with an explanation.
All the other fields are initialized to null.

**Parameters:** explanation

- A possibly null string containing additional
detail about this exception.

- MalformedLinkException

```java
public MalformedLinkException()
```

Constructs a new instance of Malformed LinkException.
All fields are initialized to null.

---

#### Constructor Detail

MalformedLinkException

```java
public MalformedLinkException​(
String
explanation)
```

Constructs a new instance of MalformedLinkException with an explanation.
All the other fields are initialized to null.

**Parameters:** explanation

- A possibly null string containing additional
detail about this exception.

---

#### MalformedLinkException

public MalformedLinkException​(

String

explanation)

Constructs a new instance of MalformedLinkException with an explanation.
All the other fields are initialized to null.

MalformedLinkException

```java
public MalformedLinkException()
```

Constructs a new instance of Malformed LinkException.
All fields are initialized to null.

---

#### MalformedLinkException

public MalformedLinkException()

Constructs a new instance of Malformed LinkException.
All fields are initialized to null.

---

