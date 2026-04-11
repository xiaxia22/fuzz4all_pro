# Interface SaslServerFactory

**Source:** `java.security.sasl\javax\security\sasl\SaslServerFactory.html`

### Class Description

```java
public interface
SaslServerFactory
```

An interface for creating instances of

SaslServer

.
A class that implements this interface
must be thread-safe and handle multiple simultaneous
requests. It must also have a public constructor that accepts no
argument.

This interface is not normally accessed directly by a server, which will use the

Sasl

static methods
instead. However, a particular environment may provide and install a
new or different

SaslServerFactory

.

**Since:** 1.5
**See Also:** SaslServer

,

Sasl

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### SaslServer
createSaslServer​(
String
mechanism,

String
protocol,

String
serverName,

Map
<
String
,​?> props,

CallbackHandler
cbh)
throws
SaslException

Creates a

SaslServer

using the parameters supplied.
It returns null
if no

SaslServer

can be created using the parameters supplied.
Throws

SaslException

if it cannot create a

SaslServer

because of an error.

**Parameters:**
- mechanism

- The non-null
IANA-registered name of a SASL mechanism. (e.g. "GSSAPI", "CRAM-MD5").
- protocol

- The non-null string name of the protocol for which
the authentication is being performed (e.g., "ldap").
- serverName

- The fully qualified host name of the server to
authenticate to, or null if the server is not bound to any specific host
name. If the mechanism does not allow an unbound server, a

SaslException

will be thrown.
- props

- The possibly null set of properties used to select the SASL
mechanism and to configure the authentication exchange of the selected
mechanism. See the

Sasl

class for a list of standard properties.
Other, possibly mechanism-specific, properties can be included.
Properties not relevant to the selected mechanism are ignored,
including any map entries with non-String keys.
- cbh

- The possibly null callback handler to used by the SASL
mechanisms to get further information from the application/library
to complete the authentication. For example, a SASL mechanism might
require the authentication ID, password and realm from the caller.
The authentication ID is requested by using a

NameCallback

.
The password is requested by using a

PasswordCallback

.
The realm is requested by using a

RealmChoiceCallback

if there is a list
of realms to choose from, and by using a

RealmCallback

if
the realm must be entered.

**Returns:**
- A possibly null

SaslServer

created using the parameters
supplied. If null, this factory cannot produce a

SaslServer

using the parameters supplied.

**Throws:**
- SaslException

- If cannot create a

SaslServer

because
of an error.

---

#### String
[] getMechanismNames​(
Map
<
String
,​?> props)

Returns an array of names of mechanisms that match the specified
mechanism selection policies.

**Parameters:**
- props

- The possibly null set of properties used to specify the
security policy of the SASL mechanisms. For example, if

props

contains the

Sasl.POLICY_NOPLAINTEXT

property with the value

"true"

, then the factory must not return any SASL mechanisms
that are susceptible to simple plain passive attacks.
See the

Sasl

class for a complete list of policy properties.
Non-policy related properties, if present in

props

, are ignored,
including any map entries with non-String keys.

**Returns:**
- A non-null array containing a IANA-registered SASL mechanism names.

---

### Additional Sections

#### Interface SaslServerFactory

```java
public interface
SaslServerFactory
```

An interface for creating instances of

SaslServer

.
A class that implements this interface
must be thread-safe and handle multiple simultaneous
requests. It must also have a public constructor that accepts no
argument.

This interface is not normally accessed directly by a server, which will use the

Sasl

static methods
instead. However, a particular environment may provide and install a
new or different

SaslServerFactory

.

**Since:** 1.5
**See Also:** SaslServer

,

Sasl

public interface

SaslServerFactory

An interface for creating instances of

SaslServer

.
A class that implements this interface
must be thread-safe and handle multiple simultaneous
requests. It must also have a public constructor that accepts no
argument.

This interface is not normally accessed directly by a server, which will use the

Sasl

static methods
instead. However, a particular environment may provide and install a
new or different

SaslServerFactory

.

This interface is not normally accessed directly by a server, which will use the

Sasl

static methods
instead. However, a particular environment may provide and install a
new or different

SaslServerFactory

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

SaslServer

createSaslServer

​(

String

mechanism,

String

protocol,

String

serverName,

Map

<

String

,​?> props,

CallbackHandler

cbh)

Creates a

SaslServer

using the parameters supplied.

String

[]

getMechanismNames

​(

Map

<

String

,​?> props)

