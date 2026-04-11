# Class KeyStoreSpi

**Source:** `java.base\java\security\KeyStoreSpi.html`

### Class Description

```java
public abstract class
KeyStoreSpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

KeyStore

class.
All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a keystore for a particular keystore type.

**Since:** 1.2
**See Also:** KeyStore

---

### Field Details

*No entries found.*

### Constructor Details

#### public KeyStoreSpi()

*No description found.*

---

### Method Details

#### public abstract
Key
engineGetKey​(
String
alias,
char[] password)
throws
NoSuchAlgorithmException
,

UnrecoverableKeyException

Returns the key associated with the given alias, using the given
password to recover it. The key must have been associated with
the alias by a call to

setKeyEntry

,
or by a call to

setEntry

with a

PrivateKeyEntry

or

SecretKeyEntry

.

**Parameters:**
- alias

- the alias name
- password

- the password for recovering the key

**Returns:**
- the requested key, or null if the given alias does not exist
or does not identify a key-related entry.

**Throws:**
- NoSuchAlgorithmException

- if the algorithm for recovering the
key cannot be found
- UnrecoverableKeyException

- if the key cannot be recovered
(e.g., the given password is wrong).

---

#### public abstract
Certificate
[] engineGetCertificateChain​(
String
alias)

Returns the certificate chain associated with the given alias.
The certificate chain must have been associated with the alias
by a call to

setKeyEntry

,
or by a call to

setEntry

with a

PrivateKeyEntry

.

**Parameters:**
- alias

- the alias name

**Returns:**
- the certificate chain (ordered with the user's certificate first
and the root certificate authority last), or null if the given alias
does not exist or does not contain a certificate chain

---

#### public abstract
Certificate
engineGetCertificate​(
String
alias)

Returns the certificate associated with the given alias.

If the given alias name identifies an entry
created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

,
then the trusted certificate contained in that entry is returned.

If the given alias name identifies an entry
created by a call to

setKeyEntry

,
or created by a call to

setEntry

with a

PrivateKeyEntry

,
then the first element of the certificate chain in that entry
(if a chain exists) is returned.

**Parameters:**
- alias

- the alias name

**Returns:**
- the certificate, or null if the given alias does not exist or
does not contain a certificate.

---

#### public abstract
Date
engineGetCreationDate​(
String
alias)

Returns the creation date of the entry identified by the given alias.

**Parameters:**
- alias

- the alias name

**Returns:**
- the creation date of this entry, or null if the given alias does
not exist

---

#### public abstract void engineSetKeyEntry​(
String
alias,

Key
key,
char[] password,

Certificate
[] chain)
throws
KeyStoreException

Assigns the given key to the given alias, protecting it with the given
password.

If the given key is of type

java.security.PrivateKey

,
it must be accompanied by a certificate chain certifying the
corresponding public key.

If the given alias already exists, the keystore information
associated with it is overridden by the given key (and possibly
certificate chain).

**Parameters:**
- alias

- the alias name
- key

- the key to be associated with the alias
- password

- the password to protect the key
- chain

- the certificate chain for the corresponding public
key (only required if the given key is of type

java.security.PrivateKey

).

**Throws:**
- KeyStoreException

- if the given key cannot be protected, or
this operation fails for some other reason

---

#### public abstract void engineSetKeyEntry​(
String
alias,
byte[] key,

Certificate
[] chain)
throws
KeyStoreException

Assigns the given key (that has already been protected) to the given
alias.

If the protected key is of type

java.security.PrivateKey

,
it must be accompanied by a certificate chain certifying the
corresponding public key.

If the given alias already exists, the keystore information
associated with it is overridden by the given key (and possibly
certificate chain).

**Parameters:**
- alias

- the alias name
- key

- the key (in protected format) to be associated with the alias
- chain

- the certificate chain for the corresponding public
key (only useful if the protected key is of type

java.security.PrivateKey

).

**Throws:**
- KeyStoreException

- if this operation fails.

---

#### public abstract void engineSetCertificateEntry​(
String
alias,

Certificate
cert)
throws
KeyStoreException

Assigns the given certificate to the given alias.

If the given alias identifies an existing entry
created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

,
the trusted certificate in the existing entry
is overridden by the given certificate.

**Parameters:**
- alias

- the alias name
- cert

- the certificate

**Throws:**
- KeyStoreException

- if the given alias already exists and does
not identify an entry containing a trusted certificate,
or this operation fails for some other reason.

---

#### public abstract void engineDeleteEntry​(
String
alias)
throws
KeyStoreException

Deletes the entry identified by the given alias from this keystore.

**Parameters:**
- alias

- the alias name

**Throws:**
- KeyStoreException

- if the entry cannot be removed.

---

#### public abstract
Enumeration
<
String
> engineAliases()

Lists all the alias names of this keystore.

**Returns:**
- enumeration of the alias names

---

#### public abstract boolean engineContainsAlias​(
String
alias)

Checks if the given alias exists in this keystore.

**Parameters:**
- alias

- the alias name

**Returns:**
- true if the alias exists, false otherwise

---

#### public abstract int engineSize()

Retrieves the number of entries in this keystore.

**Returns:**
- the number of entries in this keystore

---

#### public abstract boolean engineIsKeyEntry​(
String
alias)

Returns true if the entry identified by the given alias
was created by a call to

setKeyEntry

,
or created by a call to

setEntry

with a

PrivateKeyEntry

or a

SecretKeyEntry

.

**Parameters:**
- alias

- the alias for the keystore entry to be checked

**Returns:**
- true if the entry identified by the given alias is a
key-related, false otherwise.

---

#### public abstract boolean engineIsCertificateEntry​(
String
alias)

Returns true if the entry identified by the given alias
was created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

.

**Parameters:**
- alias

- the alias for the keystore entry to be checked

**Returns:**
- true if the entry identified by the given alias contains a
trusted certificate, false otherwise.

---

#### public abstract
String
engineGetCertificateAlias​(
Certificate
cert)

Returns the (alias) name of the first keystore entry whose certificate
matches the given certificate.

This method attempts to match the given certificate with each
keystore entry. If the entry being considered was
created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

,
then the given certificate is compared to that entry's certificate.

If the entry being considered was
created by a call to

setKeyEntry

,
or created by a call to

setEntry

with a

PrivateKeyEntry

,
then the given certificate is compared to the first
element of that entry's certificate chain.

**Parameters:**
- cert

- the certificate to match with.

**Returns:**
- the alias name of the first entry with matching certificate,
or null if no such entry exists in this keystore.

---

#### public abstract void engineStore​(
OutputStream
stream,
char[] password)
throws
IOException
,

NoSuchAlgorithmException
,

CertificateException

Stores this keystore to the given output stream, and protects its
integrity with the given password.

**Parameters:**
- stream

- the output stream to which this keystore is written.
- password

- the password to generate the keystore integrity check

**Throws:**
- IOException

- if there was an I/O problem with data
- NoSuchAlgorithmException

- if the appropriate data integrity
algorithm could not be found
- CertificateException

- if any of the certificates included in
the keystore data could not be stored

---

#### public void engineStore​(
KeyStore.LoadStoreParameter
param)
throws
IOException
,

NoSuchAlgorithmException
,

CertificateException

Stores this keystore using the given

KeyStore.LoadStoreParmeter

.

**Parameters:**
- param

- the

KeyStore.LoadStoreParmeter

that specifies how to store the keystore,
which may be

null

**Throws:**
- IllegalArgumentException

- if the given

KeyStore.LoadStoreParmeter

input is not recognized
- IOException

- if there was an I/O problem with data
- NoSuchAlgorithmException

- if the appropriate data integrity
algorithm could not be found
- CertificateException

- if any of the certificates included in
the keystore data could not be stored

**Since:**
- 1.5

---

#### public abstract void engineLoad​(
InputStream
stream,
char[] password)
throws
IOException
,

NoSuchAlgorithmException
,

CertificateException

Loads the keystore from the given input stream.

A password may be given to unlock the keystore
(e.g. the keystore resides on a hardware token device),
or to check the integrity of the keystore data.
If a password is not given for integrity checking,
then integrity checking is not performed.

**Parameters:**
- stream

- the input stream from which the keystore is loaded,
or

null
- password

- the password used to check the integrity of
the keystore, the password used to unlock the keystore,
or

null

**Throws:**
- IOException

- if there is an I/O or format problem with the
keystore data, if a password is required but not given,
or if the given password was incorrect. If the error is due to a
wrong password, the

cause

of the

IOException

should be an

UnrecoverableKeyException
- NoSuchAlgorithmException

- if the algorithm used to check
the integrity of the keystore cannot be found
- CertificateException

- if any of the certificates in the
keystore could not be loaded

---

#### public void engineLoad​(
KeyStore.LoadStoreParameter
param)
throws
IOException
,

NoSuchAlgorithmException
,

CertificateException

Loads the keystore using the given

KeyStore.LoadStoreParameter

.

Note that if this KeyStore has already been loaded, it is
reinitialized and loaded again from the given parameter.

**Parameters:**
- param

- the

KeyStore.LoadStoreParameter

that specifies how to load the keystore,
which may be

null

**Throws:**
- IllegalArgumentException

- if the given

KeyStore.LoadStoreParameter

input is not recognized
- IOException

- if there is an I/O or format problem with the
keystore data. If the error is due to an incorrect

ProtectionParameter

(e.g. wrong password)
the

cause

of the

IOException

should be an

UnrecoverableKeyException
- NoSuchAlgorithmException

- if the algorithm used to check
the integrity of the keystore cannot be found
- CertificateException

- if any of the certificates in the
keystore could not be loaded

**Since:**
- 1.5

**Implementation Requirements:**
- The default implementation examines

KeyStore.LoadStoreParameter

to extract its password and pass it to

engineLoad(InputStream, char[])

along with a

null

InputStream

.

If

KeyStore.LoadStoreParameter

is

null

then
the password parameter will also be

null

.
Otherwise the

KeyStore.ProtectionParameter

of

KeyStore.LoadStoreParameter

must be either a

KeyStore.PasswordProtection

or a

KeyStore.CallbackHandlerProtection

that supports

PasswordCallback

so that the password parameter can be
extracted. If the

KeyStore.ProtectionParameter

is neither
of those classes then a

NoSuchAlgorithmException

is thrown.

---

#### public
KeyStore.Entry
engineGetEntry​(
String
alias,

KeyStore.ProtectionParameter
protParam)
throws
KeyStoreException
,

NoSuchAlgorithmException
,

UnrecoverableEntryException

Gets a

KeyStore.Entry

for the specified alias
with the specified protection parameter.

**Parameters:**
- alias

- get the

KeyStore.Entry

for this alias
- protParam

- the

ProtectionParameter

used to protect the

Entry

,
which may be

null

**Returns:**
- the

KeyStore.Entry

for the specified alias,
or

null

if there is no such entry

**Throws:**
- KeyStoreException

- if the operation failed
- NoSuchAlgorithmException

- if the algorithm for recovering the
entry cannot be found
- UnrecoverableEntryException

- if the specified

protParam

were insufficient or invalid
- UnrecoverableKeyException

- if the entry is a

PrivateKeyEntry

or

SecretKeyEntry

and the specified

protParam

does not contain
the information needed to recover the key (e.g. wrong password)

**Since:**
- 1.5

---

#### public void engineSetEntry​(
String
alias,

KeyStore.Entry
entry,

KeyStore.ProtectionParameter
protParam)
throws
KeyStoreException

Saves a

KeyStore.Entry

under the specified alias.
The specified protection parameter is used to protect the

Entry

.

If an entry already exists for the specified alias,
it is overridden.

**Parameters:**
- alias

- save the

KeyStore.Entry

under this alias
- entry

- the

Entry

to save
- protParam

- the

ProtectionParameter

used to protect the

Entry

,
which may be

null

**Throws:**
- KeyStoreException

- if this operation fails

**Since:**
- 1.5

---

#### public boolean engineEntryInstanceOf​(
String
alias,

Class
<? extends
KeyStore.Entry
> entryClass)

Determines if the keystore

Entry

for the specified

alias

is an instance or subclass of the specified

entryClass

.

**Parameters:**
- alias

- the alias name
- entryClass

- the entry class

**Returns:**
- true if the keystore

Entry

for the specified

alias

is an instance or subclass of the
specified

entryClass

, false otherwise

**Since:**
- 1.5

---

#### public boolean engineProbe​(
InputStream
stream)
throws
IOException

Probes the specified input stream to determine whether it contains a
keystore that is supported by this implementation, or not.

**Parameters:**
- stream

- the keystore data to be probed

**Returns:**
- true if the keystore data is supported, otherwise false

**Throws:**
- IOException

- if there is an I/O problem with the keystore data.
- NullPointerException

- if stream is

null

.

**Since:**
- 9

**Implementation Requirements:**
- This method returns false by default. Keystore implementations should
override this method to peek at the data stream directly or to use other
content detection mechanisms.

---

### Additional Sections

#### Class KeyStoreSpi

java.lang.Object

- java.security.KeyStoreSpi

java.security.KeyStoreSpi

```java
public abstract class
KeyStoreSpi

