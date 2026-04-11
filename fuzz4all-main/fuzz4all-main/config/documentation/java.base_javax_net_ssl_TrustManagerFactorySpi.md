# Class TrustManagerFactorySpi

**Source:** `java.base\javax\net\ssl\TrustManagerFactorySpi.html`

### Class Description

```java
public abstract class
TrustManagerFactorySpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

TrustManagerFactory

class.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular trust manager factory.

**Since:** 1.4
**See Also:** TrustManagerFactory

,

TrustManager

---

### Field Details

*No entries found.*

### Constructor Details

#### public TrustManagerFactorySpi()

*No description found.*

---

### Method Details

#### protected abstract void engineInit​(
KeyStore
ks)
throws
KeyStoreException

Initializes this factory with a source of certificate
authorities and related trust material.

**Parameters:**
- ks

- the key store or null

**Throws:**
- KeyStoreException

- if this operation fails

**See Also:**
- TrustManagerFactory.init(KeyStore)

---

#### protected abstract void engineInit​(
ManagerFactoryParameters
spec)
throws
InvalidAlgorithmParameterException

Initializes this factory with a source of provider-specific
key material.

In some cases, initialization parameters other than a keystore
may be needed by a provider. Users of that
particular provider are expected to pass an implementation of
the appropriate

ManagerFactoryParameters

as
defined by the provider. The provider can then call the
specified methods in the

ManagerFactoryParameters

implementation to obtain the needed information.

**Parameters:**
- spec

- an implementation of a provider-specific parameter
specification

**Throws:**
- InvalidAlgorithmParameterException

- if there is problem
with the parameters

**See Also:**
- TrustManagerFactory.init(ManagerFactoryParameters spec)

---

#### protected abstract
TrustManager
[] engineGetTrustManagers()

Returns one trust manager for each type of trust material.

**Returns:**
- the trust managers

**Throws:**
- IllegalStateException

- if the factory is not initialized.

---

### Additional Sections

#### Class TrustManagerFactorySpi

java.lang.Object

- javax.net.ssl.TrustManagerFactorySpi

javax.net.ssl.TrustManagerFactorySpi

```java
public abstract class
TrustManagerFactorySpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

TrustManagerFactory

class.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular trust manager factory.

**Since:** 1.4
**See Also:** TrustManagerFactory

,

TrustManager

public abstract class

TrustManagerFactorySpi

extends

Object

This class defines the

Service Provider Interface

(

SPI

)
for the

TrustManagerFactory

class.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular trust manager factory.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular trust manager factory.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

TrustManagerFactorySpi

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

protected abstract

TrustManager

[]

engineGetTrustManagers

()

Returns one trust manager for each type of trust material.

protected abstract void

engineInit

​(

KeyStore

ks)

Initializes this factory with a source of certificate
authorities and related trust material.

protected abstract void

engineInit

​(

ManagerFactoryParameters

spec)

Initializes this factory with a source of provider-specific
key material.

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

TrustManagerFactorySpi

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

protected abstract

TrustManager

[]

engineGetTrustManagers

()

Returns one trust manager for each type of trust material.

protected abstract void

engineInit

​(

KeyStore

ks)

Initializes this factory with a source of certificate
authorities and related trust material.

protected abstract void

engineInit

​(

ManagerFactoryParameters

spec)

Initializes this factory with a source of provider-specific
key material.

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

Returns one trust manager for each type of trust material.

Initializes this factory with a source of certificate
authorities and related trust material.

Initializes this factory with a source of provider-specific
key material.

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

- TrustManagerFactorySpi

```java
public TrustManagerFactorySpi()
```

============ METHOD DETAIL ==========

- Method Detail

- engineInit

```java
protected abstract void engineInit​(
KeyStore
ks)
throws
KeyStoreException
```

Initializes this factory with a source of certificate
authorities and related trust material.

**Parameters:** ks

- the key store or null
**Throws:** KeyStoreException

- if this operation fails
**See Also:** TrustManagerFactory.init(KeyStore)

- engineInit

```java
protected abstract void engineInit​(
ManagerFactoryParameters
spec)
throws
InvalidAlgorithmParameterException
```

Initializes this factory with a source of provider-specific
key material.

In some cases, initialization parameters other than a keystore
may be needed by a provider. Users of that
particular provider are expected to pass an implementation of
the appropriate

ManagerFactoryParameters

as
defined by the provider. The provider can then call the
specified methods in the

ManagerFactoryParameters

implementation to obtain the needed information.

**Parameters:** spec

