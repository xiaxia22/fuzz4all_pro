# Class InvalidNameException

**Source:** `java.naming\javax\naming\InvalidNameException.html`

### Class Description

```java
public class
InvalidNameException

extends
NamingException
```

This exception indicates that the name being specified does
not conform to the naming syntax of a naming system.
This exception is thrown by any of the methods that does name
parsing (such as those in Context, DirContext, CompositeName and CompoundName).

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public InvalidNameException​(
String
explanation)

Constructs an instance of InvalidNameException using an
explanation of the problem.
All other fields are initialized to null.

**Parameters:**
- explanation

- A possibly null message explaining the problem.

**See Also:**
- Throwable.getMessage()

---

#### public InvalidNameException()

Constructs an instance of InvalidNameException with
all fields set to null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class InvalidNameException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.InvalidNameException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.InvalidNameException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.InvalidNameException

javax.naming.NamingException

- javax.naming.InvalidNameException

javax.naming.InvalidNameException

**All Implemented Interfaces:** Serializable

```java
public class
InvalidNameException

extends
NamingException
```

This exception indicates that the name being specified does
not conform to the naming syntax of a naming system.
This exception is thrown by any of the methods that does name
parsing (such as those in Context, DirContext, CompositeName and CompoundName).

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Context

,

DirContext

,

CompositeName

,

CompoundName

,

NameParser

,

Serialized Form

public class

InvalidNameException

extends

NamingException

This exception indicates that the name being specified does
not conform to the naming syntax of a naming system.
This exception is thrown by any of the methods that does name
parsing (such as those in Context, DirContext, CompositeName and CompoundName).

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

InvalidNameException

()

Constructs an instance of InvalidNameException with
all fields set to null.

InvalidNameException

​(

String

explanation)

Constructs an instance of InvalidNameException using an
explanation of the problem.

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

InvalidNameException

()

Constructs an instance of InvalidNameException with
all fields set to null.

InvalidNameException

​(

String

explanation)

Constructs an instance of InvalidNameException using an
explanation of the problem.

---

#### Constructor Summary

Constructs an instance of InvalidNameException with
all fields set to null.

Constructs an instance of InvalidNameException using an
explanation of the problem.

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

- InvalidNameException

```java
public InvalidNameException​(
String
explanation)
```

Constructs an instance of InvalidNameException using an
explanation of the problem.
All other fields are initialized to null.

**Parameters:** explanation

- A possibly null message explaining the problem.
**See Also:** Throwable.getMessage()

- InvalidNameException

```java
public InvalidNameException()
```

Constructs an instance of InvalidNameException with
all fields set to null.

Constructor Detail

- InvalidNameException

```java
public InvalidNameException​(
String
explanation)
```

Constructs an instance of InvalidNameException using an
explanation of the problem.
All other fields are initialized to null.

**Parameters:** explanation

- A possibly null message explaining the problem.
**See Also:** Throwable.getMessage()

- InvalidNameException

```java
public InvalidNameException()
```

Constructs an instance of InvalidNameException with
all fields set to null.

---

#### Constructor Detail

InvalidNameException

```java
public InvalidNameException​(
String
explanation)
```

Constructs an instance of InvalidNameException using an
explanation of the problem.
All other fields are initialized to null.

**Parameters:** explanation

- A possibly null message explaining the problem.
**See Also:** Throwable.getMessage()

---

#### InvalidNameException

public InvalidNameException​(

String

explanation)

Constructs an instance of InvalidNameException using an
explanation of the problem.
All other fields are initialized to null.

InvalidNameException

```java
public InvalidNameException()
```

Constructs an instance of InvalidNameException with
all fields set to null.

---

#### InvalidNameException

public InvalidNameException()

Constructs an instance of InvalidNameException with
all fields set to null.

---

