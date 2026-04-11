# Class PBEParameterSpec

**Source:** `java.base\javax\crypto\spec\PBEParameterSpec.html`

### Class Description

```java
public class
PBEParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This class specifies the set of parameters used with password-based
encryption (PBE), as defined in the

PKCS #5

standard.

**All Implemented Interfaces:** AlgorithmParameterSpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public PBEParameterSpec​(byte[] salt,
int iterationCount)

Constructs a parameter set for password-based encryption as defined in
the PKCS #5 standard.

**Parameters:**
- salt

- the salt. The contents of

salt

are copied
to protect against subsequent modification.
- iterationCount

- the iteration count.

**Throws:**
- NullPointerException

- if

salt

is null.

---

#### public PBEParameterSpec​(byte[] salt,
int iterationCount,

AlgorithmParameterSpec
paramSpec)

Constructs a parameter set for password-based encryption as defined in
the PKCS #5 standard.

**Parameters:**
- salt

- the salt. The contents of

salt

are copied
to protect against subsequent modification.
- iterationCount

- the iteration count.
- paramSpec

- the cipher algorithm parameter specification, which
may be null.

**Throws:**
- NullPointerException

- if

salt

is null.

**Since:**
- 1.8

---

### Method Details

#### public byte[] getSalt()

Returns the salt.

**Returns:**
- the salt. Returns a new array
each time this method is called.

---

#### public int getIterationCount()

Returns the iteration count.

**Returns:**
- the iteration count

---

#### public
AlgorithmParameterSpec
getParameterSpec()

Returns the cipher algorithm parameter specification.

**Returns:**
- the parameter specification, or null if none was set.

**Since:**
- 1.8

---

### Additional Sections

#### Class PBEParameterSpec

java.lang.Object

- javax.crypto.spec.PBEParameterSpec

javax.crypto.spec.PBEParameterSpec

**All Implemented Interfaces:** AlgorithmParameterSpec

```java
public class
PBEParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This class specifies the set of parameters used with password-based
encryption (PBE), as defined in the

PKCS #5

standard.

**Since:** 1.4

public class

PBEParameterSpec

extends

Object

implements

AlgorithmParameterSpec

This class specifies the set of parameters used with password-based
encryption (PBE), as defined in the

PKCS #5

standard.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PBEParameterSpec

​(byte[] salt,
int iterationCount)

Constructs a parameter set for password-based encryption as defined in
the PKCS #5 standard.

PBEParameterSpec

​(byte[] salt,
int iterationCount,

AlgorithmParameterSpec

paramSpec)

Constructs a parameter set for password-based encryption as defined in
the PKCS #5 standard.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getIterationCount

()

Returns the iteration count.

AlgorithmParameterSpec

getParameterSpec

()

Returns the cipher algorithm parameter specification.

byte[]

getSalt

()

Returns the salt.

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

PBEParameterSpec

​(byte[] salt,
int iterationCount)

Constructs a parameter set for password-based encryption as defined in
the PKCS #5 standard.

PBEParameterSpec

​(byte[] salt,
int iterationCount,

AlgorithmParameterSpec

paramSpec)

Constructs a parameter set for password-based encryption as defined in
the PKCS #5 standard.

---

#### Constructor Summary

Constructs a parameter set for password-based encryption as defined in
the PKCS #5 standard.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getIterationCount

()

Returns the iteration count.

AlgorithmParameterSpec

getParameterSpec

()

Returns the cipher algorithm parameter specification.

byte[]

getSalt

()

Returns the salt.

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

Returns the iteration count.

Returns the cipher algorithm parameter specification.

Returns the salt.

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

- PBEParameterSpec

```java
public PBEParameterSpec​(byte[] salt,
int iterationCount)
```

Constructs a parameter set for password-based encryption as defined in
the PKCS #5 standard.

**Parameters:** salt

- the salt. The contents of

salt

are copied
to protect against subsequent modification.
**Parameters:** iterationCount

- the iteration count.
**Throws:** NullPointerException

- if

salt

is null.

- PBEParameterSpec

```java
public PBEParameterSpec​(byte[] salt,
int iterationCount,

AlgorithmParameterSpec
paramSpec)
```

Constructs a parameter set for password-based encryption as defined in
the PKCS #5 standard.

**Parameters:** salt

- the salt. The contents of

salt

are copied
to protect against subsequent modification.
**Parameters:** iterationCount

