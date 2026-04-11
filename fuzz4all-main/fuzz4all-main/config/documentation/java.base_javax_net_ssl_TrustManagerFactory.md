# Class TrustManagerFactory

**Source:** `java.base\javax\net\ssl\TrustManagerFactory.html`

### Class Description

```java
public class
TrustManagerFactory

extends
Object
```

This class acts as a factory for trust managers based on a
source of trust material. Each trust manager manages a specific
type of trust material for use by secure sockets. The trust
material is based on a KeyStore and/or provider-specific sources.

Every implementation of the Java platform is required to support the
following standard

TrustManagerFactory

algorithm:

- PKIX

This algorithm is described in the

TrustManagerFactory section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

**Since:** 1.4
**See Also:** TrustManager

---

### Field Details

*No entries found.*

### Constructor Details

#### protected TrustManagerFactory​(
TrustManagerFactorySpi
factorySpi,

Provider
provider,

String
algorithm)

Creates a TrustManagerFactory object.

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

Obtains the default TrustManagerFactory algorithm name.

The default TrustManager can be changed at runtime by setting
the value of the

ssl.TrustManagerFactory.algorithm

security property to the desired algorithm name.

**Returns:**
- the default algorithm name as specified by the

ssl.TrustManagerFactory.algorithm

security property, or an
implementation-specific default if no such property exists.

**See Also:**
- security properties

---

#### public final
String
getAlgorithm()

Returns the algorithm name of this

TrustManagerFactory

object.

This is the same name that was specified in one of the

getInstance

calls that created this

TrustManagerFactory

object.

**Returns:**
- the algorithm name of this

TrustManagerFactory

object

---

#### public static final
TrustManagerFactory
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException

Returns a

TrustManagerFactory

object that acts as a
factory for trust managers.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new TrustManagerFactory object encapsulating the
TrustManagerFactorySpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:**
- algorithm

- the standard name of the requested trust management
algorithm. See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.

**Returns:**
- the new

TrustManagerFactory

object

**Throws:**
- NoSuchAlgorithmException

- if no

Provider

supports a

TrustManagerFactorySpi

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
TrustManagerFactory
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

TrustManagerFactory

object that acts as a
factory for trust managers.

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

- the standard name of the requested trust management
algorithm. See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
- provider

- the name of the provider.

**Returns:**
- the new

TrustManagerFactory

object

**Throws:**
- IllegalArgumentException

- if the provider name is

null

or empty
- NoSuchAlgorithmException

- if a

TrustManagerFactorySpi

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
TrustManagerFactory
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException

Returns a

TrustManagerFactory

object that acts as a
factory for trust managers.

A new TrustManagerFactory object encapsulating the
TrustManagerFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:**
- algorithm

- the standard name of the requested trust management
algorithm. See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
- provider

- an instance of the provider.

**Returns:**
- the new

TrustManagerFactory

object

**Throws:**
- IllegalArgumentException

- if the provider is

null
- NoSuchAlgorithmException

- if a

TrustManagerFactorySpi

implementation for the specified algorithm is not available
from the specified

Provider

object
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

TrustManagerFactory

object.

**Returns:**
- the provider of this

TrustManagerFactory

object

---

#### public final void init​(
KeyStore
ks)
throws
KeyStoreException

Initializes this factory with a source of certificate
authorities and related trust material.

The provider typically uses a KeyStore as a basis for making
trust decisions.

For more flexible initialization, please see

init(ManagerFactoryParameters)

.

**Parameters:**
- ks

- the key store, or null

**Throws:**
- KeyStoreException

- if this operation fails

---

#### public final void init​(
ManagerFactoryParameters
spec)
throws
InvalidAlgorithmParameterException

Initializes this factory with a source of provider-specific
trust material.

In some cases, initialization parameters other than a keystore
may be needed by a provider. Users of that particular provider
are expected to pass an implementation of the appropriate

ManagerFactoryParameters

as defined by the
provider. The provider can then call the specified methods in
the

ManagerFactoryParameters

implementation to obtain the
needed information.

**Parameters:**
- spec

- an implementation of a provider-specific parameter
specification

**Throws:**
- InvalidAlgorithmParameterException

- if an error is
encountered

---

#### public final
TrustManager
[] getTrustManagers()

Returns one trust manager for each type of trust material.

**Returns:**
- the trust managers

**Throws:**
- IllegalStateException

- if the factory is not initialized.

---

### Additional Sections

#### Class TrustManagerFactory

java.lang.Object

- javax.net.ssl.TrustManagerFactory

