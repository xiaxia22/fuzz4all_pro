# Class URLStreamHandler

**Source:** `java.base\java\net\URLStreamHandler.html`

### Class Description

```java
public abstract class
URLStreamHandler

extends
Object
```

The abstract class

URLStreamHandler

is the common
superclass for all stream protocol handlers. A stream protocol
handler knows how to make a connection for a particular protocol
type, such as

http

or

https

.

In most cases, an instance of a

URLStreamHandler

subclass is not created directly by an application. Rather, the
first time a protocol name is encountered when constructing a

URL

, the appropriate stream protocol handler is
automatically loaded.

**Since:** 1.0
**See Also:** URL(java.lang.String, java.lang.String, int, java.lang.String)

---

### Field Details

*No entries found.*

### Constructor Details

#### public URLStreamHandler()

*No description found.*

---

### Method Details

#### protected abstract
URLConnection
openConnection​(
URL
u)
throws
IOException

Opens a connection to the object referenced by the

URL

argument.
This method should be overridden by a subclass.

If for the handler's protocol (such as HTTP or JAR), there
exists a public, specialized URLConnection subclass belonging
to one of the following packages or one of their subpackages:
java.lang, java.io, java.util, java.net, the connection
returned will be of that subclass. For example, for HTTP an
HttpURLConnection will be returned, and for JAR a
JarURLConnection will be returned.

**Parameters:**
- u

- the URL that this connects to.

**Returns:**
- a

URLConnection

object for the

URL

.

**Throws:**
- IOException

- if an I/O error occurs while opening the
connection.

---

#### protected
URLConnection
openConnection​(
URL
u,

Proxy
p)
throws
IOException

Same as openConnection(URL), except that the connection will be
made through the specified proxy; Protocol handlers that do not
support proxying will ignore the proxy parameter and make a
normal connection.

Calling this method preempts the system's default

ProxySelector

settings.

**Parameters:**
- u

- the URL that this connects to.
- p

- the proxy through which the connection will be made.
If direct connection is desired, Proxy.NO_PROXY
should be specified.

**Returns:**
- a

URLConnection

object for the

URL

.

**Throws:**
- IOException

- if an I/O error occurs while opening the
connection.
- IllegalArgumentException

- if either u or p is null,
or p has the wrong type.
- UnsupportedOperationException

- if the subclass that
implements the protocol doesn't support this method.

**Since:**
- 1.5

---

#### protected void parseURL​(
URL
u,

String
spec,
int start,
int limit)

Parses the string representation of a

URL

into a

URL

object.

If there is any inherited context, then it has already been
copied into the

URL

argument.

The

parseURL

method of

URLStreamHandler

parses the string representation as if it were an

http

specification. Most URL protocol families have a
similar parsing. A stream protocol handler for a protocol that has
a different syntax must override this routine.

**Parameters:**
- u

- the

URL

to receive the result of parsing
the spec.
- spec

- the

String

representing the URL that
must be parsed.
- start

- the character index at which to begin parsing. This is
just past the '

:

' (if there is one) that
specifies the determination of the protocol name.
- limit

- the character position to stop parsing at. This is the
end of the string or the position of the
"

#

" character, if present. All information
after the sharp sign indicates an anchor.

---

#### protected int getDefaultPort()

Returns the default port for a URL parsed by this handler. This method
is meant to be overidden by handlers with default port numbers.

**Returns:**
- the default port for a

URL

parsed by this handler.

**Since:**
- 1.3

---

#### protected boolean equals​(
URL
u1,

URL
u2)

Provides the default equals calculation. May be overidden by handlers
for other protocols that have different requirements for equals().
This method requires that none of its arguments is null. This is
guaranteed by the fact that it is only called by java.net.URL class.

**Parameters:**
- u1

- a URL object
- u2

- a URL object

**Returns:**
- true

if the two urls are
considered equal, ie. they refer to the same
fragment in the same file.

**Since:**
- 1.3

---

#### protected int hashCode​(
URL
u)

Provides the default hash calculation. May be overidden by handlers for
other protocols that have different requirements for hashCode
calculation.

**Parameters:**
- u

- a URL object

**Returns:**
- an

int

suitable for hash table indexing

**Since:**
- 1.3

---

#### protected boolean sameFile​(
URL
u1,

URL
u2)

Compare two urls to see whether they refer to the same file,
i.e., having the same protocol, host, port, and path.
This method requires that none of its arguments is null. This is
guaranteed by the fact that it is only called indirectly
by java.net.URL class.

