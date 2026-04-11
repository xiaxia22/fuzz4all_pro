# Class MGF1ParameterSpec

**Source:** `java.base\java\security\spec\MGF1ParameterSpec.html`

### Class Description

```java
public class
MGF1ParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This class specifies the set of parameters used with mask generation
function MGF1 in OAEP Padding and RSASSA-PSS signature scheme, as
defined in the

PKCS#1 v2.2

standard.

Its ASN.1 definition in PKCS#1 standard is described below:

```java
PKCS1MGFAlgorithms ALGORITHM-IDENTIFIER ::= {
{ OID id-mgf1 PARAMETERS HashAlgorithm },
... -- Allows for future expansion --
}
```

where

```java
HashAlgorithm ::= AlgorithmIdentifier {
{OAEP-PSSDigestAlgorithms}
}

OAEP-PSSDigestAlgorithms ALGORITHM-IDENTIFIER ::= {
{ OID id-sha1 PARAMETERS NULL }|
{ OID id-sha224 PARAMETERS NULL }|
{ OID id-sha256 PARAMETERS NULL }|
{ OID id-sha384 PARAMETERS NULL }|
{ OID id-sha512 PARAMETERS NULL }|
{ OID id-sha512-224 PARAMETERS NULL }|
{ OID id-sha512-256 PARAMETERS NULL },
... -- Allows for future expansion --
}
```

**All Implemented Interfaces:** AlgorithmParameterSpec

---

### Field Details

#### public static final
MGF1ParameterSpec
SHA1

The MGF1ParameterSpec which uses "SHA-1" message digest

---

#### public static final
MGF1ParameterSpec
SHA224

The MGF1ParameterSpec which uses "SHA-224" message digest

---

#### public static final
MGF1ParameterSpec
SHA256

The MGF1ParameterSpec which uses "SHA-256" message digest

---

#### public static final
MGF1ParameterSpec
SHA384

The MGF1ParameterSpec which uses "SHA-384" message digest

---

#### public static final
MGF1ParameterSpec
SHA512

The MGF1ParameterSpec which uses SHA-512 message digest

---

#### public static final
MGF1ParameterSpec
SHA512_224

The MGF1ParameterSpec which uses SHA-512/224 message digest

---

#### public static final
MGF1ParameterSpec
SHA512_256

The MGF1ParameterSpec which uses SHA-512/256 message digest

---

### Constructor Details

#### public MGF1ParameterSpec​(
String
mdName)

Constructs a parameter set for mask generation function MGF1
as defined in the PKCS #1 standard.

**Parameters:**
- mdName

- the algorithm name for the message digest
used in this mask generation function MGF1.

**Throws:**
- NullPointerException

- if

mdName

is null.

---

### Method Details

#### public
String
getDigestAlgorithm()

Returns the algorithm name of the message digest used by the mask
generation function.

**Returns:**
- the algorithm name of the message digest.

---

### Additional Sections

#### Class MGF1ParameterSpec

java.lang.Object

- java.security.spec.MGF1ParameterSpec

java.security.spec.MGF1ParameterSpec

**All Implemented Interfaces:** AlgorithmParameterSpec

```java
public class
MGF1ParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This class specifies the set of parameters used with mask generation
function MGF1 in OAEP Padding and RSASSA-PSS signature scheme, as
defined in the

PKCS#1 v2.2

standard.

Its ASN.1 definition in PKCS#1 standard is described below:

```java
PKCS1MGFAlgorithms ALGORITHM-IDENTIFIER ::= {
{ OID id-mgf1 PARAMETERS HashAlgorithm },
... -- Allows for future expansion --
}
```

where

```java
HashAlgorithm ::= AlgorithmIdentifier {
{OAEP-PSSDigestAlgorithms}
}

OAEP-PSSDigestAlgorithms ALGORITHM-IDENTIFIER ::= {
{ OID id-sha1 PARAMETERS NULL }|
{ OID id-sha224 PARAMETERS NULL }|
{ OID id-sha256 PARAMETERS NULL }|
{ OID id-sha384 PARAMETERS NULL }|
{ OID id-sha512 PARAMETERS NULL }|
{ OID id-sha512-224 PARAMETERS NULL }|
{ OID id-sha512-256 PARAMETERS NULL },
... -- Allows for future expansion --
}
```