javax.net.ssl.TrustManagerFactory

```java
public class
TrustManagerFactory

extends
Object
```

This class acts as a factory for trust managers based on a
source of trust material. Each trust manager manages a specific
type of trust material for use by secure sockets. The trust
material is based on a KeyStore and/or provider-specific sources.

Every implementation of the Java platform is required to support the
following standard

TrustManagerFactory

algorithm:

- PKIX

This algorithm is described in the

TrustManagerFactory section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

**Since:** 1.4
**See Also:** TrustManager

public class

TrustManagerFactory

extends

Object

This class acts as a factory for trust managers based on a
source of trust material. Each trust manager manages a specific
type of trust material for use by secure sockets. The trust
material is based on a KeyStore and/or provider-specific sources.

Every implementation of the Java platform is required to support the
following standard

TrustManagerFactory

algorithm:

- PKIX

This algorithm is described in the

TrustManagerFactory section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

Every implementation of the Java platform is required to support the
following standard

TrustManagerFactory

algorithm:

- PKIX

This algorithm is described in the

TrustManagerFactory section

of the
Java Security Standard Algorithm Names Specification.
Consult the release documentation for your implementation to see if any
other algorithms are supported.

PKIX

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

TrustManagerFactory

​(

TrustManagerFactorySpi

factorySpi,

Provider

provider,

String

algorithm)

Creates a TrustManagerFactory object.

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

TrustManagerFactory

object.

static

String

getDefaultAlgorithm

()

Obtains the default TrustManagerFactory algorithm name.

static

TrustManagerFactory

getInstance

​(

String

algorithm)

Returns a

TrustManagerFactory

object that acts as a
factory for trust managers.

static

TrustManagerFactory

getInstance

​(

String

algorithm,

String

provider)

Returns a

TrustManagerFactory

object that acts as a
factory for trust managers.

static

TrustManagerFactory

getInstance

​(

String

algorithm,

Provider

provider)

Returns a

TrustManagerFactory

object that acts as a
factory for trust managers.

Provider

getProvider

()

Returns the provider of this

TrustManagerFactory

object.

TrustManager

[]

getTrustManagers

()

Returns one trust manager for each type of trust material.

void

init

​(

KeyStore

ks)

Initializes this factory with a source of certificate
authorities and related trust material.

void

init

​(

ManagerFactoryParameters

spec)

Initializes this factory with a source of provider-specific
trust material.

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

TrustManagerFactory

​(

TrustManagerFactorySpi

factorySpi,

Provider

provider,

String

algorithm)

Creates a TrustManagerFactory object.

---

#### Constructor Summary

Creates a TrustManagerFactory object.

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

TrustManagerFactory

object.

static

String

getDefaultAlgorithm

()

Obtains the default TrustManagerFactory algorithm name.

static

TrustManagerFactory

getInstance

​(

String

algorithm)

Returns a

TrustManagerFactory

object that acts as a
factory for trust managers.

static

TrustManagerFactory

getInstance

​(

String

algorithm,

String

provider)

Returns a

TrustManagerFactory

object that acts as a
factory for trust managers.

static

TrustManagerFactory

getInstance

​(

String

algorithm,

Provider

provider)

Returns a

TrustManagerFactory

object that acts as a
factory for trust managers.

Provider

getProvider

()

Returns the provider of this

TrustManagerFactory

object.

TrustManager

[]

getTrustManagers

()

Returns one trust manager for each type of trust material.

void

init

​(

KeyStore

ks)

Initializes this factory with a source of certificate
authorities and related trust material.

void

init

​(

ManagerFactoryParameters

spec)

Initializes this factory with a source of provider-specific
trust material.

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

TrustManagerFactory

object.

Obtains the default TrustManagerFactory algorithm name.

Returns a

TrustManagerFactory

object that acts as a
factory for trust managers.

Returns the provider of this

TrustManagerFactory

object.

Returns one trust manager for each type of trust material.

Initializes this factory with a source of certificate
authorities and related trust material.

Initializes this factory with a source of provider-specific
trust material.

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

- TrustManagerFactory

```java
protected TrustManagerFactory​(
TrustManagerFactorySpi
factorySpi,

Provider
provider,

String
algorithm)
```

Creates a TrustManagerFactory object.

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

Obtains the default TrustManagerFactory algorithm name.

The default TrustManager can be changed at runtime by setting
the value of the

ssl.TrustManagerFactory.algorithm

security property to the desired algorithm name.

**Returns:** the default algorithm name as specified by the

ssl.TrustManagerFactory.algorithm

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

TrustManagerFactory

object.

