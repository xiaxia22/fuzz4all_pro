# Interface XMLSignature

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\XMLSignature.html`

### Class Description

```java
public interface
XMLSignature

extends
XMLStructure
```

A representation of the XML

Signature

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
This class contains methods for signing and validating XML signatures
with behavior as defined by the W3C specification. The XML Schema Definition
is defined as:

```java
<element name="Signature" type="ds:SignatureType"/>
<complexType name="SignatureType">
<sequence>
<element ref="ds:SignedInfo"/>
<element ref="ds:SignatureValue"/>
<element ref="ds:KeyInfo" minOccurs="0"/>
<element ref="ds:Object" minOccurs="0" maxOccurs="unbounded"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
</complexType>
```

An

XMLSignature

instance may be created by invoking one of the

newXMLSignature

methods of the

XMLSignatureFactory

class.

If the contents of the underlying document containing the

XMLSignature

are subsequently modified, the behavior is
undefined.

Note that this class is named

XMLSignature

rather than

Signature

to avoid naming clashes with the existing

java.security.Signature

class.

**All Superinterfaces:** XMLStructure

---

### Field Details

#### static final
String
XMLNS

The XML Namespace URI of the W3C Recommendation for XML-Signature
Syntax and Processing.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### boolean validate​(
XMLValidateContext
validateContext)
throws
XMLSignatureException

Validates the signature according to the

core validation processing rules

. This method validates the
signature using the existing state, it does not unmarshal and
reinitialize the contents of the

XMLSignature

using the
location information specified in the context.

This method only validates the signature the first time it is
invoked. On subsequent invocations, it returns a cached result.

**Parameters:**
- validateContext

- the validating context

**Returns:**
- true

if the signature passed core validation,
otherwise

false

**Throws:**
- ClassCastException

- if the type of

validateContext

is not compatible with this

XMLSignature
- NullPointerException

- if

validateContext

is

null
- XMLSignatureException

- if an unexpected error occurs during
validation that prevented the validation operation from completing

---

#### KeyInfo
getKeyInfo()

Returns the key info of this

XMLSignature

.

**Returns:**
- the key info (may be

null

if not specified)

---

#### SignedInfo
getSignedInfo()

Returns the signed info of this

XMLSignature

.

**Returns:**
- the signed info (never

null

)

---

#### List
<
XMLObject
> getObjects()

Returns an

unmodifiable
list

of

XMLObject

s contained in this

XMLSignature

.

**Returns:**
- an unmodifiable list of

XMLObject

s (may be empty
but never

null

)

---

#### String
getId()

Returns the optional Id of this

XMLSignature

.

**Returns:**
- the Id (may be

null

if not specified)

---

#### XMLSignature.SignatureValue
getSignatureValue()

Returns the signature value of this

XMLSignature

.

**Returns:**
- the signature value

---

#### void sign​(
XMLSignContext
signContext)
throws
MarshalException
,

XMLSignatureException

Signs this

XMLSignature

.

If this method throws an exception, this

XMLSignature

and
the

signContext

parameter will be left in the state that
it was in prior to the invocation.

**Parameters:**
- signContext

- the signing context

**Throws:**
- ClassCastException

- if the type of

signContext

is
not compatible with this

XMLSignature
- NullPointerException

- if

signContext

is

null
- MarshalException

- if an exception occurs while marshalling
- XMLSignatureException

- if an unexpected exception occurs while
generating the signature

---

#### KeySelectorResult
getKeySelectorResult()

Returns the result of the

KeySelector

, if specified, after
this

XMLSignature

has been signed or validated.

**Returns:**
- the key selector result, or

null

if a key
selector has not been specified or this

XMLSignature

has not been signed or validated

---

### Additional Sections

#### Interface XMLSignature

**All Superinterfaces:** XMLStructure

```java
public interface
XMLSignature

