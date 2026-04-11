# Interface ECKey

**Source:** `java.base\java\security\interfaces\ECKey.html`

### Class Description

```java
public interface
ECKey
```

The interface to an elliptic curve (EC) key.

**All Known Subinterfaces:** ECPrivateKey

,

ECPublicKey

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### ECParameterSpec
getParams()

Returns the domain parameters associated
with this key. The domain parameters are
either explicitly specified or implicitly
created during key generation.

**Returns:**
- the associated domain parameters.

---

### Additional Sections

#### Interface ECKey

**All Known Subinterfaces:** ECPrivateKey

,

ECPublicKey

```java
public interface
ECKey
```

The interface to an elliptic curve (EC) key.

**Since:** 1.5

public interface

ECKey

The interface to an elliptic curve (EC) key.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ECParameterSpec

getParams

()

Returns the domain parameters associated
with this key.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

ECParameterSpec

getParams

()

Returns the domain parameters associated
with this key.

---

#### Method Summary

Returns the domain parameters associated
with this key.

============ METHOD DETAIL ==========

- Method Detail

- getParams

```java
ECParameterSpec
getParams()
```

Returns the domain parameters associated
with this key. The domain parameters are
either explicitly specified or implicitly
created during key generation.

**Returns:** the associated domain parameters.

Method Detail

- getParams

```java
ECParameterSpec
getParams()
```

Returns the domain parameters associated
with this key. The domain parameters are
either explicitly specified or implicitly
created during key generation.

**Returns:** the associated domain parameters.

---

#### Method Detail

getParams

```java
ECParameterSpec
getParams()
```

Returns the domain parameters associated
with this key. The domain parameters are
either explicitly specified or implicitly
created during key generation.

**Returns:** the associated domain parameters.

---

#### getParams

ECParameterSpec

getParams()

Returns the domain parameters associated
with this key. The domain parameters are
either explicitly specified or implicitly
created during key generation.

---

