# Class Authenticator

**Source:** `java.base\java\net\Authenticator.html`

### Class Description

```java
public abstract class
Authenticator

extends
Object
```

The class Authenticator represents an object that knows how to obtain
authentication for a network connection. Usually, it will do this
by prompting the user for information.

Applications use this class by overriding

getPasswordAuthentication()

in a sub-class. This method will
typically use the various getXXX() accessor methods to get information
about the entity requesting authentication. It must then acquire a
username and password either by interacting with the user or through
some other non-interactive means. The credentials are then returned
as a

PasswordAuthentication

return value.

An instance of this concrete sub-class is then registered
with the system by calling

setDefault(Authenticator)

.
When authentication is required, the system will invoke one of the
requestPasswordAuthentication() methods which in turn will call the
getPasswordAuthentication() method of the registered object.

All methods that request authentication have a default implementation
that fails.

**Since:** 1.2
**See Also:** setDefault(java.net.Authenticator)

,

getPasswordAuthentication()

---

### Field Details

*No entries found.*

### Constructor Details

#### public Authenticator()

*No description found.*

---

### Method Details

#### public static void setDefault​(
Authenticator
a)

Sets the authenticator that will be used by the networking code
when a proxy or an HTTP server asks for authentication.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("setDefaultAuthenticator")

permission.
This may result in a java.lang.SecurityException.

**Parameters:**
- a

- The authenticator to be set. If a is

null

then
any previously set authenticator is removed.

**Throws:**
- SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
setting the default authenticator.

**See Also:**
- SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

---

#### public static
Authenticator
getDefault()

Gets the default authenticator.
First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.
Then the default authenticator, if set, is returned.
Otherwise,

null

is returned.

**Returns:**
- The default authenticator, if set,

null

otherwise.

**Throws:**
- SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
requesting password authentication.

**See Also:**
- SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

**Since:**
- 9

---

#### public static
PasswordAuthentication
requestPasswordAuthentication​(
InetAddress
addr,
int port,

String
protocol,

String
prompt,

String
scheme)

Ask the authenticator that has been registered with the system
for a password.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

**Parameters:**
- addr

- The InetAddress of the site requesting authorization,
or null if not known.
- port

- the port for the requested connection
- protocol

- The protocol that's requesting the connection
(

getRequestingProtocol()

)
- prompt

- A prompt string for the user
- scheme

- The authentication scheme

**Returns:**
- The username/password, or null if one can't be gotten.

**Throws:**
- SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
the password authentication request.

**See Also:**
- SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

---

#### public static
PasswordAuthentication
requestPasswordAuthentication​(
String
host,

InetAddress
addr,
int port,

String
protocol,

String
prompt,

String
scheme)

Ask the authenticator that has been registered with the system
for a password. This is the preferred method for requesting a password
because the hostname can be provided in cases where the InetAddress
is not available.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

**Parameters:**
- host

- The hostname of the site requesting authentication.
- addr

- The InetAddress of the site requesting authentication,
or null if not known.
- port

- the port for the requested connection.
- protocol

- The protocol that's requesting the connection
(

getRequestingProtocol()

)
- prompt

- A prompt string for the user which identifies the authentication realm.
- scheme

- The authentication scheme

**Returns:**
- The username/password, or null if one can't be gotten.

**Throws:**
- SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
the password authentication request.

**See Also:**
- SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

**Since:**
- 1.4

---

#### public static
PasswordAuthentication
requestPasswordAuthentication​(
String
host,

InetAddress
addr,
int port,

String
protocol,

String
prompt,

String
scheme,

URL
url,

Authenticator.RequestorType
reqType)

Ask the authenticator that has been registered with the system
for a password.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

**Parameters:**
- host

- The hostname of the site requesting authentication.
- addr

- The InetAddress of the site requesting authorization,
or null if not known.
- port

- the port for the requested connection
- protocol

- The protocol that's requesting the connection
(

getRequestingProtocol()

)
- prompt

- A prompt string for the user
- scheme

- The authentication scheme
- url

- The requesting URL that caused the authentication
- reqType

- The type (server or proxy) of the entity requesting
authentication.

**Returns:**
- The username/password, or null if one can't be gotten.

**Throws:**
- SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
the password authentication request.

**See Also:**
- SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

**Since:**
- 1.5

---

#### public static
PasswordAuthentication
requestPasswordAuthentication​(
Authenticator
authenticator,

String
host,

InetAddress
addr,
int port,

String
protocol,

String
prompt,

String
scheme,

URL
url,

Authenticator.RequestorType
reqType)

Ask the given

authenticator

for a password. If the given

authenticator

is null, the authenticator, if any, that has been
registered with the system using

setDefault

is used.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

**Parameters:**
- authenticator

- the authenticator, or

null

.
- host

- The hostname of the site requesting authentication.
- addr

- The InetAddress of the site requesting authorization,
or null if not known.
- port

- the port for the requested connection
- protocol

- The protocol that's requesting the connection
(

getRequestingProtocol()

)
- prompt

- A prompt string for the user
- scheme

- The authentication scheme
- url

- The requesting URL that caused the authentication
- reqType

- The type (server or proxy) of the entity requesting
authentication.

**Returns:**
- The username/password, or

null

if one can't be gotten.

**Throws:**
- SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
the password authentication request.

**See Also:**
- SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

**Since:**
- 9

---

