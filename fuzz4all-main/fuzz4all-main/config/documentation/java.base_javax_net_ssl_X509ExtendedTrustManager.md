# Class X509ExtendedTrustManager

**Source:** `java.base\javax\net\ssl\X509ExtendedTrustManager.html`

### Class Description

```java
public abstract class
X509ExtendedTrustManager

extends
Object

implements
X509TrustManager
```

Extensions to the

X509TrustManager

interface to support
SSL/TLS/DTLS connection sensitive trust management.

To prevent man-in-the-middle attacks, hostname checks can be done
to verify that the hostname in an end-entity certificate matches the
targeted hostname. TLS/DTLS does not require such checks, but some
protocols over TLS/DTLS (such as HTTPS) do. In earlier versions of the
JDK, the certificate chain checks were done at the SSL/TLS/DTLS layer,
and the hostname verification checks were done at the layer over TLS/DTLS.
This class allows for the checking to be done during a single call to
this class.

RFC 2830 defines the server identification specification for the "LDAPS"
algorithm. RFC 2818 defines both the server identification and the
client identification specification for the "HTTPS" algorithm.

**All Implemented Interfaces:** TrustManager

,

X509TrustManager

---

### Field Details

*No entries found.*

### Constructor Details

#### public X509ExtendedTrustManager()

*No description found.*

---

### Method Details

#### public abstract void checkClientTrusted​(
X509Certificate
[] chain,

String
authType,

Socket
socket)
throws
CertificateException

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

The authentication type is determined by the actual certificate
used. For instance, if RSAPublicKey is used, the authType
should be "RSA". Checking is case-sensitive.

If the

socket

parameter is an instance of

SSLSocket

, and the endpoint identification
algorithm of the

SSLParameters

is non-empty, to prevent
man-in-the-middle attacks, the address that the

socket

connected to should be checked against the peer's identity presented
in the end-entity X509 certificate, as specified in the endpoint
identification algorithm.

If the

socket

parameter is an instance of

SSLSocket

, and the algorithm constraints of the

SSLParameters

is non-null, for every certificate in the
certification path, fields such as subject public key, the signature
algorithm, key usage, extended key usage, etc. need to conform to the
algorithm constraints in place on this socket.

**Parameters:**
- chain

- the peer certificate chain
- authType

- the key exchange algorithm used
- socket

- the socket used for this connection. This parameter
can be null, which indicates that implementations need not check
the ssl parameters

**Throws:**
- IllegalArgumentException

- if null or zero-length array is passed
in for the

chain

parameter or if null or zero-length
string is passed in for the

authType

parameter
- CertificateException

- if the certificate chain is not trusted
by this TrustManager

**See Also:**
- SSLParameters.getEndpointIdentificationAlgorithm()

,

SSLParameters.setEndpointIdentificationAlgorithm(String)

,

SSLParameters.getAlgorithmConstraints()

,

SSLParameters.setAlgorithmConstraints(AlgorithmConstraints)

---

#### public abstract void checkServerTrusted​(
X509Certificate
[] chain,

String
authType,

Socket
socket)
throws
CertificateException

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

The authentication type is the key exchange algorithm portion
of the cipher suites represented as a String, such as "RSA",
"DHE_DSS". Note: for some exportable cipher suites, the key
exchange algorithm is determined at run time during the
handshake. For instance, for TLS_RSA_EXPORT_WITH_RC4_40_MD5,
the authType should be RSA_EXPORT when an ephemeral RSA key is
used for the key exchange, and RSA when the key from the server
certificate is used. Checking is case-sensitive.

If the

socket

parameter is an instance of

SSLSocket

, and the endpoint identification
algorithm of the

SSLParameters

is non-empty, to prevent
man-in-the-middle attacks, the address that the

socket

connected to should be checked against the peer's identity presented
in the end-entity X509 certificate, as specified in the endpoint
identification algorithm.

If the

socket

parameter is an instance of

SSLSocket

, and the algorithm constraints of the

SSLParameters

is non-null, for every certificate in the
certification path, fields such as subject public key, the signature
algorithm, key usage, extended key usage, etc. need to conform to the
algorithm constraints in place on this socket.

**Parameters:**
- chain

- the peer certificate chain
- authType

- the key exchange algorithm used
- socket

- the socket used for this connection. This parameter
can be null, which indicates that implementations need not check
the ssl parameters

**Throws:**
- IllegalArgumentException

- if null or zero-length array is passed
in for the

chain

parameter or if null or zero-length
string is passed in for the

authType

parameter
- CertificateException

- if the certificate chain is not trusted
by this TrustManager

**See Also:**
- SSLParameters.getEndpointIdentificationAlgorithm()

,

SSLParameters.setEndpointIdentificationAlgorithm(String)

,

SSLParameters.getAlgorithmConstraints()

,

SSLParameters.setAlgorithmConstraints(AlgorithmConstraints)

---

#### public abstract void checkClientTrusted​(
X509Certificate
[] chain,

String
authType,

SSLEngine
engine)
throws
CertificateException

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

The authentication type is determined by the actual certificate
used. For instance, if RSAPublicKey is used, the authType
should be "RSA". Checking is case-sensitive.

If the

engine

parameter is available, and the endpoint
identification algorithm of the

SSLParameters

is
non-empty, to prevent man-in-the-middle attacks, the address that
the

engine

connected to should be checked against
the peer's identity presented in the end-entity X509 certificate,
as specified in the endpoint identification algorithm.

If the

engine

parameter is available, and the algorithm
constraints of the

SSLParameters

is non-null, for every
certificate in the certification path, fields such as subject public
key, the signature algorithm, key usage, extended key usage, etc.
need to conform to the algorithm constraints in place on this engine.

**Parameters:**
- chain

