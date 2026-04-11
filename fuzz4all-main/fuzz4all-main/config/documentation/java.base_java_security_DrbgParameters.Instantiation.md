# Class DrbgParameters.Instantiation

**Source:** `java.base\java\security\DrbgParameters.Instantiation.html`

### Class Description

```java
public static final class
DrbgParameters.Instantiation

extends
Object

implements
SecureRandomParameters
```

DRBG parameters for instantiation.

When used in

SecureRandom.getInstance(String, SecureRandomParameters)

or one of the other similar

getInstance

calls that take a

SecureRandomParameters

parameter, it means the
requested instantiate parameters the newly created

SecureRandom

object must minimally support. When used as the return value of the

SecureRandom.getParameters()

method, it means the effective
instantiate parameters of the

SecureRandom

object.

**All Implemented Interfaces:** SecureRandomParameters

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public int getStrength()

Returns the security strength in bits.

**Returns:**
- If used in

getInstance

, returns the minimum strength
requested, or -1 if there is no specific request on the strength.
If used in

getParameters

, returns the effective strength.
The effective strength must be greater than or equal to the minimum
strength requested.

---

#### public
DrbgParameters.Capability
getCapability()

Returns the capability.

**Returns:**
- If used in

getInstance

, returns the minimum
capability requested. If used in

getParameters

, returns
information on the effective prediction resistance flag and
whether it supports reseeding.

---

#### public byte[] getPersonalizationString()

Returns the personalization string as a byte array.

**Returns:**
- If used in

getInstance

, returns the requested
personalization string as a newly allocated array, or

null

if no personalization string is requested. The same string should
be returned in

getParameters

as a new copy, or

null

if no personalization string is requested in

getInstance

.

---

#### public
String
toString()

Returns a Human-readable string representation of this

Instantiation

.

**Overrides:**
- toString

in class

Object

**Returns:**
- the string representation

---

### Additional Sections

#### Class DrbgParameters.Instantiation

java.lang.Object

- java.security.DrbgParameters.Instantiation

java.security.DrbgParameters.Instantiation

**All Implemented Interfaces:** SecureRandomParameters

**Enclosing class:** DrbgParameters

```java
public static final class
DrbgParameters.Instantiation

extends
Object

implements
SecureRandomParameters
```

DRBG parameters for instantiation.

When used in

SecureRandom.getInstance(String, SecureRandomParameters)

or one of the other similar

getInstance

calls that take a

SecureRandomParameters

parameter, it means the
requested instantiate parameters the newly created

SecureRandom

object must minimally support. When used as the return value of the

SecureRandom.getParameters()

method, it means the effective
instantiate parameters of the

SecureRandom

object.

**Since:** 9

public static final class

DrbgParameters.Instantiation

extends

Object

implements

SecureRandomParameters

DRBG parameters for instantiation.

When used in

SecureRandom.getInstance(String, SecureRandomParameters)

or one of the other similar

getInstance

calls that take a

SecureRandomParameters

parameter, it means the
requested instantiate parameters the newly created

SecureRandom

object must minimally support. When used as the return value of the

SecureRandom.getParameters()

method, it means the effective
instantiate parameters of the

SecureRandom

object.

When used in

SecureRandom.getInstance(String, SecureRandomParameters)

or one of the other similar

getInstance

calls that take a

SecureRandomParameters

parameter, it means the
requested instantiate parameters the newly created

SecureRandom

object must minimally support. When used as the return value of the

SecureRandom.getParameters()

method, it means the effective
instantiate parameters of the

SecureRandom

object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

DrbgParameters.Capability

getCapability

()

Returns the capability.

byte[]

getPersonalizationString

()

Returns the personalization string as a byte array.

int

getStrength

()

Returns the security strength in bits.

String

toString

()

Returns a Human-readable string representation of this

Instantiation

.

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

DrbgParameters.Capability

getCapability

()

Returns the capability.

byte[]

getPersonalizationString

()

Returns the personalization string as a byte array.

