# Class ExtendedSSLSession

**Source:** `java.base\javax\net\ssl\ExtendedSSLSession.html`

### Class Description

```java
public abstract class
ExtendedSSLSession

extends
Object

implements
SSLSession
```

Extends the

SSLSession

interface to support additional
session attributes.

**All Implemented Interfaces:** SSLSession

---

### Field Details

*No entries found.*

### Constructor Details

#### public ExtendedSSLSession()

*No description found.*

---

### Method Details

#### public abstract
String
[] getLocalSupportedSignatureAlgorithms()

Obtains an array of supported signature algorithms that the local side
is willing to use.

Note: this method is used to indicate to the peer which signature
algorithms may be used for digital signatures in TLS/DTLS 1.2. It is
not meaningful for TLS/DTLS versions prior to 1.2.

The signature algorithm name must be a standard Java Security
name (such as "SHA1withRSA", "SHA256withECDSA", and so on).
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.

Note: the local supported signature algorithms should conform to
the algorithm constraints specified by

getAlgorithmConstraints()

method in

SSLParameters

.

**Returns:**
- An array of supported signature algorithms, in descending
order of preference. The return value is an empty array if
no signature algorithm is supported.

**See Also:**
- SSLParameters.getAlgorithmConstraints()

---

#### public abstract
String
[] getPeerSupportedSignatureAlgorithms()

Obtains an array of supported signature algorithms that the peer is
able to use.

Note: this method is used to indicate to the local side which signature
algorithms may be used for digital signatures in TLS/DTLS 1.2. It is
not meaningful for TLS/DTLS versions prior to 1.2.

The signature algorithm name must be a standard Java Security
name (such as "SHA1withRSA", "SHA256withECDSA", and so on).
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.

**Returns:**
- An array of supported signature algorithms, in descending
order of preference. The return value is an empty array if
the peer has not sent the supported signature algorithms.

**See Also:**
- X509KeyManager

,

X509ExtendedKeyManager

---

#### public
List
<
SNIServerName
> getRequestedServerNames()

Obtains a

List

containing all

SNIServerName

s
of the requested Server Name Indication (SNI) extension.

In server mode, unless the return

List

is empty,
the server should use the requested server names to guide its
selection of an appropriate authentication certificate, and/or
other aspects of security policy.

In client mode, unless the return

List

is empty,
the client should use the requested server names to guide its
endpoint identification of the peer's identity, and/or
other aspects of security policy.

**Returns:**
- a non-null immutable list of

SNIServerName

s of the
requested server name indications. The returned list may be
empty if no server name indications were requested.

**Throws:**
- UnsupportedOperationException

- if the underlying provider
does not implement the operation

**See Also:**
- SNIServerName

,

X509ExtendedTrustManager

,

X509ExtendedKeyManager

**Since:**
- 1.8

---

#### public
List
<byte[]> getStatusResponses()

Returns a

List

containing DER-encoded OCSP responses
(using the ASN.1 type OCSPResponse defined in RFC 6960) for
the client to verify status of the server's certificate during
handshaking.

This method only applies to certificate-based server
authentication. An

X509ExtendedTrustManager

will use the
returned value for server certificate validation.

**Returns:**
- a non-null unmodifiable list of byte arrays, each entry
containing a DER-encoded OCSP response (using the
ASN.1 type OCSPResponse defined in RFC 6960). The order
of the responses must match the order of the certificates
presented by the server in its Certificate message (See

SSLSession.getLocalCertificates()

for server mode,
and

SSLSession.getPeerCertificates()

for client mode).
It is possible that fewer response entries may be returned than
the number of presented certificates. If an entry in the list
is a zero-length byte array, it should be treated by the
caller as if the OCSP entry for the corresponding certificate
is missing. The returned list may be empty if no OCSP responses
were presented during handshaking or if OCSP stapling is not
supported by either endpoint for this handshake.

**Throws:**
- UnsupportedOperationException

- if the underlying provider
does not implement the operation

