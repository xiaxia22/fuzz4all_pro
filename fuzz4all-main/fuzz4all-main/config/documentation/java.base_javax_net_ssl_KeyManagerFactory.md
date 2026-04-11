# Class KeyManagerFactory

**Source:** `java.base\javax\net\ssl\KeyManagerFactory.html`

### Class Description

```java
public class
KeyManagerFactory

extends
Object
```

This class acts as a factory for key managers based on a
source of key material. Each key manager manages a specific
type of key material for use by secure sockets. The key
material is based on a KeyStore and/or provider specific sources.

**Since:** 1.4
**See Also:** KeyManager

---

### Field Details

*No entries found.*

### Constructor Details

#### protected KeyManagerFactory​(
KeyManagerFactorySpi
factorySpi,

Provider
provider,

String
algorithm)

Creates a KeyManagerFactory object.

**Parameters:**
- factorySpi

- the delegate
- provider

- the provider
- algorithm

- the algorithm

---

### Method Details

#### public static final
String
getDefaultAlgorithm()

Obtains the default KeyManagerFactory algorithm name.

The default algorithm can be changed at runtime by setting
the value of the

ssl.KeyManagerFactory.algorithm

security property to the desired algorithm name.

**Returns:**
- the default algorithm name as specified by the

ssl.KeyManagerFactory.algorithm

security property, or an
implementation-specific default if no such property exists.

**See Also:**
- security properties

---

#### public final
String
getAlgorithm()

Returns the algorithm name of this

KeyManagerFactory

object.

This is the same name that was specified in one of the

getInstance

calls that created this

KeyManagerFactory

object.

**Returns:**
- the algorithm name of this

KeyManagerFactory

object.

---

#### public static final
KeyManagerFactory
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException

Returns a

KeyManagerFactory

object that acts as a
factory for key managers.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyManagerFactory object encapsulating the
KeyManagerFactorySpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the standard name of the requested algorithm.
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.

**Returns:**
- the new

KeyManagerFactory

object

**Throws:**
- NoSuchAlgorithmException

- if no

Provider

supports a

KeyManagerFactorySpi

implementation for the
specified algorithm
- NullPointerException

- if

algorithm

is

null

**See Also:**
- Provider

**Implementation Note:**
- The JDK Reference Implementation additionally uses the

jdk.security.provider.preferred

Security

property to determine
the preferred provider order for the specified algorithm. This
may be different than the order of providers returned by

Security.getProviders()

.

---

#### public static final
KeyManagerFactory
getInstance​(
String
algorithm,

String
provider)
throws
NoSuchAlgorithmException
,

NoSuchProviderException

Returns a

KeyManagerFactory

object that acts as a
factory for key managers.

A new KeyManagerFactory object encapsulating the
KeyManagerFactorySpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the standard name of the requested algorithm.
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
- provider

- the name of the provider.

**Returns:**
- the new

KeyManagerFactory

object

**Throws:**
- IllegalArgumentException

- if the provider name is

null

or empty
- NoSuchAlgorithmException

- if a

KeyManagerFactorySpi

implementation for the specified algorithm is not
available from the specified provider
- NoSuchProviderException

- if the specified provider is not
registered in the security provider list
- NullPointerException

- if

algorithm

is

null

**See Also:**
- Provider

---

#### public static final
KeyManagerFactory
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException

Returns a

KeyManagerFactory

object that acts as a
factory for key managers.

A new KeyManagerFactory object encapsulating the
KeyManagerFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:**
- algorithm

- the standard name of the requested algorithm.
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
- provider

- an instance of the provider.

**Returns:**
- the new

KeyManagerFactory

object

**Throws:**
- IllegalArgumentException

- if provider is

null
- NoSuchAlgorithmException

- if a

@KeyManagerFactorySpi

implementation for the specified algorithm is not available
from the specified Provider object
- NullPointerException

- if

algorithm

is

null

**See Also:**
- Provider

---

#### public final
Provider
getProvider()

Returns the provider of this

KeyManagerFactory

