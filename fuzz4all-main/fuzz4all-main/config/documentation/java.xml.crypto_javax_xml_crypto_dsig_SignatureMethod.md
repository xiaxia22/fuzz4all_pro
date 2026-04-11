# Interface SignatureMethod

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\SignatureMethod.html`

### Class Description

```java
public interface
SignatureMethod

extends
XMLStructure
,
AlgorithmMethod
```

A representation of the XML

SignatureMethod

element
as defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="SignatureMethod" type="ds:SignatureMethodType"/>
<complexType name="SignatureMethodType" mixed="true">
<sequence>
<element name="HMACOutputLength" minOccurs="0" type="ds:HMACOutputLengthType"/>
<any namespace="##any" minOccurs="0" maxOccurs="unbounded"/>
<!-- (0,unbounded) elements from (1,1) namespace -->
</sequence>
<attribute name="Algorithm" type="anyURI" use="required"/>
</complexType>
```

A

SignatureMethod

instance may be created by invoking the

newSignatureMethod

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
DSA_SHA1

The

DSA-SHA1

(DSS) signature method algorithm URI.

**See Also:**
- Constant Field Values

---

#### static final
String
DSA_SHA256

The

DSA-SHA256

(DSS) signature method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
RSA_SHA1

The

RSA-SHA1

