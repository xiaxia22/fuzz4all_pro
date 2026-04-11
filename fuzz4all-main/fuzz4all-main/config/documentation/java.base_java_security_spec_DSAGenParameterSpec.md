# Class DSAGenParameterSpec

**Source:** `java.base\java\security\spec\DSAGenParameterSpec.html`

### Class Description

```java
public final class
DSAGenParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This immutable class specifies the set of parameters used for
generating DSA parameters as specified in

FIPS 186-3 Digital Signature Standard (DSS)

.

**All Implemented Interfaces:** AlgorithmParameterSpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public DSAGenParameterSpec​(int primePLen,
int subprimeQLen)

Creates a domain parameter specification for DSA parameter
generation using

primePLen

and

subprimeQLen

.
The value of

subprimeQLen

is also used as the default
length of the domain parameter seed in bits.

**Parameters:**
- primePLen

- the desired length of the prime P in bits.
- subprimeQLen

- the desired length of the sub-prime Q in bits.

**Throws:**
- IllegalArgumentException

- if

primePLen

or

subprimeQLen

is illegal per the specification of
FIPS 186-3.

---

#### public DSAGenParameterSpec​(int primePLen,
int subprimeQLen,
int seedLen)

Creates a domain parameter specification for DSA parameter
generation using

primePLen

,

subprimeQLen

,
and

seedLen

.

**Parameters:**
- primePLen

- the desired length of the prime P in bits.
- subprimeQLen

- the desired length of the sub-prime Q in bits.
- seedLen

- the desired length of the domain parameter seed in bits,
shall be equal to or greater than

subprimeQLen

.

**Throws:**
- IllegalArgumentException

- if

primePLenLen

,

subprimeQLen

, or

seedLen

is illegal per the
specification of FIPS 186-3.

---

### Method Details

#### public int getPrimePLength()

Returns the desired length of the prime P of the
to-be-generated DSA domain parameters in bits.

**Returns:**
- the length of the prime P.

---

#### public int getSubprimeQLength()

Returns the desired length of the sub-prime Q of the
to-be-generated DSA domain parameters in bits.

**Returns:**
- the length of the sub-prime Q.

---

#### public int getSeedLength()

Returns the desired length of the domain parameter seed in bits.

**Returns:**
- the length of the domain parameter seed.

---

### Additional Sections

#### Class DSAGenParameterSpec

java.lang.Object

- java.security.spec.DSAGenParameterSpec

java.security.spec.DSAGenParameterSpec

**All Implemented Interfaces:** AlgorithmParameterSpec

```java
public final class
DSAGenParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This immutable class specifies the set of parameters used for
generating DSA parameters as specified in

FIPS 186-3 Digital Signature Standard (DSS)

.

**Since:** 1.8
**See Also:** AlgorithmParameterSpec

public final class

DSAGenParameterSpec

extends

Object

implements

AlgorithmParameterSpec

This immutable class specifies the set of parameters used for
generating DSA parameters as specified in

FIPS 186-3 Digital Signature Standard (DSS)

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DSAGenParameterSpec

​(int primePLen,
int subprimeQLen)

Creates a domain parameter specification for DSA parameter
generation using

primePLen

and

subprimeQLen

.

DSAGenParameterSpec

​(int primePLen,
int subprimeQLen,
int seedLen)

Creates a domain parameter specification for DSA parameter
generation using

primePLen

,

subprimeQLen

,
and

seedLen

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getPrimePLength

()

Returns the desired length of the prime P of the
to-be-generated DSA domain parameters in bits.

int

getSeedLength

()

Returns the desired length of the domain parameter seed in bits.

int

getSubprimeQLength

()

Returns the desired length of the sub-prime Q of the
to-be-generated DSA domain parameters in bits.

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

DSAGenParameterSpec

​(int primePLen,
int subprimeQLen)

Creates a domain parameter specification for DSA parameter
generation using

primePLen