object.

**Returns:**
- the provider of this

KeyManagerFactory

object

---

#### public final void init​(
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

The provider typically uses a KeyStore for obtaining
key material for use during secure socket negotiations.
The KeyStore is generally password-protected.

For more flexible initialization, please see

init(ManagerFactoryParameters)

.

**Parameters:**
- ks

- the key store or null
- password

- the password for recovering keys in the KeyStore

**Throws:**
- KeyStoreException

- if this operation fails
- NoSuchAlgorithmException

- if the specified algorithm is not
available from the specified provider.
- UnrecoverableKeyException

- if the key cannot be recovered
(e.g. the given password is wrong).

---

#### public final void init​(
ManagerFactoryParameters
spec)
throws
InvalidAlgorithmParameterException

Initializes this factory with a source of provider-specific
key material.

In some cases, initialization parameters other than a keystore
and password may be needed by a provider. Users of that
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

- if an error is encountered

---

#### public final
KeyManager
[] getKeyManagers()

Returns one key manager for each type of key material.

**Returns:**
- the key managers

**Throws:**
- IllegalStateException

- if the KeyManagerFactory is not initialized

---

### Additional Sections

#### Class KeyManagerFactory

java.lang.Object

- javax.net.ssl.KeyManagerFactory

javax.net.ssl.KeyManagerFactory

```java
public class
KeyManagerFactory

extends
Object
```

This class acts as a factory for key managers based on a
source of key material. Each key manager manages a specific
type of key material for use by secure sockets. The key
material is based on a KeyStore and/or provider specific sources.

**Since:** 1.4
**See Also:** KeyManager

public class

KeyManagerFactory

extends

Object

This class acts as a factory for key managers based on a
source of key material. Each key manager manages a specific
type of key material for use by secure sockets. The key
material is based on a KeyStore and/or provider specific sources.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

KeyManagerFactory

​(

KeyManagerFactorySpi

factorySpi,

Provider

provider,

String

algorithm)

Creates a KeyManagerFactory object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getAlgorithm

()

Returns the algorithm name of this

KeyManagerFactory

object.

static

String

getDefaultAlgorithm

()

Obtains the default KeyManagerFactory algorithm name.

static

KeyManagerFactory

getInstance

​(

String

algorithm)

Returns a

KeyManagerFactory

object that acts as a
factory for key managers.

static

KeyManagerFactory

getInstance

​(

String

algorithm,

String

provider)

Returns a

KeyManagerFactory

object that acts as a
factory for key managers.

static

KeyManagerFactory

getInstance

​(

String

algorithm,

Provider

provider)

Returns a

KeyManagerFactory

object that acts as a
factory for key managers.

KeyManager

[]

getKeyManagers

()

Returns one key manager for each type of key material.

Provider

getProvider

()

Returns the provider of this

KeyManagerFactory

object.

void

init

​(

KeyStore

ks,
char[] password)

Initializes this factory with a source of key material.

void

init

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

Modifier

Constructor

Description

protected

KeyManagerFactory

​(

KeyManagerFactorySpi

factorySpi,

Provider

provider,

String

algorithm)

Creates a KeyManagerFactory object.

---

#### Constructor Summary

Creates a KeyManagerFactory object.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getAlgorithm

()

Returns the algorithm name of this

KeyManagerFactory

object.

static

String

getDefaultAlgorithm

()

Obtains the default KeyManagerFactory algorithm name.

static

KeyManagerFactory

getInstance

​(

String

algorithm)

Returns a

KeyManagerFactory

object that acts as a
factory for key managers.

static

KeyManagerFactory

getInstance

​(

String

algorithm,

String

provider)

Returns a

KeyManagerFactory

object that acts as a
factory for key managers.

static

KeyManagerFactory

getInstance

​(

String

algorithm,

Provider

provider)

Returns a

KeyManagerFactory

object that acts as a
factory for key managers.

KeyManager

[]

getKeyManagers

()

Returns one key manager for each type of key material.

Provider

getProvider

()

Returns the provider of this

