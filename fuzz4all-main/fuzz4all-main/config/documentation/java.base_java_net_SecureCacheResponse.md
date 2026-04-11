# Class SecureCacheResponse

**Source:** `java.base\java\net\SecureCacheResponse.html`

### Class Description

```java
public abstract class
SecureCacheResponse

extends
CacheResponse
```

Represents a cache response originally retrieved through secure
means, such as TLS.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

#### public SecureCacheResponse()

*No description found.*

---

### Method Details

#### public abstract
String
getCipherSuite()

Returns the cipher suite in use on the original connection that
retrieved the network resource.

**Returns:**
- a string representing the cipher suite

---

#### public abstract
List
<
Certificate
> getLocalCertificateChain()

Returns the certificate chain that were sent to the server during
handshaking of the original connection that retrieved the
network resource. Note: This method is useful only
when using certificate-based cipher suites.

**Returns:**
- an immutable List of Certificate representing the
certificate chain that was sent to the server. If no
certificate chain was sent, null will be returned.

**See Also:**
- getLocalPrincipal()

---

#### public abstract
List
<
Certificate
> getServerCertificateChain()
throws
SSLPeerUnverifiedException

Returns the server's certificate chain, which was established as
part of defining the session in the original connection that
retrieved the network resource, from cache. Note: This method
can be used only when using certificate-based cipher suites;
using it with non-certificate-based cipher suites, such as
Kerberos, will throw an SSLPeerUnverifiedException.

**Returns:**
- an immutable List of Certificate representing the server's
certificate chain.

**Throws:**
- SSLPeerUnverifiedException

- if the peer is not verified.

**See Also:**
- getPeerPrincipal()

---

#### public abstract
Principal
getPeerPrincipal()
throws
SSLPeerUnverifiedException

Returns the server's principal which was established as part of
defining the session during the original connection that
retrieved the network resource.

**Returns:**
- the server's principal. Returns an X500Principal of the
end-entity certiticate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites.

**Throws:**
- SSLPeerUnverifiedException

- if the peer was not verified.

**See Also:**
- getServerCertificateChain()

,

getLocalPrincipal()

---

#### public abstract
Principal
getLocalPrincipal()

Returns the principal that was sent to the server during
handshaking in the original connection that retrieved the
network resource.

**Returns:**
- the principal sent to the server. Returns an X500Principal
of the end-entity certificate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites. If no principal was
sent, then null is returned.

**See Also:**
- getLocalCertificateChain()

,

getPeerPrincipal()

---

### Additional Sections

#### Class SecureCacheResponse

java.lang.Object

- java.net.CacheResponse
- - java.net.SecureCacheResponse

java.net.CacheResponse

- java.net.SecureCacheResponse

java.net.SecureCacheResponse

```java
public abstract class
SecureCacheResponse

extends
CacheResponse
```

Represents a cache response originally retrieved through secure
means, such as TLS.

**Since:** 1.5

public abstract class

SecureCacheResponse

extends

CacheResponse

Represents a cache response originally retrieved through secure
means, such as TLS.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SecureCacheResponse

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

String

getCipherSuite

()

Returns the cipher suite in use on the original connection that
retrieved the network resource.

abstract

List

<

Certificate

>

getLocalCertificateChain

()

Returns the certificate chain that were sent to the server during
handshaking of the original connection that retrieved the
network resource.

abstract

Principal

getLocalPrincipal

()

Returns the principal that was sent to the server during
handshaking in the original connection that retrieved the
network resource.

abstract

Principal

getPeerPrincipal

()

Returns the server's principal which was established as part of
defining the session during the original connection that
retrieved the network resource.

abstract

List

<

Certificate

>

getServerCertificateChain

()

Returns the server's certificate chain, which was established as
part of defining the session in the original connection that
retrieved the network resource, from cache.

- Methods declared in class java.net.

CacheResponse

getBody

,

getHeaders

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

SecureCacheResponse

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

String

getCipherSuite

()

Returns the cipher suite in use on the original connection that
retrieved the network resource.

abstract

List

<

Certificate

>

getLocalCertificateChain

()

Returns the certificate chain that were sent to the server during
handshaking of the original connection that retrieved the
network resource.

abstract

Principal

getLocalPrincipal

()

Returns the principal that was sent to the server during
handshaking in the original connection that retrieved the
network resource.

abstract

Principal

getPeerPrincipal

()

Returns the server's principal which was established as part of
defining the session during the original connection that
retrieved the network resource.

