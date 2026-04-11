# Interface XMLObject

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\XMLObject.html`

### Class Description

```java
public interface
XMLObject

extends
XMLStructure
```

A representation of the XML

Object

element as defined in
the

W3C Recommendation for XML-Signature Syntax and Processing

.
An

XMLObject

may contain any data and may include optional
MIME type, ID, and encoding attributes. The XML Schema Definition is
defined as:

```java
<element name="Object" type="ds:ObjectType"/>
<complexType name="ObjectType" mixed="true">
<sequence minOccurs="0" maxOccurs="unbounded">
<any namespace="##any" processContents="lax"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
<attribute name="MimeType" type="string" use="optional"/>
<attribute name="Encoding" type="anyURI" use="optional"/>
</complexType>
```

A

XMLObject

instance may be created by invoking the

newXMLObject

method of the

XMLSignatureFactory

class; for example:

```java
XMLSignatureFactory fac = XMLSignatureFactory.getInstance("DOM");
Manifest manifest = fac.newManifest(references);
List<XMLStructure> content = Collections.singletonList(manifest);
XMLObject object = factory.newXMLObject(content, "object-1", null, null);
```

Note that this class is named

XMLObject

rather than

Object

to avoid naming clashes with the existing

java.lang.Object

class.

**All Superinterfaces:** XMLStructure

---

### Field Details

#### static final
String
TYPE

URI that identifies the

Object

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

#### List
<
XMLStructure
> getContent()

Returns an

unmodifiable
list

of

XMLStructure

s contained in this

XMLObject

,
which represent elements from any namespace.

If there is a public subclass representing the type of

XMLStructure

, it is returned as an instance of that class
(ex: a

SignatureProperties

element would be returned
as an instance of

SignatureProperties

).

**Returns:**
- an unmodifiable list of

XMLStructure

s (may be empty
but never

null

)

---

#### String
getId()

Returns the Id of this

XMLObject

.

**Returns:**
- the Id (or

null

if not specified)

---

#### String
getMimeType()

Returns the mime type of this

XMLObject

. The
mime type is an optional attribute which describes the data within this

XMLObject

(independent of its encoding).

**Returns:**
- the mime type (or

null

if not specified)

---

#### String
getEncoding()

Returns the encoding URI of this

XMLObject

. The encoding
URI identifies the method by which the object is encoded.

**Returns:**
- the encoding URI (or

null

if not specified)

---

### Additional Sections

#### Interface XMLObject

**All Superinterfaces:** XMLStructure

```java
public interface
XMLObject

