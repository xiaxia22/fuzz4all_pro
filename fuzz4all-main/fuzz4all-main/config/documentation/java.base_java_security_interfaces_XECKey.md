# Interface XECKey

**Source:** `java.base\java\security\interfaces\XECKey.html`

### Class Description

```java
public interface
XECKey
```

An interface for an elliptic curve public/private key as defined by
RFC 7748. These keys are distinct from the keys represented by

ECKey

, and they are intended for use with algorithms based on RFC
7748 such as the XDH

KeyAgreement

algorithm. This interface allows
access to the algorithm parameters associated with the key.

**All Known Subinterfaces:** XECPrivateKey

,

XECPublicKey

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### AlgorithmParameterSpec
getParams()

Returns the algorithm parameters associated
with the key.

**Returns:**
- the associated algorithm parameters

---

### Additional Sections

#### Interface XECKey

**All Known Subinterfaces:** XECPrivateKey

,

XECPublicKey

```java
public interface
XECKey
```

An interface for an elliptic curve public/private key as defined by
RFC 7748. These keys are distinct from the keys represented by

ECKey

, and they are intended for use with algorithms based on RFC
7748 such as the XDH

KeyAgreement

algorithm. This interface allows
access to the algorithm parameters associated with the key.

**Since:** 11

public interface

XECKey

An interface for an elliptic curve public/private key as defined by
RFC 7748. These keys are distinct from the keys represented by

ECKey

, and they are intended for use with algorithms based on RFC
7748 such as the XDH

KeyAgreement

algorithm. This interface allows
access to the algorithm parameters associated with the key.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

AlgorithmParameterSpec

getParams

()

Returns the algorithm parameters associated
with the key.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

AlgorithmParameterSpec

getParams

()

Returns the algorithm parameters associated
with the key.

---

#### Method Summary

Returns the algorithm parameters associated
with the key.

============ METHOD DETAIL ==========

- Method Detail

- getParams

```java
AlgorithmParameterSpec
getParams()
```

Returns the algorithm parameters associated
with the key.

**Returns:** the associated algorithm parameters

Method Detail

- getParams

```java
AlgorithmParameterSpec
getParams()
```

Returns the algorithm parameters associated
with the key.

**Returns:** the associated algorithm parameters

---

#### Method Detail

getParams

```java
AlgorithmParameterSpec
getParams()
```

Returns the algorithm parameters associated
with the key.

**Returns:** the associated algorithm parameters

---

#### getParams

AlgorithmParameterSpec

getParams()

Returns the algorithm parameters associated
with the key.

---

