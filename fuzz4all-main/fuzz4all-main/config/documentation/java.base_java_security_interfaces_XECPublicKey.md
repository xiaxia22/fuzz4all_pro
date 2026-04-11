# Interface XECPublicKey

**Source:** `java.base\java\security\interfaces\XECPublicKey.html`

### Class Description

```java
public interface
XECPublicKey

extends
XECKey
,
PublicKey
```

An interface for an elliptic curve public key as defined by RFC 7748.
These keys are distinct from the keys represented by

ECPublicKey

,
and they are intended for use with algorithms based on RFC 7748 such as the
XDH

KeyAgreement

algorithm.

An XEC public key is a particular point on the curve, which is represented
using only its u-coordinate as described in RFC 7748. A u-coordinate is an
element of the field of integers modulo some value that is determined by
the algorithm parameters. This field element is represented by a BigInteger
which may hold any value. That is, the BigInteger is not restricted to the
range of canonical field elements.

**All Superinterfaces:** Key

,

PublicKey

,

Serializable

,

XECKey

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### BigInteger
getU()

Get the u coordinate of the point.

**Returns:**
- the u-coordinate, represented using a BigInteger which may hold
any value

---

### Additional Sections

#### Interface XECPublicKey

**All Superinterfaces:** Key

,

PublicKey

,

Serializable

,

XECKey

```java
public interface
XECPublicKey

extends
XECKey
,
PublicKey
```

An interface for an elliptic curve public key as defined by RFC 7748.
These keys are distinct from the keys represented by

ECPublicKey

,
and they are intended for use with algorithms based on RFC 7748 such as the
XDH

KeyAgreement

algorithm.

An XEC public key is a particular point on the curve, which is represented
using only its u-coordinate as described in RFC 7748. A u-coordinate is an
element of the field of integers modulo some value that is determined by
the algorithm parameters. This field element is represented by a BigInteger
which may hold any value. That is, the BigInteger is not restricted to the
range of canonical field elements.

**Since:** 11

public interface

XECPublicKey

extends

XECKey

,

PublicKey

An interface for an elliptic curve public key as defined by RFC 7748.
These keys are distinct from the keys represented by

ECPublicKey

,
and they are intended for use with algorithms based on RFC 7748 such as the
XDH

KeyAgreement

algorithm.

An XEC public key is a particular point on the curve, which is represented
using only its u-coordinate as described in RFC 7748. A u-coordinate is an
element of the field of integers modulo some value that is determined by
the algorithm parameters. This field element is represented by a BigInteger
which may hold any value. That is, the BigInteger is not restricted to the
range of canonical field elements.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in interface java.security.

PublicKey

serialVersionUID

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

BigInteger

getU

()

Get the u coordinate of the point.

- Methods declared in interface java.security.

Key

getAlgorithm

,

getEncoded

,

getFormat

- Methods declared in interface java.security.interfaces.

XECKey

getParams

Field Summary

- Fields declared in interface java.security.

PublicKey

serialVersionUID

---

#### Field Summary

Fields declared in interface java.security.

PublicKey

serialVersionUID

---

#### Fields declared in interface java.security. PublicKey

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

BigInteger

getU

()

Get the u coordinate of the point.

- Methods declared in interface java.security.

Key

getAlgorithm

,

getEncoded

,

getFormat

- Methods declared in interface java.security.interfaces.

XECKey

getParams

---

#### Method Summary

Get the u coordinate of the point.

Methods declared in interface java.security.

Key

getAlgorithm

,

getEncoded

,

getFormat

---

#### Methods declared in interface java.security. Key

Methods declared in interface java.security.interfaces.

XECKey

getParams

---

#### Methods declared in interface java.security.interfaces. XECKey

============ METHOD DETAIL ==========

- Method Detail

- getU

```java
BigInteger
getU()
```

Get the u coordinate of the point.

**Returns:** the u-coordinate, represented using a BigInteger which may hold
any value

Method Detail

- getU

```java
BigInteger
getU()
```

Get the u coordinate of the point.

**Returns:** the u-coordinate, represented using a BigInteger which may hold
any value

---

#### Method Detail

getU

```java
BigInteger
getU()
```

Get the u coordinate of the point.

**Returns:** the u-coordinate, represented using a BigInteger which may hold
any value

---

#### getU

BigInteger

getU()

Get the u coordinate of the point.

---

