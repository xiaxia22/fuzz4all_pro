# Class HttpsURLConnection

**Source:** `java.base\javax\net\ssl\HttpsURLConnection.html`

### Class Description

```java
public abstract class
HttpsURLConnection

extends
HttpURLConnection
```

HttpsURLConnection

extends

HttpURLConnection

with support for https-specific features.

See

http://www.w3.org/pub/WWW/Protocols/

and

RFC 2818

for more details on the
https specification.

This class uses

HostnameVerifier

and

SSLSocketFactory

.
There are default implementations defined for both classes.
However, the implementations can be replaced on a per-class (static) or
per-instance basis. All new

HttpsURLConnection

s instances
will be assigned
the "default" static values at instance creation, but they can be overriden
by calling the appropriate per-instance set method(s) before

connect

ing.

**Since:** 1.4

---

### Field Details

#### protected
HostnameVerifier
hostnameVerifier

The

hostnameVerifier

for this object.

---

### Constructor Details

#### protected HttpsURLConnection​(
URL
url)

Creates an

HttpsURLConnection

using the
URL specified.

**Parameters:**
- url

- the URL

---

### Method Details

#### public abstract
String
getCipherSuite()

Returns the cipher suite in use on this connection.

**Returns:**
- the cipher suite

**Throws:**
- IllegalStateException

- if this method is called before
the connection has been established.

---

#### public abstract
Certificate
[] getLocalCertificates()

Returns the certificate(s) that were sent to the server during
handshaking.

Note: This method is useful only when using certificate-based
cipher suites.

When multiple certificates are available for use in a
handshake, the implementation chooses what it considers the
"best" certificate chain available, and transmits that to
the other side. This method allows the caller to know
which certificate chain was actually sent.

**Returns:**
- an ordered array of certificates,
with the client's own certificate first followed by any
certificate authorities. If no certificates were sent,
then null is returned.

**Throws:**
- IllegalStateException

- if this method is called before
the connection has been established.

**See Also:**
- getLocalPrincipal()

---

#### public abstract
Certificate
[] getServerCertificates()
throws
SSLPeerUnverifiedException

Returns the server's certificate chain which was established
as part of defining the session.

Note: This method can be used only when using certificate-based
cipher suites; using it with non-certificate-based cipher suites,
such as Kerberos, will throw an SSLPeerUnverifiedException.

Note: The returned value may not be a valid certificate chain
and should not be relied on for trust decisions.

**Returns:**
- an ordered array of server certificates,
with the peer's own certificate first followed by
any certificate authorities.

**Throws:**
- SSLPeerUnverifiedException

- if the peer is not verified.
- IllegalStateException

- if this method is called before
the connection has been established.

**See Also:**
- getPeerPrincipal()

---

#### public
Principal
getPeerPrincipal()
throws
SSLPeerUnverifiedException

Returns the server's principal which was established as part of
defining the session.

Note: Subclasses should override this method. If not overridden, it
will default to returning the X500Principal of the server's end-entity
certificate for certificate-based ciphersuites, or throw an
SSLPeerUnverifiedException for non-certificate based ciphersuites,
such as Kerberos.

**Returns:**
- the server's principal. Returns an X500Principal of the
end-entity certiticate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites.

**Throws:**
- SSLPeerUnverifiedException

- if the peer was not verified
- IllegalStateException

- if this method is called before
the connection has been established.

**See Also:**
- getServerCertificates()

,

getLocalPrincipal()

**Since:**
- 1.5

---

#### public
Principal
getLocalPrincipal()

Returns the principal that was sent to the server during handshaking.

Note: Subclasses should override this method. If not overridden, it
will default to returning the X500Principal of the end-entity certificate
that was sent to the server for certificate-based ciphersuites or,
return null for non-certificate based ciphersuites, such as Kerberos.

**Returns:**
- the principal sent to the server. Returns an X500Principal
of the end-entity certificate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites. If no principal was
sent, then null is returned.

**Throws:**
- IllegalStateException

- if this method is called before
the connection has been established.

**See Also:**
- getLocalCertificates()

,

getPeerPrincipal()

**Since:**
- 1.5

---

#### public static void setDefaultHostnameVerifier​(
HostnameVerifier
v)

Sets the default

HostnameVerifier

inherited by a
new instance of this class.

If this method is not called, the default

HostnameVerifier

assumes the connection should not
be permitted.

**Parameters:**
- v

- the default host name verifier

**Throws:**
- IllegalArgumentException

- if the

HostnameVerifier

parameter is null.
- SecurityException

- if a security manager exists and its

checkPermission

method does not allow

SSLPermission("setHostnameVerifier")

**See Also:**
- getDefaultHostnameVerifier()

---

#### public static
HostnameVerifier
getDefaultHostnameVerifier()

Gets the default

HostnameVerifier

that is inherited
by new instances of this class.

**Returns:**
- the default host name verifier

**See Also:**
- setDefaultHostnameVerifier(HostnameVerifier)

---

#### public void setHostnameVerifier​(
HostnameVerifier
v)

Sets the

HostnameVerifier

for this instance.

New instances of this class inherit the default static hostname
verifier set by

setDefaultHostnameVerifier

. Calls to this method replace
this object's

HostnameVerifier

.

**Parameters:**
- v

- the host name verifier

**Throws:**
- IllegalArgumentException

- if the

HostnameVerifier

parameter is null.

**See Also:**
- getHostnameVerifier()

,

setDefaultHostnameVerifier(HostnameVerifier)

---

#### public
HostnameVerifier
getHostnameVerifier()

Gets the

HostnameVerifier

in place on this instance.

**Returns:**
- the host name verifier

**See Also:**
- setHostnameVerifier(HostnameVerifier)

,

setDefaultHostnameVerifier(HostnameVerifier)

---

#### public static void setDefaultSSLSocketFactory​(
SSLSocketFactory
sf)

Sets the default

SSLSocketFactory

inherited by new
instances of this class.

The socket factories are used when creating sockets for secure
https URL connections.

**Parameters:**
- sf

- the default SSL socket factory

**Throws:**
- IllegalArgumentException

- if the SSLSocketFactory
parameter is null.
- SecurityException

- if a security manager exists and its

checkSetFactory

method does not allow
a socket factory to be specified.

**See Also:**
- getDefaultSSLSocketFactory()

---

#### public static
SSLSocketFactory
getDefaultSSLSocketFactory()

Gets the default static

SSLSocketFactory

that is
inherited by new instances of this class.

The socket factories are used when creating sockets for secure
https URL connections.

**Returns:**
- the default

SSLSocketFactory

