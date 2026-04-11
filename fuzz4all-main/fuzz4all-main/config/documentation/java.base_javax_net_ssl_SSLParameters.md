# Class SSLParameters

**Source:** `java.base\javax\net\ssl\SSLParameters.html`

### Class Description

```java
public class
SSLParameters

extends
Object
```

Encapsulates parameters for an SSL/TLS/DTLS connection. The parameters
are the list of ciphersuites to be accepted in an SSL/TLS/DTLS handshake,
the list of protocols to be allowed, the endpoint identification
algorithm during SSL/TLS/DTLS handshaking, the Server Name Indication (SNI),
the maximum network packet size, the algorithm constraints and whether
SSL/TLS/DTLS servers should request or require client authentication, etc.

SSLParameters can be created via the constructors in this class.
Objects can also be obtained using the

getSSLParameters()

methods in

SSLSocket

and

SSLServerSocket

and

SSLEngine

or the

getDefaultSSLParameters()

and

getSupportedSSLParameters()

methods in

SSLContext

.

SSLParameters can be applied to a connection via the methods

SSLSocket.setSSLParameters()

and

SSLServerSocket.setSSLParameters()

and

SSLEngine.setSSLParameters()

.

For example:

```java
SSLParameters p = sslSocket.getSSLParameters();
p.setProtocols(new String[] { "TLSv1.2" });
p.setCipherSuites(
new String[] { "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256", ... });
p.setApplicationProtocols(new String[] {"h2", "http/1.1"});
sslSocket.setSSLParameters(p);
```

**Since:** 1.6
**See Also:** SSLSocket

,

SSLEngine

,

SSLContext

---

### Field Details

*No entries found.*

### Constructor Details

#### public SSLParameters()

Constructs SSLParameters.

The values of cipherSuites, protocols, cryptographic algorithm
constraints, endpoint identification algorithm, server names and
server name matchers are set to

null

; useCipherSuitesOrder,
wantClientAuth and needClientAuth are set to

false

;
enableRetransmissions is set to

true

; maximum network packet
size is set to

0

.

---

#### public SSLParameters​(
String
[] cipherSuites)

Constructs SSLParameters from the specified array of ciphersuites.

Calling this constructor is equivalent to calling the no-args
constructor followed by

setCipherSuites(cipherSuites);

. Note that the
standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list.

**Parameters:**
- cipherSuites

- the array of ciphersuites (or null)

---

#### public SSLParameters​(
String
[] cipherSuites,

String
[] protocols)

Constructs SSLParameters from the specified array of ciphersuites
and protocols.

Calling this constructor is equivalent to calling the no-args
constructor followed by

setCipherSuites(cipherSuites); setProtocols(protocols);

.
Note that the standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list.

**Parameters:**
- cipherSuites

- the array of ciphersuites (or null)
- protocols

- the array of protocols (or null)

---

### Method Details

#### public
String
[] getCipherSuites()

Returns a copy of the array of ciphersuites or null if none
have been set.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:**
- a copy of the array of ciphersuites or null if none
have been set.

---

#### public void setCipherSuites​(
String
[] cipherSuites)

Sets the array of ciphersuites.

**Parameters:**
- cipherSuites

- the array of ciphersuites (or null). Note that the
standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list or might not
use the recommended name for a certain cipher suite.

---

#### public
String
[] getProtocols()

Returns a copy of the array of protocols or null if none
have been set.

**Returns:**
- a copy of the array of protocols or null if none
have been set.

---

#### public void setProtocols​(
String
[] protocols)

Sets the array of protocols.

**Parameters:**
- protocols

- the array of protocols (or null)

---

#### public boolean getWantClientAuth()

Returns whether client authentication should be requested.

**Returns:**
- whether client authentication should be requested.

---

#### public void setWantClientAuth​(boolean wantClientAuth)

Sets whether client authentication should be requested. Calling
this method clears the

needClientAuth

flag.

**Parameters:**
- wantClientAuth

- whether client authentication should be requested

---

#### public boolean getNeedClientAuth()

Returns whether client authentication should be required.

**Returns:**
- whether client authentication should be required.

---

#### public void setNeedClientAuth​(boolean needClientAuth)

Sets whether client authentication should be required. Calling
this method clears the

wantClientAuth

flag.

**Parameters:**
- needClientAuth

- whether client authentication should be required

---

#### public
AlgorithmConstraints
getAlgorithmConstraints()

Returns the cryptographic algorithm constraints.

**Returns:**
- the cryptographic algorithm constraints, or null if the
constraints have not been set

**See Also:**
- setAlgorithmConstraints(AlgorithmConstraints)

**Since:**
- 1.7

---

#### public void setAlgorithmConstraints​(
AlgorithmConstraints
constraints)

Sets the cryptographic algorithm constraints, which will be used
in addition to any configured by the runtime environment.

If the

constraints

parameter is non-null, every
cryptographic algorithm, key and algorithm parameters used in the
SSL/TLS/DTLS handshake must be permitted by the constraints.

**Parameters:**
- constraints

- the algorithm constraints (or null)

**Since:**
- 1.7

---

#### public
String
getEndpointIdentificationAlgorithm()

Gets the endpoint identification algorithm.

**Returns:**
- the endpoint identification algorithm, or null if none
has been set.

**See Also:**
- X509ExtendedTrustManager

,

setEndpointIdentificationAlgorithm(String)

**Since:**
- 1.7

---

#### public void setEndpointIdentificationAlgorithm​(
String
algorithm)

Sets the endpoint identification algorithm.

If the

algorithm

parameter is non-null or non-empty, the
endpoint identification/verification procedures must be handled during
SSL/TLS/DTLS handshaking. This is to prevent man-in-the-middle attacks.

**Parameters:**
- algorithm

- The standard string name of the endpoint
identification algorithm (or null).
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.

**See Also:**
- X509ExtendedTrustManager

**Since:**
- 1.7

---

#### public final void setServerNames​(
List
<
SNIServerName
> serverNames)

Sets the desired

SNIServerName

s of the Server Name
Indication (SNI) parameter.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in client mode.

Note that the

serverNames

list is cloned
to protect against subsequent modification.

**Parameters:**
- serverNames

- the list of desired

SNIServerName

s (or null)

**Throws:**
- NullPointerException

- if the

serverNames

contains

null

element
- IllegalArgumentException

- if the

serverNames

contains more than one name of the same name type

**See Also:**
- SNIServerName

,

getServerNames()

**Since:**
- 1.8

---

#### public final
List
<
SNIServerName
> getServerNames()

Returns a

List

containing all

SNIServerName

s of the
Server Name Indication (SNI) parameter, or null if none has been set.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in client mode.

For SSL/TLS/DTLS connections, the underlying SSL/TLS/DTLS provider
may specify a default value for a certain server name type. In
client mode, it is recommended that, by default, providers should
include the server name indication whenever the server can be located
by a supported server name type.

It is recommended that providers initialize default Server Name
Indications when creating

SSLSocket

/

SSLEngine

s.
In the following examples, the server name could be represented by an
instance of

SNIHostName

which has been initialized with the
hostname "www.example.com" and type

StandardConstants.SNI_HOST_NAME

.

```java
Socket socket =
sslSocketFactory.createSocket("www.example.com", 443);
```

or

```java
SSLEngine engine =
sslContext.createSSLEngine("www.example.com", 443);
```

**Returns:**
- null or an immutable list of non-null

SNIServerName

s

**See Also:**
- List

,

setServerNames(List)

**Since:**
- 1.8

---

#### public final void setSNIMatchers​(
Collection
<
SNIMatcher
> matchers)

Sets the

SNIMatcher

s of the Server Name Indication (SNI)
parameter.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in server mode.

Note that the

matchers

collection is cloned to protect
against subsequent modification.

**Parameters:**
- matchers

- the collection of

SNIMatcher

s (or null)

**Throws:**
- NullPointerException

- if the

matchers

contains

null

element
- IllegalArgumentException

- if the

matchers

contains more than one name of the same name type

**See Also:**
- Collection

,

SNIMatcher

,

getSNIMatchers()

**Since:**
- 1.8

---

#### public final
Collection
<
SNIMatcher
> getSNIMatchers()

Returns a

Collection

containing all

SNIMatcher

s of the
Server Name Indication (SNI) parameter, or null if none has been set.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in server mode.

For better interoperability, providers generally will not define
default matchers so that by default servers will ignore the SNI
extension and continue the handshake.

**Returns:**
- null or an immutable collection of non-null

SNIMatcher

s

**See Also:**
- SNIMatcher

,

setSNIMatchers(Collection)

**Since:**
- 1.8

---

#### public final void setUseCipherSuitesOrder​(boolean honorOrder)

Sets whether the local cipher suites preference should be honored.

**Parameters:**
- honorOrder

- whether local cipher suites order in

#getCipherSuites

should be honored during
SSL/TLS/DTLS handshaking.

**See Also:**
- getUseCipherSuitesOrder()

**Since:**
- 1.8

---

#### public final boolean getUseCipherSuitesOrder()

Returns whether the local cipher suites preference should be honored.

**Returns:**
- whether local cipher suites order in

#getCipherSuites

should be honored during SSL/TLS/DTLS handshaking.

**See Also:**
- setUseCipherSuitesOrder(boolean)

**Since:**
- 1.8

---

#### public void setEnableRetransmissions​(boolean enableRetransmissions)

Sets whether DTLS handshake retransmissions should be enabled.

This method only applies to DTLS.

**Parameters:**
- enableRetransmissions

-

true