extends
Object
```

This class defines the

Service Provider Interface

(

SPI

)
for the

KeyStore

class.
All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a keystore for a particular keystore type.

**Since:** 1.2
**See Also:** KeyStore

public abstract class

KeyStoreSpi

extends

Object

This class defines the

Service Provider Interface

(

SPI

)
for the

KeyStore

class.
All the abstract methods in this class must be implemented by each
cryptographic service provider who wishes to supply the implementation
of a keystore for a particular keystore type.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

KeyStoreSpi

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

Enumeration

<

String

>

engineAliases

()

Lists all the alias names of this keystore.

abstract boolean

engineContainsAlias

​(

String

alias)

Checks if the given alias exists in this keystore.

abstract void

engineDeleteEntry

​(

String

alias)

Deletes the entry identified by the given alias from this keystore.

boolean

engineEntryInstanceOf

​(

String

alias,

Class

<? extends

KeyStore.Entry

> entryClass)

Determines if the keystore

Entry

for the specified

alias

is an instance or subclass of the specified

entryClass

.

abstract

Certificate

engineGetCertificate

​(

String

alias)

Returns the certificate associated with the given alias.

abstract

String

engineGetCertificateAlias

​(

Certificate

cert)

Returns the (alias) name of the first keystore entry whose certificate
matches the given certificate.

abstract

Certificate

[]

engineGetCertificateChain

​(

String

alias)

Returns the certificate chain associated with the given alias.

abstract

Date

engineGetCreationDate

​(

String

alias)

Returns the creation date of the entry identified by the given alias.

KeyStore.Entry

engineGetEntry

​(

String

alias,

KeyStore.ProtectionParameter

protParam)

Gets a

KeyStore.Entry

for the specified alias
with the specified protection parameter.

abstract

Key

engineGetKey

​(

String

alias,
char[] password)

Returns the key associated with the given alias, using the given
password to recover it.

abstract boolean

engineIsCertificateEntry

​(

String

alias)

Returns true if the entry identified by the given alias
was created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

.

abstract boolean

engineIsKeyEntry

​(

String

alias)

Returns true if the entry identified by the given alias
was created by a call to

setKeyEntry

,
or created by a call to

setEntry

with a

PrivateKeyEntry

or a

SecretKeyEntry

.

abstract void

engineLoad

​(

InputStream

stream,
char[] password)

Loads the keystore from the given input stream.

void

engineLoad

​(

KeyStore.LoadStoreParameter

param)

Loads the keystore using the given

KeyStore.LoadStoreParameter

.

boolean

engineProbe

​(

InputStream

stream)

Probes the specified input stream to determine whether it contains a
keystore that is supported by this implementation, or not.

abstract void

engineSetCertificateEntry

​(

String

alias,

Certificate

cert)

Assigns the given certificate to the given alias.

void

engineSetEntry

​(

String

alias,

KeyStore.Entry

entry,

KeyStore.ProtectionParameter

protParam)

Saves a

KeyStore.Entry

under the specified alias.

abstract void

engineSetKeyEntry

​(

String

alias,
byte[] key,

Certificate

[] chain)

Assigns the given key (that has already been protected) to the given
alias.

abstract void

engineSetKeyEntry

​(

String

alias,

Key

key,
char[] password,

Certificate

[] chain)

Assigns the given key to the given alias, protecting it with the given
password.

abstract int

engineSize

()

Retrieves the number of entries in this keystore.

abstract void

engineStore

​(

OutputStream

stream,
char[] password)

Stores this keystore to the given output stream, and protects its
integrity with the given password.

void

engineStore

​(

KeyStore.LoadStoreParameter

param)

Stores this keystore using the given

KeyStore.LoadStoreParmeter

.

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

KeyStoreSpi

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

Enumeration

<

String

>

engineAliases

()

Lists all the alias names of this keystore.

abstract boolean

engineContainsAlias

​(

String

alias)

Checks if the given alias exists in this keystore.

abstract void

engineDeleteEntry

​(

String

alias)

Deletes the entry identified by the given alias from this keystore.

boolean

engineEntryInstanceOf

​(

String

alias,

Class

<? extends

KeyStore.Entry

> entryClass)

Determines if the keystore

Entry

for the specified

alias

is an instance or subclass of the specified

entryClass

.

abstract

Certificate

engineGetCertificate

​(

String

alias)

Returns the certificate associated with the given alias.

abstract

String

engineGetCertificateAlias

​(

Certificate

cert)

Returns the (alias) name of the first keystore entry whose certificate
matches the given certificate.

abstract

Certificate

[]

engineGetCertificateChain

​(

String

alias)

Returns the certificate chain associated with the given alias.

abstract

Date

engineGetCreationDate

​(

String

alias)

Returns the creation date of the entry identified by the given alias.

KeyStore.Entry

engineGetEntry

​(

String

alias,

KeyStore.ProtectionParameter

protParam)

Gets a

KeyStore.Entry

for the specified alias
with the specified protection parameter.

abstract

Key

engineGetKey

​(

String

alias,
char[] password)

Returns the key associated with the given alias, using the given
password to recover it.

abstract boolean

engineIsCertificateEntry

​(

String

alias)

Returns true if the entry identified by the given alias
was created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

.

abstract boolean

engineIsKeyEntry

​(

String

alias)

Returns true if the entry identified by the given alias
was created by a call to

setKeyEntry

,
or created by a call to

setEntry

with a

PrivateKeyEntry

or a

SecretKeyEntry

.

abstract void

engineLoad

​(

InputStream

stream,
char[] password)

Loads the keystore from the given input stream.

void

engineLoad

​(

KeyStore.LoadStoreParameter

param)

Loads the keystore using the given

KeyStore.LoadStoreParameter

.

boolean

engineProbe

​(

InputStream

stream)

Probes the specified input stream to determine whether it contains a
keystore that is supported by this implementation, or not.

abstract void

engineSetCertificateEntry

​(

String

alias,

Certificate

cert)

Assigns the given certificate to the given alias.

void

engineSetEntry

​(

String

alias,

KeyStore.Entry

entry,

KeyStore.ProtectionParameter

protParam)

Saves a

KeyStore.Entry

under the specified alias.

abstract void

engineSetKeyEntry

​(

String

alias,
byte[] key,

Certificate

[] chain)

Assigns the given key (that has already been protected) to the given
alias.

abstract void

engineSetKeyEntry

​(

String

alias,

Key

key,
char[] password,

Certificate

[] chain)

Assigns the given key to the given alias, protecting it with the given
password.

abstract int

engineSize

()

Retrieves the number of entries in this keystore.

abstract void

engineStore

​(

OutputStream

stream,
char[] password)

Stores this keystore to the given output stream, and protects its
integrity with the given password.

void

engineStore

​(

KeyStore.LoadStoreParameter

param)

Stores this keystore using the given

KeyStore.LoadStoreParmeter

.

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

Lists all the alias names of this keystore.

Checks if the given alias exists in this keystore.

Deletes the entry identified by the given alias from this keystore.

Determines if the keystore

Entry

for the specified

alias

is an instance or subclass of the specified

entryClass

.

Returns the certificate associated with the given alias.

Returns the (alias) name of the first keystore entry whose certificate
matches the given certificate.

Returns the certificate chain associated with the given alias.

Returns the creation date of the entry identified by the given alias.

Gets a

KeyStore.Entry

for the specified alias
with the specified protection parameter.

Returns the key associated with the given alias, using the given
password to recover it.

Returns true if the entry identified by the given alias
was created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

.

Returns true if the entry identified by the given alias
was created by a call to

setKeyEntry

,
or created by a call to

setEntry

with a

PrivateKeyEntry

or a

SecretKeyEntry

.

Loads the keystore from the given input stream.

Loads the keystore using the given

KeyStore.LoadStoreParameter

.

Probes the specified input stream to determine whether it contains a
keystore that is supported by this implementation, or not.

Assigns the given certificate to the given alias.

Saves a

KeyStore.Entry

under the specified alias.

Assigns the given key (that has already been protected) to the given
alias.

Assigns the given key to the given alias, protecting it with the given
password.

Retrieves the number of entries in this keystore.

Stores this keystore to the given output stream, and protects its
integrity with the given password.

Stores this keystore using the given

KeyStore.LoadStoreParmeter

.

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

- KeyStoreSpi

```java
public KeyStoreSpi()
```

============ METHOD DETAIL ==========

- Method Detail

- engineGetKey

```java
public abstract
Key
engineGetKey​(
String
alias,
char[] password)
throws
NoSuchAlgorithmException
,

