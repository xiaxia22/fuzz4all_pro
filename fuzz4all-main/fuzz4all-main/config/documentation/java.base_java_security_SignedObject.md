# Class SignedObject

**Source:** `java.base\java\security\SignedObject.html`

### Class Description

```java
public final class
SignedObject

extends
Object

implements
Serializable
```

SignedObject is a class for the purpose of creating authentic
runtime objects whose integrity cannot be compromised without being
detected.

More specifically, a SignedObject contains another Serializable
object, the (to-be-)signed object and its signature.

The signed object is a "deep copy" (in serialized form) of an
original object. Once the copy is made, further manipulation of
the original object has no side effect on the copy.

The underlying signing algorithm is designated by the Signature
object passed to the constructor and the

verify

method.
A typical usage for signing is the following:

```java
Signature signingEngine = Signature.getInstance(algorithm,
provider);
SignedObject so = new SignedObject(myobject, signingKey,
signingEngine);
```

A typical usage for verification is the following (having
received SignedObject

so

):

```java
Signature verificationEngine =
Signature.getInstance(algorithm, provider);
if (so.verify(publickey, verificationEngine))
try {
Object myobj = so.getObject();
} catch (java.lang.ClassNotFoundException e) {};
```

Several points are worth noting. First, there is no need to
initialize the signing or verification engine, as it will be
re-initialized inside the constructor and the

verify

method. Secondly, for verification to succeed, the specified
public key must be the public key corresponding to the private key
used to generate the SignedObject.

More importantly, for flexibility reasons, the
constructor and

verify

method allow for
customized signature engines, which can implement signature
algorithms that are not installed formally as part of a crypto
provider. However, it is crucial that the programmer writing the
verifier code be aware what

Signature

engine is being
used, as its own implementation of the

verify

method
is invoked to verify a signature. In other words, a malicious

Signature

may choose to always return true on
verification in an attempt to bypass a security check.

The signature algorithm can be, among others, the NIST standard
DSA, using DSA and SHA-256. The algorithm is specified using the
same convention as that for signatures. The DSA algorithm using the
SHA-256 message digest algorithm can be specified, for example, as
"SHA256withDSA". In the case of
RSA the signing algorithm could be specified as, for example,
"SHA256withRSA". The algorithm name must be
specified, as there is no default.

The name of the Cryptography Package Provider is designated
also by the Signature parameter to the constructor and the

verify

method. If the provider is not
specified, the default provider is used. Each installation can
be configured to use a particular provider as default.

Potential applications of SignedObject include:

- It can be used
internally to any Java runtime as an unforgeable authorization
token -- one that can be passed around without the fear that the
token can be maliciously modified without being detected.

It
can be used to sign and serialize data/object for storage outside
the Java runtime (e.g., storing critical access control data on
disk).

Nested SignedObjects can be used to construct a logical
sequence of signatures, resembling a chain of authorization and
delegation.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public SignedObject​(
Serializable
object,

PrivateKey
signingKey,

Signature
signingEngine)
throws
IOException
,

InvalidKeyException
,

SignatureException

Constructs a SignedObject from any Serializable object.
The given object is signed with the given signing key, using the
designated signature engine.

**Parameters:**
- object

- the object to be signed.
- signingKey

- the private key for signing.
- signingEngine

- the signature signing engine.

**Throws:**
- IOException

- if an error occurs during serialization
- InvalidKeyException

- if the key is invalid.
- SignatureException

- if signing fails.

---

### Method Details

#### public
Object
getObject()
throws
IOException
,

ClassNotFoundException

Retrieves the encapsulated object.
The encapsulated object is de-serialized before it is returned.

**Returns:**
- the encapsulated object.

**Throws:**
- IOException

- if an error occurs during de-serialization
- ClassNotFoundException

- if an error occurs during
de-serialization

---

#### public byte[] getSignature()

Retrieves the signature on the signed object, in the form of a
byte array.

**Returns:**
- the signature. Returns a new array each time this
method is called.

---

#### public
String
getAlgorithm()

Retrieves the name of the signature algorithm.

**Returns:**
- the signature algorithm name.

---

#### public boolean verify​(
PublicKey
verificationKey,

