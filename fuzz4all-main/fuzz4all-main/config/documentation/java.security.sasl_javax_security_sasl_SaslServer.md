# Interface SaslServer

**Source:** `java.security.sasl\javax\security\sasl\SaslServer.html`

### Class Description

```java
public interface
SaslServer
```

Performs SASL authentication as a server.

A server such an LDAP server gets an instance of this
class in order to perform authentication defined by a specific SASL
mechanism. Invoking methods on the

SaslServer

instance
generates challenges according to the SASL
mechanism implemented by the

SaslServer

.
As the authentication proceeds, the instance
encapsulates the state of a SASL server's authentication exchange.

Here's an example of how an LDAP server might use a

SaslServer

.
It first gets an instance of a

SaslServer

for the SASL mechanism
requested by the client:

```java
SaslServer ss = Sasl.createSaslServer(mechanism,
"ldap", myFQDN, props, callbackHandler);
```

It can then proceed to use the server for authentication.
For example, suppose the LDAP server received an LDAP BIND request
containing the name of the SASL mechanism and an (optional) initial
response. It then might use the server as follows:

```java
while (!ss.isComplete()) {
try {
byte[] challenge = ss.evaluateResponse(response);
if (ss.isComplete()) {
status = ldap.sendBindResponse(mechanism, challenge, SUCCESS);
} else {
status = ldap.sendBindResponse(mechanism, challenge,
SASL_BIND_IN_PROGRESS);
response = ldap.readBindRequest();
}
} catch (SaslException e) {
status = ldap.sendErrorResponse(e);
break;
}
}
if (ss.isComplete() && status == SUCCESS) {
String qop = (String) sc.getNegotiatedProperty(Sasl.QOP);
if (qop != null
&& (qop.equalsIgnoreCase("auth-int")
|| qop.equalsIgnoreCase("auth-conf"))) {

// Use SaslServer.wrap() and SaslServer.unwrap() for future
// communication with client
ldap.in = new SecureInputStream(ss, ldap.in);
ldap.out = new SecureOutputStream(ss, ldap.out);
}
}
```

**Since:** 1.5
**See Also:** Sasl

,

SaslServerFactory

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### String
getMechanismName()

Returns the IANA-registered mechanism name of this SASL server.
(e.g. "CRAM-MD5", "GSSAPI").

**Returns:**
- A non-null string representing the IANA-registered mechanism name.

---

#### byte[] evaluateResponse​(byte[] response)
throws
SaslException

Evaluates the response data and generates a challenge.

If a response is received from the client during the authentication
process, this method is called to prepare an appropriate next
challenge to submit to the client. The challenge is null if the
authentication has succeeded and no more challenge data is to be sent
to the client. It is non-null if the authentication must be continued
by sending a challenge to the client, or if the authentication has
succeeded but challenge data needs to be processed by the client.

isComplete()

should be called
after each call to

evaluateResponse()

,to determine if any further
response is needed from the client.

**Parameters:**
- response

- The non-null (but possibly empty) response sent
by the client.

**Returns:**
- The possibly null challenge to send to the client.
It is null if the authentication has succeeded and there is
no more challenge data to be sent to the client.

**Throws:**
- SaslException

- If an error occurred while processing
the response or generating a challenge.

---

#### boolean isComplete()

Determines whether the authentication exchange has completed.
This method is typically called after each invocation of

evaluateResponse()

to determine whether the
authentication has completed successfully or should be continued.

**Returns:**
- true if the authentication exchange has completed; false otherwise.

---

#### String
getAuthorizationID()

Reports the authorization ID in effect for the client of this
session.
This method can only be called if isComplete() returns true.

**Returns:**
- The authorization ID of the client.

**Throws:**
- IllegalStateException

- if this authentication session has not completed

---

#### byte[] unwrap​(byte[] incoming,
int offset,
int len)
throws
SaslException

Unwraps a byte array received from the client.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true) and only if
the authentication exchange has negotiated integrity and/or privacy
as the quality of protection; otherwise,
an

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
from the client.
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
has neither integrity nor privacy

---

#### byte[] wrap​(byte[] outgoing,
int offset,
int len)
throws
SaslException

Wraps a byte array to be sent to the client.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true) and only if
the authentication exchange has negotiated integrity and/or privacy
as the quality of protection; otherwise, a

