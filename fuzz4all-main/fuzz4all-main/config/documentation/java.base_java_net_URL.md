# Class URL

**Source:** `java.base\java\net\URL.html`

### Class Description

```java
public final class
URL

extends
Object

implements
Serializable
```

Class

URL

represents a Uniform Resource
Locator, a pointer to a "resource" on the World
Wide Web. A resource can be something as simple as a file or a
directory, or it can be a reference to a more complicated object,
such as a query to a database or to a search engine. More
information on the types of URLs and their formats can be found at:

Types of URL

In general, a URL can be broken into several parts. Consider the
following example:

```java
http://www.example.com/docs/resource1.html
```

The URL above indicates that the protocol to use is

http

(HyperText Transfer Protocol) and that the
information resides on a host machine named

www.example.com

. The information on that host
machine is named

/docs/resource1.html

. The exact
meaning of this name on the host machine is both protocol
dependent and host dependent. The information normally resides in
a file, but it could be generated on the fly. This component of
the URL is called the

path

component.

A URL can optionally specify a "port", which is the
port number to which the TCP connection is made on the remote host
machine. If the port is not specified, the default port for
the protocol is used instead. For example, the default port for

http

is

80

. An alternative port could be
specified as:

```java
http://www.example.com:1080/docs/resource1.html
```

The syntax of

URL

is defined by

RFC 2396: Uniform
Resource Identifiers (URI): Generic Syntax

, amended by

RFC 2732: Format for
Literal IPv6 Addresses in URLs

. The Literal IPv6 address format
also supports scope_ids. The syntax and usage of scope_ids is described

here

.

A URL may have appended to it a "fragment", also known
as a "ref" or a "reference". The fragment is indicated by the sharp
sign character "#" followed by more characters. For example,

```java
http://java.sun.com/index.html#chapter1
```

This fragment is not technically part of the URL. Rather, it
indicates that after the specified resource is retrieved, the
application is specifically interested in that part of the
document that has the tag

chapter1

attached to it. The
meaning of a tag is resource specific.

An application can also specify a "relative URL",
which contains only enough information to reach the resource
relative to another URL. Relative URLs are frequently used within
HTML pages. For example, if the contents of the URL:

```java
http://java.sun.com/index.html
```

contained within it the relative URL:

```java
FAQ.html
```

it would be a shorthand for:

```java
http://java.sun.com/FAQ.html
```

The relative URL need not specify all the components of a URL. If
the protocol, host name, or port number is missing, the value is
inherited from the fully specified URL. The file component must be
specified. The optional fragment is not inherited.

The URL class does not itself encode or decode any URL components
according to the escaping mechanism defined in RFC2396. It is the
responsibility of the caller to encode any fields, which need to be
escaped prior to calling URL, and also to decode any escaped fields,
that are returned from URL. Furthermore, because URL has no knowledge
of URL escaping, it does not recognise equivalence between the encoded
or decoded form of the same URL. For example, the two URLs:

```java
http://foo.com/hello world/ and http://foo.com/hello%20world
```

would be considered not equal to each other.

Note, the

URI

class does perform escaping of its
component fields in certain circumstances. The recommended way
to manage the encoding and decoding of URLs is to use

URI

,
and to convert between these two classes using

toURI()

and

URI.toURL()

.

The

URLEncoder

and

URLDecoder

classes can also be
used, but only for HTML form encoding, which is not the same
as the encoding scheme defined in RFC2396.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public URL​(
String
protocol,

String
host,
int port,

String
file)
throws
MalformedURLException

Creates a

URL

object from the specified

protocol

,

host

,

port

number, and

file

.

host

can be expressed as a host name or a literal
IP address. If IPv6 literal address is used, it should be
enclosed in square brackets (

'['

and

']'

), as
specified by

RFC 2732

;
However, the literal IPv6 address format defined in

RFC 2373: IP
Version 6 Addressing Architecture

is also accepted.

Specifying a

port

number of

-1

indicates that the URL should use the default port for the
protocol.

If this is the first URL object being created with the specified
protocol, a

stream protocol handler

object, an instance of
class

URLStreamHandler

, is created for that protocol:

- If the application has previously set up an instance of

URLStreamHandlerFactory

as the stream handler factory,
then the

createURLStreamHandler

method of that instance
is called with the protocol string as an argument to create the
stream protocol handler.

If no

URLStreamHandlerFactory

has yet been set up,
or if the factory's

createURLStreamHandler

method
returns

null

, then the

ServiceLoader

mechanism is used to locate

URLStreamHandlerProvider

implementations using the system class
loader. The order that providers are located is implementation
specific, and an implementation is free to cache the located
providers. A

ServiceConfigurationError

,

Error

or

RuntimeException

thrown from the

createURLStreamHandler

, if encountered, will
be propagated to the calling thread. The

createURLStreamHandler

method of each provider, if instantiated, is
invoked, with the protocol string, until a provider returns non-null,
or all providers have been exhausted.

If the previous step fails to find a protocol handler, the
constructor reads the value of the system property:

java.protocol.handler.pkgs

If the value of that system property is not

null

,
it is interpreted as a list of packages separated by a vertical
slash character '

|

'. The constructor tries to load
the class named:

<package>.<protocol>.Handler

where

<package>

is replaced by the name of the package
and

<protocol>

is replaced by the name of the protocol.
If this class does not exist, or if the class exists but it is not
a subclass of

URLStreamHandler

, then the next package
in the list is tried.

If the previous step fails to find a protocol handler, then the
constructor tries to load a built-in protocol handler.
If this class does not exist, or if the class exists but it is not a
subclass of

URLStreamHandler

, then a

MalformedURLException

is thrown.

Protocol handlers for the following protocols are guaranteed
to exist on the search path :-

```java
http, https, file, and jar
```

Protocol handlers for additional protocols may also be available.
Some protocol handlers, for example those used for loading platform
classes or classes on the class path, may not be overridden. The details
of such restrictions, and when those restrictions apply (during
initialization of the runtime for example), are implementation specific
and therefore not specified

No validation of the inputs is performed by this constructor.

**Parameters:**
- protocol

- the name of the protocol to use.
- host

- the name of the host.
- port

- the port number on the host.
- file

- the file on the host

**Throws:**
- MalformedURLException

- if an unknown protocol or the port
is a negative number other than -1

**See Also:**
- System.getProperty(java.lang.String)

,

setURLStreamHandlerFactory(
java.net.URLStreamHandlerFactory)

,

URLStreamHandler

,

URLStreamHandlerFactory.createURLStreamHandler(
java.lang.String)

---

#### public URL​(
String
protocol,

String
host,

String
file)
throws
MalformedURLException

Creates a URL from the specified

protocol

name,

host

name, and

file

name. The
default port for the specified protocol is used.

This constructor is equivalent to the four-argument
constructor with the only difference of using the
default port for the specified protocol.

No validation of the inputs is performed by this constructor.

**Parameters:**
- protocol

- the name of the protocol to use.
- host

- the name of the host.
- file

- the file on the host.

**Throws:**
- MalformedURLException

- if an unknown protocol is specified.

**See Also:**
- URL(java.lang.String, java.lang.String,
int, java.lang.String)

---

#### public URL​(
String
protocol,

String
host,
int port,

String
file,

URLStreamHandler
handler)
throws
MalformedURLException

Creates a

URL

object from the specified

protocol

,

host

,

port

number,

file

, and

handler

. Specifying
a

port

number of

-1

indicates that
the URL should use the default port for the protocol. Specifying
a

handler

of

null

indicates that the URL
should use a default stream handler for the protocol, as outlined
for:
java.net.URL#URL(java.lang.String, java.lang.String, int,
java.lang.String)

If the handler is not null and there is a security manager,
the security manager's

checkPermission

method is called with a

NetPermission("specifyStreamHandler")

permission.
This may result in a SecurityException.

No validation of the inputs is performed by this constructor.

**Parameters:**
- protocol

- the name of the protocol to use.
- host

- the name of the host.
- port

- the port number on the host.
- file

- the file on the host
- handler

- the stream handler for the URL.

**Throws:**
- MalformedURLException

- if an unknown protocol or the port
is a negative number other than -1
- SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
specifying a stream handler explicitly.

**See Also:**
- System.getProperty(java.lang.String)

,

setURLStreamHandlerFactory(
java.net.URLStreamHandlerFactory)

,

URLStreamHandler

,

URLStreamHandlerFactory.createURLStreamHandler(
java.lang.String)

,

SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

---

#### public URL​(
String
spec)
throws
MalformedURLException

Creates a

URL

object from the

String

representation.

This constructor is equivalent to a call to the two-argument
constructor with a

null

first argument.

**Parameters:**
- spec

- the

String

to parse as a URL.

**Throws:**
- MalformedURLException

- if no protocol is specified, or an
unknown protocol is found, or

spec

is

null

,
or the parsed URL fails to comply with the specific syntax
of the associated protocol.

**See Also:**
- URL(java.net.URL, java.lang.String)

---

#### public URL​(
URL
context,

String
spec)
throws
MalformedURLException

Creates a URL by parsing the given spec within a specified context.

The new URL is created from the given context URL and the spec
argument as described in
RFC2396 "Uniform Resource Identifiers : Generic * Syntax" :

```java
<scheme>://<authority><path>?<query>#<fragment>
```

The reference is parsed into the scheme, authority, path, query and
fragment parts. If the path component is empty and the scheme,
authority, and query components are undefined, then the new URL is a
reference to the current document. Otherwise, the fragment and query
parts present in the spec are used in the new URL.

If the scheme component is defined in the given spec and does not match
the scheme of the context, then the new URL is created as an absolute
URL based on the spec alone. Otherwise the scheme component is inherited
from the context URL.

If the authority component is present in the spec then the spec is
treated as absolute and the spec authority and path will replace the
context authority and path. If the authority component is absent in the
spec then the authority of the new URL will be inherited from the
context.

If the spec's path component begins with a slash character
"/" then the
path is treated as absolute and the spec path replaces the context path.

Otherwise, the path is treated as a relative path and is appended to the
context path, as described in RFC2396. Also, in this case,
the path is canonicalized through the removal of directory
changes made by occurrences of ".." and ".".

For a more detailed description of URL parsing, refer to RFC2396.

**Parameters:**
- context

- the context in which to parse the specification.
- spec

- the

String

to parse as a URL.

**Throws:**
- MalformedURLException

- if no protocol is specified, or an
unknown protocol is found, or

spec

is

null

,
or the parsed URL fails to comply with the specific syntax
of the associated protocol.

**See Also:**
- URL(java.lang.String, java.lang.String,
int, java.lang.String)

,

URLStreamHandler

,

URLStreamHandler.parseURL(java.net.URL,
java.lang.String, int, int)

---

#### public URL​(
URL
context,

String
spec,

URLStreamHandler
handler)
throws
MalformedURLException

Creates a URL by parsing the given spec with the specified handler
within a specified context. If the handler is null, the parsing
occurs as with the two argument constructor.

**Parameters:**
- context

- the context in which to parse the specification.
- spec

- the

String

to parse as a URL.
- handler

- the stream handler for the URL.

**Throws:**
- MalformedURLException

- if no protocol is specified, or an
unknown protocol is found, or

spec

is

null

,
or the parsed URL fails to comply with the specific syntax
of the associated protocol.
- SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
specifying a stream handler.

**See Also:**
- URL(java.lang.String, java.lang.String,
int, java.lang.String)

,

URLStreamHandler

,

URLStreamHandler.parseURL(java.net.URL,
java.lang.String, int, int)

---

### Method Details

#### public
String
getQuery()

Gets the query part of this

URL

.

**Returns:**
- the query part of this

URL

,
or

null

if one does not exist

**Since:**
- 1.3

---

#### public
String
getPath()

Gets the path part of this

URL

.

**Returns:**
- the path part of this

URL

, or an
empty string if one does not exist

**Since:**
- 1.3

---

#### public
String
getUserInfo()

Gets the userInfo part of this

URL

.

**Returns:**
- the userInfo part of this

URL

, or

null

if one does not exist

**Since:**
- 1.3

---

#### public
String
getAuthority()

Gets the authority part of this

URL

.

**Returns:**
- the authority part of this

URL

**Since:**
- 1.3

---

#### public int getPort()

Gets the port number of this

URL

.

**Returns:**
- the port number, or -1 if the port is not set

---

#### public int getDefaultPort()

Gets the default port number of the protocol associated
with this

URL

. If the URL scheme or the URLStreamHandler
for the URL do not define a default port number,
then -1 is returned.

**Returns:**
- the port number

**Since:**
- 1.4

---

#### public
String
getProtocol()

Gets the protocol name of this

URL

.

**Returns:**
- the protocol of this

URL

.

---

#### public
String
getHost()

Gets the host name of this

URL

, if applicable.
The format of the host conforms to RFC 2732, i.e. for a
literal IPv6 address, this method will return the IPv6 address
enclosed in square brackets (

'['

and

']'

).

**Returns:**
- the host name of this

URL

.

---

#### public
String
getFile()

Gets the file name of this

URL

.
The returned file portion will be
the same as

getPath()

, plus the concatenation of
the value of

getQuery()

, if any. If there is
no query portion, this method and

getPath()

will
return identical results.

**Returns:**
- the file name of this

URL

,
or an empty string if one does not exist

---

#### public
String
getRef()

Gets the anchor (also known as the "reference") of this

URL

.

**Returns:**
- the anchor (also known as the "reference") of this

URL

, or

null

if one does not exist

---

#### public boolean equals​(
Object
obj)

Compares this URL for equality with another object.

If the given object is not a URL then this method immediately returns

false

.

Two URL objects are equal if they have the same protocol, reference
equivalent hosts, have the same port number on the host, and the same
file and fragment of the file.

Two hosts are considered equivalent if both host names can be resolved
into the same IP addresses; else if either host name can't be
resolved, the host names must be equal without regard to case; or both
host names equal to null.

Since hosts comparison requires name resolution, this operation is a
blocking operation.

Note: The defined behavior for

equals

is known to
be inconsistent with virtual hosting in HTTP.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the URL to compare against.

**Returns:**
- true

if the objects are the same;

false

otherwise.

**See Also:**
- Object.hashCode()

,

HashMap

---

#### public int hashCode()

Creates an integer suitable for hash table indexing.

The hash code is based upon all the URL components relevant for URL
comparison. As such, this operation is a blocking operation.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- a hash code for this

URL

.

**See Also:**
- Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### public boolean sameFile​(
URL
other)

Compares two URLs, excluding the fragment component.

Returns

true

if this

URL

and the

other

argument are equal without taking the
fragment component into consideration.

**Parameters:**
- other

- the

URL

to compare against.

**Returns:**
- true

if they reference the same remote object;

false

otherwise.

---

#### public
String
toString()

Constructs a string representation of this

URL

. The
string is created by calling the

toExternalForm

method of the stream protocol handler for this object.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string representation of this object.

**See Also:**
- URL(java.lang.String, java.lang.String, int,
java.lang.String)

,

URLStreamHandler.toExternalForm(java.net.URL)

---

#### public
String
toExternalForm()

Constructs a string representation of this

URL

. The
string is created by calling the

toExternalForm

method of the stream protocol handler for this object.

**Returns:**
- a string representation of this object.

**See Also:**
- URL(java.lang.String, java.lang.String,
int, java.lang.String)

,

URLStreamHandler.toExternalForm(java.net.URL)

---

#### public
URI
toURI()
throws
URISyntaxException

Returns a

URI

equivalent to this URL.
This method functions in the same way as

new URI (this.toString())

.

