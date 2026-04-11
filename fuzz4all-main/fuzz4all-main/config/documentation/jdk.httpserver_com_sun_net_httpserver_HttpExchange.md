# Class HttpExchange

**Source:** `jdk.httpserver\com\sun\net\httpserver\HttpExchange.html`

### Class Description

```java
public abstract class
HttpExchange

extends
Object
```

This class encapsulates a HTTP request received and a
response to be generated in one exchange. It provides methods
for examining the request from the client, and for building and
sending the response.

The typical life-cycle of a HttpExchange is shown in the sequence
below.

- getRequestMethod()

to determine the command

getRequestHeaders()

to examine the request headers (if needed)

getRequestBody()

returns a

InputStream

for reading the request body.
After reading the request body, the stream is close.

getResponseHeaders()

to set any response headers, except content-length

sendResponseHeaders(int,long)

to send the response headers. Must be called before
next step.

getResponseBody()

to get a

OutputStream

to send the response body.
When the response body has been written, the stream must be closed to terminate the exchange.

Terminating exchanges

Exchanges are terminated when both the request InputStream and response OutputStream are closed.
Closing the OutputStream, implicitly closes the InputStream (if it is not already closed).
However, it is recommended
to consume all the data from the InputStream before closing it.
The convenience method

close()

does all of these tasks.
Closing an exchange without consuming all of the request body is not an error
but may make the underlying TCP connection unusable for following exchanges.
The effect of failing to terminate an exchange is undefined, but will typically
result in resources failing to be freed/reused.

**Direct Known Subclasses:** HttpsExchange

---

### Field Details

*No entries found.*

### Constructor Details

#### protected HttpExchange()

*No description found.*

---

### Method Details

#### public abstract
Headers
getRequestHeaders()

Returns an immutable Map containing the HTTP headers that were
included with this request. The keys in this Map will be the header
names, while the values will be a List of Strings containing each value
that was included (either for a header that was listed several times,
or one that accepts a comma-delimited list of values on a single line).
In either of these cases, the values for the header name will be
presented in the order that they were included in the request.

The keys in Map are case-insensitive.

**Returns:**
- a read-only Map which can be used to access request headers

---

#### public abstract
Headers
getResponseHeaders()

Returns a mutable Map into which the HTTP response headers can be stored
and which will be transmitted as part of this response. The keys in the
Map will be the header names, while the values must be a List of Strings
containing each value that should be included multiple times
(in the order that they should be included).

The keys in Map are case-insensitive.

**Returns:**
- a writable Map which can be used to set response headers.

---

#### public abstract
URI
getRequestURI()

Get the request URI

**Returns:**
- the request URI

---

#### public abstract
String
getRequestMethod()

Get the request method

**Returns:**
- the request method

---

#### public abstract
HttpContext
getHttpContext()

Get the HttpContext for this exchange

**Returns:**
- the HttpContext

---

#### public abstract void close()

Ends this exchange by doing the following in sequence:

- close the request InputStream, if not already closed;
- close the response OutputStream, if not already closed.

---

#### public abstract
InputStream
getRequestBody()

returns a stream from which the request body can be read.
Multiple calls to this method will return the same stream.
It is recommended that applications should consume (read) all of the
data from this stream before closing it. If a stream is closed
before all data has been read, then the close() call will
read and discard remaining data (up to an implementation specific
number of bytes).

**Returns:**
- the stream from which the request body can be read.

---

#### public abstract
OutputStream
getResponseBody()

returns a stream to which the response body must be
written.

sendResponseHeaders(int,long)

) must be called prior to calling
this method. Multiple calls to this method (for the same exchange)
will return the same stream. In order to correctly terminate
each exchange, the output stream must be closed, even if no
response body is being sent.

Closing this stream implicitly
closes the InputStream returned from

getRequestBody()

(if it is not already closed).

If the call to sendResponseHeaders() specified a fixed response
body length, then the exact number of bytes specified in that
call must be written to this stream. If too many bytes are written,
then write() will throw an IOException. If too few bytes are written
then the stream close() will throw an IOException. In both cases,
the exchange is aborted and the underlying TCP connection closed.

**Returns:**
- the stream to which the response body is written

---

#### public abstract void sendResponseHeaders​(int rCode,
long responseLength)
throws
IOException

Starts sending the response back to the client using the current set of response headers
and the numeric response code as specified in this method. The response body length is also specified
as follows. If the response length parameter is greater than zero, this specifies an exact
number of bytes to send and the application must send that exact amount of data.
If the response length parameter is

zero

, then chunked transfer encoding is
used and an arbitrary amount of data may be sent. The application terminates the
response body by closing the OutputStream. If response length has the value

-1

then no response body is being sent.

If the content-length response header has not already been set then
this is set to the appropriate value depending on the response length parameter.

This method must be called prior to calling

getResponseBody()

.

**Parameters:**
- rCode

- the response code to send
- responseLength

- if > 0, specifies a fixed response
body length and that exact number of bytes must be written
to the stream acquired from getResponseBody(), or else
if equal to 0, then chunked encoding is used,
and an arbitrary number of bytes may be written.
if <= -1, then no response body length is specified and
no response body may be written.

**Throws:**
- IOException

**See Also:**
- getResponseBody()

---

#### public abstract
InetSocketAddress
getRemoteAddress()

Returns the address of the remote entity invoking this request