Signature
verificationEngine)
throws
InvalidKeyException
,

SignatureException

Verifies that the signature in this SignedObject is the valid
signature for the object stored inside, with the given
verification key, using the designated verification engine.

**Parameters:**
- verificationKey

- the public key for verification.
- verificationEngine

- the signature verification engine.

**Returns:**
- true

if the signature
is valid,

false

otherwise

**Throws:**
- SignatureException

- if signature verification failed (an
exception prevented the signature verification engine from completing
normally).
- InvalidKeyException

- if the verification key is invalid.

---

### Additional Sections

#### Class SignedObject

java.lang.Object

- java.security.SignedObject

java.security.SignedObject

**All Implemented Interfaces:** Serializable

```java
public final class
SignedObject

extends
Object

implements
Serializable
```

SignedObject is a class for the purpose of creating authentic
runtime objects whose integrity cannot be compromised without being
detected.

More specifically, a SignedObject contains another Serializable
object, the (to-be-)signed object and its signature.

The signed object is a "deep copy" (in serialized form) of an
original object. Once the copy is made, further manipulation of
the original object has no side effect on the copy.

The underlying signing algorithm is designated by the Signature
object passed to the constructor and the

verify

method.
A typical usage for signing is the following:

```java
Signature signingEngine = Signature.getInstance(algorithm,
provider);
SignedObject so = new SignedObject(myobject, signingKey,
signingEngine);
```

A typical usage for verification is the following (having
received SignedObject

so

):

```java
Signature verificationEngine =
Signature.getInstance(algorithm, provider);
if (so.verify(publickey, verificationEngine))
try {
Object myobj = so.getObject();
} catch (java.lang.ClassNotFoundException e) {};
```

Several points are worth noting. First, there is no need to
initialize the signing or verification engine, as it will be
re-initialized inside the constructor and the

verify

method. Secondly, for verification to succeed, the specified
public key must be the public key corresponding to the private key
used to generate the SignedObject.

More importantly, for flexibility reasons, the
constructor and

verify

method allow for
customized signature engines, which can implement signature
algorithms that are not installed formally as part of a crypto
provider. However, it is crucial that the programmer writing the
verifier code be aware what

Signature

engine is being
used, as its own implementation of the

verify

method
is invoked to verify a signature. In other words, a malicious

Signature

may choose to always return true on
verification in an attempt to bypass a security check.

The signature algorithm can be, among others, the NIST standard
DSA, using DSA and SHA-256. The algorithm is specified using the
same convention as that for signatures. The DSA algorithm using the
SHA-256 message digest algorithm can be specified, for example, as
"SHA256withDSA". In the case of
RSA the signing algorithm could be specified as, for example,
"SHA256withRSA". The algorithm name must be
specified, as there is no default.

The name of the Cryptography Package Provider is designated
also by the Signature parameter to the constructor and the

verify

method. If the provider is not
specified, the default provider is used. Each installation can
be configured to use a particular provider as default.

Potential applications of SignedObject include:

- It can be used
internally to any Java runtime as an unforgeable authorization
token -- one that can be passed around without the fear that the
token can be maliciously modified without being detected.

It
can be used to sign and serialize data/object for storage outside
the Java runtime (e.g., storing critical access control data on
disk).

Nested SignedObjects can be used to construct a logical
sequence of signatures, resembling a chain of authorization and
delegation.

**Since:** 1.2
**See Also:** Signature

,

Serialized Form

public final class

SignedObject

extends

Object

implements

Serializable

SignedObject is a class for the purpose of creating authentic
runtime objects whose integrity cannot be compromised without being
detected.

More specifically, a SignedObject contains another Serializable
object, the (to-be-)signed object and its signature.

The signed object is a "deep copy" (in serialized form) of an
original object. Once the copy is made, further manipulation of
the original object has no side effect on the copy.

The underlying signing algorithm is designated by the Signature
object passed to the constructor and the

verify

method.
A typical usage for signing is the following:

```java
Signature signingEngine = Signature.getInstance(algorithm,
provider);
SignedObject so = new SignedObject(myobject, signingKey,
signingEngine);
```

A typical usage for verification is the following (having
received SignedObject

so

):