- the peer certificate chain
- authType

- the key exchange algorithm used
- engine

- the engine used for this connection. This parameter
can be null, which indicates that implementations need not check
the ssl parameters

**Throws:**
- IllegalArgumentException

- if null or zero-length array is passed
in for the

chain

parameter or if null or zero-length
string is passed in for the

authType

parameter
- CertificateException

- if the certificate chain is not trusted
by this TrustManager

**See Also:**
- SSLParameters.getEndpointIdentificationAlgorithm()

,

SSLParameters.setEndpointIdentificationAlgorithm(String)

,

SSLParameters.getAlgorithmConstraints()

,

SSLParameters.setAlgorithmConstraints(AlgorithmConstraints)

---

#### public abstract void checkServerTrusted​(
X509Certificate
[] chain,

String
authType,

SSLEngine
engine)
throws
CertificateException

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

The authentication type is the key exchange algorithm portion
of the cipher suites represented as a String, such as "RSA",
"DHE_DSS". Note: for some exportable cipher suites, the key
exchange algorithm is determined at run time during the
handshake. For instance, for TLS_RSA_EXPORT_WITH_RC4_40_MD5,
the authType should be RSA_EXPORT when an ephemeral RSA key is
used for the key exchange, and RSA when the key from the server
certificate is used. Checking is case-sensitive.

If the

engine

parameter is available, and the endpoint
identification algorithm of the

SSLParameters

is
non-empty, to prevent man-in-the-middle attacks, the address that
the

engine

connected to should be checked against
the peer's identity presented in the end-entity X509 certificate,
as specified in the endpoint identification algorithm.

If the

engine

parameter is available, and the algorithm
constraints of the

SSLParameters

is non-null, for every
certificate in the certification path, fields such as subject public
key, the signature algorithm, key usage, extended key usage, etc.
need to conform to the algorithm constraints in place on this engine.

**Parameters:**
- chain

- the peer certificate chain
- authType

- the key exchange algorithm used
- engine

- the engine used for this connection. This parameter
can be null, which indicates that implementations need not check
the ssl parameters

**Throws:**
- IllegalArgumentException

- if null or zero-length array is passed
in for the

chain

parameter or if null or zero-length
string is passed in for the

authType

parameter
- CertificateException

- if the certificate chain is not trusted
by this TrustManager

**See Also:**
- SSLParameters.getEndpointIdentificationAlgorithm()

,

SSLParameters.setEndpointIdentificationAlgorithm(String)

,

SSLParameters.getAlgorithmConstraints()

,

SSLParameters.setAlgorithmConstraints(AlgorithmConstraints)

---

### Additional Sections

#### Class X509ExtendedTrustManager

java.lang.Object

- javax.net.ssl.X509ExtendedTrustManager

javax.net.ssl.X509ExtendedTrustManager

**All Implemented Interfaces:** TrustManager

,

X509TrustManager

```java
public abstract class
X509ExtendedTrustManager

extends
Object

implements
X509TrustManager
```

Extensions to the

X509TrustManager

interface to support
SSL/TLS/DTLS connection sensitive trust management.

To prevent man-in-the-middle attacks, hostname checks can be done
to verify that the hostname in an end-entity certificate matches the
targeted hostname. TLS/DTLS does not require such checks, but some
protocols over TLS/DTLS (such as HTTPS) do. In earlier versions of the
JDK, the certificate chain checks were done at the SSL/TLS/DTLS layer,
and the hostname verification checks were done at the layer over TLS/DTLS.
This class allows for the checking to be done during a single call to
this class.

RFC 2830 defines the server identification specification for the "LDAPS"
algorithm. RFC 2818 defines both the server identification and the
client identification specification for the "HTTPS" algorithm.

**Since:** 1.7
**See Also:** X509TrustManager

,

HostnameVerifier

public abstract class

X509ExtendedTrustManager

extends

Object

implements

X509TrustManager

Extensions to the

X509TrustManager

interface to support
SSL/TLS/DTLS connection sensitive trust management.

To prevent man-in-the-middle attacks, hostname checks can be done
to verify that the hostname in an end-entity certificate matches the
targeted hostname. TLS/DTLS does not require such checks, but some
protocols over TLS/DTLS (such as HTTPS) do. In earlier versions of the
JDK, the certificate chain checks were done at the SSL/TLS/DTLS layer,
and the hostname verification checks were done at the layer over TLS/DTLS.
This class allows for the checking to be done during a single call to
this class.

RFC 2830 defines the server identification specification for the "LDAPS"
algorithm. RFC 2818 defines both the server identification and the
client identification specification for the "HTTPS" algorithm.

To prevent man-in-the-middle attacks, hostname checks can be done
to verify that the hostname in an end-entity certificate matches the
targeted hostname. TLS/DTLS does not require such checks, but some
protocols over TLS/DTLS (such as HTTPS) do. In earlier versions of the
JDK, the certificate chain checks were done at the SSL/TLS/DTLS layer,
and the hostname verification checks were done at the layer over TLS/DTLS.
This class allows for the checking to be done during a single call to
this class.

RFC 2830 defines the server identification specification for the "LDAPS"
algorithm. RFC 2818 defines both the server identification and the
client identification specification for the "HTTPS" algorithm.

RFC 2830 defines the server identification specification for the "LDAPS"
algorithm. RFC 2818 defines both the server identification and the
client identification specification for the "HTTPS" algorithm.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

X509ExtendedTrustManager

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract void

checkClientTrusted

​(

X509Certificate

[] chain,

String

authType,

Socket

socket)

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

abstract void

checkClientTrusted

​(

X509Certificate

[] chain,

String

authType,

SSLEngine

engine)

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

abstract void

checkServerTrusted