- an implementation of a provider-specific parameter
specification
**Throws:** InvalidAlgorithmParameterException

- if there is problem
with the parameters
**See Also:** TrustManagerFactory.init(ManagerFactoryParameters spec)

- engineGetTrustManagers

```java
protected abstract
TrustManager
[] engineGetTrustManagers()
```

Returns one trust manager for each type of trust material.

**Returns:** the trust managers
**Throws:** IllegalStateException

- if the factory is not initialized.

Constructor Detail

- TrustManagerFactorySpi

```java
public TrustManagerFactorySpi()
```

---

#### Constructor Detail

TrustManagerFactorySpi

```java
public TrustManagerFactorySpi()
```

---

#### TrustManagerFactorySpi

public TrustManagerFactorySpi()

Method Detail

- engineInit

```java
protected abstract void engineInit​(
KeyStore
ks)
throws
KeyStoreException
```

Initializes this factory with a source of certificate
authorities and related trust material.

**Parameters:** ks

- the key store or null
**Throws:** KeyStoreException

- if this operation fails
**See Also:** TrustManagerFactory.init(KeyStore)

- engineInit

```java
protected abstract void engineInit​(
ManagerFactoryParameters
spec)
throws
InvalidAlgorithmParameterException
```

Initializes this factory with a source of provider-specific
key material.

In some cases, initialization parameters other than a keystore
may be needed by a provider. Users of that
particular provider are expected to pass an implementation of
the appropriate

ManagerFactoryParameters

as
defined by the provider. The provider can then call the
specified methods in the

ManagerFactoryParameters

implementation to obtain the needed information.

**Parameters:** spec

- an implementation of a provider-specific parameter
specification
**Throws:** InvalidAlgorithmParameterException

- if there is problem
with the parameters
**See Also:** TrustManagerFactory.init(ManagerFactoryParameters spec)

- engineGetTrustManagers

```java
protected abstract
TrustManager
[] engineGetTrustManagers()
```

Returns one trust manager for each type of trust material.

**Returns:** the trust managers
**Throws:** IllegalStateException

- if the factory is not initialized.

---

#### Method Detail

engineInit

```java
protected abstract void engineInit​(
KeyStore
ks)
throws
KeyStoreException
```

Initializes this factory with a source of certificate
authorities and related trust material.

**Parameters:** ks

- the key store or null
**Throws:** KeyStoreException

- if this operation fails
**See Also:** TrustManagerFactory.init(KeyStore)

---

#### engineInit

protected abstract void engineInit​(

KeyStore

ks)
throws

KeyStoreException

Initializes this factory with a source of certificate
authorities and related trust material.

engineInit

```java
protected abstract void engineInit​(
ManagerFactoryParameters
spec)
throws
InvalidAlgorithmParameterException
```

Initializes this factory with a source of provider-specific
key material.

In some cases, initialization parameters other than a keystore
may be needed by a provider. Users of that
particular provider are expected to pass an implementation of
the appropriate

ManagerFactoryParameters

as
defined by the provider. The provider can then call the
specified methods in the

ManagerFactoryParameters

implementation to obtain the needed information.

**Parameters:** spec

- an implementation of a provider-specific parameter
specification
**Throws:** InvalidAlgorithmParameterException

- if there is problem
with the parameters
**See Also:** TrustManagerFactory.init(ManagerFactoryParameters spec)

---

#### engineInit

protected abstract void engineInit​(

ManagerFactoryParameters

spec)
throws

InvalidAlgorithmParameterException

Initializes this factory with a source of provider-specific
key material.

In some cases, initialization parameters other than a keystore
may be needed by a provider. Users of that
particular provider are expected to pass an implementation of
the appropriate

ManagerFactoryParameters

as
defined by the provider. The provider can then call the
specified methods in the

ManagerFactoryParameters

implementation to obtain the needed information.

In some cases, initialization parameters other than a keystore
may be needed by a provider. Users of that
particular provider are expected to pass an implementation of
the appropriate

ManagerFactoryParameters

as
defined by the provider. The provider can then call the
specified methods in the

ManagerFactoryParameters

implementation to obtain the needed information.

engineGetTrustManagers

```java
protected abstract
TrustManager
[] engineGetTrustManagers()
```

Returns one trust manager for each type of trust material.

**Returns:** the trust managers
**Throws:** IllegalStateException

- if the factory is not initialized.

---

#### engineGetTrustManagers

protected abstract

TrustManager

[] engineGetTrustManagers()

Returns one trust manager for each type of trust material.

---

