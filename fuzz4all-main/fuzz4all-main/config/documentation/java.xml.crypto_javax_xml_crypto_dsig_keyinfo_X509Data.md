# Interface X509Data

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\keyinfo\X509Data.html`

### Class Description

```java
public interface
X509Data

extends
XMLStructure
```

A representation of the XML

X509Data

element as defined in
the

W3C Recommendation for XML-Signature Syntax and Processing

. An

X509Data

object contains one or more identifers of keys
or X.509 certificates (or certificates' identifiers or a revocation list).
The XML Schema Definition is defined as:

```java
<element name="X509Data" type="ds:X509DataType"/>
<complexType name="X509DataType">
<sequence maxOccurs="unbounded">
<choice>
<element name="X509IssuerSerial" type="ds:X509IssuerSerialType"/>
<element name="X509SKI" type="base64Binary"/>
<element name="X509SubjectName" type="string"/>
<element name="X509Certificate" type="base64Binary"/>
<element name="X509CRL" type="base64Binary"/>
<any namespace="##other" processContents="lax"/>
</choice>
</sequence>
</complexType>

<complexType name="X509IssuerSerialType">
<sequence>
<element name="X509IssuerName" type="string"/>
<element name="X509SerialNumber" type="integer"/>
</sequence>
</complexType>
```

An

X509Data

instance may be created by invoking the

newX509Data

methods of the

KeyInfoFactory

class and passing it a list of one or more

XMLStructure

s representing X.509 content; for example:

```java
KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
X509Data x509Data = factory.newX509Data
(Collections.singletonList("cn=Alice"));
```

**All Superinterfaces:** XMLStructure

---

### Field Details

#### static final
String
TYPE

URI identifying the X509Data KeyInfo type:
http://www.w3.org/2000/09/xmldsig#X509Data. This can be specified as
the value of the

type

parameter of the

RetrievalMethod

class to describe a remote

X509Data

structure.

**See Also:**
- Constant Field Values

---

#### static final
String
RAW_X509_CERTIFICATE_TYPE

URI identifying the binary (ASN.1 DER) X.509 Certificate KeyInfo type:
http://www.w3.org/2000/09/xmldsig#rawX509Certificate. This can be
specified as the value of the

type

parameter of the

RetrievalMethod

class to describe a remote X509 Certificate.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### List
<?> getContent()

Returns an

unmodifiable
list

of the content in this

X509Data

. Valid types are

String

(subject names),

byte[]

(subject key ids),

X509Certificate

,

X509CRL

,
or

XMLStructure

(

X509IssuerSerial

objects or elements from an external namespace).

**Returns:**
- an unmodifiable list of the content in this

X509Data

(never

null

or empty)

---

### Additional Sections

#### Interface X509Data

**All Superinterfaces:** XMLStructure

```java
public interface
X509Data

extends
XMLStructure
```

A representation of the XML

X509Data

element as defined in
the

W3C Recommendation for XML-Signature Syntax and Processing

. An

X509Data

object contains one or more identifers of keys
or X.509 certificates (or certificates' identifiers or a revocation list).
The XML Schema Definition is defined as:

```java
<element name="X509Data" type="ds:X509DataType"/>
<complexType name="X509DataType">
<sequence maxOccurs="unbounded">
<choice>
<element name="X509IssuerSerial" type="ds:X509IssuerSerialType"/>
<element name="X509SKI" type="base64Binary"/>
<element name="X509SubjectName" type="string"/>
<element name="X509Certificate" type="base64Binary"/>
<element name="X509CRL" type="base64Binary"/>
<any namespace="##other" processContents="lax"/>
</choice>
</sequence>
</complexType>