​(

X509Certificate

[] chain,

String

authType,

Socket

socket)

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

abstract void

checkServerTrusted

​(

X509Certificate

[] chain,

String

authType,

SSLEngine

engine)

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

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

X509TrustManager

checkClientTrusted

,

checkServerTrusted

,

getAcceptedIssuers

Constructor Summary

Constructors

Constructor

Description

X509ExtendedTrustManager

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

abstract void

checkClientTrusted

​(

X509Certificate

[] chain,

String

authType,

Socket

socket)

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

abstract void

checkClientTrusted

​(

X509Certificate

[] chain,

String

authType,

SSLEngine

engine)

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

abstract void

checkServerTrusted

​(

X509Certificate

[] chain,

String

authType,

Socket

socket)

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

abstract void

checkServerTrusted

​(

X509Certificate

[] chain,

String

authType,

SSLEngine

engine)

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

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

X509TrustManager

checkClientTrusted

,

checkServerTrusted

,

getAcceptedIssuers

---

#### Method Summary

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

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

X509TrustManager

checkClientTrusted

,

checkServerTrusted

,

getAcceptedIssuers

---

#### Methods declared in interface javax.net.ssl. X509TrustManager

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- X509ExtendedTrustManager

```java
public X509ExtendedTrustManager()
```

============ METHOD DETAIL ==========

- Method Detail

- checkClientTrusted

```java
public abstract void checkClientTrusted​(
X509Certificate
[] chain,

String
authType,

Socket
socket)
throws
CertificateException
```

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

The authentication type is determined by the actual certificate
used. For instance, if RSAPublicKey is used, the authType
should be "RSA". Checking is case-sensitive.

If the

socket

parameter is an instance of

SSLSocket

, and the endpoint identification
algorithm of the

SSLParameters

is non-empty, to prevent
man-in-the-middle attacks, the address that the

socket

connected to should be checked against the peer's identity presented
in the end-entity X509 certificate, as specified in the endpoint
identification algorithm.

If the

socket

parameter is an instance of

SSLSocket

, and the algorithm constraints of the

SSLParameters

is non-null, for every certificate in the
certification path, fields such as subject public key, the signature
algorithm, key usage, extended key usage, etc. need to conform to the
algorithm constraints in place on this socket.

**Parameters:** chain

- the peer certificate chain
**Parameters:** authType

- the key exchange algorithm used
**Parameters:** socket

- the socket used for this connection. This parameter
can be null, which indicates that implementations need not check
the ssl parameters
**Throws:** IllegalArgumentException

- if null or zero-length array is passed
in for the

chain

parameter or if null or zero-length
string is passed in for the

authType

parameter
**Throws:** CertificateException

- if the certificate chain is not trusted
by this TrustManager
**See Also:** SSLParameters.getEndpointIdentificationAlgorithm()

,

SSLParameters.setEndpointIdentificationAlgorithm(String)

,

SSLParameters.getAlgorithmConstraints()

,

SSLParameters.setAlgorithmConstraints(AlgorithmConstraints)

- checkServerTrusted

```java
public abstract void checkServerTrusted​(
X509Certificate
[] chain,

String
authType,

Socket
socket)
throws
CertificateException
```

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

The authentication type is the key exchange algorithm portion
of the cipher suites represented as a String, such as "RSA",
"DHE_DSS". Note: for some exportable cipher suites, the key
exchange algorithm is determined at run time during the
handshake. For instance, for TLS_RSA_EXPORT_WITH_RC4_40_MD5,
the authType should be RSA_EXPORT when an ephemeral RSA key is
used for the key exchange, and RSA when the key from the server
certificate is used. Checking is case-sensitive.

If the

socket

parameter is an instance of

SSLSocket

, and the endpoint identification
algorithm of the

SSLParameters

is non-empty, to prevent
man-in-the-middle attacks, the address that the

socket

connected to should be checked against the peer's identity presented
in the end-entity X509 certificate, as specified in the endpoint
identification algorithm.

If the

socket

parameter is an instance of

SSLSocket

, and the algorithm constraints of the

SSLParameters

is non-null, for every certificate in the
certification path, fields such as subject public key, the signature
algorithm, key usage, extended key usage, etc. need to conform to the
algorithm constraints in place on this socket.

**Parameters:** chain

- the peer certificate chain
**Parameters:** authType

- the key exchange algorithm used
**Parameters:** socket

- the socket used for this connection. This parameter
can be null, which indicates that implementations need not check
the ssl parameters
**Throws:** IllegalArgumentException

- if null or zero-length array is passed
in for the

chain

parameter or if null or zero-length
string is passed in for the

authType

parameter
**Throws:** CertificateException

- if the certificate chain is not trusted
by this TrustManager
**See Also:** SSLParameters.getEndpointIdentificationAlgorithm()

,

SSLParameters.setEndpointIdentificationAlgorithm(String)

,

SSLParameters.getAlgorithmConstraints()

,

SSLParameters.setAlgorithmConstraints(AlgorithmConstraints)

- checkClientTrusted

```java
public abstract void checkClientTrusted​(
X509Certificate
[] chain,

String
authType,

SSLEngine
engine)
throws
CertificateException
```

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

The authentication type is determined by the actual certificate
used. For instance, if RSAPublicKey is used, the authType
should be "RSA". Checking is case-sensitive.

If the

engine

parameter is available, and the endpoint
identification algorithm of the

SSLParameters

is
non-empty, to prevent man-in-the-middle attacks, the address that
the

engine

connected to should be checked against
the peer's identity presented in the end-entity X509 certificate,
as specified in the endpoint identification algorithm.

If the

engine

parameter is available, and the algorithm
constraints of the

SSLParameters