**See Also:**
- X509ExtendedTrustManager

**Since:**
- 9

**Implementation Requirements:**
- This method throws UnsupportedOperationException by default.
Classes derived from ExtendedSSLSession must implement
this method.

---

### Additional Sections

#### Class ExtendedSSLSession

java.lang.Object

- javax.net.ssl.ExtendedSSLSession

javax.net.ssl.ExtendedSSLSession

**All Implemented Interfaces:** SSLSession

```java
public abstract class
ExtendedSSLSession

extends
Object

implements
SSLSession
```

Extends the

SSLSession

interface to support additional
session attributes.

**Since:** 1.7

public abstract class

ExtendedSSLSession

extends

Object

implements

SSLSession

Extends the

SSLSession

interface to support additional
session attributes.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ExtendedSSLSession

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

String

[]

getLocalSupportedSignatureAlgorithms

()

Obtains an array of supported signature algorithms that the local side
is willing to use.

abstract

String

[]

getPeerSupportedSignatureAlgorithms

()

Obtains an array of supported signature algorithms that the peer is
able to use.

List

<

SNIServerName

>

getRequestedServerNames

()

Obtains a

List

containing all

SNIServerName

s
of the requested Server Name Indication (SNI) extension.

List

<byte[]>

getStatusResponses

()

Returns a

List

containing DER-encoded OCSP responses
(using the ASN.1 type OCSPResponse defined in RFC 6960) for
the client to verify status of the server's certificate during
handshaking.

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

- Methods declared in interface javax.net.ssl.

SSLSession

getApplicationBufferSize

,

getCipherSuite

,

getCreationTime

,

getId

,

getLastAccessedTime

,

getLocalCertificates

,

getLocalPrincipal

,

getPacketBufferSize

,

getPeerCertificateChain

,

getPeerCertificates

,

getPeerHost

,

getPeerPort

,

getPeerPrincipal

,

getProtocol

,

getSessionContext

,

getValue

,

getValueNames

,

invalidate

,

isValid

,

putValue

,

removeValue

Constructor Summary

Constructors

Constructor

Description

ExtendedSSLSession

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

String

[]

getLocalSupportedSignatureAlgorithms

()

Obtains an array of supported signature algorithms that the local side
is willing to use.

abstract

String

[]

getPeerSupportedSignatureAlgorithms

()

Obtains an array of supported signature algorithms that the peer is
able to use.

List

<

SNIServerName

>

getRequestedServerNames

()

Obtains a

List

containing all

SNIServerName

s
of the requested Server Name Indication (SNI) extension.

List

<byte[]>

getStatusResponses

()

Returns a

List

containing DER-encoded OCSP responses
(using the ASN.1 type OCSPResponse defined in RFC 6960) for
the client to verify status of the server's certificate during
handshaking.

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

- Methods declared in interface javax.net.ssl.

SSLSession

getApplicationBufferSize

,

getCipherSuite

,

getCreationTime

,

getId

,

getLastAccessedTime

,

getLocalCertificates

,

getLocalPrincipal

,

getPacketBufferSize

,

getPeerCertificateChain

,

getPeerCertificates

,

getPeerHost

,

getPeerPort

,

getPeerPrincipal

,

getProtocol

,

getSessionContext

,

getValue

,

getValueNames

,

invalidate

,

isValid

,

putValue

,

removeValue

---

#### Method Summary

Obtains an array of supported signature algorithms that the local side
is willing to use.

Obtains an array of supported signature algorithms that the peer is
able to use.

Obtains a

List

containing all

SNIServerName

s
of the requested Server Name Indication (SNI) extension.

Returns a

List

containing DER-encoded OCSP responses
(using the ASN.1 type OCSPResponse defined in RFC 6960) for
the client to verify status of the server's certificate during
handshaking.

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

Methods declared in interface javax.net.ssl.

SSLSession

getApplicationBufferSize

,

getCipherSuite

,

getCreationTime

,

getId