abstract

List

<

Certificate

>

getServerCertificateChain

()

Returns the server's certificate chain, which was established as
part of defining the session in the original connection that
retrieved the network resource, from cache.

- Methods declared in class java.net.

CacheResponse

getBody

,

getHeaders

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

Returns the cipher suite in use on the original connection that
retrieved the network resource.

Returns the certificate chain that were sent to the server during
handshaking of the original connection that retrieved the
network resource.

Returns the principal that was sent to the server during
handshaking in the original connection that retrieved the
network resource.

Returns the server's principal which was established as part of
defining the session during the original connection that
retrieved the network resource.

Returns the server's certificate chain, which was established as
part of defining the session in the original connection that
retrieved the network resource, from cache.

Methods declared in class java.net.

CacheResponse

getBody

,

getHeaders

---

#### Methods declared in class java.net. CacheResponse

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

- SecureCacheResponse

```java
public SecureCacheResponse()
```

============ METHOD DETAIL ==========

- Method Detail

- getCipherSuite

```java
public abstract
String
getCipherSuite()
```

Returns the cipher suite in use on the original connection that
retrieved the network resource.

**Returns:** a string representing the cipher suite

- getLocalCertificateChain

```java
public abstract
List
<
Certificate
> getLocalCertificateChain()
```

Returns the certificate chain that were sent to the server during
handshaking of the original connection that retrieved the
network resource. Note: This method is useful only
when using certificate-based cipher suites.

**Returns:** an immutable List of Certificate representing the
certificate chain that was sent to the server. If no
certificate chain was sent, null will be returned.
**See Also:** getLocalPrincipal()

- getServerCertificateChain

```java
public abstract
List
<
Certificate
> getServerCertificateChain()
throws
SSLPeerUnverifiedException
```

Returns the server's certificate chain, which was established as
part of defining the session in the original connection that
retrieved the network resource, from cache. Note: This method
can be used only when using certificate-based cipher suites;
using it with non-certificate-based cipher suites, such as
Kerberos, will throw an SSLPeerUnverifiedException.

**Returns:** an immutable List of Certificate representing the server's
certificate chain.
**Throws:** SSLPeerUnverifiedException

- if the peer is not verified.
**See Also:** getPeerPrincipal()

- getPeerPrincipal

```java
public abstract
Principal
getPeerPrincipal()
throws
SSLPeerUnverifiedException
```

Returns the server's principal which was established as part of
defining the session during the original connection that
retrieved the network resource.

**Returns:** the server's principal. Returns an X500Principal of the
end-entity certiticate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites.
**Throws:** SSLPeerUnverifiedException

- if the peer was not verified.
**See Also:** getServerCertificateChain()

,

getLocalPrincipal()

- getLocalPrincipal

```java
public abstract
Principal
getLocalPrincipal()
```

Returns the principal that was sent to the server during
handshaking in the original connection that retrieved the
network resource.

**Returns:** the principal sent to the server. Returns an X500Principal
of the end-entity certificate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites. If no principal was
sent, then null is returned.
**See Also:** getLocalCertificateChain()

,

getPeerPrincipal()

Constructor Detail

- SecureCacheResponse

```java
public SecureCacheResponse()
```

---

#### Constructor Detail

SecureCacheResponse

```java
public SecureCacheResponse()
```

---

#### SecureCacheResponse

public SecureCacheResponse()

Method Detail

- getCipherSuite

```java
public abstract
String
getCipherSuite()
```

Returns the cipher suite in use on the original connection that
retrieved the network resource.

**Returns:** a string representing the cipher suite

- getLocalCertificateChain

```java
public abstract
List
<
Certificate
> getLocalCertificateChain()
```

Returns the certificate chain that were sent to the server during
handshaking of the original connection that retrieved the
network resource. Note: This method is useful only
when using certificate-based cipher suites.

**Returns:** an immutable List of Certificate representing the
certificate chain that was sent to the server. If no
certificate chain was sent, null will be returned.
**See Also:** getLocalPrincipal()

- getServerCertificateChain

```java
public abstract
List
<
Certificate
> getServerCertificateChain()
throws
SSLPeerUnverifiedException
```

Returns the server's certificate chain, which was established as
part of defining the session in the original connection that
retrieved the network resource, from cache. Note: This method
can be used only when using certificate-based cipher suites;
using it with non-certificate-based cipher suites, such as
Kerberos, will throw an SSLPeerUnverifiedException.

