# Class EncryptedPrivateKeyInfo

**Source:** `java.base\javax\crypto\EncryptedPrivateKeyInfo.html`

### Class Description

```java
public class
EncryptedPrivateKeyInfo

extends
Object
```

This class implements the

EncryptedPrivateKeyInfo

type
as defined in PKCS #8.

Its ASN.1 definition is as follows:

```java
EncryptedPrivateKeyInfo ::= SEQUENCE {
encryptionAlgorithm AlgorithmIdentifier,
encryptedData OCTET STRING }

AlgorithmIdentifier ::= SEQUENCE {
algorithm OBJECT IDENTIFIER,
parameters ANY DEFINED BY algorithm OPTIONAL }
```

**Since:** 1.4
**See Also:** PKCS8EncodedKeySpec

---

### Field Details

*No entries found.*

### Constructor Details

#### public EncryptedPrivateKeyInfo​(byte[] encoded)
throws
IOException

Constructs (i.e., parses) an

EncryptedPrivateKeyInfo

from
its ASN.1 encoding.

**Parameters:**
- encoded

- the ASN.1 encoding of this object. The contents of
the array are copied to protect against subsequent modification.

**Throws:**
- NullPointerException

- if the

encoded

is null.
- IOException

- if error occurs when parsing the ASN.1 encoding.

---

#### public EncryptedPrivateKeyInfo​(
String
algName,
byte[] encryptedData)
throws
NoSuchAlgorithmException

Constructs an

EncryptedPrivateKeyInfo

from the
encryption algorithm name and the encrypted data.

Note: This constructor will use null as the value of the
algorithm parameters. If the encryption algorithm has
parameters whose value is not null, a different constructor,
e.g. EncryptedPrivateKeyInfo(AlgorithmParameters, byte[]),
should be used.

**Parameters:**
- algName

- encryption algorithm name. See the

Java Security Standard Algorithm Names

document
for information about standard Cipher algorithm names.
- encryptedData

- encrypted data. The contents of

encrypedData

are copied to protect against subsequent
modification when constructing this object.

**Throws:**
- NullPointerException

- if

algName

or

encryptedData

is null.
- IllegalArgumentException

- if

encryptedData

is empty, i.e. 0-length.
- NoSuchAlgorithmException

- if the specified algName is
not supported.

---

#### public EncryptedPrivateKeyInfo​(
AlgorithmParameters
algParams,
byte[] encryptedData)
throws
NoSuchAlgorithmException

Constructs an

EncryptedPrivateKeyInfo

from the
encryption algorithm parameters and the encrypted data.

**Parameters:**
- algParams

- the algorithm parameters for the encryption
algorithm.

algParams.getEncoded()

should return
the ASN.1 encoded bytes of the

parameters

field
of the

AlgorithmIdentifer

component of the

EncryptedPrivateKeyInfo

type.
- encryptedData

- encrypted data. The contents of

encrypedData

are copied to protect against
subsequent modification when constructing this object.

**Throws:**
- NullPointerException

- if

algParams

or

encryptedData

is null.
- IllegalArgumentException

- if

encryptedData

is empty, i.e. 0-length.
- NoSuchAlgorithmException

- if the specified algName of
the specified

algParams

parameter is not supported.

---

### Method Details

#### public
String
getAlgName()

Returns the encryption algorithm.

Note: Standard name is returned instead of the specified one
in the constructor when such mapping is available.
See the

Java Security Standard Algorithm Names

document
for information about standard Cipher algorithm names.

**Returns:**
- the encryption algorithm name.

---

#### public
AlgorithmParameters
getAlgParameters()

Returns the algorithm parameters used by the encryption algorithm.

**Returns:**
- the algorithm parameters.

---

#### public byte[] getEncryptedData()

Returns the encrypted data.

**Returns:**
- the encrypted data. Returns a new array
each time this method is called.

---

#### public
PKCS8EncodedKeySpec
getKeySpec​(
Cipher
cipher)
throws
InvalidKeySpecException

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

Note: In order to successfully retrieve the enclosed
PKCS8EncodedKeySpec object,

cipher

needs
to be initialized to either Cipher.DECRYPT_MODE or
Cipher.UNWRAP_MODE, with the same key and parameters used
for generating the encrypted data.

**Parameters:**
- cipher

- the initialized cipher object which will be
used for decrypting the encrypted data.

**Returns:**
- the PKCS8EncodedKeySpec object.

**Throws:**
- NullPointerException

- if

cipher

is null.
- InvalidKeySpecException