```java
Signature verificationEngine =
Signature.getInstance(algorithm, provider);
if (so.verify(publickey, verificationEngine))
try {
Object myobj = so.getObject();
} catch (java.lang.ClassNotFoundException e) {};
```

Several points are worth noting. First, there is no need to
initialize the signing or verification engine, as it will be
re-initialized inside the constructor and the

verify

method. Secondly, for verification to succeed, the specified
public key must be the public key corresponding to the private key
used to generate the SignedObject.

More importantly, for flexibility reasons, the
constructor and

verify

method allow for
customized signature engines, which can implement signature
algorithms that are not installed formally as part of a crypto
provider. However, it is crucial that the programmer writing the
verifier code be aware what

Signature

engine is being
used, as its own implementation of the

verify

method
is invoked to verify a signature. In other words, a malicious

Signature

may choose to always return true on
verification in an attempt to bypass a security check.

The signature algorithm can be, among others, the NIST standard
DSA, using DSA and SHA-256. The algorithm is specified using the
same convention as that for signatures. The DSA algorithm using the
SHA-256 message digest algorithm can be specified, for example, as
"SHA256withDSA". In the case of
RSA the signing algorithm could be specified as, for example,
"SHA256withRSA". The algorithm name must be
specified, as there is no default.

The name of the Cryptography Package Provider is designated
also by the Signature parameter to the constructor and the

verify

method. If the provider is not
specified, the default provider is used. Each installation can
be configured to use a particular provider as default.

Potential applications of SignedObject include:

- It can be used
internally to any Java runtime as an unforgeable authorization
token -- one that can be passed around without the fear that the
token can be maliciously modified without being detected.

It
can be used to sign and serialize data/object for storage outside
the Java runtime (e.g., storing critical access control data on
disk).

Nested SignedObjects can be used to construct a logical
sequence of signatures, resembling a chain of authorization and
delegation.

More specifically, a SignedObject contains another Serializable
object, the (to-be-)signed object and its signature.

The signed object is a "deep copy" (in serialized form) of an
original object. Once the copy is made, further manipulation of
the original object has no side effect on the copy.

The underlying signing algorithm is designated by the Signature
object passed to the constructor and the

verify

method.
A typical usage for signing is the following:

```java
Signature signingEngine = Signature.getInstance(algorithm,
provider);
SignedObject so = new SignedObject(myobject, signingKey,
signingEngine);
```

A typical usage for verification is the following (having
received SignedObject

so

):

```java
Signature verificationEngine =
Signature.getInstance(algorithm, provider);
if (so.verify(publickey, verificationEngine))
try {
Object myobj = so.getObject();
} catch (java.lang.ClassNotFoundException e) {};
```

Several points are worth noting. First, there is no need to
initialize the signing or verification engine, as it will be
re-initialized inside the constructor and the

verify

method. Secondly, for verification to succeed, the specified
public key must be the public key corresponding to the private key
used to generate the SignedObject.

More importantly, for flexibility reasons, the
constructor and

verify

method allow for
customized signature engines, which can implement signature
algorithms that are not installed formally as part of a crypto
provider. However, it is crucial that the programmer writing the
verifier code be aware what

Signature

engine is being
used, as its own implementation of the

verify

method
is invoked to verify a signature. In other words, a malicious

Signature

may choose to always return true on
verification in an attempt to bypass a security check.

The signature algorithm can be, among others, the NIST standard
DSA, using DSA and SHA-256. The algorithm is specified using the
same convention as that for signatures. The DSA algorithm using the
SHA-256 message digest algorithm can be specified, for example, as
"SHA256withDSA". In the case of
RSA the signing algorithm could be specified as, for example,
"SHA256withRSA". The algorithm name must be
specified, as there is no default.

The name of the Cryptography Package Provider is designated
also by the Signature parameter to the constructor and the

verify

method. If the provider is not
specified, the default provider is used. Each installation can
be configured to use a particular provider as default.

Potential applications of SignedObject include:

- It can be used
internally to any Java runtime as an unforgeable authorization
token -- one that can be passed around without the fear that the
token can be maliciously modified without being detected.

It
can be used to sign and serialize data/object for storage outside
the Java runtime (e.g., storing critical access control data on
disk).

