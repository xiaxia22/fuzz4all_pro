# Interface Transform

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\Transform.html`

### Class Description

```java
public interface
Transform

extends
XMLStructure
,
AlgorithmMethod
```

A representation of the XML

Transform

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="Transform" type="ds:TransformType"/>
<complexType name="TransformType" mixed="true">
<choice minOccurs="0" maxOccurs="unbounded">
<any namespace="##other" processContents="lax"/>
<!-- (1,1) elements from (0,unbounded) namespaces -->
<element name="XPath" type="string"/>
</choice>
<attribute name="Algorithm" type="anyURI" use="required"/>
</complexType>
```

A

Transform

instance may be created by invoking the

newTransform

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
BASE64

The

Base64

transform algorithm URI.

**See Also:**
- Constant Field Values

---

#### static final
String
ENVELOPED

The

Enveloped Signature

transform algorithm URI.

**See Also:**
- Constant Field Values

---

#### static final
String
XPATH

The

XPath

transform algorithm URI.

**See Also:**
- Constant Field Values

---

#### static final
String
XPATH2

The

XPath Filter 2

transform algorithm URI.

**See Also:**
- Constant Field Values

---

#### static final
String
XSLT

The

XSLT

transform algorithm URI.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### AlgorithmParameterSpec
getParameterSpec()

Returns the algorithm-specific input parameters associated with this

Transform

.

The returned parameters can be typecast to a

TransformParameterSpec

object.

**Specified by:**
- getParameterSpec

in interface

AlgorithmMethod

**Returns:**
- the algorithm-specific input parameters (may be

null

if not specified)

---

#### Data
transform​(
Data
data,

XMLCryptoContext
context)
throws
TransformException

Transforms the specified data using the underlying transform algorithm.

**Parameters:**
- data

- the data to be transformed
- context

- the

XMLCryptoContext

containing
additional context (may be

null

if not applicable)

**Returns:**
- the transformed data

**Throws:**
- NullPointerException

- if

data

is

null
- TransformException

- if an error occurs while executing the
transform

---

#### Data
transform​(
Data
data,

XMLCryptoContext
context,

OutputStream
os)
throws
TransformException

Transforms the specified data using the underlying transform algorithm.
If the output of this transform is an

OctetStreamData

, then
this method returns

null

and the bytes are written to the
specified

OutputStream

. Otherwise, the

OutputStream

is ignored and the method behaves as if

transform(Data, XMLCryptoContext)

were invoked.

**Parameters:**
- data

- the data to be transformed
- context

- the

XMLCryptoContext

containing
additional context (may be

null

if not applicable)
- os

- the

OutputStream

that should be used to write
the transformed data to

**Returns:**
- the transformed data (or

null

if the data was
written to the

OutputStream

parameter)

**Throws:**
- NullPointerException

- if

data

or

os

is

null
- TransformException

- if an error occurs while executing the
transform

---

### Additional Sections

#### Interface Transform

**All Superinterfaces:** AlgorithmMethod

,

XMLStructure

**All Known Subinterfaces:** CanonicalizationMethod

**All Known Implementing Classes:** TransformService

```java
public interface
Transform

extends
XMLStructure
,
AlgorithmMethod
```

A representation of the XML

Transform

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="Transform" type="ds:TransformType"/>
<complexType name="TransformType" mixed="true">
<choice minOccurs="0" maxOccurs="unbounded">
<any namespace="##other" processContents="lax"/>
<!-- (1,1) elements from (0,unbounded) namespaces -->
<element name="XPath" type="string"/>
</choice>
<attribute name="Algorithm" type="anyURI" use="required"/>
</complexType>
```

A

Transform

instance may be created by invoking the

newTransform

method
of the

XMLSignatureFactory

class.

**Since:** 1.6
**See Also:** XMLSignatureFactory.newTransform(String, TransformParameterSpec)

public interface

Transform

extends

XMLStructure

,

AlgorithmMethod

A representation of the XML

Transform

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="Transform" type="ds:TransformType"/>
<complexType name="TransformType" mixed="true">
<choice minOccurs="0" maxOccurs="unbounded">
<any namespace="##other" processContents="lax"/>
<!-- (1,1) elements from (0,unbounded) namespaces -->
<element name="XPath" type="string"/>
</choice>
<attribute name="Algorithm" type="anyURI" use="required"/>
</complexType>
```

A

Transform

instance may be created by invoking the

newTransform

method
of the

XMLSignatureFactory

class.

<element name="Transform" type="ds:TransformType"/>
<complexType name="TransformType" mixed="true">
<choice minOccurs="0" maxOccurs="unbounded">
<any namespace="##other" processContents="lax"/>
<!-- (1,1) elements from (0,unbounded) namespaces -->
<element name="XPath" type="string"/>
</choice>
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

BASE64

The

Base64

transform algorithm URI.

static

String

ENVELOPED

The

Enveloped Signature

transform algorithm URI.

static

String

XPATH

The

XPath

transform algorithm URI.

static

String

XPATH2

The

XPath Filter 2

transform algorithm URI.