**See Also:**
- setDefaultSSLSocketFactory(SSLSocketFactory)

---

#### public void setSSLSocketFactory​(
SSLSocketFactory
sf)

Sets the

SSLSocketFactory

to be used when this instance
creates sockets for secure https URL connections.

New instances of this class inherit the default static

SSLSocketFactory

set by

setDefaultSSLSocketFactory

. Calls to this method replace
this object's

SSLSocketFactory

.

**Parameters:**
- sf

- the SSL socket factory

**Throws:**
- IllegalArgumentException

- if the

SSLSocketFactory

parameter is null.
- SecurityException

- if a security manager exists and its

checkSetFactory

method does not allow
a socket factory to be specified.

**See Also:**
- getSSLSocketFactory()

---

#### public
SSLSocketFactory
getSSLSocketFactory()

Gets the SSL socket factory to be used when creating sockets
for secure https URL connections.

**Returns:**
- the

SSLSocketFactory

**See Also:**
- setSSLSocketFactory(SSLSocketFactory)

---

### Additional Sections

#### Class HttpsURLConnection

java.lang.Object

- java.net.URLConnection
- - java.net.HttpURLConnection
- - javax.net.ssl.HttpsURLConnection

java.net.URLConnection

- java.net.HttpURLConnection
- - javax.net.ssl.HttpsURLConnection

java.net.HttpURLConnection

- javax.net.ssl.HttpsURLConnection

javax.net.ssl.HttpsURLConnection

```java
public abstract class
HttpsURLConnection

extends
HttpURLConnection
```

HttpsURLConnection

extends

HttpURLConnection

with support for https-specific features.

See

http://www.w3.org/pub/WWW/Protocols/

and

RFC 2818

for more details on the
https specification.

This class uses

HostnameVerifier

and

SSLSocketFactory

.
There are default implementations defined for both classes.
However, the implementations can be replaced on a per-class (static) or
per-instance basis. All new

HttpsURLConnection

s instances
will be assigned
the "default" static values at instance creation, but they can be overriden
by calling the appropriate per-instance set method(s) before

connect

ing.

**Since:** 1.4

public abstract class

HttpsURLConnection

extends

HttpURLConnection

HttpsURLConnection

extends

HttpURLConnection

with support for https-specific features.

See

http://www.w3.org/pub/WWW/Protocols/

and

RFC 2818

for more details on the
https specification.

This class uses

HostnameVerifier

and

SSLSocketFactory

.
There are default implementations defined for both classes.
However, the implementations can be replaced on a per-class (static) or
per-instance basis. All new

HttpsURLConnection

s instances
will be assigned
the "default" static values at instance creation, but they can be overriden
by calling the appropriate per-instance set method(s) before

connect

ing.

See

http://www.w3.org/pub/WWW/Protocols/

and

RFC 2818

for more details on the
https specification.

This class uses

HostnameVerifier

and

SSLSocketFactory

.
There are default implementations defined for both classes.
However, the implementations can be replaced on a per-class (static) or
per-instance basis. All new

HttpsURLConnection

s instances
will be assigned
the "default" static values at instance creation, but they can be overriden
by calling the appropriate per-instance set method(s) before

connect

ing.

This class uses

HostnameVerifier

and

SSLSocketFactory

.
There are default implementations defined for both classes.
However, the implementations can be replaced on a per-class (static) or
per-instance basis. All new

HttpsURLConnection

s instances
will be assigned
the "default" static values at instance creation, but they can be overriden
by calling the appropriate per-instance set method(s) before

connect

ing.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

HostnameVerifier

hostnameVerifier

The

hostnameVerifier

for this object.

- Fields declared in class java.net.

HttpURLConnection

chunkLength

,

fixedContentLength

,

fixedContentLengthLong

,

HTTP_ACCEPTED

,

HTTP_BAD_GATEWAY

,

HTTP_BAD_METHOD

,

HTTP_BAD_REQUEST

,

HTTP_CLIENT_TIMEOUT

,

HTTP_CONFLICT

,

HTTP_CREATED

,

HTTP_ENTITY_TOO_LARGE

,

HTTP_FORBIDDEN

,

HTTP_GATEWAY_TIMEOUT

,

HTTP_GONE

,

HTTP_INTERNAL_ERROR

,

HTTP_LENGTH_REQUIRED

,

HTTP_MOVED_PERM

,

HTTP_MOVED_TEMP

,

HTTP_MULT_CHOICE

,

HTTP_NO_CONTENT

,

HTTP_NOT_ACCEPTABLE

,

HTTP_NOT_AUTHORITATIVE

,

HTTP_NOT_FOUND

,

HTTP_NOT_IMPLEMENTED

,

HTTP_NOT_MODIFIED

,

HTTP_OK

,

HTTP_PARTIAL

,

HTTP_PAYMENT_REQUIRED

,

HTTP_PRECON_FAILED

,

HTTP_PROXY_AUTH

,

HTTP_REQ_TOO_LONG

,

HTTP_RESET

,

HTTP_SEE_OTHER

,

HTTP_SERVER_ERROR

,

HTTP_UNAUTHORIZED

,

HTTP_UNAVAILABLE

,

HTTP_UNSUPPORTED_TYPE

,

HTTP_USE_PROXY

,

HTTP_VERSION

,

instanceFollowRedirects

,

method

,

responseCode

,

responseMessage

- Fields declared in class java.net.

URLConnection

allowUserInteraction

,

connected

,

doInput

,

doOutput

,

ifModifiedSince

,

url

,

useCaches

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

HttpsURLConnection

​(

URL

url)

Creates an

HttpsURLConnection

using the
URL specified.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

String

getCipherSuite

()

Returns the cipher suite in use on this connection.

static

HostnameVerifier

getDefaultHostnameVerifier

()

Gets the default

HostnameVerifier

that is inherited
by new instances of this class.

static

SSLSocketFactory

getDefaultSSLSocketFactory

()

Gets the default static

SSLSocketFactory

that is
inherited by new instances of this class.

HostnameVerifier

getHostnameVerifier

()

Gets the

HostnameVerifier

in place on this instance.

abstract

Certificate

[]

getLocalCertificates

()

Returns the certificate(s) that were sent to the server during
handshaking.

Principal

getLocalPrincipal

()

Returns the principal that was sent to the server during handshaking.

Principal

getPeerPrincipal

()

Returns the server's principal which was established as part of
defining the session.

abstract

Certificate

[]

getServerCertificates

()

Returns the server's certificate chain which was established
as part of defining the session.

SSLSocketFactory

getSSLSocketFactory

()

Gets the SSL socket factory to be used when creating sockets
for secure https URL connections.

static void