indicates that DTLS handshake retransmissions
should be enabled;

false

indicates that DTLS handshake
retransmissions should be disabled

**See Also:**
- getEnableRetransmissions()

**Since:**
- 9

---

#### public boolean getEnableRetransmissions()

Returns whether DTLS handshake retransmissions should be enabled.

This method only applies to DTLS.

**Returns:**
- true, if DTLS handshake retransmissions should be enabled

**See Also:**
- setEnableRetransmissions(boolean)

**Since:**
- 9

---

#### public void setMaximumPacketSize​(int maximumPacketSize)

Sets the maximum expected network packet size in bytes for
SSL/TLS/DTLS records.

**Parameters:**
- maximumPacketSize

- the maximum expected network packet size in bytes, or

0

to use the implicit size that is automatically
specified by the underlying implementation.

**Throws:**
- IllegalArgumentException

- if

maximumPacketSize

is negative.

**See Also:**
- getMaximumPacketSize()

**Since:**
- 9

**API Note:**
- It is recommended that if possible, the maximum packet size
should not be less than 256 bytes so that small handshake
messages, such as HelloVerifyRequests, are not fragmented.

**Implementation Note:**
- If the maximum packet size is too small to hold a minimal
record, an implementation may attempt to generate as minimal
records as possible. However, this may cause a generated
packet to be larger than the maximum packet size.

---

#### public int getMaximumPacketSize()

Returns the maximum expected network packet size in bytes for
SSL/TLS/DTLS records.

**Returns:**
- the maximum expected network packet size, or

0

if
use the implicit size that is automatically specified by
the underlying implementation and this object has not been
populated by any connection.

**See Also:**
- setMaximumPacketSize(int)

**Since:**
- 9

**API Note:**
- The implicit size may not be a fixed value, especially
for a DTLS protocols implementation.

**Implementation Note:**
- For SSL/TLS/DTLS connections, the underlying provider
should calculate and specify the implicit value of the
maximum expected network packet size if it is not
configured explicitly. For any connection populated
object, this method should never return

0

so
that applications can retrieve the actual implicit size
of the underlying implementation.

An implementation should attempt to comply with the maximum
packet size configuration. However, if the maximum packet
size is too small to hold a minimal record, an implementation
may try to generate as minimal records as possible. This
may cause a generated packet to be larger than the maximum
packet size.

---

#### public
String
[] getApplicationProtocols()

Returns a prioritized array of application-layer protocol names that
can be negotiated over the SSL/TLS/DTLS protocols.

The array could be empty (zero-length), in which case protocol
indications will not be used.

This method will return a new array each time it is invoked.

**Returns:**
- a non-null, possibly zero-length array of application protocol

String

s. The array is ordered based on protocol
preference, with

protocols[0]

being the most preferred.

**See Also:**
- setApplicationProtocols(java.lang.String[])

**Since:**
- 9

---

#### public void setApplicationProtocols​(
String
[] protocols)

Sets the prioritized array of application-layer protocol names that
can be negotiated over the SSL/TLS/DTLS protocols.

If application-layer protocols are supported by the underlying
SSL/TLS implementation, this method configures which values can
be negotiated by protocols such as

RFC 7301

, the
Application Layer Protocol Negotiation (ALPN).

If this end of the connection is expected to offer application protocol
values, all protocols configured by this method will be sent to the
peer.

If this end of the connection is expected to select the application
protocol value, the

protocols

configured by this method are
compared with those sent by the peer. The first matched value becomes
the negotiated value. If none of the

protocols

were actually
requested by the peer, the underlying protocol will determine what
action to take. (For example, ALPN will send a

"no_application_protocol"

alert and terminate the connection.)

**Parameters:**
- protocols

- an ordered array of application protocols,
with

protocols[0]

being the most preferred.
If the array is empty (zero-length), protocol
indications will not be used.

**Throws:**
- IllegalArgumentException

- if protocols is null, or if
any element in a non-empty array is null or an
empty (zero-length) string

**See Also:**
- getApplicationProtocols()

**Since:**
- 9

**Implementation Requirements:**
- This method will make a copy of the

protocols

array.

---

### Additional Sections

#### Class SSLParameters

java.lang.Object

- javax.net.ssl.SSLParameters

javax.net.ssl.SSLParameters

```java
public class
SSLParameters

extends
Object
```

Encapsulates parameters for an SSL/TLS/DTLS connection. The parameters
are the list of ciphersuites to be accepted in an SSL/TLS/DTLS handshake,
the list of protocols to be allowed, the endpoint identification
algorithm during SSL/TLS/DTLS handshaking, the Server Name Indication (SNI),
the maximum network packet size, the algorithm constraints and whether
SSL/TLS/DTLS servers should request or require client authentication, etc.

SSLParameters can be created via the constructors in this class.
Objects can also be obtained using the

getSSLParameters()

methods in

SSLSocket

and

SSLServerSocket

and

SSLEngine

or the

getDefaultSSLParameters()

and

getSupportedSSLParameters()

methods in

SSLContext

.

SSLParameters can be applied to a connection via the methods

SSLSocket.setSSLParameters()

and

SSLServerSocket.setSSLParameters()

and

SSLEngine.setSSLParameters()

.

For example:

```java
SSLParameters p = sslSocket.getSSLParameters();
p.setProtocols(new String[] { "TLSv1.2" });
p.setCipherSuites(
new String[] { "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256", ... });
p.setApplicationProtocols(new String[] {"h2", "http/1.1"});
sslSocket.setSSLParameters(p);
```

**Since:** 1.6
**See Also:** SSLSocket

,

SSLEngine

,

SSLContext

public class

SSLParameters

extends

Object

Encapsulates parameters for an SSL/TLS/DTLS connection. The parameters
are the list of ciphersuites to be accepted in an SSL/TLS/DTLS handshake,
the list of protocols to be allowed, the endpoint identification
algorithm during SSL/TLS/DTLS handshaking, the Server Name Indication (SNI),
the maximum network packet size, the algorithm constraints and whether
SSL/TLS/DTLS servers should request or require client authentication, etc.

SSLParameters can be created via the constructors in this class.
Objects can also be obtained using the

getSSLParameters()

methods in

SSLSocket

and

SSLServerSocket

and

SSLEngine

or the

getDefaultSSLParameters()

and

getSupportedSSLParameters()

methods in

SSLContext

.

SSLParameters can be applied to a connection via the methods

SSLSocket.setSSLParameters()

and

SSLServerSocket.setSSLParameters()

and

SSLEngine.setSSLParameters()

.

For example:

```java
SSLParameters p = sslSocket.getSSLParameters();
p.setProtocols(new String[] { "TLSv1.2" });
p.setCipherSuites(
new String[] { "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256", ... });
p.setApplicationProtocols(new String[] {"h2", "http/1.1"});
sslSocket.setSSLParameters(p);
```

SSLParameters can be created via the constructors in this class.
Objects can also be obtained using the

getSSLParameters()

methods in

SSLSocket

and

SSLServerSocket

and

SSLEngine

or the

getDefaultSSLParameters()

and

getSupportedSSLParameters()

methods in

SSLContext

.

SSLParameters can be applied to a connection via the methods

SSLSocket.setSSLParameters()

and

SSLServerSocket.setSSLParameters()

and

SSLEngine.setSSLParameters()

.

For example:

```java
SSLParameters p = sslSocket.getSSLParameters();
p.setProtocols(new String[] { "TLSv1.2" });
p.setCipherSuites(
new String[] { "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256", ... });
p.setApplicationProtocols(new String[] {"h2", "http/1.1"});
sslSocket.setSSLParameters(p);
```

SSLParameters can be applied to a connection via the methods

SSLSocket.setSSLParameters()

and

SSLServerSocket.setSSLParameters()

and

SSLEngine.setSSLParameters()

.

For example:

```java
SSLParameters p = sslSocket.getSSLParameters();
p.setProtocols(new String[] { "TLSv1.2" });
p.setCipherSuites(
new String[] { "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256", ... });
p.setApplicationProtocols(new String[] {"h2", "http/1.1"});
sslSocket.setSSLParameters(p);
```

For example:

```java
SSLParameters p = sslSocket.getSSLParameters();
p.setProtocols(new String[] { "TLSv1.2" });
p.setCipherSuites(
new String[] { "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256", ... });
p.setApplicationProtocols(new String[] {"h2", "http/1.1"});
sslSocket.setSSLParameters(p);
```

SSLParameters p = sslSocket.getSSLParameters();
p.setProtocols(new String[] { "TLSv1.2" });
p.setCipherSuites(
new String[] { "TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256", ... });
p.setApplicationProtocols(new String[] {"h2", "http/1.1"});
sslSocket.setSSLParameters(p);

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SSLParameters

()

Constructs SSLParameters.

SSLParameters

​(

String

[] cipherSuites)

Constructs SSLParameters from the specified array of ciphersuites.

SSLParameters

​(

String

[] cipherSuites,

String

[] protocols)

Constructs SSLParameters from the specified array of ciphersuites
and protocols.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AlgorithmConstraints

getAlgorithmConstraints

()

Returns the cryptographic algorithm constraints.

String

[]

getApplicationProtocols

()

Returns a prioritized array of application-layer protocol names that
can be negotiated over the SSL/TLS/DTLS protocols.

String

[]

getCipherSuites

()

Returns a copy of the array of ciphersuites or null if none
have been set.

boolean

getEnableRetransmissions

()

Returns whether DTLS handshake retransmissions should be enabled.

String

getEndpointIdentificationAlgorithm