**Parameters:**
- u1

- a URL object
- u2

- a URL object

**Returns:**
- true if u1 and u2 refer to the same file

**Since:**
- 1.3

---

#### protected
InetAddress
getHostAddress​(
URL
u)

Get the IP address of our host. An empty host field or a DNS failure
will result in a null return.

**Parameters:**
- u

- a URL object

**Returns:**
- an

InetAddress

representing the host
IP address.

**Since:**
- 1.3

---

#### protected boolean hostsEqual​(
URL
u1,

URL
u2)

Compares the host components of two URLs.

**Parameters:**
- u1

- the URL of the first host to compare
- u2

- the URL of the second host to compare

**Returns:**
- true

if and only if they
are equal,

false

otherwise.

**Since:**
- 1.3

---

#### protected
String
toExternalForm​(
URL
u)

Converts a

URL

of a specific protocol to a

String

.

**Parameters:**
- u

- the URL.

**Returns:**
- a string representation of the

URL

argument.

---

#### protected void setURL​(
URL
u,

String
protocol,

String
host,
int port,

String
authority,

String
userInfo,

String
path,

String
query,

String
ref)

Sets the fields of the

URL

argument to the indicated values.
Only classes derived from URLStreamHandler are able
to use this method to set the values of the URL fields.

**Parameters:**
- u

- the URL to modify.
- protocol

- the protocol name.
- host

- the remote host value for the URL.
- port

- the port on the remote machine.
- authority

- the authority part for the URL.
- userInfo

- the userInfo part of the URL.
- path

- the path component of the URL.
- query

- the query part for the URL.
- ref

- the reference.

**Throws:**
- SecurityException

- if the protocol handler of the URL is
different from this one

**Since:**
- 1.3

---

#### @Deprecated

protected void setURL​(
URL
u,

String
protocol,

String
host,
int port,

String
file,

String
ref)

Sets the fields of the

URL

argument to the indicated values.
Only classes derived from URLStreamHandler are able
to use this method to set the values of the URL fields.

**Parameters:**
- u

- the URL to modify.
- protocol

- the protocol name. This value is ignored since 1.2.
- host

- the remote host value for the URL.
- port

- the port on the remote machine.
- file

- the file.
- ref

- the reference.

**Throws:**
- SecurityException

- if the protocol handler of the URL is
different from this one

---

### Additional Sections

#### Class URLStreamHandler

java.lang.Object

- java.net.URLStreamHandler

java.net.URLStreamHandler

```java
public abstract class
URLStreamHandler

extends
Object
```

The abstract class

URLStreamHandler

is the common
superclass for all stream protocol handlers. A stream protocol
handler knows how to make a connection for a particular protocol
type, such as

http

or

https

.

In most cases, an instance of a

URLStreamHandler

subclass is not created directly by an application. Rather, the
first time a protocol name is encountered when constructing a

URL

, the appropriate stream protocol handler is
automatically loaded.

**Since:** 1.0
**See Also:** URL(java.lang.String, java.lang.String, int, java.lang.String)

public abstract class

URLStreamHandler

extends

Object

The abstract class

URLStreamHandler

is the common
superclass for all stream protocol handlers. A stream protocol
handler knows how to make a connection for a particular protocol
type, such as

http

or

https

.

In most cases, an instance of a

URLStreamHandler

subclass is not created directly by an application. Rather, the
first time a protocol name is encountered when constructing a

URL

, the appropriate stream protocol handler is
automatically loaded.

In most cases, an instance of a

URLStreamHandler

subclass is not created directly by an application. Rather, the
first time a protocol name is encountered when constructing a

URL

, the appropriate stream protocol handler is
automatically loaded.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

URLStreamHandler

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

protected boolean

equals

​(

URL

u1,

URL

u2)

Provides the default equals calculation.

protected int

getDefaultPort

()

Returns the default port for a URL parsed by this handler.

protected

InetAddress

getHostAddress

​(

URL

u)

Get the IP address of our host.

protected int

hashCode

​(

URL

u)

Provides the default hash calculation.

protected boolean

hostsEqual

​(

URL

u1,

URL

u2)

Compares the host components of two URLs.

protected abstract

URLConnection

openConnection

​(

URL

u)

Opens a connection to the object referenced by the

URL

argument.

protected

URLConnection

openConnection

​(

URL

u,

Proxy

p)

Same as openConnection(URL), except that the connection will be
made through the specified proxy; Protocol handlers that do not
support proxying will ignore the proxy parameter and make a
normal connection.

protected void