SaslException

is thrown.

The result of this method
will make up the contents of the SASL buffer as defined in RFC 2222
without the leading four octet field that represents the length.

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
not completed, or if the negotiated quality of protection has
neither integrity nor privacy.

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

- the property

**Returns:**
- The value of the negotiated property. If null, the property was
not negotiated or is not applicable to this mechanism.

**Throws:**
- IllegalStateException

- if this authentication exchange has not completed

---

#### void dispose()
throws
SaslException

Disposes of any system resources or security-sensitive information
the SaslServer might be using. Invoking this method invalidates
the SaslServer instance. This method is idempotent.

**Throws:**
- SaslException

- If a problem was encountered while disposing
the resources.

---

### Additional Sections

#### Interface SaslServer

```java
public interface
SaslServer
```

Performs SASL authentication as a server.

A server such an LDAP server gets an instance of this
class in order to perform authentication defined by a specific SASL
mechanism. Invoking methods on the

SaslServer

instance
generates challenges according to the SASL
mechanism implemented by the

SaslServer

.
As the authentication proceeds, the instance
encapsulates the state of a SASL server's authentication exchange.

Here's an example of how an LDAP server might use a

SaslServer

.
It first gets an instance of a

SaslServer

for the SASL mechanism
requested by the client:

```java
SaslServer ss = Sasl.createSaslServer(mechanism,
"ldap", myFQDN, props, callbackHandler);
```

It can then proceed to use the server for authentication.
For example, suppose the LDAP server received an LDAP BIND request
containing the name of the SASL mechanism and an (optional) initial
response. It then might use the server as follows:

```java
while (!ss.isComplete()) {
try {
byte[] challenge = ss.evaluateResponse(response);
if (ss.isComplete()) {
status = ldap.sendBindResponse(mechanism, challenge, SUCCESS);
} else {
status = ldap.sendBindResponse(mechanism, challenge,
SASL_BIND_IN_PROGRESS);
response = ldap.readBindRequest();
}
} catch (SaslException e) {
status = ldap.sendErrorResponse(e);
break;
}
}
if (ss.isComplete() && status == SUCCESS) {
String qop = (String) sc.getNegotiatedProperty(Sasl.QOP);
if (qop != null
&& (qop.equalsIgnoreCase("auth-int")
|| qop.equalsIgnoreCase("auth-conf"))) {

// Use SaslServer.wrap() and SaslServer.unwrap() for future
// communication with client
ldap.in = new SecureInputStream(ss, ldap.in);
ldap.out = new SecureOutputStream(ss, ldap.out);
}
}
```

**Since:** 1.5
**See Also:** Sasl

,

SaslServerFactory

public interface

SaslServer

Performs SASL authentication as a server.

A server such an LDAP server gets an instance of this
class in order to perform authentication defined by a specific SASL
mechanism. Invoking methods on the

SaslServer

instance
generates challenges according to the SASL
mechanism implemented by the

SaslServer

.
As the authentication proceeds, the instance
encapsulates the state of a SASL server's authentication exchange.

Here's an example of how an LDAP server might use a

SaslServer

.
It first gets an instance of a

SaslServer

for the SASL mechanism
requested by the client:

```java
SaslServer ss = Sasl.createSaslServer(mechanism,
"ldap", myFQDN, props, callbackHandler);
```

It can then proceed to use the server for authentication.
For example, suppose the LDAP server received an LDAP BIND request
containing the name of the SASL mechanism and an (optional) initial
response. It then might use the server as follows:

```java
while (!ss.isComplete()) {
try {
byte[] challenge = ss.evaluateResponse(response);
if (ss.isComplete()) {
status = ldap.sendBindResponse(mechanism, challenge, SUCCESS);
} else {
status = ldap.sendBindResponse(mechanism, challenge,
SASL_BIND_IN_PROGRESS);
response = ldap.readBindRequest();
}
} catch (SaslException e) {
status = ldap.sendErrorResponse(e);
break;
}
}
if (ss.isComplete() && status == SUCCESS) {
String qop = (String) sc.getNegotiatedProperty(Sasl.QOP);
if (qop != null
&& (qop.equalsIgnoreCase("auth-int")
|| qop.equalsIgnoreCase("auth-conf"))) {

// Use SaslServer.wrap() and SaslServer.unwrap() for future
// communication with client
ldap.in = new SecureInputStream(ss, ldap.in);
ldap.out = new SecureOutputStream(ss, ldap.out);
}
}
```

