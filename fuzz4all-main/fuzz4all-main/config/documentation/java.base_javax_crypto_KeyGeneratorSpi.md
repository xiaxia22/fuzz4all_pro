# Class KeyGeneratorSpi

**Source:** `java.base\javax\crypto\KeyGeneratorSpi.html`

### Class Description

```java
public abstract class
KeyGeneratorSpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

KeyGenerator

class.
All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a key generator for a particular algorithm.

In case the client does not explicitly initialize the KeyGenerator
(via a call to an

init

method), each provider must
supply (and document) a default initialization.
See the Keysize Restriction sections of the

JDK Providers

document for information on the KeyGenerator defaults used by
JDK providers.
However, note that defaults may vary across different providers.
Additionally, the default value for a provider may change in a future
version. Therefore, it is recommended to explicitly initialize the
KeyGenerator instead of relying on provider-specific defaults.

**Since:** 1.4
**See Also:** SecretKey

---

### Field Details

*No entries found.*

### Constructor Details

#### public KeyGeneratorSpi()

*No description found.*

---

### Method Details

#### protected abstract void engineInit​(
SecureRandom
random)

Initializes the key generator.

**Parameters:**
- random

- the source of randomness for this generator

---

#### protected abstract void engineInit​(
AlgorithmParameterSpec
params,

SecureRandom
random)
throws
InvalidAlgorithmParameterException

Initializes the key generator with the specified parameter
set and a user-provided source of randomness.

**Parameters:**
- params

- the key generation parameters
- random

- the source of randomness for this key generator

**Throws:**
- InvalidAlgorithmParameterException

- if

params

is
inappropriate for this key generator

---

#### protected abstract void engineInit​(int keysize,

SecureRandom
random)

Initializes this key generator for a certain keysize, using the given
source of randomness.

**Parameters:**
- keysize

- the keysize. This is an algorithm-specific metric,
specified in number of bits.
- random

- the source of randomness for this key generator

**Throws:**
- InvalidParameterException

- if the keysize is wrong or not
supported.

---

#### protected abstract
SecretKey
engineGenerateKey()

Generates a secret key.

**Returns:**
- the new key

---

### Additional Sections

#### Class KeyGeneratorSpi

java.lang.Object

- javax.crypto.KeyGeneratorSpi

javax.crypto.KeyGeneratorSpi

```java
public abstract class
KeyGeneratorSpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

KeyGenerator

class.
All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a key generator for a particular algorithm.

In case the client does not explicitly initialize the KeyGenerator
(via a call to an

init

method), each provider must
supply (and document) a default initialization.
See the Keysize Restriction sections of the

JDK Providers

document for information on the KeyGenerator defaults used by
JDK providers.
However, note that defaults may vary across different providers.
Additionally, the default value for a provider may change in a future
version. Therefore, it is recommended to explicitly initialize the
KeyGenerator instead of relying on provider-specific defaults.

**Since:** 1.4
**See Also:** SecretKey

public abstract class

KeyGeneratorSpi

extends

Object

This class defines the

Service Provider Interface

(

SPI

)
for the

KeyGenerator

class.
All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a key generator for a particular algorithm.

In case the client does not explicitly initialize the KeyGenerator
(via a call to an

init

method), each provider must
supply (and document) a default initialization.
See the Keysize Restriction sections of the

JDK Providers

document for information on the KeyGenerator defaults used by
JDK providers.
However, note that defaults may vary across different providers.
Additionally, the default value for a provider may change in a future
version. Therefore, it is recommended to explicitly initialize the
KeyGenerator instead of relying on provider-specific defaults.

In case the client does not explicitly initialize the KeyGenerator
(via a call to an

init

method), each provider must
supply (and document) a default initialization.
See the Keysize Restriction sections of the

JDK Providers

document for information on the KeyGenerator defaults used by
JDK providers.
However, note that defaults may vary across different providers.
Additionally, the default value for a provider may change in a future
version. Therefore, it is recommended to explicitly initialize the
KeyGenerator instead of relying on provider-specific defaults.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

KeyGeneratorSpi

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

SecretKey

engineGenerateKey

()

Generates a secret key.

protected abstract void

engineInit

​(int keysize,

SecureRandom

random)

Initializes this key generator for a certain keysize, using the given
source of randomness.

protected abstract void

engineInit

​(

SecureRandom

random)

Initializes the key generator.

protected abstract void

engineInit

​(

AlgorithmParameterSpec

params,

SecureRandom

random)

Initializes the key generator with the specified parameter
set and a user-provided source of randomness.

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

KeyGeneratorSpi

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

SecretKey

engineGenerateKey

()

Generates a secret key.

protected abstract void

engineInit

​(int keysize,

SecureRandom

random)

Initializes this key generator for a certain keysize, using the given
source of randomness.

protected abstract void

engineInit

​(

SecureRandom

random)

Initializes the key generator.

protected abstract void