Returns an array of names of mechanisms that match the specified
mechanism selection policies.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

SaslServer

createSaslServer

​(

String

mechanism,

String

protocol,

String

serverName,

Map

<

String

,​?> props,

CallbackHandler

cbh)

Creates a

SaslServer

using the parameters supplied.

String

[]

getMechanismNames

​(

Map

<

String

,​?> props)

Returns an array of names of mechanisms that match the specified
mechanism selection policies.

---

#### Method Summary

Creates a

SaslServer

using the parameters supplied.

Returns an array of names of mechanisms that match the specified
mechanism selection policies.

============ METHOD DETAIL ==========

- Method Detail

- createSaslServer

```java
SaslServer
createSaslServer​(
String
mechanism,

String
protocol,

String
serverName,

Map
<
String
,​?> props,

CallbackHandler
cbh)
throws
SaslException
```

Creates a

SaslServer

using the parameters supplied.
It returns null
if no

SaslServer

can be created using the parameters supplied.
Throws

SaslException

if it cannot create a

SaslServer

because of an error.

**Parameters:** mechanism

- The non-null
IANA-registered name of a SASL mechanism. (e.g. "GSSAPI", "CRAM-MD5").
**Parameters:** protocol

- The non-null string name of the protocol for which
the authentication is being performed (e.g., "ldap").
**Parameters:** serverName

- The fully qualified host name of the server to
authenticate to, or null if the server is not bound to any specific host
name. If the mechanism does not allow an unbound server, a

SaslException

will be thrown.
**Parameters:** props

- The possibly null set of properties used to select the SASL
mechanism and to configure the authentication exchange of the selected
mechanism. See the

Sasl

class for a list of standard properties.
Other, possibly mechanism-specific, properties can be included.
Properties not relevant to the selected mechanism are ignored,
including any map entries with non-String keys.
**Parameters:** cbh

- The possibly null callback handler to used by the SASL
mechanisms to get further information from the application/library
to complete the authentication. For example, a SASL mechanism might
require the authentication ID, password and realm from the caller.
The authentication ID is requested by using a

NameCallback

.
The password is requested by using a

PasswordCallback

.
The realm is requested by using a

RealmChoiceCallback

if there is a list
of realms to choose from, and by using a

RealmCallback

if
the realm must be entered.
**Returns:** A possibly null

SaslServer

created using the parameters
supplied. If null, this factory cannot produce a

SaslServer

using the parameters supplied.
**Throws:** SaslException

- If cannot create a

SaslServer

because
of an error.

- getMechanismNames

```java
String
[] getMechanismNames​(
Map
<
String
,​?> props)
```

Returns an array of names of mechanisms that match the specified
mechanism selection policies.

**Parameters:** props

- The possibly null set of properties used to specify the
security policy of the SASL mechanisms. For example, if

props

contains the

Sasl.POLICY_NOPLAINTEXT

property with the value

"true"

, then the factory must not return any SASL mechanisms
that are susceptible to simple plain passive attacks.
See the

Sasl

class for a complete list of policy properties.
Non-policy related properties, if present in

props

, are ignored,
including any map entries with non-String keys.
**Returns:** A non-null array containing a IANA-registered SASL mechanism names.

Method Detail

- createSaslServer

```java
SaslServer
createSaslServer​(
String
mechanism,

String
protocol,

String
serverName,

Map
<
String
,​?> props,

CallbackHandler
cbh)
throws
SaslException
```

Creates a

SaslServer

using the parameters supplied.
It returns null
if no

SaslServer

can be created using the parameters supplied.
Throws

SaslException

if it cannot create a

SaslServer

because of an error.

**Parameters:** mechanism

- The non-null
IANA-registered name of a SASL mechanism. (e.g. "GSSAPI", "CRAM-MD5").
**Parameters:** protocol

- The non-null string name of the protocol for which
the authentication is being performed (e.g., "ldap").
**Parameters:** serverName

- The fully qualified host name of the server to
authenticate to, or null if the server is not bound to any specific host
name. If the mechanism does not allow an unbound server, a

SaslException

will be thrown.
**Parameters:** props

- The possibly null set of properties used to select the SASL
mechanism and to configure the authentication exchange of the selected
mechanism. See the

Sasl

class for a list of standard properties.
Other, possibly mechanism-specific, properties can be included.
Properties not relevant to the selected mechanism are ignored,
including any map entries with non-String keys.
**Parameters:** cbh