Note, any URL instance that complies with RFC 2396 can be converted
to a URI. However, some URLs that are not strictly in compliance
can not be converted to a URI.

**Returns:**
- a URI instance equivalent to this URL.

**Throws:**
- URISyntaxException

- if this URL is not formatted strictly according to
to RFC2396 and cannot be converted to a URI.

**Since:**
- 1.5

---

#### public
URLConnection
openConnection()
throws
IOException

Returns a

URLConnection

instance that
represents a connection to the remote object referred to by the

URL

.

A new instance of

URLConnection

is
created every time when invoking the

URLStreamHandler.openConnection(URL)

method of the protocol handler for
this URL.

It should be noted that a URLConnection instance does not establish
the actual network connection on creation. This will happen only when
calling

URLConnection.connect()

.

If for the URL's protocol (such as HTTP or JAR), there
exists a public, specialized URLConnection subclass belonging
to one of the following packages or one of their subpackages:
java.lang, java.io, java.util, java.net, the connection
returned will be of that subclass. For example, for HTTP an
HttpURLConnection will be returned, and for JAR a
JarURLConnection will be returned.

**Returns:**
- a

URLConnection

linking
to the URL.

**Throws:**
- IOException

- if an I/O exception occurs.

**See Also:**
- URL(java.lang.String, java.lang.String,
int, java.lang.String)

---

#### public
URLConnection
openConnection​(
Proxy
proxy)
throws
IOException

Same as

openConnection()

, except that the connection will be
made through the specified proxy; Protocol handlers that do not
support proxing will ignore the proxy parameter and make a
normal connection.

Invoking this method preempts the system's default

ProxySelector

settings.

**Parameters:**
- proxy

- the Proxy through which this connection
will be made. If direct connection is desired,
Proxy.NO_PROXY should be specified.

**Returns:**
- a

URLConnection

to the URL.

**Throws:**
- IOException

- if an I/O exception occurs.
- SecurityException

- if a security manager is present
and the caller doesn't have permission to connect
to the proxy.
- IllegalArgumentException

- will be thrown if proxy is null,
or proxy has the wrong type
- UnsupportedOperationException

- if the subclass that
implements the protocol handler doesn't support
this method.

**See Also:**
- URL(java.lang.String, java.lang.String,
int, java.lang.String)

,

URLConnection

,

URLStreamHandler.openConnection(java.net.URL,
java.net.Proxy)

**Since:**
- 1.5

---

#### public final
InputStream
openStream()
throws
IOException

Opens a connection to this

URL

and returns an

InputStream

for reading from that connection. This
method is a shorthand for:

```java
openConnection().getInputStream()
```

**Returns:**
- an input stream for reading from the URL connection.

**Throws:**
- IOException

- if an I/O exception occurs.

**See Also:**
- openConnection()

,

URLConnection.getInputStream()

---

#### public final
Object
getContent()
throws
IOException

Gets the contents of this URL. This method is a shorthand for:

```java
openConnection().getContent()
```

**Returns:**
- the contents of this URL.

**Throws:**
- IOException

- if an I/O exception occurs.

**See Also:**
- URLConnection.getContent()

---

#### public final
Object
getContent​(
Class
<?>[] classes)
throws
IOException

Gets the contents of this URL. This method is a shorthand for:

```java
openConnection().getContent(classes)
```

**Parameters:**
- classes

- an array of Java types

**Returns:**
- the content object of this URL that is the first match of
the types specified in the classes array.
null if none of the requested types are supported.

**Throws:**
- IOException

- if an I/O exception occurs.

**See Also:**
- URLConnection.getContent(Class[])

**Since:**
- 1.3

---

#### public static void setURLStreamHandlerFactory​(
URLStreamHandlerFactory
fac)

Sets an application's

URLStreamHandlerFactory

.
This method can be called at most once in a given Java Virtual
Machine.

The

URLStreamHandlerFactory

instance is used to
construct a stream protocol handler from a protocol name.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:**
- fac

- the desired factory.

**Throws:**
- Error

- if the application has already set a factory.
- SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't allow
the operation.

**See Also:**
- URL(java.lang.String, java.lang.String,
int, java.lang.String)

,

URLStreamHandlerFactory

,

SecurityManager.checkSetFactory()

---

### Additional Sections

#### Class URL

java.lang.Object

- java.net.URL

java.net.URL

**All Implemented Interfaces:** Serializable

```java
public final class
URL

extends
Object

implements
Serializable
```

Class

URL

represents a Uniform Resource
Locator, a pointer to a "resource" on the World
Wide Web. A resource can be something as simple as a file or a
directory, or it can be a reference to a more complicated object,
such as a query to a database or to a search engine. More
information on the types of URLs and their formats can be found at:

Types of URL

In general, a URL can be broken into several parts. Consider the
following example:

```java
http://www.example.com/docs/resource1.html
```

The URL above indicates that the protocol to use is

http

(HyperText Transfer Protocol) and that the
information resides on a host machine named

www.example.com

. The information on that host
machine is named

/docs/resource1.html

. The exact
meaning of this name on the host machine is both protocol
dependent and host dependent. The information normally resides in
a file, but it could be generated on the fly. This component of
the URL is called the

path

component.

A URL can optionally specify a "port", which is the
port number to which the TCP connection is made on the remote host
machine. If the port is not specified, the default port for
the protocol is used instead. For example, the default port for

http

is

80

. An alternative port could be
specified as:

```java
http://www.example.com:1080/docs/resource1.html
```

The syntax of

URL

is defined by

RFC 2396: Uniform
Resource Identifiers (URI): Generic Syntax

, amended by

RFC 2732: Format for
Literal IPv6 Addresses in URLs

. The Literal IPv6 address format
also supports scope_ids. The syntax and usage of scope_ids is described

here

.

A URL may have appended to it a "fragment", also known
as a "ref" or a "reference". The fragment is indicated by the sharp
sign character "#" followed by more characters. For example,

```java
http://java.sun.com/index.html#chapter1
```

This fragment is not technically part of the URL. Rather, it
indicates that after the specified resource is retrieved, the
application is specifically interested in that part of the
document that has the tag

chapter1

attached to it. The
meaning of a tag is resource specific.

An application can also specify a "relative URL",
which contains only enough information to reach the resource
relative to another URL. Relative URLs are frequently used within
HTML pages. For example, if the contents of the URL:

```java
http://java.sun.com/index.html
```

contained within it the relative URL:

```java
FAQ.html
```

it would be a shorthand for:

```java
http://java.sun.com/FAQ.html
```

The relative URL need not specify all the components of a URL. If
the protocol, host name, or port number is missing, the value is
inherited from the fully specified URL. The file component must be
specified. The optional fragment is not inherited.

The URL class does not itself encode or decode any URL components
according to the escaping mechanism defined in RFC2396. It is the
responsibility of the caller to encode any fields, which need to be
escaped prior to calling URL, and also to decode any escaped fields,
that are returned from URL. Furthermore, because URL has no knowledge
of URL escaping, it does not recognise equivalence between the encoded
or decoded form of the same URL. For example, the two URLs:

```java
http://foo.com/hello world/ and http://foo.com/hello%20world
```

would be considered not equal to each other.

Note, the

URI

class does perform escaping of its
component fields in certain circumstances. The recommended way
to manage the encoding and decoding of URLs is to use

URI

,
and to convert between these two classes using

toURI()

and

URI.toURL()

.

The

URLEncoder

and

URLDecoder

classes can also be
used, but only for HTML form encoding, which is not the same
as the encoding scheme defined in RFC2396.

**Since:** 1.0
**See Also:** Serialized Form

public final class

URL

extends

Object

implements

Serializable

Class

URL

represents a Uniform Resource
Locator, a pointer to a "resource" on the World
Wide Web. A resource can be something as simple as a file or a
directory, or it can be a reference to a more complicated object,
such as a query to a database or to a search engine. More
information on the types of URLs and their formats can be found at:

Types of URL

In general, a URL can be broken into several parts. Consider the
following example:

```java
http://www.example.com/docs/resource1.html
```

The URL above indicates that the protocol to use is

http

(HyperText Transfer Protocol) and that the
information resides on a host machine named

www.example.com

. The information on that host
machine is named

/docs/resource1.html

. The exact
meaning of this name on the host machine is both protocol
dependent and host dependent. The information normally resides in
a file, but it could be generated on the fly. This component of
the URL is called the

path

component.

A URL can optionally specify a "port", which is the
port number to which the TCP connection is made on the remote host
machine. If the port is not specified, the default port for
the protocol is used instead. For example, the default port for

http

is

80

. An alternative port could be
specified as:

```java
http://www.example.com:1080/docs/resource1.html
```

The syntax of

URL

is defined by

RFC 2396: Uniform
Resource Identifiers (URI): Generic Syntax

, amended by

RFC 2732: Format for
Literal IPv6 Addresses in URLs

. The Literal IPv6 address format
also supports scope_ids. The syntax and usage of scope_ids is described

here

.

A URL may have appended to it a "fragment", also known
as a "ref" or a "reference". The fragment is indicated by the sharp
sign character "#" followed by more characters. For example,

```java
http://java.sun.com/index.html#chapter1
```

This fragment is not technically part of the URL. Rather, it
indicates that after the specified resource is retrieved, the
application is specifically interested in that part of the
document that has the tag

chapter1

attached to it. The
meaning of a tag is resource specific.

An application can also specify a "relative URL",
which contains only enough information to reach the resource
relative to another URL. Relative URLs are frequently used within
HTML pages. For example, if the contents of the URL:

```java
http://java.sun.com/index.html
```

contained within it the relative URL:

```java
FAQ.html
```

it would be a shorthand for:

```java
http://java.sun.com/FAQ.html
```

The relative URL need not specify all the components of a URL. If
the protocol, host name, or port number is missing, the value is
inherited from the fully specified URL. The file component must be
specified. The optional fragment is not inherited.

The URL class does not itself encode or decode any URL components
according to the escaping mechanism defined in RFC2396. It is the
responsibility of the caller to encode any fields, which need to be
escaped prior to calling URL, and also to decode any escaped fields,
that are returned from URL. Furthermore, because URL has no knowledge
of URL escaping, it does not recognise equivalence between the encoded
or decoded form of the same URL. For example, the two URLs:

```java
http://foo.com/hello world/ and http://foo.com/hello%20world
```

would be considered not equal to each other.

Note, the

URI

class does perform escaping of its
component fields in certain circumstances. The recommended way
to manage the encoding and decoding of URLs is to use

URI

,
and to convert between these two classes using

toURI()

and

URI.toURL()

.

The

URLEncoder

and

URLDecoder

classes can also be
used, but only for HTML form encoding, which is not the same
as the encoding scheme defined in RFC2396.

In general, a URL can be broken into several parts. Consider the
following example:

```java
http://www.example.com/docs/resource1.html
```

The URL above indicates that the protocol to use is

http

(HyperText Transfer Protocol) and that the
information resides on a host machine named

www.example.com

. The information on that host
machine is named

/docs/resource1.html

. The exact
meaning of this name on the host machine is both protocol
dependent and host dependent. The information normally resides in
a file, but it could be generated on the fly. This component of
the URL is called the

path

component.

A URL can optionally specify a "port", which is the
port number to which the TCP connection is made on the remote host
machine. If the port is not specified, the default port for
the protocol is used instead. For example, the default port for

http

is

80

. An alternative port could be
specified as:

```java
http://www.example.com:1080/docs/resource1.html
```

The syntax of

URL

is defined by

RFC 2396: Uniform
Resource Identifiers (URI): Generic Syntax

, amended by

RFC 2732: Format for
Literal IPv6 Addresses in URLs

. The Literal IPv6 address format
also supports scope_ids. The syntax and usage of scope_ids is described

here

.

A URL may have appended to it a "fragment", also known
as a "ref" or a "reference". The fragment is indicated by the sharp
sign character "#" followed by more characters. For example,

```java
http://java.sun.com/index.html#chapter1
```

This fragment is not technically part of the URL. Rather, it
indicates that after the specified resource is retrieved, the
application is specifically interested in that part of the
document that has the tag

chapter1

attached to it. The
meaning of a tag is resource specific.

An application can also specify a "relative URL",
which contains only enough information to reach the resource
relative to another URL. Relative URLs are frequently used within
HTML pages. For example, if the contents of the URL:

```java
http://java.sun.com/index.html
```

contained within it the relative URL:

```java
FAQ.html
```

it would be a shorthand for:

```java
http://java.sun.com/FAQ.html
```

The relative URL need not specify all the components of a URL. If
the protocol, host name, or port number is missing, the value is
inherited from the fully specified URL. The file component must be
specified. The optional fragment is not inherited.

The URL class does not itself encode or decode any URL components
according to the escaping mechanism defined in RFC2396. It is the
responsibility of the caller to encode any fields, which need to be
escaped prior to calling URL, and also to decode any escaped fields,
that are returned from URL. Furthermore, because URL has no knowledge
of URL escaping, it does not recognise equivalence between the encoded
or decoded form of the same URL. For example, the two URLs:

```java
http://foo.com/hello world/ and http://foo.com/hello%20world
```

would be considered not equal to each other.

Note, the

URI

class does perform escaping of its
component fields in certain circumstances. The recommended way
to manage the encoding and decoding of URLs is to use

URI

,
and to convert between these two classes using

toURI()

and

URI.toURL()

.

The

URLEncoder

and

URLDecoder

classes can also be
used, but only for HTML form encoding, which is not the same
as the encoding scheme defined in RFC2396.

http://www.example.com/docs/resource1.html

The URL above indicates that the protocol to use is

http

(HyperText Transfer Protocol) and that the
information resides on a host machine named

www.example.com

. The information on that host
machine is named

/docs/resource1.html

. The exact
meaning of this name on the host machine is both protocol
dependent and host dependent. The information normally resides in
a file, but it could be generated on the fly. This component of
the URL is called the

path

component.

A URL can optionally specify a "port", which is the
port number to which the TCP connection is made on the remote host
machine. If the port is not specified, the default port for
the protocol is used instead. For example, the default port for

http

is

80

. An alternative port could be
specified as:

```java
http://www.example.com:1080/docs/resource1.html
```

The syntax of

URL

is defined by

RFC 2396: Uniform
Resource Identifiers (URI): Generic Syntax

, amended by

RFC 2732: Format for
Literal IPv6 Addresses in URLs

. The Literal IPv6 address format
also supports scope_ids. The syntax and usage of scope_ids is described

here

.

A URL may have appended to it a "fragment", also known
as a "ref" or a "reference". The fragment is indicated by the sharp
sign character "#" followed by more characters. For example,

```java
http://java.sun.com/index.html#chapter1
```

This fragment is not technically part of the URL. Rather, it
indicates that after the specified resource is retrieved, the
application is specifically interested in that part of the
document that has the tag

chapter1

attached to it. The
meaning of a tag is resource specific.

An application can also specify a "relative URL",
which contains only enough information to reach the resource
relative to another URL. Relative URLs are frequently used within
HTML pages. For example, if the contents of the URL:

```java
http://java.sun.com/index.html
```

contained within it the relative URL:

```java
FAQ.html
```

it would be a shorthand for:

```java
http://java.sun.com/FAQ.html
```

The relative URL need not specify all the components of a URL. If
the protocol, host name, or port number is missing, the value is
inherited from the fully specified URL. The file component must be
specified. The optional fragment is not inherited.

