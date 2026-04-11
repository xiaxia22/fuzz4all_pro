# Class HandshakeCompletedEvent

**Source:** `java.base\javax\net\ssl\HandshakeCompletedEvent.html`

### Class Description

```java
public class
HandshakeCompletedEvent

extends
EventObject
```

This event indicates that an SSL handshake completed on a given
SSL connection. All of the core information about that handshake's
result is captured through an "SSLSession" object. As a convenience,
this event class provides direct access to some important session
attributes.

The source of this event is the SSLSocket on which handshaking
just completed.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public HandshakeCompletedEvent​(
SSLSocket
sock,

SSLSession
s)

Constructs a new HandshakeCompletedEvent.

**Parameters:**
- sock

- the SSLSocket acting as the source of the event
- s

- the SSLSession this event is associated with

---

### Method Details

#### public
SSLSession
getSession()

Returns the session that triggered this event.

**Returns:**
- the

SSLSession

for this handshake

---

#### public
String
getCipherSuite()

Returns the cipher suite in use by the session which was produced
by the handshake. (This is a convenience method for
getting the ciphersuite from the SSLsession.)

**Returns:**
- the name of the cipher suite negotiated during this session.

---

#### public
Certificate
[] getLocalCertificates()

Returns the certificate(s) that were sent to the peer during
handshaking.
Note: This method is useful only when using certificate-based
cipher suites.

When multiple certificates are available for use in a
handshake, the implementation chooses what it considers the
"best" certificate chain available, and transmits that to
the other side. This method allows the caller to know
which certificate chain was actually used.

**Returns:**
- an ordered array of certificates, with the local
certificate first followed by any
certificate authorities. If no certificates were sent,
then null is returned.

**See Also:**
- getLocalPrincipal()

---

#### public
Certificate
[] getPeerCertificates()
throws
SSLPeerUnverifiedException

Returns the identity of the peer which was established as part
of defining the session.
Note: This method can be used only when using certificate-based
cipher suites; using it with non-certificate-based cipher suites,
such as Kerberos, will throw an SSLPeerUnverifiedException.

Note: The returned value may not be a valid certificate chain
and should not be relied on for trust decisions.

**Returns:**
- an ordered array of the peer certificates,
with the peer's own certificate first followed by
any certificate authorities.

**Throws:**
- SSLPeerUnverifiedException

- if the peer is not verified.

**See Also:**
- getPeerPrincipal()

---

#### @Deprecated
(
since
="9")
public
X509Certificate
[] getPeerCertificateChain()
throws
SSLPeerUnverifiedException

Returns the identity of the peer which was identified as part
of defining the session.
Note: This method can be used only when using certificate-based
cipher suites; using it with non-certificate-based cipher suites,
such as Kerberos, will throw an SSLPeerUnverifiedException.

Note: The returned value may not be a valid certificate chain
and should not be relied on for trust decisions.

Note: this method exists for compatibility with previous
releases. New applications should use

getPeerCertificates()

instead.

**Returns:**
- an ordered array of peer X.509 certificates,
with the peer's own certificate first followed by any
certificate authorities. (The certificates are in
the original JSSE

X509Certificate

format).

**Throws:**
- SSLPeerUnverifiedException

- if the peer is not verified.

**See Also:**
- getPeerPrincipal()

---

#### public
Principal
getPeerPrincipal()
throws
SSLPeerUnverifiedException

Returns the identity of the peer which was established as part of
defining the session.

**Returns:**
- the peer's principal. Returns an X500Principal of the
end-entity certiticate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites.

**Throws:**
- SSLPeerUnverifiedException

- if the peer's identity has not
been verified

**See Also:**
- getPeerCertificates()

,

getLocalPrincipal()

**Since:**
- 1.5

---

#### public
Principal
getLocalPrincipal()

Returns the principal that was sent to the peer during handshaking.

**Returns:**
- the principal sent to the peer. Returns an X500Principal
of the end-entity certificate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites. If no principal was
sent, then null is returned.

**See Also:**
- getLocalCertificates()

,

getPeerPrincipal()

**Since:**
- 1.5

---

#### public
SSLSocket
getSocket()

Returns the socket which is the source of this event.
(This is a convenience function, to let applications
write code without type casts.)

**Returns:**
- the socket on which the connection was made.

---

### Additional Sections

#### Class HandshakeCompletedEvent

java.lang.Object

- java.util.EventObject
- - javax.net.ssl.HandshakeCompletedEvent

java.util.EventObject

- javax.net.ssl.HandshakeCompletedEvent

javax.net.ssl.HandshakeCompletedEvent

**All Implemented Interfaces:** Serializable

