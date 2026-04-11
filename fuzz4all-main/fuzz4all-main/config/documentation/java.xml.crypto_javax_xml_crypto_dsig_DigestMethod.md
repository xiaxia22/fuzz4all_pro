# Interface DigestMethod

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\DigestMethod.html`

### Class Description

```java
public interface
DigestMethod

extends
XMLStructure
,
AlgorithmMethod
```

A representation of the XML

DigestMethod

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="DigestMethod" type="ds:DigestMethodType"/>
<complexType name="DigestMethodType" mixed="true">
<sequence>
<any namespace="##any" minOccurs="0" maxOccurs="unbounded"/>
<!-- (0,unbounded) elements from (1,1) namespace -->
</sequence>
<attribute name="Algorithm" type="anyURI" use="required"/>
</complexType>
```

A

DigestMethod

instance may be created by invoking the

newDigestMethod

method
of the

XMLSignatureFactory

class.

**All Superinterfaces:** AlgorithmMethod

,

XMLStructure

---

### Field Details

#### static final
String
SHA1

The

SHA1

digest method algorithm URI.

**See Also:**
- Constant Field Values

---

#### static final
String
SHA224

The

SHA224

digest method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
SHA256

The

SHA256

digest method algorithm URI.

**See Also:**
- Constant Field Values

---

#### static final
String
SHA384

The

SHA384

digest method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
SHA512

The

SHA512

digest method algorithm URI.

**See Also:**
- Constant Field Values

---

#### static final
String
RIPEMD160

The

RIPEMD-160

digest method algorithm URI.

**See Also:**
- Constant Field Values

---

#### static final
String
SHA3_224

The

SHA3-224

digest method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
SHA3_256

The

SHA3-256

digest method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
SHA3_384

The

SHA3-384

digest method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
SHA3_512

The

SHA3-512

digest method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

### Constructor Details

*No entries found.*

### Method Details

#### AlgorithmParameterSpec
getParameterSpec()

Returns the algorithm-specific input parameters associated with this

DigestMethod

.

The returned parameters can be typecast to a

DigestMethodParameterSpec

object.

**Specified by:**
- getParameterSpec

in interface

AlgorithmMethod

**Returns:**
- the algorithm-specific parameters (may be

null

if
not specified)

---

### Additional Sections

#### Interface DigestMethod

**All Superinterfaces:** AlgorithmMethod

,

XMLStructure

```java
public interface
DigestMethod

extends
XMLStructure
,
AlgorithmMethod
```

A representation of the XML

DigestMethod

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="DigestMethod" type="ds:DigestMethodType"/>
<complexType name="DigestMethodType" mixed="true">
<sequence>
<any namespace="##any" minOccurs="0" maxOccurs="unbounded"/>
<!-- (0,unbounded) elements from (1,1) namespace -->
</sequence>
<attribute name="Algorithm" type="anyURI" use="required"/>
</complexType>
```

A

DigestMethod

instance may be created by invoking the

newDigestMethod

method
of the

XMLSignatureFactory

class.

**Since:** 1.6
**See Also:** XMLSignatureFactory.newDigestMethod(String, DigestMethodParameterSpec)

public interface

DigestMethod

extends

XMLStructure

,

AlgorithmMethod

A representation of the XML

DigestMethod

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="DigestMethod" type="ds:DigestMethodType"/>
<complexType name="DigestMethodType" mixed="true">
<sequence>
<any namespace="##any" minOccurs="0" maxOccurs="unbounded"/>
<!-- (0,unbounded) elements from (1,1) namespace -->
</sequence>
<attribute name="Algorithm" type="anyURI" use="required"/>
</complexType>
```

A

DigestMethod

instance may be created by invoking the

newDigestMethod

method
of the

XMLSignatureFactory

class.

<element name="DigestMethod" type="ds:DigestMethodType"/>
<complexType name="DigestMethodType" mixed="true">
<sequence>
<any namespace="##any" minOccurs="0" maxOccurs="unbounded"/>
<!-- (0,unbounded) elements from (1,1) namespace -->
</sequence>
<attribute name="Algorithm" type="anyURI" use="required"/>
</complexType>

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

RIPEMD160

The

RIPEMD-160

digest method algorithm URI.

static

String

SHA1

The

SHA1

digest method algorithm URI.