int

getStrength

()

Returns the security strength in bits.

String

toString

()

Returns a Human-readable string representation of this

Instantiation

.

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

wait

,

wait

,

wait

---

#### Method Summary

Returns the capability.

Returns the personalization string as a byte array.

Returns the security strength in bits.

Returns a Human-readable string representation of this

Instantiation

.

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

Returns the security strength in bits.

**Returns:** If used in

getInstance

, returns the minimum strength
requested, or -1 if there is no specific request on the strength.
If used in

getParameters

, returns the effective strength.
The effective strength must be greater than or equal to the minimum
strength requested.

- getCapability

```java
public
DrbgParameters.Capability
getCapability()
```

Returns the capability.

**Returns:** If used in

getInstance

, returns the minimum
capability requested. If used in

getParameters

, returns
information on the effective prediction resistance flag and
whether it supports reseeding.

- getPersonalizationString

```java
public byte[] getPersonalizationString()
```

Returns the personalization string as a byte array.

**Returns:** If used in

getInstance

, returns the requested
personalization string as a newly allocated array, or

null

if no personalization string is requested. The same string should
be returned in

getParameters

as a new copy, or

null

if no personalization string is requested in

getInstance

.

- toString

```java
public
String
toString()
```

Returns a Human-readable string representation of this

Instantiation

.

**Overrides:** toString

in class

Object
**Returns:** the string representation

Method Detail

- getStrength

```java
public int getStrength()
```

Returns the security strength in bits.

**Returns:** If used in

getInstance

, returns the minimum strength
requested, or -1 if there is no specific request on the strength.
If used in

getParameters

, returns the effective strength.
The effective strength must be greater than or equal to the minimum
strength requested.

- getCapability

```java
public
DrbgParameters.Capability
getCapability()
```

Returns the capability.

**Returns:** If used in

getInstance

, returns the minimum
capability requested. If used in

getParameters

, returns
information on the effective prediction resistance flag and
whether it supports reseeding.

- getPersonalizationString

```java
public byte[] getPersonalizationString()
```

Returns the personalization string as a byte array.

**Returns:** If used in

getInstance

, returns the requested
personalization string as a newly allocated array, or

null

if no personalization string is requested. The same string should
be returned in

getParameters

as a new copy, or

null

if no personalization string is requested in

getInstance

.

- toString

```java
public
String
toString()
```

Returns a Human-readable string representation of this

Instantiation

.

**Overrides:** toString

in class

Object
**Returns:** the string representation

---

#### Method Detail

getStrength

```java
public int getStrength()
```

Returns the security strength in bits.

**Returns:** If used in

getInstance

, returns the minimum strength
requested, or -1 if there is no specific request on the strength.
If used in

getParameters

, returns the effective strength.
The effective strength must be greater than or equal to the minimum
strength requested.

---

#### getStrength

public int getStrength()

Returns the security strength in bits.

getCapability

```java
public
DrbgParameters.Capability
getCapability()
```

Returns the capability.

**Returns:** If used in

getInstance

, returns the minimum
capability requested. If used in

getParameters

, returns
information on the effective prediction resistance flag and
whether it supports reseeding.

---

#### getCapability

public

DrbgParameters.Capability

getCapability()

Returns the capability.

getPersonalizationString

```java
public byte[] getPersonalizationString()
```

Returns the personalization string as a byte array.

**Returns:** If used in

getInstance

, returns the requested
personalization string as a newly allocated array, or

null

if no personalization string is requested. The same string should
be returned in

getParameters

as a new copy, or

null

if no personalization string is requested in

getInstance

.

---

#### getPersonalizationString

public byte[] getPersonalizationString()

Returns the personalization string as a byte array.

toString

```java
public
String
toString()
```

Returns a Human-readable string representation of this

Instantiation

.

**Overrides:** toString

in class

Object
**Returns:** the string representation

---

#### toString

public

String

toString()

Returns a Human-readable string representation of this

Instantiation

.

---

