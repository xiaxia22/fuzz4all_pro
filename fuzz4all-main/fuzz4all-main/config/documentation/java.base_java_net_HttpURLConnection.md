# Class HttpURLConnection

**Source:** `java.base\java\net\HttpURLConnection.html`

### Class Description

```java
public abstract class
HttpURLConnection

extends
URLConnection
```

A URLConnection with support for HTTP-specific features. See

the spec

for
details.

Each HttpURLConnection instance is used to make a single request
but the underlying network connection to the HTTP server may be
transparently shared by other instances. Calling the close() methods
on the InputStream or OutputStream of an HttpURLConnection
after a request may free network resources associated with this
instance but has no effect on any shared persistent connection.
Calling the disconnect() method may close the underlying socket
if a persistent connection is otherwise idle at that time.

The HTTP protocol handler has a few settings that can be accessed through
System Properties. This covers

Proxy settings

as well as

various other settings

.

Security permissions

If a security manager is installed, and if a method is called which results in an
attempt to open a connection, the caller must possess either:

- a "connect"

SocketPermission

to the host/port combination of the
destination URL or
- a

URLPermission

that permits this request.

If automatic redirection is enabled, and this request is redirected to another
destination, then the caller must also have permission to connect to the
redirected host/URL.

**Direct Known Subclasses:** HttpsURLConnection

---

### Field Details

#### protected
String
method

The HTTP method (GET,POST,PUT,etc.).

---

#### protected int chunkLength

The chunk-length when using chunked encoding streaming mode for output.
A value of

-1

means chunked encoding is disabled for output.

**Since:**
- 1.5

---

#### protected int fixedContentLength

The fixed content-length when using fixed-length streaming mode.
A value of

-1

means fixed-length streaming mode is disabled
for output.

NOTE:

fixedContentLengthLong

is recommended instead
of this field, as it allows larger content lengths to be set.

**Since:**
- 1.5

---

#### protected long fixedContentLengthLong

The fixed content-length when using fixed-length streaming mode.
A value of

-1

means fixed-length streaming mode is disabled
for output.

**Since:**
- 1.7

---

#### protected int responseCode

An

int

representing the three digit HTTP Status-Code.

- 1xx: Informational

2xx: Success

3xx: Redirection

4xx: Client Error

5xx: Server Error

---

#### protected
String
responseMessage

The HTTP response message.

---

#### protected boolean instanceFollowRedirects

If

true

, the protocol will automatically follow redirects.
If

false

, the protocol will not automatically follow
redirects.

This field is set by the

setInstanceFollowRedirects

method. Its value is returned by the

getInstanceFollowRedirects

method.

Its default value is based on the value of the static followRedirects
at HttpURLConnection construction time.

**See Also:**
- setInstanceFollowRedirects(boolean)

,

getInstanceFollowRedirects()

,

setFollowRedirects(boolean)

---

#### public static final int HTTP_OK

HTTP Status-Code 200: OK.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_CREATED

HTTP Status-Code 201: Created.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_ACCEPTED

HTTP Status-Code 202: Accepted.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_NOT_AUTHORITATIVE

HTTP Status-Code 203: Non-Authoritative Information.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_NO_CONTENT

HTTP Status-Code 204: No Content.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_RESET

HTTP Status-Code 205: Reset Content.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_PARTIAL

HTTP Status-Code 206: Partial Content.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_MULT_CHOICE

HTTP Status-Code 300: Multiple Choices.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_MOVED_PERM

HTTP Status-Code 301: Moved Permanently.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_MOVED_TEMP

HTTP Status-Code 302: Temporary Redirect.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_SEE_OTHER

HTTP Status-Code 303: See Other.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_NOT_MODIFIED

HTTP Status-Code 304: Not Modified.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_USE_PROXY

HTTP Status-Code 305: Use Proxy.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_BAD_REQUEST

HTTP Status-Code 400: Bad Request.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_UNAUTHORIZED

HTTP Status-Code 401: Unauthorized.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_PAYMENT_REQUIRED

HTTP Status-Code 402: Payment Required.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_FORBIDDEN

HTTP Status-Code 403: Forbidden.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_NOT_FOUND

HTTP Status-Code 404: Not Found.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_BAD_METHOD

HTTP Status-Code 405: Method Not Allowed.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_NOT_ACCEPTABLE

HTTP Status-Code 406: Not Acceptable.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_PROXY_AUTH

HTTP Status-Code 407: Proxy Authentication Required.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_CLIENT_TIMEOUT

HTTP Status-Code 408: Request Time-Out.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_CONFLICT

HTTP Status-Code 409: Conflict.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_GONE

HTTP Status-Code 410: Gone.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_LENGTH_REQUIRED

HTTP Status-Code 411: Length Required.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_PRECON_FAILED

HTTP Status-Code 412: Precondition Failed.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_ENTITY_TOO_LARGE

HTTP Status-Code 413: Request Entity Too Large.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_REQ_TOO_LONG

HTTP Status-Code 414: Request-URI Too Large.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_UNSUPPORTED_TYPE

HTTP Status-Code 415: Unsupported Media Type.

**See Also:**
- Constant Field Values

---

#### @Deprecated

public static final int HTTP_SERVER_ERROR

HTTP Status-Code 500: Internal Server Error.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_INTERNAL_ERROR

HTTP Status-Code 500: Internal Server Error.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_NOT_IMPLEMENTED

HTTP Status-Code 501: Not Implemented.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_BAD_GATEWAY

HTTP Status-Code 502: Bad Gateway.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_UNAVAILABLE

HTTP Status-Code 503: Service Unavailable.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_GATEWAY_TIMEOUT

HTTP Status-Code 504: Gateway Timeout.

**See Also:**
- Constant Field Values

---

#### public static final int HTTP_VERSION

HTTP Status-Code 505: HTTP Version Not Supported.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### protected HttpURLConnection​(
URL
u)

Constructor for the HttpURLConnection.

**Parameters:**
- u

- the URL

---

### Method Details

#### public void setAuthenticator​(
Authenticator
auth)

Supplies an

Authenticator

to be used
when authentication is requested through the HTTP protocol for
this

HttpURLConnection

.
If no authenticator is supplied, the

default
authenticator

will be used.

**Parameters:**
- auth

- The

Authenticator

that should be used by this

HttpURLConnection

.

**Throws:**
- UnsupportedOperationException

- if setting an Authenticator is
not supported by the underlying implementation.
- IllegalStateException

- if URLConnection is already connected.
- NullPointerException

- if the supplied

auth

is

null

.

**Since:**
- 9

**Implementation Requirements:**
- The default behavior of this method is to unconditionally
throw

UnsupportedOperationException

. Concrete
implementations of

HttpURLConnection

which support supplying an

Authenticator

for a
specific

HttpURLConnection

instance should
override this method to implement a different behavior.

**Implementation Note:**
- Depending on authentication schemes, an implementation
may or may not need to use the provided authenticator
to obtain a password. For instance, an implementation that
relies on third-party security libraries may still invoke the
default authenticator if these libraries are configured
to do so.
Likewise, an implementation that supports transparent
NTLM authentication may let the system attempt
to connect using the system user credentials first,
before invoking the provided authenticator.

However, if an authenticator is specifically provided,
then the underlying connection may only be reused for

HttpURLConnection

instances which share the same

Authenticator

instance, and authentication information,
if cached, may only be reused for an

HttpURLConnection

sharing that same

Authenticator

.

---

#### public
String
getHeaderFieldKey​(int n)

Returns the key for the

n

th

header field.
Some implementations may treat the

0

th

header field as special, i.e. as the status line returned by the HTTP
server. In this case,

getHeaderField(0)

returns the status
line, but

getHeaderFieldKey(0)

returns null.

**Overrides:**
- getHeaderFieldKey

in class

URLConnection

**Parameters:**
- n

- an index, where

n >=0

.

**Returns:**
- the key for the

n

th

header field,
or

null

if the key does not exist.

---

#### public void setFixedLengthStreamingMode​(int contentLength)

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is known in
advance.

An exception will be thrown if the application
attempts to write more data than the indicated
content-length, or if the application closes the OutputStream
before writing the indicated amount.

When output streaming is enabled, authentication
and redirection cannot be handled automatically.
A HttpRetryException will be thrown when reading
the response if authentication or redirection are required.
This exception can be queried for the details of the error.

This method must be called before the URLConnection is connected.

NOTE:

setFixedLengthStreamingMode(long)

is recommended
instead of this method as it allows larger content lengths to be set.

**Parameters:**
- contentLength

- The number of bytes which will be written
to the OutputStream.

**Throws:**
- IllegalStateException

- if URLConnection is already connected
or if a different streaming mode is already enabled.
- IllegalArgumentException

- if a content length less than
zero is specified.

**See Also:**
- setChunkedStreamingMode(int)

**Since:**
- 1.5

---

#### public void setFixedLengthStreamingMode​(long contentLength)

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is known in
advance.

An exception will be thrown if the application attempts to write
more data than the indicated content-length, or if the application
closes the OutputStream before writing the indicated amount.

When output streaming is enabled, authentication and redirection
cannot be handled automatically. A

HttpRetryException

will
be thrown when reading the response if authentication or redirection
are required. This exception can be queried for the details of the
error.

This method must be called before the URLConnection is connected.

The content length set by invoking this method takes precedence
over any value set by

setFixedLengthStreamingMode(int)

.

**Parameters:**
- contentLength

- The number of bytes which will be written to the OutputStream.

**Throws:**
- IllegalStateException

- if URLConnection is already connected or if a different
streaming mode is already enabled.
- IllegalArgumentException

- if a content length less than zero is specified.

**Since:**
- 1.7

---

#### public void setChunkedStreamingMode​(int chunklen)

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is

not

known in advance. In this mode, chunked transfer encoding
is used to send the request body. Note, not all HTTP servers
support this mode.

When output streaming is enabled, authentication
and redirection cannot be handled automatically.
A HttpRetryException will be thrown when reading
the response if authentication or redirection are required.
This exception can be queried for the details of the error.

This method must be called before the URLConnection is connected.

**Parameters:**
- chunklen

- The number of bytes to write in each chunk.
If chunklen is less than or equal to zero, a default
value will be used.

**Throws:**
- IllegalStateException

- if URLConnection is already connected
or if a different streaming mode is already enabled.

**See Also:**
- setFixedLengthStreamingMode(int)

**Since:**
- 1.5

---

#### public
String
getHeaderField​(int n)

Returns the value for the

n

th

header field.
Some implementations may treat the

0

th

header field as special, i.e. as the status line returned by the HTTP
server.

This method can be used in conjunction with the

getHeaderFieldKey

method to iterate through all
the headers in the message.

**Overrides:**
- getHeaderField

in class

URLConnection

**Parameters:**
- n

- an index, where

n>=0

.

**Returns:**
- the value of the

n

th

header field,
or

null

if the value does not exist.

**See Also:**
- getHeaderFieldKey(int)

---

#### public static void setFollowRedirects​(boolean set)

Sets whether HTTP redirects (requests with response code 3xx) should
be automatically followed by this class. True by default. Applets
cannot change this variable.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:**
- set

- a

boolean

indicating whether or not
to follow HTTP redirects.

**Throws:**
- SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't
allow the operation.

**See Also:**
- SecurityManager.checkSetFactory()

,

getFollowRedirects()

---

#### public static boolean getFollowRedirects()

Returns a

boolean

indicating
whether or not HTTP redirects (3xx) should
be automatically followed.

**Returns:**
- true

if HTTP redirects should
be automatically followed,

false

if not.

**See Also:**
- setFollowRedirects(boolean)

---

#### public void setInstanceFollowRedirects​(boolean followRedirects)

Sets whether HTTP redirects (requests with response code 3xx) should
be automatically followed by this

HttpURLConnection

instance.

The default value comes from followRedirects, which defaults to
true.

**Parameters:**
- followRedirects

- a

boolean

indicating
whether or not to follow HTTP redirects.

**See Also:**
- instanceFollowRedirects

,

getInstanceFollowRedirects()

**Since:**
- 1.3

---

#### public boolean getInstanceFollowRedirects()

Returns the value of this

HttpURLConnection

's

instanceFollowRedirects

field.

**Returns:**
- the value of this

HttpURLConnection

's

instanceFollowRedirects

field.

**See Also:**
- instanceFollowRedirects

,

setInstanceFollowRedirects(boolean)

**Since:**
- 1.3

---

#### public void setRequestMethod​(
String
method)
throws
ProtocolException

Set the method for the URL request, one of:

- GET

POST

HEAD

OPTIONS

PUT

DELETE

TRACE

are legal, subject to protocol restrictions. The default
method is GET.

**Parameters:**
- method

- the HTTP method

**Throws:**
- ProtocolException

- if the method cannot be reset or if
the requested method isn't valid for HTTP.
- SecurityException

- if a security manager is set and the
method is "TRACE", but the "allowHttpTrace"
NetPermission is not granted.

**See Also:**
- getRequestMethod()

---

#### public
String
getRequestMethod()

Get the request method.

**Returns:**
- the HTTP request method

**See Also:**
- setRequestMethod(java.lang.String)

---

#### public int getResponseCode()
throws
IOException

Gets the status code from an HTTP response message.
For example, in the case of the following status lines:

```java
HTTP/1.0 200 OK
HTTP/1.0 401 Unauthorized
```

It will return 200 and 401 respectively.
Returns -1 if no code can be discerned
from the response (i.e., the response is not valid HTTP).

**Returns:**
- the HTTP Status-Code, or -1

**Throws:**
- IOException

- if an error occurred connecting to the server.

---

#### public
String
getResponseMessage()
throws
IOException

Gets the HTTP response message, if any, returned along with the
response code from a server. From responses like:

