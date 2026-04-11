# Interface KeyName

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\keyinfo\KeyName.html`

### Class Description

```java
public interface
KeyName

extends
XMLStructure
```

A representation of the XML

KeyName

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
A

KeyName

object contains a string value which may be used
by the signer to communicate a key identifier to the recipient. The
XML Schema Definition is defined as:

```java
<element name="KeyName" type="string"/>
```

A

KeyName

instance may be created by invoking the

newKeyName

method of the

KeyInfoFactory

class, and passing it a

String

representing the name of the key; for example:

```java
KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
KeyName keyName = factory.newKeyName("Alice");
```

**All Superinterfaces:** XMLStructure

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getName()

Returns the name of this

KeyName

.

**Returns:**
- the name of this

KeyName

(never

null

)

---

### Additional Sections

#### Interface KeyName

**All Superinterfaces:** XMLStructure

```java
public interface
KeyName

extends
XMLStructure
```

A representation of the XML

KeyName

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
A

KeyName

object contains a string value which may be used
by the signer to communicate a key identifier to the recipient. The
XML Schema Definition is defined as:

```java
<element name="KeyName" type="string"/>
```

A

KeyName

instance may be created by invoking the

newKeyName

method of the

KeyInfoFactory

class, and passing it a

String

representing the name of the key; for example:

```java
KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
KeyName keyName = factory.newKeyName("Alice");
```

**Since:** 1.6
**See Also:** KeyInfoFactory.newKeyName(String)

public interface

KeyName

extends

XMLStructure

A representation of the XML

KeyName

element as
defined in the

W3C Recommendation for XML-Signature Syntax and Processing

.
A

KeyName

object contains a string value which may be used
by the signer to communicate a key identifier to the recipient. The
XML Schema Definition is defined as:

```java
<element name="KeyName" type="string"/>
```

A

KeyName

instance may be created by invoking the

newKeyName

method of the

KeyInfoFactory

class, and passing it a

String

representing the name of the key; for example:

```java
KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
KeyName keyName = factory.newKeyName("Alice");
```

<element name="KeyName" type="string"/>

KeyInfoFactory factory = KeyInfoFactory.getInstance("DOM");
KeyName keyName = factory.newKeyName("Alice");

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

getName

()

Returns the name of this

KeyName

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

getName

()

Returns the name of this

KeyName

.

- Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Method Summary

Returns the name of this

KeyName

.

Methods declared in interface javax.xml.crypto.

XMLStructure

isFeatureSupported

---

#### Methods declared in interface javax.xml.crypto. XMLStructure

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
String
getName()
```

Returns the name of this

KeyName

.

**Returns:** the name of this

KeyName

(never

null

)

Method Detail

- getName

```java
String
getName()
```

Returns the name of this

KeyName

.

**Returns:** the name of this

KeyName

(never

null

)

---

#### Method Detail

getName

```java
String
getName()
```

Returns the name of this

KeyName

.

**Returns:** the name of this

KeyName

(never

null

)

---

#### getName

String

getName()

Returns the name of this

KeyName

.

---

