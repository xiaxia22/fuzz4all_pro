# Interface SaslClient

**Source:** `java.security.sasl\javax\security\sasl\SaslClient.html`

### Class Description

```java
public interface
SaslClient
```

Performs SASL authentication as a client.

A protocol library such as one for LDAP gets an instance of this
class in order to perform authentication defined by a specific SASL
mechanism. Invoking methods on the

SaslClient

instance
process challenges and create responses according to the SASL
mechanism implemented by the

SaslClient

.
As the authentication proceeds, the instance
encapsulates the state of a SASL client's authentication exchange.

Here's an example of how an LDAP library might use a

SaslClient

.
It first gets an instance of a

SaslClient

:

```java
SaslClient sc = Sasl.createSaslClient(mechanisms,
authorizationId, protocol, serverName, props, callbackHandler);
```

It can then proceed to use the client for authentication.
For example, an LDAP library might use the client as follows:

```java
// Get initial response and send to server
byte[] response = (sc.hasInitialResponse() ? sc.evaluateChallenge(new byte[0]) :
null);
LdapResult res = ldap.sendBindRequest(dn, sc.getName(), response);
while (!sc.isComplete() &&
(res.status == SASL_BIND_IN_PROGRESS || res.status == SUCCESS)) {
response = sc.evaluateChallenge(res.getBytes());
if (res.status == SUCCESS) {
// we're done; don't expect to send another BIND
if (response != null) {
throw new SaslException(
"Protocol error: attempting to send response after completion");
}
break;
}
res = ldap.sendBindRequest(dn, sc.getName(), response);
}
if (sc.isComplete() && res.status == SUCCESS) {
String qop = (String) sc.getNegotiatedProperty(Sasl.QOP);
if (qop != null
&& (qop.equalsIgnoreCase("auth-int")
|| qop.equalsIgnoreCase("auth-conf"))) {

// Use SaslClient.wrap() and SaslClient.unwrap() for future
// communication with server
ldap.in = new SecureInputStream(sc, ldap.in);
ldap.out = new SecureOutputStream(sc, ldap.out);
}
}
```

If the mechanism has an initial response, the library invokes

evaluateChallenge()

with an empty
challenge and to get initial response.
Protocols such as IMAP4, which do not include an initial response with
their first authentication command to the server, initiates the
authentication without first calling

hasInitialResponse()

or

evaluateChallenge()

.
When the server responds to the command, it sends an initial challenge.
For a SASL mechanism in which the client sends data first, the server should
have issued a challenge with no data. This will then result in a call
(on the client) to

evaluateChallenge()

with an empty challenge.

**Since:** 1.5
**See Also:** Sasl

,

SaslClientFactory

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getMechanismName()

Returns the IANA-registered mechanism name of this SASL client.
(e.g. "CRAM-MD5", "GSSAPI").

**Returns:**
- A non-null string representing the IANA-registered mechanism name.

---

#### boolean hasInitialResponse()

Determines whether this mechanism has an optional initial response.
If true, caller should call

evaluateChallenge()

with an
empty array to get the initial response.

**Returns:**
- true if this mechanism has an initial response.

---

#### byte[] evaluateChallenge​(byte[] challenge)
throws
SaslException

Evaluates the challenge data and generates a response.
If a challenge is received from the server during the authentication
process, this method is called to prepare an appropriate next
response to submit to the server.

**Parameters:**
- challenge

- The non-null challenge sent from the server.
The challenge array may have zero length.

**Returns:**
- The possibly null response to send to the server.
It is null if the challenge accompanied a "SUCCESS" status and the challenge
only contains data for the client to update its state and no response
needs to be sent to the server. The response is a zero-length byte
array if the client is to send a response with no data.

**Throws:**
- SaslException

- If an error occurred while processing
the challenge or generating a response.

---

#### boolean isComplete()

Determines whether the authentication exchange has completed.
This method may be called at any time, but typically, it
will not be called until the caller has received indication
from the server
(in a protocol-specific manner) that the exchange has completed.

**Returns:**
- true if the authentication exchange has completed; false otherwise.

---

#### byte[] unwrap​(byte[] incoming,
int offset,
int len)
throws
SaslException

Unwraps a byte array received from the server.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true) and only if
the authentication exchange has negotiated integrity and/or privacy
as the quality of protection; otherwise, an

IllegalStateException

is thrown.

incoming

