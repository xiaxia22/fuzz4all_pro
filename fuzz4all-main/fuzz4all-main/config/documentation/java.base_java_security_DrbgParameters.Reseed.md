# Class DrbgParameters.Reseed

**Source:** `java.base\java\security\DrbgParameters.Reseed.html`

### Class Description

```java
public static final class
DrbgParameters.Reseed

extends
Object

implements
SecureRandomParameters
```

DRBG parameters for reseed. It is used in

SecureRandom.reseed(SecureRandomParameters)

.

**All Implemented Interfaces:** SecureRandomParameters

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public boolean getPredictionResistance()

Returns whether prediction resistance is requested.

**Returns:**
- whether prediction resistance is requested

---

#### public byte[] getAdditionalInput()

Returns the requested additional input.

**Returns:**
- the requested additional input, or

null

if
not requested. A new byte array is returned each time this method
is called.

---

### Additional Sections

#### Class DrbgParameters.Reseed

java.lang.Object

- java.security.DrbgParameters.Reseed

java.security.DrbgParameters.Reseed

**All Implemented Interfaces:** SecureRandomParameters

**Enclosing class:** DrbgParameters

```java
public static final class
DrbgParameters.Reseed

extends
Object

implements
SecureRandomParameters
```

DRBG parameters for reseed. It is used in

SecureRandom.reseed(SecureRandomParameters)

.

**Since:** 9

public static final class

DrbgParameters.Reseed

extends

Object

implements

SecureRandomParameters

DRBG parameters for reseed. It is used in

SecureRandom.reseed(SecureRandomParameters)

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

**Returns:** the requested additional input, or

null

if
not requested. A new byte array is returned each time this method
is called.

Method Detail

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

**Returns:** the requested additional input, or

null

if
not requested. A new byte array is returned each time this method
is called.

---

#### Method Detail

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

**Returns:** the requested additional input, or

null

if
not requested. A new byte array is returned each time this method
is called.

---

#### getAdditionalInput

public byte[] getAdditionalInput()

Returns the requested additional input.

---