Nested SignedObjects can be used to construct a logical
sequence of signatures, resembling a chain of authorization and
delegation.

The signed object is a "deep copy" (in serialized form) of an
original object. Once the copy is made, further manipulation of
the original object has no side effect on the copy.

The underlying signing algorithm is designated by the Signature
object passed to the constructor and the

verify

method.
A typical usage for signing is the following:

```java
Signature signingEngine = Signature.getInstance(algorithm,
provider);
SignedObject so = new SignedObject(myobject, signingKey,
signingEngine);
```

A typical usage for verification is the following (having
received SignedObject

so

):

```java
Signature verificationEngine =
Signature.getInstance(algorithm, provider);
if (so.verify(publickey, verificationEngine))
try {
Object myobj = so.getObject();
} catch (java.lang.ClassNotFoundException e) {};
```

Several points are worth noting. First, there is no need to
initialize the signing or verification engine, as it will be
re-initialized inside the constructor and the

verify

method. Secondly, for verification to succeed, the specified
public key must be the public key corresponding to the private key
used to generate the SignedObject.

More importantly, for flexibility reasons, the
constructor and

verify

method allow for
customized signature engines, which can implement signature
algorithms that are not installed formally as part of a crypto
provider. However, it is crucial that the programmer writing the
verifier code be aware what

Signature

engine is being
used, as its own implementation of the

verify

method
is invoked to verify a signature. In other words, a malicious

Signature

may choose to always return true on
verification in an attempt to bypass a security check.

The signature algorithm can be, among others, the NIST standard
DSA, using DSA and SHA-256. The algorithm is specified using the
same convention as that for signatures. The DSA algorithm using the
SHA-256 message digest algorithm can be specified, for example, as
"SHA256withDSA". In the case of
RSA the signing algorithm could be specified as, for example,
"SHA256withRSA". The algorithm name must be
specified, as there is no default.

The name of the Cryptography Package Provider is designated
also by the Signature parameter to the constructor and the

verify

method. If the provider is not
specified, the default provider is used. Each installation can
be configured to use a particular provider as default.

Potential applications of SignedObject include:

- It can be used
internally to any Java runtime as an unforgeable authorization
token -- one that can be passed around without the fear that the
token can be maliciously modified without being detected.

It
can be used to sign and serialize data/object for storage outside
the Java runtime (e.g., storing critical access control data on
disk).

Nested SignedObjects can be used to construct a logical
sequence of signatures, resembling a chain of authorization and
delegation.

The underlying signing algorithm is designated by the Signature
object passed to the constructor and the

verify

method.
A typical usage for signing is the following:

```java
Signature signingEngine = Signature.getInstance(algorithm,
provider);
SignedObject so = new SignedObject(myobject, signingKey,
signingEngine);
```

A typical usage for verification is the following (having
received SignedObject

so

):

```java
Signature verificationEngine =
Signature.getInstance(algorithm, provider);
if (so.verify(publickey, verificationEngine))
try {
Object myobj = so.getObject();
} catch (java.lang.ClassNotFoundException e) {};
```

Several points are worth noting. First, there is no need to
initialize the signing or verification engine, as it will be
re-initialized inside the constructor and the

verify

method. Secondly, for verification to succeed, the specified
public key must be the public key corresponding to the private key
used to generate the SignedObject.

More importantly, for flexibility reasons, the
constructor and

verify

method allow for
customized signature engines, which can implement signature
algorithms that are not installed formally as part of a crypto
provider. However, it is crucial that the programmer writing the
verifier code be aware what

Signature

engine is being
used, as its own implementation of the

verify

method
is invoked to verify a signature. In other words, a malicious

Signature

may choose to always return true on
verification in an attempt to bypass a security check.

The signature algorithm can be, among others, the NIST standard
DSA, using DSA and SHA-256. The algorithm is specified using the
same convention as that for signatures. The DSA algorithm using the
SHA-256 message digest algorithm can be specified, for example, as
"SHA256withDSA". In the case of
RSA the signing algorithm could be specified as, for example,
"SHA256withRSA". The algorithm name must be
specified, as there is no default.

The name of the Cryptography Package Provider is designated
also by the Signature parameter to the constructor and the

