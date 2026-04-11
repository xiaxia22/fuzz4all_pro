# Interface X509KeyManager

**Source:** `java.base\javax\net\ssl\X509KeyManager.html`

### Class Description

```java
public interface
X509KeyManager

extends
KeyManager
```

Instances of this interface manage which X509 certificate-based
key pairs are used to authenticate the local side of a secure
socket.

During secure socket negotiations, implementations
call methods in this interface to:

- determine the set of aliases that are available for negotiations
based on the criteria presented,

select the

best alias

based on
the criteria presented, and

obtain the corresponding key material for given aliases.

Note: the X509ExtendedKeyManager should be used in favor of this
class.

**All Superinterfaces:** KeyManager

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
[] getClientAliases​(
String
keyType,

Principal
[] issuers)

Get the matching aliases for authenticating the client side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

**Parameters:**
- keyType

- the key algorithm type name
- issuers

- the list of acceptable CA issuer subject names,
or null if it does not matter which issuers are used.

**Returns:**
- an array of the matching alias names, or null if there
were no matches.

---

#### String
chooseClientAlias​(
String
[] keyType,

Principal
[] issuers,

Socket
socket)

Choose an alias to authenticate the client side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

**Parameters:**
- keyType

- the key algorithm type name(s), ordered
with the most-preferred key type first.
- issuers

- the list of acceptable CA issuer subject names
or null if it does not matter which issuers are used.
- socket

- the socket to be used for this connection. This
parameter can be null, which indicates that
implementations are free to select an alias applicable
to any socket.

**Returns:**
- the alias name for the desired key, or null if there
are no matches.

---

#### String
[] getServerAliases​(
String
keyType,

Principal
[] issuers)

Get the matching aliases for authenticating the server side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

**Parameters:**
- keyType

- the key algorithm type name
- issuers

- the list of acceptable CA issuer subject names
or null if it does not matter which issuers are used.

**Returns:**
- an array of the matching alias names, or null
if there were no matches.

---

#### String
chooseServerAlias​(
String
keyType,

Principal
[] issuers,

Socket
socket)

Choose an alias to authenticate the server side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

**Parameters:**
- keyType

- the key algorithm type name.
- issuers

- the list of acceptable CA issuer subject names
or null if it does not matter which issuers are used.
- socket

- the socket to be used for this connection. This
parameter can be null, which indicates that
implementations are free to select an alias applicable
to any socket.

**Returns:**
- the alias name for the desired key, or null if there
are no matches.

---

#### X509Certificate
[] getCertificateChain​(
String
alias)

Returns the certificate chain associated with the given alias.

**Parameters:**
- alias

- the alias name

**Returns:**
- the certificate chain (ordered with the user's certificate first
and the root certificate authority last), or null
if the alias can't be found.

---

#### PrivateKey
getPrivateKey​(
String
alias)

Returns the key associated with the given alias.

**Parameters:**
- alias

- the alias name

**Returns:**
- the requested key, or null if the alias can't be found.

---

### Additional Sections

#### Interface X509KeyManager

**All Superinterfaces:** KeyManager

**All Known Implementing Classes:** X509ExtendedKeyManager

```java
public interface
X509KeyManager

extends
KeyManager
```

Instances of this interface manage which X509 certificate-based
key pairs are used to authenticate the local side of a secure
socket.

During secure socket negotiations, implementations
call methods in this interface to:

- determine the set of aliases that are available for negotiations
based on the criteria presented,

select the

best alias

based on
the criteria presented, and

obtain the corresponding key material for given aliases.

Note: the X509ExtendedKeyManager should be used in favor of this
class.

**Since:** 1.4

public interface

X509KeyManager

extends

KeyManager

Instances of this interface manage which X509 certificate-based
key pairs are used to authenticate the local side of a secure
socket.

During secure socket negotiations, implementations
call methods in this interface to:

- determine the set of aliases that are available for negotiations
based on the criteria presented,

select the

best alias

based on
the criteria presented, and

obtain the corresponding key material for given aliases.

Note: the X509ExtendedKeyManager should be used in favor of this
class.

During secure socket negotiations, implementations
call methods in this interface to:

- determine the set of aliases that are available for negotiations
based on the criteria presented,

select the

best alias

based on
the criteria presented, and

obtain the corresponding key material for given aliases.

Note: the X509ExtendedKeyManager should be used in favor of this
class.

determine the set of aliases that are available for negotiations
based on the criteria presented,

select the

best alias

based on
the criteria presented, and

obtain the corresponding key material for given aliases.

Note: the X509ExtendedKeyManager should be used in favor of this
class.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

chooseClientAlias

​(

String

[] keyType,

Principal

[] issuers,

Socket

socket)

Choose an alias to authenticate the client side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

String

chooseServerAlias

​(

String

keyType,

Principal

[] issuers,

Socket

socket)

Choose an alias to authenticate the server side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

X509Certificate

[]

getCertificateChain

​(

String

alias)