#### public
PasswordAuthentication
requestPasswordAuthenticationInstance​(
String
host,

InetAddress
addr,
int port,

String
protocol,

String
prompt,

String
scheme,

URL
url,

Authenticator.RequestorType
reqType)

Ask this authenticator for a password.

**Parameters:**
- host

- The hostname of the site requesting authentication.
- addr

- The InetAddress of the site requesting authorization,
or null if not known.
- port

- the port for the requested connection
- protocol

- The protocol that's requesting the connection
(

getRequestingProtocol()

)
- prompt

- A prompt string for the user
- scheme

- The authentication scheme
- url

- The requesting URL that caused the authentication
- reqType

- The type (server or proxy) of the entity requesting
authentication.

**Returns:**
- The username/password, or null if one can't be gotten

**Since:**
- 9

---

#### protected final
String
getRequestingHost()

Gets the

hostname

of the
site or proxy requesting authentication, or

null

if not available.

**Returns:**
- the hostname of the connection requiring authentication, or null
if it's not available.

**Since:**
- 1.4

---

#### protected final
InetAddress
getRequestingSite()

Gets the

InetAddress

of the
site requesting authorization, or

null

if not available.

**Returns:**
- the InetAddress of the site requesting authorization, or null
if it's not available.

---

#### protected final int getRequestingPort()

Gets the port number for the requested connection.

**Returns:**
- an

int

indicating the
port for the requested connection.

---

#### protected final
String
getRequestingProtocol()

Give the protocol that's requesting the connection. Often this
will be based on a URL, but in a future JDK it could be, for
example, "SOCKS" for a password-protected SOCKS5 firewall.

**Returns:**
- the protocol, optionally followed by "/version", where
version is a version number.

**See Also:**
- URL.getProtocol()

---

#### protected final
String
getRequestingPrompt()

Gets the prompt string given by the requestor.

**Returns:**
- the prompt string given by the requestor (realm for
http requests)

---

#### protected final
String
getRequestingScheme()

Gets the scheme of the requestor (the HTTP scheme
for an HTTP firewall, for example).

**Returns:**
- the scheme of the requestor

---

#### protected
PasswordAuthentication
getPasswordAuthentication()

Called when password authorization is needed. Subclasses should
override the default implementation, which returns null.

**Returns:**
- The PasswordAuthentication collected from the
user, or null if none is provided.

---

#### protected
URL
getRequestingURL()

Returns the URL that resulted in this
request for authentication.

**Returns:**
- the requesting URL

**Since:**
- 1.5

---

#### protected
Authenticator.RequestorType
getRequestorType()

Returns whether the requestor is a Proxy or a Server.

**Returns:**
- the authentication type of the requestor

**Since:**
- 1.5

---

### Additional Sections

#### Class Authenticator

java.lang.Object

- java.net.Authenticator

java.net.Authenticator

```java
public abstract class
Authenticator

extends
Object
```

The class Authenticator represents an object that knows how to obtain
authentication for a network connection. Usually, it will do this
by prompting the user for information.

Applications use this class by overriding

getPasswordAuthentication()

in a sub-class. This method will
typically use the various getXXX() accessor methods to get information
about the entity requesting authentication. It must then acquire a
username and password either by interacting with the user or through
some other non-interactive means. The credentials are then returned
as a

PasswordAuthentication

return value.

An instance of this concrete sub-class is then registered
with the system by calling

setDefault(Authenticator)

.
When authentication is required, the system will invoke one of the
requestPasswordAuthentication() methods which in turn will call the
getPasswordAuthentication() method of the registered object.

All methods that request authentication have a default implementation
that fails.

**Since:** 1.2
**See Also:** setDefault(java.net.Authenticator)

,

getPasswordAuthentication()

public abstract class

Authenticator

extends

Object

The class Authenticator represents an object that knows how to obtain
authentication for a network connection. Usually, it will do this
by prompting the user for information.

Applications use this class by overriding

getPasswordAuthentication()

in a sub-class. This method will
typically use the various getXXX() accessor methods to get information
about the entity requesting authentication. It must then acquire a
username and password either by interacting with the user or through
some other non-interactive means. The credentials are then returned
as a

PasswordAuthentication

return value.

An instance of this concrete sub-class is then registered
with the system by calling

setDefault(Authenticator)

.
When authentication is required, the system will invoke one of the
requestPasswordAuthentication() methods which in turn will call the
getPasswordAuthentication() method of the registered object.

All methods that request authentication have a default implementation
that fails.

Applications use this class by overriding

getPasswordAuthentication()

in a sub-class. This method will
typically use the various getXXX() accessor methods to get information
about the entity requesting authentication. It must then acquire a
username and password either by interacting with the user or through
some other non-interactive means. The credentials are then returned
as a

PasswordAuthentication

return value.

An instance of this concrete sub-class is then registered
with the system by calling

setDefault(Authenticator)

.
When authentication is required, the system will invoke one of the
requestPasswordAuthentication() methods which in turn will call the
getPasswordAuthentication() method of the registered object.

All methods that request authentication have a default implementation
that fails.

An instance of this concrete sub-class is then registered
with the system by calling

setDefault(Authenticator)

.
When authentication is required, the system will invoke one of the
requestPasswordAuthentication() methods which in turn will call the
getPasswordAuthentication() method of the registered object.

All methods that request authentication have a default implementation
that fails.

