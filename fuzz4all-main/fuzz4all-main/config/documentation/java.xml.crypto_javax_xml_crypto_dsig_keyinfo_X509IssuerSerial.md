# Interface X509IssuerSerial

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\keyinfo\X509IssuerSerial.html`

### Class Description

```java
public interface
X509IssuerSerial

extends
XMLStructure
```

A representation of the XML

X509IssuerSerial

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
An

X509IssuerSerial

object contains an X.509 issuer
distinguished name (DN) and serial number pair. The XML schema definition is
defined as:

```java
<element name="X509IssuerSerial" type="ds:X509IssuerSerialType"/>
<complexType name="X509IssuerSerialType">
<sequence>
<element name="X509IssuerName" type="string"/>
<element name="X509SerialNumber" type="integer"/>
</sequence>
</complexType>
```

An

X509IssuerSerial

instance may be created by invoking the

newX509IssuerSerial

method
of the

KeyInfoFactory

class, and passing it a

String

and

BigInteger

representing the X.500
DN and serial number. Here is an example of creating an

X509IssuerSerial

from the issuer DN and serial number of an
existing

X509Certificate

:

```java
KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
X509IssuerSerial issuer = factory.newX509IssuerSerial
(cert.getIssuerX500Principal().getName(), cert.getSerialNumber());
```

**All Superinterfaces:** XMLStructure

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getIssuerName()

Returns the X.500 distinguished name of this

X509IssuerSerial

in

RFC 2253

String format.

**Returns:**
- the X.500 distinguished name in RFC 2253 String format (never

null

)

---

#### BigInteger
getSerialNumber()

Returns the serial number of this

X509IssuerSerial

.

**Returns:**
- the serial number (never

null

)

---

### Additional Sections

#### Interface X509IssuerSerial

**All Superinterfaces:** XMLStructure

```java
public interface
X509IssuerSerial

extends
XMLStructure
```

A representation of the XML

X509IssuerSerial

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
An

X509IssuerSerial

object contains an X.509 issuer
distinguished name (DN) and serial number pair. The XML schema definition is
defined as:

```java
<element name="X509IssuerSerial" type="ds:X509IssuerSerialType"/>
<complexType name="X509IssuerSerialType">
<sequence>
<element name="X509IssuerName" type="string"/>
<element name="X509SerialNumber" type="integer"/>
</sequence>
</complexType>
```

An

X509IssuerSerial

instance may be created by invoking the

newX509IssuerSerial

method
of the

KeyInfoFactory

class, and passing it a

String

and

BigInteger

representing the X.500
DN and serial number. Here is an example of creating an

X509IssuerSerial

from the issuer DN and serial number of an
existing

X509Certificate

:

```java
KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
X509IssuerSerial issuer = factory.newX509IssuerSerial
(cert.getIssuerX500Principal().getName(), cert.getSerialNumber());
```

**Since:** 1.6
**See Also:** X509Data.getContent()

,

KeyInfoFactory.newX509IssuerSerial(String, BigInteger)

public interface

X509IssuerSerial

extends

XMLStructure

A representation of the XML

X509IssuerSerial

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
An

X509IssuerSerial

object contains an X.509 issuer
distinguished name (DN) and serial number pair. The XML schema definition is
defined as:

```java
<element name="X509IssuerSerial" type="ds:X509IssuerSerialType"/>
<complexType name="X509IssuerSerialType">
<sequence>
<element name="X509IssuerName" type="string"/>
<element name="X509SerialNumber" type="integer"/>
</sequence>
</complexType>
```

An

X509IssuerSerial

instance may be created by invoking the

newX509IssuerSerial

method
of the

KeyInfoFactory

class, and passing it a

String

and

BigInteger

representing the X.500
DN and serial number. Here is an example of creating an

X509IssuerSerial

from the issuer DN and serial number of an
existing

X509Certificate

:

```java
KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
X509IssuerSerial issuer = factory.newX509IssuerSerial
(cert.getIssuerX500Principal().getName(), cert.getSerialNumber());
```

<element name="X509IssuerSerial" type="ds:X509IssuerSerialType"/>
<complexType name="X509IssuerSerialType">
<sequence>
<element name="X509IssuerName" type="string"/>
<element name="X509SerialNumber" type="integer"/>
</sequence>
</complexType>

KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
X509IssuerSerial issuer = factory.newX509IssuerSerial
(cert.getIssuerX500Principal().getName(), cert.getSerialNumber());

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getIssuerName

()

Returns the X.500 distinguished name of this

X509IssuerSerial

in

RFC 2253

String format.

BigInteger

getSerialNumber

()

Returns the serial number of this

X509IssuerSerial

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

String

getIssuerName

()

Returns the X.500 distinguished name of this

X509IssuerSerial

in

RFC 2253

String format.

BigInteger

getSerialNumber

()

Returns the serial number of this

X509IssuerSerial

.

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Method Summary

Returns the X.500 distinguished name of this

X509IssuerSerial

in

RFC 2253

String format.

Returns the serial number of this

X509IssuerSerial

.

Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Methods declared in interface javax.xml.crypto. XMLStructure

============ METHOD DETAIL ==========

- Method Detail

- getIssuerName

```java
String
getIssuerName()
```

Returns the X.500 distinguished name of this

X509IssuerSerial

in

RFC 2253

String format.

**Returns:** the X.500 distinguished name in RFC 2253 String format (never

null

)

- getSerialNumber

```java
BigInteger
getSerialNumber()
```

Returns the serial number of this

X509IssuerSerial

.

**Returns:** the serial number (never

null

)

Method Detail

- getIssuerName

```java
String
getIssuerName()
```

Returns the X.500 distinguished name of this

X509IssuerSerial

in

RFC 2253

String format.

**Returns:** the X.500 distinguished name in RFC 2253 String format (never

null

)

- getSerialNumber

```java
BigInteger
getSerialNumber()
```

Returns the serial number of this

X509IssuerSerial

.

**Returns:** the serial number (never

null

)

---

#### Method Detail

getIssuerName

```java
String
getIssuerName()
```

Returns the X.500 distinguished name of this

X509IssuerSerial

in

RFC 2253

String format.

**Returns:** the X.500 distinguished name in RFC 2253 String format (never

null

)

---

#### getIssuerName

String

getIssuerName()

Returns the X.500 distinguished name of this

X509IssuerSerial

in

RFC 2253

String format.

getSerialNumber

```java
BigInteger
getSerialNumber()
```

Returns the serial number of this

X509IssuerSerial

.

**Returns:** the serial number (never

null

)

---

#### getSerialNumber

BigInteger

getSerialNumber()

Returns the serial number of this

X509IssuerSerial

.

---

