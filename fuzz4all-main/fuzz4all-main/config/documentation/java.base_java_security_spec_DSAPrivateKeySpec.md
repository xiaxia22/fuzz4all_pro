# Class DSAPrivateKeySpec

**Source:** `java.base\java\security\spec\DSAPrivateKeySpec.html`

### Class Description

```java
public class
DSAPrivateKeySpec

extends
Object

implements
KeySpec
```

This class specifies a DSA private key with its associated parameters.

**All Implemented Interfaces:** KeySpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public DSAPrivateKeySpec​(
BigInteger
x,

BigInteger
p,

BigInteger
q,

BigInteger
g)

Creates a new DSAPrivateKeySpec with the specified parameter values.

**Parameters:**
- x

- the private key.
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
getX()

Returns the private key

x

.

**Returns:**
- the private key

x

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

#### Class DSAPrivateKeySpec

java.lang.Object

- java.security.spec.DSAPrivateKeySpec

java.security.spec.DSAPrivateKeySpec

**All Implemented Interfaces:** KeySpec

```java
public class
DSAPrivateKeySpec

extends
Object

implements
KeySpec
```

This class specifies a DSA private key with its associated parameters.

**Since:** 1.2
**See Also:** Key

,

KeyFactory

,

KeySpec

,

DSAPublicKeySpec

,

PKCS8EncodedKeySpec

public class

DSAPrivateKeySpec

extends

Object

implements

KeySpec

This class specifies a DSA private key with its associated parameters.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DSAPrivateKeySpec

​(

BigInteger

x,

BigInteger

p,

BigInteger

q,

BigInteger

g)

Creates a new DSAPrivateKeySpec with the specified parameter values.

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

getX

()

Returns the private key

x

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

DSAPrivateKeySpec

​(

BigInteger

x,

BigInteger

p,

BigInteger

q,

BigInteger

g)

Creates a new DSAPrivateKeySpec with the specified parameter values.

---

#### Constructor Summary

Creates a new DSAPrivateKeySpec with the specified parameter values.

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

getX

()

Returns the private key

x

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

Returns the private key

x

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

- DSAPrivateKeySpec

```java
public DSAPrivateKeySpec​(
BigInteger
x,

BigInteger
p,

BigInteger
q,

BigInteger
g)
```

Creates a new DSAPrivateKeySpec with the specified parameter values.

**Parameters:** x

- the private key.
**Parameters:** p

- the prime.
**Parameters:** q

- the sub-prime.
**Parameters:** g

- the base.

============ METHOD DETAIL ==========

- Method Detail

- getX

```java
public
BigInteger
getX()
```

Returns the private key

x

.

**Returns:** the private key

x

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

- DSAPrivateKeySpec

```java
public DSAPrivateKeySpec​(
BigInteger
x,

BigInteger
p,

BigInteger
q,

BigInteger
g)
```

Creates a new DSAPrivateKeySpec with the specified parameter values.

**Parameters:** x

- the private key.
**Parameters:** p

- the prime.
**Parameters:** q

- the sub-prime.
**Parameters:** g

- the base.

---

#### Constructor Detail

DSAPrivateKeySpec

```java
public DSAPrivateKeySpec​(
BigInteger
x,

BigInteger
p,

BigInteger
q,

BigInteger
g)
```

Creates a new DSAPrivateKeySpec with the specified parameter values.

**Parameters:** x

- the private key.
**Parameters:** p

- the prime.
**Parameters:** q

- the sub-prime.
**Parameters:** g

- the base.

---

#### DSAPrivateKeySpec

public DSAPrivateKeySpec​(

BigInteger

x,

BigInteger

p,

BigInteger

q,

BigInteger

g)

Creates a new DSAPrivateKeySpec with the specified parameter values.

Method Detail

- getX

```java
public
BigInteger
getX()
```

Returns the private key

x

.

**Returns:** the private key

x

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

getX

```java
public
BigInteger
getX()
```

Returns the private key

x

.

**Returns:** the private key

x

.

---

#### getX

public

BigInteger

getX()

Returns the private key

x

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