Returns the certificate chain associated with the given alias.

String

[]

getClientAliases

​(

String

keyType,

Principal

[] issuers)

Get the matching aliases for authenticating the client side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

PrivateKey

getPrivateKey

​(

String

alias)

Returns the key associated with the given alias.

String

[]

getServerAliases

​(

String

keyType,

Principal

[] issuers)

Get the matching aliases for authenticating the server side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

String

chooseClientAlias

​(

String

[] keyType,

Principal

[] issuers,

Socket

socket)

Choose an alias to authenticate the client side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

String

chooseServerAlias

​(

String

keyType,

Principal

[] issuers,

Socket

socket)

Choose an alias to authenticate the server side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

X509Certificate

[]

getCertificateChain

​(

String

alias)

Returns the certificate chain associated with the given alias.

String

[]

getClientAliases

​(

String

keyType,

Principal

[] issuers)

Get the matching aliases for authenticating the client side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

PrivateKey

getPrivateKey

​(

String

alias)

Returns the key associated with the given alias.

String

[]

getServerAliases

​(

String

keyType,

Principal

[] issuers)

Get the matching aliases for authenticating the server side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

---

#### Method Summary

Choose an alias to authenticate the client side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

Choose an alias to authenticate the server side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

Returns the certificate chain associated with the given alias.

Get the matching aliases for authenticating the client side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

Returns the key associated with the given alias.

Get the matching aliases for authenticating the server side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

============ METHOD DETAIL ==========

- Method Detail

- getClientAliases

```java
String
[] getClientAliases​(
String
keyType,

Principal
[] issuers)
```

Get the matching aliases for authenticating the client side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

**Parameters:** keyType

- the key algorithm type name
**Parameters:** issuers

- the list of acceptable CA issuer subject names,
or null if it does not matter which issuers are used.
**Returns:** an array of the matching alias names, or null if there
were no matches.

- chooseClientAlias

```java
String
chooseClientAlias​(
String
[] keyType,

Principal
[] issuers,

Socket
socket)
```

Choose an alias to authenticate the client side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

**Parameters:** keyType

- the key algorithm type name(s), ordered
with the most-preferred key type first.
**Parameters:** issuers

- the list of acceptable CA issuer subject names
or null if it does not matter which issuers are used.
**Parameters:** socket

- the socket to be used for this connection. This
parameter can be null, which indicates that
implementations are free to select an alias applicable
to any socket.
**Returns:** the alias name for the desired key, or null if there
are no matches.

- getServerAliases

```java
String
[] getServerAliases​(
String
keyType,

Principal
[] issuers)
```

Get the matching aliases for authenticating the server side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

**Parameters:** keyType

- the key algorithm type name
**Parameters:** issuers

- the list of acceptable CA issuer subject names
or null if it does not matter which issuers are used.
**Returns:** an array of the matching alias names, or null
if there were no matches.

- chooseServerAlias

```java
String
chooseServerAlias​(
String
keyType,

Principal
[] issuers,

Socket
socket)
```

Choose an alias to authenticate the server side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

**Parameters:** keyType

- the key algorithm type name.
**Parameters:** issuers

- the list of acceptable CA issuer subject names
or null if it does not matter which issuers are used.
**Parameters:** socket

- the socket to be used for this connection. This
parameter can be null, which indicates that
implementations are free to select an alias applicable
to any socket.
**Returns:** the alias name for the desired key, or null if there
are no matches.

- getCertificateChain

```java
X509Certificate
[] getCertificateChain​(
String
alias)
```

Returns the certificate chain associated with the given alias.

**Parameters:** alias

- the alias name
**Returns:** the certificate chain (ordered with the user's certificate first
and the root certificate authority last), or null
if the alias can't be found.

- getPrivateKey

```java
PrivateKey
getPrivateKey​(
String
alias)
```

Returns the key associated with the given alias.

**Parameters:** alias

- the alias name
**Returns:** the requested key, or null if the alias can't be found.

Method Detail

- getClientAliases

```java
String
[] getClientAliases​(
String
keyType,

Principal
[] issuers)
```

Get the matching aliases for authenticating the client side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

**Parameters:** keyType

- the key algorithm type name
**Parameters:** issuers

- the list of acceptable CA issuer subject names,
or null if it does not matter which issuers are used.
**Returns:** an array of the matching alias names, or null if there
were no matches.

- chooseClientAlias

```java
String
chooseClientAlias​(
String
[] keyType,

Principal
[] issuers,

Socket
socket)
```

Choose an alias to authenticate the client side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

**Parameters:** keyType

- the key algorithm type name(s), ordered
with the most-preferred key type first.
**Parameters:** issuers

- the list of acceptable CA issuer subject names
or null if it does not matter which issuers are used.
**Parameters:** socket

- the socket to be used for this connection. This
parameter can be null, which indicates that
implementations are free to select an alias applicable
to any socket.
**Returns:** the alias name for the desired key, or null if there
are no matches.