**Returns:**
- the InetSocketAddress of the caller

---

#### public abstract int getResponseCode()

Returns the response code, if it has already been set

**Returns:**
- the response code, if available.

-1

if not available yet.

---

#### public abstract
InetSocketAddress
getLocalAddress()

Returns the local address on which the request was received

**Returns:**
- the InetSocketAddress of the local interface

---

#### public abstract
String
getProtocol()

Returns the protocol string from the request in the form

protocol/majorVersion.minorVersion

. For example,
"HTTP/1.1"

**Returns:**
- the protocol string from the request

---

#### public abstract
Object
getAttribute​(
String
name)

Filter modules may store arbitrary objects with HttpExchange
instances as an out-of-band communication mechanism. Other Filters
or the exchange handler may then access these objects.

Each Filter class will document the attributes which they make
available.

**Parameters:**
- name

- the name of the attribute to retrieve

**Returns:**
- the attribute object, or null if it does not exist

**Throws:**
- NullPointerException

- if name is

null

---

#### public abstract void setAttribute​(
String
name,

Object
value)

Filter modules may store arbitrary objects with HttpExchange
instances as an out-of-band communication mechanism. Other Filters
or the exchange handler may then access these objects.

Each Filter class will document the attributes which they make
available.

**Parameters:**
- name

- the name to associate with the attribute value
- value

- the object to store as the attribute value.

null

value is permitted.

**Throws:**
- NullPointerException

- if name is

null

---

#### public abstract void setStreams​(
InputStream
i,

OutputStream
o)

Used by Filters to wrap either (or both) of this exchange's InputStream
and OutputStream, with the given filtered streams so
that subsequent calls to

getRequestBody()

will
return the given

InputStream

, and calls to

getResponseBody()

will return the given

OutputStream

. The streams provided to this
call must wrap the original streams, and may be (but are not
required to be) sub-classes of

FilterInputStream

and

FilterOutputStream

.

**Parameters:**
- i

- the filtered input stream to set as this object's inputstream,
or

null

if no change.
- o

- the filtered output stream to set as this object's outputstream,
or

null

if no change.

---

#### public abstract
HttpPrincipal
getPrincipal()

If an authenticator is set on the HttpContext that owns this exchange,
then this method will return the

HttpPrincipal

that represents
the authenticated user for this HttpExchange.

**Returns:**
- the HttpPrincipal, or

null

if no authenticator is set.

---

### Additional Sections

#### Class HttpExchange

java.lang.Object

- com.sun.net.httpserver.HttpExchange

com.sun.net.httpserver.HttpExchange

**Direct Known Subclasses:** HttpsExchange

```java
public abstract class
HttpExchange

extends
Object
```

This class encapsulates a HTTP request received and a
response to be generated in one exchange. It provides methods
for examining the request from the client, and for building and
sending the response.

The typical life-cycle of a HttpExchange is shown in the sequence
below.

- getRequestMethod()

to determine the command

getRequestHeaders()

to examine the request headers (if needed)

getRequestBody()

returns a

InputStream

for reading the request body.
After reading the request body, the stream is close.

getResponseHeaders()

to set any response headers, except content-length

sendResponseHeaders(int,long)

to send the response headers. Must be called before
next step.

getResponseBody()

to get a

OutputStream

to send the response body.
When the response body has been written, the stream must be closed to terminate the exchange.

Terminating exchanges

Exchanges are terminated when both the request InputStream and response OutputStream are closed.
Closing the OutputStream, implicitly closes the InputStream (if it is not already closed).
However, it is recommended
to consume all the data from the InputStream before closing it.
The convenience method

close()

does all of these tasks.
Closing an exchange without consuming all of the request body is not an error
but may make the underlying TCP connection unusable for following exchanges.
The effect of failing to terminate an exchange is undefined, but will typically
result in resources failing to be freed/reused.

**Since:** 1.6

public abstract class

HttpExchange

extends

Object

This class encapsulates a HTTP request received and a
response to be generated in one exchange. It provides methods
for examining the request from the client, and for building and
sending the response.

The typical life-cycle of a HttpExchange is shown in the sequence
below.

- getRequestMethod()

to determine the command

getRequestHeaders()

to examine the request headers (if needed)

getRequestBody()

returns a

InputStream

for reading the request body.
After reading the request body, the stream is close.

getResponseHeaders()

to set any response headers, except content-length

sendResponseHeaders(int,long)

to send the response headers. Must be called before
next step.

getResponseBody()

to get a

OutputStream

to send the response body.
When the response body has been written, the stream must be closed to terminate the exchange.

Terminating exchanges

Exchanges are terminated when both the request InputStream and response OutputStream are closed.
Closing the OutputStream, implicitly closes the InputStream (if it is not already closed).
However, it is recommended
to consume all the data from the InputStream before closing it.
The convenience method

close()

does all of these tasks.
Closing an exchange without consuming all of the request body is not an error
but may make the underlying TCP connection unusable for following exchanges.
The effect of failing to terminate an exchange is undefined, but will typically
result in resources failing to be freed/reused.

The typical life-cycle of a HttpExchange is shown in the sequence
below.

- getRequestMethod()

to determine the command

getRequestHeaders()

to examine the request headers (if needed)

getRequestBody()

returns a

InputStream

for reading the request body.
After reading the request body, the stream is close.

getResponseHeaders()

to set any response headers, except content-length