UnrecoverableKeyException
```

Returns the key associated with the given alias, using the given
password to recover it. The key must have been associated with
the alias by a call to

setKeyEntry

,
or by a call to

setEntry

with a

PrivateKeyEntry

or

SecretKeyEntry

.

**Parameters:** alias

- the alias name
**Parameters:** password

- the password for recovering the key
**Returns:** the requested key, or null if the given alias does not exist
or does not identify a key-related entry.
**Throws:** NoSuchAlgorithmException

- if the algorithm for recovering the
key cannot be found
**Throws:** UnrecoverableKeyException

- if the key cannot be recovered
(e.g., the given password is wrong).

- engineGetCertificateChain

```java
public abstract
Certificate
[] engineGetCertificateChain​(
String
alias)
```

Returns the certificate chain associated with the given alias.
The certificate chain must have been associated with the alias
by a call to

setKeyEntry

,
or by a call to

setEntry

with a

PrivateKeyEntry

.

**Parameters:** alias

- the alias name
**Returns:** the certificate chain (ordered with the user's certificate first
and the root certificate authority last), or null if the given alias
does not exist or does not contain a certificate chain

- engineGetCertificate

```java
public abstract
Certificate
engineGetCertificate​(
String
alias)
```

Returns the certificate associated with the given alias.

If the given alias name identifies an entry
created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

,
then the trusted certificate contained in that entry is returned.

If the given alias name identifies an entry
created by a call to

setKeyEntry

,
or created by a call to

setEntry

with a

PrivateKeyEntry

,
then the first element of the certificate chain in that entry
(if a chain exists) is returned.

**Parameters:** alias

- the alias name
**Returns:** the certificate, or null if the given alias does not exist or
does not contain a certificate.

- engineGetCreationDate

```java
public abstract
Date
engineGetCreationDate​(
String
alias)
```

Returns the creation date of the entry identified by the given alias.

**Parameters:** alias

- the alias name
**Returns:** the creation date of this entry, or null if the given alias does
not exist

- engineSetKeyEntry

```java
public abstract void engineSetKeyEntry​(
String
alias,

Key
key,
char[] password,

Certificate
[] chain)
throws
KeyStoreException
```

Assigns the given key to the given alias, protecting it with the given
password.

If the given key is of type

java.security.PrivateKey

,
it must be accompanied by a certificate chain certifying the
corresponding public key.

If the given alias already exists, the keystore information
associated with it is overridden by the given key (and possibly
certificate chain).

**Parameters:** alias

- the alias name
**Parameters:** key

- the key to be associated with the alias
**Parameters:** password

- the password to protect the key
**Parameters:** chain

- the certificate chain for the corresponding public
key (only required if the given key is of type

java.security.PrivateKey

).
**Throws:** KeyStoreException

- if the given key cannot be protected, or
this operation fails for some other reason

- engineSetKeyEntry

```java
public abstract void engineSetKeyEntry​(
String
alias,
byte[] key,

Certificate
[] chain)
throws
KeyStoreException
```

Assigns the given key (that has already been protected) to the given
alias.

If the protected key is of type

java.security.PrivateKey

,
it must be accompanied by a certificate chain certifying the
corresponding public key.

If the given alias already exists, the keystore information
associated with it is overridden by the given key (and possibly
certificate chain).

**Parameters:** alias

- the alias name
**Parameters:** key

- the key (in protected format) to be associated with the alias
**Parameters:** chain

- the certificate chain for the corresponding public
key (only useful if the protected key is of type

java.security.PrivateKey

).
**Throws:** KeyStoreException

- if this operation fails.

- engineSetCertificateEntry

```java
public abstract void engineSetCertificateEntry​(
String
alias,

Certificate
cert)
throws
KeyStoreException
```

Assigns the given certificate to the given alias.

If the given alias identifies an existing entry
created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

,
the trusted certificate in the existing entry
is overridden by the given certificate.

**Parameters:** alias

- the alias name
**Parameters:** cert

- the certificate
**Throws:** KeyStoreException

- if the given alias already exists and does
not identify an entry containing a trusted certificate,
or this operation fails for some other reason.

- engineDeleteEntry

```java
public abstract void engineDeleteEntry​(
String
alias)
throws
KeyStoreException
```

Deletes the entry identified by the given alias from this keystore.

**Parameters:** alias

- the alias name
**Throws:** KeyStoreException

- if the entry cannot be removed.

- engineAliases

```java
public abstract
Enumeration
<
String
> engineAliases()
```

Lists all the alias names of this keystore.

**Returns:** enumeration of the alias names

- engineContainsAlias

```java
public abstract boolean engineContainsAlias​(
String
alias)
```

Checks if the given alias exists in this keystore.

**Parameters:** alias

- the alias name
**Returns:** true if the alias exists, false otherwise

- engineSize

```java
public abstract int engineSize()
```

Retrieves the number of entries in this keystore.

**Returns:** the number of entries in this keystore

- engineIsKeyEntry

```java
public abstract boolean engineIsKeyEntry​(
String
alias)
```

Returns true if the entry identified by the given alias
was created by a call to

setKeyEntry

,
or created by a call to

setEntry

with a

PrivateKeyEntry

or a

SecretKeyEntry

.

**Parameters:** alias

- the alias for the keystore entry to be checked
**Returns:** true if the entry identified by the given alias is a
key-related, false otherwise.

- engineIsCertificateEntry

```java
public abstract boolean engineIsCertificateEntry​(
String
alias)
```

Returns true if the entry identified by the given alias
was created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

.

**Parameters:** alias

- the alias for the keystore entry to be checked
**Returns:** true if the entry identified by the given alias contains a
trusted certificate, false otherwise.

- engineGetCertificateAlias

```java
public abstract
String
engineGetCertificateAlias​(
Certificate
cert)
```

Returns the (alias) name of the first keystore entry whose certificate
matches the given certificate.

This method attempts to match the given certificate with each
keystore entry. If the entry being considered was
created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

,
then the given certificate is compared to that entry's certificate.

If the entry being considered was
created by a call to

setKeyEntry

,
or created by a call to

setEntry

with a

PrivateKeyEntry

,
then the given certificate is compared to the first
element of that entry's certificate chain.

**Parameters:** cert

- the certificate to match with.
**Returns:** the alias name of the first entry with matching certificate,
or null if no such entry exists in this keystore.

- engineStore

```java
public abstract void engineStore​(
OutputStream
stream,
char[] password)
throws
IOException
,

