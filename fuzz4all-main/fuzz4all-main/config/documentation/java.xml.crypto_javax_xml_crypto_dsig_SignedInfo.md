# Interface SignedInfo

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\SignedInfo.html`

### Class Description

```java
public interface
SignedInfo

extends
XMLStructure
```

An representation of the XML

SignedInfo

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="SignedInfo" type="ds:SignedInfoType"/>
<complexType name="SignedInfoType">
<sequence>
<element ref="ds:CanonicalizationMethod"/>
<element ref="ds:SignatureMethod"/>
<element ref="ds:Reference" maxOccurs="unbounded"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
</complexType>
```

A

SignedInfo

instance may be created by invoking one of the

newSignedInfo

methods of the

XMLSignatureFactory

class.

**All Superinterfaces:** XMLStructure

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### CanonicalizationMethod
getCanonicalizationMethod()

Returns the canonicalization method of this

SignedInfo

.

**Returns:**
- the canonicalization method

---

#### SignatureMethod
getSignatureMethod()

Returns the signature method of this

SignedInfo

.

**Returns:**
- the signature method

---

#### List
<
Reference
> getReferences()

Returns an

unmodifiable list

of one or more

Reference

s.

**Returns:**
- an unmodifiable list of one or more

Reference

s

---

#### String
getId()

Returns the optional

Id

attribute of this

SignedInfo

.

**Returns:**
- the id (may be

null

if not specified)

---

#### InputStream
getCanonicalizedData()

Returns the canonicalized signed info bytes after a signing or
validation operation. This method is useful for debugging.

**Returns:**
- an

InputStream

containing the canonicalized bytes,
or

null

if this

SignedInfo

has not been
signed or validated yet

---

### Additional Sections

#### Interface SignedInfo

**All Superinterfaces:** XMLStructure

```java
public interface
SignedInfo

extends
XMLStructure
```

An representation of the XML

SignedInfo

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="SignedInfo" type="ds:SignedInfoType"/>
<complexType name="SignedInfoType">
<sequence>
<element ref="ds:CanonicalizationMethod"/>
<element ref="ds:SignatureMethod"/>
<element ref="ds:Reference" maxOccurs="unbounded"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
</complexType>
```

A

SignedInfo

instance may be created by invoking one of the

newSignedInfo

methods of the

XMLSignatureFactory

class.

**Since:** 1.6
**See Also:** XMLSignatureFactory.newSignedInfo(CanonicalizationMethod, SignatureMethod, List)

,

XMLSignatureFactory.newSignedInfo(CanonicalizationMethod, SignatureMethod, List, String)

public interface

SignedInfo

extends

XMLStructure

An representation of the XML

SignedInfo

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="SignedInfo" type="ds:SignedInfoType"/>
<complexType name="SignedInfoType">
<sequence>
<element ref="ds:CanonicalizationMethod"/>
<element ref="ds:SignatureMethod"/>
<element ref="ds:Reference" maxOccurs="unbounded"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
</complexType>
```

A

SignedInfo

instance may be created by invoking one of the

newSignedInfo

methods of the

XMLSignatureFactory

class.

<element name="SignedInfo" type="ds:SignedInfoType"/>
<complexType name="SignedInfoType">
<sequence>
<element ref="ds:CanonicalizationMethod"/>
<element ref="ds:SignatureMethod"/>
<element ref="ds:Reference" maxOccurs="unbounded"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
</complexType>

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

CanonicalizationMethod

getCanonicalizationMethod

()

Returns the canonicalization method of this

SignedInfo

.

InputStream

getCanonicalizedData

()

Returns the canonicalized signed info bytes after a signing or
validation operation.

String

getId

()

Returns the optional

Id

attribute of this

SignedInfo

.

List

<

Reference

>

getReferences

()

Returns an

unmodifiable list

of one or more

Reference

s.

SignatureMethod

getSignatureMethod

()

Returns the signature method of this

SignedInfo

.

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

CanonicalizationMethod

getCanonicalizationMethod

()

Returns the canonicalization method of this

SignedInfo

.

InputStream

getCanonicalizedData

()

Returns the canonicalized signed info bytes after a signing or
validation operation.

String

getId

()

Returns the optional

Id

attribute of this

SignedInfo

.

List

<

Reference

>

getReferences

()

Returns an

