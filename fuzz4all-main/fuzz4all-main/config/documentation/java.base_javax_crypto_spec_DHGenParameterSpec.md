# Class DHGenParameterSpec

**Source:** `java.base\javax\crypto\spec\DHGenParameterSpec.html`

### Class Description

```java
public class
DHGenParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This class specifies the set of parameters used for generating
Diffie-Hellman (system) parameters for use in Diffie-Hellman key
agreement. This is typically done by a central
authority.

The central authority, after computing the parameters, must send this
information to the parties looking to agree on a secret key.

**All Implemented Interfaces:** AlgorithmParameterSpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public DHGenParameterSpec​(int primeSize,
int exponentSize)

Constructs a parameter set for the generation of Diffie-Hellman
(system) parameters. The constructed parameter set can be used to
initialize an

AlgorithmParameterGenerator

object for the generation of Diffie-Hellman parameters.

**Parameters:**
- primeSize

- the size (in bits) of the prime modulus.
- exponentSize

- the size (in bits) of the random exponent.

---

### Method Details

#### public int getPrimeSize()

Returns the size in bits of the prime modulus.

**Returns:**
- the size in bits of the prime modulus

---

#### public int getExponentSize()

Returns the size in bits of the random exponent (private value).

**Returns:**
- the size in bits of the random exponent (private value)

---

### Additional Sections

#### Class DHGenParameterSpec

java.lang.Object

- javax.crypto.spec.DHGenParameterSpec

javax.crypto.spec.DHGenParameterSpec

**All Implemented Interfaces:** AlgorithmParameterSpec

```java
public class
DHGenParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This class specifies the set of parameters used for generating
Diffie-Hellman (system) parameters for use in Diffie-Hellman key
agreement. This is typically done by a central
authority.

The central authority, after computing the parameters, must send this
information to the parties looking to agree on a secret key.

**Since:** 1.4
**See Also:** DHParameterSpec

public class

DHGenParameterSpec

extends

Object

implements

AlgorithmParameterSpec

This class specifies the set of parameters used for generating
Diffie-Hellman (system) parameters for use in Diffie-Hellman key
agreement. This is typically done by a central
authority.

The central authority, after computing the parameters, must send this
information to the parties looking to agree on a secret key.

The central authority, after computing the parameters, must send this
information to the parties looking to agree on a secret key.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DHGenParameterSpec

​(int primeSize,
int exponentSize)

Constructs a parameter set for the generation of Diffie-Hellman
(system) parameters.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getExponentSize

()

Returns the size in bits of the random exponent (private value).

int

getPrimeSize

()

Returns the size in bits of the prime modulus.

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

DHGenParameterSpec

​(int primeSize,
int exponentSize)

Constructs a parameter set for the generation of Diffie-Hellman
(system) parameters.

---

#### Constructor Summary

Constructs a parameter set for the generation of Diffie-Hellman
(system) parameters.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getExponentSize

()

Returns the size in bits of the random exponent (private value).

int

getPrimeSize

()

Returns the size in bits of the prime modulus.

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

Returns the size in bits of the random exponent (private value).

Returns the size in bits of the prime modulus.

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

- DHGenParameterSpec

```java
public DHGenParameterSpec​(int primeSize,
int exponentSize)
```

Constructs a parameter set for the generation of Diffie-Hellman
(system) parameters. The constructed parameter set can be used to
initialize an

AlgorithmParameterGenerator

object for the generation of Diffie-Hellman parameters.

**Parameters:** primeSize

- the size (in bits) of the prime modulus.
**Parameters:** exponentSize

- the size (in bits) of the random exponent.

============ METHOD DETAIL ==========

- Method Detail

- getPrimeSize

```java
public int getPrimeSize()
```

Returns the size in bits of the prime modulus.

**Returns:** the size in bits of the prime modulus

- getExponentSize

```java
public int getExponentSize()
```

Returns the size in bits of the random exponent (private value).

**Returns:** the size in bits of the random exponent (private value)

Constructor Detail

- DHGenParameterSpec

```java
public DHGenParameterSpec​(int primeSize,
int exponentSize)
```

Constructs a parameter set for the generation of Diffie-Hellman
(system) parameters. The constructed parameter set can be used to
initialize an

AlgorithmParameterGenerator

object for the generation of Diffie-Hellman parameters.

**Parameters:** primeSize

- the size (in bits) of the prime modulus.
**Parameters:** exponentSize

- the size (in bits) of the random exponent.

---

#### Constructor Detail

DHGenParameterSpec

```java
public DHGenParameterSpec​(int primeSize,
int exponentSize)
```

Constructs a parameter set for the generation of Diffie-Hellman
(system) parameters. The constructed parameter set can be used to
initialize an

AlgorithmParameterGenerator

object for the generation of Diffie-Hellman parameters.

**Parameters:** primeSize

- the size (in bits) of the prime modulus.
**Parameters:** exponentSize

- the size (in bits) of the random exponent.

---

#### DHGenParameterSpec

public DHGenParameterSpec​(int primeSize,
int exponentSize)

Constructs a parameter set for the generation of Diffie-Hellman
(system) parameters. The constructed parameter set can be used to
initialize an

AlgorithmParameterGenerator

object for the generation of Diffie-Hellman parameters.

Method Detail

- getPrimeSize

```java
public int getPrimeSize()
```

Returns the size in bits of the prime modulus.

**Returns:** the size in bits of the prime modulus

- getExponentSize

```java
public int getExponentSize()
```

Returns the size in bits of the random exponent (private value).

**Returns:** the size in bits of the random exponent (private value)

---

#### Method Detail

getPrimeSize

```java
public int getPrimeSize()
```

Returns the size in bits of the prime modulus.

**Returns:** the size in bits of the prime modulus

---

#### getPrimeSize

public int getPrimeSize()

Returns the size in bits of the prime modulus.

getExponentSize

```java
public int getExponentSize()
```

Returns the size in bits of the random exponent (private value).

**Returns:** the size in bits of the random exponent (private value)

---

#### getExponentSize

public int getExponentSize()

Returns the size in bits of the random exponent (private value).

---

