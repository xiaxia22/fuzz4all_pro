# Class SchemaViolationException

**Source:** `java.naming\javax\naming\directory\SchemaViolationException.html`

### Class Description

```java
public class
SchemaViolationException

extends
NamingException
```

This exception is thrown when a method
in some ways violates the schema. An example of schema violation
is modifying attributes of an object that violates the object's
schema definition. Another example is renaming or moving an object
to a part of the namespace that violates the namespace's
schema definition.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public SchemaViolationException()

Constructs a new instance of SchemaViolationException.
All fields are set to null.

---

#### public SchemaViolationException​(
String
explanation)

Constructs a new instance of SchemaViolationException
using the explanation supplied. All other fields are set to null.

**Parameters:**
- explanation

- Detail about this exception. Can be null.

**See Also:**
- Throwable.getMessage()

---

### Method Details

*No entries found.*

### Additional Sections

#### Class SchemaViolationException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.directory.SchemaViolationException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.directory.SchemaViolationException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.directory.SchemaViolationException

javax.naming.NamingException

- javax.naming.directory.SchemaViolationException

javax.naming.directory.SchemaViolationException

**All Implemented Interfaces:** Serializable

```java
public class
SchemaViolationException

extends
NamingException
```

This exception is thrown when a method
in some ways violates the schema. An example of schema violation
is modifying attributes of an object that violates the object's
schema definition. Another example is renaming or moving an object
to a part of the namespace that violates the namespace's
schema definition.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Context.bind(javax.naming.Name, java.lang.Object)

,

DirContext.bind(javax.naming.Name, java.lang.Object, javax.naming.directory.Attributes)

,

Context.rebind(javax.naming.Name, java.lang.Object)

,

DirContext.rebind(javax.naming.Name, java.lang.Object, javax.naming.directory.Attributes)

,

DirContext.createSubcontext(javax.naming.Name, javax.naming.directory.Attributes)

,

Context.createSubcontext(javax.naming.Name)

,

DirContext.modifyAttributes(javax.naming.Name, int, javax.naming.directory.Attributes)

,

Serialized Form

public class

SchemaViolationException

extends

NamingException

This exception is thrown when a method
in some ways violates the schema. An example of schema violation
is modifying attributes of an object that violates the object's
schema definition. Another example is renaming or moving an object
to a part of the namespace that violates the namespace's
schema definition.

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

SchemaViolationException

()

Constructs a new instance of SchemaViolationException.

SchemaViolationException

​(

String

explanation)

Constructs a new instance of SchemaViolationException
using the explanation supplied.

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

SchemaViolationException

()

Constructs a new instance of SchemaViolationException.

SchemaViolationException

​(

String

explanation)

Constructs a new instance of SchemaViolationException
using the explanation supplied.

---

#### Constructor Summary

Constructs a new instance of SchemaViolationException.

Constructs a new instance of SchemaViolationException
using the explanation supplied.

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

- SchemaViolationException

```java
public SchemaViolationException()
```

Constructs a new instance of SchemaViolationException.
All fields are set to null.

- SchemaViolationException

```java
public SchemaViolationException​(
String
explanation)
```

Constructs a new instance of SchemaViolationException
using the explanation supplied. All other fields are set to null.

**Parameters:** explanation

- Detail about this exception. Can be null.
**See Also:** Throwable.getMessage()

Constructor Detail

- SchemaViolationException

```java
public SchemaViolationException()
```

Constructs a new instance of SchemaViolationException.
All fields are set to null.

- SchemaViolationException

```java
public SchemaViolationException​(
String
explanation)
```

Constructs a new instance of SchemaViolationException
using the explanation supplied. All other fields are set to null.

**Parameters:** explanation

- Detail about this exception. Can be null.
**See Also:** Throwable.getMessage()

---

#### Constructor Detail

SchemaViolationException

```java
public SchemaViolationException()
```

Constructs a new instance of SchemaViolationException.
All fields are set to null.

---

#### SchemaViolationException

public SchemaViolationException()

Constructs a new instance of SchemaViolationException.
All fields are set to null.

SchemaViolationException

```java
public SchemaViolationException​(
String
explanation)
```

Constructs a new instance of SchemaViolationException
using the explanation supplied. All other fields are set to null.

**Parameters:** explanation

- Detail about this exception. Can be null.
**See Also:** Throwable.getMessage()

---

#### SchemaViolationException

public SchemaViolationException​(

String

explanation)

Constructs a new instance of SchemaViolationException
using the explanation supplied. All other fields are set to null.

---