parseURL

​(

URL

u,

String

spec,
int start,
int limit)

Parses the string representation of a

URL

into a

URL

object.

protected boolean

sameFile

​(

URL

u1,

URL

u2)

Compare two urls to see whether they refer to the same file,
i.e., having the same protocol, host, port, and path.

protected void

setURL

​(

URL

u,

String

protocol,

String

host,
int port,

String

file,

String

ref)

Deprecated.

Use setURL(URL, String, String, int, String, String, String,
String);

protected void

setURL

​(

URL

u,

String

protocol,

String

host,
int port,

String

authority,

String

userInfo,

String

path,

String

query,

String

ref)

Sets the fields of the

URL

argument to the indicated values.

protected

String

toExternalForm

​(

URL

u)

Converts a

URL

of a specific protocol to a

String

.

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

URLStreamHandler

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Deprecated Methods

Modifier and Type

Method

Description

protected boolean

equals

​(

URL

u1,

URL

u2)

Provides the default equals calculation.

protected int

getDefaultPort

()

Returns the default port for a URL parsed by this handler.

protected

InetAddress

getHostAddress

​(

URL

u)

Get the IP address of our host.

protected int

hashCode

​(

URL

u)

Provides the default hash calculation.

protected boolean

hostsEqual

​(

URL

u1,

URL

u2)

Compares the host components of two URLs.

protected abstract

URLConnection

openConnection

​(

URL

u)

Opens a connection to the object referenced by the

URL

argument.

protected

URLConnection

openConnection

​(

URL

u,

Proxy

p)

Same as openConnection(URL), except that the connection will be
made through the specified proxy; Protocol handlers that do not
support proxying will ignore the proxy parameter and make a
normal connection.

protected void

parseURL

​(

URL

u,

String

spec,
int start,
int limit)

Parses the string representation of a

URL

into a

URL

object.

protected boolean

sameFile

​(

URL

u1,

URL

u2)

Compare two urls to see whether they refer to the same file,
i.e., having the same protocol, host, port, and path.

protected void

setURL

​(

URL

u,

String

protocol,

String

host,
int port,

String

file,

String

ref)

Deprecated.

Use setURL(URL, String, String, int, String, String, String,
String);

protected void

setURL

​(

URL

u,

String

protocol,

String

host,
int port,

String

authority,

String

userInfo,

String

path,

String

query,

String

ref)

Sets the fields of the

URL

argument to the indicated values.

protected

String

toExternalForm

​(

URL

u)

Converts a

URL

of a specific protocol to a

String

.

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

Provides the default equals calculation.

Returns the default port for a URL parsed by this handler.

Get the IP address of our host.

Provides the default hash calculation.

Compares the host components of two URLs.

Opens a connection to the object referenced by the

URL

argument.

Same as openConnection(URL), except that the connection will be
made through the specified proxy; Protocol handlers that do not
support proxying will ignore the proxy parameter and make a
normal connection.

Parses the string representation of a

URL

into a

URL

object.

Compare two urls to see whether they refer to the same file,
i.e., having the same protocol, host, port, and path.

Deprecated.

Use setURL(URL, String, String, int, String, String, String,
String);

Sets the fields of the

URL

argument to the indicated values.

Converts a

URL

of a specific protocol to a

String

.

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

- URLStreamHandler

```java
public URLStreamHandler()
```

============ METHOD DETAIL ==========

- Method Detail

- openConnection

```java
protected abstract
URLConnection
openConnection​(
URL
u)
throws
IOException
```

Opens a connection to the object referenced by the

URL

argument.
This method should be overridden by a subclass.

If for the handler's protocol (such as HTTP or JAR), there
exists a public, specialized URLConnection subclass belonging
to one of the following packages or one of their subpackages:
java.lang, java.io, java.util, java.net, the connection
returned will be of that subclass. For example, for HTTP an
HttpURLConnection will be returned, and for JAR a
JarURLConnection will be returned.

**Parameters:** u

- the URL that this connects to.
**Returns:** a

URLConnection

object for the

URL

.
**Throws:** IOException

- if an I/O error occurs while opening the
connection.

- openConnection

```java
protected
URLConnection
openConnection​(
URL
u,

Proxy
p)
throws
IOException
```

Same as openConnection(URL), except that the connection will be
made through the specified proxy; Protocol handlers that do not
support proxying will ignore the proxy parameter and make a
normal connection.

Calling this method preempts the system's default

ProxySelector

settings.

**Parameters:** u

- the URL that this connects to.
**Parameters:** p

