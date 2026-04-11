# Interface KeyValue

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\keyinfo\KeyValue.html`

### Class Description

```java
public interface
KeyValue

extends
XMLStructure
```

A representation of the XML

KeyValue

element as defined
in the

W3C Recommendation for XML-Signature Syntax and Processing

. A

KeyValue

object contains a single public key that may be
useful in validating the signature. The XML schema definition is defined as:

```java
<element name="KeyValue" type="ds:KeyValueType"/>
<complexType name="KeyValueType" mixed="true">
<choice>
<element ref="ds:DSAKeyValue"/>
<element ref="ds:RSAKeyValue"/>
<any namespace="##other" processContents="lax"/>
</choice>
</complexType>

<element name="DSAKeyValue" type="ds:DSAKeyValueType"/>
<complexType name="DSAKeyValueType">
<sequence>
<sequence minOccurs="0">
<element name="P" type="ds:CryptoBinary"/>
<element name="Q" type="ds:CryptoBinary"/>
</sequence>
<element name="G" type="ds:CryptoBinary" minOccurs="0"/>
<element name="Y" type="ds:CryptoBinary"/>
<element name="J" type="ds:CryptoBinary" minOccurs="0"/>
<sequence minOccurs="0">
<element name="Seed" type="ds:CryptoBinary"/>
<element name="PgenCounter" type="ds:CryptoBinary"/>
</sequence>
</sequence>
</complexType>

<element name="RSAKeyValue" type="ds:RSAKeyValueType"/>
<complexType name="RSAKeyValueType">
<sequence>
<element name="Modulus" type="ds:CryptoBinary"/>
<element name="Exponent" type="ds:CryptoBinary"/>
</sequence>
</complexType>
```

A

KeyValue

instance may be created by invoking the

newKeyValue

method of the

KeyInfoFactory

class, and passing it a

PublicKey

representing the value of the public key. Here is
an example of creating a

KeyValue

from a

DSAPublicKey

of a

Certificate

stored in a

KeyStore

:

```java
KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());
PublicKey dsaPublicKey = keyStore.getCertificate("myDSASigningCert").getPublicKey();
KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
KeyValue keyValue = factory.newKeyValue(dsaPublicKey);
```

This class returns the

DSAKeyValue

and

RSAKeyValue

elements as objects of type

DSAPublicKey

and

RSAPublicKey

, respectively. Note that not
all of the fields in the schema are accessible as parameters of these
types.

**All Superinterfaces:** XMLStructure

---

### Field Details

#### static final
String
DSA_TYPE

URI identifying the DSA KeyValue KeyInfo type:
http://www.w3.org/2000/09/xmldsig#DSAKeyValue. This can be specified as
the value of the

type

parameter of the

RetrievalMethod

class to describe a remote

DSAKeyValue

structure.

**See Also:**
- Constant Field Values

---

#### static final
String
RSA_TYPE

URI identifying the RSA KeyValue KeyInfo type:
http://www.w3.org/2000/09/xmldsig#RSAKeyValue. This can be specified as
the value of the

type

parameter of the

RetrievalMethod

class to describe a remote

RSAKeyValue

structure.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### PublicKey
getPublicKey()
throws
KeyException

Returns the public key of this

KeyValue

.

**Returns:**
- the public key of this

KeyValue

**Throws:**
- KeyException

- if this

KeyValue

cannot be converted
to a

PublicKey

---

### Additional Sections

#### Interface KeyValue

**All Superinterfaces:** XMLStructure

```java
public interface
KeyValue

extends
XMLStructure
```

A representation of the XML

KeyValue

element as defined
in the

W3C Recommendation for XML-Signature Syntax and Processing

. A

KeyValue

object contains a single public key that may be
useful in validating the signature. The XML schema definition is defined as:

```java
<element name="KeyValue" type="ds:KeyValueType"/>
<complexType name="KeyValueType" mixed="true">
<choice>
<element ref="ds:DSAKeyValue"/>
<element ref="ds:RSAKeyValue"/>
<any namespace="##other" processContents="lax"/>
</choice>
</complexType>

<element name="DSAKeyValue" type="ds:DSAKeyValueType"/>
<complexType name="DSAKeyValueType">
<sequence>
<sequence minOccurs="0">
<element name="P" type="ds:CryptoBinary"/>
<element name="Q" type="ds:CryptoBinary"/>
</sequence>
<element name="G" type="ds:CryptoBinary" minOccurs="0"/>
<element name="Y" type="ds:CryptoBinary"/>
<element name="J" type="ds:CryptoBinary" minOccurs="0"/>
<sequence minOccurs="0">
<element name="Seed" type="ds:CryptoBinary"/>
<element name="PgenCounter" type="ds:CryptoBinary"/>
</sequence>
</sequence>
</complexType>

