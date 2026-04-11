# Interface HostnameVerifier

**Source:** `java.base\javax\net\ssl\HostnameVerifier.html`

### Class Description

```java
public interface
HostnameVerifier
```

This class is the base interface for hostname verification.

During handshaking, if the URL's hostname and
the server's identification hostname mismatch, the
verification mechanism can call back to implementers of this
interface to determine if this connection should be allowed.

The policies can be certificate-based
or may depend on other authentication schemes.

These callbacks are used when the default rules for URL hostname
verification fail.

**Since:** 1.4

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean verify​(
String
hostname,

SSLSession
session)

Verify that the host name is an acceptable match with
the server's authentication scheme.

**Parameters:**
- hostname

- the host name
- session

- SSLSession used on the connection to host

**Returns:**
- true if the host name is acceptable

---

### Additional Sections

#### Interface HostnameVerifier

```java
public interface
HostnameVerifier
```

This class is the base interface for hostname verification.

During handshaking, if the URL's hostname and
the server's identification hostname mismatch, the
verification mechanism can call back to implementers of this
interface to determine if this connection should be allowed.

The policies can be certificate-based
or may depend on other authentication schemes.

These callbacks are used when the default rules for URL hostname
verification fail.

**Since:** 1.4

public interface

HostnameVerifier

This class is the base interface for hostname verification.

During handshaking, if the URL's hostname and
the server's identification hostname mismatch, the
verification mechanism can call back to implementers of this
interface to determine if this connection should be allowed.

The policies can be certificate-based
or may depend on other authentication schemes.

These callbacks are used when the default rules for URL hostname
verification fail.

During handshaking, if the URL's hostname and
the server's identification hostname mismatch, the
verification mechanism can call back to implementers of this
interface to determine if this connection should be allowed.

The policies can be certificate-based
or may depend on other authentication schemes.

These callbacks are used when the default rules for URL hostname
verification fail.

The policies can be certificate-based
or may depend on other authentication schemes.

These callbacks are used when the default rules for URL hostname
verification fail.

These callbacks are used when the default rules for URL hostname
verification fail.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

verify

​(

String

hostname,

SSLSession

session)

Verify that the host name is an acceptable match with
the server's authentication scheme.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

verify

​(

String

hostname,

SSLSession

session)

Verify that the host name is an acceptable match with
the server's authentication scheme.

---

#### Method Summary

Verify that the host name is an acceptable match with
the server's authentication scheme.

============ METHOD DETAIL ==========

- Method Detail

- verify

```java
boolean verify​(
String
hostname,

SSLSession
session)
```

Verify that the host name is an acceptable match with
the server's authentication scheme.

**Parameters:** hostname

- the host name
**Parameters:** session

- SSLSession used on the connection to host
**Returns:** true if the host name is acceptable

Method Detail

- verify

```java
boolean verify​(
String
hostname,

SSLSession
session)
```

Verify that the host name is an acceptable match with
the server's authentication scheme.

**Parameters:** hostname

- the host name
**Parameters:** session

- SSLSession used on the connection to host
**Returns:** true if the host name is acceptable

---

#### Method Detail

verify

```java
boolean verify​(
String
hostname,

SSLSession
session)
```

Verify that the host name is an acceptable match with
the server's authentication scheme.

**Parameters:** hostname

- the host name
**Parameters:** session

- SSLSession used on the connection to host
**Returns:** true if the host name is acceptable

---

#### verify

boolean verify​(

String

hostname,

SSLSession

session)

Verify that the host name is an acceptable match with
the server's authentication scheme.

---