NoSuchAlgorithmException
,

CertificateException
```

Stores this keystore to the given output stream, and protects its
integrity with the given password.

**Parameters:** stream

- the output stream to which this keystore is written.
**Parameters:** password

- the password to generate the keystore integrity check
**Throws:** IOException

- if there was an I/O problem with data
**Throws:** NoSuchAlgorithmException

- if the appropriate data integrity
algorithm could not be found
**Throws:** CertificateException

- if any of the certificates included in
the keystore data could not be stored

- engineStore

```java
public void engineStore​(
KeyStore.LoadStoreParameter
param)
throws
IOException
,

NoSuchAlgorithmException
,

CertificateException
```

Stores this keystore using the given

KeyStore.LoadStoreParmeter

.

**Parameters:** param

- the

KeyStore.LoadStoreParmeter

that specifies how to store the keystore,
which may be

null
**Throws:** IllegalArgumentException

- if the given

KeyStore.LoadStoreParmeter

input is not recognized
**Throws:** IOException

- if there was an I/O problem with data
**Throws:** NoSuchAlgorithmException

- if the appropriate data integrity
algorithm could not be found
**Throws:** CertificateException

- if any of the certificates included in
the keystore data could not be stored
**Since:** 1.5

- engineLoad

```java
public abstract void engineLoad​(
InputStream
stream,
char[] password)
throws
IOException
,

NoSuchAlgorithmException
,

CertificateException
```

Loads the keystore from the given input stream.

A password may be given to unlock the keystore
(e.g. the keystore resides on a hardware token device),
or to check the integrity of the keystore data.
If a password is not given for integrity checking,
then integrity checking is not performed.

**Parameters:** stream

- the input stream from which the keystore is loaded,
or

null
**Parameters:** password

- the password used to check the integrity of
the keystore, the password used to unlock the keystore,
or

null
**Throws:** IOException

- if there is an I/O or format problem with the
keystore data, if a password is required but not given,
or if the given password was incorrect. If the error is due to a
wrong password, the

cause

of the

IOException

should be an

UnrecoverableKeyException
**Throws:** NoSuchAlgorithmException

- if the algorithm used to check
the integrity of the keystore cannot be found
**Throws:** CertificateException

- if any of the certificates in the
keystore could not be loaded

- engineLoad

```java
public void engineLoad​(
KeyStore.LoadStoreParameter
param)
throws
IOException
,

NoSuchAlgorithmException
,

CertificateException
```

Loads the keystore using the given

KeyStore.LoadStoreParameter

.

Note that if this KeyStore has already been loaded, it is
reinitialized and loaded again from the given parameter.

**Implementation Requirements:** The default implementation examines

KeyStore.LoadStoreParameter

to extract its password and pass it to

engineLoad(InputStream, char[])

along with a

null

InputStream

.

If

KeyStore.LoadStoreParameter

is

null

then
the password parameter will also be

null

.
Otherwise the

KeyStore.ProtectionParameter

of

KeyStore.LoadStoreParameter

must be either a

KeyStore.PasswordProtection

or a

KeyStore.CallbackHandlerProtection

that supports

PasswordCallback

so that the password parameter can be
extracted. If the

KeyStore.ProtectionParameter

is neither
of those classes then a

NoSuchAlgorithmException

is thrown.
**Parameters:** param

- the

KeyStore.LoadStoreParameter

that specifies how to load the keystore,
which may be

null
**Throws:** IllegalArgumentException

- if the given

KeyStore.LoadStoreParameter

input is not recognized
**Throws:** IOException

- if there is an I/O or format problem with the
keystore data. If the error is due to an incorrect

ProtectionParameter

(e.g. wrong password)
the

cause

of the

IOException

should be an

UnrecoverableKeyException
**Throws:** NoSuchAlgorithmException

- if the algorithm used to check
the integrity of the keystore cannot be found
**Throws:** CertificateException

- if any of the certificates in the
keystore could not be loaded
**Since:** 1.5

- engineGetEntry

```java
public
KeyStore.Entry
engineGetEntry​(
String
alias,

KeyStore.ProtectionParameter
protParam)
throws
KeyStoreException
,

NoSuchAlgorithmException
,

UnrecoverableEntryException
```

Gets a

KeyStore.Entry

for the specified alias
with the specified protection parameter.

**Parameters:** alias

- get the

KeyStore.Entry

for this alias
**Parameters:** protParam

- the

ProtectionParameter

used to protect the

Entry

,
which may be

null
**Returns:** the

KeyStore.Entry

for the specified alias,
or

null

if there is no such entry
**Throws:** KeyStoreException

- if the operation failed
**Throws:** NoSuchAlgorithmException

- if the algorithm for recovering the
entry cannot be found
**Throws:** UnrecoverableEntryException

- if the specified

protParam

were insufficient or invalid
**Throws:** UnrecoverableKeyException

- if the entry is a

PrivateKeyEntry

or

SecretKeyEntry

and the specified

protParam

does not contain
the information needed to recover the key (e.g. wrong password)
**Since:** 1.5

- engineSetEntry

```java
public void engineSetEntry​(
String
alias,

KeyStore.Entry
entry,

KeyStore.ProtectionParameter
protParam)
throws
KeyStoreException
```

Saves a

KeyStore.Entry

under the specified alias.
The specified protection parameter is used to protect the

Entry

.

If an entry already exists for the specified alias,
it is overridden.

**Parameters:** alias

- save the

KeyStore.Entry

under this alias
**Parameters:** entry

- the

Entry

to save
**Parameters:** protParam

- the

ProtectionParameter

used to protect the

Entry

,
which may be

null
**Throws:** KeyStoreException

- if this operation fails
**Since:** 1.5

- engineEntryInstanceOf

```java
public boolean engineEntryInstanceOf​(
String
alias,

Class
<? extends
KeyStore.Entry
> entryClass)
```

Determines if the keystore

Entry

for the specified

alias

is an instance or subclass of the specified

entryClass

.

**Parameters:** alias

- the alias name
**Parameters:** entryClass

- the entry class
**Returns:** true if the keystore

Entry

for the specified

alias

is an instance or subclass of the
specified

entryClass

, false otherwise
**Since:** 1.5

- engineProbe

```java
public boolean engineProbe​(
InputStream
stream)
throws
IOException
```

Probes the specified input stream to determine whether it contains a
keystore that is supported by this implementation, or not.

**Implementation Requirements:** This method returns false by default. Keystore implementations should
override this method to peek at the data stream directly or to use other
content detection mechanisms.
**Parameters:** stream

- the keystore data to be probed
**Returns:** true if the keystore data is supported, otherwise false
**Throws:** IOException

- if there is an I/O problem with the keystore data.
**Throws:** NullPointerException

- if stream is

null

.
**Since:** 9

Constructor Detail

- KeyStoreSpi

```java
public KeyStoreSpi()
```

---

#### Constructor Detail

KeyStoreSpi

```java
public KeyStoreSpi()
```

---

#### KeyStoreSpi

public KeyStoreSpi()

Method Detail

- engineGetKey

```java
public abstract
Key
engineGetKey​(
String
alias,
char[] password)
throws
NoSuchAlgorithmException
,