All methods that request authentication have a default implementation
that fails.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Authenticator.RequestorType

The type of the entity requesting authentication.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

Authenticator

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

Authenticator

getDefault

()

Gets the default authenticator.

protected

PasswordAuthentication

getPasswordAuthentication

()

Called when password authorization is needed.

protected

String

getRequestingHost

()

Gets the

hostname

of the
site or proxy requesting authentication, or

null

if not available.

protected int

getRequestingPort

()

Gets the port number for the requested connection.

protected

String

getRequestingPrompt

()

Gets the prompt string given by the requestor.

protected

String

getRequestingProtocol

()

Give the protocol that's requesting the connection.

protected

String

getRequestingScheme

()

Gets the scheme of the requestor (the HTTP scheme
for an HTTP firewall, for example).

protected

InetAddress

getRequestingSite

()

Gets the

InetAddress

of the
site requesting authorization, or

null

if not available.

protected

URL

getRequestingURL

()

Returns the URL that resulted in this
request for authentication.

protected

Authenticator.RequestorType

getRequestorType

()

Returns whether the requestor is a Proxy or a Server.

static

PasswordAuthentication

requestPasswordAuthentication

​(

String

host,

InetAddress

addr,
int port,

String

protocol,

String

prompt,

String

scheme)

Ask the authenticator that has been registered with the system
for a password.

static

PasswordAuthentication

requestPasswordAuthentication

​(

String

host,

InetAddress

addr,
int port,

String

protocol,

String

prompt,

String

scheme,

URL

url,

Authenticator.RequestorType

reqType)

Ask the authenticator that has been registered with the system
for a password.

static

PasswordAuthentication

requestPasswordAuthentication

​(

Authenticator

authenticator,

String

host,

InetAddress

addr,
int port,

String

protocol,

String

prompt,

String

scheme,

URL

url,

Authenticator.RequestorType

reqType)

Ask the given

authenticator

for a password.

static

PasswordAuthentication

requestPasswordAuthentication

​(

InetAddress

addr,
int port,

String

protocol,

String

prompt,

String

scheme)

Ask the authenticator that has been registered with the system
for a password.

PasswordAuthentication

requestPasswordAuthenticationInstance

​(

String

host,

InetAddress

addr,
int port,

String

protocol,

String

prompt,

String

scheme,

URL

url,

Authenticator.RequestorType

reqType)

Ask this authenticator for a password.

static void

setDefault

​(

Authenticator

a)

Sets the authenticator that will be used by the networking code
when a proxy or an HTTP server asks for authentication.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

Authenticator.RequestorType

The type of the entity requesting authentication.

---

#### Nested Class Summary

The type of the entity requesting authentication.

Constructor Summary

Constructors

Constructor

Description

Authenticator

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

static

Authenticator

getDefault

()

Gets the default authenticator.

protected

PasswordAuthentication

getPasswordAuthentication

()

Called when password authorization is needed.

protected

String

getRequestingHost

()

Gets the

hostname

of the
site or proxy requesting authentication, or

null

if not available.

protected int

getRequestingPort

()

Gets the port number for the requested connection.

protected

String

getRequestingPrompt

()

Gets the prompt string given by the requestor.

protected

String

getRequestingProtocol

()

Give the protocol that's requesting the connection.

protected

String

getRequestingScheme

()

Gets the scheme of the requestor (the HTTP scheme
for an HTTP firewall, for example).

protected

InetAddress

getRequestingSite

()

Gets the

InetAddress

of the
site requesting authorization, or

null

if not available.

protected

URL

getRequestingURL

()

Returns the URL that resulted in this
request for authentication.

protected

Authenticator.RequestorType

getRequestorType

()

Returns whether the requestor is a Proxy or a Server.

static

PasswordAuthentication

requestPasswordAuthentication

​(

String

host,

InetAddress

addr,
int port,

String

protocol,

String

prompt,

String

scheme)

Ask the authenticator that has been registered with the system
for a password.

static

PasswordAuthentication

requestPasswordAuthentication

​(

String

host,

InetAddress

addr,
int port,

String

protocol,

String

prompt,

String

scheme,

URL

url,

Authenticator.RequestorType

reqType)

Ask the authenticator that has been registered with the system
for a password.

static

PasswordAuthentication

requestPasswordAuthentication

​(

Authenticator

authenticator,

String

host,

InetAddress

addr,
int port,

String

protocol,

String

prompt,

String

scheme,

URL

url,

Authenticator.RequestorType

reqType)

Ask the given

authenticator

for a password.

static

PasswordAuthentication

requestPasswordAuthentication

​(

InetAddress

addr,
int port,

String

protocol,

String

prompt,

String

scheme)

Ask the authenticator that has been registered with the system
for a password.

PasswordAuthentication

requestPasswordAuthenticationInstance

​(

String

host,

InetAddress

addr,
int port,

String

protocol,

String

prompt,

String

scheme,

URL

url,

Authenticator.RequestorType

reqType)

Ask this authenticator for a password.

static void

setDefault

​(

Authenticator

a)

Sets the authenticator that will be used by the networking code
when a proxy or an HTTP server asks for authentication.

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

Gets the default authenticator.

Called when password authorization is needed.

Gets the

hostname

of the
site or proxy requesting authentication, or

null

if not available.

Gets the port number for the requested connection.

Gets the prompt string given by the requestor.

Give the protocol that's requesting the connection.

