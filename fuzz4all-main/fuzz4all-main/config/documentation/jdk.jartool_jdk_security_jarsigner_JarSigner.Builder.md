# Class JarSigner.Builder

**Source:** `jdk.jartool\jdk\security\jarsigner\JarSigner.Builder.html`

### Class Description

```java
public static class
JarSigner.Builder

extends
Object
```

A mutable builder class that can create an immutable

JarSigner

from various signing-related parameters.

**Enclosing class:** JarSigner

---

### Field Details

*No entries found.*

### Constructor Details

#### public Builder​(
KeyStore.PrivateKeyEntry
entry)

Creates a

JarSigner.Builder

object with
a

KeyStore.PrivateKeyEntry

object.

**Parameters:**
- entry

- the

KeyStore.PrivateKeyEntry

of the signer.

---

#### public Builder​(
PrivateKey
privateKey,

CertPath
certPath)

Creates a

JarSigner.Builder

object with a private key and
a certification path.

**Parameters:**
- privateKey

- the private key of the signer.
- certPath

- the certification path of the signer.

**Throws:**
- IllegalArgumentException

- if

certPath

is empty, or
the

privateKey

algorithm does not match the algorithm
of the

PublicKey

in the end entity certificate
(the first certificate in

certPath

).

---

### Method Details

#### public
JarSigner.Builder
digestAlgorithm​(
String
algorithm)
throws
NoSuchAlgorithmException

Sets the digest algorithm. If no digest algorithm is specified,
the default algorithm returned by

getDefaultDigestAlgorithm()

will be used.

**Parameters:**
- algorithm

- the standard name of the algorithm. See
the

MessageDigest

section in the

Java Cryptography Architecture Standard Algorithm Name
Documentation

for information about standard algorithm names.

**Returns:**
- the

JarSigner.Builder

itself.

**Throws:**
- NoSuchAlgorithmException

- if

algorithm

is not available.

---

#### public
JarSigner.Builder
digestAlgorithm​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException

Sets the digest algorithm from the specified provider.
If no digest algorithm is specified, the default algorithm
returned by

getDefaultDigestAlgorithm()

will be used.

**Parameters:**
- algorithm

- the standard name of the algorithm. See
the

MessageDigest

section in the

Java Cryptography Architecture Standard Algorithm Name
Documentation

for information about standard algorithm names.
- provider

- the provider.

**Returns:**
- the

JarSigner.Builder

itself.

**Throws:**
- NoSuchAlgorithmException

- if

algorithm

is not
available in the specified provider.

---

#### public
JarSigner.Builder
signatureAlgorithm​(
String
algorithm)
throws
NoSuchAlgorithmException

Sets the signature algorithm. If no signature algorithm
is specified, the default signature algorithm returned by

getDefaultSignatureAlgorithm(java.security.PrivateKey)

for the private key
will be used.

**Parameters:**
- algorithm

- the standard name of the algorithm. See
the

Signature

section in the

Java Cryptography Architecture Standard Algorithm Name
Documentation

for information about standard algorithm names.

**Returns:**
- the

JarSigner.Builder

itself.

**Throws:**
- NoSuchAlgorithmException

- if

algorithm

is not available.
- IllegalArgumentException

- if

algorithm

is not
compatible with the algorithm of the signer's private key.

---

#### public
JarSigner.Builder
signatureAlgorithm​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException

Sets the signature algorithm from the specified provider. If no
signature algorithm is specified, the default signature algorithm
returned by

getDefaultSignatureAlgorithm(java.security.PrivateKey)

for the private
key will be used.

**Parameters:**
- algorithm

- the standard name of the algorithm. See
the

Signature

section in the

Java Cryptography Architecture Standard Algorithm Name
Documentation

for information about standard algorithm names.
- provider

- the provider.

**Returns:**
- the

JarSigner.Builder

itself.

**Throws:**
- NoSuchAlgorithmException

- if

algorithm

is not
available in the specified provider.
- IllegalArgumentException

- if

algorithm

is not
compatible with the algorithm of the signer's private key.

---

#### public
JarSigner.Builder
tsa​(
URI
uri)

Sets the URI of the Time Stamping Authority (TSA).

**Parameters:**
- uri

- the URI.

**Returns:**
- the

JarSigner.Builder

itself.

---

#### public
JarSigner.Builder
signerName​(
String
name)

Sets the signer name. The name will be used as the base name for
the signature files. All lowercase characters will be converted to
uppercase for signature file names. If a signer name is not
specified, the string "SIGNER" will be used.

**Parameters:**
- name

- the signer name.

**Returns:**
- the

JarSigner.Builder

itself.

**Throws:**
- IllegalArgumentException

- if

name

is empty or has
a size bigger than 8, or it contains characters not from the
set "a-zA-Z0-9_-".

---

#### public
JarSigner.Builder
eventHandler​(
BiConsumer
<
String
,​
String
> handler)

Sets en event handler that will be triggered when a

JarEntry