sendResponseHeaders(int,long)

to send the response headers. Must be called before
next step.

getResponseBody()

to get a

OutputStream

to send the response body.
When the response body has been written, the stream must be closed to terminate the exchange.

Terminating exchanges

Exchanges are terminated when both the request InputStream and response OutputStream are closed.
Closing the OutputStream, implicitly closes the InputStream (if it is not already closed).
However, it is recommended
to consume all the data from the InputStream before closing it.
The convenience method

close()

does all of these tasks.
Closing an exchange without consuming all of the request body is not an error
but may make the underlying TCP connection unusable for following exchanges.
The effect of failing to terminate an exchange is undefined, but will typically
result in resources failing to be freed/reused.

getRequestMethod()

to determine the command

getRequestHeaders()

to examine the request headers (if needed)

getRequestBody()

returns a

InputStream

for reading the request body.
After reading the request body, the stream is close.

getResponseHeaders()

to set any response headers, except content-length

sendResponseHeaders(int,long)

to send the response headers. Must be called before
next step.

getResponseBody()

to get a

OutputStream

to send the response body.
When the response body has been written, the stream must be closed to terminate the exchange.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

HttpExchange

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract void

close

()

Ends this exchange by doing the following in sequence:
close the request InputStream, if not already closed;
close the response OutputStream, if not already closed.

abstract

Object

getAttribute

​(

String

name)

Filter modules may store arbitrary objects with HttpExchange
instances as an out-of-band communication mechanism.

abstract

HttpContext

getHttpContext

()

Get the HttpContext for this exchange

abstract

InetSocketAddress

getLocalAddress

()

Returns the local address on which the request was received

abstract

HttpPrincipal

getPrincipal

()

If an authenticator is set on the HttpContext that owns this exchange,
then this method will return the

HttpPrincipal

that represents
the authenticated user for this HttpExchange.

abstract

String

getProtocol

()

Returns the protocol string from the request in the form

protocol/majorVersion.minorVersion

.

abstract

InetSocketAddress

getRemoteAddress

()

Returns the address of the remote entity invoking this request

abstract

InputStream

getRequestBody

()

returns a stream from which the request body can be read.

abstract

Headers

getRequestHeaders

()

Returns an immutable Map containing the HTTP headers that were
included with this request.

abstract

String

getRequestMethod

()

Get the request method

abstract

URI

getRequestURI

()

Get the request URI

abstract

OutputStream

getResponseBody

()

returns a stream to which the response body must be
written.

abstract int

getResponseCode

()

Returns the response code, if it has already been set

abstract

Headers

getResponseHeaders

()

Returns a mutable Map into which the HTTP response headers can be stored
and which will be transmitted as part of this response.

abstract void

sendResponseHeaders

​(int rCode,
long responseLength)

Starts sending the response back to the client using the current set of response headers
and the numeric response code as specified in this method.

abstract void

setAttribute

​(

String

name,

Object

value)

Filter modules may store arbitrary objects with HttpExchange
instances as an out-of-band communication mechanism.

abstract void

setStreams

​(

InputStream

i,

OutputStream

o)

Used by Filters to wrap either (or both) of this exchange's InputStream
and OutputStream, with the given filtered streams so
that subsequent calls to

getRequestBody()

will
return the given

InputStream

, and calls to

getResponseBody()

will return the given

OutputStream

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

Modifier

Constructor

Description

protected

HttpExchange

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract void

close

()

Ends this exchange by doing the following in sequence:
close the request InputStream, if not already closed;
close the response OutputStream, if not already closed.

abstract

Object

getAttribute

​(

String

name)

Filter modules may store arbitrary objects with HttpExchange
instances as an out-of-band communication mechanism.

abstract

HttpContext

getHttpContext

()

Get the HttpContext for this exchange

abstract

InetSocketAddress

getLocalAddress

()

Returns the local address on which the request was received

abstract

HttpPrincipal

getPrincipal

()

If an authenticator is set on the HttpContext that owns this exchange,
then this method will return the

HttpPrincipal

that represents
the authenticated user for this HttpExchange.

abstract

String

getProtocol

()

Returns the protocol string from the request in the form

protocol/majorVersion.minorVersion

.

abstract

InetSocketAddress

getRemoteAddress

()

Returns the address of the remote entity invoking this request

abstract

InputStream

getRequestBody

()

returns a stream from which the request body can be read.

abstract

Headers

getRequestHeaders

()

Returns an immutable Map containing the HTTP headers that were
included with this request.

abstract

String

getRequestMethod

()

Get the request method

abstract

URI

getRequestURI

()

Get the request URI

abstract

OutputStream

getResponseBody

()

returns a stream to which the response body must be
written.

abstract int

getResponseCode

()

Returns the response code, if it has already been set

abstract

Headers

getResponseHeaders

()

Returns a mutable Map into which the HTTP response headers can be stored
and which will be transmitted as part of this response.

abstract void

sendResponseHeaders

​(int rCode,
long responseLength)

Starts sending the response back to the client using the current set of response headers
and the numeric response code as specified in this method.

abstract void

setAttribute

​(

String

name,

Object

value)

Filter modules may store arbitrary objects with HttpExchange
instances as an out-of-band communication mechanism.

abstract void

setStreams

​(

InputStream

i,

OutputStream

o)