The URL class does not itself encode or decode any URL components
according to the escaping mechanism defined in RFC2396. It is the
responsibility of the caller to encode any fields, which need to be
escaped prior to calling URL, and also to decode any escaped fields,
that are returned from URL. Furthermore, because URL has no knowledge
of URL escaping, it does not recognise equivalence between the encoded
or decoded form of the same URL. For example, the two URLs:

```java
http://foo.com/hello world/ and http://foo.com/hello%20world
```

would be considered not equal to each other.

Note, the

URI

class does perform escaping of its
component fields in certain circumstances. The recommended way
to manage the encoding and decoding of URLs is to use

URI

,
and to convert between these two classes using

toURI()

and

URI.toURL()

.

The

URLEncoder

and

URLDecoder

classes can also be
used, but only for HTML form encoding, which is not the same
as the encoding scheme defined in RFC2396.

A URL can optionally specify a "port", which is the
port number to which the TCP connection is made on the remote host
machine. If the port is not specified, the default port for
the protocol is used instead. For example, the default port for

http

is

80

. An alternative port could be
specified as:

```java
http://www.example.com:1080/docs/resource1.html
```

The syntax of

URL

is defined by

RFC 2396: Uniform
Resource Identifiers (URI): Generic Syntax

, amended by

RFC 2732: Format for
Literal IPv6 Addresses in URLs

. The Literal IPv6 address format
also supports scope_ids. The syntax and usage of scope_ids is described

here

.

A URL may have appended to it a "fragment", also known
as a "ref" or a "reference". The fragment is indicated by the sharp
sign character "#" followed by more characters. For example,

```java
http://java.sun.com/index.html#chapter1
```

This fragment is not technically part of the URL. Rather, it
indicates that after the specified resource is retrieved, the
application is specifically interested in that part of the
document that has the tag

chapter1

attached to it. The
meaning of a tag is resource specific.

An application can also specify a "relative URL",
which contains only enough information to reach the resource
relative to another URL. Relative URLs are frequently used within
HTML pages. For example, if the contents of the URL:

```java
http://java.sun.com/index.html
```

contained within it the relative URL:

```java
FAQ.html
```

it would be a shorthand for:

```java
http://java.sun.com/FAQ.html
```

The relative URL need not specify all the components of a URL. If
the protocol, host name, or port number is missing, the value is
inherited from the fully specified URL. The file component must be
specified. The optional fragment is not inherited.

The URL class does not itself encode or decode any URL components
according to the escaping mechanism defined in RFC2396. It is the
responsibility of the caller to encode any fields, which need to be
escaped prior to calling URL, and also to decode any escaped fields,
that are returned from URL. Furthermore, because URL has no knowledge
of URL escaping, it does not recognise equivalence between the encoded
or decoded form of the same URL. For example, the two URLs:

```java
http://foo.com/hello world/ and http://foo.com/hello%20world
```

would be considered not equal to each other.

Note, the

URI

class does perform escaping of its
component fields in certain circumstances. The recommended way
to manage the encoding and decoding of URLs is to use

URI

,
and to convert between these two classes using

toURI()

and

URI.toURL()

.

The

URLEncoder

and

URLDecoder

classes can also be
used, but only for HTML form encoding, which is not the same
as the encoding scheme defined in RFC2396.

http://www.example.com:1080/docs/resource1.html

The syntax of

URL

is defined by

RFC 2396: Uniform
Resource Identifiers (URI): Generic Syntax

, amended by

RFC 2732: Format for
Literal IPv6 Addresses in URLs

. The Literal IPv6 address format
also supports scope_ids. The syntax and usage of scope_ids is described

here

.

A URL may have appended to it a "fragment", also known
as a "ref" or a "reference". The fragment is indicated by the sharp
sign character "#" followed by more characters. For example,

```java
http://java.sun.com/index.html#chapter1
```

This fragment is not technically part of the URL. Rather, it
indicates that after the specified resource is retrieved, the
application is specifically interested in that part of the
document that has the tag

chapter1

attached to it. The
meaning of a tag is resource specific.

An application can also specify a "relative URL",
which contains only enough information to reach the resource
relative to another URL. Relative URLs are frequently used within
HTML pages. For example, if the contents of the URL:

```java
http://java.sun.com/index.html
```

contained within it the relative URL:

```java
FAQ.html
```

it would be a shorthand for:

```java
http://java.sun.com/FAQ.html
```

The relative URL need not specify all the components of a URL. If
the protocol, host name, or port number is missing, the value is
inherited from the fully specified URL. The file component must be
specified. The optional fragment is not inherited.

The URL class does not itself encode or decode any URL components
according to the escaping mechanism defined in RFC2396. It is the
responsibility of the caller to encode any fields, which need to be
escaped prior to calling URL, and also to decode any escaped fields,
that are returned from URL. Furthermore, because URL has no knowledge
of URL escaping, it does not recognise equivalence between the encoded
or decoded form of the same URL. For example, the two URLs:

```java
http://foo.com/hello world/ and http://foo.com/hello%20world
```

would be considered not equal to each other.

Note, the

URI

class does perform escaping of its
component fields in certain circumstances. The recommended way
to manage the encoding and decoding of URLs is to use

URI

,
and to convert between these two classes using

toURI()

and

URI.toURL()

.

The

URLEncoder

and

URLDecoder

classes can also be
used, but only for HTML form encoding, which is not the same
as the encoding scheme defined in RFC2396.

A URL may have appended to it a "fragment", also known
as a "ref" or a "reference". The fragment is indicated by the sharp
sign character "#" followed by more characters. For example,

```java
http://java.sun.com/index.html#chapter1
```

This fragment is not technically part of the URL. Rather, it
indicates that after the specified resource is retrieved, the
application is specifically interested in that part of the
document that has the tag

chapter1

attached to it. The
meaning of a tag is resource specific.

An application can also specify a "relative URL",
which contains only enough information to reach the resource
relative to another URL. Relative URLs are frequently used within
HTML pages. For example, if the contents of the URL:

```java
http://java.sun.com/index.html
```

contained within it the relative URL:

```java
FAQ.html
```

it would be a shorthand for:

```java
http://java.sun.com/FAQ.html
```

The relative URL need not specify all the components of a URL. If
the protocol, host name, or port number is missing, the value is
inherited from the fully specified URL. The file component must be
specified. The optional fragment is not inherited.

The URL class does not itself encode or decode any URL components
according to the escaping mechanism defined in RFC2396. It is the
responsibility of the caller to encode any fields, which need to be
escaped prior to calling URL, and also to decode any escaped fields,
that are returned from URL. Furthermore, because URL has no knowledge
of URL escaping, it does not recognise equivalence between the encoded
or decoded form of the same URL. For example, the two URLs:

```java
http://foo.com/hello world/ and http://foo.com/hello%20world
```

would be considered not equal to each other.

Note, the

URI

class does perform escaping of its
component fields in certain circumstances. The recommended way
to manage the encoding and decoding of URLs is to use

URI

,
and to convert between these two classes using

toURI()

and

URI.toURL()

.

The

URLEncoder

and

URLDecoder

classes can also be
used, but only for HTML form encoding, which is not the same
as the encoding scheme defined in RFC2396.

http://java.sun.com/index.html#chapter1

This fragment is not technically part of the URL. Rather, it
indicates that after the specified resource is retrieved, the
application is specifically interested in that part of the
document that has the tag

chapter1

attached to it. The
meaning of a tag is resource specific.

An application can also specify a "relative URL",
which contains only enough information to reach the resource
relative to another URL. Relative URLs are frequently used within
HTML pages. For example, if the contents of the URL:

```java
http://java.sun.com/index.html
```

contained within it the relative URL:

```java
FAQ.html
```

it would be a shorthand for:

```java
http://java.sun.com/FAQ.html
```

The relative URL need not specify all the components of a URL. If
the protocol, host name, or port number is missing, the value is
inherited from the fully specified URL. The file component must be
specified. The optional fragment is not inherited.

The URL class does not itself encode or decode any URL components
according to the escaping mechanism defined in RFC2396. It is the
responsibility of the caller to encode any fields, which need to be
escaped prior to calling URL, and also to decode any escaped fields,
that are returned from URL. Furthermore, because URL has no knowledge
of URL escaping, it does not recognise equivalence between the encoded
or decoded form of the same URL. For example, the two URLs:

```java
http://foo.com/hello world/ and http://foo.com/hello%20world
```

would be considered not equal to each other.

Note, the

URI

class does perform escaping of its
component fields in certain circumstances. The recommended way
to manage the encoding and decoding of URLs is to use

URI

,
and to convert between these two classes using

toURI()

and

URI.toURL()

.

The

URLEncoder

and

URLDecoder

classes can also be
used, but only for HTML form encoding, which is not the same
as the encoding scheme defined in RFC2396.

An application can also specify a "relative URL",
which contains only enough information to reach the resource
relative to another URL. Relative URLs are frequently used within
HTML pages. For example, if the contents of the URL:

```java
http://java.sun.com/index.html
```

contained within it the relative URL:

```java
FAQ.html
```

it would be a shorthand for:

```java
http://java.sun.com/FAQ.html
```

The relative URL need not specify all the components of a URL. If
the protocol, host name, or port number is missing, the value is
inherited from the fully specified URL. The file component must be
specified. The optional fragment is not inherited.

The URL class does not itself encode or decode any URL components
according to the escaping mechanism defined in RFC2396. It is the
responsibility of the caller to encode any fields, which need to be
escaped prior to calling URL, and also to decode any escaped fields,
that are returned from URL. Furthermore, because URL has no knowledge
of URL escaping, it does not recognise equivalence between the encoded
or decoded form of the same URL. For example, the two URLs:

```java
http://foo.com/hello world/ and http://foo.com/hello%20world
```

would be considered not equal to each other.

Note, the

URI

class does perform escaping of its
component fields in certain circumstances. The recommended way
to manage the encoding and decoding of URLs is to use

URI

,
and to convert between these two classes using

toURI()

and

URI.toURL()

.

The

URLEncoder

and

URLDecoder

classes can also be
used, but only for HTML form encoding, which is not the same
as the encoding scheme defined in RFC2396.

http://java.sun.com/index.html

FAQ.html

http://java.sun.com/FAQ.html

The relative URL need not specify all the components of a URL. If
the protocol, host name, or port number is missing, the value is
inherited from the fully specified URL. The file component must be
specified. The optional fragment is not inherited.

The URL class does not itself encode or decode any URL components
according to the escaping mechanism defined in RFC2396. It is the
responsibility of the caller to encode any fields, which need to be
escaped prior to calling URL, and also to decode any escaped fields,
that are returned from URL. Furthermore, because URL has no knowledge
of URL escaping, it does not recognise equivalence between the encoded
or decoded form of the same URL. For example, the two URLs:

```java
http://foo.com/hello world/ and http://foo.com/hello%20world
```

would be considered not equal to each other.

Note, the

URI

class does perform escaping of its
component fields in certain circumstances. The recommended way
to manage the encoding and decoding of URLs is to use

URI

,
and to convert between these two classes using

toURI()

and

URI.toURL()

.

The

URLEncoder

and

URLDecoder

classes can also be
used, but only for HTML form encoding, which is not the same
as the encoding scheme defined in RFC2396.

The URL class does not itself encode or decode any URL components
according to the escaping mechanism defined in RFC2396. It is the
responsibility of the caller to encode any fields, which need to be
escaped prior to calling URL, and also to decode any escaped fields,
that are returned from URL. Furthermore, because URL has no knowledge
of URL escaping, it does not recognise equivalence between the encoded
or decoded form of the same URL. For example, the two URLs:

```java
http://foo.com/hello world/ and http://foo.com/hello%20world
```

would be considered not equal to each other.

Note, the

URI

class does perform escaping of its
component fields in certain circumstances. The recommended way
to manage the encoding and decoding of URLs is to use

URI

,
and to convert between these two classes using

toURI()

and

URI.toURL()

.

The

URLEncoder

and

URLDecoder

classes can also be
used, but only for HTML form encoding, which is not the same
as the encoding scheme defined in RFC2396.

http://foo.com/hello world/ and http://foo.com/hello%20world

Note, the

URI

class does perform escaping of its
component fields in certain circumstances. The recommended way
to manage the encoding and decoding of URLs is to use

URI

,
and to convert between these two classes using

toURI()

and

URI.toURL()

.

The

URLEncoder

and

URLDecoder

classes can also be
used, but only for HTML form encoding, which is not the same
as the encoding scheme defined in RFC2396.

The

URLEncoder

and

URLDecoder

classes can also be
used, but only for HTML form encoding, which is not the same
as the encoding scheme defined in RFC2396.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

URL

​(

String

spec)

Creates a

URL

object from the

String

representation.

URL

​(

String

protocol,

String

host,
int port,

String

file)

Creates a

URL

object from the specified

protocol

,

host

,

port

number, and

file

.

URL

​(

String

protocol,

String

host,
int port,

String

file,

URLStreamHandler

handler)

Creates a

URL

object from the specified

protocol

,

host

,

port

number,

file

, and

handler

.

URL

​(

String

protocol,

String

host,

String

file)

Creates a URL from the specified

protocol

name,

host

name, and

file

name.

URL

​(

URL

context,

String

spec)

Creates a URL by parsing the given spec within a specified context.

URL

​(

URL

context,

String

spec,

URLStreamHandler

handler)

Creates a URL by parsing the given spec with the specified handler
within a specified context.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares this URL for equality with another object.

String

getAuthority

()

Gets the authority part of this

URL

.

Object

getContent

()

Gets the contents of this URL.

Object

getContent

​(

Class

<?>[] classes)

Gets the contents of this URL.

int

getDefaultPort

()

Gets the default port number of the protocol associated
with this

URL

.

String

getFile

()

Gets the file name of this

URL

.

String

getHost

()

Gets the host name of this

URL

, if applicable.

String

getPath

()

Gets the path part of this

URL

.

int

getPort

()

Gets the port number of this

URL

.

String

getProtocol

()

Gets the protocol name of this

URL

.

String

getQuery

()

Gets the query part of this

URL

.

String

getRef

()

Gets the anchor (also known as the "reference") of this

URL

.

String

getUserInfo

()

Gets the userInfo part of this

URL

.

int

hashCode

()

Creates an integer suitable for hash table indexing.

URLConnection

openConnection

()

Returns a

URLConnection

instance that
represents a connection to the remote object referred to by the

URL

.

URLConnection

openConnection

​(

Proxy

proxy)

Same as

openConnection()

, except that the connection will be
made through the specified proxy; Protocol handlers that do not
support proxing will ignore the proxy parameter and make a
normal connection.

InputStream

openStream

()

Opens a connection to this

URL

and returns an

InputStream

for reading from that connection.

boolean

sameFile

​(

URL

other)

Compares two URLs, excluding the fragment component.

static void

setURLStreamHandlerFactory

​(

URLStreamHandlerFactory

fac)

Sets an application's

URLStreamHandlerFactory

.

String

toExternalForm

()

Constructs a string representation of this

URL

.

String

toString

()

Constructs a string representation of this

URL

.

URI

toURI

()

Returns a

URI

equivalent to this URL.

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

URL

​(

String

spec)

Creates a

URL

object from the

String

representation.

URL

​(

String

protocol,

String

host,
int port,

String

file)

Creates a

URL

object from the specified

protocol

,

host

,

port

number, and

file

.

URL

​(

String

protocol,

String

host,
int port,

String

file,

URLStreamHandler

handler)

Creates a

URL

object from the specified

protocol

,

host

,

port

number,

file

, and

handler

.

URL

​(

String

protocol,

String

host,

String

file)

Creates a URL from the specified

protocol

name,

host

name, and

file

name.

