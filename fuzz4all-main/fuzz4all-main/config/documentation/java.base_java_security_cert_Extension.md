# Interface Extension

**Source:** `java.base\java\security\cert\Extension.html`

### Class Description

```java
public interface
Extension
```

This interface represents an X.509 extension.

Extensions provide a means of associating additional attributes with users
or public keys and for managing a certification hierarchy. The extension
format also allows communities to define private extensions to carry
information unique to those communities.

Each extension contains an object identifier, a criticality setting
indicating whether it is a critical or a non-critical extension, and
and an ASN.1 DER-encoded value. Its ASN.1 definition is:

```java
Extension ::= SEQUENCE {
extnId OBJECT IDENTIFIER,
critical BOOLEAN DEFAULT FALSE,
extnValue OCTET STRING
-- contains a DER encoding of a value
-- of the type registered for use with
-- the extnId object identifier value
}
```

This interface is designed to provide access to a single extension,
unlike

X509Extension

which is more suitable
for accessing a set of extensions.

**Since:** 1.7

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getId()

Gets the extensions's object identifier.

**Returns:**
- the object identifier as a String

---

#### boolean isCritical()

Gets the extension's criticality setting.

**Returns:**
- true if this is a critical extension.

---

#### byte[] getValue()

Gets the extensions's DER-encoded value. Note, this is the bytes
that are encoded as an OCTET STRING. It does not include the OCTET
STRING tag and length.

**Returns:**
- a copy of the extension's value, or

null

if no
extension value is present.

---

#### void encode​(
OutputStream
out)
throws
IOException

Generates the extension's DER encoding and writes it to the output
stream.

**Parameters:**
- out

- the output stream

**Throws:**
- IOException

- on encoding or output error.
- NullPointerException

- if

out

is

null

.

---

### Additional Sections

#### Interface Extension

```java
public interface
Extension
```

This interface represents an X.509 extension.

Extensions provide a means of associating additional attributes with users
or public keys and for managing a certification hierarchy. The extension
format also allows communities to define private extensions to carry
information unique to those communities.

Each extension contains an object identifier, a criticality setting
indicating whether it is a critical or a non-critical extension, and
and an ASN.1 DER-encoded value. Its ASN.1 definition is:

```java
Extension ::= SEQUENCE {
extnId OBJECT IDENTIFIER,
critical BOOLEAN DEFAULT FALSE,
extnValue OCTET STRING
-- contains a DER encoding of a value
-- of the type registered for use with
-- the extnId object identifier value
}
```

This interface is designed to provide access to a single extension,
unlike

X509Extension

which is more suitable
for accessing a set of extensions.

**Since:** 1.7

public interface

Extension

This interface represents an X.509 extension.

Extensions provide a means of associating additional attributes with users
or public keys and for managing a certification hierarchy. The extension
format also allows communities to define private extensions to carry
information unique to those communities.

Each extension contains an object identifier, a criticality setting
indicating whether it is a critical or a non-critical extension, and
and an ASN.1 DER-encoded value. Its ASN.1 definition is:

```java
Extension ::= SEQUENCE {
extnId OBJECT IDENTIFIER,
critical BOOLEAN DEFAULT FALSE,
extnValue OCTET STRING
-- contains a DER encoding of a value
-- of the type registered for use with
-- the extnId object identifier value
}
```

This interface is designed to provide access to a single extension,
unlike

X509Extension

which is more suitable
for accessing a set of extensions.

Extensions provide a means of associating additional attributes with users
or public keys and for managing a certification hierarchy. The extension
format also allows communities to define private extensions to carry
information unique to those communities.

Each extension contains an object identifier, a criticality setting
indicating whether it is a critical or a non-critical extension, and
and an ASN.1 DER-encoded value. Its ASN.1 definition is:

```java
Extension ::= SEQUENCE {
extnId OBJECT IDENTIFIER,
critical BOOLEAN DEFAULT FALSE,
extnValue OCTET STRING
-- contains a DER encoding of a value
-- of the type registered for use with
-- the extnId object identifier value
}
```

This interface is designed to provide access to a single extension,
unlike

X509Extension

which is more suitable
for accessing a set of extensions.

Each extension contains an object identifier, a criticality setting
indicating whether it is a critical or a non-critical extension, and
and an ASN.1 DER-encoded value. Its ASN.1 definition is:

