# Class X500PrivateCredential

**Source:** `java.base\javax\security\auth\x500\X500PrivateCredential.html`

### Class Description

```java
public final class
X500PrivateCredential

extends
Object

implements
Destroyable
```

This class represents an

X500PrivateCredential

.
It associates an X.509 certificate, corresponding private key and the
KeyStore alias used to reference that exact key pair in the KeyStore.
This enables looking up the private credentials for an X.500 principal
in a subject.

**All Implemented Interfaces:** Destroyable

---

### Field Details

*No entries found.*

### Constructor Details

#### public X500PrivateCredential​(
X509Certificate
cert,

PrivateKey
key)

Creates an X500PrivateCredential that associates an X.509 certificate,
a private key and the KeyStore alias.

**Parameters:**
- cert

- X509Certificate
- key

- PrivateKey for the certificate

**Throws:**
- IllegalArgumentException

- if either

cert

or

key

is null

---

#### public X500PrivateCredential​(
X509Certificate
cert,

PrivateKey
key,

String
alias)

Creates an X500PrivateCredential that associates an X.509 certificate,
a private key and the KeyStore alias.

**Parameters:**
- cert

- X509Certificate
- key

- PrivateKey for the certificate
- alias

- KeyStore alias

**Throws:**
- IllegalArgumentException

- if either

cert

,

key

or

alias

is null

---

### Method Details

#### public
X509Certificate
getCertificate()

Returns the X.509 certificate.

**Returns:**
- the X509Certificate

---

#### public
PrivateKey
getPrivateKey()

Returns the PrivateKey.

**Returns:**
- the PrivateKey

---

#### public
String
getAlias()

Returns the KeyStore alias.

**Returns:**
- the KeyStore alias

---

#### public void destroy()

Clears the references to the X.509 certificate, private key and the
KeyStore alias in this object.

**Specified by:**
- destroy

in interface

Destroyable

---

#### public boolean isDestroyed()

Determines if the references to the X.509 certificate and private key
in this object have been cleared.

**Specified by:**
- isDestroyed

in interface

Destroyable

**Returns:**
- true if X509Certificate and the PrivateKey are null

---

### Additional Sections

#### Class X500PrivateCredential

java.lang.Object

- javax.security.auth.x500.X500PrivateCredential

javax.security.auth.x500.X500PrivateCredential

**All Implemented Interfaces:** Destroyable

```java
public final class
X500PrivateCredential

extends
Object

implements
Destroyable
```

This class represents an

X500PrivateCredential

.
It associates an X.509 certificate, corresponding private key and the
KeyStore alias used to reference that exact key pair in the KeyStore.
This enables looking up the private credentials for an X.500 principal
in a subject.

**Since:** 1.4

public final class

X500PrivateCredential

extends

Object

implements

Destroyable

This class represents an

X500PrivateCredential

.
It associates an X.509 certificate, corresponding private key and the
KeyStore alias used to reference that exact key pair in the KeyStore.
This enables looking up the private credentials for an X.500 principal
in a subject.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

X500PrivateCredential

​(

X509Certificate

cert,

PrivateKey

key)

Creates an X500PrivateCredential that associates an X.509 certificate,
a private key and the KeyStore alias.

X500PrivateCredential

​(

X509Certificate

cert,

PrivateKey

key,

String

alias)

Creates an X500PrivateCredential that associates an X.509 certificate,
a private key and the KeyStore alias.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

destroy

()

Clears the references to the X.509 certificate, private key and the
KeyStore alias in this object.

String

getAlias

()

Returns the KeyStore alias.

X509Certificate

getCertificate

()

Returns the X.509 certificate.

PrivateKey

getPrivateKey

()

Returns the PrivateKey.

boolean

isDestroyed

()

Determines if the references to the X.509 certificate and private key
in this object have been cleared.

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

X500PrivateCredential

​(

X509Certificate

cert,

PrivateKey

key)

Creates an X500PrivateCredential that associates an X.509 certificate,
a private key and the KeyStore alias.

X500PrivateCredential

​(

X509Certificate

cert,

PrivateKey

key,

String

alias)

Creates an X500PrivateCredential that associates an X.509 certificate,
a private key and the KeyStore alias.

---

#### Constructor Summary

Creates an X500PrivateCredential that associates an X.509 certificate,
a private key and the KeyStore alias.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

destroy

()

Clears the references to the X.509 certificate, private key and the
KeyStore alias in this object.

String

getAlias

()

Returns the KeyStore alias.

X509Certificate

getCertificate

()

Returns the X.509 certificate.

PrivateKey

getPrivateKey

()

Returns the PrivateKey.

boolean

isDestroyed

()

Determines if the references to the X.509 certificate and private key
in this object have been cleared.

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

Clears the references to the X.509 certificate, private key and the
KeyStore alias in this object.

Returns the KeyStore alias.

Returns the X.509 certificate.

Returns the PrivateKey.

Determines if the references to the X.509 certificate and private key
in this object have been cleared.

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

- X500PrivateCredential

```java
public X500PrivateCredential​(
X509Certificate
cert,

PrivateKey
key)
```

Creates an X500PrivateCredential that associates an X.509 certificate,
a private key and the KeyStore alias.

**Parameters:** cert

- X509Certificate
**Parameters:** key

- PrivateKey for the certificate
**Throws:** IllegalArgumentException

- if either

cert

or

key

is null

- X500PrivateCredential

```java
public X500PrivateCredential​(
X509Certificate
cert,

PrivateKey
key,

String
alias)
```

Creates an X500PrivateCredential that associates an X.509 certificate,
a private key and the KeyStore alias.