Used by Filters to wrap either (or both) of this exchange's InputStream
and OutputStream, with the given filtered streams so
that subsequent calls to

getRequestBody()

will
return the given

InputStream

, and calls to

getResponseBody()

will return the given

OutputStream

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

Ends this exchange by doing the following in sequence:
close the request InputStream, if not already closed;
close the response OutputStream, if not already closed.

Filter modules may store arbitrary objects with HttpExchange
instances as an out-of-band communication mechanism.

Get the HttpContext for this exchange

Returns the local address on which the request was received

If an authenticator is set on the HttpContext that owns this exchange,
then this method will return the

HttpPrincipal

that represents
the authenticated user for this HttpExchange.

Returns the protocol string from the request in the form

protocol/majorVersion.minorVersion

.

Returns the address of the remote entity invoking this request

returns a stream from which the request body can be read.

Returns an immutable Map containing the HTTP headers that were
included with this request.

Get the request method

Get the request URI

returns a stream to which the response body must be
written.

Returns the response code, if it has already been set

Returns a mutable Map into which the HTTP response headers can be stored
and which will be transmitted as part of this response.

Starts sending the response back to the client using the current set of response headers
and the numeric response code as specified in this method.

Used by Filters to wrap either (or both) of this exchange's InputStream
and OutputStream, with the given filtered streams so
that subsequent calls to

getRequestBody()

will
return the given

InputStream

, and calls to

getResponseBody()

will return the given

OutputStream

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

- HttpExchange

```java
protected HttpExchange()
```

============ METHOD DETAIL ==========

- Method Detail

- getRequestHeaders

```java
public abstract
Headers
getRequestHeaders()
```

Returns an immutable Map containing the HTTP headers that were
included with this request. The keys in this Map will be the header
names, while the values will be a List of Strings containing each value
that was included (either for a header that was listed several times,
or one that accepts a comma-delimited list of values on a single line).
In either of these cases, the values for the header name will be
presented in the order that they were included in the request.

The keys in Map are case-insensitive.

**Returns:** a read-only Map which can be used to access request headers

- getResponseHeaders

```java
public abstract
Headers
getResponseHeaders()
```

Returns a mutable Map into which the HTTP response headers can be stored
and which will be transmitted as part of this response. The keys in the
Map will be the header names, while the values must be a List of Strings
containing each value that should be included multiple times
(in the order that they should be included).

The keys in Map are case-insensitive.

**Returns:** a writable Map which can be used to set response headers.

- getRequestURI

```java
public abstract
URI
getRequestURI()
```

Get the request URI

**Returns:** the request URI

- getRequestMethod

```java
public abstract
String
getRequestMethod()
```

Get the request method

**Returns:** the request method

- getHttpContext

```java
public abstract
HttpContext
getHttpContext()
```

Get the HttpContext for this exchange

**Returns:** the HttpContext

- close

```java
public abstract void close()
```

Ends this exchange by doing the following in sequence:

- close the request InputStream, if not already closed;
- close the response OutputStream, if not already closed.

- getRequestBody

```java
public abstract
InputStream
getRequestBody()
```

returns a stream from which the request body can be read.
Multiple calls to this method will return the same stream.
It is recommended that applications should consume (read) all of the
data from this stream before closing it. If a stream is closed
before all data has been read, then the close() call will
read and discard remaining data (up to an implementation specific
number of bytes).

**Returns:** the stream from which the request body can be read.

- getResponseBody

```java
public abstract
OutputStream
getResponseBody()
```

returns a stream to which the response body must be
written.

sendResponseHeaders(int,long)

) must be called prior to calling
this method. Multiple calls to this method (for the same exchange)
will return the same stream. In order to correctly terminate
each exchange, the output stream must be closed, even if no
response body is being sent.

Closing this stream implicitly
closes the InputStream returned from

getRequestBody()

(if it is not already closed).

If the call to sendResponseHeaders() specified a fixed response
body length, then the exact number of bytes specified in that
call must be written to this stream. If too many bytes are written,
then write() will throw an IOException. If too few bytes are written
then the stream close() will throw an IOException. In both cases,
the exchange is aborted and the underlying TCP connection closed.

**Returns:** the stream to which the response body is written

- sendResponseHeaders

```java
public abstract void sendResponseHeaders​(int rCode,
long responseLength)
throws
IOException
```

Starts sending the response back to the client using the current set of response headers
and the numeric response code as specified in this method. The response body length is also specified
as follows. If the response length parameter is greater than zero, this specifies an exact
number of bytes to send and the application must send that exact amount of data.
If the response length parameter is

zero

, then chunked transfer encoding is
used and an arbitrary amount of data may be sent. The application terminates the
response body by closing the OutputStream. If response length has the value

-1

then no response body is being sent.

If the content-length response header has not already been set then
this is set to the appropriate value depending on the response length parameter.

This method must be called prior to calling

getResponseBody()

.

**Parameters:** rCode

- the response code to send
**Parameters:** responseLength

- if > 0, specifies a fixed response
body length and that exact number of bytes must be written
to the stream acquired from getResponseBody(), or else
if equal to 0, then chunked encoding is used,
and an arbitrary number of bytes may be written.
if <= -1, then no response body length is specified and
no response body may be written.
**Throws:** IOException
**See Also:** getResponseBody()

- getRemoteAddress

```java
public abstract
InetSocketAddress
getRemoteAddress()
```

Returns the address of the remote entity invoking this request

