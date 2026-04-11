# Class CertPathTrustManagerParameters

**Source:** `java.base\javax\net\ssl\CertPathTrustManagerParameters.html`

### Class Description

```java
public class
CertPathTrustManagerParameters

extends
Object

implements
ManagerFactoryParameters
```

A wrapper for CertPathParameters. This class is used to pass validation
settings to CertPath based

TrustManager

s using the

TrustManagerFactory.init()

method.

Instances of this class are immutable.

**All Implemented Interfaces:** ManagerFactoryParameters

---

### Field Details

*No entries found.*

### Constructor Details

#### public CertPathTrustManagerParameters​(
CertPathParameters
parameters)

Construct new CertPathTrustManagerParameters from the specified
parameters. The parameters are cloned to protect against subsequent
modification.

**Parameters:**
- parameters

- the CertPathParameters to be used

**Throws:**
- NullPointerException

- if parameters is null

---

### Method Details

#### public
CertPathParameters
getParameters()

Return a clone of the CertPathParameters encapsulated by this class.

**Returns:**
- a clone of the CertPathParameters encapsulated by this class.

---

### Additional Sections

#### Class CertPathTrustManagerParameters

java.lang.Object

- javax.net.ssl.CertPathTrustManagerParameters

javax.net.ssl.CertPathTrustManagerParameters

**All Implemented Interfaces:** ManagerFactoryParameters

```java
public class
CertPathTrustManagerParameters

extends
Object

implements
ManagerFactoryParameters
```

A wrapper for CertPathParameters. This class is used to pass validation
settings to CertPath based

TrustManager

s using the

TrustManagerFactory.init()

method.

Instances of this class are immutable.

**Since:** 1.5
**See Also:** X509TrustManager

,

TrustManagerFactory

,

CertPathParameters

public class

CertPathTrustManagerParameters

extends

Object

implements

ManagerFactoryParameters

A wrapper for CertPathParameters. This class is used to pass validation
settings to CertPath based

TrustManager

s using the

TrustManagerFactory.init()

method.

Instances of this class are immutable.

Instances of this class are immutable.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CertPathTrustManagerParameters

​(

CertPathParameters

parameters)

Construct new CertPathTrustManagerParameters from the specified
parameters.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

CertPathParameters

getParameters

()

Return a clone of the CertPathParameters encapsulated by this class.

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

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

CertPathTrustManagerParameters

​(

CertPathParameters

parameters)

Construct new CertPathTrustManagerParameters from the specified
parameters.

---

#### Constructor Summary

Construct new CertPathTrustManagerParameters from the specified
parameters.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

CertPathParameters

getParameters

()

Return a clone of the CertPathParameters encapsulated by this class.

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Return a clone of the CertPathParameters encapsulated by this class.

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

toString

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

- CertPathTrustManagerParameters

```java
public CertPathTrustManagerParameters​(
CertPathParameters
parameters)
```

Construct new CertPathTrustManagerParameters from the specified
parameters. The parameters are cloned to protect against subsequent
modification.

**Parameters:** parameters

- the CertPathParameters to be used
**Throws:** NullPointerException

- if parameters is null

============ METHOD DETAIL ==========

- Method Detail

- getParameters

```java
public
CertPathParameters
getParameters()
```

Return a clone of the CertPathParameters encapsulated by this class.

**Returns:** a clone of the CertPathParameters encapsulated by this class.

Constructor Detail

- CertPathTrustManagerParameters

```java
public CertPathTrustManagerParameters​(
CertPathParameters
parameters)
```

Construct new CertPathTrustManagerParameters from the specified
parameters. The parameters are cloned to protect against subsequent
modification.

**Parameters:** parameters

- the CertPathParameters to be used
**Throws:** NullPointerException

- if parameters is null

---

#### Constructor Detail

CertPathTrustManagerParameters

```java
public CertPathTrustManagerParameters​(
CertPathParameters
parameters)
```

Construct new CertPathTrustManagerParameters from the specified
parameters. The parameters are cloned to protect against subsequent
modification.

**Parameters:** parameters

- the CertPathParameters to be used
**Throws:** NullPointerException

- if parameters is null

---

#### CertPathTrustManagerParameters

public CertPathTrustManagerParameters​(

CertPathParameters

parameters)

Construct new CertPathTrustManagerParameters from the specified
parameters. The parameters are cloned to protect against subsequent
modification.

Method Detail

- getParameters

```java
public
CertPathParameters
getParameters()
```

Return a clone of the CertPathParameters encapsulated by this class.

**Returns:** a clone of the CertPathParameters encapsulated by this class.

---

#### Method Detail

getParameters

```java
public
CertPathParameters
getParameters()
```

Return a clone of the CertPathParameters encapsulated by this class.

**Returns:** a clone of the CertPathParameters encapsulated by this class.

---

#### getParameters

public

CertPathParameters

getParameters()

Return a clone of the CertPathParameters encapsulated by this class.

---

