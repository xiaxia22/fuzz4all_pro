# Class SealedObject

**Source:** `java.base\javax\crypto\SealedObject.html`

### Class Description

```java
public class
SealedObject

extends
Object

implements
Serializable
```

This class enables a programmer to create an object and protect its
confidentiality with a cryptographic algorithm.

Given any Serializable object, one can create a SealedObject
that encapsulates the original object, in serialized
format (i.e., a "deep copy"), and seals (encrypts) its serialized contents,
using a cryptographic algorithm such as AES, to protect its
confidentiality. The encrypted content can later be decrypted (with
the corresponding algorithm using the correct decryption key) and
de-serialized, yielding the original object.

Note that the Cipher object must be fully initialized with the
correct algorithm, key, padding scheme, etc., before being applied
to a SealedObject.

The original object that was sealed can be recovered in two different
ways:

- by using the

getObject

method that takes a

Cipher

object.

This method requires a fully initialized

Cipher

object,
initialized with the
exact same algorithm, key, padding scheme, etc., that were used to seal the
object.

This approach has the advantage that the party who unseals the
sealed object does not require knowledge of the decryption key. For example,
after one party has initialized the cipher object with the required
decryption key, it could hand over the cipher object to
another party who then unseals the sealed object.

by using one of the

getObject

methods
that take a

Key

object.

In this approach, the

getObject

method creates a cipher
object for the appropriate decryption algorithm and initializes it with the
given decryption key and the algorithm parameters (if any) that were stored
in the sealed object.

This approach has the advantage that the party who
unseals the object does not need to keep track of the parameters (e.g., an
IV) that were used to seal the object.

**All Implemented Interfaces:** Serializable

---

### Field Details

#### protected byte[] encodedParams

The cryptographic parameters used by the sealing Cipher,
encoded in the default format.

That is,

cipher.getParameters().getEncoded()

.

---

### Constructor Details

#### public SealedObject​(
Serializable
object,

Cipher
c)
throws
IOException
,

IllegalBlockSizeException

Constructs a SealedObject from any Serializable object.

The given object is serialized, and its serialized contents are
encrypted using the given Cipher, which must be fully initialized.

Any algorithm parameters that may be used in the encryption
operation are stored inside of the new

SealedObject

.

**Parameters:**
- object

- the object to be sealed; can be null.
- c

- the cipher used to seal the object.

**Throws:**
- NullPointerException

- if the given cipher is null.
- IOException

- if an error occurs during serialization
- IllegalBlockSizeException

- if the given cipher is a block
cipher, no padding has been requested, and the total input length
(i.e., the length of the serialized object contents) is not a multiple
of the cipher's block size

---

#### protected SealedObject​(
SealedObject
so)

Constructs a SealedObject object from the passed-in SealedObject.

**Parameters:**
- so

- a SealedObject object

**Throws:**
- NullPointerException

- if the given sealed object is null.

---

### Method Details

#### public final
String
getAlgorithm()

Returns the algorithm that was used to seal this object.

**Returns:**
- the algorithm that was used to seal this object.

---

#### public final
Object
getObject​(
Key
key)
throws
IOException
,

ClassNotFoundException
,

NoSuchAlgorithmException
,

InvalidKeyException

Retrieves the original (encapsulated) object.

This method creates a cipher for the algorithm that had been used in
the sealing operation.
If the default provider package provides an implementation of that
algorithm, an instance of Cipher containing that implementation is used.
If the algorithm is not available in the default package, other
packages are searched.
The Cipher object is initialized for decryption, using the given

key

and the parameters (if any) that had been used in the
sealing operation.

The encapsulated object is unsealed and de-serialized, before it is
returned.

**Parameters:**
- key

- the key used to unseal the object.

**Returns:**
- the original object.

**Throws:**
- IOException

- if an error occurs during de-serialiazation.
- ClassNotFoundException

- if an error occurs during
de-serialiazation.
- NoSuchAlgorithmException

- if the algorithm to unseal the
object is not available.
- InvalidKeyException

- if the given key cannot be used to unseal
the object (e.g., it has the wrong algorithm).
- NullPointerException

- if

key

is null.

---

#### public final
Object
getObject​(
Cipher
c)
throws
IOException
,

ClassNotFoundException
,

IllegalBlockSizeException
,

BadPaddingException

Retrieves the original (encapsulated) object.