```java
HTTP/1.0 200 OK
HTTP/1.0 404 Not Found
```

Extracts the Strings "OK" and "Not Found" respectively.
Returns null if none could be discerned from the responses
(the result was not valid HTTP).

**Returns:**
- the HTTP response message, or

null

**Throws:**
- IOException

- if an error occurred connecting to the server.

---

#### public abstract void disconnect()

Indicates that other requests to the server
are unlikely in the near future. Calling disconnect()
should not imply that this HttpURLConnection
instance can be reused for other requests.

---

#### public abstract boolean usingProxy()

Indicates if the connection is going through a proxy.

**Returns:**
- a boolean indicating if the connection is
using a proxy.

---

#### public
Permission
getPermission()
throws
IOException

Returns a

SocketPermission

object representing the
permission necessary to connect to the destination host and port.

**Overrides:**
- getPermission

in class

URLConnection

**Returns:**
- a

SocketPermission

object representing the
permission necessary to connect to the destination
host and port.

**Throws:**
- IOException

- if an error occurs while computing
the permission.

---

#### public
InputStream
getErrorStream()

Returns the error stream if the connection failed
but the server sent useful data nonetheless. The
typical example is when an HTTP server responds
with a 404, which will cause a FileNotFoundException
to be thrown in connect, but the server sent an HTML
help page with suggestions as to what to do.

This method will not cause a connection to be initiated. If
the connection was not connected, or if the server did not have
an error while connecting or if the server had an error but
no error data was sent, this method will return null. This is
the default.

**Returns:**
- an error stream if any, null if there have been no
errors, the connection is not connected or the server sent no
useful data.

---

### Additional Sections

#### Class HttpURLConnection

java.lang.Object

- java.net.URLConnection
- - java.net.HttpURLConnection

java.net.URLConnection

- java.net.HttpURLConnection

java.net.HttpURLConnection

**Direct Known Subclasses:** HttpsURLConnection

```java
public abstract class
HttpURLConnection

extends
URLConnection
```

A URLConnection with support for HTTP-specific features. See

the spec

for
details.

Each HttpURLConnection instance is used to make a single request
but the underlying network connection to the HTTP server may be
transparently shared by other instances. Calling the close() methods
on the InputStream or OutputStream of an HttpURLConnection
after a request may free network resources associated with this
instance but has no effect on any shared persistent connection.
Calling the disconnect() method may close the underlying socket
if a persistent connection is otherwise idle at that time.

The HTTP protocol handler has a few settings that can be accessed through
System Properties. This covers

Proxy settings

as well as

various other settings

.

Security permissions

If a security manager is installed, and if a method is called which results in an
attempt to open a connection, the caller must possess either:

- a "connect"

SocketPermission

to the host/port combination of the
destination URL or
- a

URLPermission

that permits this request.

If automatic redirection is enabled, and this request is redirected to another
destination, then the caller must also have permission to connect to the
redirected host/URL.

**Since:** 1.1
**See Also:** disconnect()

public abstract class

HttpURLConnection

extends

URLConnection

A URLConnection with support for HTTP-specific features. See

the spec

for
details.

Each HttpURLConnection instance is used to make a single request
but the underlying network connection to the HTTP server may be
transparently shared by other instances. Calling the close() methods
on the InputStream or OutputStream of an HttpURLConnection
after a request may free network resources associated with this
instance but has no effect on any shared persistent connection.
Calling the disconnect() method may close the underlying socket
if a persistent connection is otherwise idle at that time.

The HTTP protocol handler has a few settings that can be accessed through
System Properties. This covers

Proxy settings

as well as

various other settings

.

Security permissions

If a security manager is installed, and if a method is called which results in an
attempt to open a connection, the caller must possess either:

- a "connect"

SocketPermission

to the host/port combination of the
destination URL or
- a

URLPermission

that permits this request.

If automatic redirection is enabled, and this request is redirected to another
destination, then the caller must also have permission to connect to the
redirected host/URL.

Each HttpURLConnection instance is used to make a single request
but the underlying network connection to the HTTP server may be
transparently shared by other instances. Calling the close() methods
on the InputStream or OutputStream of an HttpURLConnection
after a request may free network resources associated with this
instance but has no effect on any shared persistent connection.
Calling the disconnect() method may close the underlying socket
if a persistent connection is otherwise idle at that time.

The HTTP protocol handler has a few settings that can be accessed through
System Properties. This covers

Proxy settings

as well as

various other settings

.

Security permissions

If a security manager is installed, and if a method is called which results in an
attempt to open a connection, the caller must possess either:

- a "connect"

SocketPermission

to the host/port combination of the
destination URL or
- a

URLPermission

that permits this request.

If automatic redirection is enabled, and this request is redirected to another
destination, then the caller must also have permission to connect to the
redirected host/URL.

The HTTP protocol handler has a few settings that can be accessed through
System Properties. This covers

Proxy settings

as well as

various other settings

.

Security permissions

If a security manager is installed, and if a method is called which results in an
attempt to open a connection, the caller must possess either:

- a "connect"

SocketPermission

to the host/port combination of the
destination URL or
- a

URLPermission

that permits this request.

If automatic redirection is enabled, and this request is redirected to another
destination, then the caller must also have permission to connect to the
redirected host/URL.

If a security manager is installed, and if a method is called which results in an
attempt to open a connection, the caller must possess either:

- a "connect"

SocketPermission

to the host/port combination of the
destination URL or
- a

URLPermission

that permits this request.

If automatic redirection is enabled, and this request is redirected to another
destination, then the caller must also have permission to connect to the
redirected host/URL.

a "connect"

SocketPermission

to the host/port combination of the
destination URL or

a

URLPermission

that permits this request.

If automatic redirection is enabled, and this request is redirected to another
destination, then the caller must also have permission to connect to the
redirected host/URL.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected int

chunkLength

The chunk-length when using chunked encoding streaming mode for output.

protected int

fixedContentLength

The fixed content-length when using fixed-length streaming mode.

protected long

fixedContentLengthLong

The fixed content-length when using fixed-length streaming mode.

static int

HTTP_ACCEPTED

HTTP Status-Code 202: Accepted.

static int

HTTP_BAD_GATEWAY

HTTP Status-Code 502: Bad Gateway.

static int

HTTP_BAD_METHOD

HTTP Status-Code 405: Method Not Allowed.

static int

HTTP_BAD_REQUEST

HTTP Status-Code 400: Bad Request.

static int

HTTP_CLIENT_TIMEOUT

HTTP Status-Code 408: Request Time-Out.

static int

HTTP_CONFLICT

HTTP Status-Code 409: Conflict.

static int

HTTP_CREATED

HTTP Status-Code 201: Created.

static int

HTTP_ENTITY_TOO_LARGE

HTTP Status-Code 413: Request Entity Too Large.

static int

HTTP_FORBIDDEN

HTTP Status-Code 403: Forbidden.

static int

HTTP_GATEWAY_TIMEOUT

HTTP Status-Code 504: Gateway Timeout.

static int

HTTP_GONE

HTTP Status-Code 410: Gone.

static int

HTTP_INTERNAL_ERROR

HTTP Status-Code 500: Internal Server Error.

static int

HTTP_LENGTH_REQUIRED

HTTP Status-Code 411: Length Required.

static int

HTTP_MOVED_PERM

HTTP Status-Code 301: Moved Permanently.

static int

HTTP_MOVED_TEMP

HTTP Status-Code 302: Temporary Redirect.

static int

HTTP_MULT_CHOICE

HTTP Status-Code 300: Multiple Choices.

static int

HTTP_NO_CONTENT

HTTP Status-Code 204: No Content.

static int

HTTP_NOT_ACCEPTABLE

HTTP Status-Code 406: Not Acceptable.

static int

HTTP_NOT_AUTHORITATIVE

HTTP Status-Code 203: Non-Authoritative Information.

static int

HTTP_NOT_FOUND

HTTP Status-Code 404: Not Found.

static int

HTTP_NOT_IMPLEMENTED

HTTP Status-Code 501: Not Implemented.

static int

HTTP_NOT_MODIFIED

HTTP Status-Code 304: Not Modified.

static int

HTTP_OK

HTTP Status-Code 200: OK.

static int

HTTP_PARTIAL

HTTP Status-Code 206: Partial Content.

static int

HTTP_PAYMENT_REQUIRED

HTTP Status-Code 402: Payment Required.

static int

HTTP_PRECON_FAILED

HTTP Status-Code 412: Precondition Failed.

static int

HTTP_PROXY_AUTH

HTTP Status-Code 407: Proxy Authentication Required.

static int

HTTP_REQ_TOO_LONG

HTTP Status-Code 414: Request-URI Too Large.

static int

HTTP_RESET

HTTP Status-Code 205: Reset Content.

static int

HTTP_SEE_OTHER

HTTP Status-Code 303: See Other.

static int

HTTP_SERVER_ERROR

Deprecated.

it is misplaced and shouldn't have existed.

static int

HTTP_UNAUTHORIZED

HTTP Status-Code 401: Unauthorized.

static int

HTTP_UNAVAILABLE

HTTP Status-Code 503: Service Unavailable.

static int

HTTP_UNSUPPORTED_TYPE

HTTP Status-Code 415: Unsupported Media Type.

static int

HTTP_USE_PROXY

HTTP Status-Code 305: Use Proxy.

static int

HTTP_VERSION

HTTP Status-Code 505: HTTP Version Not Supported.

protected boolean

instanceFollowRedirects

If

true

, the protocol will automatically follow redirects.

protected

String

method

The HTTP method (GET,POST,PUT,etc.).

protected int

responseCode

An

int

representing the three digit HTTP Status-Code.

protected

String

responseMessage

The HTTP response message.

- Fields declared in class java.net.

URLConnection

allowUserInteraction

,

connected

,

doInput

,

doOutput

,

ifModifiedSince

,

url

,

useCaches

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

HttpURLConnection

​(

URL

u)

Constructor for the HttpURLConnection.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract void

disconnect

()

Indicates that other requests to the server
are unlikely in the near future.

InputStream

getErrorStream

()

Returns the error stream if the connection failed
but the server sent useful data nonetheless.

static boolean

getFollowRedirects

()

Returns a

boolean

indicating
whether or not HTTP redirects (3xx) should
be automatically followed.

String

getHeaderField

​(int n)

Returns the value for the

n

th

header field.

String

getHeaderFieldKey

​(int n)

Returns the key for the

n

th

header field.

boolean

getInstanceFollowRedirects

()

Returns the value of this

HttpURLConnection

's

instanceFollowRedirects

field.

Permission

getPermission

()

Returns a

SocketPermission

object representing the
permission necessary to connect to the destination host and port.

String

getRequestMethod

()

Get the request method.

int

getResponseCode

()

Gets the status code from an HTTP response message.

String

getResponseMessage

()

Gets the HTTP response message, if any, returned along with the
response code from a server.

void

setAuthenticator

​(

Authenticator

auth)

Supplies an

Authenticator

to be used
when authentication is requested through the HTTP protocol for
this

HttpURLConnection

.

void

setChunkedStreamingMode

​(int chunklen)

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is

not

known in advance.

void

setFixedLengthStreamingMode

​(int contentLength)

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is known in
advance.

void

setFixedLengthStreamingMode

​(long contentLength)

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is known in
advance.

static void

setFollowRedirects

​(boolean set)

Sets whether HTTP redirects (requests with response code 3xx) should
be automatically followed by this class.

void

setInstanceFollowRedirects

​(boolean followRedirects)

Sets whether HTTP redirects (requests with response code 3xx) should
be automatically followed by this

HttpURLConnection

instance.

void

setRequestMethod

​(

String

method)

Set the method for the URL request, one of:

GET
POST
HEAD
OPTIONS
PUT
DELETE
TRACE
are legal, subject to protocol restrictions.

abstract boolean

usingProxy

()

Indicates if the connection is going through a proxy.

- Methods declared in class java.net.

URLConnection

addRequestProperty

,

connect

,

getAllowUserInteraction

,

getConnectTimeout

,

getContent

,

getContent

,

getContentEncoding

,

getContentLength

,

getContentLengthLong

,

getContentType

,

getDate

,

getDefaultAllowUserInteraction

,

getDefaultRequestProperty

,

getDefaultUseCaches

,

getDefaultUseCaches

,

getDoInput

,

getDoOutput

,

getExpiration

,

getFileNameMap

,

getHeaderField

,

getHeaderFieldDate

,

getHeaderFieldInt

,

getHeaderFieldLong

,

getHeaderFields

,

getIfModifiedSince

,

getInputStream

,

getLastModified

,

getOutputStream

,

getReadTimeout

,

getRequestProperties

,

getRequestProperty

,

getURL

,

getUseCaches

,

guessContentTypeFromName

,

guessContentTypeFromStream

,

setAllowUserInteraction

,

setConnectTimeout

,

setContentHandlerFactory

,

setDefaultAllowUserInteraction

,

setDefaultRequestProperty

,

setDefaultUseCaches

,

setDefaultUseCaches

,

setDoInput

,

setDoOutput

,

setFileNameMap

,

setIfModifiedSince

,

setReadTimeout

,

setRequestProperty

,

setUseCaches

,

toString

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

protected int

chunkLength

The chunk-length when using chunked encoding streaming mode for output.

protected int

fixedContentLength

The fixed content-length when using fixed-length streaming mode.

protected long

fixedContentLengthLong

The fixed content-length when using fixed-length streaming mode.

static int

HTTP_ACCEPTED

HTTP Status-Code 202: Accepted.

static int

HTTP_BAD_GATEWAY

HTTP Status-Code 502: Bad Gateway.

static int

HTTP_BAD_METHOD