Gets the scheme of the requestor (the HTTP scheme
for an HTTP firewall, for example).

Gets the

InetAddress

of the
site requesting authorization, or

null

if not available.

Returns the URL that resulted in this
request for authentication.

Returns whether the requestor is a Proxy or a Server.

Ask the authenticator that has been registered with the system
for a password.

Ask the given

authenticator

for a password.

Ask this authenticator for a password.

Sets the authenticator that will be used by the networking code
when a proxy or an HTTP server asks for authentication.

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

- Authenticator

```java
public Authenticator()
```

============ METHOD DETAIL ==========

- Method Detail

- setDefault

```java
public static void setDefault​(
Authenticator
a)
```

Sets the authenticator that will be used by the networking code
when a proxy or an HTTP server asks for authentication.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("setDefaultAuthenticator")

permission.
This may result in a java.lang.SecurityException.

**Parameters:** a

- The authenticator to be set. If a is

null

then
any previously set authenticator is removed.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
setting the default authenticator.
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

- getDefault

```java
public static
Authenticator
getDefault()
```

Gets the default authenticator.
First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.
Then the default authenticator, if set, is returned.
Otherwise,

null

is returned.

**Returns:** The default authenticator, if set,

null

otherwise.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
requesting password authentication.
**Since:** 9
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

- requestPasswordAuthentication

```java
public static
PasswordAuthentication
requestPasswordAuthentication​(
InetAddress
addr,
int port,

String
protocol,

String
prompt,

String
scheme)
```

Ask the authenticator that has been registered with the system
for a password.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

**Parameters:** addr

- The InetAddress of the site requesting authorization,
or null if not known.
**Parameters:** port

- the port for the requested connection
**Parameters:** protocol

- The protocol that's requesting the connection
(

getRequestingProtocol()

)
**Parameters:** prompt

- A prompt string for the user
**Parameters:** scheme

- The authentication scheme
**Returns:** The username/password, or null if one can't be gotten.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
the password authentication request.
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

- requestPasswordAuthentication

```java
public static
PasswordAuthentication
requestPasswordAuthentication​(
String
host,

InetAddress
addr,
int port,

String
protocol,

String
prompt,

String
scheme)
```

Ask the authenticator that has been registered with the system
for a password. This is the preferred method for requesting a password
because the hostname can be provided in cases where the InetAddress
is not available.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

**Parameters:** host

- The hostname of the site requesting authentication.
**Parameters:** addr

- The InetAddress of the site requesting authentication,
or null if not known.
**Parameters:** port

- the port for the requested connection.
**Parameters:** protocol

- The protocol that's requesting the connection
(

getRequestingProtocol()

)
**Parameters:** prompt

- A prompt string for the user which identifies the authentication realm.
**Parameters:** scheme

- The authentication scheme
**Returns:** The username/password, or null if one can't be gotten.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
the password authentication request.
**Since:** 1.4
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

- requestPasswordAuthentication

```java
public static
PasswordAuthentication
requestPasswordAuthentication​(
String
host,

InetAddress
addr,
int port,

String
protocol,

String
prompt,

String
scheme,

URL
url,

Authenticator.RequestorType
reqType)
```

Ask the authenticator that has been registered with the system
for a password.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

**Parameters:** host

- The hostname of the site requesting authentication.
**Parameters:** addr

- The InetAddress of the site requesting authorization,
or null if not known.
**Parameters:** port

- the port for the requested connection
**Parameters:** protocol

- The protocol that's requesting the connection
(

getRequestingProtocol()

)
**Parameters:** prompt

- A prompt string for the user
**Parameters:** scheme

- The authentication scheme
**Parameters:** url

- The requesting URL that caused the authentication
**Parameters:** reqType

- The type (server or proxy) of the entity requesting
authentication.
**Returns:** The username/password, or null if one can't be gotten.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
the password authentication request.
**Since:** 1.5
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

- requestPasswordAuthentication

```java
public static
PasswordAuthentication
requestPasswordAuthentication​(
Authenticator
authenticator,

String
host,

InetAddress
addr,
int port,

String
protocol,

String
prompt,

String
scheme,

URL
url,

Authenticator.RequestorType
reqType)
```

Ask the given

authenticator

for a password. If the given

authenticator

is null, the authenticator, if any, that has been
registered with the system using

setDefault

is used.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

**Parameters:** authenticator

- the authenticator, or

null

.
**Parameters:** host

- The hostname of the site requesting authentication.
**Parameters:** addr

- The InetAddress of the site requesting authorization,
or null if not known.
**Parameters:** port

- the port for the requested connection
**Parameters:** protocol

- The protocol that's requesting the connection
(

getRequestingProtocol()

)
**Parameters:** prompt

- A prompt string for the user
**Parameters:** scheme

- The authentication scheme
**Parameters:** url

- The requesting URL that caused the authentication
**Parameters:** reqType

- The type (server or proxy) of the entity requesting
authentication.
**Returns:** The username/password, or

null

if one can't be gotten.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
the password authentication request.
**Since:** 9
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

- requestPasswordAuthenticationInstance

```java
public
PasswordAuthentication
requestPasswordAuthenticationInstance​(
String
host,

InetAddress
addr,
int port,

String
protocol,

String
prompt,

String
scheme,

URL
url,

Authenticator.RequestorType
reqType)
```

Ask this authenticator for a password.

**Parameters:** host