The encapsulated object is unsealed (using the given Cipher,
assuming that the Cipher is already properly initialized) and
de-serialized, before it is returned.

**Parameters:**
- c

- the cipher used to unseal the object

**Returns:**
- the original object.

**Throws:**
- NullPointerException

- if the given cipher is null.
- IOException

- if an error occurs during de-serialiazation
- ClassNotFoundException

- if an error occurs during
de-serialiazation
- IllegalBlockSizeException

- if the given cipher is a block
cipher, no padding has been requested, and the total input length is
not a multiple of the cipher's block size
- BadPaddingException

- if the given cipher has been
initialized for decryption, and padding has been specified, but
the input data does not have proper expected padding bytes

---

#### public final
Object
getObject​(
Key
key,

String
provider)
throws
IOException
,

ClassNotFoundException
,

NoSuchAlgorithmException
,

NoSuchProviderException
,

InvalidKeyException

Retrieves the original (encapsulated) object.

This method creates a cipher for the algorithm that had been used in
the sealing operation, using an implementation of that algorithm from
the given

provider

.
The Cipher object is initialized for decryption, using the given

key

and the parameters (if any) that had been used in the
sealing operation.

The encapsulated object is unsealed and de-serialized, before it is
returned.

**Parameters:**
- key

- the key used to unseal the object.
- provider

- the name of the provider of the algorithm to unseal
the object.

**Returns:**
- the original object.

**Throws:**
- IllegalArgumentException

- if the given provider is null
or empty.
- IOException

- if an error occurs during de-serialiazation.
- ClassNotFoundException

- if an error occurs during
de-serialiazation.
- NoSuchAlgorithmException

- if the algorithm to unseal the
object is not available.
- NoSuchProviderException

- if the given provider is not
configured.
- InvalidKeyException

- if the given key cannot be used to unseal
the object (e.g., it has the wrong algorithm).
- NullPointerException

- if

key

is null.

---

### Additional Sections

#### Class SealedObject

java.lang.Object

- javax.crypto.SealedObject

javax.crypto.SealedObject

**All Implemented Interfaces:** Serializable

```java
public class
SealedObject

extends
Object

implements
Serializable
```

This class enables a programmer to create an object and protect its
confidentiality with a cryptographic algorithm.

Given any Serializable object, one can create a SealedObject
that encapsulates the original object, in serialized
format (i.e., a "deep copy"), and seals (encrypts) its serialized contents,
using a cryptographic algorithm such as AES, to protect its
confidentiality. The encrypted content can later be decrypted (with
the corresponding algorithm using the correct decryption key) and
de-serialized, yielding the original object.

Note that the Cipher object must be fully initialized with the
correct algorithm, key, padding scheme, etc., before being applied
to a SealedObject.

The original object that was sealed can be recovered in two different
ways:

- by using the

getObject

method that takes a

Cipher

object.

This method requires a fully initialized

Cipher

object,
initialized with the
exact same algorithm, key, padding scheme, etc., that were used to seal the
object.

This approach has the advantage that the party who unseals the
sealed object does not require knowledge of the decryption key. For example,
after one party has initialized the cipher object with the required
decryption key, it could hand over the cipher object to
another party who then unseals the sealed object.

by using one of the

getObject

methods
that take a

Key

object.

In this approach, the

getObject

method creates a cipher
object for the appropriate decryption algorithm and initializes it with the
given decryption key and the algorithm parameters (if any) that were stored
in the sealed object.

This approach has the advantage that the party who
unseals the object does not need to keep track of the parameters (e.g., an
IV) that were used to seal the object.

**Since:** 1.4
**See Also:** Cipher

,

Serialized Form

public class

SealedObject

extends

Object

implements

Serializable

This class enables a programmer to create an object and protect its
confidentiality with a cryptographic algorithm.

Given any Serializable object, one can create a SealedObject
that encapsulates the original object, in serialized
format (i.e., a "deep copy"), and seals (encrypts) its serialized contents,
using a cryptographic algorithm such as AES, to protect its
confidentiality. The encrypted content can later be decrypted (with
the corresponding algorithm using the correct decryption key) and
de-serialized, yielding the original object.

Note that the Cipher object must be fully initialized with the
correct algorithm, key, padding scheme, etc., before being applied
to a SealedObject.

The original object that was sealed can be recovered in two different
ways:

- by using the

getObject

method that takes a

Cipher

object.