- getServerAliases

```java
String
[] getServerAliases​(
String
keyType,

Principal
[] issuers)
```

Get the matching aliases for authenticating the server side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

**Parameters:** keyType

- the key algorithm type name
**Parameters:** issuers

- the list of acceptable CA issuer subject names
or null if it does not matter which issuers are used.
**Returns:** an array of the matching alias names, or null
if there were no matches.

- chooseServerAlias

```java
String
chooseServerAlias​(
String
keyType,

Principal
[] issuers,

Socket
socket)
```

Choose an alias to authenticate the server side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

**Parameters:** keyType

- the key algorithm type name.
**Parameters:** issuers

- the list of acceptable CA issuer subject names
or null if it does not matter which issuers are used.
**Parameters:** socket

- the socket to be used for this connection. This
parameter can be null, which indicates that
implementations are free to select an alias applicable
to any socket.
**Returns:** the alias name for the desired key, or null if there
are no matches.

- getCertificateChain

```java
X509Certificate
[] getCertificateChain​(
String
alias)
```

Returns the certificate chain associated with the given alias.

**Parameters:** alias

- the alias name
**Returns:** the certificate chain (ordered with the user's certificate first
and the root certificate authority last), or null
if the alias can't be found.

- getPrivateKey

```java
PrivateKey
getPrivateKey​(
String
alias)
```

Returns the key associated with the given alias.

**Parameters:** alias

- the alias name
**Returns:** the requested key, or null if the alias can't be found.

---

#### Method Detail

getClientAliases

```java
String
[] getClientAliases​(
String
keyType,

Principal
[] issuers)
```

Get the matching aliases for authenticating the client side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

**Parameters:** keyType

- the key algorithm type name
**Parameters:** issuers

- the list of acceptable CA issuer subject names,
or null if it does not matter which issuers are used.
**Returns:** an array of the matching alias names, or null if there
were no matches.

---

#### getClientAliases

String

[] getClientAliases​(

String

keyType,

Principal

[] issuers)

Get the matching aliases for authenticating the client side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

chooseClientAlias

```java
String
chooseClientAlias​(
String
[] keyType,

Principal
[] issuers,

Socket
socket)
```

Choose an alias to authenticate the client side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

**Parameters:** keyType

- the key algorithm type name(s), ordered
with the most-preferred key type first.
**Parameters:** issuers

- the list of acceptable CA issuer subject names
or null if it does not matter which issuers are used.
**Parameters:** socket

- the socket to be used for this connection. This
parameter can be null, which indicates that
implementations are free to select an alias applicable
to any socket.
**Returns:** the alias name for the desired key, or null if there
are no matches.

---

#### chooseClientAlias

String

chooseClientAlias​(

String

[] keyType,

Principal

[] issuers,

Socket

socket)

Choose an alias to authenticate the client side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

getServerAliases

```java
String
[] getServerAliases​(
String
keyType,

Principal
[] issuers)
```

Get the matching aliases for authenticating the server side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

**Parameters:** keyType

- the key algorithm type name
**Parameters:** issuers

- the list of acceptable CA issuer subject names
or null if it does not matter which issuers are used.
**Returns:** an array of the matching alias names, or null
if there were no matches.

---

#### getServerAliases

String

[] getServerAliases​(

String

keyType,

Principal

[] issuers)

Get the matching aliases for authenticating the server side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

chooseServerAlias

```java
String
chooseServerAlias​(
String
keyType,

Principal
[] issuers,

Socket
socket)
```

Choose an alias to authenticate the server side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

**Parameters:** keyType

- the key algorithm type name.
**Parameters:** issuers

- the list of acceptable CA issuer subject names
or null if it does not matter which issuers are used.
**Parameters:** socket

- the socket to be used for this connection. This
parameter can be null, which indicates that
implementations are free to select an alias applicable
to any socket.
**Returns:** the alias name for the desired key, or null if there
are no matches.

---

#### chooseServerAlias

String

chooseServerAlias​(

String

keyType,

Principal

[] issuers,

Socket

socket)

Choose an alias to authenticate the server side of a secure
socket given the public key type and the list of
certificate issuer authorities recognized by the peer (if any).

getCertificateChain

```java
X509Certificate
[] getCertificateChain​(
String
alias)
```

Returns the certificate chain associated with the given alias.

**Parameters:** alias

- the alias name
**Returns:** the certificate chain (ordered with the user's certificate first
and the root certificate authority last), or null
if the alias can't be found.

---

#### getCertificateChain

X509Certificate

[] getCertificateChain​(

String

alias)

Returns the certificate chain associated with the given alias.

getPrivateKey

```java
PrivateKey
getPrivateKey​(
String
alias)
```

Returns the key associated with the given alias.

**Parameters:** alias

- the alias name
**Returns:** the requested key, or null if the alias can't be found.

---

#### getPrivateKey

PrivateKey

getPrivateKey​(

String

alias)

Returns the key associated with the given alias.

---