A server such an LDAP server gets an instance of this
class in order to perform authentication defined by a specific SASL
mechanism. Invoking methods on the

SaslServer

instance
generates challenges according to the SASL
mechanism implemented by the

SaslServer

.
As the authentication proceeds, the instance
encapsulates the state of a SASL server's authentication exchange.

Here's an example of how an LDAP server might use a

SaslServer

.
It first gets an instance of a

SaslServer

for the SASL mechanism
requested by the client:

```java
SaslServer ss = Sasl.createSaslServer(mechanism,
"ldap", myFQDN, props, callbackHandler);
```

It can then proceed to use the server for authentication.
For example, suppose the LDAP server received an LDAP BIND request
containing the name of the SASL mechanism and an (optional) initial
response. It then might use the server as follows:

```java
while (!ss.isComplete()) {
try {
byte[] challenge = ss.evaluateResponse(response);
if (ss.isComplete()) {
status = ldap.sendBindResponse(mechanism, challenge, SUCCESS);
} else {
status = ldap.sendBindResponse(mechanism, challenge,
SASL_BIND_IN_PROGRESS);
response = ldap.readBindRequest();
}
} catch (SaslException e) {
status = ldap.sendErrorResponse(e);
break;
}
}
if (ss.isComplete() && status == SUCCESS) {
String qop = (String) sc.getNegotiatedProperty(Sasl.QOP);
if (qop != null
&& (qop.equalsIgnoreCase("auth-int")
|| qop.equalsIgnoreCase("auth-conf"))) {

// Use SaslServer.wrap() and SaslServer.unwrap() for future
// communication with client
ldap.in = new SecureInputStream(ss, ldap.in);
ldap.out = new SecureOutputStream(ss, ldap.out);
}
}
```

Here's an example of how an LDAP server might use a

SaslServer

.
It first gets an instance of a

SaslServer

for the SASL mechanism
requested by the client:

```java
SaslServer ss = Sasl.createSaslServer(mechanism,
"ldap", myFQDN, props, callbackHandler);
```

It can then proceed to use the server for authentication.
For example, suppose the LDAP server received an LDAP BIND request
containing the name of the SASL mechanism and an (optional) initial
response. It then might use the server as follows:

```java
while (!ss.isComplete()) {
try {
byte[] challenge = ss.evaluateResponse(response);
if (ss.isComplete()) {
status = ldap.sendBindResponse(mechanism, challenge, SUCCESS);
} else {
status = ldap.sendBindResponse(mechanism, challenge,
SASL_BIND_IN_PROGRESS);
response = ldap.readBindRequest();
}
} catch (SaslException e) {
status = ldap.sendErrorResponse(e);
break;
}
}
if (ss.isComplete() && status == SUCCESS) {
String qop = (String) sc.getNegotiatedProperty(Sasl.QOP);
if (qop != null
&& (qop.equalsIgnoreCase("auth-int")
|| qop.equalsIgnoreCase("auth-conf"))) {

// Use SaslServer.wrap() and SaslServer.unwrap() for future
// communication with client
ldap.in = new SecureInputStream(ss, ldap.in);
ldap.out = new SecureOutputStream(ss, ldap.out);
}
}
```

SaslServer ss = Sasl.createSaslServer(mechanism,
"ldap", myFQDN, props, callbackHandler);

