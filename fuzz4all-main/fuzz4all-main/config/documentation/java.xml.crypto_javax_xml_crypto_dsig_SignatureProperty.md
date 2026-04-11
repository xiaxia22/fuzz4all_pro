# Interface SignatureProperty

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\SignatureProperty.html`

### Class Description

```java
public interface
SignatureProperty

extends
XMLStructure
```

A representation of the XML

SignatureProperty

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="SignatureProperty" type="ds:SignaturePropertyType"/>
<complexType name="SignaturePropertyType" mixed="true">
<choice maxOccurs="unbounded">
<any namespace="##other" processContents="lax"/>
<!-- (1,1) elements from (1, unbounded) namespaces -->
</choice>
<attribute name="Target" type="anyURI" use="required"/>
<attribute name="Id" type="ID" use="optional"/>
</complexType>
```

A

SignatureProperty

instance may be created by invoking the

newSignatureProperty

method of the

XMLSignatureFactory

class; for example:

```java
XMLSignatureFactory factory = XMLSignatureFactory.getInstance("DOM");
SignatureProperty property = factory.newSignatureProperty
(Collections.singletonList(content), "#Signature-1", "TimeStamp");
```

**All Superinterfaces:** XMLStructure

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getTarget()

Returns the target URI of this

SignatureProperty

.

**Returns:**
- the target URI of this

SignatureProperty

(never

null

)

---

#### String
getId()

Returns the Id of this

SignatureProperty

.

**Returns:**
- the Id of this

SignatureProperty

(or

null

if not specified)

---

#### List
<
XMLStructure
> getContent()

Returns an

unmodifiable
list

of one or more

XMLStructure

s that are contained in
this

SignatureProperty

. These represent additional
information items concerning the generation of the

XMLSignature

(i.e. date/time stamp or serial numbers of cryptographic hardware used
in signature generation).

**Returns:**
- an unmodifiable list of one or more

XMLStructure

s

---

### Additional Sections

#### Interface SignatureProperty

**All Superinterfaces:** XMLStructure

```java
public interface
SignatureProperty

extends
XMLStructure
```

A representation of the XML

SignatureProperty

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="SignatureProperty" type="ds:SignaturePropertyType"/>
<complexType name="SignaturePropertyType" mixed="true">
<choice maxOccurs="unbounded">
<any namespace="##other" processContents="lax"/>
<!-- (1,1) elements from (1, unbounded) namespaces -->
</choice>
<attribute name="Target" type="anyURI" use="required"/>
<attribute name="Id" type="ID" use="optional"/>
</complexType>
```

A

SignatureProperty

instance may be created by invoking the

newSignatureProperty

method of the

XMLSignatureFactory

class; for example:

```java
XMLSignatureFactory factory = XMLSignatureFactory.getInstance("DOM");
SignatureProperty property = factory.newSignatureProperty
(Collections.singletonList(content), "#Signature-1", "TimeStamp");
```

**Since:** 1.6
**See Also:** XMLSignatureFactory.newSignatureProperty(List, String, String)

,

SignatureProperties

public interface

SignatureProperty

extends

XMLStructure

A representation of the XML

SignatureProperty

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="SignatureProperty" type="ds:SignaturePropertyType"/>
<complexType name="SignaturePropertyType" mixed="true">
<choice maxOccurs="unbounded">
<any namespace="##other" processContents="lax"/>
<!-- (1,1) elements from (1, unbounded) namespaces -->
</choice>
<attribute name="Target" type="anyURI" use="required"/>
<attribute name="Id" type="ID" use="optional"/>
</complexType>
```

A

SignatureProperty

instance may be created by invoking the

newSignatureProperty

method of the

XMLSignatureFactory

class; for example:

```java
XMLSignatureFactory factory = XMLSignatureFactory.getInstance("DOM");
SignatureProperty property = factory.newSignatureProperty
(Collections.singletonList(content), "#Signature-1", "TimeStamp");
```

