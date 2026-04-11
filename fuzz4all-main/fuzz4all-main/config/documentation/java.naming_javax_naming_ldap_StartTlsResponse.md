# Class StartTlsResponse

**Source:** `java.naming\javax\naming\ldap\StartTlsResponse.html`

### Class Description

```java
public abstract class
StartTlsResponse

extends
Object

implements
ExtendedResponse
```

This class implements the LDAPv3 Extended Response for StartTLS as
defined in

Lightweight Directory
Access Protocol (v3): Extension for Transport Layer Security

The object identifier for StartTLS is 1.3.6.1.4.1.1466.20037
and no extended response value is defined.

The Start TLS extended request and response are used to establish
a TLS connection over the existing LDAP connection associated with
the JNDI context on which

extendedOperation()

is invoked.
Typically, a JNDI program uses the StartTLS extended request and response
classes as follows.

```java
import javax.naming.ldap.*;

// Open an LDAP association
LdapContext ctx = new InitialLdapContext();

// Perform a StartTLS extended operation
StartTlsResponse tls =
(StartTlsResponse) ctx.extendedOperation(new StartTlsRequest());

// Open a TLS connection (over the existing LDAP association) and get details
// of the negotiated TLS session: cipher suite, peer certificate, ...
SSLSession session = tls.negotiate();

// ... use ctx to perform protected LDAP operations

// Close the TLS connection (revert back to the underlying LDAP association)
tls.close();

// ... use ctx to perform unprotected LDAP operations

// Close the LDAP association
ctx.close;
```

**All Implemented Interfaces:** Serializable

,

ExtendedResponse

---

### Field Details

#### public static final
String
OID

The StartTLS extended response's assigned object identifier
is 1.3.6.1.4.1.1466.20037.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### protected StartTlsResponse()

Constructs a StartTLS extended response.
A concrete subclass must have a public no-arg constructor.

---

### Method Details

#### public
String
getID()

Retrieves the StartTLS response's object identifier string.

**Specified by:**
- getID

in interface

ExtendedResponse

**Returns:**
- The object identifier string, "1.3.6.1.4.1.1466.20037".

---

#### public byte[] getEncodedValue()

Retrieves the StartTLS response's ASN.1 BER encoded value.
Since the response has no defined value, null is always
returned.

**Specified by:**
- getEncodedValue

in interface

ExtendedResponse

**Returns:**
- The null value.

---

#### public abstract void setEnabledCipherSuites​(
String
[] suites)

Overrides the default list of cipher suites enabled for use on the
TLS connection. The cipher suites must have already been listed by

SSLSocketFactory.getSupportedCipherSuites()

as being supported.
Even if a suite has been enabled, it still might not be used because
the peer does not support it, or because the requisite certificates
(and private keys) are not available.

**Parameters:**
- suites

- The non-null list of names of all the cipher suites to
enable.

**See Also:**
- negotiate()

---

#### public abstract void setHostnameVerifier​(
HostnameVerifier
verifier)

Sets the hostname verifier used by

negotiate()

after the TLS handshake has completed and the default hostname
verification has failed.

setHostnameVerifier()

must be called before

negotiate()

is invoked for it to have effect.
If called after

negotiate()

, this method does not do anything.

**Parameters:**
- verifier

- The non-null hostname verifier callback.

**See Also:**
- negotiate()

---

#### public abstract
SSLSession
negotiate()
throws
IOException

Negotiates a TLS session using the default SSL socket factory.

This method is equivalent to

negotiate(null)

.

**Returns:**
- The negotiated SSL session

**Throws:**
- IOException

- If an IO error was encountered while establishing
the TLS session.

**See Also:**
- setEnabledCipherSuites(java.lang.String[])

,

setHostnameVerifier(javax.net.ssl.HostnameVerifier)

---

#### public abstract
SSLSession
negotiate​(
SSLSocketFactory
factory)
throws
IOException

Negotiates a TLS session using an SSL socket factory.

Creates an SSL socket using the supplied SSL socket factory and
attaches it to the existing connection. Performs the TLS handshake
and returns the negotiated session information.

