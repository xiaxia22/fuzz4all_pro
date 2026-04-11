# Class DHPublicKeySpec

**Source:** `java.base\javax\crypto\spec\DHPublicKeySpec.html`

### Class Description

```java
public class
DHPublicKeySpec

extends
Object

implements
KeySpec
```

This class specifies a Diffie-Hellman public key with its associated
parameters.

Note that this class does not perform any validation on specified
parameters. Thus, the specified values are returned directly even
if they are null.

**All Implemented Interfaces:** KeySpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public DHPublicKeySpec​(
BigInteger
y,

BigInteger
p,

BigInteger
g)

Constructor that takes a public value

y

, a prime
modulus

p

, and a base generator

g

.

**Parameters:**
- y

- public value y
- p

- prime modulus p
- g

- base generator g

---

### Method Details

#### public
BigInteger
getY()

Returns the public value

y

.

**Returns:**
- the public value

y

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

#### Class DHPublicKeySpec

java.lang.Object

- javax.crypto.spec.DHPublicKeySpec

javax.crypto.spec.DHPublicKeySpec

**All Implemented Interfaces:** KeySpec

```java
public class
DHPublicKeySpec

extends
Object

implements
KeySpec
```

This class specifies a Diffie-Hellman public key with its associated
parameters.

Note that this class does not perform any validation on specified
parameters. Thus, the specified values are returned directly even
if they are null.

**Since:** 1.4
**See Also:** DHPrivateKeySpec

public class

DHPublicKeySpec

extends

Object

implements

KeySpec

This class specifies a Diffie-Hellman public key with its associated
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

DHPublicKeySpec

​(

BigInteger

y,

BigInteger

p,

BigInteger

g)

Constructor that takes a public value

y

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

getY

()

Returns the public value

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

DHPublicKeySpec

​(

BigInteger

y,

BigInteger

p,

BigInteger

g)

Constructor that takes a public value

y

, a prime
modulus

p

, and a base generator

g

.

---

#### Constructor Summary

Constructor that takes a public value

y

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

getY

()

Returns the public value

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

Returns the base generator

g

.

Returns the prime modulus

p

.

Returns the public value

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

- DHPublicKeySpec

```java
public DHPublicKeySpec​(
BigInteger
y,

BigInteger
p,

BigInteger
g)
```

Constructor that takes a public value

y

, a prime
modulus

p

, and a base generator

g

.

**Parameters:** y

- public value y
**Parameters:** p

- prime modulus p
**Parameters:** g

- base generator g

============ METHOD DETAIL ==========

- Method Detail

- getY

```java
public
BigInteger
getY()
```

Returns the public value

y

.

**Returns:** the public value

y

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

- DHPublicKeySpec

```java
public DHPublicKeySpec​(
BigInteger
y,

BigInteger
p,

BigInteger
g)
```

Constructor that takes a public value

y

, a prime
modulus

p

, and a base generator

g

.

**Parameters:** y

- public value y
**Parameters:** p

- prime modulus p
**Parameters:** g

- base generator g

---

#### Constructor Detail

DHPublicKeySpec

```java
public DHPublicKeySpec​(
BigInteger
y,

BigInteger
p,

BigInteger
g)
```

Constructor that takes a public value

y

, a prime
modulus

p

, and a base generator

g

.

**Parameters:** y

- public value y
**Parameters:** p

- prime modulus p
**Parameters:** g

- base generator g

---

#### DHPublicKeySpec

public DHPublicKeySpec​(

BigInteger

y,

BigInteger

p,

BigInteger

g)

Constructor that takes a public value

y

, a prime
modulus

p

, and a base generator

g

.

Method Detail

- getY

```java
public
BigInteger
getY()
```

Returns the public value

y

.

**Returns:** the public value

y

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

getY

```java
public
BigInteger
getY()
```

Returns the public value

y

.

**Returns:** the public value

y

---

#### getY

public

BigInteger

getY()

Returns the public value

y

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