**Returns:** the InetSocketAddress of the caller

- getResponseCode

```java
public abstract int getResponseCode()
```

Returns the response code, if it has already been set

**Returns:** the response code, if available.

-1

if not available yet.

- getLocalAddress

```java
public abstract
InetSocketAddress
getLocalAddress()
```

Returns the local address on which the request was received

**Returns:** the InetSocketAddress of the local interface

- getProtocol

```java
public abstract
String
getProtocol()
```

Returns the protocol string from the request in the form

protocol/majorVersion.minorVersion

. For example,
"HTTP/1.1"

**Returns:** the protocol string from the request

- getAttribute

```java
public abstract
Object
getAttribute​(
String
name)
```

Filter modules may store arbitrary objects with HttpExchange
instances as an out-of-band communication mechanism. Other Filters
or the exchange handler may then access these objects.

Each Filter class will document the attributes which they make
available.

**Parameters:** name

- the name of the attribute to retrieve
**Returns:** the attribute object, or null if it does not exist
**Throws:** NullPointerException

- if name is

null

- setAttribute

```java
public abstract void setAttribute​(
String
name,

Object
value)
```

Filter modules may store arbitrary objects with HttpExchange
instances as an out-of-band communication mechanism. Other Filters
or the exchange handler may then access these objects.

Each Filter class will document the attributes which they make
available.

**Parameters:** name

- the name to associate with the attribute value
**Parameters:** value

- the object to store as the attribute value.

null

value is permitted.
**Throws:** NullPointerException

- if name is

null

- setStreams

```java
public abstract void setStreams​(
InputStream
i,

OutputStream
o)
```

Used by Filters to wrap either (or both) of this exchange's InputStream
and OutputStream, with the given filtered streams so
that subsequent calls to

getRequestBody()

will
return the given

InputStream

, and calls to

getResponseBody()

will return the given

OutputStream

. The streams provided to this
call must wrap the original streams, and may be (but are not
required to be) sub-classes of

FilterInputStream

and

FilterOutputStream

.

**Parameters:** i

- the filtered input stream to set as this object's inputstream,
or

null

if no change.
**Parameters:** o

- the filtered output stream to set as this object's outputstream,
or

null

if no change.

- getPrincipal

```java
public abstract
HttpPrincipal
getPrincipal()
```

If an authenticator is set on the HttpContext that owns this exchange,
then this method will return the

HttpPrincipal

that represents
the authenticated user for this HttpExchange.

**Returns:** the HttpPrincipal, or

null

if no authenticator is set.

Constructor Detail

- HttpExchange

```java
protected HttpExchange()
```

---

#### Constructor Detail

HttpExchange

```java
protected HttpExchange()
```

---

#### HttpExchange

protected HttpExchange()

Method Detail

- getRequestHeaders

```java
public abstract
Headers
getRequestHeaders()
```

Returns an immutable Map containing the HTTP headers that were
included with this request. The keys in this Map will be the header
names, while the values will be a List of Strings containing each value
that was included (either for a header that was listed several times,
or one that accepts a comma-delimited list of values on a single line).
In either of these cases, the values for the header name will be
presented in the order that they were included in the request.

The keys in Map are case-insensitive.

**Returns:** a read-only Map which can be used to access request headers

- getResponseHeaders

```java
public abstract
Headers
getResponseHeaders()
```

Returns a mutable Map into which the HTTP response headers can be stored
and which will be transmitted as part of this response. The keys in the
Map will be the header names, while the values must be a List of Strings
containing each value that should be included multiple times
(in the order that they should be included).

The keys in Map are case-insensitive.

**Returns:** a writable Map which can be used to set response headers.

- getRequestURI

```java
public abstract
URI
getRequestURI()
```

Get the request URI

**Returns:** the request URI

- getRequestMethod

```java
public abstract
String
getRequestMethod()
```

Get the request method

**Returns:** the request method

- getHttpContext

```java
public abstract
HttpContext
getHttpContext()
```

Get the HttpContext for this exchange

**Returns:** the HttpContext

- close

```java
public abstract void close()
```

Ends this exchange by doing the following in sequence:

- close the request InputStream, if not already closed;
- close the response OutputStream, if not already closed.

- getRequestBody

```java
public abstract
InputStream
getRequestBody()
```

returns a stream from which the request body can be read.
Multiple calls to this method will return the same stream.
It is recommended that applications should consume (read) all of the
data from this stream before closing it. If a stream is closed
before all data has been read, then the close() call will
read and discard remaining data (up to an implementation specific
number of bytes).

**Returns:** the stream from which the request body can be read.

- getResponseBody

```java
public abstract
OutputStream
getResponseBody()
```

returns a stream to which the response body must be
written.

sendResponseHeaders(int,long)

) must be called prior to calling
this method. Multiple calls to this method (for the same exchange)
will return the same stream. In order to correctly terminate
each exchange, the output stream must be closed, even if no
response body is being sent.

Closing this stream implicitly
closes the InputStream returned from

getRequestBody()

(if it is not already closed).

If the call to sendResponseHeaders() specified a fixed response
body length, then the exact number of bytes specified in that
call must be written to this stream. If too many bytes are written,
then write() will throw an IOException. If too few bytes are written
then the stream close() will throw an IOException. In both cases,
the exchange is aborted and the underlying TCP connection closed.

**Returns:** the stream to which the response body is written