- the proxy through which the connection will be made.
If direct connection is desired, Proxy.NO_PROXY
should be specified.
**Returns:** a

URLConnection

object for the

URL

.
**Throws:** IOException

- if an I/O error occurs while opening the
connection.
**Throws:** IllegalArgumentException

- if either u or p is null,
or p has the wrong type.
**Throws:** UnsupportedOperationException

- if the subclass that
implements the protocol doesn't support this method.
**Since:** 1.5

- parseURL

```java
protected void parseURL​(
URL
u,

String
spec,
int start,
int limit)
```

Parses the string representation of a

URL

into a

URL

object.

If there is any inherited context, then it has already been
copied into the

URL

argument.

The

parseURL

method of

URLStreamHandler

parses the string representation as if it were an

http

specification. Most URL protocol families have a
similar parsing. A stream protocol handler for a protocol that has
a different syntax must override this routine.

**Parameters:** u

- the

URL

to receive the result of parsing
the spec.
**Parameters:** spec

- the

String

representing the URL that
must be parsed.
**Parameters:** start

- the character index at which to begin parsing. This is
just past the '

:

' (if there is one) that
specifies the determination of the protocol name.
**Parameters:** limit

- the character position to stop parsing at. This is the
end of the string or the position of the
"

#

" character, if present. All information
after the sharp sign indicates an anchor.

- getDefaultPort

```java
protected int getDefaultPort()
```

Returns the default port for a URL parsed by this handler. This method
is meant to be overidden by handlers with default port numbers.

**Returns:** the default port for a

URL

parsed by this handler.
**Since:** 1.3

- equals

```java
protected boolean equals​(
URL
u1,

URL
u2)
```

Provides the default equals calculation. May be overidden by handlers
for other protocols that have different requirements for equals().
This method requires that none of its arguments is null. This is
guaranteed by the fact that it is only called by java.net.URL class.

**Parameters:** u1

- a URL object
**Parameters:** u2

- a URL object
**Returns:** true

if the two urls are
considered equal, ie. they refer to the same
fragment in the same file.
**Since:** 1.3

- hashCode

```java
protected int hashCode​(
URL
u)
```

Provides the default hash calculation. May be overidden by handlers for
other protocols that have different requirements for hashCode
calculation.

**Parameters:** u

- a URL object
**Returns:** an

int

suitable for hash table indexing
**Since:** 1.3

- sameFile

```java
protected boolean sameFile​(
URL
u1,

URL
u2)
```

Compare two urls to see whether they refer to the same file,
i.e., having the same protocol, host, port, and path.
This method requires that none of its arguments is null. This is
guaranteed by the fact that it is only called indirectly
by java.net.URL class.

**Parameters:** u1

- a URL object
**Parameters:** u2

- a URL object
**Returns:** true if u1 and u2 refer to the same file
**Since:** 1.3

- getHostAddress

```java
protected
InetAddress
getHostAddress​(
URL
u)
```

Get the IP address of our host. An empty host field or a DNS failure
will result in a null return.

**Parameters:** u

- a URL object
**Returns:** an

InetAddress

representing the host
IP address.
**Since:** 1.3

- hostsEqual

```java
protected boolean hostsEqual​(
URL
u1,

URL
u2)
```

Compares the host components of two URLs.

**Parameters:** u1

- the URL of the first host to compare
**Parameters:** u2

- the URL of the second host to compare
**Returns:** true

if and only if they
are equal,

false

otherwise.
**Since:** 1.3

- toExternalForm

```java
protected
String
toExternalForm​(
URL
u)
```

Converts a

URL

of a specific protocol to a

String

.

**Parameters:** u

- the URL.
**Returns:** a string representation of the

URL

argument.

- setURL

```java
protected void setURL​(
URL
u,

String
protocol,

String
host,
int port,

String
authority,

String
userInfo,

String
path,

String
query,

String
ref)
```

Sets the fields of the

URL

argument to the indicated values.
Only classes derived from URLStreamHandler are able
to use this method to set the values of the URL fields.

**Parameters:** u

- the URL to modify.
**Parameters:** protocol

- the protocol name.
**Parameters:** host

- the remote host value for the URL.
**Parameters:** port

- the port on the remote machine.
**Parameters:** authority

- the authority part for the URL.
**Parameters:** userInfo

- the userInfo part of the URL.
**Parameters:** path

- the path component of the URL.
**Parameters:** query

- the query part for the URL.
**Parameters:** ref

- the reference.
**Throws:** SecurityException