URL

​(

URL

context,

String

spec)

Creates a URL by parsing the given spec within a specified context.

URL

​(

URL

context,

String

spec,

URLStreamHandler

handler)

Creates a URL by parsing the given spec with the specified handler
within a specified context.

---

#### Constructor Summary

Creates a

URL

object from the

String

representation.

Creates a

URL

object from the specified

protocol

,

host

,

port

number, and

file

.

Creates a

URL

object from the specified

protocol

,

host

,

port

number,

file

, and

handler

.

Creates a URL from the specified

protocol

name,

host

name, and

file

name.

Creates a URL by parsing the given spec within a specified context.

Creates a URL by parsing the given spec with the specified handler
within a specified context.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares this URL for equality with another object.

String

getAuthority

()

Gets the authority part of this

URL

.

Object

getContent

()

Gets the contents of this URL.

Object

getContent

​(

Class

<?>[] classes)

Gets the contents of this URL.

int

getDefaultPort

()

Gets the default port number of the protocol associated
with this

URL

.

String

getFile

()

Gets the file name of this

URL

.

String

getHost

()

Gets the host name of this

URL

, if applicable.

String

getPath

()

Gets the path part of this

URL

.

int

getPort

()

Gets the port number of this

URL

.

String

getProtocol

()

Gets the protocol name of this

URL

.

String

getQuery

()

Gets the query part of this

URL

.

String

getRef

()

Gets the anchor (also known as the "reference") of this

URL

.

String

getUserInfo

()

Gets the userInfo part of this

URL

.

int

hashCode

()

Creates an integer suitable for hash table indexing.

URLConnection

openConnection

()

Returns a

URLConnection

instance that
represents a connection to the remote object referred to by the

URL

.

URLConnection

openConnection

​(

Proxy

proxy)

Same as

openConnection()

, except that the connection will be
made through the specified proxy; Protocol handlers that do not
support proxing will ignore the proxy parameter and make a
normal connection.

InputStream

openStream

()

Opens a connection to this

URL

and returns an

InputStream

for reading from that connection.

boolean

sameFile

​(

URL

other)

Compares two URLs, excluding the fragment component.

static void

setURLStreamHandlerFactory

​(

URLStreamHandlerFactory

fac)

Sets an application's

URLStreamHandlerFactory

.

String

toExternalForm

()

Constructs a string representation of this

URL

.

String

toString

()

Constructs a string representation of this

URL

.

URI

toURI

()

Returns a

URI

equivalent to this URL.

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

Compares this URL for equality with another object.

Gets the authority part of this

URL

.

Gets the contents of this URL.

Gets the default port number of the protocol associated
with this

URL

.

Gets the file name of this

URL

.

Gets the host name of this

URL

, if applicable.

Gets the path part of this

URL

.

Gets the port number of this

URL

.

Gets the protocol name of this

URL

.

Gets the query part of this

URL

.

Gets the anchor (also known as the "reference") of this

URL

.

Gets the userInfo part of this

URL

.

Creates an integer suitable for hash table indexing.

Returns a

URLConnection

instance that
represents a connection to the remote object referred to by the

URL

.

Same as

openConnection()

, except that the connection will be
made through the specified proxy; Protocol handlers that do not
support proxing will ignore the proxy parameter and make a
normal connection.

Opens a connection to this

URL

and returns an

InputStream

for reading from that connection.

Compares two URLs, excluding the fragment component.

Sets an application's

URLStreamHandlerFactory

.

Constructs a string representation of this

URL

.

Returns a

URI

equivalent to this URL.

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

- URL

```java
public URL​(
String
protocol,

String
host,
int port,

String
file)
throws
MalformedURLException
```

Creates a

URL

object from the specified

protocol

,

host

,

port

number, and

file

.

host

can be expressed as a host name or a literal
IP address. If IPv6 literal address is used, it should be
enclosed in square brackets (

'['

and

']'

), as
specified by

RFC 2732

;
However, the literal IPv6 address format defined in

RFC 2373: IP
Version 6 Addressing Architecture

is also accepted.

Specifying a

port

number of

-1

indicates that the URL should use the default port for the
protocol.

If this is the first URL object being created with the specified
protocol, a

stream protocol handler

object, an instance of
class

URLStreamHandler

, is created for that protocol:

- If the application has previously set up an instance of

URLStreamHandlerFactory

as the stream handler factory,
then the

createURLStreamHandler

method of that instance
is called with the protocol string as an argument to create the
stream protocol handler.

If no

URLStreamHandlerFactory

has yet been set up,
or if the factory's

createURLStreamHandler

method
returns

null

, then the

ServiceLoader

mechanism is used to locate

URLStreamHandlerProvider

implementations using the system class
loader. The order that providers are located is implementation
specific, and an implementation is free to cache the located
providers. A

ServiceConfigurationError

,

Error

or

RuntimeException

thrown from the

createURLStreamHandler

, if encountered, will
be propagated to the calling thread. The

createURLStreamHandler

method of each provider, if instantiated, is
invoked, with the protocol string, until a provider returns non-null,
or all providers have been exhausted.

If the previous step fails to find a protocol handler, the
constructor reads the value of the system property:

java.protocol.handler.pkgs

If the value of that system property is not

null

,
it is interpreted as a list of packages separated by a vertical
slash character '

|

'. The constructor tries to load
the class named:

<package>.<protocol>.Handler

where

<package>

is replaced by the name of the package
and

<protocol>

is replaced by the name of the protocol.
If this class does not exist, or if the class exists but it is not
a subclass of

URLStreamHandler

, then the next package
in the list is tried.

If the previous step fails to find a protocol handler, then the
constructor tries to load a built-in protocol handler.
If this class does not exist, or if the class exists but it is not a
subclass of

URLStreamHandler

, then a

MalformedURLException

is thrown.

Protocol handlers for the following protocols are guaranteed
to exist on the search path :-

```java
http, https, file, and jar
```

Protocol handlers for additional protocols may also be available.
Some protocol handlers, for example those used for loading platform
classes or classes on the class path, may not be overridden. The details
of such restrictions, and when those restrictions apply (during
initialization of the runtime for example), are implementation specific
and therefore not specified

No validation of the inputs is performed by this constructor.

**Parameters:** protocol

- the name of the protocol to use.
**Parameters:** host

- the name of the host.
**Parameters:** port

- the port number on the host.
**Parameters:** file

- the file on the host
**Throws:** MalformedURLException

- if an unknown protocol or the port
is a negative number other than -1
**See Also:** System.getProperty(java.lang.String)

,

setURLStreamHandlerFactory(
java.net.URLStreamHandlerFactory)

,

URLStreamHandler

,

URLStreamHandlerFactory.createURLStreamHandler(
java.lang.String)

- URL

```java
public URL​(
String
protocol,

String
host,

String
file)
throws
MalformedURLException
```

Creates a URL from the specified

protocol

name,

host

name, and

file

name. The
default port for the specified protocol is used.

This constructor is equivalent to the four-argument
constructor with the only difference of using the
default port for the specified protocol.

No validation of the inputs is performed by this constructor.

**Parameters:** protocol

- the name of the protocol to use.
**Parameters:** host

- the name of the host.
**Parameters:** file

- the file on the host.
**Throws:** MalformedURLException

- if an unknown protocol is specified.
**See Also:** URL(java.lang.String, java.lang.String,
int, java.lang.String)

- URL

```java
public URL​(
String
protocol,

String
host,
int port,

String
file,

URLStreamHandler
handler)
throws
MalformedURLException
```

Creates a

URL

object from the specified

protocol

,

host

,

port

number,

file

, and

handler

. Specifying
a

port

number of

-1

indicates that
the URL should use the default port for the protocol. Specifying
a

handler

of

null

indicates that the URL
should use a default stream handler for the protocol, as outlined
for:
java.net.URL#URL(java.lang.String, java.lang.String, int,
java.lang.String)

If the handler is not null and there is a security manager,
the security manager's

checkPermission

method is called with a

NetPermission("specifyStreamHandler")

permission.
This may result in a SecurityException.

No validation of the inputs is performed by this constructor.

**Parameters:** protocol

- the name of the protocol to use.
**Parameters:** host

- the name of the host.
**Parameters:** port

- the port number on the host.
**Parameters:** file

- the file on the host
**Parameters:** handler

- the stream handler for the URL.
**Throws:** MalformedURLException

- if an unknown protocol or the port
is a negative number other than -1
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
specifying a stream handler explicitly.
**See Also:** System.getProperty(java.lang.String)

,

setURLStreamHandlerFactory(
java.net.URLStreamHandlerFactory)

,

URLStreamHandler

,

URLStreamHandlerFactory.createURLStreamHandler(
java.lang.String)

,

SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

- URL

```java
public URL​(
String
spec)
throws
MalformedURLException
```

Creates a

URL

object from the

String

representation.

This constructor is equivalent to a call to the two-argument
constructor with a

null

first argument.

**Parameters:** spec

- the

String

to parse as a URL.
**Throws:** MalformedURLException

- if no protocol is specified, or an
unknown protocol is found, or

spec

is

null

,
or the parsed URL fails to comply with the specific syntax
of the associated protocol.
**See Also:** URL(java.net.URL, java.lang.String)

- URL

```java
public URL​(
URL
context,

String
spec)
throws
MalformedURLException
```

Creates a URL by parsing the given spec within a specified context.

The new URL is created from the given context URL and the spec
argument as described in
RFC2396 "Uniform Resource Identifiers : Generic * Syntax" :

```java
<scheme>://<authority><path>?<query>#<fragment>
```

The reference is parsed into the scheme, authority, path, query and
fragment parts. If the path component is empty and the scheme,
authority, and query components are undefined, then the new URL is a
reference to the current document. Otherwise, the fragment and query
parts present in the spec are used in the new URL.

If the scheme component is defined in the given spec and does not match
the scheme of the context, then the new URL is created as an absolute
URL based on the spec alone. Otherwise the scheme component is inherited
from the context URL.

If the authority component is present in the spec then the spec is
treated as absolute and the spec authority and path will replace the
context authority and path. If the authority component is absent in the
spec then the authority of the new URL will be inherited from the
context.

If the spec's path component begins with a slash character
"/" then the
path is treated as absolute and the spec path replaces the context path.

Otherwise, the path is treated as a relative path and is appended to the
context path, as described in RFC2396. Also, in this case,
the path is canonicalized through the removal of directory
changes made by occurrences of ".." and ".".

For a more detailed description of URL parsing, refer to RFC2396.

**Parameters:** context

- the context in which to parse the specification.
**Parameters:** spec

- the

String

to parse as a URL.
**Throws:** MalformedURLException

- if no protocol is specified, or an
unknown protocol is found, or

spec

is

null

,
or the parsed URL fails to comply with the specific syntax
of the associated protocol.
**See Also:** URL(java.lang.String, java.lang.String,
int, java.lang.String)

,

URLStreamHandler

,

URLStreamHandler.parseURL(java.net.URL,
java.lang.String, int, int)

- URL

```java
public URL​(
URL
context,

String
spec,

URLStreamHandler
handler)
throws
MalformedURLException
```

Creates a URL by parsing the given spec with the specified handler
within a specified context. If the handler is null, the parsing
occurs as with the two argument constructor.

**Parameters:** context

- the context in which to parse the specification.
**Parameters:** spec

- the

String

to parse as a URL.
**Parameters:** handler

- the stream handler for the URL.
**Throws:** MalformedURLException

- if no protocol is specified, or an
unknown protocol is found, or

spec

is

null

,
or the parsed URL fails to comply with the specific syntax
of the associated protocol.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
specifying a stream handler.
**See Also:** URL(java.lang.String, java.lang.String,
int, java.lang.String)

,

URLStreamHandler

,

URLStreamHandler.parseURL(java.net.URL,
java.lang.String, int, int)

============ METHOD DETAIL ==========

- Method Detail

- getQuery

```java
public
String
getQuery()
```

Gets the query part of this

URL

.

**Returns:** the query part of this

URL

,
or

null

if one does not exist
**Since:** 1.3

- getPath

```java
public
String
getPath()
```

Gets the path part of this

URL

.

**Returns:** the path part of this

URL

, or an
empty string if one does not exist
**Since:** 1.3

- getUserInfo

```java
public
String
getUserInfo()
```

Gets the userInfo part of this

URL

.

**Returns:** the userInfo part of this

URL

, or

null

if one does not exist
**Since:** 1.3

- getAuthority

```java
public
String
getAuthority()
```

Gets the authority part of this

URL

.

**Returns:** the authority part of this

URL
**Since:** 1.3

- getPort

```java
public int getPort()
```

Gets the port number of this

URL

.

**Returns:** the port number, or -1 if the port is not set

- getDefaultPort

```java
public int getDefaultPort()
```

Gets the default port number of the protocol associated
with this

URL

. If the URL scheme or the URLStreamHandler
for the URL do not define a default port number,
then -1 is returned.

**Returns:** the port number
**Since:** 1.4

- getProtocol

```java
public
String
getProtocol()
```

Gets the protocol name of this

URL

.

**Returns:** the protocol of this

URL

.

- getHost

```java
public
String
getHost()
```

Gets the host name of this

URL

, if applicable.
The format of the host conforms to RFC 2732, i.e. for a
literal IPv6 address, this method will return the IPv6 address
enclosed in square brackets (

'['

and

']'

).

**Returns:** the host name of this

URL

.

- getFile

```java
public
String
getFile()
```

Gets the file name of this

URL

.
The returned file portion will be
the same as

getPath()

, plus the concatenation of
the value of

getQuery()

, if any. If there is
no query portion, this method and

getPath()

will
return identical results.

**Returns:** the file name of this

URL

,
or an empty string if one does not exist

- getRef

```java
public
String
getRef()
```

Gets the anchor (also known as the "reference") of this

URL

.

**Returns:** the anchor (also known as the "reference") of this

URL

, or

null

if one does not exist

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this URL for equality with another object.

If the given object is not a URL then this method immediately returns

false

.

Two URL objects are equal if they have the same protocol, reference
equivalent hosts, have the same port number on the host, and the same
file and fragment of the file.

Two hosts are considered equivalent if both host names can be resolved
into the same IP addresses; else if either host name can't be
resolved, the host names must be equal without regard to case; or both
host names equal to null.

Since hosts comparison requires name resolution, this operation is a
blocking operation.

Note: The defined behavior for

equals

is known to
be inconsistent with virtual hosting in HTTP.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the URL to compare against.
**Returns:** true

if the objects are the same;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Creates an integer suitable for hash table indexing.

The hash code is based upon all the URL components relevant for URL
comparison. As such, this operation is a blocking operation.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

URL

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- sameFile

```java
public boolean sameFile​(
URL
other)
```

Compares two URLs, excluding the fragment component.

Returns

true

if this

URL

and the

other

argument are equal without taking the
fragment component into consideration.

**Parameters:** other

- the

URL

to compare against.
**Returns:** true

if they reference the same remote object;

false

otherwise.

- toString

```java
public
String
toString()
```

Constructs a string representation of this

URL

. The
string is created by calling the

toExternalForm

method of the stream protocol handler for this object.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this object.
**See Also:** URL(java.lang.String, java.lang.String, int,
java.lang.String)

,

URLStreamHandler.toExternalForm(java.net.URL)

- toExternalForm

```java
public
String
toExternalForm()
```

Constructs a string representation of this

URL

. The
string is created by calling the

toExternalForm

method of the stream protocol handler for this object.

**Returns:** a string representation of this object.
**See Also:** URL(java.lang.String, java.lang.String,
int, java.lang.String)

