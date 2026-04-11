# Class RSAOtherPrimeInfo

**Source:** `java.base\java\security\spec\RSAOtherPrimeInfo.html`

### Class Description

```java
public class
RSAOtherPrimeInfo

extends
Object
```

This class represents the triplet (prime, exponent, and coefficient)
inside RSA's OtherPrimeInfo structure, as defined in the

PKCS#1 v2.2

standard.
The ASN.1 syntax of RSA's OtherPrimeInfo is as follows:

```java
OtherPrimeInfo ::= SEQUENCE {
prime INTEGER,
exponent INTEGER,
coefficient INTEGER
}
```

**Since:** 1.4
**See Also:** RSAPrivateCrtKeySpec

,

RSAMultiPrimePrivateCrtKey

---

### Field Details

*No entries found.*

### Constructor Details

#### public RSAOtherPrimeInfo​(
BigInteger
prime,

BigInteger
primeExponent,

BigInteger
crtCoefficient)

Creates a new

RSAOtherPrimeInfo

given the prime, primeExponent, and
crtCoefficient as defined in PKCS#1.

**Parameters:**
- prime

- the prime factor of n.
- primeExponent

- the exponent.
- crtCoefficient

- the Chinese Remainder Theorem
coefficient.

**Throws:**
- NullPointerException

- if any of the parameters, i.e.

prime

,

primeExponent

,

crtCoefficient

, is null.

---

### Method Details

#### public final
BigInteger
getPrime()

Returns the prime.

**Returns:**
- the prime.

---

#### public final
BigInteger
getExponent()

Returns the prime's exponent.

**Returns:**
- the primeExponent.

---

#### public final
BigInteger
getCrtCoefficient()

Returns the prime's crtCoefficient.

**Returns:**
- the crtCoefficient.

---

### Additional Sections

#### Class RSAOtherPrimeInfo

java.lang.Object

- java.security.spec.RSAOtherPrimeInfo

java.security.spec.RSAOtherPrimeInfo

```java
public class
RSAOtherPrimeInfo

extends
Object
```

This class represents the triplet (prime, exponent, and coefficient)
inside RSA's OtherPrimeInfo structure, as defined in the

PKCS#1 v2.2

standard.
The ASN.1 syntax of RSA's OtherPrimeInfo is as follows:

```java
OtherPrimeInfo ::= SEQUENCE {
prime INTEGER,
exponent INTEGER,
coefficient INTEGER
}
```

**Since:** 1.4
**See Also:** RSAPrivateCrtKeySpec

,

RSAMultiPrimePrivateCrtKey

public class

RSAOtherPrimeInfo

extends

Object

This class represents the triplet (prime, exponent, and coefficient)
inside RSA's OtherPrimeInfo structure, as defined in the

PKCS#1 v2.2

standard.
The ASN.1 syntax of RSA's OtherPrimeInfo is as follows:

```java
OtherPrimeInfo ::= SEQUENCE {
prime INTEGER,
exponent INTEGER,
coefficient INTEGER
}
```

OtherPrimeInfo ::= SEQUENCE {
prime INTEGER,
exponent INTEGER,
coefficient INTEGER
}

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

RSAOtherPrimeInfo

​(

BigInteger

prime,

BigInteger

primeExponent,

BigInteger

crtCoefficient)

Creates a new

RSAOtherPrimeInfo

given the prime, primeExponent, and
crtCoefficient as defined in PKCS#1.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

BigInteger

getCrtCoefficient

()

Returns the prime's crtCoefficient.

BigInteger

getExponent

()

Returns the prime's exponent.

BigInteger

getPrime

()

Returns the prime.

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

RSAOtherPrimeInfo

​(

BigInteger

prime,

BigInteger

primeExponent,

BigInteger

crtCoefficient)

Creates a new

RSAOtherPrimeInfo

given the prime, primeExponent, and
crtCoefficient as defined in PKCS#1.

---

#### Constructor Summary

Creates a new

RSAOtherPrimeInfo

given the prime, primeExponent, and
crtCoefficient as defined in PKCS#1.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

BigInteger

getCrtCoefficient

()

Returns the prime's crtCoefficient.