- sendResponseHeaders

```java
public abstract void sendResponseHeaders​(int rCode,
long responseLength)
throws
IOException
```

Starts sending the response back to the client using the current set of response headers
and the numeric response code as specified in this method. The response body length is also specified
as follows. If the response length parameter is greater than zero, this specifies an exact
number of bytes to send and the application must send that exact amount of data.
If the response length parameter is

zero

, then chunked transfer encoding is
used and an arbitrary amount of data may be sent. The application terminates the
response body by closing the OutputStream. If response length has the value

-1

then no response body is being sent.

If the content-length response header has not already been set then
this is set to the appropriate value depending on the response length parameter.

This method must be called prior to calling

getResponseBody()

.

**Parameters:** rCode

- the response code to send
**Parameters:** responseLength

- if > 0, specifies a fixed response
body length and that exact number of bytes must be written
to the stream acquired from getResponseBody(), or else
if equal to 0, then chunked encoding is used,
and an arbitrary number of bytes may be written.
if <= -1, then no response body length is specified and
no response body may be written.
**Throws:** IOException
**See Also:** getResponseBody()

- getRemoteAddress

```java
public abstract
InetSocketAddress
getRemoteAddress()
```

Returns the address of the remote entity invoking this request

**Returns:** the InetSocketAddress of the caller

- getResponseCode

```java
public abstract int getResponseCode()
```

Returns the response code, if it has already been set

**Returns:** the response code, if available.

-1

if not available yet.

- getLocalAddress

```java
public abstract
InetSocketAddress
getLocalAddress()
```

Returns the local address on which the request was received

**Returns:** the InetSocketAddress of the local interface

- getProtocol

```java
public abstract
String
getProtocol()
```

Returns the protocol string from the request in the form

protocol/majorVersion.minorVersion

. For example,
"HTTP/1.1"

**Returns:** the protocol string from the request

- getAttribute

```java
public abstract
Object
getAttribute​(
String
name)
```

Filter modules may store arbitrary objects with HttpExchange
instances as an out-of-band communication mechanism. Other Filters
or the exchange handler may then access these objects.

Each Filter class will document the attributes which they make
available.

**Parameters:** name

- the name of the attribute to retrieve
**Returns:** the attribute object, or null if it does not exist
**Throws:** NullPointerException

- if name is

null

- setAttribute

```java
public abstract void setAttribute​(
String
name,

Object
value)
```

Filter modules may store arbitrary objects with HttpExchange
instances as an out-of-band communication mechanism. Other Filters
or the exchange handler may then access these objects.

Each Filter class will document the attributes which they make
available.

**Parameters:** name

- the name to associate with the attribute value
**Parameters:** value

- the object to store as the attribute value.

null

value is permitted.
**Throws:** NullPointerException

- if name is

null

- setStreams

```java
public abstract void setStreams​(
InputStream
i,

OutputStream
o)
```

Used by Filters to wrap either (or both) of this exchange's InputStream
and OutputStream, with the given filtered streams so
that subsequent calls to

getRequestBody()

will
return the given

InputStream

, and calls to

getResponseBody()

will return the given

OutputStream

. The streams provided to this
call must wrap the original streams, and may be (but are not
required to be) sub-classes of

FilterInputStream

and

FilterOutputStream

.

**Parameters:** i

- the filtered input stream to set as this object's inputstream,
or

null

if no change.
**Parameters:** o

- the filtered output stream to set as this object's outputstream,
or

null

if no change.

- getPrincipal

```java
public abstract
HttpPrincipal
getPrincipal()
```

If an authenticator is set on the HttpContext that owns this exchange,
then this method will return the

HttpPrincipal

that represents
the authenticated user for this HttpExchange.

**Returns:** the HttpPrincipal, or

null

if no authenticator is set.

---

#### Method Detail

getRequestHeaders

```java
public abstract
Headers
getRequestHeaders()
```

Returns an immutable Map containing the HTTP headers that were
included with this request. The keys in this Map will be the header
names, while the values will be a List of Strings containing each value
that was included (either for a header that was listed several times,
or one that accepts a comma-delimited list of values on a single line).
In either of these cases, the values for the header name will be
presented in the order that they were included in the request.

The keys in Map are case-insensitive.

**Returns:** a read-only Map which can be used to access request headers

---

#### getRequestHeaders

public abstract

Headers

getRequestHeaders()

Returns an immutable Map containing the HTTP headers that were
included with this request. The keys in this Map will be the header
names, while the values will be a List of Strings containing each value
that was included (either for a header that was listed several times,
or one that accepts a comma-delimited list of values on a single line).
In either of these cases, the values for the header name will be
presented in the order that they were included in the request.

The keys in Map are case-insensitive.

The keys in Map are case-insensitive.

getResponseHeaders

```java
public abstract
Headers
getResponseHeaders()
```

Returns a mutable Map into which the HTTP response headers can be stored
and which will be transmitted as part of this response. The keys in the
Map will be the header names, while the values must be a List of Strings
containing each value that should be included multiple times
(in the order that they should be included).

The keys in Map are case-insensitive.

**Returns:** a writable Map which can be used to set response headers.

---

#### getResponseHeaders

public abstract

Headers

getResponseHeaders()

Returns a mutable Map into which the HTTP response headers can be stored
and which will be transmitted as part of this response. The keys in the
Map will be the header names, while the values must be a List of Strings
containing each value that should be included multiple times
(in the order that they should be included).