This is the same name that was specified in one of the

getInstance

calls that created this

TrustManagerFactory

object.

**Returns:** the algorithm name of this

TrustManagerFactory

object

- getInstance

```java
public static final
TrustManagerFactory
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a

TrustManagerFactory

object that acts as a
factory for trust managers.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new TrustManagerFactory object encapsulating the
TrustManagerFactorySpi implementation from the first
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

- the standard name of the requested trust management
algorithm. See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
**Returns:** the new

TrustManagerFactory

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

TrustManagerFactorySpi

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
TrustManagerFactory
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

TrustManagerFactory

object that acts as a
factory for trust managers.

A new KeyManagerFactory object encapsulating the
KeyManagerFactorySpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the standard name of the requested trust management
algorithm. See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

TrustManagerFactory

object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

TrustManagerFactorySpi

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
TrustManagerFactory
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

TrustManagerFactory

object that acts as a
factory for trust managers.

A new TrustManagerFactory object encapsulating the
TrustManagerFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the standard name of the requested trust management
algorithm. See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
**Parameters:** provider

- an instance of the provider.
**Returns:** the new

TrustManagerFactory

object
**Throws:** IllegalArgumentException

- if the provider is

null
**Throws:** NoSuchAlgorithmException

- if a

TrustManagerFactorySpi

implementation for the specified algorithm is not available
from the specified

Provider

object
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

TrustManagerFactory

object.

**Returns:** the provider of this

TrustManagerFactory

object

- init

```java
public final void init​(
KeyStore
ks)
throws
KeyStoreException
```

Initializes this factory with a source of certificate
authorities and related trust material.

The provider typically uses a KeyStore as a basis for making
trust decisions.

For more flexible initialization, please see

init(ManagerFactoryParameters)

.

**Parameters:** ks

- the key store, or null
**Throws:** KeyStoreException

- if this operation fails

- init

```java
public final void init​(
ManagerFactoryParameters
spec)
throws
InvalidAlgorithmParameterException
```

Initializes this factory with a source of provider-specific
trust material.

In some cases, initialization parameters other than a keystore
may be needed by a provider. Users of that particular provider
are expected to pass an implementation of the appropriate

ManagerFactoryParameters

as defined by the
provider. The provider can then call the specified methods in
the

ManagerFactoryParameters

implementation to obtain the
needed information.

**Parameters:** spec

- an implementation of a provider-specific parameter
specification
**Throws:** InvalidAlgorithmParameterException

- if an error is
encountered

- getTrustManagers

```java
public final
TrustManager
[] getTrustManagers()
```

Returns one trust manager for each type of trust material.

**Returns:** the trust managers
**Throws:** IllegalStateException

- if the factory is not initialized.

Constructor Detail

- TrustManagerFactory

```java
protected TrustManagerFactory​(
TrustManagerFactorySpi
factorySpi,

Provider
provider,

String
algorithm)
```

Creates a TrustManagerFactory object.

**Parameters:** factorySpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** algorithm

- the algorithm

---

#### Constructor Detail

TrustManagerFactory

```java
protected TrustManagerFactory​(
TrustManagerFactorySpi
factorySpi,

Provider
provider,

String
algorithm)
```

Creates a TrustManagerFactory object.

**Parameters:** factorySpi

- the delegate
**Parameters:** provider

- the provider
**Parameters:** algorithm

- the algorithm

---

#### TrustManagerFactory

protected TrustManagerFactory​(

TrustManagerFactorySpi

factorySpi,

Provider

provider,

String

algorithm)

Creates a TrustManagerFactory object.

Method Detail

- getDefaultAlgorithm

```java
public static final
String
getDefaultAlgorithm()
```

Obtains the default TrustManagerFactory algorithm name.

The default TrustManager can be changed at runtime by setting
the value of the

ssl.TrustManagerFactory.algorithm

security property to the desired algorithm name.

**Returns:** the default algorithm name as specified by the

ssl.TrustManagerFactory.algorithm

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

TrustManagerFactory

object.

This is the same name that was specified in one of the

getInstance

calls that created this

TrustManagerFactory

object.

**Returns:** the algorithm name of this

TrustManagerFactory

object

- getInstance

```java
public static final
TrustManagerFactory
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a

TrustManagerFactory

object that acts as a
factory for trust managers.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new TrustManagerFactory object encapsulating the
TrustManagerFactorySpi implementation from the first
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

- the standard name of the requested trust management
algorithm. See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
**Returns:** the new

TrustManagerFactory

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

TrustManagerFactorySpi

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
TrustManagerFactory
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

