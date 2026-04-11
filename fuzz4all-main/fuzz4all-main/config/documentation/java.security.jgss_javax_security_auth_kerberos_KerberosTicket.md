# Class KerberosTicket

**Source:** `java.security.jgss\javax\security\auth\kerberos\KerberosTicket.html`

### Class Description

```java
public class
KerberosTicket

extends
Object

implements
Destroyable
,
Refreshable
,
Serializable
```

This class encapsulates a Kerberos ticket and associated
information as viewed from the client's point of view. It captures all
information that the Key Distribution Center (KDC) sends to the client
in the reply message KDC-REP defined in the Kerberos Protocol
Specification (

RFC 4120

).

All Kerberos JAAS login modules that authenticate a user to a KDC should
use this class. Where available, the login module might even read this
information from a ticket cache in the operating system instead of
directly communicating with the KDC. During the commit phase of the JAAS
authentication process, the JAAS login module should instantiate this
class and store the instance in the private credential set of a

Subject

.

It might be necessary for the application to be granted a

PrivateCredentialPermission

if it needs to access a

KerberosTicket

instance from a

Subject

. This permission is not needed when the
application depends on the default JGSS Kerberos mechanism to access the

KerberosTicket

. In that case, however, the application will need an
appropriate

ServicePermission

.

Note that this class is applicable to both ticket granting tickets and
other regular service tickets. A ticket granting ticket is just a
special case of a more generalized service ticket.

**All Implemented Interfaces:** Serializable

,

Destroyable

,

Refreshable

---

### Field Details

*No entries found.*

### Constructor Details

#### public KerberosTicket​(byte[] asn1Encoding,

KerberosPrincipal
client,

KerberosPrincipal
server,
byte[] sessionKey,
int keyType,
boolean[] flags,

Date
authTime,

Date
startTime,

Date
endTime,

Date
renewTill,

InetAddress
[] clientAddresses)

Constructs a

KerberosTicket

using credentials information that a
client either receives from a KDC or reads from a cache.

**Parameters:**
- asn1Encoding

- the ASN.1 encoding of the ticket as defined by
the Kerberos protocol specification.
- client

- the client that owns this service
ticket
- server

- the service that this ticket is for
- sessionKey

- the raw bytes for the session key that must be
used to encrypt the authenticator that will be sent to the server
- keyType

- the key type for the session key as defined by the
Kerberos protocol specification.
- flags

- the ticket flags. Each element in this array indicates
the value for the corresponding bit in the ASN.1 BitString that
represents the ticket flags. If the number of elements in this array
is less than the number of flags used by the Kerberos protocol,
then the missing flags will be filled in with false.
- authTime

- the time of initial authentication for the client
- startTime

- the time after which the ticket will be valid. This
may be null in which case the value of authTime is treated as the
startTime.
- endTime

- the time after which the ticket will no longer be
valid
- renewTill

- an absolute expiration time for the ticket,
including all renewal that might be possible. This field may be null
for tickets that are not renewable.
- clientAddresses

- the addresses from where the ticket may be
used by the client. This field may be null when the ticket is usable
from any address.

---

### Method Details

#### public final
KerberosPrincipal
getClient()

Returns the client principal associated with this ticket.

**Returns:**
- the client principal, or

null

if destroyed.

---

#### public final
KerberosPrincipal
getServer()

Returns the service principal associated with this ticket.

**Returns:**
- the service principal, or

null

if destroyed.

---

#### public final
SecretKey
getSessionKey()

Returns the session key associated with this ticket. The return value
is always a

EncryptionKey

object.

**Returns:**
- the session key.

**Throws:**
- IllegalStateException

- if this ticket is destroyed

---

#### public final int getSessionKeyType()

Returns the key type of the session key associated with this
ticket as defined by the Kerberos Protocol Specification.

**Returns:**
- the key type of the session key associated with this
ticket.

**Throws:**
- IllegalStateException

- if this ticket is destroyed

**See Also:**
- getSessionKey()

---

#### public final boolean isForwardable()

Determines if this ticket is forwardable.

**Returns:**
- true if this ticket is forwardable, or false if not forwardable
or destroyed.

---

#### public final boolean isForwarded()

Determines if this ticket had been forwarded or was issued based on
authentication involving a forwarded ticket-granting ticket.

**Returns:**
- true if this ticket had been forwarded or was issued based on
authentication involving a forwarded ticket-granting ticket,
or false otherwise or destroyed.

---

#### public final boolean isProxiable()

Determines if this ticket is proxiable.

**Returns:**
- true if this ticket is proxiable, or false if not proxiable
or destroyed.

---

#### public final boolean isProxy()

Determines is this ticket is a proxy-ticket.

**Returns:**
- true if this ticket is a proxy-ticket, or false if not
a proxy-ticket or destroyed.

---

#### public final boolean isPostdated()

Determines is this ticket is post-dated.

**Returns:**
- true if this ticket is post-dated, or false if not post-dated
or destroyed.

---

#### public final boolean isRenewable()

Determines is this ticket is renewable. If so, the

refresh

method can be called, assuming the validity period for
renewing is not already over.

**Returns:**
- true if this ticket is renewable, or false if not renewable
or destroyed.

---

#### public final boolean isInitial()

Determines if this ticket was issued using the Kerberos AS-Exchange
protocol, and not issued based on some ticket-granting ticket.

**Returns:**
- true if this ticket was issued using the Kerberos AS-Exchange
protocol, or false if not issued this way or destroyed.

---

#### public final boolean[] getFlags()

Returns the flags associated with this ticket. Each element in the
returned array indicates the value for the corresponding bit in the
ASN.1 BitString that represents the ticket flags.

**Returns:**
- the flags associated with this ticket, or

null

if destroyed.

---

#### public final
Date
getAuthTime()

Returns the time that the client was authenticated.

**Returns:**
- the time that the client was authenticated
or

null

if the field is not set or
this ticket is destroyed.

---

#### public final
Date
getStartTime()

Returns the start time for this ticket's validity period.