(PKCS #1) signature method algorithm URI.

**See Also:**
- Constant Field Values

---

#### static final
String
RSA_SHA224

The

RSA-SHA224

(PKCS #1) signature method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
RSA_SHA256

The

RSA-SHA256

(PKCS #1) signature method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
RSA_SHA384

The

RSA-SHA384

(PKCS #1) signature method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
RSA_SHA512

The

RSA-SHA512

(PKCS #1) signature method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
SHA1_RSA_MGF1

The

SHA1-RSA-MGF1

(PKCS #1) signature method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
SHA224_RSA_MGF1

The

SHA224-RSA-MGF1

(PKCS #1) signature method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
SHA256_RSA_MGF1

The

SHA256-RSA-MGF1

(PKCS #1) signature method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
SHA384_RSA_MGF1

The

SHA384-RSA-MGF1

(PKCS #1) signature method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
SHA512_RSA_MGF1

The

SHA512-RSA-MGF1

(PKCS #1) signature method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
ECDSA_SHA1

The

ECDSA-SHA1

(FIPS 180-4) signature method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
ECDSA_SHA224

The

ECDSA-SHA224

(FIPS 180-4) signature method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
ECDSA_SHA256

The

ECDSA-SHA256

(FIPS 180-4) signature method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
ECDSA_SHA384

The

ECDSA-SHA384

(FIPS 180-4) signature method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
ECDSA_SHA512

The

ECDSA-SHA512

(FIPS 180-4) signature method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
HMAC_SHA1

The

HMAC-SHA1

MAC signature method algorithm URI

**See Also:**
- Constant Field Values

---

#### static final
String
HMAC_SHA224

The

HMAC-SHA224

MAC signature method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
HMAC_SHA256

The

HMAC-SHA256

MAC signature method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
HMAC_SHA384

The

HMAC-SHA384

MAC signature method algorithm URI.

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### static final
String
HMAC_SHA512

The

HMAC-SHA512

MAC signature method algorithm URI.

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

Returns the algorithm-specific input parameters of this

SignatureMethod

.

The returned parameters can be typecast to a

SignatureMethodParameterSpec

object.

**Specified by:**
- getParameterSpec

in interface

AlgorithmMethod

**Returns:**
- the algorithm-specific input parameters of this

SignatureMethod

(may be

null

if not
specified)

---

### Additional Sections

#### Interface SignatureMethod

**All Superinterfaces:** AlgorithmMethod

,

XMLStructure

```java
public interface
SignatureMethod

extends
XMLStructure
,
AlgorithmMethod
```

A representation of the XML

SignatureMethod

element
as defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="SignatureMethod" type="ds:SignatureMethodType"/>
<complexType name="SignatureMethodType" mixed="true">
<sequence>
<element name="HMACOutputLength" minOccurs="0" type="ds:HMACOutputLengthType"/>
<any namespace="##any" minOccurs="0" maxOccurs="unbounded"/>
<!-- (0,unbounded) elements from (1,1) namespace -->
</sequence>
<attribute name="Algorithm" type="anyURI" use="required"/>
</complexType>
```

A

SignatureMethod

instance may be created by invoking the

newSignatureMethod

method
of the

XMLSignatureFactory

class.

**Since:** 1.6
**See Also:** XMLSignatureFactory.newSignatureMethod(String, SignatureMethodParameterSpec)

public interface

SignatureMethod

extends

XMLStructure

,

AlgorithmMethod

A representation of the XML

SignatureMethod

element
as defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="SignatureMethod" type="ds:SignatureMethodType"/>
<complexType name="SignatureMethodType" mixed="true">
<sequence>
<element name="HMACOutputLength" minOccurs="0" type="ds:HMACOutputLengthType"/>
<any namespace="##any" minOccurs="0" maxOccurs="unbounded"/>
<!-- (0,unbounded) elements from (1,1) namespace -->
</sequence>
<attribute name="Algorithm" type="anyURI" use="required"/>
</complexType>
```

A

SignatureMethod

instance may be created by invoking the

newSignatureMethod

method
of the

XMLSignatureFactory

class.

<element name="SignatureMethod" type="ds:SignatureMethodType"/>
<complexType name="SignatureMethodType" mixed="true">
<sequence>
<element name="HMACOutputLength" minOccurs="0" type="ds:HMACOutputLengthType"/>
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

DSA_SHA1

The

DSA-SHA1

(DSS) signature method algorithm URI.

static

String

DSA_SHA256

The

DSA-SHA256

(DSS) signature method algorithm URI.

static

String

ECDSA_SHA1

The

ECDSA-SHA1

(FIPS 180-4) signature method algorithm URI.

static

String

ECDSA_SHA224

The

ECDSA-SHA224

(FIPS 180-4) signature method algorithm URI.

static

String

ECDSA_SHA256

The

ECDSA-SHA256

(FIPS 180-4) signature method algorithm URI.

static

String

ECDSA_SHA384

The

ECDSA-SHA384

(FIPS 180-4) signature method algorithm URI.

static

String

ECDSA_SHA512

The

ECDSA-SHA512

(FIPS 180-4) signature method algorithm URI.

static

String

HMAC_SHA1

The

HMAC-SHA1

MAC signature method algorithm URI

static

String

HMAC_SHA224

The

HMAC-SHA224

MAC signature method algorithm URI.

static

String

HMAC_SHA256

The

HMAC-SHA256

MAC signature method algorithm URI.

static

String

HMAC_SHA384

The

HMAC-SHA384

MAC signature method algorithm URI.

static

String

HMAC_SHA512

The

HMAC-SHA512

MAC signature method algorithm URI.

static

String

RSA_SHA1

The

RSA-SHA1

(PKCS #1) signature method algorithm URI.

static

String

RSA_SHA224

The

RSA-SHA224

(PKCS #1) signature method algorithm URI.

static

String

RSA_SHA256

The

RSA-SHA256

(PKCS #1) signature method algorithm URI.

static

String

RSA_SHA384

The

RSA-SHA384

(PKCS #1) signature method algorithm URI.

static

String

RSA_SHA512

The

RSA-SHA512

(PKCS #1) signature method algorithm URI.

static

String

SHA1_RSA_MGF1

The

SHA1-RSA-MGF1

(PKCS #1) signature method algorithm URI.

static

String

SHA224_RSA_MGF1

The

SHA224-RSA-MGF1

(PKCS #1) signature method algorithm URI.

static

String

SHA256_RSA_MGF1

The

SHA256-RSA-MGF1

(PKCS #1) signature method algorithm URI.

static

String

SHA384_RSA_MGF1

The

SHA384-RSA-MGF1

(PKCS #1) signature method algorithm URI.

static

String

SHA512_RSA_MGF1

The

SHA512-RSA-MGF1

(PKCS #1) signature method algorithm URI.

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

Returns the algorithm-specific input parameters of this

SignatureMethod

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

DSA_SHA1

The

DSA-SHA1

(DSS) signature method algorithm URI.

static

String

DSA_SHA256

The

DSA-SHA256

(DSS) signature method algorithm URI.

static

String

ECDSA_SHA1

The

ECDSA-SHA1

(FIPS 180-4) signature method algorithm URI.

static

String

ECDSA_SHA224

The

ECDSA-SHA224

(FIPS 180-4) signature method algorithm URI.

static

String

ECDSA_SHA256

The

ECDSA-SHA256

(FIPS 180-4) signature method algorithm URI.

static

String

ECDSA_SHA384

The

ECDSA-SHA384

(FIPS 180-4) signature method algorithm URI.

static

String

ECDSA_SHA512

The

ECDSA-SHA512

(FIPS 180-4) signature method algorithm URI.

static

String

HMAC_SHA1

The

HMAC-SHA1

MAC signature method algorithm URI

static

String

HMAC_SHA224

The

HMAC-SHA224

MAC signature method algorithm URI.

static

String

HMAC_SHA256

The

HMAC-SHA256

MAC signature method algorithm URI.

static

String

HMAC_SHA384

The

HMAC-SHA384

MAC signature method algorithm URI.

static

String

HMAC_SHA512

The

HMAC-SHA512

MAC signature method algorithm URI.

static

String

RSA_SHA1

The

RSA-SHA1

(PKCS #1) signature method algorithm URI.

static

String

RSA_SHA224

The

RSA-SHA224

(PKCS #1) signature method algorithm URI.

static

String

RSA_SHA256

The

RSA-SHA256

(PKCS #1) signature method algorithm URI.

static

String

RSA_SHA384

The

RSA-SHA384

(PKCS #1) signature method algorithm URI.

static

String

RSA_SHA512

The

RSA-SHA512

(PKCS #1) signature method algorithm URI.

static

String

SHA1_RSA_MGF1

The

SHA1-RSA-MGF1

(PKCS #1) signature method algorithm URI.

static

String

SHA224_RSA_MGF1

The

SHA224-RSA-MGF1

(PKCS #1) signature method algorithm URI.

static

String

SHA256_RSA_MGF1

The

SHA256-RSA-MGF1

(PKCS #1) signature method algorithm URI.

static

String

SHA384_RSA_MGF1

The

SHA384-RSA-MGF1

(PKCS #1) signature method algorithm URI.

static

String

SHA512_RSA_MGF1

The

SHA512-RSA-MGF1

(PKCS #1) signature method algorithm URI.

---

#### Field Summary

The

DSA-SHA1

(DSS) signature method algorithm URI.

The

DSA-SHA256

(DSS) signature method algorithm URI.

The

ECDSA-SHA1

(FIPS 180-4) signature method algorithm URI.

The

ECDSA-SHA224

(FIPS 180-4) signature method algorithm URI.

The

ECDSA-SHA256

(FIPS 180-4) signature method algorithm URI.

The

ECDSA-SHA384

(FIPS 180-4) signature method algorithm URI.

The

ECDSA-SHA512

(FIPS 180-4) signature method algorithm URI.

The

HMAC-SHA1

MAC signature method algorithm URI

The

HMAC-SHA224

MAC signature method algorithm URI.

The

HMAC-SHA256

MAC signature method algorithm URI.

The

HMAC-SHA384

MAC signature method algorithm URI.

The

HMAC-SHA512

MAC signature method algorithm URI.

The

RSA-SHA1

(PKCS #1) signature method algorithm URI.

The

RSA-SHA224

(PKCS #1) signature method algorithm URI.

The

RSA-SHA256

(PKCS #1) signature method algorithm URI.

The

RSA-SHA384

(PKCS #1) signature method algorithm URI.

The

RSA-SHA512

(PKCS #1) signature method algorithm URI.

The

SHA1-RSA-MGF1

(PKCS #1) signature method algorithm URI.

The

SHA224-RSA-MGF1

(PKCS #1) signature method algorithm URI.

The

SHA256-RSA-MGF1

(PKCS #1) signature method algorithm URI.

The

SHA384-RSA-MGF1

(PKCS #1) signature method algorithm URI.

The

SHA512-RSA-MGF1

(PKCS #1) signature method algorithm URI.

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

Returns the algorithm-specific input parameters of this

SignatureMethod

.

- Methods declared in interface javax.xml.crypto.

AlgorithmMethod

getAlgorithm

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Method Summary

Returns the algorithm-specific input parameters of this

SignatureMethod

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

- DSA_SHA1

```java
static final
String
DSA_SHA1
```

The

DSA-SHA1

(DSS) signature method algorithm URI.

**See Also:** Constant Field Values

- DSA_SHA256

```java
static final
String
DSA_SHA256
```

The

DSA-SHA256

(DSS) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- RSA_SHA1

```java
static final
String
RSA_SHA1
```

The

RSA-SHA1

(PKCS #1) signature method algorithm URI.

**See Also:** Constant Field Values

- RSA_SHA224

```java
static final
String
RSA_SHA224
```

The

RSA-SHA224

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- RSA_SHA256

```java
static final
String
RSA_SHA256
```

The

RSA-SHA256

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- RSA_SHA384

```java
static final
String
RSA_SHA384
```

The

RSA-SHA384

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- RSA_SHA512

```java
static final
String
RSA_SHA512
```

The

RSA-SHA512

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- SHA1_RSA_MGF1

```java
static final
String
SHA1_RSA_MGF1
```

The

SHA1-RSA-MGF1

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- SHA224_RSA_MGF1

```java
static final
String
SHA224_RSA_MGF1
```

The

SHA224-RSA-MGF1

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- SHA256_RSA_MGF1

```java
static final
String
SHA256_RSA_MGF1
```

The

SHA256-RSA-MGF1

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- SHA384_RSA_MGF1

```java
static final
String
SHA384_RSA_MGF1
```

The

SHA384-RSA-MGF1

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- SHA512_RSA_MGF1

```java
static final
String
SHA512_RSA_MGF1
```

The

SHA512-RSA-MGF1

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- ECDSA_SHA1

```java
static final
String
ECDSA_SHA1
```

The

ECDSA-SHA1

(FIPS 180-4) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- ECDSA_SHA224

```java
static final
String
ECDSA_SHA224
```

The

ECDSA-SHA224

(FIPS 180-4) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- ECDSA_SHA256

```java
static final
String
ECDSA_SHA256
```

The

ECDSA-SHA256

(FIPS 180-4) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- ECDSA_SHA384

```java
static final
String
ECDSA_SHA384
```

The

ECDSA-SHA384

(FIPS 180-4) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- ECDSA_SHA512

```java
static final
String
ECDSA_SHA512
```

The

ECDSA-SHA512

(FIPS 180-4) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- HMAC_SHA1

```java
static final
String
HMAC_SHA1
```

The

HMAC-SHA1

MAC signature method algorithm URI

**See Also:** Constant Field Values

- HMAC_SHA224

```java
static final
String
HMAC_SHA224
```

The

HMAC-SHA224

MAC signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- HMAC_SHA256

```java
static final
String
HMAC_SHA256
```

The

HMAC-SHA256

MAC signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- HMAC_SHA384

```java
static final
String
HMAC_SHA384
```

The

HMAC-SHA384

MAC signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- HMAC_SHA512

```java
static final
String
HMAC_SHA512
```

The

HMAC-SHA512

MAC signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getParameterSpec

```java
AlgorithmParameterSpec
getParameterSpec()
```

Returns the algorithm-specific input parameters of this

SignatureMethod

.

The returned parameters can be typecast to a

SignatureMethodParameterSpec

object.

**Specified by:** getParameterSpec

in interface

AlgorithmMethod
**Returns:** the algorithm-specific input parameters of this

SignatureMethod

(may be

null

if not
specified)

Field Detail

- DSA_SHA1

```java
static final
String
DSA_SHA1
```

The

DSA-SHA1

(DSS) signature method algorithm URI.

**See Also:** Constant Field Values

- DSA_SHA256

```java
static final
String
DSA_SHA256
```

The

DSA-SHA256

(DSS) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- RSA_SHA1

```java
static final
String
RSA_SHA1
```

The

RSA-SHA1

(PKCS #1) signature method algorithm URI.

**See Also:** Constant Field Values

- RSA_SHA224

```java
static final
String
RSA_SHA224
```

The

RSA-SHA224

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- RSA_SHA256

```java
static final
String
RSA_SHA256
```

The

RSA-SHA256

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- RSA_SHA384

```java
static final
String
RSA_SHA384
```

The

RSA-SHA384

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- RSA_SHA512

```java
static final
String
RSA_SHA512
```

The

RSA-SHA512

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- SHA1_RSA_MGF1

```java
static final
String
SHA1_RSA_MGF1
```

The

SHA1-RSA-MGF1

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- SHA224_RSA_MGF1

```java
static final
String
SHA224_RSA_MGF1
```

The

SHA224-RSA-MGF1

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- SHA256_RSA_MGF1

```java
static final
String
SHA256_RSA_MGF1
```

The

SHA256-RSA-MGF1

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- SHA384_RSA_MGF1

```java
static final
String
SHA384_RSA_MGF1
```

The

SHA384-RSA-MGF1

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- SHA512_RSA_MGF1

```java
static final
String
SHA512_RSA_MGF1
```

The

SHA512-RSA-MGF1

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- ECDSA_SHA1

```java
static final
String
ECDSA_SHA1
```

The

ECDSA-SHA1

(FIPS 180-4) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- ECDSA_SHA224

```java
static final
String
ECDSA_SHA224
```

The

ECDSA-SHA224

(FIPS 180-4) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- ECDSA_SHA256

```java
static final
String
ECDSA_SHA256
```

The

ECDSA-SHA256

(FIPS 180-4) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- ECDSA_SHA384

```java
static final
String
ECDSA_SHA384
```

The

ECDSA-SHA384

(FIPS 180-4) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- ECDSA_SHA512

```java
static final
String
ECDSA_SHA512
```

The

ECDSA-SHA512

(FIPS 180-4) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- HMAC_SHA1

```java
static final
String
HMAC_SHA1
```

The

HMAC-SHA1

MAC signature method algorithm URI

**See Also:** Constant Field Values

- HMAC_SHA224

```java
static final
String
HMAC_SHA224
```

The

HMAC-SHA224

MAC signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- HMAC_SHA256

```java
static final
String
HMAC_SHA256
```

The

HMAC-SHA256

MAC signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- HMAC_SHA384

```java
static final
String
HMAC_SHA384
```

The

HMAC-SHA384

MAC signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

- HMAC_SHA512

```java
static final
String
HMAC_SHA512
```

The

HMAC-SHA512

MAC signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### Field Detail

DSA_SHA1

```java
static final
String
DSA_SHA1
```

The

DSA-SHA1

(DSS) signature method algorithm URI.

**See Also:** Constant Field Values

---

#### DSA_SHA1

static final

String

DSA_SHA1

The

DSA-SHA1

(DSS) signature method algorithm URI.

DSA_SHA256

```java
static final
String
DSA_SHA256
```

The

DSA-SHA256

(DSS) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### DSA_SHA256

static final

String

DSA_SHA256

The

DSA-SHA256

(DSS) signature method algorithm URI.

RSA_SHA1

```java
static final
String
RSA_SHA1
```

The

RSA-SHA1

(PKCS #1) signature method algorithm URI.

**See Also:** Constant Field Values

---

#### RSA_SHA1

static final

String

RSA_SHA1

The

RSA-SHA1

(PKCS #1) signature method algorithm URI.

RSA_SHA224

```java
static final
String
RSA_SHA224
```

The

RSA-SHA224

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### RSA_SHA224

static final

String

RSA_SHA224

The

RSA-SHA224

(PKCS #1) signature method algorithm URI.

RSA_SHA256

```java
static final
String
RSA_SHA256
```

The

RSA-SHA256

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### RSA_SHA256

static final

String

RSA_SHA256

The

RSA-SHA256

(PKCS #1) signature method algorithm URI.

RSA_SHA384

```java
static final
String
RSA_SHA384
```

The

RSA-SHA384

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### RSA_SHA384

static final

String

RSA_SHA384

The

RSA-SHA384

(PKCS #1) signature method algorithm URI.

RSA_SHA512

```java
static final
String
RSA_SHA512
```

The

RSA-SHA512

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### RSA_SHA512

static final

String

RSA_SHA512

The

RSA-SHA512

(PKCS #1) signature method algorithm URI.

SHA1_RSA_MGF1

```java
static final
String
SHA1_RSA_MGF1
```

The

SHA1-RSA-MGF1

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### SHA1_RSA_MGF1

static final

String

SHA1_RSA_MGF1

The

SHA1-RSA-MGF1

(PKCS #1) signature method algorithm URI.

SHA224_RSA_MGF1

```java
static final
String
SHA224_RSA_MGF1
```

The

SHA224-RSA-MGF1

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### SHA224_RSA_MGF1

static final

String

SHA224_RSA_MGF1

The

SHA224-RSA-MGF1

(PKCS #1) signature method algorithm URI.

SHA256_RSA_MGF1

```java
static final
String
SHA256_RSA_MGF1
```

The

SHA256-RSA-MGF1

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### SHA256_RSA_MGF1

static final

String

SHA256_RSA_MGF1

The

SHA256-RSA-MGF1

(PKCS #1) signature method algorithm URI.

SHA384_RSA_MGF1

```java
static final
String
SHA384_RSA_MGF1
```

The

SHA384-RSA-MGF1

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### SHA384_RSA_MGF1

static final

String

SHA384_RSA_MGF1

The

SHA384-RSA-MGF1

(PKCS #1) signature method algorithm URI.

SHA512_RSA_MGF1

```java
static final
String
SHA512_RSA_MGF1
```

The

SHA512-RSA-MGF1

(PKCS #1) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### SHA512_RSA_MGF1

static final

String

SHA512_RSA_MGF1

The

SHA512-RSA-MGF1

(PKCS #1) signature method algorithm URI.

ECDSA_SHA1

```java
static final
String
ECDSA_SHA1
```

The

ECDSA-SHA1

(FIPS 180-4) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### ECDSA_SHA1

static final

String

ECDSA_SHA1

The

ECDSA-SHA1

(FIPS 180-4) signature method algorithm URI.

ECDSA_SHA224

```java
static final
String
ECDSA_SHA224
```

The

ECDSA-SHA224

(FIPS 180-4) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### ECDSA_SHA224

static final

String

ECDSA_SHA224

The

ECDSA-SHA224

(FIPS 180-4) signature method algorithm URI.

ECDSA_SHA256

```java
static final
String
ECDSA_SHA256
```

The

ECDSA-SHA256

(FIPS 180-4) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### ECDSA_SHA256

static final

String

ECDSA_SHA256

The

ECDSA-SHA256

(FIPS 180-4) signature method algorithm URI.

ECDSA_SHA384

```java
static final
String
ECDSA_SHA384
```

The

ECDSA-SHA384

(FIPS 180-4) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### ECDSA_SHA384

static final

String

ECDSA_SHA384

The

ECDSA-SHA384

(FIPS 180-4) signature method algorithm URI.

ECDSA_SHA512

```java
static final
String
ECDSA_SHA512
```

The

ECDSA-SHA512

(FIPS 180-4) signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### ECDSA_SHA512

static final

String

ECDSA_SHA512

The

ECDSA-SHA512

(FIPS 180-4) signature method algorithm URI.

HMAC_SHA1

```java
static final
String
HMAC_SHA1
```

The

HMAC-SHA1

MAC signature method algorithm URI

**See Also:** Constant Field Values

---

#### HMAC_SHA1

static final

String

HMAC_SHA1

The

HMAC-SHA1

MAC signature method algorithm URI

HMAC_SHA224

```java
static final
String
HMAC_SHA224
```

The

HMAC-SHA224

MAC signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### HMAC_SHA224

static final

String

HMAC_SHA224

The

HMAC-SHA224

MAC signature method algorithm URI.

HMAC_SHA256

```java
static final
String
HMAC_SHA256
```

The

HMAC-SHA256

MAC signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### HMAC_SHA256

static final

String

HMAC_SHA256

The

HMAC-SHA256

MAC signature method algorithm URI.

HMAC_SHA384

```java
static final
String
HMAC_SHA384
```

The

HMAC-SHA384

MAC signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### HMAC_SHA384

static final

String

HMAC_SHA384

The

HMAC-SHA384

MAC signature method algorithm URI.

HMAC_SHA512

```java
static final
String
HMAC_SHA512
```

The

HMAC-SHA512

MAC signature method algorithm URI.

**Since:** 11
**See Also:** Constant Field Values

---

#### HMAC_SHA512

static final

String

HMAC_SHA512

The

HMAC-SHA512

MAC signature method algorithm URI.

Method Detail

- getParameterSpec

```java
AlgorithmParameterSpec
getParameterSpec()
```

Returns the algorithm-specific input parameters of this

SignatureMethod

.

The returned parameters can be typecast to a

SignatureMethodParameterSpec

object.

**Specified by:** getParameterSpec

in interface

AlgorithmMethod
**Returns:** the algorithm-specific input parameters of this

SignatureMethod

(may be

null

if not
specified)

---

#### Method Detail

getParameterSpec

```java
AlgorithmParameterSpec
getParameterSpec()
```

Returns the algorithm-specific input parameters of this

SignatureMethod

.

The returned parameters can be typecast to a

SignatureMethodParameterSpec

object.

**Specified by:** getParameterSpec

in interface

AlgorithmMethod
**Returns:** the algorithm-specific input parameters of this

SignatureMethod

(may be

null

if not
specified)

---

#### getParameterSpec

AlgorithmParameterSpec

getParameterSpec()

Returns the algorithm-specific input parameters of this

SignatureMethod

.

The returned parameters can be typecast to a

SignatureMethodParameterSpec

object.

The returned parameters can be typecast to a

SignatureMethodParameterSpec

object.

---

