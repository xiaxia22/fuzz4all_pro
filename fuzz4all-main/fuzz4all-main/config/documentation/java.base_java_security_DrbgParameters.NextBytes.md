# Class DrbgParameters.NextBytes

**Source:** `java.base\java\security\DrbgParameters.NextBytes.html`

### Class Description

```java
public static final class
DrbgParameters.NextBytes

extends
Object

implements
SecureRandomParameters
```

DRBG parameters for random bits generation. It is used in

SecureRandom.nextBytes(byte[], SecureRandomParameters)

.

**All Implemented Interfaces:** SecureRandomParameters

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public int getStrength()

Returns the security strength requested in bits.

**Returns:**
- the strength requested, or -1 if the effective strength
should be used.

---

#### public boolean getPredictionResistance()

Returns whether prediction resistance is requested.

**Returns:**
- whether prediction resistance is requested

---

#### public byte[] getAdditionalInput()

Returns the requested additional input.

**Returns:**
- the requested additional input,

null

if not
requested. A new byte array is returned each time this method
is called.

---

### Additional Sections

#### Class DrbgParameters.NextBytes

java.lang.Object

- java.security.DrbgParameters.NextBytes

java.security.DrbgParameters.NextBytes

**All Implemented Interfaces:** SecureRandomParameters

**Enclosing class:** DrbgParameters

```java
public static final class
DrbgParameters.NextBytes

extends
Object

implements
SecureRandomParameters
```

DRBG parameters for random bits generation. It is used in

SecureRandom.nextBytes(byte[], SecureRandomParameters)

.

**Since:** 9

public static final class

DrbgParameters.NextBytes

extends

Object

implements

SecureRandomParameters

DRBG parameters for random bits generation. It is used in

SecureRandom.nextBytes(byte[], SecureRandomParameters)

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

byte[]

getAdditionalInput

()

Returns the requested additional input.

boolean

getPredictionResistance

()

Returns whether prediction resistance is requested.

int

getStrength

()

Returns the security strength requested in bits.

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

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

byte[]

getAdditionalInput

()

Returns the requested additional input.

boolean

getPredictionResistance

()

Returns whether prediction resistance is requested.

int

getStrength

()

Returns the security strength requested in bits.

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

Returns the requested additional input.

Returns whether prediction resistance is requested.

Returns the security strength requested in bits.

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

============ METHOD DETAIL ==========

- Method Detail

- getStrength

```java
public int getStrength()
```

Returns the security strength requested in bits.

**Returns:** the strength requested, or -1 if the effective strength
should be used.

- getPredictionResistance

```java
public boolean getPredictionResistance()
```

Returns whether prediction resistance is requested.

**Returns:** whether prediction resistance is requested

- getAdditionalInput

```java
public byte[] getAdditionalInput()
```

Returns the requested additional input.

**Returns:** the requested additional input,

null

if not
requested. A new byte array is returned each time this method
is called.

Method Detail

- getStrength

```java
public int getStrength()
```

Returns the security strength requested in bits.

**Returns:** the strength requested, or -1 if the effective strength
should be used.

- getPredictionResistance

```java
public boolean getPredictionResistance()
```

Returns whether prediction resistance is requested.

**Returns:** whether prediction resistance is requested

- getAdditionalInput

```java
public byte[] getAdditionalInput()
```

Returns the requested additional input.

**Returns:** the requested additional input,

null

if not
requested. A new byte array is returned each time this method
is called.

---

#### Method Detail

getStrength

```java
public int getStrength()
```

Returns the security strength requested in bits.

**Returns:** the strength requested, or -1 if the effective strength
should be used.

---

#### getStrength

public int getStrength()

Returns the security strength requested in bits.

getPredictionResistance

```java
public boolean getPredictionResistance()
```

Returns whether prediction resistance is requested.

**Returns:** whether prediction resistance is requested

---

#### getPredictionResistance

public boolean getPredictionResistance()

Returns whether prediction resistance is requested.

getAdditionalInput

```java
public byte[] getAdditionalInput()
```

Returns the requested additional input.

**Returns:** the requested additional input,

null

if not
requested. A new byte array is returned each time this method
is called.

---

#### getAdditionalInput

public byte[] getAdditionalInput()

Returns the requested additional input.

---