- if the protocol handler of the URL is
different from this one
**Since:** 1.3

- setURL

```java
@Deprecated

protected void setURL​(
URL
u,

String
protocol,

String
host,
int port,

String
file,

String
ref)
```

Deprecated.

Use setURL(URL, String, String, int, String, String, String,
String);

Sets the fields of the

URL

argument to the indicated values.
Only classes derived from URLStreamHandler are able
to use this method to set the values of the URL fields.

**Parameters:** u

- the URL to modify.
**Parameters:** protocol

- the protocol name. This value is ignored since 1.2.
**Parameters:** host

- the remote host value for the URL.
**Parameters:** port

- the port on the remote machine.
**Parameters:** file

- the file.
**Parameters:** ref

- the reference.
**Throws:** SecurityException

- if the protocol handler of the URL is
different from this one

Constructor Detail

- URLStreamHandler

```java
public URLStreamHandler()
```

---

#### Constructor Detail

URLStreamHandler

```java
public URLStreamHandler()
```

---

#### URLStreamHandler

public URLStreamHandler()

Method Detail

- openConnection

```java
protected abstract
URLConnection
openConnection​(
URL
u)
throws
IOException
```

Opens a connection to the object referenced by the

URL

argument.
This method should be overridden by a subclass.

If for the handler's protocol (such as HTTP or JAR), there
exists a public, specialized URLConnection subclass belonging
to one of the following packages or one of their subpackages:
java.lang, java.io, java.util, java.net, the connection
returned will be of that subclass. For example, for HTTP an
HttpURLConnection will be returned, and for JAR a
JarURLConnection will be returned.

**Parameters:** u

- the URL that this connects to.
**Returns:** a

URLConnection

object for the

URL

.
**Throws:** IOException

- if an I/O error occurs while opening the
connection.

- openConnection

```java
protected
URLConnection
openConnection​(
URL
u,

Proxy
p)
throws
IOException
```

Same as openConnection(URL), except that the connection will be
made through the specified proxy; Protocol handlers that do not
support proxying will ignore the proxy parameter and make a
normal connection.

Calling this method preempts the system's default

ProxySelector

settings.

**Parameters:** u

- the URL that this connects to.
**Parameters:** p

- the proxy through which the connection will be made.
If direct connection is desired, Proxy.NO_PROXY
should be specified.
**Returns:** a

URLConnection

object for the

URL

.
**Throws:** IOException

- if an I/O error occurs while opening the
connection.
**Throws:** IllegalArgumentException

- if either u or p is null,
or p has the wrong type.
**Throws:** UnsupportedOperationException

- if the subclass that
implements the protocol doesn't support this method.
**Since:** 1.5

- parseURL

```java
protected void parseURL​(
URL
u,

String
spec,
int start,
int limit)
```

Parses the string representation of a

URL

into a

URL

object.

If there is any inherited context, then it has already been
copied into the

URL

argument.

The

parseURL

method of

URLStreamHandler

parses the string representation as if it were an

http

specification. Most URL protocol families have a
similar parsing. A stream protocol handler for a protocol that has
a different syntax must override this routine.

**Parameters:** u

- the

URL

to receive the result of parsing
the spec.
**Parameters:** spec

- the

String

representing the URL that
must be parsed.
**Parameters:** start

- the character index at which to begin parsing. This is
just past the '

:

' (if there is one) that
specifies the determination of the protocol name.
**Parameters:** limit

- the character position to stop parsing at. This is the
end of the string or the position of the
"

#

" character, if present. All information
after the sharp sign indicates an anchor.

- getDefaultPort

```java
protected int getDefaultPort()
```

Returns the default port for a URL parsed by this handler. This method
is meant to be overidden by handlers with default port numbers.

**Returns:** the default port for a

URL

parsed by this handler.
**Since:** 1.3

- equals

```java
protected boolean equals​(
URL
u1,

URL
u2)
```

Provides the default equals calculation. May be overidden by handlers
for other protocols that have different requirements for equals().
This method requires that none of its arguments is null. This is
guaranteed by the fact that it is only called by java.net.URL class.

**Parameters:** u1

- a URL object
**Parameters:** u2

- a URL object
**Returns:** true

if the two urls are
considered equal, ie. they refer to the same
fragment in the same file.
**Since:** 1.3

- hashCode

```java
protected int hashCode​(
URL
u)
```

Provides the default hash calculation. May be overidden by handlers for
other protocols that have different requirements for hashCode
calculation.

**Parameters:** u

- a URL object
**Returns:** an

