# Interface CanonicalizationMethod

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\CanonicalizationMethod.html`

### Class Description

```java
public interface
CanonicalizationMethod

extends
Transform
```

A representation of the XML

CanonicalizationMethod

element as defined in the

W3C Recommendation for XML-Signature Syntax and Processing

. The XML
Schema Definition is defined as:

```java
<element name="CanonicalizationMethod" type="ds:CanonicalizationMethodType"/>
<complexType name="CanonicalizationMethodType" mixed="true">
<sequence>
<any namespace="##any" minOccurs="0" maxOccurs="unbounded"/>
<!-- (0,unbounded) elements from (1,1) namespace -->
</sequence>
<attribute name="Algorithm" type="anyURI" use="required"/>
</complexType>
```

A

CanonicalizationMethod

instance may be created by invoking
the

newCanonicalizationMethod

method of the

XMLSignatureFactory

class.

**All Superinterfaces:** AlgorithmMethod

,

Transform

,

XMLStructure

---

### Field Details

#### static final
String
INCLUSIVE

The

Canonical
XML (without comments)

canonicalization method algorithm URI.

**See Also:**
- Constant Field Values

---

#### static final
String
INCLUSIVE_WITH_COMMENTS

The

Canonical XML with comments

canonicalization method algorithm URI.

**See Also:**
- Constant Field Values

---

#### static final
String
EXCLUSIVE

The

Exclusive
Canonical XML (without comments)

canonicalization method algorithm
URI.

**See Also:**
- Constant Field Values

---

#### static final
String
EXCLUSIVE_WITH_COMMENTS

The

Exclusive Canonical XML with comments

canonicalization method
algorithm URI.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### AlgorithmParameterSpec
getParameterSpec()

Returns the algorithm-specific input parameters associated with this

CanonicalizationMethod

.

The returned parameters can be typecast to a

C14NMethodParameterSpec

object.

**Specified by:**
- getParameterSpec

in interface

AlgorithmMethod
- getParameterSpec

in interface

Transform

**Returns:**
- the algorithm-specific input parameters (may be

null

if not specified)

---

### Additional Sections

#### Interface CanonicalizationMethod

**All Superinterfaces:** AlgorithmMethod

,

Transform

,

XMLStructure

```java
public interface
CanonicalizationMethod

