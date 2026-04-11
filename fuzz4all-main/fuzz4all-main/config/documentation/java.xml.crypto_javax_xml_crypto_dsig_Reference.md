# Interface Reference

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\Reference.html`

### Class Description

```java
public interface
Reference

extends
URIReference
,
XMLStructure
```

A representation of the

Reference

element as defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML schema is defined as:

```java
<element name="Reference" type="ds:ReferenceType"/>
<complexType name="ReferenceType">
<sequence>
<element ref="ds:Transforms" minOccurs="0"/>
<element ref="ds:DigestMethod"/>
<element ref="ds:DigestValue"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
<attribute name="URI" type="anyURI" use="optional"/>
<attribute name="Type" type="anyURI" use="optional"/>
</complexType>

<element name="DigestValue" type="ds:DigestValueType"/>
<simpleType name="DigestValueType">
<restriction base="base64Binary"/>
</simpleType>
```

A

Reference

instance may be created by invoking one of the

newReference

methods of the

XMLSignatureFactory

class; for example:

```java
XMLSignatureFactory factory = XMLSignatureFactory.getInstance("DOM");
Reference ref = factory.newReference
("http://www.ietf.org/rfc/rfc3275.txt",
factory.newDigestMethod(DigestMethod.SHA1, null));
```

**All Superinterfaces:** URIReference

,

XMLStructure

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### List
<
Transform
> getTransforms()

Returns an

unmodifiable
list

of

Transform

s that are contained in this

Reference

.

**Returns:**
- an unmodifiable list of

Transform

s
(may be empty but never

null

)

---

#### DigestMethod
getDigestMethod()

Returns the digest method of this

Reference

.

**Returns:**
- the digest method

---

#### String
getId()

Returns the optional

Id

attribute of this

Reference

, which permits this reference to be
referenced from elsewhere.

**Returns:**
- the

Id

attribute (may be

null

if not
specified)

---

#### byte[] getDigestValue()

Returns the digest value of this

Reference

.

**Returns:**
- the raw digest value, or

null

if this reference has
not been digested yet. Each invocation of this method returns a new
clone to protect against subsequent modification.

---

#### byte[] getCalculatedDigestValue()

Returns the calculated digest value of this

Reference

after a validation operation. This method is useful for debugging if
the reference fails to validate.

**Returns:**
- the calculated digest value, or

null

if this
reference has not been validated yet. Each invocation of this method
returns a new clone to protect against subsequent modification.

---

#### boolean validate​(
XMLValidateContext
validateContext)
throws
XMLSignatureException

Validates this reference. This method verifies the digest of this
reference.

This method only validates the reference the first time it is
invoked. On subsequent invocations, it returns a cached result.

**Parameters:**
- validateContext

- the validating context

**Returns:**
- true

if this reference was validated successfully;

false

otherwise

**Throws:**
- NullPointerException

- if

validateContext

is

null
- XMLSignatureException

- if an unexpected exception occurs while
validating the reference

---

#### Data
getDereferencedData()

Returns the dereferenced data, if

reference caching

is enabled. This is the result of dereferencing the URI of this
reference during a validation or generation operation.

**Returns:**
- the dereferenced data, or

null

if reference
caching is not enabled or this reference has not been generated or
validated

---

#### InputStream
getDigestInputStream()

Returns the pre-digested input stream, if

reference caching

is enabled. This is the input to the digest operation during a
validation or signing operation.

**Returns:**
- an input stream containing the pre-digested input, or

null

if reference caching is not enabled or this
reference has not been generated or validated

---

### Additional Sections

#### Interface Reference

**All Superinterfaces:** URIReference

,

XMLStructure

```java
public interface
Reference

extends
URIReference
,
XMLStructure
```

A representation of the

Reference

element as defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML schema is defined as:

```java
<element name="Reference" type="ds:ReferenceType"/>
<complexType name="ReferenceType">
<sequence>
<element ref="ds:Transforms" minOccurs="0"/>
<element ref="ds:DigestMethod"/>
<element ref="ds:DigestValue"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
<attribute name="URI" type="anyURI" use="optional"/>
<attribute name="Type" type="anyURI" use="optional"/>
</complexType>