,

getLastAccessedTime

,

getLocalCertificates

,

getLocalPrincipal

,

getPacketBufferSize

,

getPeerCertificateChain

,

getPeerCertificates

,

getPeerHost

,

getPeerPort

,

getPeerPrincipal

,

getProtocol

,

getSessionContext

,

getValue

,

getValueNames

,

invalidate

,

isValid

,

putValue

,

removeValue

---

#### Methods declared in interface javax.net.ssl. SSLSession

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- ExtendedSSLSession

```java
public ExtendedSSLSession()
```

============ METHOD DETAIL ==========

- Method Detail

- getLocalSupportedSignatureAlgorithms

```java
public abstract
String
[] getLocalSupportedSignatureAlgorithms()
```

Obtains an array of supported signature algorithms that the local side
is willing to use.

Note: this method is used to indicate to the peer which signature
algorithms may be used for digital signatures in TLS/DTLS 1.2. It is
not meaningful for TLS/DTLS versions prior to 1.2.

The signature algorithm name must be a standard Java Security
name (such as "SHA1withRSA", "SHA256withECDSA", and so on).
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.

Note: the local supported signature algorithms should conform to
the algorithm constraints specified by

getAlgorithmConstraints()

method in

SSLParameters

.

**Returns:** An array of supported signature algorithms, in descending
order of preference. The return value is an empty array if
no signature algorithm is supported.
**See Also:** SSLParameters.getAlgorithmConstraints()

- getPeerSupportedSignatureAlgorithms

```java
public abstract
String
[] getPeerSupportedSignatureAlgorithms()
```

Obtains an array of supported signature algorithms that the peer is
able to use.

Note: this method is used to indicate to the local side which signature
algorithms may be used for digital signatures in TLS/DTLS 1.2. It is
not meaningful for TLS/DTLS versions prior to 1.2.

The signature algorithm name must be a standard Java Security
name (such as "SHA1withRSA", "SHA256withECDSA", and so on).
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.

**Returns:** An array of supported signature algorithms, in descending
order of preference. The return value is an empty array if
the peer has not sent the supported signature algorithms.
**See Also:** X509KeyManager

,

X509ExtendedKeyManager

- getRequestedServerNames

```java
public
List
<
SNIServerName
> getRequestedServerNames()
```

Obtains a

List

containing all

SNIServerName

s
of the requested Server Name Indication (SNI) extension.

In server mode, unless the return

List

is empty,
the server should use the requested server names to guide its
selection of an appropriate authentication certificate, and/or
other aspects of security policy.

In client mode, unless the return

List

is empty,
the client should use the requested server names to guide its
endpoint identification of the peer's identity, and/or
other aspects of security policy.

**Returns:** a non-null immutable list of

SNIServerName

s of the
requested server name indications. The returned list may be
empty if no server name indications were requested.
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation
**Since:** 1.8
**See Also:** SNIServerName

,

X509ExtendedTrustManager

,

X509ExtendedKeyManager

- getStatusResponses

```java
public
List
<byte[]> getStatusResponses()
```

Returns a

List

containing DER-encoded OCSP responses
(using the ASN.1 type OCSPResponse defined in RFC 6960) for
the client to verify status of the server's certificate during
handshaking.

This method only applies to certificate-based server
authentication. An

X509ExtendedTrustManager

will use the
returned value for server certificate validation.

**Implementation Requirements:** This method throws UnsupportedOperationException by default.
Classes derived from ExtendedSSLSession must implement
this method.
**Returns:** a non-null unmodifiable list of byte arrays, each entry
containing a DER-encoded OCSP response (using the
ASN.1 type OCSPResponse defined in RFC 6960). The order
of the responses must match the order of the certificates
presented by the server in its Certificate message (See

SSLSession.getLocalCertificates()

for server mode,
and

SSLSession.getPeerCertificates()

for client mode).
It is possible that fewer response entries may be returned than
the number of presented certificates. If an entry in the list
is a zero-length byte array, it should be treated by the
caller as if the OCSP entry for the corresponding certificate
is missing. The returned list may be empty if no OCSP responses
were presented during handshaking or if OCSP stapling is not
supported by either endpoint for this handshake.
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation
**Since:** 9
**See Also:** X509ExtendedTrustManager

