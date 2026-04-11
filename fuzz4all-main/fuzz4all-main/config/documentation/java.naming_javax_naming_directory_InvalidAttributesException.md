# Class InvalidAttributesException

**Source:** `java.naming\javax\naming\directory\InvalidAttributesException.html`

### Class Description

```java
public class
InvalidAttributesException

extends
NamingException
```

This exception is thrown when an attempt is
made to add or modify an attribute set that has been specified
incompletely or incorrectly. This could happen, for example,
when attempting to add or modify a binding, or to create a new
subcontext without specifying all the mandatory attributes
required for creation of the object. Another situation in
which this exception is thrown is by specification of incompatible
attributes within the same attribute set, or attributes in conflict
with that specified by the object's schema.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public InvalidAttributesException​(
String
explanation)

Constructs a new instance of InvalidAttributesException using an
explanation. All other fields are set to null.

**Parameters:**
- explanation

- Additional detail about this exception. Can be null.

**See Also:**
- Throwable.getMessage()

---

#### public InvalidAttributesException()

Constructs a new instance of InvalidAttributesException.
All fields are set to null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class InvalidAttributesException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.directory.InvalidAttributesException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.directory.InvalidAttributesException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.directory.InvalidAttributesException

javax.naming.NamingException

- javax.naming.directory.InvalidAttributesException

javax.naming.directory.InvalidAttributesException

**All Implemented Interfaces:** Serializable

```java
public class
InvalidAttributesException

extends
NamingException
```

This exception is thrown when an attempt is
made to add or modify an attribute set that has been specified
incompletely or incorrectly. This could happen, for example,
when attempting to add or modify a binding, or to create a new
subcontext without specifying all the mandatory attributes
required for creation of the object. Another situation in
which this exception is thrown is by specification of incompatible
attributes within the same attribute set, or attributes in conflict
with that specified by the object's schema.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Serialized Form

public class

InvalidAttributesException

extends

NamingException

This exception is thrown when an attempt is
made to add or modify an attribute set that has been specified
incompletely or incorrectly. This could happen, for example,
when attempting to add or modify a binding, or to create a new
subcontext without specifying all the mandatory attributes
required for creation of the object. Another situation in
which this exception is thrown is by specification of incompatible
attributes within the same attribute set, or attributes in conflict
with that specified by the object's schema.

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

InvalidAttributesException

()

Constructs a new instance of InvalidAttributesException.

InvalidAttributesException

​(

String

explanation)

Constructs a new instance of InvalidAttributesException using an
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

InvalidAttributesException

()

Constructs a new instance of InvalidAttributesException.

InvalidAttributesException

​(

String

explanation)

Constructs a new instance of InvalidAttributesException using an
explanation.

---

#### Constructor Summary

Constructs a new instance of InvalidAttributesException.

Constructs a new instance of InvalidAttributesException using an
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

- InvalidAttributesException

```java
public InvalidAttributesException​(
String
explanation)
```

Constructs a new instance of InvalidAttributesException using an
explanation. All other fields are set to null.

**Parameters:** explanation

- Additional detail about this exception. Can be null.
**See Also:** Throwable.getMessage()

- InvalidAttributesException

```java
public InvalidAttributesException()
```

Constructs a new instance of InvalidAttributesException.
All fields are set to null.

Constructor Detail

- InvalidAttributesException

```java
public InvalidAttributesException​(
String
explanation)
```

Constructs a new instance of InvalidAttributesException using an
explanation. All other fields are set to null.

**Parameters:** explanation

- Additional detail about this exception. Can be null.
**See Also:** Throwable.getMessage()

- InvalidAttributesException

```java
public InvalidAttributesException()
```

Constructs a new instance of InvalidAttributesException.
All fields are set to null.

---

#### Constructor Detail

InvalidAttributesException

```java
public InvalidAttributesException​(
String
explanation)
```

Constructs a new instance of InvalidAttributesException using an
explanation. All other fields are set to null.

**Parameters:** explanation

- Additional detail about this exception. Can be null.
**See Also:** Throwable.getMessage()

---

#### InvalidAttributesException

public InvalidAttributesException​(

String

explanation)

Constructs a new instance of InvalidAttributesException using an
explanation. All other fields are set to null.

InvalidAttributesException

```java
public InvalidAttributesException()
```

Constructs a new instance of InvalidAttributesException.
All fields are set to null.

---

#### InvalidAttributesException

public InvalidAttributesException()

Constructs a new instance of InvalidAttributesException.
All fields are set to null.

---