UnrecoverableKeyException
```

Returns the key associated with the given alias, using the given
password to recover it. The key must have been associated with
the alias by a call to

setKeyEntry

,
or by a call to

setEntry

with a

PrivateKeyEntry

or

SecretKeyEntry

.

**Parameters:** alias

- the alias name
**Parameters:** password

- the password for recovering the key
**Returns:** the requested key, or null if the given alias does not exist
or does not identify a key-related entry.
**Throws:** NoSuchAlgorithmException

- if the algorithm for recovering the
key cannot be found
**Throws:** UnrecoverableKeyException

- if the key cannot be recovered
(e.g., the given password is wrong).

- engineGetCertificateChain

```java
public abstract
Certificate
[] engineGetCertificateChain​(
String
alias)
```

Returns the certificate chain associated with the given alias.
The certificate chain must have been associated with the alias
by a call to

setKeyEntry

,
or by a call to

setEntry

with a

PrivateKeyEntry

.

**Parameters:** alias

- the alias name
**Returns:** the certificate chain (ordered with the user's certificate first
and the root certificate authority last), or null if the given alias
does not exist or does not contain a certificate chain

- engineGetCertificate

```java
public abstract
Certificate
engineGetCertificate​(
String
alias)
```

Returns the certificate associated with the given alias.

If the given alias name identifies an entry
created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

,
then the trusted certificate contained in that entry is returned.

If the given alias name identifies an entry
created by a call to

setKeyEntry

,
or created by a call to

setEntry

with a

PrivateKeyEntry

,
then the first element of the certificate chain in that entry
(if a chain exists) is returned.

**Parameters:** alias

- the alias name
**Returns:** the certificate, or null if the given alias does not exist or
does not contain a certificate.

- engineGetCreationDate

```java
public abstract
Date
engineGetCreationDate​(
String
alias)
```

Returns the creation date of the entry identified by the given alias.

**Parameters:** alias

- the alias name
**Returns:** the creation date of this entry, or null if the given alias does
not exist

- engineSetKeyEntry

```java
public abstract void engineSetKeyEntry​(
String
alias,

Key
key,
char[] password,

Certificate
[] chain)
throws
KeyStoreException
```

Assigns the given key to the given alias, protecting it with the given
password.

If the given key is of type

java.security.PrivateKey

,
it must be accompanied by a certificate chain certifying the
corresponding public key.

If the given alias already exists, the keystore information
associated with it is overridden by the given key (and possibly
certificate chain).

**Parameters:** alias

- the alias name
**Parameters:** key

- the key to be associated with the alias
**Parameters:** password

- the password to protect the key
**Parameters:** chain

- the certificate chain for the corresponding public
key (only required if the given key is of type

java.security.PrivateKey

).
**Throws:** KeyStoreException

- if the given key cannot be protected, or
this operation fails for some other reason

- engineSetKeyEntry

```java
public abstract void engineSetKeyEntry​(
String
alias,
byte[] key,

Certificate
[] chain)
throws
KeyStoreException
```

Assigns the given key (that has already been protected) to the given
alias.

If the protected key is of type

java.security.PrivateKey

,
it must be accompanied by a certificate chain certifying the
corresponding public key.

If the given alias already exists, the keystore information
associated with it is overridden by the given key (and possibly
certificate chain).

**Parameters:** alias

- the alias name
**Parameters:** key

- the key (in protected format) to be associated with the alias
**Parameters:** chain

- the certificate chain for the corresponding public
key (only useful if the protected key is of type

java.security.PrivateKey

).
**Throws:** KeyStoreException

- if this operation fails.

- engineSetCertificateEntry

```java
public abstract void engineSetCertificateEntry​(
String
alias,

Certificate
cert)
throws
KeyStoreException
```

Assigns the given certificate to the given alias.

If the given alias identifies an existing entry
created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

,
the trusted certificate in the existing entry
is overridden by the given certificate.

**Parameters:** alias

- the alias name
**Parameters:** cert

- the certificate
**Throws:** KeyStoreException

- if the given alias already exists and does
not identify an entry containing a trusted certificate,
or this operation fails for some other reason.

- engineDeleteEntry

```java
public abstract void engineDeleteEntry​(
String
alias)
throws
KeyStoreException
```

Deletes the entry identified by the given alias from this keystore.

**Parameters:** alias

- the alias name
**Throws:** KeyStoreException

- if the entry cannot be removed.

- engineAliases

```java
public abstract
Enumeration
<
String
> engineAliases()
```

Lists all the alias names of this keystore.

**Returns:** enumeration of the alias names

- engineContainsAlias

```java
public abstract boolean engineContainsAlias​(
String
alias)
```

Checks if the given alias exists in this keystore.

**Parameters:** alias

- the alias name
**Returns:** true if the alias exists, false otherwise

- engineSize

```java
public abstract int engineSize()
```

Retrieves the number of entries in this keystore.

**Returns:** the number of entries in this keystore

- engineIsKeyEntry

```java
public abstract boolean engineIsKeyEntry​(
String
alias)
```

Returns true if the entry identified by the given alias
was created by a call to

setKeyEntry

,
or created by a call to

setEntry

with a

PrivateKeyEntry

or a

SecretKeyEntry

.

**Parameters:** alias

- the alias for the keystore entry to be checked
**Returns:** true if the entry identified by the given alias is a
key-related, false otherwise.

- engineIsCertificateEntry

```java
public abstract boolean engineIsCertificateEntry​(
String
alias)
```

Returns true if the entry identified by the given alias
was created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

.

**Parameters:** alias

- the alias for the keystore entry to be checked
**Returns:** true if the entry identified by the given alias contains a
trusted certificate, false otherwise.

- engineGetCertificateAlias

```java
public abstract
String
engineGetCertificateAlias​(
Certificate
cert)
```

Returns the (alias) name of the first keystore entry whose certificate
matches the given certificate.

This method attempts to match the given certificate with each
keystore entry. If the entry being considered was
created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

,
then the given certificate is compared to that entry's certificate.

If the entry being considered was
created by a call to

setKeyEntry

,
or created by a call to

setEntry

with a

PrivateKeyEntry

,
then the given certificate is compared to the first
element of that entry's certificate chain.

**Parameters:** cert

- the certificate to match with.
**Returns:** the alias name of the first entry with matching certificate,
or null if no such entry exists in this keystore.

- engineStore

```java
public abstract void engineStore​(
OutputStream
stream,
char[] password)
throws
IOException
,

NoSuchAlgorithmException
,

CertificateException
```

Stores this keystore to the given output stream, and protects its
integrity with the given password.

**Parameters:** stream

- the output stream to which this keystore is written.
**Parameters:** password

- the password to generate the keystore integrity check
**Throws:** IOException

- if there was an I/O problem with data
**Throws:** NoSuchAlgorithmException

- if the appropriate data integrity
algorithm could not be found
**Throws:** CertificateException

- if any of the certificates included in
the keystore data could not be stored

- engineStore

```java
public void engineStore​(
KeyStore.LoadStoreParameter
param)
throws
IOException
,

NoSuchAlgorithmException
,

CertificateException
```

Stores this keystore using the given

KeyStore.LoadStoreParmeter

.

**Parameters:** param

- the

KeyStore.LoadStoreParmeter

that specifies how to store the keystore,
which may be

null
**Throws:** IllegalArgumentException

- if the given

KeyStore.LoadStoreParmeter

input is not recognized
**Throws:** IOException

- if there was an I/O problem with data
**Throws:** NoSuchAlgorithmException

- if the appropriate data integrity
algorithm could not be found
**Throws:** CertificateException

- if any of the certificates included in
the keystore data could not be stored
**Since:** 1.5

- engineLoad

```java
public abstract void engineLoad​(
InputStream
stream,
char[] password)
throws
IOException
,

NoSuchAlgorithmException
,

CertificateException
```

Loads the keystore from the given input stream.

A password may be given to unlock the keystore
(e.g. the keystore resides on a hardware token device),
or to check the integrity of the keystore data.
If a password is not given for integrity checking,
then integrity checking is not performed.

**Parameters:** stream

- the input stream from which the keystore is loaded,
or

null
**Parameters:** password

- the password used to check the integrity of
the keystore, the password used to unlock the keystore,
or

null
**Throws:** IOException

- if there is an I/O or format problem with the
keystore data, if a password is required but not given,
or if the given password was incorrect. If the error is due to a
wrong password, the

cause

of the

IOException

should be an

UnrecoverableKeyException
**Throws:** NoSuchAlgorithmException

- if the algorithm used to check
the integrity of the keystore cannot be found
**Throws:** CertificateException

- if any of the certificates in the
keystore could not be loaded

- engineLoad

```java
public void engineLoad​(
KeyStore.LoadStoreParameter
param)
throws
IOException
,

NoSuchAlgorithmException
,