is non-null, for every
certificate in the certification path, fields such as subject public
key, the signature algorithm, key usage, extended key usage, etc.
need to conform to the algorithm constraints in place on this engine.

**Parameters:** chain

- the peer certificate chain
**Parameters:** authType

- the key exchange algorithm used
**Parameters:** engine

- the engine used for this connection. This parameter
can be null, which indicates that implementations need not check
the ssl parameters
**Throws:** IllegalArgumentException

- if null or zero-length array is passed
in for the

chain

parameter or if null or zero-length
string is passed in for the

authType

parameter
**Throws:** CertificateException

- if the certificate chain is not trusted
by this TrustManager
**See Also:** SSLParameters.getEndpointIdentificationAlgorithm()

,

SSLParameters.setEndpointIdentificationAlgorithm(String)

,

SSLParameters.getAlgorithmConstraints()

,

SSLParameters.setAlgorithmConstraints(AlgorithmConstraints)

- checkServerTrusted

```java
public abstract void checkServerTrusted​(
X509Certificate
[] chain,

String
authType,

SSLEngine
engine)
throws
CertificateException
```

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

The authentication type is the key exchange algorithm portion
of the cipher suites represented as a String, such as "RSA",
"DHE_DSS". Note: for some exportable cipher suites, the key
exchange algorithm is determined at run time during the
handshake. For instance, for TLS_RSA_EXPORT_WITH_RC4_40_MD5,
the authType should be RSA_EXPORT when an ephemeral RSA key is
used for the key exchange, and RSA when the key from the server
certificate is used. Checking is case-sensitive.

If the

engine

parameter is available, and the endpoint
identification algorithm of the

SSLParameters

is
non-empty, to prevent man-in-the-middle attacks, the address that
the

engine

connected to should be checked against
the peer's identity presented in the end-entity X509 certificate,
as specified in the endpoint identification algorithm.

If the

engine

parameter is available, and the algorithm
constraints of the

SSLParameters

is non-null, for every
certificate in the certification path, fields such as subject public
key, the signature algorithm, key usage, extended key usage, etc.
need to conform to the algorithm constraints in place on this engine.

**Parameters:** chain

- the peer certificate chain
**Parameters:** authType

- the key exchange algorithm used
**Parameters:** engine

- the engine used for this connection. This parameter
can be null, which indicates that implementations need not check
the ssl parameters
**Throws:** IllegalArgumentException

- if null or zero-length array is passed
in for the

chain

parameter or if null or zero-length
string is passed in for the

authType

parameter
**Throws:** CertificateException

- if the certificate chain is not trusted
by this TrustManager
**See Also:** SSLParameters.getEndpointIdentificationAlgorithm()

,

SSLParameters.setEndpointIdentificationAlgorithm(String)

,

SSLParameters.getAlgorithmConstraints()

,

SSLParameters.setAlgorithmConstraints(AlgorithmConstraints)

Constructor Detail

- X509ExtendedTrustManager

```java
public X509ExtendedTrustManager()
```

---

#### Constructor Detail

X509ExtendedTrustManager

```java
public X509ExtendedTrustManager()
```

---

#### X509ExtendedTrustManager

public X509ExtendedTrustManager()

Method Detail

- checkClientTrusted

```java
public abstract void checkClientTrusted​(
X509Certificate
[] chain,

String
authType,

Socket
socket)
throws
CertificateException
```

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

The authentication type is determined by the actual certificate
used. For instance, if RSAPublicKey is used, the authType
should be "RSA". Checking is case-sensitive.

If the

socket

parameter is an instance of

SSLSocket

, and the endpoint identification
algorithm of the

SSLParameters

is non-empty, to prevent
man-in-the-middle attacks, the address that the

socket

connected to should be checked against the peer's identity presented
in the end-entity X509 certificate, as specified in the endpoint
identification algorithm.

If the

socket

parameter is an instance of

SSLSocket

, and the algorithm constraints of the

SSLParameters

is non-null, for every certificate in the
certification path, fields such as subject public key, the signature
algorithm, key usage, extended key usage, etc. need to conform to the
algorithm constraints in place on this socket.

**Parameters:** chain

- the peer certificate chain
**Parameters:** authType

- the key exchange algorithm used
**Parameters:** socket

- the socket used for this connection. This parameter
can be null, which indicates that implementations need not check
the ssl parameters
**Throws:** IllegalArgumentException

- if null or zero-length array is passed
in for the

chain

parameter or if null or zero-length
string is passed in for the

authType

parameter
**Throws:** CertificateException

- if the certificate chain is not trusted
by this TrustManager
**See Also:** SSLParameters.getEndpointIdentificationAlgorithm()

,

SSLParameters.setEndpointIdentificationAlgorithm(String)

,

SSLParameters.getAlgorithmConstraints()

,

SSLParameters.setAlgorithmConstraints(AlgorithmConstraints)

- checkServerTrusted

```java
public abstract void checkServerTrusted​(
X509Certificate
[] chain,

String
authType,

Socket
socket)
throws
CertificateException
```

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

The authentication type is the key exchange algorithm portion
of the cipher suites represented as a String, such as "RSA",
"DHE_DSS". Note: for some exportable cipher suites, the key
exchange algorithm is determined at run time during the
handshake. For instance, for TLS_RSA_EXPORT_WITH_RC4_40_MD5,
the authType should be RSA_EXPORT when an ephemeral RSA key is
used for the key exchange, and RSA when the key from the server
certificate is used. Checking is case-sensitive.

If the

socket

parameter is an instance of

SSLSocket

, and the endpoint identification
algorithm of the

SSLParameters

is non-empty, to prevent
man-in-the-middle attacks, the address that the

socket

connected to should be checked against the peer's identity presented
in the end-entity X509 certificate, as specified in the endpoint
identification algorithm.

If the

socket