<element name="SignatureProperty" type="ds:SignaturePropertyType"/>
<complexType name="SignaturePropertyType" mixed="true">
<choice maxOccurs="unbounded">
<any namespace="##other" processContents="lax"/>
<!-- (1,1) elements from (1, unbounded) namespaces -->
</choice>
<attribute name="Target" type="anyURI" use="required"/>
<attribute name="Id" type="ID" use="optional"/>
</complexType>

XMLSignatureFactory factory = XMLSignatureFactory.getInstance("DOM");
SignatureProperty property = factory.newSignatureProperty
(Collections.singletonList(content), "#Signature-1", "TimeStamp");

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

of one or more

XMLStructure

s that are contained in
this

SignatureProperty

.

String

getId

()

Returns the Id of this

SignatureProperty

.

String

getTarget

()

Returns the target URI of this

SignatureProperty

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

List

<

XMLStructure

>

getContent

()

Returns an

unmodifiable
list

of one or more

XMLStructure

s that are contained in
this

SignatureProperty

.

String

getId

()

Returns the Id of this

SignatureProperty

.

String

getTarget

()

Returns the target URI of this

SignatureProperty

.

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Method Summary

Returns an

unmodifiable
list

of one or more

XMLStructure

s that are contained in
this

SignatureProperty

.

Returns the Id of this

SignatureProperty

.

Returns the target URI of this

SignatureProperty

.

Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Methods declared in interface javax.xml.crypto. XMLStructure

============ METHOD DETAIL ==========

- Method Detail

- getTarget

```java
String
getTarget()
```

Returns the target URI of this

SignatureProperty

.

**Returns:** the target URI of this

SignatureProperty

(never

null

)

- getId

```java
String
getId()
```

Returns the Id of this

SignatureProperty

.

**Returns:** the Id of this

SignatureProperty

(or

null

if not specified)

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

of one or more

XMLStructure

s that are contained in
this

SignatureProperty

. These represent additional
information items concerning the generation of the

XMLSignature

(i.e. date/time stamp or serial numbers of cryptographic hardware used
in signature generation).

**Returns:** an unmodifiable list of one or more

XMLStructure

s

Method Detail

- getTarget

```java
String
getTarget()
```

Returns the target URI of this

SignatureProperty

.

**Returns:** the target URI of this

SignatureProperty

(never

null

)

- getId

```java
String
getId()
```

Returns the Id of this

SignatureProperty

.

**Returns:** the Id of this

SignatureProperty

(or

null

if not specified)

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

of one or more

XMLStructure

s that are contained in
this

SignatureProperty

. These represent additional
information items concerning the generation of the

XMLSignature

(i.e. date/time stamp or serial numbers of cryptographic hardware used
in signature generation).

**Returns:** an unmodifiable list of one or more

XMLStructure

s

---

#### Method Detail

getTarget

```java
String
getTarget()
```

Returns the target URI of this

SignatureProperty

.

**Returns:** the target URI of this

SignatureProperty

(never

null

)

---

#### getTarget

String

getTarget()

Returns the target URI of this

SignatureProperty

.

getId

```java
String
getId()
```

Returns the Id of this

SignatureProperty

.

**Returns:** the Id of this

SignatureProperty

(or

null

if not specified)

---

#### getId

String

getId()

Returns the Id of this

SignatureProperty

.

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

of one or more

XMLStructure

s that are contained in
this

SignatureProperty

. These represent additional
information items concerning the generation of the

XMLSignature

(i.e. date/time stamp or serial numbers of cryptographic hardware used
in signature generation).

**Returns:** an unmodifiable list of one or more

XMLStructure

s

---

#### getContent

List

<

XMLStructure

> getContent()

Returns an

unmodifiable
list

of one or more

XMLStructure

s that are contained in
this

SignatureProperty

. These represent additional
information items concerning the generation of the

XMLSignature

(i.e. date/time stamp or serial numbers of cryptographic hardware used
in signature generation).

---