is to be added, signed, or updated during the signing process.

The handler can be used to display signing progress. The first
argument of the handler can be "adding", "signing", or "updating",
and the second argument is the name of the

JarEntry

being processed.

**Parameters:**
- handler

- the event handler.

**Returns:**
- the

JarSigner.Builder

itself.

---

#### public
JarSigner.Builder
setProperty​(
String
key,

String
value)

Sets an additional implementation-specific property indicated by
the specified key.

**Parameters:**
- key

- the name of the property.
- value

- the value of the property.

**Returns:**
- the

JarSigner.Builder

itself.

**Throws:**
- UnsupportedOperationException

- if the key is not supported
by this implementation.
- IllegalArgumentException

- if the value is not accepted as
a legal value for this key.

**Implementation Note:**
- This implementation supports the following properties:

- "tsaDigestAlg": algorithm of digest data in the timestamping
request. The default value is the same as the result of

getDefaultDigestAlgorithm()

.

"tsaPolicyId": TSAPolicyID for Timestamping Authority.
No default value.

"internalsf": "true" if the .SF file is included inside the
signature block, "false" otherwise. Default "false".

"sectionsonly": "true" if the .SF file only contains the hash
value for each section of the manifest and not for the whole
manifest, "false" otherwise. Default "false".

All property names are case-insensitive.

---

#### public static
String
getDefaultDigestAlgorithm()

Gets the default digest algorithm.

**Returns:**
- the default digest algorithm.

**Implementation Note:**
- This implementation returns "SHA-256". The value may
change in the future.

---

#### public static
String
getDefaultSignatureAlgorithm​(
PrivateKey
key)

Gets the default signature algorithm for a private key.
For example, SHA256withRSA for a 2048-bit RSA key, and
SHA384withECDSA for a 384-bit EC key.

**Parameters:**
- key

- the private key.

**Returns:**
- the default signature algorithm. Returns null if a default
signature algorithm cannot be found. In this case,

signatureAlgorithm(java.lang.String)

must be called to specify a
signature algorithm. Otherwise, the

build()

method
will throw an

IllegalArgumentException

.

**Implementation Note:**
- This implementation makes use of comparable strengths
as defined in Tables 2 and 3 of NIST SP 800-57 Part 1-Rev.4.
Specifically, if a DSA or RSA key with a key size greater than 7680
bits, or an EC key with a key size greater than or equal to 512 bits,
SHA-512 will be used as the hash function for the signature.
If a DSA or RSA key has a key size greater than 3072 bits, or an
EC key has a key size greater than or equal to 384 bits, SHA-384 will
be used. Otherwise, SHA-256 will be used. The value may
change in the future.

---

#### public
JarSigner
build()

Builds a

JarSigner

object from the parameters set by the
setter methods.

This method does not modify internal state of this

Builder

object and can be called multiple times to generate multiple

JarSigner

objects. After this method is called, calling
any method on this

Builder

will have no effect on
the newly built

JarSigner

object.

**Returns:**
- the

JarSigner

object.

**Throws:**
- IllegalArgumentException

- if a signature algorithm is not
set and cannot be derived from the private key using the

getDefaultSignatureAlgorithm(java.security.PrivateKey)

method.

---

### Additional Sections

#### Class JarSigner.Builder

java.lang.Object

- jdk.security.jarsigner.JarSigner.Builder

jdk.security.jarsigner.JarSigner.Builder

**Enclosing class:** JarSigner

```java
public static class
JarSigner.Builder

extends
Object
```

A mutable builder class that can create an immutable

JarSigner

from various signing-related parameters.

**Since:** 9

public static class

JarSigner.Builder

extends

Object

A mutable builder class that can create an immutable

JarSigner

from various signing-related parameters.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Builder

​(

KeyStore.PrivateKeyEntry

entry)

Creates a

JarSigner.Builder

object with
a

KeyStore.PrivateKeyEntry

object.

Builder

​(

PrivateKey

privateKey,

CertPath

certPath)

Creates a

JarSigner.Builder

object with a private key and
a certification path.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JarSigner

build

()

Builds a

JarSigner

object from the parameters set by the
setter methods.

JarSigner.Builder

digestAlgorithm

​(

String

algorithm)

Sets the digest algorithm.

JarSigner.Builder

digestAlgorithm

​(

String

algorithm,

Provider

provider)

Sets the digest algorithm from the specified provider.

JarSigner.Builder

eventHandler

​(

BiConsumer

<

String

,​

String

> handler)

Sets en event handler that will be triggered when a

JarEntry

is to be added, signed, or updated during the signing process.

static

String

getDefaultDigestAlgorithm

()

Gets the default digest algorithm.

static

String

getDefaultSignatureAlgorithm

​(

PrivateKey

key)

Gets the default signature algorithm for a private key.

JarSigner.Builder

setProperty

​(

String

key,

String

value)

Sets an additional implementation-specific property indicated by
the specified key.

JarSigner.Builder

signatureAlgorithm

​(

String

algorithm)

