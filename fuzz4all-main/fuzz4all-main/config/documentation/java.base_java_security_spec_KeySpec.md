# Interface KeySpec

**Source:** `java.base\java\security\spec\KeySpec.html`

### Class Description

```java
public interface
KeySpec
```

A (transparent) specification of the key material
that constitutes a cryptographic key.

If the key is stored on a hardware device, its
specification may contain information that helps identify the key on the
device.

A key may be specified in an algorithm-specific way, or in an
algorithm-independent encoding format (such as ASN.1).
For example, a DSA private key may be specified by its components

x

,

p

,

q

, and

g

(see

DSAPrivateKeySpec

), or it may be
specified using its DER encoding
(see

PKCS8EncodedKeySpec

).

This interface contains no methods or constants. Its only purpose
is to group (and provide type safety for) all key specifications.
All key specifications must implement this interface.

**All Known Implementing Classes:** DESedeKeySpec

,

DESKeySpec

,

DHPrivateKeySpec

,

DHPublicKeySpec

,

DSAPrivateKeySpec

,

DSAPublicKeySpec

,

ECPrivateKeySpec

,

ECPublicKeySpec

,

EncodedKeySpec

,

PBEKeySpec

,

PKCS8EncodedKeySpec

,

RSAMultiPrimePrivateCrtKeySpec

,

RSAPrivateCrtKeySpec

,

RSAPrivateKeySpec

,

RSAPublicKeySpec

,

SecretKeySpec

,

X509EncodedKeySpec

,

XECPrivateKeySpec

,

XECPublicKeySpec

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Interface KeySpec

**All Known Implementing Classes:** DESedeKeySpec

,

DESKeySpec

,

DHPrivateKeySpec

,

DHPublicKeySpec

,

DSAPrivateKeySpec

,

DSAPublicKeySpec

,

ECPrivateKeySpec

,

ECPublicKeySpec

,

EncodedKeySpec

,

PBEKeySpec

,

PKCS8EncodedKeySpec

,

RSAMultiPrimePrivateCrtKeySpec

,

RSAPrivateCrtKeySpec

,

RSAPrivateKeySpec

,

RSAPublicKeySpec

,

SecretKeySpec

,

X509EncodedKeySpec

,

XECPrivateKeySpec

,

XECPublicKeySpec

```java
public interface
KeySpec
```

A (transparent) specification of the key material
that constitutes a cryptographic key.

If the key is stored on a hardware device, its
specification may contain information that helps identify the key on the
device.

A key may be specified in an algorithm-specific way, or in an
algorithm-independent encoding format (such as ASN.1).
For example, a DSA private key may be specified by its components

x

,

p

,

q

, and

g

(see

DSAPrivateKeySpec

), or it may be
specified using its DER encoding
(see

PKCS8EncodedKeySpec

).

This interface contains no methods or constants. Its only purpose
is to group (and provide type safety for) all key specifications.
All key specifications must implement this interface.

**Since:** 1.2
**See Also:** Key

,

KeyFactory

,

EncodedKeySpec

,

X509EncodedKeySpec

,

PKCS8EncodedKeySpec

,

DSAPrivateKeySpec

,

DSAPublicKeySpec

public interface

KeySpec

A (transparent) specification of the key material
that constitutes a cryptographic key.

If the key is stored on a hardware device, its
specification may contain information that helps identify the key on the
device.

A key may be specified in an algorithm-specific way, or in an
algorithm-independent encoding format (such as ASN.1).
For example, a DSA private key may be specified by its components

x

,

p

,

q

, and

g

(see

DSAPrivateKeySpec

), or it may be
specified using its DER encoding
(see

PKCS8EncodedKeySpec

).

This interface contains no methods or constants. Its only purpose
is to group (and provide type safety for) all key specifications.
All key specifications must implement this interface.

If the key is stored on a hardware device, its
specification may contain information that helps identify the key on the
device.

A key may be specified in an algorithm-specific way, or in an
algorithm-independent encoding format (such as ASN.1).
For example, a DSA private key may be specified by its components

x

,

p

,

q

, and

g

(see

DSAPrivateKeySpec

), or it may be
specified using its DER encoding
(see

PKCS8EncodedKeySpec

).

This interface contains no methods or constants. Its only purpose
is to group (and provide type safety for) all key specifications.
All key specifications must implement this interface.

A key may be specified in an algorithm-specific way, or in an
algorithm-independent encoding format (such as ASN.1).
For example, a DSA private key may be specified by its components

x

,

p

,

q

, and

g

(see

DSAPrivateKeySpec

), or it may be
specified using its DER encoding
(see

PKCS8EncodedKeySpec

).

This interface contains no methods or constants. Its only purpose
is to group (and provide type safety for) all key specifications.
All key specifications must implement this interface.

This interface contains no methods or constants. Its only purpose
is to group (and provide type safety for) all key specifications.
All key specifications must implement this interface.

---

