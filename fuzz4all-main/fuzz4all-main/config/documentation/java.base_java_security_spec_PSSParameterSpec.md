# Class PSSParameterSpec

**Source:** `java.base\java\security\spec\PSSParameterSpec.html`

### Class Description

```java
public class
PSSParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This class specifies a parameter spec for RSASSA-PSS signature scheme,
as defined in the

PKCS#1 v2.2

standard.

Its ASN.1 definition in PKCS#1 standard is described below:

```java
RSASSA-PSS-params ::= SEQUENCE {
hashAlgorithm [0] HashAlgorithm DEFAULT sha1,
maskGenAlgorithm [1] MaskGenAlgorithm DEFAULT mgf1SHA1,
saltLength [2] INTEGER DEFAULT 20,
trailerField [3] TrailerField DEFAULT trailerFieldBC(1)
}
```

where

```java
HashAlgorithm ::= AlgorithmIdentifier {
{OAEP-PSSDigestAlgorithms}
}
MaskGenAlgorithm ::= AlgorithmIdentifier { {PKCS1MGFAlgorithms} }
TrailerField ::= INTEGER { trailerFieldBC(1) }

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
```

Note: the PSSParameterSpec.DEFAULT uses the following:
message digest -- "SHA-1"
mask generation function (mgf) -- "MGF1"
parameters for mgf -- MGF1ParameterSpec.SHA1
SaltLength -- 20
TrailerField -- 1

**All Implemented Interfaces:** AlgorithmParameterSpec

---

### Field Details

#### public static final int TRAILER_FIELD_BC

The

TrailerFieldBC

constant as defined in PKCS#1

**See Also:**
- Constant Field Values

**Since:**
- 11

---

#### public static final
PSSParameterSpec
DEFAULT

The PSS parameter set with all default values

**Since:**
- 1.5

---

### Constructor Details

#### public PSSParameterSpec​(
String
mdName,

String
mgfName,

AlgorithmParameterSpec
mgfSpec,
int saltLen,
int trailerField)

Creates a new

PSSParameterSpec

as defined in
the PKCS #1 standard using the specified message digest,
mask generation function, parameters for mask generation
function, salt length, and trailer field values.

**Parameters:**
- mdName

- the algorithm name of the hash function
- mgfName

- the algorithm name of the mask generation function
- mgfSpec

- the parameters for the mask generation function.
If null is specified, null will be returned by
getMGFParameters().
- saltLen

- the length of salt
- trailerField

- the value of the trailer field

**Throws:**
- NullPointerException

- if

mdName

, or

mgfName

is null
- IllegalArgumentException

- if

saltLen

or

trailerField

is less than 0

**Since:**
- 1.5

---

#### public PSSParameterSpec​(int saltLen)

Creates a new

PSSParameterSpec

using the specified salt length and other default values as
defined in PKCS#1.

**Parameters:**
- saltLen

- the length of salt in bytes to be used in PKCS#1
PSS encoding

**Throws:**
- IllegalArgumentException

- if

saltLen

is
less than 0

---

### Method Details

#### public
String
getDigestAlgorithm()

Returns the message digest algorithm name.

**Returns:**
- the message digest algorithm name

**Since:**
- 1.5

---

#### public
String
getMGFAlgorithm()

Returns the mask generation function algorithm name.

**Returns:**
- the mask generation function algorithm name

**Since:**
- 1.5

---

#### public
AlgorithmParameterSpec
getMGFParameters()

Returns the parameters for the mask generation function.

**Returns:**
- the parameters for the mask generation function

**Since:**
- 1.5

---

#### public int getSaltLength()

Returns the salt length in bytes.

**Returns:**
- the salt length

---

#### public int getTrailerField()

Returns the value for the trailer field.

**Returns:**
- the value for the trailer field

**Since:**
- 1.5

---

### Additional Sections

#### Class PSSParameterSpec

java.lang.Object

- java.security.spec.PSSParameterSpec

java.security.spec.PSSParameterSpec

**All Implemented Interfaces:** AlgorithmParameterSpec

```java
public class
PSSParameterSpec

extends
Object