Sets the signature algorithm.

JarSigner.Builder

signatureAlgorithm

​(

String

algorithm,

Provider

provider)

Sets the signature algorithm from the specified provider.

JarSigner.Builder

signerName

​(

String

name)

Sets the signer name.

JarSigner.Builder

tsa

​(

URI

uri)

Sets the URI of the Time Stamping Authority (TSA).

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

Builder

​(

KeyStore.PrivateKeyEntry

entry)

Creates a

JarSigner.Builder

object with
a

KeyStore.PrivateKeyEntry

object.

Builder

​(

PrivateKey

privateKey,

CertPath

certPath)

Creates a

JarSigner.Builder

object with a private key and
a certification path.

---

#### Constructor Summary

Creates a

JarSigner.Builder

object with
a

KeyStore.PrivateKeyEntry

object.

Creates a

JarSigner.Builder

object with a private key and
a certification path.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

JarSigner

build

()

Builds a

JarSigner

object from the parameters set by the
setter methods.

JarSigner.Builder

digestAlgorithm

​(

String

algorithm)

Sets the digest algorithm.

JarSigner.Builder

digestAlgorithm

​(

String

algorithm,

Provider

provider)

Sets the digest algorithm from the specified provider.

JarSigner.Builder

eventHandler

​(

BiConsumer

<

String

,​

String

> handler)

Sets en event handler that will be triggered when a

JarEntry

is to be added, signed, or updated during the signing process.

static

String

getDefaultDigestAlgorithm

()

Gets the default digest algorithm.

static

String

getDefaultSignatureAlgorithm

​(

PrivateKey

key)

Gets the default signature algorithm for a private key.

JarSigner.Builder

setProperty

​(

String

key,

String

value)

Sets an additional implementation-specific property indicated by
the specified key.

JarSigner.Builder

signatureAlgorithm

​(

String

algorithm)

Sets the signature algorithm.

JarSigner.Builder

signatureAlgorithm

​(

String

algorithm,

Provider

provider)

Sets the signature algorithm from the specified provider.

JarSigner.Builder

signerName

​(

String

name)

Sets the signer name.

JarSigner.Builder

tsa

​(

URI

uri)

Sets the URI of the Time Stamping Authority (TSA).

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

Builds a

JarSigner

object from the parameters set by the
setter methods.

Sets the digest algorithm.

Sets the digest algorithm from the specified provider.

Sets en event handler that will be triggered when a

JarEntry

is to be added, signed, or updated during the signing process.

Gets the default digest algorithm.

Gets the default signature algorithm for a private key.

Sets an additional implementation-specific property indicated by
the specified key.

Sets the signature algorithm.

Sets the signature algorithm from the specified provider.

Sets the signer name.

Sets the URI of the Time Stamping Authority (TSA).

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

- Builder

```java
public Builder​(
KeyStore.PrivateKeyEntry
entry)
```

Creates a

JarSigner.Builder

object with
a

KeyStore.PrivateKeyEntry

object.

**Parameters:** entry

- the

KeyStore.PrivateKeyEntry

of the signer.

- Builder

```java
public Builder​(
PrivateKey
privateKey,

CertPath
certPath)
```

Creates a

JarSigner.Builder

object with a private key and
a certification path.

**Parameters:** privateKey

- the private key of the signer.
**Parameters:** certPath

- the certification path of the signer.
**Throws:** IllegalArgumentException

- if

certPath

is empty, or
the

privateKey

algorithm does not match the algorithm
of the

PublicKey

in the end entity certificate
(the first certificate in

certPath

).

============ METHOD DETAIL ==========

- Method Detail

- digestAlgorithm

```java
public
JarSigner.Builder
digestAlgorithm​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Sets the digest algorithm. If no digest algorithm is specified,
the default algorithm returned by

getDefaultDigestAlgorithm()

will be used.

**Parameters:** algorithm

- the standard name of the algorithm. See
the

MessageDigest

section in the

Java Cryptography Architecture Standard Algorithm Name
Documentation

for information about standard algorithm names.
**Returns:** the

JarSigner.Builder

itself.
**Throws:** NoSuchAlgorithmException

- if

algorithm

is not available.

- digestAlgorithm

```java
public
JarSigner.Builder
digestAlgorithm​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Sets the digest algorithm from the specified provider.
If no digest algorithm is specified, the default algorithm
returned by

getDefaultDigestAlgorithm()

will be used.

**Parameters:** algorithm

- the standard name of the algorithm. See
the

MessageDigest

section in the

Java Cryptography Architecture Standard Algorithm Name
Documentation

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the

JarSigner.Builder

itself.
**Throws:** NoSuchAlgorithmException

- if

algorithm

is not
available in the specified provider.

- signatureAlgorithm