<element name="RSAKeyValue" type="ds:RSAKeyValueType"/>
<complexType name="RSAKeyValueType">
<sequence>
<element name="Modulus" type="ds:CryptoBinary"/>
<element name="Exponent" type="ds:CryptoBinary"/>
</sequence>
</complexType>
```

A

KeyValue

instance may be created by invoking the

newKeyValue

method of the

KeyInfoFactory

class, and passing it a

PublicKey

representing the value of the public key. Here is
an example of creating a

KeyValue

from a

DSAPublicKey

of a

Certificate

stored in a

KeyStore

:

```java
KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());
PublicKey dsaPublicKey = keyStore.getCertificate("myDSASigningCert").getPublicKey();
KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
KeyValue keyValue = factory.newKeyValue(dsaPublicKey);
```

This class returns the

DSAKeyValue

and

RSAKeyValue

elements as objects of type

DSAPublicKey

and

RSAPublicKey

, respectively. Note that not
all of the fields in the schema are accessible as parameters of these
types.

**Since:** 1.6
**See Also:** KeyInfoFactory.newKeyValue(PublicKey)

public interface

KeyValue

extends

XMLStructure

A representation of the XML

KeyValue

element as defined
in the

W3C Recommendation for XML-Signature Syntax and Processing

. A

KeyValue

object contains a single public key that may be
useful in validating the signature. The XML schema definition is defined as:

```java
<element name="KeyValue" type="ds:KeyValueType"/>
<complexType name="KeyValueType" mixed="true">
<choice>
<element ref="ds:DSAKeyValue"/>
<element ref="ds:RSAKeyValue"/>
<any namespace="##other" processContents="lax"/>
</choice>
</complexType>

<element name="DSAKeyValue" type="ds:DSAKeyValueType"/>
<complexType name="DSAKeyValueType">
<sequence>
<sequence minOccurs="0">
<element name="P" type="ds:CryptoBinary"/>
<element name="Q" type="ds:CryptoBinary"/>
</sequence>
<element name="G" type="ds:CryptoBinary" minOccurs="0"/>
<element name="Y" type="ds:CryptoBinary"/>
<element name="J" type="ds:CryptoBinary" minOccurs="0"/>
<sequence minOccurs="0">
<element name="Seed" type="ds:CryptoBinary"/>
<element name="PgenCounter" type="ds:CryptoBinary"/>
</sequence>
</sequence>
</complexType>