If cipher suites have been set via

setEnabledCipherSuites

then they are enabled before the TLS handshake begins.

Hostname verification is performed after the TLS handshake completes.
The default hostname verification performs a match of the server's
hostname against the hostname information found in the server's certificate.
If this verification fails and no callback has been set via

setHostnameVerifier

then the negotiation fails.
If this verification fails and a callback has been set via

setHostnameVerifier

, then the callback is used to determine whether
the negotiation succeeds.

If an error occurs then the SSL socket is closed and an IOException
is thrown. The underlying connection remains intact.

**Parameters:**
- factory

- The possibly null SSL socket factory to use.
If null, the default SSL socket factory is used.

**Returns:**
- The negotiated SSL session

**Throws:**
- IOException

- If an IO error was encountered while establishing
the TLS session.

**See Also:**
- setEnabledCipherSuites(java.lang.String[])

,

setHostnameVerifier(javax.net.ssl.HostnameVerifier)

---

#### public abstract void close()
throws
IOException

Closes the TLS connection gracefully and reverts back to the underlying
connection.

**Throws:**
- IOException

- If an IO error was encountered while closing the
TLS connection

---

### Additional Sections

#### Class StartTlsResponse

java.lang.Object

- javax.naming.ldap.StartTlsResponse

javax.naming.ldap.StartTlsResponse

**All Implemented Interfaces:** Serializable

,

ExtendedResponse

```java
public abstract class
StartTlsResponse

extends
Object

implements
ExtendedResponse
```

This class implements the LDAPv3 Extended Response for StartTLS as
defined in

Lightweight Directory
Access Protocol (v3): Extension for Transport Layer Security

The object identifier for StartTLS is 1.3.6.1.4.1.1466.20037
and no extended response value is defined.

The Start TLS extended request and response are used to establish
a TLS connection over the existing LDAP connection associated with
the JNDI context on which

extendedOperation()

is invoked.
Typically, a JNDI program uses the StartTLS extended request and response
classes as follows.

```java
import javax.naming.ldap.*;

// Open an LDAP association
LdapContext ctx = new InitialLdapContext();

// Perform a StartTLS extended operation
StartTlsResponse tls =
(StartTlsResponse) ctx.extendedOperation(new StartTlsRequest());

// Open a TLS connection (over the existing LDAP association) and get details
// of the negotiated TLS session: cipher suite, peer certificate, ...
SSLSession session = tls.negotiate();

// ... use ctx to perform protected LDAP operations

// Close the TLS connection (revert back to the underlying LDAP association)
tls.close();

// ... use ctx to perform unprotected LDAP operations

// Close the LDAP association
ctx.close;
```

**Since:** 1.4
**See Also:** StartTlsRequest

,

Serialized Form

public abstract class

StartTlsResponse

extends

Object

implements

ExtendedResponse

This class implements the LDAPv3 Extended Response for StartTLS as
defined in

Lightweight Directory
Access Protocol (v3): Extension for Transport Layer Security

The object identifier for StartTLS is 1.3.6.1.4.1.1466.20037
and no extended response value is defined.

The Start TLS extended request and response are used to establish
a TLS connection over the existing LDAP connection associated with
the JNDI context on which

extendedOperation()

is invoked.
Typically, a JNDI program uses the StartTLS extended request and response
classes as follows.

```java
import javax.naming.ldap.*;

// Open an LDAP association
LdapContext ctx = new InitialLdapContext();

// Perform a StartTLS extended operation
StartTlsResponse tls =
(StartTlsResponse) ctx.extendedOperation(new StartTlsRequest());

// Open a TLS connection (over the existing LDAP association) and get details
// of the negotiated TLS session: cipher suite, peer certificate, ...
SSLSession session = tls.negotiate();

// ... use ctx to perform protected LDAP operations

// Close the TLS connection (revert back to the underlying LDAP association)
tls.close();

// ... use ctx to perform unprotected LDAP operations

// Close the LDAP association
ctx.close;
```