This method requires a fully initialized

Cipher

object,
initialized with the
exact same algorithm, key, padding scheme, etc., that were used to seal the
object.

This approach has the advantage that the party who unseals the
sealed object does not require knowledge of the decryption key. For example,
after one party has initialized the cipher object with the required
decryption key, it could hand over the cipher object to
another party who then unseals the sealed object.

by using one of the

getObject

methods
that take a

Key

object.

In this approach, the

getObject

method creates a cipher
object for the appropriate decryption algorithm and initializes it with the
given decryption key and the algorithm parameters (if any) that were stored
in the sealed object.

This approach has the advantage that the party who
unseals the object does not need to keep track of the parameters (e.g., an
IV) that were used to seal the object.

Given any Serializable object, one can create a SealedObject
that encapsulates the original object, in serialized
format (i.e., a "deep copy"), and seals (encrypts) its serialized contents,
using a cryptographic algorithm such as AES, to protect its
confidentiality. The encrypted content can later be decrypted (with
the corresponding algorithm using the correct decryption key) and
de-serialized, yielding the original object.

Note that the Cipher object must be fully initialized with the
correct algorithm, key, padding scheme, etc., before being applied
to a SealedObject.

The original object that was sealed can be recovered in two different
ways:

- by using the

getObject

method that takes a

Cipher

object.

This method requires a fully initialized

Cipher

object,
initialized with the
exact same algorithm, key, padding scheme, etc., that were used to seal the
object.

This approach has the advantage that the party who unseals the
sealed object does not require knowledge of the decryption key. For example,
after one party has initialized the cipher object with the required
decryption key, it could hand over the cipher object to
another party who then unseals the sealed object.

by using one of the

getObject

methods
that take a

Key

object.

In this approach, the

getObject

method creates a cipher
object for the appropriate decryption algorithm and initializes it with the
given decryption key and the algorithm parameters (if any) that were stored
in the sealed object.

This approach has the advantage that the party who
unseals the object does not need to keep track of the parameters (e.g., an
IV) that were used to seal the object.

Note that the Cipher object must be fully initialized with the
correct algorithm, key, padding scheme, etc., before being applied
to a SealedObject.

The original object that was sealed can be recovered in two different
ways:

- by using the

getObject

method that takes a

Cipher

object.

This method requires a fully initialized

Cipher

object,
initialized with the
exact same algorithm, key, padding scheme, etc., that were used to seal the
object.

This approach has the advantage that the party who unseals the
sealed object does not require knowledge of the decryption key. For example,
after one party has initialized the cipher object with the required
decryption key, it could hand over the cipher object to
another party who then unseals the sealed object.

by using one of the

getObject

methods
that take a

Key

object.

In this approach, the

getObject

method creates a cipher
object for the appropriate decryption algorithm and initializes it with the
given decryption key and the algorithm parameters (if any) that were stored
in the sealed object.

This approach has the advantage that the party who
unseals the object does not need to keep track of the parameters (e.g., an
IV) that were used to seal the object.

The original object that was sealed can be recovered in two different
ways:

- by using the

getObject

method that takes a

Cipher

object.

This method requires a fully initialized

Cipher

object,
initialized with the
exact same algorithm, key, padding scheme, etc., that were used to seal the
object.

This approach has the advantage that the party who unseals the
sealed object does not require knowledge of the decryption key. For example,
after one party has initialized the cipher object with the required
decryption key, it could hand over the cipher object to
another party who then unseals the sealed object.

by using one of the

getObject

methods
that take a

Key

object.

In this approach, the

getObject

method creates a cipher
object for the appropriate decryption algorithm and initializes it with the
given decryption key and the algorithm parameters (if any) that were stored
in the sealed object.

This approach has the advantage that the party who
unseals the object does not need to keep track of the parameters (e.g., an
IV) that were used to seal the object.

by using the

getObject

method that takes a

Cipher

object.

This method requires a fully initialized

Cipher

object,
initialized with the
exact same algorithm, key, padding scheme, etc., that were used to seal the
object.

This approach has the advantage that the party who unseals the
sealed object does not require knowledge of the decryption key. For example,
after one party has initialized the cipher object with the required
decryption key, it could hand over the cipher object to
another party who then unseals the sealed object.

by using one of the

getObject

methods
that take a

Key

object.

In this approach, the

getObject