CertificateException
```

Loads the keystore using the given

KeyStore.LoadStoreParameter

.

Note that if this KeyStore has already been loaded, it is
reinitialized and loaded again from the given parameter.

**Implementation Requirements:** The default implementation examines

KeyStore.LoadStoreParameter

to extract its password and pass it to

engineLoad(InputStream, char[])

along with a

null

InputStream

.

If

KeyStore.LoadStoreParameter

is

null

then
the password parameter will also be

null

.
Otherwise the

KeyStore.ProtectionParameter

of

KeyStore.LoadStoreParameter

must be either a

KeyStore.PasswordProtection

or a

KeyStore.CallbackHandlerProtection

that supports

PasswordCallback

so that the password parameter can be
extracted. If the

KeyStore.ProtectionParameter

is neither
of those classes then a

NoSuchAlgorithmException

is thrown.
**Parameters:** param

- the

KeyStore.LoadStoreParameter

that specifies how to load the keystore,
which may be

null
**Throws:** IllegalArgumentException

- if the given

KeyStore.LoadStoreParameter

input is not recognized
**Throws:** IOException

- if there is an I/O or format problem with the
keystore data. If the error is due to an incorrect

ProtectionParameter

(e.g. wrong password)
the

cause

of the

IOException

should be an

UnrecoverableKeyException
**Throws:** NoSuchAlgorithmException

- if the algorithm used to check
the integrity of the keystore cannot be found
**Throws:** CertificateException

- if any of the certificates in the
keystore could not be loaded
**Since:** 1.5

- engineGetEntry

```java
public
KeyStore.Entry
engineGetEntry​(
String
alias,

KeyStore.ProtectionParameter
protParam)
throws
KeyStoreException
,

NoSuchAlgorithmException
,

UnrecoverableEntryException
```

Gets a

KeyStore.Entry

for the specified alias
with the specified protection parameter.

**Parameters:** alias

- get the

KeyStore.Entry

for this alias
**Parameters:** protParam

- the

ProtectionParameter

used to protect the

Entry

,
which may be

null
**Returns:** the

KeyStore.Entry

for the specified alias,
or

null

if there is no such entry
**Throws:** KeyStoreException

- if the operation failed
**Throws:** NoSuchAlgorithmException

- if the algorithm for recovering the
entry cannot be found
**Throws:** UnrecoverableEntryException

- if the specified

protParam

were insufficient or invalid
**Throws:** UnrecoverableKeyException

- if the entry is a

PrivateKeyEntry

or

SecretKeyEntry

and the specified

protParam

does not contain
the information needed to recover the key (e.g. wrong password)
**Since:** 1.5

- engineSetEntry

```java
public void engineSetEntry​(
String
alias,

KeyStore.Entry
entry,

KeyStore.ProtectionParameter
protParam)
throws
KeyStoreException
```

Saves a

KeyStore.Entry

under the specified alias.
The specified protection parameter is used to protect the

Entry

.

If an entry already exists for the specified alias,
it is overridden.

**Parameters:** alias

- save the

KeyStore.Entry

under this alias
**Parameters:** entry

- the

Entry

to save
**Parameters:** protParam

- the

ProtectionParameter

used to protect the

Entry

,
which may be

null
**Throws:** KeyStoreException

- if this operation fails
**Since:** 1.5

- engineEntryInstanceOf

```java
public boolean engineEntryInstanceOf​(
String
alias,

Class
<? extends
KeyStore.Entry
> entryClass)
```

Determines if the keystore

Entry

for the specified

alias

is an instance or subclass of the specified

entryClass

.

**Parameters:** alias

- the alias name
**Parameters:** entryClass

- the entry class
**Returns:** true if the keystore

Entry

for the specified

alias

is an instance or subclass of the
specified

entryClass

, false otherwise
**Since:** 1.5

- engineProbe

```java
public boolean engineProbe​(
InputStream
stream)
throws
IOException
```

Probes the specified input stream to determine whether it contains a
keystore that is supported by this implementation, or not.

**Implementation Requirements:** This method returns false by default. Keystore implementations should
override this method to peek at the data stream directly or to use other
content detection mechanisms.
**Parameters:** stream

- the keystore data to be probed
**Returns:** true if the keystore data is supported, otherwise false
**Throws:** IOException

- if there is an I/O problem with the keystore data.
**Throws:** NullPointerException

- if stream is

null

.
**Since:** 9

---

#### Method Detail

engineGetKey

```java
public abstract
Key
engineGetKey​(
String
alias,
char[] password)
throws
NoSuchAlgorithmException
,