- if the given cipher is
inappropriate for the encrypted data or the encrypted
data is corrupted and cannot be decrypted.

---

#### public
PKCS8EncodedKeySpec
getKeySpec​(
Key
decryptKey)
throws
NoSuchAlgorithmException
,

InvalidKeyException

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

**Parameters:**
- decryptKey

- key used for decrypting the encrypted data.

**Returns:**
- the PKCS8EncodedKeySpec object.

**Throws:**
- NullPointerException

- if

decryptKey

is null.
- NoSuchAlgorithmException

- if cannot find appropriate
cipher to decrypt the encrypted data.
- InvalidKeyException

- if

decryptKey

cannot be used to decrypt the encrypted data or the decryption
result is not a valid PKCS8KeySpec.

**Since:**
- 1.5

---

#### public
PKCS8EncodedKeySpec
getKeySpec​(
Key
decryptKey,

String
providerName)
throws
NoSuchProviderException
,

NoSuchAlgorithmException
,

InvalidKeyException

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

**Parameters:**
- decryptKey

- key used for decrypting the encrypted data.
- providerName

- the name of provider whose Cipher
implementation will be used.

**Returns:**
- the PKCS8EncodedKeySpec object.

**Throws:**
- NullPointerException

- if

decryptKey

or

providerName

is null.
- NoSuchProviderException

- if no provider

providerName

is registered.
- NoSuchAlgorithmException

- if cannot find appropriate
cipher to decrypt the encrypted data.
- InvalidKeyException

- if

decryptKey

cannot be used to decrypt the encrypted data or the decryption
result is not a valid PKCS8KeySpec.

**Since:**
- 1.5

---

#### public
PKCS8EncodedKeySpec
getKeySpec​(
Key
decryptKey,

Provider
provider)
throws
NoSuchAlgorithmException
,

InvalidKeyException

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

**Parameters:**
- decryptKey

- key used for decrypting the encrypted data.
- provider

- the name of provider whose Cipher implementation
will be used.

**Returns:**
- the PKCS8EncodedKeySpec object.

**Throws:**
- NullPointerException

- if

decryptKey

or

provider

is null.
- NoSuchAlgorithmException

- if cannot find appropriate
cipher to decrypt the encrypted data in

provider

.
- InvalidKeyException

- if

decryptKey

cannot be used to decrypt the encrypted data or the decryption
result is not a valid PKCS8KeySpec.

**Since:**
- 1.5

---

#### public byte[] getEncoded()
throws
IOException

Returns the ASN.1 encoding of this object.

**Returns:**
- the ASN.1 encoding. Returns a new array
each time this method is called.

**Throws:**
- IOException

- if error occurs when constructing its
ASN.1 encoding.

---

### Additional Sections

#### Class EncryptedPrivateKeyInfo

java.lang.Object

- javax.crypto.EncryptedPrivateKeyInfo

javax.crypto.EncryptedPrivateKeyInfo

```java
public class
EncryptedPrivateKeyInfo

extends
Object
```

This class implements the

EncryptedPrivateKeyInfo

type
as defined in PKCS #8.

Its ASN.1 definition is as follows:

```java
EncryptedPrivateKeyInfo ::= SEQUENCE {
encryptionAlgorithm AlgorithmIdentifier,
encryptedData OCTET STRING }

AlgorithmIdentifier ::= SEQUENCE {
algorithm OBJECT IDENTIFIER,
parameters ANY DEFINED BY algorithm OPTIONAL }
```

**Since:** 1.4
**See Also:** PKCS8EncodedKeySpec

public class

EncryptedPrivateKeyInfo

extends

Object

This class implements the

EncryptedPrivateKeyInfo

type
as defined in PKCS #8.

Its ASN.1 definition is as follows:

```java
EncryptedPrivateKeyInfo ::= SEQUENCE {
encryptionAlgorithm AlgorithmIdentifier,
encryptedData OCTET STRING }

AlgorithmIdentifier ::= SEQUENCE {
algorithm OBJECT IDENTIFIER,
parameters ANY DEFINED BY algorithm OPTIONAL }
```

Its ASN.1 definition is as follows:

```java
EncryptedPrivateKeyInfo ::= SEQUENCE {
encryptionAlgorithm AlgorithmIdentifier,
encryptedData OCTET STRING }

AlgorithmIdentifier ::= SEQUENCE {
algorithm OBJECT IDENTIFIER,
parameters ANY DEFINED BY algorithm OPTIONAL }
```

