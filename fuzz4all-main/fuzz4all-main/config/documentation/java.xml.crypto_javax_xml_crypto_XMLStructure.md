# Interface XMLStructure

**Source:** `java.xml.crypto\javax\xml\crypto\XMLStructure.html`

### Class Description

```java
public interface
XMLStructure
```

A representation of an XML structure from any namespace. The purpose of
this interface is to group (and provide type safety for) all
representations of XML structures.

**All Known Subinterfaces:** CanonicalizationMethod

,

DigestMethod

,

KeyInfo

,

KeyName

,

KeyValue

,

Manifest

,

PGPData

,

Reference

,

RetrievalMethod

,

SignatureMethod

,

SignatureProperties

,

SignatureProperty

,

SignedInfo

,

Transform

,

X509Data

,

X509IssuerSerial

,

XMLObject

,

XMLSignature

,

XMLSignature.SignatureValue

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean isFeatureSupported​(
String
feature)

Indicates whether a specified feature is supported.

**Parameters:**
- feature

- the feature name (as an absolute URI)

**Returns:**
- true

if the specified feature is supported,

false

otherwise

**Throws:**
- NullPointerException

- if

feature

is

null

---

### Additional Sections

#### Interface XMLStructure

**All Known Subinterfaces:** CanonicalizationMethod

,

DigestMethod

,

KeyInfo

,

KeyName

,

KeyValue

,

Manifest

,

PGPData

,

Reference

,

RetrievalMethod

,

SignatureMethod

,

SignatureProperties

,

SignatureProperty

,

SignedInfo

,

Transform

,

X509Data

,

X509IssuerSerial

,

XMLObject

,

XMLSignature

,

XMLSignature.SignatureValue

**All Known Implementing Classes:** DOMStructure

,

TransformService

```java
public interface
XMLStructure
```

A representation of an XML structure from any namespace. The purpose of
this interface is to group (and provide type safety for) all
representations of XML structures.

**Since:** 1.6

public interface

XMLStructure

A representation of an XML structure from any namespace. The purpose of
this interface is to group (and provide type safety for) all
representations of XML structures.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

isFeatureSupported

​(

String

feature)

Indicates whether a specified feature is supported.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

isFeatureSupported

​(

String

feature)

Indicates whether a specified feature is supported.

---

#### Method Summary

Indicates whether a specified feature is supported.

============ METHOD DETAIL ==========

- Method Detail

- isFeatureSupported

```java
boolean isFeatureSupported​(
String
feature)
```

Indicates whether a specified feature is supported.

**Parameters:** feature

- the feature name (as an absolute URI)
**Returns:** true

if the specified feature is supported,

false

otherwise
**Throws:** NullPointerException

- if

feature

is

null

Method Detail

- isFeatureSupported

```java
boolean isFeatureSupported​(
String
feature)
```

Indicates whether a specified feature is supported.

**Parameters:** feature

- the feature name (as an absolute URI)
**Returns:** true

if the specified feature is supported,

false

otherwise
**Throws:** NullPointerException

- if

feature

is

null

---

#### Method Detail

isFeatureSupported

```java
boolean isFeatureSupported​(
String
feature)
```

Indicates whether a specified feature is supported.

**Parameters:** feature

- the feature name (as an absolute URI)
**Returns:** true

if the specified feature is supported,

false

otherwise
**Throws:** NullPointerException

- if

feature

is

null

---

#### isFeatureSupported

boolean isFeatureSupported​(

String

feature)

Indicates whether a specified feature is supported.

---