Constructor Detail

- ExtendedSSLSession

```java
public ExtendedSSLSession()
```

---

#### Constructor Detail

ExtendedSSLSession

```java
public ExtendedSSLSession()
```

---

#### ExtendedSSLSession

public ExtendedSSLSession()

Method Detail

- getLocalSupportedSignatureAlgorithms

```java
public abstract
String
[] getLocalSupportedSignatureAlgorithms()
```

Obtains an array of supported signature algorithms that the local side
is willing to use.

Note: this method is used to indicate to the peer which signature
algorithms may be used for digital signatures in TLS/DTLS 1.2. It is
not meaningful for TLS/DTLS versions prior to 1.2.

The signature algorithm name must be a standard Java Security
name (such as "SHA1withRSA", "SHA256withECDSA", and so on).
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.

Note: the local supported signature algorithms should conform to
the algorithm constraints specified by

getAlgorithmConstraints()

method in

SSLParameters

.

**Returns:** An array of supported signature algorithms, in descending
order of preference. The return value is an empty array if
no signature algorithm is supported.
**See Also:** SSLParameters.getAlgorithmConstraints()

- getPeerSupportedSignatureAlgorithms

```java
public abstract
String
[] getPeerSupportedSignatureAlgorithms()
```

Obtains an array of supported signature algorithms that the peer is
able to use.

Note: this method is used to indicate to the local side which signature
algorithms may be used for digital signatures in TLS/DTLS 1.2. It is
not meaningful for TLS/DTLS versions prior to 1.2.

The signature algorithm name must be a standard Java Security
name (such as "SHA1withRSA", "SHA256withECDSA", and so on).
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.

**Returns:** An array of supported signature algorithms, in descending
order of preference. The return value is an empty array if
the peer has not sent the supported signature algorithms.
**See Also:** X509KeyManager

,

X509ExtendedKeyManager

- getRequestedServerNames

```java
public
List
<
SNIServerName
> getRequestedServerNames()
```

Obtains a

List

containing all

SNIServerName

s
of the requested Server Name Indication (SNI) extension.

In server mode, unless the return

List

is empty,
the server should use the requested server names to guide its
selection of an appropriate authentication certificate, and/or
other aspects of security policy.

In client mode, unless the return

List

is empty,
the client should use the requested server names to guide its
endpoint identification of the peer's identity, and/or
other aspects of security policy.

**Returns:** a non-null immutable list of

SNIServerName

s of the
requested server name indications. The returned list may be
empty if no server name indications were requested.
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation
**Since:** 1.8
**See Also:** SNIServerName

,

X509ExtendedTrustManager

,

X509ExtendedKeyManager

- getStatusResponses

```java
public
List
<byte[]> getStatusResponses()
```

Returns a

List

containing DER-encoded OCSP responses
(using the ASN.1 type OCSPResponse defined in RFC 6960) for
the client to verify status of the server's certificate during
handshaking.

This method only applies to certificate-based server
authentication. An

X509ExtendedTrustManager

will use the
returned value for server certificate validation.

**Implementation Requirements:** This method throws UnsupportedOperationException by default.
Classes derived from ExtendedSSLSession must implement
this method.
**Returns:** a non-null unmodifiable list of byte arrays, each entry
containing a DER-encoded OCSP response (using the
ASN.1 type OCSPResponse defined in RFC 6960). The order
of the responses must match the order of the certificates
presented by the server in its Certificate message (See

SSLSession.getLocalCertificates()

for server mode,
and

SSLSession.getPeerCertificates()

for client mode).
It is possible that fewer response entries may be returned than
the number of presented certificates. If an entry in the list
is a zero-length byte array, it should be treated by the
caller as if the OCSP entry for the corresponding certificate
is missing. The returned list may be empty if no OCSP responses
were presented during handshaking or if OCSP stapling is not
supported by either endpoint for this handshake.
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation
**Since:** 9
**See Also:** X509ExtendedTrustManager