while (!ss.isComplete()) {
try {
byte[] challenge = ss.evaluateResponse(response);
if (ss.isComplete()) {
status = ldap.sendBindResponse(mechanism, challenge, SUCCESS);
} else {
status = ldap.sendBindResponse(mechanism, challenge,
SASL_BIND_IN_PROGRESS);
response = ldap.readBindRequest();
}
} catch (SaslException e) {
status = ldap.sendErrorResponse(e);
break;
}
}
if (ss.isComplete() && status == SUCCESS) {
String qop = (String) sc.getNegotiatedProperty(Sasl.QOP);
if (qop != null
&& (qop.equalsIgnoreCase("auth-int")
|| qop.equalsIgnoreCase("auth-conf"))) {

// Use SaslServer.wrap() and SaslServer.unwrap() for future
// communication with client
ldap.in = new SecureInputStream(ss, ldap.in);
ldap.out = new SecureOutputStream(ss, ldap.out);
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
the SaslServer might be using.

byte[]

evaluateResponse

​(byte[] response)

Evaluates the response data and generates a challenge.

String

getAuthorizationID

()

Reports the authorization ID in effect for the client of this
session.

String

getMechanismName

()

Returns the IANA-registered mechanism name of this SASL server.

Object

getNegotiatedProperty

​(

String

propName)

Retrieves the negotiated property.

boolean

isComplete

()

Determines whether the authentication exchange has completed.

byte[]

unwrap

​(byte[] incoming,
int offset,
int len)

Unwraps a byte array received from the client.

byte[]

wrap

​(byte[] outgoing,
int offset,
int len)

Wraps a byte array to be sent to the client.

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
the SaslServer might be using.

byte[]

evaluateResponse

​(byte[] response)

Evaluates the response data and generates a challenge.

String

getAuthorizationID

()

Reports the authorization ID in effect for the client of this
session.

String

getMechanismName

()

Returns the IANA-registered mechanism name of this SASL server.

Object

getNegotiatedProperty

​(

String

propName)

Retrieves the negotiated property.

boolean

isComplete

()

Determines whether the authentication exchange has completed.

byte[]

unwrap

​(byte[] incoming,
int offset,
int len)

Unwraps a byte array received from the client.

byte[]

wrap

​(byte[] outgoing,
int offset,
int len)

Wraps a byte array to be sent to the client.

---

#### Method Summary

Disposes of any system resources or security-sensitive information
the SaslServer might be using.

Evaluates the response data and generates a challenge.

Reports the authorization ID in effect for the client of this
session.

Returns the IANA-registered mechanism name of this SASL server.

Retrieves the negotiated property.

Determines whether the authentication exchange has completed.

Unwraps a byte array received from the client.

Wraps a byte array to be sent to the client.

============ METHOD DETAIL ==========

- Method Detail

- getMechanismName

```java
String
getMechanismName()
```

Returns the IANA-registered mechanism name of this SASL server.
(e.g. "CRAM-MD5", "GSSAPI").

**Returns:** A non-null string representing the IANA-registered mechanism name.

- evaluateResponse

```java
byte[] evaluateResponse​(byte[] response)
throws
SaslException
```

Evaluates the response data and generates a challenge.

If a response is received from the client during the authentication
process, this method is called to prepare an appropriate next
challenge to submit to the client. The challenge is null if the
authentication has succeeded and no more challenge data is to be sent
to the client. It is non-null if the authentication must be continued
by sending a challenge to the client, or if the authentication has
succeeded but challenge data needs to be processed by the client.

isComplete()

should be called
after each call to

evaluateResponse()

,to determine if any further
response is needed from the client.

**Parameters:** response

- The non-null (but possibly empty) response sent
by the client.
**Returns:** The possibly null challenge to send to the client.
It is null if the authentication has succeeded and there is
no more challenge data to be sent to the client.
**Throws:** SaslException

- If an error occurred while processing
the response or generating a challenge.

- isComplete

```java
boolean isComplete()
```

Determines whether the authentication exchange has completed.
This method is typically called after each invocation of

evaluateResponse()

to determine whether the
authentication has completed successfully or should be continued.

**Returns:** true if the authentication exchange has completed; false otherwise.

- getAuthorizationID

```java
String
getAuthorizationID()
```

Reports the authorization ID in effect for the client of this
session.
This method can only be called if isComplete() returns true.

**Returns:** The authorization ID of the client.
**Throws:** IllegalStateException

- if this authentication session has not completed

- unwrap

```java
byte[] unwrap​(byte[] incoming,
int offset,
int len)
throws
SaslException
```

Unwraps a byte array received from the client.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true) and only if
the authentication exchange has negotiated integrity and/or privacy
as the quality of protection; otherwise,
an

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
from the client.
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
has neither integrity nor privacy

- wrap

```java
byte[] wrap​(byte[] outgoing,
int offset,
int len)
throws
SaslException
```

Wraps a byte array to be sent to the client.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true) and only if
the authentication exchange has negotiated integrity and/or privacy
as the quality of protection; otherwise, a