and

subprimeQLen

.

DSAGenParameterSpec

​(int primePLen,
int subprimeQLen,
int seedLen)

Creates a domain parameter specification for DSA parameter
generation using

primePLen

,

subprimeQLen

,
and

seedLen

.

---

#### Constructor Summary

Creates a domain parameter specification for DSA parameter
generation using

primePLen

and

subprimeQLen

.

Creates a domain parameter specification for DSA parameter
generation using

primePLen

,

subprimeQLen

,
and

seedLen

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getPrimePLength

()

Returns the desired length of the prime P of the
to-be-generated DSA domain parameters in bits.

int

getSeedLength

()

Returns the desired length of the domain parameter seed in bits.

int

getSubprimeQLength

()

Returns the desired length of the sub-prime Q of the
to-be-generated DSA domain parameters in bits.

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

Returns the desired length of the prime P of the
to-be-generated DSA domain parameters in bits.

Returns the desired length of the domain parameter seed in bits.

Returns the desired length of the sub-prime Q of the
to-be-generated DSA domain parameters in bits.

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

- DSAGenParameterSpec

```java
public DSAGenParameterSpec​(int primePLen,
int subprimeQLen)
```

Creates a domain parameter specification for DSA parameter
generation using

primePLen

and

subprimeQLen

.
The value of

subprimeQLen

is also used as the default
length of the domain parameter seed in bits.

**Parameters:** primePLen

- the desired length of the prime P in bits.
**Parameters:** subprimeQLen

- the desired length of the sub-prime Q in bits.
**Throws:** IllegalArgumentException

- if

primePLen

or

subprimeQLen

is illegal per the specification of
FIPS 186-3.

- DSAGenParameterSpec

```java
public DSAGenParameterSpec​(int primePLen,
int subprimeQLen,
int seedLen)
```

Creates a domain parameter specification for DSA parameter
generation using

primePLen

,

subprimeQLen

,
and

seedLen

.

**Parameters:** primePLen

- the desired length of the prime P in bits.
**Parameters:** subprimeQLen

- the desired length of the sub-prime Q in bits.
**Parameters:** seedLen

- the desired length of the domain parameter seed in bits,
shall be equal to or greater than

subprimeQLen

.
**Throws:** IllegalArgumentException

- if

primePLenLen

,

subprimeQLen

, or

seedLen

is illegal per the
specification of FIPS 186-3.

============ METHOD DETAIL ==========

- Method Detail

- getPrimePLength

```java
public int getPrimePLength()
```

Returns the desired length of the prime P of the
to-be-generated DSA domain parameters in bits.

**Returns:** the length of the prime P.

- getSubprimeQLength

```java
public int getSubprimeQLength()
```

Returns the desired length of the sub-prime Q of the
to-be-generated DSA domain parameters in bits.

**Returns:** the length of the sub-prime Q.

- getSeedLength

```java
public int getSeedLength()
```

Returns the desired length of the domain parameter seed in bits.

**Returns:** the length of the domain parameter seed.

Constructor Detail

- DSAGenParameterSpec

```java
public DSAGenParameterSpec​(int primePLen,
int subprimeQLen)
```

Creates a domain parameter specification for DSA parameter
generation using

primePLen

and

subprimeQLen

.
The value of

subprimeQLen

is also used as the default
length of the domain parameter seed in bits.

**Parameters:** primePLen

- the desired length of the prime P in bits.
**Parameters:** subprimeQLen

- the desired length of the sub-prime Q in bits.
**Throws:** IllegalArgumentException

- if

primePLen

or

subprimeQLen

is illegal per the specification of
FIPS 186-3.

- DSAGenParameterSpec

```java
public DSAGenParameterSpec​(int primePLen,
int subprimeQLen,
int seedLen)
```

Creates a domain parameter specification for DSA parameter
generation using

primePLen

,

subprimeQLen

,
and

seedLen

.

**Parameters:** primePLen