The Start TLS extended request and response are used to establish
a TLS connection over the existing LDAP connection associated with
the JNDI context on which

extendedOperation()

is invoked.
Typically, a JNDI program uses the StartTLS extended request and response
classes as follows.

```java
import javax.naming.ldap.*;

// Open an LDAP association
LdapContext ctx = new InitialLdapContext();

// Perform a StartTLS extended operation
StartTlsResponse tls =
(StartTlsResponse) ctx.extendedOperation(new StartTlsRequest());

// Open a TLS connection (over the existing LDAP association) and get details
// of the negotiated TLS session: cipher suite, peer certificate, ...
SSLSession session = tls.negotiate();

// ... use ctx to perform protected LDAP operations

// Close the TLS connection (revert back to the underlying LDAP association)
tls.close();

// ... use ctx to perform unprotected LDAP operations

// Close the LDAP association
ctx.close;
```

import javax.naming.ldap.*;

// Open an LDAP association
LdapContext ctx = new InitialLdapContext();

// Perform a StartTLS extended operation
StartTlsResponse tls =
(StartTlsResponse) ctx.extendedOperation(new StartTlsRequest());

// Open a TLS connection (over the existing LDAP association) and get details
// of the negotiated TLS session: cipher suite, peer certificate, ...
SSLSession session = tls.negotiate();

// ... use ctx to perform protected LDAP operations

// Close the TLS connection (revert back to the underlying LDAP association)
tls.close();

// ... use ctx to perform unprotected LDAP operations

// Close the LDAP association
ctx.close;

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

OID

The StartTLS extended response's assigned object identifier
is 1.3.6.1.4.1.1466.20037.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

StartTlsResponse

()

Constructs a StartTLS extended response.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract void

close

()

Closes the TLS connection gracefully and reverts back to the underlying
connection.

byte[]

getEncodedValue

()

Retrieves the StartTLS response's ASN.1 BER encoded value.

String

getID

()

Retrieves the StartTLS response's object identifier string.

abstract

SSLSession

negotiate

()

Negotiates a TLS session using the default SSL socket factory.

abstract

SSLSession

negotiate

​(

SSLSocketFactory

factory)

Negotiates a TLS session using an SSL socket factory.

abstract void

setEnabledCipherSuites

​(

String

[] suites)

Overrides the default list of cipher suites enabled for use on the
TLS connection.

abstract void

setHostnameVerifier

​(

HostnameVerifier

verifier)

Sets the hostname verifier used by

negotiate()

after the TLS handshake has completed and the default hostname
verification has failed.

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

Field Summary

Fields

Modifier and Type

Field

Description

static

String

OID

The StartTLS extended response's assigned object identifier
is 1.3.6.1.4.1.1466.20037.

---

#### Field Summary

The StartTLS extended response's assigned object identifier
is 1.3.6.1.4.1.1466.20037.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

StartTlsResponse

()

Constructs a StartTLS extended response.

---

#### Constructor Summary

Constructs a StartTLS extended response.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract void

close

()

Closes the TLS connection gracefully and reverts back to the underlying
connection.

byte[]

getEncodedValue

()

Retrieves the StartTLS response's ASN.1 BER encoded value.

String

getID

()

Retrieves the StartTLS response's object identifier string.

abstract

SSLSession

negotiate

()

Negotiates a TLS session using the default SSL socket factory.

abstract

SSLSession

negotiate

​(

SSLSocketFactory

factory)

Negotiates a TLS session using an SSL socket factory.

abstract void

setEnabledCipherSuites

​(

String

[] suites)

Overrides the default list of cipher suites enabled for use on the
TLS connection.

abstract void

setHostnameVerifier

​(

HostnameVerifier

verifier)

Sets the hostname verifier used by

negotiate()

after the TLS handshake has completed and the default hostname
verification has failed.

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

Closes the TLS connection gracefully and reverts back to the underlying
connection.

Retrieves the StartTLS response's ASN.1 BER encoded value.

Retrieves the StartTLS response's object identifier string.