parameter is an instance of

SSLSocket

, and the algorithm constraints of the

SSLParameters

is non-null, for every certificate in the
certification path, fields such as subject public key, the signature
algorithm, key usage, extended key usage, etc. need to conform to the
algorithm constraints in place on this socket.

**Parameters:** chain

- the peer certificate chain
**Parameters:** authType

- the key exchange algorithm used
**Parameters:** socket

- the socket used for this connection. This parameter
can be null, which indicates that implementations need not check
the ssl parameters
**Throws:** IllegalArgumentException

- if null or zero-length array is passed
in for the

chain

parameter or if null or zero-length
string is passed in for the

authType

parameter
**Throws:** CertificateException

- if the certificate chain is not trusted
by this TrustManager
**See Also:** SSLParameters.getEndpointIdentificationAlgorithm()

,

SSLParameters.setEndpointIdentificationAlgorithm(String)

,

SSLParameters.getAlgorithmConstraints()

,

SSLParameters.setAlgorithmConstraints(AlgorithmConstraints)

- checkClientTrusted

```java
public abstract void checkClientTrusted​(
X509Certificate
[] chain,

String
authType,

SSLEngine
engine)
throws
CertificateException
```

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

The authentication type is determined by the actual certificate
used. For instance, if RSAPublicKey is used, the authType
should be "RSA". Checking is case-sensitive.

If the

engine

parameter is available, and the endpoint
identification algorithm of the

SSLParameters

is
non-empty, to prevent man-in-the-middle attacks, the address that
the

engine

connected to should be checked against
the peer's identity presented in the end-entity X509 certificate,
as specified in the endpoint identification algorithm.

If the

engine

parameter is available, and the algorithm
constraints of the

SSLParameters

is non-null, for every
certificate in the certification path, fields such as subject public
key, the signature algorithm, key usage, extended key usage, etc.
need to conform to the algorithm constraints in place on this engine.

**Parameters:** chain

- the peer certificate chain
**Parameters:** authType

- the key exchange algorithm used
**Parameters:** engine

- the engine used for this connection. This parameter
can be null, which indicates that implementations need not check
the ssl parameters
**Throws:** IllegalArgumentException

- if null or zero-length array is passed
in for the

chain

parameter or if null or zero-length
string is passed in for the

authType

parameter
**Throws:** CertificateException

- if the certificate chain is not trusted
by this TrustManager
**See Also:** SSLParameters.getEndpointIdentificationAlgorithm()

,

SSLParameters.setEndpointIdentificationAlgorithm(String)

,

SSLParameters.getAlgorithmConstraints()

,

SSLParameters.setAlgorithmConstraints(AlgorithmConstraints)

- checkServerTrusted

```java
public abstract void checkServerTrusted​(
X509Certificate
[] chain,

String
authType,

SSLEngine
engine)
throws
CertificateException
```

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

The authentication type is the key exchange algorithm portion
of the cipher suites represented as a String, such as "RSA",
"DHE_DSS". Note: for some exportable cipher suites, the key
exchange algorithm is determined at run time during the
handshake. For instance, for TLS_RSA_EXPORT_WITH_RC4_40_MD5,
the authType should be RSA_EXPORT when an ephemeral RSA key is
used for the key exchange, and RSA when the key from the server
certificate is used. Checking is case-sensitive.

If the

engine

parameter is available, and the endpoint
identification algorithm of the

SSLParameters

is
non-empty, to prevent man-in-the-middle attacks, the address that
the

engine

connected to should be checked against
the peer's identity presented in the end-entity X509 certificate,
as specified in the endpoint identification algorithm.

If the

engine

parameter is available, and the algorithm
constraints of the

SSLParameters

is non-null, for every
certificate in the certification path, fields such as subject public
key, the signature algorithm, key usage, extended key usage, etc.
need to conform to the algorithm constraints in place on this engine.

**Parameters:** chain

- the peer certificate chain
**Parameters:** authType

- the key exchange algorithm used
**Parameters:** engine

- the engine used for this connection. This parameter
can be null, which indicates that implementations need not check
the ssl parameters
**Throws:** IllegalArgumentException

- if null or zero-length array is passed
in for the

chain

parameter or if null or zero-length
string is passed in for the

authType

parameter
**Throws:** CertificateException

- if the certificate chain is not trusted
by this TrustManager
**See Also:** SSLParameters.getEndpointIdentificationAlgorithm()

,

SSLParameters.setEndpointIdentificationAlgorithm(String)

,

SSLParameters.getAlgorithmConstraints()

,

SSLParameters.setAlgorithmConstraints(AlgorithmConstraints)

---

#### Method Detail

checkClientTrusted

```java
public abstract void checkClientTrusted​(
X509Certificate
[] chain,

String
authType,

Socket
socket)
throws
CertificateException
```

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

The authentication type is determined by the actual certificate
used. For instance, if RSAPublicKey is used, the authType
should be "RSA". Checking is case-sensitive.

If the

socket

parameter is an instance of

SSLSocket

, and the endpoint identification
algorithm of the

SSLParameters

is non-empty, to prevent
man-in-the-middle attacks, the address that the

socket

connected to should be checked against the peer's identity presented
in the end-entity X509 certificate, as specified in the endpoint
identification algorithm.

If the

socket

parameter is an instance of

SSLSocket

, and the algorithm constraints of the

SSLParameters

is non-null, for every certificate in the
certification path, fields such as subject public key, the signature
algorithm, key usage, extended key usage, etc. need to conform to the
algorithm constraints in place on this socket.

**Parameters:** chain

- the peer certificate chain
**Parameters:** authType

- the key exchange algorithm used
**Parameters:** socket

- the socket used for this connection. This parameter
can be null, which indicates that implementations need not check
the ssl parameters
**Throws:** IllegalArgumentException

