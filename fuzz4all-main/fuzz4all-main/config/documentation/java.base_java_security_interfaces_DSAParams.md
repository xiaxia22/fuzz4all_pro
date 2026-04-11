# Interface DSAParams

**Source:** `java.base\java\security\interfaces\DSAParams.html`

### Class Description

```java
public interface
DSAParams
```

Interface to a DSA-specific set of key parameters, which defines a
DSA

key family

. DSA (Digital Signature Algorithm) is defined
in NIST's FIPS-186.

**All Known Implementing Classes:** DSAParameterSpec

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### BigInteger
getP()

Returns the prime,

p

.

**Returns:**
- the prime,

p

.

---

#### BigInteger
getQ()

Returns the subprime,

q

.

**Returns:**
- the subprime,

q

.

---

#### BigInteger
getG()

Returns the base,

g

.

**Returns:**
- the base,

g

.

---

### Additional Sections

#### Interface DSAParams

**All Known Implementing Classes:** DSAParameterSpec

```java
public interface
DSAParams
```

Interface to a DSA-specific set of key parameters, which defines a
DSA

key family

. DSA (Digital Signature Algorithm) is defined
in NIST's FIPS-186.

**Since:** 1.1
**See Also:** DSAKey

,

Key

,

Signature

public interface

DSAParams

Interface to a DSA-specific set of key parameters, which defines a
DSA

key family

. DSA (Digital Signature Algorithm) is defined
in NIST's FIPS-186.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

BigInteger

getG

()

Returns the base,

g

.

BigInteger

getP

()

Returns the prime,

p

.

BigInteger

getQ

()

Returns the subprime,

q

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

BigInteger

getG

()

Returns the base,

g

.

BigInteger

getP

()

Returns the prime,

p

.

BigInteger

getQ

()

Returns the subprime,

q

.

---

#### Method Summary

Returns the base,

g

.

Returns the prime,

p

.

Returns the subprime,

q

.

============ METHOD DETAIL ==========

- Method Detail

- getP

```java
BigInteger
getP()
```

Returns the prime,

p

.

**Returns:** the prime,

p

.

- getQ

```java
BigInteger
getQ()
```

Returns the subprime,

q

.

**Returns:** the subprime,

q

.

- getG

```java
BigInteger
getG()
```

Returns the base,

g

.

**Returns:** the base,

g

.

Method Detail

- getP

```java
BigInteger
getP()
```

Returns the prime,

p

.

**Returns:** the prime,

p

.

- getQ

```java
BigInteger
getQ()
```

Returns the subprime,

q

.

**Returns:** the subprime,

q

.

- getG

```java
BigInteger
getG()
```

Returns the base,

g

.

**Returns:** the base,

g

.

---

#### Method Detail

getP

```java
BigInteger
getP()
```

Returns the prime,

p

.

**Returns:** the prime,

p

.

---

#### getP

BigInteger

getP()

Returns the prime,

p

.

getQ

```java
BigInteger
getQ()
```

Returns the subprime,

q

.

**Returns:** the subprime,

q

.

---

#### getQ

BigInteger

getQ()

Returns the subprime,

q

.

getG

```java
BigInteger
getG()
```

Returns the base,

g

.

**Returns:** the base,

g

.

---

#### getG

BigInteger

getG()

Returns the base,

g

.

---