()

Gets the endpoint identification algorithm.

int

getMaximumPacketSize

()

Returns the maximum expected network packet size in bytes for
SSL/TLS/DTLS records.

boolean

getNeedClientAuth

()

Returns whether client authentication should be required.

String

[]

getProtocols

()

Returns a copy of the array of protocols or null if none
have been set.

List

<

SNIServerName

>

getServerNames

()

Returns a

List

containing all

SNIServerName

s of the
Server Name Indication (SNI) parameter, or null if none has been set.

Collection

<

SNIMatcher

>

getSNIMatchers

()

Returns a

Collection

containing all

SNIMatcher

s of the
Server Name Indication (SNI) parameter, or null if none has been set.

boolean

getUseCipherSuitesOrder

()

Returns whether the local cipher suites preference should be honored.

boolean

getWantClientAuth

()

Returns whether client authentication should be requested.

void

setAlgorithmConstraints

​(

AlgorithmConstraints

constraints)

Sets the cryptographic algorithm constraints, which will be used
in addition to any configured by the runtime environment.

void

setApplicationProtocols

​(

String

[] protocols)

Sets the prioritized array of application-layer protocol names that
can be negotiated over the SSL/TLS/DTLS protocols.

void

setCipherSuites

​(

String

[] cipherSuites)

Sets the array of ciphersuites.

void

setEnableRetransmissions

​(boolean enableRetransmissions)

Sets whether DTLS handshake retransmissions should be enabled.

void

setEndpointIdentificationAlgorithm

​(

String

algorithm)

Sets the endpoint identification algorithm.

void

setMaximumPacketSize

​(int maximumPacketSize)

Sets the maximum expected network packet size in bytes for
SSL/TLS/DTLS records.

void

setNeedClientAuth

​(boolean needClientAuth)

Sets whether client authentication should be required.

void

setProtocols

​(

String

[] protocols)

Sets the array of protocols.

void

setServerNames

​(

List

<

SNIServerName

> serverNames)

Sets the desired

SNIServerName

s of the Server Name
Indication (SNI) parameter.

void

setSNIMatchers

​(

Collection

<

SNIMatcher

> matchers)

Sets the

SNIMatcher

s of the Server Name Indication (SNI)
parameter.

void

setUseCipherSuitesOrder

​(boolean honorOrder)

Sets whether the local cipher suites preference should be honored.

void

setWantClientAuth

​(boolean wantClientAuth)

Sets whether client authentication should be requested.

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

SSLParameters

()

Constructs SSLParameters.

SSLParameters

​(

String

[] cipherSuites)

Constructs SSLParameters from the specified array of ciphersuites.

SSLParameters

​(

String

[] cipherSuites,

String

[] protocols)

Constructs SSLParameters from the specified array of ciphersuites
and protocols.

---

#### Constructor Summary

Constructs SSLParameters.

Constructs SSLParameters from the specified array of ciphersuites.

Constructs SSLParameters from the specified array of ciphersuites
and protocols.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

AlgorithmConstraints

getAlgorithmConstraints

()

Returns the cryptographic algorithm constraints.

String

[]

getApplicationProtocols

()

Returns a prioritized array of application-layer protocol names that
can be negotiated over the SSL/TLS/DTLS protocols.

String

[]

getCipherSuites

()

Returns a copy of the array of ciphersuites or null if none
have been set.

boolean

getEnableRetransmissions

()

Returns whether DTLS handshake retransmissions should be enabled.

String

getEndpointIdentificationAlgorithm

()

Gets the endpoint identification algorithm.

int

getMaximumPacketSize

()

Returns the maximum expected network packet size in bytes for
SSL/TLS/DTLS records.

boolean

getNeedClientAuth

()

Returns whether client authentication should be required.

String

[]

getProtocols

()

Returns a copy of the array of protocols or null if none
have been set.

List

<

SNIServerName

>

getServerNames

()

Returns a

List

containing all

SNIServerName

s of the
Server Name Indication (SNI) parameter, or null if none has been set.

Collection

<

SNIMatcher

>

getSNIMatchers

()

Returns a

Collection

containing all

SNIMatcher

s of the
Server Name Indication (SNI) parameter, or null if none has been set.

boolean

getUseCipherSuitesOrder

()

Returns whether the local cipher suites preference should be honored.

boolean

getWantClientAuth

()

Returns whether client authentication should be requested.

void

setAlgorithmConstraints

​(

AlgorithmConstraints

constraints)

Sets the cryptographic algorithm constraints, which will be used
in addition to any configured by the runtime environment.

void

setApplicationProtocols

​(

String

[] protocols)

Sets the prioritized array of application-layer protocol names that
can be negotiated over the SSL/TLS/DTLS protocols.

void

setCipherSuites

​(

String

[] cipherSuites)

Sets the array of ciphersuites.

void

setEnableRetransmissions

​(boolean enableRetransmissions)

Sets whether DTLS handshake retransmissions should be enabled.

void

setEndpointIdentificationAlgorithm

​(

String

algorithm)

Sets the endpoint identification algorithm.

void

setMaximumPacketSize

​(int maximumPacketSize)

Sets the maximum expected network packet size in bytes for
SSL/TLS/DTLS records.

void

setNeedClientAuth

​(boolean needClientAuth)

Sets whether client authentication should be required.

void

setProtocols

​(

String

[] protocols)

Sets the array of protocols.

void

setServerNames

​(

List

<

SNIServerName

> serverNames)

Sets the desired

SNIServerName

s of the Server Name
Indication (SNI) parameter.

void

setSNIMatchers

​(

Collection

<

SNIMatcher

> matchers)

Sets the

SNIMatcher

s of the Server Name Indication (SNI)
parameter.

void

setUseCipherSuitesOrder

​(boolean honorOrder)

Sets whether the local cipher suites preference should be honored.

void

setWantClientAuth

​(boolean wantClientAuth)

Sets whether client authentication should be requested.

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

Returns the cryptographic algorithm constraints.

Returns a prioritized array of application-layer protocol names that
can be negotiated over the SSL/TLS/DTLS protocols.

Returns a copy of the array of ciphersuites or null if none
have been set.

Returns whether DTLS handshake retransmissions should be enabled.

Gets the endpoint identification algorithm.

Returns the maximum expected network packet size in bytes for
SSL/TLS/DTLS records.

Returns whether client authentication should be required.

Returns a copy of the array of protocols or null if none
have been set.

Returns a

List

containing all

SNIServerName

s of the
Server Name Indication (SNI) parameter, or null if none has been set.

Returns a

Collection

containing all

SNIMatcher

s of the
Server Name Indication (SNI) parameter, or null if none has been set.

Returns whether the local cipher suites preference should be honored.

Returns whether client authentication should be requested.

Sets the cryptographic algorithm constraints, which will be used
in addition to any configured by the runtime environment.

Sets the prioritized array of application-layer protocol names that
can be negotiated over the SSL/TLS/DTLS protocols.

Sets the array of ciphersuites.

Sets whether DTLS handshake retransmissions should be enabled.

Sets the endpoint identification algorithm.

Sets the maximum expected network packet size in bytes for
SSL/TLS/DTLS records.

Sets whether client authentication should be required.

Sets the array of protocols.

Sets the desired

SNIServerName

s of the Server Name
Indication (SNI) parameter.

Sets the

SNIMatcher

s of the Server Name Indication (SNI)
parameter.

Sets whether the local cipher suites preference should be honored.

Sets whether client authentication should be requested.

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

- SSLParameters

```java
public SSLParameters()
```

Constructs SSLParameters.

The values of cipherSuites, protocols, cryptographic algorithm
constraints, endpoint identification algorithm, server names and
server name matchers are set to

null

; useCipherSuitesOrder,
wantClientAuth and needClientAuth are set to

false

;
enableRetransmissions is set to

true

; maximum network packet
size is set to

0

.

- SSLParameters

```java
public SSLParameters​(
String
[] cipherSuites)
```

Constructs SSLParameters from the specified array of ciphersuites.

Calling this constructor is equivalent to calling the no-args
constructor followed by

setCipherSuites(cipherSuites);

. Note that the
standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list.

**Parameters:** cipherSuites

- the array of ciphersuites (or null)

- SSLParameters

```java
public SSLParameters​(
String
[] cipherSuites,

String
[] protocols)
```

Constructs SSLParameters from the specified array of ciphersuites
and protocols.

Calling this constructor is equivalent to calling the no-args
constructor followed by

setCipherSuites(cipherSuites); setProtocols(protocols);

.
Note that the standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list.

**Parameters:** cipherSuites

- the array of ciphersuites (or null)
**Parameters:** protocols

- the array of protocols (or null)

============ METHOD DETAIL ==========

- Method Detail

- getCipherSuites

```java
public
String
[] getCipherSuites()
```

Returns a copy of the array of ciphersuites or null if none
have been set.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:** a copy of the array of ciphersuites or null if none
have been set.

- setCipherSuites

```java
public void setCipherSuites​(
String
[] cipherSuites)
```

Sets the array of ciphersuites.

**Parameters:** cipherSuites

- the array of ciphersuites (or null). Note that the
standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list or might not
use the recommended name for a certain cipher suite.

- getProtocols

```java
public
String
[] getProtocols()
```

Returns a copy of the array of protocols or null if none
have been set.

**Returns:** a copy of the array of protocols or null if none
have been set.

- setProtocols

```java
public void setProtocols​(
String
[] protocols)
```

Sets the array of protocols.

**Parameters:** protocols

- the array of protocols (or null)