BigInteger

getExponent

()

Returns the prime's exponent.

BigInteger

getPrime

()

Returns the prime.

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

Returns the prime's crtCoefficient.

Returns the prime's exponent.

Returns the prime.

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

- RSAOtherPrimeInfo

```java
public RSAOtherPrimeInfo​(
BigInteger
prime,

BigInteger
primeExponent,

BigInteger
crtCoefficient)
```

Creates a new

RSAOtherPrimeInfo

given the prime, primeExponent, and
crtCoefficient as defined in PKCS#1.

**Parameters:** prime

- the prime factor of n.
**Parameters:** primeExponent

- the exponent.
**Parameters:** crtCoefficient

- the Chinese Remainder Theorem
coefficient.
**Throws:** NullPointerException

- if any of the parameters, i.e.

prime

,

primeExponent

,

crtCoefficient

, is null.

============ METHOD DETAIL ==========

- Method Detail

- getPrime

```java
public final
BigInteger
getPrime()
```

Returns the prime.

**Returns:** the prime.

- getExponent

```java
public final
BigInteger
getExponent()
```

Returns the prime's exponent.

**Returns:** the primeExponent.

- getCrtCoefficient

```java
public final
BigInteger
getCrtCoefficient()
```

Returns the prime's crtCoefficient.

**Returns:** the crtCoefficient.

Constructor Detail

- RSAOtherPrimeInfo

```java
public RSAOtherPrimeInfo​(
BigInteger
prime,

BigInteger
primeExponent,

BigInteger
crtCoefficient)
```

Creates a new

RSAOtherPrimeInfo

given the prime, primeExponent, and
crtCoefficient as defined in PKCS#1.

**Parameters:** prime

- the prime factor of n.
**Parameters:** primeExponent

- the exponent.
**Parameters:** crtCoefficient

- the Chinese Remainder Theorem
coefficient.
**Throws:** NullPointerException

- if any of the parameters, i.e.

prime

,

primeExponent

,

crtCoefficient

, is null.

---

#### Constructor Detail

RSAOtherPrimeInfo

```java
public RSAOtherPrimeInfo​(
BigInteger
prime,

BigInteger
primeExponent,

BigInteger
crtCoefficient)
```

Creates a new

RSAOtherPrimeInfo

given the prime, primeExponent, and
crtCoefficient as defined in PKCS#1.

**Parameters:** prime

- the prime factor of n.
**Parameters:** primeExponent

- the exponent.
**Parameters:** crtCoefficient

- the Chinese Remainder Theorem
coefficient.
**Throws:** NullPointerException

- if any of the parameters, i.e.

prime

,

primeExponent

,

crtCoefficient

, is null.

---

#### RSAOtherPrimeInfo

public RSAOtherPrimeInfo​(

BigInteger

prime,

BigInteger

primeExponent,

BigInteger

crtCoefficient)

Creates a new

RSAOtherPrimeInfo

given the prime, primeExponent, and
crtCoefficient as defined in PKCS#1.

Method Detail

- getPrime

```java
public final
BigInteger
getPrime()
```

Returns the prime.

**Returns:** the prime.

- getExponent

```java
public final
BigInteger
getExponent()
```

Returns the prime's exponent.

**Returns:** the primeExponent.

- getCrtCoefficient

```java
public final
BigInteger
getCrtCoefficient()
```

Returns the prime's crtCoefficient.

**Returns:** the crtCoefficient.

---

#### Method Detail

getPrime

```java
public final
BigInteger
getPrime()
```

Returns the prime.

**Returns:** the prime.

---

#### getPrime

public final

BigInteger

getPrime()

Returns the prime.

getExponent

```java
public final
BigInteger
getExponent()
```

Returns the prime's exponent.

**Returns:** the primeExponent.

---

#### getExponent

public final

BigInteger

getExponent()

Returns the prime's exponent.

getCrtCoefficient

```java
public final
BigInteger
getCrtCoefficient()
```

Returns the prime's crtCoefficient.

**Returns:** the crtCoefficient.

---

#### getCrtCoefficient

public final

BigInteger

getCrtCoefficient()

Returns the prime's crtCoefficient.

---