```java
public class
HandshakeCompletedEvent

extends
EventObject
```

This event indicates that an SSL handshake completed on a given
SSL connection. All of the core information about that handshake's
result is captured through an "SSLSession" object. As a convenience,
this event class provides direct access to some important session
attributes.

The source of this event is the SSLSocket on which handshaking
just completed.

**Since:** 1.4
**See Also:** SSLSocket

,

HandshakeCompletedListener

,

SSLSession

,

Serialized Form

public class

HandshakeCompletedEvent

extends

EventObject

This event indicates that an SSL handshake completed on a given
SSL connection. All of the core information about that handshake's
result is captured through an "SSLSession" object. As a convenience,
this event class provides direct access to some important session
attributes.

The source of this event is the SSLSocket on which handshaking
just completed.

The source of this event is the SSLSocket on which handshaking
just completed.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

HandshakeCompletedEvent

​(

SSLSocket

sock,

SSLSession

s)

Constructs a new HandshakeCompletedEvent.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

String

getCipherSuite

()

Returns the cipher suite in use by the session which was produced
by the handshake.

Certificate

[]

getLocalCertificates

()

Returns the certificate(s) that were sent to the peer during
handshaking.

Principal

getLocalPrincipal

()

Returns the principal that was sent to the peer during handshaking.

X509Certificate

[]

getPeerCertificateChain

()

Deprecated.

The

getPeerCertificates()

method that returns an
array of

java.security.cert.Certificate

should
be used instead.

Certificate

[]

getPeerCertificates

()

Returns the identity of the peer which was established as part
of defining the session.

Principal

getPeerPrincipal

()

Returns the identity of the peer which was established as part of
defining the session.

SSLSession

getSession

()

Returns the session that triggered this event.

SSLSocket

getSocket

()

Returns the socket which is the source of this event.

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

wait

,

wait

,

wait

Field Summary

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

HandshakeCompletedEvent

​(

SSLSocket

sock,

SSLSession

s)

Constructs a new HandshakeCompletedEvent.

---

#### Constructor Summary

Constructs a new HandshakeCompletedEvent.

Method Summary

All Methods

Instance Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

String

getCipherSuite

()

Returns the cipher suite in use by the session which was produced
by the handshake.

Certificate

[]

getLocalCertificates

()

Returns the certificate(s) that were sent to the peer during
handshaking.

Principal

getLocalPrincipal

()

Returns the principal that was sent to the peer during handshaking.

X509Certificate

[]

getPeerCertificateChain

()

Deprecated.

The

getPeerCertificates()

method that returns an
array of

java.security.cert.Certificate

should
be used instead.

Certificate

[]

getPeerCertificates

()

Returns the identity of the peer which was established as part
of defining the session.

Principal

getPeerPrincipal

()

Returns the identity of the peer which was established as part of
defining the session.

SSLSession

getSession

()

Returns the session that triggered this event.

SSLSocket

getSocket

()

Returns the socket which is the source of this event.

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

wait

,

wait

,

wait

---

#### Method Summary

Returns the cipher suite in use by the session which was produced
by the handshake.

Returns the certificate(s) that were sent to the peer during
handshaking.

Returns the principal that was sent to the peer during handshaking.

Deprecated.

The

getPeerCertificates()

method that returns an
array of

java.security.cert.Certificate

should
be used instead.

Returns the identity of the peer which was established as part
of defining the session.

Returns the identity of the peer which was established as part of
defining the session.

Returns the session that triggered this event.

Returns the socket which is the source of this event.

Methods declared in class java.util.

EventObject

getSource

,

toString

---

#### Methods declared in class java.util. EventObject

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- HandshakeCompletedEvent

```java
public HandshakeCompletedEvent​(
SSLSocket
sock,

SSLSession
s)
```

Constructs a new HandshakeCompletedEvent.

**Parameters:** sock

- the SSLSocket acting as the source of the event
**Parameters:** s

- the SSLSession this event is associated with

============ METHOD DETAIL ==========

- Method Detail

- getSession

```java
public
SSLSession
getSession()
```

Returns the session that triggered this event.

**Returns:** the

SSLSession

for this handshake

- getCipherSuite

```java
public
String
getCipherSuite()
```

Returns the cipher suite in use by the session which was produced
by the handshake. (This is a convenience method for
getting the ciphersuite from the SSLsession.)

**Returns:** the name of the cipher suite negotiated during this session.

- getLocalCertificates

```java
public
Certificate
[] getLocalCertificates()
```

Returns the certificate(s) that were sent to the peer during
handshaking.
Note: This method is useful only when using certificate-based
cipher suites.

