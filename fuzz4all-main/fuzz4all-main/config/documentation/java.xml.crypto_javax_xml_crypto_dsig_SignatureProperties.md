# Interface SignatureProperties

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\SignatureProperties.html`

### Class Description

```java
public interface
SignatureProperties

extends
XMLStructure
```

A representation of the XML

SignatureProperties

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="SignatureProperties" type="ds:SignaturePropertiesType"/>
<complexType name="SignaturePropertiesType">
<sequence>
<element ref="ds:SignatureProperty" maxOccurs="unbounded"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
</complexType>
```

A

SignatureProperties

instance may be created by invoking the

newSignatureProperties

method of the

XMLSignatureFactory

class; for example:

```java
XMLSignatureFactory factory = XMLSignatureFactory.getInstance("DOM");
SignatureProperties properties =
factory.newSignatureProperties(props, "signature-properties-1");
```

**All Superinterfaces:** XMLStructure

---

### Field Details

#### static final
String
TYPE

URI that identifies the

SignatureProperties

element (this
can be specified as the value of the

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

SignatureProperties

.

**Returns:**
- the Id of this

SignatureProperties

(or

null

if not specified)

---

#### List
<
SignatureProperty
> getProperties()

Returns an

unmodifiable
list

of one or more

SignatureProperty

s that are contained in
this

SignatureProperties

.

**Returns:**
- an unmodifiable list of one or more

SignatureProperty

s

---

### Additional Sections

#### Interface SignatureProperties

**All Superinterfaces:** XMLStructure

```java
public interface
SignatureProperties

extends
XMLStructure
```

A representation of the XML

SignatureProperties

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="SignatureProperties" type="ds:SignaturePropertiesType"/>
<complexType name="SignaturePropertiesType">
<sequence>
<element ref="ds:SignatureProperty" maxOccurs="unbounded"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
</complexType>
```

A

SignatureProperties

instance may be created by invoking the

newSignatureProperties

method of the

XMLSignatureFactory

class; for example:

```java
XMLSignatureFactory factory = XMLSignatureFactory.getInstance("DOM");
SignatureProperties properties =
factory.newSignatureProperties(props, "signature-properties-1");
```

**Since:** 1.6
**See Also:** XMLSignatureFactory.newSignatureProperties(List, String)

,

SignatureProperty

public interface

SignatureProperties

extends

XMLStructure

A representation of the XML

SignatureProperties

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
The XML Schema Definition is defined as:

```java
<element name="SignatureProperties" type="ds:SignaturePropertiesType"/>
<complexType name="SignaturePropertiesType">
<sequence>
<element ref="ds:SignatureProperty" maxOccurs="unbounded"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
</complexType>
```

A

SignatureProperties

instance may be created by invoking the

newSignatureProperties

method of the

XMLSignatureFactory

class; for example:

```java
XMLSignatureFactory factory = XMLSignatureFactory.getInstance("DOM");
SignatureProperties properties =
factory.newSignatureProperties(props, "signature-properties-1");
```

<element name="SignatureProperties" type="ds:SignaturePropertiesType"/>
<complexType name="SignaturePropertiesType">
<sequence>
<element ref="ds:SignatureProperty" maxOccurs="unbounded"/>
</sequence>
<attribute name="Id" type="ID" use="optional"/>
</complexType>

XMLSignatureFactory factory = XMLSignatureFactory.getInstance("DOM");
SignatureProperties properties =
factory.newSignatureProperties(props, "signature-properties-1");

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

SignatureProperties

element (this
can be specified as the value of the

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

SignatureProperties

.

List

<

SignatureProperty

>

getProperties

()

Returns an

unmodifiable
list

of one or more

SignatureProperty

s that are contained in
this

SignatureProperties

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

SignatureProperties

element (this
can be specified as the value of the

type

parameter of the

Reference

class to identify the referent's type).

---

#### Field Summary

URI that identifies the

SignatureProperties

element (this
can be specified as the value of the

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

SignatureProperties

.

List

<

SignatureProperty

>

getProperties

()

Returns an

unmodifiable
list

of one or more

SignatureProperty

s that are contained in
this

SignatureProperties

.

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Method Summary

Returns the Id of this

SignatureProperties

.

Returns an

unmodifiable
list

of one or more

SignatureProperty

s that are contained in
this

SignatureProperties

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

SignatureProperties

element (this
can be specified as the value of the

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

SignatureProperties

.

**Returns:** the Id of this

SignatureProperties

(or

null

if not specified)

- getProperties

```java
List
<
SignatureProperty
> getProperties()
```

Returns an

unmodifiable
list

of one or more

SignatureProperty

s that are contained in
this

SignatureProperties

.

**Returns:** an unmodifiable list of one or more

SignatureProperty

s

Field Detail

- TYPE

```java
static final
String
TYPE
```

URI that identifies the

SignatureProperties

element (this
can be specified as the value of the

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

SignatureProperties

element (this
can be specified as the value of the

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

SignatureProperties

element (this
can be specified as the value of the

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

SignatureProperties

.

**Returns:** the Id of this

SignatureProperties

(or

null

if not specified)

- getProperties

```java
List
<
SignatureProperty
> getProperties()
```

Returns an

unmodifiable
list

of one or more

SignatureProperty

s that are contained in
this

SignatureProperties

.

**Returns:** an unmodifiable list of one or more

SignatureProperty

s

---

#### Method Detail

getId

```java
String
getId()
```

Returns the Id of this

SignatureProperties

.

**Returns:** the Id of this

SignatureProperties

(or

null

if not specified)

---

#### getId

String

getId()

Returns the Id of this

SignatureProperties

.

getProperties

```java
List
<
SignatureProperty
> getProperties()
```

Returns an

unmodifiable
list

of one or more

SignatureProperty

s that are contained in
this

SignatureProperties

.

**Returns:** an unmodifiable list of one or more

SignatureProperty

s

---

#### getProperties

List

<

SignatureProperty

> getProperties()

Returns an

unmodifiable
list

of one or more

SignatureProperty

s that are contained in
this

SignatureProperties

.

---