**Since:** 1.5
**See Also:** PSSParameterSpec

,

OAEPParameterSpec

public class

MGF1ParameterSpec

extends

Object

implements

AlgorithmParameterSpec

This class specifies the set of parameters used with mask generation
function MGF1 in OAEP Padding and RSASSA-PSS signature scheme, as
defined in the

PKCS#1 v2.2

standard.

Its ASN.1 definition in PKCS#1 standard is described below:

```java
PKCS1MGFAlgorithms ALGORITHM-IDENTIFIER ::= {
{ OID id-mgf1 PARAMETERS HashAlgorithm },
... -- Allows for future expansion --
}
```

where

```java
HashAlgorithm ::= AlgorithmIdentifier {
{OAEP-PSSDigestAlgorithms}
}

OAEP-PSSDigestAlgorithms ALGORITHM-IDENTIFIER ::= {
{ OID id-sha1 PARAMETERS NULL }|
{ OID id-sha224 PARAMETERS NULL }|
{ OID id-sha256 PARAMETERS NULL }|
{ OID id-sha384 PARAMETERS NULL }|
{ OID id-sha512 PARAMETERS NULL }|
{ OID id-sha512-224 PARAMETERS NULL }|
{ OID id-sha512-256 PARAMETERS NULL },
... -- Allows for future expansion --
}
```

Its ASN.1 definition in PKCS#1 standard is described below:

```java
PKCS1MGFAlgorithms ALGORITHM-IDENTIFIER ::= {
{ OID id-mgf1 PARAMETERS HashAlgorithm },
... -- Allows for future expansion --
}
```

where

```java
HashAlgorithm ::= AlgorithmIdentifier {
{OAEP-PSSDigestAlgorithms}
}

OAEP-PSSDigestAlgorithms ALGORITHM-IDENTIFIER ::= {
{ OID id-sha1 PARAMETERS NULL }|
{ OID id-sha224 PARAMETERS NULL }|
{ OID id-sha256 PARAMETERS NULL }|
{ OID id-sha384 PARAMETERS NULL }|
{ OID id-sha512 PARAMETERS NULL }|
{ OID id-sha512-224 PARAMETERS NULL }|
{ OID id-sha512-256 PARAMETERS NULL },
... -- Allows for future expansion --
}
```

PKCS1MGFAlgorithms ALGORITHM-IDENTIFIER ::= {
{ OID id-mgf1 PARAMETERS HashAlgorithm },
... -- Allows for future expansion --
}

HashAlgorithm ::= AlgorithmIdentifier {
{OAEP-PSSDigestAlgorithms}
}

OAEP-PSSDigestAlgorithms ALGORITHM-IDENTIFIER ::= {
{ OID id-sha1 PARAMETERS NULL }|
{ OID id-sha224 PARAMETERS NULL }|
{ OID id-sha256 PARAMETERS NULL }|
{ OID id-sha384 PARAMETERS NULL }|
{ OID id-sha512 PARAMETERS NULL }|
{ OID id-sha512-224 PARAMETERS NULL }|
{ OID id-sha512-256 PARAMETERS NULL },
... -- Allows for future expansion --
}

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

MGF1ParameterSpec

SHA1

The MGF1ParameterSpec which uses "SHA-1" message digest

static

MGF1ParameterSpec

SHA224

The MGF1ParameterSpec which uses "SHA-224" message digest

static

MGF1ParameterSpec

SHA256

The MGF1ParameterSpec which uses "SHA-256" message digest

static

MGF1ParameterSpec

SHA384

The MGF1ParameterSpec which uses "SHA-384" message digest

static

MGF1ParameterSpec

SHA512

The MGF1ParameterSpec which uses SHA-512 message digest

static

MGF1ParameterSpec

SHA512_224

The MGF1ParameterSpec which uses SHA-512/224 message digest

static

MGF1ParameterSpec

SHA512_256

The MGF1ParameterSpec which uses SHA-512/256 message digest

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MGF1ParameterSpec

​(

String

mdName)

