# Class DHPrivateKeySpec

**Source:** `java.base\javax\crypto\spec\DHPrivateKeySpec.html`

### Class Description

```java
public class
DHPrivateKeySpec

extends
Object

implements
KeySpec
```

This class specifies a Diffie-Hellman private key with its associated
parameters.

Note that this class does not perform any validation on specified
parameters. Thus, the specified values are returned directly even
if they are null.

**All Implemented Interfaces:** KeySpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public DHPrivateKeySpec​(
BigInteger
x,

BigInteger
p,

BigInteger
g)

Constructor that takes a private value

x

, a prime
modulus

p

, and a base generator

g

.

**Parameters:**
- x

- private value x
- p

- prime modulus p
- g

- base generator g

---

### Method Details

#### public
BigInteger
getX()

Returns the private value

x

.

**Returns:**
- the private value

x

---

#### public
BigInteger
getP()

Returns the prime modulus

p

.

**Returns:**
- the prime modulus

p

---

#### public
BigInteger
getG()

Returns the base generator

g

.

**Returns:**
- the base generator

g

---

### Additional Sections

#### Class DHPrivateKeySpec

java.lang.Object

- javax.crypto.spec.DHPrivateKeySpec

javax.crypto.spec.DHPrivateKeySpec

**All Implemented Interfaces:** KeySpec

```java
public class
DHPrivateKeySpec

extends
Object

implements
KeySpec
```

This class specifies a Diffie-Hellman private key with its associated
parameters.

Note that this class does not perform any validation on specified
parameters. Thus, the specified values are returned directly even
if they are null.

**Since:** 1.4
**See Also:** DHPublicKeySpec

public class

DHPrivateKeySpec

extends

Object

implements

KeySpec

This class specifies a Diffie-Hellman private key with its associated
parameters.

Note that this class does not perform any validation on specified
parameters. Thus, the specified values are returned directly even
if they are null.

Note that this class does not perform any validation on specified
parameters. Thus, the specified values are returned directly even
if they are null.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DHPrivateKeySpec

​(

BigInteger

x,

BigInteger

p,

BigInteger

g)

Constructor that takes a private value

x

, a prime
modulus

p

, and a base generator

g

.

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

Returns the base generator

g

.

BigInteger

getP

()

Returns the prime modulus

p

.

BigInteger

getX

()

Returns the private value

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

DHPrivateKeySpec

​(

BigInteger

x,

BigInteger

p,

BigInteger

g)

Constructor that takes a private value

x

, a prime
modulus

p

, and a base generator

g

.

---

#### Constructor Summary

Constructor that takes a private value

x

, a prime
modulus

p

, and a base generator

g

.

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

Returns the base generator

g

.

BigInteger

getP

()

Returns the prime modulus

p

.

BigInteger

getX

()

Returns the private value

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

Returns the base generator

g

.

Returns the prime modulus

p

.

Returns the private value

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

- DHPrivateKeySpec

```java
public DHPrivateKeySpec​(
BigInteger
x,

BigInteger
p,

BigInteger
g)
```

Constructor that takes a private value

x

, a prime
modulus

p

, and a base generator

g

.

**Parameters:** x

- private value x
**Parameters:** p

- prime modulus p
**Parameters:** g

- base generator g

============ METHOD DETAIL ==========

- Method Detail

- getX

```java
public
BigInteger
getX()
```

Returns the private value

x

.

**Returns:** the private value

x

- getP

```java
public
BigInteger
getP()
```

Returns the prime modulus

p

.

**Returns:** the prime modulus

p

- getG

```java
public
BigInteger
getG()
```

Returns the base generator

g

.

**Returns:** the base generator

g

Constructor Detail

- DHPrivateKeySpec

```java
public DHPrivateKeySpec​(
BigInteger
x,

BigInteger
p,

BigInteger
g)
```

Constructor that takes a private value

x

, a prime
modulus

p

, and a base generator

g

.

**Parameters:** x

- private value x
**Parameters:** p

- prime modulus p
**Parameters:** g

- base generator g

---

#### Constructor Detail

DHPrivateKeySpec

```java
public DHPrivateKeySpec​(
BigInteger
x,

BigInteger
p,

BigInteger
g)
```

Constructor that takes a private value

x

, a prime
modulus

p

, and a base generator

g

.

**Parameters:** x

- private value x
**Parameters:** p

- prime modulus p
**Parameters:** g

- base generator g

---

#### DHPrivateKeySpec

public DHPrivateKeySpec​(

BigInteger

x,

BigInteger

p,

BigInteger

g)

Constructor that takes a private value

x

, a prime
modulus

p

, and a base generator

g

.

Method Detail

- getX

```java
public
BigInteger
getX()
```

Returns the private value

x

.

**Returns:** the private value

x

- getP

```java
public
BigInteger
getP()
```

Returns the prime modulus

p

.

**Returns:** the prime modulus

p

- getG

```java
public
BigInteger
getG()
```

Returns the base generator

g

.

**Returns:** the base generator

g

---

#### Method Detail

getX

```java
public
BigInteger
getX()
```

Returns the private value

x

.

**Returns:** the private value

x

---

#### getX

public

BigInteger

getX()

Returns the private value

x

.

getP

```java
public
BigInteger
getP()
```

Returns the prime modulus

p

.

**Returns:** the prime modulus

p

---

#### getP

public

BigInteger

getP()

Returns the prime modulus

p

.

getG

```java
public
BigInteger
getG()
```

Returns the base generator

g

.

**Returns:** the base generator

g

---

#### getG

public

BigInteger

getG()

Returns the base generator

g

.

---

