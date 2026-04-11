# Interface XMLSignature.SignatureValue

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\XMLSignature.SignatureValue.html`

### Class Description

```java
public static interface
XMLSignature.SignatureValue

extends
XMLStructure
```

A representation of the XML

SignatureValue

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="SignatureValue" type="ds:SignatureValueType"/>
<complexType name="SignatureValueType">
<simpleContent>
<extension base="base64Binary">
<attribute name="Id" type="ID" use="optional"/>
</extension>
</simpleContent>
</complexType>
```

**All Superinterfaces:** XMLStructure

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getId()

Returns the optional

Id

attribute of this

SignatureValue

, which permits this element to be
referenced from elsewhere.

**Returns:**
- the

Id

attribute (may be

null

if
not specified)

---

#### byte[] getValue()

Returns the signature value of this

SignatureValue

.

**Returns:**
- the signature value (may be

null

if the

XMLSignature

has not been signed yet). Each
invocation of this method returns a new clone of the array to
prevent subsequent modification.

---

#### boolean validate​(
XMLValidateContext
validateContext)
throws
XMLSignatureException

Validates the signature value. This method performs a
cryptographic validation of the signature calculated over the

SignedInfo

of the

XMLSignature

.

This method only validates the signature the first
time it is invoked. On subsequent invocations, it returns a cached
result.

**Parameters:**
- validateContext

- the validating context

**Returns:**
- true

if the signature was
validated successfully;

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
validating the signature

---

### Additional Sections

#### Interface XMLSignature.SignatureValue

**All Superinterfaces:** XMLStructure

**Enclosing interface:** XMLSignature

```java
public static interface
XMLSignature.SignatureValue

extends
XMLStructure
```

A representation of the XML

SignatureValue

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="SignatureValue" type="ds:SignatureValueType"/>
<complexType name="SignatureValueType">
<simpleContent>
<extension base="base64Binary">
<attribute name="Id" type="ID" use="optional"/>
</extension>
</simpleContent>
</complexType>
```

public static interface

XMLSignature.SignatureValue

extends

XMLStructure

A representation of the XML

SignatureValue

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="SignatureValue" type="ds:SignatureValueType"/>
<complexType name="SignatureValueType">
<simpleContent>
<extension base="base64Binary">
<attribute name="Id" type="ID" use="optional"/>
</extension>
</simpleContent>
</complexType>
```

<element name="SignatureValue" type="ds:SignatureValueType"/>
<complexType name="SignatureValueType">
<simpleContent>
<extension base="base64Binary">
<attribute name="Id" type="ID" use="optional"/>
</extension>
</simpleContent>
</complexType>

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getId

()

Returns the optional

Id

attribute of this

SignatureValue

, which permits this element to be
referenced from elsewhere.

byte[]

getValue

()

Returns the signature value of this

SignatureValue

.

boolean

validate

​(

XMLValidateContext

validateContext)

Validates the signature value.

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

String

getId

()

Returns the optional

Id

attribute of this

SignatureValue

, which permits this element to be
referenced from elsewhere.

byte[]

getValue

()

Returns the signature value of this

SignatureValue

.

boolean

validate

​(

XMLValidateContext

validateContext)

Validates the signature value.

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Method Summary

Returns the optional

Id

attribute of this

SignatureValue

, which permits this element to be
referenced from elsewhere.

Returns the signature value of this

SignatureValue

.

Validates the signature value.

Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Methods declared in interface javax.xml.crypto. XMLStructure

============ METHOD DETAIL ==========

- Method Detail

- getId

```java
String
getId()
```

Returns the optional

Id

attribute of this

SignatureValue

, which permits this element to be
referenced from elsewhere.

**Returns:** the

Id

attribute (may be

null

if
not specified)

- getValue

```java
byte[] getValue()
```

Returns the signature value of this

SignatureValue

.

**Returns:** the signature value (may be

null

if the

XMLSignature

has not been signed yet). Each
invocation of this method returns a new clone of the array to
prevent subsequent modification.

- validate

```java
boolean validate​(
XMLValidateContext
validateContext)
throws
XMLSignatureException
```

Validates the signature value. This method performs a
cryptographic validation of the signature calculated over the

SignedInfo

of the

XMLSignature

.

This method only validates the signature the first
time it is invoked. On subsequent invocations, it returns a cached
result.

**Parameters:** validateContext

- the validating context
**Returns:** true

if the signature was
validated successfully;

false

otherwise
**Throws:** NullPointerException

- if

validateContext

is

null
**Throws:** XMLSignatureException

- if an unexpected exception occurs while
validating the signature

Method Detail

- getId

```java
String
getId()
```

Returns the optional

Id

attribute of this

SignatureValue

, which permits this element to be
referenced from elsewhere.

**Returns:** the

Id

attribute (may be

null

if
not specified)

- getValue

```java
byte[] getValue()
```

Returns the signature value of this

SignatureValue

.

**Returns:** the signature value (may be

null

if the

XMLSignature

has not been signed yet). Each
invocation of this method returns a new clone of the array to
prevent subsequent modification.

- validate

```java
boolean validate​(
XMLValidateContext
validateContext)
throws
XMLSignatureException
```

Validates the signature value. This method performs a
cryptographic validation of the signature calculated over the

SignedInfo

of the

XMLSignature

.

This method only validates the signature the first
time it is invoked. On subsequent invocations, it returns a cached
result.

**Parameters:** validateContext

- the validating context
**Returns:** true

if the signature was
validated successfully;

false

otherwise
**Throws:** NullPointerException

- if

validateContext

is

null
**Throws:** XMLSignatureException

- if an unexpected exception occurs while
validating the signature

---

#### Method Detail

getId

```java
String
getId()
```

Returns the optional

Id

attribute of this

SignatureValue

, which permits this element to be
referenced from elsewhere.

**Returns:** the

Id

attribute (may be

null

if
not specified)

---

#### getId

String

getId()

Returns the optional

Id

attribute of this

SignatureValue

, which permits this element to be
referenced from elsewhere.

getValue

```java
byte[] getValue()
```

Returns the signature value of this

SignatureValue

.

**Returns:** the signature value (may be

null

if the

XMLSignature

has not been signed yet). Each
invocation of this method returns a new clone of the array to
prevent subsequent modification.

---

#### getValue

byte[] getValue()

Returns the signature value of this

SignatureValue

.

validate

```java
boolean validate​(
XMLValidateContext
validateContext)
throws
XMLSignatureException
```

Validates the signature value. This method performs a
cryptographic validation of the signature calculated over the

SignedInfo

of the

XMLSignature

.

This method only validates the signature the first
time it is invoked. On subsequent invocations, it returns a cached
result.

**Parameters:** validateContext

- the validating context
**Returns:** true

if the signature was
validated successfully;

false

otherwise
**Throws:** NullPointerException

- if

validateContext

is

null
**Throws:** XMLSignatureException

- if an unexpected exception occurs while
validating the signature

---

#### validate

boolean validate​(

XMLValidateContext

validateContext)
throws

XMLSignatureException

Validates the signature value. This method performs a
cryptographic validation of the signature calculated over the

SignedInfo

of the

XMLSignature

.

This method only validates the signature the first
time it is invoked. On subsequent invocations, it returns a cached
result.

This method only validates the signature the first
time it is invoked. On subsequent invocations, it returns a cached
result.

---