,

URLStreamHandler.toExternalForm(java.net.URL)

- toURI

```java
public
URI
toURI()
throws
URISyntaxException
```

Returns a

URI

equivalent to this URL.
This method functions in the same way as

new URI (this.toString())

.

Note, any URL instance that complies with RFC 2396 can be converted
to a URI. However, some URLs that are not strictly in compliance
can not be converted to a URI.

**Returns:** a URI instance equivalent to this URL.
**Throws:** URISyntaxException

- if this URL is not formatted strictly according to
to RFC2396 and cannot be converted to a URI.
**Since:** 1.5

- openConnection

```java
public
URLConnection
openConnection()
throws
IOException
```

Returns a

URLConnection

instance that
represents a connection to the remote object referred to by the

URL

.

A new instance of

URLConnection

is
created every time when invoking the

URLStreamHandler.openConnection(URL)

method of the protocol handler for
this URL.

It should be noted that a URLConnection instance does not establish
the actual network connection on creation. This will happen only when
calling

URLConnection.connect()

.

If for the URL's protocol (such as HTTP or JAR), there
exists a public, specialized URLConnection subclass belonging
to one of the following packages or one of their subpackages:
java.lang, java.io, java.util, java.net, the connection
returned will be of that subclass. For example, for HTTP an
HttpURLConnection will be returned, and for JAR a
JarURLConnection will be returned.

**Returns:** a

URLConnection

linking
to the URL.
**Throws:** IOException

- if an I/O exception occurs.
**See Also:** URL(java.lang.String, java.lang.String,
int, java.lang.String)

- openConnection

```java
public
URLConnection
openConnection​(
Proxy
proxy)
throws
IOException
```

Same as

openConnection()

, except that the connection will be
made through the specified proxy; Protocol handlers that do not
support proxing will ignore the proxy parameter and make a
normal connection.

Invoking this method preempts the system's default

ProxySelector

settings.

**Parameters:** proxy

- the Proxy through which this connection
will be made. If direct connection is desired,
Proxy.NO_PROXY should be specified.
**Returns:** a

URLConnection

to the URL.
**Throws:** IOException

- if an I/O exception occurs.
**Throws:** SecurityException

- if a security manager is present
and the caller doesn't have permission to connect
to the proxy.
**Throws:** IllegalArgumentException

- will be thrown if proxy is null,
or proxy has the wrong type
**Throws:** UnsupportedOperationException

- if the subclass that
implements the protocol handler doesn't support
this method.
**Since:** 1.5
**See Also:** URL(java.lang.String, java.lang.String,
int, java.lang.String)

,

URLConnection

,

URLStreamHandler.openConnection(java.net.URL,
java.net.Proxy)

- openStream

```java
public final
InputStream
openStream()
throws
IOException
```

Opens a connection to this

URL

and returns an

InputStream

for reading from that connection. This
method is a shorthand for:

```java
openConnection().getInputStream()
```

**Returns:** an input stream for reading from the URL connection.
**Throws:** IOException

- if an I/O exception occurs.
**See Also:** openConnection()

,

URLConnection.getInputStream()

- getContent

```java
public final
Object
getContent()
throws
IOException
```

Gets the contents of this URL. This method is a shorthand for:

```java
openConnection().getContent()
```

**Returns:** the contents of this URL.
**Throws:** IOException

- if an I/O exception occurs.
**See Also:** URLConnection.getContent()

- getContent

```java
public final
Object
getContent​(
Class
<?>[] classes)
throws
IOException
```

Gets the contents of this URL. This method is a shorthand for:

```java
openConnection().getContent(classes)
```

**Parameters:** classes

- an array of Java types
**Returns:** the content object of this URL that is the first match of
the types specified in the classes array.
null if none of the requested types are supported.
**Throws:** IOException

- if an I/O exception occurs.
**Since:** 1.3
**See Also:** URLConnection.getContent(Class[])

- setURLStreamHandlerFactory

```java
public static void setURLStreamHandlerFactory​(
URLStreamHandlerFactory
fac)
```

Sets an application's

URLStreamHandlerFactory

.
This method can be called at most once in a given Java Virtual
Machine.

The

URLStreamHandlerFactory

instance is used to
construct a stream protocol handler from a protocol name.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:** fac

- the desired factory.
**Throws:** Error

- if the application has already set a factory.
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't allow
the operation.
**See Also:** URL(java.lang.String, java.lang.String,
int, java.lang.String)

,

URLStreamHandlerFactory

,

SecurityManager.checkSetFactory()

Constructor Detail

- URL

```java
public URL​(
String
protocol,

String
host,
int port,

String
file)
throws
MalformedURLException
```

Creates a

URL

object from the specified

protocol

,

host

,

port

number, and

file

.

host

can be expressed as a host name or a literal
IP address. If IPv6 literal address is used, it should be
enclosed in square brackets (

'['

and

']'

), as
specified by

RFC 2732

;
However, the literal IPv6 address format defined in

RFC 2373: IP
Version 6 Addressing Architecture

is also accepted.

Specifying a

port

number of

-1

indicates that the URL should use the default port for the
protocol.

If this is the first URL object being created with the specified
protocol, a

stream protocol handler

object, an instance of
class

URLStreamHandler

, is created for that protocol:

- If the application has previously set up an instance of

URLStreamHandlerFactory

as the stream handler factory,
then the

createURLStreamHandler

method of that instance
is called with the protocol string as an argument to create the
stream protocol handler.

If no

URLStreamHandlerFactory

has yet been set up,
or if the factory's

createURLStreamHandler

method
returns

null

, then the

ServiceLoader

mechanism is used to locate

URLStreamHandlerProvider

implementations using the system class
loader. The order that providers are located is implementation
specific, and an implementation is free to cache the located
providers. A

ServiceConfigurationError

,

Error

or

RuntimeException

thrown from the

createURLStreamHandler

, if encountered, will
be propagated to the calling thread. The

createURLStreamHandler

method of each provider, if instantiated, is
invoked, with the protocol string, until a provider returns non-null,
or all providers have been exhausted.

If the previous step fails to find a protocol handler, the
constructor reads the value of the system property:

java.protocol.handler.pkgs

If the value of that system property is not

null

,
it is interpreted as a list of packages separated by a vertical
slash character '

|

'. The constructor tries to load
the class named:

<package>.<protocol>.Handler

where

<package>

is replaced by the name of the package
and

<protocol>

is replaced by the name of the protocol.
If this class does not exist, or if the class exists but it is not
a subclass of

URLStreamHandler

, then the next package
in the list is tried.

If the previous step fails to find a protocol handler, then the
constructor tries to load a built-in protocol handler.
If this class does not exist, or if the class exists but it is not a
subclass of

URLStreamHandler

, then a

MalformedURLException

is thrown.

Protocol handlers for the following protocols are guaranteed
to exist on the search path :-

```java
http, https, file, and jar
```

Protocol handlers for additional protocols may also be available.
Some protocol handlers, for example those used for loading platform
classes or classes on the class path, may not be overridden. The details
of such restrictions, and when those restrictions apply (during
initialization of the runtime for example), are implementation specific
and therefore not specified

No validation of the inputs is performed by this constructor.

**Parameters:** protocol

- the name of the protocol to use.
**Parameters:** host

- the name of the host.
**Parameters:** port

- the port number on the host.
**Parameters:** file

- the file on the host
**Throws:** MalformedURLException

- if an unknown protocol or the port
is a negative number other than -1
**See Also:** System.getProperty(java.lang.String)

,

setURLStreamHandlerFactory(
java.net.URLStreamHandlerFactory)

,

URLStreamHandler

,

URLStreamHandlerFactory.createURLStreamHandler(
java.lang.String)

- URL

```java
public URL​(
String
protocol,

String
host,

String
file)
throws
MalformedURLException
```

Creates a URL from the specified

protocol

name,

host

name, and

file

name. The
default port for the specified protocol is used.

This constructor is equivalent to the four-argument
constructor with the only difference of using the
default port for the specified protocol.

No validation of the inputs is performed by this constructor.

**Parameters:** protocol

- the name of the protocol to use.
**Parameters:** host

- the name of the host.
**Parameters:** file

- the file on the host.
**Throws:** MalformedURLException

- if an unknown protocol is specified.
**See Also:** URL(java.lang.String, java.lang.String,
int, java.lang.String)

- URL

```java
public URL​(
String
protocol,

String
host,
int port,

String
file,

URLStreamHandler
handler)
throws
MalformedURLException
```

Creates a

URL

object from the specified

protocol

,

host

,

port

number,

file

, and

handler

. Specifying
a

port

number of

-1

indicates that
the URL should use the default port for the protocol. Specifying
a

handler

of

null

indicates that the URL
should use a default stream handler for the protocol, as outlined
for:
java.net.URL#URL(java.lang.String, java.lang.String, int,
java.lang.String)

If the handler is not null and there is a security manager,
the security manager's

checkPermission

method is called with a

NetPermission("specifyStreamHandler")

permission.
This may result in a SecurityException.

No validation of the inputs is performed by this constructor.

**Parameters:** protocol

- the name of the protocol to use.
**Parameters:** host

- the name of the host.
**Parameters:** port

- the port number on the host.
**Parameters:** file

- the file on the host
**Parameters:** handler

- the stream handler for the URL.
**Throws:** MalformedURLException

- if an unknown protocol or the port
is a negative number other than -1
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
specifying a stream handler explicitly.
**See Also:** System.getProperty(java.lang.String)

,

setURLStreamHandlerFactory(
java.net.URLStreamHandlerFactory)

,

URLStreamHandler

,

URLStreamHandlerFactory.createURLStreamHandler(
java.lang.String)

,

SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

- URL

```java
public URL​(
String
spec)
throws
MalformedURLException
```

Creates a

URL

object from the

String

representation.

This constructor is equivalent to a call to the two-argument
constructor with a

null

first argument.

**Parameters:** spec

- the

String

to parse as a URL.
**Throws:** MalformedURLException

- if no protocol is specified, or an
unknown protocol is found, or

spec

is

null

,
or the parsed URL fails to comply with the specific syntax
of the associated protocol.
**See Also:** URL(java.net.URL, java.lang.String)

- URL

```java
public URL​(
URL
context,

String
spec)
throws
MalformedURLException
```

Creates a URL by parsing the given spec within a specified context.

The new URL is created from the given context URL and the spec
argument as described in
RFC2396 "Uniform Resource Identifiers : Generic * Syntax" :

```java
<scheme>://<authority><path>?<query>#<fragment>
```

The reference is parsed into the scheme, authority, path, query and
fragment parts. If the path component is empty and the scheme,
authority, and query components are undefined, then the new URL is a
reference to the current document. Otherwise, the fragment and query
parts present in the spec are used in the new URL.

If the scheme component is defined in the given spec and does not match
the scheme of the context, then the new URL is created as an absolute
URL based on the spec alone. Otherwise the scheme component is inherited
from the context URL.

If the authority component is present in the spec then the spec is
treated as absolute and the spec authority and path will replace the
context authority and path. If the authority component is absent in the
spec then the authority of the new URL will be inherited from the
context.

If the spec's path component begins with a slash character
"/" then the
path is treated as absolute and the spec path replaces the context path.

Otherwise, the path is treated as a relative path and is appended to the
context path, as described in RFC2396. Also, in this case,
the path is canonicalized through the removal of directory
changes made by occurrences of ".." and ".".

For a more detailed description of URL parsing, refer to RFC2396.

**Parameters:** context

- the context in which to parse the specification.
**Parameters:** spec

- the

String

to parse as a URL.
**Throws:** MalformedURLException

- if no protocol is specified, or an
unknown protocol is found, or

spec

is

null

,
or the parsed URL fails to comply with the specific syntax
of the associated protocol.
**See Also:** URL(java.lang.String, java.lang.String,
int, java.lang.String)

,

URLStreamHandler

,

URLStreamHandler.parseURL(java.net.URL,
java.lang.String, int, int)

- URL

```java
public URL​(
URL
context,

String
spec,

URLStreamHandler
handler)
throws
MalformedURLException
```

Creates a URL by parsing the given spec with the specified handler
within a specified context. If the handler is null, the parsing
occurs as with the two argument constructor.

**Parameters:** context

- the context in which to parse the specification.
**Parameters:** spec

- the

String

to parse as a URL.
**Parameters:** handler

- the stream handler for the URL.
**Throws:** MalformedURLException

- if no protocol is specified, or an
unknown protocol is found, or

spec

is

null

,
or the parsed URL fails to comply with the specific syntax
of the associated protocol.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
specifying a stream handler.
**See Also:** URL(java.lang.String, java.lang.String,
int, java.lang.String)

,

URLStreamHandler

,

URLStreamHandler.parseURL(java.net.URL,
java.lang.String, int, int)

---

#### Constructor Detail

URL

```java
public URL​(
String
protocol,

String
host,
int port,

String
file)
throws
MalformedURLException
```

Creates a

URL

object from the specified

protocol

,

host

,

port

number, and

file

.

host

can be expressed as a host name or a literal
IP address. If IPv6 literal address is used, it should be
enclosed in square brackets (

'['

and

']'

), as
specified by

RFC 2732

;
However, the literal IPv6 address format defined in

RFC 2373: IP
Version 6 Addressing Architecture

is also accepted.

Specifying a

port

number of

-1

indicates that the URL should use the default port for the
protocol.

If this is the first URL object being created with the specified
protocol, a

stream protocol handler

object, an instance of
class

URLStreamHandler

, is created for that protocol:

- If the application has previously set up an instance of

URLStreamHandlerFactory

as the stream handler factory,
then the

createURLStreamHandler

method of that instance
is called with the protocol string as an argument to create the
stream protocol handler.

If no

URLStreamHandlerFactory

has yet been set up,
or if the factory's

createURLStreamHandler

method
returns

null

, then the

ServiceLoader

mechanism is used to locate

URLStreamHandlerProvider

implementations using the system class
loader. The order that providers are located is implementation
specific, and an implementation is free to cache the located
providers. A

ServiceConfigurationError

,

Error

or

RuntimeException

thrown from the

createURLStreamHandler

, if encountered, will
be propagated to the calling thread. The

createURLStreamHandler

method of each provider, if instantiated, is
invoked, with the protocol string, until a provider returns non-null,
or all providers have been exhausted.

If the previous step fails to find a protocol handler, the
constructor reads the value of the system property:

java.protocol.handler.pkgs

If the value of that system property is not

null

,
it is interpreted as a list of packages separated by a vertical
slash character '

|

'. The constructor tries to load
the class named:

<package>.<protocol>.Handler

where

<package>

is replaced by the name of the package
and

<protocol>

is replaced by the name of the protocol.
If this class does not exist, or if the class exists but it is not
a subclass of

URLStreamHandler

, then the next package
in the list is tried.

If the previous step fails to find a protocol handler, then the
constructor tries to load a built-in protocol handler.
If this class does not exist, or if the class exists but it is not a
subclass of

URLStreamHandler

, then a

MalformedURLException

is thrown.

Protocol handlers for the following protocols are guaranteed
to exist on the search path :-

```java
http, https, file, and jar
```

Protocol handlers for additional protocols may also be available.
Some protocol handlers, for example those used for loading platform
classes or classes on the class path, may not be overridden. The details
of such restrictions, and when those restrictions apply (during
initialization of the runtime for example), are implementation specific
and therefore not specified

No validation of the inputs is performed by this constructor.

**Parameters:** protocol

- the name of the protocol to use.
**Parameters:** host

- the name of the host.
**Parameters:** port

