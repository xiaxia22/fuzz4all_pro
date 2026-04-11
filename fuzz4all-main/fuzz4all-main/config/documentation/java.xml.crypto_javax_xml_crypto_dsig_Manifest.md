# Interface Manifest

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\Manifest.html`

### Class Description

```java
public interface
Manifest

extends
XMLStructure
```

A representation of the XML

Manifest

element as defined in
the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="Manifest" type="ds:ManifestType"/>
<complexType name="ManifestType">
<sequence>
<element ref="ds:Reference" maxOccurs="unbounded"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
</complexType>
```

A

Manifest

instance may be created by invoking
one of the

newManifest

methods of the

XMLSignatureFactory

class; for example:

```java
XMLSignatureFactory factory = XMLSignatureFactory.getInstance("DOM");
Reference ref = factory.newReference("#reference-1", DigestMethod.SHA1);
List<Reference> references = Collections.singletonList(ref);
Manifest manifest = factory.newManifest(references, "manifest-1");
```

**All Superinterfaces:** XMLStructure

---

### Field Details

#### static final
String
TYPE

URI that identifies the

Manifest

element (this can be
specified as the value of the

type

parameter of the

Reference

class to identify the referent's type).

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### String
getId()

Returns the Id of this

Manifest

.

**Returns:**
- the Id of this

Manifest

(or

null

if not specified)

---

#### List
<
Reference
> getReferences()

Returns an

unmodifiable
list

of one or more

Reference

s that are contained in this

Manifest

.

**Returns:**
- an unmodifiable list of one or more

Reference

s

---

### Additional Sections

#### Interface Manifest

**All Superinterfaces:** XMLStructure

```java
public interface
Manifest

extends
XMLStructure
```

A representation of the XML

Manifest

element as defined in
the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="Manifest" type="ds:ManifestType"/>
<complexType name="ManifestType">
<sequence>
<element ref="ds:Reference" maxOccurs="unbounded"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
</complexType>
```

A

Manifest

instance may be created by invoking
one of the

newManifest

methods of the

XMLSignatureFactory

class; for example:

```java
XMLSignatureFactory factory = XMLSignatureFactory.getInstance("DOM");
Reference ref = factory.newReference("#reference-1", DigestMethod.SHA1);
List<Reference> references = Collections.singletonList(ref);
Manifest manifest = factory.newManifest(references, "manifest-1");
```

**Since:** 1.6
**See Also:** XMLSignatureFactory.newManifest(List)

,

XMLSignatureFactory.newManifest(List, String)

public interface

Manifest

extends

XMLStructure

A representation of the XML

Manifest

element as defined in
the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="Manifest" type="ds:ManifestType"/>
<complexType name="ManifestType">
<sequence>
<element ref="ds:Reference" maxOccurs="unbounded"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
</complexType>
```

A

Manifest

instance may be created by invoking
one of the

newManifest

methods of the

XMLSignatureFactory

class; for example:

```java
XMLSignatureFactory factory = XMLSignatureFactory.getInstance("DOM");
Reference ref = factory.newReference("#reference-1", DigestMethod.SHA1);
List<Reference> references = Collections.singletonList(ref);
Manifest manifest = factory.newManifest(references, "manifest-1");
```

<element name="Manifest" type="ds:ManifestType"/>
<complexType name="ManifestType">
<sequence>
<element ref="ds:Reference" maxOccurs="unbounded"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
</complexType>

XMLSignatureFactory factory = XMLSignatureFactory.getInstance("DOM");
Reference ref = factory.newReference("#reference-1", DigestMethod.SHA1);
List<Reference> references = Collections.singletonList(ref);
Manifest manifest = factory.newManifest(references, "manifest-1");

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

TYPE

URI that identifies the

Manifest

element (this can be
specified as the value of the

type

parameter of the

Reference

class to identify the referent's type).

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

Returns the Id of this

Manifest

.

List

<

Reference

>

getReferences

()

Returns an

unmodifiable
list

of one or more

Reference

s that are contained in this

Manifest

.

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

TYPE

URI that identifies the

Manifest

element (this can be
specified as the value of the

type

parameter of the

Reference

class to identify the referent's type).

---

#### Field Summary

URI that identifies the

Manifest

element (this can be
specified as the value of the

type

parameter of the

Reference

class to identify the referent's type).

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

Returns the Id of this

Manifest

.

List

<

Reference

>

getReferences

()

Returns an

unmodifiable
list

of one or more

Reference

s that are contained in this

Manifest

.

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Method Summary

Returns the Id of this

Manifest

.

Returns an

unmodifiable
list

of one or more

Reference

s that are contained in this

Manifest

.

Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Methods declared in interface javax.xml.crypto. XMLStructure

============ FIELD DETAIL ===========

- Field Detail

- TYPE

```java
static final
String
TYPE
```

URI that identifies the

Manifest

element (this can be
specified as the value of the

type

parameter of the

Reference

class to identify the referent's type).

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getId

```java
String
getId()
```

Returns the Id of this

Manifest

.

**Returns:** the Id of this

Manifest

(or

null

if not specified)

- getReferences

```java
List
<
Reference
> getReferences()
```

Returns an

unmodifiable
list

of one or more

Reference

s that are contained in this

Manifest

.

**Returns:** an unmodifiable list of one or more

Reference

s

Field Detail

- TYPE

```java
static final
String
TYPE
```

URI that identifies the

Manifest

element (this can be
specified as the value of the

type

parameter of the

Reference

class to identify the referent's type).

**See Also:** Constant Field Values

---

#### Field Detail

TYPE

```java
static final
String
TYPE
```

URI that identifies the

Manifest

element (this can be
specified as the value of the

type

parameter of the

Reference

class to identify the referent's type).

**See Also:** Constant Field Values

---

#### TYPE

static final

String

TYPE

URI that identifies the

Manifest

element (this can be
specified as the value of the

type

parameter of the

Reference

class to identify the referent's type).

Method Detail

- getId

```java
String
getId()
```

Returns the Id of this

Manifest

.

**Returns:** the Id of this

Manifest

(or

null

if not specified)

- getReferences

```java
List
<
Reference
> getReferences()
```

Returns an

unmodifiable
list

of one or more

Reference

s that are contained in this

Manifest

.

**Returns:** an unmodifiable list of one or more

Reference

s

---

#### Method Detail

getId

```java
String
getId()
```

Returns the Id of this

Manifest

.

**Returns:** the Id of this

Manifest

(or

null

if not specified)

---

#### getId

String

getId()

Returns the Id of this

Manifest

.

getReferences

```java
List
<
Reference
> getReferences()
```

Returns an

unmodifiable
list

of one or more

Reference

s that are contained in this

Manifest

.

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

unmodifiable
list

of one or more

Reference

s that are contained in this

Manifest

.

---