method creates a cipher
object for the appropriate decryption algorithm and initializes it with the
given decryption key and the algorithm parameters (if any) that were stored
in the sealed object.

This approach has the advantage that the party who
unseals the object does not need to keep track of the parameters (e.g., an
IV) that were used to seal the object.

This method requires a fully initialized

Cipher

object,
initialized with the
exact same algorithm, key, padding scheme, etc., that were used to seal the
object.

This approach has the advantage that the party who unseals the
sealed object does not require knowledge of the decryption key. For example,
after one party has initialized the cipher object with the required
decryption key, it could hand over the cipher object to
another party who then unseals the sealed object.

by using one of the

getObject

methods
that take a

Key

object.

In this approach, the

getObject

method creates a cipher
object for the appropriate decryption algorithm and initializes it with the
given decryption key and the algorithm parameters (if any) that were stored
in the sealed object.

This approach has the advantage that the party who
unseals the object does not need to keep track of the parameters (e.g., an
IV) that were used to seal the object.

This approach has the advantage that the party who unseals the
sealed object does not require knowledge of the decryption key. For example,
after one party has initialized the cipher object with the required
decryption key, it could hand over the cipher object to
another party who then unseals the sealed object.

by using one of the

getObject

methods
that take a

Key

object.

In this approach, the

getObject

method creates a cipher
object for the appropriate decryption algorithm and initializes it with the
given decryption key and the algorithm parameters (if any) that were stored
in the sealed object.

This approach has the advantage that the party who
unseals the object does not need to keep track of the parameters (e.g., an
IV) that were used to seal the object.

In this approach, the

getObject

method creates a cipher
object for the appropriate decryption algorithm and initializes it with the
given decryption key and the algorithm parameters (if any) that were stored
in the sealed object.

This approach has the advantage that the party who
unseals the object does not need to keep track of the parameters (e.g., an
IV) that were used to seal the object.

This approach has the advantage that the party who
unseals the object does not need to keep track of the parameters (e.g., an
IV) that were used to seal the object.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected byte[]

encodedParams

The cryptographic parameters used by the sealing Cipher,
encoded in the default format.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

SealedObject

​(

Serializable

object,

Cipher

c)

Constructs a SealedObject from any Serializable object.

protected

SealedObject

​(

SealedObject

so)

Constructs a SealedObject object from the passed-in SealedObject.

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

Returns the algorithm that was used to seal this object.

Object

getObject

​(

Key

key)

Retrieves the original (encapsulated) object.

Object

getObject

​(

Key

key,

String

provider)

Retrieves the original (encapsulated) object.

Object

getObject

​(

Cipher

c)

Retrieves the original (encapsulated) object.

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

protected byte[]

encodedParams

The cryptographic parameters used by the sealing Cipher,
encoded in the default format.

---

#### Field Summary

The cryptographic parameters used by the sealing Cipher,
encoded in the default format.

Constructor Summary

Constructors

Modifier

Constructor

Description

SealedObject

​(

Serializable

object,

Cipher

c)

Constructs a SealedObject from any Serializable object.

protected

SealedObject

​(

SealedObject

so)

Constructs a SealedObject object from the passed-in SealedObject.

---

#### Constructor Summary

Constructs a SealedObject from any Serializable object.

Constructs a SealedObject object from the passed-in SealedObject.

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

Returns the algorithm that was used to seal this object.

Object

getObject

​(

Key

key)

Retrieves the original (encapsulated) object.

Object

getObject

​(

Key

key,

String

provider)

Retrieves the original (encapsulated) object.

Object

getObject

​(

Cipher

c)

Retrieves the original (encapsulated) object.

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

Returns the algorithm that was used to seal this object.

Retrieves the original (encapsulated) object.

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

- encodedParams

```java
protected byte[] encodedParams
```

The cryptographic parameters used by the sealing Cipher,
encoded in the default format.

That is,

cipher.getParameters().getEncoded()

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SealedObject

```java
public SealedObject​(
Serializable
object,

Cipher
c)
throws
IOException
,

IllegalBlockSizeException
```

Constructs a SealedObject from any Serializable object.

The given object is serialized, and its serialized contents are
encrypted using the given Cipher, which must be fully initialized.

Any algorithm parameters that may be used in the encryption
operation are stored inside of the new

SealedObject

.

**Parameters:** object

- the object to be sealed; can be null.
**Parameters:** c

- the cipher used to seal the object.
**Throws:** NullPointerException