engineInit

​(

AlgorithmParameterSpec

params,

SecureRandom

random)

Initializes the key generator with the specified parameter
set and a user-provided source of randomness.

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

Generates a secret key.

Initializes this key generator for a certain keysize, using the given
source of randomness.

Initializes the key generator.

Initializes the key generator with the specified parameter
set and a user-provided source of randomness.

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

- KeyGeneratorSpi

```java
public KeyGeneratorSpi()
```

============ METHOD DETAIL ==========

- Method Detail

- engineInit

```java
protected abstract void engineInit​(
SecureRandom
random)
```

Initializes the key generator.

**Parameters:** random

- the source of randomness for this generator

- engineInit

```java
protected abstract void engineInit​(
AlgorithmParameterSpec
params,

SecureRandom
random)
throws
InvalidAlgorithmParameterException
```

Initializes the key generator with the specified parameter
set and a user-provided source of randomness.

**Parameters:** params

- the key generation parameters
**Parameters:** random

- the source of randomness for this key generator
**Throws:** InvalidAlgorithmParameterException

- if

params

is
inappropriate for this key generator

- engineInit

```java
protected abstract void engineInit​(int keysize,

SecureRandom
random)
```

Initializes this key generator for a certain keysize, using the given
source of randomness.

**Parameters:** keysize

- the keysize. This is an algorithm-specific metric,
specified in number of bits.
**Parameters:** random

- the source of randomness for this key generator
**Throws:** InvalidParameterException

- if the keysize is wrong or not
supported.

- engineGenerateKey

```java
protected abstract
SecretKey
engineGenerateKey()
```

Generates a secret key.

**Returns:** the new key

Constructor Detail

- KeyGeneratorSpi

```java
public KeyGeneratorSpi()
```

---

#### Constructor Detail

KeyGeneratorSpi

```java
public KeyGeneratorSpi()
```

---

#### KeyGeneratorSpi

public KeyGeneratorSpi()

Method Detail

- engineInit

```java
protected abstract void engineInit​(
SecureRandom
random)
```

Initializes the key generator.

**Parameters:** random

- the source of randomness for this generator

- engineInit

```java
protected abstract void engineInit​(
AlgorithmParameterSpec
params,

SecureRandom
random)
throws
InvalidAlgorithmParameterException
```

Initializes the key generator with the specified parameter
set and a user-provided source of randomness.

**Parameters:** params

- the key generation parameters
**Parameters:** random

- the source of randomness for this key generator
**Throws:** InvalidAlgorithmParameterException

- if

params

is
inappropriate for this key generator

- engineInit

```java
protected abstract void engineInit​(int keysize,

SecureRandom
random)
```

Initializes this key generator for a certain keysize, using the given
source of randomness.

**Parameters:** keysize

- the keysize. This is an algorithm-specific metric,
specified in number of bits.
**Parameters:** random

- the source of randomness for this key generator
**Throws:** InvalidParameterException

- if the keysize is wrong or not
supported.

- engineGenerateKey

```java
protected abstract
SecretKey
engineGenerateKey()
```

Generates a secret key.

**Returns:** the new key

---

#### Method Detail

engineInit

```java
protected abstract void engineInit​(
SecureRandom
random)
```

Initializes the key generator.

**Parameters:** random

- the source of randomness for this generator

---

#### engineInit

protected abstract void engineInit​(

SecureRandom

random)

Initializes the key generator.

engineInit

```java
protected abstract void engineInit​(
AlgorithmParameterSpec
params,

SecureRandom
random)
throws
InvalidAlgorithmParameterException
```

Initializes the key generator with the specified parameter
set and a user-provided source of randomness.

**Parameters:** params

- the key generation parameters
**Parameters:** random

- the source of randomness for this key generator
**Throws:** InvalidAlgorithmParameterException

- if

params

is
inappropriate for this key generator

---

#### engineInit

protected abstract void engineInit​(

AlgorithmParameterSpec

params,

SecureRandom

random)
throws

InvalidAlgorithmParameterException

Initializes the key generator with the specified parameter
set and a user-provided source of randomness.

engineInit

```java
protected abstract void engineInit​(int keysize,

SecureRandom
random)
```

Initializes this key generator for a certain keysize, using the given
source of randomness.

**Parameters:** keysize

- the keysize. This is an algorithm-specific metric,
specified in number of bits.
**Parameters:** random

- the source of randomness for this key generator
**Throws:** InvalidParameterException

- if the keysize is wrong or not
supported.

---

#### engineInit

protected abstract void engineInit​(int keysize,

SecureRandom

random)

Initializes this key generator for a certain keysize, using the given
source of randomness.

engineGenerateKey

```java
protected abstract
SecretKey
engineGenerateKey()
```

Generates a secret key.

**Returns:** the new key

---

#### engineGenerateKey

protected abstract

SecretKey

engineGenerateKey()

Generates a secret key.

---