KeyManagerFactory

object.

void

init

​(

KeyStore

ks,
char[] password)

Initializes this factory with a source of key material.

void

init

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

Returns the algorithm name of this

KeyManagerFactory

object.

Obtains the default KeyManagerFactory algorithm name.

Returns a

KeyManagerFactory

object that acts as a
factory for key managers.

Returns one key manager for each type of key material.

Returns the provider of this

KeyManagerFactory

object.

Initializes this factory with a source of key material.

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

- KeyManagerFactory

```java
protected KeyManagerFactory​(
KeyManagerFactorySpi
factorySpi,

Provider
provider,

String
algorithm)
```

Creates a KeyManagerFactory object.

**Parameters:** factorySpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** algorithm

- the algorithm

============ METHOD DETAIL ==========

- Method Detail

- getDefaultAlgorithm

```java
public static final
String
getDefaultAlgorithm()
```

Obtains the default KeyManagerFactory algorithm name.

The default algorithm can be changed at runtime by setting
the value of the

ssl.KeyManagerFactory.algorithm

security property to the desired algorithm name.

**Returns:** the default algorithm name as specified by the

ssl.KeyManagerFactory.algorithm

security property, or an
implementation-specific default if no such property exists.
**See Also:** security properties

- getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the algorithm name of this

KeyManagerFactory

object.

This is the same name that was specified in one of the

getInstance

calls that created this

KeyManagerFactory

object.

**Returns:** the algorithm name of this

KeyManagerFactory

object.

- getInstance

```java
public static final
KeyManagerFactory
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a

KeyManagerFactory

object that acts as a
factory for key managers.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyManagerFactory object encapsulating the
KeyManagerFactorySpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Implementation Note:** The JDK Reference Implementation additionally uses the

jdk.security.provider.preferred

Security

property to determine
the preferred provider order for the specified algorithm. This
may be different than the order of providers returned by

Security.getProviders()

.
**Parameters:** algorithm

- the standard name of the requested algorithm.
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
**Returns:** the new

KeyManagerFactory

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

KeyManagerFactorySpi

implementation for the
specified algorithm
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

- getInstance

```java
public static final
KeyManagerFactory
getInstance​(
String
algorithm,

String
provider)
throws
NoSuchAlgorithmException
,

NoSuchProviderException
```

Returns a

KeyManagerFactory

object that acts as a
factory for key managers.

A new KeyManagerFactory object encapsulating the
KeyManagerFactorySpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the standard name of the requested algorithm.
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

KeyManagerFactory

object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

KeyManagerFactorySpi

implementation for the specified algorithm is not
available from the specified provider
**Throws:** NoSuchProviderException

- if the specified provider is not
registered in the security provider list
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

- getInstance

```java
public static final
KeyManagerFactory
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

KeyManagerFactory

object that acts as a
factory for key managers.

A new KeyManagerFactory object encapsulating the
KeyManagerFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the standard name of the requested algorithm.
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
**Parameters:** provider

- an instance of the provider.
**Returns:** the new

KeyManagerFactory

object
**Throws:** IllegalArgumentException

- if provider is

null
**Throws:** NoSuchAlgorithmException

- if a

@KeyManagerFactorySpi

implementation for the specified algorithm is not available
from the specified Provider object
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

- getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this

KeyManagerFactory

object.

**Returns:** the provider of this

KeyManagerFactory

object

- init