is the contents of the SASL buffer as defined in RFC 2222
without the leading four octet field that represents the length.

offset

and

len

specify the portion of

incoming

to use.

**Parameters:**
- incoming

- A non-null byte array containing the encoded bytes
from the server.
- offset

- The starting position at

incoming

of the bytes to use.
- len

- The number of bytes from

incoming

to use.

**Returns:**
- A non-null byte array containing the decoded bytes.

**Throws:**
- SaslException

- if

incoming

cannot be successfully
unwrapped.
- IllegalStateException

- if the authentication exchange has
not completed, or if the negotiated quality of protection
has neither integrity nor privacy.

---

#### byte[] wrap​(byte[] outgoing,
int offset,
int len)
throws
SaslException

Wraps a byte array to be sent to the server.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true) and only if
the authentication exchange has negotiated integrity and/or privacy
as the quality of protection; otherwise, an

IllegalStateException

is thrown.

The result of this method will make up the contents of the SASL buffer
as defined in RFC 2222 without the leading four octet field that
represents the length.

offset

and

len

specify the portion of

outgoing

to use.

**Parameters:**
- outgoing

- A non-null byte array containing the bytes to encode.
- offset

- The starting position at

outgoing

of the bytes to use.
- len

- The number of bytes from

outgoing

to use.

**Returns:**
- A non-null byte array containing the encoded bytes.

**Throws:**
- SaslException

- if

outgoing

cannot be successfully
wrapped.
- IllegalStateException

- if the authentication exchange has
not completed, or if the negotiated quality of protection
has neither integrity nor privacy.

---

#### Object
getNegotiatedProperty​(
String
propName)

Retrieves the negotiated property.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true); otherwise, an

IllegalStateException

is thrown.

The

Sasl

class includes several well-known property names
(For example,

Sasl.QOP

). A SASL provider can support other
properties which are specific to the vendor and/or a mechanism.

**Parameters:**
- propName

- The non-null property name.

**Returns:**
- The value of the negotiated property. If null, the property was
not negotiated or is not applicable to this mechanism.

**Throws:**
- IllegalStateException

- if this authentication exchange
has not completed

---

#### void dispose()
throws
SaslException

Disposes of any system resources or security-sensitive information
the SaslClient might be using. Invoking this method invalidates
the SaslClient instance. This method is idempotent.

**Throws:**
- SaslException

- If a problem was encountered while disposing
the resources.

---

### Additional Sections

#### Interface SaslClient

```java
public interface
SaslClient
```

Performs SASL authentication as a client.

A protocol library such as one for LDAP gets an instance of this
class in order to perform authentication defined by a specific SASL
mechanism. Invoking methods on the

SaslClient

instance
process challenges and create responses according to the SASL
mechanism implemented by the

SaslClient

.
As the authentication proceeds, the instance
encapsulates the state of a SASL client's authentication exchange.

Here's an example of how an LDAP library might use a

SaslClient

.
It first gets an instance of a

SaslClient

:

```java
SaslClient sc = Sasl.createSaslClient(mechanisms,
authorizationId, protocol, serverName, props, callbackHandler);
```

It can then proceed to use the client for authentication.
For example, an LDAP library might use the client as follows:

```java
// Get initial response and send to server
byte[] response = (sc.hasInitialResponse() ? sc.evaluateChallenge(new byte[0]) :
null);
LdapResult res = ldap.sendBindRequest(dn, sc.getName(), response);
while (!sc.isComplete() &&
(res.status == SASL_BIND_IN_PROGRESS || res.status == SUCCESS)) {
response = sc.evaluateChallenge(res.getBytes());
if (res.status == SUCCESS) {
// we're done; don't expect to send another BIND
if (response != null) {
throw new SaslException(
"Protocol error: attempting to send response after completion");
}
break;
}
res = ldap.sendBindRequest(dn, sc.getName(), response);
}
if (sc.isComplete() && res.status == SUCCESS) {
String qop = (String) sc.getNegotiatedProperty(Sasl.QOP);
if (qop != null
&& (qop.equalsIgnoreCase("auth-int")
|| qop.equalsIgnoreCase("auth-conf"))) {

// Use SaslClient.wrap() and SaslClient.unwrap() for future
// communication with server
ldap.in = new SecureInputStream(sc, ldap.in);
ldap.out = new SecureOutputStream(sc, ldap.out);
}
}
```

If the mechanism has an initial response, the library invokes

