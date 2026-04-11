# Class ConfigurationException

**Source:** `java.naming\javax\naming\ConfigurationException.html`

### Class Description

```java
public class
ConfigurationException

extends
NamingException
```

This exception is thrown when there is a configuration problem.
This can arise when installation of a provider was
not done correctly, or if there are configuration problems with the
server, or if configuration information required to access
the provider or service is malformed or missing.
For example, a request to use SSL as the security protocol when
the service provider software was not configured with the SSL
component would cause such an exception. Another example is
if the provider requires that a URL be specified as one of the
environment properties but the client failed to provide it.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ConfigurationException​(
String
explanation)

Constructs a new instance of ConfigurationException using an
explanation. All other fields default to null.

**Parameters:**
- explanation

- A possibly null string containing
additional detail about this exception.

**See Also:**
- Throwable.getMessage()

---

#### public ConfigurationException()

Constructs a new instance of ConfigurationException with
all name resolution fields and explanation initialized to null.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class ConfigurationException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.ConfigurationException

java.lang.Throwable

- java.lang.Exception
- - javax.naming.NamingException
- - javax.naming.ConfigurationException

java.lang.Exception

- javax.naming.NamingException
- - javax.naming.ConfigurationException

javax.naming.NamingException

- javax.naming.ConfigurationException

javax.naming.ConfigurationException

**All Implemented Interfaces:** Serializable

```java
public class
ConfigurationException

extends
NamingException
```

This exception is thrown when there is a configuration problem.
This can arise when installation of a provider was
not done correctly, or if there are configuration problems with the
server, or if configuration information required to access
the provider or service is malformed or missing.
For example, a request to use SSL as the security protocol when
the service provider software was not configured with the SSL
component would cause such an exception. Another example is
if the provider requires that a URL be specified as one of the
environment properties but the client failed to provide it.

Synchronization and serialization issues that apply to NamingException
apply directly here.

**Since:** 1.3
**See Also:** Serialized Form

public class

ConfigurationException

extends

NamingException

This exception is thrown when there is a configuration problem.
This can arise when installation of a provider was
not done correctly, or if there are configuration problems with the
server, or if configuration information required to access
the provider or service is malformed or missing.
For example, a request to use SSL as the security protocol when
the service provider software was not configured with the SSL
component would cause such an exception. Another example is
if the provider requires that a URL be specified as one of the
environment properties but the client failed to provide it.

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

ConfigurationException

()

Constructs a new instance of ConfigurationException with
all name resolution fields and explanation initialized to null.

ConfigurationException

​(

String

explanation)

Constructs a new instance of ConfigurationException using an
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

ConfigurationException

()

Constructs a new instance of ConfigurationException with
all name resolution fields and explanation initialized to null.

ConfigurationException

​(

String

explanation)

Constructs a new instance of ConfigurationException using an
explanation.

---

#### Constructor Summary

Constructs a new instance of ConfigurationException with
all name resolution fields and explanation initialized to null.

Constructs a new instance of ConfigurationException using an
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

- ConfigurationException

```java
public ConfigurationException​(
String
explanation)
```

Constructs a new instance of ConfigurationException using an
explanation. All other fields default to null.

**Parameters:** explanation

- A possibly null string containing
additional detail about this exception.
**See Also:** Throwable.getMessage()

- ConfigurationException

```java
public ConfigurationException()
```

Constructs a new instance of ConfigurationException with
all name resolution fields and explanation initialized to null.

Constructor Detail

- ConfigurationException

```java
public ConfigurationException​(
String
explanation)
```

Constructs a new instance of ConfigurationException using an
explanation. All other fields default to null.

**Parameters:** explanation

- A possibly null string containing
additional detail about this exception.
**See Also:** Throwable.getMessage()

- ConfigurationException

```java
public ConfigurationException()
```

Constructs a new instance of ConfigurationException with
all name resolution fields and explanation initialized to null.

---

#### Constructor Detail

ConfigurationException

```java
public ConfigurationException​(
String
explanation)
```

Constructs a new instance of ConfigurationException using an
explanation. All other fields default to null.

**Parameters:** explanation

- A possibly null string containing
additional detail about this exception.
**See Also:** Throwable.getMessage()

---

#### ConfigurationException

public ConfigurationException​(

String

explanation)

Constructs a new instance of ConfigurationException using an
explanation. All other fields default to null.

ConfigurationException

```java
public ConfigurationException()
```

Constructs a new instance of ConfigurationException with
all name resolution fields and explanation initialized to null.

---

#### ConfigurationException

public ConfigurationException()

Constructs a new instance of ConfigurationException with
all name resolution fields and explanation initialized to null.

---

