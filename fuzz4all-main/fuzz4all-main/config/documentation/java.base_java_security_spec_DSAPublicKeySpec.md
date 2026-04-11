# Class DSAPublicKeySpec

**Source:** `java.base\java\security\spec\DSAPublicKeySpec.html`

### Class Description

```java
public class
DSAPublicKeySpec

extends
Object

implements
KeySpec
```

This class specifies a DSA public key with its associated parameters.

**All Implemented Interfaces:** KeySpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public DSAPublicKeySpec​(
BigInteger
y,

BigInteger
p,

BigInteger
q,

BigInteger
g)

Creates a new DSAPublicKeySpec with the specified parameter values.

**Parameters:**
- y

- the public key.
- p

- the prime.
- q

- the sub-prime.
- g

- the base.

---

### Method Details

#### public
BigInteger
getY()

Returns the public key

y

.

**Returns:**
- the public key

y

.

---

#### public
BigInteger
getP()

Returns the prime

p

.

**Returns:**
- the prime

p

.

---

#### public
BigInteger
getQ()

Returns the sub-prime

q

.

**Returns:**
- the sub-prime

q

.

---

#### public
BigInteger
getG()

Returns the base

g

.

**Returns:**
- the base

g

.

---

### Additional Sections

#### Class DSAPublicKeySpec

java.lang.Object

- java.security.spec.DSAPublicKeySpec

java.security.spec.DSAPublicKeySpec

**All Implemented Interfaces:** KeySpec

```java
public class
DSAPublicKeySpec

extends
Object

implements
KeySpec
```

This class specifies a DSA public key with its associated parameters.

**Since:** 1.2
**See Also:** Key

,

KeyFactory

,

KeySpec

,

DSAPrivateKeySpec

,

X509EncodedKeySpec

public class

DSAPublicKeySpec

extends

Object

implements

KeySpec

This class specifies a DSA public key with its associated parameters.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DSAPublicKeySpec

​(

BigInteger

y,

BigInteger

p,

BigInteger

q,

BigInteger

g)

Creates a new DSAPublicKeySpec with the specified parameter values.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

BigInteger

getG

()

Returns the base

g

.

BigInteger

getP

()

Returns the prime

p

.

BigInteger

getQ

()

Returns the sub-prime

q

.

BigInteger

getY

()

Returns the public key

y

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

DSAPublicKeySpec

​(

BigInteger

y,

BigInteger

p,

BigInteger

q,

BigInteger

g)

Creates a new DSAPublicKeySpec with the specified parameter values.

---

#### Constructor Summary

Creates a new DSAPublicKeySpec with the specified parameter values.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

BigInteger

getG

()

Returns the base

g

.

BigInteger

getP

()

Returns the prime

p

.

BigInteger

getQ

()

Returns the sub-prime

q

.

BigInteger

getY

()

Returns the public key

y

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

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns the base

g

.

Returns the prime

p

.

Returns the sub-prime

q

.

Returns the public key

y

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

- DSAPublicKeySpec

```java
public DSAPublicKeySpec​(
BigInteger
y,

BigInteger
p,

BigInteger
q,

BigInteger
g)
```

Creates a new DSAPublicKeySpec with the specified parameter values.

**Parameters:** y

- the public key.
**Parameters:** p

- the prime.
**Parameters:** q

- the sub-prime.
**Parameters:** g

- the base.

============ METHOD DETAIL ==========

- Method Detail

- getY

```java
public
BigInteger
getY()
```

Returns the public key

y

.

**Returns:** the public key

y

.

- getP

```java
public
BigInteger
getP()
```

Returns the prime

p

.

**Returns:** the prime

p

.

- getQ

```java
public
BigInteger
getQ()
```

Returns the sub-prime

q

.

**Returns:** the sub-prime

q

.

- getG

```java
public
BigInteger
getG()
```

Returns the base

g

.

**Returns:** the base

g

.

Constructor Detail

- DSAPublicKeySpec

```java
public DSAPublicKeySpec​(
BigInteger
y,

BigInteger
p,

BigInteger
q,

BigInteger
g)
```

Creates a new DSAPublicKeySpec with the specified parameter values.

**Parameters:** y

- the public key.
**Parameters:** p

- the prime.
**Parameters:** q

- the sub-prime.
**Parameters:** g

- the base.

---

#### Constructor Detail

DSAPublicKeySpec

```java
public DSAPublicKeySpec​(
BigInteger
y,

BigInteger
p,

BigInteger
q,

BigInteger
g)
```

Creates a new DSAPublicKeySpec with the specified parameter values.

**Parameters:** y

- the public key.
**Parameters:** p

- the prime.
**Parameters:** q

- the sub-prime.
**Parameters:** g

- the base.

---

#### DSAPublicKeySpec

public DSAPublicKeySpec​(

BigInteger

y,

BigInteger

p,

BigInteger

q,

BigInteger

g)

Creates a new DSAPublicKeySpec with the specified parameter values.

Method Detail

- getY

```java
public
BigInteger
getY()
```

Returns the public key

y

.

**Returns:** the public key

y

.

- getP

```java
public
BigInteger
getP()
```

Returns the prime

p

.

**Returns:** the prime

p

.

- getQ

```java
public
BigInteger
getQ()
```

Returns the sub-prime

q

.

**Returns:** the sub-prime

q

.

- getG

```java
public
BigInteger
getG()
```

Returns the base

g

.

**Returns:** the base

g

.

---

#### Method Detail

getY

```java
public
BigInteger
getY()
```

Returns the public key

y

.

**Returns:** the public key

y

.

---

#### getY

public

BigInteger

getY()

Returns the public key

y

.

getP

```java
public
BigInteger
getP()
```

Returns the prime

p

.

**Returns:** the prime

p

.

---

#### getP

public

BigInteger

getP()

Returns the prime

p

.

getQ

```java
public
BigInteger
getQ()
```

Returns the sub-prime

q

.

**Returns:** the sub-prime

q

.

---

#### getQ

public

BigInteger

getQ()

Returns the sub-prime

q

.

getG

```java
public
BigInteger
getG()
```

Returns the base

g

.

**Returns:** the base

g

.

---

#### getG

public

BigInteger

getG()

Returns the base

g

.

---