- getWantClientAuth

```java
public boolean getWantClientAuth()
```

Returns whether client authentication should be requested.

**Returns:** whether client authentication should be requested.

- setWantClientAuth

```java
public void setWantClientAuth​(boolean wantClientAuth)
```

Sets whether client authentication should be requested. Calling
this method clears the

needClientAuth

flag.

**Parameters:** wantClientAuth

- whether client authentication should be requested

- getNeedClientAuth

```java
public boolean getNeedClientAuth()
```

Returns whether client authentication should be required.

**Returns:** whether client authentication should be required.

- setNeedClientAuth

```java
public void setNeedClientAuth​(boolean needClientAuth)
```

Sets whether client authentication should be required. Calling
this method clears the

wantClientAuth

flag.

**Parameters:** needClientAuth

- whether client authentication should be required

- getAlgorithmConstraints

```java
public
AlgorithmConstraints
getAlgorithmConstraints()
```

Returns the cryptographic algorithm constraints.

**Returns:** the cryptographic algorithm constraints, or null if the
constraints have not been set
**Since:** 1.7
**See Also:** setAlgorithmConstraints(AlgorithmConstraints)

- setAlgorithmConstraints

```java
public void setAlgorithmConstraints​(
AlgorithmConstraints
constraints)
```

Sets the cryptographic algorithm constraints, which will be used
in addition to any configured by the runtime environment.

If the

constraints

parameter is non-null, every
cryptographic algorithm, key and algorithm parameters used in the
SSL/TLS/DTLS handshake must be permitted by the constraints.

**Parameters:** constraints

- the algorithm constraints (or null)
**Since:** 1.7

- getEndpointIdentificationAlgorithm

```java
public
String
getEndpointIdentificationAlgorithm()
```

Gets the endpoint identification algorithm.

**Returns:** the endpoint identification algorithm, or null if none
has been set.
**Since:** 1.7
**See Also:** X509ExtendedTrustManager

,

setEndpointIdentificationAlgorithm(String)

- setEndpointIdentificationAlgorithm

```java
public void setEndpointIdentificationAlgorithm​(
String
algorithm)
```

Sets the endpoint identification algorithm.

If the

algorithm

parameter is non-null or non-empty, the
endpoint identification/verification procedures must be handled during
SSL/TLS/DTLS handshaking. This is to prevent man-in-the-middle attacks.

**Parameters:** algorithm

- The standard string name of the endpoint
identification algorithm (or null).
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
**Since:** 1.7
**See Also:** X509ExtendedTrustManager

- setServerNames

```java
public final void setServerNames​(
List
<
SNIServerName
> serverNames)
```

Sets the desired

SNIServerName

s of the Server Name
Indication (SNI) parameter.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in client mode.

Note that the

serverNames

list is cloned
to protect against subsequent modification.

**Parameters:** serverNames

- the list of desired

SNIServerName

s (or null)
**Throws:** NullPointerException

- if the

serverNames

contains

null

element
**Throws:** IllegalArgumentException

- if the

serverNames

contains more than one name of the same name type
**Since:** 1.8
**See Also:** SNIServerName

,

getServerNames()

- getServerNames

```java
public final
List
<
SNIServerName
> getServerNames()
```

Returns a

List

containing all

SNIServerName

s of the
Server Name Indication (SNI) parameter, or null if none has been set.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in client mode.

For SSL/TLS/DTLS connections, the underlying SSL/TLS/DTLS provider
may specify a default value for a certain server name type. In
client mode, it is recommended that, by default, providers should
include the server name indication whenever the server can be located
by a supported server name type.

It is recommended that providers initialize default Server Name
Indications when creating

SSLSocket

/

SSLEngine

s.
In the following examples, the server name could be represented by an
instance of

SNIHostName

which has been initialized with the
hostname "www.example.com" and type

StandardConstants.SNI_HOST_NAME

.

```java
Socket socket =
sslSocketFactory.createSocket("www.example.com", 443);
```

or

```java
SSLEngine engine =
sslContext.createSSLEngine("www.example.com", 443);
```

**Returns:** null or an immutable list of non-null

SNIServerName

s
**Since:** 1.8
**See Also:** List

,

setServerNames(List)

- setSNIMatchers

```java
public final void setSNIMatchers​(
Collection
<
SNIMatcher
> matchers)
```

Sets the

SNIMatcher

s of the Server Name Indication (SNI)
parameter.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in server mode.

Note that the

matchers

collection is cloned to protect
against subsequent modification.

**Parameters:** matchers

- the collection of

SNIMatcher

s (or null)
**Throws:** NullPointerException

- if the

matchers

contains

null

element
**Throws:** IllegalArgumentException

- if the

matchers

contains more than one name of the same name type
**Since:** 1.8
**See Also:** Collection

,

SNIMatcher

,

getSNIMatchers()

- getSNIMatchers

```java
public final
Collection
<
SNIMatcher
> getSNIMatchers()
```

Returns a

Collection

containing all

SNIMatcher

s of the
Server Name Indication (SNI) parameter, or null if none has been set.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in server mode.

For better interoperability, providers generally will not define
default matchers so that by default servers will ignore the SNI
extension and continue the handshake.

**Returns:** null or an immutable collection of non-null

SNIMatcher

s
**Since:** 1.8
**See Also:** SNIMatcher

,

setSNIMatchers(Collection)

- setUseCipherSuitesOrder

```java
public final void setUseCipherSuitesOrder​(boolean honorOrder)
```

Sets whether the local cipher suites preference should be honored.

**Parameters:** honorOrder

- whether local cipher suites order in

#getCipherSuites

should be honored during
SSL/TLS/DTLS handshaking.
**Since:** 1.8
**See Also:** getUseCipherSuitesOrder()

- getUseCipherSuitesOrder

```java
public final boolean getUseCipherSuitesOrder()
```

Returns whether the local cipher suites preference should be honored.

**Returns:** whether local cipher suites order in

#getCipherSuites

should be honored during SSL/TLS/DTLS handshaking.
**Since:** 1.8
**See Also:** setUseCipherSuitesOrder(boolean)

- setEnableRetransmissions

```java
public void setEnableRetransmissions​(boolean enableRetransmissions)
```

Sets whether DTLS handshake retransmissions should be enabled.

This method only applies to DTLS.

**Parameters:** enableRetransmissions

-

true

indicates that DTLS handshake retransmissions
should be enabled;

false

indicates that DTLS handshake
retransmissions should be disabled
**Since:** 9
**See Also:** getEnableRetransmissions()

- getEnableRetransmissions

```java
public boolean getEnableRetransmissions()
```

Returns whether DTLS handshake retransmissions should be enabled.

This method only applies to DTLS.

**Returns:** true, if DTLS handshake retransmissions should be enabled
**Since:** 9
**See Also:** setEnableRetransmissions(boolean)

- setMaximumPacketSize

```java
public void setMaximumPacketSize​(int maximumPacketSize)
```

Sets the maximum expected network packet size in bytes for
SSL/TLS/DTLS records.

**API Note:** It is recommended that if possible, the maximum packet size
should not be less than 256 bytes so that small handshake
messages, such as HelloVerifyRequests, are not fragmented.
**Implementation Note:** If the maximum packet size is too small to hold a minimal
record, an implementation may attempt to generate as minimal
records as possible. However, this may cause a generated
packet to be larger than the maximum packet size.
**Parameters:** maximumPacketSize

- the maximum expected network packet size in bytes, or

0

to use the implicit size that is automatically
specified by the underlying implementation.
**Throws:** IllegalArgumentException

- if

maximumPacketSize

is negative.
**Since:** 9
**See Also:** getMaximumPacketSize()

- getMaximumPacketSize

```java
public int getMaximumPacketSize()
```

Returns the maximum expected network packet size in bytes for
SSL/TLS/DTLS records.

**API Note:** The implicit size may not be a fixed value, especially
for a DTLS protocols implementation.
**Implementation Note:** For SSL/TLS/DTLS connections, the underlying provider
should calculate and specify the implicit value of the
maximum expected network packet size if it is not
configured explicitly. For any connection populated
object, this method should never return

0

so
that applications can retrieve the actual implicit size
of the underlying implementation.

An implementation should attempt to comply with the maximum
packet size configuration. However, if the maximum packet
size is too small to hold a minimal record, an implementation
may try to generate as minimal records as possible. This
may cause a generated packet to be larger than the maximum
packet size.
**Returns:** the maximum expected network packet size, or

0

if
use the implicit size that is automatically specified by
the underlying implementation and this object has not been
populated by any connection.
**Since:** 9
**See Also:** setMaximumPacketSize(int)

- getApplicationProtocols

```java
public
String
[] getApplicationProtocols()
```

Returns a prioritized array of application-layer protocol names that
can be negotiated over the SSL/TLS/DTLS protocols.

The array could be empty (zero-length), in which case protocol
indications will not be used.

This method will return a new array each time it is invoked.

**Returns:** a non-null, possibly zero-length array of application protocol

String

s. The array is ordered based on protocol
preference, with

protocols[0]

being the most preferred.
**Since:** 9
**See Also:** setApplicationProtocols(java.lang.String[])

- setApplicationProtocols

```java
public void setApplicationProtocols​(
String
[] protocols)
```

Sets the prioritized array of application-layer protocol names that
can be negotiated over the SSL/TLS/DTLS protocols.

If application-layer protocols are supported by the underlying
SSL/TLS implementation, this method configures which values can
be negotiated by protocols such as

RFC 7301

, the
Application Layer Protocol Negotiation (ALPN).