evaluateChallenge()

with an empty
challenge and to get initial response.
Protocols such as IMAP4, which do not include an initial response with
their first authentication command to the server, initiates the
authentication without first calling

hasInitialResponse()

or

evaluateChallenge()

.
When the server responds to the command, it sends an initial challenge.
For a SASL mechanism in which the client sends data first, the server should
have issued a challenge with no data. This will then result in a call
(on the client) to

evaluateChallenge()

with an empty challenge.

**Since:** 1.5
**See Also:** Sasl

,

SaslClientFactory

public interface

SaslClient

Performs SASL authentication as a client.

A protocol library such as one for LDAP gets an instance of this
class in order to perform authentication defined by a specific SASL
mechanism. Invoking methods on the

SaslClient

instance
process challenges and create responses according to the SASL
mechanism implemented by the

SaslClient

.
As the authentication proceeds, the instance
encapsulates the state of a SASL client's authentication exchange.

Here's an example of how an LDAP library might use a

SaslClient

.
It first gets an instance of a

SaslClient

:

```java
SaslClient sc = Sasl.createSaslClient(mechanisms,
authorizationId, protocol, serverName, props, callbackHandler);
```

It can then proceed to use the client for authentication.
For example, an LDAP library might use the client as follows:

```java
// Get initial response and send to server
byte[] response = (sc.hasInitialResponse() ? sc.evaluateChallenge(new byte[0]) :
null);
LdapResult res = ldap.sendBindRequest(dn, sc.getName(), response);
while (!sc.isComplete() &&
(res.status == SASL_BIND_IN_PROGRESS || res.status == SUCCESS)) {
response = sc.evaluateChallenge(res.getBytes());
if (res.status == SUCCESS) {
// we're done; don't expect to send another BIND
if (response != null) {
throw new SaslException(
"Protocol error: attempting to send response after completion");
}
break;
}
res = ldap.sendBindRequest(dn, sc.getName(), response);
}
if (sc.isComplete() && res.status == SUCCESS) {
String qop = (String) sc.getNegotiatedProperty(Sasl.QOP);
if (qop != null
&& (qop.equalsIgnoreCase("auth-int")
|| qop.equalsIgnoreCase("auth-conf"))) {

// Use SaslClient.wrap() and SaslClient.unwrap() for future
// communication with server
ldap.in = new SecureInputStream(sc, ldap.in);
ldap.out = new SecureOutputStream(sc, ldap.out);
}
}
```

If the mechanism has an initial response, the library invokes

evaluateChallenge()

with an empty
challenge and to get initial response.
Protocols such as IMAP4, which do not include an initial response with
their first authentication command to the server, initiates the
authentication without first calling

hasInitialResponse()

or

evaluateChallenge()

.
When the server responds to the command, it sends an initial challenge.
For a SASL mechanism in which the client sends data first, the server should
have issued a challenge with no data. This will then result in a call
(on the client) to

evaluateChallenge()

with an empty challenge.

A protocol library such as one for LDAP gets an instance of this
class in order to perform authentication defined by a specific SASL
mechanism. Invoking methods on the

SaslClient

instance
process challenges and create responses according to the SASL
mechanism implemented by the

SaslClient

.
As the authentication proceeds, the instance
encapsulates the state of a SASL client's authentication exchange.

Here's an example of how an LDAP library might use a

SaslClient

.
It first gets an instance of a

SaslClient

:

```java
SaslClient sc = Sasl.createSaslClient(mechanisms,
authorizationId, protocol, serverName, props, callbackHandler);
```

It can then proceed to use the client for authentication.
For example, an LDAP library might use the client as follows:

```java
// Get initial response and send to server
byte[] response = (sc.hasInitialResponse() ? sc.evaluateChallenge(new byte[0]) :
null);
LdapResult res = ldap.sendBindRequest(dn, sc.getName(), response);
while (!sc.isComplete() &&
(res.status == SASL_BIND_IN_PROGRESS || res.status == SUCCESS)) {
response = sc.evaluateChallenge(res.getBytes());
if (res.status == SUCCESS) {
// we're done; don't expect to send another BIND
if (response != null) {
throw new SaslException(
"Protocol error: attempting to send response after completion");
}
break;
}
res = ldap.sendBindRequest(dn, sc.getName(), response);
}
if (sc.isComplete() && res.status == SUCCESS) {
String qop = (String) sc.getNegotiatedProperty(Sasl.QOP);
if (qop != null
&& (qop.equalsIgnoreCase("auth-int")
|| qop.equalsIgnoreCase("auth-conf"))) {

// Use SaslClient.wrap() and SaslClient.unwrap() for future
// communication with server
ldap.in = new SecureInputStream(sc, ldap.in);
ldap.out = new SecureOutputStream(sc, ldap.out);
}
}
```