TrustManagerFactory

object that acts as a
factory for trust managers.

A new KeyManagerFactory object encapsulating the
KeyManagerFactorySpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the standard name of the requested trust management
algorithm. See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

TrustManagerFactory

object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

TrustManagerFactorySpi

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
TrustManagerFactory
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

TrustManagerFactory

object that acts as a
factory for trust managers.

A new TrustManagerFactory object encapsulating the
TrustManagerFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the standard name of the requested trust management
algorithm. See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
**Parameters:** provider

- an instance of the provider.
**Returns:** the new

TrustManagerFactory

object
**Throws:** IllegalArgumentException

- if the provider is

null
**Throws:** NoSuchAlgorithmException

- if a

TrustManagerFactorySpi

implementation for the specified algorithm is not available
from the specified

Provider

object
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

TrustManagerFactory

object.

**Returns:** the provider of this

TrustManagerFactory

object

- init

```java
public final void init​(
KeyStore
ks)
throws
KeyStoreException
```

Initializes this factory with a source of certificate
authorities and related trust material.

The provider typically uses a KeyStore as a basis for making
trust decisions.

For more flexible initialization, please see

init(ManagerFactoryParameters)

.

**Parameters:** ks

- the key store, or null
**Throws:** KeyStoreException

- if this operation fails

- init

```java
public final void init​(
ManagerFactoryParameters
spec)
throws
InvalidAlgorithmParameterException
```

Initializes this factory with a source of provider-specific
trust material.

In some cases, initialization parameters other than a keystore
may be needed by a provider. Users of that particular provider
are expected to pass an implementation of the appropriate

ManagerFactoryParameters

as defined by the
provider. The provider can then call the specified methods in
the

ManagerFactoryParameters

implementation to obtain the
needed information.

**Parameters:** spec

- an implementation of a provider-specific parameter
specification
**Throws:** InvalidAlgorithmParameterException

- if an error is
encountered

- getTrustManagers

```java
public final
TrustManager
[] getTrustManagers()
```

Returns one trust manager for each type of trust material.

**Returns:** the trust managers
**Throws:** IllegalStateException

- if the factory is not initialized.

---

#### Method Detail

getDefaultAlgorithm

```java
public static final
String
getDefaultAlgorithm()
```

Obtains the default TrustManagerFactory algorithm name.

The default TrustManager can be changed at runtime by setting
the value of the

ssl.TrustManagerFactory.algorithm

security property to the desired algorithm name.

**Returns:** the default algorithm name as specified by the

ssl.TrustManagerFactory.algorithm

security property, or an
implementation-specific default if no such property exists.
**See Also:** security properties

---

#### getDefaultAlgorithm

public static final

String

getDefaultAlgorithm()

Obtains the default TrustManagerFactory algorithm name.

The default TrustManager can be changed at runtime by setting
the value of the

ssl.TrustManagerFactory.algorithm

security property to the desired algorithm name.

The default TrustManager can be changed at runtime by setting
the value of the

ssl.TrustManagerFactory.algorithm

security property to the desired algorithm name.

getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the algorithm name of this

TrustManagerFactory

object.

This is the same name that was specified in one of the

getInstance

calls that created this

TrustManagerFactory

object.

**Returns:** the algorithm name of this

TrustManagerFactory

object

---

#### getAlgorithm

public final

String

getAlgorithm()

Returns the algorithm name of this

TrustManagerFactory

object.

This is the same name that was specified in one of the

getInstance

calls that created this

TrustManagerFactory

object.

This is the same name that was specified in one of the

getInstance

calls that created this

TrustManagerFactory

object.

getInstance

