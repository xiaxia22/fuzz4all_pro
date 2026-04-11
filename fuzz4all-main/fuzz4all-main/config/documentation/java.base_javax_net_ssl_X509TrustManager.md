# Interface X509TrustManager

**Source:** `java.base\javax\net\ssl\X509TrustManager.html`

### Class Description

```java
public interface
X509TrustManager

extends
TrustManager
```

Instance of this interface manage which X509 certificates
may be used to authenticate the remote side of a secure
socket. Decisions may be based on trusted certificate
authorities, certificate revocation lists, online
status checking or other means.

**All Superinterfaces:** TrustManager

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void checkClientTrusted​(
X509Certificate
[] chain,

String
authType)
throws
CertificateException

Given the partial or complete certificate chain provided by the
peer, build a certificate path to a trusted root and return if
it can be validated and is trusted for client SSL
authentication based on the authentication type.

The authentication type is determined by the actual certificate
used. For instance, if RSAPublicKey is used, the authType
should be "RSA". Checking is case-sensitive.

**Parameters:**
- chain

- the peer certificate chain
- authType

- the authentication type based on the client certificate

**Throws:**
- IllegalArgumentException

- if null or zero-length chain
is passed in for the chain parameter or if null or zero-length
string is passed in for the authType parameter
- CertificateException

- if the certificate chain is not trusted
by this TrustManager.

---

#### void checkServerTrusted​(
X509Certificate
[] chain,

String
authType)
throws
CertificateException

Given the partial or complete certificate chain provided by the
peer, build a certificate path to a trusted root and return if
it can be validated and is trusted for server SSL
authentication based on the authentication type.

The authentication type is the key exchange algorithm portion
of the cipher suites represented as a String, such as "RSA",
"DHE_DSS". Note: for some exportable cipher suites, the key
exchange algorithm is determined at run time during the
handshake. For instance, for TLS_RSA_EXPORT_WITH_RC4_40_MD5,
the authType should be RSA_EXPORT when an ephemeral RSA key is
used for the key exchange, and RSA when the key from the server
certificate is used. Checking is case-sensitive.

**Parameters:**
- chain

- the peer certificate chain
- authType

- the key exchange algorithm used

**Throws:**
- IllegalArgumentException

- if null or zero-length chain
is passed in for the chain parameter or if null or zero-length
string is passed in for the authType parameter
- CertificateException

- if the certificate chain is not trusted
by this TrustManager.

---

#### X509Certificate
[] getAcceptedIssuers()

Return an array of certificate authority certificates
which are trusted for authenticating peers.

**Returns:**
- a non-null (possibly empty) array of acceptable
CA issuer certificates.

---

### Additional Sections

#### Interface X509TrustManager

**All Superinterfaces:** TrustManager

**All Known Implementing Classes:** X509ExtendedTrustManager

```java
public interface
X509TrustManager

extends
TrustManager
```

Instance of this interface manage which X509 certificates
may be used to authenticate the remote side of a secure
socket. Decisions may be based on trusted certificate
authorities, certificate revocation lists, online
status checking or other means.

**Since:** 1.4

public interface

X509TrustManager

extends

TrustManager

Instance of this interface manage which X509 certificates
may be used to authenticate the remote side of a secure
socket. Decisions may be based on trusted certificate
authorities, certificate revocation lists, online
status checking or other means.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

checkClientTrusted

​(

X509Certificate

[] chain,

String

authType)

Given the partial or complete certificate chain provided by the
peer, build a certificate path to a trusted root and return if
it can be validated and is trusted for client SSL
authentication based on the authentication type.

void

checkServerTrusted

​(

X509Certificate

[] chain,

String

authType)

Given the partial or complete certificate chain provided by the
peer, build a certificate path to a trusted root and return if
it can be validated and is trusted for server SSL
authentication based on the authentication type.

X509Certificate

[]

getAcceptedIssuers

()

Return an array of certificate authority certificates
which are trusted for authenticating peers.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

checkClientTrusted

​(

X509Certificate

[] chain,

String

authType)

Given the partial or complete certificate chain provided by the
peer, build a certificate path to a trusted root and return if
it can be validated and is trusted for client SSL
authentication based on the authentication type.

void

checkServerTrusted

​(

X509Certificate

[] chain,

String

authType)

Given the partial or complete certificate chain provided by the
peer, build a certificate path to a trusted root and return if
it can be validated and is trusted for server SSL
authentication based on the authentication type.

X509Certificate

[]

getAcceptedIssuers

()

