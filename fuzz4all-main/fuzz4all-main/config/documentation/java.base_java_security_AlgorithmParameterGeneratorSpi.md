# Class AlgorithmParameterGeneratorSpi

**Source:** `java.base\java\security\AlgorithmParameterGeneratorSpi.html`

### Class Description

```java
public abstract class
AlgorithmParameterGeneratorSpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

AlgorithmParameterGenerator

class, which
is used to generate a set of parameters to be used with a certain algorithm.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a parameter generator for a particular algorithm.

In case the client does not explicitly initialize the
AlgorithmParameterGenerator (via a call to an

engineInit

method), each provider must supply (and document) a default initialization.
See the Keysize Restriction sections of the

JDK Providers

document for information on the AlgorithmParameterGenerator defaults
used by JDK providers.
However, note that defaults may vary across different providers.
Additionally, the default value for a provider may change in a future
version. Therefore, it is recommended to explicitly initialize the
AlgorithmParameterGenerator instead of relying on provider-specific defaults.

**Since:** 1.2
**See Also:** AlgorithmParameterGenerator

,

AlgorithmParameters

,

AlgorithmParameterSpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public AlgorithmParameterGeneratorSpi()

*No description found.*

---

### Method Details

#### protected abstract void engineInit​(int size,

SecureRandom
random)

Initializes this parameter generator for a certain size
and source of randomness.

**Parameters:**
- size

- the size (number of bits).
- random

- the source of randomness.

---

#### protected abstract void engineInit​(
AlgorithmParameterSpec
genParamSpec,

SecureRandom
random)
throws
InvalidAlgorithmParameterException

Initializes this parameter generator with a set of
algorithm-specific parameter generation values.

**Parameters:**
- genParamSpec

- the set of algorithm-specific parameter generation values.
- random

- the source of randomness.

**Throws:**
- InvalidAlgorithmParameterException

- if the given parameter
generation values are inappropriate for this parameter generator.

---

#### protected abstract
AlgorithmParameters
engineGenerateParameters()

Generates the parameters.

**Returns:**
- the new AlgorithmParameters object.

---

### Additional Sections

#### Class AlgorithmParameterGeneratorSpi

java.lang.Object

- java.security.AlgorithmParameterGeneratorSpi

java.security.AlgorithmParameterGeneratorSpi

```java
public abstract class
AlgorithmParameterGeneratorSpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

AlgorithmParameterGenerator

class, which
is used to generate a set of parameters to be used with a certain algorithm.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a parameter generator for a particular algorithm.

In case the client does not explicitly initialize the
AlgorithmParameterGenerator (via a call to an

engineInit

method), each provider must supply (and document) a default initialization.
See the Keysize Restriction sections of the

JDK Providers

document for information on the AlgorithmParameterGenerator defaults
used by JDK providers.
However, note that defaults may vary across different providers.
Additionally, the default value for a provider may change in a future
version. Therefore, it is recommended to explicitly initialize the
AlgorithmParameterGenerator instead of relying on provider-specific defaults.

**Since:** 1.2
**See Also:** AlgorithmParameterGenerator

,

AlgorithmParameters

,

AlgorithmParameterSpec

public abstract class

AlgorithmParameterGeneratorSpi

extends

Object

This class defines the

Service Provider Interface

(

SPI

)
for the

AlgorithmParameterGenerator

class, which
is used to generate a set of parameters to be used with a certain algorithm.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a parameter generator for a particular algorithm.

In case the client does not explicitly initialize the
AlgorithmParameterGenerator (via a call to an

engineInit

method), each provider must supply (and document) a default initialization.
See the Keysize Restriction sections of the

JDK Providers

document for information on the AlgorithmParameterGenerator defaults
used by JDK providers.
However, note that defaults may vary across different providers.
Additionally, the default value for a provider may change in a future
version. Therefore, it is recommended to explicitly initialize the
AlgorithmParameterGenerator instead of relying on provider-specific defaults.

All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a parameter generator for a particular algorithm.

In case the client does not explicitly initialize the
AlgorithmParameterGenerator (via a call to an

engineInit

method), each provider must supply (and document) a default initialization.
See the Keysize Restriction sections of the

JDK Providers

document for information on the AlgorithmParameterGenerator defaults
used by JDK providers.
However, note that defaults may vary across different providers.
Additionally, the default value for a provider may change in a future
version. Therefore, it is recommended to explicitly initialize the
AlgorithmParameterGenerator instead of relying on provider-specific defaults.

In case the client does not explicitly initialize the
AlgorithmParameterGenerator (via a call to an

engineInit

method), each provider must supply (and document) a default initialization.
See the Keysize Restriction sections of the

JDK Providers

document for information on the AlgorithmParameterGenerator defaults
used by JDK providers.
However, note that defaults may vary across different providers.
Additionally, the default value for a provider may change in a future
version. Therefore, it is recommended to explicitly initialize the
AlgorithmParameterGenerator instead of relying on provider-specific defaults.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