Negotiates a TLS session using the default SSL socket factory.

Negotiates a TLS session using an SSL socket factory.

Overrides the default list of cipher suites enabled for use on the
TLS connection.

Sets the hostname verifier used by

negotiate()

after the TLS handshake has completed and the default hostname
verification has failed.

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

============ FIELD DETAIL ===========

- Field Detail

- OID

```java
public static final
String
OID
```

The StartTLS extended response's assigned object identifier
is 1.3.6.1.4.1.1466.20037.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- StartTlsResponse

```java
protected StartTlsResponse()
```

Constructs a StartTLS extended response.
A concrete subclass must have a public no-arg constructor.

============ METHOD DETAIL ==========

- Method Detail

- getID

```java
public
String
getID()
```

Retrieves the StartTLS response's object identifier string.

**Specified by:** getID

in interface

ExtendedResponse
**Returns:** The object identifier string, "1.3.6.1.4.1.1466.20037".

- getEncodedValue

```java
public byte[] getEncodedValue()
```

Retrieves the StartTLS response's ASN.1 BER encoded value.
Since the response has no defined value, null is always
returned.

**Specified by:** getEncodedValue

in interface

ExtendedResponse
**Returns:** The null value.

- setEnabledCipherSuites

```java
public abstract void setEnabledCipherSuites​(
String
[] suites)
```

Overrides the default list of cipher suites enabled for use on the
TLS connection. The cipher suites must have already been listed by

SSLSocketFactory.getSupportedCipherSuites()

as being supported.
Even if a suite has been enabled, it still might not be used because
the peer does not support it, or because the requisite certificates
(and private keys) are not available.

**Parameters:** suites

- The non-null list of names of all the cipher suites to
enable.
**See Also:** negotiate()

- setHostnameVerifier

```java
public abstract void setHostnameVerifier​(
HostnameVerifier
verifier)
```

Sets the hostname verifier used by

negotiate()

after the TLS handshake has completed and the default hostname
verification has failed.

setHostnameVerifier()

must be called before

negotiate()

is invoked for it to have effect.
If called after

negotiate()

, this method does not do anything.

**Parameters:** verifier

- The non-null hostname verifier callback.
**See Also:** negotiate()

- negotiate

```java
public abstract
SSLSession
negotiate()
throws
IOException
```

Negotiates a TLS session using the default SSL socket factory.

This method is equivalent to

negotiate(null)

.

**Returns:** The negotiated SSL session
**Throws:** IOException

- If an IO error was encountered while establishing
the TLS session.
**See Also:** setEnabledCipherSuites(java.lang.String[])

,

setHostnameVerifier(javax.net.ssl.HostnameVerifier)

- negotiate

```java
public abstract
SSLSession
negotiate​(
SSLSocketFactory
factory)
throws
IOException
```

Negotiates a TLS session using an SSL socket factory.

Creates an SSL socket using the supplied SSL socket factory and
attaches it to the existing connection. Performs the TLS handshake
and returns the negotiated session information.

If cipher suites have been set via

setEnabledCipherSuites

then they are enabled before the TLS handshake begins.

Hostname verification is performed after the TLS handshake completes.
The default hostname verification performs a match of the server's
hostname against the hostname information found in the server's certificate.
If this verification fails and no callback has been set via

setHostnameVerifier

then the negotiation fails.
If this verification fails and a callback has been set via

setHostnameVerifier

, then the callback is used to determine whether
the negotiation succeeds.

If an error occurs then the SSL socket is closed and an IOException
is thrown. The underlying connection remains intact.

**Parameters:** factory

- The possibly null SSL socket factory to use.
If null, the default SSL socket factory is used.
**Returns:** The negotiated SSL session
**Throws:** IOException

- If an IO error was encountered while establishing
the TLS session.
**See Also:** setEnabledCipherSuites(java.lang.String[])

,

setHostnameVerifier(javax.net.ssl.HostnameVerifier)

- close

```java
public abstract void close()
throws
IOException
```

Closes the TLS connection gracefully and reverts back to the underlying
connection.