extends
XMLStructure
```

A representation of the XML

Signature

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
This class contains methods for signing and validating XML signatures
with behavior as defined by the W3C specification. The XML Schema Definition
is defined as:

```java
<element name="Signature" type="ds:SignatureType"/>
<complexType name="SignatureType">
<sequence>
<element ref="ds:SignedInfo"/>
<element ref="ds:SignatureValue"/>
<element ref="ds:KeyInfo" minOccurs="0"/>
<element ref="ds:Object" minOccurs="0" maxOccurs="unbounded"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
</complexType>
```

An

XMLSignature

instance may be created by invoking one of the

newXMLSignature

methods of the

XMLSignatureFactory

class.

If the contents of the underlying document containing the

XMLSignature

are subsequently modified, the behavior is
undefined.

Note that this class is named

XMLSignature

rather than

Signature

to avoid naming clashes with the existing

java.security.Signature

class.

**Since:** 1.6
**See Also:** XMLSignatureFactory.newXMLSignature(SignedInfo, KeyInfo)

,

XMLSignatureFactory.newXMLSignature(SignedInfo, KeyInfo, List, String, String)

public interface

XMLSignature

extends

XMLStructure

A representation of the XML

Signature

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
This class contains methods for signing and validating XML signatures
with behavior as defined by the W3C specification. The XML Schema Definition
is defined as:

```java
<element name="Signature" type="ds:SignatureType"/>
<complexType name="SignatureType">
<sequence>
<element ref="ds:SignedInfo"/>
<element ref="ds:SignatureValue"/>
<element ref="ds:KeyInfo" minOccurs="0"/>
<element ref="ds:Object" minOccurs="0" maxOccurs="unbounded"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
</complexType>
```

An

XMLSignature

instance may be created by invoking one of the

newXMLSignature

methods of the

XMLSignatureFactory

class.

If the contents of the underlying document containing the

XMLSignature

are subsequently modified, the behavior is
undefined.

Note that this class is named

XMLSignature

rather than

Signature

to avoid naming clashes with the existing

java.security.Signature

class.

<element name="Signature" type="ds:SignatureType"/>
<complexType name="SignatureType">
<sequence>
<element ref="ds:SignedInfo"/>
<element ref="ds:SignatureValue"/>
<element ref="ds:KeyInfo" minOccurs="0"/>
<element ref="ds:Object" minOccurs="0" maxOccurs="unbounded"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
</complexType>

An

XMLSignature

instance may be created by invoking one of the

newXMLSignature

methods of the

XMLSignatureFactory

class.

If the contents of the underlying document containing the

XMLSignature

are subsequently modified, the behavior is
undefined.

Note that this class is named

XMLSignature

rather than

Signature

to avoid naming clashes with the existing

java.security.Signature

class.

If the contents of the underlying document containing the

XMLSignature

are subsequently modified, the behavior is
undefined.

Note that this class is named

XMLSignature

rather than

Signature

to avoid naming clashes with the existing

java.security.Signature

class.

Note that this class is named

XMLSignature

rather than

Signature

to avoid naming clashes with the existing

java.security.Signature

class.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

XMLSignature.SignatureValue

A representation of the XML

SignatureValue

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

XMLNS

The XML Namespace URI of the W3C Recommendation for XML-Signature
Syntax and Processing.

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

Returns the optional Id of this

XMLSignature

.

KeyInfo

getKeyInfo

()

Returns the key info of this

XMLSignature

.

KeySelectorResult

getKeySelectorResult

()

Returns the result of the

KeySelector

, if specified, after
this

XMLSignature

has been signed or validated.

List

<

XMLObject

>

getObjects

()

Returns an

unmodifiable
list

of

XMLObject

s contained in this

XMLSignature

.

XMLSignature.SignatureValue

getSignatureValue

()

Returns the signature value of this

XMLSignature

.

SignedInfo

getSignedInfo

()

Returns the signed info of this

XMLSignature

.

void

sign

​(

XMLSignContext

signContext)

Signs this

XMLSignature

.

boolean

validate

​(

XMLValidateContext

validateContext)

Validates the signature according to the

core validation processing rules

.

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

Nested Class Summary

Nested Classes

Modifier and Type

Interface

Description

static interface

XMLSignature.SignatureValue

A representation of the XML

SignatureValue

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.

---

#### Nested Class Summary

A representation of the XML

SignatureValue

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.

Field Summary

Fields

Modifier and Type

Field

Description

static

String

XMLNS

The XML Namespace URI of the W3C Recommendation for XML-Signature
Syntax and Processing.

---

#### Field Summary

The XML Namespace URI of the W3C Recommendation for XML-Signature
Syntax and Processing.

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

Returns the optional Id of this

XMLSignature

.

KeyInfo

getKeyInfo

()

Returns the key info of this

XMLSignature

.

KeySelectorResult

getKeySelectorResult

()

Returns the result of the

KeySelector

, if specified, after
this

XMLSignature

has been signed or validated.

List

<

XMLObject

>

getObjects

()

Returns an

unmodifiable
list

of

XMLObject

s contained in this

XMLSignature

.

XMLSignature.SignatureValue

getSignatureValue

()

Returns the signature value of this

XMLSignature

.

SignedInfo

getSignedInfo

()

Returns the signed info of this

XMLSignature

.

void

sign

​(

XMLSignContext

signContext)

Signs this

XMLSignature

.

boolean

validate

​(

XMLValidateContext

validateContext)

Validates the signature according to the

core validation processing rules

.

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Method Summary

Returns the optional Id of this

XMLSignature

.

Returns the key info of this

XMLSignature

.

Returns the result of the

KeySelector

, if specified, after
this

XMLSignature

has been signed or validated.

Returns an

unmodifiable
list

of

XMLObject

s contained in this

XMLSignature

.

Returns the signature value of this

XMLSignature

.

Returns the signed info of this

XMLSignature

.

Signs this

XMLSignature

.

Validates the signature according to the

core validation processing rules

.

Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Methods declared in interface javax.xml.crypto. XMLStructure

============ FIELD DETAIL ===========

- Field Detail

- XMLNS

```java
static final
String
XMLNS
```

The XML Namespace URI of the W3C Recommendation for XML-Signature
Syntax and Processing.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- validate

```java
boolean validate​(
XMLValidateContext
validateContext)
throws
XMLSignatureException
```

Validates the signature according to the

core validation processing rules

. This method validates the
signature using the existing state, it does not unmarshal and
reinitialize the contents of the

XMLSignature

using the
location information specified in the context.

This method only validates the signature the first time it is
invoked. On subsequent invocations, it returns a cached result.

**Parameters:** validateContext

- the validating context
**Returns:** true

if the signature passed core validation,
otherwise

false
**Throws:** ClassCastException

- if the type of

validateContext

is not compatible with this

XMLSignature
**Throws:** NullPointerException

- if

validateContext

is

null
**Throws:** XMLSignatureException

- if an unexpected error occurs during
validation that prevented the validation operation from completing

- getKeyInfo

```java
KeyInfo
getKeyInfo()
```

Returns the key info of this

XMLSignature

.

**Returns:** the key info (may be

null

if not specified)

- getSignedInfo

```java
SignedInfo
getSignedInfo()
```

Returns the signed info of this

XMLSignature

.

**Returns:** the signed info (never

null

)

- getObjects

```java
List
<
XMLObject
> getObjects()
```

Returns an

unmodifiable
list

of

XMLObject

s contained in this

XMLSignature

.

**Returns:** an unmodifiable list of

XMLObject

s (may be empty
but never

null

)

- getId

```java
String
getId()
```

Returns the optional Id of this

XMLSignature

.

**Returns:** the Id (may be

null

if not specified)

- getSignatureValue

```java
XMLSignature.SignatureValue
getSignatureValue()
```

Returns the signature value of this

XMLSignature

.

**Returns:** the signature value

- sign

```java
void sign​(
XMLSignContext
signContext)
throws
MarshalException
,