UnrecoverableKeyException
```

Returns the key associated with the given alias, using the given
password to recover it. The key must have been associated with
the alias by a call to

setKeyEntry

,
or by a call to

setEntry

with a

PrivateKeyEntry

or

SecretKeyEntry

.

**Parameters:** alias

- the alias name
**Parameters:** password

- the password for recovering the key
**Returns:** the requested key, or null if the given alias does not exist
or does not identify a key-related entry.
**Throws:** NoSuchAlgorithmException

- if the algorithm for recovering the
key cannot be found
**Throws:** UnrecoverableKeyException

- if the key cannot be recovered
(e.g., the given password is wrong).

---

#### engineGetKey

public abstract

Key

engineGetKey​(

String

alias,
char[] password)
throws

NoSuchAlgorithmException

,

UnrecoverableKeyException

Returns the key associated with the given alias, using the given
password to recover it. The key must have been associated with
the alias by a call to

setKeyEntry

,
or by a call to

setEntry

with a

PrivateKeyEntry

or

SecretKeyEntry

.

engineGetCertificateChain

```java
public abstract
Certificate
[] engineGetCertificateChain​(
String
alias)
```

Returns the certificate chain associated with the given alias.
The certificate chain must have been associated with the alias
by a call to

setKeyEntry

,
or by a call to

setEntry

with a

PrivateKeyEntry

.

**Parameters:** alias

- the alias name
**Returns:** the certificate chain (ordered with the user's certificate first
and the root certificate authority last), or null if the given alias
does not exist or does not contain a certificate chain

---

#### engineGetCertificateChain

public abstract

Certificate

[] engineGetCertificateChain​(

String

alias)

Returns the certificate chain associated with the given alias.
The certificate chain must have been associated with the alias
by a call to

setKeyEntry

,
or by a call to

setEntry

with a

PrivateKeyEntry

.

engineGetCertificate

```java
public abstract
Certificate
engineGetCertificate​(
String
alias)
```

Returns the certificate associated with the given alias.

If the given alias name identifies an entry
created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

,
then the trusted certificate contained in that entry is returned.

If the given alias name identifies an entry
created by a call to

setKeyEntry

,
or created by a call to

setEntry

with a

PrivateKeyEntry

,
then the first element of the certificate chain in that entry
(if a chain exists) is returned.

**Parameters:** alias

- the alias name
**Returns:** the certificate, or null if the given alias does not exist or
does not contain a certificate.

---

#### engineGetCertificate

public abstract

Certificate

engineGetCertificate​(

String

alias)

Returns the certificate associated with the given alias.

If the given alias name identifies an entry
created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

,
then the trusted certificate contained in that entry is returned.

If the given alias name identifies an entry
created by a call to

setKeyEntry

,
or created by a call to

setEntry

with a

PrivateKeyEntry

,
then the first element of the certificate chain in that entry
(if a chain exists) is returned.

If the given alias name identifies an entry
created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

,
then the trusted certificate contained in that entry is returned.

If the given alias name identifies an entry
created by a call to

setKeyEntry

,
or created by a call to

setEntry

with a

PrivateKeyEntry

,
then the first element of the certificate chain in that entry
(if a chain exists) is returned.

If the given alias name identifies an entry
created by a call to

setKeyEntry

,
or created by a call to

setEntry

with a

PrivateKeyEntry

,
then the first element of the certificate chain in that entry
(if a chain exists) is returned.

engineGetCreationDate

```java
public abstract
Date
engineGetCreationDate​(
String
alias)
```

Returns the creation date of the entry identified by the given alias.

**Parameters:** alias

- the alias name
**Returns:** the creation date of this entry, or null if the given alias does
not exist

---

#### engineGetCreationDate

public abstract

Date

engineGetCreationDate​(

String

alias)

Returns the creation date of the entry identified by the given alias.

engineSetKeyEntry

```java
public abstract void engineSetKeyEntry​(
String
alias,

Key
key,
char[] password,

Certificate
[] chain)
throws
KeyStoreException
```

Assigns the given key to the given alias, protecting it with the given
password.

If the given key is of type

java.security.PrivateKey

,
it must be accompanied by a certificate chain certifying the
corresponding public key.

If the given alias already exists, the keystore information
associated with it is overridden by the given key (and possibly
certificate chain).

**Parameters:** alias

- the alias name
**Parameters:** key

- the key to be associated with the alias
**Parameters:** password

- the password to protect the key
**Parameters:** chain

- the certificate chain for the corresponding public
key (only required if the given key is of type

java.security.PrivateKey

).
**Throws:** KeyStoreException

- if the given key cannot be protected, or
this operation fails for some other reason

---

#### engineSetKeyEntry

public abstract void engineSetKeyEntry​(

String

alias,

Key

key,
char[] password,

Certificate

[] chain)
throws

KeyStoreException

Assigns the given key to the given alias, protecting it with the given
password.

If the given key is of type

java.security.PrivateKey

,
it must be accompanied by a certificate chain certifying the
corresponding public key.

If the given alias already exists, the keystore information
associated with it is overridden by the given key (and possibly
certificate chain).

If the given key is of type

java.security.PrivateKey

,
it must be accompanied by a certificate chain certifying the
corresponding public key.

If the given alias already exists, the keystore information
associated with it is overridden by the given key (and possibly
certificate chain).

If the given alias already exists, the keystore information
associated with it is overridden by the given key (and possibly
certificate chain).

engineSetKeyEntry

```java
public abstract void engineSetKeyEntry​(
String
alias,
byte[] key,

Certificate
[] chain)
throws
KeyStoreException
```

Assigns the given key (that has already been protected) to the given
alias.

If the protected key is of type

java.security.PrivateKey

,
it must be accompanied by a certificate chain certifying the
corresponding public key.

If the given alias already exists, the keystore information
associated with it is overridden by the given key (and possibly
certificate chain).

**Parameters:** alias

- the alias name
**Parameters:** key

- the key (in protected format) to be associated with the alias
**Parameters:** chain

- the certificate chain for the corresponding public
key (only useful if the protected key is of type

java.security.PrivateKey

).
**Throws:** KeyStoreException

- if this operation fails.

---

#### engineSetKeyEntry

public abstract void engineSetKeyEntry​(

String

alias,
byte[] key,

Certificate

[] chain)
throws

KeyStoreException

Assigns the given key (that has already been protected) to the given
alias.

If the protected key is of type

java.security.PrivateKey

,
it must be accompanied by a certificate chain certifying the
corresponding public key.

If the given alias already exists, the keystore information
associated with it is overridden by the given key (and possibly
certificate chain).

If the protected key is of type

java.security.PrivateKey

,
it must be accompanied by a certificate chain certifying the
corresponding public key.

If the given alias already exists, the keystore information
associated with it is overridden by the given key (and possibly
certificate chain).

If the given alias already exists, the keystore information
associated with it is overridden by the given key (and possibly
certificate chain).

engineSetCertificateEntry

```java
public abstract void engineSetCertificateEntry​(
String
alias,

Certificate
cert)
throws
KeyStoreException
```

Assigns the given certificate to the given alias.

If the given alias identifies an existing entry
created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

,
the trusted certificate in the existing entry
is overridden by the given certificate.

**Parameters:** alias

- the alias name
**Parameters:** cert

- the certificate
**Throws:** KeyStoreException

- if the given alias already exists and does
not identify an entry containing a trusted certificate,
or this operation fails for some other reason.

---

#### engineSetCertificateEntry

public abstract void engineSetCertificateEntry​(

String

alias,

Certificate

cert)
throws

KeyStoreException

Assigns the given certificate to the given alias.

If the given alias identifies an existing entry
created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

,
the trusted certificate in the existing entry
is overridden by the given certificate.

If the given alias identifies an existing entry
created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

,
the trusted certificate in the existing entry
is overridden by the given certificate.

engineDeleteEntry

```java
public abstract void engineDeleteEntry​(
String
alias)
throws
KeyStoreException
```

Deletes the entry identified by the given alias from this keystore.

**Parameters:** alias

- the alias name
**Throws:** KeyStoreException

- if the entry cannot be removed.

---

#### engineDeleteEntry

public abstract void engineDeleteEntry​(

String

alias)
throws

KeyStoreException

Deletes the entry identified by the given alias from this keystore.

engineAliases

```java
public abstract
Enumeration
<
String
> engineAliases()
```

Lists all the alias names of this keystore.

**Returns:** enumeration of the alias names

---

#### engineAliases

public abstract

Enumeration

<

String

> engineAliases()

Lists all the alias names of this keystore.

engineContainsAlias

```java
public abstract boolean engineContainsAlias​(
String
alias)
```

Checks if the given alias exists in this keystore.

**Parameters:** alias

- the alias name
**Returns:** true if the alias exists, false otherwise

---

#### engineContainsAlias

public abstract boolean engineContainsAlias​(

String

alias)

Checks if the given alias exists in this keystore.

engineSize

```java
public abstract int engineSize()
```

Retrieves the number of entries in this keystore.

**Returns:** the number of entries in this keystore

---

#### engineSize

public abstract int engineSize()

Retrieves the number of entries in this keystore.

engineIsKeyEntry

```java
public abstract boolean engineIsKeyEntry​(
String
alias)
```

Returns true if the entry identified by the given alias
was created by a call to

setKeyEntry

,
or created by a call to

setEntry

with a

PrivateKeyEntry

or a

SecretKeyEntry

.

**Parameters:** alias

- the alias for the keystore entry to be checked
**Returns:** true if the entry identified by the given alias is a
key-related, false otherwise.

---

#### engineIsKeyEntry

public abstract boolean engineIsKeyEntry​(

String

alias)

Returns true if the entry identified by the given alias
was created by a call to

setKeyEntry

,
or created by a call to

setEntry

with a

PrivateKeyEntry

or a

SecretKeyEntry

.

engineIsCertificateEntry

```java
public abstract boolean engineIsCertificateEntry​(
String
alias)
```

Returns true if the entry identified by the given alias
was created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

.

**Parameters:** alias

- the alias for the keystore entry to be checked
**Returns:** true if the entry identified by the given alias contains a
trusted certificate, false otherwise.

---

#### engineIsCertificateEntry

public abstract boolean engineIsCertificateEntry​(

String

alias)

Returns true if the entry identified by the given alias
was created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

.

engineGetCertificateAlias

```java
public abstract
String
engineGetCertificateAlias​(
Certificate
cert)
```

Returns the (alias) name of the first keystore entry whose certificate
matches the given certificate.

This method attempts to match the given certificate with each
keystore entry. If the entry being considered was
created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

,
then the given certificate is compared to that entry's certificate.

If the entry being considered was
created by a call to

setKeyEntry

,
or created by a call to

setEntry

with a

PrivateKeyEntry

,
then the given certificate is compared to the first
element of that entry's certificate chain.

**Parameters:** cert

- the certificate to match with.
**Returns:** the alias name of the first entry with matching certificate,
or null if no such entry exists in this keystore.

---

#### engineGetCertificateAlias

public abstract

String

engineGetCertificateAlias​(

Certificate

cert)

Returns the (alias) name of the first keystore entry whose certificate
matches the given certificate.

This method attempts to match the given certificate with each
keystore entry. If the entry being considered was
created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

,
then the given certificate is compared to that entry's certificate.

If the entry being considered was
created by a call to

setKeyEntry

,
or created by a call to

setEntry

with a

PrivateKeyEntry

,
then the given certificate is compared to the first
element of that entry's certificate chain.

This method attempts to match the given certificate with each
keystore entry. If the entry being considered was
created by a call to

setCertificateEntry

,
or created by a call to

setEntry

with a

TrustedCertificateEntry

,
then the given certificate is compared to that entry's certificate.

If the entry being considered was
created by a call to

setKeyEntry

,
or created by a call to

setEntry

with a

PrivateKeyEntry

,
then the given certificate is compared to the first
element of that entry's certificate chain.

If the entry being considered was
created by a call to

setKeyEntry

,
or created by a call to

setEntry

with a

PrivateKeyEntry

,
then the given certificate is compared to the first
element of that entry's certificate chain.

engineStore

```java
public abstract void engineStore​(
OutputStream
stream,
char[] password)
throws
IOException
,

NoSuchAlgorithmException
,

CertificateException
```

Stores this keystore to the given output stream, and protects its
integrity with the given password.

**Parameters:** stream

- the output stream to which this keystore is written.
**Parameters:** password

- the password to generate the keystore integrity check
**Throws:** IOException

- if there was an I/O problem with data
**Throws:** NoSuchAlgorithmException

- if the appropriate data integrity
algorithm could not be found
**Throws:** CertificateException

- if any of the certificates included in
the keystore data could not be stored

---

#### engineStore

public abstract void engineStore​(

OutputStream

stream,
char[] password)
throws

IOException

,

NoSuchAlgorithmException

,

CertificateException

Stores this keystore to the given output stream, and protects its
integrity with the given password.

engineStore

```java
public void engineStore​(
KeyStore.LoadStoreParameter
param)
throws
IOException
,

NoSuchAlgorithmException
,