- The hostname of the site requesting authentication.
**Parameters:** addr

- The InetAddress of the site requesting authorization,
or null if not known.
**Parameters:** port

- the port for the requested connection
**Parameters:** protocol

- The protocol that's requesting the connection
(

getRequestingProtocol()

)
**Parameters:** prompt

- A prompt string for the user
**Parameters:** scheme

- The authentication scheme
**Parameters:** url

- The requesting URL that caused the authentication
**Parameters:** reqType

- The type (server or proxy) of the entity requesting
authentication.
**Returns:** The username/password, or null if one can't be gotten
**Since:** 9

- getRequestingHost

```java
protected final
String
getRequestingHost()
```

Gets the

hostname

of the
site or proxy requesting authentication, or

null

if not available.

**Returns:** the hostname of the connection requiring authentication, or null
if it's not available.
**Since:** 1.4

- getRequestingSite

```java
protected final
InetAddress
getRequestingSite()
```

Gets the

InetAddress

of the
site requesting authorization, or

null

if not available.

**Returns:** the InetAddress of the site requesting authorization, or null
if it's not available.

- getRequestingPort

```java
protected final int getRequestingPort()
```

Gets the port number for the requested connection.

**Returns:** an

int

indicating the
port for the requested connection.

- getRequestingProtocol

```java
protected final
String
getRequestingProtocol()
```

Give the protocol that's requesting the connection. Often this
will be based on a URL, but in a future JDK it could be, for
example, "SOCKS" for a password-protected SOCKS5 firewall.

**Returns:** the protocol, optionally followed by "/version", where
version is a version number.
**See Also:** URL.getProtocol()

- getRequestingPrompt

```java
protected final
String
getRequestingPrompt()
```

Gets the prompt string given by the requestor.

**Returns:** the prompt string given by the requestor (realm for
http requests)

- getRequestingScheme

```java
protected final
String
getRequestingScheme()
```

Gets the scheme of the requestor (the HTTP scheme
for an HTTP firewall, for example).

**Returns:** the scheme of the requestor

- getPasswordAuthentication

```java
protected
PasswordAuthentication
getPasswordAuthentication()
```

Called when password authorization is needed. Subclasses should
override the default implementation, which returns null.

**Returns:** The PasswordAuthentication collected from the
user, or null if none is provided.

- getRequestingURL

```java
protected
URL
getRequestingURL()
```

Returns the URL that resulted in this
request for authentication.

**Returns:** the requesting URL
**Since:** 1.5

- getRequestorType

```java
protected
Authenticator.RequestorType
getRequestorType()
```

Returns whether the requestor is a Proxy or a Server.

**Returns:** the authentication type of the requestor
**Since:** 1.5

Constructor Detail

- Authenticator

```java
public Authenticator()
```

---

#### Constructor Detail

Authenticator

```java
public Authenticator()
```

---

#### Authenticator

public Authenticator()

Method Detail

- setDefault

```java
public static void setDefault​(
Authenticator
a)
```

Sets the authenticator that will be used by the networking code
when a proxy or an HTTP server asks for authentication.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("setDefaultAuthenticator")

permission.
This may result in a java.lang.SecurityException.

**Parameters:** a

- The authenticator to be set. If a is

null

then
any previously set authenticator is removed.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
setting the default authenticator.
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

- getDefault

```java
public static
Authenticator
getDefault()
```

Gets the default authenticator.
First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.
Then the default authenticator, if set, is returned.
Otherwise,

null

is returned.

**Returns:** The default authenticator, if set,

null

otherwise.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
requesting password authentication.
**Since:** 9
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

- requestPasswordAuthentication

```java
public static
PasswordAuthentication
requestPasswordAuthentication​(
InetAddress
addr,
int port,

String
protocol,

String
prompt,

String
scheme)
```

Ask the authenticator that has been registered with the system
for a password.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

**Parameters:** addr

- The InetAddress of the site requesting authorization,
or null if not known.
**Parameters:** port

- the port for the requested connection
**Parameters:** protocol

- The protocol that's requesting the connection
(

getRequestingProtocol()

)
**Parameters:** prompt

- A prompt string for the user
**Parameters:** scheme

- The authentication scheme
**Returns:** The username/password, or null if one can't be gotten.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
the password authentication request.
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

- requestPasswordAuthentication

```java
public static
PasswordAuthentication
requestPasswordAuthentication​(
String
host,

InetAddress
addr,
int port,

String
protocol,

String
prompt,

String
scheme)
```

Ask the authenticator that has been registered with the system
for a password. This is the preferred method for requesting a password
because the hostname can be provided in cases where the InetAddress
is not available.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

**Parameters:** host

- The hostname of the site requesting authentication.
**Parameters:** addr

- The InetAddress of the site requesting authentication,
or null if not known.
**Parameters:** port

- the port for the requested connection.
**Parameters:** protocol

- The protocol that's requesting the connection
(

getRequestingProtocol()

)
**Parameters:** prompt

- A prompt string for the user which identifies the authentication realm.
**Parameters:** scheme

- The authentication scheme
**Returns:** The username/password, or null if one can't be gotten.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
the password authentication request.
**Since:** 1.4
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

- requestPasswordAuthentication

```java
public static
PasswordAuthentication
requestPasswordAuthentication​(
String
host,

InetAddress
addr,
int port,

String
protocol,

String
prompt,

String
scheme,

URL
url,

Authenticator.RequestorType
reqType)
```