```java
public final void init​(
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

The provider typically uses a KeyStore for obtaining
key material for use during secure socket negotiations.
The KeyStore is generally password-protected.

For more flexible initialization, please see

init(ManagerFactoryParameters)

.

**Parameters:** ks

- the key store or null
**Parameters:** password

- the password for recovering keys in the KeyStore
**Throws:** KeyStoreException

- if this operation fails
**Throws:** NoSuchAlgorithmException

- if the specified algorithm is not
available from the specified provider.
**Throws:** UnrecoverableKeyException

- if the key cannot be recovered
(e.g. the given password is wrong).

- init

```java
public final void init​(
ManagerFactoryParameters
spec)
throws
InvalidAlgorithmParameterException
```

Initializes this factory with a source of provider-specific
key material.

In some cases, initialization parameters other than a keystore
and password may be needed by a provider. Users of that
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

- if an error is encountered

- getKeyManagers

```java
public final
KeyManager
[] getKeyManagers()
```

Returns one key manager for each type of key material.

**Returns:** the key managers
**Throws:** IllegalStateException

- if the KeyManagerFactory is not initialized

Constructor Detail

- KeyManagerFactory

```java
protected KeyManagerFactory​(
KeyManagerFactorySpi
factorySpi,

Provider
provider,

String
algorithm)
```

Creates a KeyManagerFactory object.

**Parameters:** factorySpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** algorithm

- the algorithm

---

#### Constructor Detail

KeyManagerFactory

```java
protected KeyManagerFactory​(
KeyManagerFactorySpi
factorySpi,

Provider
provider,

String
algorithm)
```

Creates a KeyManagerFactory object.

**Parameters:** factorySpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** algorithm

- the algorithm

---

#### KeyManagerFactory

protected KeyManagerFactory​(

KeyManagerFactorySpi

factorySpi,

Provider

provider,

String

algorithm)

Creates a KeyManagerFactory object.

Method Detail

- getDefaultAlgorithm

```java
public static final
String
getDefaultAlgorithm()
```

Obtains the default KeyManagerFactory algorithm name.

The default algorithm can be changed at runtime by setting
the value of the

ssl.KeyManagerFactory.algorithm

security property to the desired algorithm name.

**Returns:** the default algorithm name as specified by the

ssl.KeyManagerFactory.algorithm

security property, or an
implementation-specific default if no such property exists.
**See Also:** security properties

- getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the algorithm name of this

KeyManagerFactory

object.

This is the same name that was specified in one of the

getInstance

calls that created this

KeyManagerFactory

object.

**Returns:** the algorithm name of this

KeyManagerFactory

object.

- getInstance

```java
public static final
KeyManagerFactory
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a

KeyManagerFactory

object that acts as a
factory for key managers.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyManagerFactory object encapsulating the
KeyManagerFactorySpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Implementation Note:** The JDK Reference Implementation additionally uses the

jdk.security.provider.preferred

Security

property to determine
the preferred provider order for the specified algorithm. This
may be different than the order of providers returned by

Security.getProviders()

.
**Parameters:** algorithm

- the standard name of the requested algorithm.
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
**Returns:** the new

KeyManagerFactory

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

KeyManagerFactorySpi

implementation for the
specified algorithm
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

- getInstance

```java
public static final
KeyManagerFactory
getInstance​(
String
algorithm,

String
provider)
throws
NoSuchAlgorithmException
,

NoSuchProviderException
```

Returns a

KeyManagerFactory

object that acts as a
factory for key managers.

A new KeyManagerFactory object encapsulating the
KeyManagerFactorySpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the standard name of the requested algorithm.
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

KeyManagerFactory

object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

KeyManagerFactorySpi

implementation for the specified algorithm is not
available from the specified provider
**Throws:** NoSuchProviderException

- if the specified provider is not
registered in the security provider list
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

- getInstance