- if null or zero-length array is passed
in for the

chain

parameter or if null or zero-length
string is passed in for the

authType

parameter
**Throws:** CertificateException

- if the certificate chain is not trusted
by this TrustManager
**See Also:** SSLParameters.getEndpointIdentificationAlgorithm()

,

SSLParameters.setEndpointIdentificationAlgorithm(String)

,

SSLParameters.getAlgorithmConstraints()

,

SSLParameters.setAlgorithmConstraints(AlgorithmConstraints)

---

#### checkClientTrusted

public abstract void checkClientTrusted​(

X509Certificate

[] chain,

String

authType,

Socket

socket)
throws

CertificateException

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

The authentication type is determined by the actual certificate
used. For instance, if RSAPublicKey is used, the authType
should be "RSA". Checking is case-sensitive.

If the

socket

parameter is an instance of

SSLSocket

, and the endpoint identification
algorithm of the

SSLParameters

is non-empty, to prevent
man-in-the-middle attacks, the address that the

socket

connected to should be checked against the peer's identity presented
in the end-entity X509 certificate, as specified in the endpoint
identification algorithm.

If the

socket

parameter is an instance of

SSLSocket

, and the algorithm constraints of the

SSLParameters

is non-null, for every certificate in the
certification path, fields such as subject public key, the signature
algorithm, key usage, extended key usage, etc. need to conform to the
algorithm constraints in place on this socket.

The authentication type is determined by the actual certificate
used. For instance, if RSAPublicKey is used, the authType
should be "RSA". Checking is case-sensitive.

If the

socket

parameter is an instance of

SSLSocket

, and the endpoint identification
algorithm of the

SSLParameters

is non-empty, to prevent
man-in-the-middle attacks, the address that the

socket

connected to should be checked against the peer's identity presented
in the end-entity X509 certificate, as specified in the endpoint
identification algorithm.

If the

socket

parameter is an instance of

SSLSocket

, and the algorithm constraints of the

SSLParameters

is non-null, for every certificate in the
certification path, fields such as subject public key, the signature
algorithm, key usage, extended key usage, etc. need to conform to the
algorithm constraints in place on this socket.

If the

socket

parameter is an instance of

SSLSocket

, and the endpoint identification
algorithm of the

SSLParameters

is non-empty, to prevent
man-in-the-middle attacks, the address that the

socket

connected to should be checked against the peer's identity presented
in the end-entity X509 certificate, as specified in the endpoint
identification algorithm.

If the

socket

parameter is an instance of

SSLSocket

, and the algorithm constraints of the

SSLParameters

is non-null, for every certificate in the
certification path, fields such as subject public key, the signature
algorithm, key usage, extended key usage, etc. need to conform to the
algorithm constraints in place on this socket.

If the

socket

parameter is an instance of

SSLSocket

, and the algorithm constraints of the

SSLParameters

is non-null, for every certificate in the
certification path, fields such as subject public key, the signature
algorithm, key usage, extended key usage, etc. need to conform to the
algorithm constraints in place on this socket.

checkServerTrusted

```java
public abstract void checkServerTrusted​(
X509Certificate
[] chain,

String
authType,

Socket
socket)
throws
CertificateException
```

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

The authentication type is the key exchange algorithm portion
of the cipher suites represented as a String, such as "RSA",
"DHE_DSS". Note: for some exportable cipher suites, the key
exchange algorithm is determined at run time during the
handshake. For instance, for TLS_RSA_EXPORT_WITH_RC4_40_MD5,
the authType should be RSA_EXPORT when an ephemeral RSA key is
used for the key exchange, and RSA when the key from the server
certificate is used. Checking is case-sensitive.

If the

socket

parameter is an instance of

SSLSocket

, and the endpoint identification
algorithm of the

SSLParameters

is non-empty, to prevent
man-in-the-middle attacks, the address that the

socket

connected to should be checked against the peer's identity presented
in the end-entity X509 certificate, as specified in the endpoint
identification algorithm.

If the

socket

parameter is an instance of

SSLSocket

, and the algorithm constraints of the

SSLParameters

is non-null, for every certificate in the
certification path, fields such as subject public key, the signature
algorithm, key usage, extended key usage, etc. need to conform to the
algorithm constraints in place on this socket.

**Parameters:** chain

- the peer certificate chain
**Parameters:** authType

- the key exchange algorithm used
**Parameters:** socket

- the socket used for this connection. This parameter
can be null, which indicates that implementations need not check
the ssl parameters
**Throws:** IllegalArgumentException

- if null or zero-length array is passed
in for the

chain

parameter or if null or zero-length
string is passed in for the

authType

parameter
**Throws:** CertificateException

- if the certificate chain is not trusted
by this TrustManager
**See Also:** SSLParameters.getEndpointIdentificationAlgorithm()

,

SSLParameters.setEndpointIdentificationAlgorithm(String)

,

SSLParameters.getAlgorithmConstraints()

,

SSLParameters.setAlgorithmConstraints(AlgorithmConstraints)

---

#### checkServerTrusted

public abstract void checkServerTrusted​(

X509Certificate

[] chain,

String

authType,

Socket

socket)
throws

CertificateException

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

The authentication type is the key exchange algorithm portion
of the cipher suites represented as a String, such as "RSA",
"DHE_DSS". Note: for some exportable cipher suites, the key
exchange algorithm is determined at run time during the
handshake. For instance, for TLS_RSA_EXPORT_WITH_RC4_40_MD5,
the authType should be RSA_EXPORT when an ephemeral RSA key is
used for the key exchange, and RSA when the key from the server
certificate is used. Checking is case-sensitive.

If the

socket

parameter is an instance of

SSLSocket