verify

method. If the provider is not
specified, the default provider is used. Each installation can
be configured to use a particular provider as default.

Potential applications of SignedObject include:

- It can be used
internally to any Java runtime as an unforgeable authorization
token -- one that can be passed around without the fear that the
token can be maliciously modified without being detected.

It
can be used to sign and serialize data/object for storage outside
the Java runtime (e.g., storing critical access control data on
disk).

Nested SignedObjects can be used to construct a logical
sequence of signatures, resembling a chain of authorization and
delegation.

Signature signingEngine = Signature.getInstance(algorithm,
provider);
SignedObject so = new SignedObject(myobject, signingKey,
signingEngine);

A typical usage for verification is the following (having
received SignedObject

so

):

```java
Signature verificationEngine =
Signature.getInstance(algorithm, provider);
if (so.verify(publickey, verificationEngine))
try {
Object myobj = so.getObject();
} catch (java.lang.ClassNotFoundException e) {};
```

Several points are worth noting. First, there is no need to
initialize the signing or verification engine, as it will be
re-initialized inside the constructor and the

verify

method. Secondly, for verification to succeed, the specified
public key must be the public key corresponding to the private key
used to generate the SignedObject.

More importantly, for flexibility reasons, the
constructor and

verify

method allow for
customized signature engines, which can implement signature
algorithms that are not installed formally as part of a crypto
provider. However, it is crucial that the programmer writing the
verifier code be aware what

Signature

engine is being
used, as its own implementation of the

verify

method
is invoked to verify a signature. In other words, a malicious

Signature

may choose to always return true on
verification in an attempt to bypass a security check.

The signature algorithm can be, among others, the NIST standard
DSA, using DSA and SHA-256. The algorithm is specified using the
same convention as that for signatures. The DSA algorithm using the
SHA-256 message digest algorithm can be specified, for example, as
"SHA256withDSA". In the case of
RSA the signing algorithm could be specified as, for example,
"SHA256withRSA". The algorithm name must be
specified, as there is no default.

The name of the Cryptography Package Provider is designated
also by the Signature parameter to the constructor and the

verify

method. If the provider is not
specified, the default provider is used. Each installation can
be configured to use a particular provider as default.

Potential applications of SignedObject include:

- It can be used
internally to any Java runtime as an unforgeable authorization
token -- one that can be passed around without the fear that the
token can be maliciously modified without being detected.

It
can be used to sign and serialize data/object for storage outside
the Java runtime (e.g., storing critical access control data on
disk).

Nested SignedObjects can be used to construct a logical
sequence of signatures, resembling a chain of authorization and
delegation.

Signature verificationEngine =
Signature.getInstance(algorithm, provider);
if (so.verify(publickey, verificationEngine))
try {
Object myobj = so.getObject();
} catch (java.lang.ClassNotFoundException e) {};

Several points are worth noting. First, there is no need to
initialize the signing or verification engine, as it will be
re-initialized inside the constructor and the

verify

method. Secondly, for verification to succeed, the specified
public key must be the public key corresponding to the private key
used to generate the SignedObject.

More importantly, for flexibility reasons, the
constructor and

verify

method allow for
customized signature engines, which can implement signature
algorithms that are not installed formally as part of a crypto
provider. However, it is crucial that the programmer writing the
verifier code be aware what

Signature

engine is being
used, as its own implementation of the

verify

method
is invoked to verify a signature. In other words, a malicious

Signature

may choose to always return true on
verification in an attempt to bypass a security check.

The signature algorithm can be, among others, the NIST standard
DSA, using DSA and SHA-256. The algorithm is specified using the
same convention as that for signatures. The DSA algorithm using the
SHA-256 message digest algorithm can be specified, for example, as
"SHA256withDSA". In the case of
RSA the signing algorithm could be specified as, for example,
"SHA256withRSA". The algorithm name must be
specified, as there is no default.

The name of the Cryptography Package Provider is designated
also by the Signature parameter to the constructor and the

verify

method. If the provider is not
specified, the default provider is used. Each installation can
be configured to use a particular provider as default.

Potential applications of SignedObject include:

- It can be used
internally to any Java runtime as an unforgeable authorization
token -- one that can be passed around without the fear that the
token can be maliciously modified without being detected.