Ask the authenticator that has been registered with the system
for a password.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

**Parameters:** host

- The hostname of the site requesting authentication.
**Parameters:** addr

- The InetAddress of the site requesting authorization,
or null if not known.
**Parameters:** port

- the port for the requested connection
**Parameters:** protocol

- The protocol that's requesting the connection
(

getRequestingProtocol()

)
**Parameters:** prompt

- A prompt string for the user
**Parameters:** scheme

- The authentication scheme
**Parameters:** url

- The requesting URL that caused the authentication
**Parameters:** reqType

- The type (server or proxy) of the entity requesting
authentication.
**Returns:** The username/password, or null if one can't be gotten.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
the password authentication request.
**Since:** 1.5
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

- requestPasswordAuthentication

```java
public static
PasswordAuthentication
requestPasswordAuthentication​(
Authenticator
authenticator,

String
host,

InetAddress
addr,
int port,

String
protocol,

String
prompt,

String
scheme,

URL
url,

Authenticator.RequestorType
reqType)
```

Ask the given

authenticator

for a password. If the given

authenticator

is null, the authenticator, if any, that has been
registered with the system using

setDefault

is used.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

**Parameters:** authenticator

- the authenticator, or

null

.
**Parameters:** host

- The hostname of the site requesting authentication.
**Parameters:** addr

- The InetAddress of the site requesting authorization,
or null if not known.
**Parameters:** port

- the port for the requested connection
**Parameters:** protocol

- The protocol that's requesting the connection
(

getRequestingProtocol()

)
**Parameters:** prompt

- A prompt string for the user
**Parameters:** scheme

- The authentication scheme
**Parameters:** url

- The requesting URL that caused the authentication
**Parameters:** reqType

- The type (server or proxy) of the entity requesting
authentication.
**Returns:** The username/password, or

null

if one can't be gotten.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
the password authentication request.
**Since:** 9
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

- requestPasswordAuthenticationInstance

```java
public
PasswordAuthentication
requestPasswordAuthenticationInstance​(
String
host,

InetAddress
addr,
int port,

String
protocol,

String
prompt,

String
scheme,

URL
url,

Authenticator.RequestorType
reqType)
```

Ask this authenticator for a password.

**Parameters:** host

- The hostname of the site requesting authentication.
**Parameters:** addr

- The InetAddress of the site requesting authorization,
or null if not known.
**Parameters:** port

- the port for the requested connection
**Parameters:** protocol

- The protocol that's requesting the connection
(

getRequestingProtocol()

)
**Parameters:** prompt

- A prompt string for the user
**Parameters:** scheme

- The authentication scheme
**Parameters:** url

- The requesting URL that caused the authentication
**Parameters:** reqType

- The type (server or proxy) of the entity requesting
authentication.
**Returns:** The username/password, or null if one can't be gotten
**Since:** 9

- getRequestingHost

```java
protected final
String
getRequestingHost()
```

Gets the

hostname

of the
site or proxy requesting authentication, or

null

if not available.

**Returns:** the hostname of the connection requiring authentication, or null
if it's not available.
**Since:** 1.4

- getRequestingSite

```java
protected final
InetAddress
getRequestingSite()
```

Gets the

InetAddress

of the
site requesting authorization, or

null

if not available.

**Returns:** the InetAddress of the site requesting authorization, or null
if it's not available.

- getRequestingPort

```java
protected final int getRequestingPort()
```

Gets the port number for the requested connection.

**Returns:** an

int

indicating the
port for the requested connection.

- getRequestingProtocol

```java
protected final
String
getRequestingProtocol()
```

Give the protocol that's requesting the connection. Often this
will be based on a URL, but in a future JDK it could be, for
example, "SOCKS" for a password-protected SOCKS5 firewall.

**Returns:** the protocol, optionally followed by "/version", where
version is a version number.
**See Also:** URL.getProtocol()

- getRequestingPrompt

```java
protected final
String
getRequestingPrompt()
```

Gets the prompt string given by the requestor.

**Returns:** the prompt string given by the requestor (realm for
http requests)

- getRequestingScheme

```java
protected final
String
getRequestingScheme()
```

Gets the scheme of the requestor (the HTTP scheme
for an HTTP firewall, for example).

**Returns:** the scheme of the requestor

- getPasswordAuthentication

```java
protected
PasswordAuthentication
getPasswordAuthentication()
```

Called when password authorization is needed. Subclasses should
override the default implementation, which returns null.

**Returns:** The PasswordAuthentication collected from the
user, or null if none is provided.

- getRequestingURL

```java
protected
URL
getRequestingURL()
```

Returns the URL that resulted in this
request for authentication.

**Returns:** the requesting URL
**Since:** 1.5

- getRequestorType

```java
protected
Authenticator.RequestorType
getRequestorType()
```

Returns whether the requestor is a Proxy or a Server.

**Returns:** the authentication type of the requestor
**Since:** 1.5

---

#### Method Detail

setDefault

```java
public static void setDefault​(
Authenticator
a)
```

Sets the authenticator that will be used by the networking code
when a proxy or an HTTP server asks for authentication.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("setDefaultAuthenticator")

permission.
This may result in a java.lang.SecurityException.

**Parameters:** a

- The authenticator to be set. If a is

null

then
any previously set authenticator is removed.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
setting the default authenticator.
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

---

#### setDefault