```java
public
JarSigner.Builder
signatureAlgorithm​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Sets the signature algorithm. If no signature algorithm
is specified, the default signature algorithm returned by

getDefaultSignatureAlgorithm(java.security.PrivateKey)

for the private key
will be used.

**Parameters:** algorithm

- the standard name of the algorithm. See
the

Signature

section in the

Java Cryptography Architecture Standard Algorithm Name
Documentation

for information about standard algorithm names.
**Returns:** the

JarSigner.Builder

itself.
**Throws:** NoSuchAlgorithmException

- if

algorithm

is not available.
**Throws:** IllegalArgumentException

- if

algorithm

is not
compatible with the algorithm of the signer's private key.

- signatureAlgorithm

```java
public
JarSigner.Builder
signatureAlgorithm​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Sets the signature algorithm from the specified provider. If no
signature algorithm is specified, the default signature algorithm
returned by

getDefaultSignatureAlgorithm(java.security.PrivateKey)

for the private
key will be used.

**Parameters:** algorithm

- the standard name of the algorithm. See
the

Signature

section in the

Java Cryptography Architecture Standard Algorithm Name
Documentation

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the

JarSigner.Builder

itself.
**Throws:** NoSuchAlgorithmException

- if

algorithm

is not
available in the specified provider.
**Throws:** IllegalArgumentException

- if

algorithm

is not
compatible with the algorithm of the signer's private key.

- tsa

```java
public
JarSigner.Builder
tsa​(
URI
uri)
```

Sets the URI of the Time Stamping Authority (TSA).

**Parameters:** uri

- the URI.
**Returns:** the

JarSigner.Builder

itself.

- signerName

```java
public
JarSigner.Builder
signerName​(
String
name)
```

Sets the signer name. The name will be used as the base name for
the signature files. All lowercase characters will be converted to
uppercase for signature file names. If a signer name is not
specified, the string "SIGNER" will be used.

**Parameters:** name

- the signer name.
**Returns:** the

JarSigner.Builder

itself.
**Throws:** IllegalArgumentException

- if

name

is empty or has
a size bigger than 8, or it contains characters not from the
set "a-zA-Z0-9_-".

- eventHandler

```java
public
JarSigner.Builder
eventHandler​(
BiConsumer
<
String
,​
String
> handler)
```

Sets en event handler that will be triggered when a

JarEntry

is to be added, signed, or updated during the signing process.

The handler can be used to display signing progress. The first
argument of the handler can be "adding", "signing", or "updating",
and the second argument is the name of the

JarEntry

being processed.

**Parameters:** handler

- the event handler.
**Returns:** the

JarSigner.Builder

itself.

- setProperty

```java
public
JarSigner.Builder
setProperty​(
String
key,

String
value)
```

Sets an additional implementation-specific property indicated by
the specified key.

**Implementation Note:** This implementation supports the following properties:

- "tsaDigestAlg": algorithm of digest data in the timestamping
request. The default value is the same as the result of

getDefaultDigestAlgorithm()

.

"tsaPolicyId": TSAPolicyID for Timestamping Authority.
No default value.

"internalsf": "true" if the .SF file is included inside the
signature block, "false" otherwise. Default "false".

"sectionsonly": "true" if the .SF file only contains the hash
value for each section of the manifest and not for the whole
manifest, "false" otherwise. Default "false".

All property names are case-insensitive.
**Parameters:** key

- the name of the property.
**Parameters:** value

- the value of the property.
**Returns:** the

JarSigner.Builder

itself.
**Throws:** UnsupportedOperationException

- if the key is not supported
by this implementation.
**Throws:** IllegalArgumentException

- if the value is not accepted as
a legal value for this key.

- getDefaultDigestAlgorithm

```java
public static
String
getDefaultDigestAlgorithm()
```

Gets the default digest algorithm.

**Implementation Note:** This implementation returns "SHA-256". The value may
change in the future.
**Returns:** the default digest algorithm.

- getDefaultSignatureAlgorithm

```java
public static
String
getDefaultSignatureAlgorithm​(
PrivateKey
key)
```

Gets the default signature algorithm for a private key.
For example, SHA256withRSA for a 2048-bit RSA key, and
SHA384withECDSA for a 384-bit EC key.

**Implementation Note:** This implementation makes use of comparable strengths
as defined in Tables 2 and 3 of NIST SP 800-57 Part 1-Rev.4.
Specifically, if a DSA or RSA key with a key size greater than 7680
bits, or an EC key with a key size greater than or equal to 512 bits,
SHA-512 will be used as the hash function for the signature.
If a DSA or RSA key has a key size greater than 3072 bits, or an
EC key has a key size greater than or equal to 384 bits, SHA-384 will
be used. Otherwise, SHA-256 will be used. The value may
change in the future.
**Parameters:** key

- the private key.
**Returns:** the default signature algorithm. Returns null if a default
signature algorithm cannot be found. In this case,

signatureAlgorithm(java.lang.String)

must be called to specify a
signature algorithm. Otherwise, the

build()

method
will throw an

IllegalArgumentException

.

- build

```java
public
JarSigner
build()
```

Builds a

JarSigner

object from the parameters set by the
setter methods.

This method does not modify internal state of this

Builder