implements
AlgorithmParameterSpec
```

This class specifies a parameter spec for RSASSA-PSS signature scheme,
as defined in the

PKCS#1 v2.2

standard.

Its ASN.1 definition in PKCS#1 standard is described below:

```java
RSASSA-PSS-params ::= SEQUENCE {
hashAlgorithm [0] HashAlgorithm DEFAULT sha1,
maskGenAlgorithm [1] MaskGenAlgorithm DEFAULT mgf1SHA1,
saltLength [2] INTEGER DEFAULT 20,
trailerField [3] TrailerField DEFAULT trailerFieldBC(1)
}
```

where

```java
HashAlgorithm ::= AlgorithmIdentifier {
{OAEP-PSSDigestAlgorithms}
}
MaskGenAlgorithm ::= AlgorithmIdentifier { {PKCS1MGFAlgorithms} }
TrailerField ::= INTEGER { trailerFieldBC(1) }

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
```

Note: the PSSParameterSpec.DEFAULT uses the following:
message digest -- "SHA-1"
mask generation function (mgf) -- "MGF1"
parameters for mgf -- MGF1ParameterSpec.SHA1
SaltLength -- 20
TrailerField -- 1

**Since:** 1.4
**See Also:** MGF1ParameterSpec

,

AlgorithmParameterSpec

,

Signature

public class

PSSParameterSpec

extends

Object

implements

AlgorithmParameterSpec

This class specifies a parameter spec for RSASSA-PSS signature scheme,
as defined in the

PKCS#1 v2.2

standard.

Its ASN.1 definition in PKCS#1 standard is described below:

```java
RSASSA-PSS-params ::= SEQUENCE {
hashAlgorithm [0] HashAlgorithm DEFAULT sha1,
maskGenAlgorithm [1] MaskGenAlgorithm DEFAULT mgf1SHA1,
saltLength [2] INTEGER DEFAULT 20,
trailerField [3] TrailerField DEFAULT trailerFieldBC(1)
}
```

where

```java
HashAlgorithm ::= AlgorithmIdentifier {
{OAEP-PSSDigestAlgorithms}
}
MaskGenAlgorithm ::= AlgorithmIdentifier { {PKCS1MGFAlgorithms} }
TrailerField ::= INTEGER { trailerFieldBC(1) }

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
```

Note: the PSSParameterSpec.DEFAULT uses the following:
message digest -- "SHA-1"
mask generation function (mgf) -- "MGF1"
parameters for mgf -- MGF1ParameterSpec.SHA1
SaltLength -- 20
TrailerField -- 1

Its ASN.1 definition in PKCS#1 standard is described below:

```java
RSASSA-PSS-params ::= SEQUENCE {
hashAlgorithm [0] HashAlgorithm DEFAULT sha1,
maskGenAlgorithm [1] MaskGenAlgorithm DEFAULT mgf1SHA1,
saltLength [2] INTEGER DEFAULT 20,
trailerField [3] TrailerField DEFAULT trailerFieldBC(1)
}
```

where

```java
HashAlgorithm ::= AlgorithmIdentifier {
{OAEP-PSSDigestAlgorithms}
}
MaskGenAlgorithm ::= AlgorithmIdentifier { {PKCS1MGFAlgorithms} }
TrailerField ::= INTEGER { trailerFieldBC(1) }

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
```

Note: the PSSParameterSpec.DEFAULT uses the following:
message digest -- "SHA-1"
mask generation function (mgf) -- "MGF1"
parameters for mgf -- MGF1ParameterSpec.SHA1
SaltLength -- 20
TrailerField -- 1

RSASSA-PSS-params ::= SEQUENCE {
hashAlgorithm [0] HashAlgorithm DEFAULT sha1,
maskGenAlgorithm [1] MaskGenAlgorithm DEFAULT mgf1SHA1,
saltLength [2] INTEGER DEFAULT 20,
trailerField [3] TrailerField DEFAULT trailerFieldBC(1)
}

HashAlgorithm ::= AlgorithmIdentifier {
{OAEP-PSSDigestAlgorithms}
}
MaskGenAlgorithm ::= AlgorithmIdentifier { {PKCS1MGFAlgorithms} }
TrailerField ::= INTEGER { trailerFieldBC(1) }

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

Note: the PSSParameterSpec.DEFAULT uses the following:
message digest -- "SHA-1"
mask generation function (mgf) -- "MGF1"
parameters for mgf -- MGF1ParameterSpec.SHA1
SaltLength -- 20
TrailerField -- 1

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

PSSParameterSpec

DEFAULT

The PSS parameter set with all default values

static int

TRAILER_FIELD_BC

The

TrailerFieldBC

constant as defined in PKCS#1

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

PSSParameterSpec

​(int saltLen)

Creates a new

PSSParameterSpec

using the specified salt length and other default values as
defined in PKCS#1.

PSSParameterSpec

​(

String

mdName,

String

mgfName,

AlgorithmParameterSpec

mgfSpec,
int saltLen,
int trailerField)

Creates a new

PSSParameterSpec

as defined in
the PKCS #1 standard using the specified message digest,
mask generation function, parameters for mask generation
function, salt length, and trailer field values.

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

int

getSaltLength

()

Returns the salt length in bytes.

int

getTrailerField

()

Returns the value for the trailer field.

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

PSSParameterSpec

DEFAULT

The PSS parameter set with all default values

static int

TRAILER_FIELD_BC

The

TrailerFieldBC

constant as defined in PKCS#1

---

#### Field Summary

The PSS parameter set with all default values

The

TrailerFieldBC

constant as defined in PKCS#1

Constructor Summary

Constructors

Constructor

Description

PSSParameterSpec

​(int saltLen)

Creates a new

PSSParameterSpec

using the specified salt length and other default values as
defined in PKCS#1.

PSSParameterSpec

​(

String

mdName,

String

mgfName,

AlgorithmParameterSpec

mgfSpec,
int saltLen,
int trailerField)

Creates a new

PSSParameterSpec

as defined in
the PKCS #1 standard using the specified message digest,
mask generation function, parameters for mask generation
function, salt length, and trailer field values.

---

#### Constructor Summary

Creates a new

PSSParameterSpec

using the specified salt length and other default values as
defined in PKCS#1.

Creates a new

PSSParameterSpec

as defined in
the PKCS #1 standard using the specified message digest,
mask generation function, parameters for mask generation
function, salt length, and trailer field values.

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

int

getSaltLength

()

Returns the salt length in bytes.

int

getTrailerField

()

Returns the value for the trailer field.

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

Returns the salt length in bytes.

Returns the value for the trailer field.

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

- TRAILER_FIELD_BC

```java
public static final int TRAILER_FIELD_BC
```

The

TrailerFieldBC

constant as defined in PKCS#1

**Since:** 11
**See Also:** Constant Field Values

- DEFAULT

```java
public static final
PSSParameterSpec
DEFAULT
```

The PSS parameter set with all default values

**Since:** 1.5

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- PSSParameterSpec

```java
public PSSParameterSpec​(
String
mdName,

String
mgfName,

AlgorithmParameterSpec
mgfSpec,
int saltLen,
int trailerField)
```

Creates a new

PSSParameterSpec

as defined in
the PKCS #1 standard using the specified message digest,
mask generation function, parameters for mask generation
function, salt length, and trailer field values.

**Parameters:** mdName

- the algorithm name of the hash function
**Parameters:** mgfName

- the algorithm name of the mask generation function
**Parameters:** mgfSpec

- the parameters for the mask generation function.
If null is specified, null will be returned by
getMGFParameters().
**Parameters:** saltLen

- the length of salt
**Parameters:** trailerField

- the value of the trailer field
**Throws:** NullPointerException

- if

mdName

, or

mgfName

is null
**Throws:** IllegalArgumentException

- if

saltLen

or

trailerField

is less than 0
**Since:** 1.5

- PSSParameterSpec

```java
public PSSParameterSpec​(int saltLen)
```

Creates a new

PSSParameterSpec

using the specified salt length and other default values as
defined in PKCS#1.

**Parameters:** saltLen

- the length of salt in bytes to be used in PKCS#1
PSS encoding
**Throws:** IllegalArgumentException

- if

saltLen

is
less than 0

============ METHOD DETAIL ==========

- Method Detail

- getDigestAlgorithm

```java
public
String
getDigestAlgorithm()
```

Returns the message digest algorithm name.

**Returns:** the message digest algorithm name
**Since:** 1.5

- getMGFAlgorithm

```java
public
String
getMGFAlgorithm()
```

Returns the mask generation function algorithm name.

**Returns:** the mask generation function algorithm name
**Since:** 1.5

- getMGFParameters

```java
public
AlgorithmParameterSpec
getMGFParameters()
```

Returns the parameters for the mask generation function.

**Returns:** the parameters for the mask generation function
**Since:** 1.5

- getSaltLength

```java
public int getSaltLength()
```

Returns the salt length in bytes.

**Returns:** the salt length

- getTrailerField

```java
public int getTrailerField()
```

Returns the value for the trailer field.

**Returns:** the value for the trailer field
**Since:** 1.5

Field Detail

- TRAILER_FIELD_BC

```java
public static final int TRAILER_FIELD_BC
```

The

TrailerFieldBC

constant as defined in PKCS#1

**Since:** 11
**See Also:** Constant Field Values

- DEFAULT

```java
public static final
PSSParameterSpec
DEFAULT
```

The PSS parameter set with all default values

**Since:** 1.5

---

#### Field Detail

TRAILER_FIELD_BC

```java
public static final int TRAILER_FIELD_BC
```

The

TrailerFieldBC

constant as defined in PKCS#1

**Since:** 11
**See Also:** Constant Field Values

---

#### TRAILER_FIELD_BC

public static final int TRAILER_FIELD_BC

The

TrailerFieldBC

constant as defined in PKCS#1

DEFAULT

```java
public static final
PSSParameterSpec
DEFAULT
```

The PSS parameter set with all default values

**Since:** 1.5

---

#### DEFAULT

public static final

PSSParameterSpec

DEFAULT

The PSS parameter set with all default values

Constructor Detail

- PSSParameterSpec

```java
public PSSParameterSpec​(
String
mdName,

String
mgfName,

AlgorithmParameterSpec
mgfSpec,
int saltLen,
int trailerField)
```

Creates a new

PSSParameterSpec

as defined in
the PKCS #1 standard using the specified message digest,
mask generation function, parameters for mask generation
function, salt length, and trailer field values.

**Parameters:** mdName

- the algorithm name of the hash function
**Parameters:** mgfName

- the algorithm name of the mask generation function
**Parameters:** mgfSpec

- the parameters for the mask generation function.
If null is specified, null will be returned by
getMGFParameters().
**Parameters:** saltLen

- the length of salt
**Parameters:** trailerField

- the value of the trailer field
**Throws:** NullPointerException

- if

mdName

, or

mgfName

is null
**Throws:** IllegalArgumentException

- if

saltLen

or

trailerField

is less than 0
**Since:** 1.5

- PSSParameterSpec

```java
public PSSParameterSpec​(int saltLen)
```

Creates a new

PSSParameterSpec

using the specified salt length and other default values as
defined in PKCS#1.

**Parameters:** saltLen

- the length of salt in bytes to be used in PKCS#1
PSS encoding
**Throws:** IllegalArgumentException

- if

saltLen

is
less than 0

---

#### Constructor Detail

PSSParameterSpec

```java
public PSSParameterSpec​(
String
mdName,

String
mgfName,

AlgorithmParameterSpec
mgfSpec,
int saltLen,
int trailerField)
```

Creates a new

PSSParameterSpec

as defined in
the PKCS #1 standard using the specified message digest,
mask generation function, parameters for mask generation
function, salt length, and trailer field values.

**Parameters:** mdName

- the algorithm name of the hash function
**Parameters:** mgfName

- the algorithm name of the mask generation function
**Parameters:** mgfSpec

- the parameters for the mask generation function.
If null is specified, null will be returned by
getMGFParameters().
**Parameters:** saltLen

- the length of salt
**Parameters:** trailerField

- the value of the trailer field
**Throws:** NullPointerException

- if

mdName

, or

mgfName

is null
**Throws:** IllegalArgumentException

- if

saltLen

or

trailerField

is less than 0
**Since:** 1.5

---

#### PSSParameterSpec

public PSSParameterSpec​(

String

mdName,

String

mgfName,

AlgorithmParameterSpec

mgfSpec,
int saltLen,
int trailerField)

Creates a new

PSSParameterSpec

as defined in
the PKCS #1 standard using the specified message digest,
mask generation function, parameters for mask generation
function, salt length, and trailer field values.

PSSParameterSpec

```java
public PSSParameterSpec​(int saltLen)
```

Creates a new

PSSParameterSpec

using the specified salt length and other default values as
defined in PKCS#1.

**Parameters:** saltLen

- the length of salt in bytes to be used in PKCS#1
PSS encoding
**Throws:** IllegalArgumentException

- if

saltLen

is
less than 0

---

#### PSSParameterSpec

public PSSParameterSpec​(int saltLen)

Creates a new

PSSParameterSpec

using the specified salt length and other default values as
defined in PKCS#1.

Method Detail

- getDigestAlgorithm

```java
public
String
getDigestAlgorithm()
```

Returns the message digest algorithm name.

**Returns:** the message digest algorithm name
**Since:** 1.5

- getMGFAlgorithm

```java
public
String
getMGFAlgorithm()
```

Returns the mask generation function algorithm name.

**Returns:** the mask generation function algorithm name
**Since:** 1.5

- getMGFParameters

```java
public
AlgorithmParameterSpec
getMGFParameters()
```

Returns the parameters for the mask generation function.

**Returns:** the parameters for the mask generation function
**Since:** 1.5

- getSaltLength

```java
public int getSaltLength()
```

Returns the salt length in bytes.

**Returns:** the salt length

- getTrailerField

```java
public int getTrailerField()
```

Returns the value for the trailer field.

**Returns:** the value for the trailer field
**Since:** 1.5

---

#### Method Detail

getDigestAlgorithm

```java
public
String
getDigestAlgorithm()
```

Returns the message digest algorithm name.

**Returns:** the message digest algorithm name
**Since:** 1.5

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

**Returns:** the mask generation function algorithm name
**Since:** 1.5

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

**Returns:** the parameters for the mask generation function
**Since:** 1.5

---

#### getMGFParameters

public

AlgorithmParameterSpec

getMGFParameters()

Returns the parameters for the mask generation function.

getSaltLength

```java
public int getSaltLength()
```

Returns the salt length in bytes.

**Returns:** the salt length

---

#### getSaltLength

public int getSaltLength()

Returns the salt length in bytes.

getTrailerField

```java
public int getTrailerField()
```

Returns the value for the trailer field.

**Returns:** the value for the trailer field
**Since:** 1.5

---

#### getTrailerField

public int getTrailerField()

Returns the value for the trailer field.

---