setDefaultHostnameVerifier

​(

HostnameVerifier

v)

Sets the default

HostnameVerifier

inherited by a
new instance of this class.

static void

setDefaultSSLSocketFactory

​(

SSLSocketFactory

sf)

Sets the default

SSLSocketFactory

inherited by new
instances of this class.

void

setHostnameVerifier

​(

HostnameVerifier

v)

Sets the

HostnameVerifier

for this instance.

void

setSSLSocketFactory

​(

SSLSocketFactory

sf)

Sets the

SSLSocketFactory

to be used when this instance
creates sockets for secure https URL connections.

- Methods declared in class java.net.

HttpURLConnection

disconnect

,

getErrorStream

,

getFollowRedirects

,

getHeaderField

,

getHeaderFieldKey

,

getInstanceFollowRedirects

,

getPermission

,

getRequestMethod

,

getResponseCode

,

getResponseMessage

,

setAuthenticator

,

setChunkedStreamingMode

,

setFixedLengthStreamingMode

,

setFixedLengthStreamingMode

,

setFollowRedirects

,

setInstanceFollowRedirects

,

setRequestMethod

,

usingProxy

- Methods declared in class java.net.

URLConnection

addRequestProperty

,

connect

,

getAllowUserInteraction

,

getConnectTimeout

,

getContent

,

getContent

,

getContentEncoding

,

getContentLength

,

getContentLengthLong

,

getContentType

,

getDate

,

getDefaultAllowUserInteraction

,

getDefaultRequestProperty

,

getDefaultUseCaches

,

getDefaultUseCaches

,

getDoInput

,

getDoOutput

,

getExpiration

,

getFileNameMap

,

getHeaderField

,

getHeaderFieldDate

,

getHeaderFieldInt

,

getHeaderFieldLong

,

getHeaderFields

,

getIfModifiedSince

,

getInputStream

,

getLastModified

,

getOutputStream

,

getReadTimeout

,

getRequestProperties

,

getRequestProperty

,

getURL

,

getUseCaches

,

guessContentTypeFromName

,

guessContentTypeFromStream

,

setAllowUserInteraction

,

setConnectTimeout

,

setContentHandlerFactory

,

setDefaultAllowUserInteraction

,

setDefaultRequestProperty

,

setDefaultUseCaches

,

setDefaultUseCaches

,

setDoInput

,

setDoOutput

,

setFileNameMap

,

setIfModifiedSince

,

setReadTimeout

,

setRequestProperty

,

setUseCaches

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

Fields

Modifier and Type

Field

Description

protected

HostnameVerifier

hostnameVerifier

The

hostnameVerifier

for this object.

- Fields declared in class java.net.

HttpURLConnection

chunkLength

,

fixedContentLength

,

fixedContentLengthLong

,

HTTP_ACCEPTED

,

HTTP_BAD_GATEWAY

,

HTTP_BAD_METHOD

,

HTTP_BAD_REQUEST

,

HTTP_CLIENT_TIMEOUT

,

HTTP_CONFLICT

,

HTTP_CREATED

,

HTTP_ENTITY_TOO_LARGE

,

HTTP_FORBIDDEN

,

HTTP_GATEWAY_TIMEOUT

,

HTTP_GONE

,

HTTP_INTERNAL_ERROR

,

HTTP_LENGTH_REQUIRED

,

HTTP_MOVED_PERM

,

HTTP_MOVED_TEMP

,

HTTP_MULT_CHOICE

,

HTTP_NO_CONTENT

,

HTTP_NOT_ACCEPTABLE

,

HTTP_NOT_AUTHORITATIVE

,

HTTP_NOT_FOUND

,

HTTP_NOT_IMPLEMENTED

,

HTTP_NOT_MODIFIED

,

HTTP_OK

,

HTTP_PARTIAL

,

HTTP_PAYMENT_REQUIRED

,

HTTP_PRECON_FAILED

,

HTTP_PROXY_AUTH

,

HTTP_REQ_TOO_LONG

,

HTTP_RESET

,

HTTP_SEE_OTHER

,

HTTP_SERVER_ERROR

,

HTTP_UNAUTHORIZED

,

HTTP_UNAVAILABLE

,

HTTP_UNSUPPORTED_TYPE

,

HTTP_USE_PROXY

,

HTTP_VERSION

,

instanceFollowRedirects

,

method

,

responseCode

,

responseMessage

- Fields declared in class java.net.

URLConnection

allowUserInteraction

,

connected

,

doInput

,

doOutput

,

ifModifiedSince

,

url

,

useCaches

---

#### Field Summary

The

hostnameVerifier

for this object.

Fields declared in class java.net.

HttpURLConnection

chunkLength

,

fixedContentLength

,

fixedContentLengthLong

,

HTTP_ACCEPTED

,

HTTP_BAD_GATEWAY

,

HTTP_BAD_METHOD

,

HTTP_BAD_REQUEST

,

HTTP_CLIENT_TIMEOUT

,

HTTP_CONFLICT

,

HTTP_CREATED

,

HTTP_ENTITY_TOO_LARGE

,

HTTP_FORBIDDEN

,

HTTP_GATEWAY_TIMEOUT

,

HTTP_GONE

,

HTTP_INTERNAL_ERROR

,

HTTP_LENGTH_REQUIRED

,

HTTP_MOVED_PERM

,

HTTP_MOVED_TEMP

,

HTTP_MULT_CHOICE

,

HTTP_NO_CONTENT

,

HTTP_NOT_ACCEPTABLE

,

HTTP_NOT_AUTHORITATIVE

,

HTTP_NOT_FOUND

,

HTTP_NOT_IMPLEMENTED

,

HTTP_NOT_MODIFIED

,

HTTP_OK

,

HTTP_PARTIAL

,

HTTP_PAYMENT_REQUIRED

,

HTTP_PRECON_FAILED

,

HTTP_PROXY_AUTH

,

HTTP_REQ_TOO_LONG

,

HTTP_RESET

,

HTTP_SEE_OTHER

,

HTTP_SERVER_ERROR

,

HTTP_UNAUTHORIZED

,

HTTP_UNAVAILABLE

,

HTTP_UNSUPPORTED_TYPE

,

HTTP_USE_PROXY

,

HTTP_VERSION

,

instanceFollowRedirects

,

method

,

responseCode

,

responseMessage

---

#### Fields declared in class java.net. HttpURLConnection

Fields declared in class java.net.

URLConnection

allowUserInteraction

,

connected

,

doInput

,

doOutput

,

ifModifiedSince

,

url

,

useCaches

---

#### Fields declared in class java.net. URLConnection

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

HttpsURLConnection

