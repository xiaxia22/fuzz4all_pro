# Class KeyManagerFactorySpi

**Source:** `java.base\javax\net\ssl\KeyManagerFactorySpi.html`

### Class Description

```java
public abstract class
KeyManagerFactorySpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

KeyManagerFactory

class.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular key manager factory.

**Since:** 1.4
**See Also:** KeyManagerFactory

,

KeyManager

---

### Field Details

*No entries found.*

### Constructor Details

#### public KeyManagerFactorySpi()

*No description found.*

---

### Method Details

#### protected abstract void engineInit​(
KeyStore
ks,
char[] password)
throws
KeyStoreException
,

NoSuchAlgorithmException
,

UnrecoverableKeyException

Initializes this factory with a source of key material.

**Parameters:**
- ks

- the key store or null
- password

- the password for recovering keys

**Throws:**
- KeyStoreException

- if this operation fails
- NoSuchAlgorithmException

- if the specified algorithm is not
available from the specified provider.
- UnrecoverableKeyException

- if the key cannot be recovered

**See Also:**
- KeyManagerFactory.init(KeyStore, char[])

---

#### protected abstract void engineInit​(
ManagerFactoryParameters
spec)
throws
InvalidAlgorithmParameterException

Initializes this factory with a source of key material.

In some cases, initialization parameters other than a keystore
and password may be needed by a provider. Users of that
particular provider are expected to pass an implementation of
the appropriate

ManagerFactoryParameters

as
defined by the provider. The provider can then call the
specified methods in the ManagerFactoryParameters
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
- KeyManagerFactory.init(ManagerFactoryParameters spec)

---

#### protected abstract
KeyManager
[] engineGetKeyManagers()

Returns one key manager for each type of key material.

**Returns:**
- the key managers

**Throws:**
- IllegalStateException

- if the KeyManagerFactorySpi is not initialized

---

### Additional Sections

#### Class KeyManagerFactorySpi

java.lang.Object

- javax.net.ssl.KeyManagerFactorySpi

javax.net.ssl.KeyManagerFactorySpi

```java
public abstract class
KeyManagerFactorySpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

KeyManagerFactory

class.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular key manager factory.

**Since:** 1.4
**See Also:** KeyManagerFactory

,

KeyManager

public abstract class

KeyManagerFactorySpi

extends

Object

This class defines the

Service Provider Interface

(

SPI

)
for the

KeyManagerFactory

class.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular key manager factory.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a particular key manager factory.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

KeyManagerFactorySpi

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

KeyManager

[]

engineGetKeyManagers

()

Returns one key manager for each type of key material.

protected abstract void

engineInit

​(

KeyStore

ks,
char[] password)

Initializes this factory with a source of key material.

protected abstract void

engineInit

​(

ManagerFactoryParameters

spec)

Initializes this factory with a source of key material.

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

KeyManagerFactorySpi

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

KeyManager

[]

engineGetKeyManagers

()

Returns one key manager for each type of key material.

protected abstract void

engineInit

​(

KeyStore

ks,
char[] password)

Initializes this factory with a source of key material.

protected abstract void

engineInit

​(

ManagerFactoryParameters

spec)

Initializes this factory with a source of key material.

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

Returns one key manager for each type of key material.

Initializes this factory with a source of key material.

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

- KeyManagerFactorySpi

```java
public KeyManagerFactorySpi()
```

============ METHOD DETAIL ==========

- Method Detail

- engineInit

```java
protected abstract void engineInit​(
KeyStore
ks,
char[] password)
throws
KeyStoreException
,

NoSuchAlgorithmException
,

UnrecoverableKeyException
```

Initializes this factory with a source of key material.

**Parameters:** ks

- the key store or null
**Parameters:** password

- the password for recovering keys
**Throws:** KeyStoreException

- if this operation fails
**Throws:** NoSuchAlgorithmException

- if the specified algorithm is not
available from the specified provider.
**Throws:** UnrecoverableKeyException

- if the key cannot be recovered
**See Also:** KeyManagerFactory.init(KeyStore, char[])

- engineInit

```java
protected abstract void engineInit​(
ManagerFactoryParameters
spec)
throws
InvalidAlgorithmParameterException
```

Initializes this factory with a source of key material.

In some cases, initialization parameters other than a keystore
and password may be needed by a provider. Users of that
particular provider are expected to pass an implementation of
the appropriate

ManagerFactoryParameters

as
defined by the provider. The provider can then call the
specified methods in the ManagerFactoryParameters
implementation to obtain the needed information.

**Parameters:** spec

- an implementation of a provider-specific parameter
specification
**Throws:** InvalidAlgorithmParameterException

- if there is problem
with the parameters
**See Also:** KeyManagerFactory.init(ManagerFactoryParameters spec)

- engineGetKeyManagers

```java
protected abstract
KeyManager
[] engineGetKeyManagers()
```