---

#### Method Detail

getLocalSupportedSignatureAlgorithms

```java
public abstract
String
[] getLocalSupportedSignatureAlgorithms()
```

Obtains an array of supported signature algorithms that the local side
is willing to use.

Note: this method is used to indicate to the peer which signature
algorithms may be used for digital signatures in TLS/DTLS 1.2. It is
not meaningful for TLS/DTLS versions prior to 1.2.

The signature algorithm name must be a standard Java Security
name (such as "SHA1withRSA", "SHA256withECDSA", and so on).
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.

Note: the local supported signature algorithms should conform to
the algorithm constraints specified by

getAlgorithmConstraints()

method in

SSLParameters

.

**Returns:** An array of supported signature algorithms, in descending
order of preference. The return value is an empty array if
no signature algorithm is supported.
**See Also:** SSLParameters.getAlgorithmConstraints()

---

#### getLocalSupportedSignatureAlgorithms

public abstract

String

[] getLocalSupportedSignatureAlgorithms()

Obtains an array of supported signature algorithms that the local side
is willing to use.

Note: this method is used to indicate to the peer which signature
algorithms may be used for digital signatures in TLS/DTLS 1.2. It is
not meaningful for TLS/DTLS versions prior to 1.2.

The signature algorithm name must be a standard Java Security
name (such as "SHA1withRSA", "SHA256withECDSA", and so on).
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.

Note: the local supported signature algorithms should conform to
the algorithm constraints specified by

getAlgorithmConstraints()

method in

SSLParameters

.

Note: this method is used to indicate to the peer which signature
algorithms may be used for digital signatures in TLS/DTLS 1.2. It is
not meaningful for TLS/DTLS versions prior to 1.2.

The signature algorithm name must be a standard Java Security
name (such as "SHA1withRSA", "SHA256withECDSA", and so on).
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.

Note: the local supported signature algorithms should conform to
the algorithm constraints specified by

getAlgorithmConstraints()

method in

SSLParameters

.

The signature algorithm name must be a standard Java Security
name (such as "SHA1withRSA", "SHA256withECDSA", and so on).
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.

Note: the local supported signature algorithms should conform to
the algorithm constraints specified by

getAlgorithmConstraints()

method in

SSLParameters

.

Note: the local supported signature algorithms should conform to
the algorithm constraints specified by

getAlgorithmConstraints()

method in

SSLParameters

.

getPeerSupportedSignatureAlgorithms

```java
public abstract
String
[] getPeerSupportedSignatureAlgorithms()
```

Obtains an array of supported signature algorithms that the peer is
able to use.

Note: this method is used to indicate to the local side which signature
algorithms may be used for digital signatures in TLS/DTLS 1.2. It is
not meaningful for TLS/DTLS versions prior to 1.2.

The signature algorithm name must be a standard Java Security
name (such as "SHA1withRSA", "SHA256withECDSA", and so on).
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.

**Returns:** An array of supported signature algorithms, in descending
order of preference. The return value is an empty array if
the peer has not sent the supported signature algorithms.
**See Also:** X509KeyManager

,

X509ExtendedKeyManager

---

#### getPeerSupportedSignatureAlgorithms

public abstract

String

[] getPeerSupportedSignatureAlgorithms()

Obtains an array of supported signature algorithms that the peer is
able to use.

Note: this method is used to indicate to the local side which signature
algorithms may be used for digital signatures in TLS/DTLS 1.2. It is
not meaningful for TLS/DTLS versions prior to 1.2.

The signature algorithm name must be a standard Java Security
name (such as "SHA1withRSA", "SHA256withECDSA", and so on).
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.