, and the endpoint identification
algorithm of the

SSLParameters

is non-empty, to prevent
man-in-the-middle attacks, the address that the

socket

connected to should be checked against the peer's identity presented
in the end-entity X509 certificate, as specified in the endpoint
identification algorithm.

If the

socket

parameter is an instance of

SSLSocket

, and the algorithm constraints of the

SSLParameters

is non-null, for every certificate in the
certification path, fields such as subject public key, the signature
algorithm, key usage, extended key usage, etc. need to conform to the
algorithm constraints in place on this socket.

The authentication type is the key exchange algorithm portion
of the cipher suites represented as a String, such as "RSA",
"DHE_DSS". Note: for some exportable cipher suites, the key
exchange algorithm is determined at run time during the
handshake. For instance, for TLS_RSA_EXPORT_WITH_RC4_40_MD5,
the authType should be RSA_EXPORT when an ephemeral RSA key is
used for the key exchange, and RSA when the key from the server
certificate is used. Checking is case-sensitive.

If the

socket

parameter is an instance of

SSLSocket

, and the endpoint identification
algorithm of the

SSLParameters

is non-empty, to prevent
man-in-the-middle attacks, the address that the

socket

connected to should be checked against the peer's identity presented
in the end-entity X509 certificate, as specified in the endpoint
identification algorithm.

If the

socket

parameter is an instance of

SSLSocket

, and the algorithm constraints of the

SSLParameters

is non-null, for every certificate in the
certification path, fields such as subject public key, the signature
algorithm, key usage, extended key usage, etc. need to conform to the
algorithm constraints in place on this socket.

If the

socket

parameter is an instance of

SSLSocket

, and the endpoint identification
algorithm of the

SSLParameters

is non-empty, to prevent
man-in-the-middle attacks, the address that the

socket

connected to should be checked against the peer's identity presented
in the end-entity X509 certificate, as specified in the endpoint
identification algorithm.

If the

socket

parameter is an instance of

SSLSocket

, and the algorithm constraints of the

SSLParameters

is non-null, for every certificate in the
certification path, fields such as subject public key, the signature
algorithm, key usage, extended key usage, etc. need to conform to the
algorithm constraints in place on this socket.

If the

socket

parameter is an instance of

SSLSocket

, and the algorithm constraints of the

SSLParameters

is non-null, for every certificate in the
certification path, fields such as subject public key, the signature
algorithm, key usage, extended key usage, etc. need to conform to the
algorithm constraints in place on this socket.

checkClientTrusted

```java
public abstract void checkClientTrusted​(
X509Certificate
[] chain,

String
authType,

SSLEngine
engine)
throws
CertificateException
```

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

The authentication type is determined by the actual certificate
used. For instance, if RSAPublicKey is used, the authType
should be "RSA". Checking is case-sensitive.

If the

engine

parameter is available, and the endpoint
identification algorithm of the

SSLParameters

is
non-empty, to prevent man-in-the-middle attacks, the address that
the

engine

connected to should be checked against
the peer's identity presented in the end-entity X509 certificate,
as specified in the endpoint identification algorithm.

If the

engine

parameter is available, and the algorithm
constraints of the

SSLParameters

is non-null, for every
certificate in the certification path, fields such as subject public
key, the signature algorithm, key usage, extended key usage, etc.
need to conform to the algorithm constraints in place on this engine.

**Parameters:** chain

- the peer certificate chain
**Parameters:** authType

- the key exchange algorithm used
**Parameters:** engine

- the engine used for this connection. This parameter
can be null, which indicates that implementations need not check
the ssl parameters
**Throws:** IllegalArgumentException

- if null or zero-length array is passed
in for the

chain

parameter or if null or zero-length
string is passed in for the

authType

parameter
**Throws:** CertificateException

- if the certificate chain is not trusted
by this TrustManager
**See Also:** SSLParameters.getEndpointIdentificationAlgorithm()

,

SSLParameters.setEndpointIdentificationAlgorithm(String)

,

SSLParameters.getAlgorithmConstraints()

,

SSLParameters.setAlgorithmConstraints(AlgorithmConstraints)

---

#### checkClientTrusted

public abstract void checkClientTrusted​(

X509Certificate

[] chain,

String

authType,

SSLEngine

engine)
throws

CertificateException

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

The authentication type is determined by the actual certificate
used. For instance, if RSAPublicKey is used, the authType
should be "RSA". Checking is case-sensitive.

If the

engine

parameter is available, and the endpoint
identification algorithm of the

SSLParameters

is
non-empty, to prevent man-in-the-middle attacks, the address that
the

engine

connected to should be checked against
the peer's identity presented in the end-entity X509 certificate,
as specified in the endpoint identification algorithm.

If the

engine

parameter is available, and the algorithm
constraints of the

SSLParameters

is non-null, for every
certificate in the certification path, fields such as subject public
key, the signature algorithm, key usage, extended key usage, etc.
need to conform to the algorithm constraints in place on this engine.

The authentication type is determined by the actual certificate
used. For instance, if RSAPublicKey is used, the authType
should be "RSA". Checking is case-sensitive.

If the

engine

parameter is available, and the endpoint
identification algorithm of the

SSLParameters

is
non-empty, to prevent man-in-the-middle attacks, the address that
the

engine

connected to should be checked against
the peer's identity presented in the end-entity X509 certificate,
as specified in the endpoint identification algorithm.

If the

engine

parameter is available, and the algorithm
constraints of the

SSLParameters

is non-null, for every
certificate in the certification path, fields such as subject public
key, the signature algorithm, key usage, extended key usage, etc.
need to conform to the algorithm constraints in place on this engine.

If the

engine

parameter is available, and the endpoint
identification algorithm of the

SSLParameters