It
can be used to sign and serialize data/object for storage outside
the Java runtime (e.g., storing critical access control data on
disk).

Nested SignedObjects can be used to construct a logical
sequence of signatures, resembling a chain of authorization and
delegation.

More importantly, for flexibility reasons, the
constructor and

verify

method allow for
customized signature engines, which can implement signature
algorithms that are not installed formally as part of a crypto
provider. However, it is crucial that the programmer writing the
verifier code be aware what

Signature

engine is being
used, as its own implementation of the

verify

method
is invoked to verify a signature. In other words, a malicious

Signature

may choose to always return true on
verification in an attempt to bypass a security check.

The signature algorithm can be, among others, the NIST standard
DSA, using DSA and SHA-256. The algorithm is specified using the
same convention as that for signatures. The DSA algorithm using the
SHA-256 message digest algorithm can be specified, for example, as
"SHA256withDSA". In the case of
RSA the signing algorithm could be specified as, for example,
"SHA256withRSA". The algorithm name must be
specified, as there is no default.

The name of the Cryptography Package Provider is designated
also by the Signature parameter to the constructor and the

verify

method. If the provider is not
specified, the default provider is used. Each installation can
be configured to use a particular provider as default.

Potential applications of SignedObject include:

- It can be used
internally to any Java runtime as an unforgeable authorization
token -- one that can be passed around without the fear that the
token can be maliciously modified without being detected.

It
can be used to sign and serialize data/object for storage outside
the Java runtime (e.g., storing critical access control data on
disk).

Nested SignedObjects can be used to construct a logical
sequence of signatures, resembling a chain of authorization and
delegation.

The signature algorithm can be, among others, the NIST standard
DSA, using DSA and SHA-256. The algorithm is specified using the
same convention as that for signatures. The DSA algorithm using the
SHA-256 message digest algorithm can be specified, for example, as
"SHA256withDSA". In the case of
RSA the signing algorithm could be specified as, for example,
"SHA256withRSA". The algorithm name must be
specified, as there is no default.

The name of the Cryptography Package Provider is designated
also by the Signature parameter to the constructor and the

verify

method. If the provider is not
specified, the default provider is used. Each installation can
be configured to use a particular provider as default.

Potential applications of SignedObject include:

- It can be used
internally to any Java runtime as an unforgeable authorization
token -- one that can be passed around without the fear that the
token can be maliciously modified without being detected.

It
can be used to sign and serialize data/object for storage outside
the Java runtime (e.g., storing critical access control data on
disk).

Nested SignedObjects can be used to construct a logical
sequence of signatures, resembling a chain of authorization and
delegation.

The name of the Cryptography Package Provider is designated
also by the Signature parameter to the constructor and the

verify

method. If the provider is not
specified, the default provider is used. Each installation can
be configured to use a particular provider as default.

Potential applications of SignedObject include:

- It can be used
internally to any Java runtime as an unforgeable authorization
token -- one that can be passed around without the fear that the
token can be maliciously modified without being detected.

It
can be used to sign and serialize data/object for storage outside
the Java runtime (e.g., storing critical access control data on
disk).

Nested SignedObjects can be used to construct a logical
sequence of signatures, resembling a chain of authorization and
delegation.

Potential applications of SignedObject include:

- It can be used
internally to any Java runtime as an unforgeable authorization
token -- one that can be passed around without the fear that the
token can be maliciously modified without being detected.

It
can be used to sign and serialize data/object for storage outside
the Java runtime (e.g., storing critical access control data on
disk).

Nested SignedObjects can be used to construct a logical
sequence of signatures, resembling a chain of authorization and
delegation.

It can be used
internally to any Java runtime as an unforgeable authorization
token -- one that can be passed around without the fear that the
token can be maliciously modified without being detected.

It
can be used to sign and serialize data/object for storage outside
the Java runtime (e.g., storing critical access control data on
disk).

Nested SignedObjects can be used to construct a logical
sequence of signatures, resembling a chain of authorization and
delegation.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SignedObject

​(

Serializable

object,

PrivateKey

signingKey,

Signature

signingEngine)