**Returns:** an immutable List of Certificate representing the server's
certificate chain.
**Throws:** SSLPeerUnverifiedException

- if the peer is not verified.
**See Also:** getPeerPrincipal()

- getPeerPrincipal

```java
public abstract
Principal
getPeerPrincipal()
throws
SSLPeerUnverifiedException
```

Returns the server's principal which was established as part of
defining the session during the original connection that
retrieved the network resource.

**Returns:** the server's principal. Returns an X500Principal of the
end-entity certiticate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites.
**Throws:** SSLPeerUnverifiedException

- if the peer was not verified.
**See Also:** getServerCertificateChain()

,

getLocalPrincipal()

- getLocalPrincipal

```java
public abstract
Principal
getLocalPrincipal()
```

Returns the principal that was sent to the server during
handshaking in the original connection that retrieved the
network resource.

**Returns:** the principal sent to the server. Returns an X500Principal
of the end-entity certificate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites. If no principal was
sent, then null is returned.
**See Also:** getLocalCertificateChain()

,

getPeerPrincipal()

---

#### Method Detail

getCipherSuite

```java
public abstract
String
getCipherSuite()
```

Returns the cipher suite in use on the original connection that
retrieved the network resource.

**Returns:** a string representing the cipher suite

---

#### getCipherSuite

public abstract

String

getCipherSuite()

Returns the cipher suite in use on the original connection that
retrieved the network resource.

getLocalCertificateChain

```java
public abstract
List
<
Certificate
> getLocalCertificateChain()
```

Returns the certificate chain that were sent to the server during
handshaking of the original connection that retrieved the
network resource. Note: This method is useful only
when using certificate-based cipher suites.

**Returns:** an immutable List of Certificate representing the
certificate chain that was sent to the server. If no
certificate chain was sent, null will be returned.
**See Also:** getLocalPrincipal()

---

#### getLocalCertificateChain

public abstract

List

<

Certificate

> getLocalCertificateChain()

Returns the certificate chain that were sent to the server during
handshaking of the original connection that retrieved the
network resource. Note: This method is useful only
when using certificate-based cipher suites.

getServerCertificateChain

```java
public abstract
List
<
Certificate
> getServerCertificateChain()
throws
SSLPeerUnverifiedException
```

Returns the server's certificate chain, which was established as
part of defining the session in the original connection that
retrieved the network resource, from cache. Note: This method
can be used only when using certificate-based cipher suites;
using it with non-certificate-based cipher suites, such as
Kerberos, will throw an SSLPeerUnverifiedException.

**Returns:** an immutable List of Certificate representing the server's
certificate chain.
**Throws:** SSLPeerUnverifiedException

- if the peer is not verified.
**See Also:** getPeerPrincipal()

---

#### getServerCertificateChain

public abstract

List

<

Certificate

> getServerCertificateChain()
throws

SSLPeerUnverifiedException

Returns the server's certificate chain, which was established as
part of defining the session in the original connection that
retrieved the network resource, from cache. Note: This method
can be used only when using certificate-based cipher suites;
using it with non-certificate-based cipher suites, such as
Kerberos, will throw an SSLPeerUnverifiedException.

getPeerPrincipal

```java
public abstract
Principal
getPeerPrincipal()
throws
SSLPeerUnverifiedException
```

Returns the server's principal which was established as part of
defining the session during the original connection that
retrieved the network resource.

**Returns:** the server's principal. Returns an X500Principal of the
end-entity certiticate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites.
**Throws:** SSLPeerUnverifiedException

- if the peer was not verified.
**See Also:** getServerCertificateChain()

,

getLocalPrincipal()

---

#### getPeerPrincipal

public abstract

Principal

getPeerPrincipal()
throws

SSLPeerUnverifiedException

Returns the server's principal which was established as part of
defining the session during the original connection that
retrieved the network resource.

getLocalPrincipal

```java
public abstract
Principal
getLocalPrincipal()
```

Returns the principal that was sent to the server during
handshaking in the original connection that retrieved the
network resource.

**Returns:** the principal sent to the server. Returns an X500Principal
of the end-entity certificate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites. If no principal was
sent, then null is returned.
**See Also:** getLocalCertificateChain()

,

getPeerPrincipal()

---

#### getLocalPrincipal

public abstract

Principal

getLocalPrincipal()

Returns the principal that was sent to the server during
handshaking in the original connection that retrieved the
network resource.

---