**Returns:**
- the start time for this ticket's validity period
or

null

if the field is not set or
this ticket is destroyed.

---

#### public final
Date
getEndTime()

Returns the expiration time for this ticket's validity period.

**Returns:**
- the expiration time for this ticket's validity period,
or

null

if destroyed.

---

#### public final
Date
getRenewTill()

Returns the latest expiration time for this ticket, including all
renewals. This will return a null value for non-renewable tickets.

**Returns:**
- the latest expiration time for this ticket, or

null

if destroyed.

---

#### public final
InetAddress
[] getClientAddresses()

Returns a list of addresses from where the ticket can be used.

**Returns:**
- the list of addresses, or

null

if the field was not
provided or this ticket is destroyed.

---

#### public final byte[] getEncoded()

Returns an ASN.1 encoding of the entire ticket.

**Returns:**
- an ASN.1 encoding of the entire ticket. A new byte
array is returned each time this method is called.

**Throws:**
- IllegalStateException

- if this ticket is destroyed

---

#### public boolean isCurrent()

Determines if this ticket is still current.

**Specified by:**
- isCurrent

in interface

Refreshable

**Returns:**
- true if this ticket is still current, or false if not current
or destroyed.

---

#### public void refresh()
throws
RefreshFailedException

Extends the validity period of this ticket. The ticket will contain
a new session key if the refresh operation succeeds. The refresh
operation will fail if the ticket is not renewable or the latest
allowable renew time has passed. Any other error returned by the
KDC will also cause this method to fail.

Note: This method is not synchronized with the accessor
methods of this object. Hence callers need to be aware of multiple
threads that might access this and try to renew it at the same
time.

**Specified by:**
- refresh

in interface

Refreshable

**Throws:**
- IllegalStateException

- if this ticket is destroyed
- RefreshFailedException

- if the ticket is not renewable, or
the latest allowable renew time has passed, or the KDC returns some
error.

**See Also:**
- isRenewable()

,

getRenewTill()

---

#### public void destroy()
throws
DestroyFailedException

Destroys the ticket and destroys any sensitive information stored in
it.

**Specified by:**
- destroy

in interface

Destroyable

**Throws:**
- DestroyFailedException

- if the destroy operation fails.

---

#### public boolean isDestroyed()

Determines if this ticket has been destroyed.

**Specified by:**
- isDestroyed

in interface

Destroyable

**Returns:**
- true if this

Object

has been destroyed,
false otherwise.

---

#### public
String
toString()

Returns an informative textual representation of this

KerberosTicket

.

**Overrides:**
- toString

in class

Object

**Returns:**
- an informative textual representation of this

KerberosTicket

.

---

#### public int hashCode()

Returns a hash code for this

KerberosTicket

.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code for this

KerberosTicket

.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

**Since:**
- 1.6

---

#### public boolean equals​(
Object
other)

Compares the specified object with this

KerberosTicket

for equality.
Returns true if the given object is also a

KerberosTicket

and the two

KerberosTicket

instances are equivalent.
A destroyed

KerberosTicket

object is only equal to itself.

**Overrides:**
- equals

in class

Object

**Parameters:**
- other

- the object to compare to

**Returns:**
- true if the specified object is equal to this

KerberosTicket

,
false otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

**Since:**
- 1.6

---

### Additional Sections

#### Class KerberosTicket

java.lang.Object

- javax.security.auth.kerberos.KerberosTicket

javax.security.auth.kerberos.KerberosTicket

**All Implemented Interfaces:** Serializable

,

Destroyable

,

Refreshable

```java
public class
KerberosTicket

extends
Object

implements
Destroyable
,
Refreshable
,
Serializable
```

This class encapsulates a Kerberos ticket and associated
information as viewed from the client's point of view. It captures all
information that the Key Distribution Center (KDC) sends to the client
in the reply message KDC-REP defined in the Kerberos Protocol
Specification (

RFC 4120

).

All Kerberos JAAS login modules that authenticate a user to a KDC should
use this class. Where available, the login module might even read this
information from a ticket cache in the operating system instead of
directly communicating with the KDC. During the commit phase of the JAAS
authentication process, the JAAS login module should instantiate this
class and store the instance in the private credential set of a

Subject

.

It might be necessary for the application to be granted a

PrivateCredentialPermission

if it needs to access a

KerberosTicket

instance from a

Subject

. This permission is not needed when the
application depends on the default JGSS Kerberos mechanism to access the

KerberosTicket

. In that case, however, the application will need an
appropriate

ServicePermission

.

Note that this class is applicable to both ticket granting tickets and
other regular service tickets. A ticket granting ticket is just a
special case of a more generalized service ticket.

**Implementation Note:** The JAAS login module in the JDK reference implementation destroys
all tickets after logout.
**Since:** 1.4
**See Also:** Subject

,

PrivateCredentialPermission

,

LoginContext

,

GSSCredential

,

GSSManager

,

Serialized Form

public class

KerberosTicket

extends

Object

implements

Destroyable

,

Refreshable

,

Serializable

This class encapsulates a Kerberos ticket and associated
information as viewed from the client's point of view. It captures all
information that the Key Distribution Center (KDC) sends to the client
in the reply message KDC-REP defined in the Kerberos Protocol
Specification (

RFC 4120

).

All Kerberos JAAS login modules that authenticate a user to a KDC should
use this class. Where available, the login module might even read this
information from a ticket cache in the operating system instead of
directly communicating with the KDC. During the commit phase of the JAAS
authentication process, the JAAS login module should instantiate this
class and store the instance in the private credential set of a

Subject

.

It might be necessary for the application to be granted a

PrivateCredentialPermission

if it needs to access a

KerberosTicket

instance from a

Subject

. This permission is not needed when the
application depends on the default JGSS Kerberos mechanism to access the

KerberosTicket

. In that case, however, the application will need an
appropriate

ServicePermission

.

Note that this class is applicable to both ticket granting tickets and
other regular service tickets. A ticket granting ticket is just a
special case of a more generalized service ticket.