AlgorithmParameterGeneratorSpi

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

AlgorithmParameters

engineGenerateParameters

()

Generates the parameters.

protected abstract void

engineInit

​(int size,

SecureRandom

random)

Initializes this parameter generator for a certain size
and source of randomness.

protected abstract void

engineInit

​(

AlgorithmParameterSpec

genParamSpec,

SecureRandom

random)

Initializes this parameter generator with a set of
algorithm-specific parameter generation values.

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

AlgorithmParameterGeneratorSpi

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

AlgorithmParameters

engineGenerateParameters

()

Generates the parameters.

protected abstract void

engineInit

​(int size,

SecureRandom

random)

Initializes this parameter generator for a certain size
and source of randomness.

protected abstract void

engineInit

​(

AlgorithmParameterSpec

genParamSpec,

SecureRandom

random)

Initializes this parameter generator with a set of
algorithm-specific parameter generation values.

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

Generates the parameters.

Initializes this parameter generator for a certain size
and source of randomness.

Initializes this parameter generator with a set of
algorithm-specific parameter generation values.

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

- AlgorithmParameterGeneratorSpi

```java
public AlgorithmParameterGeneratorSpi()
```

============ METHOD DETAIL ==========

- Method Detail

- engineInit

```java
protected abstract void engineInit​(int size,

SecureRandom
random)
```

Initializes this parameter generator for a certain size
and source of randomness.

**Parameters:** size

- the size (number of bits).
**Parameters:** random

- the source of randomness.

- engineInit

```java
protected abstract void engineInit​(
AlgorithmParameterSpec
genParamSpec,

SecureRandom
random)
throws
InvalidAlgorithmParameterException
```

Initializes this parameter generator with a set of
algorithm-specific parameter generation values.

**Parameters:** genParamSpec

- the set of algorithm-specific parameter generation values.
**Parameters:** random

- the source of randomness.
**Throws:** InvalidAlgorithmParameterException

- if the given parameter
generation values are inappropriate for this parameter generator.

- engineGenerateParameters

```java
protected abstract
AlgorithmParameters
engineGenerateParameters()
```

Generates the parameters.

**Returns:** the new AlgorithmParameters object.

Constructor Detail

- AlgorithmParameterGeneratorSpi

```java
public AlgorithmParameterGeneratorSpi()
```

---

#### Constructor Detail

AlgorithmParameterGeneratorSpi

```java
public AlgorithmParameterGeneratorSpi()
```

---

#### AlgorithmParameterGeneratorSpi

public AlgorithmParameterGeneratorSpi()

Method Detail

- engineInit

```java
protected abstract void engineInit​(int size,

SecureRandom
random)
```

Initializes this parameter generator for a certain size
and source of randomness.

**Parameters:** size

- the size (number of bits).
**Parameters:** random

- the source of randomness.

- engineInit

```java
protected abstract void engineInit​(
AlgorithmParameterSpec
genParamSpec,

SecureRandom
random)
throws
InvalidAlgorithmParameterException
```

Initializes this parameter generator with a set of
algorithm-specific parameter generation values.

**Parameters:** genParamSpec

- the set of algorithm-specific parameter generation values.
**Parameters:** random

- the source of randomness.
**Throws:** InvalidAlgorithmParameterException

- if the given parameter
generation values are inappropriate for this parameter generator.

- engineGenerateParameters

```java
protected abstract
AlgorithmParameters
engineGenerateParameters()
```

Generates the parameters.

**Returns:** the new AlgorithmParameters object.

---

#### Method Detail

engineInit

```java
protected abstract void engineInit​(int size,

SecureRandom
random)
```

Initializes this parameter generator for a certain size
and source of randomness.

**Parameters:** size

- the size (number of bits).
**Parameters:** random

- the source of randomness.

---

#### engineInit

protected abstract void engineInit​(int size,

SecureRandom

random)

Initializes this parameter generator for a certain size
and source of randomness.

engineInit

```java
protected abstract void engineInit​(
AlgorithmParameterSpec
genParamSpec,

SecureRandom
random)
throws
InvalidAlgorithmParameterException
```

Initializes this parameter generator with a set of
algorithm-specific parameter generation values.

**Parameters:** genParamSpec

- the set of algorithm-specific parameter generation values.
**Parameters:** random

- the source of randomness.
**Throws:** InvalidAlgorithmParameterException

- if the given parameter
generation values are inappropriate for this parameter generator.

---

#### engineInit

protected abstract void engineInit​(

AlgorithmParameterSpec

genParamSpec,

SecureRandom

random)
throws

InvalidAlgorithmParameterException

Initializes this parameter generator with a set of
algorithm-specific parameter generation values.

engineGenerateParameters

```java
protected abstract
AlgorithmParameters
engineGenerateParameters()
```

Generates the parameters.

**Returns:** the new AlgorithmParameters object.

---

#### engineGenerateParameters

protected abstract

AlgorithmParameters

engineGenerateParameters()

Generates the parameters.

---