- the desired length of the prime P in bits.
**Parameters:** subprimeQLen

- the desired length of the sub-prime Q in bits.
**Parameters:** seedLen

- the desired length of the domain parameter seed in bits,
shall be equal to or greater than

subprimeQLen

.
**Throws:** IllegalArgumentException

- if

primePLenLen

,

subprimeQLen

, or

seedLen

is illegal per the
specification of FIPS 186-3.

---

#### Constructor Detail

DSAGenParameterSpec

```java
public DSAGenParameterSpec​(int primePLen,
int subprimeQLen)
```

Creates a domain parameter specification for DSA parameter
generation using

primePLen

and

subprimeQLen

.
The value of

subprimeQLen

is also used as the default
length of the domain parameter seed in bits.

**Parameters:** primePLen

- the desired length of the prime P in bits.
**Parameters:** subprimeQLen

- the desired length of the sub-prime Q in bits.
**Throws:** IllegalArgumentException

- if

primePLen

or

subprimeQLen

is illegal per the specification of
FIPS 186-3.

---

#### DSAGenParameterSpec

public DSAGenParameterSpec​(int primePLen,
int subprimeQLen)

Creates a domain parameter specification for DSA parameter
generation using

primePLen

and

subprimeQLen

.
The value of

subprimeQLen

is also used as the default
length of the domain parameter seed in bits.

DSAGenParameterSpec

```java
public DSAGenParameterSpec​(int primePLen,
int subprimeQLen,
int seedLen)
```

Creates a domain parameter specification for DSA parameter
generation using

primePLen

,

subprimeQLen

,
and

seedLen

.

**Parameters:** primePLen

- the desired length of the prime P in bits.
**Parameters:** subprimeQLen

- the desired length of the sub-prime Q in bits.
**Parameters:** seedLen

- the desired length of the domain parameter seed in bits,
shall be equal to or greater than

subprimeQLen

.
**Throws:** IllegalArgumentException

- if

primePLenLen

,

subprimeQLen

, or

seedLen

is illegal per the
specification of FIPS 186-3.

---

#### DSAGenParameterSpec

public DSAGenParameterSpec​(int primePLen,
int subprimeQLen,
int seedLen)

Creates a domain parameter specification for DSA parameter
generation using

primePLen

,

subprimeQLen

,
and

seedLen

.

Method Detail

- getPrimePLength

```java
public int getPrimePLength()
```

Returns the desired length of the prime P of the
to-be-generated DSA domain parameters in bits.

**Returns:** the length of the prime P.

- getSubprimeQLength

```java
public int getSubprimeQLength()
```

Returns the desired length of the sub-prime Q of the
to-be-generated DSA domain parameters in bits.

**Returns:** the length of the sub-prime Q.

- getSeedLength

```java
public int getSeedLength()
```

Returns the desired length of the domain parameter seed in bits.

**Returns:** the length of the domain parameter seed.

---

#### Method Detail

getPrimePLength

```java
public int getPrimePLength()
```

Returns the desired length of the prime P of the
to-be-generated DSA domain parameters in bits.

**Returns:** the length of the prime P.

---

#### getPrimePLength

public int getPrimePLength()

Returns the desired length of the prime P of the
to-be-generated DSA domain parameters in bits.

getSubprimeQLength

```java
public int getSubprimeQLength()
```

Returns the desired length of the sub-prime Q of the
to-be-generated DSA domain parameters in bits.

**Returns:** the length of the sub-prime Q.

---

#### getSubprimeQLength

public int getSubprimeQLength()

Returns the desired length of the sub-prime Q of the
to-be-generated DSA domain parameters in bits.

getSeedLength

```java
public int getSeedLength()
```

Returns the desired length of the domain parameter seed in bits.

**Returns:** the length of the domain parameter seed.

---

#### getSeedLength

public int getSeedLength()

Returns the desired length of the domain parameter seed in bits.

---