extends
XMLStructure
```

A representation of the XML

Object

element as defined in
the

W3C Recommendation for XML-Signature Syntax and Processing

.
An

XMLObject

may contain any data and may include optional
MIME type, ID, and encoding attributes. The XML Schema Definition is
defined as:

```java
<element name="Object" type="ds:ObjectType"/>
<complexType name="ObjectType" mixed="true">
<sequence minOccurs="0" maxOccurs="unbounded">
<any namespace="##any" processContents="lax"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
<attribute name="MimeType" type="string" use="optional"/>
<attribute name="Encoding" type="anyURI" use="optional"/>
</complexType>
```

A

XMLObject

instance may be created by invoking the

newXMLObject

method of the

XMLSignatureFactory

class; for example:

```java
XMLSignatureFactory fac = XMLSignatureFactory.getInstance("DOM");
Manifest manifest = fac.newManifest(references);
List<XMLStructure> content = Collections.singletonList(manifest);
XMLObject object = factory.newXMLObject(content, "object-1", null, null);
```

Note that this class is named

XMLObject

rather than

Object

to avoid naming clashes with the existing

java.lang.Object

class.

**Since:** 1.6
**See Also:** XMLSignatureFactory.newXMLObject(List, String, String, String)

public interface

XMLObject

extends

XMLStructure

A representation of the XML

Object

element as defined in
the

W3C Recommendation for XML-Signature Syntax and Processing

.
An

XMLObject

may contain any data and may include optional
MIME type, ID, and encoding attributes. The XML Schema Definition is
defined as:

```java
<element name="Object" type="ds:ObjectType"/>
<complexType name="ObjectType" mixed="true">
<sequence minOccurs="0" maxOccurs="unbounded">
<any namespace="##any" processContents="lax"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
<attribute name="MimeType" type="string" use="optional"/>
<attribute name="Encoding" type="anyURI" use="optional"/>
</complexType>
```

A

XMLObject

instance may be created by invoking the

newXMLObject

method of the

XMLSignatureFactory

class; for example:

```java
XMLSignatureFactory fac = XMLSignatureFactory.getInstance("DOM");
Manifest manifest = fac.newManifest(references);
List<XMLStructure> content = Collections.singletonList(manifest);
XMLObject object = factory.newXMLObject(content, "object-1", null, null);
```

Note that this class is named

XMLObject

rather than

Object

to avoid naming clashes with the existing

java.lang.Object

class.

<element name="Object" type="ds:ObjectType"/>
<complexType name="ObjectType" mixed="true">
<sequence minOccurs="0" maxOccurs="unbounded">
<any namespace="##any" processContents="lax"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
<attribute name="MimeType" type="string" use="optional"/>
<attribute name="Encoding" type="anyURI" use="optional"/>
</complexType>

XMLSignatureFactory fac = XMLSignatureFactory.getInstance("DOM");
Manifest manifest = fac.newManifest(references);
List<XMLStructure> content = Collections.singletonList(manifest);
XMLObject object = factory.newXMLObject(content, "object-1", null, null);

Note that this class is named

XMLObject

rather than

Object

to avoid naming clashes with the existing

java.lang.Object

class.

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

Object

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

List

<

XMLStructure

>

getContent

()

Returns an

unmodifiable
list

of

XMLStructure

s contained in this

XMLObject

,
which represent elements from any namespace.

String

getEncoding

()

Returns the encoding URI of this

XMLObject

.

String

getId

()

Returns the Id of this

XMLObject

.

String

getMimeType

()

Returns the mime type of this

XMLObject

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

Object

element (this can be
specified as the value of the

type

parameter of the

Reference

class to identify the referent's type).

---

#### Field Summary

URI that identifies the

Object

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

List

<

XMLStructure

>

getContent

()

Returns an

unmodifiable
list

of

XMLStructure

s contained in this

XMLObject

,
which represent elements from any namespace.

String

getEncoding

()

Returns the encoding URI of this

XMLObject

.

String

getId

()

Returns the Id of this

XMLObject

.

String

getMimeType

()

Returns the mime type of this

XMLObject

.

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Method Summary

Returns an

unmodifiable
list

of

XMLStructure

s contained in this

XMLObject

,
which represent elements from any namespace.

Returns the encoding URI of this

XMLObject

.

Returns the Id of this

XMLObject

.

Returns the mime type of this

XMLObject

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

Object

element (this can be
specified as the value of the

type

parameter of the

Reference

class to identify the referent's type).

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getContent

```java
List
<
XMLStructure
> getContent()
```

Returns an

unmodifiable
list

of

XMLStructure

s contained in this

XMLObject

,
which represent elements from any namespace.

If there is a public subclass representing the type of

XMLStructure

, it is returned as an instance of that class
(ex: a

SignatureProperties

element would be returned
as an instance of

SignatureProperties

).

**Returns:** an unmodifiable list of

XMLStructure

s (may be empty
but never

null

)

- getId

```java
String
getId()
```

Returns the Id of this

XMLObject

.

**Returns:** the Id (or

null

if not specified)

- getMimeType

```java
String
getMimeType()
```

Returns the mime type of this

XMLObject

. The
mime type is an optional attribute which describes the data within this

XMLObject

(independent of its encoding).

**Returns:** the mime type (or

null

if not specified)

- getEncoding

```java
String
getEncoding()
```

Returns the encoding URI of this

XMLObject

. The encoding
URI identifies the method by which the object is encoded.

**Returns:** the encoding URI (or

null

if not specified)

Field Detail

- TYPE

```java
static final
String
TYPE
```

URI that identifies the

Object

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

Object

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

Object

element (this can be
specified as the value of the

type

parameter of the

Reference

class to identify the referent's type).

Method Detail

- getContent

```java
List
<
XMLStructure
> getContent()
```

Returns an

unmodifiable
list

of

XMLStructure

s contained in this

XMLObject

,
which represent elements from any namespace.

If there is a public subclass representing the type of

XMLStructure

, it is returned as an instance of that class
(ex: a

SignatureProperties

element would be returned
as an instance of

SignatureProperties

).

**Returns:** an unmodifiable list of

XMLStructure

s (may be empty
but never

null

)

- getId

```java
String
getId()
```

Returns the Id of this

XMLObject

.

**Returns:** the Id (or

null

if not specified)

- getMimeType

```java
String
getMimeType()
```

Returns the mime type of this

XMLObject

. The
mime type is an optional attribute which describes the data within this

XMLObject

(independent of its encoding).

**Returns:** the mime type (or

null

if not specified)

- getEncoding

```java
String
getEncoding()
```

Returns the encoding URI of this

XMLObject

. The encoding
URI identifies the method by which the object is encoded.

**Returns:** the encoding URI (or

null

if not specified)

---

#### Method Detail

getContent

```java
List
<
XMLStructure
> getContent()
```

Returns an

unmodifiable
list

of

XMLStructure

s contained in this

XMLObject

,
which represent elements from any namespace.

If there is a public subclass representing the type of

XMLStructure

, it is returned as an instance of that class
(ex: a

SignatureProperties

element would be returned
as an instance of

SignatureProperties

).

**Returns:** an unmodifiable list of

XMLStructure

s (may be empty
but never

null

)

---

#### getContent

List

<

XMLStructure

> getContent()

Returns an

unmodifiable
list

of

XMLStructure

s contained in this

XMLObject

,
which represent elements from any namespace.

If there is a public subclass representing the type of

XMLStructure

, it is returned as an instance of that class
(ex: a

SignatureProperties

element would be returned
as an instance of

SignatureProperties

).

If there is a public subclass representing the type of

XMLStructure

, it is returned as an instance of that class
(ex: a

SignatureProperties

element would be returned
as an instance of

SignatureProperties

).

getId

```java
String
getId()
```

Returns the Id of this

XMLObject

.

**Returns:** the Id (or

null

if not specified)

---

#### getId

String

getId()

Returns the Id of this

XMLObject

.

getMimeType

```java
String
getMimeType()
```

Returns the mime type of this

XMLObject

. The
mime type is an optional attribute which describes the data within this

XMLObject

(independent of its encoding).

**Returns:** the mime type (or

null

if not specified)

---

#### getMimeType

String

getMimeType()

Returns the mime type of this

XMLObject

. The
mime type is an optional attribute which describes the data within this

XMLObject

(independent of its encoding).

getEncoding

```java
String
getEncoding()
```

Returns the encoding URI of this

XMLObject

. The encoding
URI identifies the method by which the object is encoded.

**Returns:** the encoding URI (or

null

if not specified)

---

#### getEncoding

String

getEncoding()

Returns the encoding URI of this

XMLObject

. The encoding
URI identifies the method by which the object is encoded.

---