​(

URL

url)

Creates an

HttpsURLConnection

using the
URL specified.

---

#### Constructor Summary

Creates an

HttpsURLConnection

using the
URL specified.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

String

getCipherSuite

()

Returns the cipher suite in use on this connection.

static

HostnameVerifier

getDefaultHostnameVerifier

()

Gets the default

HostnameVerifier

that is inherited
by new instances of this class.

static

SSLSocketFactory

getDefaultSSLSocketFactory

()

Gets the default static

SSLSocketFactory

that is
inherited by new instances of this class.

HostnameVerifier

getHostnameVerifier

()

Gets the

HostnameVerifier

in place on this instance.

abstract

Certificate

[]

getLocalCertificates

()

Returns the certificate(s) that were sent to the server during
handshaking.

Principal

getLocalPrincipal

()

Returns the principal that was sent to the server during handshaking.

Principal

getPeerPrincipal

()

Returns the server's principal which was established as part of
defining the session.

abstract

Certificate

[]

getServerCertificates

()

Returns the server's certificate chain which was established
as part of defining the session.

SSLSocketFactory

getSSLSocketFactory

()

Gets the SSL socket factory to be used when creating sockets
for secure https URL connections.

static void

setDefaultHostnameVerifier

​(

HostnameVerifier

v)

Sets the default

HostnameVerifier

inherited by a
new instance of this class.

static void

setDefaultSSLSocketFactory

​(

SSLSocketFactory

sf)

Sets the default

SSLSocketFactory

inherited by new
instances of this class.

void

setHostnameVerifier

​(

HostnameVerifier

v)

Sets the

HostnameVerifier

for this instance.

void

setSSLSocketFactory

​(

SSLSocketFactory

sf)

Sets the

SSLSocketFactory

to be used when this instance
creates sockets for secure https URL connections.

- Methods declared in class java.net.

HttpURLConnection

disconnect

,

getErrorStream

,

getFollowRedirects

,

getHeaderField

,

getHeaderFieldKey

,

getInstanceFollowRedirects

,

getPermission

,

getRequestMethod

,

getResponseCode

,

getResponseMessage

,

setAuthenticator

,

setChunkedStreamingMode

,

setFixedLengthStreamingMode

,

setFixedLengthStreamingMode

,

setFollowRedirects

,

setInstanceFollowRedirects

,

setRequestMethod

,

usingProxy

- Methods declared in class java.net.

URLConnection

addRequestProperty

,

connect

,

getAllowUserInteraction

,

getConnectTimeout

,

getContent

,

getContent

,

getContentEncoding

,

getContentLength

,

getContentLengthLong

,

getContentType

,

getDate

,

getDefaultAllowUserInteraction

,

getDefaultRequestProperty

,

getDefaultUseCaches

,

getDefaultUseCaches

,

getDoInput

,

getDoOutput

,

getExpiration

,

getFileNameMap

,

getHeaderField

,

getHeaderFieldDate

,

getHeaderFieldInt

,

getHeaderFieldLong

,

getHeaderFields

,

getIfModifiedSince

,

getInputStream

,

getLastModified

,

getOutputStream

,

getReadTimeout

,

getRequestProperties

,

getRequestProperty

,

getURL

,

getUseCaches

,

guessContentTypeFromName

,

guessContentTypeFromStream

,

setAllowUserInteraction

,

setConnectTimeout

,

setContentHandlerFactory

,

setDefaultAllowUserInteraction

,

setDefaultRequestProperty

,

setDefaultUseCaches

,

setDefaultUseCaches

,

setDoInput

,

setDoOutput

,

setFileNameMap

,

setIfModifiedSince

,

setReadTimeout

,

setRequestProperty

,

setUseCaches

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

Returns the cipher suite in use on this connection.

Gets the default

HostnameVerifier

that is inherited
by new instances of this class.

Gets the default static

SSLSocketFactory

that is
inherited by new instances of this class.

Gets the

HostnameVerifier

in place on this instance.

Returns the certificate(s) that were sent to the server during
handshaking.

Returns the principal that was sent to the server during handshaking.

Returns the server's principal which was established as part of
defining the session.

Returns the server's certificate chain which was established
as part of defining the session.

Gets the SSL socket factory to be used when creating sockets
for secure https URL connections.

Sets the default

HostnameVerifier

inherited by a
new instance of this class.

Sets the default

SSLSocketFactory

inherited by new
instances of this class.

Sets the

HostnameVerifier

for this instance.

Sets the

SSLSocketFactory

to be used when this instance
creates sockets for secure https URL connections.

Methods declared in class java.net.

HttpURLConnection

disconnect

,

getErrorStream

,

getFollowRedirects

,

getHeaderField

,

getHeaderFieldKey

,

getInstanceFollowRedirects

,

getPermission

,

getRequestMethod

,

getResponseCode

,

getResponseMessage

,

setAuthenticator

,

setChunkedStreamingMode

,

setFixedLengthStreamingMode

,

setFixedLengthStreamingMode

,

setFollowRedirects

,

setInstanceFollowRedirects

,

setRequestMethod

,

usingProxy

---

#### Methods declared in class java.net. HttpURLConnection

Methods declared in class java.net.

URLConnection

addRequestProperty

,

connect

,

getAllowUserInteraction

,

getConnectTimeout

,

getContent

,

getContent

,

getContentEncoding

,

getContentLength

,

getContentLengthLong

,

getContentType

,

getDate

,

getDefaultAllowUserInteraction

,

getDefaultRequestProperty

,

getDefaultUseCaches

,

getDefaultUseCaches

,

getDoInput

,

getDoOutput

,

getExpiration

,

getFileNameMap

,

getHeaderField

,

getHeaderFieldDate

,

getHeaderFieldInt

,

getHeaderFieldLong

,

getHeaderFields

,

getIfModifiedSince

,

getInputStream

,

getLastModified

,

getOutputStream

,

getReadTimeout

,

getRequestProperties

,

getRequestProperty

,

getURL

,

getUseCaches

,

guessContentTypeFromName

,

guessContentTypeFromStream

,

setAllowUserInteraction

,

setConnectTimeout

,

setContentHandlerFactory

,

setDefaultAllowUserInteraction

,

setDefaultRequestProperty

,

setDefaultUseCaches

,

setDefaultUseCaches

,

setDoInput

,

setDoOutput

,

setFileNameMap

,

setIfModifiedSince

,

setReadTimeout

,

setRequestProperty

,

setUseCaches

,

toString

---

#### Methods declared in class java.net. URLConnection

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

============ FIELD DETAIL ===========

- Field Detail

- hostnameVerifier