int

suitable for hash table indexing
**Since:** 1.3

- sameFile

```java
protected boolean sameFile​(
URL
u1,

URL
u2)
```

Compare two urls to see whether they refer to the same file,
i.e., having the same protocol, host, port, and path.
This method requires that none of its arguments is null. This is
guaranteed by the fact that it is only called indirectly
by java.net.URL class.

**Parameters:** u1

- a URL object
**Parameters:** u2

- a URL object
**Returns:** true if u1 and u2 refer to the same file
**Since:** 1.3

- getHostAddress

```java
protected
InetAddress
getHostAddress​(
URL
u)
```

Get the IP address of our host. An empty host field or a DNS failure
will result in a null return.

**Parameters:** u

- a URL object
**Returns:** an

InetAddress

representing the host
IP address.
**Since:** 1.3

- hostsEqual

```java
protected boolean hostsEqual​(
URL
u1,

URL
u2)
```

Compares the host components of two URLs.

**Parameters:** u1

- the URL of the first host to compare
**Parameters:** u2

- the URL of the second host to compare
**Returns:** true

if and only if they
are equal,

false

otherwise.
**Since:** 1.3

- toExternalForm

```java
protected
String
toExternalForm​(
URL
u)
```

Converts a

URL

of a specific protocol to a

String

.

**Parameters:** u

- the URL.
**Returns:** a string representation of the

URL

argument.

- setURL

```java
protected void setURL​(
URL
u,

String
protocol,

String
host,
int port,

String
authority,

String
userInfo,

String
path,

String
query,

String
ref)
```

Sets the fields of the

URL

argument to the indicated values.
Only classes derived from URLStreamHandler are able
to use this method to set the values of the URL fields.

**Parameters:** u

- the URL to modify.
**Parameters:** protocol

- the protocol name.
**Parameters:** host

- the remote host value for the URL.
**Parameters:** port

- the port on the remote machine.
**Parameters:** authority

- the authority part for the URL.
**Parameters:** userInfo

- the userInfo part of the URL.
**Parameters:** path

- the path component of the URL.
**Parameters:** query

- the query part for the URL.
**Parameters:** ref

- the reference.
**Throws:** SecurityException

- if the protocol handler of the URL is
different from this one
**Since:** 1.3

- setURL

```java
@Deprecated

protected void setURL​(
URL
u,

String
protocol,

String
host,
int port,

String
file,

String
ref)
```

Deprecated.

Use setURL(URL, String, String, int, String, String, String,
String);

Sets the fields of the

URL

argument to the indicated values.
Only classes derived from URLStreamHandler are able
to use this method to set the values of the URL fields.

**Parameters:** u

- the URL to modify.
**Parameters:** protocol

- the protocol name. This value is ignored since 1.2.
**Parameters:** host

- the remote host value for the URL.
**Parameters:** port

- the port on the remote machine.
**Parameters:** file

- the file.
**Parameters:** ref

- the reference.
**Throws:** SecurityException

- if the protocol handler of the URL is
different from this one

---

#### Method Detail

openConnection

```java
protected abstract
URLConnection
openConnection​(
URL
u)
throws
IOException
```

Opens a connection to the object referenced by the

URL

argument.
This method should be overridden by a subclass.

If for the handler's protocol (such as HTTP or JAR), there
exists a public, specialized URLConnection subclass belonging
to one of the following packages or one of their subpackages:
java.lang, java.io, java.util, java.net, the connection
returned will be of that subclass. For example, for HTTP an
HttpURLConnection will be returned, and for JAR a
JarURLConnection will be returned.

**Parameters:** u

- the URL that this connects to.
**Returns:** a

URLConnection

object for the

URL

.
**Throws:** IOException

- if an I/O error occurs while opening the
connection.

---

#### openConnection

protected abstract

URLConnection

openConnection​(

URL

u)
throws

IOException

Opens a connection to the object referenced by the

URL

argument.
This method should be overridden by a subclass.

If for the handler's protocol (such as HTTP or JAR), there
exists a public, specialized URLConnection subclass belonging
to one of the following packages or one of their subpackages:
java.lang, java.io, java.util, java.net, the connection
returned will be of that subclass. For example, for HTTP an
HttpURLConnection will be returned, and for JAR a
JarURLConnection will be returned.

If for the handler's protocol (such as HTTP or JAR), there
exists a public, specialized URLConnection subclass belonging
to one of the following packages or one of their subpackages:
java.lang, java.io, java.util, java.net, the connection
returned will be of that subclass. For example, for HTTP an
HttpURLConnection will be returned, and for JAR a
JarURLConnection will be returned.

