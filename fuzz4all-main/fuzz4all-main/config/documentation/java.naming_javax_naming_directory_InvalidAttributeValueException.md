# Class InvalidAttributeValueException

**Source:** `java.naming\javax\naming\directory\InvalidAttributeValueException.html`

### Class Description

```java
public class
InvalidAttributeValueException

extends
NamingException
```

This class is thrown when an attempt is
made to add to an attribute a value that conflicts with the attribute's
schema definition. This could happen, for example, if attempting
to add an attribute with no value when the attribute is required
to have at least one value, or if attempting to add more than
one value to a single valued-attribute, or if attempting to
add a value that conflicts with the syntax of the attribute.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public InvalidAttributeValueException​(
String
explanation)

Constructs a new instance of InvalidAttributeValueException using
an explanation. All other fields are set to null.

**Parameters:**
- explanation

- Additional detail about this exception. Can be null.

**See Also:**
- Throwable.getMessage()

---

#### public InvalidAttributeValueException()

Constructs a new instance of InvalidAttributeValueException.
All fields are set to null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class InvalidAttributeValueException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.directory.InvalidAttributeValueException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.directory.InvalidAttributeValueException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.directory.InvalidAttributeValueException

javax.naming.NamingException

- javax.naming.directory.InvalidAttributeValueException

javax.naming.directory.InvalidAttributeValueException

**All Implemented Interfaces:** Serializable

```java
public class
InvalidAttributeValueException

extends
NamingException
```

This class is thrown when an attempt is
made to add to an attribute a value that conflicts with the attribute's
schema definition. This could happen, for example, if attempting
to add an attribute with no value when the attribute is required
to have at least one value, or if attempting to add more than
one value to a single valued-attribute, or if attempting to
add a value that conflicts with the syntax of the attribute.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Serialized Form

public class

InvalidAttributeValueException

extends

NamingException

This class is thrown when an attempt is
made to add to an attribute a value that conflicts with the attribute's
schema definition. This could happen, for example, if attempting
to add an attribute with no value when the attribute is required
to have at least one value, or if attempting to add more than
one value to a single valued-attribute, or if attempting to
add a value that conflicts with the syntax of the attribute.

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

InvalidAttributeValueException

()

Constructs a new instance of InvalidAttributeValueException.

InvalidAttributeValueException

​(

String

explanation)

Constructs a new instance of InvalidAttributeValueException using
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

InvalidAttributeValueException

()

Constructs a new instance of InvalidAttributeValueException.

InvalidAttributeValueException

​(

String

explanation)

Constructs a new instance of InvalidAttributeValueException using
an explanation.

---

#### Constructor Summary

Constructs a new instance of InvalidAttributeValueException.

Constructs a new instance of InvalidAttributeValueException using
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

- InvalidAttributeValueException

```java
public InvalidAttributeValueException​(
String
explanation)
```

Constructs a new instance of InvalidAttributeValueException using
an explanation. All other fields are set to null.

**Parameters:** explanation

- Additional detail about this exception. Can be null.
**See Also:** Throwable.getMessage()

- InvalidAttributeValueException

```java
public InvalidAttributeValueException()
```

Constructs a new instance of InvalidAttributeValueException.
All fields are set to null.

Constructor Detail

- InvalidAttributeValueException

```java
public InvalidAttributeValueException​(
String
explanation)
```

Constructs a new instance of InvalidAttributeValueException using
an explanation. All other fields are set to null.

**Parameters:** explanation

- Additional detail about this exception. Can be null.
**See Also:** Throwable.getMessage()

- InvalidAttributeValueException

```java
public InvalidAttributeValueException()
```

Constructs a new instance of InvalidAttributeValueException.
All fields are set to null.

---

#### Constructor Detail

InvalidAttributeValueException

```java
public InvalidAttributeValueException​(
String
explanation)
```

Constructs a new instance of InvalidAttributeValueException using
an explanation. All other fields are set to null.

**Parameters:** explanation

- Additional detail about this exception. Can be null.
**See Also:** Throwable.getMessage()

---

#### InvalidAttributeValueException

public InvalidAttributeValueException​(

String

explanation)

Constructs a new instance of InvalidAttributeValueException using
an explanation. All other fields are set to null.

InvalidAttributeValueException

```java
public InvalidAttributeValueException()
```

Constructs a new instance of InvalidAttributeValueException.
All fields are set to null.

---

#### InvalidAttributeValueException

public InvalidAttributeValueException()

Constructs a new instance of InvalidAttributeValueException.
All fields are set to null.

---

