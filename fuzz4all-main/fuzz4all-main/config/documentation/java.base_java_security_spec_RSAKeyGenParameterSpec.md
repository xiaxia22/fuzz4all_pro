# Class RSAKeyGenParameterSpec

**Source:** `java.base\java\security\spec\RSAKeyGenParameterSpec.html`

### Class Description

```java
public class
RSAKeyGenParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This class specifies the set of parameters used to generate an RSA
key pair.

**All Implemented Interfaces:** AlgorithmParameterSpec

---

### Field Details

#### public static final
BigInteger
F0

The public-exponent value F0 = 3.

---

#### public static final
BigInteger
F4

The public exponent-value F4 = 65537.

---

### Constructor Details

#### public RSAKeyGenParameterSpec​(int keysize,

BigInteger
publicExponent)

Constructs a new

RSAKeyGenParameterSpec

object from the
given keysize, public-exponent value, and null key parameters.

**Parameters:**
- keysize

- the modulus size (specified in number of bits)
- publicExponent

- the public exponent

---

#### public RSAKeyGenParameterSpec​(int keysize,

BigInteger
publicExponent,

AlgorithmParameterSpec
keyParams)

Constructs a new

RSAKeyGenParameterSpec

object from the
given keysize, public-exponent value, and key parameters.

**Parameters:**
- keysize

- the modulus size (specified in number of bits)
- publicExponent

- the public exponent
- keyParams

- the key parameters, may be null

**Since:**
- 11

---

### Method Details

#### public int getKeysize()

Returns the keysize.

**Returns:**
- the keysize.

---

#### public
BigInteger
getPublicExponent()

Returns the public-exponent value.

**Returns:**
- the public-exponent value.

---

#### public
AlgorithmParameterSpec
getKeyParams()

Returns the parameters to be associated with key.

**Returns:**
- the associated parameters, may be null if
not present

**Since:**
- 11

---

### Additional Sections

#### Class RSAKeyGenParameterSpec

java.lang.Object

- java.security.spec.RSAKeyGenParameterSpec

java.security.spec.RSAKeyGenParameterSpec

**All Implemented Interfaces:** AlgorithmParameterSpec

```java
public class
RSAKeyGenParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This class specifies the set of parameters used to generate an RSA
key pair.

**Since:** 1.3
**See Also:** KeyPairGenerator.initialize(java.security.spec.AlgorithmParameterSpec)

public class

RSAKeyGenParameterSpec

extends

Object

implements

AlgorithmParameterSpec

This class specifies the set of parameters used to generate an RSA
key pair.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

BigInteger

F0

The public-exponent value F0 = 3.

static

BigInteger

F4

The public exponent-value F4 = 65537.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RSAKeyGenParameterSpec

​(int keysize,

BigInteger

publicExponent)

Constructs a new

RSAKeyGenParameterSpec

object from the
given keysize, public-exponent value, and null key parameters.

RSAKeyGenParameterSpec

​(int keysize,

BigInteger

publicExponent,

AlgorithmParameterSpec

keyParams)

Constructs a new

RSAKeyGenParameterSpec

object from the
given keysize, public-exponent value, and key parameters.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AlgorithmParameterSpec

getKeyParams

()

Returns the parameters to be associated with key.

int

getKeysize

()

Returns the keysize.

BigInteger

getPublicExponent

()

Returns the public-exponent value.

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

Field Summary

Fields

Modifier and Type

Field

Description

static

BigInteger

F0

The public-exponent value F0 = 3.

static

BigInteger

F4

The public exponent-value F4 = 65537.

---

#### Field Summary

The public-exponent value F0 = 3.

The public exponent-value F4 = 65537.

Constructor Summary

Constructors

Constructor

Description

RSAKeyGenParameterSpec

​(int keysize,

BigInteger

publicExponent)

Constructs a new

RSAKeyGenParameterSpec

object from the
given keysize, public-exponent value, and null key parameters.

RSAKeyGenParameterSpec

​(int keysize,

BigInteger

publicExponent,

AlgorithmParameterSpec

keyParams)

Constructs a new

RSAKeyGenParameterSpec

object from the
given keysize, public-exponent value, and key parameters.

---

#### Constructor Summary

Constructs a new

RSAKeyGenParameterSpec

object from the
given keysize, public-exponent value, and null key parameters.

Constructs a new

RSAKeyGenParameterSpec

object from the
given keysize, public-exponent value, and key parameters.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AlgorithmParameterSpec

getKeyParams

()

Returns the parameters to be associated with key.

int

getKeysize

()

Returns the keysize.

BigInteger

getPublicExponent

()

Returns the public-exponent value.

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

Returns the parameters to be associated with key.

Returns the keysize.

Returns the public-exponent value.

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

============ FIELD DETAIL ===========

- Field Detail

- F0

```java
public static final
BigInteger
F0
```

The public-exponent value F0 = 3.

- F4

```java
public static final
BigInteger
F4
```

The public exponent-value F4 = 65537.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- RSAKeyGenParameterSpec

```java
public RSAKeyGenParameterSpec​(int keysize,

BigInteger
publicExponent)
```

Constructs a new

RSAKeyGenParameterSpec

object from the
given keysize, public-exponent value, and null key parameters.

**Parameters:** keysize