object and can be called multiple times to generate multiple

JarSigner

objects. After this method is called, calling
any method on this

Builder

will have no effect on
the newly built

JarSigner

object.

**Returns:** the

JarSigner

object.
**Throws:** IllegalArgumentException

- if a signature algorithm is not
set and cannot be derived from the private key using the

getDefaultSignatureAlgorithm(java.security.PrivateKey)

method.

Constructor Detail

- Builder

```java
public Builder​(
KeyStore.PrivateKeyEntry
entry)
```

Creates a

JarSigner.Builder

object with
a

KeyStore.PrivateKeyEntry

object.

**Parameters:** entry

- the

KeyStore.PrivateKeyEntry

of the signer.

- Builder

```java
public Builder​(
PrivateKey
privateKey,

CertPath
certPath)
```

Creates a

JarSigner.Builder

object with a private key and
a certification path.

**Parameters:** privateKey

- the private key of the signer.
**Parameters:** certPath

- the certification path of the signer.
**Throws:** IllegalArgumentException

- if

certPath

is empty, or
the

privateKey

algorithm does not match the algorithm
of the

PublicKey

in the end entity certificate
(the first certificate in

certPath

).

---

#### Constructor Detail

Builder

```java
public Builder​(
KeyStore.PrivateKeyEntry
entry)
```

Creates a

JarSigner.Builder

object with
a

KeyStore.PrivateKeyEntry

object.

**Parameters:** entry

- the

KeyStore.PrivateKeyEntry

of the signer.

---

#### Builder

public Builder​(

KeyStore.PrivateKeyEntry

entry)

Creates a

JarSigner.Builder

object with
a

KeyStore.PrivateKeyEntry

object.

Builder

```java
public Builder​(
PrivateKey
privateKey,

CertPath
certPath)
```

Creates a

JarSigner.Builder

object with a private key and
a certification path.

**Parameters:** privateKey

- the private key of the signer.
**Parameters:** certPath

- the certification path of the signer.
**Throws:** IllegalArgumentException

- if

certPath

is empty, or
the

privateKey

algorithm does not match the algorithm
of the

PublicKey

in the end entity certificate
(the first certificate in

certPath

).

---

#### Builder

public Builder​(

PrivateKey

privateKey,

CertPath

certPath)

Creates a

JarSigner.Builder

object with a private key and
a certification path.

Method Detail

- digestAlgorithm

```java
public
JarSigner.Builder
digestAlgorithm​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Sets the digest algorithm. If no digest algorithm is specified,
the default algorithm returned by

getDefaultDigestAlgorithm()

will be used.

**Parameters:** algorithm

- the standard name of the algorithm. See
the

MessageDigest

section in the

Java Cryptography Architecture Standard Algorithm Name
Documentation

for information about standard algorithm names.
**Returns:** the

JarSigner.Builder

itself.
**Throws:** NoSuchAlgorithmException

- if

algorithm

is not available.

- digestAlgorithm

```java
public
JarSigner.Builder
digestAlgorithm​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Sets the digest algorithm from the specified provider.
If no digest algorithm is specified, the default algorithm
returned by

getDefaultDigestAlgorithm()

will be used.

**Parameters:** algorithm

- the standard name of the algorithm. See
the

MessageDigest

section in the

Java Cryptography Architecture Standard Algorithm Name
Documentation

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the

JarSigner.Builder

itself.
**Throws:** NoSuchAlgorithmException

- if

algorithm

is not
available in the specified provider.

- signatureAlgorithm

```java
public
JarSigner.Builder
signatureAlgorithm​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Sets the signature algorithm. If no signature algorithm
is specified, the default signature algorithm returned by

getDefaultSignatureAlgorithm(java.security.PrivateKey)

for the private key
will be used.

**Parameters:** algorithm

- the standard name of the algorithm. See
the

Signature

section in the

Java Cryptography Architecture Standard Algorithm Name
Documentation

for information about standard algorithm names.
**Returns:** the

JarSigner.Builder

itself.
**Throws:** NoSuchAlgorithmException

- if

algorithm

is not available.
**Throws:** IllegalArgumentException

- if

algorithm

is not
compatible with the algorithm of the signer's private key.

- signatureAlgorithm

```java
public
JarSigner.Builder
signatureAlgorithm​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Sets the signature algorithm from the specified provider. If no
signature algorithm is specified, the default signature algorithm
returned by

getDefaultSignatureAlgorithm(java.security.PrivateKey)

for the private
key will be used.

**Parameters:** algorithm

- the standard name of the algorithm. See
the

Signature

section in the

Java Cryptography Architecture Standard Algorithm Name
Documentation

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the

JarSigner.Builder

itself.
**Throws:** NoSuchAlgorithmException

- if

algorithm

is not
available in the specified provider.
**Throws:** IllegalArgumentException

- if

algorithm

is not
compatible with the algorithm of the signer's private key.

- tsa

```java
public
JarSigner.Builder
tsa​(
URI
uri)
```