EncryptedPrivateKeyInfo ::= SEQUENCE {
encryptionAlgorithm AlgorithmIdentifier,
encryptedData OCTET STRING }

AlgorithmIdentifier ::= SEQUENCE {
algorithm OBJECT IDENTIFIER,
parameters ANY DEFINED BY algorithm OPTIONAL }

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

EncryptedPrivateKeyInfo

​(byte[] encoded)

Constructs (i.e., parses) an

EncryptedPrivateKeyInfo

from
its ASN.1 encoding.

EncryptedPrivateKeyInfo

​(

String

algName,
byte[] encryptedData)

Constructs an

EncryptedPrivateKeyInfo

from the
encryption algorithm name and the encrypted data.

EncryptedPrivateKeyInfo

​(

AlgorithmParameters

algParams,
byte[] encryptedData)

Constructs an

EncryptedPrivateKeyInfo

from the
encryption algorithm parameters and the encrypted data.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getAlgName

()

Returns the encryption algorithm.

AlgorithmParameters

getAlgParameters

()

Returns the algorithm parameters used by the encryption algorithm.

byte[]

getEncoded

()

Returns the ASN.1 encoding of this object.

byte[]

getEncryptedData

()

Returns the encrypted data.

PKCS8EncodedKeySpec

getKeySpec

​(

Key

decryptKey)

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

PKCS8EncodedKeySpec

getKeySpec

​(

Key

decryptKey,

String

providerName)

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

PKCS8EncodedKeySpec

getKeySpec

​(

Key

decryptKey,

Provider

provider)

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

PKCS8EncodedKeySpec

getKeySpec

​(

Cipher

cipher)

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

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

EncryptedPrivateKeyInfo

​(byte[] encoded)

Constructs (i.e., parses) an

EncryptedPrivateKeyInfo

from
its ASN.1 encoding.

EncryptedPrivateKeyInfo

​(

String

algName,
byte[] encryptedData)

Constructs an

EncryptedPrivateKeyInfo

from the
encryption algorithm name and the encrypted data.

EncryptedPrivateKeyInfo

​(

AlgorithmParameters

algParams,
byte[] encryptedData)

Constructs an

EncryptedPrivateKeyInfo

from the
encryption algorithm parameters and the encrypted data.

---

#### Constructor Summary

Constructs (i.e., parses) an

EncryptedPrivateKeyInfo

from
its ASN.1 encoding.

Constructs an

EncryptedPrivateKeyInfo

from the
encryption algorithm name and the encrypted data.

Constructs an

EncryptedPrivateKeyInfo

from the
encryption algorithm parameters and the encrypted data.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getAlgName

()

Returns the encryption algorithm.

AlgorithmParameters

getAlgParameters

()

Returns the algorithm parameters used by the encryption algorithm.

byte[]

getEncoded

()

Returns the ASN.1 encoding of this object.

byte[]

getEncryptedData

()

Returns the encrypted data.

PKCS8EncodedKeySpec

getKeySpec

​(

Key

decryptKey)

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

PKCS8EncodedKeySpec

getKeySpec

​(

Key

decryptKey,

String

providerName)

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

PKCS8EncodedKeySpec

getKeySpec

​(

Key

decryptKey,

Provider

provider)

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

PKCS8EncodedKeySpec

getKeySpec

​(

Cipher

cipher)

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

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

Returns the encryption algorithm.

Returns the algorithm parameters used by the encryption algorithm.

Returns the ASN.1 encoding of this object.

Returns the encrypted data.

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

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

- EncryptedPrivateKeyInfo

```java
public EncryptedPrivateKeyInfo​(byte[] encoded)
throws
IOException
```

Constructs (i.e., parses) an

EncryptedPrivateKeyInfo

from
its ASN.1 encoding.

**Parameters:** encoded

- the ASN.1 encoding of this object. The contents of
the array are copied to protect against subsequent modification.
**Throws:** NullPointerException

- if the

encoded

is null.
**Throws:** IOException

- if error occurs when parsing the ASN.1 encoding.

- EncryptedPrivateKeyInfo

```java
public EncryptedPrivateKeyInfo​(
String
algName,
byte[] encryptedData)
throws
NoSuchAlgorithmException
```

Constructs an

EncryptedPrivateKeyInfo

from the
encryption algorithm name and the encrypted data.

Note: This constructor will use null as the value of the
algorithm parameters. If the encryption algorithm has
parameters whose value is not null, a different constructor,
e.g. EncryptedPrivateKeyInfo(AlgorithmParameters, byte[]),
should be used.

**Parameters:** algName