```java
Extension ::= SEQUENCE {
extnId OBJECT IDENTIFIER,
critical BOOLEAN DEFAULT FALSE,
extnValue OCTET STRING
-- contains a DER encoding of a value
-- of the type registered for use with
-- the extnId object identifier value
}
```

This interface is designed to provide access to a single extension,
unlike

X509Extension

which is more suitable
for accessing a set of extensions.

Extension ::= SEQUENCE {
extnId OBJECT IDENTIFIER,
critical BOOLEAN DEFAULT FALSE,
extnValue OCTET STRING
-- contains a DER encoding of a value
-- of the type registered for use with
-- the extnId object identifier value
}

This interface is designed to provide access to a single extension,
unlike

X509Extension

which is more suitable
for accessing a set of extensions.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

encode

​(

OutputStream

out)

Generates the extension's DER encoding and writes it to the output
stream.

String

getId

()

Gets the extensions's object identifier.

byte[]

getValue

()

Gets the extensions's DER-encoded value.

boolean

isCritical

()

Gets the extension's criticality setting.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

encode

​(

OutputStream

out)

Generates the extension's DER encoding and writes it to the output
stream.

String

getId

()

Gets the extensions's object identifier.

byte[]

getValue

()

Gets the extensions's DER-encoded value.

boolean

isCritical

()

Gets the extension's criticality setting.

---

#### Method Summary

Generates the extension's DER encoding and writes it to the output
stream.

Gets the extensions's object identifier.

Gets the extensions's DER-encoded value.

Gets the extension's criticality setting.

============ METHOD DETAIL ==========

- Method Detail

- getId

```java
String
getId()
```

Gets the extensions's object identifier.

**Returns:** the object identifier as a String

- isCritical

```java
boolean isCritical()
```

Gets the extension's criticality setting.

**Returns:** true if this is a critical extension.

- getValue

```java
byte[] getValue()
```

Gets the extensions's DER-encoded value. Note, this is the bytes
that are encoded as an OCTET STRING. It does not include the OCTET
STRING tag and length.

**Returns:** a copy of the extension's value, or

null

if no
extension value is present.

- encode

```java
void encode​(
OutputStream
out)
throws
IOException
```

Generates the extension's DER encoding and writes it to the output
stream.

**Parameters:** out

- the output stream
**Throws:** IOException

- on encoding or output error.
**Throws:** NullPointerException

- if

out

is

null

.

Method Detail

- getId

```java
String
getId()
```

Gets the extensions's object identifier.

**Returns:** the object identifier as a String

- isCritical

```java
boolean isCritical()
```

Gets the extension's criticality setting.

**Returns:** true if this is a critical extension.

- getValue

```java
byte[] getValue()
```

Gets the extensions's DER-encoded value. Note, this is the bytes
that are encoded as an OCTET STRING. It does not include the OCTET
STRING tag and length.

**Returns:** a copy of the extension's value, or

null

if no
extension value is present.

- encode

```java
void encode​(
OutputStream
out)
throws
IOException
```

Generates the extension's DER encoding and writes it to the output
stream.

**Parameters:** out

- the output stream
**Throws:** IOException

- on encoding or output error.
**Throws:** NullPointerException

- if

out

is

null

.

---

#### Method Detail

getId

```java
String
getId()
```

Gets the extensions's object identifier.

**Returns:** the object identifier as a String

---

#### getId

String

getId()

Gets the extensions's object identifier.

isCritical

```java
boolean isCritical()
```

Gets the extension's criticality setting.

**Returns:** true if this is a critical extension.

---

#### isCritical

boolean isCritical()

Gets the extension's criticality setting.

getValue

```java
byte[] getValue()
```

Gets the extensions's DER-encoded value. Note, this is the bytes
that are encoded as an OCTET STRING. It does not include the OCTET
STRING tag and length.

**Returns:** a copy of the extension's value, or

null

if no
extension value is present.

---

#### getValue

byte[] getValue()

Gets the extensions's DER-encoded value. Note, this is the bytes
that are encoded as an OCTET STRING. It does not include the OCTET
STRING tag and length.

encode

```java
void encode​(
OutputStream
out)
throws
IOException
```

Generates the extension's DER encoding and writes it to the output
stream.

**Parameters:** out

- the output stream
**Throws:** IOException

- on encoding or output error.
**Throws:** NullPointerException

- if

out

is

null

.

---

#### encode

void encode​(

OutputStream

out)
throws

IOException

Generates the extension's DER encoding and writes it to the output
stream.

---