static

String

XSLT

The

XSLT

transform algorithm URI.

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

Transform

.

Data

transform

​(

Data

data,

XMLCryptoContext

context)

Transforms the specified data using the underlying transform algorithm.

Data

transform

​(

Data

data,

XMLCryptoContext

context,

OutputStream

os)

Transforms the specified data using the underlying transform algorithm.

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

BASE64

The

Base64

transform algorithm URI.

static

String

ENVELOPED

The

Enveloped Signature

transform algorithm URI.

static

String

XPATH

The

XPath

transform algorithm URI.

static

String

XPATH2

The

XPath Filter 2

transform algorithm URI.

static

String

XSLT

The

XSLT

transform algorithm URI.

---

#### Field Summary

The

Base64

transform algorithm URI.

The

Enveloped Signature

transform algorithm URI.

The

XPath

transform algorithm URI.

The

XPath Filter 2

transform algorithm URI.

The

XSLT

transform algorithm URI.

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

Transform

.

Data

transform

​(

Data

data,

XMLCryptoContext

context)

Transforms the specified data using the underlying transform algorithm.

Data

transform

​(

Data

data,

XMLCryptoContext

context,

OutputStream

os)

Transforms the specified data using the underlying transform algorithm.

- Methods declared in interface javax.xml.crypto.

AlgorithmMethod

getAlgorithm

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Method Summary

Returns the algorithm-specific input parameters associated with this

Transform

.

Transforms the specified data using the underlying transform algorithm.

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

- BASE64

```java
static final
String
BASE64
```

The

Base64

transform algorithm URI.

**See Also:** Constant Field Values

- ENVELOPED

```java
static final
String
ENVELOPED
```

The

Enveloped Signature

transform algorithm URI.

**See Also:** Constant Field Values

- XPATH

```java
static final
String
XPATH
```

The

XPath

transform algorithm URI.

**See Also:** Constant Field Values

- XPATH2

```java
static final
String
XPATH2
```

The

XPath Filter 2

transform algorithm URI.

**See Also:** Constant Field Values

- XSLT

```java
static final
String
XSLT
```

The

XSLT

transform algorithm URI.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getParameterSpec

```java
AlgorithmParameterSpec
getParameterSpec()
```

Returns the algorithm-specific input parameters associated with this

Transform

.

The returned parameters can be typecast to a

TransformParameterSpec

object.

**Specified by:** getParameterSpec

in interface

AlgorithmMethod
**Returns:** the algorithm-specific input parameters (may be

null

if not specified)

- transform

```java
Data
transform​(
Data
data,

XMLCryptoContext
context)
throws
TransformException
```

Transforms the specified data using the underlying transform algorithm.

**Parameters:** data

- the data to be transformed
**Parameters:** context

- the

XMLCryptoContext

containing
additional context (may be

null

if not applicable)
**Returns:** the transformed data
**Throws:** NullPointerException

- if

data

is

null
**Throws:** TransformException

- if an error occurs while executing the
transform

- transform

```java
Data
transform​(
Data
data,

XMLCryptoContext
context,

OutputStream
os)
throws
TransformException
```

Transforms the specified data using the underlying transform algorithm.
If the output of this transform is an

OctetStreamData

, then
this method returns

null

and the bytes are written to the
specified

OutputStream

. Otherwise, the

OutputStream

is ignored and the method behaves as if

transform(Data, XMLCryptoContext)

were invoked.

**Parameters:** data

- the data to be transformed
**Parameters:** context

- the

XMLCryptoContext

containing
additional context (may be

null

if not applicable)
**Parameters:** os

- the

OutputStream

that should be used to write
the transformed data to
**Returns:** the transformed data (or

null

if the data was
written to the

OutputStream

parameter)
**Throws:** NullPointerException

- if

data

or

os

is

null
**Throws:** TransformException

- if an error occurs while executing the
transform

Field Detail

- BASE64

```java
static final
String
BASE64
```

The

Base64

transform algorithm URI.

**See Also:** Constant Field Values

- ENVELOPED

```java
static final
String
ENVELOPED
```

The

Enveloped Signature

transform algorithm URI.

**See Also:** Constant Field Values

- XPATH

```java
static final
String
XPATH
```

The

XPath

transform algorithm URI.

**See Also:** Constant Field Values

- XPATH2

```java
static final
String
XPATH2
```

The

XPath Filter 2

transform algorithm URI.

**See Also:** Constant Field Values

- XSLT

```java
static final
String
XSLT
```

The

XSLT

transform algorithm URI.

**See Also:** Constant Field Values

---

#### Field Detail

BASE64

```java
static final
String
BASE64
```

The

Base64

transform algorithm URI.

**See Also:** Constant Field Values

---

#### BASE64

static final

String

BASE64

The

Base64

transform algorithm URI.

ENVELOPED

```java
static final
String
ENVELOPED
```

The

Enveloped Signature

transform algorithm URI.

**See Also:** Constant Field Values

---

#### ENVELOPED

static final

String

ENVELOPED

The

Enveloped Signature