Return an array of certificate authority certificates
which are trusted for authenticating peers.

---

#### Method Summary

Given the partial or complete certificate chain provided by the
peer, build a certificate path to a trusted root and return if
it can be validated and is trusted for client SSL
authentication based on the authentication type.

Given the partial or complete certificate chain provided by the
peer, build a certificate path to a trusted root and return if
it can be validated and is trusted for server SSL
authentication based on the authentication type.

Return an array of certificate authority certificates
which are trusted for authenticating peers.

============ METHOD DETAIL ==========

- Method Detail

- checkClientTrusted

```java
void checkClientTrusted​(
X509Certificate
[] chain,

String
authType)
throws
CertificateException
```

Given the partial or complete certificate chain provided by the
peer, build a certificate path to a trusted root and return if
it can be validated and is trusted for client SSL
authentication based on the authentication type.

The authentication type is determined by the actual certificate
used. For instance, if RSAPublicKey is used, the authType
should be "RSA". Checking is case-sensitive.

**Parameters:** chain

- the peer certificate chain
**Parameters:** authType

- the authentication type based on the client certificate
**Throws:** IllegalArgumentException

- if null or zero-length chain
is passed in for the chain parameter or if null or zero-length
string is passed in for the authType parameter
**Throws:** CertificateException

- if the certificate chain is not trusted
by this TrustManager.

- checkServerTrusted

```java
void checkServerTrusted​(
X509Certificate
[] chain,

String
authType)
throws
CertificateException
```

Given the partial or complete certificate chain provided by the
peer, build a certificate path to a trusted root and return if
it can be validated and is trusted for server SSL
authentication based on the authentication type.

The authentication type is the key exchange algorithm portion
of the cipher suites represented as a String, such as "RSA",
"DHE_DSS". Note: for some exportable cipher suites, the key
exchange algorithm is determined at run time during the
handshake. For instance, for TLS_RSA_EXPORT_WITH_RC4_40_MD5,
the authType should be RSA_EXPORT when an ephemeral RSA key is
used for the key exchange, and RSA when the key from the server
certificate is used. Checking is case-sensitive.

**Parameters:** chain

- the peer certificate chain
**Parameters:** authType

- the key exchange algorithm used
**Throws:** IllegalArgumentException

- if null or zero-length chain
is passed in for the chain parameter or if null or zero-length
string is passed in for the authType parameter
**Throws:** CertificateException

- if the certificate chain is not trusted
by this TrustManager.

- getAcceptedIssuers

```java
X509Certificate
[] getAcceptedIssuers()
```

Return an array of certificate authority certificates
which are trusted for authenticating peers.

**Returns:** a non-null (possibly empty) array of acceptable
CA issuer certificates.

Method Detail

- checkClientTrusted

```java
void checkClientTrusted​(
X509Certificate
[] chain,

String
authType)
throws
CertificateException
```

Given the partial or complete certificate chain provided by the
peer, build a certificate path to a trusted root and return if
it can be validated and is trusted for client SSL
authentication based on the authentication type.

The authentication type is determined by the actual certificate
used. For instance, if RSAPublicKey is used, the authType
should be "RSA". Checking is case-sensitive.

**Parameters:** chain

- the peer certificate chain
**Parameters:** authType

- the authentication type based on the client certificate
**Throws:** IllegalArgumentException

- if null or zero-length chain
is passed in for the chain parameter or if null or zero-length
string is passed in for the authType parameter
**Throws:** CertificateException

- if the certificate chain is not trusted
by this TrustManager.

- checkServerTrusted

```java
void checkServerTrusted​(
X509Certificate
[] chain,

String
authType)
throws
CertificateException
```

Given the partial or complete certificate chain provided by the
peer, build a certificate path to a trusted root and return if
it can be validated and is trusted for server SSL
authentication based on the authentication type.

The authentication type is the key exchange algorithm portion
of the cipher suites represented as a String, such as "RSA",
"DHE_DSS". Note: for some exportable cipher suites, the key
exchange algorithm is determined at run time during the
handshake. For instance, for TLS_RSA_EXPORT_WITH_RC4_40_MD5,
the authType should be RSA_EXPORT when an ephemeral RSA key is
used for the key exchange, and RSA when the key from the server
certificate is used. Checking is case-sensitive.

**Parameters:** chain

- the peer certificate chain
**Parameters:** authType

- the key exchange algorithm used
**Throws:** IllegalArgumentException

- if null or zero-length chain
is passed in for the chain parameter or if null or zero-length
string is passed in for the authType parameter
**Throws:** CertificateException