- encryption algorithm name. See the

Java Security Standard Algorithm Names

document
for information about standard Cipher algorithm names.
**Parameters:** encryptedData

- encrypted data. The contents of

encrypedData

are copied to protect against subsequent
modification when constructing this object.
**Throws:** NullPointerException

- if

algName

or

encryptedData

is null.
**Throws:** IllegalArgumentException

- if

encryptedData

is empty, i.e. 0-length.
**Throws:** NoSuchAlgorithmException

- if the specified algName is
not supported.

- EncryptedPrivateKeyInfo

```java
public EncryptedPrivateKeyInfo​(
AlgorithmParameters
algParams,
byte[] encryptedData)
throws
NoSuchAlgorithmException
```

Constructs an

EncryptedPrivateKeyInfo

from the
encryption algorithm parameters and the encrypted data.

**Parameters:** algParams

- the algorithm parameters for the encryption
algorithm.

algParams.getEncoded()

should return
the ASN.1 encoded bytes of the

parameters

field
of the

AlgorithmIdentifer

component of the

EncryptedPrivateKeyInfo

type.
**Parameters:** encryptedData

- encrypted data. The contents of

encrypedData

are copied to protect against
subsequent modification when constructing this object.
**Throws:** NullPointerException

- if

algParams

or

encryptedData

is null.
**Throws:** IllegalArgumentException

- if

encryptedData

is empty, i.e. 0-length.
**Throws:** NoSuchAlgorithmException

- if the specified algName of
the specified

algParams

parameter is not supported.

============ METHOD DETAIL ==========

- Method Detail

- getAlgName

```java
public
String
getAlgName()
```

Returns the encryption algorithm.

Note: Standard name is returned instead of the specified one
in the constructor when such mapping is available.
See the

Java Security Standard Algorithm Names

document
for information about standard Cipher algorithm names.

**Returns:** the encryption algorithm name.

- getAlgParameters

```java
public
AlgorithmParameters
getAlgParameters()
```

Returns the algorithm parameters used by the encryption algorithm.

**Returns:** the algorithm parameters.

- getEncryptedData

```java
public byte[] getEncryptedData()
```

Returns the encrypted data.

**Returns:** the encrypted data. Returns a new array
each time this method is called.

- getKeySpec

```java
public
PKCS8EncodedKeySpec
getKeySpec​(
Cipher
cipher)
throws
InvalidKeySpecException
```

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

Note: In order to successfully retrieve the enclosed
PKCS8EncodedKeySpec object,

cipher

needs
to be initialized to either Cipher.DECRYPT_MODE or
Cipher.UNWRAP_MODE, with the same key and parameters used
for generating the encrypted data.

**Parameters:** cipher

- the initialized cipher object which will be
used for decrypting the encrypted data.
**Returns:** the PKCS8EncodedKeySpec object.
**Throws:** NullPointerException

- if

cipher

is null.
**Throws:** InvalidKeySpecException

- if the given cipher is
inappropriate for the encrypted data or the encrypted
data is corrupted and cannot be decrypted.

- getKeySpec

```java
public
PKCS8EncodedKeySpec
getKeySpec​(
Key
decryptKey)
throws
NoSuchAlgorithmException
,

InvalidKeyException
```

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

**Parameters:** decryptKey

- key used for decrypting the encrypted data.
**Returns:** the PKCS8EncodedKeySpec object.
**Throws:** NullPointerException

- if

decryptKey

is null.
**Throws:** NoSuchAlgorithmException

- if cannot find appropriate
cipher to decrypt the encrypted data.
**Throws:** InvalidKeyException

- if

decryptKey

cannot be used to decrypt the encrypted data or the decryption
result is not a valid PKCS8KeySpec.
**Since:** 1.5

- getKeySpec

```java
public
PKCS8EncodedKeySpec
getKeySpec​(
Key
decryptKey,

String
providerName)
throws
NoSuchProviderException
,

NoSuchAlgorithmException
,

InvalidKeyException
```

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

**Parameters:** decryptKey

- key used for decrypting the encrypted data.
**Parameters:** providerName

- the name of provider whose Cipher
implementation will be used.
**Returns:** the PKCS8EncodedKeySpec object.
**Throws:** NullPointerException

- if

decryptKey

or

providerName

is null.
**Throws:** NoSuchProviderException

- if no provider

providerName

is registered.
**Throws:** NoSuchAlgorithmException

- if cannot find appropriate
cipher to decrypt the encrypted data.
**Throws:** InvalidKeyException

- if

decryptKey