transform algorithm URI.

XPATH

```java
static final
String
XPATH
```

The

XPath

transform algorithm URI.

**See Also:** Constant Field Values

---

#### XPATH

static final

String

XPATH

The

XPath

transform algorithm URI.

XPATH2

```java
static final
String
XPATH2
```

The

XPath Filter 2

transform algorithm URI.

**See Also:** Constant Field Values

---

#### XPATH2

static final

String

XPATH2

The

XPath Filter 2

transform algorithm URI.

XSLT

```java
static final
String
XSLT
```

The

XSLT

transform algorithm URI.

**See Also:** Constant Field Values

---

#### XSLT

static final

String

XSLT

The

XSLT

transform algorithm URI.

Method Detail

- getParameterSpec

```java
AlgorithmParameterSpec
getParameterSpec()
```

Returns the algorithm-specific input parameters associated with this

Transform

.

The returned parameters can be typecast to a

TransformParameterSpec

object.

**Specified by:** getParameterSpec

in interface

AlgorithmMethod
**Returns:** the algorithm-specific input parameters (may be

null

if not specified)

- transform

```java
Data
transform​(
Data
data,

XMLCryptoContext
context)
throws
TransformException
```

Transforms the specified data using the underlying transform algorithm.

**Parameters:** data

- the data to be transformed
**Parameters:** context

- the

XMLCryptoContext

containing
additional context (may be

null

if not applicable)
**Returns:** the transformed data
**Throws:** NullPointerException

- if

data

is

null
**Throws:** TransformException

- if an error occurs while executing the
transform

- transform

```java
Data
transform​(
Data
data,

XMLCryptoContext
context,

OutputStream
os)
throws
TransformException
```

Transforms the specified data using the underlying transform algorithm.
If the output of this transform is an

OctetStreamData

, then
this method returns

null

and the bytes are written to the
specified

OutputStream

. Otherwise, the

OutputStream

is ignored and the method behaves as if

transform(Data, XMLCryptoContext)

were invoked.

**Parameters:** data

- the data to be transformed
**Parameters:** context

- the

XMLCryptoContext

containing
additional context (may be

null

if not applicable)
**Parameters:** os

- the

OutputStream

that should be used to write
the transformed data to
**Returns:** the transformed data (or

null

if the data was
written to the

OutputStream

parameter)
**Throws:** NullPointerException

- if

data

or

os

is

null
**Throws:** TransformException

- if an error occurs while executing the
transform

---

#### Method Detail

getParameterSpec

```java
AlgorithmParameterSpec
getParameterSpec()
```

Returns the algorithm-specific input parameters associated with this

Transform

.

The returned parameters can be typecast to a

TransformParameterSpec

object.

**Specified by:** getParameterSpec

in interface

AlgorithmMethod
**Returns:** the algorithm-specific input parameters (may be

null

if not specified)

---

#### getParameterSpec

AlgorithmParameterSpec

getParameterSpec()

Returns the algorithm-specific input parameters associated with this

Transform

.

The returned parameters can be typecast to a

TransformParameterSpec

object.

The returned parameters can be typecast to a

TransformParameterSpec

object.

transform

```java
Data
transform​(
Data
data,

XMLCryptoContext
context)
throws
TransformException
```

Transforms the specified data using the underlying transform algorithm.

**Parameters:** data

- the data to be transformed
**Parameters:** context

- the

XMLCryptoContext

containing
additional context (may be

null

if not applicable)
**Returns:** the transformed data
**Throws:** NullPointerException

- if

data

is

null
**Throws:** TransformException

- if an error occurs while executing the
transform

---

#### transform

Data

transform​(

Data

data,

XMLCryptoContext

context)
throws

TransformException

Transforms the specified data using the underlying transform algorithm.

transform

```java
Data
transform​(
Data
data,

XMLCryptoContext
context,

OutputStream
os)
throws
TransformException
```

Transforms the specified data using the underlying transform algorithm.
If the output of this transform is an

OctetStreamData

, then
this method returns

null

and the bytes are written to the
specified

OutputStream

. Otherwise, the

OutputStream

is ignored and the method behaves as if

transform(Data, XMLCryptoContext)

were invoked.

**Parameters:** data

- the data to be transformed
**Parameters:** context

- the

XMLCryptoContext

containing
additional context (may be

null

if not applicable)
**Parameters:** os

- the

OutputStream

that should be used to write
the transformed data to
**Returns:** the transformed data (or

null

if the data was
written to the

OutputStream

parameter)
**Throws:** NullPointerException

- if

data

or

os

is

null
**Throws:** TransformException

- if an error occurs while executing the
transform

---

#### transform

Data

transform​(

Data

data,

XMLCryptoContext

context,

OutputStream

os)
throws

TransformException

Transforms the specified data using the underlying transform algorithm.
If the output of this transform is an

OctetStreamData

, then
this method returns

null

and the bytes are written to the
specified

OutputStream

. Otherwise, the

OutputStream

is ignored and the method behaves as if

transform(Data, XMLCryptoContext)

were invoked.

---