If this end of the connection is expected to offer application protocol
values, all protocols configured by this method will be sent to the
peer.

If this end of the connection is expected to select the application
protocol value, the

protocols

configured by this method are
compared with those sent by the peer. The first matched value becomes
the negotiated value. If none of the

protocols

were actually
requested by the peer, the underlying protocol will determine what
action to take. (For example, ALPN will send a

"no_application_protocol"

alert and terminate the connection.)

**Implementation Requirements:** This method will make a copy of the

protocols

array.
**Parameters:** protocols

- an ordered array of application protocols,
with

protocols[0]

being the most preferred.
If the array is empty (zero-length), protocol
indications will not be used.
**Throws:** IllegalArgumentException

- if protocols is null, or if
any element in a non-empty array is null or an
empty (zero-length) string
**Since:** 9
**See Also:** getApplicationProtocols()

Constructor Detail

- SSLParameters

```java
public SSLParameters()
```

Constructs SSLParameters.

The values of cipherSuites, protocols, cryptographic algorithm
constraints, endpoint identification algorithm, server names and
server name matchers are set to

null

; useCipherSuitesOrder,
wantClientAuth and needClientAuth are set to

false

;
enableRetransmissions is set to

true

; maximum network packet
size is set to

0

.

- SSLParameters

```java
public SSLParameters​(
String
[] cipherSuites)
```

Constructs SSLParameters from the specified array of ciphersuites.

Calling this constructor is equivalent to calling the no-args
constructor followed by

setCipherSuites(cipherSuites);

. Note that the
standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list.

**Parameters:** cipherSuites

- the array of ciphersuites (or null)

- SSLParameters

```java
public SSLParameters​(
String
[] cipherSuites,

String
[] protocols)
```

Constructs SSLParameters from the specified array of ciphersuites
and protocols.

Calling this constructor is equivalent to calling the no-args
constructor followed by

setCipherSuites(cipherSuites); setProtocols(protocols);

.
Note that the standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list.

**Parameters:** cipherSuites

- the array of ciphersuites (or null)
**Parameters:** protocols

- the array of protocols (or null)

---

#### Constructor Detail

SSLParameters

```java
public SSLParameters()
```

Constructs SSLParameters.

The values of cipherSuites, protocols, cryptographic algorithm
constraints, endpoint identification algorithm, server names and
server name matchers are set to

null

; useCipherSuitesOrder,
wantClientAuth and needClientAuth are set to

false

;
enableRetransmissions is set to

true

; maximum network packet
size is set to

0

.

---

#### SSLParameters

public SSLParameters()

Constructs SSLParameters.

The values of cipherSuites, protocols, cryptographic algorithm
constraints, endpoint identification algorithm, server names and
server name matchers are set to

null

; useCipherSuitesOrder,
wantClientAuth and needClientAuth are set to

false

;
enableRetransmissions is set to

true

; maximum network packet
size is set to

0

.

The values of cipherSuites, protocols, cryptographic algorithm
constraints, endpoint identification algorithm, server names and
server name matchers are set to

null

; useCipherSuitesOrder,
wantClientAuth and needClientAuth are set to

false

;
enableRetransmissions is set to

true

; maximum network packet
size is set to

0

.

SSLParameters

```java
public SSLParameters​(
String
[] cipherSuites)
```

Constructs SSLParameters from the specified array of ciphersuites.

Calling this constructor is equivalent to calling the no-args
constructor followed by

setCipherSuites(cipherSuites);

. Note that the
standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list.

**Parameters:** cipherSuites

- the array of ciphersuites (or null)

---

#### SSLParameters

public SSLParameters​(

String

[] cipherSuites)

Constructs SSLParameters from the specified array of ciphersuites.

Calling this constructor is equivalent to calling the no-args
constructor followed by

setCipherSuites(cipherSuites);

. Note that the
standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list.

Calling this constructor is equivalent to calling the no-args
constructor followed by

setCipherSuites(cipherSuites);

. Note that the
standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list.

SSLParameters

```java
public SSLParameters​(
String
[] cipherSuites,

String
[] protocols)
```

Constructs SSLParameters from the specified array of ciphersuites
and protocols.

Calling this constructor is equivalent to calling the no-args
constructor followed by

setCipherSuites(cipherSuites); setProtocols(protocols);

.
Note that the standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list.

**Parameters:** cipherSuites

- the array of ciphersuites (or null)
**Parameters:** protocols

- the array of protocols (or null)

---

#### SSLParameters

public SSLParameters​(

String

[] cipherSuites,

String

[] protocols)

Constructs SSLParameters from the specified array of ciphersuites
and protocols.

Calling this constructor is equivalent to calling the no-args
constructor followed by

setCipherSuites(cipherSuites); setProtocols(protocols);

.
Note that the standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list.

Calling this constructor is equivalent to calling the no-args
constructor followed by

setCipherSuites(cipherSuites); setProtocols(protocols);

.
Note that the standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list.

Method Detail

- getCipherSuites

```java
public
String
[] getCipherSuites()
```

Returns a copy of the array of ciphersuites or null if none
have been set.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:** a copy of the array of ciphersuites or null if none
have been set.

- setCipherSuites

```java
public void setCipherSuites​(
String
[] cipherSuites)
```

Sets the array of ciphersuites.

**Parameters:** cipherSuites

- the array of ciphersuites (or null). Note that the
standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list or might not
use the recommended name for a certain cipher suite.

- getProtocols

```java
public
String
[] getProtocols()
```

Returns a copy of the array of protocols or null if none
have been set.

**Returns:** a copy of the array of protocols or null if none
have been set.

- setProtocols

```java
public void setProtocols​(
String
[] protocols)
```

Sets the array of protocols.

**Parameters:** protocols

- the array of protocols (or null)

- getWantClientAuth

```java
public boolean getWantClientAuth()
```

Returns whether client authentication should be requested.

**Returns:** whether client authentication should be requested.

- setWantClientAuth

```java
public void setWantClientAuth​(boolean wantClientAuth)
```

Sets whether client authentication should be requested. Calling
this method clears the

needClientAuth

flag.

**Parameters:** wantClientAuth

- whether client authentication should be requested

- getNeedClientAuth

```java
public boolean getNeedClientAuth()
```

Returns whether client authentication should be required.

**Returns:** whether client authentication should be required.

- setNeedClientAuth

```java
public void setNeedClientAuth​(boolean needClientAuth)
```

Sets whether client authentication should be required. Calling
this method clears the

wantClientAuth

flag.

**Parameters:** needClientAuth

- whether client authentication should be required

- getAlgorithmConstraints

```java
public
AlgorithmConstraints
getAlgorithmConstraints()
```

Returns the cryptographic algorithm constraints.

**Returns:** the cryptographic algorithm constraints, or null if the
constraints have not been set
**Since:** 1.7
**See Also:** setAlgorithmConstraints(AlgorithmConstraints)

- setAlgorithmConstraints

```java
public void setAlgorithmConstraints​(
AlgorithmConstraints
constraints)
```

Sets the cryptographic algorithm constraints, which will be used
in addition to any configured by the runtime environment.

If the

constraints

parameter is non-null, every
cryptographic algorithm, key and algorithm parameters used in the
SSL/TLS/DTLS handshake must be permitted by the constraints.

**Parameters:** constraints

- the algorithm constraints (or null)
**Since:** 1.7

- getEndpointIdentificationAlgorithm

```java
public
String
getEndpointIdentificationAlgorithm()
```

Gets the endpoint identification algorithm.

**Returns:** the endpoint identification algorithm, or null if none
has been set.
**Since:** 1.7
**See Also:** X509ExtendedTrustManager

,

setEndpointIdentificationAlgorithm(String)

- setEndpointIdentificationAlgorithm

```java
public void setEndpointIdentificationAlgorithm​(
String
algorithm)
```

Sets the endpoint identification algorithm.

If the

algorithm

parameter is non-null or non-empty, the
endpoint identification/verification procedures must be handled during
SSL/TLS/DTLS handshaking. This is to prevent man-in-the-middle attacks.

**Parameters:** algorithm

- The standard string name of the endpoint
identification algorithm (or null).
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
**Since:** 1.7
**See Also:** X509ExtendedTrustManager

- setServerNames

```java
public final void setServerNames​(
List
<
SNIServerName
> serverNames)
```

Sets the desired

SNIServerName

s of the Server Name
Indication (SNI) parameter.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in client mode.

Note that the

serverNames

list is cloned
to protect against subsequent modification.

**Parameters:** serverNames

- the list of desired

SNIServerName

s (or null)
**Throws:** NullPointerException

- if the

serverNames

contains

null

element
**Throws:** IllegalArgumentException

- if the

serverNames

contains more than one name of the same name type
**Since:** 1.8
**See Also:** SNIServerName

,

getServerNames()

- getServerNames

```java
public final
List
<
SNIServerName
> getServerNames()
```

Returns a

List

containing all

SNIServerName

s of the
Server Name Indication (SNI) parameter, or null if none has been set.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in client mode.

For SSL/TLS/DTLS connections, the underlying SSL/TLS/DTLS provider
may specify a default value for a certain server name type. In
client mode, it is recommended that, by default, providers should
include the server name indication whenever the server can be located
by a supported server name type.

It is recommended that providers initialize default Server Name
Indications when creating

SSLSocket

/

SSLEngine

s.
In the following examples, the server name could be represented by an
instance of

SNIHostName

which has been initialized with the
hostname "www.example.com" and type

StandardConstants.SNI_HOST_NAME