- if the given cipher is null.
**Throws:** IOException

- if an error occurs during serialization
**Throws:** IllegalBlockSizeException

- if the given cipher is a block
cipher, no padding has been requested, and the total input length
(i.e., the length of the serialized object contents) is not a multiple
of the cipher's block size

- SealedObject

```java
protected SealedObject​(
SealedObject
so)
```

Constructs a SealedObject object from the passed-in SealedObject.

**Parameters:** so

- a SealedObject object
**Throws:** NullPointerException

- if the given sealed object is null.

============ METHOD DETAIL ==========

- Method Detail

- getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the algorithm that was used to seal this object.

**Returns:** the algorithm that was used to seal this object.

- getObject

```java
public final
Object
getObject​(
Key
key)
throws
IOException
,

ClassNotFoundException
,

NoSuchAlgorithmException
,

InvalidKeyException
```

Retrieves the original (encapsulated) object.

This method creates a cipher for the algorithm that had been used in
the sealing operation.
If the default provider package provides an implementation of that
algorithm, an instance of Cipher containing that implementation is used.
If the algorithm is not available in the default package, other
packages are searched.
The Cipher object is initialized for decryption, using the given

key

and the parameters (if any) that had been used in the
sealing operation.

The encapsulated object is unsealed and de-serialized, before it is
returned.

**Parameters:** key

- the key used to unseal the object.
**Returns:** the original object.
**Throws:** IOException

- if an error occurs during de-serialiazation.
**Throws:** ClassNotFoundException

- if an error occurs during
de-serialiazation.
**Throws:** NoSuchAlgorithmException

- if the algorithm to unseal the
object is not available.
**Throws:** InvalidKeyException

- if the given key cannot be used to unseal
the object (e.g., it has the wrong algorithm).
**Throws:** NullPointerException

- if

key

is null.

- getObject

```java
public final
Object
getObject​(
Cipher
c)
throws
IOException
,

ClassNotFoundException
,

IllegalBlockSizeException
,

BadPaddingException
```

Retrieves the original (encapsulated) object.

The encapsulated object is unsealed (using the given Cipher,
assuming that the Cipher is already properly initialized) and
de-serialized, before it is returned.

**Parameters:** c

- the cipher used to unseal the object
**Returns:** the original object.
**Throws:** NullPointerException

- if the given cipher is null.
**Throws:** IOException

- if an error occurs during de-serialiazation
**Throws:** ClassNotFoundException

- if an error occurs during
de-serialiazation
**Throws:** IllegalBlockSizeException

- if the given cipher is a block
cipher, no padding has been requested, and the total input length is
not a multiple of the cipher's block size
**Throws:** BadPaddingException

- if the given cipher has been
initialized for decryption, and padding has been specified, but
the input data does not have proper expected padding bytes

- getObject

```java
public final
Object
getObject​(
Key
key,

String
provider)
throws
IOException
,

ClassNotFoundException
,

NoSuchAlgorithmException
,

NoSuchProviderException
,

InvalidKeyException
```

Retrieves the original (encapsulated) object.

This method creates a cipher for the algorithm that had been used in
the sealing operation, using an implementation of that algorithm from
the given

provider

.
The Cipher object is initialized for decryption, using the given

key

and the parameters (if any) that had been used in the
sealing operation.

The encapsulated object is unsealed and de-serialized, before it is
returned.

**Parameters:** key

- the key used to unseal the object.
**Parameters:** provider

- the name of the provider of the algorithm to unseal
the object.
**Returns:** the original object.
**Throws:** IllegalArgumentException

- if the given provider is null
or empty.
**Throws:** IOException

- if an error occurs during de-serialiazation.
**Throws:** ClassNotFoundException

- if an error occurs during
de-serialiazation.
**Throws:** NoSuchAlgorithmException

- if the algorithm to unseal the
object is not available.
**Throws:** NoSuchProviderException

- if the given provider is not
configured.
**Throws:** InvalidKeyException

- if the given key cannot be used to unseal
the object (e.g., it has the wrong algorithm).
**Throws:** NullPointerException

- if

key

is null.

Field Detail

- encodedParams

```java
protected byte[] encodedParams
```

The cryptographic parameters used by the sealing Cipher,
encoded in the default format.

That is,

cipher.getParameters().getEncoded()

.

---

#### Field Detail

encodedParams