- the port number on the host.
**Parameters:** file

- the file on the host
**Throws:** MalformedURLException

- if an unknown protocol or the port
is a negative number other than -1
**See Also:** System.getProperty(java.lang.String)

,

setURLStreamHandlerFactory(
java.net.URLStreamHandlerFactory)

,

URLStreamHandler

,

URLStreamHandlerFactory.createURLStreamHandler(
java.lang.String)

---

#### URL

public URL​(

String

protocol,

String

host,
int port,

String

file)
throws

MalformedURLException

Creates a

URL

object from the specified

protocol

,

host

,

port

number, and

file

.

host

can be expressed as a host name or a literal
IP address. If IPv6 literal address is used, it should be
enclosed in square brackets (

'['

and

']'

), as
specified by

RFC 2732

;
However, the literal IPv6 address format defined in

RFC 2373: IP
Version 6 Addressing Architecture

is also accepted.

Specifying a

port

number of

-1

indicates that the URL should use the default port for the
protocol.

If this is the first URL object being created with the specified
protocol, a

stream protocol handler

object, an instance of
class

URLStreamHandler

, is created for that protocol:

- If the application has previously set up an instance of

URLStreamHandlerFactory

as the stream handler factory,
then the

createURLStreamHandler

method of that instance
is called with the protocol string as an argument to create the
stream protocol handler.

If no

URLStreamHandlerFactory

has yet been set up,
or if the factory's

createURLStreamHandler

method
returns

null

, then the

ServiceLoader

mechanism is used to locate

URLStreamHandlerProvider

implementations using the system class
loader. The order that providers are located is implementation
specific, and an implementation is free to cache the located
providers. A

ServiceConfigurationError

,

Error

or

RuntimeException

thrown from the

createURLStreamHandler

, if encountered, will
be propagated to the calling thread. The

createURLStreamHandler

method of each provider, if instantiated, is
invoked, with the protocol string, until a provider returns non-null,
or all providers have been exhausted.

If the previous step fails to find a protocol handler, the
constructor reads the value of the system property:

java.protocol.handler.pkgs

If the value of that system property is not

null

,
it is interpreted as a list of packages separated by a vertical
slash character '

|

'. The constructor tries to load
the class named:

<package>.<protocol>.Handler

where

<package>

is replaced by the name of the package
and

<protocol>

is replaced by the name of the protocol.
If this class does not exist, or if the class exists but it is not
a subclass of

URLStreamHandler

, then the next package
in the list is tried.

If the previous step fails to find a protocol handler, then the
constructor tries to load a built-in protocol handler.
If this class does not exist, or if the class exists but it is not a
subclass of

URLStreamHandler

, then a

MalformedURLException

is thrown.

Protocol handlers for the following protocols are guaranteed
to exist on the search path :-

```java
http, https, file, and jar
```

Protocol handlers for additional protocols may also be available.
Some protocol handlers, for example those used for loading platform
classes or classes on the class path, may not be overridden. The details
of such restrictions, and when those restrictions apply (during
initialization of the runtime for example), are implementation specific
and therefore not specified

No validation of the inputs is performed by this constructor.

host

can be expressed as a host name or a literal
IP address. If IPv6 literal address is used, it should be
enclosed in square brackets (

'['

and

']'

), as
specified by

RFC 2732

;
However, the literal IPv6 address format defined in

RFC 2373: IP
Version 6 Addressing Architecture

is also accepted.

Specifying a

port

number of

-1

indicates that the URL should use the default port for the
protocol.

If this is the first URL object being created with the specified
protocol, a

stream protocol handler

object, an instance of
class

URLStreamHandler

, is created for that protocol:

- If the application has previously set up an instance of

URLStreamHandlerFactory

as the stream handler factory,
then the

createURLStreamHandler

method of that instance
is called with the protocol string as an argument to create the
stream protocol handler.

If no

URLStreamHandlerFactory

has yet been set up,
or if the factory's

createURLStreamHandler

method
returns

null

, then the

ServiceLoader

mechanism is used to locate

URLStreamHandlerProvider

implementations using the system class
loader. The order that providers are located is implementation
specific, and an implementation is free to cache the located
providers. A

ServiceConfigurationError

,

Error

or

RuntimeException

thrown from the

createURLStreamHandler

, if encountered, will
be propagated to the calling thread. The

createURLStreamHandler

method of each provider, if instantiated, is
invoked, with the protocol string, until a provider returns non-null,
or all providers have been exhausted.

If the previous step fails to find a protocol handler, the
constructor reads the value of the system property:

java.protocol.handler.pkgs

If the value of that system property is not

null

,
it is interpreted as a list of packages separated by a vertical
slash character '

|

'. The constructor tries to load
the class named:

<package>.<protocol>.Handler

where

<package>

is replaced by the name of the package
and

<protocol>

is replaced by the name of the protocol.
If this class does not exist, or if the class exists but it is not
a subclass of

URLStreamHandler

, then the next package
in the list is tried.

If the previous step fails to find a protocol handler, then the
constructor tries to load a built-in protocol handler.
If this class does not exist, or if the class exists but it is not a
subclass of

URLStreamHandler

, then a

MalformedURLException

is thrown.

Protocol handlers for the following protocols are guaranteed
to exist on the search path :-

```java
http, https, file, and jar
```

Protocol handlers for additional protocols may also be available.
Some protocol handlers, for example those used for loading platform
classes or classes on the class path, may not be overridden. The details
of such restrictions, and when those restrictions apply (during
initialization of the runtime for example), are implementation specific
and therefore not specified

No validation of the inputs is performed by this constructor.

Specifying a

port

number of

-1

indicates that the URL should use the default port for the
protocol.

If this is the first URL object being created with the specified
protocol, a

stream protocol handler

object, an instance of
class

URLStreamHandler

, is created for that protocol:

- If the application has previously set up an instance of

URLStreamHandlerFactory

as the stream handler factory,
then the

createURLStreamHandler

method of that instance
is called with the protocol string as an argument to create the
stream protocol handler.

If no

URLStreamHandlerFactory

has yet been set up,
or if the factory's

createURLStreamHandler

method
returns

null

, then the

ServiceLoader

mechanism is used to locate

URLStreamHandlerProvider

implementations using the system class
loader. The order that providers are located is implementation
specific, and an implementation is free to cache the located
providers. A

ServiceConfigurationError

,

Error

or

RuntimeException

thrown from the

createURLStreamHandler

, if encountered, will
be propagated to the calling thread. The

createURLStreamHandler

method of each provider, if instantiated, is
invoked, with the protocol string, until a provider returns non-null,
or all providers have been exhausted.

If the previous step fails to find a protocol handler, the
constructor reads the value of the system property:

java.protocol.handler.pkgs

If the value of that system property is not

null

,
it is interpreted as a list of packages separated by a vertical
slash character '

|

'. The constructor tries to load
the class named:

<package>.<protocol>.Handler

where

<package>

is replaced by the name of the package
and

<protocol>

is replaced by the name of the protocol.
If this class does not exist, or if the class exists but it is not
a subclass of

URLStreamHandler

, then the next package
in the list is tried.

If the previous step fails to find a protocol handler, then the
constructor tries to load a built-in protocol handler.
If this class does not exist, or if the class exists but it is not a
subclass of

URLStreamHandler

, then a

MalformedURLException

is thrown.

Protocol handlers for the following protocols are guaranteed
to exist on the search path :-

```java
http, https, file, and jar
```

Protocol handlers for additional protocols may also be available.
Some protocol handlers, for example those used for loading platform
classes or classes on the class path, may not be overridden. The details
of such restrictions, and when those restrictions apply (during
initialization of the runtime for example), are implementation specific
and therefore not specified

No validation of the inputs is performed by this constructor.

If this is the first URL object being created with the specified
protocol, a

stream protocol handler

object, an instance of
class

URLStreamHandler

, is created for that protocol:

- If the application has previously set up an instance of

URLStreamHandlerFactory

as the stream handler factory,
then the

createURLStreamHandler

method of that instance
is called with the protocol string as an argument to create the
stream protocol handler.

If no

URLStreamHandlerFactory

has yet been set up,
or if the factory's

createURLStreamHandler

method
returns

null

, then the

ServiceLoader

mechanism is used to locate

URLStreamHandlerProvider

implementations using the system class
loader. The order that providers are located is implementation
specific, and an implementation is free to cache the located
providers. A

ServiceConfigurationError

,

Error

or

RuntimeException

thrown from the

createURLStreamHandler

, if encountered, will
be propagated to the calling thread. The

createURLStreamHandler

method of each provider, if instantiated, is
invoked, with the protocol string, until a provider returns non-null,
or all providers have been exhausted.

If the previous step fails to find a protocol handler, the
constructor reads the value of the system property:

java.protocol.handler.pkgs

If the value of that system property is not

null

,
it is interpreted as a list of packages separated by a vertical
slash character '

|

'. The constructor tries to load
the class named:

<package>.<protocol>.Handler

where

<package>

is replaced by the name of the package
and

<protocol>

is replaced by the name of the protocol.
If this class does not exist, or if the class exists but it is not
a subclass of

URLStreamHandler

, then the next package
in the list is tried.

If the previous step fails to find a protocol handler, then the
constructor tries to load a built-in protocol handler.
If this class does not exist, or if the class exists but it is not a
subclass of

URLStreamHandler

, then a

MalformedURLException

is thrown.

Protocol handlers for the following protocols are guaranteed
to exist on the search path :-

```java
http, https, file, and jar
```

Protocol handlers for additional protocols may also be available.
Some protocol handlers, for example those used for loading platform
classes or classes on the class path, may not be overridden. The details
of such restrictions, and when those restrictions apply (during
initialization of the runtime for example), are implementation specific
and therefore not specified

No validation of the inputs is performed by this constructor.

If the application has previously set up an instance of

URLStreamHandlerFactory

as the stream handler factory,
then the

createURLStreamHandler

method of that instance
is called with the protocol string as an argument to create the
stream protocol handler.

If no

URLStreamHandlerFactory

has yet been set up,
or if the factory's

createURLStreamHandler

method
returns

null

, then the

ServiceLoader

mechanism is used to locate

URLStreamHandlerProvider

implementations using the system class
loader. The order that providers are located is implementation
specific, and an implementation is free to cache the located
providers. A

ServiceConfigurationError

,

Error

or

RuntimeException

thrown from the

createURLStreamHandler

, if encountered, will
be propagated to the calling thread. The

createURLStreamHandler

method of each provider, if instantiated, is
invoked, with the protocol string, until a provider returns non-null,
or all providers have been exhausted.

If the previous step fails to find a protocol handler, the
constructor reads the value of the system property:

java.protocol.handler.pkgs

If the value of that system property is not

null

,
it is interpreted as a list of packages separated by a vertical
slash character '

|

'. The constructor tries to load
the class named:

<package>.<protocol>.Handler

where

<package>

is replaced by the name of the package
and

<protocol>

is replaced by the name of the protocol.
If this class does not exist, or if the class exists but it is not
a subclass of

URLStreamHandler

, then the next package
in the list is tried.

If the previous step fails to find a protocol handler, then the
constructor tries to load a built-in protocol handler.
If this class does not exist, or if the class exists but it is not a
subclass of

URLStreamHandler

, then a

MalformedURLException

is thrown.

Protocol handlers for the following protocols are guaranteed
to exist on the search path :-

```java
http, https, file, and jar
```

Protocol handlers for additional protocols may also be available.
Some protocol handlers, for example those used for loading platform
classes or classes on the class path, may not be overridden. The details
of such restrictions, and when those restrictions apply (during
initialization of the runtime for example), are implementation specific
and therefore not specified

No validation of the inputs is performed by this constructor.

http, https, file, and jar

No validation of the inputs is performed by this constructor.

URL

```java
public URL​(
String
protocol,

String
host,

String
file)
throws
MalformedURLException
```

Creates a URL from the specified

protocol

name,

host

name, and

file

name. The
default port for the specified protocol is used.

This constructor is equivalent to the four-argument
constructor with the only difference of using the
default port for the specified protocol.

No validation of the inputs is performed by this constructor.

**Parameters:** protocol

- the name of the protocol to use.
**Parameters:** host

- the name of the host.
**Parameters:** file

- the file on the host.
**Throws:** MalformedURLException

- if an unknown protocol is specified.
**See Also:** URL(java.lang.String, java.lang.String,
int, java.lang.String)

---

#### URL

public URL​(

String

protocol,

String

host,

String

file)
throws

MalformedURLException

Creates a URL from the specified

protocol

name,

host

name, and

file

name. The
default port for the specified protocol is used.

This constructor is equivalent to the four-argument
constructor with the only difference of using the
default port for the specified protocol.

No validation of the inputs is performed by this constructor.

This constructor is equivalent to the four-argument
constructor with the only difference of using the
default port for the specified protocol.

No validation of the inputs is performed by this constructor.

URL

```java
public URL​(
String
protocol,

String
host,
int port,

String
file,

URLStreamHandler
handler)
throws
MalformedURLException
```

Creates a

URL

object from the specified

protocol

,

host

,

port

number,

file

, and

handler

. Specifying
a

port

number of

-1

indicates that
the URL should use the default port for the protocol. Specifying
a

handler

of

null

indicates that the URL
should use a default stream handler for the protocol, as outlined
for:
java.net.URL#URL(java.lang.String, java.lang.String, int,
java.lang.String)

If the handler is not null and there is a security manager,
the security manager's

checkPermission

method is called with a

NetPermission("specifyStreamHandler")

permission.
This may result in a SecurityException.

No validation of the inputs is performed by this constructor.

**Parameters:** protocol

- the name of the protocol to use.
**Parameters:** host

- the name of the host.
**Parameters:** port

- the port number on the host.
**Parameters:** file

- the file on the host
**Parameters:** handler

- the stream handler for the URL.
**Throws:** MalformedURLException

- if an unknown protocol or the port
is a negative number other than -1
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
specifying a stream handler explicitly.
**See Also:** System.getProperty(java.lang.String)

,

setURLStreamHandlerFactory(
java.net.URLStreamHandlerFactory)

,

URLStreamHandler

,

URLStreamHandlerFactory.createURLStreamHandler(
java.lang.String)

,

SecurityManager.checkPermission(java.security.Permission)

,

NetPermission

---

#### URL

public URL​(

String

protocol,

String

host,
int port,

String

file,

URLStreamHandler

handler)
throws

MalformedURLException

Creates a

URL

object from the specified

protocol

,

host

,

port

number,

file

, and

handler

. Specifying
a

port

number of

-1

indicates that
the URL should use the default port for the protocol. Specifying
a

handler

of

null

indicates that the URL
should use a default stream handler for the protocol, as outlined
for:
java.net.URL#URL(java.lang.String, java.lang.String, int,
java.lang.String)

If the handler is not null and there is a security manager,
the security manager's

checkPermission

method is called with a

NetPermission("specifyStreamHandler")

permission.
This may result in a SecurityException.

No validation of the inputs is performed by this constructor.

If the handler is not null and there is a security manager,
the security manager's

checkPermission

method is called with a

NetPermission("specifyStreamHandler")

permission.
This may result in a SecurityException.

No validation of the inputs is performed by this constructor.

URL

```java
public URL​(
String
spec)
throws
MalformedURLException
```

Creates a

URL

object from the

String

representation.

This constructor is equivalent to a call to the two-argument
constructor with a

null

first argument.

**Parameters:** spec

- the

String

to parse as a URL.
**Throws:** MalformedURLException

- if no protocol is specified, or an
unknown protocol is found, or

spec

is