.

```java
Socket socket =
sslSocketFactory.createSocket("www.example.com", 443);
```

or

```java
SSLEngine engine =
sslContext.createSSLEngine("www.example.com", 443);
```

**Returns:** null or an immutable list of non-null

SNIServerName

s
**Since:** 1.8
**See Also:** List

,

setServerNames(List)

- setSNIMatchers

```java
public final void setSNIMatchers​(
Collection
<
SNIMatcher
> matchers)
```

Sets the

SNIMatcher

s of the Server Name Indication (SNI)
parameter.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in server mode.

Note that the

matchers

collection is cloned to protect
against subsequent modification.

**Parameters:** matchers

- the collection of

SNIMatcher

s (or null)
**Throws:** NullPointerException

- if the

matchers

contains

null

element
**Throws:** IllegalArgumentException

- if the

matchers

contains more than one name of the same name type
**Since:** 1.8
**See Also:** Collection

,

SNIMatcher

,

getSNIMatchers()

- getSNIMatchers

```java
public final
Collection
<
SNIMatcher
> getSNIMatchers()
```

Returns a

Collection

containing all

SNIMatcher

s of the
Server Name Indication (SNI) parameter, or null if none has been set.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in server mode.

For better interoperability, providers generally will not define
default matchers so that by default servers will ignore the SNI
extension and continue the handshake.

**Returns:** null or an immutable collection of non-null

SNIMatcher

s
**Since:** 1.8
**See Also:** SNIMatcher

,

setSNIMatchers(Collection)

- setUseCipherSuitesOrder

```java
public final void setUseCipherSuitesOrder​(boolean honorOrder)
```

Sets whether the local cipher suites preference should be honored.

**Parameters:** honorOrder

- whether local cipher suites order in

#getCipherSuites

should be honored during
SSL/TLS/DTLS handshaking.
**Since:** 1.8
**See Also:** getUseCipherSuitesOrder()

- getUseCipherSuitesOrder

```java
public final boolean getUseCipherSuitesOrder()
```

Returns whether the local cipher suites preference should be honored.

**Returns:** whether local cipher suites order in

#getCipherSuites

should be honored during SSL/TLS/DTLS handshaking.
**Since:** 1.8
**See Also:** setUseCipherSuitesOrder(boolean)

- setEnableRetransmissions

```java
public void setEnableRetransmissions​(boolean enableRetransmissions)
```

Sets whether DTLS handshake retransmissions should be enabled.

This method only applies to DTLS.

**Parameters:** enableRetransmissions

-

true

indicates that DTLS handshake retransmissions
should be enabled;

false

indicates that DTLS handshake
retransmissions should be disabled
**Since:** 9
**See Also:** getEnableRetransmissions()

- getEnableRetransmissions

```java
public boolean getEnableRetransmissions()
```

Returns whether DTLS handshake retransmissions should be enabled.

This method only applies to DTLS.

**Returns:** true, if DTLS handshake retransmissions should be enabled
**Since:** 9
**See Also:** setEnableRetransmissions(boolean)

- setMaximumPacketSize

```java
public void setMaximumPacketSize​(int maximumPacketSize)
```

Sets the maximum expected network packet size in bytes for
SSL/TLS/DTLS records.

**API Note:** It is recommended that if possible, the maximum packet size
should not be less than 256 bytes so that small handshake
messages, such as HelloVerifyRequests, are not fragmented.
**Implementation Note:** If the maximum packet size is too small to hold a minimal
record, an implementation may attempt to generate as minimal
records as possible. However, this may cause a generated
packet to be larger than the maximum packet size.
**Parameters:** maximumPacketSize

- the maximum expected network packet size in bytes, or

0

to use the implicit size that is automatically
specified by the underlying implementation.
**Throws:** IllegalArgumentException

- if

maximumPacketSize

is negative.
**Since:** 9
**See Also:** getMaximumPacketSize()

- getMaximumPacketSize

```java
public int getMaximumPacketSize()
```

Returns the maximum expected network packet size in bytes for
SSL/TLS/DTLS records.

**API Note:** The implicit size may not be a fixed value, especially
for a DTLS protocols implementation.
**Implementation Note:** For SSL/TLS/DTLS connections, the underlying provider
should calculate and specify the implicit value of the
maximum expected network packet size if it is not
configured explicitly. For any connection populated
object, this method should never return

0

so
that applications can retrieve the actual implicit size
of the underlying implementation.

An implementation should attempt to comply with the maximum
packet size configuration. However, if the maximum packet
size is too small to hold a minimal record, an implementation
may try to generate as minimal records as possible. This
may cause a generated packet to be larger than the maximum
packet size.
**Returns:** the maximum expected network packet size, or

0

if
use the implicit size that is automatically specified by
the underlying implementation and this object has not been
populated by any connection.
**Since:** 9
**See Also:** setMaximumPacketSize(int)

- getApplicationProtocols

```java
public
String
[] getApplicationProtocols()
```

Returns a prioritized array of application-layer protocol names that
can be negotiated over the SSL/TLS/DTLS protocols.

The array could be empty (zero-length), in which case protocol
indications will not be used.

This method will return a new array each time it is invoked.

**Returns:** a non-null, possibly zero-length array of application protocol

String

s. The array is ordered based on protocol
preference, with

protocols[0]

being the most preferred.
**Since:** 9
**See Also:** setApplicationProtocols(java.lang.String[])

- setApplicationProtocols

```java
public void setApplicationProtocols​(
String
[] protocols)
```

Sets the prioritized array of application-layer protocol names that
can be negotiated over the SSL/TLS/DTLS protocols.

If application-layer protocols are supported by the underlying
SSL/TLS implementation, this method configures which values can
be negotiated by protocols such as

RFC 7301

, the
Application Layer Protocol Negotiation (ALPN).

If this end of the connection is expected to offer application protocol
values, all protocols configured by this method will be sent to the
peer.

If this end of the connection is expected to select the application
protocol value, the

protocols

configured by this method are
compared with those sent by the peer. The first matched value becomes
the negotiated value. If none of the

protocols

were actually
requested by the peer, the underlying protocol will determine what
action to take. (For example, ALPN will send a

"no_application_protocol"

alert and terminate the connection.)

**Implementation Requirements:** This method will make a copy of the

protocols

array.
**Parameters:** protocols

- an ordered array of application protocols,
with

protocols[0]

being the most preferred.
If the array is empty (zero-length), protocol
indications will not be used.
**Throws:** IllegalArgumentException

- if protocols is null, or if
any element in a non-empty array is null or an
empty (zero-length) string
**Since:** 9
**See Also:** getApplicationProtocols()

---

#### Method Detail

getCipherSuites

```java
public
String
[] getCipherSuites()
```

Returns a copy of the array of ciphersuites or null if none
have been set.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:** a copy of the array of ciphersuites or null if none
have been set.

---

#### getCipherSuites

public

String

[] getCipherSuites()

Returns a copy of the array of ciphersuites or null if none
have been set.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

setCipherSuites

```java
public void setCipherSuites​(
String
[] cipherSuites)
```

Sets the array of ciphersuites.

**Parameters:** cipherSuites

- the array of ciphersuites (or null). Note that the
standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list or might not
use the recommended name for a certain cipher suite.

---

#### setCipherSuites

public void setCipherSuites​(

String

[] cipherSuites)

Sets the array of ciphersuites.

getProtocols

```java
public
String
[] getProtocols()
```

Returns a copy of the array of protocols or null if none
have been set.

**Returns:** a copy of the array of protocols or null if none
have been set.

---

#### getProtocols

public

String

[] getProtocols()

Returns a copy of the array of protocols or null if none
have been set.

setProtocols

```java
public void setProtocols​(
String
[] protocols)
```

Sets the array of protocols.

**Parameters:** protocols

- the array of protocols (or null)

---

#### setProtocols

public void setProtocols​(

String

[] protocols)

Sets the array of protocols.

getWantClientAuth

```java
public boolean getWantClientAuth()
```

Returns whether client authentication should be requested.

**Returns:** whether client authentication should be requested.

---

#### getWantClientAuth

public boolean getWantClientAuth()

Returns whether client authentication should be requested.

setWantClientAuth

```java
public void setWantClientAuth​(boolean wantClientAuth)
```

Sets whether client authentication should be requested. Calling
this method clears the

needClientAuth

flag.

**Parameters:** wantClientAuth

- whether client authentication should be requested

---

#### setWantClientAuth

public void setWantClientAuth​(boolean wantClientAuth)

Sets whether client authentication should be requested. Calling
this method clears the

needClientAuth

flag.

getNeedClientAuth

```java
public boolean getNeedClientAuth()
```

Returns whether client authentication should be required.

**Returns:** whether client authentication should be required.

---

#### getNeedClientAuth

public boolean getNeedClientAuth()

Returns whether client authentication should be required.

setNeedClientAuth

```java
public void setNeedClientAuth​(boolean needClientAuth)
```

Sets whether client authentication should be required. Calling
this method clears the

wantClientAuth

flag.

**Parameters:** needClientAuth

- whether client authentication should be required

---

#### setNeedClientAuth

public void setNeedClientAuth​(boolean needClientAuth)

Sets whether client authentication should be required. Calling
this method clears the

wantClientAuth

flag.

getAlgorithmConstraints

```java
public
AlgorithmConstraints
getAlgorithmConstraints()
```

Returns the cryptographic algorithm constraints.

**Returns:** the cryptographic algorithm constraints, or null if the
constraints have not been set
**Since:** 1.7
**See Also:** setAlgorithmConstraints(AlgorithmConstraints)