When multiple certificates are available for use in a
handshake, the implementation chooses what it considers the
"best" certificate chain available, and transmits that to
the other side. This method allows the caller to know
which certificate chain was actually used.

**Returns:** an ordered array of certificates, with the local
certificate first followed by any
certificate authorities. If no certificates were sent,
then null is returned.
**See Also:** getLocalPrincipal()

- getPeerCertificates

```java
public
Certificate
[] getPeerCertificates()
throws
SSLPeerUnverifiedException
```

Returns the identity of the peer which was established as part
of defining the session.
Note: This method can be used only when using certificate-based
cipher suites; using it with non-certificate-based cipher suites,
such as Kerberos, will throw an SSLPeerUnverifiedException.

Note: The returned value may not be a valid certificate chain
and should not be relied on for trust decisions.

**Returns:** an ordered array of the peer certificates,
with the peer's own certificate first followed by
any certificate authorities.
**Throws:** SSLPeerUnverifiedException

- if the peer is not verified.
**See Also:** getPeerPrincipal()

- getPeerCertificateChain

```java
@Deprecated
(
since
="9")
public
X509Certificate
[] getPeerCertificateChain()
throws
SSLPeerUnverifiedException
```

Deprecated.

The

getPeerCertificates()

method that returns an
array of

java.security.cert.Certificate

should
be used instead.

Returns the identity of the peer which was identified as part
of defining the session.
Note: This method can be used only when using certificate-based
cipher suites; using it with non-certificate-based cipher suites,
such as Kerberos, will throw an SSLPeerUnverifiedException.

Note: The returned value may not be a valid certificate chain
and should not be relied on for trust decisions.

Note: this method exists for compatibility with previous
releases. New applications should use

getPeerCertificates()

instead.

**Returns:** an ordered array of peer X.509 certificates,
with the peer's own certificate first followed by any
certificate authorities. (The certificates are in
the original JSSE

X509Certificate

format).
**Throws:** SSLPeerUnverifiedException

- if the peer is not verified.
**See Also:** getPeerPrincipal()

- getPeerPrincipal

```java
public
Principal
getPeerPrincipal()
throws
SSLPeerUnverifiedException
```

Returns the identity of the peer which was established as part of
defining the session.

**Returns:** the peer's principal. Returns an X500Principal of the
end-entity certiticate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites.
**Throws:** SSLPeerUnverifiedException

- if the peer's identity has not
been verified
**Since:** 1.5
**See Also:** getPeerCertificates()

,

getLocalPrincipal()

- getLocalPrincipal

```java
public
Principal
getLocalPrincipal()
```

Returns the principal that was sent to the peer during handshaking.

**Returns:** the principal sent to the peer. Returns an X500Principal
of the end-entity certificate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites. If no principal was
sent, then null is returned.
**Since:** 1.5
**See Also:** getLocalCertificates()

,

getPeerPrincipal()

- getSocket

```java
public
SSLSocket
getSocket()
```

Returns the socket which is the source of this event.
(This is a convenience function, to let applications
write code without type casts.)

**Returns:** the socket on which the connection was made.

Constructor Detail

- HandshakeCompletedEvent

```java
public HandshakeCompletedEvent​(
SSLSocket
sock,

SSLSession
s)
```

Constructs a new HandshakeCompletedEvent.

**Parameters:** sock

- the SSLSocket acting as the source of the event
**Parameters:** s

- the SSLSession this event is associated with

---

#### Constructor Detail

HandshakeCompletedEvent

```java
public HandshakeCompletedEvent​(
SSLSocket
sock,

SSLSession
s)
```

Constructs a new HandshakeCompletedEvent.

**Parameters:** sock

- the SSLSocket acting as the source of the event
**Parameters:** s

- the SSLSession this event is associated with

---

#### HandshakeCompletedEvent

public HandshakeCompletedEvent​(

SSLSocket

sock,

SSLSession

s)

Constructs a new HandshakeCompletedEvent.

Method Detail

- getSession

```java
public
SSLSession
getSession()
```

Returns the session that triggered this event.

**Returns:** the

SSLSession

for this handshake

- getCipherSuite

```java
public
String
getCipherSuite()
```

Returns the cipher suite in use by the session which was produced
by the handshake. (This is a convenience method for
getting the ciphersuite from the SSLsession.)

**Returns:** the name of the cipher suite negotiated during this session.

- getLocalCertificates

```java
public
Certificate
[] getLocalCertificates()
```

Returns the certificate(s) that were sent to the peer during
handshaking.
Note: This method is useful only when using certificate-based
cipher suites.