All Kerberos JAAS login modules that authenticate a user to a KDC should
use this class. Where available, the login module might even read this
information from a ticket cache in the operating system instead of
directly communicating with the KDC. During the commit phase of the JAAS
authentication process, the JAAS login module should instantiate this
class and store the instance in the private credential set of a

Subject

.

It might be necessary for the application to be granted a

PrivateCredentialPermission

if it needs to access a

KerberosTicket

instance from a

Subject

. This permission is not needed when the
application depends on the default JGSS Kerberos mechanism to access the

KerberosTicket

. In that case, however, the application will need an
appropriate

ServicePermission

.

Note that this class is applicable to both ticket granting tickets and
other regular service tickets. A ticket granting ticket is just a
special case of a more generalized service ticket.

It might be necessary for the application to be granted a

PrivateCredentialPermission

if it needs to access a

KerberosTicket

instance from a

Subject

. This permission is not needed when the
application depends on the default JGSS Kerberos mechanism to access the

KerberosTicket

. In that case, however, the application will need an
appropriate

ServicePermission

.

Note that this class is applicable to both ticket granting tickets and
other regular service tickets. A ticket granting ticket is just a
special case of a more generalized service ticket.

Note that this class is applicable to both ticket granting tickets and
other regular service tickets. A ticket granting ticket is just a
special case of a more generalized service ticket.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

KerberosTicket

​(byte[] asn1Encoding,

KerberosPrincipal

client,

KerberosPrincipal

server,
byte[] sessionKey,
int keyType,
boolean[] flags,

Date

authTime,

Date

startTime,

Date

endTime,

Date

renewTill,

InetAddress

[] clientAddresses)

Constructs a

KerberosTicket

using credentials information that a
client either receives from a KDC or reads from a cache.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

destroy

()

Destroys the ticket and destroys any sensitive information stored in
it.

boolean

equals

​(

Object

other)

Compares the specified object with this

KerberosTicket

for equality.

Date

getAuthTime

()

Returns the time that the client was authenticated.

KerberosPrincipal

getClient

()

Returns the client principal associated with this ticket.

InetAddress

[]

getClientAddresses

()

Returns a list of addresses from where the ticket can be used.

byte[]

getEncoded

()

Returns an ASN.1 encoding of the entire ticket.

Date

getEndTime

()

Returns the expiration time for this ticket's validity period.

boolean[]

getFlags

()

Returns the flags associated with this ticket.

Date

getRenewTill

()

Returns the latest expiration time for this ticket, including all
renewals.

KerberosPrincipal

getServer

()

Returns the service principal associated with this ticket.

SecretKey

getSessionKey

()

Returns the session key associated with this ticket.

int

getSessionKeyType

()

Returns the key type of the session key associated with this
ticket as defined by the Kerberos Protocol Specification.

Date

getStartTime

()

Returns the start time for this ticket's validity period.

int

hashCode

()

Returns a hash code for this

KerberosTicket

.

boolean

isCurrent

()

Determines if this ticket is still current.

boolean

isDestroyed

()

Determines if this ticket has been destroyed.

boolean

isForwardable

()

Determines if this ticket is forwardable.

boolean

isForwarded

()

Determines if this ticket had been forwarded or was issued based on
authentication involving a forwarded ticket-granting ticket.

boolean

isInitial

()

Determines if this ticket was issued using the Kerberos AS-Exchange
protocol, and not issued based on some ticket-granting ticket.

boolean

isPostdated

()

Determines is this ticket is post-dated.

boolean

isProxiable

()

Determines if this ticket is proxiable.

boolean

isProxy

()

Determines is this ticket is a proxy-ticket.

boolean

isRenewable

()

Determines is this ticket is renewable.

void

refresh

()

Extends the validity period of this ticket.

String

toString

()

Returns an informative textual representation of this

KerberosTicket

.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Constructor Summary

Constructors

Constructor

Description

KerberosTicket

​(byte[] asn1Encoding,

KerberosPrincipal

client,

KerberosPrincipal

server,
byte[] sessionKey,
int keyType,
boolean[] flags,

Date

authTime,

Date

startTime,

Date

endTime,

Date

renewTill,

InetAddress

[] clientAddresses)

Constructs a

KerberosTicket

using credentials information that a
client either receives from a KDC or reads from a cache.

---

#### Constructor Summary

Constructs a

KerberosTicket

using credentials information that a
client either receives from a KDC or reads from a cache.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

destroy

()

Destroys the ticket and destroys any sensitive information stored in
it.

boolean

equals

​(

Object

other)

Compares the specified object with this

KerberosTicket

for equality.

Date

getAuthTime

()

Returns the time that the client was authenticated.

KerberosPrincipal

getClient

()

Returns the client principal associated with this ticket.

InetAddress

[]

getClientAddresses

()

Returns a list of addresses from where the ticket can be used.

byte[]

getEncoded

()

Returns an ASN.1 encoding of the entire ticket.

Date

getEndTime

()

Returns the expiration time for this ticket's validity period.

boolean[]

getFlags

()

Returns the flags associated with this ticket.

Date

getRenewTill

()

Returns the latest expiration time for this ticket, including all
renewals.

KerberosPrincipal

getServer

()

Returns the service principal associated with this ticket.

SecretKey

getSessionKey

()

Returns the session key associated with this ticket.

int

getSessionKeyType

()

Returns the key type of the session key associated with this
ticket as defined by the Kerberos Protocol Specification.

Date

getStartTime

()

Returns the start time for this ticket's validity period.

int

hashCode

()

Returns a hash code for this

KerberosTicket

.

boolean

isCurrent

()

Determines if this ticket is still current.

boolean

isDestroyed

()

Determines if this ticket has been destroyed.

boolean

isForwardable

()

Determines if this ticket is forwardable.

boolean

isForwarded

()

Determines if this ticket had been forwarded or was issued based on
authentication involving a forwarded ticket-granting ticket.

boolean

isInitial

()

Determines if this ticket was issued using the Kerberos AS-Exchange
protocol, and not issued based on some ticket-granting ticket.