unmodifiable list

of one or more

Reference

s.

SignatureMethod

getSignatureMethod

()

Returns the signature method of this

SignedInfo

.

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Method Summary

Returns the canonicalization method of this

SignedInfo

.

Returns the canonicalized signed info bytes after a signing or
validation operation.

Returns the optional

Id

attribute of this

SignedInfo

.

Returns an

unmodifiable list

of one or more

Reference

s.

Returns the signature method of this

SignedInfo

.

Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Methods declared in interface javax.xml.crypto. XMLStructure

============ METHOD DETAIL ==========

- Method Detail

- getCanonicalizationMethod

```java
CanonicalizationMethod
getCanonicalizationMethod()
```

Returns the canonicalization method of this

SignedInfo

.

**Returns:** the canonicalization method

- getSignatureMethod

```java
SignatureMethod
getSignatureMethod()
```

Returns the signature method of this

SignedInfo

.

**Returns:** the signature method

- getReferences

```java
List
<
Reference
> getReferences()
```

Returns an

unmodifiable list

of one or more

Reference

s.

**Returns:** an unmodifiable list of one or more

Reference

s

- getId

```java
String
getId()
```

Returns the optional

Id

attribute of this

SignedInfo

.

**Returns:** the id (may be

null

if not specified)

- getCanonicalizedData

```java
InputStream
getCanonicalizedData()
```

Returns the canonicalized signed info bytes after a signing or
validation operation. This method is useful for debugging.

**Returns:** an

InputStream

containing the canonicalized bytes,
or

null

if this

SignedInfo

has not been
signed or validated yet

Method Detail

- getCanonicalizationMethod

```java
CanonicalizationMethod
getCanonicalizationMethod()
```

Returns the canonicalization method of this

SignedInfo

.

**Returns:** the canonicalization method

- getSignatureMethod

```java
SignatureMethod
getSignatureMethod()
```

Returns the signature method of this

SignedInfo

.

**Returns:** the signature method

- getReferences

```java
List
<
Reference
> getReferences()
```

Returns an

unmodifiable list

of one or more

Reference

s.

**Returns:** an unmodifiable list of one or more

Reference

s

- getId

```java
String
getId()
```

Returns the optional

Id

attribute of this

SignedInfo

.

**Returns:** the id (may be

null

if not specified)

- getCanonicalizedData

```java
InputStream
getCanonicalizedData()
```

Returns the canonicalized signed info bytes after a signing or
validation operation. This method is useful for debugging.

**Returns:** an

InputStream

containing the canonicalized bytes,
or

null

if this

SignedInfo

has not been
signed or validated yet

---

#### Method Detail

getCanonicalizationMethod

```java
CanonicalizationMethod
getCanonicalizationMethod()
```

Returns the canonicalization method of this

SignedInfo

.

**Returns:** the canonicalization method

---

#### getCanonicalizationMethod

CanonicalizationMethod

getCanonicalizationMethod()

Returns the canonicalization method of this

SignedInfo

.

getSignatureMethod

```java
SignatureMethod
getSignatureMethod()
```

Returns the signature method of this

SignedInfo

.

**Returns:** the signature method

---

#### getSignatureMethod

SignatureMethod

getSignatureMethod()

Returns the signature method of this

SignedInfo

.

getReferences

```java
List
<
Reference
> getReferences()
```

Returns an

unmodifiable list

of one or more

Reference

s.

**Returns:** an unmodifiable list of one or more

Reference

s

---

#### getReferences

List

<

Reference

> getReferences()

Returns an

unmodifiable list

of one or more

Reference

s.

getId

```java
String
getId()
```

Returns the optional

Id

attribute of this

SignedInfo

.

**Returns:** the id (may be

null

if not specified)

---

#### getId

String

getId()

Returns the optional

Id

attribute of this

SignedInfo

.

getCanonicalizedData

```java
InputStream
getCanonicalizedData()
```

Returns the canonicalized signed info bytes after a signing or
validation operation. This method is useful for debugging.

**Returns:** an

InputStream

containing the canonicalized bytes,
or

null

if this

SignedInfo

has not been
signed or validated yet

---

#### getCanonicalizedData

InputStream

getCanonicalizedData()

Returns the canonicalized signed info bytes after a signing or
validation operation. This method is useful for debugging.

---