```java
protected
HostnameVerifier
hostnameVerifier
```

The

hostnameVerifier

for this object.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- HttpsURLConnection

```java
protected HttpsURLConnection​(
URL
url)
```

Creates an

HttpsURLConnection

using the
URL specified.

**Parameters:** url

- the URL

============ METHOD DETAIL ==========

- Method Detail

- getCipherSuite

```java
public abstract
String
getCipherSuite()
```

Returns the cipher suite in use on this connection.

**Returns:** the cipher suite
**Throws:** IllegalStateException

- if this method is called before
the connection has been established.

- getLocalCertificates

```java
public abstract
Certificate
[] getLocalCertificates()
```

Returns the certificate(s) that were sent to the server during
handshaking.

Note: This method is useful only when using certificate-based
cipher suites.

When multiple certificates are available for use in a
handshake, the implementation chooses what it considers the
"best" certificate chain available, and transmits that to
the other side. This method allows the caller to know
which certificate chain was actually sent.

**Returns:** an ordered array of certificates,
with the client's own certificate first followed by any
certificate authorities. If no certificates were sent,
then null is returned.
**Throws:** IllegalStateException

- if this method is called before
the connection has been established.
**See Also:** getLocalPrincipal()

- getServerCertificates

```java
public abstract
Certificate
[] getServerCertificates()
throws
SSLPeerUnverifiedException
```

Returns the server's certificate chain which was established
as part of defining the session.

Note: This method can be used only when using certificate-based
cipher suites; using it with non-certificate-based cipher suites,
such as Kerberos, will throw an SSLPeerUnverifiedException.

Note: The returned value may not be a valid certificate chain
and should not be relied on for trust decisions.

**Returns:** an ordered array of server certificates,
with the peer's own certificate first followed by
any certificate authorities.
**Throws:** SSLPeerUnverifiedException

- if the peer is not verified.
**Throws:** IllegalStateException

- if this method is called before
the connection has been established.
**See Also:** getPeerPrincipal()

- getPeerPrincipal

```java
public
Principal
getPeerPrincipal()
throws
SSLPeerUnverifiedException
```

Returns the server's principal which was established as part of
defining the session.

Note: Subclasses should override this method. If not overridden, it
will default to returning the X500Principal of the server's end-entity
certificate for certificate-based ciphersuites, or throw an
SSLPeerUnverifiedException for non-certificate based ciphersuites,
such as Kerberos.

**Returns:** the server's principal. Returns an X500Principal of the
end-entity certiticate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites.
**Throws:** SSLPeerUnverifiedException

- if the peer was not verified
**Throws:** IllegalStateException

- if this method is called before
the connection has been established.
**Since:** 1.5
**See Also:** getServerCertificates()

,

getLocalPrincipal()

- getLocalPrincipal

```java
public
Principal
getLocalPrincipal()
```

Returns the principal that was sent to the server during handshaking.

Note: Subclasses should override this method. If not overridden, it
will default to returning the X500Principal of the end-entity certificate
that was sent to the server for certificate-based ciphersuites or,
return null for non-certificate based ciphersuites, such as Kerberos.

**Returns:** the principal sent to the server. Returns an X500Principal
of the end-entity certificate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites. If no principal was
sent, then null is returned.
**Throws:** IllegalStateException

- if this method is called before
the connection has been established.
**Since:** 1.5
**See Also:** getLocalCertificates()

,

getPeerPrincipal()

- setDefaultHostnameVerifier

```java
public static void setDefaultHostnameVerifier​(
HostnameVerifier
v)
```

Sets the default

HostnameVerifier

inherited by a
new instance of this class.

If this method is not called, the default

HostnameVerifier

assumes the connection should not
be permitted.

**Parameters:** v

- the default host name verifier
**Throws:** IllegalArgumentException

- if the

HostnameVerifier

parameter is null.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method does not allow

SSLPermission("setHostnameVerifier")
**See Also:** getDefaultHostnameVerifier()

- getDefaultHostnameVerifier

```java
public static
HostnameVerifier
getDefaultHostnameVerifier()
```

Gets the default

HostnameVerifier

that is inherited
by new instances of this class.

**Returns:** the default host name verifier
**See Also:** setDefaultHostnameVerifier(HostnameVerifier)

- setHostnameVerifier

```java
public void setHostnameVerifier​(
HostnameVerifier
v)
```

Sets the

HostnameVerifier

for this instance.

New instances of this class inherit the default static hostname
verifier set by

setDefaultHostnameVerifier

. Calls to this method replace
this object's

HostnameVerifier

.

**Parameters:** v

- the host name verifier
**Throws:** IllegalArgumentException

- if the

HostnameVerifier

parameter is null.
**See Also:** getHostnameVerifier()

,

setDefaultHostnameVerifier(HostnameVerifier)

- getHostnameVerifier

```java
public
HostnameVerifier
getHostnameVerifier()
```

Gets the

HostnameVerifier

in place on this instance.

**Returns:** the host name verifier
**See Also:** setHostnameVerifier(HostnameVerifier)

,

setDefaultHostnameVerifier(HostnameVerifier)

- setDefaultSSLSocketFactory

```java
public static void setDefaultSSLSocketFactory​(
SSLSocketFactory
sf)
```

Sets the default

SSLSocketFactory

inherited by new
instances of this class.

The socket factories are used when creating sockets for secure
https URL connections.

**Parameters:** sf

- the default SSL socket factory
**Throws:** IllegalArgumentException

- if the SSLSocketFactory
parameter is null.
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method does not allow
a socket factory to be specified.
**See Also:** getDefaultSSLSocketFactory()

- getDefaultSSLSocketFactory

```java
public static
SSLSocketFactory
getDefaultSSLSocketFactory()
```

Gets the default static

SSLSocketFactory

that is
inherited by new instances of this class.

The socket factories are used when creating sockets for secure
https URL connections.

**Returns:** the default

SSLSocketFactory
**See Also:** setDefaultSSLSocketFactory(SSLSocketFactory)

- setSSLSocketFactory

```java
public void setSSLSocketFactory​(
SSLSocketFactory
sf)
```

Sets the

SSLSocketFactory

to be used when this instance
creates sockets for secure https URL connections.

New instances of this class inherit the default static

SSLSocketFactory

set by

setDefaultSSLSocketFactory

. Calls to this method replace
this object's

SSLSocketFactory

.

**Parameters:** sf

- the SSL socket factory
**Throws:** IllegalArgumentException

- if the

SSLSocketFactory

parameter is null.
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method does not allow
a socket factory to be specified.
**See Also:** getSSLSocketFactory()

- getSSLSocketFactory