```java
public static final
TrustManagerFactory
getInstance​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Returns a

TrustManagerFactory

object that acts as a
factory for trust managers.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new TrustManagerFactory object encapsulating the
TrustManagerFactorySpi implementation from the first
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

- the standard name of the requested trust management
algorithm. See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
**Returns:** the new

TrustManagerFactory

object
**Throws:** NoSuchAlgorithmException

- if no

Provider

supports a

TrustManagerFactorySpi

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

TrustManagerFactory

getInstance​(

String

algorithm)
throws

NoSuchAlgorithmException

Returns a

TrustManagerFactory

object that acts as a
factory for trust managers.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new TrustManagerFactory object encapsulating the
TrustManagerFactorySpi implementation from the first
Provider that supports the specified algorithm is returned.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

This method traverses the list of registered security Providers,
starting with the most preferred Provider.
A new TrustManagerFactory object encapsulating the
TrustManagerFactorySpi implementation from the first
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
TrustManagerFactory
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

TrustManagerFactory

object that acts as a
factory for trust managers.

A new KeyManagerFactory object encapsulating the
KeyManagerFactorySpi implementation from the specified provider
is returned. The specified provider must be registered
in the security provider list.

Note that the list of registered providers may be retrieved via
the

Security.getProviders()

method.

**Parameters:** algorithm

- the standard name of the requested trust management
algorithm. See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
**Parameters:** provider

- the name of the provider.
**Returns:** the new

TrustManagerFactory

object
**Throws:** IllegalArgumentException

- if the provider name is

null

or empty
**Throws:** NoSuchAlgorithmException

- if a

TrustManagerFactorySpi

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

TrustManagerFactory

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

TrustManagerFactory

object that acts as a
factory for trust managers.

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
TrustManagerFactory
getInstance​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Returns a

TrustManagerFactory

object that acts as a
factory for trust managers.

A new TrustManagerFactory object encapsulating the
TrustManagerFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

**Parameters:** algorithm

- the standard name of the requested trust management
algorithm. See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
**Parameters:** provider

- an instance of the provider.
**Returns:** the new

TrustManagerFactory

object
**Throws:** IllegalArgumentException

- if the provider is

null
**Throws:** NoSuchAlgorithmException

- if a

TrustManagerFactorySpi

implementation for the specified algorithm is not available
from the specified

Provider

object
**Throws:** NullPointerException

- if

algorithm

is

null
**See Also:** Provider

---

#### getInstance

public static final

TrustManagerFactory

getInstance​(

String

algorithm,

Provider

provider)
throws

NoSuchAlgorithmException

Returns a

TrustManagerFactory

object that acts as a
factory for trust managers.

A new TrustManagerFactory object encapsulating the
TrustManagerFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

A new TrustManagerFactory object encapsulating the
TrustManagerFactorySpi implementation from the specified Provider
object is returned. Note that the specified Provider object
does not have to be registered in the provider list.

getProvider

```java
public final
Provider
getProvider()
```

Returns the provider of this

TrustManagerFactory

object.

**Returns:** the provider of this

TrustManagerFactory

object

---

#### getProvider

public final

Provider

getProvider()

Returns the provider of this

TrustManagerFactory

object.

init

```java
public final void init​(
KeyStore
ks)
throws
KeyStoreException
```

Initializes this factory with a source of certificate
authorities and related trust material.

The provider typically uses a KeyStore as a basis for making
trust decisions.

For more flexible initialization, please see

init(ManagerFactoryParameters)

.

**Parameters:** ks

- the key store, or null
**Throws:** KeyStoreException

- if this operation fails

---

#### init

public final void init​(

KeyStore

ks)
throws

KeyStoreException

Initializes this factory with a source of certificate
authorities and related trust material.

The provider typically uses a KeyStore as a basis for making
trust decisions.

For more flexible initialization, please see

init(ManagerFactoryParameters)

.

The provider typically uses a KeyStore as a basis for making
trust decisions.

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
trust material.

In some cases, initialization parameters other than a keystore
may be needed by a provider. Users of that particular provider
are expected to pass an implementation of the appropriate

ManagerFactoryParameters

as defined by the
provider. The provider can then call the specified methods in
the

ManagerFactoryParameters

implementation to obtain the
needed information.

**Parameters:** spec

- an implementation of a provider-specific parameter
specification
**Throws:** InvalidAlgorithmParameterException

- if an error is
encountered

---

#### init

public final void init​(

ManagerFactoryParameters

spec)
throws

InvalidAlgorithmParameterException

Initializes this factory with a source of provider-specific
trust material.

In some cases, initialization parameters other than a keystore
may be needed by a provider. Users of that particular provider
are expected to pass an implementation of the appropriate

ManagerFactoryParameters

as defined by the
provider. The provider can then call the specified methods in
the

ManagerFactoryParameters

implementation to obtain the
needed information.

In some cases, initialization parameters other than a keystore
may be needed by a provider. Users of that particular provider
are expected to pass an implementation of the appropriate

ManagerFactoryParameters

as defined by the
provider. The provider can then call the specified methods in
the

ManagerFactoryParameters

implementation to obtain the
needed information.

getTrustManagers

```java
public final
TrustManager
[] getTrustManagers()
```

Returns one trust manager for each type of trust material.

**Returns:** the trust managers
**Throws:** IllegalStateException

- if the factory is not initialized.

---

#### getTrustManagers

public final

TrustManager

[] getTrustManagers()

Returns one trust manager for each type of trust material.

---