The keys in Map are case-insensitive.

The keys in Map are case-insensitive.

getRequestURI

```java
public abstract
URI
getRequestURI()
```

Get the request URI

**Returns:** the request URI

---

#### getRequestURI

public abstract

URI

getRequestURI()

Get the request URI

getRequestMethod

```java
public abstract
String
getRequestMethod()
```

Get the request method

**Returns:** the request method

---

#### getRequestMethod

public abstract

String

getRequestMethod()

Get the request method

getHttpContext

```java
public abstract
HttpContext
getHttpContext()
```

Get the HttpContext for this exchange

**Returns:** the HttpContext

---

#### getHttpContext

public abstract

HttpContext

getHttpContext()

Get the HttpContext for this exchange

close

```java
public abstract void close()
```

Ends this exchange by doing the following in sequence:

- close the request InputStream, if not already closed;
- close the response OutputStream, if not already closed.

---

#### close

public abstract void close()

Ends this exchange by doing the following in sequence:

- close the request InputStream, if not already closed;
- close the response OutputStream, if not already closed.

close the request InputStream, if not already closed;

close the response OutputStream, if not already closed.

getRequestBody

```java
public abstract
InputStream
getRequestBody()
```

returns a stream from which the request body can be read.
Multiple calls to this method will return the same stream.
It is recommended that applications should consume (read) all of the
data from this stream before closing it. If a stream is closed
before all data has been read, then the close() call will
read and discard remaining data (up to an implementation specific
number of bytes).

**Returns:** the stream from which the request body can be read.

---

#### getRequestBody

public abstract

InputStream

getRequestBody()

returns a stream from which the request body can be read.
Multiple calls to this method will return the same stream.
It is recommended that applications should consume (read) all of the
data from this stream before closing it. If a stream is closed
before all data has been read, then the close() call will
read and discard remaining data (up to an implementation specific
number of bytes).

getResponseBody

```java
public abstract
OutputStream
getResponseBody()
```

returns a stream to which the response body must be
written.

sendResponseHeaders(int,long)

) must be called prior to calling
this method. Multiple calls to this method (for the same exchange)
will return the same stream. In order to correctly terminate
each exchange, the output stream must be closed, even if no
response body is being sent.

Closing this stream implicitly
closes the InputStream returned from

getRequestBody()

(if it is not already closed).

If the call to sendResponseHeaders() specified a fixed response
body length, then the exact number of bytes specified in that
call must be written to this stream. If too many bytes are written,
then write() will throw an IOException. If too few bytes are written
then the stream close() will throw an IOException. In both cases,
the exchange is aborted and the underlying TCP connection closed.

**Returns:** the stream to which the response body is written

---

#### getResponseBody

public abstract

OutputStream

getResponseBody()

returns a stream to which the response body must be
written.

sendResponseHeaders(int,long)

) must be called prior to calling
this method. Multiple calls to this method (for the same exchange)
will return the same stream. In order to correctly terminate
each exchange, the output stream must be closed, even if no
response body is being sent.

Closing this stream implicitly
closes the InputStream returned from

getRequestBody()

(if it is not already closed).

If the call to sendResponseHeaders() specified a fixed response
body length, then the exact number of bytes specified in that
call must be written to this stream. If too many bytes are written,
then write() will throw an IOException. If too few bytes are written
then the stream close() will throw an IOException. In both cases,
the exchange is aborted and the underlying TCP connection closed.

Closing this stream implicitly
closes the InputStream returned from

getRequestBody()

(if it is not already closed).

If the call to sendResponseHeaders() specified a fixed response
body length, then the exact number of bytes specified in that
call must be written to this stream. If too many bytes are written,
then write() will throw an IOException. If too few bytes are written
then the stream close() will throw an IOException. In both cases,
the exchange is aborted and the underlying TCP connection closed.

If the call to sendResponseHeaders() specified a fixed response
body length, then the exact number of bytes specified in that
call must be written to this stream. If too many bytes are written,
then write() will throw an IOException. If too few bytes are written
then the stream close() will throw an IOException. In both cases,
the exchange is aborted and the underlying TCP connection closed.

sendResponseHeaders

```java
public abstract void sendResponseHeaders​(int rCode,
long responseLength)
throws
IOException
```

Starts sending the response back to the client using the current set of response headers
and the numeric response code as specified in this method. The response body length is also specified
as follows. If the response length parameter is greater than zero, this specifies an exact
number of bytes to send and the application must send that exact amount of data.
If the response length parameter is

zero

, then chunked transfer encoding is
used and an arbitrary amount of data may be sent. The application terminates the
response body by closing the OutputStream. If response length has the value

-1

then no response body is being sent.

If the content-length response header has not already been set then
this is set to the appropriate value depending on the response length parameter.

This method must be called prior to calling

getResponseBody()

.

**Parameters:** rCode

- the response code to send
**Parameters:** responseLength

- if > 0, specifies a fixed response
body length and that exact number of bytes must be written
to the stream acquired from getResponseBody(), or else
if equal to 0, then chunked encoding is used,
and an arbitrary number of bytes may be written.
if <= -1, then no response body length is specified and
no response body may be written.
**Throws:** IOException
**See Also:** getResponseBody()

---

#### sendResponseHeaders