```java
public
SSLSocketFactory
getSSLSocketFactory()
```

Gets the SSL socket factory to be used when creating sockets
for secure https URL connections.

**Returns:** the

SSLSocketFactory
**See Also:** setSSLSocketFactory(SSLSocketFactory)

Field Detail

- hostnameVerifier

```java
protected
HostnameVerifier
hostnameVerifier
```

The

hostnameVerifier

for this object.

---

#### Field Detail

hostnameVerifier

```java
protected
HostnameVerifier
hostnameVerifier
```

The

hostnameVerifier

for this object.

---

#### hostnameVerifier

protected

HostnameVerifier

hostnameVerifier

The

hostnameVerifier

for this object.

Constructor Detail

- HttpsURLConnection

```java
protected HttpsURLConnection​(
URL
url)
```

Creates an

HttpsURLConnection

using the
URL specified.

**Parameters:** url

- the URL

---

#### Constructor Detail

HttpsURLConnection

```java
protected HttpsURLConnection​(
URL
url)
```

Creates an

HttpsURLConnection

using the
URL specified.

**Parameters:** url

- the URL

---

#### HttpsURLConnection

protected HttpsURLConnection​(

URL

url)

Creates an

HttpsURLConnection

using the
URL specified.

Method Detail

- getCipherSuite

```java
public abstract
String
getCipherSuite()
```

Returns the cipher suite in use on this connection.

**Returns:** the cipher suite
**Throws:** IllegalStateException

- if this method is called before
the connection has been established.

- getLocalCertificates

```java
public abstract
Certificate
[] getLocalCertificates()
```

Returns the certificate(s) that were sent to the server during
handshaking.

Note: This method is useful only when using certificate-based
cipher suites.

When multiple certificates are available for use in a
handshake, the implementation chooses what it considers the
"best" certificate chain available, and transmits that to
the other side. This method allows the caller to know
which certificate chain was actually sent.

**Returns:** an ordered array of certificates,
with the client's own certificate first followed by any
certificate authorities. If no certificates were sent,
then null is returned.
**Throws:** IllegalStateException

- if this method is called before
the connection has been established.
**See Also:** getLocalPrincipal()

- getServerCertificates

```java
public abstract
Certificate
[] getServerCertificates()
throws
SSLPeerUnverifiedException
```

Returns the server's certificate chain which was established
as part of defining the session.

Note: This method can be used only when using certificate-based
cipher suites; using it with non-certificate-based cipher suites,
such as Kerberos, will throw an SSLPeerUnverifiedException.

Note: The returned value may not be a valid certificate chain
and should not be relied on for trust decisions.

**Returns:** an ordered array of server certificates,
with the peer's own certificate first followed by
any certificate authorities.
**Throws:** SSLPeerUnverifiedException

- if the peer is not verified.
**Throws:** IllegalStateException

- if this method is called before
the connection has been established.
**See Also:** getPeerPrincipal()

- getPeerPrincipal

```java
public
Principal
getPeerPrincipal()
throws
SSLPeerUnverifiedException
```

Returns the server's principal which was established as part of
defining the session.

Note: Subclasses should override this method. If not overridden, it
will default to returning the X500Principal of the server's end-entity
certificate for certificate-based ciphersuites, or throw an
SSLPeerUnverifiedException for non-certificate based ciphersuites,
such as Kerberos.

**Returns:** the server's principal. Returns an X500Principal of the
end-entity certiticate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites.
**Throws:** SSLPeerUnverifiedException

- if the peer was not verified
**Throws:** IllegalStateException

- if this method is called before
the connection has been established.
**Since:** 1.5
**See Also:** getServerCertificates()

,

getLocalPrincipal()

- getLocalPrincipal

```java
public
Principal
getLocalPrincipal()
```

Returns the principal that was sent to the server during handshaking.

Note: Subclasses should override this method. If not overridden, it
will default to returning the X500Principal of the end-entity certificate
that was sent to the server for certificate-based ciphersuites or,
return null for non-certificate based ciphersuites, such as Kerberos.

**Returns:** the principal sent to the server. Returns an X500Principal
of the end-entity certificate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites. If no principal was
sent, then null is returned.
**Throws:** IllegalStateException

- if this method is called before
the connection has been established.
**Since:** 1.5
**See Also:** getLocalCertificates()

,

getPeerPrincipal()

- setDefaultHostnameVerifier

```java
public static void setDefaultHostnameVerifier​(
HostnameVerifier
v)
```

Sets the default

HostnameVerifier

inherited by a
new instance of this class.

If this method is not called, the default

HostnameVerifier

assumes the connection should not
be permitted.

**Parameters:** v

- the default host name verifier
**Throws:** IllegalArgumentException

- if the

HostnameVerifier

parameter is null.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method does not allow

SSLPermission("setHostnameVerifier")
**See Also:** getDefaultHostnameVerifier()

- getDefaultHostnameVerifier

```java
public static
HostnameVerifier
getDefaultHostnameVerifier()
```

Gets the default

HostnameVerifier

that is inherited
by new instances of this class.

**Returns:** the default host name verifier
**See Also:** setDefaultHostnameVerifier(HostnameVerifier)

- setHostnameVerifier

```java
public void setHostnameVerifier​(
HostnameVerifier
v)
```

Sets the

HostnameVerifier

for this instance.

New instances of this class inherit the default static hostname
verifier set by

setDefaultHostnameVerifier

. Calls to this method replace
this object's

HostnameVerifier

.

**Parameters:** v

- the host name verifier
**Throws:** IllegalArgumentException

- if the

HostnameVerifier

parameter is null.
**See Also:** getHostnameVerifier()

,

setDefaultHostnameVerifier(HostnameVerifier)

- getHostnameVerifier

```java
public
HostnameVerifier
getHostnameVerifier()
```

Gets the

HostnameVerifier

in place on this instance.

**Returns:** the host name verifier
**See Also:** setHostnameVerifier(HostnameVerifier)

,

setDefaultHostnameVerifier(HostnameVerifier)

- setDefaultSSLSocketFactory

```java
public static void setDefaultSSLSocketFactory​(
SSLSocketFactory
sf)
```

Sets the default

SSLSocketFactory

inherited by new
instances of this class.

The socket factories are used when creating sockets for secure
https URL connections.

**Parameters:** sf

- the default SSL socket factory
**Throws:** IllegalArgumentException

- if the SSLSocketFactory
parameter is null.
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method does not allow
a socket factory to be specified.
**See Also:** getDefaultSSLSocketFactory()

- getDefaultSSLSocketFactory

```java
public static
SSLSocketFactory
getDefaultSSLSocketFactory()
```

Gets the default static