Sets the URI of the Time Stamping Authority (TSA).

**Parameters:** uri

- the URI.
**Returns:** the

JarSigner.Builder

itself.

- signerName

```java
public
JarSigner.Builder
signerName​(
String
name)
```

Sets the signer name. The name will be used as the base name for
the signature files. All lowercase characters will be converted to
uppercase for signature file names. If a signer name is not
specified, the string "SIGNER" will be used.

**Parameters:** name

- the signer name.
**Returns:** the

JarSigner.Builder

itself.
**Throws:** IllegalArgumentException

- if

name

is empty or has
a size bigger than 8, or it contains characters not from the
set "a-zA-Z0-9_-".

- eventHandler

```java
public
JarSigner.Builder
eventHandler​(
BiConsumer
<
String
,​
String
> handler)
```

Sets en event handler that will be triggered when a

JarEntry

is to be added, signed, or updated during the signing process.

The handler can be used to display signing progress. The first
argument of the handler can be "adding", "signing", or "updating",
and the second argument is the name of the

JarEntry

being processed.

**Parameters:** handler

- the event handler.
**Returns:** the

JarSigner.Builder

itself.

- setProperty

```java
public
JarSigner.Builder
setProperty​(
String
key,

String
value)
```

Sets an additional implementation-specific property indicated by
the specified key.

**Implementation Note:** This implementation supports the following properties:

- "tsaDigestAlg": algorithm of digest data in the timestamping
request. The default value is the same as the result of

getDefaultDigestAlgorithm()

.

"tsaPolicyId": TSAPolicyID for Timestamping Authority.
No default value.

"internalsf": "true" if the .SF file is included inside the
signature block, "false" otherwise. Default "false".

"sectionsonly": "true" if the .SF file only contains the hash
value for each section of the manifest and not for the whole
manifest, "false" otherwise. Default "false".

All property names are case-insensitive.
**Parameters:** key

- the name of the property.
**Parameters:** value

- the value of the property.
**Returns:** the

JarSigner.Builder

itself.
**Throws:** UnsupportedOperationException

- if the key is not supported
by this implementation.
**Throws:** IllegalArgumentException

- if the value is not accepted as
a legal value for this key.

- getDefaultDigestAlgorithm

```java
public static
String
getDefaultDigestAlgorithm()
```

Gets the default digest algorithm.

**Implementation Note:** This implementation returns "SHA-256". The value may
change in the future.
**Returns:** the default digest algorithm.

- getDefaultSignatureAlgorithm

```java
public static
String
getDefaultSignatureAlgorithm​(
PrivateKey
key)
```

Gets the default signature algorithm for a private key.
For example, SHA256withRSA for a 2048-bit RSA key, and
SHA384withECDSA for a 384-bit EC key.

**Implementation Note:** This implementation makes use of comparable strengths
as defined in Tables 2 and 3 of NIST SP 800-57 Part 1-Rev.4.
Specifically, if a DSA or RSA key with a key size greater than 7680
bits, or an EC key with a key size greater than or equal to 512 bits,
SHA-512 will be used as the hash function for the signature.
If a DSA or RSA key has a key size greater than 3072 bits, or an
EC key has a key size greater than or equal to 384 bits, SHA-384 will
be used. Otherwise, SHA-256 will be used. The value may
change in the future.
**Parameters:** key

- the private key.
**Returns:** the default signature algorithm. Returns null if a default
signature algorithm cannot be found. In this case,

signatureAlgorithm(java.lang.String)

must be called to specify a
signature algorithm. Otherwise, the

build()

method
will throw an

IllegalArgumentException

.

- build

```java
public
JarSigner
build()
```

Builds a

JarSigner

object from the parameters set by the
setter methods.

This method does not modify internal state of this

Builder

object and can be called multiple times to generate multiple

JarSigner

objects. After this method is called, calling
any method on this

Builder

will have no effect on
the newly built

JarSigner

object.

**Returns:** the

JarSigner

object.
**Throws:** IllegalArgumentException

- if a signature algorithm is not
set and cannot be derived from the private key using the

getDefaultSignatureAlgorithm(java.security.PrivateKey)

method.

---

#### Method Detail

digestAlgorithm

```java
public
JarSigner.Builder
digestAlgorithm​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Sets the digest algorithm. If no digest algorithm is specified,
the default algorithm returned by

getDefaultDigestAlgorithm()

will be used.

**Parameters:** algorithm

- the standard name of the algorithm. See
the

MessageDigest

section in the

Java Cryptography Architecture Standard Algorithm Name
Documentation

for information about standard algorithm names.
**Returns:** the

JarSigner.Builder

itself.
**Throws:** NoSuchAlgorithmException

- if

algorithm

is not available.

---

#### digestAlgorithm

public

JarSigner.Builder

digestAlgorithm​(

String

algorithm)
throws

NoSuchAlgorithmException

Sets the digest algorithm. If no digest algorithm is specified,
the default algorithm returned by

getDefaultDigestAlgorithm()

will be used.

digestAlgorithm

```java
public
JarSigner.Builder
digestAlgorithm​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Sets the digest algorithm from the specified provider.
If no digest algorithm is specified, the default algorithm
returned by