If the mechanism has an initial response, the library invokes

evaluateChallenge()

with an empty
challenge and to get initial response.
Protocols such as IMAP4, which do not include an initial response with
their first authentication command to the server, initiates the
authentication without first calling

hasInitialResponse()

or

evaluateChallenge()

.
When the server responds to the command, it sends an initial challenge.
For a SASL mechanism in which the client sends data first, the server should
have issued a challenge with no data. This will then result in a call
(on the client) to

evaluateChallenge()

with an empty challenge.

Here's an example of how an LDAP library might use a

SaslClient

.
It first gets an instance of a

SaslClient

:

```java
SaslClient sc = Sasl.createSaslClient(mechanisms,
authorizationId, protocol, serverName, props, callbackHandler);
```

It can then proceed to use the client for authentication.
For example, an LDAP library might use the client as follows:

```java
// Get initial response and send to server
byte[] response = (sc.hasInitialResponse() ? sc.evaluateChallenge(new byte[0]) :
null);
LdapResult res = ldap.sendBindRequest(dn, sc.getName(), response);
while (!sc.isComplete() &&
(res.status == SASL_BIND_IN_PROGRESS || res.status == SUCCESS)) {
response = sc.evaluateChallenge(res.getBytes());
if (res.status == SUCCESS) {
// we're done; don't expect to send another BIND
if (response != null) {
throw new SaslException(
"Protocol error: attempting to send response after completion");
}
break;
}
res = ldap.sendBindRequest(dn, sc.getName(), response);
}
if (sc.isComplete() && res.status == SUCCESS) {
String qop = (String) sc.getNegotiatedProperty(Sasl.QOP);
if (qop != null
&& (qop.equalsIgnoreCase("auth-int")
|| qop.equalsIgnoreCase("auth-conf"))) {

// Use SaslClient.wrap() and SaslClient.unwrap() for future
// communication with server
ldap.in = new SecureInputStream(sc, ldap.in);
ldap.out = new SecureOutputStream(sc, ldap.out);
}
}
```

If the mechanism has an initial response, the library invokes

evaluateChallenge()

with an empty
challenge and to get initial response.
Protocols such as IMAP4, which do not include an initial response with
their first authentication command to the server, initiates the
authentication without first calling

hasInitialResponse()

or

evaluateChallenge()

.
When the server responds to the command, it sends an initial challenge.
For a SASL mechanism in which the client sends data first, the server should
have issued a challenge with no data. This will then result in a call
(on the client) to

evaluateChallenge()

with an empty challenge.

SaslClient sc = Sasl.createSaslClient(mechanisms,
authorizationId, protocol, serverName, props, callbackHandler);

// Get initial response and send to server
byte[] response = (sc.hasInitialResponse() ? sc.evaluateChallenge(new byte[0]) :
null);
LdapResult res = ldap.sendBindRequest(dn, sc.getName(), response);
while (!sc.isComplete() &&
(res.status == SASL_BIND_IN_PROGRESS || res.status == SUCCESS)) {
response = sc.evaluateChallenge(res.getBytes());
if (res.status == SUCCESS) {
// we're done; don't expect to send another BIND
if (response != null) {
throw new SaslException(
"Protocol error: attempting to send response after completion");
}
break;
}
res = ldap.sendBindRequest(dn, sc.getName(), response);
}
if (sc.isComplete() && res.status == SUCCESS) {
String qop = (String) sc.getNegotiatedProperty(Sasl.QOP);
if (qop != null
&& (qop.equalsIgnoreCase("auth-int")
|| qop.equalsIgnoreCase("auth-conf"))) {

// Use SaslClient.wrap() and SaslClient.unwrap() for future
// communication with server
ldap.in = new SecureInputStream(sc, ldap.in);
ldap.out = new SecureOutputStream(sc, ldap.out);
}
}

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

dispose

()

Disposes of any system resources or security-sensitive information
the SaslClient might be using.

byte[]

evaluateChallenge

