# Class HMACParameterSpec

**Source:** `java.xml.crypto\javax\xml\crypto\dsig\spec\HMACParameterSpec.html`

### Class Description

```java
public final class
HMACParameterSpec

extends
Object

implements
SignatureMethodParameterSpec
```

Parameters for the

XML Signature HMAC Algorithm

. The parameters include an optional output
length which specifies the MAC truncation length in bits. The resulting
HMAC will be truncated to the specified number of bits. If the parameter is
not specified, then this implies that all the bits of the hash are to be
output. The XML Schema Definition of the

HMACOutputLength

element is defined as:

```java
<element name="HMACOutputLength" minOccurs="0" type="ds:HMACOutputLengthType"/>
<simpleType name="HMACOutputLengthType">
<restriction base="integer"/>
</simpleType>
```

**All Implemented Interfaces:** AlgorithmParameterSpec

,

SignatureMethodParameterSpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public HMACParameterSpec​(int outputLength)

Creates an

HMACParameterSpec

with the specified truncation
length.

**Parameters:**
- outputLength

- the truncation length in number of bits

---

### Method Details

#### public int getOutputLength()

Returns the truncation length.

**Returns:**
- the truncation length in number of bits

---

### Additional Sections

#### Class HMACParameterSpec

java.lang.Object

- javax.xml.crypto.dsig.spec.HMACParameterSpec

javax.xml.crypto.dsig.spec.HMACParameterSpec

**All Implemented Interfaces:** AlgorithmParameterSpec

,

SignatureMethodParameterSpec

```java
public final class
HMACParameterSpec

extends
Object

implements
SignatureMethodParameterSpec
```

Parameters for the

XML Signature HMAC Algorithm

. The parameters include an optional output
length which specifies the MAC truncation length in bits. The resulting
HMAC will be truncated to the specified number of bits. If the parameter is
not specified, then this implies that all the bits of the hash are to be
output. The XML Schema Definition of the

HMACOutputLength

element is defined as:

```java
<element name="HMACOutputLength" minOccurs="0" type="ds:HMACOutputLengthType"/>
<simpleType name="HMACOutputLengthType">
<restriction base="integer"/>
</simpleType>
```

**Since:** 1.6
**See Also:** SignatureMethod

,

RFC 2104

public final class

HMACParameterSpec

extends

Object

implements

SignatureMethodParameterSpec

Parameters for the

XML Signature HMAC Algorithm

. The parameters include an optional output
length which specifies the MAC truncation length in bits. The resulting
HMAC will be truncated to the specified number of bits. If the parameter is
not specified, then this implies that all the bits of the hash are to be
output. The XML Schema Definition of the

HMACOutputLength

element is defined as:

```java
<element name="HMACOutputLength" minOccurs="0" type="ds:HMACOutputLengthType"/>
<simpleType name="HMACOutputLengthType">
<restriction base="integer"/>
</simpleType>
```

<element name="HMACOutputLength" minOccurs="0" type="ds:HMACOutputLengthType"/>
<simpleType name="HMACOutputLengthType">
<restriction base="integer"/>
</simpleType>

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

HMACParameterSpec

​(int outputLength)

Creates an

HMACParameterSpec

with the specified truncation
length.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getOutputLength

()

Returns the truncation length.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

HMACParameterSpec

​(int outputLength)

Creates an

HMACParameterSpec

with the specified truncation
length.

---

#### Constructor Summary

Creates an

HMACParameterSpec

with the specified truncation
length.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

int

getOutputLength

()

Returns the truncation length.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Method Summary

Returns the truncation length.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- HMACParameterSpec

```java
public HMACParameterSpec​(int outputLength)
```

Creates an

HMACParameterSpec

with the specified truncation
length.

**Parameters:** outputLength

- the truncation length in number of bits

============ METHOD DETAIL ==========

- Method Detail

- getOutputLength

```java
public int getOutputLength()
```

Returns the truncation length.

**Returns:** the truncation length in number of bits

Constructor Detail

- HMACParameterSpec

```java
public HMACParameterSpec​(int outputLength)
```

Creates an

HMACParameterSpec

with the specified truncation
length.

**Parameters:** outputLength

- the truncation length in number of bits

---

#### Constructor Detail

HMACParameterSpec

```java
public HMACParameterSpec​(int outputLength)
```

Creates an

HMACParameterSpec

with the specified truncation
length.

**Parameters:** outputLength

- the truncation length in number of bits

---

#### HMACParameterSpec

public HMACParameterSpec​(int outputLength)

Creates an

HMACParameterSpec

with the specified truncation
length.

Method Detail

- getOutputLength

```java
public int getOutputLength()
```

Returns the truncation length.

**Returns:** the truncation length in number of bits

---

#### Method Detail

getOutputLength

```java
public int getOutputLength()
```

Returns the truncation length.

**Returns:** the truncation length in number of bits

---

#### getOutputLength

public int getOutputLength()

Returns the truncation length.

---