Note: this method is used to indicate to the local side which signature
algorithms may be used for digital signatures in TLS/DTLS 1.2. It is
not meaningful for TLS/DTLS versions prior to 1.2.

The signature algorithm name must be a standard Java Security
name (such as "SHA1withRSA", "SHA256withECDSA", and so on).
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.

The signature algorithm name must be a standard Java Security
name (such as "SHA1withRSA", "SHA256withECDSA", and so on).
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.

getRequestedServerNames

```java
public
List
<
SNIServerName
> getRequestedServerNames()
```

Obtains a

List

containing all

SNIServerName

s
of the requested Server Name Indication (SNI) extension.

In server mode, unless the return

List

is empty,
the server should use the requested server names to guide its
selection of an appropriate authentication certificate, and/or
other aspects of security policy.

In client mode, unless the return

List

is empty,
the client should use the requested server names to guide its
endpoint identification of the peer's identity, and/or
other aspects of security policy.

**Returns:** a non-null immutable list of

SNIServerName

s of the
requested server name indications. The returned list may be
empty if no server name indications were requested.
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation
**Since:** 1.8
**See Also:** SNIServerName

,

X509ExtendedTrustManager

,

X509ExtendedKeyManager

---

#### getRequestedServerNames

public

List

<

SNIServerName

> getRequestedServerNames()

Obtains a

List

containing all

SNIServerName

s
of the requested Server Name Indication (SNI) extension.

In server mode, unless the return

List

is empty,
the server should use the requested server names to guide its
selection of an appropriate authentication certificate, and/or
other aspects of security policy.

In client mode, unless the return

List

is empty,
the client should use the requested server names to guide its
endpoint identification of the peer's identity, and/or
other aspects of security policy.

In server mode, unless the return

List

is empty,
the server should use the requested server names to guide its
selection of an appropriate authentication certificate, and/or
other aspects of security policy.

In client mode, unless the return

List

is empty,
the client should use the requested server names to guide its
endpoint identification of the peer's identity, and/or
other aspects of security policy.

In client mode, unless the return

List

is empty,
the client should use the requested server names to guide its
endpoint identification of the peer's identity, and/or
other aspects of security policy.

getStatusResponses

```java
public
List
<byte[]> getStatusResponses()
```

Returns a

List

containing DER-encoded OCSP responses
(using the ASN.1 type OCSPResponse defined in RFC 6960) for
the client to verify status of the server's certificate during
handshaking.

This method only applies to certificate-based server
authentication. An

X509ExtendedTrustManager

will use the
returned value for server certificate validation.

**Implementation Requirements:** This method throws UnsupportedOperationException by default.
Classes derived from ExtendedSSLSession must implement
this method.
**Returns:** a non-null unmodifiable list of byte arrays, each entry
containing a DER-encoded OCSP response (using the
ASN.1 type OCSPResponse defined in RFC 6960). The order
of the responses must match the order of the certificates
presented by the server in its Certificate message (See

SSLSession.getLocalCertificates()

for server mode,
and

SSLSession.getPeerCertificates()

for client mode).
It is possible that fewer response entries may be returned than
the number of presented certificates. If an entry in the list
is a zero-length byte array, it should be treated by the
caller as if the OCSP entry for the corresponding certificate
is missing. The returned list may be empty if no OCSP responses
were presented during handshaking or if OCSP stapling is not
supported by either endpoint for this handshake.
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation
**Since:** 9
**See Also:** X509ExtendedTrustManager

---

#### getStatusResponses

public

List

<byte[]> getStatusResponses()

Returns a

List

containing DER-encoded OCSP responses
(using the ASN.1 type OCSPResponse defined in RFC 6960) for
the client to verify status of the server's certificate during
handshaking.

This method only applies to certificate-based server
authentication. An

X509ExtendedTrustManager

will use the
returned value for server certificate validation.

This method only applies to certificate-based server
authentication. An

X509ExtendedTrustManager

will use the
returned value for server certificate validation.

---