HTTP Status-Code 405: Method Not Allowed.

static int

HTTP_BAD_REQUEST

HTTP Status-Code 400: Bad Request.

static int

HTTP_CLIENT_TIMEOUT

HTTP Status-Code 408: Request Time-Out.

static int

HTTP_CONFLICT

HTTP Status-Code 409: Conflict.

static int

HTTP_CREATED

HTTP Status-Code 201: Created.

static int

HTTP_ENTITY_TOO_LARGE

HTTP Status-Code 413: Request Entity Too Large.

static int

HTTP_FORBIDDEN

HTTP Status-Code 403: Forbidden.

static int

HTTP_GATEWAY_TIMEOUT

HTTP Status-Code 504: Gateway Timeout.

static int

HTTP_GONE

HTTP Status-Code 410: Gone.

static int

HTTP_INTERNAL_ERROR

HTTP Status-Code 500: Internal Server Error.

static int

HTTP_LENGTH_REQUIRED

HTTP Status-Code 411: Length Required.

static int

HTTP_MOVED_PERM

HTTP Status-Code 301: Moved Permanently.

static int

HTTP_MOVED_TEMP

HTTP Status-Code 302: Temporary Redirect.

static int

HTTP_MULT_CHOICE

HTTP Status-Code 300: Multiple Choices.

static int

HTTP_NO_CONTENT

HTTP Status-Code 204: No Content.

static int

HTTP_NOT_ACCEPTABLE

HTTP Status-Code 406: Not Acceptable.

static int

HTTP_NOT_AUTHORITATIVE

HTTP Status-Code 203: Non-Authoritative Information.

static int

HTTP_NOT_FOUND

HTTP Status-Code 404: Not Found.

static int

HTTP_NOT_IMPLEMENTED

HTTP Status-Code 501: Not Implemented.

static int

HTTP_NOT_MODIFIED

HTTP Status-Code 304: Not Modified.

static int

HTTP_OK

HTTP Status-Code 200: OK.

static int

HTTP_PARTIAL

HTTP Status-Code 206: Partial Content.

static int

HTTP_PAYMENT_REQUIRED

HTTP Status-Code 402: Payment Required.

static int

HTTP_PRECON_FAILED

HTTP Status-Code 412: Precondition Failed.

static int

HTTP_PROXY_AUTH

HTTP Status-Code 407: Proxy Authentication Required.

static int

HTTP_REQ_TOO_LONG

HTTP Status-Code 414: Request-URI Too Large.

static int

HTTP_RESET

HTTP Status-Code 205: Reset Content.

static int

HTTP_SEE_OTHER

HTTP Status-Code 303: See Other.

static int

HTTP_SERVER_ERROR

Deprecated.

it is misplaced and shouldn't have existed.

static int

HTTP_UNAUTHORIZED

HTTP Status-Code 401: Unauthorized.

static int

HTTP_UNAVAILABLE

HTTP Status-Code 503: Service Unavailable.

static int

HTTP_UNSUPPORTED_TYPE

HTTP Status-Code 415: Unsupported Media Type.

static int

HTTP_USE_PROXY

HTTP Status-Code 305: Use Proxy.

static int

HTTP_VERSION

HTTP Status-Code 505: HTTP Version Not Supported.

protected boolean

instanceFollowRedirects

If

true

, the protocol will automatically follow redirects.

protected

String

method

The HTTP method (GET,POST,PUT,etc.).

protected int

responseCode

An

int

representing the three digit HTTP Status-Code.

protected

String

responseMessage

The HTTP response message.

- Fields declared in class java.net.

URLConnection

allowUserInteraction

,

connected

,

doInput

,

doOutput

,

ifModifiedSince

,

url

,

useCaches

---

#### Field Summary

The chunk-length when using chunked encoding streaming mode for output.

The fixed content-length when using fixed-length streaming mode.

HTTP Status-Code 202: Accepted.

HTTP Status-Code 502: Bad Gateway.

HTTP Status-Code 405: Method Not Allowed.

HTTP Status-Code 400: Bad Request.

HTTP Status-Code 408: Request Time-Out.

HTTP Status-Code 409: Conflict.

HTTP Status-Code 201: Created.

HTTP Status-Code 413: Request Entity Too Large.

HTTP Status-Code 403: Forbidden.

HTTP Status-Code 504: Gateway Timeout.

HTTP Status-Code 410: Gone.

HTTP Status-Code 500: Internal Server Error.

HTTP Status-Code 411: Length Required.

HTTP Status-Code 301: Moved Permanently.

HTTP Status-Code 302: Temporary Redirect.

HTTP Status-Code 300: Multiple Choices.

HTTP Status-Code 204: No Content.

HTTP Status-Code 406: Not Acceptable.

HTTP Status-Code 203: Non-Authoritative Information.

HTTP Status-Code 404: Not Found.

HTTP Status-Code 501: Not Implemented.

HTTP Status-Code 304: Not Modified.

HTTP Status-Code 200: OK.

HTTP Status-Code 206: Partial Content.

HTTP Status-Code 402: Payment Required.

HTTP Status-Code 412: Precondition Failed.

HTTP Status-Code 407: Proxy Authentication Required.

HTTP Status-Code 414: Request-URI Too Large.

HTTP Status-Code 205: Reset Content.

HTTP Status-Code 303: See Other.

Deprecated.

it is misplaced and shouldn't have existed.

HTTP Status-Code 401: Unauthorized.

HTTP Status-Code 503: Service Unavailable.

HTTP Status-Code 415: Unsupported Media Type.

HTTP Status-Code 305: Use Proxy.

HTTP Status-Code 505: HTTP Version Not Supported.

If

true

, the protocol will automatically follow redirects.

The HTTP method (GET,POST,PUT,etc.).

An

int

representing the three digit HTTP Status-Code.

The HTTP response message.

Fields declared in class java.net.

URLConnection

allowUserInteraction

,

connected

,

doInput

,

doOutput

,

ifModifiedSince

,

url

,

useCaches

---

#### Fields declared in class java.net. URLConnection

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

HttpURLConnection

​(

URL

u)

Constructor for the HttpURLConnection.

---

#### Constructor Summary

Constructor for the HttpURLConnection.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract void

disconnect

()

Indicates that other requests to the server
are unlikely in the near future.

InputStream

getErrorStream

()

Returns the error stream if the connection failed
but the server sent useful data nonetheless.

static boolean

getFollowRedirects

()

Returns a

boolean

indicating
whether or not HTTP redirects (3xx) should
be automatically followed.

String

getHeaderField

​(int n)

Returns the value for the

n

th

header field.

String

getHeaderFieldKey

​(int n)

Returns the key for the

n

th

header field.

boolean

getInstanceFollowRedirects

()

Returns the value of this

HttpURLConnection

's

instanceFollowRedirects

field.

Permission

getPermission

()

Returns a

SocketPermission

object representing the
permission necessary to connect to the destination host and port.

String

getRequestMethod

()

Get the request method.

int

getResponseCode

()

Gets the status code from an HTTP response message.

String

getResponseMessage

()

Gets the HTTP response message, if any, returned along with the
response code from a server.

void

setAuthenticator

​(

Authenticator

auth)

Supplies an

Authenticator

to be used
when authentication is requested through the HTTP protocol for
this

HttpURLConnection

.

void

setChunkedStreamingMode

​(int chunklen)

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is

not

known in advance.

void

setFixedLengthStreamingMode

​(int contentLength)

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is known in
advance.

void

setFixedLengthStreamingMode

​(long contentLength)

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is known in
advance.

static void

setFollowRedirects

​(boolean set)

Sets whether HTTP redirects (requests with response code 3xx) should
be automatically followed by this class.

void

setInstanceFollowRedirects

​(boolean followRedirects)

Sets whether HTTP redirects (requests with response code 3xx) should
be automatically followed by this

HttpURLConnection

instance.

void

setRequestMethod

​(

String

method)

Set the method for the URL request, one of:

GET
POST
HEAD
OPTIONS
PUT
DELETE
TRACE
are legal, subject to protocol restrictions.

abstract boolean

usingProxy

()

Indicates if the connection is going through a proxy.

- Methods declared in class java.net.

URLConnection

addRequestProperty

,

connect

,

getAllowUserInteraction

,

getConnectTimeout

,

getContent

,

getContent

,

getContentEncoding

,

getContentLength

,

getContentLengthLong

,

getContentType

,

getDate

,

getDefaultAllowUserInteraction

,

getDefaultRequestProperty

,

getDefaultUseCaches

,

getDefaultUseCaches

,

getDoInput

,

getDoOutput

,

getExpiration

,

getFileNameMap

,

getHeaderField

,

getHeaderFieldDate

,

getHeaderFieldInt

,

getHeaderFieldLong

,

getHeaderFields

,

getIfModifiedSince

,

getInputStream

,

getLastModified

,

getOutputStream

,

getReadTimeout

,

getRequestProperties

,

getRequestProperty

,

getURL

,

getUseCaches

,

guessContentTypeFromName

,

guessContentTypeFromStream

,

setAllowUserInteraction

,

setConnectTimeout

,

setContentHandlerFactory

,

setDefaultAllowUserInteraction

,

setDefaultRequestProperty

,

setDefaultUseCaches

,

setDefaultUseCaches

,

setDoInput

,

setDoOutput

,

setFileNameMap

,

setIfModifiedSince

,

setReadTimeout

,

setRequestProperty

,

setUseCaches

,

toString

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

wait

,

wait

,

wait

---

#### Method Summary

Indicates that other requests to the server
are unlikely in the near future.

Returns the error stream if the connection failed
but the server sent useful data nonetheless.

Returns a

boolean

indicating
whether or not HTTP redirects (3xx) should
be automatically followed.

Returns the value for the

n

th

header field.

Returns the key for the

n

th

header field.

Returns the value of this

HttpURLConnection

's

instanceFollowRedirects

field.

Returns a

SocketPermission

object representing the
permission necessary to connect to the destination host and port.

Get the request method.

Gets the status code from an HTTP response message.

Gets the HTTP response message, if any, returned along with the
response code from a server.

Supplies an

Authenticator

to be used
when authentication is requested through the HTTP protocol for
this

HttpURLConnection

.

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is

not

known in advance.

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is known in
advance.

Sets whether HTTP redirects (requests with response code 3xx) should
be automatically followed by this class.

Sets whether HTTP redirects (requests with response code 3xx) should
be automatically followed by this

HttpURLConnection

instance.

Set the method for the URL request, one of:

GET
POST
HEAD
OPTIONS
PUT
DELETE
TRACE
are legal, subject to protocol restrictions.

Indicates if the connection is going through a proxy.

Methods declared in class java.net.

URLConnection

addRequestProperty

,

connect

,

getAllowUserInteraction

,

getConnectTimeout

,

getContent

,

getContent

,

getContentEncoding

,

getContentLength

,

getContentLengthLong

,

getContentType

,

getDate

,

getDefaultAllowUserInteraction

,

getDefaultRequestProperty

,

getDefaultUseCaches

,

getDefaultUseCaches

,

getDoInput

,

getDoOutput

,

getExpiration

,

getFileNameMap

,

getHeaderField

,

getHeaderFieldDate

,

getHeaderFieldInt

,

getHeaderFieldLong

,

getHeaderFields

,

getIfModifiedSince

,

getInputStream

,

getLastModified

,

getOutputStream

,

getReadTimeout

,

getRequestProperties

,

getRequestProperty

,

getURL

,

getUseCaches

,

guessContentTypeFromName

,

guessContentTypeFromStream

,

setAllowUserInteraction

,

setConnectTimeout

,

setContentHandlerFactory

,

setDefaultAllowUserInteraction

,

setDefaultRequestProperty

,

setDefaultUseCaches

,

setDefaultUseCaches

,

setDoInput

,

setDoOutput

,

setFileNameMap

,

setIfModifiedSince

,

setReadTimeout

,

setRequestProperty

,

setUseCaches

,

toString

---

#### Methods declared in class java.net. URLConnection

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- method

```java
protected
String
method
```

The HTTP method (GET,POST,PUT,etc.).

- chunkLength

```java
protected int chunkLength
```

The chunk-length when using chunked encoding streaming mode for output.
A value of

-1

means chunked encoding is disabled for output.

**Since:** 1.5

- fixedContentLength

```java
protected int fixedContentLength
```

The fixed content-length when using fixed-length streaming mode.
A value of

-1

means fixed-length streaming mode is disabled
for output.

NOTE:

fixedContentLengthLong

is recommended instead
of this field, as it allows larger content lengths to be set.

**Since:** 1.5

- fixedContentLengthLong

```java
protected long fixedContentLengthLong
```

The fixed content-length when using fixed-length streaming mode.
A value of

-1

means fixed-length streaming mode is disabled
for output.

**Since:** 1.7

- responseCode

```java
protected int responseCode
```

An

int

representing the three digit HTTP Status-Code.

- 1xx: Informational

2xx: Success

3xx: Redirection

4xx: Client Error

5xx: Server Error

- responseMessage

```java
protected
String
responseMessage
```

The HTTP response message.

- instanceFollowRedirects

```java
protected boolean instanceFollowRedirects
```

If

true

, the protocol will automatically follow redirects.
If

false

, the protocol will not automatically follow
redirects.

This field is set by the

setInstanceFollowRedirects

method. Its value is returned by the

getInstanceFollowRedirects

method.

Its default value is based on the value of the static followRedirects
at HttpURLConnection construction time.

**See Also:** setInstanceFollowRedirects(boolean)

,

getInstanceFollowRedirects()

,

setFollowRedirects(boolean)

- HTTP_OK

```java
public static final int HTTP_OK
```

HTTP Status-Code 200: OK.