boolean

isPostdated

()

Determines is this ticket is post-dated.

boolean

isProxiable

()

Determines if this ticket is proxiable.

boolean

isProxy

()

Determines is this ticket is a proxy-ticket.

boolean

isRenewable

()

Determines is this ticket is renewable.

void

refresh

()

Extends the validity period of this ticket.

String

toString

()

Returns an informative textual representation of this

KerberosTicket

.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Destroys the ticket and destroys any sensitive information stored in
it.

Compares the specified object with this

KerberosTicket

for equality.

Returns the time that the client was authenticated.

Returns the client principal associated with this ticket.

Returns a list of addresses from where the ticket can be used.

Returns an ASN.1 encoding of the entire ticket.

Returns the expiration time for this ticket's validity period.

Returns the flags associated with this ticket.

Returns the latest expiration time for this ticket, including all
renewals.

Returns the service principal associated with this ticket.

Returns the session key associated with this ticket.

Returns the key type of the session key associated with this
ticket as defined by the Kerberos Protocol Specification.

Returns the start time for this ticket's validity period.

Returns a hash code for this

KerberosTicket

.

Determines if this ticket is still current.

Determines if this ticket has been destroyed.

Determines if this ticket is forwardable.

Determines if this ticket had been forwarded or was issued based on
authentication involving a forwarded ticket-granting ticket.

Determines if this ticket was issued using the Kerberos AS-Exchange
protocol, and not issued based on some ticket-granting ticket.

Determines is this ticket is post-dated.

Determines if this ticket is proxiable.

Determines is this ticket is a proxy-ticket.

Determines is this ticket is renewable.

Extends the validity period of this ticket.

Returns an informative textual representation of this

KerberosTicket

.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- KerberosTicket

```java
public KerberosTicket​(byte[] asn1Encoding,

KerberosPrincipal
client,

KerberosPrincipal
server,
byte[] sessionKey,
int keyType,
boolean[] flags,

Date
authTime,

Date
startTime,

Date
endTime,

Date
renewTill,

InetAddress
[] clientAddresses)
```

Constructs a

KerberosTicket

using credentials information that a
client either receives from a KDC or reads from a cache.

**Parameters:** asn1Encoding

- the ASN.1 encoding of the ticket as defined by
the Kerberos protocol specification.
**Parameters:** client

- the client that owns this service
ticket
**Parameters:** server

- the service that this ticket is for
**Parameters:** sessionKey

- the raw bytes for the session key that must be
used to encrypt the authenticator that will be sent to the server
**Parameters:** keyType

- the key type for the session key as defined by the
Kerberos protocol specification.
**Parameters:** flags

- the ticket flags. Each element in this array indicates
the value for the corresponding bit in the ASN.1 BitString that
represents the ticket flags. If the number of elements in this array
is less than the number of flags used by the Kerberos protocol,
then the missing flags will be filled in with false.
**Parameters:** authTime

- the time of initial authentication for the client
**Parameters:** startTime

- the time after which the ticket will be valid. This
may be null in which case the value of authTime is treated as the
startTime.
**Parameters:** endTime

- the time after which the ticket will no longer be
valid
**Parameters:** renewTill

- an absolute expiration time for the ticket,
including all renewal that might be possible. This field may be null
for tickets that are not renewable.
**Parameters:** clientAddresses

- the addresses from where the ticket may be
used by the client. This field may be null when the ticket is usable
from any address.

============ METHOD DETAIL ==========

- Method Detail

- getClient

```java
public final
KerberosPrincipal
getClient()
```

Returns the client principal associated with this ticket.

**Returns:** the client principal, or

null

if destroyed.

- getServer

```java
public final
KerberosPrincipal
getServer()
```

Returns the service principal associated with this ticket.

**Returns:** the service principal, or

null

if destroyed.

- getSessionKey

```java
public final
SecretKey
getSessionKey()
```

Returns the session key associated with this ticket. The return value
is always a

EncryptionKey

object.

**Returns:** the session key.
**Throws:** IllegalStateException

- if this ticket is destroyed

- getSessionKeyType

```java
public final int getSessionKeyType()
```

Returns the key type of the session key associated with this
ticket as defined by the Kerberos Protocol Specification.

**Returns:** the key type of the session key associated with this
ticket.
**Throws:** IllegalStateException

- if this ticket is destroyed
**See Also:** getSessionKey()

- isForwardable

```java
public final boolean isForwardable()
```

Determines if this ticket is forwardable.

**Returns:** true if this ticket is forwardable, or false if not forwardable
or destroyed.

- isForwarded

```java
public final boolean isForwarded()
```

Determines if this ticket had been forwarded or was issued based on
authentication involving a forwarded ticket-granting ticket.

**Returns:** true if this ticket had been forwarded or was issued based on
authentication involving a forwarded ticket-granting ticket,
or false otherwise or destroyed.

- isProxiable

```java
public final boolean isProxiable()
```

Determines if this ticket is proxiable.

**Returns:** true if this ticket is proxiable, or false if not proxiable
or destroyed.

- isProxy

```java
public final boolean isProxy()
```

Determines is this ticket is a proxy-ticket.

**Returns:** true if this ticket is a proxy-ticket, or false if not
a proxy-ticket or destroyed.

- isPostdated

```java
public final boolean isPostdated()
```

Determines is this ticket is post-dated.

**Returns:** true if this ticket is post-dated, or false if not post-dated
or destroyed.

- isRenewable

```java
public final boolean isRenewable()
```

Determines is this ticket is renewable. If so, the

refresh

method can be called, assuming the validity period for
renewing is not already over.

**Returns:** true if this ticket is renewable, or false if not renewable
or destroyed.

- isInitial

```java
public final boolean isInitial()
```

Determines if this ticket was issued using the Kerberos AS-Exchange
protocol, and not issued based on some ticket-granting ticket.

**Returns:** true if this ticket was issued using the Kerberos AS-Exchange
protocol, or false if not issued this way or destroyed.

- getFlags