public static void setDefault​(

Authenticator

a)

Sets the authenticator that will be used by the networking code
when a proxy or an HTTP server asks for authentication.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("setDefaultAuthenticator")

permission.
This may result in a java.lang.SecurityException.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("setDefaultAuthenticator")

permission.
This may result in a java.lang.SecurityException.

getDefault

```java
public static
Authenticator
getDefault()
```

Gets the default authenticator.
First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.
Then the default authenticator, if set, is returned.
Otherwise,

null

is returned.

**Returns:** The default authenticator, if set,

null

otherwise.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
requesting password authentication.
**Since:** 9
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

---

#### getDefault

public static

Authenticator

getDefault()

Gets the default authenticator.
First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.
Then the default authenticator, if set, is returned.
Otherwise,

null

is returned.

requestPasswordAuthentication

```java
public static
PasswordAuthentication
requestPasswordAuthentication​(
InetAddress
addr,
int port,

String
protocol,

String
prompt,

String
scheme)
```

Ask the authenticator that has been registered with the system
for a password.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

**Parameters:** addr

- The InetAddress of the site requesting authorization,
or null if not known.
**Parameters:** port

- the port for the requested connection
**Parameters:** protocol

- The protocol that's requesting the connection
(

getRequestingProtocol()

)
**Parameters:** prompt

- A prompt string for the user
**Parameters:** scheme

- The authentication scheme
**Returns:** The username/password, or null if one can't be gotten.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
the password authentication request.
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

---

#### requestPasswordAuthentication

public static

PasswordAuthentication

requestPasswordAuthentication​(

InetAddress

addr,
int port,

String

protocol,

String

prompt,

String

scheme)

Ask the authenticator that has been registered with the system
for a password.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

requestPasswordAuthentication

```java
public static
PasswordAuthentication
requestPasswordAuthentication​(
String
host,

InetAddress
addr,
int port,

String
protocol,

String
prompt,

String
scheme)
```

Ask the authenticator that has been registered with the system
for a password. This is the preferred method for requesting a password
because the hostname can be provided in cases where the InetAddress
is not available.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

**Parameters:** host

- The hostname of the site requesting authentication.
**Parameters:** addr

- The InetAddress of the site requesting authentication,
or null if not known.
**Parameters:** port

- the port for the requested connection.
**Parameters:** protocol

- The protocol that's requesting the connection
(

getRequestingProtocol()

)
**Parameters:** prompt

- A prompt string for the user which identifies the authentication realm.
**Parameters:** scheme

- The authentication scheme
**Returns:** The username/password, or null if one can't be gotten.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
the password authentication request.
**Since:** 1.4
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

---

#### requestPasswordAuthentication

public static

PasswordAuthentication

requestPasswordAuthentication​(

String

host,

InetAddress

addr,
int port,

String

protocol,

String

prompt,

String

scheme)

Ask the authenticator that has been registered with the system
for a password. This is the preferred method for requesting a password
because the hostname can be provided in cases where the InetAddress
is not available.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

requestPasswordAuthentication

```java
public static
PasswordAuthentication
requestPasswordAuthentication​(
String
host,

InetAddress
addr,
int port,

String
protocol,

String
prompt,

String
scheme,

URL
url,

Authenticator.RequestorType
reqType)
```

Ask the authenticator that has been registered with the system
for a password.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

**Parameters:** host

- The hostname of the site requesting authentication.
**Parameters:** addr

- The InetAddress of the site requesting authorization,
or null if not known.
**Parameters:** port

- the port for the requested connection
**Parameters:** protocol

- The protocol that's requesting the connection
(

getRequestingProtocol()

)
**Parameters:** prompt

- A prompt string for the user
**Parameters:** scheme

- The authentication scheme
**Parameters:** url

- The requesting URL that caused the authentication
**Parameters:** reqType

- The type (server or proxy) of the entity requesting
authentication.
**Returns:** The username/password, or null if one can't be gotten.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
the password authentication request.
**Since:** 1.5
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

---

#### requestPasswordAuthentication

public static

PasswordAuthentication

requestPasswordAuthentication​(

String

host,

InetAddress

addr,
int port,

String

protocol,

String

prompt,

String

scheme,

URL

url,

Authenticator.RequestorType

reqType)

Ask the authenticator that has been registered with the system
for a password.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

requestPasswordAuthentication

```java
public static
PasswordAuthentication
requestPasswordAuthentication​(
Authenticator
authenticator,

String
host,

InetAddress
addr,
int port,

String
protocol,

String
prompt,

String
scheme,

URL
url,

Authenticator.RequestorType
reqType)
```

Ask the given

authenticator

for a password. If the given

authenticator

is null, the authenticator, if any, that has been
registered with the system using

setDefault

is used.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

**Parameters:** authenticator

- the authenticator, or

null

.
**Parameters:** host

- The hostname of the site requesting authentication.
**Parameters:** addr

- The InetAddress of the site requesting authorization,
or null if not known.
**Parameters:** port

- the port for the requested connection
**Parameters:** protocol

- The protocol that's requesting the connection
(

getRequestingProtocol()

)
**Parameters:** prompt

- A prompt string for the user
**Parameters:** scheme

- The authentication scheme
**Parameters:** url

- The requesting URL that caused the authentication
**Parameters:** reqType

- The type (server or proxy) of the entity requesting
authentication.
**Returns:** The username/password, or

null