**See Also:** Constant Field Values

- HTTP_CREATED

```java
public static final int HTTP_CREATED
```

HTTP Status-Code 201: Created.

**See Also:** Constant Field Values

- HTTP_ACCEPTED

```java
public static final int HTTP_ACCEPTED
```

HTTP Status-Code 202: Accepted.

**See Also:** Constant Field Values

- HTTP_NOT_AUTHORITATIVE

```java
public static final int HTTP_NOT_AUTHORITATIVE
```

HTTP Status-Code 203: Non-Authoritative Information.

**See Also:** Constant Field Values

- HTTP_NO_CONTENT

```java
public static final int HTTP_NO_CONTENT
```

HTTP Status-Code 204: No Content.

**See Also:** Constant Field Values

- HTTP_RESET

```java
public static final int HTTP_RESET
```

HTTP Status-Code 205: Reset Content.

**See Also:** Constant Field Values

- HTTP_PARTIAL

```java
public static final int HTTP_PARTIAL
```

HTTP Status-Code 206: Partial Content.

**See Also:** Constant Field Values

- HTTP_MULT_CHOICE

```java
public static final int HTTP_MULT_CHOICE
```

HTTP Status-Code 300: Multiple Choices.

**See Also:** Constant Field Values

- HTTP_MOVED_PERM

```java
public static final int HTTP_MOVED_PERM
```

HTTP Status-Code 301: Moved Permanently.

**See Also:** Constant Field Values

- HTTP_MOVED_TEMP

```java
public static final int HTTP_MOVED_TEMP
```

HTTP Status-Code 302: Temporary Redirect.

**See Also:** Constant Field Values

- HTTP_SEE_OTHER

```java
public static final int HTTP_SEE_OTHER
```

HTTP Status-Code 303: See Other.

**See Also:** Constant Field Values

- HTTP_NOT_MODIFIED

```java
public static final int HTTP_NOT_MODIFIED
```

HTTP Status-Code 304: Not Modified.

**See Also:** Constant Field Values

- HTTP_USE_PROXY

```java
public static final int HTTP_USE_PROXY
```

HTTP Status-Code 305: Use Proxy.

**See Also:** Constant Field Values

- HTTP_BAD_REQUEST

```java
public static final int HTTP_BAD_REQUEST
```

HTTP Status-Code 400: Bad Request.

**See Also:** Constant Field Values

- HTTP_UNAUTHORIZED

```java
public static final int HTTP_UNAUTHORIZED
```

HTTP Status-Code 401: Unauthorized.

**See Also:** Constant Field Values

- HTTP_PAYMENT_REQUIRED

```java
public static final int HTTP_PAYMENT_REQUIRED
```

HTTP Status-Code 402: Payment Required.

**See Also:** Constant Field Values

- HTTP_FORBIDDEN

```java
public static final int HTTP_FORBIDDEN
```

HTTP Status-Code 403: Forbidden.

**See Also:** Constant Field Values

- HTTP_NOT_FOUND

```java
public static final int HTTP_NOT_FOUND
```

HTTP Status-Code 404: Not Found.

**See Also:** Constant Field Values

- HTTP_BAD_METHOD

```java
public static final int HTTP_BAD_METHOD
```

HTTP Status-Code 405: Method Not Allowed.

**See Also:** Constant Field Values

- HTTP_NOT_ACCEPTABLE

```java
public static final int HTTP_NOT_ACCEPTABLE
```

HTTP Status-Code 406: Not Acceptable.

**See Also:** Constant Field Values

- HTTP_PROXY_AUTH

```java
public static final int HTTP_PROXY_AUTH
```

HTTP Status-Code 407: Proxy Authentication Required.

**See Also:** Constant Field Values

- HTTP_CLIENT_TIMEOUT

```java
public static final int HTTP_CLIENT_TIMEOUT
```

HTTP Status-Code 408: Request Time-Out.

**See Also:** Constant Field Values

- HTTP_CONFLICT

```java
public static final int HTTP_CONFLICT
```

HTTP Status-Code 409: Conflict.

**See Also:** Constant Field Values

- HTTP_GONE

```java
public static final int HTTP_GONE
```

HTTP Status-Code 410: Gone.

**See Also:** Constant Field Values

- HTTP_LENGTH_REQUIRED

```java
public static final int HTTP_LENGTH_REQUIRED
```

HTTP Status-Code 411: Length Required.

**See Also:** Constant Field Values

- HTTP_PRECON_FAILED

```java
public static final int HTTP_PRECON_FAILED
```

HTTP Status-Code 412: Precondition Failed.

**See Also:** Constant Field Values

- HTTP_ENTITY_TOO_LARGE

```java
public static final int HTTP_ENTITY_TOO_LARGE
```

HTTP Status-Code 413: Request Entity Too Large.

**See Also:** Constant Field Values

- HTTP_REQ_TOO_LONG

```java
public static final int HTTP_REQ_TOO_LONG
```

HTTP Status-Code 414: Request-URI Too Large.

**See Also:** Constant Field Values

- HTTP_UNSUPPORTED_TYPE

```java
public static final int HTTP_UNSUPPORTED_TYPE
```

HTTP Status-Code 415: Unsupported Media Type.

**See Also:** Constant Field Values

- HTTP_SERVER_ERROR

```java
@Deprecated

public static final int HTTP_SERVER_ERROR
```

Deprecated.

it is misplaced and shouldn't have existed.

HTTP Status-Code 500: Internal Server Error.

**See Also:** Constant Field Values

- HTTP_INTERNAL_ERROR

```java
public static final int HTTP_INTERNAL_ERROR
```

HTTP Status-Code 500: Internal Server Error.

**See Also:** Constant Field Values

- HTTP_NOT_IMPLEMENTED

```java
public static final int HTTP_NOT_IMPLEMENTED
```

HTTP Status-Code 501: Not Implemented.

**See Also:** Constant Field Values

- HTTP_BAD_GATEWAY

```java
public static final int HTTP_BAD_GATEWAY
```

HTTP Status-Code 502: Bad Gateway.

**See Also:** Constant Field Values

- HTTP_UNAVAILABLE

```java
public static final int HTTP_UNAVAILABLE
```

HTTP Status-Code 503: Service Unavailable.

**See Also:** Constant Field Values

- HTTP_GATEWAY_TIMEOUT

```java
public static final int HTTP_GATEWAY_TIMEOUT
```

HTTP Status-Code 504: Gateway Timeout.

**See Also:** Constant Field Values

- HTTP_VERSION

```java
public static final int HTTP_VERSION
```

HTTP Status-Code 505: HTTP Version Not Supported.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- HttpURLConnection

```java
protected HttpURLConnection​(
URL
u)
```

Constructor for the HttpURLConnection.

**Parameters:** u

- the URL

============ METHOD DETAIL ==========

- Method Detail

- setAuthenticator

```java
public void setAuthenticator​(
Authenticator
auth)
```

Supplies an

Authenticator

to be used
when authentication is requested through the HTTP protocol for
this

HttpURLConnection

.
If no authenticator is supplied, the

default
authenticator

will be used.

**Implementation Requirements:** The default behavior of this method is to unconditionally
throw

UnsupportedOperationException

. Concrete
implementations of

HttpURLConnection

which support supplying an

Authenticator

for a
specific

HttpURLConnection

instance should
override this method to implement a different behavior.
**Implementation Note:** Depending on authentication schemes, an implementation
may or may not need to use the provided authenticator
to obtain a password. For instance, an implementation that
relies on third-party security libraries may still invoke the
default authenticator if these libraries are configured
to do so.
Likewise, an implementation that supports transparent
NTLM authentication may let the system attempt
to connect using the system user credentials first,
before invoking the provided authenticator.

However, if an authenticator is specifically provided,
then the underlying connection may only be reused for

HttpURLConnection

instances which share the same

Authenticator

instance, and authentication information,
if cached, may only be reused for an

HttpURLConnection

sharing that same

Authenticator

.
**Parameters:** auth

- The

Authenticator

that should be used by this

HttpURLConnection

.
**Throws:** UnsupportedOperationException

- if setting an Authenticator is
not supported by the underlying implementation.
**Throws:** IllegalStateException

- if URLConnection is already connected.
**Throws:** NullPointerException

- if the supplied

auth

is

null

.
**Since:** 9

- getHeaderFieldKey

```java
public
String
getHeaderFieldKey​(int n)
```

Returns the key for the

n

th

header field.
Some implementations may treat the

0

th

header field as special, i.e. as the status line returned by the HTTP
server. In this case,

getHeaderField(0)

returns the status
line, but

getHeaderFieldKey(0)

returns null.

**Overrides:** getHeaderFieldKey

in class

URLConnection
**Parameters:** n

- an index, where

n >=0

.
**Returns:** the key for the

n

th

header field,
or

null

if the key does not exist.

- setFixedLengthStreamingMode

```java
public void setFixedLengthStreamingMode​(int contentLength)
```

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is known in
advance.

An exception will be thrown if the application
attempts to write more data than the indicated
content-length, or if the application closes the OutputStream
before writing the indicated amount.

When output streaming is enabled, authentication
and redirection cannot be handled automatically.
A HttpRetryException will be thrown when reading
the response if authentication or redirection are required.
This exception can be queried for the details of the error.

This method must be called before the URLConnection is connected.

NOTE:

setFixedLengthStreamingMode(long)

is recommended
instead of this method as it allows larger content lengths to be set.

**Parameters:** contentLength

- The number of bytes which will be written
to the OutputStream.
**Throws:** IllegalStateException

- if URLConnection is already connected
or if a different streaming mode is already enabled.
**Throws:** IllegalArgumentException

- if a content length less than
zero is specified.
**Since:** 1.5
**See Also:** setChunkedStreamingMode(int)

- setFixedLengthStreamingMode

```java
public void setFixedLengthStreamingMode​(long contentLength)
```

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is known in
advance.

An exception will be thrown if the application attempts to write
more data than the indicated content-length, or if the application
closes the OutputStream before writing the indicated amount.

When output streaming is enabled, authentication and redirection
cannot be handled automatically. A

HttpRetryException

will
be thrown when reading the response if authentication or redirection
are required. This exception can be queried for the details of the
error.

This method must be called before the URLConnection is connected.

The content length set by invoking this method takes precedence
over any value set by

setFixedLengthStreamingMode(int)

.

**Parameters:** contentLength

- The number of bytes which will be written to the OutputStream.
**Throws:** IllegalStateException

- if URLConnection is already connected or if a different
streaming mode is already enabled.
**Throws:** IllegalArgumentException

- if a content length less than zero is specified.
**Since:** 1.7

- setChunkedStreamingMode

```java
public void setChunkedStreamingMode​(int chunklen)
```

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is

not

known in advance. In this mode, chunked transfer encoding
is used to send the request body. Note, not all HTTP servers
support this mode.

When output streaming is enabled, authentication
and redirection cannot be handled automatically.
A HttpRetryException will be thrown when reading
the response if authentication or redirection are required.
This exception can be queried for the details of the error.

This method must be called before the URLConnection is connected.

**Parameters:** chunklen

- The number of bytes to write in each chunk.
If chunklen is less than or equal to zero, a default
value will be used.
**Throws:** IllegalStateException

- if URLConnection is already connected
or if a different streaming mode is already enabled.
**Since:** 1.5
**See Also:** setFixedLengthStreamingMode(int)

- getHeaderField

```java
public
String
getHeaderField​(int n)
```

Returns the value for the

n

th

header field.
Some implementations may treat the

0

th

header field as special, i.e. as the status line returned by the HTTP
server.

This method can be used in conjunction with the

getHeaderFieldKey

method to iterate through all
the headers in the message.

**Overrides:** getHeaderField

in class

URLConnection
**Parameters:** n

- an index, where

n>=0

.
**Returns:** the value of the

n

th

header field,
or

null

if the value does not exist.
**See Also:** getHeaderFieldKey(int)

- setFollowRedirects

```java
public static void setFollowRedirects​(boolean set)
```

Sets whether HTTP redirects (requests with response code 3xx) should
be automatically followed by this class. True by default. Applets
cannot change this variable.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:** set

- a

boolean

indicating whether or not
to follow HTTP redirects.
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't
allow the operation.
**See Also:** SecurityManager.checkSetFactory()

,

getFollowRedirects()

- getFollowRedirects

```java
public static boolean getFollowRedirects()
```

Returns a

boolean

indicating
whether or not HTTP redirects (3xx) should
be automatically followed.

**Returns:** true

if HTTP redirects should
be automatically followed,

false

if not.
**See Also:** setFollowRedirects(boolean)

- setInstanceFollowRedirects

```java
public void setInstanceFollowRedirects​(boolean followRedirects)
```

Sets whether HTTP redirects (requests with response code 3xx) should
be automatically followed by this

HttpURLConnection

instance.

The default value comes from followRedirects, which defaults to
true.

**Parameters:** followRedirects

- a

boolean

indicating
whether or not to follow HTTP redirects.
**Since:** 1.3
**See Also:** instanceFollowRedirects

,

getInstanceFollowRedirects()

- getInstanceFollowRedirects

```java
public boolean getInstanceFollowRedirects()
```

Returns the value of this

HttpURLConnection

's

instanceFollowRedirects

field.

**Returns:** the value of this

HttpURLConnection

's

instanceFollowRedirects

field.
**Since:** 1.3
**See Also:** instanceFollowRedirects

,

setInstanceFollowRedirects(boolean)

- setRequestMethod

```java
public void setRequestMethod​(
String
method)
throws
ProtocolException
```

Set the method for the URL request, one of:

- GET

POST

HEAD

OPTIONS

PUT

DELETE

TRACE

are legal, subject to protocol restrictions. The default
method is GET.