CertificateException
```

Stores this keystore using the given

KeyStore.LoadStoreParmeter

.

**Parameters:** param

- the

KeyStore.LoadStoreParmeter

that specifies how to store the keystore,
which may be

null
**Throws:** IllegalArgumentException

- if the given

KeyStore.LoadStoreParmeter

input is not recognized
**Throws:** IOException

- if there was an I/O problem with data
**Throws:** NoSuchAlgorithmException

- if the appropriate data integrity
algorithm could not be found
**Throws:** CertificateException

- if any of the certificates included in
the keystore data could not be stored
**Since:** 1.5

---

#### engineStore

public void engineStore​(

KeyStore.LoadStoreParameter

param)
throws

IOException

,

NoSuchAlgorithmException

,

CertificateException

Stores this keystore using the given

KeyStore.LoadStoreParmeter

.

engineLoad

```java
public abstract void engineLoad​(
InputStream
stream,
char[] password)
throws
IOException
,

NoSuchAlgorithmException
,

CertificateException
```

Loads the keystore from the given input stream.

A password may be given to unlock the keystore
(e.g. the keystore resides on a hardware token device),
or to check the integrity of the keystore data.
If a password is not given for integrity checking,
then integrity checking is not performed.

**Parameters:** stream

- the input stream from which the keystore is loaded,
or

null
**Parameters:** password

- the password used to check the integrity of
the keystore, the password used to unlock the keystore,
or

null
**Throws:** IOException

- if there is an I/O or format problem with the
keystore data, if a password is required but not given,
or if the given password was incorrect. If the error is due to a
wrong password, the

cause

of the

IOException

should be an

UnrecoverableKeyException
**Throws:** NoSuchAlgorithmException

- if the algorithm used to check
the integrity of the keystore cannot be found
**Throws:** CertificateException

- if any of the certificates in the
keystore could not be loaded

---

#### engineLoad

public abstract void engineLoad​(

InputStream

stream,
char[] password)
throws

IOException

,

NoSuchAlgorithmException

,

CertificateException

Loads the keystore from the given input stream.

A password may be given to unlock the keystore
(e.g. the keystore resides on a hardware token device),
or to check the integrity of the keystore data.
If a password is not given for integrity checking,
then integrity checking is not performed.

A password may be given to unlock the keystore
(e.g. the keystore resides on a hardware token device),
or to check the integrity of the keystore data.
If a password is not given for integrity checking,
then integrity checking is not performed.

engineLoad

```java
public void engineLoad​(
KeyStore.LoadStoreParameter
param)
throws
IOException
,

NoSuchAlgorithmException
,

CertificateException
```

Loads the keystore using the given

KeyStore.LoadStoreParameter

.

Note that if this KeyStore has already been loaded, it is
reinitialized and loaded again from the given parameter.

**Implementation Requirements:** The default implementation examines

KeyStore.LoadStoreParameter

to extract its password and pass it to

engineLoad(InputStream, char[])

along with a

null

InputStream

.

If

KeyStore.LoadStoreParameter

is

null

then
the password parameter will also be

null

.
Otherwise the

KeyStore.ProtectionParameter

of

KeyStore.LoadStoreParameter

must be either a

KeyStore.PasswordProtection

or a

KeyStore.CallbackHandlerProtection

that supports

PasswordCallback

so that the password parameter can be
extracted. If the

KeyStore.ProtectionParameter

is neither
of those classes then a

NoSuchAlgorithmException

is thrown.
**Parameters:** param

- the

KeyStore.LoadStoreParameter

that specifies how to load the keystore,
which may be

null
**Throws:** IllegalArgumentException

- if the given

KeyStore.LoadStoreParameter

input is not recognized
**Throws:** IOException

- if there is an I/O or format problem with the
keystore data. If the error is due to an incorrect

ProtectionParameter

(e.g. wrong password)
the

cause

of the

IOException

should be an

UnrecoverableKeyException
**Throws:** NoSuchAlgorithmException

- if the algorithm used to check
the integrity of the keystore cannot be found
**Throws:** CertificateException

- if any of the certificates in the
keystore could not be loaded
**Since:** 1.5

---

#### engineLoad

public void engineLoad​(

KeyStore.LoadStoreParameter

param)
throws

IOException

,

NoSuchAlgorithmException

,

CertificateException

Loads the keystore using the given

KeyStore.LoadStoreParameter

.

Note that if this KeyStore has already been loaded, it is
reinitialized and loaded again from the given parameter.

Note that if this KeyStore has already been loaded, it is
reinitialized and loaded again from the given parameter.

If

KeyStore.LoadStoreParameter

is

null

then
the password parameter will also be

null

.
Otherwise the

KeyStore.ProtectionParameter

of

KeyStore.LoadStoreParameter

must be either a

KeyStore.PasswordProtection

or a

KeyStore.CallbackHandlerProtection

that supports

PasswordCallback

so that the password parameter can be
extracted. If the

KeyStore.ProtectionParameter

is neither
of those classes then a

NoSuchAlgorithmException

is thrown.

engineGetEntry

```java
public
KeyStore.Entry
engineGetEntry​(
String
alias,

KeyStore.ProtectionParameter
protParam)
throws
KeyStoreException
,

NoSuchAlgorithmException
,

UnrecoverableEntryException
```

Gets a

KeyStore.Entry

for the specified alias
with the specified protection parameter.

**Parameters:** alias

- get the

KeyStore.Entry

for this alias
**Parameters:** protParam

- the

ProtectionParameter

used to protect the

Entry

,
which may be

null
**Returns:** the

KeyStore.Entry

for the specified alias,
or

null

if there is no such entry
**Throws:** KeyStoreException

- if the operation failed
**Throws:** NoSuchAlgorithmException

- if the algorithm for recovering the
entry cannot be found
**Throws:** UnrecoverableEntryException

- if the specified

protParam

were insufficient or invalid
**Throws:** UnrecoverableKeyException

- if the entry is a

PrivateKeyEntry

or

SecretKeyEntry

and the specified

protParam

does not contain
the information needed to recover the key (e.g. wrong password)
**Since:** 1.5

---

#### engineGetEntry

public

KeyStore.Entry

engineGetEntry​(

String

alias,

KeyStore.ProtectionParameter

protParam)
throws

KeyStoreException

,

NoSuchAlgorithmException

,

UnrecoverableEntryException

Gets a

KeyStore.Entry

for the specified alias
with the specified protection parameter.

engineSetEntry

```java
public void engineSetEntry​(
String
alias,

KeyStore.Entry
entry,

KeyStore.ProtectionParameter
protParam)
throws
KeyStoreException
```

Saves a

KeyStore.Entry

under the specified alias.
The specified protection parameter is used to protect the

Entry

.

If an entry already exists for the specified alias,
it is overridden.

**Parameters:** alias

- save the

KeyStore.Entry

under this alias
**Parameters:** entry

- the

Entry

to save
**Parameters:** protParam

- the

ProtectionParameter

used to protect the

Entry

,
which may be

null
**Throws:** KeyStoreException

- if this operation fails
**Since:** 1.5

---

#### engineSetEntry

public void engineSetEntry​(

String

alias,

KeyStore.Entry

entry,

KeyStore.ProtectionParameter

protParam)
throws

KeyStoreException

Saves a

KeyStore.Entry

under the specified alias.
The specified protection parameter is used to protect the

Entry

.

If an entry already exists for the specified alias,
it is overridden.

If an entry already exists for the specified alias,
it is overridden.

engineEntryInstanceOf

```java
public boolean engineEntryInstanceOf​(
String
alias,

Class
<? extends
KeyStore.Entry
> entryClass)
```

Determines if the keystore

Entry

for the specified

alias

is an instance or subclass of the specified

entryClass

.

**Parameters:** alias

- the alias name
**Parameters:** entryClass

- the entry class
**Returns:** true if the keystore

Entry

for the specified

alias

is an instance or subclass of the
specified

entryClass

, false otherwise
**Since:** 1.5

---

#### engineEntryInstanceOf

public boolean engineEntryInstanceOf​(

String

alias,

Class

<? extends

KeyStore.Entry

> entryClass)

Determines if the keystore

Entry

for the specified

alias

is an instance or subclass of the specified

entryClass

.

engineProbe

```java
public boolean engineProbe​(
InputStream
stream)
throws
IOException
```

Probes the specified input stream to determine whether it contains a
keystore that is supported by this implementation, or not.

**Implementation Requirements:** This method returns false by default. Keystore implementations should
override this method to peek at the data stream directly or to use other
content detection mechanisms.
**Parameters:** stream

- the keystore data to be probed
**Returns:** true if the keystore data is supported, otherwise false
**Throws:** IOException

- if there is an I/O problem with the keystore data.
**Throws:** NullPointerException

- if stream is

null

.
**Since:** 9

---

#### engineProbe

public boolean engineProbe​(

InputStream

stream)
throws

IOException

Probes the specified input stream to determine whether it contains a
keystore that is supported by this implementation, or not.

---