cannot be used to decrypt the encrypted data or the decryption
result is not a valid PKCS8KeySpec.
**Since:** 1.5

- getKeySpec

```java
public
PKCS8EncodedKeySpec
getKeySpec​(
Key
decryptKey,

Provider
provider)
throws
NoSuchAlgorithmException
,

InvalidKeyException
```

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

**Parameters:** decryptKey

- key used for decrypting the encrypted data.
**Parameters:** provider

- the name of provider whose Cipher implementation
will be used.
**Returns:** the PKCS8EncodedKeySpec object.
**Throws:** NullPointerException

- if

decryptKey

or

provider

is null.
**Throws:** NoSuchAlgorithmException

- if cannot find appropriate
cipher to decrypt the encrypted data in

provider

.
**Throws:** InvalidKeyException

- if

decryptKey

cannot be used to decrypt the encrypted data or the decryption
result is not a valid PKCS8KeySpec.
**Since:** 1.5

- getEncoded

```java
public byte[] getEncoded()
throws
IOException
```

Returns the ASN.1 encoding of this object.

**Returns:** the ASN.1 encoding. Returns a new array
each time this method is called.
**Throws:** IOException

- if error occurs when constructing its
ASN.1 encoding.

Constructor Detail

- EncryptedPrivateKeyInfo

```java
public EncryptedPrivateKeyInfo​(byte[] encoded)
throws
IOException
```

Constructs (i.e., parses) an

EncryptedPrivateKeyInfo

from
its ASN.1 encoding.

**Parameters:** encoded

- the ASN.1 encoding of this object. The contents of
the array are copied to protect against subsequent modification.
**Throws:** NullPointerException

- if the

encoded

is null.
**Throws:** IOException

- if error occurs when parsing the ASN.1 encoding.

- EncryptedPrivateKeyInfo

```java
public EncryptedPrivateKeyInfo​(
String
algName,
byte[] encryptedData)
throws
NoSuchAlgorithmException
```

Constructs an

EncryptedPrivateKeyInfo

from the
encryption algorithm name and the encrypted data.

Note: This constructor will use null as the value of the
algorithm parameters. If the encryption algorithm has
parameters whose value is not null, a different constructor,
e.g. EncryptedPrivateKeyInfo(AlgorithmParameters, byte[]),
should be used.

**Parameters:** algName

- encryption algorithm name. See the

Java Security Standard Algorithm Names

document
for information about standard Cipher algorithm names.
**Parameters:** encryptedData

- encrypted data. The contents of

encrypedData

are copied to protect against subsequent
modification when constructing this object.
**Throws:** NullPointerException

- if

algName

or

encryptedData

is null.
**Throws:** IllegalArgumentException

- if

encryptedData

is empty, i.e. 0-length.
**Throws:** NoSuchAlgorithmException

- if the specified algName is
not supported.

- EncryptedPrivateKeyInfo

```java
public EncryptedPrivateKeyInfo​(
AlgorithmParameters
algParams,
byte[] encryptedData)
throws
NoSuchAlgorithmException
```

Constructs an

EncryptedPrivateKeyInfo

from the
encryption algorithm parameters and the encrypted data.

**Parameters:** algParams

- the algorithm parameters for the encryption
algorithm.

algParams.getEncoded()

should return
the ASN.1 encoded bytes of the

parameters

field
of the

AlgorithmIdentifer

component of the

EncryptedPrivateKeyInfo

type.
**Parameters:** encryptedData

- encrypted data. The contents of

encrypedData

are copied to protect against
subsequent modification when constructing this object.
**Throws:** NullPointerException

- if

algParams

or

encryptedData

is null.
**Throws:** IllegalArgumentException

- if

encryptedData

is empty, i.e. 0-length.
**Throws:** NoSuchAlgorithmException

- if the specified algName of
the specified

algParams

parameter is not supported.

---

#### Constructor Detail

EncryptedPrivateKeyInfo

```java
public EncryptedPrivateKeyInfo​(byte[] encoded)
throws
IOException
```

Constructs (i.e., parses) an

EncryptedPrivateKeyInfo

from
its ASN.1 encoding.

**Parameters:** encoded

- the ASN.1 encoding of this object. The contents of
the array are copied to protect against subsequent modification.
**Throws:** NullPointerException

- if the

encoded

is null.
**Throws:** IOException

- if error occurs when parsing the ASN.1 encoding.

---

#### EncryptedPrivateKeyInfo

public EncryptedPrivateKeyInfo​(byte[] encoded)
throws

IOException