​(byte[] challenge)

Evaluates the challenge data and generates a response.

String

getMechanismName

()

Returns the IANA-registered mechanism name of this SASL client.

Object

getNegotiatedProperty

​(

String

propName)

Retrieves the negotiated property.

boolean

hasInitialResponse

()

Determines whether this mechanism has an optional initial response.

boolean

isComplete

()

Determines whether the authentication exchange has completed.

byte[]

unwrap

​(byte[] incoming,
int offset,
int len)

Unwraps a byte array received from the server.

byte[]

wrap

​(byte[] outgoing,
int offset,
int len)

Wraps a byte array to be sent to the server.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

dispose

()

Disposes of any system resources or security-sensitive information
the SaslClient might be using.

byte[]

evaluateChallenge

​(byte[] challenge)

Evaluates the challenge data and generates a response.

String

getMechanismName

()

Returns the IANA-registered mechanism name of this SASL client.

Object

getNegotiatedProperty

​(

String

propName)

Retrieves the negotiated property.

boolean

hasInitialResponse

()

Determines whether this mechanism has an optional initial response.

boolean

isComplete

()

Determines whether the authentication exchange has completed.

byte[]

unwrap

​(byte[] incoming,
int offset,
int len)

Unwraps a byte array received from the server.

byte[]

wrap

​(byte[] outgoing,
int offset,
int len)

Wraps a byte array to be sent to the server.

---

#### Method Summary

Disposes of any system resources or security-sensitive information
the SaslClient might be using.

Evaluates the challenge data and generates a response.

Returns the IANA-registered mechanism name of this SASL client.

Retrieves the negotiated property.

Determines whether this mechanism has an optional initial response.

Determines whether the authentication exchange has completed.

Unwraps a byte array received from the server.

Wraps a byte array to be sent to the server.

============ METHOD DETAIL ==========

- Method Detail

- getMechanismName

```java
String
getMechanismName()
```

Returns the IANA-registered mechanism name of this SASL client.
(e.g. "CRAM-MD5", "GSSAPI").

**Returns:** A non-null string representing the IANA-registered mechanism name.

- hasInitialResponse

```java
boolean hasInitialResponse()
```

Determines whether this mechanism has an optional initial response.
If true, caller should call

evaluateChallenge()

with an
empty array to get the initial response.

**Returns:** true if this mechanism has an initial response.

- evaluateChallenge

```java
byte[] evaluateChallenge​(byte[] challenge)
throws
SaslException
```

Evaluates the challenge data and generates a response.
If a challenge is received from the server during the authentication
process, this method is called to prepare an appropriate next
response to submit to the server.

**Parameters:** challenge

- The non-null challenge sent from the server.
The challenge array may have zero length.
**Returns:** The possibly null response to send to the server.
It is null if the challenge accompanied a "SUCCESS" status and the challenge
only contains data for the client to update its state and no response
needs to be sent to the server. The response is a zero-length byte
array if the client is to send a response with no data.
**Throws:** SaslException

- If an error occurred while processing
the challenge or generating a response.

- isComplete

```java
boolean isComplete()
```

Determines whether the authentication exchange has completed.
This method may be called at any time, but typically, it
will not be called until the caller has received indication
from the server
(in a protocol-specific manner) that the exchange has completed.

**Returns:** true if the authentication exchange has completed; false otherwise.

- unwrap

```java
byte[] unwrap​(byte[] incoming,
int offset,
int len)
throws
SaslException
```

Unwraps a byte array received from the server.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true) and only if
the authentication exchange has negotiated integrity and/or privacy
as the quality of protection; otherwise, an

IllegalStateException

is thrown.

incoming

is the contents of the SASL buffer as defined in RFC 2222
without the leading four octet field that represents the length.

offset

and

len

specify the portion of

incoming

to use.

**Parameters:** incoming

- A non-null byte array containing the encoded bytes
from the server.
**Parameters:** offset

- The starting position at

incoming

of the bytes to use.
**Parameters:** len

- The number of bytes from

incoming

to use.
**Returns:** A non-null byte array containing the decoded bytes.
**Throws:** SaslException

- if

incoming

cannot be successfully
unwrapped.
**Throws:** IllegalStateException

- if the authentication exchange has
not completed, or if the negotiated quality of protection
has neither integrity nor privacy.

- wrap

```java
byte[] wrap​(byte[] outgoing,
int offset,
int len)
throws
SaslException
```