**Parameters:** method

- the HTTP method
**Throws:** ProtocolException

- if the method cannot be reset or if
the requested method isn't valid for HTTP.
**Throws:** SecurityException

- if a security manager is set and the
method is "TRACE", but the "allowHttpTrace"
NetPermission is not granted.
**See Also:** getRequestMethod()

- getRequestMethod

```java
public
String
getRequestMethod()
```

Get the request method.

**Returns:** the HTTP request method
**See Also:** setRequestMethod(java.lang.String)

- getResponseCode

```java
public int getResponseCode()
throws
IOException
```

Gets the status code from an HTTP response message.
For example, in the case of the following status lines:

```java
HTTP/1.0 200 OK
HTTP/1.0 401 Unauthorized
```

It will return 200 and 401 respectively.
Returns -1 if no code can be discerned
from the response (i.e., the response is not valid HTTP).

**Returns:** the HTTP Status-Code, or -1
**Throws:** IOException

- if an error occurred connecting to the server.

- getResponseMessage

```java
public
String
getResponseMessage()
throws
IOException
```

Gets the HTTP response message, if any, returned along with the
response code from a server. From responses like:

```java
HTTP/1.0 200 OK
HTTP/1.0 404 Not Found
```

Extracts the Strings "OK" and "Not Found" respectively.
Returns null if none could be discerned from the responses
(the result was not valid HTTP).

**Returns:** the HTTP response message, or

null
**Throws:** IOException

- if an error occurred connecting to the server.

- disconnect

```java
public abstract void disconnect()
```

Indicates that other requests to the server
are unlikely in the near future. Calling disconnect()
should not imply that this HttpURLConnection
instance can be reused for other requests.

- usingProxy

```java
public abstract boolean usingProxy()
```

Indicates if the connection is going through a proxy.

**Returns:** a boolean indicating if the connection is
using a proxy.

- getPermission

```java
public
Permission
getPermission()
throws
IOException
```

Returns a

SocketPermission

object representing the
permission necessary to connect to the destination host and port.

**Overrides:** getPermission

in class

URLConnection
**Returns:** a

SocketPermission

object representing the
permission necessary to connect to the destination
host and port.
**Throws:** IOException

- if an error occurs while computing
the permission.

- getErrorStream

```java
public
InputStream
getErrorStream()
```

Returns the error stream if the connection failed
but the server sent useful data nonetheless. The
typical example is when an HTTP server responds
with a 404, which will cause a FileNotFoundException
to be thrown in connect, but the server sent an HTML
help page with suggestions as to what to do.

This method will not cause a connection to be initiated. If
the connection was not connected, or if the server did not have
an error while connecting or if the server had an error but
no error data was sent, this method will return null. This is
the default.

**Returns:** an error stream if any, null if there have been no
errors, the connection is not connected or the server sent no
useful data.

Field Detail

- method

```java
protected
String
method
```

The HTTP method (GET,POST,PUT,etc.).

- chunkLength

```java
protected int chunkLength
```

The chunk-length when using chunked encoding streaming mode for output.
A value of

-1

means chunked encoding is disabled for output.

**Since:** 1.5

- fixedContentLength

```java
protected int fixedContentLength
```

The fixed content-length when using fixed-length streaming mode.
A value of

-1

means fixed-length streaming mode is disabled
for output.

NOTE:

fixedContentLengthLong

is recommended instead
of this field, as it allows larger content lengths to be set.

**Since:** 1.5

- fixedContentLengthLong

```java
protected long fixedContentLengthLong
```

The fixed content-length when using fixed-length streaming mode.
A value of

-1

means fixed-length streaming mode is disabled
for output.

**Since:** 1.7

- responseCode

```java
protected int responseCode
```

An

int

representing the three digit HTTP Status-Code.

- 1xx: Informational

2xx: Success

3xx: Redirection

4xx: Client Error

5xx: Server Error

- responseMessage

```java
protected
String
responseMessage
```

The HTTP response message.

- instanceFollowRedirects

```java
protected boolean instanceFollowRedirects
```

If

true

, the protocol will automatically follow redirects.
If

false

, the protocol will not automatically follow
redirects.

This field is set by the

setInstanceFollowRedirects

method. Its value is returned by the

getInstanceFollowRedirects

method.

Its default value is based on the value of the static followRedirects
at HttpURLConnection construction time.

**See Also:** setInstanceFollowRedirects(boolean)

,

getInstanceFollowRedirects()

,

setFollowRedirects(boolean)

- HTTP_OK

```java
public static final int HTTP_OK
```

HTTP Status-Code 200: OK.

**See Also:** Constant Field Values

- HTTP_CREATED

```java
public static final int HTTP_CREATED
```

HTTP Status-Code 201: Created.

**See Also:** Constant Field Values

- HTTP_ACCEPTED

```java
public static final int HTTP_ACCEPTED
```

HTTP Status-Code 202: Accepted.

**See Also:** Constant Field Values

- HTTP_NOT_AUTHORITATIVE

```java
public static final int HTTP_NOT_AUTHORITATIVE
```

HTTP Status-Code 203: Non-Authoritative Information.

**See Also:** Constant Field Values

- HTTP_NO_CONTENT

```java
public static final int HTTP_NO_CONTENT
```

HTTP Status-Code 204: No Content.

**See Also:** Constant Field Values

- HTTP_RESET

```java
public static final int HTTP_RESET
```

HTTP Status-Code 205: Reset Content.

**See Also:** Constant Field Values

- HTTP_PARTIAL

```java
public static final int HTTP_PARTIAL
```

HTTP Status-Code 206: Partial Content.

**See Also:** Constant Field Values

- HTTP_MULT_CHOICE

```java
public static final int HTTP_MULT_CHOICE
```

HTTP Status-Code 300: Multiple Choices.

**See Also:** Constant Field Values

- HTTP_MOVED_PERM

```java
public static final int HTTP_MOVED_PERM
```

HTTP Status-Code 301: Moved Permanently.

**See Also:** Constant Field Values

- HTTP_MOVED_TEMP

```java
public static final int HTTP_MOVED_TEMP
```

HTTP Status-Code 302: Temporary Redirect.

**See Also:** Constant Field Values

- HTTP_SEE_OTHER

```java
public static final int HTTP_SEE_OTHER
```

HTTP Status-Code 303: See Other.

**See Also:** Constant Field Values

- HTTP_NOT_MODIFIED

```java
public static final int HTTP_NOT_MODIFIED
```

HTTP Status-Code 304: Not Modified.

**See Also:** Constant Field Values

- HTTP_USE_PROXY

```java
public static final int HTTP_USE_PROXY
```

HTTP Status-Code 305: Use Proxy.

**See Also:** Constant Field Values

- HTTP_BAD_REQUEST

```java
public static final int HTTP_BAD_REQUEST
```

HTTP Status-Code 400: Bad Request.

**See Also:** Constant Field Values

- HTTP_UNAUTHORIZED

```java
public static final int HTTP_UNAUTHORIZED
```

HTTP Status-Code 401: Unauthorized.

**See Also:** Constant Field Values

- HTTP_PAYMENT_REQUIRED

```java
public static final int HTTP_PAYMENT_REQUIRED
```

HTTP Status-Code 402: Payment Required.

**See Also:** Constant Field Values

- HTTP_FORBIDDEN

```java
public static final int HTTP_FORBIDDEN
```

HTTP Status-Code 403: Forbidden.

**See Also:** Constant Field Values

- HTTP_NOT_FOUND

```java
public static final int HTTP_NOT_FOUND
```

HTTP Status-Code 404: Not Found.

**See Also:** Constant Field Values

- HTTP_BAD_METHOD

```java
public static final int HTTP_BAD_METHOD
```

HTTP Status-Code 405: Method Not Allowed.

**See Also:** Constant Field Values

- HTTP_NOT_ACCEPTABLE

```java
public static final int HTTP_NOT_ACCEPTABLE
```

HTTP Status-Code 406: Not Acceptable.

**See Also:** Constant Field Values

- HTTP_PROXY_AUTH

```java
public static final int HTTP_PROXY_AUTH
```

HTTP Status-Code 407: Proxy Authentication Required.

**See Also:** Constant Field Values

- HTTP_CLIENT_TIMEOUT

```java
public static final int HTTP_CLIENT_TIMEOUT
```

HTTP Status-Code 408: Request Time-Out.

**See Also:** Constant Field Values

- HTTP_CONFLICT

```java
public static final int HTTP_CONFLICT
```

HTTP Status-Code 409: Conflict.

**See Also:** Constant Field Values

- HTTP_GONE

```java
public static final int HTTP_GONE
```

HTTP Status-Code 410: Gone.

**See Also:** Constant Field Values

- HTTP_LENGTH_REQUIRED

```java
public static final int HTTP_LENGTH_REQUIRED
```

HTTP Status-Code 411: Length Required.

**See Also:** Constant Field Values

- HTTP_PRECON_FAILED

```java
public static final int HTTP_PRECON_FAILED
```

HTTP Status-Code 412: Precondition Failed.

**See Also:** Constant Field Values

- HTTP_ENTITY_TOO_LARGE

```java
public static final int HTTP_ENTITY_TOO_LARGE
```

HTTP Status-Code 413: Request Entity Too Large.

**See Also:** Constant Field Values

- HTTP_REQ_TOO_LONG

```java
public static final int HTTP_REQ_TOO_LONG
```

HTTP Status-Code 414: Request-URI Too Large.

**See Also:** Constant Field Values

- HTTP_UNSUPPORTED_TYPE

```java
public static final int HTTP_UNSUPPORTED_TYPE
```

HTTP Status-Code 415: Unsupported Media Type.

**See Also:** Constant Field Values

- HTTP_SERVER_ERROR

```java
@Deprecated

public static final int HTTP_SERVER_ERROR
```

Deprecated.

it is misplaced and shouldn't have existed.

HTTP Status-Code 500: Internal Server Error.

**See Also:** Constant Field Values

- HTTP_INTERNAL_ERROR

```java
public static final int HTTP_INTERNAL_ERROR
```

HTTP Status-Code 500: Internal Server Error.

**See Also:** Constant Field Values

- HTTP_NOT_IMPLEMENTED

```java
public static final int HTTP_NOT_IMPLEMENTED
```

HTTP Status-Code 501: Not Implemented.

**See Also:** Constant Field Values

- HTTP_BAD_GATEWAY

```java
public static final int HTTP_BAD_GATEWAY
```

HTTP Status-Code 502: Bad Gateway.

**See Also:** Constant Field Values

- HTTP_UNAVAILABLE

```java
public static final int HTTP_UNAVAILABLE
```

HTTP Status-Code 503: Service Unavailable.

**See Also:** Constant Field Values

- HTTP_GATEWAY_TIMEOUT

```java
public static final int HTTP_GATEWAY_TIMEOUT
```

HTTP Status-Code 504: Gateway Timeout.

**See Also:** Constant Field Values

- HTTP_VERSION

```java
public static final int HTTP_VERSION
```

HTTP Status-Code 505: HTTP Version Not Supported.

**See Also:** Constant Field Values

---

#### Field Detail

method

```java
protected
String
method
```

The HTTP method (GET,POST,PUT,etc.).

---

#### method

protected

String

method

The HTTP method (GET,POST,PUT,etc.).

chunkLength

```java
protected int chunkLength
```

The chunk-length when using chunked encoding streaming mode for output.
A value of

-1

means chunked encoding is disabled for output.

**Since:** 1.5

---

#### chunkLength

protected int chunkLength

The chunk-length when using chunked encoding streaming mode for output.
A value of

-1

means chunked encoding is disabled for output.

fixedContentLength

```java
protected int fixedContentLength
```

The fixed content-length when using fixed-length streaming mode.
A value of

-1

means fixed-length streaming mode is disabled
for output.

NOTE:

fixedContentLengthLong

is recommended instead
of this field, as it allows larger content lengths to be set.

**Since:** 1.5

---

#### fixedContentLength

protected int fixedContentLength

The fixed content-length when using fixed-length streaming mode.
A value of

-1

means fixed-length streaming mode is disabled
for output.

NOTE:

fixedContentLengthLong

is recommended instead
of this field, as it allows larger content lengths to be set.

NOTE:

fixedContentLengthLong

is recommended instead
of this field, as it allows larger content lengths to be set.

fixedContentLengthLong

```java
protected long fixedContentLengthLong
```

The fixed content-length when using fixed-length streaming mode.
A value of

-1

means fixed-length streaming mode is disabled
for output.

**Since:** 1.7

---

#### fixedContentLengthLong

protected long fixedContentLengthLong

The fixed content-length when using fixed-length streaming mode.
A value of

-1

means fixed-length streaming mode is disabled
for output.

responseCode

```java
protected int responseCode
```

An

int

representing the three digit HTTP Status-Code.

- 1xx: Informational

2xx: Success

3xx: Redirection

4xx: Client Error

5xx: Server Error

---

#### responseCode

protected int responseCode

An

int

representing the three digit HTTP Status-Code.

- 1xx: Informational

2xx: Success

3xx: Redirection

4xx: Client Error

5xx: Server Error

1xx: Informational

2xx: Success

3xx: Redirection

4xx: Client Error

5xx: Server Error

responseMessage

```java
protected
String
responseMessage
```

The HTTP response message.

---

#### responseMessage

protected

String

responseMessage

The HTTP response message.

instanceFollowRedirects

```java
protected boolean instanceFollowRedirects
```

If

true

, the protocol will automatically follow redirects.
If

false

, the protocol will not automatically follow
redirects.

This field is set by the

setInstanceFollowRedirects

method. Its value is returned by the

getInstanceFollowRedirects

method.

Its default value is based on the value of the static followRedirects
at HttpURLConnection construction time.