Constructs (i.e., parses) an

EncryptedPrivateKeyInfo

from
its ASN.1 encoding.

EncryptedPrivateKeyInfo

```java
public EncryptedPrivateKeyInfo​(
String
algName,
byte[] encryptedData)
throws
NoSuchAlgorithmException
```

Constructs an

EncryptedPrivateKeyInfo

from the
encryption algorithm name and the encrypted data.

Note: This constructor will use null as the value of the
algorithm parameters. If the encryption algorithm has
parameters whose value is not null, a different constructor,
e.g. EncryptedPrivateKeyInfo(AlgorithmParameters, byte[]),
should be used.

**Parameters:** algName

- encryption algorithm name. See the

Java Security Standard Algorithm Names

document
for information about standard Cipher algorithm names.
**Parameters:** encryptedData

- encrypted data. The contents of

encrypedData

are copied to protect against subsequent
modification when constructing this object.
**Throws:** NullPointerException

- if

algName

or

encryptedData

is null.
**Throws:** IllegalArgumentException

- if

encryptedData

is empty, i.e. 0-length.
**Throws:** NoSuchAlgorithmException

- if the specified algName is
not supported.

---

#### EncryptedPrivateKeyInfo

public EncryptedPrivateKeyInfo​(

String

algName,
byte[] encryptedData)
throws

NoSuchAlgorithmException

Constructs an

EncryptedPrivateKeyInfo

from the
encryption algorithm name and the encrypted data.

Note: This constructor will use null as the value of the
algorithm parameters. If the encryption algorithm has
parameters whose value is not null, a different constructor,
e.g. EncryptedPrivateKeyInfo(AlgorithmParameters, byte[]),
should be used.

Note: This constructor will use null as the value of the
algorithm parameters. If the encryption algorithm has
parameters whose value is not null, a different constructor,
e.g. EncryptedPrivateKeyInfo(AlgorithmParameters, byte[]),
should be used.

EncryptedPrivateKeyInfo

```java
public EncryptedPrivateKeyInfo​(
AlgorithmParameters
algParams,
byte[] encryptedData)
throws
NoSuchAlgorithmException
```

Constructs an

EncryptedPrivateKeyInfo

from the
encryption algorithm parameters and the encrypted data.

**Parameters:** algParams

- the algorithm parameters for the encryption
algorithm.

algParams.getEncoded()

should return
the ASN.1 encoded bytes of the

parameters

field
of the

AlgorithmIdentifer

component of the

EncryptedPrivateKeyInfo

type.
**Parameters:** encryptedData

- encrypted data. The contents of

encrypedData

are copied to protect against
subsequent modification when constructing this object.
**Throws:** NullPointerException

- if

algParams

or

encryptedData

is null.
**Throws:** IllegalArgumentException

- if

encryptedData

is empty, i.e. 0-length.
**Throws:** NoSuchAlgorithmException

- if the specified algName of
the specified

algParams

parameter is not supported.

---

#### EncryptedPrivateKeyInfo

public EncryptedPrivateKeyInfo​(

AlgorithmParameters

algParams,
byte[] encryptedData)
throws

NoSuchAlgorithmException

Constructs an

EncryptedPrivateKeyInfo

from the
encryption algorithm parameters and the encrypted data.

Method Detail

- getAlgName

```java
public
String
getAlgName()
```

Returns the encryption algorithm.

Note: Standard name is returned instead of the specified one
in the constructor when such mapping is available.
See the

Java Security Standard Algorithm Names

document
for information about standard Cipher algorithm names.

**Returns:** the encryption algorithm name.

- getAlgParameters

```java
public
AlgorithmParameters
getAlgParameters()
```

Returns the algorithm parameters used by the encryption algorithm.

**Returns:** the algorithm parameters.

- getEncryptedData

```java
public byte[] getEncryptedData()
```

Returns the encrypted data.

**Returns:** the encrypted data. Returns a new array
each time this method is called.

- getKeySpec

```java
public
PKCS8EncodedKeySpec
getKeySpec​(
Cipher
cipher)
throws
InvalidKeySpecException
```

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

Note: In order to successfully retrieve the enclosed
PKCS8EncodedKeySpec object,

cipher

needs
to be initialized to either Cipher.DECRYPT_MODE or
Cipher.UNWRAP_MODE, with the same key and parameters used
for generating the encrypted data.

**Parameters:** cipher

- the initialized cipher object which will be
used for decrypting the encrypted data.
**Returns:** the PKCS8EncodedKeySpec object.
**Throws:** NullPointerException