Wraps a byte array to be sent to the server.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true) and only if
the authentication exchange has negotiated integrity and/or privacy
as the quality of protection; otherwise, an

IllegalStateException

is thrown.

The result of this method will make up the contents of the SASL buffer
as defined in RFC 2222 without the leading four octet field that
represents the length.

offset

and

len

specify the portion of

outgoing

to use.

**Parameters:** outgoing

- A non-null byte array containing the bytes to encode.
**Parameters:** offset

- The starting position at

outgoing

of the bytes to use.
**Parameters:** len

- The number of bytes from

outgoing

to use.
**Returns:** A non-null byte array containing the encoded bytes.
**Throws:** SaslException

- if

outgoing

cannot be successfully
wrapped.
**Throws:** IllegalStateException

- if the authentication exchange has
not completed, or if the negotiated quality of protection
has neither integrity nor privacy.

- getNegotiatedProperty

```java
Object
getNegotiatedProperty​(
String
propName)
```

Retrieves the negotiated property.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true); otherwise, an

IllegalStateException

is thrown.

The

Sasl

class includes several well-known property names
(For example,

Sasl.QOP

). A SASL provider can support other
properties which are specific to the vendor and/or a mechanism.

**Parameters:** propName

- The non-null property name.
**Returns:** The value of the negotiated property. If null, the property was
not negotiated or is not applicable to this mechanism.
**Throws:** IllegalStateException

- if this authentication exchange
has not completed

- dispose

```java
void dispose()
throws
SaslException
```

Disposes of any system resources or security-sensitive information
the SaslClient might be using. Invoking this method invalidates
the SaslClient instance. This method is idempotent.

**Throws:** SaslException

- If a problem was encountered while disposing
the resources.

Method Detail

- getMechanismName

```java
String
getMechanismName()
```

Returns the IANA-registered mechanism name of this SASL client.
(e.g. "CRAM-MD5", "GSSAPI").

**Returns:** A non-null string representing the IANA-registered mechanism name.

- hasInitialResponse

```java
boolean hasInitialResponse()
```

Determines whether this mechanism has an optional initial response.
If true, caller should call

evaluateChallenge()

with an
empty array to get the initial response.

**Returns:** true if this mechanism has an initial response.

- evaluateChallenge

```java
byte[] evaluateChallenge​(byte[] challenge)
throws
SaslException
```

Evaluates the challenge data and generates a response.
If a challenge is received from the server during the authentication
process, this method is called to prepare an appropriate next
response to submit to the server.

**Parameters:** challenge

- The non-null challenge sent from the server.
The challenge array may have zero length.
**Returns:** The possibly null response to send to the server.
It is null if the challenge accompanied a "SUCCESS" status and the challenge
only contains data for the client to update its state and no response
needs to be sent to the server. The response is a zero-length byte
array if the client is to send a response with no data.
**Throws:** SaslException

- If an error occurred while processing
the challenge or generating a response.

- isComplete

```java
boolean isComplete()
```

Determines whether the authentication exchange has completed.
This method may be called at any time, but typically, it
will not be called until the caller has received indication
from the server
(in a protocol-specific manner) that the exchange has completed.

**Returns:** true if the authentication exchange has completed; false otherwise.

- unwrap

```java
byte[] unwrap​(byte[] incoming,
int offset,
int len)
throws
SaslException
```

Unwraps a byte array received from the server.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true) and only if
the authentication exchange has negotiated integrity and/or privacy
as the quality of protection; otherwise, an

IllegalStateException

is thrown.

incoming

is the contents of the SASL buffer as defined in RFC 2222
without the leading four octet field that represents the length.

offset

and

len

specify the portion of

incoming

to use.

**Parameters:** incoming

- A non-null byte array containing the encoded bytes
from the server.
**Parameters:** offset

- The starting position at

incoming

of the bytes to use.
**Parameters:** len

- The number of bytes from

incoming

to use.
**Returns:** A non-null byte array containing the decoded bytes.
**Throws:** SaslException

- if

incoming

cannot be successfully
unwrapped.
**Throws:** IllegalStateException

- if the authentication exchange has
not completed, or if the negotiated quality of protection
has neither integrity nor privacy.

- wrap

```java
byte[] wrap​(byte[] outgoing,
int offset,
int len)
throws
SaslException
```