Constructs a SignedObject from any Serializable object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getAlgorithm

()

Retrieves the name of the signature algorithm.

Object

getObject

()

Retrieves the encapsulated object.

byte[]

getSignature

()

Retrieves the signature on the signed object, in the form of a
byte array.

boolean

verify

​(

PublicKey

verificationKey,

Signature

verificationEngine)

Verifies that the signature in this SignedObject is the valid
signature for the object stored inside, with the given
verification key, using the designated verification engine.

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

SignedObject

​(

Serializable

object,

PrivateKey

signingKey,

Signature

signingEngine)

Constructs a SignedObject from any Serializable object.

---

#### Constructor Summary

Constructs a SignedObject from any Serializable object.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getAlgorithm

()

Retrieves the name of the signature algorithm.

Object

getObject

()

Retrieves the encapsulated object.

byte[]

getSignature

()

Retrieves the signature on the signed object, in the form of a
byte array.

boolean

verify

​(

PublicKey

verificationKey,

Signature

verificationEngine)

Verifies that the signature in this SignedObject is the valid
signature for the object stored inside, with the given
verification key, using the designated verification engine.

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

Retrieves the name of the signature algorithm.

Retrieves the encapsulated object.

Retrieves the signature on the signed object, in the form of a
byte array.

Verifies that the signature in this SignedObject is the valid
signature for the object stored inside, with the given
verification key, using the designated verification engine.

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

- SignedObject

```java
public SignedObject​(
Serializable
object,

PrivateKey
signingKey,

Signature
signingEngine)
throws
IOException
,

InvalidKeyException
,

SignatureException
```

Constructs a SignedObject from any Serializable object.
The given object is signed with the given signing key, using the
designated signature engine.

**Parameters:** object

- the object to be signed.
**Parameters:** signingKey

- the private key for signing.
**Parameters:** signingEngine

- the signature signing engine.
**Throws:** IOException

- if an error occurs during serialization
**Throws:** InvalidKeyException

- if the key is invalid.
**Throws:** SignatureException

- if signing fails.

============ METHOD DETAIL ==========

- Method Detail

- getObject

```java
public
Object
getObject()
throws
IOException
,

ClassNotFoundException
```

Retrieves the encapsulated object.
The encapsulated object is de-serialized before it is returned.

**Returns:** the encapsulated object.
**Throws:** IOException

- if an error occurs during de-serialization
**Throws:** ClassNotFoundException

- if an error occurs during
de-serialization

- getSignature

```java
public byte[] getSignature()
```

Retrieves the signature on the signed object, in the form of a
byte array.

**Returns:** the signature. Returns a new array each time this
method is called.

- getAlgorithm

```java
public
String
getAlgorithm()
```

Retrieves the name of the signature algorithm.

**Returns:** the signature algorithm name.

- verify

```java
public boolean verify​(
PublicKey
verificationKey,

Signature
verificationEngine)
throws
InvalidKeyException
,

SignatureException
```

Verifies that the signature in this SignedObject is the valid
signature for the object stored inside, with the given
verification key, using the designated verification engine.

**Parameters:** verificationKey

- the public key for verification.
**Parameters:** verificationEngine

- the signature verification engine.
**Returns:** true

if the signature
is valid,

false

otherwise
**Throws:** SignatureException

- if signature verification failed (an
exception prevented the signature verification engine from completing
normally).
**Throws:** InvalidKeyException

- if the verification key is invalid.

Constructor Detail

- SignedObject

```java
public SignedObject​(
Serializable
object,

PrivateKey
signingKey,

Signature
signingEngine)
throws
IOException
,

InvalidKeyException
,

SignatureException
```

Constructs a SignedObject from any Serializable object.
The given object is signed with the given signing key, using the
designated signature engine.

**Parameters:** object

- the object to be signed.
**Parameters:** signingKey

- the private key for signing.
**Parameters:** signingEngine

- the signature signing engine.
**Throws:** IOException

- if an error occurs during serialization
**Throws:** InvalidKeyException

- if the key is invalid.
**Throws:** SignatureException

- if signing fails.

---

#### Constructor Detail

SignedObject

```java
public SignedObject​(
Serializable
object,

PrivateKey
signingKey,

Signature
signingEngine)
throws
IOException
,

InvalidKeyException
,

SignatureException
```

