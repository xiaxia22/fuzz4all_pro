# Class OAEPParameterSpec

**Source:** `java.base\javax\crypto\spec\OAEPParameterSpec.html`

### Class Description

```java
public class
OAEPParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This class specifies the set of parameters used with OAEP Padding,
as defined in the

PKCS#1 v2.2

standard.

Its ASN.1 definition in PKCS#1 standard is described below:

```java
RSAES-OAEP-params ::= SEQUENCE {
hashAlgorithm [0] HashAlgorithm DEFAULT sha1,
maskGenAlgorithm [1] MaskGenAlgorithm DEFAULT mgf1SHA1,
pSourceAlgorithm [2] PSourceAlgorithm DEFAULT pSpecifiedEmpty
}
```

where

```java
HashAlgorithm ::= AlgorithmIdentifier {
{OAEP-PSSDigestAlgorithms}
}
MaskGenAlgorithm ::= AlgorithmIdentifier { {PKCS1MGFAlgorithms} }
PSourceAlgorithm ::= AlgorithmIdentifier {
{PKCS1PSourceAlgorithms}
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
PKCS1MGFAlgorithms ALGORITHM-IDENTIFIER ::= {
{ OID id-mgf1 PARAMETERS HashAlgorithm },
... -- Allows for future expansion --
}
PKCS1PSourceAlgorithms ALGORITHM-IDENTIFIER ::= {
{ OID id-pSpecified PARAMETERS EncodingParameters },
... -- Allows for future expansion --
}
EncodingParameters ::= OCTET STRING(SIZE(0..MAX))
```

Note: the OAEPParameterSpec.DEFAULT uses the following:

```java
message digest -- "SHA-1"
mask generation function (mgf) -- "MGF1"
parameters for mgf -- MGF1ParameterSpec.SHA1
source of encoding input -- PSource.PSpecified.DEFAULT
```

**All Implemented Interfaces:** AlgorithmParameterSpec

---

### Field Details

#### public static final
OAEPParameterSpec
DEFAULT

The OAEP parameter set with all default values.

---

### Constructor Details

#### public OAEPParameterSpec​(
String
mdName,

String
mgfName,

AlgorithmParameterSpec
mgfSpec,

PSource
pSrc)

Constructs a parameter set for OAEP padding as defined in
the PKCS #1 standard using the specified message digest
algorithm

mdName

, mask generation function
algorithm

mgfName

, parameters for the mask
generation function

mgfSpec

, and source of
the encoding input P

pSrc

.

**Parameters:**
- mdName

- the algorithm name for the message digest.
- mgfName

- the algorithm name for the mask generation
function.
- mgfSpec

- the parameters for the mask generation function.
If null is specified, null will be returned by getMGFParameters().
- pSrc

- the source of the encoding input P.

**Throws:**
- NullPointerException

- if

mdName

,

mgfName

, or

pSrc

is null.

---

### Method Details

#### public
String
getDigestAlgorithm()

Returns the message digest algorithm name.

**Returns:**
- the message digest algorithm name.

---

#### public
String
getMGFAlgorithm()

Returns the mask generation function algorithm name.

**Returns:**
- the mask generation function algorithm name.

---

#### public
AlgorithmParameterSpec
getMGFParameters()

Returns the parameters for the mask generation function.

**Returns:**
- the parameters for the mask generation function.

---

#### public
PSource
getPSource()

Returns the source of encoding input P.

**Returns:**
- the source of encoding input P.

---

### Additional Sections

#### Class OAEPParameterSpec

java.lang.Object

- javax.crypto.spec.OAEPParameterSpec

javax.crypto.spec.OAEPParameterSpec

**All Implemented Interfaces:** AlgorithmParameterSpec

```java
public class
OAEPParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This class specifies the set of parameters used with OAEP Padding,
as defined in the

PKCS#1 v2.2

standard.

Its ASN.1 definition in PKCS#1 standard is described below:

```java
RSAES-OAEP-params ::= SEQUENCE {
hashAlgorithm [0] HashAlgorithm DEFAULT sha1,
maskGenAlgorithm [1] MaskGenAlgorithm DEFAULT mgf1SHA1,
pSourceAlgorithm [2] PSourceAlgorithm DEFAULT pSpecifiedEmpty
}
```

where

```java
HashAlgorithm ::= AlgorithmIdentifier {
{OAEP-PSSDigestAlgorithms}
}
MaskGenAlgorithm ::= AlgorithmIdentifier { {PKCS1MGFAlgorithms} }
PSourceAlgorithm ::= AlgorithmIdentifier {
{PKCS1PSourceAlgorithms}
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
PKCS1MGFAlgorithms ALGORITHM-IDENTIFIER ::= {
{ OID id-mgf1 PARAMETERS HashAlgorithm },
... -- Allows for future expansion --
}
PKCS1PSourceAlgorithms ALGORITHM-IDENTIFIER ::= {
{ OID id-pSpecified PARAMETERS EncodingParameters },
... -- Allows for future expansion --
}
EncodingParameters ::= OCTET STRING(SIZE(0..MAX))
```

Note: the OAEPParameterSpec.DEFAULT uses the following:

```java
message digest -- "SHA-1"
mask generation function (mgf) -- "MGF1"
parameters for mgf -- MGF1ParameterSpec.SHA1
source of encoding input -- PSource.PSpecified.DEFAULT
```

**Since:** 1.5
**See Also:** MGF1ParameterSpec

,

PSource

public class

OAEPParameterSpec

extends

Object

implements

AlgorithmParameterSpec

This class specifies the set of parameters used with OAEP Padding,
as defined in the

PKCS#1 v2.2

standard.

Its ASN.1 definition in PKCS#1 standard is described below:

```java
RSAES-OAEP-params ::= SEQUENCE {
hashAlgorithm [0] HashAlgorithm DEFAULT sha1,
maskGenAlgorithm [1] MaskGenAlgorithm DEFAULT mgf1SHA1,
pSourceAlgorithm [2] PSourceAlgorithm DEFAULT pSpecifiedEmpty
}
```

where

```java
HashAlgorithm ::= AlgorithmIdentifier {
{OAEP-PSSDigestAlgorithms}
}
MaskGenAlgorithm ::= AlgorithmIdentifier { {PKCS1MGFAlgorithms} }
PSourceAlgorithm ::= AlgorithmIdentifier {
{PKCS1PSourceAlgorithms}
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
PKCS1MGFAlgorithms ALGORITHM-IDENTIFIER ::= {
{ OID id-mgf1 PARAMETERS HashAlgorithm },
... -- Allows for future expansion --
}
PKCS1PSourceAlgorithms ALGORITHM-IDENTIFIER ::= {
{ OID id-pSpecified PARAMETERS EncodingParameters },
... -- Allows for future expansion --
}
EncodingParameters ::= OCTET STRING(SIZE(0..MAX))
```

Note: the OAEPParameterSpec.DEFAULT uses the following:

```java
message digest -- "SHA-1"
mask generation function (mgf) -- "MGF1"
parameters for mgf -- MGF1ParameterSpec.SHA1
source of encoding input -- PSource.PSpecified.DEFAULT
```

RSAES-OAEP-params ::= SEQUENCE {
hashAlgorithm [0] HashAlgorithm DEFAULT sha1,
maskGenAlgorithm [1] MaskGenAlgorithm DEFAULT mgf1SHA1,
pSourceAlgorithm [2] PSourceAlgorithm DEFAULT pSpecifiedEmpty
}

HashAlgorithm ::= AlgorithmIdentifier {
{OAEP-PSSDigestAlgorithms}
}
MaskGenAlgorithm ::= AlgorithmIdentifier { {PKCS1MGFAlgorithms} }
PSourceAlgorithm ::= AlgorithmIdentifier {
{PKCS1PSourceAlgorithms}
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
PKCS1MGFAlgorithms ALGORITHM-IDENTIFIER ::= {
{ OID id-mgf1 PARAMETERS HashAlgorithm },
... -- Allows for future expansion --
}
PKCS1PSourceAlgorithms ALGORITHM-IDENTIFIER ::= {
{ OID id-pSpecified PARAMETERS EncodingParameters },
... -- Allows for future expansion --
}
EncodingParameters ::= OCTET STRING(SIZE(0..MAX))

Note: the OAEPParameterSpec.DEFAULT uses the following:

```java
message digest -- "SHA-1"
mask generation function (mgf) -- "MGF1"
parameters for mgf -- MGF1ParameterSpec.SHA1
source of encoding input -- PSource.PSpecified.DEFAULT
```

message digest -- "SHA-1"
mask generation function (mgf) -- "MGF1"
parameters for mgf -- MGF1ParameterSpec.SHA1
source of encoding input -- PSource.PSpecified.DEFAULT

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

OAEPParameterSpec

DEFAULT

The OAEP parameter set with all default values.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

OAEPParameterSpec

​(

String

mdName,

String

mgfName,

AlgorithmParameterSpec

mgfSpec,

PSource

pSrc)

Constructs a parameter set for OAEP padding as defined in
the PKCS #1 standard using the specified message digest
algorithm

mdName

, mask generation function
algorithm

mgfName

, parameters for the mask
generation function

mgfSpec

, and source of
the encoding input P

pSrc

.

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

Returns the message digest algorithm name.

String

getMGFAlgorithm

()

Returns the mask generation function algorithm name.

AlgorithmParameterSpec

getMGFParameters

()

Returns the parameters for the mask generation function.

PSource

getPSource

()

Returns the source of encoding input P.

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

OAEPParameterSpec

DEFAULT

The OAEP parameter set with all default values.

---

#### Field Summary

The OAEP parameter set with all default values.

Constructor Summary

Constructors

Constructor

Description

OAEPParameterSpec

​(

String

mdName,

String

mgfName,

AlgorithmParameterSpec

mgfSpec,

PSource

pSrc)

Constructs a parameter set for OAEP padding as defined in
the PKCS #1 standard using the specified message digest
algorithm

mdName

, mask generation function
algorithm

mgfName

, parameters for the mask
generation function

mgfSpec

, and source of
the encoding input P

pSrc

.

---

#### Constructor Summary

Constructs a parameter set for OAEP padding as defined in
the PKCS #1 standard using the specified message digest
algorithm

mdName

, mask generation function
algorithm

mgfName

, parameters for the mask
generation function

mgfSpec

, and source of
the encoding input P

pSrc

.

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

Returns the message digest algorithm name.

String

getMGFAlgorithm

()

Returns the mask generation function algorithm name.

AlgorithmParameterSpec

getMGFParameters

()

Returns the parameters for the mask generation function.

PSource

getPSource

()

Returns the source of encoding input P.

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

Returns the message digest algorithm name.

Returns the mask generation function algorithm name.

Returns the parameters for the mask generation function.

Returns the source of encoding input P.

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

- DEFAULT

```java
public static final
OAEPParameterSpec
DEFAULT
```

The OAEP parameter set with all default values.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- OAEPParameterSpec

```java
public OAEPParameterSpec​(
String
mdName,

String
mgfName,

AlgorithmParameterSpec
mgfSpec,

PSource
pSrc)
```

Constructs a parameter set for OAEP padding as defined in
the PKCS #1 standard using the specified message digest
algorithm

mdName

, mask generation function
algorithm

mgfName

, parameters for the mask
generation function

mgfSpec

, and source of
the encoding input P

pSrc

.

**Parameters:** mdName

- the algorithm name for the message digest.
**Parameters:** mgfName

- the algorithm name for the mask generation
function.
**Parameters:** mgfSpec

- the parameters for the mask generation function.
If null is specified, null will be returned by getMGFParameters().
**Parameters:** pSrc

- the source of the encoding input P.
**Throws:** NullPointerException

- if

mdName

,

mgfName

, or

pSrc

is null.

============ METHOD DETAIL ==========

- Method Detail

- getDigestAlgorithm

```java
public
String
getDigestAlgorithm()
```

Returns the message digest algorithm name.

**Returns:** the message digest algorithm name.

- getMGFAlgorithm

```java
public
String
getMGFAlgorithm()
```

Returns the mask generation function algorithm name.

**Returns:** the mask generation function algorithm name.

- getMGFParameters

```java
public
AlgorithmParameterSpec
getMGFParameters()
```

Returns the parameters for the mask generation function.

**Returns:** the parameters for the mask generation function.

- getPSource

```java
public
PSource
getPSource()
```

Returns the source of encoding input P.

**Returns:** the source of encoding input P.

Field Detail

- DEFAULT

```java
public static final
OAEPParameterSpec
DEFAULT
```

The OAEP parameter set with all default values.

---

#### Field Detail

DEFAULT

```java
public static final
OAEPParameterSpec
DEFAULT
```

The OAEP parameter set with all default values.

---

#### DEFAULT

public static final

OAEPParameterSpec

DEFAULT

The OAEP parameter set with all default values.

Constructor Detail

- OAEPParameterSpec

```java
public OAEPParameterSpec​(
String
mdName,

String
mgfName,

AlgorithmParameterSpec
mgfSpec,

PSource
pSrc)
```

Constructs a parameter set for OAEP padding as defined in
the PKCS #1 standard using the specified message digest
algorithm

mdName

, mask generation function
algorithm

mgfName

, parameters for the mask
generation function

mgfSpec

, and source of
the encoding input P

pSrc

.

**Parameters:** mdName

- the algorithm name for the message digest.
**Parameters:** mgfName

- the algorithm name for the mask generation
function.
**Parameters:** mgfSpec

- the parameters for the mask generation function.
If null is specified, null will be returned by getMGFParameters().
**Parameters:** pSrc

- the source of the encoding input P.
**Throws:** NullPointerException

- if

mdName

,

mgfName

, or

pSrc

is null.

---

#### Constructor Detail

OAEPParameterSpec

```java
public OAEPParameterSpec​(
String
mdName,

String
mgfName,

AlgorithmParameterSpec
mgfSpec,

PSource
pSrc)
```

Constructs a parameter set for OAEP padding as defined in
the PKCS #1 standard using the specified message digest
algorithm

mdName

, mask generation function
algorithm

mgfName

, parameters for the mask
generation function

mgfSpec

, and source of
the encoding input P

pSrc

.

**Parameters:** mdName

- the algorithm name for the message digest.
**Parameters:** mgfName

- the algorithm name for the mask generation
function.
**Parameters:** mgfSpec

- the parameters for the mask generation function.
If null is specified, null will be returned by getMGFParameters().
**Parameters:** pSrc

- the source of the encoding input P.
**Throws:** NullPointerException

- if

mdName

,

mgfName

, or

pSrc

is null.

---

#### OAEPParameterSpec

public OAEPParameterSpec​(

String

mdName,

String

mgfName,

AlgorithmParameterSpec

mgfSpec,

PSource

pSrc)

Constructs a parameter set for OAEP padding as defined in
the PKCS #1 standard using the specified message digest
algorithm

mdName

, mask generation function
algorithm

mgfName

, parameters for the mask
generation function

mgfSpec

, and source of
the encoding input P

pSrc

.

Method Detail

- getDigestAlgorithm

```java
public
String
getDigestAlgorithm()
```

Returns the message digest algorithm name.

**Returns:** the message digest algorithm name.

- getMGFAlgorithm

```java
public
String
getMGFAlgorithm()
```

Returns the mask generation function algorithm name.

**Returns:** the mask generation function algorithm name.

- getMGFParameters

```java
public
AlgorithmParameterSpec
getMGFParameters()
```

Returns the parameters for the mask generation function.

**Returns:** the parameters for the mask generation function.

- getPSource

```java
public
PSource
getPSource()
```

Returns the source of encoding input P.

**Returns:** the source of encoding input P.

---

#### Method Detail

getDigestAlgorithm

```java
public
String
getDigestAlgorithm()
```

Returns the message digest algorithm name.

**Returns:** the message digest algorithm name.

---

#### getDigestAlgorithm

public

String

getDigestAlgorithm()

Returns the message digest algorithm name.

getMGFAlgorithm

```java
public
String
getMGFAlgorithm()
```

Returns the mask generation function algorithm name.

**Returns:** the mask generation function algorithm name.

---

#### getMGFAlgorithm

public

String

getMGFAlgorithm()

Returns the mask generation function algorithm name.

getMGFParameters

```java
public
AlgorithmParameterSpec
getMGFParameters()
```

Returns the parameters for the mask generation function.

**Returns:** the parameters for the mask generation function.

---

#### getMGFParameters

public

AlgorithmParameterSpec

getMGFParameters()

Returns the parameters for the mask generation function.

getPSource

```java
public
PSource
getPSource()
```

Returns the source of encoding input P.

**Returns:** the source of encoding input P.

---

#### getPSource

public

PSource

getPSource()

Returns the source of encoding input P.

---