null

,
or the parsed URL fails to comply with the specific syntax
of the associated protocol.
**See Also:** URL(java.net.URL, java.lang.String)

---

#### URL

public URL​(

String

spec)
throws

MalformedURLException

Creates a

URL

object from the

String

representation.

This constructor is equivalent to a call to the two-argument
constructor with a

null

first argument.

This constructor is equivalent to a call to the two-argument
constructor with a

null

first argument.

URL

```java
public URL​(
URL
context,

String
spec)
throws
MalformedURLException
```

Creates a URL by parsing the given spec within a specified context.

The new URL is created from the given context URL and the spec
argument as described in
RFC2396 "Uniform Resource Identifiers : Generic * Syntax" :

```java
<scheme>://<authority><path>?<query>#<fragment>
```

The reference is parsed into the scheme, authority, path, query and
fragment parts. If the path component is empty and the scheme,
authority, and query components are undefined, then the new URL is a
reference to the current document. Otherwise, the fragment and query
parts present in the spec are used in the new URL.

If the scheme component is defined in the given spec and does not match
the scheme of the context, then the new URL is created as an absolute
URL based on the spec alone. Otherwise the scheme component is inherited
from the context URL.

If the authority component is present in the spec then the spec is
treated as absolute and the spec authority and path will replace the
context authority and path. If the authority component is absent in the
spec then the authority of the new URL will be inherited from the
context.

If the spec's path component begins with a slash character
"/" then the
path is treated as absolute and the spec path replaces the context path.

Otherwise, the path is treated as a relative path and is appended to the
context path, as described in RFC2396. Also, in this case,
the path is canonicalized through the removal of directory
changes made by occurrences of ".." and ".".

For a more detailed description of URL parsing, refer to RFC2396.

**Parameters:** context

- the context in which to parse the specification.
**Parameters:** spec

- the

String

to parse as a URL.
**Throws:** MalformedURLException

- if no protocol is specified, or an
unknown protocol is found, or

spec

is

null

,
or the parsed URL fails to comply with the specific syntax
of the associated protocol.
**See Also:** URL(java.lang.String, java.lang.String,
int, java.lang.String)

,

URLStreamHandler

,

URLStreamHandler.parseURL(java.net.URL,
java.lang.String, int, int)

---

#### URL

public URL​(

URL

context,

String

spec)
throws

MalformedURLException

Creates a URL by parsing the given spec within a specified context.

The new URL is created from the given context URL and the spec
argument as described in
RFC2396 "Uniform Resource Identifiers : Generic * Syntax" :

```java
<scheme>://<authority><path>?<query>#<fragment>
```

The reference is parsed into the scheme, authority, path, query and
fragment parts. If the path component is empty and the scheme,
authority, and query components are undefined, then the new URL is a
reference to the current document. Otherwise, the fragment and query
parts present in the spec are used in the new URL.

If the scheme component is defined in the given spec and does not match
the scheme of the context, then the new URL is created as an absolute
URL based on the spec alone. Otherwise the scheme component is inherited
from the context URL.

If the authority component is present in the spec then the spec is
treated as absolute and the spec authority and path will replace the
context authority and path. If the authority component is absent in the
spec then the authority of the new URL will be inherited from the
context.

If the spec's path component begins with a slash character
"/" then the
path is treated as absolute and the spec path replaces the context path.

Otherwise, the path is treated as a relative path and is appended to the
context path, as described in RFC2396. Also, in this case,
the path is canonicalized through the removal of directory
changes made by occurrences of ".." and ".".

For a more detailed description of URL parsing, refer to RFC2396.

<scheme>://<authority><path>?<query>#<fragment>

If the scheme component is defined in the given spec and does not match
the scheme of the context, then the new URL is created as an absolute
URL based on the spec alone. Otherwise the scheme component is inherited
from the context URL.

If the authority component is present in the spec then the spec is
treated as absolute and the spec authority and path will replace the
context authority and path. If the authority component is absent in the
spec then the authority of the new URL will be inherited from the
context.

If the spec's path component begins with a slash character
"/" then the
path is treated as absolute and the spec path replaces the context path.

Otherwise, the path is treated as a relative path and is appended to the
context path, as described in RFC2396. Also, in this case,
the path is canonicalized through the removal of directory
changes made by occurrences of ".." and ".".

For a more detailed description of URL parsing, refer to RFC2396.

If the authority component is present in the spec then the spec is
treated as absolute and the spec authority and path will replace the
context authority and path. If the authority component is absent in the
spec then the authority of the new URL will be inherited from the
context.

If the spec's path component begins with a slash character
"/" then the
path is treated as absolute and the spec path replaces the context path.

Otherwise, the path is treated as a relative path and is appended to the
context path, as described in RFC2396. Also, in this case,
the path is canonicalized through the removal of directory
changes made by occurrences of ".." and ".".

For a more detailed description of URL parsing, refer to RFC2396.

If the spec's path component begins with a slash character
"/" then the
path is treated as absolute and the spec path replaces the context path.

Otherwise, the path is treated as a relative path and is appended to the
context path, as described in RFC2396. Also, in this case,
the path is canonicalized through the removal of directory
changes made by occurrences of ".." and ".".

For a more detailed description of URL parsing, refer to RFC2396.

Otherwise, the path is treated as a relative path and is appended to the
context path, as described in RFC2396. Also, in this case,
the path is canonicalized through the removal of directory
changes made by occurrences of ".." and ".".

For a more detailed description of URL parsing, refer to RFC2396.

For a more detailed description of URL parsing, refer to RFC2396.

URL

```java
public URL​(
URL
context,

String
spec,

URLStreamHandler
handler)
throws
MalformedURLException
```

Creates a URL by parsing the given spec with the specified handler
within a specified context. If the handler is null, the parsing
occurs as with the two argument constructor.

**Parameters:** context

- the context in which to parse the specification.
**Parameters:** spec

- the

String

to parse as a URL.
**Parameters:** handler

- the stream handler for the URL.
**Throws:** MalformedURLException

- if no protocol is specified, or an
unknown protocol is found, or

spec

is

null

,
or the parsed URL fails to comply with the specific syntax
of the associated protocol.
**Throws:** SecurityException

- if a security manager exists and its

checkPermission

method doesn't allow
specifying a stream handler.
**See Also:** URL(java.lang.String, java.lang.String,
int, java.lang.String)

,

URLStreamHandler

,

URLStreamHandler.parseURL(java.net.URL,
java.lang.String, int, int)

---

#### URL

public URL​(

URL

context,

String

spec,

URLStreamHandler

handler)
throws

MalformedURLException

Creates a URL by parsing the given spec with the specified handler
within a specified context. If the handler is null, the parsing
occurs as with the two argument constructor.

Method Detail

- getQuery

```java
public
String
getQuery()
```

Gets the query part of this

URL

.

**Returns:** the query part of this

URL

,
or

null

if one does not exist
**Since:** 1.3

- getPath

```java
public
String
getPath()
```

Gets the path part of this

URL

.

**Returns:** the path part of this

URL

, or an
empty string if one does not exist
**Since:** 1.3

- getUserInfo

```java
public
String
getUserInfo()
```

Gets the userInfo part of this

URL

.

**Returns:** the userInfo part of this

URL

, or

null

if one does not exist
**Since:** 1.3

- getAuthority

```java
public
String
getAuthority()
```

Gets the authority part of this

URL

.

**Returns:** the authority part of this

URL
**Since:** 1.3

- getPort

```java
public int getPort()
```

Gets the port number of this

URL

.

**Returns:** the port number, or -1 if the port is not set

- getDefaultPort

```java
public int getDefaultPort()
```

Gets the default port number of the protocol associated
with this

URL

. If the URL scheme or the URLStreamHandler
for the URL do not define a default port number,
then -1 is returned.

**Returns:** the port number
**Since:** 1.4

- getProtocol

```java
public
String
getProtocol()
```

Gets the protocol name of this

URL

.

**Returns:** the protocol of this

URL

.

- getHost

```java
public
String
getHost()
```

Gets the host name of this

URL

, if applicable.
The format of the host conforms to RFC 2732, i.e. for a
literal IPv6 address, this method will return the IPv6 address
enclosed in square brackets (

'['

and

']'

).

**Returns:** the host name of this

URL

.

- getFile

```java
public
String
getFile()
```

Gets the file name of this

URL

.
The returned file portion will be
the same as

getPath()

, plus the concatenation of
the value of

getQuery()

, if any. If there is
no query portion, this method and

getPath()

will
return identical results.

**Returns:** the file name of this

URL

,
or an empty string if one does not exist

- getRef

```java
public
String
getRef()
```

Gets the anchor (also known as the "reference") of this

URL

.

**Returns:** the anchor (also known as the "reference") of this

URL

, or

null

if one does not exist

- equals

```java
public boolean equals​(
Object
obj)
```

Compares this URL for equality with another object.

If the given object is not a URL then this method immediately returns

false

.

Two URL objects are equal if they have the same protocol, reference
equivalent hosts, have the same port number on the host, and the same
file and fragment of the file.

Two hosts are considered equivalent if both host names can be resolved
into the same IP addresses; else if either host name can't be
resolved, the host names must be equal without regard to case; or both
host names equal to null.

Since hosts comparison requires name resolution, this operation is a
blocking operation.

Note: The defined behavior for

equals

is known to
be inconsistent with virtual hosting in HTTP.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the URL to compare against.
**Returns:** true

if the objects are the same;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

- hashCode

```java
public int hashCode()
```

Creates an integer suitable for hash table indexing.

The hash code is based upon all the URL components relevant for URL
comparison. As such, this operation is a blocking operation.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

URL

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

- sameFile

```java
public boolean sameFile​(
URL
other)
```

Compares two URLs, excluding the fragment component.

Returns

true

if this

URL

and the

other

argument are equal without taking the
fragment component into consideration.

**Parameters:** other

- the

URL

to compare against.
**Returns:** true

if they reference the same remote object;

false

otherwise.

- toString

```java
public
String
toString()
```

Constructs a string representation of this

URL

. The
string is created by calling the

toExternalForm

method of the stream protocol handler for this object.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this object.
**See Also:** URL(java.lang.String, java.lang.String, int,
java.lang.String)

,

URLStreamHandler.toExternalForm(java.net.URL)

- toExternalForm

```java
public
String
toExternalForm()
```

Constructs a string representation of this

URL

. The
string is created by calling the

toExternalForm

method of the stream protocol handler for this object.

**Returns:** a string representation of this object.
**See Also:** URL(java.lang.String, java.lang.String,
int, java.lang.String)

,

URLStreamHandler.toExternalForm(java.net.URL)

- toURI

```java
public
URI
toURI()
throws
URISyntaxException
```

Returns a

URI

equivalent to this URL.
This method functions in the same way as

new URI (this.toString())

.

Note, any URL instance that complies with RFC 2396 can be converted
to a URI. However, some URLs that are not strictly in compliance
can not be converted to a URI.

**Returns:** a URI instance equivalent to this URL.
**Throws:** URISyntaxException

- if this URL is not formatted strictly according to
to RFC2396 and cannot be converted to a URI.
**Since:** 1.5

- openConnection

```java
public
URLConnection
openConnection()
throws
IOException
```

Returns a

URLConnection

instance that
represents a connection to the remote object referred to by the

URL

.

A new instance of

URLConnection

is
created every time when invoking the

URLStreamHandler.openConnection(URL)

method of the protocol handler for
this URL.

It should be noted that a URLConnection instance does not establish
the actual network connection on creation. This will happen only when
calling

URLConnection.connect()

.

If for the URL's protocol (such as HTTP or JAR), there
exists a public, specialized URLConnection subclass belonging
to one of the following packages or one of their subpackages:
java.lang, java.io, java.util, java.net, the connection
returned will be of that subclass. For example, for HTTP an
HttpURLConnection will be returned, and for JAR a
JarURLConnection will be returned.

**Returns:** a

URLConnection

linking
to the URL.
**Throws:** IOException

- if an I/O exception occurs.
**See Also:** URL(java.lang.String, java.lang.String,
int, java.lang.String)

- openConnection

```java
public
URLConnection
openConnection​(
Proxy
proxy)
throws
IOException
```

Same as

openConnection()

, except that the connection will be
made through the specified proxy; Protocol handlers that do not
support proxing will ignore the proxy parameter and make a
normal connection.

Invoking this method preempts the system's default

ProxySelector

settings.

**Parameters:** proxy

- the Proxy through which this connection
will be made. If direct connection is desired,
Proxy.NO_PROXY should be specified.
**Returns:** a

URLConnection

to the URL.
**Throws:** IOException

- if an I/O exception occurs.
**Throws:** SecurityException

- if a security manager is present
and the caller doesn't have permission to connect
to the proxy.
**Throws:** IllegalArgumentException

- will be thrown if proxy is null,
or proxy has the wrong type
**Throws:** UnsupportedOperationException

- if the subclass that
implements the protocol handler doesn't support
this method.
**Since:** 1.5
**See Also:** URL(java.lang.String, java.lang.String,
int, java.lang.String)

,

URLConnection

,

URLStreamHandler.openConnection(java.net.URL,
java.net.Proxy)

- openStream

```java
public final
InputStream
openStream()
throws
IOException
```

Opens a connection to this

URL

and returns an

InputStream

for reading from that connection. This
method is a shorthand for:

```java
openConnection().getInputStream()
```

**Returns:** an input stream for reading from the URL connection.
**Throws:** IOException

- if an I/O exception occurs.
**See Also:** openConnection()

,

URLConnection.getInputStream()

- getContent

```java
public final
Object
getContent()
throws
IOException
```

Gets the contents of this URL. This method is a shorthand for:

```java
openConnection().getContent()
```

**Returns:** the contents of this URL.
**Throws:** IOException

- if an I/O exception occurs.
**See Also:** URLConnection.getContent()

- getContent

```java
public final
Object
getContent​(
Class
<?>[] classes)
throws
IOException
```

Gets the contents of this URL. This method is a shorthand for:

```java
openConnection().getContent(classes)
```

**Parameters:** classes

- an array of Java types
**Returns:** the content object of this URL that is the first match of
the types specified in the classes array.
null if none of the requested types are supported.
**Throws:** IOException

- if an I/O exception occurs.
**Since:** 1.3
**See Also:** URLConnection.getContent(Class[])

- setURLStreamHandlerFactory

```java
public static void setURLStreamHandlerFactory​(
URLStreamHandlerFactory
fac)
```

Sets an application's

URLStreamHandlerFactory

.
This method can be called at most once in a given Java Virtual
Machine.

The

URLStreamHandlerFactory

instance is used to
construct a stream protocol handler from a protocol name.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:** fac

- the desired factory.
**Throws:** Error

- if the application has already set a factory.
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't allow
the operation.
**See Also:** URL(java.lang.String, java.lang.String,
int, java.lang.String)

,

URLStreamHandlerFactory

,

SecurityManager.checkSetFactory()

---

#### Method Detail

getQuery

```java
public
String
getQuery()
```

Gets the query part of this

URL

.

**Returns:** the query part of this

URL

,
or

null

if one does not exist
**Since:** 1.3

---

#### getQuery

public

String

getQuery()

Gets the query part of this

URL

.

getPath

```java
public
String
getPath()
```

Gets the path part of this

URL

.

**Returns:** the path part of this

URL

, or an
empty string if one does not exist
**Since:** 1.3

---

#### getPath

public

String

getPath()

Gets the path part of this

URL

.

getUserInfo

```java
public
String
getUserInfo()
```

Gets the userInfo part of this

URL

.