public abstract void sendResponseHeaders​(int rCode,
long responseLength)
throws

IOException

Starts sending the response back to the client using the current set of response headers
and the numeric response code as specified in this method. The response body length is also specified
as follows. If the response length parameter is greater than zero, this specifies an exact
number of bytes to send and the application must send that exact amount of data.
If the response length parameter is

zero

, then chunked transfer encoding is
used and an arbitrary amount of data may be sent. The application terminates the
response body by closing the OutputStream. If response length has the value

-1

then no response body is being sent.

If the content-length response header has not already been set then
this is set to the appropriate value depending on the response length parameter.

This method must be called prior to calling

getResponseBody()

.

If the content-length response header has not already been set then
this is set to the appropriate value depending on the response length parameter.

This method must be called prior to calling

getResponseBody()

.

This method must be called prior to calling

getResponseBody()

.

getRemoteAddress

```java
public abstract
InetSocketAddress
getRemoteAddress()
```

Returns the address of the remote entity invoking this request

**Returns:** the InetSocketAddress of the caller

---

#### getRemoteAddress

public abstract

InetSocketAddress

getRemoteAddress()

Returns the address of the remote entity invoking this request

getResponseCode

```java
public abstract int getResponseCode()
```

Returns the response code, if it has already been set

**Returns:** the response code, if available.

-1

if not available yet.

---

#### getResponseCode

public abstract int getResponseCode()

Returns the response code, if it has already been set

getLocalAddress

```java
public abstract
InetSocketAddress
getLocalAddress()
```

Returns the local address on which the request was received

**Returns:** the InetSocketAddress of the local interface

---

#### getLocalAddress

public abstract

InetSocketAddress

getLocalAddress()

Returns the local address on which the request was received

getProtocol

```java
public abstract
String
getProtocol()
```

Returns the protocol string from the request in the form

protocol/majorVersion.minorVersion

. For example,
"HTTP/1.1"

**Returns:** the protocol string from the request

---

#### getProtocol

public abstract

String

getProtocol()

Returns the protocol string from the request in the form

protocol/majorVersion.minorVersion

. For example,
"HTTP/1.1"

getAttribute

```java
public abstract
Object
getAttribute​(
String
name)
```

Filter modules may store arbitrary objects with HttpExchange
instances as an out-of-band communication mechanism. Other Filters
or the exchange handler may then access these objects.

Each Filter class will document the attributes which they make
available.

**Parameters:** name

- the name of the attribute to retrieve
**Returns:** the attribute object, or null if it does not exist
**Throws:** NullPointerException

- if name is

null

---

#### getAttribute

public abstract

Object

getAttribute​(

String

name)

Filter modules may store arbitrary objects with HttpExchange
instances as an out-of-band communication mechanism. Other Filters
or the exchange handler may then access these objects.

Each Filter class will document the attributes which they make
available.

Each Filter class will document the attributes which they make
available.

setAttribute

```java
public abstract void setAttribute​(
String
name,

Object
value)
```

Filter modules may store arbitrary objects with HttpExchange
instances as an out-of-band communication mechanism. Other Filters
or the exchange handler may then access these objects.

Each Filter class will document the attributes which they make
available.

**Parameters:** name

- the name to associate with the attribute value
**Parameters:** value

- the object to store as the attribute value.

null

value is permitted.
**Throws:** NullPointerException

- if name is

null

---

#### setAttribute

public abstract void setAttribute​(

String

name,

Object

value)

Filter modules may store arbitrary objects with HttpExchange
instances as an out-of-band communication mechanism. Other Filters
or the exchange handler may then access these objects.

Each Filter class will document the attributes which they make
available.

Each Filter class will document the attributes which they make
available.

setStreams

```java
public abstract void setStreams​(
InputStream
i,

OutputStream
o)
```

Used by Filters to wrap either (or both) of this exchange's InputStream
and OutputStream, with the given filtered streams so
that subsequent calls to

getRequestBody()

will
return the given

InputStream

, and calls to

getResponseBody()

will return the given

OutputStream

. The streams provided to this
call must wrap the original streams, and may be (but are not
required to be) sub-classes of

FilterInputStream

and

FilterOutputStream

.

**Parameters:** i

- the filtered input stream to set as this object's inputstream,
or

null

if no change.
**Parameters:** o

- the filtered output stream to set as this object's outputstream,
or

null

if no change.

---

#### setStreams

public abstract void setStreams​(

InputStream

i,

OutputStream

o)

Used by Filters to wrap either (or both) of this exchange's InputStream
and OutputStream, with the given filtered streams so
that subsequent calls to

getRequestBody()

will
return the given

InputStream

, and calls to

getResponseBody()

will return the given

OutputStream

. The streams provided to this
call must wrap the original streams, and may be (but are not
required to be) sub-classes of

FilterInputStream

and

FilterOutputStream

.

getPrincipal

```java
public abstract
HttpPrincipal
getPrincipal()
```

If an authenticator is set on the HttpContext that owns this exchange,
then this method will return the

HttpPrincipal

that represents
the authenticated user for this HttpExchange.

**Returns:** the HttpPrincipal, or

null

if no authenticator is set.

---

#### getPrincipal

public abstract

HttpPrincipal

getPrincipal()

If an authenticator is set on the HttpContext that owns this exchange,
then this method will return the

HttpPrincipal

that represents
the authenticated user for this HttpExchange.

---