- The possibly null callback handler to used by the SASL
mechanisms to get further information from the application/library
to complete the authentication. For example, a SASL mechanism might
require the authentication ID, password and realm from the caller.
The authentication ID is requested by using a

NameCallback

.
The password is requested by using a

PasswordCallback

.
The realm is requested by using a

RealmChoiceCallback

if there is a list
of realms to choose from, and by using a

RealmCallback

if
the realm must be entered.
**Returns:** A possibly null

SaslServer

created using the parameters
supplied. If null, this factory cannot produce a

SaslServer

using the parameters supplied.
**Throws:** SaslException

- If cannot create a

SaslServer

because
of an error.

- getMechanismNames

```java
String
[] getMechanismNames​(
Map
<
String
,​?> props)
```

Returns an array of names of mechanisms that match the specified
mechanism selection policies.

**Parameters:** props

- The possibly null set of properties used to specify the
security policy of the SASL mechanisms. For example, if

props

contains the

Sasl.POLICY_NOPLAINTEXT

property with the value

"true"

, then the factory must not return any SASL mechanisms
that are susceptible to simple plain passive attacks.
See the

Sasl

class for a complete list of policy properties.
Non-policy related properties, if present in

props

, are ignored,
including any map entries with non-String keys.
**Returns:** A non-null array containing a IANA-registered SASL mechanism names.

---

#### Method Detail

createSaslServer

```java
SaslServer
createSaslServer​(
String
mechanism,

String
protocol,

String
serverName,

Map
<
String
,​?> props,

CallbackHandler
cbh)
throws
SaslException
```

Creates a

SaslServer

using the parameters supplied.
It returns null
if no

SaslServer

can be created using the parameters supplied.
Throws

SaslException

if it cannot create a

SaslServer

because of an error.

**Parameters:** mechanism

- The non-null
IANA-registered name of a SASL mechanism. (e.g. "GSSAPI", "CRAM-MD5").
**Parameters:** protocol

- The non-null string name of the protocol for which
the authentication is being performed (e.g., "ldap").
**Parameters:** serverName

- The fully qualified host name of the server to
authenticate to, or null if the server is not bound to any specific host
name. If the mechanism does not allow an unbound server, a

SaslException

will be thrown.
**Parameters:** props

- The possibly null set of properties used to select the SASL
mechanism and to configure the authentication exchange of the selected
mechanism. See the

Sasl

class for a list of standard properties.
Other, possibly mechanism-specific, properties can be included.
Properties not relevant to the selected mechanism are ignored,
including any map entries with non-String keys.
**Parameters:** cbh

- The possibly null callback handler to used by the SASL
mechanisms to get further information from the application/library
to complete the authentication. For example, a SASL mechanism might
require the authentication ID, password and realm from the caller.
The authentication ID is requested by using a

NameCallback

.
The password is requested by using a

PasswordCallback

.
The realm is requested by using a

RealmChoiceCallback

if there is a list
of realms to choose from, and by using a

RealmCallback

if
the realm must be entered.
**Returns:** A possibly null

SaslServer

created using the parameters
supplied. If null, this factory cannot produce a

SaslServer

using the parameters supplied.
**Throws:** SaslException

- If cannot create a

SaslServer

because
of an error.

---

#### createSaslServer

SaslServer

createSaslServer​(

String

mechanism,

String

protocol,

String

serverName,

Map

<

String

,​?> props,

CallbackHandler

cbh)
throws

SaslException

Creates a

SaslServer

using the parameters supplied.
It returns null
if no

SaslServer

can be created using the parameters supplied.
Throws

SaslException

if it cannot create a

SaslServer

because of an error.

getMechanismNames

```java
String
[] getMechanismNames​(
Map
<
String
,​?> props)
```

Returns an array of names of mechanisms that match the specified
mechanism selection policies.

**Parameters:** props

- The possibly null set of properties used to specify the
security policy of the SASL mechanisms. For example, if

props

contains the

Sasl.POLICY_NOPLAINTEXT

property with the value

"true"

, then the factory must not return any SASL mechanisms
that are susceptible to simple plain passive attacks.
See the

Sasl

class for a complete list of policy properties.
Non-policy related properties, if present in

props

, are ignored,
including any map entries with non-String keys.
**Returns:** A non-null array containing a IANA-registered SASL mechanism names.

---

#### getMechanismNames

String

[] getMechanismNames​(

Map

<

String

,​?> props)

Returns an array of names of mechanisms that match the specified
mechanism selection policies.

---