openConnection

```java
protected
URLConnection
openConnection​(
URL
u,

Proxy
p)
throws
IOException
```

Same as openConnection(URL), except that the connection will be
made through the specified proxy; Protocol handlers that do not
support proxying will ignore the proxy parameter and make a
normal connection.

Calling this method preempts the system's default

ProxySelector

settings.

**Parameters:** u

- the URL that this connects to.
**Parameters:** p

- the proxy through which the connection will be made.
If direct connection is desired, Proxy.NO_PROXY
should be specified.
**Returns:** a

URLConnection

object for the

URL

.
**Throws:** IOException

- if an I/O error occurs while opening the
connection.
**Throws:** IllegalArgumentException

- if either u or p is null,
or p has the wrong type.
**Throws:** UnsupportedOperationException

- if the subclass that
implements the protocol doesn't support this method.
**Since:** 1.5

---

#### openConnection

protected

URLConnection

openConnection​(

URL

u,

Proxy

p)
throws

IOException

Same as openConnection(URL), except that the connection will be
made through the specified proxy; Protocol handlers that do not
support proxying will ignore the proxy parameter and make a
normal connection.

Calling this method preempts the system's default

ProxySelector

settings.

parseURL

```java
protected void parseURL​(
URL
u,

String
spec,
int start,
int limit)
```

Parses the string representation of a

URL

into a

URL

object.

If there is any inherited context, then it has already been
copied into the

URL

argument.

The

parseURL

method of

URLStreamHandler

parses the string representation as if it were an

http

specification. Most URL protocol families have a
similar parsing. A stream protocol handler for a protocol that has
a different syntax must override this routine.

**Parameters:** u

- the

URL

to receive the result of parsing
the spec.
**Parameters:** spec

- the

String

representing the URL that
must be parsed.
**Parameters:** start

- the character index at which to begin parsing. This is
just past the '

:

' (if there is one) that
specifies the determination of the protocol name.
**Parameters:** limit

- the character position to stop parsing at. This is the
end of the string or the position of the
"

#

" character, if present. All information
after the sharp sign indicates an anchor.

---

#### parseURL

protected void parseURL​(

URL

u,

String

spec,
int start,
int limit)

Parses the string representation of a

URL

into a

URL

object.

If there is any inherited context, then it has already been
copied into the

URL

argument.

The

parseURL

method of

URLStreamHandler

parses the string representation as if it were an

http

specification. Most URL protocol families have a
similar parsing. A stream protocol handler for a protocol that has
a different syntax must override this routine.

If there is any inherited context, then it has already been
copied into the

URL

argument.

The

parseURL

method of

URLStreamHandler

parses the string representation as if it were an

http

specification. Most URL protocol families have a
similar parsing. A stream protocol handler for a protocol that has
a different syntax must override this routine.

The

parseURL

method of

URLStreamHandler

parses the string representation as if it were an

http

specification. Most URL protocol families have a
similar parsing. A stream protocol handler for a protocol that has
a different syntax must override this routine.

getDefaultPort

```java
protected int getDefaultPort()
```

Returns the default port for a URL parsed by this handler. This method
is meant to be overidden by handlers with default port numbers.

**Returns:** the default port for a

URL

parsed by this handler.
**Since:** 1.3

---

#### getDefaultPort

protected int getDefaultPort()

Returns the default port for a URL parsed by this handler. This method
is meant to be overidden by handlers with default port numbers.

equals

```java
protected boolean equals​(
URL
u1,

URL
u2)
```

Provides the default equals calculation. May be overidden by handlers
for other protocols that have different requirements for equals().
This method requires that none of its arguments is null. This is
guaranteed by the fact that it is only called by java.net.URL class.

**Parameters:** u1

- a URL object
**Parameters:** u2

- a URL object
**Returns:** true

if the two urls are
considered equal, ie. they refer to the same
fragment in the same file.
**Since:** 1.3

---

#### equals

protected boolean equals​(

URL

u1,

URL

u2)

Provides the default equals calculation. May be overidden by handlers
for other protocols that have different requirements for equals().
This method requires that none of its arguments is null. This is
guaranteed by the fact that it is only called by java.net.URL class.

hashCode

```java
protected int hashCode​(
URL
u)
```

Provides the default hash calculation. May be overidden by handlers for
other protocols that have different requirements for hashCode
calculation.

**Parameters:** u

- a URL object
**Returns:** an