When multiple certificates are available for use in a
handshake, the implementation chooses what it considers the
"best" certificate chain available, and transmits that to
the other side. This method allows the caller to know
which certificate chain was actually used.

**Returns:** an ordered array of certificates, with the local
certificate first followed by any
certificate authorities. If no certificates were sent,
then null is returned.
**See Also:** getLocalPrincipal()

- getPeerCertificates

```java
public
Certificate
[] getPeerCertificates()
throws
SSLPeerUnverifiedException
```

Returns the identity of the peer which was established as part
of defining the session.
Note: This method can be used only when using certificate-based
cipher suites; using it with non-certificate-based cipher suites,
such as Kerberos, will throw an SSLPeerUnverifiedException.

Note: The returned value may not be a valid certificate chain
and should not be relied on for trust decisions.

**Returns:** an ordered array of the peer certificates,
with the peer's own certificate first followed by
any certificate authorities.
**Throws:** SSLPeerUnverifiedException

- if the peer is not verified.
**See Also:** getPeerPrincipal()

- getPeerCertificateChain

```java
@Deprecated
(
since
="9")
public
X509Certificate
[] getPeerCertificateChain()
throws
SSLPeerUnverifiedException
```

Deprecated.

The

getPeerCertificates()

method that returns an
array of

java.security.cert.Certificate

should
be used instead.

Returns the identity of the peer which was identified as part
of defining the session.
Note: This method can be used only when using certificate-based
cipher suites; using it with non-certificate-based cipher suites,
such as Kerberos, will throw an SSLPeerUnverifiedException.

Note: The returned value may not be a valid certificate chain
and should not be relied on for trust decisions.

Note: this method exists for compatibility with previous
releases. New applications should use

getPeerCertificates()

instead.

**Returns:** an ordered array of peer X.509 certificates,
with the peer's own certificate first followed by any
certificate authorities. (The certificates are in
the original JSSE

X509Certificate

format).
**Throws:** SSLPeerUnverifiedException

- if the peer is not verified.
**See Also:** getPeerPrincipal()

- getPeerPrincipal

```java
public
Principal
getPeerPrincipal()
throws
SSLPeerUnverifiedException
```

Returns the identity of the peer which was established as part of
defining the session.

**Returns:** the peer's principal. Returns an X500Principal of the
end-entity certiticate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites.
**Throws:** SSLPeerUnverifiedException

- if the peer's identity has not
been verified
**Since:** 1.5
**See Also:** getPeerCertificates()

,

getLocalPrincipal()

- getLocalPrincipal

```java
public
Principal
getLocalPrincipal()
```

Returns the principal that was sent to the peer during handshaking.

**Returns:** the principal sent to the peer. Returns an X500Principal
of the end-entity certificate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites. If no principal was
sent, then null is returned.
**Since:** 1.5
**See Also:** getLocalCertificates()

,

getPeerPrincipal()

- getSocket

```java
public
SSLSocket
getSocket()
```

Returns the socket which is the source of this event.
(This is a convenience function, to let applications
write code without type casts.)

**Returns:** the socket on which the connection was made.

---

#### Method Detail

getSession

```java
public
SSLSession
getSession()
```

Returns the session that triggered this event.

**Returns:** the

SSLSession

for this handshake

---

#### getSession

public

SSLSession

getSession()

Returns the session that triggered this event.

getCipherSuite

```java
public
String
getCipherSuite()
```

Returns the cipher suite in use by the session which was produced
by the handshake. (This is a convenience method for
getting the ciphersuite from the SSLsession.)

**Returns:** the name of the cipher suite negotiated during this session.

---

#### getCipherSuite

public

String

getCipherSuite()

Returns the cipher suite in use by the session which was produced
by the handshake. (This is a convenience method for
getting the ciphersuite from the SSLsession.)

getLocalCertificates

```java
public
Certificate
[] getLocalCertificates()
```

Returns the certificate(s) that were sent to the peer during
handshaking.
Note: This method is useful only when using certificate-based
cipher suites.

When multiple certificates are available for use in a
handshake, the implementation chooses what it considers the
"best" certificate chain available, and transmits that to
the other side. This method allows the caller to know
which certificate chain was actually used.

**Returns:** an ordered array of certificates, with the local
certificate first followed by any
certificate authorities. If no certificates were sent,
then null is returned.
**See Also:** getLocalPrincipal()

---

#### getLocalCertificates

public

Certificate

[] getLocalCertificates()

Returns the certificate(s) that were sent to the peer during
handshaking.
Note: This method is useful only when using certificate-based
cipher suites.

When multiple certificates are available for use in a
handshake, the implementation chooses what it considers the
"best" certificate chain available, and transmits that to
the other side. This method allows the caller to know
which certificate chain was actually used.