static

String

SHA224

The

SHA224

digest method algorithm URI.

static

String

SHA256

The

SHA256

digest method algorithm URI.

static

String

SHA3_224

The

SHA3-224

digest method algorithm URI.

static

String

SHA3_256

The

SHA3-256

digest method algorithm URI.

static

String

SHA3_384

The

SHA3-384

digest method algorithm URI.

static

String

SHA3_512

The

SHA3-512

digest method algorithm URI.

static

String

SHA384

The

SHA384

digest method algorithm URI.

static

String

SHA512

The

SHA512

digest method algorithm URI.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

AlgorithmParameterSpec

getParameterSpec

()

Returns the algorithm-specific input parameters associated with this

DigestMethod

.

- Methods declared in interface javax.xml.crypto.

AlgorithmMethod

getAlgorithm

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

Field Summary

Fields

Modifier and Type

Field

Description

static

String

RIPEMD160

The

RIPEMD-160

digest method algorithm URI.

static

String

SHA1

The

SHA1

digest method algorithm URI.

static

String

SHA224

The

SHA224

digest method algorithm URI.

static

String

SHA256

The

SHA256

digest method algorithm URI.

static

String

SHA3_224

The

SHA3-224

digest method algorithm URI.

static

String

SHA3_256

The

SHA3-256

digest method algorithm URI.

static

String

SHA3_384

The

SHA3-384

digest method algorithm URI.

static

String

SHA3_512

The

SHA3-512

digest method algorithm URI.

static

String

SHA384

The

SHA384

digest method algorithm URI.

static

String

SHA512

The

SHA512

digest method algorithm URI.

---

#### Field Summary

The

RIPEMD-160

digest method algorithm URI.

The

SHA1

digest method algorithm URI.

The

SHA224

digest method algorithm URI.

The

SHA256

digest method algorithm URI.

The

SHA3-224

digest method algorithm URI.

The

SHA3-256

digest method algorithm URI.

The

SHA3-384

digest method algorithm URI.

The

SHA3-512

digest method algorithm URI.

The

SHA384

digest method algorithm URI.

The

SHA512

digest method algorithm URI.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

AlgorithmParameterSpec

getParameterSpec

()

Returns the algorithm-specific input parameters associated with this

DigestMethod

.

- Methods declared in interface javax.xml.crypto.

AlgorithmMethod

getAlgorithm

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Method Summary

Returns the algorithm-specific input parameters associated with this

DigestMethod

.

Methods declared in interface javax.xml.crypto.

AlgorithmMethod

getAlgorithm

---

#### Methods declared in interface javax.xml.crypto. AlgorithmMethod

Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Methods declared in interface javax.xml.crypto. XMLStructure

============ FIELD DETAIL ===========

- Field Detail

- SHA1

```java
static final
String
SHA1
```

The

SHA1

digest method algorithm URI.

**See Also:** Constant Field Values

- SHA224

```java
static final
String
SHA224
```

The

SHA224

digest method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- SHA256

```java
static final
String
SHA256
```

The

SHA256

digest method algorithm URI.

**See Also:** Constant Field Values

- SHA384

```java
static final
String
SHA384
```

The

SHA384

digest method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- SHA512

```java
static final
String
SHA512
```

The

SHA512

digest method algorithm URI.

**See Also:** Constant Field Values

- RIPEMD160

```java
static final
String
RIPEMD160
```

The

RIPEMD-160

digest method algorithm URI.

**See Also:** Constant Field Values

- SHA3_224

```java
static final
String
SHA3_224
```

The

SHA3-224

digest method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- SHA3_256

```java
static final
String
SHA3_256
```

The

SHA3-256

digest method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- SHA3_384

```java
static final
String
SHA3_384
```

The

SHA3-384

digest method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- SHA3_512

```java
static final
String
SHA3_512
```

The

SHA3-512

digest method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getParameterSpec

```java
AlgorithmParameterSpec
getParameterSpec()
```

Returns the algorithm-specific input parameters associated with this

DigestMethod

.

The returned parameters can be typecast to a

DigestMethodParameterSpec

object.

**Specified by:** getParameterSpec

in interface

AlgorithmMethod
**Returns:** the algorithm-specific parameters (may be

null

if
not specified)

Field Detail

- SHA1