<complexType name="X509IssuerSerialType">
<sequence>
<element name="X509IssuerName" type="string"/>
<element name="X509SerialNumber" type="integer"/>
</sequence>
</complexType>
```

An

X509Data

instance may be created by invoking the

newX509Data

methods of the

KeyInfoFactory

class and passing it a list of one or more

XMLStructure

s representing X.509 content; for example:

```java
KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
X509Data x509Data = factory.newX509Data
(Collections.singletonList("cn=Alice"));
```

**Since:** 1.6
**See Also:** KeyInfoFactory.newX509Data(List)

public interface

X509Data

extends

XMLStructure

A representation of the XML

X509Data

element as defined in
the

W3C Recommendation for XML-Signature Syntax and Processing

. An

X509Data

object contains one or more identifers of keys
or X.509 certificates (or certificates' identifiers or a revocation list).
The XML Schema Definition is defined as:

```java
<element name="X509Data" type="ds:X509DataType"/>
<complexType name="X509DataType">
<sequence maxOccurs="unbounded">
<choice>
<element name="X509IssuerSerial" type="ds:X509IssuerSerialType"/>
<element name="X509SKI" type="base64Binary"/>
<element name="X509SubjectName" type="string"/>
<element name="X509Certificate" type="base64Binary"/>
<element name="X509CRL" type="base64Binary"/>
<any namespace="##other" processContents="lax"/>
</choice>
</sequence>
</complexType>

