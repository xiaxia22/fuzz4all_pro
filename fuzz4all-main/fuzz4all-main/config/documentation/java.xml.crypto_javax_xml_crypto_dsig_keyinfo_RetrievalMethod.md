# Interface RetrievalMethod

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\keyinfo\RetrievalMethod.html`

### Class Description

```java
public interface
RetrievalMethod

extends
URIReference
,
XMLStructure
```

A representation of the XML

RetrievalMethod

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
A

RetrievalMethod

object is used to convey a reference to

KeyInfo

information that is stored at another location.
The XML schema definition is defined as:

```java
<element name="RetrievalMethod" type="ds:RetrievalMethodType"/>
<complexType name="RetrievalMethodType">
<sequence>
<element name="Transforms" type="ds:TransformsType" minOccurs="0"/>
</sequence>
<attribute name="URI" type="anyURI"/>
<attribute name="Type" type="anyURI" use="optional"/>
</complexType>
```

A

RetrievalMethod

instance may be created by invoking one of the

newRetrievalMethod

methods
of the

KeyInfoFactory

class, and passing it the URI
identifying the location of the KeyInfo, an optional type URI identifying
the type of KeyInfo, and an optional list of

Transform

s; for example:

```java
KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
RetrievalMethod rm = factory.newRetrievalMethod
("#KeyValue-1", KeyValue.DSA_TYPE, Collections.singletonList(Transform.BASE64));
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

s of this

RetrievalMethod

.

**Returns:**
- an unmodifiable list of

Transform

objects (may be
empty but never

null

).

---

#### String
getURI()

Returns the URI of the referenced

KeyInfo

information.

**Specified by:**
- getURI

in interface

URIReference

**Returns:**
- the URI of the referenced

KeyInfo

information in
RFC 2396 format (never

null

)

---

#### Data
dereference​(
XMLCryptoContext
context)
throws
URIReferenceException

Dereferences the

KeyInfo

information referenced by this

RetrievalMethod

and applies the specified

Transform

s.

**Parameters:**
- context

- an

XMLCryptoContext

that may contain
additional useful information for dereferencing the URI. The
context's

baseURI

and

dereferencer

parameters (if specified) are used to resolve and dereference this

RetrievalMethod

**Returns:**
- a

Data

object representing the raw contents of the

KeyInfo

information referenced by this

RetrievalMethod

. It is the caller's responsibility to
convert the returned data to an appropriate

KeyInfo

object.

**Throws:**
- NullPointerException

- if

context

is

null
- URIReferenceException

- if there is an error while dereferencing

---

### Additional Sections

#### Interface RetrievalMethod

**All Superinterfaces:** URIReference

,

XMLStructure

```java
public interface
RetrievalMethod

extends
URIReference
,
XMLStructure
```

A representation of the XML

RetrievalMethod

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
A

RetrievalMethod

object is used to convey a reference to

KeyInfo

information that is stored at another location.
The XML schema definition is defined as:

```java
<element name="RetrievalMethod" type="ds:RetrievalMethodType"/>
<complexType name="RetrievalMethodType">
<sequence>
<element name="Transforms" type="ds:TransformsType" minOccurs="0"/>
</sequence>
<attribute name="URI" type="anyURI"/>
<attribute name="Type" type="anyURI" use="optional"/>
</complexType>
```

A

RetrievalMethod

instance may be created by invoking one of the

newRetrievalMethod

methods
of the

KeyInfoFactory

class, and passing it the URI
identifying the location of the KeyInfo, an optional type URI identifying
the type of KeyInfo, and an optional list of

Transform

s; for example:

```java
KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
RetrievalMethod rm = factory.newRetrievalMethod
("#KeyValue-1", KeyValue.DSA_TYPE, Collections.singletonList(Transform.BASE64));
```

**Since:** 1.6
**See Also:** KeyInfoFactory.newRetrievalMethod(String)

,

KeyInfoFactory.newRetrievalMethod(String, String, List)

public interface

RetrievalMethod

extends

URIReference

,

XMLStructure

A representation of the XML

RetrievalMethod

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
A

RetrievalMethod

object is used to convey a reference to

KeyInfo

information that is stored at another location.
The XML schema definition is defined as:

```java
<element name="RetrievalMethod" type="ds:RetrievalMethodType"/>
<complexType name="RetrievalMethodType">
<sequence>
<element name="Transforms" type="ds:TransformsType" minOccurs="0"/>
</sequence>
<attribute name="URI" type="anyURI"/>
<attribute name="Type" type="anyURI" use="optional"/>
</complexType>
```

A

RetrievalMethod

instance may be created by invoking one of the

newRetrievalMethod

methods
of the

KeyInfoFactory

class, and passing it the URI
identifying the location of the KeyInfo, an optional type URI identifying
the type of KeyInfo, and an optional list of

Transform

s; for example:

```java
KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
RetrievalMethod rm = factory.newRetrievalMethod
("#KeyValue-1", KeyValue.DSA_TYPE, Collections.singletonList(Transform.BASE64));
```

<element name="RetrievalMethod" type="ds:RetrievalMethodType"/>
<complexType name="RetrievalMethodType">
<sequence>
<element name="Transforms" type="ds:TransformsType" minOccurs="0"/>
</sequence>
<attribute name="URI" type="anyURI"/>
<attribute name="Type" type="anyURI" use="optional"/>
</complexType>

KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
RetrievalMethod rm = factory.newRetrievalMethod
("#KeyValue-1", KeyValue.DSA_TYPE, Collections.singletonList(Transform.BASE64));

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Data

dereference

​(

XMLCryptoContext

context)

Dereferences the

KeyInfo

information referenced by this

RetrievalMethod

and applies the specified

Transform

s.

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

s of this

RetrievalMethod

.

String

getURI

()

Returns the URI of the referenced

KeyInfo

information.

- Methods declared in interface javax.xml.crypto.

URIReference

getType

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

Data

dereference

​(

XMLCryptoContext

context)

Dereferences the

KeyInfo

information referenced by this

RetrievalMethod

and applies the specified

Transform

s.

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

s of this

RetrievalMethod

.

String

getURI

()

Returns the URI of the referenced

KeyInfo

information.

- Methods declared in interface javax.xml.crypto.

URIReference

getType

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Method Summary

Dereferences the

KeyInfo

information referenced by this

RetrievalMethod

and applies the specified

Transform

s.

Returns an

unmodifiable
list

of

Transform

s of this

RetrievalMethod

.

Returns the URI of the referenced

KeyInfo

information.

Methods declared in interface javax.xml.crypto.

URIReference

getType

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

s of this

RetrievalMethod

.

**Returns:** an unmodifiable list of

Transform

objects (may be
empty but never

null

).

- getURI

```java
String
getURI()
```

Returns the URI of the referenced

KeyInfo

information.

**Specified by:** getURI

in interface

URIReference
**Returns:** the URI of the referenced

KeyInfo

information in
RFC 2396 format (never

null

)

- dereference

```java
Data
dereference​(
XMLCryptoContext
context)
throws
URIReferenceException
```

Dereferences the

KeyInfo

information referenced by this

RetrievalMethod

and applies the specified

Transform

s.

**Parameters:** context

- an

XMLCryptoContext

that may contain
additional useful information for dereferencing the URI. The
context's

baseURI

and

dereferencer

parameters (if specified) are used to resolve and dereference this

RetrievalMethod
**Returns:** a

Data

object representing the raw contents of the

KeyInfo

information referenced by this

RetrievalMethod

. It is the caller's responsibility to
convert the returned data to an appropriate

KeyInfo

object.
**Throws:** NullPointerException

- if

context

is

null
**Throws:** URIReferenceException

- if there is an error while dereferencing

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

s of this

RetrievalMethod

.

**Returns:** an unmodifiable list of

Transform

objects (may be
empty but never

null

).

- getURI

```java
String
getURI()
```

Returns the URI of the referenced

KeyInfo

information.

**Specified by:** getURI

in interface

URIReference
**Returns:** the URI of the referenced

KeyInfo

information in
RFC 2396 format (never

null

)

- dereference

```java
Data
dereference​(
XMLCryptoContext
context)
throws
URIReferenceException
```

Dereferences the

KeyInfo

information referenced by this

RetrievalMethod

and applies the specified

Transform

s.

**Parameters:** context

- an

XMLCryptoContext

that may contain
additional useful information for dereferencing the URI. The
context's

baseURI

and

dereferencer

parameters (if specified) are used to resolve and dereference this

RetrievalMethod
**Returns:** a

Data

object representing the raw contents of the

KeyInfo

information referenced by this

RetrievalMethod

. It is the caller's responsibility to
convert the returned data to an appropriate

KeyInfo

object.
**Throws:** NullPointerException

- if

context

is

null
**Throws:** URIReferenceException

- if there is an error while dereferencing

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

s of this

RetrievalMethod

.

**Returns:** an unmodifiable list of

Transform

objects (may be
empty but never

null

).

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

s of this

RetrievalMethod

.

getURI

```java
String
getURI()
```

Returns the URI of the referenced

KeyInfo

information.

**Specified by:** getURI

in interface

URIReference
**Returns:** the URI of the referenced

KeyInfo

information in
RFC 2396 format (never

null

)

---

#### getURI

String

getURI()

Returns the URI of the referenced

KeyInfo

information.

dereference

```java
Data
dereference​(
XMLCryptoContext
context)
throws
URIReferenceException
```

Dereferences the

KeyInfo

information referenced by this

RetrievalMethod

and applies the specified

Transform

s.

**Parameters:** context

- an

XMLCryptoContext

that may contain
additional useful information for dereferencing the URI. The
context's

baseURI

and

dereferencer

parameters (if specified) are used to resolve and dereference this

RetrievalMethod
**Returns:** a

Data

object representing the raw contents of the

KeyInfo

information referenced by this

RetrievalMethod

. It is the caller's responsibility to
convert the returned data to an appropriate

KeyInfo

object.
**Throws:** NullPointerException

- if

context

is

null
**Throws:** URIReferenceException

- if there is an error while dereferencing

---

#### dereference

Data

dereference​(

XMLCryptoContext

context)
throws

URIReferenceException

Dereferences the

KeyInfo

information referenced by this

RetrievalMethod

and applies the specified

Transform

s.

---