```java
static final
String
SHA1
```

The

SHA1

digest method algorithm URI.

**See Also:** Constant Field Values

- SHA224

```java
static final
String
SHA224
```

The

SHA224

digest method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- SHA256

```java
static final
String
SHA256
```

The

SHA256

digest method algorithm URI.

**See Also:** Constant Field Values

- SHA384

```java
static final
String
SHA384
```

The

SHA384

digest method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- SHA512

```java
static final
String
SHA512
```

The

SHA512

digest method algorithm URI.

**See Also:** Constant Field Values

- RIPEMD160

```java
static final
String
RIPEMD160
```

The

RIPEMD-160

digest method algorithm URI.

**See Also:** Constant Field Values

- SHA3_224

```java
static final
String
SHA3_224
```

The

SHA3-224

digest method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- SHA3_256

```java
static final
String
SHA3_256
```

The

SHA3-256

digest method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- SHA3_384

```java
static final
String
SHA3_384
```

The

SHA3-384

digest method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- SHA3_512

```java
static final
String
SHA3_512
```

The

SHA3-512

digest method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### Field Detail

SHA1

```java
static final
String
SHA1
```

The

SHA1

digest method algorithm URI.

**See Also:** Constant Field Values

---

#### SHA1

static final

String

SHA1

The

SHA1

digest method algorithm URI.

SHA224

```java
static final
String
SHA224
```

The

SHA224

digest method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### SHA224

static final

String

SHA224

The

SHA224

digest method algorithm URI.

SHA256

```java
static final
String
SHA256
```

The

SHA256

digest method algorithm URI.

**See Also:** Constant Field Values

---

#### SHA256

static final

String

SHA256

The

SHA256

digest method algorithm URI.

SHA384

```java
static final
String
SHA384
```

The

SHA384

digest method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### SHA384

static final

String

SHA384

The

SHA384

digest method algorithm URI.

SHA512

```java
static final
String
SHA512
```

The

SHA512

digest method algorithm URI.

**See Also:** Constant Field Values

---

#### SHA512

static final

String

SHA512

The

SHA512

digest method algorithm URI.

RIPEMD160

```java
static final
String
RIPEMD160
```

The

RIPEMD-160

digest method algorithm URI.

**See Also:** Constant Field Values

---

#### RIPEMD160

static final

String

RIPEMD160

The

RIPEMD-160

digest method algorithm URI.

SHA3_224

```java
static final
String
SHA3_224
```

The

SHA3-224

digest method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### SHA3_224

static final

String

SHA3_224

The

SHA3-224

digest method algorithm URI.

SHA3_256

```java
static final
String
SHA3_256
```

The

SHA3-256

digest method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### SHA3_256

static final

String

SHA3_256

The

SHA3-256

digest method algorithm URI.

SHA3_384

```java
static final
String
SHA3_384
```

The

SHA3-384

digest method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### SHA3_384

static final

String

SHA3_384

The

SHA3-384

digest method algorithm URI.

SHA3_512

```java
static final
String
SHA3_512
```

The

SHA3-512

digest method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### SHA3_512

static final

String

SHA3_512

The

SHA3-512

digest method algorithm URI.

Method Detail

- getParameterSpec

```java
AlgorithmParameterSpec
getParameterSpec()
```

Returns the algorithm-specific input parameters associated with this

DigestMethod

.

The returned parameters can be typecast to a

DigestMethodParameterSpec

object.

**Specified by:** getParameterSpec

in interface

AlgorithmMethod
**Returns:** the algorithm-specific parameters (may be

null

if
not specified)

---

#### Method Detail

getParameterSpec

```java
AlgorithmParameterSpec
getParameterSpec()
```

Returns the algorithm-specific input parameters associated with this

DigestMethod

.

The returned parameters can be typecast to a

DigestMethodParameterSpec

object.

**Specified by:** getParameterSpec

in interface

AlgorithmMethod
**Returns:** the algorithm-specific parameters (may be

null

if
not specified)

---

#### getParameterSpec

AlgorithmParameterSpec

getParameterSpec()

Returns the algorithm-specific input parameters associated with this

DigestMethod

.

The returned parameters can be typecast to a

DigestMethodParameterSpec

object.

The returned parameters can be typecast to a

DigestMethodParameterSpec

object.

---