getDefaultDigestAlgorithm()

will be used.

**Parameters:** algorithm

- the standard name of the algorithm. See
the

MessageDigest

section in the

Java Cryptography Architecture Standard Algorithm Name
Documentation

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the

JarSigner.Builder

itself.
**Throws:** NoSuchAlgorithmException

- if

algorithm

is not
available in the specified provider.

---

#### digestAlgorithm

public

JarSigner.Builder

digestAlgorithm​(

String

algorithm,

Provider

provider)
throws

NoSuchAlgorithmException

Sets the digest algorithm from the specified provider.
If no digest algorithm is specified, the default algorithm
returned by

getDefaultDigestAlgorithm()

will be used.

signatureAlgorithm

```java
public
JarSigner.Builder
signatureAlgorithm​(
String
algorithm)
throws
NoSuchAlgorithmException
```

Sets the signature algorithm. If no signature algorithm
is specified, the default signature algorithm returned by

getDefaultSignatureAlgorithm(java.security.PrivateKey)

for the private key
will be used.

**Parameters:** algorithm

- the standard name of the algorithm. See
the

Signature

section in the

Java Cryptography Architecture Standard Algorithm Name
Documentation

for information about standard algorithm names.
**Returns:** the

JarSigner.Builder

itself.
**Throws:** NoSuchAlgorithmException

- if

algorithm

is not available.
**Throws:** IllegalArgumentException

- if

algorithm

is not
compatible with the algorithm of the signer's private key.

---

#### signatureAlgorithm

public

JarSigner.Builder

signatureAlgorithm​(

String

algorithm)
throws

NoSuchAlgorithmException

Sets the signature algorithm. If no signature algorithm
is specified, the default signature algorithm returned by

getDefaultSignatureAlgorithm(java.security.PrivateKey)

for the private key
will be used.

signatureAlgorithm

```java
public
JarSigner.Builder
signatureAlgorithm​(
String
algorithm,

Provider
provider)
throws
NoSuchAlgorithmException
```

Sets the signature algorithm from the specified provider. If no
signature algorithm is specified, the default signature algorithm
returned by

getDefaultSignatureAlgorithm(java.security.PrivateKey)

for the private
key will be used.

**Parameters:** algorithm

- the standard name of the algorithm. See
the

Signature

section in the

Java Cryptography Architecture Standard Algorithm Name
Documentation

for information about standard algorithm names.
**Parameters:** provider

- the provider.
**Returns:** the

JarSigner.Builder

itself.
**Throws:** NoSuchAlgorithmException

- if

algorithm

is not
available in the specified provider.
**Throws:** IllegalArgumentException

- if

algorithm

is not
compatible with the algorithm of the signer's private key.

---

#### signatureAlgorithm

public

JarSigner.Builder

signatureAlgorithm​(

String

algorithm,

Provider

provider)
throws

NoSuchAlgorithmException

Sets the signature algorithm from the specified provider. If no
signature algorithm is specified, the default signature algorithm
returned by

getDefaultSignatureAlgorithm(java.security.PrivateKey)

for the private
key will be used.

tsa

```java
public
JarSigner.Builder
tsa​(
URI
uri)
```

Sets the URI of the Time Stamping Authority (TSA).

**Parameters:** uri

- the URI.
**Returns:** the

JarSigner.Builder

itself.

---

#### tsa

public

JarSigner.Builder

tsa​(

URI

uri)

Sets the URI of the Time Stamping Authority (TSA).

signerName

```java
public
JarSigner.Builder
signerName​(
String
name)
```

Sets the signer name. The name will be used as the base name for
the signature files. All lowercase characters will be converted to
uppercase for signature file names. If a signer name is not
specified, the string "SIGNER" will be used.

**Parameters:** name

- the signer name.
**Returns:** the

JarSigner.Builder

itself.
**Throws:** IllegalArgumentException

- if

name

is empty or has
a size bigger than 8, or it contains characters not from the
set "a-zA-Z0-9_-".

---

#### signerName

public

JarSigner.Builder

signerName​(

String

name)

Sets the signer name. The name will be used as the base name for
the signature files. All lowercase characters will be converted to
uppercase for signature file names. If a signer name is not
specified, the string "SIGNER" will be used.

eventHandler

```java
public
JarSigner.Builder
eventHandler​(
BiConsumer
<
String
,​
String
> handler)
```

Sets en event handler that will be triggered when a

JarEntry

is to be added, signed, or updated during the signing process.

The handler can be used to display signing progress. The first
argument of the handler can be "adding", "signing", or "updating",
and the second argument is the name of the

JarEntry

being processed.

**Parameters:** handler

- the event handler.
**Returns:** the

JarSigner.Builder

itself.

---

#### eventHandler

public

JarSigner.Builder