extends
Transform
```

A representation of the XML

CanonicalizationMethod

element as defined in the

W3C Recommendation for XML-Signature Syntax and Processing

. The XML
Schema Definition is defined as:

```java
<element name="CanonicalizationMethod" type="ds:CanonicalizationMethodType"/>
<complexType name="CanonicalizationMethodType" mixed="true">
<sequence>
<any namespace="##any" minOccurs="0" maxOccurs="unbounded"/>
<!-- (0,unbounded) elements from (1,1) namespace -->
</sequence>
<attribute name="Algorithm" type="anyURI" use="required"/>
</complexType>
```

A

CanonicalizationMethod

instance may be created by invoking
the

newCanonicalizationMethod

method of the

XMLSignatureFactory

class.

**Since:** 1.6
**See Also:** XMLSignatureFactory.newCanonicalizationMethod(String, C14NMethodParameterSpec)

public interface

CanonicalizationMethod

extends

Transform

A representation of the XML

CanonicalizationMethod

element as defined in the

W3C Recommendation for XML-Signature Syntax and Processing

. The XML
Schema Definition is defined as:

```java
<element name="CanonicalizationMethod" type="ds:CanonicalizationMethodType"/>
<complexType name="CanonicalizationMethodType" mixed="true">
<sequence>
<any namespace="##any" minOccurs="0" maxOccurs="unbounded"/>
<!-- (0,unbounded) elements from (1,1) namespace -->
</sequence>
<attribute name="Algorithm" type="anyURI" use="required"/>
</complexType>
```

A

CanonicalizationMethod

instance may be created by invoking
the

newCanonicalizationMethod

method of the

XMLSignatureFactory

class.

<element name="CanonicalizationMethod" type="ds:CanonicalizationMethodType"/>
<complexType name="CanonicalizationMethodType" mixed="true">
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

EXCLUSIVE

The

Exclusive
Canonical XML (without comments)

canonicalization method algorithm
URI.

static

String

EXCLUSIVE_WITH_COMMENTS

The

Exclusive Canonical XML with comments

canonicalization method
algorithm URI.

static

String

INCLUSIVE

The

Canonical
XML (without comments)

canonicalization method algorithm URI.

static

String

INCLUSIVE_WITH_COMMENTS

The

Canonical XML with comments

canonicalization method algorithm URI.

- Fields declared in interface javax.xml.crypto.dsig.

Transform

BASE64

,

ENVELOPED

,

XPATH

,

XPATH2

,

XSLT

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

CanonicalizationMethod

.

- Methods declared in interface javax.xml.crypto.

AlgorithmMethod

getAlgorithm

- Methods declared in interface javax.xml.crypto.dsig.

Transform

transform

,

transform

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

EXCLUSIVE

The

Exclusive
Canonical XML (without comments)

canonicalization method algorithm
URI.

static

String

EXCLUSIVE_WITH_COMMENTS

The

Exclusive Canonical XML with comments

canonicalization method
algorithm URI.

static

String

INCLUSIVE

The

Canonical
XML (without comments)

canonicalization method algorithm URI.

static

String

INCLUSIVE_WITH_COMMENTS

The

Canonical XML with comments

canonicalization method algorithm URI.

- Fields declared in interface javax.xml.crypto.dsig.

Transform

BASE64

,

ENVELOPED

,

XPATH

,

XPATH2

,

XSLT

---

#### Field Summary

The

Exclusive
Canonical XML (without comments)

canonicalization method algorithm
URI.

The

Exclusive Canonical XML with comments

canonicalization method
algorithm URI.

The

Canonical
XML (without comments)

canonicalization method algorithm URI.

The

Canonical XML with comments

canonicalization method algorithm URI.

Fields declared in interface javax.xml.crypto.dsig.

Transform

BASE64

,

ENVELOPED

,

XPATH

,

XPATH2

,

XSLT

---

#### Fields declared in interface javax.xml.crypto.dsig. Transform

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

CanonicalizationMethod

.

- Methods declared in interface javax.xml.crypto.

AlgorithmMethod

getAlgorithm

- Methods declared in interface javax.xml.crypto.dsig.

Transform

transform

,

transform

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Method Summary

Returns the algorithm-specific input parameters associated with this

CanonicalizationMethod

.

Methods declared in interface javax.xml.crypto.

AlgorithmMethod

getAlgorithm

---

#### Methods declared in interface javax.xml.crypto. AlgorithmMethod

Methods declared in interface javax.xml.crypto.dsig.

Transform

transform

,

transform

---

#### Methods declared in interface javax.xml.crypto.dsig. Transform

Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Methods declared in interface javax.xml.crypto. XMLStructure

============ FIELD DETAIL ===========

- Field Detail

- INCLUSIVE

```java
static final
String
INCLUSIVE
```

The

Canonical
XML (without comments)

canonicalization method algorithm URI.

**See Also:** Constant Field Values

- INCLUSIVE_WITH_COMMENTS

```java
static final
String
INCLUSIVE_WITH_COMMENTS
```

The

Canonical XML with comments

canonicalization method algorithm URI.

**See Also:** Constant Field Values

- EXCLUSIVE

```java
static final
String
EXCLUSIVE
```

The

Exclusive
Canonical XML (without comments)

canonicalization method algorithm
URI.

**See Also:** Constant Field Values

- EXCLUSIVE_WITH_COMMENTS

```java
static final
String
EXCLUSIVE_WITH_COMMENTS
```

The

Exclusive Canonical XML with comments

canonicalization method
algorithm URI.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getParameterSpec

```java
AlgorithmParameterSpec
getParameterSpec()
```

Returns the algorithm-specific input parameters associated with this

CanonicalizationMethod

.

The returned parameters can be typecast to a

C14NMethodParameterSpec

object.

**Specified by:** getParameterSpec

in interface

AlgorithmMethod
**Specified by:** getParameterSpec

in interface

Transform
**Returns:** the algorithm-specific input parameters (may be

null

if not specified)

Field Detail

- INCLUSIVE

```java
static final
String
INCLUSIVE
```

The

Canonical
XML (without comments)

canonicalization method algorithm URI.

**See Also:** Constant Field Values

- INCLUSIVE_WITH_COMMENTS

```java
static final
String
INCLUSIVE_WITH_COMMENTS
```

The

Canonical XML with comments

canonicalization method algorithm URI.

**See Also:** Constant Field Values

- EXCLUSIVE

```java
static final
String
EXCLUSIVE
```

The

Exclusive
Canonical XML (without comments)

canonicalization method algorithm
URI.

**See Also:** Constant Field Values

- EXCLUSIVE_WITH_COMMENTS

```java
static final
String
EXCLUSIVE_WITH_COMMENTS
```

The

Exclusive Canonical XML with comments

canonicalization method
algorithm URI.

**See Also:** Constant Field Values

---

#### Field Detail

INCLUSIVE

```java
static final
String
INCLUSIVE
```

The

Canonical
XML (without comments)

canonicalization method algorithm URI.

**See Also:** Constant Field Values

---

#### INCLUSIVE

static final

String

INCLUSIVE

The

Canonical
XML (without comments)

canonicalization method algorithm URI.

INCLUSIVE_WITH_COMMENTS

```java
static final
String
INCLUSIVE_WITH_COMMENTS
```

The

Canonical XML with comments

canonicalization method algorithm URI.

**See Also:** Constant Field Values

---

#### INCLUSIVE_WITH_COMMENTS

static final

String

INCLUSIVE_WITH_COMMENTS

The

Canonical XML with comments

canonicalization method algorithm URI.

EXCLUSIVE

```java
static final
String
EXCLUSIVE
```

The

Exclusive
Canonical XML (without comments)

canonicalization method algorithm
URI.

**See Also:** Constant Field Values

---

#### EXCLUSIVE

static final

String

EXCLUSIVE

The

Exclusive
Canonical XML (without comments)

canonicalization method algorithm
URI.

EXCLUSIVE_WITH_COMMENTS

```java
static final
String
EXCLUSIVE_WITH_COMMENTS
```

The

Exclusive Canonical XML with comments

canonicalization method
algorithm URI.

**See Also:** Constant Field Values

---

#### EXCLUSIVE_WITH_COMMENTS

static final

String

EXCLUSIVE_WITH_COMMENTS

The

Exclusive Canonical XML with comments

canonicalization method
algorithm URI.

Method Detail

- getParameterSpec

```java
AlgorithmParameterSpec
getParameterSpec()
```

Returns the algorithm-specific input parameters associated with this

CanonicalizationMethod

.

The returned parameters can be typecast to a

C14NMethodParameterSpec

object.

**Specified by:** getParameterSpec

in interface

AlgorithmMethod
**Specified by:** getParameterSpec

in interface

Transform
**Returns:** the algorithm-specific input parameters (may be

null

if not specified)

---

#### Method Detail

getParameterSpec

```java
AlgorithmParameterSpec
getParameterSpec()
```

Returns the algorithm-specific input parameters associated with this

CanonicalizationMethod

.

The returned parameters can be typecast to a

C14NMethodParameterSpec

object.

**Specified by:** getParameterSpec

in interface

AlgorithmMethod
**Specified by:** getParameterSpec

in interface

Transform
**Returns:** the algorithm-specific input parameters (may be

null

if not specified)

---

#### getParameterSpec

AlgorithmParameterSpec

getParameterSpec()

Returns the algorithm-specific input parameters associated with this

CanonicalizationMethod

.

The returned parameters can be typecast to a

C14NMethodParameterSpec

object.

The returned parameters can be typecast to a

C14NMethodParameterSpec

object.

---