**Throws:** IOException

- If an IO error was encountered while closing the
TLS connection

Field Detail

- OID

```java
public static final
String
OID
```

The StartTLS extended response's assigned object identifier
is 1.3.6.1.4.1.1466.20037.

**See Also:** Constant Field Values

---

#### Field Detail

OID

```java
public static final
String
OID
```

The StartTLS extended response's assigned object identifier
is 1.3.6.1.4.1.1466.20037.

**See Also:** Constant Field Values

---

#### OID

public static final

String

OID

The StartTLS extended response's assigned object identifier
is 1.3.6.1.4.1.1466.20037.

Constructor Detail

- StartTlsResponse

```java
protected StartTlsResponse()
```

Constructs a StartTLS extended response.
A concrete subclass must have a public no-arg constructor.

---

#### Constructor Detail

StartTlsResponse

```java
protected StartTlsResponse()
```

Constructs a StartTLS extended response.
A concrete subclass must have a public no-arg constructor.

---

#### StartTlsResponse

protected StartTlsResponse()

Constructs a StartTLS extended response.
A concrete subclass must have a public no-arg constructor.

Method Detail

- getID

```java
public
String
getID()
```

Retrieves the StartTLS response's object identifier string.

**Specified by:** getID

in interface

ExtendedResponse
**Returns:** The object identifier string, "1.3.6.1.4.1.1466.20037".

- getEncodedValue

```java
public byte[] getEncodedValue()
```

Retrieves the StartTLS response's ASN.1 BER encoded value.
Since the response has no defined value, null is always
returned.

**Specified by:** getEncodedValue

in interface

ExtendedResponse
**Returns:** The null value.

- setEnabledCipherSuites

```java
public abstract void setEnabledCipherSuites​(
String
[] suites)
```

Overrides the default list of cipher suites enabled for use on the
TLS connection. The cipher suites must have already been listed by

SSLSocketFactory.getSupportedCipherSuites()

as being supported.
Even if a suite has been enabled, it still might not be used because
the peer does not support it, or because the requisite certificates
(and private keys) are not available.

**Parameters:** suites

- The non-null list of names of all the cipher suites to
enable.
**See Also:** negotiate()

- setHostnameVerifier

```java
public abstract void setHostnameVerifier​(
HostnameVerifier
verifier)
```

Sets the hostname verifier used by

negotiate()

after the TLS handshake has completed and the default hostname
verification has failed.

setHostnameVerifier()

must be called before

negotiate()

is invoked for it to have effect.
If called after

negotiate()

, this method does not do anything.

**Parameters:** verifier

- The non-null hostname verifier callback.
**See Also:** negotiate()

- negotiate

```java
public abstract
SSLSession
negotiate()
throws
IOException
```

Negotiates a TLS session using the default SSL socket factory.

This method is equivalent to

negotiate(null)

.

**Returns:** The negotiated SSL session
**Throws:** IOException

- If an IO error was encountered while establishing
the TLS session.
**See Also:** setEnabledCipherSuites(java.lang.String[])

,

setHostnameVerifier(javax.net.ssl.HostnameVerifier)

- negotiate

```java
public abstract
SSLSession
negotiate​(
SSLSocketFactory
factory)
throws
IOException
```

Negotiates a TLS session using an SSL socket factory.

Creates an SSL socket using the supplied SSL socket factory and
attaches it to the existing connection. Performs the TLS handshake
and returns the negotiated session information.

If cipher suites have been set via

setEnabledCipherSuites

then they are enabled before the TLS handshake begins.

Hostname verification is performed after the TLS handshake completes.
The default hostname verification performs a match of the server's
hostname against the hostname information found in the server's certificate.
If this verification fails and no callback has been set via

setHostnameVerifier

then the negotiation fails.
If this verification fails and a callback has been set via

setHostnameVerifier

, then the callback is used to determine whether
the negotiation succeeds.

If an error occurs then the SSL socket is closed and an IOException
is thrown. The underlying connection remains intact.

**Parameters:** factory