```java
protected byte[] encodedParams
```

The cryptographic parameters used by the sealing Cipher,
encoded in the default format.

That is,

cipher.getParameters().getEncoded()

.

---

#### encodedParams

protected byte[] encodedParams

The cryptographic parameters used by the sealing Cipher,
encoded in the default format.

That is,

cipher.getParameters().getEncoded()

.

That is,

cipher.getParameters().getEncoded()

.

Constructor Detail

- SealedObject

```java
public SealedObject​(
Serializable
object,

Cipher
c)
throws
IOException
,

IllegalBlockSizeException
```

Constructs a SealedObject from any Serializable object.

The given object is serialized, and its serialized contents are
encrypted using the given Cipher, which must be fully initialized.

Any algorithm parameters that may be used in the encryption
operation are stored inside of the new

SealedObject

.

**Parameters:** object

- the object to be sealed; can be null.
**Parameters:** c

- the cipher used to seal the object.
**Throws:** NullPointerException

- if the given cipher is null.
**Throws:** IOException

- if an error occurs during serialization
**Throws:** IllegalBlockSizeException

- if the given cipher is a block
cipher, no padding has been requested, and the total input length
(i.e., the length of the serialized object contents) is not a multiple
of the cipher's block size

- SealedObject

```java
protected SealedObject​(
SealedObject
so)
```

Constructs a SealedObject object from the passed-in SealedObject.

**Parameters:** so

- a SealedObject object
**Throws:** NullPointerException

- if the given sealed object is null.

---

#### Constructor Detail

SealedObject

```java
public SealedObject​(
Serializable
object,

Cipher
c)
throws
IOException
,

IllegalBlockSizeException
```

Constructs a SealedObject from any Serializable object.

The given object is serialized, and its serialized contents are
encrypted using the given Cipher, which must be fully initialized.

Any algorithm parameters that may be used in the encryption
operation are stored inside of the new

SealedObject

.

**Parameters:** object

- the object to be sealed; can be null.
**Parameters:** c

- the cipher used to seal the object.
**Throws:** NullPointerException

- if the given cipher is null.
**Throws:** IOException

- if an error occurs during serialization
**Throws:** IllegalBlockSizeException

- if the given cipher is a block
cipher, no padding has been requested, and the total input length
(i.e., the length of the serialized object contents) is not a multiple
of the cipher's block size

---

#### SealedObject

public SealedObject​(

Serializable

object,

Cipher

c)
throws

IOException

,

IllegalBlockSizeException

Constructs a SealedObject from any Serializable object.

The given object is serialized, and its serialized contents are
encrypted using the given Cipher, which must be fully initialized.

Any algorithm parameters that may be used in the encryption
operation are stored inside of the new

SealedObject

.

The given object is serialized, and its serialized contents are
encrypted using the given Cipher, which must be fully initialized.

Any algorithm parameters that may be used in the encryption
operation are stored inside of the new

SealedObject

.

Any algorithm parameters that may be used in the encryption
operation are stored inside of the new

SealedObject

.

SealedObject

```java
protected SealedObject​(
SealedObject
so)
```

Constructs a SealedObject object from the passed-in SealedObject.

**Parameters:** so

- a SealedObject object
**Throws:** NullPointerException

- if the given sealed object is null.

---

#### SealedObject

protected SealedObject​(

SealedObject

so)

Constructs a SealedObject object from the passed-in SealedObject.

Method Detail

- getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the algorithm that was used to seal this object.

**Returns:** the algorithm that was used to seal this object.

- getObject

```java
public final
Object
getObject​(
Key
key)
throws
IOException
,

ClassNotFoundException
,

NoSuchAlgorithmException
,

InvalidKeyException
```

Retrieves the original (encapsulated) object.

This method creates a cipher for the algorithm that had been used in
the sealing operation.
If the default provider package provides an implementation of that
algorithm, an instance of Cipher containing that implementation is used.
If the algorithm is not available in the default package, other
packages are searched.
The Cipher object is initialized for decryption, using the given

key

and the parameters (if any) that had been used in the
sealing operation.

The encapsulated object is unsealed and de-serialized, before it is
returned.

**Parameters:** key

- the key used to unseal the object.
**Returns:** the original object.
**Throws:** IOException

- if an error occurs during de-serialiazation.
**Throws:** ClassNotFoundException

- if an error occurs during
de-serialiazation.
**Throws:** NoSuchAlgorithmException