SaslException

is thrown.

The result of this method
will make up the contents of the SASL buffer as defined in RFC 2222
without the leading four octet field that represents the length.

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
not completed, or if the negotiated quality of protection has
neither integrity nor privacy.

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

- the property
**Returns:** The value of the negotiated property. If null, the property was
not negotiated or is not applicable to this mechanism.
**Throws:** IllegalStateException

- if this authentication exchange has not completed

- dispose

```java
void dispose()
throws
SaslException
```

Disposes of any system resources or security-sensitive information
the SaslServer might be using. Invoking this method invalidates
the SaslServer instance. This method is idempotent.

**Throws:** SaslException

- If a problem was encountered while disposing
the resources.

Method Detail

- getMechanismName

```java
String
getMechanismName()
```

Returns the IANA-registered mechanism name of this SASL server.
(e.g. "CRAM-MD5", "GSSAPI").

**Returns:** A non-null string representing the IANA-registered mechanism name.

- evaluateResponse

```java
byte[] evaluateResponse​(byte[] response)
throws
SaslException
```

Evaluates the response data and generates a challenge.

If a response is received from the client during the authentication
process, this method is called to prepare an appropriate next
challenge to submit to the client. The challenge is null if the
authentication has succeeded and no more challenge data is to be sent
to the client. It is non-null if the authentication must be continued
by sending a challenge to the client, or if the authentication has
succeeded but challenge data needs to be processed by the client.

isComplete()

should be called
after each call to

evaluateResponse()

,to determine if any further
response is needed from the client.

**Parameters:** response

- The non-null (but possibly empty) response sent
by the client.
**Returns:** The possibly null challenge to send to the client.
It is null if the authentication has succeeded and there is
no more challenge data to be sent to the client.
**Throws:** SaslException

- If an error occurred while processing
the response or generating a challenge.

- isComplete

```java
boolean isComplete()
```

Determines whether the authentication exchange has completed.
This method is typically called after each invocation of

evaluateResponse()

to determine whether the
authentication has completed successfully or should be continued.

**Returns:** true if the authentication exchange has completed; false otherwise.

- getAuthorizationID

```java
String
getAuthorizationID()
```

Reports the authorization ID in effect for the client of this
session.
This method can only be called if isComplete() returns true.

**Returns:** The authorization ID of the client.
**Throws:** IllegalStateException

- if this authentication session has not completed

- unwrap

```java
byte[] unwrap​(byte[] incoming,
int offset,
int len)
throws
SaslException
```

Unwraps a byte array received from the client.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true) and only if
the authentication exchange has negotiated integrity and/or privacy
as the quality of protection; otherwise,
an

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
from the client.
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
has neither integrity nor privacy

- wrap

```java
byte[] wrap​(byte[] outgoing,
int offset,
int len)
throws
SaslException
```

Wraps a byte array to be sent to the client.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true) and only if
the authentication exchange has negotiated integrity and/or privacy
as the quality of protection; otherwise, a

SaslException

is thrown.

The result of this method
will make up the contents of the SASL buffer as defined in RFC 2222
without the leading four octet field that represents the length.

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
not completed, or if the negotiated quality of protection has
neither integrity nor privacy.

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

- the property
**Returns:** The value of the negotiated property. If null, the property was
not negotiated or is not applicable to this mechanism.
**Throws:** IllegalStateException

- if this authentication exchange has not completed

- dispose

```java
void dispose()
throws
SaslException
```

Disposes of any system resources or security-sensitive information
the SaslServer might be using. Invoking this method invalidates
the SaslServer instance. This method is idempotent.

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

Returns the IANA-registered mechanism name of this SASL server.
(e.g. "CRAM-MD5", "GSSAPI").

**Returns:** A non-null string representing the IANA-registered mechanism name.

---

#### getMechanismName

String

getMechanismName()

Returns the IANA-registered mechanism name of this SASL server.
(e.g. "CRAM-MD5", "GSSAPI").

evaluateResponse

```java
byte[] evaluateResponse​(byte[] response)
throws
SaslException
```

Evaluates the response data and generates a challenge.