- if the certificate chain is not trusted
by this TrustManager.

- getAcceptedIssuers

```java
X509Certificate
[] getAcceptedIssuers()
```

Return an array of certificate authority certificates
which are trusted for authenticating peers.

**Returns:** a non-null (possibly empty) array of acceptable
CA issuer certificates.

---

#### Method Detail

checkClientTrusted

```java
void checkClientTrusted​(
X509Certificate
[] chain,

String
authType)
throws
CertificateException
```

Given the partial or complete certificate chain provided by the
peer, build a certificate path to a trusted root and return if
it can be validated and is trusted for client SSL
authentication based on the authentication type.

The authentication type is determined by the actual certificate
used. For instance, if RSAPublicKey is used, the authType
should be "RSA". Checking is case-sensitive.

**Parameters:** chain

- the peer certificate chain
**Parameters:** authType

- the authentication type based on the client certificate
**Throws:** IllegalArgumentException

- if null or zero-length chain
is passed in for the chain parameter or if null or zero-length
string is passed in for the authType parameter
**Throws:** CertificateException

- if the certificate chain is not trusted
by this TrustManager.

---

#### checkClientTrusted

void checkClientTrusted​(

X509Certificate

[] chain,

String

authType)
throws

CertificateException

Given the partial or complete certificate chain provided by the
peer, build a certificate path to a trusted root and return if
it can be validated and is trusted for client SSL
authentication based on the authentication type.

The authentication type is determined by the actual certificate
used. For instance, if RSAPublicKey is used, the authType
should be "RSA". Checking is case-sensitive.

The authentication type is determined by the actual certificate
used. For instance, if RSAPublicKey is used, the authType
should be "RSA". Checking is case-sensitive.

checkServerTrusted

```java
void checkServerTrusted​(
X509Certificate
[] chain,

String
authType)
throws
CertificateException
```

Given the partial or complete certificate chain provided by the
peer, build a certificate path to a trusted root and return if
it can be validated and is trusted for server SSL
authentication based on the authentication type.

The authentication type is the key exchange algorithm portion
of the cipher suites represented as a String, such as "RSA",
"DHE_DSS". Note: for some exportable cipher suites, the key
exchange algorithm is determined at run time during the
handshake. For instance, for TLS_RSA_EXPORT_WITH_RC4_40_MD5,
the authType should be RSA_EXPORT when an ephemeral RSA key is
used for the key exchange, and RSA when the key from the server
certificate is used. Checking is case-sensitive.

**Parameters:** chain

- the peer certificate chain
**Parameters:** authType

- the key exchange algorithm used
**Throws:** IllegalArgumentException

- if null or zero-length chain
is passed in for the chain parameter or if null or zero-length
string is passed in for the authType parameter
**Throws:** CertificateException

- if the certificate chain is not trusted
by this TrustManager.

---

#### checkServerTrusted

void checkServerTrusted​(

X509Certificate

[] chain,

String

authType)
throws

CertificateException

Given the partial or complete certificate chain provided by the
peer, build a certificate path to a trusted root and return if
it can be validated and is trusted for server SSL
authentication based on the authentication type.

The authentication type is the key exchange algorithm portion
of the cipher suites represented as a String, such as "RSA",
"DHE_DSS". Note: for some exportable cipher suites, the key
exchange algorithm is determined at run time during the
handshake. For instance, for TLS_RSA_EXPORT_WITH_RC4_40_MD5,
the authType should be RSA_EXPORT when an ephemeral RSA key is
used for the key exchange, and RSA when the key from the server
certificate is used. Checking is case-sensitive.

The authentication type is the key exchange algorithm portion
of the cipher suites represented as a String, such as "RSA",
"DHE_DSS". Note: for some exportable cipher suites, the key
exchange algorithm is determined at run time during the
handshake. For instance, for TLS_RSA_EXPORT_WITH_RC4_40_MD5,
the authType should be RSA_EXPORT when an ephemeral RSA key is
used for the key exchange, and RSA when the key from the server
certificate is used. Checking is case-sensitive.

getAcceptedIssuers

```java
X509Certificate
[] getAcceptedIssuers()
```

Return an array of certificate authority certificates
which are trusted for authenticating peers.

**Returns:** a non-null (possibly empty) array of acceptable
CA issuer certificates.

---

#### getAcceptedIssuers

X509Certificate

[] getAcceptedIssuers()

Return an array of certificate authority certificates
which are trusted for authenticating peers.

---