XMLSignatureException
```

Signs this

XMLSignature

.

If this method throws an exception, this

XMLSignature

and
the

signContext

parameter will be left in the state that
it was in prior to the invocation.

**Parameters:** signContext

- the signing context
**Throws:** ClassCastException

- if the type of

signContext

is
not compatible with this

XMLSignature
**Throws:** NullPointerException

- if

signContext

is

null
**Throws:** MarshalException

- if an exception occurs while marshalling
**Throws:** XMLSignatureException

- if an unexpected exception occurs while
generating the signature

- getKeySelectorResult

```java
KeySelectorResult
getKeySelectorResult()
```

Returns the result of the

KeySelector

, if specified, after
this

XMLSignature

has been signed or validated.

**Returns:** the key selector result, or

null

if a key
selector has not been specified or this

XMLSignature

has not been signed or validated

Field Detail

- XMLNS

```java
static final
String
XMLNS
```

The XML Namespace URI of the W3C Recommendation for XML-Signature
Syntax and Processing.

**See Also:** Constant Field Values

---

#### Field Detail

XMLNS

```java
static final
String
XMLNS
```

The XML Namespace URI of the W3C Recommendation for XML-Signature
Syntax and Processing.

**See Also:** Constant Field Values

---

#### XMLNS

static final

String

XMLNS

The XML Namespace URI of the W3C Recommendation for XML-Signature
Syntax and Processing.

Method Detail

- validate

```java
boolean validate​(
XMLValidateContext
validateContext)
throws
XMLSignatureException
```

Validates the signature according to the

core validation processing rules

. This method validates the
signature using the existing state, it does not unmarshal and
reinitialize the contents of the

XMLSignature

using the
location information specified in the context.

This method only validates the signature the first time it is
invoked. On subsequent invocations, it returns a cached result.

**Parameters:** validateContext

- the validating context
**Returns:** true

if the signature passed core validation,
otherwise

false
**Throws:** ClassCastException

- if the type of

validateContext

is not compatible with this

XMLSignature
**Throws:** NullPointerException

- if

validateContext

is

null
**Throws:** XMLSignatureException

- if an unexpected error occurs during
validation that prevented the validation operation from completing

- getKeyInfo

```java
KeyInfo
getKeyInfo()
```

Returns the key info of this

XMLSignature

.

**Returns:** the key info (may be

null

if not specified)

- getSignedInfo

```java
SignedInfo
getSignedInfo()
```

Returns the signed info of this

XMLSignature

.

**Returns:** the signed info (never

null

)

- getObjects

```java
List
<
XMLObject
> getObjects()
```

Returns an

unmodifiable
list

of

XMLObject

s contained in this

XMLSignature

.

**Returns:** an unmodifiable list of

XMLObject

s (may be empty
but never

null

)

- getId

```java
String
getId()
```

Returns the optional Id of this

XMLSignature

.

**Returns:** the Id (may be

null

if not specified)

- getSignatureValue

```java
XMLSignature.SignatureValue
getSignatureValue()
```

Returns the signature value of this

XMLSignature

.

**Returns:** the signature value

- sign

```java
void sign​(
XMLSignContext
signContext)
throws
MarshalException
,