**See Also:** setInstanceFollowRedirects(boolean)

,

getInstanceFollowRedirects()

,

setFollowRedirects(boolean)

---

#### instanceFollowRedirects

protected boolean instanceFollowRedirects

If

true

, the protocol will automatically follow redirects.
If

false

, the protocol will not automatically follow
redirects.

This field is set by the

setInstanceFollowRedirects

method. Its value is returned by the

getInstanceFollowRedirects

method.

Its default value is based on the value of the static followRedirects
at HttpURLConnection construction time.

This field is set by the

setInstanceFollowRedirects

method. Its value is returned by the

getInstanceFollowRedirects

method.

Its default value is based on the value of the static followRedirects
at HttpURLConnection construction time.

Its default value is based on the value of the static followRedirects
at HttpURLConnection construction time.

HTTP_OK

```java
public static final int HTTP_OK
```

HTTP Status-Code 200: OK.

**See Also:** Constant Field Values

---

#### HTTP_OK

public static final int HTTP_OK

HTTP Status-Code 200: OK.

HTTP_CREATED

```java
public static final int HTTP_CREATED
```

HTTP Status-Code 201: Created.

**See Also:** Constant Field Values

---

#### HTTP_CREATED

public static final int HTTP_CREATED

HTTP Status-Code 201: Created.

HTTP_ACCEPTED

```java
public static final int HTTP_ACCEPTED
```

HTTP Status-Code 202: Accepted.

**See Also:** Constant Field Values

---

#### HTTP_ACCEPTED

public static final int HTTP_ACCEPTED

HTTP Status-Code 202: Accepted.

HTTP_NOT_AUTHORITATIVE

```java
public static final int HTTP_NOT_AUTHORITATIVE
```

HTTP Status-Code 203: Non-Authoritative Information.

**See Also:** Constant Field Values

---

#### HTTP_NOT_AUTHORITATIVE

public static final int HTTP_NOT_AUTHORITATIVE

HTTP Status-Code 203: Non-Authoritative Information.

HTTP_NO_CONTENT

```java
public static final int HTTP_NO_CONTENT
```

HTTP Status-Code 204: No Content.

**See Also:** Constant Field Values

---

#### HTTP_NO_CONTENT

public static final int HTTP_NO_CONTENT

HTTP Status-Code 204: No Content.

HTTP_RESET

```java
public static final int HTTP_RESET
```

HTTP Status-Code 205: Reset Content.

**See Also:** Constant Field Values

---

#### HTTP_RESET

public static final int HTTP_RESET

HTTP Status-Code 205: Reset Content.

HTTP_PARTIAL

```java
public static final int HTTP_PARTIAL
```

HTTP Status-Code 206: Partial Content.

**See Also:** Constant Field Values

---

#### HTTP_PARTIAL

public static final int HTTP_PARTIAL

HTTP Status-Code 206: Partial Content.

HTTP_MULT_CHOICE

```java
public static final int HTTP_MULT_CHOICE
```

HTTP Status-Code 300: Multiple Choices.

**See Also:** Constant Field Values

---

#### HTTP_MULT_CHOICE

public static final int HTTP_MULT_CHOICE

HTTP Status-Code 300: Multiple Choices.

HTTP_MOVED_PERM

```java
public static final int HTTP_MOVED_PERM
```

HTTP Status-Code 301: Moved Permanently.

**See Also:** Constant Field Values

---

#### HTTP_MOVED_PERM

public static final int HTTP_MOVED_PERM

HTTP Status-Code 301: Moved Permanently.

HTTP_MOVED_TEMP

```java
public static final int HTTP_MOVED_TEMP
```

HTTP Status-Code 302: Temporary Redirect.

**See Also:** Constant Field Values

---

#### HTTP_MOVED_TEMP

public static final int HTTP_MOVED_TEMP

HTTP Status-Code 302: Temporary Redirect.

HTTP_SEE_OTHER

```java
public static final int HTTP_SEE_OTHER
```

HTTP Status-Code 303: See Other.

**See Also:** Constant Field Values

---

#### HTTP_SEE_OTHER

public static final int HTTP_SEE_OTHER

HTTP Status-Code 303: See Other.

HTTP_NOT_MODIFIED

```java
public static final int HTTP_NOT_MODIFIED
```

HTTP Status-Code 304: Not Modified.

**See Also:** Constant Field Values

---

#### HTTP_NOT_MODIFIED

public static final int HTTP_NOT_MODIFIED

HTTP Status-Code 304: Not Modified.

HTTP_USE_PROXY

```java
public static final int HTTP_USE_PROXY
```

HTTP Status-Code 305: Use Proxy.

**See Also:** Constant Field Values

---

#### HTTP_USE_PROXY

public static final int HTTP_USE_PROXY

HTTP Status-Code 305: Use Proxy.

HTTP_BAD_REQUEST

```java
public static final int HTTP_BAD_REQUEST
```

HTTP Status-Code 400: Bad Request.

**See Also:** Constant Field Values

---

#### HTTP_BAD_REQUEST

public static final int HTTP_BAD_REQUEST

HTTP Status-Code 400: Bad Request.

HTTP_UNAUTHORIZED

```java
public static final int HTTP_UNAUTHORIZED
```

HTTP Status-Code 401: Unauthorized.

**See Also:** Constant Field Values

---

#### HTTP_UNAUTHORIZED

public static final int HTTP_UNAUTHORIZED

HTTP Status-Code 401: Unauthorized.

HTTP_PAYMENT_REQUIRED

```java
public static final int HTTP_PAYMENT_REQUIRED
```

HTTP Status-Code 402: Payment Required.

**See Also:** Constant Field Values

---

#### HTTP_PAYMENT_REQUIRED

public static final int HTTP_PAYMENT_REQUIRED

HTTP Status-Code 402: Payment Required.

HTTP_FORBIDDEN

```java
public static final int HTTP_FORBIDDEN
```

HTTP Status-Code 403: Forbidden.

**See Also:** Constant Field Values

---

#### HTTP_FORBIDDEN

public static final int HTTP_FORBIDDEN

HTTP Status-Code 403: Forbidden.

HTTP_NOT_FOUND

```java
public static final int HTTP_NOT_FOUND
```

HTTP Status-Code 404: Not Found.

**See Also:** Constant Field Values

---

#### HTTP_NOT_FOUND

public static final int HTTP_NOT_FOUND

HTTP Status-Code 404: Not Found.

HTTP_BAD_METHOD

```java
public static final int HTTP_BAD_METHOD
```

HTTP Status-Code 405: Method Not Allowed.

**See Also:** Constant Field Values

---

#### HTTP_BAD_METHOD

public static final int HTTP_BAD_METHOD

HTTP Status-Code 405: Method Not Allowed.

HTTP_NOT_ACCEPTABLE

```java
public static final int HTTP_NOT_ACCEPTABLE
```

HTTP Status-Code 406: Not Acceptable.

**See Also:** Constant Field Values

---

#### HTTP_NOT_ACCEPTABLE

public static final int HTTP_NOT_ACCEPTABLE

HTTP Status-Code 406: Not Acceptable.

HTTP_PROXY_AUTH

```java
public static final int HTTP_PROXY_AUTH
```

HTTP Status-Code 407: Proxy Authentication Required.

**See Also:** Constant Field Values

---

#### HTTP_PROXY_AUTH

public static final int HTTP_PROXY_AUTH

HTTP Status-Code 407: Proxy Authentication Required.

HTTP_CLIENT_TIMEOUT

```java
public static final int HTTP_CLIENT_TIMEOUT
```

HTTP Status-Code 408: Request Time-Out.

**See Also:** Constant Field Values

---

#### HTTP_CLIENT_TIMEOUT

public static final int HTTP_CLIENT_TIMEOUT

HTTP Status-Code 408: Request Time-Out.

HTTP_CONFLICT

```java
public static final int HTTP_CONFLICT
```

HTTP Status-Code 409: Conflict.

**See Also:** Constant Field Values

---

#### HTTP_CONFLICT

public static final int HTTP_CONFLICT

HTTP Status-Code 409: Conflict.

HTTP_GONE

```java
public static final int HTTP_GONE
```

HTTP Status-Code 410: Gone.

**See Also:** Constant Field Values

---

#### HTTP_GONE

public static final int HTTP_GONE

HTTP Status-Code 410: Gone.

HTTP_LENGTH_REQUIRED

```java
public static final int HTTP_LENGTH_REQUIRED
```

HTTP Status-Code 411: Length Required.

**See Also:** Constant Field Values

---

#### HTTP_LENGTH_REQUIRED

public static final int HTTP_LENGTH_REQUIRED

HTTP Status-Code 411: Length Required.

HTTP_PRECON_FAILED

```java
public static final int HTTP_PRECON_FAILED
```

HTTP Status-Code 412: Precondition Failed.

**See Also:** Constant Field Values

---

#### HTTP_PRECON_FAILED

public static final int HTTP_PRECON_FAILED

HTTP Status-Code 412: Precondition Failed.

HTTP_ENTITY_TOO_LARGE

```java
public static final int HTTP_ENTITY_TOO_LARGE
```

HTTP Status-Code 413: Request Entity Too Large.

**See Also:** Constant Field Values

---

#### HTTP_ENTITY_TOO_LARGE

public static final int HTTP_ENTITY_TOO_LARGE

HTTP Status-Code 413: Request Entity Too Large.

HTTP_REQ_TOO_LONG

```java
public static final int HTTP_REQ_TOO_LONG
```

HTTP Status-Code 414: Request-URI Too Large.

**See Also:** Constant Field Values

---

#### HTTP_REQ_TOO_LONG

public static final int HTTP_REQ_TOO_LONG

HTTP Status-Code 414: Request-URI Too Large.

HTTP_UNSUPPORTED_TYPE

```java
public static final int HTTP_UNSUPPORTED_TYPE
```

HTTP Status-Code 415: Unsupported Media Type.

**See Also:** Constant Field Values

---

#### HTTP_UNSUPPORTED_TYPE

public static final int HTTP_UNSUPPORTED_TYPE

HTTP Status-Code 415: Unsupported Media Type.

HTTP_SERVER_ERROR

```java
@Deprecated

public static final int HTTP_SERVER_ERROR
```

Deprecated.

it is misplaced and shouldn't have existed.

HTTP Status-Code 500: Internal Server Error.

**See Also:** Constant Field Values

---

#### HTTP_SERVER_ERROR

@Deprecated

public static final int HTTP_SERVER_ERROR

HTTP Status-Code 500: Internal Server Error.

HTTP_INTERNAL_ERROR

```java
public static final int HTTP_INTERNAL_ERROR
```

HTTP Status-Code 500: Internal Server Error.

**See Also:** Constant Field Values

---

#### HTTP_INTERNAL_ERROR

public static final int HTTP_INTERNAL_ERROR

HTTP Status-Code 500: Internal Server Error.

HTTP_NOT_IMPLEMENTED

```java
public static final int HTTP_NOT_IMPLEMENTED
```

HTTP Status-Code 501: Not Implemented.

**See Also:** Constant Field Values

---

#### HTTP_NOT_IMPLEMENTED

public static final int HTTP_NOT_IMPLEMENTED

HTTP Status-Code 501: Not Implemented.

HTTP_BAD_GATEWAY

```java
public static final int HTTP_BAD_GATEWAY
```

HTTP Status-Code 502: Bad Gateway.

**See Also:** Constant Field Values

---

#### HTTP_BAD_GATEWAY

public static final int HTTP_BAD_GATEWAY

HTTP Status-Code 502: Bad Gateway.

HTTP_UNAVAILABLE

```java
public static final int HTTP_UNAVAILABLE
```

HTTP Status-Code 503: Service Unavailable.

**See Also:** Constant Field Values

---

#### HTTP_UNAVAILABLE

public static final int HTTP_UNAVAILABLE

HTTP Status-Code 503: Service Unavailable.

HTTP_GATEWAY_TIMEOUT

```java
public static final int HTTP_GATEWAY_TIMEOUT
```

HTTP Status-Code 504: Gateway Timeout.

**See Also:** Constant Field Values

---

#### HTTP_GATEWAY_TIMEOUT

public static final int HTTP_GATEWAY_TIMEOUT

HTTP Status-Code 504: Gateway Timeout.

HTTP_VERSION

```java
public static final int HTTP_VERSION
```

HTTP Status-Code 505: HTTP Version Not Supported.

**See Also:** Constant Field Values

---

#### HTTP_VERSION

public static final int HTTP_VERSION

HTTP Status-Code 505: HTTP Version Not Supported.

Constructor Detail

- HttpURLConnection

```java
protected HttpURLConnection​(
URL
u)
```

Constructor for the HttpURLConnection.

**Parameters:** u

- the URL

---

#### Constructor Detail

HttpURLConnection

```java
protected HttpURLConnection​(
URL
u)
```

Constructor for the HttpURLConnection.

**Parameters:** u

- the URL

---

#### HttpURLConnection

protected HttpURLConnection​(

URL

u)

Constructor for the HttpURLConnection.

Method Detail

- setAuthenticator

```java
public void setAuthenticator​(
Authenticator
auth)
```

Supplies an

Authenticator

to be used
when authentication is requested through the HTTP protocol for
this

HttpURLConnection

.
If no authenticator is supplied, the

default
authenticator

will be used.

**Implementation Requirements:** The default behavior of this method is to unconditionally
throw

UnsupportedOperationException

. Concrete
implementations of

HttpURLConnection

which support supplying an

Authenticator

for a
specific

HttpURLConnection