Returns one key manager for each type of key material.

**Returns:** the key managers
**Throws:** IllegalStateException

- if the KeyManagerFactorySpi is not initialized

Constructor Detail

- KeyManagerFactorySpi

```java
public KeyManagerFactorySpi()
```

---

#### Constructor Detail

KeyManagerFactorySpi

```java
public KeyManagerFactorySpi()
```

---

#### KeyManagerFactorySpi

public KeyManagerFactorySpi()

Method Detail

- engineInit

```java
protected abstract void engineInit​(
KeyStore
ks,
char[] password)
throws
KeyStoreException
,

NoSuchAlgorithmException
,

UnrecoverableKeyException
```

Initializes this factory with a source of key material.

**Parameters:** ks

- the key store or null
**Parameters:** password

- the password for recovering keys
**Throws:** KeyStoreException

- if this operation fails
**Throws:** NoSuchAlgorithmException

- if the specified algorithm is not
available from the specified provider.
**Throws:** UnrecoverableKeyException

- if the key cannot be recovered
**See Also:** KeyManagerFactory.init(KeyStore, char[])

- engineInit

```java
protected abstract void engineInit​(
ManagerFactoryParameters
spec)
throws
InvalidAlgorithmParameterException
```

Initializes this factory with a source of key material.

In some cases, initialization parameters other than a keystore
and password may be needed by a provider. Users of that
particular provider are expected to pass an implementation of
the appropriate

ManagerFactoryParameters

as
defined by the provider. The provider can then call the
specified methods in the ManagerFactoryParameters
implementation to obtain the needed information.

**Parameters:** spec

- an implementation of a provider-specific parameter
specification
**Throws:** InvalidAlgorithmParameterException

- if there is problem
with the parameters
**See Also:** KeyManagerFactory.init(ManagerFactoryParameters spec)

- engineGetKeyManagers

```java
protected abstract
KeyManager
[] engineGetKeyManagers()
```

Returns one key manager for each type of key material.

**Returns:** the key managers
**Throws:** IllegalStateException

- if the KeyManagerFactorySpi is not initialized

---

#### Method Detail

engineInit

```java
protected abstract void engineInit​(
KeyStore
ks,
char[] password)
throws
KeyStoreException
,

NoSuchAlgorithmException
,

UnrecoverableKeyException
```

Initializes this factory with a source of key material.

**Parameters:** ks

- the key store or null
**Parameters:** password

- the password for recovering keys
**Throws:** KeyStoreException

- if this operation fails
**Throws:** NoSuchAlgorithmException

- if the specified algorithm is not
available from the specified provider.
**Throws:** UnrecoverableKeyException

- if the key cannot be recovered
**See Also:** KeyManagerFactory.init(KeyStore, char[])

---

#### engineInit

protected abstract void engineInit​(

KeyStore

ks,
char[] password)
throws

KeyStoreException

,

NoSuchAlgorithmException

,

UnrecoverableKeyException

Initializes this factory with a source of key material.

engineInit

```java
protected abstract void engineInit​(
ManagerFactoryParameters
spec)
throws
InvalidAlgorithmParameterException
```

Initializes this factory with a source of key material.

In some cases, initialization parameters other than a keystore
and password may be needed by a provider. Users of that
particular provider are expected to pass an implementation of
the appropriate

ManagerFactoryParameters

as
defined by the provider. The provider can then call the
specified methods in the ManagerFactoryParameters
implementation to obtain the needed information.

**Parameters:** spec

- an implementation of a provider-specific parameter
specification
**Throws:** InvalidAlgorithmParameterException

- if there is problem
with the parameters
**See Also:** KeyManagerFactory.init(ManagerFactoryParameters spec)

---

#### engineInit

protected abstract void engineInit​(

ManagerFactoryParameters

spec)
throws

InvalidAlgorithmParameterException

Initializes this factory with a source of key material.

In some cases, initialization parameters other than a keystore
and password may be needed by a provider. Users of that
particular provider are expected to pass an implementation of
the appropriate

ManagerFactoryParameters

as
defined by the provider. The provider can then call the
specified methods in the ManagerFactoryParameters
implementation to obtain the needed information.

In some cases, initialization parameters other than a keystore
and password may be needed by a provider. Users of that
particular provider are expected to pass an implementation of
the appropriate

ManagerFactoryParameters

as
defined by the provider. The provider can then call the
specified methods in the ManagerFactoryParameters
implementation to obtain the needed information.

engineGetKeyManagers

```java
protected abstract
KeyManager
[] engineGetKeyManagers()
```

Returns one key manager for each type of key material.

**Returns:** the key managers
**Throws:** IllegalStateException

- if the KeyManagerFactorySpi is not initialized

---

#### engineGetKeyManagers

protected abstract

KeyManager

[] engineGetKeyManagers()

Returns one key manager for each type of key material.

---