---

#### getAlgorithmConstraints

public

AlgorithmConstraints

getAlgorithmConstraints()

Returns the cryptographic algorithm constraints.

setAlgorithmConstraints

```java
public void setAlgorithmConstraints​(
AlgorithmConstraints
constraints)
```

Sets the cryptographic algorithm constraints, which will be used
in addition to any configured by the runtime environment.

If the

constraints

parameter is non-null, every
cryptographic algorithm, key and algorithm parameters used in the
SSL/TLS/DTLS handshake must be permitted by the constraints.

**Parameters:** constraints

- the algorithm constraints (or null)
**Since:** 1.7

---

#### setAlgorithmConstraints

public void setAlgorithmConstraints​(

AlgorithmConstraints

constraints)

Sets the cryptographic algorithm constraints, which will be used
in addition to any configured by the runtime environment.

If the

constraints

parameter is non-null, every
cryptographic algorithm, key and algorithm parameters used in the
SSL/TLS/DTLS handshake must be permitted by the constraints.

If the

constraints

parameter is non-null, every
cryptographic algorithm, key and algorithm parameters used in the
SSL/TLS/DTLS handshake must be permitted by the constraints.

getEndpointIdentificationAlgorithm

```java
public
String
getEndpointIdentificationAlgorithm()
```

Gets the endpoint identification algorithm.

**Returns:** the endpoint identification algorithm, or null if none
has been set.
**Since:** 1.7
**See Also:** X509ExtendedTrustManager

,

setEndpointIdentificationAlgorithm(String)

---

#### getEndpointIdentificationAlgorithm

public

String

getEndpointIdentificationAlgorithm()

Gets the endpoint identification algorithm.

setEndpointIdentificationAlgorithm

```java
public void setEndpointIdentificationAlgorithm​(
String
algorithm)
```

Sets the endpoint identification algorithm.

If the

algorithm

parameter is non-null or non-empty, the
endpoint identification/verification procedures must be handled during
SSL/TLS/DTLS handshaking. This is to prevent man-in-the-middle attacks.

**Parameters:** algorithm

- The standard string name of the endpoint
identification algorithm (or null).
See the

Java Security Standard Algorithm Names

document
for information about standard algorithm names.
**Since:** 1.7
**See Also:** X509ExtendedTrustManager

---

#### setEndpointIdentificationAlgorithm

public void setEndpointIdentificationAlgorithm​(

String

algorithm)

Sets the endpoint identification algorithm.

If the

algorithm

parameter is non-null or non-empty, the
endpoint identification/verification procedures must be handled during
SSL/TLS/DTLS handshaking. This is to prevent man-in-the-middle attacks.

If the

algorithm

parameter is non-null or non-empty, the
endpoint identification/verification procedures must be handled during
SSL/TLS/DTLS handshaking. This is to prevent man-in-the-middle attacks.

setServerNames

```java
public final void setServerNames​(
List
<
SNIServerName
> serverNames)
```

Sets the desired

SNIServerName

s of the Server Name
Indication (SNI) parameter.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in client mode.

Note that the

serverNames

list is cloned
to protect against subsequent modification.

**Parameters:** serverNames

- the list of desired

SNIServerName

s (or null)
**Throws:** NullPointerException

- if the

serverNames

contains

null

element
**Throws:** IllegalArgumentException

- if the

serverNames

contains more than one name of the same name type
**Since:** 1.8
**See Also:** SNIServerName

,

getServerNames()

---

#### setServerNames

public final void setServerNames​(

List

<

SNIServerName

> serverNames)

Sets the desired

SNIServerName

s of the Server Name
Indication (SNI) parameter.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in client mode.

Note that the

serverNames

list is cloned
to protect against subsequent modification.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in client mode.

Note that the

serverNames

list is cloned
to protect against subsequent modification.

Note that the

serverNames

list is cloned
to protect against subsequent modification.

getServerNames

```java
public final
List
<
SNIServerName
> getServerNames()
```

Returns a

List

containing all

SNIServerName

s of the
Server Name Indication (SNI) parameter, or null if none has been set.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in client mode.

For SSL/TLS/DTLS connections, the underlying SSL/TLS/DTLS provider
may specify a default value for a certain server name type. In
client mode, it is recommended that, by default, providers should
include the server name indication whenever the server can be located
by a supported server name type.

It is recommended that providers initialize default Server Name
Indications when creating

SSLSocket

/

SSLEngine

s.
In the following examples, the server name could be represented by an
instance of

SNIHostName

which has been initialized with the
hostname "www.example.com" and type

StandardConstants.SNI_HOST_NAME

.

```java
Socket socket =
sslSocketFactory.createSocket("www.example.com", 443);
```

or

```java
SSLEngine engine =
sslContext.createSSLEngine("www.example.com", 443);
```

**Returns:** null or an immutable list of non-null

SNIServerName

s
**Since:** 1.8
**See Also:** List

,

setServerNames(List)

---

#### getServerNames

public final

List

<

SNIServerName

> getServerNames()

Returns a

List

containing all

SNIServerName

s of the
Server Name Indication (SNI) parameter, or null if none has been set.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in client mode.

For SSL/TLS/DTLS connections, the underlying SSL/TLS/DTLS provider
may specify a default value for a certain server name type. In
client mode, it is recommended that, by default, providers should
include the server name indication whenever the server can be located
by a supported server name type.

It is recommended that providers initialize default Server Name
Indications when creating

SSLSocket

/

SSLEngine

s.
In the following examples, the server name could be represented by an
instance of

SNIHostName

which has been initialized with the
hostname "www.example.com" and type

StandardConstants.SNI_HOST_NAME

.

```java
Socket socket =
sslSocketFactory.createSocket("www.example.com", 443);
```

or

```java
SSLEngine engine =
sslContext.createSSLEngine("www.example.com", 443);
```

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in client mode.

For SSL/TLS/DTLS connections, the underlying SSL/TLS/DTLS provider
may specify a default value for a certain server name type. In
client mode, it is recommended that, by default, providers should
include the server name indication whenever the server can be located
by a supported server name type.

It is recommended that providers initialize default Server Name
Indications when creating

SSLSocket

/

SSLEngine

s.
In the following examples, the server name could be represented by an
instance of

SNIHostName

which has been initialized with the
hostname "www.example.com" and type

StandardConstants.SNI_HOST_NAME

.

```java
Socket socket =
sslSocketFactory.createSocket("www.example.com", 443);
```

or

```java
SSLEngine engine =
sslContext.createSSLEngine("www.example.com", 443);
```

For SSL/TLS/DTLS connections, the underlying SSL/TLS/DTLS provider
may specify a default value for a certain server name type. In
client mode, it is recommended that, by default, providers should
include the server name indication whenever the server can be located
by a supported server name type.

It is recommended that providers initialize default Server Name
Indications when creating

SSLSocket

/

SSLEngine

s.
In the following examples, the server name could be represented by an
instance of

SNIHostName

which has been initialized with the
hostname "www.example.com" and type

StandardConstants.SNI_HOST_NAME

.

```java
Socket socket =
sslSocketFactory.createSocket("www.example.com", 443);
```

or

```java
SSLEngine engine =
sslContext.createSSLEngine("www.example.com", 443);
```

It is recommended that providers initialize default Server Name
Indications when creating

SSLSocket

/

SSLEngine

s.
In the following examples, the server name could be represented by an
instance of

SNIHostName

which has been initialized with the
hostname "www.example.com" and type

StandardConstants.SNI_HOST_NAME

.

```java
Socket socket =
sslSocketFactory.createSocket("www.example.com", 443);
```

or

```java
SSLEngine engine =
sslContext.createSSLEngine("www.example.com", 443);
```

Socket socket =
sslSocketFactory.createSocket("www.example.com", 443);

SSLEngine engine =
sslContext.createSSLEngine("www.example.com", 443);

setSNIMatchers

```java
public final void setSNIMatchers​(
Collection
<
SNIMatcher
> matchers)
```

Sets the

SNIMatcher

s of the Server Name Indication (SNI)
parameter.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in server mode.

Note that the

matchers

collection is cloned to protect
against subsequent modification.

**Parameters:** matchers

- the collection of

SNIMatcher

s (or null)
**Throws:** NullPointerException

- if the

matchers

contains

null

element
**Throws:** IllegalArgumentException

- if the

matchers

contains more than one name of the same name type
**Since:** 1.8
**See Also:** Collection

,

SNIMatcher

,

getSNIMatchers()

---

#### setSNIMatchers

public final void setSNIMatchers​(

Collection

<

SNIMatcher

> matchers)

Sets the

SNIMatcher

s of the Server Name Indication (SNI)
parameter.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in server mode.

Note that the

matchers

collection is cloned to protect
against subsequent modification.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in server mode.

Note that the

matchers

collection is cloned to protect
against subsequent modification.

Note that the

matchers

collection is cloned to protect
against subsequent modification.

getSNIMatchers

```java
public final
Collection
<
SNIMatcher
> getSNIMatchers()
```

Returns a

Collection

containing all

SNIMatcher

s of the
Server Name Indication (SNI) parameter, or null if none has been set.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in server mode.

For better interoperability, providers generally will not define
default matchers so that by default servers will ignore the SNI
extension and continue the handshake.

**Returns:** null or an immutable collection of non-null

SNIMatcher

s
**Since:** 1.8
**See Also:** SNIMatcher

,

setSNIMatchers(Collection)

---

#### getSNIMatchers

public final

Collection

<

SNIMatcher