<complexType name="X509IssuerSerialType">
<sequence>
<element name="X509IssuerName" type="string"/>
<element name="X509SerialNumber" type="integer"/>
</sequence>
</complexType>
```

An

X509Data

instance may be created by invoking the

newX509Data

methods of the

KeyInfoFactory

class and passing it a list of one or more

XMLStructure

s representing X.509 content; for example:

```java
KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
X509Data x509Data = factory.newX509Data
(Collections.singletonList("cn=Alice"));
```

<element name="X509Data" type="ds:X509DataType"/>
<complexType name="X509DataType">
<sequence maxOccurs="unbounded">
<choice>
<element name="X509IssuerSerial" type="ds:X509IssuerSerialType"/>
<element name="X509SKI" type="base64Binary"/>
<element name="X509SubjectName" type="string"/>
<element name="X509Certificate" type="base64Binary"/>
<element name="X509CRL" type="base64Binary"/>
<any namespace="##other" processContents="lax"/>
</choice>
</sequence>
</complexType>

<complexType name="X509IssuerSerialType">
<sequence>
<element name="X509IssuerName" type="string"/>
<element name="X509SerialNumber" type="integer"/>
</sequence>
</complexType>

KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
X509Data x509Data = factory.newX509Data
(Collections.singletonList("cn=Alice"));

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

RAW_X509_CERTIFICATE_TYPE

URI identifying the binary (ASN.1 DER) X.509 Certificate KeyInfo type:
http://www.w3.org/2000/09/xmldsig#rawX509Certificate.

static

String

TYPE

URI identifying the X509Data KeyInfo type:
http://www.w3.org/2000/09/xmldsig#X509Data.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<?>

getContent

()

Returns an

unmodifiable
list

of the content in this

X509Data

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

RAW_X509_CERTIFICATE_TYPE

URI identifying the binary (ASN.1 DER) X.509 Certificate KeyInfo type:
http://www.w3.org/2000/09/xmldsig#rawX509Certificate.

static

String

TYPE

URI identifying the X509Data KeyInfo type:
http://www.w3.org/2000/09/xmldsig#X509Data.

---

#### Field Summary

URI identifying the binary (ASN.1 DER) X.509 Certificate KeyInfo type:
http://www.w3.org/2000/09/xmldsig#rawX509Certificate.

URI identifying the X509Data KeyInfo type:
http://www.w3.org/2000/09/xmldsig#X509Data.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

List

<?>

getContent

()

Returns an

unmodifiable
list

of the content in this

X509Data

.

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Method Summary

Returns an

unmodifiable
list

of the content in this

X509Data

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

URI identifying the X509Data KeyInfo type:
http://www.w3.org/2000/09/xmldsig#X509Data. This can be specified as
the value of the

type

parameter of the

RetrievalMethod

class to describe a remote

X509Data

structure.

**See Also:** Constant Field Values

- RAW_X509_CERTIFICATE_TYPE

```java
static final
String
RAW_X509_CERTIFICATE_TYPE
```

URI identifying the binary (ASN.1 DER) X.509 Certificate KeyInfo type:
http://www.w3.org/2000/09/xmldsig#rawX509Certificate. This can be
specified as the value of the

type

parameter of the

RetrievalMethod

class to describe a remote X509 Certificate.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getContent

```java
List
<?> getContent()
```

Returns an

unmodifiable
list

of the content in this

X509Data

. Valid types are

String

(subject names),

byte[]

(subject key ids),

X509Certificate

,

X509CRL

,
or

XMLStructure

(

X509IssuerSerial

objects or elements from an external namespace).

**Returns:** an unmodifiable list of the content in this

X509Data

(never

null

or empty)

Field Detail

- TYPE

```java
static final
String
TYPE
```

URI identifying the X509Data KeyInfo type:
http://www.w3.org/2000/09/xmldsig#X509Data. This can be specified as
the value of the

type

parameter of the

RetrievalMethod

class to describe a remote

X509Data

structure.

**See Also:** Constant Field Values

- RAW_X509_CERTIFICATE_TYPE

```java
static final
String
RAW_X509_CERTIFICATE_TYPE
```

URI identifying the binary (ASN.1 DER) X.509 Certificate KeyInfo type:
http://www.w3.org/2000/09/xmldsig#rawX509Certificate. This can be
specified as the value of the

type

parameter of the

RetrievalMethod

class to describe a remote X509 Certificate.

**See Also:** Constant Field Values

---

#### Field Detail

TYPE

```java
static final
String
TYPE
```

URI identifying the X509Data KeyInfo type:
http://www.w3.org/2000/09/xmldsig#X509Data. This can be specified as
the value of the

type

parameter of the

RetrievalMethod

class to describe a remote

X509Data

structure.

**See Also:** Constant Field Values

---

#### TYPE

static final

String

TYPE

URI identifying the X509Data KeyInfo type:
http://www.w3.org/2000/09/xmldsig#X509Data. This can be specified as
the value of the

type

parameter of the

RetrievalMethod

class to describe a remote

X509Data

structure.

RAW_X509_CERTIFICATE_TYPE

```java
static final
String
RAW_X509_CERTIFICATE_TYPE
```

URI identifying the binary (ASN.1 DER) X.509 Certificate KeyInfo type:
http://www.w3.org/2000/09/xmldsig#rawX509Certificate. This can be
specified as the value of the

type

parameter of the

RetrievalMethod

class to describe a remote X509 Certificate.

**See Also:** Constant Field Values

---

#### RAW_X509_CERTIFICATE_TYPE

static final

String

RAW_X509_CERTIFICATE_TYPE

URI identifying the binary (ASN.1 DER) X.509 Certificate KeyInfo type:
http://www.w3.org/2000/09/xmldsig#rawX509Certificate. This can be
specified as the value of the

type

parameter of the

RetrievalMethod

class to describe a remote X509 Certificate.

Method Detail

- getContent

```java
List
<?> getContent()
```

Returns an

unmodifiable
list

of the content in this

X509Data

. Valid types are

String

(subject names),

byte[]

(subject key ids),

X509Certificate

,

X509CRL

,
or

XMLStructure

(

X509IssuerSerial

objects or elements from an external namespace).

**Returns:** an unmodifiable list of the content in this

X509Data

(never

null

or empty)

---

#### Method Detail

getContent

```java
List
<?> getContent()
```

Returns an

unmodifiable
list

of the content in this

X509Data

. Valid types are

String

(subject names),

byte[]

(subject key ids),

X509Certificate

,

X509CRL

,
or

XMLStructure

(

X509IssuerSerial

objects or elements from an external namespace).

**Returns:** an unmodifiable list of the content in this

X509Data

(never

null

or empty)

---

#### getContent

List

<?> getContent()

Returns an

unmodifiable
list

of the content in this

X509Data

. Valid types are

String

(subject names),

byte[]

(subject key ids),

X509Certificate

,

X509CRL

,
or

XMLStructure

(

X509IssuerSerial

objects or elements from an external namespace).

---