- The possibly null SSL socket factory to use.
If null, the default SSL socket factory is used.
**Returns:** The negotiated SSL session
**Throws:** IOException

- If an IO error was encountered while establishing
the TLS session.
**See Also:** setEnabledCipherSuites(java.lang.String[])

,

setHostnameVerifier(javax.net.ssl.HostnameVerifier)

- close

```java
public abstract void close()
throws
IOException
```

Closes the TLS connection gracefully and reverts back to the underlying
connection.

**Throws:** IOException

- If an IO error was encountered while closing the
TLS connection

---

#### Method Detail

getID

```java
public
String
getID()
```

Retrieves the StartTLS response's object identifier string.

**Specified by:** getID

in interface

ExtendedResponse
**Returns:** The object identifier string, "1.3.6.1.4.1.1466.20037".

---

#### getID

public

String

getID()

Retrieves the StartTLS response's object identifier string.

getEncodedValue

```java
public byte[] getEncodedValue()
```

Retrieves the StartTLS response's ASN.1 BER encoded value.
Since the response has no defined value, null is always
returned.

**Specified by:** getEncodedValue

in interface

ExtendedResponse
**Returns:** The null value.

---

#### getEncodedValue

public byte[] getEncodedValue()

Retrieves the StartTLS response's ASN.1 BER encoded value.
Since the response has no defined value, null is always
returned.

setEnabledCipherSuites

```java
public abstract void setEnabledCipherSuites​(
String
[] suites)
```

Overrides the default list of cipher suites enabled for use on the
TLS connection. The cipher suites must have already been listed by

SSLSocketFactory.getSupportedCipherSuites()

as being supported.
Even if a suite has been enabled, it still might not be used because
the peer does not support it, or because the requisite certificates
(and private keys) are not available.

**Parameters:** suites

- The non-null list of names of all the cipher suites to
enable.
**See Also:** negotiate()

---

#### setEnabledCipherSuites

public abstract void setEnabledCipherSuites​(

String

[] suites)

Overrides the default list of cipher suites enabled for use on the
TLS connection. The cipher suites must have already been listed by

SSLSocketFactory.getSupportedCipherSuites()

as being supported.
Even if a suite has been enabled, it still might not be used because
the peer does not support it, or because the requisite certificates
(and private keys) are not available.

setHostnameVerifier

```java
public abstract void setHostnameVerifier​(
HostnameVerifier
verifier)
```

Sets the hostname verifier used by

negotiate()

after the TLS handshake has completed and the default hostname
verification has failed.

setHostnameVerifier()

must be called before

negotiate()

is invoked for it to have effect.
If called after

negotiate()

, this method does not do anything.

**Parameters:** verifier

- The non-null hostname verifier callback.
**See Also:** negotiate()

---

#### setHostnameVerifier

public abstract void setHostnameVerifier​(

HostnameVerifier

verifier)

Sets the hostname verifier used by

negotiate()

after the TLS handshake has completed and the default hostname
verification has failed.

setHostnameVerifier()

must be called before

negotiate()

is invoked for it to have effect.
If called after

negotiate()

, this method does not do anything.

negotiate

```java
public abstract
SSLSession
negotiate()
throws
IOException
```

Negotiates a TLS session using the default SSL socket factory.

This method is equivalent to

negotiate(null)

.

**Returns:** The negotiated SSL session
**Throws:** IOException

- If an IO error was encountered while establishing
the TLS session.
**See Also:** setEnabledCipherSuites(java.lang.String[])

,

setHostnameVerifier(javax.net.ssl.HostnameVerifier)

---

#### negotiate

public abstract

SSLSession

negotiate()
throws

IOException

Negotiates a TLS session using the default SSL socket factory.

This method is equivalent to

negotiate(null)

.

This method is equivalent to

negotiate(null)

.

negotiate

```java
public abstract
SSLSession
negotiate​(
SSLSocketFactory
factory)
throws
IOException
```

Negotiates a TLS session using an SSL socket factory.