eventHandler​(

BiConsumer

<

String

,​

String

> handler)

Sets en event handler that will be triggered when a

JarEntry

is to be added, signed, or updated during the signing process.

The handler can be used to display signing progress. The first
argument of the handler can be "adding", "signing", or "updating",
and the second argument is the name of the

JarEntry

being processed.

The handler can be used to display signing progress. The first
argument of the handler can be "adding", "signing", or "updating",
and the second argument is the name of the

JarEntry

being processed.

setProperty

```java
public
JarSigner.Builder
setProperty​(
String
key,

String
value)
```

Sets an additional implementation-specific property indicated by
the specified key.

**Implementation Note:** This implementation supports the following properties:

- "tsaDigestAlg": algorithm of digest data in the timestamping
request. The default value is the same as the result of

getDefaultDigestAlgorithm()

.

"tsaPolicyId": TSAPolicyID for Timestamping Authority.
No default value.

"internalsf": "true" if the .SF file is included inside the
signature block, "false" otherwise. Default "false".

"sectionsonly": "true" if the .SF file only contains the hash
value for each section of the manifest and not for the whole
manifest, "false" otherwise. Default "false".

All property names are case-insensitive.
**Parameters:** key

- the name of the property.
**Parameters:** value

- the value of the property.
**Returns:** the

JarSigner.Builder

itself.
**Throws:** UnsupportedOperationException

- if the key is not supported
by this implementation.
**Throws:** IllegalArgumentException

- if the value is not accepted as
a legal value for this key.

---

#### setProperty

public

JarSigner.Builder

setProperty​(

String

key,

String

value)

Sets an additional implementation-specific property indicated by
the specified key.

"tsaDigestAlg": algorithm of digest data in the timestamping
request. The default value is the same as the result of

getDefaultDigestAlgorithm()

.

"tsaPolicyId": TSAPolicyID for Timestamping Authority.
No default value.

"internalsf": "true" if the .SF file is included inside the
signature block, "false" otherwise. Default "false".

"sectionsonly": "true" if the .SF file only contains the hash
value for each section of the manifest and not for the whole
manifest, "false" otherwise. Default "false".

getDefaultDigestAlgorithm

```java
public static
String
getDefaultDigestAlgorithm()
```

Gets the default digest algorithm.

**Implementation Note:** This implementation returns "SHA-256". The value may
change in the future.
**Returns:** the default digest algorithm.

---

#### getDefaultDigestAlgorithm

public static

String

getDefaultDigestAlgorithm()

Gets the default digest algorithm.

getDefaultSignatureAlgorithm

```java
public static
String
getDefaultSignatureAlgorithm​(
PrivateKey
key)
```

Gets the default signature algorithm for a private key.
For example, SHA256withRSA for a 2048-bit RSA key, and
SHA384withECDSA for a 384-bit EC key.

**Implementation Note:** This implementation makes use of comparable strengths
as defined in Tables 2 and 3 of NIST SP 800-57 Part 1-Rev.4.
Specifically, if a DSA or RSA key with a key size greater than 7680
bits, or an EC key with a key size greater than or equal to 512 bits,
SHA-512 will be used as the hash function for the signature.
If a DSA or RSA key has a key size greater than 3072 bits, or an
EC key has a key size greater than or equal to 384 bits, SHA-384 will
be used. Otherwise, SHA-256 will be used. The value may
change in the future.
**Parameters:** key

- the private key.
**Returns:** the default signature algorithm. Returns null if a default
signature algorithm cannot be found. In this case,

signatureAlgorithm(java.lang.String)

must be called to specify a
signature algorithm. Otherwise, the

build()

method
will throw an

IllegalArgumentException

.

---

#### getDefaultSignatureAlgorithm

public static

String

getDefaultSignatureAlgorithm​(

PrivateKey

key)

Gets the default signature algorithm for a private key.
For example, SHA256withRSA for a 2048-bit RSA key, and
SHA384withECDSA for a 384-bit EC key.

build

```java
public
JarSigner
build()
```

Builds a

JarSigner

object from the parameters set by the
setter methods.

This method does not modify internal state of this

Builder

object and can be called multiple times to generate multiple

JarSigner

objects. After this method is called, calling
any method on this

Builder

will have no effect on
the newly built

JarSigner

object.

**Returns:** the

JarSigner

object.
**Throws:** IllegalArgumentException

- if a signature algorithm is not
set and cannot be derived from the private key using the

getDefaultSignatureAlgorithm(java.security.PrivateKey)

method.

---

#### build

public

JarSigner

build()

Builds a

JarSigner

object from the parameters set by the
setter methods.

This method does not modify internal state of this

Builder

object and can be called multiple times to generate multiple

JarSigner

objects. After this method is called, calling
any method on this

Builder

will have no effect on
the newly built

JarSigner

object.

This method does not modify internal state of this

Builder

object and can be called multiple times to generate multiple

JarSigner

objects. After this method is called, calling
any method on this

Builder

will have no effect on
the newly built

JarSigner

object.

---