- if

cipher

is null.
**Throws:** InvalidKeySpecException

- if the given cipher is
inappropriate for the encrypted data or the encrypted
data is corrupted and cannot be decrypted.

- getKeySpec

```java
public
PKCS8EncodedKeySpec
getKeySpec​(
Key
decryptKey)
throws
NoSuchAlgorithmException
,

InvalidKeyException
```

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

**Parameters:** decryptKey

- key used for decrypting the encrypted data.
**Returns:** the PKCS8EncodedKeySpec object.
**Throws:** NullPointerException

- if

decryptKey

is null.
**Throws:** NoSuchAlgorithmException

- if cannot find appropriate
cipher to decrypt the encrypted data.
**Throws:** InvalidKeyException

- if

decryptKey

cannot be used to decrypt the encrypted data or the decryption
result is not a valid PKCS8KeySpec.
**Since:** 1.5

- getKeySpec

```java
public
PKCS8EncodedKeySpec
getKeySpec​(
Key
decryptKey,

String
providerName)
throws
NoSuchProviderException
,

NoSuchAlgorithmException
,

InvalidKeyException
```

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

**Parameters:** decryptKey

- key used for decrypting the encrypted data.
**Parameters:** providerName

- the name of provider whose Cipher
implementation will be used.
**Returns:** the PKCS8EncodedKeySpec object.
**Throws:** NullPointerException

- if

decryptKey

or

providerName

is null.
**Throws:** NoSuchProviderException

- if no provider

providerName

is registered.
**Throws:** NoSuchAlgorithmException

- if cannot find appropriate
cipher to decrypt the encrypted data.
**Throws:** InvalidKeyException

- if

decryptKey

cannot be used to decrypt the encrypted data or the decryption
result is not a valid PKCS8KeySpec.
**Since:** 1.5

- getKeySpec

```java
public
PKCS8EncodedKeySpec
getKeySpec​(
Key
decryptKey,

Provider
provider)
throws
NoSuchAlgorithmException
,

InvalidKeyException
```

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

**Parameters:** decryptKey

- key used for decrypting the encrypted data.
**Parameters:** provider

- the name of provider whose Cipher implementation
will be used.
**Returns:** the PKCS8EncodedKeySpec object.
**Throws:** NullPointerException

- if

decryptKey

or

provider

is null.
**Throws:** NoSuchAlgorithmException

- if cannot find appropriate
cipher to decrypt the encrypted data in

provider

.
**Throws:** InvalidKeyException

- if

decryptKey

cannot be used to decrypt the encrypted data or the decryption
result is not a valid PKCS8KeySpec.
**Since:** 1.5

- getEncoded

```java
public byte[] getEncoded()
throws
IOException
```

Returns the ASN.1 encoding of this object.

**Returns:** the ASN.1 encoding. Returns a new array
each time this method is called.
**Throws:** IOException

- if error occurs when constructing its
ASN.1 encoding.

---

#### Method Detail

getAlgName

```java
public
String
getAlgName()
```

Returns the encryption algorithm.

Note: Standard name is returned instead of the specified one
in the constructor when such mapping is available.
See the

Java Security Standard Algorithm Names

document
for information about standard Cipher algorithm names.

**Returns:** the encryption algorithm name.

---

#### getAlgName

public

String

getAlgName()

Returns the encryption algorithm.

Note: Standard name is returned instead of the specified one
in the constructor when such mapping is available.
See the

Java Security Standard Algorithm Names

document
for information about standard Cipher algorithm names.

Note: Standard name is returned instead of the specified one
in the constructor when such mapping is available.
See the

Java Security Standard Algorithm Names

document
for information about standard Cipher algorithm names.

getAlgParameters

```java
public
AlgorithmParameters
getAlgParameters()
```

Returns the algorithm parameters used by the encryption algorithm.

**Returns:** the algorithm parameters.

---

#### getAlgParameters

public

AlgorithmParameters

getAlgParameters()

Returns the algorithm parameters used by the encryption algorithm.

getEncryptedData

```java
public byte[] getEncryptedData()
```

Returns the encrypted data.

**Returns:** the encrypted data. Returns a new array
each time this method is called.

---

#### getEncryptedData

public byte[] getEncryptedData()

Returns the encrypted data.

getKeySpec

```java
public
PKCS8EncodedKeySpec
getKeySpec​(
Cipher
cipher)
throws
InvalidKeySpecException
```

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

Note: In order to successfully retrieve the enclosed
PKCS8EncodedKeySpec object,

cipher