Wraps a byte array to be sent to the server.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true) and only if
the authentication exchange has negotiated integrity and/or privacy
as the quality of protection; otherwise, an

IllegalStateException

is thrown.

The result of this method will make up the contents of the SASL buffer
as defined in RFC 2222 without the leading four octet field that
represents the length.

offset

and

len

specify the portion of

outgoing

to use.

**Parameters:** outgoing

- A non-null byte array containing the bytes to encode.
**Parameters:** offset

- The starting position at

outgoing

of the bytes to use.
**Parameters:** len

- The number of bytes from

outgoing

to use.
**Returns:** A non-null byte array containing the encoded bytes.
**Throws:** SaslException

- if

outgoing

cannot be successfully
wrapped.
**Throws:** IllegalStateException

- if the authentication exchange has
not completed, or if the negotiated quality of protection
has neither integrity nor privacy.

- getNegotiatedProperty

```java
Object
getNegotiatedProperty​(
String
propName)
```

Retrieves the negotiated property.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true); otherwise, an

IllegalStateException

is thrown.

The

Sasl

class includes several well-known property names
(For example,

Sasl.QOP

). A SASL provider can support other
properties which are specific to the vendor and/or a mechanism.

**Parameters:** propName

- The non-null property name.
**Returns:** The value of the negotiated property. If null, the property was
not negotiated or is not applicable to this mechanism.
**Throws:** IllegalStateException

- if this authentication exchange
has not completed

- dispose

```java
void dispose()
throws
SaslException
```

Disposes of any system resources or security-sensitive information
the SaslClient might be using. Invoking this method invalidates
the SaslClient instance. This method is idempotent.

**Throws:** SaslException

- If a problem was encountered while disposing
the resources.

---

#### Method Detail

getMechanismName

```java
String
getMechanismName()
```

Returns the IANA-registered mechanism name of this SASL client.
(e.g. "CRAM-MD5", "GSSAPI").

**Returns:** A non-null string representing the IANA-registered mechanism name.

---

#### getMechanismName

String

getMechanismName()

Returns the IANA-registered mechanism name of this SASL client.
(e.g. "CRAM-MD5", "GSSAPI").

hasInitialResponse

```java
boolean hasInitialResponse()
```

Determines whether this mechanism has an optional initial response.
If true, caller should call

evaluateChallenge()

with an
empty array to get the initial response.

**Returns:** true if this mechanism has an initial response.

---

#### hasInitialResponse

boolean hasInitialResponse()

Determines whether this mechanism has an optional initial response.
If true, caller should call

evaluateChallenge()

with an
empty array to get the initial response.

evaluateChallenge

```java
byte[] evaluateChallenge​(byte[] challenge)
throws
SaslException
```

Evaluates the challenge data and generates a response.
If a challenge is received from the server during the authentication
process, this method is called to prepare an appropriate next
response to submit to the server.

**Parameters:** challenge

- The non-null challenge sent from the server.
The challenge array may have zero length.
**Returns:** The possibly null response to send to the server.
It is null if the challenge accompanied a "SUCCESS" status and the challenge
only contains data for the client to update its state and no response
needs to be sent to the server. The response is a zero-length byte
array if the client is to send a response with no data.
**Throws:** SaslException

- If an error occurred while processing
the challenge or generating a response.

---

#### evaluateChallenge

byte[] evaluateChallenge​(byte[] challenge)
throws

SaslException

Evaluates the challenge data and generates a response.
If a challenge is received from the server during the authentication
process, this method is called to prepare an appropriate next
response to submit to the server.

isComplete

```java
boolean isComplete()
```

Determines whether the authentication exchange has completed.
This method may be called at any time, but typically, it
will not be called until the caller has received indication
from the server
(in a protocol-specific manner) that the exchange has completed.

**Returns:** true if the authentication exchange has completed; false otherwise.

---

#### isComplete

boolean isComplete()

Determines whether the authentication exchange has completed.
This method may be called at any time, but typically, it
will not be called until the caller has received indication
from the server
(in a protocol-specific manner) that the exchange has completed.

unwrap

```java
byte[] unwrap​(byte[] incoming,
int offset,
int len)
throws
SaslException
```

Unwraps a byte array received from the server.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true) and only if
the authentication exchange has negotiated integrity and/or privacy
as the quality of protection; otherwise, an

IllegalStateException

is thrown.

incoming

is the contents of the SASL buffer as defined in RFC 2222
without the leading four octet field that represents the length.

