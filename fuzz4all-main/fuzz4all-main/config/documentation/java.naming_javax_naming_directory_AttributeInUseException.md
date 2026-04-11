# Class AttributeInUseException

**Source:** `java.naming\javax\naming\directory\AttributeInUseException.html`

### Class Description

```java
public class
AttributeInUseException

extends
NamingException
```

This exception is thrown when an operation attempts
to add an attribute that already exists.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public AttributeInUseException​(
String
explanation)

Constructs a new instance of AttributeInUseException with
an explanation. All other fields are set to null.

**Parameters:**
- explanation

- Possibly null additional detail about this exception.

**See Also:**
- Throwable.getMessage()

---

#### public AttributeInUseException()

Constructs a new instance of AttributeInUseException.
All fields are initialized to null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class AttributeInUseException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.directory.AttributeInUseException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.directory.AttributeInUseException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.directory.AttributeInUseException

javax.naming.NamingException

- javax.naming.directory.AttributeInUseException

javax.naming.directory.AttributeInUseException

**All Implemented Interfaces:** Serializable

```java
public class
AttributeInUseException

extends
NamingException
```

This exception is thrown when an operation attempts
to add an attribute that already exists.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** DirContext.modifyAttributes(javax.naming.Name, int, javax.naming.directory.Attributes)

,

Serialized Form

public class

AttributeInUseException

extends

NamingException

This exception is thrown when an operation attempts
to add an attribute that already exists.

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

AttributeInUseException

()

Constructs a new instance of AttributeInUseException.

AttributeInUseException

​(

String

explanation)

Constructs a new instance of AttributeInUseException with
an explanation.

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

AttributeInUseException

()

Constructs a new instance of AttributeInUseException.

AttributeInUseException

​(

String

explanation)

Constructs a new instance of AttributeInUseException with
an explanation.

---

#### Constructor Summary

Constructs a new instance of AttributeInUseException.

Constructs a new instance of AttributeInUseException with
an explanation.

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

- AttributeInUseException

```java
public AttributeInUseException​(
String
explanation)
```

Constructs a new instance of AttributeInUseException with
an explanation. All other fields are set to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
**See Also:** Throwable.getMessage()

- AttributeInUseException

```java
public AttributeInUseException()
```

Constructs a new instance of AttributeInUseException.
All fields are initialized to null.

Constructor Detail

- AttributeInUseException

```java
public AttributeInUseException​(
String
explanation)
```

Constructs a new instance of AttributeInUseException with
an explanation. All other fields are set to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
**See Also:** Throwable.getMessage()

- AttributeInUseException

```java
public AttributeInUseException()
```

Constructs a new instance of AttributeInUseException.
All fields are initialized to null.

---

#### Constructor Detail

AttributeInUseException

```java
public AttributeInUseException​(
String
explanation)
```

Constructs a new instance of AttributeInUseException with
an explanation. All other fields are set to null.

**Parameters:** explanation

- Possibly null additional detail about this exception.
**See Also:** Throwable.getMessage()

---

#### AttributeInUseException

public AttributeInUseException​(

String

explanation)

Constructs a new instance of AttributeInUseException with
an explanation. All other fields are set to null.

AttributeInUseException

```java
public AttributeInUseException()
```

Constructs a new instance of AttributeInUseException.
All fields are initialized to null.

---

#### AttributeInUseException

public AttributeInUseException()

Constructs a new instance of AttributeInUseException.
All fields are initialized to null.

---