- the modulus size (specified in number of bits)
**Parameters:** publicExponent

- the public exponent

- RSAKeyGenParameterSpec

```java
public RSAKeyGenParameterSpec​(int keysize,

BigInteger
publicExponent,

AlgorithmParameterSpec
keyParams)
```

Constructs a new

RSAKeyGenParameterSpec

object from the
given keysize, public-exponent value, and key parameters.

**Parameters:** keysize

- the modulus size (specified in number of bits)
**Parameters:** publicExponent

- the public exponent
**Parameters:** keyParams

- the key parameters, may be null
**Since:** 11

============ METHOD DETAIL ==========

- Method Detail

- getKeysize

```java
public int getKeysize()
```

Returns the keysize.

**Returns:** the keysize.

- getPublicExponent

```java
public
BigInteger
getPublicExponent()
```

Returns the public-exponent value.

**Returns:** the public-exponent value.

- getKeyParams

```java
public
AlgorithmParameterSpec
getKeyParams()
```

Returns the parameters to be associated with key.

**Returns:** the associated parameters, may be null if
not present
**Since:** 11

Field Detail

- F0

```java
public static final
BigInteger
F0
```

The public-exponent value F0 = 3.

- F4

```java
public static final
BigInteger
F4
```

The public exponent-value F4 = 65537.

---

#### Field Detail

F0

```java
public static final
BigInteger
F0
```

The public-exponent value F0 = 3.

---

#### F0

public static final

BigInteger

F0

The public-exponent value F0 = 3.

F4

```java
public static final
BigInteger
F4
```

The public exponent-value F4 = 65537.

---

#### F4

public static final

BigInteger

F4

The public exponent-value F4 = 65537.

Constructor Detail

- RSAKeyGenParameterSpec

```java
public RSAKeyGenParameterSpec​(int keysize,

BigInteger
publicExponent)
```

Constructs a new

RSAKeyGenParameterSpec

object from the
given keysize, public-exponent value, and null key parameters.

**Parameters:** keysize

- the modulus size (specified in number of bits)
**Parameters:** publicExponent

- the public exponent

- RSAKeyGenParameterSpec

```java
public RSAKeyGenParameterSpec​(int keysize,

BigInteger
publicExponent,

AlgorithmParameterSpec
keyParams)
```

Constructs a new

RSAKeyGenParameterSpec

object from the
given keysize, public-exponent value, and key parameters.

**Parameters:** keysize

- the modulus size (specified in number of bits)
**Parameters:** publicExponent

- the public exponent
**Parameters:** keyParams

- the key parameters, may be null
**Since:** 11

---

#### Constructor Detail

RSAKeyGenParameterSpec

```java
public RSAKeyGenParameterSpec​(int keysize,

BigInteger
publicExponent)
```

Constructs a new

RSAKeyGenParameterSpec

object from the
given keysize, public-exponent value, and null key parameters.

**Parameters:** keysize

- the modulus size (specified in number of bits)
**Parameters:** publicExponent

- the public exponent

---

#### RSAKeyGenParameterSpec

public RSAKeyGenParameterSpec​(int keysize,

BigInteger

publicExponent)

Constructs a new

RSAKeyGenParameterSpec

object from the
given keysize, public-exponent value, and null key parameters.

RSAKeyGenParameterSpec

```java
public RSAKeyGenParameterSpec​(int keysize,

BigInteger
publicExponent,

AlgorithmParameterSpec
keyParams)
```

Constructs a new

RSAKeyGenParameterSpec

object from the
given keysize, public-exponent value, and key parameters.

**Parameters:** keysize

- the modulus size (specified in number of bits)
**Parameters:** publicExponent

- the public exponent
**Parameters:** keyParams

- the key parameters, may be null
**Since:** 11

---

#### RSAKeyGenParameterSpec

public RSAKeyGenParameterSpec​(int keysize,

BigInteger

publicExponent,

AlgorithmParameterSpec

keyParams)

Constructs a new

RSAKeyGenParameterSpec

object from the
given keysize, public-exponent value, and key parameters.

Method Detail

- getKeysize

```java
public int getKeysize()
```

Returns the keysize.

**Returns:** the keysize.

- getPublicExponent

```java
public
BigInteger
getPublicExponent()
```

Returns the public-exponent value.

**Returns:** the public-exponent value.

- getKeyParams

```java
public
AlgorithmParameterSpec
getKeyParams()
```

Returns the parameters to be associated with key.

**Returns:** the associated parameters, may be null if
not present
**Since:** 11

---

#### Method Detail

getKeysize

```java
public int getKeysize()
```

Returns the keysize.

**Returns:** the keysize.

---

#### getKeysize

public int getKeysize()

Returns the keysize.

getPublicExponent

```java
public
BigInteger
getPublicExponent()
```

Returns the public-exponent value.

**Returns:** the public-exponent value.

---

#### getPublicExponent

public

BigInteger

getPublicExponent()

Returns the public-exponent value.

getKeyParams

```java
public
AlgorithmParameterSpec
getKeyParams()
```

Returns the parameters to be associated with key.

**Returns:** the associated parameters, may be null if
not present
**Since:** 11

---

#### getKeyParams

public

AlgorithmParameterSpec

getKeyParams()

Returns the parameters to be associated with key.

---