- if the algorithm to unseal the
object is not available.
**Throws:** InvalidKeyException

- if the given key cannot be used to unseal
the object (e.g., it has the wrong algorithm).
**Throws:** NullPointerException

- if

key

is null.

- getObject

```java
public final
Object
getObject​(
Cipher
c)
throws
IOException
,

ClassNotFoundException
,

IllegalBlockSizeException
,

BadPaddingException
```

Retrieves the original (encapsulated) object.

The encapsulated object is unsealed (using the given Cipher,
assuming that the Cipher is already properly initialized) and
de-serialized, before it is returned.

**Parameters:** c

- the cipher used to unseal the object
**Returns:** the original object.
**Throws:** NullPointerException

- if the given cipher is null.
**Throws:** IOException

- if an error occurs during de-serialiazation
**Throws:** ClassNotFoundException

- if an error occurs during
de-serialiazation
**Throws:** IllegalBlockSizeException

- if the given cipher is a block
cipher, no padding has been requested, and the total input length is
not a multiple of the cipher's block size
**Throws:** BadPaddingException

- if the given cipher has been
initialized for decryption, and padding has been specified, but
the input data does not have proper expected padding bytes

- getObject

```java
public final
Object
getObject​(
Key
key,

String
provider)
throws
IOException
,

ClassNotFoundException
,

NoSuchAlgorithmException
,

NoSuchProviderException
,

InvalidKeyException
```

Retrieves the original (encapsulated) object.

This method creates a cipher for the algorithm that had been used in
the sealing operation, using an implementation of that algorithm from
the given

provider

.
The Cipher object is initialized for decryption, using the given

key

and the parameters (if any) that had been used in the
sealing operation.

The encapsulated object is unsealed and de-serialized, before it is
returned.

**Parameters:** key

- the key used to unseal the object.
**Parameters:** provider

- the name of the provider of the algorithm to unseal
the object.
**Returns:** the original object.
**Throws:** IllegalArgumentException

- if the given provider is null
or empty.
**Throws:** IOException

- if an error occurs during de-serialiazation.
**Throws:** ClassNotFoundException

- if an error occurs during
de-serialiazation.
**Throws:** NoSuchAlgorithmException

- if the algorithm to unseal the
object is not available.
**Throws:** NoSuchProviderException

- if the given provider is not
configured.
**Throws:** InvalidKeyException

- if the given key cannot be used to unseal
the object (e.g., it has the wrong algorithm).
**Throws:** NullPointerException

- if

key

is null.

---

#### Method Detail

getAlgorithm

```java
public final
String
getAlgorithm()
```

Returns the algorithm that was used to seal this object.

**Returns:** the algorithm that was used to seal this object.

---

#### getAlgorithm

public final

String

getAlgorithm()

Returns the algorithm that was used to seal this object.

getObject

```java
public final
Object
getObject​(
Key
key)
throws
IOException
,

ClassNotFoundException
,

NoSuchAlgorithmException
,

InvalidKeyException
```

Retrieves the original (encapsulated) object.

This method creates a cipher for the algorithm that had been used in
the sealing operation.
If the default provider package provides an implementation of that
algorithm, an instance of Cipher containing that implementation is used.
If the algorithm is not available in the default package, other
packages are searched.
The Cipher object is initialized for decryption, using the given

key

and the parameters (if any) that had been used in the
sealing operation.

The encapsulated object is unsealed and de-serialized, before it is
returned.

**Parameters:** key

- the key used to unseal the object.
**Returns:** the original object.
**Throws:** IOException

- if an error occurs during de-serialiazation.
**Throws:** ClassNotFoundException

- if an error occurs during
de-serialiazation.
**Throws:** NoSuchAlgorithmException

- if the algorithm to unseal the
object is not available.
**Throws:** InvalidKeyException

- if the given key cannot be used to unseal
the object (e.g., it has the wrong algorithm).
**Throws:** NullPointerException

- if

key

is null.

---

#### getObject

public final

Object

getObject​(

Key

key)
throws

IOException

,

ClassNotFoundException

,

NoSuchAlgorithmException

,

InvalidKeyException

Retrieves the original (encapsulated) object.

This method creates a cipher for the algorithm that had been used in
the sealing operation.
If the default provider package provides an implementation of that
algorithm, an instance of Cipher containing that implementation is used.
If the algorithm is not available in the default package, other
packages are searched.
The Cipher object is initialized for decryption, using the given