Constructs a parameter set for mask generation function MGF1
as defined in the PKCS #1 standard.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getDigestAlgorithm

()

Returns the algorithm name of the message digest used by the mask
generation function.

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

Field Summary

Fields

Modifier and Type

Field

Description

static

MGF1ParameterSpec

SHA1

The MGF1ParameterSpec which uses "SHA-1" message digest

static

MGF1ParameterSpec

SHA224

The MGF1ParameterSpec which uses "SHA-224" message digest

static

MGF1ParameterSpec

SHA256

The MGF1ParameterSpec which uses "SHA-256" message digest

static

MGF1ParameterSpec

SHA384

The MGF1ParameterSpec which uses "SHA-384" message digest

static

MGF1ParameterSpec

SHA512

The MGF1ParameterSpec which uses SHA-512 message digest

static

MGF1ParameterSpec

SHA512_224

The MGF1ParameterSpec which uses SHA-512/224 message digest

static

MGF1ParameterSpec

SHA512_256

The MGF1ParameterSpec which uses SHA-512/256 message digest

---

#### Field Summary

The MGF1ParameterSpec which uses "SHA-1" message digest

The MGF1ParameterSpec which uses "SHA-224" message digest

The MGF1ParameterSpec which uses "SHA-256" message digest

The MGF1ParameterSpec which uses "SHA-384" message digest

The MGF1ParameterSpec which uses SHA-512 message digest

The MGF1ParameterSpec which uses SHA-512/224 message digest

The MGF1ParameterSpec which uses SHA-512/256 message digest

Constructor Summary

Constructors

Constructor

Description

MGF1ParameterSpec

​(

String

mdName)

Constructs a parameter set for mask generation function MGF1
as defined in the PKCS #1 standard.

---

#### Constructor Summary

Constructs a parameter set for mask generation function MGF1
as defined in the PKCS #1 standard.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getDigestAlgorithm

()

Returns the algorithm name of the message digest used by the mask
generation function.

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

Returns the algorithm name of the message digest used by the mask
generation function.

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

============ FIELD DETAIL ===========

- Field Detail

- SHA1

```java
public static final
MGF1ParameterSpec
SHA1
```

The MGF1ParameterSpec which uses "SHA-1" message digest

- SHA224

```java
public static final
MGF1ParameterSpec
SHA224
```

The MGF1ParameterSpec which uses "SHA-224" message digest

- SHA256

```java
public static final
MGF1ParameterSpec
SHA256
```

The MGF1ParameterSpec which uses "SHA-256" message digest

- SHA384

```java
public static final
MGF1ParameterSpec
SHA384
```

The MGF1ParameterSpec which uses "SHA-384" message digest

- SHA512

```java
public static final
MGF1ParameterSpec
SHA512
```

The MGF1ParameterSpec which uses SHA-512 message digest

- SHA512_224

```java
public static final
MGF1ParameterSpec
SHA512_224
```

The MGF1ParameterSpec which uses SHA-512/224 message digest

- SHA512_256

```java
public static final
MGF1ParameterSpec
SHA512_256
```

The MGF1ParameterSpec which uses SHA-512/256 message digest

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MGF1ParameterSpec

```java
public MGF1ParameterSpec​(
String
mdName)
```

Constructs a parameter set for mask generation function MGF1
as defined in the PKCS #1 standard.

**Parameters:** mdName

- the algorithm name for the message digest
used in this mask generation function MGF1.
**Throws:** NullPointerException

- if

mdName

is null.

============ METHOD DETAIL ==========

- Method Detail

- getDigestAlgorithm

```java
public
String
getDigestAlgorithm()
```

Returns the algorithm name of the message digest used by the mask
generation function.

**Returns:** the algorithm name of the message digest.

Field Detail

- SHA1

```java
public static final
MGF1ParameterSpec
SHA1
```

The MGF1ParameterSpec which uses "SHA-1" message digest

- SHA224

```java
public static final
MGF1ParameterSpec
SHA224
```

The MGF1ParameterSpec which uses "SHA-224" message digest

- SHA256

```java
public static final
MGF1ParameterSpec
SHA256
```

The MGF1ParameterSpec which uses "SHA-256" message digest

- SHA384