Creates an SSL socket using the supplied SSL socket factory and
attaches it to the existing connection. Performs the TLS handshake
and returns the negotiated session information.

If cipher suites have been set via

setEnabledCipherSuites

then they are enabled before the TLS handshake begins.

Hostname verification is performed after the TLS handshake completes.
The default hostname verification performs a match of the server's
hostname against the hostname information found in the server's certificate.
If this verification fails and no callback has been set via

setHostnameVerifier

then the negotiation fails.
If this verification fails and a callback has been set via

setHostnameVerifier

, then the callback is used to determine whether
the negotiation succeeds.

If an error occurs then the SSL socket is closed and an IOException
is thrown. The underlying connection remains intact.

**Parameters:** factory

- The possibly null SSL socket factory to use.
If null, the default SSL socket factory is used.
**Returns:** The negotiated SSL session
**Throws:** IOException

- If an IO error was encountered while establishing
the TLS session.
**See Also:** setEnabledCipherSuites(java.lang.String[])

,

setHostnameVerifier(javax.net.ssl.HostnameVerifier)

---

#### negotiate

public abstract

SSLSession

negotiate​(

SSLSocketFactory

factory)
throws

IOException

Negotiates a TLS session using an SSL socket factory.

Creates an SSL socket using the supplied SSL socket factory and
attaches it to the existing connection. Performs the TLS handshake
and returns the negotiated session information.

If cipher suites have been set via

setEnabledCipherSuites

then they are enabled before the TLS handshake begins.

Hostname verification is performed after the TLS handshake completes.
The default hostname verification performs a match of the server's
hostname against the hostname information found in the server's certificate.
If this verification fails and no callback has been set via

setHostnameVerifier

then the negotiation fails.
If this verification fails and a callback has been set via

setHostnameVerifier

, then the callback is used to determine whether
the negotiation succeeds.

If an error occurs then the SSL socket is closed and an IOException
is thrown. The underlying connection remains intact.

Creates an SSL socket using the supplied SSL socket factory and
attaches it to the existing connection. Performs the TLS handshake
and returns the negotiated session information.

If cipher suites have been set via

setEnabledCipherSuites

then they are enabled before the TLS handshake begins.

Hostname verification is performed after the TLS handshake completes.
The default hostname verification performs a match of the server's
hostname against the hostname information found in the server's certificate.
If this verification fails and no callback has been set via

setHostnameVerifier

then the negotiation fails.
If this verification fails and a callback has been set via

setHostnameVerifier

, then the callback is used to determine whether
the negotiation succeeds.

If an error occurs then the SSL socket is closed and an IOException
is thrown. The underlying connection remains intact.

If cipher suites have been set via

setEnabledCipherSuites

then they are enabled before the TLS handshake begins.

Hostname verification is performed after the TLS handshake completes.
The default hostname verification performs a match of the server's
hostname against the hostname information found in the server's certificate.
If this verification fails and no callback has been set via

setHostnameVerifier

then the negotiation fails.
If this verification fails and a callback has been set via

setHostnameVerifier

, then the callback is used to determine whether
the negotiation succeeds.

If an error occurs then the SSL socket is closed and an IOException
is thrown. The underlying connection remains intact.

Hostname verification is performed after the TLS handshake completes.
The default hostname verification performs a match of the server's
hostname against the hostname information found in the server's certificate.
If this verification fails and no callback has been set via

setHostnameVerifier

then the negotiation fails.
If this verification fails and a callback has been set via

setHostnameVerifier

, then the callback is used to determine whether
the negotiation succeeds.

If an error occurs then the SSL socket is closed and an IOException
is thrown. The underlying connection remains intact.

If an error occurs then the SSL socket is closed and an IOException
is thrown. The underlying connection remains intact.

close

```java
public abstract void close()
throws
IOException
```

Closes the TLS connection gracefully and reverts back to the underlying
connection.

**Throws:** IOException

- If an IO error was encountered while closing the
TLS connection

---

#### close

public abstract void close()
throws

IOException

Closes the TLS connection gracefully and reverts back to the underlying
connection.

---