is
non-empty, to prevent man-in-the-middle attacks, the address that
the

engine

connected to should be checked against
the peer's identity presented in the end-entity X509 certificate,
as specified in the endpoint identification algorithm.

If the

engine

parameter is available, and the algorithm
constraints of the

SSLParameters

is non-null, for every
certificate in the certification path, fields such as subject public
key, the signature algorithm, key usage, extended key usage, etc.
need to conform to the algorithm constraints in place on this engine.

If the

engine

parameter is available, and the algorithm
constraints of the

SSLParameters

is non-null, for every
certificate in the certification path, fields such as subject public
key, the signature algorithm, key usage, extended key usage, etc.
need to conform to the algorithm constraints in place on this engine.

checkServerTrusted

```java
public abstract void checkServerTrusted​(
X509Certificate
[] chain,

String
authType,

SSLEngine
engine)
throws
CertificateException
```

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

The authentication type is the key exchange algorithm portion
of the cipher suites represented as a String, such as "RSA",
"DHE_DSS". Note: for some exportable cipher suites, the key
exchange algorithm is determined at run time during the
handshake. For instance, for TLS_RSA_EXPORT_WITH_RC4_40_MD5,
the authType should be RSA_EXPORT when an ephemeral RSA key is
used for the key exchange, and RSA when the key from the server
certificate is used. Checking is case-sensitive.

If the

engine

parameter is available, and the endpoint
identification algorithm of the

SSLParameters

is
non-empty, to prevent man-in-the-middle attacks, the address that
the

engine

connected to should be checked against
the peer's identity presented in the end-entity X509 certificate,
as specified in the endpoint identification algorithm.

If the

engine

parameter is available, and the algorithm
constraints of the

SSLParameters

is non-null, for every
certificate in the certification path, fields such as subject public
key, the signature algorithm, key usage, extended key usage, etc.
need to conform to the algorithm constraints in place on this engine.

**Parameters:** chain

- the peer certificate chain
**Parameters:** authType

- the key exchange algorithm used
**Parameters:** engine

- the engine used for this connection. This parameter
can be null, which indicates that implementations need not check
the ssl parameters
**Throws:** IllegalArgumentException

- if null or zero-length array is passed
in for the

chain

parameter or if null or zero-length
string is passed in for the

authType

parameter
**Throws:** CertificateException

- if the certificate chain is not trusted
by this TrustManager
**See Also:** SSLParameters.getEndpointIdentificationAlgorithm()

,

SSLParameters.setEndpointIdentificationAlgorithm(String)

,

SSLParameters.getAlgorithmConstraints()

,

SSLParameters.setAlgorithmConstraints(AlgorithmConstraints)

---

#### checkServerTrusted

public abstract void checkServerTrusted​(

X509Certificate

[] chain,

String

authType,

SSLEngine

engine)
throws

CertificateException

Given the partial or complete certificate chain provided by the
peer, build and validate the certificate path based on the
authentication type and ssl parameters.

The authentication type is the key exchange algorithm portion
of the cipher suites represented as a String, such as "RSA",
"DHE_DSS". Note: for some exportable cipher suites, the key
exchange algorithm is determined at run time during the
handshake. For instance, for TLS_RSA_EXPORT_WITH_RC4_40_MD5,
the authType should be RSA_EXPORT when an ephemeral RSA key is
used for the key exchange, and RSA when the key from the server
certificate is used. Checking is case-sensitive.

If the

engine

parameter is available, and the endpoint
identification algorithm of the

SSLParameters

is
non-empty, to prevent man-in-the-middle attacks, the address that
the

engine

connected to should be checked against
the peer's identity presented in the end-entity X509 certificate,
as specified in the endpoint identification algorithm.

If the

engine

parameter is available, and the algorithm
constraints of the

SSLParameters

is non-null, for every
certificate in the certification path, fields such as subject public
key, the signature algorithm, key usage, extended key usage, etc.
need to conform to the algorithm constraints in place on this engine.

The authentication type is the key exchange algorithm portion
of the cipher suites represented as a String, such as "RSA",
"DHE_DSS". Note: for some exportable cipher suites, the key
exchange algorithm is determined at run time during the
handshake. For instance, for TLS_RSA_EXPORT_WITH_RC4_40_MD5,
the authType should be RSA_EXPORT when an ephemeral RSA key is
used for the key exchange, and RSA when the key from the server
certificate is used. Checking is case-sensitive.

If the

engine

parameter is available, and the endpoint
identification algorithm of the

SSLParameters

is
non-empty, to prevent man-in-the-middle attacks, the address that
the

engine

connected to should be checked against
the peer's identity presented in the end-entity X509 certificate,
as specified in the endpoint identification algorithm.

If the

engine

parameter is available, and the algorithm
constraints of the

SSLParameters

is non-null, for every
certificate in the certification path, fields such as subject public
key, the signature algorithm, key usage, extended key usage, etc.
need to conform to the algorithm constraints in place on this engine.

If the

engine

parameter is available, and the endpoint
identification algorithm of the

SSLParameters

is
non-empty, to prevent man-in-the-middle attacks, the address that
the

engine

connected to should be checked against
the peer's identity presented in the end-entity X509 certificate,
as specified in the endpoint identification algorithm.

If the

engine

parameter is available, and the algorithm
constraints of the

SSLParameters

is non-null, for every
certificate in the certification path, fields such as subject public
key, the signature algorithm, key usage, extended key usage, etc.
need to conform to the algorithm constraints in place on this engine.

If the

engine

parameter is available, and the algorithm
constraints of the

SSLParameters

is non-null, for every
certificate in the certification path, fields such as subject public
key, the signature algorithm, key usage, extended key usage, etc.
need to conform to the algorithm constraints in place on this engine.

---