> getSNIMatchers()

Returns a

Collection

containing all

SNIMatcher

s of the
Server Name Indication (SNI) parameter, or null if none has been set.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in server mode.

For better interoperability, providers generally will not define
default matchers so that by default servers will ignore the SNI
extension and continue the handshake.

This method is only useful to

SSLSocket

s or

SSLEngine

s
operating in server mode.

For better interoperability, providers generally will not define
default matchers so that by default servers will ignore the SNI
extension and continue the handshake.

For better interoperability, providers generally will not define
default matchers so that by default servers will ignore the SNI
extension and continue the handshake.

setUseCipherSuitesOrder

```java
public final void setUseCipherSuitesOrder​(boolean honorOrder)
```

Sets whether the local cipher suites preference should be honored.

**Parameters:** honorOrder

- whether local cipher suites order in

#getCipherSuites

should be honored during
SSL/TLS/DTLS handshaking.
**Since:** 1.8
**See Also:** getUseCipherSuitesOrder()

---

#### setUseCipherSuitesOrder

public final void setUseCipherSuitesOrder​(boolean honorOrder)

Sets whether the local cipher suites preference should be honored.

getUseCipherSuitesOrder

```java
public final boolean getUseCipherSuitesOrder()
```

Returns whether the local cipher suites preference should be honored.

**Returns:** whether local cipher suites order in

#getCipherSuites

should be honored during SSL/TLS/DTLS handshaking.
**Since:** 1.8
**See Also:** setUseCipherSuitesOrder(boolean)

---

#### getUseCipherSuitesOrder

public final boolean getUseCipherSuitesOrder()

Returns whether the local cipher suites preference should be honored.

setEnableRetransmissions

```java
public void setEnableRetransmissions​(boolean enableRetransmissions)
```

Sets whether DTLS handshake retransmissions should be enabled.

This method only applies to DTLS.

**Parameters:** enableRetransmissions

-

true

indicates that DTLS handshake retransmissions
should be enabled;

false

indicates that DTLS handshake
retransmissions should be disabled
**Since:** 9
**See Also:** getEnableRetransmissions()

---

#### setEnableRetransmissions

public void setEnableRetransmissions​(boolean enableRetransmissions)

Sets whether DTLS handshake retransmissions should be enabled.

This method only applies to DTLS.

getEnableRetransmissions

```java
public boolean getEnableRetransmissions()
```

Returns whether DTLS handshake retransmissions should be enabled.

This method only applies to DTLS.

**Returns:** true, if DTLS handshake retransmissions should be enabled
**Since:** 9
**See Also:** setEnableRetransmissions(boolean)

---

#### getEnableRetransmissions

public boolean getEnableRetransmissions()

Returns whether DTLS handshake retransmissions should be enabled.

This method only applies to DTLS.

setMaximumPacketSize

```java
public void setMaximumPacketSize​(int maximumPacketSize)
```

Sets the maximum expected network packet size in bytes for
SSL/TLS/DTLS records.

**API Note:** It is recommended that if possible, the maximum packet size
should not be less than 256 bytes so that small handshake
messages, such as HelloVerifyRequests, are not fragmented.
**Implementation Note:** If the maximum packet size is too small to hold a minimal
record, an implementation may attempt to generate as minimal
records as possible. However, this may cause a generated
packet to be larger than the maximum packet size.
**Parameters:** maximumPacketSize

- the maximum expected network packet size in bytes, or

0

to use the implicit size that is automatically
specified by the underlying implementation.
**Throws:** IllegalArgumentException

- if

maximumPacketSize

is negative.
**Since:** 9
**See Also:** getMaximumPacketSize()

---

#### setMaximumPacketSize

public void setMaximumPacketSize​(int maximumPacketSize)

Sets the maximum expected network packet size in bytes for
SSL/TLS/DTLS records.

getMaximumPacketSize

```java
public int getMaximumPacketSize()
```

Returns the maximum expected network packet size in bytes for
SSL/TLS/DTLS records.

**API Note:** The implicit size may not be a fixed value, especially
for a DTLS protocols implementation.
**Implementation Note:** For SSL/TLS/DTLS connections, the underlying provider
should calculate and specify the implicit value of the
maximum expected network packet size if it is not
configured explicitly. For any connection populated
object, this method should never return

0

so
that applications can retrieve the actual implicit size
of the underlying implementation.

An implementation should attempt to comply with the maximum
packet size configuration. However, if the maximum packet
size is too small to hold a minimal record, an implementation
may try to generate as minimal records as possible. This
may cause a generated packet to be larger than the maximum
packet size.
**Returns:** the maximum expected network packet size, or

0

if
use the implicit size that is automatically specified by
the underlying implementation and this object has not been
populated by any connection.
**Since:** 9
**See Also:** setMaximumPacketSize(int)

---

#### getMaximumPacketSize

public int getMaximumPacketSize()

Returns the maximum expected network packet size in bytes for
SSL/TLS/DTLS records.

An implementation should attempt to comply with the maximum
packet size configuration. However, if the maximum packet
size is too small to hold a minimal record, an implementation
may try to generate as minimal records as possible. This
may cause a generated packet to be larger than the maximum
packet size.

getApplicationProtocols

```java
public
String
[] getApplicationProtocols()
```

Returns a prioritized array of application-layer protocol names that
can be negotiated over the SSL/TLS/DTLS protocols.

The array could be empty (zero-length), in which case protocol
indications will not be used.

This method will return a new array each time it is invoked.

**Returns:** a non-null, possibly zero-length array of application protocol

String

s. The array is ordered based on protocol
preference, with

protocols[0]

being the most preferred.
**Since:** 9
**See Also:** setApplicationProtocols(java.lang.String[])

---

#### getApplicationProtocols

public

String

[] getApplicationProtocols()

Returns a prioritized array of application-layer protocol names that
can be negotiated over the SSL/TLS/DTLS protocols.

The array could be empty (zero-length), in which case protocol
indications will not be used.

This method will return a new array each time it is invoked.

The array could be empty (zero-length), in which case protocol
indications will not be used.

This method will return a new array each time it is invoked.

This method will return a new array each time it is invoked.

setApplicationProtocols

```java
public void setApplicationProtocols​(
String
[] protocols)
```

Sets the prioritized array of application-layer protocol names that
can be negotiated over the SSL/TLS/DTLS protocols.

If application-layer protocols are supported by the underlying
SSL/TLS implementation, this method configures which values can
be negotiated by protocols such as

RFC 7301

, the
Application Layer Protocol Negotiation (ALPN).

If this end of the connection is expected to offer application protocol
values, all protocols configured by this method will be sent to the
peer.

If this end of the connection is expected to select the application
protocol value, the

protocols

configured by this method are
compared with those sent by the peer. The first matched value becomes
the negotiated value. If none of the

protocols

were actually
requested by the peer, the underlying protocol will determine what
action to take. (For example, ALPN will send a

"no_application_protocol"

alert and terminate the connection.)

**Implementation Requirements:** This method will make a copy of the

protocols

array.
**Parameters:** protocols

- an ordered array of application protocols,
with

protocols[0]

being the most preferred.
If the array is empty (zero-length), protocol
indications will not be used.
**Throws:** IllegalArgumentException

- if protocols is null, or if
any element in a non-empty array is null or an
empty (zero-length) string
**Since:** 9
**See Also:** getApplicationProtocols()

---

#### setApplicationProtocols

public void setApplicationProtocols​(

String

[] protocols)

Sets the prioritized array of application-layer protocol names that
can be negotiated over the SSL/TLS/DTLS protocols.

If application-layer protocols are supported by the underlying
SSL/TLS implementation, this method configures which values can
be negotiated by protocols such as

RFC 7301

, the
Application Layer Protocol Negotiation (ALPN).

If this end of the connection is expected to offer application protocol
values, all protocols configured by this method will be sent to the
peer.

If this end of the connection is expected to select the application
protocol value, the

protocols

configured by this method are
compared with those sent by the peer. The first matched value becomes
the negotiated value. If none of the

protocols

were actually
requested by the peer, the underlying protocol will determine what
action to take. (For example, ALPN will send a

"no_application_protocol"

alert and terminate the connection.)

If application-layer protocols are supported by the underlying
SSL/TLS implementation, this method configures which values can
be negotiated by protocols such as

RFC 7301

, the
Application Layer Protocol Negotiation (ALPN).

If this end of the connection is expected to offer application protocol
values, all protocols configured by this method will be sent to the
peer.

If this end of the connection is expected to select the application
protocol value, the

protocols

configured by this method are
compared with those sent by the peer. The first matched value becomes
the negotiated value. If none of the

protocols

were actually
requested by the peer, the underlying protocol will determine what
action to take. (For example, ALPN will send a

"no_application_protocol"

alert and terminate the connection.)

If this end of the connection is expected to offer application protocol
values, all protocols configured by this method will be sent to the
peer.

If this end of the connection is expected to select the application
protocol value, the

protocols

configured by this method are
compared with those sent by the peer. The first matched value becomes
the negotiated value. If none of the

protocols

were actually
requested by the peer, the underlying protocol will determine what
action to take. (For example, ALPN will send a

"no_application_protocol"

alert and terminate the connection.)

If this end of the connection is expected to select the application
protocol value, the

protocols

configured by this method are
compared with those sent by the peer. The first matched value becomes
the negotiated value. If none of the

protocols

were actually
requested by the peer, the underlying protocol will determine what
action to take. (For example, ALPN will send a

"no_application_protocol"

alert and terminate the connection.)

---