offset

and

len

specify the portion of

incoming

to use.

**Parameters:** incoming

- A non-null byte array containing the encoded bytes
from the server.
**Parameters:** offset

- The starting position at

incoming

of the bytes to use.
**Parameters:** len

- The number of bytes from

incoming

to use.
**Returns:** A non-null byte array containing the decoded bytes.
**Throws:** SaslException

- if

incoming

cannot be successfully
unwrapped.
**Throws:** IllegalStateException

- if the authentication exchange has
not completed, or if the negotiated quality of protection
has neither integrity nor privacy.

---

#### unwrap

byte[] unwrap​(byte[] incoming,
int offset,
int len)
throws

SaslException

Unwraps a byte array received from the server.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true) and only if
the authentication exchange has negotiated integrity and/or privacy
as the quality of protection; otherwise, an

IllegalStateException

is thrown.

incoming

is the contents of the SASL buffer as defined in RFC 2222
without the leading four octet field that represents the length.

offset

and

len

specify the portion of

incoming

to use.

incoming

is the contents of the SASL buffer as defined in RFC 2222
without the leading four octet field that represents the length.

offset

and

len

specify the portion of

incoming

to use.

wrap

```java
byte[] wrap​(byte[] outgoing,
int offset,
int len)
throws
SaslException
```

Wraps a byte array to be sent to the server.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true) and only if
the authentication exchange has negotiated integrity and/or privacy
as the quality of protection; otherwise, an

IllegalStateException

is thrown.

The result of this method will make up the contents of the SASL buffer
as defined in RFC 2222 without the leading four octet field that
represents the length.

offset

and

len

specify the portion of

outgoing

to use.

**Parameters:** outgoing

- A non-null byte array containing the bytes to encode.
**Parameters:** offset

- The starting position at

outgoing

of the bytes to use.
**Parameters:** len

- The number of bytes from

outgoing

to use.
**Returns:** A non-null byte array containing the encoded bytes.
**Throws:** SaslException

- if

outgoing

cannot be successfully
wrapped.
**Throws:** IllegalStateException

- if the authentication exchange has
not completed, or if the negotiated quality of protection
has neither integrity nor privacy.

---

#### wrap

byte[] wrap​(byte[] outgoing,
int offset,
int len)
throws

SaslException

Wraps a byte array to be sent to the server.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true) and only if
the authentication exchange has negotiated integrity and/or privacy
as the quality of protection; otherwise, an

IllegalStateException

is thrown.

The result of this method will make up the contents of the SASL buffer
as defined in RFC 2222 without the leading four octet field that
represents the length.

offset

and

len

specify the portion of

outgoing

to use.

The result of this method will make up the contents of the SASL buffer
as defined in RFC 2222 without the leading four octet field that
represents the length.

offset

and

len

specify the portion of

outgoing

to use.

getNegotiatedProperty

```java
Object
getNegotiatedProperty​(
String
propName)
```

Retrieves the negotiated property.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true); otherwise, an

IllegalStateException

is thrown.

The

Sasl

class includes several well-known property names
(For example,

Sasl.QOP

). A SASL provider can support other
properties which are specific to the vendor and/or a mechanism.

**Parameters:** propName

- The non-null property name.
**Returns:** The value of the negotiated property. If null, the property was
not negotiated or is not applicable to this mechanism.
**Throws:** IllegalStateException

- if this authentication exchange
has not completed

---

#### getNegotiatedProperty

Object

getNegotiatedProperty​(

String

propName)

Retrieves the negotiated property.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true); otherwise, an

IllegalStateException

is thrown.

The

Sasl

class includes several well-known property names
(For example,

Sasl.QOP

). A SASL provider can support other
properties which are specific to the vendor and/or a mechanism.

The

Sasl

class includes several well-known property names
(For example,

Sasl.QOP

). A SASL provider can support other
properties which are specific to the vendor and/or a mechanism.

dispose

```java
void dispose()
throws
SaslException
```

Disposes of any system resources or security-sensitive information
the SaslClient might be using. Invoking this method invalidates
the SaslClient instance. This method is idempotent.

**Throws:** SaslException

- If a problem was encountered while disposing
the resources.

---

#### dispose

void dispose()
throws

SaslException

Disposes of any system resources or security-sensitive information
the SaslClient might be using. Invoking this method invalidates
the SaslClient instance. This method is idempotent.

---