```java
public static final
KeyManagerFactory
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

KeyManagerFactory

object that acts as a
factory for key managers.

A new KeyManagerFactory object encapsulating the
KeyManagerFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the standard name of the requested algorithm.
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
**Parameters:** provider

- an instance of the provider.
**Returns:** the new

KeyManagerFactory

object
**Throws:** IllegalArgumentException

- if provider is

null
**Throws:** NoSuchAlgorithmException

- if a

@KeyManagerFactorySpi

implementation for the specified algorithm is not available
from the specified Provider object
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

- getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this

KeyManagerFactory

object.

**Returns:** the provider of this

KeyManagerFactory

object

- init

```java
public final void init​(
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

The provider typically uses a KeyStore for obtaining
key material for use during secure socket negotiations.
The KeyStore is generally password-protected.

For more flexible initialization, please see

init(ManagerFactoryParameters)

.

**Parameters:** ks

- the key store or null
**Parameters:** password

- the password for recovering keys in the KeyStore
**Throws:** KeyStoreException

- if this operation fails
**Throws:** NoSuchAlgorithmException

- if the specified algorithm is not
available from the specified provider.
**Throws:** UnrecoverableKeyException

- if the key cannot be recovered
(e.g. the given password is wrong).

- init

```java
public final void init​(
ManagerFactoryParameters
spec)
throws
InvalidAlgorithmParameterException
```

Initializes this factory with a source of provider-specific
key material.

In some cases, initialization parameters other than a keystore
and password may be needed by a provider. Users of that
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

- if an error is encountered

- getKeyManagers

```java
public final
KeyManager
[] getKeyManagers()
```

Returns one key manager for each type of key material.

**Returns:** the key managers
**Throws:** IllegalStateException

- if the KeyManagerFactory is not initialized

---

#### Method Detail

getDefaultAlgorithm

```java
public static final
String
getDefaultAlgorithm()
```

Obtains the default KeyManagerFactory algorithm name.

The default algorithm can be changed at runtime by setting
the value of the

ssl.KeyManagerFactory.algorithm

security property to the desired algorithm name.

**Returns:** the default algorithm name as specified by the

ssl.KeyManagerFactory.algorithm

security property, or an
implementation-specific default if no such property exists.
**See Also:** security properties

---

#### getDefaultAlgorithm

public static final

String

getDefaultAlgorithm()

Obtains the default KeyManagerFactory algorithm name.

The default algorithm can be changed at runtime by setting
the value of the

ssl.KeyManagerFactory.algorithm

security property to the desired algorithm name.

The default algorithm can be changed at runtime by setting
the value of the

ssl.KeyManagerFactory.algorithm

security property to the desired algorithm name.

getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the algorithm name of this

KeyManagerFactory

object.

This is the same name that was specified in one of the

getInstance

calls that created this

KeyManagerFactory

object.

**Returns:** the algorithm name of this

KeyManagerFactory

object.

---

#### getAlgorithm

public final

String

getAlgorithm()

Returns the algorithm name of this

KeyManagerFactory

object.

This is the same name that was specified in one of the

getInstance

calls that created this

KeyManagerFactory

object.

This is the same name that was specified in one of the

getInstance

calls that created this

KeyManagerFactory

object.

getInstance

```java
public static final
KeyManagerFactory
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a

KeyManagerFactory

object that acts as a
factory for key managers.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyManagerFactory object encapsulating the
KeyManagerFactorySpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Implementation Note:** The JDK Reference Implementation additionally uses the

jdk.security.provider.preferred

Security

property to determine
the preferred provider order for the specified algorithm. This
may be different than the order of providers returned by

Security.getProviders()

.
**Parameters:** algorithm

- the standard name of the requested algorithm.
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
**Returns:** the new

KeyManagerFactory

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

KeyManagerFactorySpi

implementation for the
specified algorithm
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

---

#### getInstance

public static final

KeyManagerFactory

getInstance​(

String

algorithm)
throws

NoSuchAlgorithmException

Returns a

KeyManagerFactory

object that acts as a
factory for key managers.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyManagerFactory object encapsulating the
KeyManagerFactorySpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new KeyManagerFactory object encapsulating the
KeyManagerFactorySpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

getInstance

```java
public static final
KeyManagerFactory
getInstance​(
String
algorithm,

String
provider)
throws
NoSuchAlgorithmException
,

NoSuchProviderException
```

Returns a

KeyManagerFactory

object that acts as a
factory for key managers.

A new KeyManagerFactory object encapsulating the
KeyManagerFactorySpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the standard name of the requested algorithm.
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

KeyManagerFactory

object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

KeyManagerFactorySpi

implementation for the specified algorithm is not
available from the specified provider
**Throws:** NoSuchProviderException

- if the specified provider is not
registered in the security provider list
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

---

#### getInstance

public static final

KeyManagerFactory

getInstance​(

String

algorithm,

String

provider)
throws

NoSuchAlgorithmException

,

NoSuchProviderException

Returns a

KeyManagerFactory

object that acts as a
factory for key managers.

A new KeyManagerFactory object encapsulating the
KeyManagerFactorySpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

A new KeyManagerFactory object encapsulating the
KeyManagerFactorySpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

getInstance

```java
public static final
KeyManagerFactory
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

KeyManagerFactory

object that acts as a
factory for key managers.

A new KeyManagerFactory object encapsulating the
KeyManagerFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the standard name of the requested algorithm.
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
**Parameters:** provider

- an instance of the provider.
**Returns:** the new

KeyManagerFactory

object
**Throws:** IllegalArgumentException

- if provider is

null
**Throws:** NoSuchAlgorithmException

- if a

@KeyManagerFactorySpi

implementation for the specified algorithm is not available
from the specified Provider object
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

---

#### getInstance

public static final

KeyManagerFactory

getInstance​(

String

algorithm,

Provider

provider)
throws

NoSuchAlgorithmException

Returns a

KeyManagerFactory

object that acts as a
factory for key managers.

A new KeyManagerFactory object encapsulating the
KeyManagerFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

A new KeyManagerFactory object encapsulating the
KeyManagerFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this

KeyManagerFactory

object.

**Returns:** the provider of this

KeyManagerFactory

object

---

#### getProvider

public final

Provider

getProvider()

Returns the provider of this

KeyManagerFactory

object.

init

```java
public final void init​(
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

The provider typically uses a KeyStore for obtaining
key material for use during secure socket negotiations.
The KeyStore is generally password-protected.

For more flexible initialization, please see

init(ManagerFactoryParameters)

.

**Parameters:** ks

- the key store or null
**Parameters:** password

- the password for recovering keys in the KeyStore
**Throws:** KeyStoreException

- if this operation fails
**Throws:** NoSuchAlgorithmException

- if the specified algorithm is not
available from the specified provider.
**Throws:** UnrecoverableKeyException

- if the key cannot be recovered
(e.g. the given password is wrong).

---

#### init

public final void init​(

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

The provider typically uses a KeyStore for obtaining
key material for use during secure socket negotiations.
The KeyStore is generally password-protected.

For more flexible initialization, please see

init(ManagerFactoryParameters)

.

The provider typically uses a KeyStore for obtaining
key material for use during secure socket negotiations.
The KeyStore is generally password-protected.

For more flexible initialization, please see

init(ManagerFactoryParameters)

.

For more flexible initialization, please see

init(ManagerFactoryParameters)

.

init

```java
public final void init​(
ManagerFactoryParameters
spec)
throws
InvalidAlgorithmParameterException
```

Initializes this factory with a source of provider-specific
key material.

In some cases, initialization parameters other than a keystore
and password may be needed by a provider. Users of that
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

- if an error is encountered

---

#### init

public final void init​(

ManagerFactoryParameters

spec)
throws

InvalidAlgorithmParameterException

Initializes this factory with a source of provider-specific
key material.

In some cases, initialization parameters other than a keystore
and password may be needed by a provider. Users of that
particular provider are expected to pass an implementation of
the appropriate

ManagerFactoryParameters

as
defined by the provider. The provider can then call the
specified methods in the

ManagerFactoryParameters

implementation to obtain the needed information.

In some cases, initialization parameters other than a keystore
and password may be needed by a provider. Users of that
particular provider are expected to pass an implementation of
the appropriate

ManagerFactoryParameters

as
defined by the provider. The provider can then call the
specified methods in the

ManagerFactoryParameters

implementation to obtain the needed information.

getKeyManagers

```java
public final
KeyManager
[] getKeyManagers()
```

Returns one key manager for each type of key material.

**Returns:** the key managers
**Throws:** IllegalStateException

- if the KeyManagerFactory is not initialized

---

#### getKeyManagers

public final

KeyManager

[] getKeyManagers()

Returns one key manager for each type of key material.

---