<element name="DigestValue" type="ds:DigestValueType"/>
<simpleType name="DigestValueType">
<restriction base="base64Binary"/>
</simpleType>
```

A

Reference

instance may be created by invoking one of the

newReference

methods of the

XMLSignatureFactory

class; for example:

```java
XMLSignatureFactory factory = XMLSignatureFactory.getInstance("DOM");
Reference ref = factory.newReference
("http://www.ietf.org/rfc/rfc3275.txt",
factory.newDigestMethod(DigestMethod.SHA1, null));
```

**Since:** 1.6
**See Also:** XMLSignatureFactory.newReference(String, DigestMethod)

,

XMLSignatureFactory.newReference(String, DigestMethod, List, String, String)

public interface

Reference

extends

URIReference

,

XMLStructure

A representation of the

Reference

element as defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML schema is defined as:

```java
<element name="Reference" type="ds:ReferenceType"/>
<complexType name="ReferenceType">
<sequence>
<element ref="ds:Transforms" minOccurs="0"/>
<element ref="ds:DigestMethod"/>
<element ref="ds:DigestValue"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
<attribute name="URI" type="anyURI" use="optional"/>
<attribute name="Type" type="anyURI" use="optional"/>
</complexType>

<element name="DigestValue" type="ds:DigestValueType"/>
<simpleType name="DigestValueType">
<restriction base="base64Binary"/>
</simpleType>
```

A

Reference

instance may be created by invoking one of the

newReference

methods of the

XMLSignatureFactory

class; for example:

```java
XMLSignatureFactory factory = XMLSignatureFactory.getInstance("DOM");
Reference ref = factory.newReference
("http://www.ietf.org/rfc/rfc3275.txt",
factory.newDigestMethod(DigestMethod.SHA1, null));
```

<element name="Reference" type="ds:ReferenceType"/>
<complexType name="ReferenceType">
<sequence>
<element ref="ds:Transforms" minOccurs="0"/>
<element ref="ds:DigestMethod"/>
<element ref="ds:DigestValue"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
<attribute name="URI" type="anyURI" use="optional"/>
<attribute name="Type" type="anyURI" use="optional"/>
</complexType>

<element name="DigestValue" type="ds:DigestValueType"/>
<simpleType name="DigestValueType">
<restriction base="base64Binary"/>
</simpleType>

A

Reference

instance may be created by invoking one of the

newReference

methods of the

XMLSignatureFactory

class; for example:

```java
XMLSignatureFactory factory = XMLSignatureFactory.getInstance("DOM");
Reference ref = factory.newReference
("http://www.ietf.org/rfc/rfc3275.txt",
factory.newDigestMethod(DigestMethod.SHA1, null));
```

XMLSignatureFactory factory = XMLSignatureFactory.getInstance("DOM");
Reference ref = factory.newReference
("http://www.ietf.org/rfc/rfc3275.txt",
factory.newDigestMethod(DigestMethod.SHA1, null));

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

byte[]

getCalculatedDigestValue

()

Returns the calculated digest value of this

Reference

after a validation operation.

Data

getDereferencedData

()

Returns the dereferenced data, if

reference caching

is enabled.

InputStream

getDigestInputStream

()

Returns the pre-digested input stream, if

reference caching

is enabled.

DigestMethod

getDigestMethod

()

Returns the digest method of this

Reference

.

byte[]

getDigestValue

()

Returns the digest value of this

Reference

.

String

getId

()

Returns the optional

Id

attribute of this

Reference

, which permits this reference to be
referenced from elsewhere.

List

<

Transform

>

getTransforms

()

Returns an

unmodifiable
list

of

Transform

s that are contained in this

Reference

.

boolean

validate

​(

XMLValidateContext

validateContext)

Validates this reference.

- Methods declared in interface javax.xml.crypto.

URIReference

getType

,

getURI

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

byte[]

getCalculatedDigestValue

()

Returns the calculated digest value of this

Reference

after a validation operation.

Data

getDereferencedData

()

Returns the dereferenced data, if

reference caching

is enabled.

InputStream

getDigestInputStream

()

Returns the pre-digested input stream, if

reference caching

is enabled.

DigestMethod

getDigestMethod

()

Returns the digest method of this

Reference

.

byte[]

getDigestValue

()

Returns the digest value of this

Reference

.

String

getId

()

Returns the optional

Id

attribute of this

Reference

, which permits this reference to be
referenced from elsewhere.

List

<

Transform

>

getTransforms

()

Returns an

unmodifiable
list

of

Transform

s that are contained in this

Reference

.

boolean

validate

​(

XMLValidateContext

validateContext)

Validates this reference.

- Methods declared in interface javax.xml.crypto.

URIReference

getType

,

getURI

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Method Summary

Returns the calculated digest value of this

Reference

after a validation operation.

Returns the dereferenced data, if

reference caching

is enabled.

Returns the pre-digested input stream, if

reference caching

is enabled.

Returns the digest method of this

Reference

.

Returns the digest value of this

Reference

.

Returns the optional

Id

attribute of this

Reference

, which permits this reference to be
referenced from elsewhere.

Returns an

unmodifiable
list

of

Transform

s that are contained in this

Reference

.

Validates this reference.

Methods declared in interface javax.xml.crypto.

URIReference

getType

,

getURI

---

#### Methods declared in interface javax.xml.crypto. URIReference

Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Methods declared in interface javax.xml.crypto. XMLStructure

============ METHOD DETAIL ==========

- Method Detail

- getTransforms

```java
List
<
Transform
> getTransforms()
```

Returns an

unmodifiable
list

of

Transform

s that are contained in this

Reference

.

**Returns:** an unmodifiable list of

Transform

s
(may be empty but never

null

)

- getDigestMethod

```java
DigestMethod
getDigestMethod()
```

Returns the digest method of this

Reference

.

**Returns:** the digest method

- getId

```java
String
getId()
```

Returns the optional

Id

attribute of this

Reference

, which permits this reference to be
referenced from elsewhere.

**Returns:** the

Id

attribute (may be

null

if not
specified)

- getDigestValue

```java
byte[] getDigestValue()
```

Returns the digest value of this

Reference

.

**Returns:** the raw digest value, or

null

if this reference has
not been digested yet. Each invocation of this method returns a new
clone to protect against subsequent modification.

- getCalculatedDigestValue

```java
byte[] getCalculatedDigestValue()
```

Returns the calculated digest value of this

Reference

after a validation operation. This method is useful for debugging if
the reference fails to validate.

**Returns:** the calculated digest value, or

null

if this
reference has not been validated yet. Each invocation of this method
returns a new clone to protect against subsequent modification.

- validate

```java
boolean validate​(
XMLValidateContext
validateContext)
throws
XMLSignatureException
```

Validates this reference. This method verifies the digest of this
reference.

This method only validates the reference the first time it is
invoked. On subsequent invocations, it returns a cached result.

**Parameters:** validateContext

- the validating context
**Returns:** true

if this reference was validated successfully;

false

otherwise
**Throws:** NullPointerException

- if

validateContext

is

null
**Throws:** XMLSignatureException

- if an unexpected exception occurs while
validating the reference

- getDereferencedData

```java
Data
getDereferencedData()
```

Returns the dereferenced data, if

reference caching

is enabled. This is the result of dereferencing the URI of this
reference during a validation or generation operation.

**Returns:** the dereferenced data, or

null

if reference
caching is not enabled or this reference has not been generated or
validated

- getDigestInputStream

```java
InputStream
getDigestInputStream()
```

Returns the pre-digested input stream, if

reference caching

is enabled. This is the input to the digest operation during a
validation or signing operation.

**Returns:** an input stream containing the pre-digested input, or

null

if reference caching is not enabled or this
reference has not been generated or validated

Method Detail

- getTransforms

```java
List
<
Transform
> getTransforms()
```

Returns an

unmodifiable
list

of

Transform

s that are contained in this

Reference

.

**Returns:** an unmodifiable list of

Transform

s
(may be empty but never

null

)

- getDigestMethod

```java
DigestMethod
getDigestMethod()
```

Returns the digest method of this

Reference

.

**Returns:** the digest method

- getId

```java
String
getId()
```

Returns the optional

Id

attribute of this

Reference

, which permits this reference to be
referenced from elsewhere.

**Returns:** the

Id

attribute (may be

null

if not
specified)

- getDigestValue

```java
byte[] getDigestValue()
```

Returns the digest value of this

Reference

.

**Returns:** the raw digest value, or

null

if this reference has
not been digested yet. Each invocation of this method returns a new
clone to protect against subsequent modification.

- getCalculatedDigestValue

```java
byte[] getCalculatedDigestValue()
```

Returns the calculated digest value of this

Reference

after a validation operation. This method is useful for debugging if
the reference fails to validate.

**Returns:** the calculated digest value, or

null

if this
reference has not been validated yet. Each invocation of this method
returns a new clone to protect against subsequent modification.

- validate

```java
boolean validate​(
XMLValidateContext
validateContext)
throws
XMLSignatureException
```

Validates this reference. This method verifies the digest of this
reference.

This method only validates the reference the first time it is
invoked. On subsequent invocations, it returns a cached result.

**Parameters:** validateContext

- the validating context
**Returns:** true

if this reference was validated successfully;

false

otherwise
**Throws:** NullPointerException

- if

validateContext

is

null
**Throws:** XMLSignatureException

- if an unexpected exception occurs while
validating the reference

- getDereferencedData

```java
Data
getDereferencedData()
```

Returns the dereferenced data, if

reference caching

is enabled. This is the result of dereferencing the URI of this
reference during a validation or generation operation.

**Returns:** the dereferenced data, or

null

if reference
caching is not enabled or this reference has not been generated or
validated

- getDigestInputStream

```java
InputStream
getDigestInputStream()
```

Returns the pre-digested input stream, if

reference caching

is enabled. This is the input to the digest operation during a
validation or signing operation.

**Returns:** an input stream containing the pre-digested input, or

null

if reference caching is not enabled or this
reference has not been generated or validated

---

#### Method Detail

getTransforms

```java
List
<
Transform
> getTransforms()
```

Returns an

unmodifiable
list

of

Transform

s that are contained in this

Reference

.

**Returns:** an unmodifiable list of

Transform

s
(may be empty but never

null

)

---

#### getTransforms

List

<

Transform

> getTransforms()

Returns an

unmodifiable
list

of

Transform

s that are contained in this

Reference

.

getDigestMethod

```java
DigestMethod
getDigestMethod()
```

Returns the digest method of this

Reference

.

**Returns:** the digest method

---

#### getDigestMethod

DigestMethod

getDigestMethod()

Returns the digest method of this

Reference

.

getId

```java
String
getId()
```

Returns the optional

Id

attribute of this

Reference

, which permits this reference to be
referenced from elsewhere.

**Returns:** the

Id

attribute (may be

null

if not
specified)

---

#### getId

String

getId()

Returns the optional

Id

attribute of this

Reference

, which permits this reference to be
referenced from elsewhere.

getDigestValue

```java
byte[] getDigestValue()
```

Returns the digest value of this

Reference

.

**Returns:** the raw digest value, or

null

if this reference has
not been digested yet. Each invocation of this method returns a new
clone to protect against subsequent modification.

---

#### getDigestValue

byte[] getDigestValue()

Returns the digest value of this

Reference

.

getCalculatedDigestValue

```java
byte[] getCalculatedDigestValue()
```

Returns the calculated digest value of this

Reference

after a validation operation. This method is useful for debugging if
the reference fails to validate.

**Returns:** the calculated digest value, or

null

if this
reference has not been validated yet. Each invocation of this method
returns a new clone to protect against subsequent modification.

---

#### getCalculatedDigestValue

byte[] getCalculatedDigestValue()

Returns the calculated digest value of this

Reference

after a validation operation. This method is useful for debugging if
the reference fails to validate.

validate

```java
boolean validate​(
XMLValidateContext
validateContext)
throws
XMLSignatureException
```

Validates this reference. This method verifies the digest of this
reference.

This method only validates the reference the first time it is
invoked. On subsequent invocations, it returns a cached result.

**Parameters:** validateContext

- the validating context
**Returns:** true

if this reference was validated successfully;

false

otherwise
**Throws:** NullPointerException

- if

validateContext

is

null
**Throws:** XMLSignatureException

- if an unexpected exception occurs while
validating the reference

---

#### validate

boolean validate​(

XMLValidateContext

validateContext)
throws

XMLSignatureException

Validates this reference. This method verifies the digest of this
reference.

This method only validates the reference the first time it is
invoked. On subsequent invocations, it returns a cached result.

This method only validates the reference the first time it is
invoked. On subsequent invocations, it returns a cached result.

getDereferencedData

```java
Data
getDereferencedData()
```

Returns the dereferenced data, if

reference caching

is enabled. This is the result of dereferencing the URI of this
reference during a validation or generation operation.

**Returns:** the dereferenced data, or

null

if reference
caching is not enabled or this reference has not been generated or
validated

---

#### getDereferencedData

Data

getDereferencedData()

Returns the dereferenced data, if

reference caching

is enabled. This is the result of dereferencing the URI of this
reference during a validation or generation operation.

getDigestInputStream

```java
InputStream
getDigestInputStream()
```

Returns the pre-digested input stream, if

reference caching

is enabled. This is the input to the digest operation during a
validation or signing operation.

**Returns:** an input stream containing the pre-digested input, or

null

if reference caching is not enabled or this
reference has not been generated or validated

---

#### getDigestInputStream

InputStream

getDigestInputStream()

Returns the pre-digested input stream, if

reference caching

is enabled. This is the input to the digest operation during a
validation or signing operation.

---