XMLSignatureException
```

Signs this

XMLSignature

.

If this method throws an exception, this

XMLSignature

and
the

signContext

parameter will be left in the state that
it was in prior to the invocation.

**Parameters:** signContext

- the signing context
**Throws:** ClassCastException

- if the type of

signContext

is
not compatible with this

XMLSignature
**Throws:** NullPointerException

- if

signContext

is

null
**Throws:** MarshalException

- if an exception occurs while marshalling
**Throws:** XMLSignatureException

- if an unexpected exception occurs while
generating the signature

- getKeySelectorResult

```java
KeySelectorResult
getKeySelectorResult()
```

Returns the result of the

KeySelector

, if specified, after
this

XMLSignature

has been signed or validated.

**Returns:** the key selector result, or

null

if a key
selector has not been specified or this

XMLSignature

has not been signed or validated

---

#### Method Detail

validate

```java
boolean validate​(
XMLValidateContext
validateContext)
throws
XMLSignatureException
```

Validates the signature according to the

core validation processing rules

. This method validates the
signature using the existing state, it does not unmarshal and
reinitialize the contents of the

XMLSignature

using the
location information specified in the context.

This method only validates the signature the first time it is
invoked. On subsequent invocations, it returns a cached result.

**Parameters:** validateContext

- the validating context
**Returns:** true

if the signature passed core validation,
otherwise

false
**Throws:** ClassCastException

- if the type of

validateContext

is not compatible with this

XMLSignature
**Throws:** NullPointerException

- if

validateContext

is

null
**Throws:** XMLSignatureException

- if an unexpected error occurs during
validation that prevented the validation operation from completing

---

#### validate

boolean validate​(

XMLValidateContext

validateContext)
throws

XMLSignatureException

Validates the signature according to the

core validation processing rules

. This method validates the
signature using the existing state, it does not unmarshal and
reinitialize the contents of the

XMLSignature

using the
location information specified in the context.

This method only validates the signature the first time it is
invoked. On subsequent invocations, it returns a cached result.

This method only validates the signature the first time it is
invoked. On subsequent invocations, it returns a cached result.

getKeyInfo

```java
KeyInfo
getKeyInfo()
```

Returns the key info of this

XMLSignature

.

**Returns:** the key info (may be

null

if not specified)

---

#### getKeyInfo

KeyInfo

getKeyInfo()

Returns the key info of this

XMLSignature

.

getSignedInfo

```java
SignedInfo
getSignedInfo()
```

Returns the signed info of this

XMLSignature

.

**Returns:** the signed info (never

null

)

---

#### getSignedInfo

SignedInfo

getSignedInfo()

Returns the signed info of this

XMLSignature

.

getObjects

```java
List
<
XMLObject
> getObjects()
```

Returns an

unmodifiable
list

of

XMLObject

s contained in this

XMLSignature

.

**Returns:** an unmodifiable list of

XMLObject

s (may be empty
but never

null

)

---

#### getObjects

List

<

XMLObject

> getObjects()

Returns an

unmodifiable
list

of

XMLObject

s contained in this

XMLSignature

.

getId

```java
String
getId()
```

Returns the optional Id of this

XMLSignature

.

**Returns:** the Id (may be

null

if not specified)

---

#### getId

String

getId()

Returns the optional Id of this

XMLSignature

.

getSignatureValue

```java
XMLSignature.SignatureValue
getSignatureValue()
```

Returns the signature value of this

XMLSignature

.

**Returns:** the signature value

---

#### getSignatureValue

XMLSignature.SignatureValue

getSignatureValue()

Returns the signature value of this

XMLSignature

.

sign

```java
void sign​(
XMLSignContext
signContext)
throws
MarshalException
,