- the iteration count.
**Parameters:** paramSpec

- the cipher algorithm parameter specification, which
may be null.
**Throws:** NullPointerException

- if

salt

is null.
**Since:** 1.8

============ METHOD DETAIL ==========

- Method Detail

- getSalt

```java
public byte[] getSalt()
```

Returns the salt.

**Returns:** the salt. Returns a new array
each time this method is called.

- getIterationCount

```java
public int getIterationCount()
```

Returns the iteration count.

**Returns:** the iteration count

- getParameterSpec

```java
public
AlgorithmParameterSpec
getParameterSpec()
```

Returns the cipher algorithm parameter specification.

**Returns:** the parameter specification, or null if none was set.
**Since:** 1.8

Constructor Detail

- PBEParameterSpec

```java
public PBEParameterSpec​(byte[] salt,
int iterationCount)
```

Constructs a parameter set for password-based encryption as defined in
the PKCS #5 standard.

**Parameters:** salt

- the salt. The contents of

salt

are copied
to protect against subsequent modification.
**Parameters:** iterationCount

- the iteration count.
**Throws:** NullPointerException

- if

salt

is null.

- PBEParameterSpec

```java
public PBEParameterSpec​(byte[] salt,
int iterationCount,

AlgorithmParameterSpec
paramSpec)
```

Constructs a parameter set for password-based encryption as defined in
the PKCS #5 standard.

**Parameters:** salt

- the salt. The contents of

salt

are copied
to protect against subsequent modification.
**Parameters:** iterationCount

- the iteration count.
**Parameters:** paramSpec

- the cipher algorithm parameter specification, which
may be null.
**Throws:** NullPointerException

- if

salt

is null.
**Since:** 1.8

---

#### Constructor Detail

PBEParameterSpec

```java
public PBEParameterSpec​(byte[] salt,
int iterationCount)
```

Constructs a parameter set for password-based encryption as defined in
the PKCS #5 standard.

**Parameters:** salt

- the salt. The contents of

salt

are copied
to protect against subsequent modification.
**Parameters:** iterationCount

- the iteration count.
**Throws:** NullPointerException

- if

salt

is null.

---

#### PBEParameterSpec

public PBEParameterSpec​(byte[] salt,
int iterationCount)

Constructs a parameter set for password-based encryption as defined in
the PKCS #5 standard.

PBEParameterSpec

```java
public PBEParameterSpec​(byte[] salt,
int iterationCount,

AlgorithmParameterSpec
paramSpec)
```

Constructs a parameter set for password-based encryption as defined in
the PKCS #5 standard.

**Parameters:** salt

- the salt. The contents of

salt

are copied
to protect against subsequent modification.
**Parameters:** iterationCount

- the iteration count.
**Parameters:** paramSpec

- the cipher algorithm parameter specification, which
may be null.
**Throws:** NullPointerException

- if

salt

is null.
**Since:** 1.8

---

#### PBEParameterSpec

public PBEParameterSpec​(byte[] salt,
int iterationCount,

AlgorithmParameterSpec

paramSpec)

Constructs a parameter set for password-based encryption as defined in
the PKCS #5 standard.

Method Detail

- getSalt

```java
public byte[] getSalt()
```

Returns the salt.

**Returns:** the salt. Returns a new array
each time this method is called.

- getIterationCount

```java
public int getIterationCount()
```

Returns the iteration count.

**Returns:** the iteration count

- getParameterSpec

```java
public
AlgorithmParameterSpec
getParameterSpec()
```

Returns the cipher algorithm parameter specification.

**Returns:** the parameter specification, or null if none was set.
**Since:** 1.8

---

#### Method Detail

getSalt

```java
public byte[] getSalt()
```

Returns the salt.

**Returns:** the salt. Returns a new array
each time this method is called.

---

#### getSalt

public byte[] getSalt()

Returns the salt.

getIterationCount

```java
public int getIterationCount()
```

Returns the iteration count.

**Returns:** the iteration count

---

#### getIterationCount

public int getIterationCount()

Returns the iteration count.

getParameterSpec

```java
public
AlgorithmParameterSpec
getParameterSpec()
```

Returns the cipher algorithm parameter specification.

**Returns:** the parameter specification, or null if none was set.
**Since:** 1.8

---

#### getParameterSpec

public

AlgorithmParameterSpec

getParameterSpec()

Returns the cipher algorithm parameter specification.

---

