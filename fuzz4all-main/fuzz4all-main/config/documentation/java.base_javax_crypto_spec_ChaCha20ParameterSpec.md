# Class ChaCha20ParameterSpec

**Source:** `java.base\javax\crypto\spec\ChaCha20ParameterSpec.html`

### Class Description

```java
public final class
ChaCha20ParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This class specifies the parameters used with the

ChaCha20

algorithm.

The parameters consist of a 12-byte nonce and an initial
counter value expressed as a 32-bit integer.

This class can be used to initialize a

Cipher

object that
implements the

ChaCha20

algorithm.

**All Implemented Interfaces:** AlgorithmParameterSpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public ChaCha20ParameterSpec​(byte[] nonce,
int counter)

Constructs a parameter set for ChaCha20 from the given nonce
and counter.

**Parameters:**
- nonce

- a 12-byte nonce value
- counter

- the initial counter value

**Throws:**
- NullPointerException

- if

nonce

is

null
- IllegalArgumentException

- if

nonce

is not 12 bytes
in length

---

### Method Details

#### public byte[] getNonce()

Returns the nonce value.

**Returns:**
- the nonce value. This method returns a new array each time
this method is called.

---

#### public int getCounter()

Returns the configured counter value.

**Returns:**
- the counter value

---

### Additional Sections

#### Class ChaCha20ParameterSpec

java.lang.Object

- javax.crypto.spec.ChaCha20ParameterSpec

javax.crypto.spec.ChaCha20ParameterSpec

**All Implemented Interfaces:** AlgorithmParameterSpec

```java
public final class
ChaCha20ParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This class specifies the parameters used with the

ChaCha20

algorithm.

The parameters consist of a 12-byte nonce and an initial
counter value expressed as a 32-bit integer.

This class can be used to initialize a

Cipher

object that
implements the

ChaCha20

algorithm.

**Since:** 11

public final class

ChaCha20ParameterSpec

extends

Object

implements

AlgorithmParameterSpec

This class specifies the parameters used with the

ChaCha20

algorithm.

The parameters consist of a 12-byte nonce and an initial
counter value expressed as a 32-bit integer.

This class can be used to initialize a

Cipher

object that
implements the

ChaCha20

algorithm.

The parameters consist of a 12-byte nonce and an initial
counter value expressed as a 32-bit integer.

This class can be used to initialize a

Cipher

object that
implements the

ChaCha20

algorithm.

This class can be used to initialize a

Cipher

object that
implements the

ChaCha20

algorithm.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ChaCha20ParameterSpec

​(byte[] nonce,
int counter)

Constructs a parameter set for ChaCha20 from the given nonce
and counter.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getCounter

()

Returns the configured counter value.

byte[]

getNonce

()

Returns the nonce value.

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

ChaCha20ParameterSpec

​(byte[] nonce,
int counter)

Constructs a parameter set for ChaCha20 from the given nonce
and counter.

---

#### Constructor Summary

Constructs a parameter set for ChaCha20 from the given nonce
and counter.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getCounter

()

Returns the configured counter value.

byte[]

getNonce

()

Returns the nonce value.

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

Returns the configured counter value.

Returns the nonce value.

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

- ChaCha20ParameterSpec

```java
public ChaCha20ParameterSpec​(byte[] nonce,
int counter)
```

Constructs a parameter set for ChaCha20 from the given nonce
and counter.

**Parameters:** nonce

- a 12-byte nonce value
**Parameters:** counter

- the initial counter value
**Throws:** NullPointerException

- if

nonce

is

null
**Throws:** IllegalArgumentException

- if

nonce

is not 12 bytes
in length

============ METHOD DETAIL ==========

- Method Detail

- getNonce

```java
public byte[] getNonce()
```

Returns the nonce value.

**Returns:** the nonce value. This method returns a new array each time
this method is called.

- getCounter

```java
public int getCounter()
```

Returns the configured counter value.

**Returns:** the counter value

Constructor Detail

- ChaCha20ParameterSpec

```java
public ChaCha20ParameterSpec​(byte[] nonce,
int counter)
```

Constructs a parameter set for ChaCha20 from the given nonce
and counter.

**Parameters:** nonce

- a 12-byte nonce value
**Parameters:** counter

- the initial counter value
**Throws:** NullPointerException

- if

nonce

is

null
**Throws:** IllegalArgumentException

- if

nonce

is not 12 bytes
in length

---

#### Constructor Detail

ChaCha20ParameterSpec

```java
public ChaCha20ParameterSpec​(byte[] nonce,
int counter)
```

Constructs a parameter set for ChaCha20 from the given nonce
and counter.

**Parameters:** nonce

- a 12-byte nonce value
**Parameters:** counter

- the initial counter value
**Throws:** NullPointerException

- if

nonce

is

null
**Throws:** IllegalArgumentException

- if

nonce

is not 12 bytes
in length

---

#### ChaCha20ParameterSpec

public ChaCha20ParameterSpec​(byte[] nonce,
int counter)

Constructs a parameter set for ChaCha20 from the given nonce
and counter.

Method Detail

- getNonce

```java
public byte[] getNonce()
```

Returns the nonce value.

**Returns:** the nonce value. This method returns a new array each time
this method is called.

- getCounter

```java
public int getCounter()
```

Returns the configured counter value.

**Returns:** the counter value

---

#### Method Detail

getNonce

```java
public byte[] getNonce()
```

Returns the nonce value.

**Returns:** the nonce value. This method returns a new array each time
this method is called.

---

#### getNonce

public byte[] getNonce()

Returns the nonce value.

getCounter

```java
public int getCounter()
```

Returns the configured counter value.

**Returns:** the counter value

---

#### getCounter

public int getCounter()

Returns the configured counter value.

---

