# Class DSAParameterSpec

**Source:** `java.base\java\security\spec\DSAParameterSpec.html`

### Class Description

```java
public class
DSAParameterSpec

extends
Object

implements
AlgorithmParameterSpec
,
DSAParams
```

This class specifies the set of parameters used with the DSA algorithm.

**All Implemented Interfaces:** DSAParams

,

AlgorithmParameterSpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public DSAParameterSpec​(
BigInteger
p,

BigInteger
q,

BigInteger
g)

Creates a new DSAParameterSpec with the specified parameter values.

**Parameters:**
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
getP()

Returns the prime

p

.

**Specified by:**
- getP

in interface

DSAParams

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

**Specified by:**
- getQ

in interface

DSAParams

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

**Specified by:**
- getG

in interface

DSAParams

**Returns:**
- the base

g

.

---

### Additional Sections

#### Class DSAParameterSpec

java.lang.Object

- java.security.spec.DSAParameterSpec

java.security.spec.DSAParameterSpec

**All Implemented Interfaces:** DSAParams

,

AlgorithmParameterSpec

```java
public class
DSAParameterSpec

extends
Object

implements
AlgorithmParameterSpec
,
DSAParams
```

This class specifies the set of parameters used with the DSA algorithm.

**Since:** 1.2
**See Also:** AlgorithmParameterSpec

public class

DSAParameterSpec

extends

Object

implements

AlgorithmParameterSpec

,

DSAParams

This class specifies the set of parameters used with the DSA algorithm.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

DSAParameterSpec

​(

BigInteger

p,

BigInteger

q,

BigInteger

g)

Creates a new DSAParameterSpec with the specified parameter values.

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

DSAParameterSpec

​(

BigInteger

p,

BigInteger

q,

BigInteger

g)

Creates a new DSAParameterSpec with the specified parameter values.

---

#### Constructor Summary

Creates a new DSAParameterSpec with the specified parameter values.

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

- DSAParameterSpec

```java
public DSAParameterSpec​(
BigInteger
p,

BigInteger
q,

BigInteger
g)
```

Creates a new DSAParameterSpec with the specified parameter values.

**Parameters:** p

- the prime.
**Parameters:** q

- the sub-prime.
**Parameters:** g

- the base.

============ METHOD DETAIL ==========

- Method Detail

- getP

```java
public
BigInteger
getP()
```

Returns the prime

p

.

**Specified by:** getP

in interface

DSAParams
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

**Specified by:** getQ

in interface

DSAParams
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

**Specified by:** getG

in interface

DSAParams
**Returns:** the base

g

.

Constructor Detail

- DSAParameterSpec

```java
public DSAParameterSpec​(
BigInteger
p,

BigInteger
q,

BigInteger
g)
```

Creates a new DSAParameterSpec with the specified parameter values.

**Parameters:** p

- the prime.
**Parameters:** q

- the sub-prime.
**Parameters:** g

- the base.

---

#### Constructor Detail

DSAParameterSpec

```java
public DSAParameterSpec​(
BigInteger
p,

BigInteger
q,

BigInteger
g)
```

Creates a new DSAParameterSpec with the specified parameter values.

**Parameters:** p

- the prime.
**Parameters:** q

- the sub-prime.
**Parameters:** g

- the base.

---

#### DSAParameterSpec

public DSAParameterSpec​(

BigInteger

p,

BigInteger

q,

BigInteger

g)

Creates a new DSAParameterSpec with the specified parameter values.

Method Detail

- getP

```java
public
BigInteger
getP()
```

Returns the prime

p

.

**Specified by:** getP

in interface

DSAParams
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

**Specified by:** getQ

in interface

DSAParams
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

**Specified by:** getG

in interface

DSAParams
**Returns:** the base

g

.

---

#### Method Detail

getP

```java
public
BigInteger
getP()
```

Returns the prime

p

.

**Specified by:** getP

in interface

DSAParams
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

**Specified by:** getQ

in interface

DSAParams
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

**Specified by:** getG

in interface

DSAParams
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