Constructs a SignedObject from any Serializable object.
The given object is signed with the given signing key, using the
designated signature engine.

**Parameters:** object

- the object to be signed.
**Parameters:** signingKey

- the private key for signing.
**Parameters:** signingEngine

- the signature signing engine.
**Throws:** IOException

- if an error occurs during serialization
**Throws:** InvalidKeyException

- if the key is invalid.
**Throws:** SignatureException

- if signing fails.

---

#### SignedObject

public SignedObject​(

Serializable

object,

PrivateKey

signingKey,

Signature

signingEngine)
throws

IOException

,

InvalidKeyException

,

SignatureException

Constructs a SignedObject from any Serializable object.
The given object is signed with the given signing key, using the
designated signature engine.

Method Detail

- getObject

```java
public
Object
getObject()
throws
IOException
,

ClassNotFoundException
```

Retrieves the encapsulated object.
The encapsulated object is de-serialized before it is returned.

**Returns:** the encapsulated object.
**Throws:** IOException

- if an error occurs during de-serialization
**Throws:** ClassNotFoundException

- if an error occurs during
de-serialization

- getSignature

```java
public byte[] getSignature()
```

Retrieves the signature on the signed object, in the form of a
byte array.

**Returns:** the signature. Returns a new array each time this
method is called.

- getAlgorithm

```java
public
String
getAlgorithm()
```

Retrieves the name of the signature algorithm.

**Returns:** the signature algorithm name.

- verify

```java
public boolean verify​(
PublicKey
verificationKey,

Signature
verificationEngine)
throws
InvalidKeyException
,

SignatureException
```

Verifies that the signature in this SignedObject is the valid
signature for the object stored inside, with the given
verification key, using the designated verification engine.

**Parameters:** verificationKey

- the public key for verification.
**Parameters:** verificationEngine

- the signature verification engine.
**Returns:** true

if the signature
is valid,

false

otherwise
**Throws:** SignatureException

- if signature verification failed (an
exception prevented the signature verification engine from completing
normally).
**Throws:** InvalidKeyException

- if the verification key is invalid.

---

#### Method Detail

getObject

```java
public
Object
getObject()
throws
IOException
,

ClassNotFoundException
```

Retrieves the encapsulated object.
The encapsulated object is de-serialized before it is returned.

**Returns:** the encapsulated object.
**Throws:** IOException

- if an error occurs during de-serialization
**Throws:** ClassNotFoundException

- if an error occurs during
de-serialization

---

#### getObject

public

Object

getObject()
throws

IOException

,

ClassNotFoundException

Retrieves the encapsulated object.
The encapsulated object is de-serialized before it is returned.

getSignature

```java
public byte[] getSignature()
```

Retrieves the signature on the signed object, in the form of a
byte array.

**Returns:** the signature. Returns a new array each time this
method is called.

---

#### getSignature

public byte[] getSignature()

Retrieves the signature on the signed object, in the form of a
byte array.

getAlgorithm

```java
public
String
getAlgorithm()
```

Retrieves the name of the signature algorithm.

**Returns:** the signature algorithm name.

---

#### getAlgorithm

public

String

getAlgorithm()

Retrieves the name of the signature algorithm.

verify

```java
public boolean verify​(
PublicKey
verificationKey,

Signature
verificationEngine)
throws
InvalidKeyException
,

SignatureException
```

Verifies that the signature in this SignedObject is the valid
signature for the object stored inside, with the given
verification key, using the designated verification engine.

**Parameters:** verificationKey

- the public key for verification.
**Parameters:** verificationEngine

- the signature verification engine.
**Returns:** true

if the signature
is valid,

false

otherwise
**Throws:** SignatureException

- if signature verification failed (an
exception prevented the signature verification engine from completing
normally).
**Throws:** InvalidKeyException

- if the verification key is invalid.

---

#### verify

public boolean verify​(

PublicKey

verificationKey,

Signature

verificationEngine)
throws

InvalidKeyException

,

SignatureException

Verifies that the signature in this SignedObject is the valid
signature for the object stored inside, with the given
verification key, using the designated verification engine.

---

