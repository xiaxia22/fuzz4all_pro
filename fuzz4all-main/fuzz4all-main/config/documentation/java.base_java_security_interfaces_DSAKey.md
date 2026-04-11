# Interface DSAKey

**Source:** `java.base\java\security\interfaces\DSAKey.html`

### Class Description

```java
public interface
DSAKey
```

The interface to a DSA public or private key. DSA (Digital Signature
Algorithm) is defined in NIST's FIPS-186.

**All Known Subinterfaces:** DSAPrivateKey

,

DSAPublicKey

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### DSAParams
getParams()

Returns the DSA-specific key parameters. These parameters are
never secret.

**Returns:**
- the DSA-specific key parameters.

**See Also:**
- DSAParams

---

### Additional Sections

#### Interface DSAKey

**All Known Subinterfaces:** DSAPrivateKey

,

DSAPublicKey

```java
public interface
DSAKey
```

The interface to a DSA public or private key. DSA (Digital Signature
Algorithm) is defined in NIST's FIPS-186.

**Since:** 1.1
**See Also:** DSAParams

,

Key

,

Signature

public interface

DSAKey

The interface to a DSA public or private key. DSA (Digital Signature
Algorithm) is defined in NIST's FIPS-186.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

DSAParams

getParams

()

Returns the DSA-specific key parameters.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

DSAParams

getParams

()

Returns the DSA-specific key parameters.

---

#### Method Summary

Returns the DSA-specific key parameters.

============ METHOD DETAIL ==========

- Method Detail

- getParams

```java
DSAParams
getParams()
```

Returns the DSA-specific key parameters. These parameters are
never secret.

**Returns:** the DSA-specific key parameters.
**See Also:** DSAParams

Method Detail

- getParams

```java
DSAParams
getParams()
```

Returns the DSA-specific key parameters. These parameters are
never secret.

**Returns:** the DSA-specific key parameters.
**See Also:** DSAParams

---

#### Method Detail

getParams

```java
DSAParams
getParams()
```

Returns the DSA-specific key parameters. These parameters are
never secret.

**Returns:** the DSA-specific key parameters.
**See Also:** DSAParams

---

#### getParams

DSAParams

getParams()

Returns the DSA-specific key parameters. These parameters are
never secret.

---