```java
public static final
MGF1ParameterSpec
SHA384
```

The MGF1ParameterSpec which uses "SHA-384" message digest

- SHA512

```java
public static final
MGF1ParameterSpec
SHA512
```

The MGF1ParameterSpec which uses SHA-512 message digest

- SHA512_224

```java
public static final
MGF1ParameterSpec
SHA512_224
```

The MGF1ParameterSpec which uses SHA-512/224 message digest

- SHA512_256

```java
public static final
MGF1ParameterSpec
SHA512_256
```

The MGF1ParameterSpec which uses SHA-512/256 message digest

---

#### Field Detail

SHA1

```java
public static final
MGF1ParameterSpec
SHA1
```

The MGF1ParameterSpec which uses "SHA-1" message digest

---

#### SHA1

public static final

MGF1ParameterSpec

SHA1

The MGF1ParameterSpec which uses "SHA-1" message digest

SHA224

```java
public static final
MGF1ParameterSpec
SHA224
```

The MGF1ParameterSpec which uses "SHA-224" message digest

---

#### SHA224

public static final

MGF1ParameterSpec

SHA224

The MGF1ParameterSpec which uses "SHA-224" message digest

SHA256

```java
public static final
MGF1ParameterSpec
SHA256
```

The MGF1ParameterSpec which uses "SHA-256" message digest

---

#### SHA256

public static final

MGF1ParameterSpec

SHA256

The MGF1ParameterSpec which uses "SHA-256" message digest

SHA384

```java
public static final
MGF1ParameterSpec
SHA384
```

The MGF1ParameterSpec which uses "SHA-384" message digest

---

#### SHA384

public static final

MGF1ParameterSpec

SHA384

The MGF1ParameterSpec which uses "SHA-384" message digest

SHA512

```java
public static final
MGF1ParameterSpec
SHA512
```

The MGF1ParameterSpec which uses SHA-512 message digest

---

#### SHA512

public static final

MGF1ParameterSpec

SHA512

The MGF1ParameterSpec which uses SHA-512 message digest

SHA512_224

```java
public static final
MGF1ParameterSpec
SHA512_224
```

The MGF1ParameterSpec which uses SHA-512/224 message digest

---

#### SHA512_224

public static final

MGF1ParameterSpec

SHA512_224

The MGF1ParameterSpec which uses SHA-512/224 message digest

SHA512_256

```java
public static final
MGF1ParameterSpec
SHA512_256
```

The MGF1ParameterSpec which uses SHA-512/256 message digest

---

#### SHA512_256

public static final

MGF1ParameterSpec

SHA512_256

The MGF1ParameterSpec which uses SHA-512/256 message digest

Constructor Detail

- MGF1ParameterSpec

```java
public MGF1ParameterSpec​(
String
mdName)
```

Constructs a parameter set for mask generation function MGF1
as defined in the PKCS #1 standard.

**Parameters:** mdName

- the algorithm name for the message digest
used in this mask generation function MGF1.
**Throws:** NullPointerException

- if

mdName

is null.

---

#### Constructor Detail

MGF1ParameterSpec

```java
public MGF1ParameterSpec​(
String
mdName)
```

Constructs a parameter set for mask generation function MGF1
as defined in the PKCS #1 standard.

**Parameters:** mdName

- the algorithm name for the message digest
used in this mask generation function MGF1.
**Throws:** NullPointerException

- if

mdName

is null.

---

#### MGF1ParameterSpec

public MGF1ParameterSpec​(

String

mdName)

Constructs a parameter set for mask generation function MGF1
as defined in the PKCS #1 standard.

Method Detail

- getDigestAlgorithm

```java
public
String
getDigestAlgorithm()
```

Returns the algorithm name of the message digest used by the mask
generation function.

**Returns:** the algorithm name of the message digest.

---

#### Method Detail

getDigestAlgorithm

```java
public
String
getDigestAlgorithm()
```

Returns the algorithm name of the message digest used by the mask
generation function.

**Returns:** the algorithm name of the message digest.

---

#### getDigestAlgorithm

public

String

getDigestAlgorithm()

Returns the algorithm name of the message digest used by the mask
generation function.

---