int

suitable for hash table indexing
**Since:** 1.3

---

#### hashCode

protected int hashCode​(

URL

u)

Provides the default hash calculation. May be overidden by handlers for
other protocols that have different requirements for hashCode
calculation.

sameFile

```java
protected boolean sameFile​(
URL
u1,

URL
u2)
```

Compare two urls to see whether they refer to the same file,
i.e., having the same protocol, host, port, and path.
This method requires that none of its arguments is null. This is
guaranteed by the fact that it is only called indirectly
by java.net.URL class.

**Parameters:** u1

- a URL object
**Parameters:** u2

- a URL object
**Returns:** true if u1 and u2 refer to the same file
**Since:** 1.3

---

#### sameFile

protected boolean sameFile​(

URL

u1,

URL

u2)

Compare two urls to see whether they refer to the same file,
i.e., having the same protocol, host, port, and path.
This method requires that none of its arguments is null. This is
guaranteed by the fact that it is only called indirectly
by java.net.URL class.

getHostAddress

```java
protected
InetAddress
getHostAddress​(
URL
u)
```

Get the IP address of our host. An empty host field or a DNS failure
will result in a null return.

**Parameters:** u

- a URL object
**Returns:** an

InetAddress

representing the host
IP address.
**Since:** 1.3

---

#### getHostAddress

protected

InetAddress

getHostAddress​(

URL

u)

Get the IP address of our host. An empty host field or a DNS failure
will result in a null return.

hostsEqual

```java
protected boolean hostsEqual​(
URL
u1,

URL
u2)
```

Compares the host components of two URLs.

**Parameters:** u1

- the URL of the first host to compare
**Parameters:** u2

- the URL of the second host to compare
**Returns:** true

if and only if they
are equal,

false

otherwise.
**Since:** 1.3

---

#### hostsEqual

protected boolean hostsEqual​(

URL

u1,

URL

u2)

Compares the host components of two URLs.

toExternalForm

```java
protected
String
toExternalForm​(
URL
u)
```

Converts a

URL

of a specific protocol to a

String

.

**Parameters:** u

- the URL.
**Returns:** a string representation of the

URL

argument.

---

#### toExternalForm

protected

String

toExternalForm​(

URL

u)

Converts a

URL

of a specific protocol to a

String

.

setURL

```java
protected void setURL​(
URL
u,

String
protocol,

String
host,
int port,

String
authority,

String
userInfo,

String
path,

String
query,

String
ref)
```

Sets the fields of the

URL

argument to the indicated values.
Only classes derived from URLStreamHandler are able
to use this method to set the values of the URL fields.

**Parameters:** u

- the URL to modify.
**Parameters:** protocol

- the protocol name.
**Parameters:** host

- the remote host value for the URL.
**Parameters:** port

- the port on the remote machine.
**Parameters:** authority

- the authority part for the URL.
**Parameters:** userInfo

- the userInfo part of the URL.
**Parameters:** path

- the path component of the URL.
**Parameters:** query

- the query part for the URL.
**Parameters:** ref

- the reference.
**Throws:** SecurityException

- if the protocol handler of the URL is
different from this one
**Since:** 1.3

---

#### setURL

protected void setURL​(

URL

u,

String

protocol,

String

host,
int port,

String

authority,

String

userInfo,

String

path,

String

query,

String

ref)

Sets the fields of the

URL

argument to the indicated values.
Only classes derived from URLStreamHandler are able
to use this method to set the values of the URL fields.

setURL

```java
@Deprecated

protected void setURL​(
URL
u,

String
protocol,

String
host,
int port,

String
file,

String
ref)
```

Deprecated.

Use setURL(URL, String, String, int, String, String, String,
String);

Sets the fields of the

URL

argument to the indicated values.
Only classes derived from URLStreamHandler are able
to use this method to set the values of the URL fields.

**Parameters:** u

- the URL to modify.
**Parameters:** protocol

- the protocol name. This value is ignored since 1.2.
**Parameters:** host

- the remote host value for the URL.
**Parameters:** port

- the port on the remote machine.
**Parameters:** file

- the file.
**Parameters:** ref

- the reference.
**Throws:** SecurityException

- if the protocol handler of the URL is
different from this one

---

#### setURL

@Deprecated

protected void setURL​(

URL

u,

String

protocol,

String

host,
int port,

String

file,

String

ref)

Sets the fields of the

URL

argument to the indicated values.
Only classes derived from URLStreamHandler are able
to use this method to set the values of the URL fields.

---

