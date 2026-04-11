# Interface AlgorithmMethod

**Source:** `java.xml.crypto\javax\xml\crypto\AlgorithmMethod.html`

### Class Description

```java
public interface
AlgorithmMethod
```

An abstract representation of an algorithm defined in the XML Security
specifications. Subclasses represent specific types of XML security
algorithms, such as a

Transform

.

**All Known Subinterfaces:** CanonicalizationMethod

,

DigestMethod

,

SignatureMethod

,

Transform

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getAlgorithm()

Returns the algorithm URI of this

AlgorithmMethod

.

**Returns:**
- the algorithm URI of this

AlgorithmMethod

---

#### AlgorithmParameterSpec
getParameterSpec()

Returns the algorithm parameters of this

AlgorithmMethod

.

**Returns:**
- the algorithm parameters of this

AlgorithmMethod

.
Returns

null

if this

AlgorithmMethod

does
not require parameters and they are not specified.

---

### Additional Sections

#### Interface AlgorithmMethod

**All Known Subinterfaces:** CanonicalizationMethod

,

DigestMethod

,

SignatureMethod

,

Transform

**All Known Implementing Classes:** TransformService

```java
public interface
AlgorithmMethod
```

An abstract representation of an algorithm defined in the XML Security
specifications. Subclasses represent specific types of XML security
algorithms, such as a

Transform

.

**Since:** 1.6

public interface

AlgorithmMethod

An abstract representation of an algorithm defined in the XML Security
specifications. Subclasses represent specific types of XML security
algorithms, such as a

Transform

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getAlgorithm

()

Returns the algorithm URI of this

AlgorithmMethod

.

AlgorithmParameterSpec

getParameterSpec

()

Returns the algorithm parameters of this

AlgorithmMethod

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getAlgorithm

()

Returns the algorithm URI of this

AlgorithmMethod

.

AlgorithmParameterSpec

getParameterSpec

()

Returns the algorithm parameters of this

AlgorithmMethod

.

---

#### Method Summary

Returns the algorithm URI of this

AlgorithmMethod

.

Returns the algorithm parameters of this

AlgorithmMethod

.

============ METHOD DETAIL ==========

- Method Detail

- getAlgorithm

```java
String
getAlgorithm()
```

Returns the algorithm URI of this

AlgorithmMethod

.

**Returns:** the algorithm URI of this

AlgorithmMethod

- getParameterSpec

```java
AlgorithmParameterSpec
getParameterSpec()
```

Returns the algorithm parameters of this

AlgorithmMethod

.

**Returns:** the algorithm parameters of this

AlgorithmMethod

.
Returns

null

if this

AlgorithmMethod

does
not require parameters and they are not specified.

Method Detail

- getAlgorithm

```java
String
getAlgorithm()
```

Returns the algorithm URI of this

AlgorithmMethod

.

**Returns:** the algorithm URI of this

AlgorithmMethod

- getParameterSpec

```java
AlgorithmParameterSpec
getParameterSpec()
```

Returns the algorithm parameters of this

AlgorithmMethod

.

**Returns:** the algorithm parameters of this

AlgorithmMethod

.
Returns

null

if this

AlgorithmMethod

does
not require parameters and they are not specified.

---

#### Method Detail

getAlgorithm

```java
String
getAlgorithm()
```

Returns the algorithm URI of this

AlgorithmMethod

.

**Returns:** the algorithm URI of this

AlgorithmMethod

---

#### getAlgorithm

String

getAlgorithm()

Returns the algorithm URI of this

AlgorithmMethod

.

getParameterSpec

```java
AlgorithmParameterSpec
getParameterSpec()
```

Returns the algorithm parameters of this

AlgorithmMethod

.

**Returns:** the algorithm parameters of this

AlgorithmMethod

.
Returns

null

if this

AlgorithmMethod

does
not require parameters and they are not specified.

---

#### getParameterSpec

AlgorithmParameterSpec

getParameterSpec()

Returns the algorithm parameters of this

AlgorithmMethod

.

---