needs
to be initialized to either Cipher.DECRYPT_MODE or
Cipher.UNWRAP_MODE, with the same key and parameters used
for generating the encrypted data.

**Parameters:** cipher

- the initialized cipher object which will be
used for decrypting the encrypted data.
**Returns:** the PKCS8EncodedKeySpec object.
**Throws:** NullPointerException

- if

cipher

is null.
**Throws:** InvalidKeySpecException

- if the given cipher is
inappropriate for the encrypted data or the encrypted
data is corrupted and cannot be decrypted.

---

#### getKeySpec

public

PKCS8EncodedKeySpec

getKeySpec​(

Cipher

cipher)
throws

InvalidKeySpecException

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

Note: In order to successfully retrieve the enclosed
PKCS8EncodedKeySpec object,

cipher

needs
to be initialized to either Cipher.DECRYPT_MODE or
Cipher.UNWRAP_MODE, with the same key and parameters used
for generating the encrypted data.

getKeySpec

```java
public
PKCS8EncodedKeySpec
getKeySpec​(
Key
decryptKey)
throws
NoSuchAlgorithmException
,

InvalidKeyException
```

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

**Parameters:** decryptKey

- key used for decrypting the encrypted data.
**Returns:** the PKCS8EncodedKeySpec object.
**Throws:** NullPointerException

- if

decryptKey

is null.
**Throws:** NoSuchAlgorithmException

- if cannot find appropriate
cipher to decrypt the encrypted data.
**Throws:** InvalidKeyException

- if

decryptKey

cannot be used to decrypt the encrypted data or the decryption
result is not a valid PKCS8KeySpec.
**Since:** 1.5

---

#### getKeySpec

public

PKCS8EncodedKeySpec

getKeySpec​(

Key

decryptKey)
throws

NoSuchAlgorithmException

,

InvalidKeyException

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

getKeySpec

```java
public
PKCS8EncodedKeySpec
getKeySpec​(
Key
decryptKey,

String
providerName)
throws
NoSuchProviderException
,

NoSuchAlgorithmException
,

InvalidKeyException
```

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

**Parameters:** decryptKey

- key used for decrypting the encrypted data.
**Parameters:** providerName

- the name of provider whose Cipher
implementation will be used.
**Returns:** the PKCS8EncodedKeySpec object.
**Throws:** NullPointerException

- if

decryptKey

or

providerName

is null.
**Throws:** NoSuchProviderException

- if no provider

providerName

is registered.
**Throws:** NoSuchAlgorithmException

- if cannot find appropriate
cipher to decrypt the encrypted data.
**Throws:** InvalidKeyException

- if

decryptKey

cannot be used to decrypt the encrypted data or the decryption
result is not a valid PKCS8KeySpec.
**Since:** 1.5

---

#### getKeySpec

public

PKCS8EncodedKeySpec

getKeySpec​(

Key

decryptKey,

String

providerName)
throws

NoSuchProviderException

,

NoSuchAlgorithmException

,

InvalidKeyException

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

getKeySpec

```java
public
PKCS8EncodedKeySpec
getKeySpec​(
Key
decryptKey,

Provider
provider)
throws
NoSuchAlgorithmException
,

InvalidKeyException
```

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

**Parameters:** decryptKey

- key used for decrypting the encrypted data.
**Parameters:** provider

- the name of provider whose Cipher implementation
will be used.
**Returns:** the PKCS8EncodedKeySpec object.
**Throws:** NullPointerException

- if

decryptKey

or

provider

is null.
**Throws:** NoSuchAlgorithmException

- if cannot find appropriate
cipher to decrypt the encrypted data in

provider

.
**Throws:** InvalidKeyException

- if

decryptKey

cannot be used to decrypt the encrypted data or the decryption
result is not a valid PKCS8KeySpec.
**Since:** 1.5

---

#### getKeySpec

public

PKCS8EncodedKeySpec

getKeySpec​(

Key

decryptKey,

Provider

provider)
throws

NoSuchAlgorithmException

,

InvalidKeyException

Extract the enclosed PKCS8EncodedKeySpec object from the
encrypted data and return it.

getEncoded

```java
public byte[] getEncoded()
throws
IOException
```

Returns the ASN.1 encoding of this object.

**Returns:** the ASN.1 encoding. Returns a new array
each time this method is called.
**Throws:** IOException

- if error occurs when constructing its
ASN.1 encoding.

---

#### getEncoded

public byte[] getEncoded()
throws

IOException

Returns the ASN.1 encoding of this object.

---