XMLSignatureException
```

Signs this

XMLSignature

.

If this method throws an exception, this

XMLSignature

and
the

signContext

parameter will be left in the state that
it was in prior to the invocation.

**Parameters:** signContext

- the signing context
**Throws:** ClassCastException

- if the type of

signContext

is
not compatible with this

XMLSignature
**Throws:** NullPointerException

- if

signContext

is

null
**Throws:** MarshalException

- if an exception occurs while marshalling
**Throws:** XMLSignatureException

- if an unexpected exception occurs while
generating the signature

---

#### sign

void sign​(

XMLSignContext

signContext)
throws

MarshalException

,

XMLSignatureException

Signs this

XMLSignature

.

If this method throws an exception, this

XMLSignature

and
the

signContext

parameter will be left in the state that
it was in prior to the invocation.

If this method throws an exception, this

XMLSignature

and
the

signContext

parameter will be left in the state that
it was in prior to the invocation.

getKeySelectorResult

```java
KeySelectorResult
getKeySelectorResult()
```

Returns the result of the

KeySelector

, if specified, after
this

XMLSignature

has been signed or validated.

**Returns:** the key selector result, or

null

if a key
selector has not been specified or this

XMLSignature

has not been signed or validated

---

#### getKeySelectorResult

KeySelectorResult

getKeySelectorResult()

Returns the result of the

KeySelector

, if specified, after
this

XMLSignature

has been signed or validated.

---