getPeerCertificates

```java
public
Certificate
[] getPeerCertificates()
throws
SSLPeerUnverifiedException
```

Returns the identity of the peer which was established as part
of defining the session.
Note: This method can be used only when using certificate-based
cipher suites; using it with non-certificate-based cipher suites,
such as Kerberos, will throw an SSLPeerUnverifiedException.

Note: The returned value may not be a valid certificate chain
and should not be relied on for trust decisions.

**Returns:** an ordered array of the peer certificates,
with the peer's own certificate first followed by
any certificate authorities.
**Throws:** SSLPeerUnverifiedException

- if the peer is not verified.
**See Also:** getPeerPrincipal()

---

#### getPeerCertificates

public

Certificate

[] getPeerCertificates()
throws

SSLPeerUnverifiedException

Returns the identity of the peer which was established as part
of defining the session.
Note: This method can be used only when using certificate-based
cipher suites; using it with non-certificate-based cipher suites,
such as Kerberos, will throw an SSLPeerUnverifiedException.

Note: The returned value may not be a valid certificate chain
and should not be relied on for trust decisions.

Note: The returned value may not be a valid certificate chain
and should not be relied on for trust decisions.

getPeerCertificateChain

```java
@Deprecated
(
since
="9")
public
X509Certificate
[] getPeerCertificateChain()
throws
SSLPeerUnverifiedException
```

Deprecated.

The

getPeerCertificates()

method that returns an
array of

java.security.cert.Certificate

should
be used instead.

Returns the identity of the peer which was identified as part
of defining the session.
Note: This method can be used only when using certificate-based
cipher suites; using it with non-certificate-based cipher suites,
such as Kerberos, will throw an SSLPeerUnverifiedException.

Note: The returned value may not be a valid certificate chain
and should not be relied on for trust decisions.

Note: this method exists for compatibility with previous
releases. New applications should use

getPeerCertificates()

instead.

**Returns:** an ordered array of peer X.509 certificates,
with the peer's own certificate first followed by any
certificate authorities. (The certificates are in
the original JSSE

X509Certificate

format).
**Throws:** SSLPeerUnverifiedException

- if the peer is not verified.
**See Also:** getPeerPrincipal()

---

#### getPeerCertificateChain

@Deprecated

(

since

="9")
public

X509Certificate

[] getPeerCertificateChain()
throws

SSLPeerUnverifiedException

Returns the identity of the peer which was identified as part
of defining the session.
Note: This method can be used only when using certificate-based
cipher suites; using it with non-certificate-based cipher suites,
such as Kerberos, will throw an SSLPeerUnverifiedException.

Note: The returned value may not be a valid certificate chain
and should not be relied on for trust decisions.

Note: this method exists for compatibility with previous
releases. New applications should use

getPeerCertificates()

instead.

Note: The returned value may not be a valid certificate chain
and should not be relied on for trust decisions.

Note: this method exists for compatibility with previous
releases. New applications should use

getPeerCertificates()

instead.

Note: this method exists for compatibility with previous
releases. New applications should use

getPeerCertificates()

instead.

getPeerPrincipal

```java
public
Principal
getPeerPrincipal()
throws
SSLPeerUnverifiedException
```

Returns the identity of the peer which was established as part of
defining the session.

**Returns:** the peer's principal. Returns an X500Principal of the
end-entity certiticate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites.
**Throws:** SSLPeerUnverifiedException

- if the peer's identity has not
been verified
**Since:** 1.5
**See Also:** getPeerCertificates()

,

getLocalPrincipal()

---

#### getPeerPrincipal

public

Principal

getPeerPrincipal()
throws

SSLPeerUnverifiedException

Returns the identity of the peer which was established as part of
defining the session.

getLocalPrincipal

```java
public
Principal
getLocalPrincipal()
```

Returns the principal that was sent to the peer during handshaking.

**Returns:** the principal sent to the peer. Returns an X500Principal
of the end-entity certificate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites. If no principal was
sent, then null is returned.
**Since:** 1.5
**See Also:** getLocalCertificates()

,

getPeerPrincipal()

---

#### getLocalPrincipal

public

Principal

getLocalPrincipal()

Returns the principal that was sent to the peer during handshaking.

getSocket

```java
public
SSLSocket
getSocket()
```

Returns the socket which is the source of this event.
(This is a convenience function, to let applications
write code without type casts.)

**Returns:** the socket on which the connection was made.

---

#### getSocket

public

SSLSocket

getSocket()

Returns the socket which is the source of this event.
(This is a convenience function, to let applications
write code without type casts.)

---