```java
public final boolean[] getFlags()
```

Returns the flags associated with this ticket. Each element in the
returned array indicates the value for the corresponding bit in the
ASN.1 BitString that represents the ticket flags.

**Returns:** the flags associated with this ticket, or

null

if destroyed.

- getAuthTime

```java
public final
Date
getAuthTime()
```

Returns the time that the client was authenticated.

**Returns:** the time that the client was authenticated
or

null

if the field is not set or
this ticket is destroyed.

- getStartTime

```java
public final
Date
getStartTime()
```

Returns the start time for this ticket's validity period.

**Returns:** the start time for this ticket's validity period
or

null

if the field is not set or
this ticket is destroyed.

- getEndTime

```java
public final
Date
getEndTime()
```

Returns the expiration time for this ticket's validity period.

**Returns:** the expiration time for this ticket's validity period,
or

null

if destroyed.

- getRenewTill

```java
public final
Date
getRenewTill()
```

Returns the latest expiration time for this ticket, including all
renewals. This will return a null value for non-renewable tickets.

**Returns:** the latest expiration time for this ticket, or

null

if destroyed.

- getClientAddresses

```java
public final
InetAddress
[] getClientAddresses()
```

Returns a list of addresses from where the ticket can be used.

**Returns:** the list of addresses, or

null

if the field was not
provided or this ticket is destroyed.

- getEncoded

```java
public final byte[] getEncoded()
```

Returns an ASN.1 encoding of the entire ticket.

**Returns:** an ASN.1 encoding of the entire ticket. A new byte
array is returned each time this method is called.
**Throws:** IllegalStateException

- if this ticket is destroyed

- isCurrent

```java
public boolean isCurrent()
```

Determines if this ticket is still current.

**Specified by:** isCurrent

in interface

Refreshable
**Returns:** true if this ticket is still current, or false if not current
or destroyed.

- refresh

```java
public void refresh()
throws
RefreshFailedException
```

Extends the validity period of this ticket. The ticket will contain
a new session key if the refresh operation succeeds. The refresh
operation will fail if the ticket is not renewable or the latest
allowable renew time has passed. Any other error returned by the
KDC will also cause this method to fail.

Note: This method is not synchronized with the accessor
methods of this object. Hence callers need to be aware of multiple
threads that might access this and try to renew it at the same
time.

**Specified by:** refresh

in interface

Refreshable
**Throws:** IllegalStateException

- if this ticket is destroyed
**Throws:** RefreshFailedException

- if the ticket is not renewable, or
the latest allowable renew time has passed, or the KDC returns some
error.
**See Also:** isRenewable()

,

getRenewTill()

- destroy

```java
public void destroy()
throws
DestroyFailedException
```

Destroys the ticket and destroys any sensitive information stored in
it.

**Specified by:** destroy

in interface

Destroyable
**Throws:** DestroyFailedException

- if the destroy operation fails.

- isDestroyed

```java
public boolean isDestroyed()
```

Determines if this ticket has been destroyed.

**Specified by:** isDestroyed

in interface

Destroyable
**Returns:** true if this

Object

has been destroyed,
false otherwise.

- toString

```java
public
String
toString()
```

Returns an informative textual representation of this

KerberosTicket

.

**Overrides:** toString

in class

Object
**Returns:** an informative textual representation of this

KerberosTicket

.

- hashCode

```java
public int hashCode()
```

Returns a hash code for this

KerberosTicket

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

KerberosTicket