key

and the parameters (if any) that had been used in the
sealing operation.

The encapsulated object is unsealed and de-serialized, before it is
returned.

This method creates a cipher for the algorithm that had been used in
the sealing operation.
If the default provider package provides an implementation of that
algorithm, an instance of Cipher containing that implementation is used.
If the algorithm is not available in the default package, other
packages are searched.
The Cipher object is initialized for decryption, using the given

key

and the parameters (if any) that had been used in the
sealing operation.

The encapsulated object is unsealed and de-serialized, before it is
returned.

The encapsulated object is unsealed and de-serialized, before it is
returned.

getObject

```java
public final
Object
getObject​(
Cipher
c)
throws
IOException
,

ClassNotFoundException
,

IllegalBlockSizeException
,

BadPaddingException
```

Retrieves the original (encapsulated) object.

The encapsulated object is unsealed (using the given Cipher,
assuming that the Cipher is already properly initialized) and
de-serialized, before it is returned.

**Parameters:** c

- the cipher used to unseal the object
**Returns:** the original object.
**Throws:** NullPointerException

- if the given cipher is null.
**Throws:** IOException

- if an error occurs during de-serialiazation
**Throws:** ClassNotFoundException

- if an error occurs during
de-serialiazation
**Throws:** IllegalBlockSizeException

- if the given cipher is a block
cipher, no padding has been requested, and the total input length is
not a multiple of the cipher's block size
**Throws:** BadPaddingException

- if the given cipher has been
initialized for decryption, and padding has been specified, but
the input data does not have proper expected padding bytes

---

#### getObject

public final

Object

getObject​(

Cipher

c)
throws

IOException

,

ClassNotFoundException

,

IllegalBlockSizeException

,

BadPaddingException

Retrieves the original (encapsulated) object.

The encapsulated object is unsealed (using the given Cipher,
assuming that the Cipher is already properly initialized) and
de-serialized, before it is returned.

The encapsulated object is unsealed (using the given Cipher,
assuming that the Cipher is already properly initialized) and
de-serialized, before it is returned.

getObject

```java
public final
Object
getObject​(
Key
key,

String
provider)
throws
IOException
,

ClassNotFoundException
,

NoSuchAlgorithmException
,

NoSuchProviderException
,

InvalidKeyException
```

Retrieves the original (encapsulated) object.

This method creates a cipher for the algorithm that had been used in
the sealing operation, using an implementation of that algorithm from
the given

provider

.
The Cipher object is initialized for decryption, using the given

key

and the parameters (if any) that had been used in the
sealing operation.

The encapsulated object is unsealed and de-serialized, before it is
returned.

**Parameters:** key

- the key used to unseal the object.
**Parameters:** provider

- the name of the provider of the algorithm to unseal
the object.
**Returns:** the original object.
**Throws:** IllegalArgumentException

- if the given provider is null
or empty.
**Throws:** IOException

- if an error occurs during de-serialiazation.
**Throws:** ClassNotFoundException

- if an error occurs during
de-serialiazation.
**Throws:** NoSuchAlgorithmException

- if the algorithm to unseal the
object is not available.
**Throws:** NoSuchProviderException

- if the given provider is not
configured.
**Throws:** InvalidKeyException

- if the given key cannot be used to unseal
the object (e.g., it has the wrong algorithm).
**Throws:** NullPointerException

- if

key

is null.

---

#### getObject

public final

Object

getObject​(

Key

key,

String

provider)
throws

IOException

,

ClassNotFoundException

,

NoSuchAlgorithmException

,

NoSuchProviderException

,

InvalidKeyException

Retrieves the original (encapsulated) object.

This method creates a cipher for the algorithm that had been used in
the sealing operation, using an implementation of that algorithm from
the given

provider

.
The Cipher object is initialized for decryption, using the given

key

and the parameters (if any) that had been used in the
sealing operation.

The encapsulated object is unsealed and de-serialized, before it is
returned.

This method creates a cipher for the algorithm that had been used in
the sealing operation, using an implementation of that algorithm from
the given

provider

.
The Cipher object is initialized for decryption, using the given

key

and the parameters (if any) that had been used in the
sealing operation.

The encapsulated object is unsealed and de-serialized, before it is
returned.

The encapsulated object is unsealed and de-serialized, before it is
returned.

---