if one can't be gotten.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
the password authentication request.
**Since:** 9
**See Also:** SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

---

#### requestPasswordAuthentication

public static

PasswordAuthentication

requestPasswordAuthentication​(

Authenticator

authenticator,

String

host,

InetAddress

addr,
int port,

String

protocol,

String

prompt,

String

scheme,

URL

url,

Authenticator.RequestorType

reqType)

Ask the given

authenticator

for a password. If the given

authenticator

is null, the authenticator, if any, that has been
registered with the system using

setDefault

is used.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

First, if there is a security manager, its

checkPermission

method is called with a

NetPermission("requestPasswordAuthentication")

permission.
This may result in a java.lang.SecurityException.

requestPasswordAuthenticationInstance

```java
public
PasswordAuthentication
requestPasswordAuthenticationInstance​(
String
host,

InetAddress
addr,
int port,

String
protocol,

String
prompt,

String
scheme,

URL
url,

Authenticator.RequestorType
reqType)
```

Ask this authenticator for a password.

**Parameters:** host

- The hostname of the site requesting authentication.
**Parameters:** addr

- The InetAddress of the site requesting authorization,
or null if not known.
**Parameters:** port

- the port for the requested connection
**Parameters:** protocol

- The protocol that's requesting the connection
(

getRequestingProtocol()

)
**Parameters:** prompt

- A prompt string for the user
**Parameters:** scheme

- The authentication scheme
**Parameters:** url

- The requesting URL that caused the authentication
**Parameters:** reqType

- The type (server or proxy) of the entity requesting
authentication.
**Returns:** The username/password, or null if one can't be gotten
**Since:** 9

---

#### requestPasswordAuthenticationInstance

public

PasswordAuthentication

requestPasswordAuthenticationInstance​(

String

host,

InetAddress

addr,
int port,

String

protocol,

String

prompt,

String

scheme,

URL

url,

Authenticator.RequestorType

reqType)

Ask this authenticator for a password.

getRequestingHost

```java
protected final
String
getRequestingHost()
```

Gets the

hostname

of the
site or proxy requesting authentication, or

null

if not available.

**Returns:** the hostname of the connection requiring authentication, or null
if it's not available.
**Since:** 1.4

---

#### getRequestingHost

protected final

String

getRequestingHost()

Gets the

hostname

of the
site or proxy requesting authentication, or

null

if not available.

getRequestingSite

```java
protected final
InetAddress
getRequestingSite()
```

Gets the

InetAddress

of the
site requesting authorization, or

null

if not available.

**Returns:** the InetAddress of the site requesting authorization, or null
if it's not available.

---

#### getRequestingSite

protected final

InetAddress

getRequestingSite()

Gets the

InetAddress

of the
site requesting authorization, or

null

if not available.

getRequestingPort

```java
protected final int getRequestingPort()
```

Gets the port number for the requested connection.

**Returns:** an

int

indicating the
port for the requested connection.

---

#### getRequestingPort

protected final int getRequestingPort()

Gets the port number for the requested connection.

getRequestingProtocol

```java
protected final
String
getRequestingProtocol()
```

Give the protocol that's requesting the connection. Often this
will be based on a URL, but in a future JDK it could be, for
example, "SOCKS" for a password-protected SOCKS5 firewall.

**Returns:** the protocol, optionally followed by "/version", where
version is a version number.
**See Also:** URL.getProtocol()

---

#### getRequestingProtocol

protected final

String

getRequestingProtocol()

Give the protocol that's requesting the connection. Often this
will be based on a URL, but in a future JDK it could be, for
example, "SOCKS" for a password-protected SOCKS5 firewall.

getRequestingPrompt

```java
protected final
String
getRequestingPrompt()
```

Gets the prompt string given by the requestor.

**Returns:** the prompt string given by the requestor (realm for
http requests)

---

#### getRequestingPrompt

protected final

String

getRequestingPrompt()

Gets the prompt string given by the requestor.

getRequestingScheme

```java
protected final
String
getRequestingScheme()
```

Gets the scheme of the requestor (the HTTP scheme
for an HTTP firewall, for example).

**Returns:** the scheme of the requestor

---

#### getRequestingScheme

protected final

String

getRequestingScheme()

Gets the scheme of the requestor (the HTTP scheme
for an HTTP firewall, for example).

getPasswordAuthentication

```java
protected
PasswordAuthentication
getPasswordAuthentication()
```

Called when password authorization is needed. Subclasses should
override the default implementation, which returns null.

**Returns:** The PasswordAuthentication collected from the
user, or null if none is provided.

---

#### getPasswordAuthentication

protected

PasswordAuthentication

getPasswordAuthentication()

Called when password authorization is needed. Subclasses should
override the default implementation, which returns null.

getRequestingURL

```java
protected
URL
getRequestingURL()
```

Returns the URL that resulted in this
request for authentication.

**Returns:** the requesting URL
**Since:** 1.5

---

#### getRequestingURL

protected

URL

getRequestingURL()

Returns the URL that resulted in this
request for authentication.

getRequestorType

```java
protected
Authenticator.RequestorType
getRequestorType()
```

Returns whether the requestor is a Proxy or a Server.

**Returns:** the authentication type of the requestor
**Since:** 1.5

---

#### getRequestorType

protected

Authenticator.RequestorType

getRequestorType()

Returns whether the requestor is a Proxy or a Server.

---