.
**Since:** 1.6
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
other)
```

Compares the specified object with this

KerberosTicket

for equality.
Returns true if the given object is also a

KerberosTicket

and the two

KerberosTicket

instances are equivalent.
A destroyed

KerberosTicket

object is only equal to itself.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to compare to
**Returns:** true if the specified object is equal to this

KerberosTicket

,
false otherwise.
**Since:** 1.6
**See Also:** Object.hashCode()

,

HashMap

Constructor Detail

- KerberosTicket

```java
public KerberosTicket​(byte[] asn1Encoding,

KerberosPrincipal
client,

KerberosPrincipal
server,
byte[] sessionKey,
int keyType,
boolean[] flags,

Date
authTime,

Date
startTime,

Date
endTime,

Date
renewTill,

InetAddress
[] clientAddresses)
```

Constructs a

KerberosTicket

using credentials information that a
client either receives from a KDC or reads from a cache.

**Parameters:** asn1Encoding

- the ASN.1 encoding of the ticket as defined by
the Kerberos protocol specification.
**Parameters:** client

- the client that owns this service
ticket
**Parameters:** server

- the service that this ticket is for
**Parameters:** sessionKey

- the raw bytes for the session key that must be
used to encrypt the authenticator that will be sent to the server
**Parameters:** keyType

- the key type for the session key as defined by the
Kerberos protocol specification.
**Parameters:** flags

- the ticket flags. Each element in this array indicates
the value for the corresponding bit in the ASN.1 BitString that
represents the ticket flags. If the number of elements in this array
is less than the number of flags used by the Kerberos protocol,
then the missing flags will be filled in with false.
**Parameters:** authTime

- the time of initial authentication for the client
**Parameters:** startTime

- the time after which the ticket will be valid. This
may be null in which case the value of authTime is treated as the
startTime.
**Parameters:** endTime

- the time after which the ticket will no longer be
valid
**Parameters:** renewTill

- an absolute expiration time for the ticket,
including all renewal that might be possible. This field may be null
for tickets that are not renewable.
**Parameters:** clientAddresses

- the addresses from where the ticket may be
used by the client. This field may be null when the ticket is usable
from any address.

---

#### Constructor Detail

KerberosTicket

```java
public KerberosTicket​(byte[] asn1Encoding,

KerberosPrincipal
client,

KerberosPrincipal
server,
byte[] sessionKey,
int keyType,
boolean[] flags,

Date
authTime,

Date
startTime,

Date
endTime,

Date
renewTill,

InetAddress
[] clientAddresses)
```

Constructs a

KerberosTicket

using credentials information that a
client either receives from a KDC or reads from a cache.

**Parameters:** asn1Encoding

- the ASN.1 encoding of the ticket as defined by
the Kerberos protocol specification.
**Parameters:** client

- the client that owns this service
ticket
**Parameters:** server

- the service that this ticket is for
**Parameters:** sessionKey

- the raw bytes for the session key that must be
used to encrypt the authenticator that will be sent to the server
**Parameters:** keyType

- the key type for the session key as defined by the
Kerberos protocol specification.
**Parameters:** flags

- the ticket flags. Each element in this array indicates
the value for the corresponding bit in the ASN.1 BitString that
represents the ticket flags. If the number of elements in this array
is less than the number of flags used by the Kerberos protocol,
then the missing flags will be filled in with false.
**Parameters:** authTime

- the time of initial authentication for the client
**Parameters:** startTime

- the time after which the ticket will be valid. This
may be null in which case the value of authTime is treated as the
startTime.
**Parameters:** endTime

- the time after which the ticket will no longer be
valid
**Parameters:** renewTill

- an absolute expiration time for the ticket,
including all renewal that might be possible. This field may be null
for tickets that are not renewable.
**Parameters:** clientAddresses

- the addresses from where the ticket may be
used by the client. This field may be null when the ticket is usable
from any address.

---

#### KerberosTicket

public KerberosTicket​(byte[] asn1Encoding,

KerberosPrincipal

client,

KerberosPrincipal

server,
byte[] sessionKey,
int keyType,
boolean[] flags,

Date

authTime,

Date

startTime,

Date

endTime,

Date

renewTill,

InetAddress

[] clientAddresses)

Constructs a

KerberosTicket

using credentials information that a
client either receives from a KDC or reads from a cache.

Method Detail

- getClient

```java
public final
KerberosPrincipal
getClient()
```

Returns the client principal associated with this ticket.

**Returns:** the client principal, or

null

if destroyed.

- getServer

```java
public final
KerberosPrincipal
getServer()
```

Returns the service principal associated with this ticket.

**Returns:** the service principal, or

null

if destroyed.

- getSessionKey

```java
public final
SecretKey
getSessionKey()
```

Returns the session key associated with this ticket. The return value
is always a

EncryptionKey

object.

**Returns:** the session key.
**Throws:** IllegalStateException

- if this ticket is destroyed

- getSessionKeyType

```java
public final int getSessionKeyType()
```

Returns the key type of the session key associated with this
ticket as defined by the Kerberos Protocol Specification.

**Returns:** the key type of the session key associated with this
ticket.
**Throws:** IllegalStateException

- if this ticket is destroyed
**See Also:** getSessionKey()

- isForwardable

```java
public final boolean isForwardable()
```

Determines if this ticket is forwardable.

**Returns:** true if this ticket is forwardable, or false if not forwardable
or destroyed.

- isForwarded

```java
public final boolean isForwarded()
```

Determines if this ticket had been forwarded or was issued based on
authentication involving a forwarded ticket-granting ticket.

**Returns:** true if this ticket had been forwarded or was issued based on
authentication involving a forwarded ticket-granting ticket,
or false otherwise or destroyed.

- isProxiable

```java
public final boolean isProxiable()
```

Determines if this ticket is proxiable.

**Returns:** true if this ticket is proxiable, or false if not proxiable
or destroyed.

- isProxy

```java
public final boolean isProxy()
```

Determines is this ticket is a proxy-ticket.

**Returns:** true if this ticket is a proxy-ticket, or false if not
a proxy-ticket or destroyed.

- isPostdated

```java
public final boolean isPostdated()
```

Determines is this ticket is post-dated.

**Returns:** true if this ticket is post-dated, or false if not post-dated
or destroyed.

- isRenewable

```java
public final boolean isRenewable()
```

Determines is this ticket is renewable. If so, the

refresh

method can be called, assuming the validity period for
renewing is not already over.

**Returns:** true if this ticket is renewable, or false if not renewable
or destroyed.

- isInitial

```java
public final boolean isInitial()
```

Determines if this ticket was issued using the Kerberos AS-Exchange
protocol, and not issued based on some ticket-granting ticket.

**Returns:** true if this ticket was issued using the Kerberos AS-Exchange
protocol, or false if not issued this way or destroyed.

- getFlags

```java
public final boolean[] getFlags()
```

Returns the flags associated with this ticket. Each element in the
returned array indicates the value for the corresponding bit in the
ASN.1 BitString that represents the ticket flags.

**Returns:** the flags associated with this ticket, or

null

if destroyed.

- getAuthTime

```java
public final
Date
getAuthTime()
```

Returns the time that the client was authenticated.

**Returns:** the time that the client was authenticated
or

null

if the field is not set or
this ticket is destroyed.

- getStartTime

```java
public final
Date
getStartTime()
```

Returns the start time for this ticket's validity period.

**Returns:** the start time for this ticket's validity period
or

null

if the field is not set or
this ticket is destroyed.

- getEndTime

```java
public final
Date
getEndTime()
```

Returns the expiration time for this ticket's validity period.

**Returns:** the expiration time for this ticket's validity period,
or

null

if destroyed.

- getRenewTill

```java
public final
Date
getRenewTill()
```

Returns the latest expiration time for this ticket, including all
renewals. This will return a null value for non-renewable tickets.

**Returns:** the latest expiration time for this ticket, or

null

if destroyed.

- getClientAddresses

```java
public final
InetAddress
[] getClientAddresses()
```

Returns a list of addresses from where the ticket can be used.

**Returns:** the list of addresses, or

null

if the field was not
provided or this ticket is destroyed.

- getEncoded

```java
public final byte[] getEncoded()
```

Returns an ASN.1 encoding of the entire ticket.

**Returns:** an ASN.1 encoding of the entire ticket. A new byte
array is returned each time this method is called.
**Throws:** IllegalStateException

- if this ticket is destroyed

- isCurrent

```java
public boolean isCurrent()
```

Determines if this ticket is still current.

**Specified by:** isCurrent

in interface

Refreshable
**Returns:** true if this ticket is still current, or false if not current
or destroyed.

- refresh

```java
public void refresh()
throws
RefreshFailedException
```

Extends the validity period of this ticket. The ticket will contain
a new session key if the refresh operation succeeds. The refresh
operation will fail if the ticket is not renewable or the latest
allowable renew time has passed. Any other error returned by the
KDC will also cause this method to fail.

Note: This method is not synchronized with the accessor
methods of this object. Hence callers need to be aware of multiple
threads that might access this and try to renew it at the same
time.

**Specified by:** refresh

in interface

Refreshable
**Throws:** IllegalStateException

- if this ticket is destroyed
**Throws:** RefreshFailedException

- if the ticket is not renewable, or
the latest allowable renew time has passed, or the KDC returns some
error.
**See Also:** isRenewable()

,

getRenewTill()

- destroy

```java
public void destroy()
throws
DestroyFailedException
```

Destroys the ticket and destroys any sensitive information stored in
it.

**Specified by:** destroy

in interface

Destroyable
**Throws:** DestroyFailedException

- if the destroy operation fails.

- isDestroyed

```java
public boolean isDestroyed()
```

Determines if this ticket has been destroyed.

**Specified by:** isDestroyed

in interface

Destroyable
**Returns:** true if this

Object

has been destroyed,
false otherwise.

- toString

```java
public
String
toString()
```

Returns an informative textual representation of this

KerberosTicket

.

**Overrides:** toString

in class

Object
**Returns:** an informative textual representation of this

KerberosTicket

.

- hashCode

```java
public int hashCode()
```

Returns a hash code for this

KerberosTicket

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

KerberosTicket

.
**Since:** 1.6
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- equals

```java
public boolean equals​(
Object
other)
```

Compares the specified object with this

KerberosTicket

for equality.
Returns true if the given object is also a

KerberosTicket

and the two

KerberosTicket

instances are equivalent.
A destroyed

KerberosTicket

object is only equal to itself.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to compare to
**Returns:** true if the specified object is equal to this

KerberosTicket

,
false otherwise.
**Since:** 1.6
**See Also:** Object.hashCode()

,

HashMap

---

#### Method Detail

getClient

```java
public final
KerberosPrincipal
getClient()
```

Returns the client principal associated with this ticket.

**Returns:** the client principal, or

null

if destroyed.

---

#### getClient

public final

KerberosPrincipal

getClient()

Returns the client principal associated with this ticket.

getServer

```java
public final
KerberosPrincipal
getServer()
```

Returns the service principal associated with this ticket.

**Returns:** the service principal, or

null

if destroyed.

---

#### getServer

public final

KerberosPrincipal

getServer()

Returns the service principal associated with this ticket.

getSessionKey

```java
public final
SecretKey
getSessionKey()
```

Returns the session key associated with this ticket. The return value
is always a

EncryptionKey

object.

**Returns:** the session key.
**Throws:** IllegalStateException

- if this ticket is destroyed

---

#### getSessionKey

public final

SecretKey

getSessionKey()

Returns the session key associated with this ticket. The return value
is always a

EncryptionKey

object.

getSessionKeyType

```java
public final int getSessionKeyType()
```

Returns the key type of the session key associated with this
ticket as defined by the Kerberos Protocol Specification.

**Returns:** the key type of the session key associated with this
ticket.
**Throws:** IllegalStateException

- if this ticket is destroyed
**See Also:** getSessionKey()

---

#### getSessionKeyType

public final int getSessionKeyType()

Returns the key type of the session key associated with this
ticket as defined by the Kerberos Protocol Specification.

isForwardable

```java
public final boolean isForwardable()
```

Determines if this ticket is forwardable.

**Returns:** true if this ticket is forwardable, or false if not forwardable
or destroyed.

---

#### isForwardable

public final boolean isForwardable()

Determines if this ticket is forwardable.

isForwarded

```java
public final boolean isForwarded()
```

Determines if this ticket had been forwarded or was issued based on
authentication involving a forwarded ticket-granting ticket.

**Returns:** true if this ticket had been forwarded or was issued based on
authentication involving a forwarded ticket-granting ticket,
or false otherwise or destroyed.

---

#### isForwarded

public final boolean isForwarded()

Determines if this ticket had been forwarded or was issued based on
authentication involving a forwarded ticket-granting ticket.

isProxiable

```java
public final boolean isProxiable()
```

Determines if this ticket is proxiable.

**Returns:** true if this ticket is proxiable, or false if not proxiable
or destroyed.

---

#### isProxiable

public final boolean isProxiable()

Determines if this ticket is proxiable.

isProxy

```java
public final boolean isProxy()
```

Determines is this ticket is a proxy-ticket.

**Returns:** true if this ticket is a proxy-ticket, or false if not
a proxy-ticket or destroyed.

---

#### isProxy

public final boolean isProxy()

Determines is this ticket is a proxy-ticket.

isPostdated

```java
public final boolean isPostdated()
```

Determines is this ticket is post-dated.

**Returns:** true if this ticket is post-dated, or false if not post-dated
or destroyed.

---

#### isPostdated

public final boolean isPostdated()

Determines is this ticket is post-dated.

isRenewable

```java
public final boolean isRenewable()
```

Determines is this ticket is renewable. If so, the

refresh

method can be called, assuming the validity period for
renewing is not already over.

**Returns:** true if this ticket is renewable, or false if not renewable
or destroyed.

---

#### isRenewable

public final boolean isRenewable()

Determines is this ticket is renewable. If so, the

refresh

method can be called, assuming the validity period for
renewing is not already over.

isInitial

```java
public final boolean isInitial()
```

Determines if this ticket was issued using the Kerberos AS-Exchange
protocol, and not issued based on some ticket-granting ticket.

**Returns:** true if this ticket was issued using the Kerberos AS-Exchange
protocol, or false if not issued this way or destroyed.

---

#### isInitial

public final boolean isInitial()

Determines if this ticket was issued using the Kerberos AS-Exchange
protocol, and not issued based on some ticket-granting ticket.

getFlags

```java
public final boolean[] getFlags()
```

Returns the flags associated with this ticket. Each element in the
returned array indicates the value for the corresponding bit in the
ASN.1 BitString that represents the ticket flags.

**Returns:** the flags associated with this ticket, or

null

if destroyed.

---

#### getFlags

public final boolean[] getFlags()

Returns the flags associated with this ticket. Each element in the
returned array indicates the value for the corresponding bit in the
ASN.1 BitString that represents the ticket flags.

getAuthTime

```java
public final
Date
getAuthTime()
```

Returns the time that the client was authenticated.

**Returns:** the time that the client was authenticated
or

null

if the field is not set or
this ticket is destroyed.

---

#### getAuthTime

public final

Date

getAuthTime()

Returns the time that the client was authenticated.

getStartTime

```java
public final
Date
getStartTime()
```

Returns the start time for this ticket's validity period.

**Returns:** the start time for this ticket's validity period
or

null

if the field is not set or
this ticket is destroyed.

---

#### getStartTime

public final

Date

getStartTime()

Returns the start time for this ticket's validity period.

getEndTime

```java
public final
Date
getEndTime()
```

Returns the expiration time for this ticket's validity period.

**Returns:** the expiration time for this ticket's validity period,
or

null

if destroyed.

---

#### getEndTime

public final

Date

getEndTime()

Returns the expiration time for this ticket's validity period.

getRenewTill

```java
public final
Date
getRenewTill()
```

Returns the latest expiration time for this ticket, including all
renewals. This will return a null value for non-renewable tickets.

**Returns:** the latest expiration time for this ticket, or

null

if destroyed.

---

#### getRenewTill

public final

Date

getRenewTill()

Returns the latest expiration time for this ticket, including all
renewals. This will return a null value for non-renewable tickets.

getClientAddresses

```java
public final
InetAddress
[] getClientAddresses()
```

Returns a list of addresses from where the ticket can be used.

**Returns:** the list of addresses, or

null

if the field was not
provided or this ticket is destroyed.

---

#### getClientAddresses

public final

InetAddress

[] getClientAddresses()

Returns a list of addresses from where the ticket can be used.

getEncoded

```java
public final byte[] getEncoded()
```

Returns an ASN.1 encoding of the entire ticket.

**Returns:** an ASN.1 encoding of the entire ticket. A new byte
array is returned each time this method is called.
**Throws:** IllegalStateException

- if this ticket is destroyed

---

#### getEncoded

public final byte[] getEncoded()

Returns an ASN.1 encoding of the entire ticket.

isCurrent

```java
public boolean isCurrent()
```

Determines if this ticket is still current.

**Specified by:** isCurrent

in interface

Refreshable
**Returns:** true if this ticket is still current, or false if not current
or destroyed.

---

#### isCurrent

public boolean isCurrent()

Determines if this ticket is still current.

refresh

```java
public void refresh()
throws
RefreshFailedException
```

Extends the validity period of this ticket. The ticket will contain
a new session key if the refresh operation succeeds. The refresh
operation will fail if the ticket is not renewable or the latest
allowable renew time has passed. Any other error returned by the
KDC will also cause this method to fail.

Note: This method is not synchronized with the accessor
methods of this object. Hence callers need to be aware of multiple
threads that might access this and try to renew it at the same
time.

**Specified by:** refresh

in interface

Refreshable
**Throws:** IllegalStateException

- if this ticket is destroyed
**Throws:** RefreshFailedException

- if the ticket is not renewable, or
the latest allowable renew time has passed, or the KDC returns some
error.
**See Also:** isRenewable()

,

getRenewTill()

---

#### refresh

public void refresh()
throws

RefreshFailedException

Extends the validity period of this ticket. The ticket will contain
a new session key if the refresh operation succeeds. The refresh
operation will fail if the ticket is not renewable or the latest
allowable renew time has passed. Any other error returned by the
KDC will also cause this method to fail.

Note: This method is not synchronized with the accessor
methods of this object. Hence callers need to be aware of multiple
threads that might access this and try to renew it at the same
time.

destroy

```java
public void destroy()
throws
DestroyFailedException
```

Destroys the ticket and destroys any sensitive information stored in
it.

**Specified by:** destroy

in interface

Destroyable
**Throws:** DestroyFailedException

- if the destroy operation fails.

---

#### destroy

public void destroy()
throws

DestroyFailedException

Destroys the ticket and destroys any sensitive information stored in
it.

isDestroyed

```java
public boolean isDestroyed()
```

Determines if this ticket has been destroyed.

**Specified by:** isDestroyed

in interface

Destroyable
**Returns:** true if this

Object

has been destroyed,
false otherwise.

---

#### isDestroyed

public boolean isDestroyed()

Determines if this ticket has been destroyed.

toString

```java
public
String
toString()
```

Returns an informative textual representation of this

KerberosTicket

.

**Overrides:** toString

in class

Object
**Returns:** an informative textual representation of this

KerberosTicket

.

---

#### toString

public

String

toString()

Returns an informative textual representation of this

KerberosTicket

.

hashCode

```java
public int hashCode()
```

Returns a hash code for this

KerberosTicket

.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

KerberosTicket

.
**Since:** 1.6
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Returns a hash code for this

KerberosTicket

.

equals

```java
public boolean equals​(
Object
other)
```

Compares the specified object with this

KerberosTicket

for equality.
Returns true if the given object is also a

KerberosTicket

and the two

KerberosTicket

instances are equivalent.
A destroyed

KerberosTicket

object is only equal to itself.

**Overrides:** equals

in class

Object
**Parameters:** other

- the object to compare to
**Returns:** true if the specified object is equal to this

KerberosTicket

,
false otherwise.
**Since:** 1.6
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

other)

Compares the specified object with this

KerberosTicket

for equality.
Returns true if the given object is also a

KerberosTicket

and the two

KerberosTicket

instances are equivalent.
A destroyed

KerberosTicket

object is only equal to itself.

---