instance should
override this method to implement a different behavior.
**Implementation Note:** Depending on authentication schemes, an implementation
may or may not need to use the provided authenticator
to obtain a password. For instance, an implementation that
relies on third-party security libraries may still invoke the
default authenticator if these libraries are configured
to do so.
Likewise, an implementation that supports transparent
NTLM authentication may let the system attempt
to connect using the system user credentials first,
before invoking the provided authenticator.

However, if an authenticator is specifically provided,
then the underlying connection may only be reused for

HttpURLConnection

instances which share the same

Authenticator

instance, and authentication information,
if cached, may only be reused for an

HttpURLConnection

sharing that same

Authenticator

.
**Parameters:** auth

- The

Authenticator

that should be used by this

HttpURLConnection

.
**Throws:** UnsupportedOperationException

- if setting an Authenticator is
not supported by the underlying implementation.
**Throws:** IllegalStateException

- if URLConnection is already connected.
**Throws:** NullPointerException

- if the supplied

auth

is

null

.
**Since:** 9

- getHeaderFieldKey

```java
public
String
getHeaderFieldKey​(int n)
```

Returns the key for the

n

th

header field.
Some implementations may treat the

0

th

header field as special, i.e. as the status line returned by the HTTP
server. In this case,

getHeaderField(0)

returns the status
line, but

getHeaderFieldKey(0)

returns null.

**Overrides:** getHeaderFieldKey

in class

URLConnection
**Parameters:** n

- an index, where

n >=0

.
**Returns:** the key for the

n

th

header field,
or

null

if the key does not exist.

- setFixedLengthStreamingMode

```java
public void setFixedLengthStreamingMode​(int contentLength)
```

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is known in
advance.

An exception will be thrown if the application
attempts to write more data than the indicated
content-length, or if the application closes the OutputStream
before writing the indicated amount.

When output streaming is enabled, authentication
and redirection cannot be handled automatically.
A HttpRetryException will be thrown when reading
the response if authentication or redirection are required.
This exception can be queried for the details of the error.

This method must be called before the URLConnection is connected.

NOTE:

setFixedLengthStreamingMode(long)

is recommended
instead of this method as it allows larger content lengths to be set.

**Parameters:** contentLength

- The number of bytes which will be written
to the OutputStream.
**Throws:** IllegalStateException

- if URLConnection is already connected
or if a different streaming mode is already enabled.
**Throws:** IllegalArgumentException

- if a content length less than
zero is specified.
**Since:** 1.5
**See Also:** setChunkedStreamingMode(int)

- setFixedLengthStreamingMode

```java
public void setFixedLengthStreamingMode​(long contentLength)
```

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is known in
advance.

An exception will be thrown if the application attempts to write
more data than the indicated content-length, or if the application
closes the OutputStream before writing the indicated amount.

When output streaming is enabled, authentication and redirection
cannot be handled automatically. A

HttpRetryException

will
be thrown when reading the response if authentication or redirection
are required. This exception can be queried for the details of the
error.

This method must be called before the URLConnection is connected.

The content length set by invoking this method takes precedence
over any value set by

setFixedLengthStreamingMode(int)

.

**Parameters:** contentLength

- The number of bytes which will be written to the OutputStream.
**Throws:** IllegalStateException

- if URLConnection is already connected or if a different
streaming mode is already enabled.
**Throws:** IllegalArgumentException

- if a content length less than zero is specified.
**Since:** 1.7

- setChunkedStreamingMode

```java
public void setChunkedStreamingMode​(int chunklen)
```

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is

not

known in advance. In this mode, chunked transfer encoding
is used to send the request body. Note, not all HTTP servers
support this mode.

When output streaming is enabled, authentication
and redirection cannot be handled automatically.
A HttpRetryException will be thrown when reading
the response if authentication or redirection are required.
This exception can be queried for the details of the error.

This method must be called before the URLConnection is connected.

**Parameters:** chunklen

- The number of bytes to write in each chunk.
If chunklen is less than or equal to zero, a default
value will be used.
**Throws:** IllegalStateException

- if URLConnection is already connected
or if a different streaming mode is already enabled.
**Since:** 1.5
**See Also:** setFixedLengthStreamingMode(int)

- getHeaderField

```java
public
String
getHeaderField​(int n)
```

Returns the value for the

n

th

header field.
Some implementations may treat the

0

th

header field as special, i.e. as the status line returned by the HTTP
server.

This method can be used in conjunction with the

getHeaderFieldKey

method to iterate through all
the headers in the message.

**Overrides:** getHeaderField

in class

URLConnection
**Parameters:** n

- an index, where

n>=0

.
**Returns:** the value of the

n

th

header field,
or

null

if the value does not exist.
**See Also:** getHeaderFieldKey(int)

- setFollowRedirects

```java
public static void setFollowRedirects​(boolean set)
```

Sets whether HTTP redirects (requests with response code 3xx) should
be automatically followed by this class. True by default. Applets
cannot change this variable.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:** set

- a

boolean

indicating whether or not
to follow HTTP redirects.
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't
allow the operation.
**See Also:** SecurityManager.checkSetFactory()

,

getFollowRedirects()

- getFollowRedirects

```java
public static boolean getFollowRedirects()
```

Returns a

boolean

indicating
whether or not HTTP redirects (3xx) should
be automatically followed.

**Returns:** true

if HTTP redirects should
be automatically followed,

false

if not.
**See Also:** setFollowRedirects(boolean)

- setInstanceFollowRedirects

```java
public void setInstanceFollowRedirects​(boolean followRedirects)
```

Sets whether HTTP redirects (requests with response code 3xx) should
be automatically followed by this

HttpURLConnection

instance.

The default value comes from followRedirects, which defaults to
true.

**Parameters:** followRedirects

- a

boolean

indicating
whether or not to follow HTTP redirects.
**Since:** 1.3
**See Also:** instanceFollowRedirects

,

getInstanceFollowRedirects()

- getInstanceFollowRedirects

```java
public boolean getInstanceFollowRedirects()
```

Returns the value of this

HttpURLConnection

's

instanceFollowRedirects

field.

**Returns:** the value of this

HttpURLConnection

's

instanceFollowRedirects

field.
**Since:** 1.3
**See Also:** instanceFollowRedirects

,

setInstanceFollowRedirects(boolean)

- setRequestMethod

```java
public void setRequestMethod​(
String
method)
throws
ProtocolException
```

Set the method for the URL request, one of:

- GET

POST

HEAD

OPTIONS

PUT

DELETE

TRACE

are legal, subject to protocol restrictions. The default
method is GET.

**Parameters:** method

- the HTTP method
**Throws:** ProtocolException

- if the method cannot be reset or if
the requested method isn't valid for HTTP.
**Throws:** SecurityException

- if a security manager is set and the
method is "TRACE", but the "allowHttpTrace"
NetPermission is not granted.
**See Also:** getRequestMethod()

- getRequestMethod

```java
public
String
getRequestMethod()
```

Get the request method.

**Returns:** the HTTP request method
**See Also:** setRequestMethod(java.lang.String)

- getResponseCode

```java
public int getResponseCode()
throws
IOException
```

Gets the status code from an HTTP response message.
For example, in the case of the following status lines:

```java
HTTP/1.0 200 OK
HTTP/1.0 401 Unauthorized
```

It will return 200 and 401 respectively.
Returns -1 if no code can be discerned
from the response (i.e., the response is not valid HTTP).

**Returns:** the HTTP Status-Code, or -1
**Throws:** IOException

- if an error occurred connecting to the server.

- getResponseMessage

```java
public
String
getResponseMessage()
throws
IOException
```

Gets the HTTP response message, if any, returned along with the
response code from a server. From responses like:

```java
HTTP/1.0 200 OK
HTTP/1.0 404 Not Found
```

Extracts the Strings "OK" and "Not Found" respectively.
Returns null if none could be discerned from the responses
(the result was not valid HTTP).

**Returns:** the HTTP response message, or

null
**Throws:** IOException

- if an error occurred connecting to the server.

- disconnect

```java
public abstract void disconnect()
```

Indicates that other requests to the server
are unlikely in the near future. Calling disconnect()
should not imply that this HttpURLConnection
instance can be reused for other requests.

- usingProxy

```java
public abstract boolean usingProxy()
```

Indicates if the connection is going through a proxy.

**Returns:** a boolean indicating if the connection is
using a proxy.

- getPermission

```java
public
Permission
getPermission()
throws
IOException
```

Returns a

SocketPermission

object representing the
permission necessary to connect to the destination host and port.

**Overrides:** getPermission

in class

URLConnection
**Returns:** a

SocketPermission

object representing the
permission necessary to connect to the destination
host and port.
**Throws:** IOException

- if an error occurs while computing
the permission.

- getErrorStream

```java
public
InputStream
getErrorStream()
```

Returns the error stream if the connection failed
but the server sent useful data nonetheless. The
typical example is when an HTTP server responds
with a 404, which will cause a FileNotFoundException
to be thrown in connect, but the server sent an HTML
help page with suggestions as to what to do.

This method will not cause a connection to be initiated. If
the connection was not connected, or if the server did not have
an error while connecting or if the server had an error but
no error data was sent, this method will return null. This is
the default.

**Returns:** an error stream if any, null if there have been no
errors, the connection is not connected or the server sent no
useful data.

---

#### Method Detail

setAuthenticator

```java
public void setAuthenticator​(
Authenticator
auth)
```

Supplies an

Authenticator

to be used
when authentication is requested through the HTTP protocol for
this

HttpURLConnection

.
If no authenticator is supplied, the

default
authenticator

will be used.

**Implementation Requirements:** The default behavior of this method is to unconditionally
throw

UnsupportedOperationException

. Concrete
implementations of

HttpURLConnection

which support supplying an

Authenticator

for a
specific

HttpURLConnection

instance should
override this method to implement a different behavior.
**Implementation Note:** Depending on authentication schemes, an implementation
may or may not need to use the provided authenticator
to obtain a password. For instance, an implementation that
relies on third-party security libraries may still invoke the
default authenticator if these libraries are configured
to do so.
Likewise, an implementation that supports transparent
NTLM authentication may let the system attempt
to connect using the system user credentials first,
before invoking the provided authenticator.

However, if an authenticator is specifically provided,
then the underlying connection may only be reused for

HttpURLConnection

instances which share the same

Authenticator

instance, and authentication information,
if cached, may only be reused for an

HttpURLConnection

sharing that same

Authenticator

.
**Parameters:** auth

- The

Authenticator

that should be used by this

HttpURLConnection

.
**Throws:** UnsupportedOperationException

- if setting an Authenticator is
not supported by the underlying implementation.
**Throws:** IllegalStateException

- if URLConnection is already connected.
**Throws:** NullPointerException

- if the supplied

auth

is

null

.
**Since:** 9

---

#### setAuthenticator

public void setAuthenticator​(

Authenticator

auth)

Supplies an

Authenticator

to be used
when authentication is requested through the HTTP protocol for
this

HttpURLConnection

.
If no authenticator is supplied, the

default
authenticator

will be used.

getHeaderFieldKey

```java
public
String
getHeaderFieldKey​(int n)
```

Returns the key for the

n

th

header field.
Some implementations may treat the

0

th

header field as special, i.e. as the status line returned by the HTTP
server. In this case,

getHeaderField(0)

returns the status
line, but

getHeaderFieldKey(0)

returns null.

**Overrides:** getHeaderFieldKey

in class

URLConnection
**Parameters:** n

- an index, where

n >=0

.
**Returns:** the key for the

n

th

header field,
or

null

if the key does not exist.

---

#### getHeaderFieldKey

public

String

getHeaderFieldKey​(int n)

Returns the key for the

n

th

header field.
Some implementations may treat the

0

th

header field as special, i.e. as the status line returned by the HTTP
server. In this case,

getHeaderField(0)

returns the status
line, but

getHeaderFieldKey(0)

returns null.

setFixedLengthStreamingMode

```java
public void setFixedLengthStreamingMode​(int contentLength)
```

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is known in
advance.

An exception will be thrown if the application
attempts to write more data than the indicated
content-length, or if the application closes the OutputStream
before writing the indicated amount.

When output streaming is enabled, authentication
and redirection cannot be handled automatically.
A HttpRetryException will be thrown when reading
the response if authentication or redirection are required.
This exception can be queried for the details of the error.

This method must be called before the URLConnection is connected.

NOTE:

setFixedLengthStreamingMode(long)

is recommended
instead of this method as it allows larger content lengths to be set.

**Parameters:** contentLength

- The number of bytes which will be written
to the OutputStream.
**Throws:** IllegalStateException

- if URLConnection is already connected
or if a different streaming mode is already enabled.
**Throws:** IllegalArgumentException

- if a content length less than
zero is specified.
**Since:** 1.5
**See Also:** setChunkedStreamingMode(int)

---

#### setFixedLengthStreamingMode

public void setFixedLengthStreamingMode​(int contentLength)

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is known in
advance.

An exception will be thrown if the application
attempts to write more data than the indicated
content-length, or if the application closes the OutputStream
before writing the indicated amount.

When output streaming is enabled, authentication
and redirection cannot be handled automatically.
A HttpRetryException will be thrown when reading
the response if authentication or redirection are required.
This exception can be queried for the details of the error.

This method must be called before the URLConnection is connected.

NOTE:

setFixedLengthStreamingMode(long)

is recommended
instead of this method as it allows larger content lengths to be set.

An exception will be thrown if the application
attempts to write more data than the indicated
content-length, or if the application closes the OutputStream
before writing the indicated amount.

When output streaming is enabled, authentication
and redirection cannot be handled automatically.
A HttpRetryException will be thrown when reading
the response if authentication or redirection are required.
This exception can be queried for the details of the error.

This method must be called before the URLConnection is connected.

NOTE:

setFixedLengthStreamingMode(long)