<element name="RSAKeyValue" type="ds:RSAKeyValueType"/>
<complexType name="RSAKeyValueType">
<sequence>
<element name="Modulus" type="ds:CryptoBinary"/>
<element name="Exponent" type="ds:CryptoBinary"/>
</sequence>
</complexType>
```

A

KeyValue

instance may be created by invoking the

newKeyValue

method of the

KeyInfoFactory

class, and passing it a

PublicKey

representing the value of the public key. Here is
an example of creating a

KeyValue

from a

DSAPublicKey

of a

Certificate

stored in a

KeyStore

:

```java
KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());
PublicKey dsaPublicKey = keyStore.getCertificate("myDSASigningCert").getPublicKey();
KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
KeyValue keyValue = factory.newKeyValue(dsaPublicKey);
```

This class returns the

DSAKeyValue

and

RSAKeyValue

elements as objects of type

DSAPublicKey

and

RSAPublicKey

, respectively. Note that not
all of the fields in the schema are accessible as parameters of these
types.

<element name="KeyValue" type="ds:KeyValueType"/>
<complexType name="KeyValueType" mixed="true">
<choice>
<element ref="ds:DSAKeyValue"/>
<element ref="ds:RSAKeyValue"/>
<any namespace="##other" processContents="lax"/>
</choice>
</complexType>

<element name="DSAKeyValue" type="ds:DSAKeyValueType"/>
<complexType name="DSAKeyValueType">
<sequence>
<sequence minOccurs="0">
<element name="P" type="ds:CryptoBinary"/>
<element name="Q" type="ds:CryptoBinary"/>
</sequence>
<element name="G" type="ds:CryptoBinary" minOccurs="0"/>
<element name="Y" type="ds:CryptoBinary"/>
<element name="J" type="ds:CryptoBinary" minOccurs="0"/>
<sequence minOccurs="0">
<element name="Seed" type="ds:CryptoBinary"/>
<element name="PgenCounter" type="ds:CryptoBinary"/>
</sequence>
</sequence>
</complexType>

<element name="RSAKeyValue" type="ds:RSAKeyValueType"/>
<complexType name="RSAKeyValueType">
<sequence>
<element name="Modulus" type="ds:CryptoBinary"/>
<element name="Exponent" type="ds:CryptoBinary"/>
</sequence>
</complexType>

KeyStore keyStore = KeyStore.getInstance(KeyStore.getDefaultType());
PublicKey dsaPublicKey = keyStore.getCertificate("myDSASigningCert").getPublicKey();
KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
KeyValue keyValue = factory.newKeyValue(dsaPublicKey);

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

DSA_TYPE

URI identifying the DSA KeyValue KeyInfo type:
http://www.w3.org/2000/09/xmldsig#DSAKeyValue.

static

String

RSA_TYPE

URI identifying the RSA KeyValue KeyInfo type:
http://www.w3.org/2000/09/xmldsig#RSAKeyValue.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

PublicKey

getPublicKey

()

Returns the public key of this

KeyValue

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

DSA_TYPE

URI identifying the DSA KeyValue KeyInfo type:
http://www.w3.org/2000/09/xmldsig#DSAKeyValue.

static

String

RSA_TYPE

URI identifying the RSA KeyValue KeyInfo type:
http://www.w3.org/2000/09/xmldsig#RSAKeyValue.

---

#### Field Summary

URI identifying the DSA KeyValue KeyInfo type:
http://www.w3.org/2000/09/xmldsig#DSAKeyValue.

URI identifying the RSA KeyValue KeyInfo type:
http://www.w3.org/2000/09/xmldsig#RSAKeyValue.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

PublicKey

getPublicKey

()

Returns the public key of this

KeyValue

.

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Method Summary

Returns the public key of this

KeyValue

.

Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Methods declared in interface javax.xml.crypto. XMLStructure

============ FIELD DETAIL ===========

- Field Detail

- DSA_TYPE

```java
static final
String
DSA_TYPE
```

URI identifying the DSA KeyValue KeyInfo type:
http://www.w3.org/2000/09/xmldsig#DSAKeyValue. This can be specified as
the value of the

type

parameter of the

RetrievalMethod

class to describe a remote

DSAKeyValue

structure.

**See Also:** Constant Field Values

- RSA_TYPE

```java
static final
String
RSA_TYPE
```

URI identifying the RSA KeyValue KeyInfo type:
http://www.w3.org/2000/09/xmldsig#RSAKeyValue. This can be specified as
the value of the

type

parameter of the

RetrievalMethod

class to describe a remote

RSAKeyValue

structure.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getPublicKey

```java
PublicKey
getPublicKey()
throws
KeyException
```

Returns the public key of this

KeyValue

.

**Returns:** the public key of this

KeyValue
**Throws:** KeyException

- if this

KeyValue

cannot be converted
to a

PublicKey

Field Detail

- DSA_TYPE

```java
static final
String
DSA_TYPE
```

URI identifying the DSA KeyValue KeyInfo type:
http://www.w3.org/2000/09/xmldsig#DSAKeyValue. This can be specified as
the value of the

type

parameter of the

RetrievalMethod

class to describe a remote

DSAKeyValue

structure.

**See Also:** Constant Field Values

- RSA_TYPE

```java
static final
String
RSA_TYPE
```

URI identifying the RSA KeyValue KeyInfo type:
http://www.w3.org/2000/09/xmldsig#RSAKeyValue. This can be specified as
the value of the

type

parameter of the

RetrievalMethod

class to describe a remote

RSAKeyValue

structure.

**See Also:** Constant Field Values

---

#### Field Detail

DSA_TYPE

```java
static final
String
DSA_TYPE
```

URI identifying the DSA KeyValue KeyInfo type:
http://www.w3.org/2000/09/xmldsig#DSAKeyValue. This can be specified as
the value of the

type

parameter of the

RetrievalMethod

class to describe a remote

DSAKeyValue

structure.

**See Also:** Constant Field Values

---

#### DSA_TYPE

static final

String

DSA_TYPE

URI identifying the DSA KeyValue KeyInfo type:
http://www.w3.org/2000/09/xmldsig#DSAKeyValue. This can be specified as
the value of the

type

parameter of the

RetrievalMethod

class to describe a remote

DSAKeyValue

structure.

RSA_TYPE

```java
static final
String
RSA_TYPE
```

URI identifying the RSA KeyValue KeyInfo type:
http://www.w3.org/2000/09/xmldsig#RSAKeyValue. This can be specified as
the value of the

type

parameter of the

RetrievalMethod

class to describe a remote

RSAKeyValue

structure.

**See Also:** Constant Field Values

---

#### RSA_TYPE

static final

String

RSA_TYPE

URI identifying the RSA KeyValue KeyInfo type:
http://www.w3.org/2000/09/xmldsig#RSAKeyValue. This can be specified as
the value of the

type

parameter of the

RetrievalMethod

class to describe a remote

RSAKeyValue

structure.

Method Detail

- getPublicKey

```java
PublicKey
getPublicKey()
throws
KeyException
```

Returns the public key of this

KeyValue

.

**Returns:** the public key of this

KeyValue
**Throws:** KeyException

- if this

KeyValue

cannot be converted
to a

PublicKey

---

#### Method Detail

getPublicKey

```java
PublicKey
getPublicKey()
throws
KeyException
```

Returns the public key of this

KeyValue

.

**Returns:** the public key of this

KeyValue
**Throws:** KeyException

- if this

KeyValue

cannot be converted
to a

PublicKey

---

#### getPublicKey

PublicKey

getPublicKey()
throws

KeyException

Returns the public key of this

KeyValue

.

---