**Parameters:** cert

- X509Certificate
**Parameters:** key

- PrivateKey for the certificate
**Parameters:** alias

- KeyStore alias
**Throws:** IllegalArgumentException

- if either

cert

,

key

or

alias

is null

============ METHOD DETAIL ==========

- Method Detail

- getCertificate

```java
public
X509Certificate
getCertificate()
```

Returns the X.509 certificate.

**Returns:** the X509Certificate

- getPrivateKey

```java
public
PrivateKey
getPrivateKey()
```

Returns the PrivateKey.

**Returns:** the PrivateKey

- getAlias

```java
public
String
getAlias()
```

Returns the KeyStore alias.

**Returns:** the KeyStore alias

- destroy

```java
public void destroy()
```

Clears the references to the X.509 certificate, private key and the
KeyStore alias in this object.

**Specified by:** destroy

in interface

Destroyable

- isDestroyed

```java
public boolean isDestroyed()
```

Determines if the references to the X.509 certificate and private key
in this object have been cleared.

**Specified by:** isDestroyed

in interface

Destroyable
**Returns:** true if X509Certificate and the PrivateKey are null

Constructor Detail

- X500PrivateCredential

```java
public X500PrivateCredential​(
X509Certificate
cert,

PrivateKey
key)
```

Creates an X500PrivateCredential that associates an X.509 certificate,
a private key and the KeyStore alias.

**Parameters:** cert

- X509Certificate
**Parameters:** key

- PrivateKey for the certificate
**Throws:** IllegalArgumentException

- if either

cert

or

key

is null

- X500PrivateCredential

```java
public X500PrivateCredential​(
X509Certificate
cert,

PrivateKey
key,

String
alias)
```

Creates an X500PrivateCredential that associates an X.509 certificate,
a private key and the KeyStore alias.

**Parameters:** cert

- X509Certificate
**Parameters:** key

- PrivateKey for the certificate
**Parameters:** alias

- KeyStore alias
**Throws:** IllegalArgumentException

- if either

cert

,

key

or

alias

is null

---

#### Constructor Detail

X500PrivateCredential

```java
public X500PrivateCredential​(
X509Certificate
cert,

PrivateKey
key)
```

Creates an X500PrivateCredential that associates an X.509 certificate,
a private key and the KeyStore alias.

**Parameters:** cert

- X509Certificate
**Parameters:** key

- PrivateKey for the certificate
**Throws:** IllegalArgumentException

- if either

cert

or

key

is null

---

#### X500PrivateCredential

public X500PrivateCredential​(

X509Certificate

cert,

PrivateKey

key)

Creates an X500PrivateCredential that associates an X.509 certificate,
a private key and the KeyStore alias.

X500PrivateCredential

```java
public X500PrivateCredential​(
X509Certificate
cert,

PrivateKey
key,

String
alias)
```

Creates an X500PrivateCredential that associates an X.509 certificate,
a private key and the KeyStore alias.

**Parameters:** cert

- X509Certificate
**Parameters:** key

- PrivateKey for the certificate
**Parameters:** alias

- KeyStore alias
**Throws:** IllegalArgumentException

- if either

cert

,

key

or

alias

is null

---

#### X500PrivateCredential

public X500PrivateCredential​(

X509Certificate

cert,

PrivateKey

key,

String

alias)

Creates an X500PrivateCredential that associates an X.509 certificate,
a private key and the KeyStore alias.

Method Detail

- getCertificate

```java
public
X509Certificate
getCertificate()
```

Returns the X.509 certificate.

**Returns:** the X509Certificate

- getPrivateKey

```java
public
PrivateKey
getPrivateKey()
```

Returns the PrivateKey.

**Returns:** the PrivateKey

- getAlias

```java
public
String
getAlias()
```

Returns the KeyStore alias.

**Returns:** the KeyStore alias

- destroy

```java
public void destroy()
```

Clears the references to the X.509 certificate, private key and the
KeyStore alias in this object.

**Specified by:** destroy

in interface

Destroyable

- isDestroyed

```java
public boolean isDestroyed()
```

Determines if the references to the X.509 certificate and private key
in this object have been cleared.

**Specified by:** isDestroyed

in interface

Destroyable
**Returns:** true if X509Certificate and the PrivateKey are null

---

#### Method Detail

getCertificate

```java
public
X509Certificate
getCertificate()
```

Returns the X.509 certificate.

**Returns:** the X509Certificate

---

#### getCertificate

public

X509Certificate

getCertificate()

Returns the X.509 certificate.

getPrivateKey

```java
public
PrivateKey
getPrivateKey()
```

Returns the PrivateKey.

**Returns:** the PrivateKey

---

#### getPrivateKey

public

PrivateKey

getPrivateKey()

Returns the PrivateKey.

getAlias

```java
public
String
getAlias()
```

Returns the KeyStore alias.

**Returns:** the KeyStore alias

---

#### getAlias

public

String

getAlias()

Returns the KeyStore alias.

destroy

```java
public void destroy()
```

Clears the references to the X.509 certificate, private key and the
KeyStore alias in this object.

**Specified by:** destroy

in interface

Destroyable

---

#### destroy

public void destroy()

Clears the references to the X.509 certificate, private key and the
KeyStore alias in this object.

isDestroyed

```java
public boolean isDestroyed()
```

Determines if the references to the X.509 certificate and private key
in this object have been cleared.

**Specified by:** isDestroyed

in interface

Destroyable
**Returns:** true if X509Certificate and the PrivateKey are null

---

#### isDestroyed

public boolean isDestroyed()

Determines if the references to the X.509 certificate and private key
in this object have been cleared.

---