is recommended
instead of this method as it allows larger content lengths to be set.

When output streaming is enabled, authentication
and redirection cannot be handled automatically.
A HttpRetryException will be thrown when reading
the response if authentication or redirection are required.
This exception can be queried for the details of the error.

This method must be called before the URLConnection is connected.

NOTE:

setFixedLengthStreamingMode(long)

is recommended
instead of this method as it allows larger content lengths to be set.

This method must be called before the URLConnection is connected.

NOTE:

setFixedLengthStreamingMode(long)

is recommended
instead of this method as it allows larger content lengths to be set.

NOTE:

setFixedLengthStreamingMode(long)

is recommended
instead of this method as it allows larger content lengths to be set.

setFixedLengthStreamingMode

```java
public void setFixedLengthStreamingMode​(long contentLength)
```

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is known in
advance.

An exception will be thrown if the application attempts to write
more data than the indicated content-length, or if the application
closes the OutputStream before writing the indicated amount.

When output streaming is enabled, authentication and redirection
cannot be handled automatically. A

HttpRetryException

will
be thrown when reading the response if authentication or redirection
are required. This exception can be queried for the details of the
error.

This method must be called before the URLConnection is connected.

The content length set by invoking this method takes precedence
over any value set by

setFixedLengthStreamingMode(int)

.

**Parameters:** contentLength

- The number of bytes which will be written to the OutputStream.
**Throws:** IllegalStateException

- if URLConnection is already connected or if a different
streaming mode is already enabled.
**Throws:** IllegalArgumentException

- if a content length less than zero is specified.
**Since:** 1.7

---

#### setFixedLengthStreamingMode

public void setFixedLengthStreamingMode​(long contentLength)

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is known in
advance.

An exception will be thrown if the application attempts to write
more data than the indicated content-length, or if the application
closes the OutputStream before writing the indicated amount.

When output streaming is enabled, authentication and redirection
cannot be handled automatically. A

HttpRetryException

will
be thrown when reading the response if authentication or redirection
are required. This exception can be queried for the details of the
error.

This method must be called before the URLConnection is connected.

The content length set by invoking this method takes precedence
over any value set by

setFixedLengthStreamingMode(int)

.

An exception will be thrown if the application attempts to write
more data than the indicated content-length, or if the application
closes the OutputStream before writing the indicated amount.

When output streaming is enabled, authentication and redirection
cannot be handled automatically. A

HttpRetryException

will
be thrown when reading the response if authentication or redirection
are required. This exception can be queried for the details of the
error.

This method must be called before the URLConnection is connected.

The content length set by invoking this method takes precedence
over any value set by

setFixedLengthStreamingMode(int)

.

When output streaming is enabled, authentication and redirection
cannot be handled automatically. A

HttpRetryException

will
be thrown when reading the response if authentication or redirection
are required. This exception can be queried for the details of the
error.

This method must be called before the URLConnection is connected.

The content length set by invoking this method takes precedence
over any value set by

setFixedLengthStreamingMode(int)

.

This method must be called before the URLConnection is connected.

The content length set by invoking this method takes precedence
over any value set by

setFixedLengthStreamingMode(int)

.

The content length set by invoking this method takes precedence
over any value set by

setFixedLengthStreamingMode(int)

.

setChunkedStreamingMode

```java
public void setChunkedStreamingMode​(int chunklen)
```

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is

not

known in advance. In this mode, chunked transfer encoding
is used to send the request body. Note, not all HTTP servers
support this mode.

When output streaming is enabled, authentication
and redirection cannot be handled automatically.
A HttpRetryException will be thrown when reading
the response if authentication or redirection are required.
This exception can be queried for the details of the error.

This method must be called before the URLConnection is connected.

**Parameters:** chunklen

- The number of bytes to write in each chunk.
If chunklen is less than or equal to zero, a default
value will be used.
**Throws:** IllegalStateException

- if URLConnection is already connected
or if a different streaming mode is already enabled.
**Since:** 1.5
**See Also:** setFixedLengthStreamingMode(int)

---

#### setChunkedStreamingMode

public void setChunkedStreamingMode​(int chunklen)

This method is used to enable streaming of a HTTP request body
without internal buffering, when the content length is

not

known in advance. In this mode, chunked transfer encoding
is used to send the request body. Note, not all HTTP servers
support this mode.

When output streaming is enabled, authentication
and redirection cannot be handled automatically.
A HttpRetryException will be thrown when reading
the response if authentication or redirection are required.
This exception can be queried for the details of the error.

This method must be called before the URLConnection is connected.

When output streaming is enabled, authentication
and redirection cannot be handled automatically.
A HttpRetryException will be thrown when reading
the response if authentication or redirection are required.
This exception can be queried for the details of the error.

This method must be called before the URLConnection is connected.

This method must be called before the URLConnection is connected.

getHeaderField

```java
public
String
getHeaderField​(int n)
```

Returns the value for the

n

th

header field.
Some implementations may treat the

0

th

header field as special, i.e. as the status line returned by the HTTP
server.

This method can be used in conjunction with the

getHeaderFieldKey

method to iterate through all
the headers in the message.

**Overrides:** getHeaderField

in class

URLConnection
**Parameters:** n

- an index, where

n>=0

.
**Returns:** the value of the

n

th

header field,
or

null

if the value does not exist.
**See Also:** getHeaderFieldKey(int)

---

#### getHeaderField

public

String

getHeaderField​(int n)

Returns the value for the

n

th

header field.
Some implementations may treat the

0

th

header field as special, i.e. as the status line returned by the HTTP
server.

This method can be used in conjunction with the

getHeaderFieldKey

method to iterate through all
the headers in the message.

This method can be used in conjunction with the

getHeaderFieldKey

method to iterate through all
the headers in the message.

setFollowRedirects

```java
public static void setFollowRedirects​(boolean set)
```

Sets whether HTTP redirects (requests with response code 3xx) should
be automatically followed by this class. True by default. Applets
cannot change this variable.

If there is a security manager, this method first calls
the security manager's

checkSetFactory

method
to ensure the operation is allowed.
This could result in a SecurityException.

**Parameters:** set

- a

boolean

indicating whether or not
to follow HTTP redirects.
**Throws:** SecurityException

- if a security manager exists and its

checkSetFactory

method doesn't
allow the operation.
**See Also:** SecurityManager.checkSetFactory()

,

getFollowRedirects()

---

#### setFollowRedirects

public static void setFollowRedirects​(boolean set)

Sets whether HTTP redirects (requests with response code 3xx) should
be automatically followed by this class. True by default. Applets
cannot change this variable.

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

getFollowRedirects

```java
public static boolean getFollowRedirects()
```

Returns a

boolean

indicating
whether or not HTTP redirects (3xx) should
be automatically followed.

**Returns:** true

if HTTP redirects should
be automatically followed,

false

if not.
**See Also:** setFollowRedirects(boolean)

---

#### getFollowRedirects

public static boolean getFollowRedirects()

Returns a

boolean

indicating
whether or not HTTP redirects (3xx) should
be automatically followed.

setInstanceFollowRedirects

```java
public void setInstanceFollowRedirects​(boolean followRedirects)
```

Sets whether HTTP redirects (requests with response code 3xx) should
be automatically followed by this

HttpURLConnection

instance.

The default value comes from followRedirects, which defaults to
true.

**Parameters:** followRedirects

- a

boolean

indicating
whether or not to follow HTTP redirects.
**Since:** 1.3
**See Also:** instanceFollowRedirects

,

getInstanceFollowRedirects()

---

#### setInstanceFollowRedirects

public void setInstanceFollowRedirects​(boolean followRedirects)

Sets whether HTTP redirects (requests with response code 3xx) should
be automatically followed by this

HttpURLConnection

instance.

The default value comes from followRedirects, which defaults to
true.

The default value comes from followRedirects, which defaults to
true.

getInstanceFollowRedirects

```java
public boolean getInstanceFollowRedirects()
```

Returns the value of this

HttpURLConnection

's

instanceFollowRedirects

field.

**Returns:** the value of this

HttpURLConnection

's

instanceFollowRedirects

field.
**Since:** 1.3
**See Also:** instanceFollowRedirects

,

setInstanceFollowRedirects(boolean)

---

#### getInstanceFollowRedirects

public boolean getInstanceFollowRedirects()

Returns the value of this

HttpURLConnection

's

instanceFollowRedirects

field.

setRequestMethod

```java
public void setRequestMethod​(
String
method)
throws
ProtocolException
```

Set the method for the URL request, one of:

- GET

POST

HEAD

OPTIONS

PUT

DELETE

TRACE

are legal, subject to protocol restrictions. The default
method is GET.

**Parameters:** method

- the HTTP method
**Throws:** ProtocolException

- if the method cannot be reset or if
the requested method isn't valid for HTTP.
**Throws:** SecurityException

- if a security manager is set and the
method is "TRACE", but the "allowHttpTrace"
NetPermission is not granted.
**See Also:** getRequestMethod()

---

#### setRequestMethod

public void setRequestMethod​(

String

method)
throws

ProtocolException

Set the method for the URL request, one of:

- GET

POST

HEAD

OPTIONS

PUT

DELETE

TRACE

are legal, subject to protocol restrictions. The default
method is GET.

GET

POST

HEAD

OPTIONS

PUT

DELETE

TRACE

getRequestMethod

```java
public
String
getRequestMethod()
```

Get the request method.

**Returns:** the HTTP request method
**See Also:** setRequestMethod(java.lang.String)

---

#### getRequestMethod

public

String

getRequestMethod()

Get the request method.

getResponseCode

```java
public int getResponseCode()
throws
IOException
```

Gets the status code from an HTTP response message.
For example, in the case of the following status lines:

```java
HTTP/1.0 200 OK
HTTP/1.0 401 Unauthorized
```

It will return 200 and 401 respectively.
Returns -1 if no code can be discerned
from the response (i.e., the response is not valid HTTP).

**Returns:** the HTTP Status-Code, or -1
**Throws:** IOException

- if an error occurred connecting to the server.

---

#### getResponseCode

public int getResponseCode()
throws

IOException

Gets the status code from an HTTP response message.
For example, in the case of the following status lines:

```java
HTTP/1.0 200 OK
HTTP/1.0 401 Unauthorized
```

It will return 200 and 401 respectively.
Returns -1 if no code can be discerned
from the response (i.e., the response is not valid HTTP).

HTTP/1.0 200 OK
HTTP/1.0 401 Unauthorized

getResponseMessage

```java
public
String
getResponseMessage()
throws
IOException
```

Gets the HTTP response message, if any, returned along with the
response code from a server. From responses like:

```java
HTTP/1.0 200 OK
HTTP/1.0 404 Not Found
```

Extracts the Strings "OK" and "Not Found" respectively.
Returns null if none could be discerned from the responses
(the result was not valid HTTP).

**Returns:** the HTTP response message, or

null
**Throws:** IOException

- if an error occurred connecting to the server.

---

#### getResponseMessage

public

String

getResponseMessage()
throws

IOException

Gets the HTTP response message, if any, returned along with the
response code from a server. From responses like:

```java
HTTP/1.0 200 OK
HTTP/1.0 404 Not Found
```

Extracts the Strings "OK" and "Not Found" respectively.
Returns null if none could be discerned from the responses
(the result was not valid HTTP).

HTTP/1.0 200 OK
HTTP/1.0 404 Not Found

disconnect

```java
public abstract void disconnect()
```

Indicates that other requests to the server
are unlikely in the near future. Calling disconnect()
should not imply that this HttpURLConnection
instance can be reused for other requests.

---

#### disconnect

public abstract void disconnect()

Indicates that other requests to the server
are unlikely in the near future. Calling disconnect()
should not imply that this HttpURLConnection
instance can be reused for other requests.

usingProxy

```java
public abstract boolean usingProxy()
```

Indicates if the connection is going through a proxy.

**Returns:** a boolean indicating if the connection is
using a proxy.

---

#### usingProxy

public abstract boolean usingProxy()

Indicates if the connection is going through a proxy.

getPermission

```java
public
Permission
getPermission()
throws
IOException
```

Returns a

SocketPermission

object representing the
permission necessary to connect to the destination host and port.

**Overrides:** getPermission

in class

URLConnection
**Returns:** a

SocketPermission

object representing the
permission necessary to connect to the destination
host and port.
**Throws:** IOException

- if an error occurs while computing
the permission.

---

#### getPermission

public

Permission

getPermission()
throws

IOException

Returns a

SocketPermission

object representing the
permission necessary to connect to the destination host and port.

getErrorStream

```java
public
InputStream
getErrorStream()
```

Returns the error stream if the connection failed
but the server sent useful data nonetheless. The
typical example is when an HTTP server responds
with a 404, which will cause a FileNotFoundException
to be thrown in connect, but the server sent an HTML
help page with suggestions as to what to do.

This method will not cause a connection to be initiated. If
the connection was not connected, or if the server did not have
an error while connecting or if the server had an error but
no error data was sent, this method will return null. This is
the default.

**Returns:** an error stream if any, null if there have been no
errors, the connection is not connected or the server sent no
useful data.

---

#### getErrorStream

public

InputStream

getErrorStream()

Returns the error stream if the connection failed
but the server sent useful data nonetheless. The
typical example is when an HTTP server responds
with a 404, which will cause a FileNotFoundException
to be thrown in connect, but the server sent an HTML
help page with suggestions as to what to do.

This method will not cause a connection to be initiated. If
the connection was not connected, or if the server did not have
an error while connecting or if the server had an error but
no error data was sent, this method will return null. This is
the default.

This method will not cause a connection to be initiated. If
the connection was not connected, or if the server did not have
an error while connecting or if the server had an error but
no error data was sent, this method will return null. This is
the default.

---