**Returns:** the userInfo part of this

URL

, or

null

if one does not exist
**Since:** 1.3

---

#### getUserInfo

public

String

getUserInfo()

Gets the userInfo part of this

URL

.

getAuthority

```java
public
String
getAuthority()
```

Gets the authority part of this

URL

.

**Returns:** the authority part of this

URL
**Since:** 1.3

---

#### getAuthority

public

String

getAuthority()

Gets the authority part of this

URL

.

getPort

```java
public int getPort()
```

Gets the port number of this

URL

.

**Returns:** the port number, or -1 if the port is not set

---

#### getPort

public int getPort()

Gets the port number of this

URL

.

getDefaultPort

```java
public int getDefaultPort()
```

Gets the default port number of the protocol associated
with this

URL

. If the URL scheme or the URLStreamHandler
for the URL do not define a default port number,
then -1 is returned.

**Returns:** the port number
**Since:** 1.4

---

#### getDefaultPort

public int getDefaultPort()

Gets the default port number of the protocol associated
with this

URL

. If the URL scheme or the URLStreamHandler
for the URL do not define a default port number,
then -1 is returned.

getProtocol

```java
public
String
getProtocol()
```

Gets the protocol name of this

URL

.

**Returns:** the protocol of this

URL

.

---

#### getProtocol

public

String

getProtocol()

Gets the protocol name of this

URL

.

getHost

```java
public
String
getHost()
```

Gets the host name of this

URL

, if applicable.
The format of the host conforms to RFC 2732, i.e. for a
literal IPv6 address, this method will return the IPv6 address
enclosed in square brackets (

'['

and

']'

).

**Returns:** the host name of this

URL

.

---

#### getHost

public

String

getHost()

Gets the host name of this

URL

, if applicable.
The format of the host conforms to RFC 2732, i.e. for a
literal IPv6 address, this method will return the IPv6 address
enclosed in square brackets (

'['

and

']'

).

getFile

```java
public
String
getFile()
```

Gets the file name of this

URL

.
The returned file portion will be
the same as

getPath()

, plus the concatenation of
the value of

getQuery()

, if any. If there is
no query portion, this method and

getPath()

will
return identical results.

**Returns:** the file name of this

URL

,
or an empty string if one does not exist

---

#### getFile

public

String

getFile()

Gets the file name of this

URL

.
The returned file portion will be
the same as

getPath()

, plus the concatenation of
the value of

getQuery()

, if any. If there is
no query portion, this method and

getPath()

will
return identical results.

getRef

```java
public
String
getRef()
```

Gets the anchor (also known as the "reference") of this

URL

.

**Returns:** the anchor (also known as the "reference") of this

URL

, or

null

if one does not exist

---

#### getRef

public

String

getRef()

Gets the anchor (also known as the "reference") of this

URL

.

equals

```java
public boolean equals​(
Object
obj)
```

Compares this URL for equality with another object.

If the given object is not a URL then this method immediately returns

false

.

Two URL objects are equal if they have the same protocol, reference
equivalent hosts, have the same port number on the host, and the same
file and fragment of the file.

Two hosts are considered equivalent if both host names can be resolved
into the same IP addresses; else if either host name can't be
resolved, the host names must be equal without regard to case; or both
host names equal to null.

Since hosts comparison requires name resolution, this operation is a
blocking operation.

Note: The defined behavior for

equals

is known to
be inconsistent with virtual hosting in HTTP.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the URL to compare against.
**Returns:** true

if the objects are the same;

false

otherwise.
**See Also:** Object.hashCode()

,

HashMap

---

#### equals

public boolean equals​(

Object

obj)

Compares this URL for equality with another object.

If the given object is not a URL then this method immediately returns

false

.

Two URL objects are equal if they have the same protocol, reference
equivalent hosts, have the same port number on the host, and the same
file and fragment of the file.

Two hosts are considered equivalent if both host names can be resolved
into the same IP addresses; else if either host name can't be
resolved, the host names must be equal without regard to case; or both
host names equal to null.

Since hosts comparison requires name resolution, this operation is a
blocking operation.

Note: The defined behavior for

equals

is known to
be inconsistent with virtual hosting in HTTP.

If the given object is not a URL then this method immediately returns

false

.

Two URL objects are equal if they have the same protocol, reference
equivalent hosts, have the same port number on the host, and the same
file and fragment of the file.

Two hosts are considered equivalent if both host names can be resolved
into the same IP addresses; else if either host name can't be
resolved, the host names must be equal without regard to case; or both
host names equal to null.

Since hosts comparison requires name resolution, this operation is a
blocking operation.

Note: The defined behavior for

equals

is known to
be inconsistent with virtual hosting in HTTP.

Two URL objects are equal if they have the same protocol, reference
equivalent hosts, have the same port number on the host, and the same
file and fragment of the file.

Two hosts are considered equivalent if both host names can be resolved
into the same IP addresses; else if either host name can't be
resolved, the host names must be equal without regard to case; or both
host names equal to null.

Since hosts comparison requires name resolution, this operation is a
blocking operation.

Note: The defined behavior for

equals

is known to
be inconsistent with virtual hosting in HTTP.

Two hosts are considered equivalent if both host names can be resolved
into the same IP addresses; else if either host name can't be
resolved, the host names must be equal without regard to case; or both
host names equal to null.

Since hosts comparison requires name resolution, this operation is a
blocking operation.

Note: The defined behavior for

equals

is known to
be inconsistent with virtual hosting in HTTP.

Since hosts comparison requires name resolution, this operation is a
blocking operation.

Note: The defined behavior for

equals

is known to
be inconsistent with virtual hosting in HTTP.

Note: The defined behavior for

equals

is known to
be inconsistent with virtual hosting in HTTP.

hashCode

```java
public int hashCode()
```

Creates an integer suitable for hash table indexing.

The hash code is based upon all the URL components relevant for URL
comparison. As such, this operation is a blocking operation.

**Overrides:** hashCode

in class

Object
**Returns:** a hash code for this

URL

.
**See Also:** Object.equals(java.lang.Object)

,

System.identityHashCode(java.lang.Object)

---

#### hashCode

public int hashCode()

Creates an integer suitable for hash table indexing.

The hash code is based upon all the URL components relevant for URL
comparison. As such, this operation is a blocking operation.

The hash code is based upon all the URL components relevant for URL
comparison. As such, this operation is a blocking operation.

sameFile

```java
public boolean sameFile​(
URL
other)
```

Compares two URLs, excluding the fragment component.

Returns

true

if this

URL

and the

other

argument are equal without taking the
fragment component into consideration.

**Parameters:** other

- the

URL

to compare against.
**Returns:** true

if they reference the same remote object;

false

otherwise.

---

#### sameFile

public boolean sameFile​(

URL

other)

Compares two URLs, excluding the fragment component.

Returns

true

if this

URL

and the

other

argument are equal without taking the
fragment component into consideration.

Returns

true

if this

URL

and the

other

argument are equal without taking the
fragment component into consideration.

toString

```java
public
String
toString()
```

Constructs a string representation of this

URL

. The
string is created by calling the

toExternalForm

method of the stream protocol handler for this object.

**Overrides:** toString

in class

Object
**Returns:** a string representation of this object.
**See Also:** URL(java.lang.String, java.lang.String, int,
java.lang.String)

,

URLStreamHandler.toExternalForm(java.net.URL)

---

#### toString

public

String

toString()

Constructs a string representation of this

URL

. The
string is created by calling the

toExternalForm

method of the stream protocol handler for this object.

toExternalForm

```java
public
String
toExternalForm()
```

Constructs a string representation of this

URL

. The
string is created by calling the

toExternalForm

method of the stream protocol handler for this object.

**Returns:** a string representation of this object.
**See Also:** URL(java.lang.String, java.lang.String,
int, java.lang.String)

,

URLStreamHandler.toExternalForm(java.net.URL)

---

#### toExternalForm

public

String

toExternalForm()

Constructs a string representation of this

URL

. The
string is created by calling the

toExternalForm

method of the stream protocol handler for this object.

toURI

```java
public
URI
toURI()
throws
URISyntaxException
```

Returns a

URI

equivalent to this URL.
This method functions in the same way as

new URI (this.toString())

.

Note, any URL instance that complies with RFC 2396 can be converted
to a URI. However, some URLs that are not strictly in compliance
can not be converted to a URI.

**Returns:** a URI instance equivalent to this URL.
**Throws:** URISyntaxException

- if this URL is not formatted strictly according to
to RFC2396 and cannot be converted to a URI.
**Since:** 1.5

---

#### toURI

public

URI

toURI()
throws

URISyntaxException

Returns a

URI

equivalent to this URL.
This method functions in the same way as

new URI (this.toString())

.

Note, any URL instance that complies with RFC 2396 can be converted
to a URI. However, some URLs that are not strictly in compliance
can not be converted to a URI.

Note, any URL instance that complies with RFC 2396 can be converted
to a URI. However, some URLs that are not strictly in compliance
can not be converted to a URI.

openConnection

```java
public
URLConnection
openConnection()
throws
IOException
```

Returns a

URLConnection

instance that
represents a connection to the remote object referred to by the

URL

.

A new instance of

URLConnection

is
created every time when invoking the

URLStreamHandler.openConnection(URL)

method of the protocol handler for
this URL.

It should be noted that a URLConnection instance does not establish
the actual network connection on creation. This will happen only when
calling

URLConnection.connect()

.

If for the URL's protocol (such as HTTP or JAR), there
exists a public, specialized URLConnection subclass belonging
to one of the following packages or one of their subpackages:
java.lang, java.io, java.util, java.net, the connection
returned will be of that subclass. For example, for HTTP an
HttpURLConnection will be returned, and for JAR a
JarURLConnection will be returned.

**Returns:** a

URLConnection

linking
to the URL.
**Throws:** IOException

- if an I/O exception occurs.
**See Also:** URL(java.lang.String, java.lang.String,
int, java.lang.String)

---

#### openConnection

public

URLConnection

openConnection()
throws

IOException

Returns a

URLConnection

instance that
represents a connection to the remote object referred to by the

URL

.

A new instance of

URLConnection

is
created every time when invoking the

URLStreamHandler.openConnection(URL)

method of the protocol handler for
this URL.

It should be noted that a URLConnection instance does not establish
the actual network connection on creation. This will happen only when
calling

URLConnection.connect()

.

If for the URL's protocol (such as HTTP or JAR), there
exists a public, specialized URLConnection subclass belonging
to one of the following packages or one of their subpackages:
java.lang, java.io, java.util, java.net, the connection
returned will be of that subclass. For example, for HTTP an
HttpURLConnection will be returned, and for JAR a
JarURLConnection will be returned.

A new instance of

URLConnection

is
created every time when invoking the

URLStreamHandler.openConnection(URL)

method of the protocol handler for
this URL.

It should be noted that a URLConnection instance does not establish
the actual network connection on creation. This will happen only when
calling

URLConnection.connect()

.

If for the URL's protocol (such as HTTP or JAR), there
exists a public, specialized URLConnection subclass belonging
to one of the following packages or one of their subpackages:
java.lang, java.io, java.util, java.net, the connection
returned will be of that subclass. For example, for HTTP an
HttpURLConnection will be returned, and for JAR a
JarURLConnection will be returned.

openConnection

```java
public
URLConnection
openConnection​(
Proxy
proxy)
throws
IOException
```

Same as

openConnection()

, except that the connection will be
made through the specified proxy; Protocol handlers that do not
support proxing will ignore the proxy parameter and make a
normal connection.

Invoking this method preempts the system's default

ProxySelector

settings.

**Parameters:** proxy

- the Proxy through which this connection
will be made. If direct connection is desired,
Proxy.NO_PROXY should be specified.
**Returns:** a

URLConnection

to the URL.
**Throws:** IOException

- if an I/O exception occurs.
**Throws:** SecurityException

- if a security manager is present
and the caller doesn't have permission to connect
to the proxy.
**Throws:** IllegalArgumentException

- will be thrown if proxy is null,
or proxy has the wrong type
**Throws:** UnsupportedOperationException

- if the subclass that
implements the protocol handler doesn't support
this method.
**Since:** 1.5
**See Also:** URL(java.lang.String, java.lang.String,
int, java.lang.String)

,

URLConnection

,

URLStreamHandler.openConnection(java.net.URL,
java.net.Proxy)

---

#### openConnection

public

URLConnection

openConnection​(

Proxy

proxy)
throws

IOException

Same as

openConnection()

, except that the connection will be
made through the specified proxy; Protocol handlers that do not
support proxing will ignore the proxy parameter and make a
normal connection.

Invoking this method preempts the system's default

ProxySelector

settings.

openStream

```java
public final
InputStream
openStream()
throws
IOException
```

Opens a connection to this

URL

and returns an

InputStream

for reading from that connection. This
method is a shorthand for:

```java
openConnection().getInputStream()
```

**Returns:** an input stream for reading from the URL connection.
**Throws:** IOException

- if an I/O exception occurs.
**See Also:** openConnection()

,

URLConnection.getInputStream()

---

#### openStream

public final

InputStream

openStream()
throws

IOException

Opens a connection to this

URL

and returns an

InputStream

for reading from that connection. This
method is a shorthand for:

```java
openConnection().getInputStream()
```

openConnection().getInputStream()

getContent

```java
public final
Object
getContent()
throws
IOException
```

Gets the contents of this URL. This method is a shorthand for:

```java
openConnection().getContent()
```

**Returns:** the contents of this URL.
**Throws:** IOException

- if an I/O exception occurs.
**See Also:** URLConnection.getContent()

---

#### getContent

public final

Object

getContent()
throws

IOException

Gets the contents of this URL. This method is a shorthand for:

```java
openConnection().getContent()
```

openConnection().getContent()

getContent

```java
public final
Object
getContent​(
Class
<?>[] classes)
throws
IOException
```

Gets the contents of this URL. This method is a shorthand for:

```java
openConnection().getContent(classes)
```

**Parameters:** classes

- an array of Java types
**Returns:** the content object of this URL that is the first match of
the types specified in the classes array.
null if none of the requested types are supported.
**Throws:** IOException

- if an I/O exception occurs.
**Since:** 1.3
**See Also:** URLConnection.getContent(Class[])

---

#### getContent

public final

Object

getContent​(

Class

<?>[] classes)
throws

IOException

Gets the contents of this URL. This method is a shorthand for:

```java
openConnection().getContent(classes)
```

openConnection().getContent(classes)

setURLStreamHandlerFactory

```java
public static void setURLStreamHandlerFactory​(
URLStreamHandlerFactory
fac)
```

Sets an application's

URLStreamHandlerFactory

.
This method can be called at most once in a given Java Virtual
Machine.

The

URLStreamHandlerFactory

instance is used to
construct a stream protocol handler from a protocol name.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:** fac

- the desired factory.
**Throws:** Error

- if the application has already set a factory.
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't allow
the operation.
**See Also:** URL(java.lang.String, java.lang.String,
int, java.lang.String)

,

URLStreamHandlerFactory

,

SecurityManager.checkSetFactory()

---

#### setURLStreamHandlerFactory

public static void setURLStreamHandlerFactory​(

URLStreamHandlerFactory

fac)

Sets an application's

URLStreamHandlerFactory

.
This method can be called at most once in a given Java Virtual
Machine.

The

URLStreamHandlerFactory

instance is used to
construct a stream protocol handler from a protocol name.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a SecurityException.

The

URLStreamHandlerFactory

instance is used to
construct a stream protocol handler from a protocol name.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a SecurityException.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a SecurityException.

---