If a response is received from the client during the authentication
process, this method is called to prepare an appropriate next
challenge to submit to the client. The challenge is null if the
authentication has succeeded and no more challenge data is to be sent
to the client. It is non-null if the authentication must be continued
by sending a challenge to the client, or if the authentication has
succeeded but challenge data needs to be processed by the client.

isComplete()

should be called
after each call to

evaluateResponse()

,to determine if any further
response is needed from the client.

**Parameters:** response

- The non-null (but possibly empty) response sent
by the client.
**Returns:** The possibly null challenge to send to the client.
It is null if the authentication has succeeded and there is
no more challenge data to be sent to the client.
**Throws:** SaslException

- If an error occurred while processing
the response or generating a challenge.

---

#### evaluateResponse

byte[] evaluateResponse​(byte[] response)
throws

SaslException

Evaluates the response data and generates a challenge.

If a response is received from the client during the authentication
process, this method is called to prepare an appropriate next
challenge to submit to the client. The challenge is null if the
authentication has succeeded and no more challenge data is to be sent
to the client. It is non-null if the authentication must be continued
by sending a challenge to the client, or if the authentication has
succeeded but challenge data needs to be processed by the client.

isComplete()

should be called
after each call to

evaluateResponse()

,to determine if any further
response is needed from the client.

isComplete

```java
boolean isComplete()
```

Determines whether the authentication exchange has completed.
This method is typically called after each invocation of

evaluateResponse()

to determine whether the
authentication has completed successfully or should be continued.

**Returns:** true if the authentication exchange has completed; false otherwise.

---

#### isComplete

boolean isComplete()

Determines whether the authentication exchange has completed.
This method is typically called after each invocation of

evaluateResponse()

to determine whether the
authentication has completed successfully or should be continued.

getAuthorizationID

```java
String
getAuthorizationID()
```

Reports the authorization ID in effect for the client of this
session.
This method can only be called if isComplete() returns true.

**Returns:** The authorization ID of the client.
**Throws:** IllegalStateException

- if this authentication session has not completed

---

#### getAuthorizationID

String

getAuthorizationID()

Reports the authorization ID in effect for the client of this
session.
This method can only be called if isComplete() returns true.

unwrap

```java
byte[] unwrap​(byte[] incoming,
int offset,
int len)
throws
SaslException
```

Unwraps a byte array received from the client.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true) and only if
the authentication exchange has negotiated integrity and/or privacy
as the quality of protection; otherwise,
an

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
from the client.
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
has neither integrity nor privacy

---

#### unwrap

byte[] unwrap​(byte[] incoming,
int offset,
int len)
throws

SaslException

Unwraps a byte array received from the client.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true) and only if
the authentication exchange has negotiated integrity and/or privacy
as the quality of protection; otherwise,
an

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

Wraps a byte array to be sent to the client.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true) and only if
the authentication exchange has negotiated integrity and/or privacy
as the quality of protection; otherwise, a

SaslException

is thrown.

The result of this method
will make up the contents of the SASL buffer as defined in RFC 2222
without the leading four octet field that represents the length.

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
not completed, or if the negotiated quality of protection has
neither integrity nor privacy.

---

#### wrap

byte[] wrap​(byte[] outgoing,
int offset,
int len)
throws

SaslException

Wraps a byte array to be sent to the client.
This method can be called only after the authentication exchange has
completed (i.e., when

isComplete()

returns true) and only if
the authentication exchange has negotiated integrity and/or privacy
as the quality of protection; otherwise, a

SaslException

is thrown.

The result of this method
will make up the contents of the SASL buffer as defined in RFC 2222
without the leading four octet field that represents the length.

offset

and

len

specify the portion of

outgoing

to use.

The result of this method
will make up the contents of the SASL buffer as defined in RFC 2222
without the leading four octet field that represents the length.

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

- the property
**Returns:** The value of the negotiated property. If null, the property was
not negotiated or is not applicable to this mechanism.
**Throws:** IllegalStateException

- if this authentication exchange has not completed

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
the SaslServer might be using. Invoking this method invalidates
the SaslServer instance. This method is idempotent.

**Throws:** SaslException

- If a problem was encountered while disposing
the resources.

---

#### dispose

void dispose()
throws

SaslException

Disposes of any system resources or security-sensitive information
the SaslServer might be using. Invoking this method invalidates
the SaslServer instance. This method is idempotent.

---