SSLSocketFactory

that is
inherited by new instances of this class.

The socket factories are used when creating sockets for secure
https URL connections.

**Returns:** the default

SSLSocketFactory
**See Also:** setDefaultSSLSocketFactory(SSLSocketFactory)

- setSSLSocketFactory

```java
public void setSSLSocketFactory​(
SSLSocketFactory
sf)
```

Sets the

SSLSocketFactory

to be used when this instance
creates sockets for secure https URL connections.

New instances of this class inherit the default static

SSLSocketFactory

set by

setDefaultSSLSocketFactory

. Calls to this method replace
this object's

SSLSocketFactory

.

**Parameters:** sf

- the SSL socket factory
**Throws:** IllegalArgumentException

- if the

SSLSocketFactory

parameter is null.
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method does not allow
a socket factory to be specified.
**See Also:** getSSLSocketFactory()

- getSSLSocketFactory

```java
public
SSLSocketFactory
getSSLSocketFactory()
```

Gets the SSL socket factory to be used when creating sockets
for secure https URL connections.

**Returns:** the

SSLSocketFactory
**See Also:** setSSLSocketFactory(SSLSocketFactory)

---

#### Method Detail

getCipherSuite

```java
public abstract
String
getCipherSuite()
```

Returns the cipher suite in use on this connection.

**Returns:** the cipher suite
**Throws:** IllegalStateException

- if this method is called before
the connection has been established.

---

#### getCipherSuite

public abstract

String

getCipherSuite()

Returns the cipher suite in use on this connection.

getLocalCertificates

```java
public abstract
Certificate
[] getLocalCertificates()
```

Returns the certificate(s) that were sent to the server during
handshaking.

Note: This method is useful only when using certificate-based
cipher suites.

When multiple certificates are available for use in a
handshake, the implementation chooses what it considers the
"best" certificate chain available, and transmits that to
the other side. This method allows the caller to know
which certificate chain was actually sent.

**Returns:** an ordered array of certificates,
with the client's own certificate first followed by any
certificate authorities. If no certificates were sent,
then null is returned.
**Throws:** IllegalStateException

- if this method is called before
the connection has been established.
**See Also:** getLocalPrincipal()

---

#### getLocalCertificates

public abstract

Certificate

[] getLocalCertificates()

Returns the certificate(s) that were sent to the server during
handshaking.

Note: This method is useful only when using certificate-based
cipher suites.

When multiple certificates are available for use in a
handshake, the implementation chooses what it considers the
"best" certificate chain available, and transmits that to
the other side. This method allows the caller to know
which certificate chain was actually sent.

Note: This method is useful only when using certificate-based
cipher suites.

When multiple certificates are available for use in a
handshake, the implementation chooses what it considers the
"best" certificate chain available, and transmits that to
the other side. This method allows the caller to know
which certificate chain was actually sent.

When multiple certificates are available for use in a
handshake, the implementation chooses what it considers the
"best" certificate chain available, and transmits that to
the other side. This method allows the caller to know
which certificate chain was actually sent.

getServerCertificates

```java
public abstract
Certificate
[] getServerCertificates()
throws
SSLPeerUnverifiedException
```

Returns the server's certificate chain which was established
as part of defining the session.

Note: This method can be used only when using certificate-based
cipher suites; using it with non-certificate-based cipher suites,
such as Kerberos, will throw an SSLPeerUnverifiedException.

Note: The returned value may not be a valid certificate chain
and should not be relied on for trust decisions.

**Returns:** an ordered array of server certificates,
with the peer's own certificate first followed by
any certificate authorities.
**Throws:** SSLPeerUnverifiedException

- if the peer is not verified.
**Throws:** IllegalStateException

- if this method is called before
the connection has been established.
**See Also:** getPeerPrincipal()

---

#### getServerCertificates

public abstract

Certificate

[] getServerCertificates()
throws

SSLPeerUnverifiedException

Returns the server's certificate chain which was established
as part of defining the session.

Note: This method can be used only when using certificate-based
cipher suites; using it with non-certificate-based cipher suites,
such as Kerberos, will throw an SSLPeerUnverifiedException.

Note: The returned value may not be a valid certificate chain
and should not be relied on for trust decisions.

Note: This method can be used only when using certificate-based
cipher suites; using it with non-certificate-based cipher suites,
such as Kerberos, will throw an SSLPeerUnverifiedException.

Note: The returned value may not be a valid certificate chain
and should not be relied on for trust decisions.

Note: The returned value may not be a valid certificate chain
and should not be relied on for trust decisions.

getPeerPrincipal

```java
public
Principal
getPeerPrincipal()
throws
SSLPeerUnverifiedException
```

Returns the server's principal which was established as part of
defining the session.

Note: Subclasses should override this method. If not overridden, it
will default to returning the X500Principal of the server's end-entity
certificate for certificate-based ciphersuites, or throw an
SSLPeerUnverifiedException for non-certificate based ciphersuites,
such as Kerberos.

**Returns:** the server's principal. Returns an X500Principal of the
end-entity certiticate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites.
**Throws:** SSLPeerUnverifiedException

- if the peer was not verified
**Throws:** IllegalStateException

- if this method is called before
the connection has been established.
**Since:** 1.5
**See Also:** getServerCertificates()

,

getLocalPrincipal()

---

#### getPeerPrincipal

public

Principal

getPeerPrincipal()
throws

SSLPeerUnverifiedException

Returns the server's principal which was established as part of
defining the session.

Note: Subclasses should override this method. If not overridden, it
will default to returning the X500Principal of the server's end-entity
certificate for certificate-based ciphersuites, or throw an
SSLPeerUnverifiedException for non-certificate based ciphersuites,
such as Kerberos.

Note: Subclasses should override this method. If not overridden, it
will default to returning the X500Principal of the server's end-entity
certificate for certificate-based ciphersuites, or throw an
SSLPeerUnverifiedException for non-certificate based ciphersuites,
such as Kerberos.

getLocalPrincipal

```java
public
Principal
getLocalPrincipal()
```

Returns the principal that was sent to the server during handshaking.

Note: Subclasses should override this method. If not overridden, it
will default to returning the X500Principal of the end-entity certificate
that was sent to the server for certificate-based ciphersuites or,
return null for non-certificate based ciphersuites, such as Kerberos.

**Returns:** the principal sent to the server. Returns an X500Principal
of the end-entity certificate for X509-based cipher suites, and
KerberosPrincipal for Kerberos cipher suites. If no principal was
sent, then null is returned.
**Throws:** IllegalStateException

- if this method is called before
the connection has been established.
**Since:** 1.5
**See Also:** getLocalCertificates()

