# Class UnknownEntityException

**Source:** `java.compiler\javax\lang\model\UnknownEntityException.html`

### Class Description

```java
public class
UnknownEntityException

extends
RuntimeException
```

Superclass of exceptions which indicate that an unknown kind of
entity was encountered. This situation can occur if the language
evolves and new kinds of constructs are introduced. Subclasses of
this exception may be thrown by visitors to indicate that the
visitor was created for a prior version of the language.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### protected UnknownEntityException​(
String
message)

Creates a new

UnknownEntityException

with the specified
detail message.

**Parameters:**
- message

- the detail message

---

### Method Details

*No entries found.*

### Additional Sections

#### Class UnknownEntityException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.RuntimeException
- - javax.lang.model.UnknownEntityException

java.lang.Throwable

- java.lang.Exception
- - java.lang.RuntimeException
- - javax.lang.model.UnknownEntityException

java.lang.Exception

- java.lang.RuntimeException
- - javax.lang.model.UnknownEntityException

java.lang.RuntimeException

- javax.lang.model.UnknownEntityException

javax.lang.model.UnknownEntityException

**All Implemented Interfaces:** Serializable

**Direct Known Subclasses:** UnknownAnnotationValueException

,

UnknownDirectiveException

,

UnknownElementException

,

UnknownTypeException

```java
public class
UnknownEntityException

extends
RuntimeException
```

Superclass of exceptions which indicate that an unknown kind of
entity was encountered. This situation can occur if the language
evolves and new kinds of constructs are introduced. Subclasses of
this exception may be thrown by visitors to indicate that the
visitor was created for a prior version of the language.

**API Note:** A common superclass for exceptions specific to different
kinds of unknown entities allows a single catch block to easily
provide uniform handling of those related conditions.
**Since:** 1.7
**See Also:** UnknownElementException

,

UnknownAnnotationValueException

,

UnknownTypeException

,

Serialized Form

public class

UnknownEntityException

extends

RuntimeException

Superclass of exceptions which indicate that an unknown kind of
entity was encountered. This situation can occur if the language
evolves and new kinds of constructs are introduced. Subclasses of
this exception may be thrown by visitors to indicate that the
visitor was created for a prior version of the language.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

UnknownEntityException

​(

String

message)

Creates a new

UnknownEntityException

with the specified
detail message.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

UnknownEntityException

​(

String

message)

Creates a new

UnknownEntityException

with the specified
detail message.

---

#### Constructor Summary

Creates a new

UnknownEntityException

with the specified
detail message.

Method Summary

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

- UnknownEntityException

```java
protected UnknownEntityException​(
String
message)
```

Creates a new

UnknownEntityException

with the specified
detail message.

**Parameters:** message

- the detail message

Constructor Detail

- UnknownEntityException

```java
protected UnknownEntityException​(
String
message)
```

Creates a new

UnknownEntityException

with the specified
detail message.

**Parameters:** message

- the detail message

---

#### Constructor Detail

UnknownEntityException

```java
protected UnknownEntityException​(
String
message)
```

Creates a new

UnknownEntityException

with the specified
detail message.

**Parameters:** message

- the detail message

---

#### UnknownEntityException

protected UnknownEntityException​(

String

message)

Creates a new

UnknownEntityException

with the specified
detail message.

---