,

getPeerPrincipal()

---

#### getLocalPrincipal

public

Principal

getLocalPrincipal()

Returns the principal that was sent to the server during handshaking.

Note: Subclasses should override this method. If not overridden, it
will default to returning the X500Principal of the end-entity certificate
that was sent to the server for certificate-based ciphersuites or,
return null for non-certificate based ciphersuites, such as Kerberos.

Note: Subclasses should override this method. If not overridden, it
will default to returning the X500Principal of the end-entity certificate
that was sent to the server for certificate-based ciphersuites or,
return null for non-certificate based ciphersuites, such as Kerberos.

setDefaultHostnameVerifier

```java
public static void setDefaultHostnameVerifier​(
HostnameVerifier
v)
```

Sets the default

HostnameVerifier

inherited by a
new instance of this class.

If this method is not called, the default

HostnameVerifier

assumes the connection should not
be permitted.

**Parameters:** v

- the default host name verifier
**Throws:** IllegalArgumentException

- if the

HostnameVerifier

parameter is null.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method does not allow

SSLPermission("setHostnameVerifier")
**See Also:** getDefaultHostnameVerifier()

---

#### setDefaultHostnameVerifier

public static void setDefaultHostnameVerifier​(

HostnameVerifier

v)

Sets the default

HostnameVerifier

inherited by a
new instance of this class.

If this method is not called, the default

HostnameVerifier

assumes the connection should not
be permitted.

If this method is not called, the default

HostnameVerifier

assumes the connection should not
be permitted.

getDefaultHostnameVerifier

```java
public static
HostnameVerifier
getDefaultHostnameVerifier()
```

Gets the default

HostnameVerifier

that is inherited
by new instances of this class.

**Returns:** the default host name verifier
**See Also:** setDefaultHostnameVerifier(HostnameVerifier)

---

#### getDefaultHostnameVerifier

public static

HostnameVerifier

getDefaultHostnameVerifier()

Gets the default

HostnameVerifier

that is inherited
by new instances of this class.

setHostnameVerifier

```java
public void setHostnameVerifier​(
HostnameVerifier
v)
```

Sets the

HostnameVerifier

for this instance.

New instances of this class inherit the default static hostname
verifier set by

setDefaultHostnameVerifier

. Calls to this method replace
this object's

HostnameVerifier

.

**Parameters:** v

- the host name verifier
**Throws:** IllegalArgumentException

- if the

HostnameVerifier

parameter is null.
**See Also:** getHostnameVerifier()

,

setDefaultHostnameVerifier(HostnameVerifier)

---

#### setHostnameVerifier

public void setHostnameVerifier​(

HostnameVerifier

v)

Sets the

HostnameVerifier

for this instance.

New instances of this class inherit the default static hostname
verifier set by

setDefaultHostnameVerifier

. Calls to this method replace
this object's

HostnameVerifier

.

New instances of this class inherit the default static hostname
verifier set by

setDefaultHostnameVerifier

. Calls to this method replace
this object's

HostnameVerifier

.

getHostnameVerifier

```java
public
HostnameVerifier
getHostnameVerifier()
```

Gets the

HostnameVerifier

in place on this instance.

**Returns:** the host name verifier
**See Also:** setHostnameVerifier(HostnameVerifier)

,

setDefaultHostnameVerifier(HostnameVerifier)

---

#### getHostnameVerifier

public

HostnameVerifier

getHostnameVerifier()

Gets the

HostnameVerifier

in place on this instance.

setDefaultSSLSocketFactory

```java
public static void setDefaultSSLSocketFactory​(
SSLSocketFactory
sf)
```

Sets the default

SSLSocketFactory

inherited by new
instances of this class.

The socket factories are used when creating sockets for secure
https URL connections.

**Parameters:** sf

- the default SSL socket factory
**Throws:** IllegalArgumentException

- if the SSLSocketFactory
parameter is null.
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method does not allow
a socket factory to be specified.
**See Also:** getDefaultSSLSocketFactory()

---

#### setDefaultSSLSocketFactory

public static void setDefaultSSLSocketFactory​(

SSLSocketFactory

sf)

Sets the default

SSLSocketFactory

inherited by new
instances of this class.

The socket factories are used when creating sockets for secure
https URL connections.

The socket factories are used when creating sockets for secure
https URL connections.

getDefaultSSLSocketFactory

```java
public static
SSLSocketFactory
getDefaultSSLSocketFactory()
```

Gets the default static

SSLSocketFactory

that is
inherited by new instances of this class.

The socket factories are used when creating sockets for secure
https URL connections.

**Returns:** the default

SSLSocketFactory
**See Also:** setDefaultSSLSocketFactory(SSLSocketFactory)

---

#### getDefaultSSLSocketFactory

public static

SSLSocketFactory

getDefaultSSLSocketFactory()

Gets the default static

SSLSocketFactory

that is
inherited by new instances of this class.

The socket factories are used when creating sockets for secure
https URL connections.

The socket factories are used when creating sockets for secure
https URL connections.

setSSLSocketFactory

```java
public void setSSLSocketFactory​(
SSLSocketFactory
sf)
```

Sets the

SSLSocketFactory

to be used when this instance
creates sockets for secure https URL connections.

New instances of this class inherit the default static

SSLSocketFactory

set by

setDefaultSSLSocketFactory

. Calls to this method replace
this object's

SSLSocketFactory

.

**Parameters:** sf

- the SSL socket factory
**Throws:** IllegalArgumentException

- if the

SSLSocketFactory

parameter is null.
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method does not allow
a socket factory to be specified.
**See Also:** getSSLSocketFactory()

---

#### setSSLSocketFactory

public void setSSLSocketFactory​(

SSLSocketFactory

sf)

Sets the

SSLSocketFactory

to be used when this instance
creates sockets for secure https URL connections.

New instances of this class inherit the default static

SSLSocketFactory

set by

setDefaultSSLSocketFactory

. Calls to this method replace
this object's

SSLSocketFactory

.

New instances of this class inherit the default static

SSLSocketFactory

set by

setDefaultSSLSocketFactory

. Calls to this method replace
this object's

SSLSocketFactory

.

getSSLSocketFactory

```java
public
SSLSocketFactory
getSSLSocketFactory()
```

Gets the SSL socket factory to be used when creating sockets
for secure https URL connections.

**Returns:** the

SSLSocketFactory
**See Also:** setSSLSocketFactory(SSLSocketFactory)

---

#### getSSLSocketFactory

public

SSLSocketFactory

getSSLSocketFactory()

Gets the SSL socket factory to be used when creating sockets
for secure https URL connections.

---

