# Class HttpResponse.BodyHandlers

**Source:** `java.net.http\java\net\http\HttpResponse.BodyHandlers.html`

### Class Description

```java
public static class
HttpResponse.BodyHandlers

extends
Object
```

Implementations of

BodyHandler

that implement various
useful handlers, such as handling the response body as a String, or
streaming the response body to a file.

These implementations do not examine the status code, meaning the
body is always accepted. They typically return an equivalently named

BodySubscriber

. Alternatively, a custom handler can be used to
examine the status code and headers, and return a different body
subscriber, of the same type, as appropriate.

The following are examples of using the predefined body handlers to
convert a flow of response body data into common high-level Java objects:

```java
// Receives the response body as a String
HttpResponse<String> response = client
.send(request, BodyHandlers.ofString());

// Receives the response body as a file
HttpResponse<Path> response = client
.send(request, BodyHandlers.ofFile(Paths.get("example.html")));

// Receives the response body as an InputStream
HttpResponse<InputStream> response = client
.send(request, BodyHandlers.ofInputStream());

// Discards the response body
HttpResponse<Void> response = client
.send(request, BodyHandlers.discarding());
```

**Enclosing interface:** HttpResponse

<

T

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
HttpResponse.BodyHandler
<
Void
> fromSubscriber​(
Flow.Subscriber
<? super
List
<
ByteBuffer
>> subscriber)

Returns a response body handler that returns a

BodySubscriber

<Void>

obtained from

HttpResponse.BodySubscribers.fromSubscriber(Subscriber)

, with the given

subscriber

.

The response body is not available through this, or the

HttpResponse

API, but instead all response body is forwarded to the
given

subscriber

, which should make it available, if
appropriate, through some other mechanism, e.g. an entry in a
database, etc.

**Parameters:**
- subscriber

- the subscriber

**Returns:**
- a response body handler

**API Note:**
- This method can be used as an adapter between

BodySubscriber

and

Flow.Subscriber

.

For example:

```java
TextSubscriber subscriber = new TextSubscriber();
HttpResponse<Void> response = client.sendAsync(request,
BodyHandlers.fromSubscriber(subscriber)).join();
System.out.println(response.statusCode());
```

---

#### public static <S extends
Flow.Subscriber
<? super
List
<
ByteBuffer
>>,​T>
HttpResponse.BodyHandler
<T> fromSubscriber​(S subscriber,

Function
<? super S,​? extends T> finisher)

Returns a response body handler that returns a

BodySubscriber

<T>

obtained from

HttpResponse.BodySubscribers.fromSubscriber(Subscriber, Function)

, with the
given

subscriber

and

finisher

function.

The given

finisher

function is applied after the given
subscriber's

onComplete

has been invoked. The

finisher

function is invoked with the given subscriber, and returns a value
that is set as the response's body.

**Parameters:**
- subscriber

- the subscriber
- finisher

- a function to be applied after the subscriber has completed

**Returns:**
- a response body handler

**API Note:**
- This method can be used as an adapter between

BodySubscriber

and

Flow.Subscriber

.

For example:

```java
TextSubscriber subscriber = ...; // accumulates bytes and transforms them into a String
HttpResponse<String> response = client.sendAsync(request,
BodyHandlers.fromSubscriber(subscriber, TextSubscriber::getTextResult)).join();
String text = response.body();
```

**Type Parameters:**
- S

- the type of the Subscriber
- T

- the type of the response body

---

#### public static
HttpResponse.BodyHandler
<
Void
> fromLineSubscriber​(
Flow.Subscriber
<? super
String
> subscriber)

Returns a response body handler that returns a

BodySubscriber

<Void>

obtained from

BodySubscribers.fromLineSubscriber(subscriber, s -> null, charset, null)

,
with the given

subscriber

.
The

charset

used to decode the response body bytes is
obtained from the HTTP response headers as specified by

ofString()

,
and lines are delimited in the manner of

BufferedReader.readLine()

.

The response body is not available through this, or the

HttpResponse

API, but instead all response body is forwarded to the
given

subscriber

, which should make it available, if
appropriate, through some other mechanism, e.g. an entry in a
database, etc.

**Parameters:**
- subscriber

- the subscriber

**Returns:**
- a response body handler

**API Note:**
- This method can be used as an adapter between a

BodySubscriber

and a text based

Flow.Subscriber

that parses
text line by line.

For example:

```java
// A PrintSubscriber that implements Flow.Subscriber<String>
// and print lines received by onNext() on System.out
PrintSubscriber subscriber = new PrintSubscriber(System.out);
client.sendAsync(request, BodyHandlers.fromLineSubscriber(subscriber))
.thenApply(HttpResponse::statusCode)
.thenAccept((status) -> {
if (status != 200) {
System.err.printf("ERROR: %d status received%n", status);
}
});
```

---

#### public static <S extends
Flow.Subscriber
<? super
String
>,​T>
HttpResponse.BodyHandler
<T> fromLineSubscriber​(S subscriber,

Function
<? super S,​? extends T> finisher,

String
lineSeparator)

Returns a response body handler that returns a

BodySubscriber

<T>

obtained from

BodySubscribers.fromLineSubscriber(subscriber, finisher, charset, lineSeparator)

,
with the given

subscriber

,

finisher

function, and line separator.
The

charset

used to decode the response body bytes is
obtained from the HTTP response headers as specified by

ofString()

.

The given

finisher

function is applied after the given
subscriber's

onComplete

has been invoked. The

finisher

function is invoked with the given subscriber, and returns a value
that is set as the response's body.

**Parameters:**
- subscriber

- the subscriber
- finisher

- a function to be applied after the subscriber has completed
- lineSeparator

- an optional line separator: can be

null

,
in which case lines will be delimited in the manner of

BufferedReader.readLine()

.

**Returns:**
- a response body handler

**Throws:**
- IllegalArgumentException

- if the supplied

lineSeparator

is the empty string

**API Note:**
- This method can be used as an adapter between a

BodySubscriber

and a text based

Flow.Subscriber

that parses
text line by line.

For example:

```java
// A LineParserSubscriber that implements Flow.Subscriber<String>
// and accumulates lines that match a particular pattern
Pattern pattern = ...;
LineParserSubscriber subscriber = new LineParserSubscriber(pattern);
HttpResponse<List<String>> response = client.send(request,
BodyHandlers.fromLineSubscriber(subscriber, s -> s.getMatchingLines(), "\n"));
if (response.statusCode() != 200) {
System.err.printf("ERROR: %d status received%n", response.statusCode());
}
```

**Type Parameters:**
- S

- the type of the Subscriber
- T

- the type of the response body

---

#### public static
HttpResponse.BodyHandler
<
Void
> discarding()

Returns a response body handler that discards the response body.

**Returns:**
- a response body handler

---

#### public static <U>
HttpResponse.BodyHandler
<U> replacing​(U value)

Returns a response body handler that returns the given replacement
value, after discarding the response body.

**Parameters:**
- value

- the value of U to return as the body, may be

null

**Returns:**
- a response body handler

**Type Parameters:**
- U

- the response body type

---

#### public static
HttpResponse.BodyHandler
<
String
> ofString​(
Charset
charset)

Returns a

BodyHandler<String>

that returns a

BodySubscriber

<String>

obtained from

BodySubscribers.ofString(Charset)

.
The body is decoded using the given character set.

**Parameters:**
- charset

- the character set to convert the body with

**Returns:**
- a response body handler

---

#### public static
HttpResponse.BodyHandler
<
Path
> ofFile​(
Path
file,

OpenOption
... openOptions)

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<Path>

obtained from

BodySubscribers.ofFile(Path,OpenOption...)

.

When the

HttpResponse

object is returned, the body has
been completely written to the file, and

HttpResponse.body()

returns a
reference to its

Path

.

Security manager permission checks are performed in this factory
method, when the

BodyHandler

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

**Parameters:**
- file

- the file to store the body in
- openOptions

- any options to use when opening/creating the file

**Returns:**
- a response body handler

**Throws:**
- IllegalArgumentException

- if an invalid set of open options
are specified
- SecurityException

- If a security manager has been installed
and it denies

write access

to the file.

---

#### public static
HttpResponse.BodyHandler
<
Path
> ofFile​(
Path
file)

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<Path>

.

Equivalent to:

ofFile(file, CREATE, WRITE)

Security manager permission checks are performed in this factory
method, when the

BodyHandler

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

**Parameters:**
- file

- the file to store the body in

**Returns:**
- a response body handler

**Throws:**
- SecurityException

- If a security manager has been installed
and it denies

write access

to the file.

---

#### public static
HttpResponse.BodyHandler
<
Path
> ofFileDownload​(
Path
directory,

OpenOption
... openOptions)

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<

Path

>
where the download directory is specified, but the filename is
obtained from the

Content-Disposition

response header. The

Content-Disposition

header must specify the

attachment

type and must also contain a

filename

parameter. If the
filename specifies multiple path components only the final component
is used as the filename (with the given directory name).

When the

HttpResponse

object is returned, the body has
been completely written to the file and

HttpResponse.body()

returns a

Path

object for the file. The returned

Path

is the
combination of the supplied directory name and the file name supplied
by the server. If the destination directory does not exist or cannot
be written to, then the response will fail with an

IOException

.

Security manager permission checks are performed in this factory
method, when the

BodyHandler

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

**Parameters:**
- directory

- the directory to store the file in
- openOptions

- open options used when opening the file

**Returns:**
- a response body handler

**Throws:**
- IllegalArgumentException

- if the given path does not exist,
is not a directory, is not writable, or if an invalid set
of open options are specified
- SecurityException

- If a security manager has been installed
and it denies

read access

to the directory, or it denies

write access

to the directory, or it denies

write access

to the files within the directory.

---

#### public static
HttpResponse.BodyHandler
<
InputStream
> ofInputStream()

Returns a

BodyHandler<InputStream>

that returns a

BodySubscriber

<InputStream>

obtained from

BodySubscribers.ofInputStream

.

When the

HttpResponse

object is returned, the response
headers will have been completely read, but the body may not have
been fully received yet. The

HttpResponse.body()

method returns an

InputStream

from which the body can be read as it is received.

**Returns:**
- a response body handler

**API Note:**
- See

HttpResponse.BodySubscribers.ofInputStream()

for more
information.

---

#### public static
HttpResponse.BodyHandler
<
Stream
<
String
>> ofLines()

Returns a

BodyHandler<Stream<String>>

that returns a

BodySubscriber

<Stream<String>>

obtained
from

BodySubscribers.ofLines(charset)

.
The

charset

used to decode the response body bytes is
obtained from the HTTP response headers as specified by

ofString()

,
and lines are delimited in the manner of

BufferedReader.readLine()

.

When the

HttpResponse

object is returned, the body may
not have been completely received.

**Returns:**
- a response body handler

---

#### public static
HttpResponse.BodyHandler
<
Void
> ofByteArrayConsumer​(
Consumer
<
Optional
<byte[]>> consumer)

Returns a

BodyHandler<Void>

that returns a

BodySubscriber

<Void>

obtained from

BodySubscribers.ofByteArrayConsumer(Consumer)

.

When the

HttpResponse

object is returned, the body has
been completely written to the consumer.

**Parameters:**
- consumer

- a Consumer to accept the response body

**Returns:**
- a response body handler

**API Note:**
- The subscriber returned by this handler is not flow controlled.
Therefore, the supplied consumer must be able to process whatever
amount of data is delivered in a timely fashion.

---

#### public static
HttpResponse.BodyHandler
<byte[]> ofByteArray()

Returns a

BodyHandler<byte[]>

that returns a

BodySubscriber

<

byte[]

> obtained
from

BodySubscribers.ofByteArray()

.

When the

HttpResponse

object is returned, the body has
been completely written to the byte array.

**Returns:**
- a response body handler

---

#### public static
HttpResponse.BodyHandler
<
String
> ofString()

Returns a

BodyHandler<String>

that returns a

BodySubscriber

<String>

obtained from

BodySubscribers.ofString(Charset)

.
The body is decoded using the character set specified in
the

Content-Type

response header. If there is no such
header, or the character set is not supported, then

UTF_8

is used.

When the

HttpResponse

object is returned, the body has
been completely written to the string.

**Returns:**
- a response body handler

---

#### public static
HttpResponse.BodyHandler
<
Flow.Publisher
<
List
<
ByteBuffer
>>> ofPublisher()

Returns a

BodyHandler<Publisher<List<ByteBuffer>>>

that creates a

BodySubscriber

<Publisher<List<ByteBuffer>>>

obtained from

BodySubscribers.ofPublisher()

.

When the

HttpResponse

object is returned, the response
headers will have been completely read, but the body may not have
been fully received yet. The

HttpResponse.body()

method returns a

Publisher

>

from which the body
response bytes can be obtained as they are received. The publisher
can and must be subscribed to only once.

**Returns:**
- a response body handler

**API Note:**
- See

HttpResponse.BodySubscribers.ofPublisher()

for more
information.

---

#### public static <T>
HttpResponse.BodyHandler
<T> buffering​(
HttpResponse.BodyHandler
<T> downstreamHandler,
int bufferSize)

Returns a

BodyHandler

which, when invoked, returns a

buffering BodySubscriber

that buffers data before delivering it to the downstream subscriber.
These

BodySubscriber

instances are created by calling

BodySubscribers.buffering

with a subscriber obtained from the given
downstream handler and the

bufferSize

parameter.

**Parameters:**
- downstreamHandler

- the downstream handler
- bufferSize

- the buffer size parameter passed to

BodySubscribers.buffering

**Returns:**
- a body handler

**Throws:**
- IllegalArgumentException

- if

bufferSize <= 0

**Type Parameters:**
- T

- the response body type

---

### Additional Sections

#### Class HttpResponse.BodyHandlers

java.lang.Object

- java.net.http.HttpResponse.BodyHandlers

java.net.http.HttpResponse.BodyHandlers

**Enclosing interface:** HttpResponse

<

T

>

```java
public static class
HttpResponse.BodyHandlers

extends
Object
```

Implementations of

BodyHandler

that implement various
useful handlers, such as handling the response body as a String, or
streaming the response body to a file.

These implementations do not examine the status code, meaning the
body is always accepted. They typically return an equivalently named

BodySubscriber

. Alternatively, a custom handler can be used to
examine the status code and headers, and return a different body
subscriber, of the same type, as appropriate.

The following are examples of using the predefined body handlers to
convert a flow of response body data into common high-level Java objects:

```java
// Receives the response body as a String
HttpResponse<String> response = client
.send(request, BodyHandlers.ofString());

// Receives the response body as a file
HttpResponse<Path> response = client
.send(request, BodyHandlers.ofFile(Paths.get("example.html")));

// Receives the response body as an InputStream
HttpResponse<InputStream> response = client
.send(request, BodyHandlers.ofInputStream());

// Discards the response body
HttpResponse<Void> response = client
.send(request, BodyHandlers.discarding());
```

**Since:** 11

public static class

HttpResponse.BodyHandlers

extends

Object

Implementations of

BodyHandler

that implement various
useful handlers, such as handling the response body as a String, or
streaming the response body to a file.

These implementations do not examine the status code, meaning the
body is always accepted. They typically return an equivalently named

BodySubscriber

. Alternatively, a custom handler can be used to
examine the status code and headers, and return a different body
subscriber, of the same type, as appropriate.

The following are examples of using the predefined body handlers to
convert a flow of response body data into common high-level Java objects:

```java
// Receives the response body as a String
HttpResponse<String> response = client
.send(request, BodyHandlers.ofString());

// Receives the response body as a file
HttpResponse<Path> response = client
.send(request, BodyHandlers.ofFile(Paths.get("example.html")));

// Receives the response body as an InputStream
HttpResponse<InputStream> response = client
.send(request, BodyHandlers.ofInputStream());

// Discards the response body
HttpResponse<Void> response = client
.send(request, BodyHandlers.discarding());
```

These implementations do not examine the status code, meaning the
body is always accepted. They typically return an equivalently named

BodySubscriber

. Alternatively, a custom handler can be used to
examine the status code and headers, and return a different body
subscriber, of the same type, as appropriate.

The following are examples of using the predefined body handlers to
convert a flow of response body data into common high-level Java objects:

```java
// Receives the response body as a String
HttpResponse<String> response = client
.send(request, BodyHandlers.ofString());

// Receives the response body as a file
HttpResponse<Path> response = client
.send(request, BodyHandlers.ofFile(Paths.get("example.html")));

// Receives the response body as an InputStream
HttpResponse<InputStream> response = client
.send(request, BodyHandlers.ofInputStream());

// Discards the response body
HttpResponse<Void> response = client
.send(request, BodyHandlers.discarding());
```

The following are examples of using the predefined body handlers to
convert a flow of response body data into common high-level Java objects:

```java
// Receives the response body as a String
HttpResponse<String> response = client
.send(request, BodyHandlers.ofString());

// Receives the response body as a file
HttpResponse<Path> response = client
.send(request, BodyHandlers.ofFile(Paths.get("example.html")));

// Receives the response body as an InputStream
HttpResponse<InputStream> response = client
.send(request, BodyHandlers.ofInputStream());

// Discards the response body
HttpResponse<Void> response = client
.send(request, BodyHandlers.discarding());
```

// Receives the response body as a String
HttpResponse<String> response = client
.send(request, BodyHandlers.ofString());

// Receives the response body as a file
HttpResponse<Path> response = client
.send(request, BodyHandlers.ofFile(Paths.get("example.html")));

// Receives the response body as an InputStream
HttpResponse<InputStream> response = client
.send(request, BodyHandlers.ofInputStream());

// Discards the response body
HttpResponse<Void> response = client
.send(request, BodyHandlers.discarding());

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static <T>

HttpResponse.BodyHandler

<T>

buffering

​(

HttpResponse.BodyHandler

<T> downstreamHandler,
int bufferSize)

Returns a

BodyHandler

which, when invoked, returns a

buffering BodySubscriber

that buffers data before delivering it to the downstream subscriber.

static

HttpResponse.BodyHandler

<

Void

>

discarding

()

Returns a response body handler that discards the response body.

static

HttpResponse.BodyHandler

<

Void

>

fromLineSubscriber

​(

Flow.Subscriber

<? super

String

> subscriber)

Returns a response body handler that returns a

BodySubscriber

<Void>

obtained from

BodySubscribers.fromLineSubscriber(subscriber, s -> null, charset, null)

,
with the given

subscriber

.

static <S extends

Flow.Subscriber

<? super

String

>,​T>

HttpResponse.BodyHandler

<T>

fromLineSubscriber

​(S subscriber,

Function

<? super S,​? extends T> finisher,

String

lineSeparator)

Returns a response body handler that returns a

BodySubscriber

<T>

obtained from

BodySubscribers.fromLineSubscriber(subscriber, finisher, charset, lineSeparator)

,
with the given

subscriber

,

finisher

function, and line separator.

static

HttpResponse.BodyHandler

<

Void

>

fromSubscriber

​(

Flow.Subscriber

<? super

List

<

ByteBuffer

>> subscriber)

Returns a response body handler that returns a

BodySubscriber

<Void>

obtained from

HttpResponse.BodySubscribers.fromSubscriber(Subscriber)

, with the given

subscriber

.

static <S extends

Flow.Subscriber

<? super

List

<

ByteBuffer

>>,​T>

HttpResponse.BodyHandler

<T>

fromSubscriber

​(S subscriber,

Function

<? super S,​? extends T> finisher)

Returns a response body handler that returns a

BodySubscriber

<T>

obtained from

HttpResponse.BodySubscribers.fromSubscriber(Subscriber, Function)

, with the
given

subscriber

and

finisher

function.

static

HttpResponse.BodyHandler

<byte[]>

ofByteArray

()

Returns a

BodyHandler<byte[]>

that returns a

BodySubscriber

<

byte[]

> obtained
from

BodySubscribers.ofByteArray()

.

static

HttpResponse.BodyHandler

<

Void

>

ofByteArrayConsumer

​(

Consumer

<

Optional

<byte[]>> consumer)

Returns a

BodyHandler<Void>

that returns a

BodySubscriber

<Void>

obtained from

BodySubscribers.ofByteArrayConsumer(Consumer)

.

static

HttpResponse.BodyHandler

<

Path

>

ofFile

​(

Path

file)

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<Path>

.

static

HttpResponse.BodyHandler

<

Path

>

ofFile

​(

Path

file,

OpenOption

... openOptions)

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<Path>

obtained from

BodySubscribers.ofFile(Path,OpenOption...)

.

static

HttpResponse.BodyHandler

<

Path

>

ofFileDownload

​(

Path

directory,

OpenOption

... openOptions)

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<

Path

>
where the download directory is specified, but the filename is
obtained from the

Content-Disposition

response header.

static

HttpResponse.BodyHandler

<

InputStream

>

ofInputStream

()

Returns a

BodyHandler<InputStream>

that returns a

BodySubscriber

<InputStream>

obtained from

BodySubscribers.ofInputStream

.

static

HttpResponse.BodyHandler

<

Stream

<

String

>>

ofLines

()

Returns a

BodyHandler<Stream<String>>

that returns a

BodySubscriber

<Stream<String>>

obtained
from

BodySubscribers.ofLines(charset)

.

static

HttpResponse.BodyHandler

<

Flow.Publisher

<

List

<

ByteBuffer

>>>

ofPublisher

()

Returns a

BodyHandler<Publisher<List<ByteBuffer>>>

that creates a

BodySubscriber

<Publisher<List<ByteBuffer>>>

obtained from

BodySubscribers.ofPublisher()

.

static

HttpResponse.BodyHandler

<

String

>

ofString

()

Returns a

BodyHandler<String>

that returns a

BodySubscriber

<String>

obtained from

BodySubscribers.ofString(Charset)

.

static

HttpResponse.BodyHandler

<

String

>

ofString

​(

Charset

charset)

Returns a

BodyHandler<String>

that returns a

BodySubscriber

<String>

obtained from

BodySubscribers.ofString(Charset)

.

static <U>

HttpResponse.BodyHandler

<U>

replacing

​(U value)

Returns a response body handler that returns the given replacement
value, after discarding the response body.

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

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static <T>

HttpResponse.BodyHandler

<T>

buffering

​(

HttpResponse.BodyHandler

<T> downstreamHandler,
int bufferSize)

Returns a

BodyHandler

which, when invoked, returns a

buffering BodySubscriber

that buffers data before delivering it to the downstream subscriber.

static

HttpResponse.BodyHandler

<

Void

>

discarding

()

Returns a response body handler that discards the response body.

static

HttpResponse.BodyHandler

<

Void

>

fromLineSubscriber

​(

Flow.Subscriber

<? super

String

> subscriber)

Returns a response body handler that returns a

BodySubscriber

<Void>

obtained from

BodySubscribers.fromLineSubscriber(subscriber, s -> null, charset, null)

,
with the given

subscriber

.

static <S extends

Flow.Subscriber

<? super

String

>,​T>

HttpResponse.BodyHandler

<T>

fromLineSubscriber

​(S subscriber,

Function

<? super S,​? extends T> finisher,

String

lineSeparator)

Returns a response body handler that returns a

BodySubscriber

<T>

obtained from

BodySubscribers.fromLineSubscriber(subscriber, finisher, charset, lineSeparator)

,
with the given

subscriber

,

finisher

function, and line separator.

static

HttpResponse.BodyHandler

<

Void

>

fromSubscriber

​(

Flow.Subscriber

<? super

List

<

ByteBuffer

>> subscriber)

Returns a response body handler that returns a

BodySubscriber

<Void>

obtained from

HttpResponse.BodySubscribers.fromSubscriber(Subscriber)

, with the given

subscriber

.

static <S extends

Flow.Subscriber

<? super

List

<

ByteBuffer

>>,​T>

HttpResponse.BodyHandler

<T>

fromSubscriber

​(S subscriber,

Function

<? super S,​? extends T> finisher)

Returns a response body handler that returns a

BodySubscriber

<T>

obtained from

HttpResponse.BodySubscribers.fromSubscriber(Subscriber, Function)

, with the
given

subscriber

and

finisher

function.

static

HttpResponse.BodyHandler

<byte[]>

ofByteArray

()

Returns a

BodyHandler<byte[]>

that returns a

BodySubscriber

<

byte[]

> obtained
from

BodySubscribers.ofByteArray()

.

static

HttpResponse.BodyHandler

<

Void

>

ofByteArrayConsumer

​(

Consumer

<

Optional

<byte[]>> consumer)

Returns a

BodyHandler<Void>

that returns a

BodySubscriber

<Void>

obtained from

BodySubscribers.ofByteArrayConsumer(Consumer)

.

static

HttpResponse.BodyHandler

<

Path

>

ofFile

​(

Path

file)

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<Path>

.

static

HttpResponse.BodyHandler

<

Path

>

ofFile

​(

Path

file,

OpenOption

... openOptions)

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<Path>

obtained from

BodySubscribers.ofFile(Path,OpenOption...)

.

static

HttpResponse.BodyHandler

<

Path

>

ofFileDownload

​(

Path

directory,

OpenOption

... openOptions)

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<

Path

>
where the download directory is specified, but the filename is
obtained from the

Content-Disposition

response header.

static

HttpResponse.BodyHandler

<

InputStream

>

ofInputStream

()

Returns a

BodyHandler<InputStream>

that returns a

BodySubscriber

<InputStream>

obtained from

BodySubscribers.ofInputStream

.

static

HttpResponse.BodyHandler

<

Stream

<

String

>>

ofLines

()

Returns a

BodyHandler<Stream<String>>

that returns a

BodySubscriber

<Stream<String>>

obtained
from

BodySubscribers.ofLines(charset)

.

static

HttpResponse.BodyHandler

<

Flow.Publisher

<

List

<

ByteBuffer

>>>

ofPublisher

()

Returns a

BodyHandler<Publisher<List<ByteBuffer>>>

that creates a

BodySubscriber

<Publisher<List<ByteBuffer>>>

obtained from

BodySubscribers.ofPublisher()

.

static

HttpResponse.BodyHandler

<

String

>

ofString

()

Returns a

BodyHandler<String>

that returns a

BodySubscriber

<String>

obtained from

BodySubscribers.ofString(Charset)

.

static

HttpResponse.BodyHandler

<

String

>

ofString

​(

Charset

charset)

Returns a

BodyHandler<String>

that returns a

BodySubscriber

<String>

obtained from

BodySubscribers.ofString(Charset)

.

static <U>

HttpResponse.BodyHandler

<U>

replacing

​(U value)

Returns a response body handler that returns the given replacement
value, after discarding the response body.

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

Returns a

BodyHandler

which, when invoked, returns a

buffering BodySubscriber

that buffers data before delivering it to the downstream subscriber.

Returns a response body handler that discards the response body.

Returns a response body handler that returns a

BodySubscriber

<Void>

obtained from

BodySubscribers.fromLineSubscriber(subscriber, s -> null, charset, null)

,
with the given

subscriber

.

Returns a response body handler that returns a

BodySubscriber

<T>

obtained from

BodySubscribers.fromLineSubscriber(subscriber, finisher, charset, lineSeparator)

,
with the given

subscriber

,

finisher

function, and line separator.

Returns a response body handler that returns a

BodySubscriber

<Void>

obtained from

HttpResponse.BodySubscribers.fromSubscriber(Subscriber)

, with the given

subscriber

.

Returns a response body handler that returns a

BodySubscriber

<T>

obtained from

HttpResponse.BodySubscribers.fromSubscriber(Subscriber, Function)

, with the
given

subscriber

and

finisher

function.

Returns a

BodyHandler<byte[]>

that returns a

BodySubscriber

<

byte[]

> obtained
from

BodySubscribers.ofByteArray()

.

Returns a

BodyHandler<Void>

that returns a

BodySubscriber

<Void>

obtained from

BodySubscribers.ofByteArrayConsumer(Consumer)

.

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<Path>

.

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<Path>

obtained from

BodySubscribers.ofFile(Path,OpenOption...)

.

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<

Path

>
where the download directory is specified, but the filename is
obtained from the

Content-Disposition

response header.

Returns a

BodyHandler<InputStream>

that returns a

BodySubscriber

<InputStream>

obtained from

BodySubscribers.ofInputStream

.

Returns a

BodyHandler<Stream<String>>

that returns a

BodySubscriber

<Stream<String>>

obtained
from

BodySubscribers.ofLines(charset)

.

Returns a

BodyHandler<Publisher<List<ByteBuffer>>>

that creates a

BodySubscriber

<Publisher<List<ByteBuffer>>>

obtained from

BodySubscribers.ofPublisher()

.

Returns a

BodyHandler<String>

that returns a

BodySubscriber

<String>

obtained from

BodySubscribers.ofString(Charset)

.

Returns a response body handler that returns the given replacement
value, after discarding the response body.

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

============ METHOD DETAIL ==========

- Method Detail

- fromSubscriber

```java
public static
HttpResponse.BodyHandler
<
Void
> fromSubscriber​(
Flow.Subscriber
<? super
List
<
ByteBuffer
>> subscriber)
```

Returns a response body handler that returns a

BodySubscriber

<Void>

obtained from

HttpResponse.BodySubscribers.fromSubscriber(Subscriber)

, with the given

subscriber

.

The response body is not available through this, or the

HttpResponse

API, but instead all response body is forwarded to the
given

subscriber

, which should make it available, if
appropriate, through some other mechanism, e.g. an entry in a
database, etc.

**API Note:** This method can be used as an adapter between

BodySubscriber

and

Flow.Subscriber

.

For example:

```java
TextSubscriber subscriber = new TextSubscriber();
HttpResponse<Void> response = client.sendAsync(request,
BodyHandlers.fromSubscriber(subscriber)).join();
System.out.println(response.statusCode());
```
**Parameters:** subscriber

- the subscriber
**Returns:** a response body handler

- fromSubscriber

```java
public static <S extends
Flow.Subscriber
<? super
List
<
ByteBuffer
>>,​T>
HttpResponse.BodyHandler
<T> fromSubscriber​(S subscriber,

Function
<? super S,​? extends T> finisher)
```

Returns a response body handler that returns a

BodySubscriber

<T>

obtained from

HttpResponse.BodySubscribers.fromSubscriber(Subscriber, Function)

, with the
given

subscriber

and

finisher

function.

The given

finisher

function is applied after the given
subscriber's

onComplete

has been invoked. The

finisher

function is invoked with the given subscriber, and returns a value
that is set as the response's body.

**API Note:** This method can be used as an adapter between

BodySubscriber

and

Flow.Subscriber

.

For example:

```java
TextSubscriber subscriber = ...; // accumulates bytes and transforms them into a String
HttpResponse<String> response = client.sendAsync(request,
BodyHandlers.fromSubscriber(subscriber, TextSubscriber::getTextResult)).join();
String text = response.body();
```
**Type Parameters:** S

- the type of the Subscriber
**Type Parameters:** T

- the type of the response body
**Parameters:** subscriber

- the subscriber
**Parameters:** finisher

- a function to be applied after the subscriber has completed
**Returns:** a response body handler

- fromLineSubscriber

```java
public static
HttpResponse.BodyHandler
<
Void
> fromLineSubscriber​(
Flow.Subscriber
<? super
String
> subscriber)
```

Returns a response body handler that returns a

BodySubscriber

<Void>

obtained from

BodySubscribers.fromLineSubscriber(subscriber, s -> null, charset, null)

,
with the given

subscriber

.
The

charset

used to decode the response body bytes is
obtained from the HTTP response headers as specified by

ofString()

,
and lines are delimited in the manner of

BufferedReader.readLine()

.

The response body is not available through this, or the

HttpResponse

API, but instead all response body is forwarded to the
given

subscriber

, which should make it available, if
appropriate, through some other mechanism, e.g. an entry in a
database, etc.

**API Note:** This method can be used as an adapter between a

BodySubscriber

and a text based

Flow.Subscriber

that parses
text line by line.

For example:

```java
// A PrintSubscriber that implements Flow.Subscriber<String>
// and print lines received by onNext() on System.out
PrintSubscriber subscriber = new PrintSubscriber(System.out);
client.sendAsync(request, BodyHandlers.fromLineSubscriber(subscriber))
.thenApply(HttpResponse::statusCode)
.thenAccept((status) -> {
if (status != 200) {
System.err.printf("ERROR: %d status received%n", status);
}
});
```
**Parameters:** subscriber

- the subscriber
**Returns:** a response body handler

- fromLineSubscriber

```java
public static <S extends
Flow.Subscriber
<? super
String
>,​T>
HttpResponse.BodyHandler
<T> fromLineSubscriber​(S subscriber,

Function
<? super S,​? extends T> finisher,

String
lineSeparator)
```

Returns a response body handler that returns a

BodySubscriber

<T>

obtained from

BodySubscribers.fromLineSubscriber(subscriber, finisher, charset, lineSeparator)

,
with the given

subscriber

,

finisher

function, and line separator.
The

charset

used to decode the response body bytes is
obtained from the HTTP response headers as specified by

ofString()

.

The given

finisher

function is applied after the given
subscriber's

onComplete

has been invoked. The

finisher

function is invoked with the given subscriber, and returns a value
that is set as the response's body.

**API Note:** This method can be used as an adapter between a

BodySubscriber

and a text based

Flow.Subscriber

that parses
text line by line.

For example:

```java
// A LineParserSubscriber that implements Flow.Subscriber<String>
// and accumulates lines that match a particular pattern
Pattern pattern = ...;
LineParserSubscriber subscriber = new LineParserSubscriber(pattern);
HttpResponse<List<String>> response = client.send(request,
BodyHandlers.fromLineSubscriber(subscriber, s -> s.getMatchingLines(), "\n"));
if (response.statusCode() != 200) {
System.err.printf("ERROR: %d status received%n", response.statusCode());
}
```
**Type Parameters:** S

- the type of the Subscriber
**Type Parameters:** T

- the type of the response body
**Parameters:** subscriber

- the subscriber
**Parameters:** finisher

- a function to be applied after the subscriber has completed
**Parameters:** lineSeparator

- an optional line separator: can be

null

,
in which case lines will be delimited in the manner of

BufferedReader.readLine()

.
**Returns:** a response body handler
**Throws:** IllegalArgumentException

- if the supplied

lineSeparator

is the empty string

- discarding

```java
public static
HttpResponse.BodyHandler
<
Void
> discarding()
```

Returns a response body handler that discards the response body.

**Returns:** a response body handler

- replacing

```java
public static <U>
HttpResponse.BodyHandler
<U> replacing​(U value)
```

Returns a response body handler that returns the given replacement
value, after discarding the response body.

**Type Parameters:** U

- the response body type
**Parameters:** value

- the value of U to return as the body, may be

null
**Returns:** a response body handler

- ofString

```java
public static
HttpResponse.BodyHandler
<
String
> ofString​(
Charset
charset)
```

Returns a

BodyHandler<String>

that returns a

BodySubscriber

<String>

obtained from

BodySubscribers.ofString(Charset)

.
The body is decoded using the given character set.

**Parameters:** charset

- the character set to convert the body with
**Returns:** a response body handler

- ofFile

```java
public static
HttpResponse.BodyHandler
<
Path
> ofFile​(
Path
file,

OpenOption
... openOptions)
```

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<Path>

obtained from

BodySubscribers.ofFile(Path,OpenOption...)

.

When the

HttpResponse

object is returned, the body has
been completely written to the file, and

HttpResponse.body()

returns a
reference to its

Path

.

Security manager permission checks are performed in this factory
method, when the

BodyHandler

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

**Parameters:** file

- the file to store the body in
**Parameters:** openOptions

- any options to use when opening/creating the file
**Returns:** a response body handler
**Throws:** IllegalArgumentException

- if an invalid set of open options
are specified
**Throws:** SecurityException

- If a security manager has been installed
and it denies

write access

to the file.

- ofFile

```java
public static
HttpResponse.BodyHandler
<
Path
> ofFile​(
Path
file)
```

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<Path>

.

Equivalent to:

ofFile(file, CREATE, WRITE)

Security manager permission checks are performed in this factory
method, when the

BodyHandler

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

**Parameters:** file

- the file to store the body in
**Returns:** a response body handler
**Throws:** SecurityException

- If a security manager has been installed
and it denies

write access

to the file.

- ofFileDownload

```java
public static
HttpResponse.BodyHandler
<
Path
> ofFileDownload​(
Path
directory,

OpenOption
... openOptions)
```

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<

Path

>
where the download directory is specified, but the filename is
obtained from the

Content-Disposition

response header. The

Content-Disposition

header must specify the

attachment

type and must also contain a

filename

parameter. If the
filename specifies multiple path components only the final component
is used as the filename (with the given directory name).

When the

HttpResponse

object is returned, the body has
been completely written to the file and

HttpResponse.body()

returns a

Path

object for the file. The returned

Path

is the
combination of the supplied directory name and the file name supplied
by the server. If the destination directory does not exist or cannot
be written to, then the response will fail with an

IOException

.

Security manager permission checks are performed in this factory
method, when the

BodyHandler

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

**Parameters:** directory

- the directory to store the file in
**Parameters:** openOptions

- open options used when opening the file
**Returns:** a response body handler
**Throws:** IllegalArgumentException

- if the given path does not exist,
is not a directory, is not writable, or if an invalid set
of open options are specified
**Throws:** SecurityException

- If a security manager has been installed
and it denies

read access

to the directory, or it denies

write access

to the directory, or it denies

write access

to the files within the directory.

- ofInputStream

```java
public static
HttpResponse.BodyHandler
<
InputStream
> ofInputStream()
```

Returns a

BodyHandler<InputStream>

that returns a

BodySubscriber

<InputStream>

obtained from

BodySubscribers.ofInputStream

.

When the

HttpResponse

object is returned, the response
headers will have been completely read, but the body may not have
been fully received yet. The

HttpResponse.body()

method returns an

InputStream

from which the body can be read as it is received.

**API Note:** See

HttpResponse.BodySubscribers.ofInputStream()

for more
information.
**Returns:** a response body handler

- ofLines

```java
public static
HttpResponse.BodyHandler
<
Stream
<
String
>> ofLines()
```

Returns a

BodyHandler<Stream<String>>

that returns a

BodySubscriber

<Stream<String>>

obtained
from

BodySubscribers.ofLines(charset)

.
The

charset

used to decode the response body bytes is
obtained from the HTTP response headers as specified by

ofString()

,
and lines are delimited in the manner of

BufferedReader.readLine()

.

When the

HttpResponse

object is returned, the body may
not have been completely received.

**Returns:** a response body handler

- ofByteArrayConsumer

```java
public static
HttpResponse.BodyHandler
<
Void
> ofByteArrayConsumer​(
Consumer
<
Optional
<byte[]>> consumer)
```

Returns a

BodyHandler<Void>

that returns a

BodySubscriber

<Void>

obtained from

BodySubscribers.ofByteArrayConsumer(Consumer)

.

When the

HttpResponse

object is returned, the body has
been completely written to the consumer.

**API Note:** The subscriber returned by this handler is not flow controlled.
Therefore, the supplied consumer must be able to process whatever
amount of data is delivered in a timely fashion.
**Parameters:** consumer

- a Consumer to accept the response body
**Returns:** a response body handler

- ofByteArray

```java
public static
HttpResponse.BodyHandler
<byte[]> ofByteArray()
```

Returns a

BodyHandler<byte[]>

that returns a

BodySubscriber

<

byte[]

> obtained
from

BodySubscribers.ofByteArray()

.

When the

HttpResponse

object is returned, the body has
been completely written to the byte array.

**Returns:** a response body handler

- ofString

```java
public static
HttpResponse.BodyHandler
<
String
> ofString()
```

Returns a

BodyHandler<String>

that returns a

BodySubscriber

<String>

obtained from

BodySubscribers.ofString(Charset)

.
The body is decoded using the character set specified in
the

Content-Type

response header. If there is no such
header, or the character set is not supported, then

UTF_8

is used.

When the

HttpResponse

object is returned, the body has
been completely written to the string.

**Returns:** a response body handler

- ofPublisher

```java
public static
HttpResponse.BodyHandler
<
Flow.Publisher
<
List
<
ByteBuffer
>>> ofPublisher()
```

Returns a

BodyHandler<Publisher<List<ByteBuffer>>>

that creates a

BodySubscriber

<Publisher<List<ByteBuffer>>>

obtained from

BodySubscribers.ofPublisher()

.

When the

HttpResponse

object is returned, the response
headers will have been completely read, but the body may not have
been fully received yet. The

HttpResponse.body()

method returns a

Publisher

>

from which the body
response bytes can be obtained as they are received. The publisher
can and must be subscribed to only once.

**API Note:** See

HttpResponse.BodySubscribers.ofPublisher()

for more
information.
**Returns:** a response body handler

- buffering

```java
public static <T>
HttpResponse.BodyHandler
<T> buffering​(
HttpResponse.BodyHandler
<T> downstreamHandler,
int bufferSize)
```

Returns a

BodyHandler

which, when invoked, returns a

buffering BodySubscriber

that buffers data before delivering it to the downstream subscriber.
These

BodySubscriber

instances are created by calling

BodySubscribers.buffering

with a subscriber obtained from the given
downstream handler and the

bufferSize

parameter.

**Type Parameters:** T

- the response body type
**Parameters:** downstreamHandler

- the downstream handler
**Parameters:** bufferSize

- the buffer size parameter passed to

BodySubscribers.buffering
**Returns:** a body handler
**Throws:** IllegalArgumentException

- if

bufferSize <= 0

Method Detail

- fromSubscriber

```java
public static
HttpResponse.BodyHandler
<
Void
> fromSubscriber​(
Flow.Subscriber
<? super
List
<
ByteBuffer
>> subscriber)
```

Returns a response body handler that returns a

BodySubscriber

<Void>

obtained from

HttpResponse.BodySubscribers.fromSubscriber(Subscriber)

, with the given

subscriber

.

The response body is not available through this, or the

HttpResponse

API, but instead all response body is forwarded to the
given

subscriber

, which should make it available, if
appropriate, through some other mechanism, e.g. an entry in a
database, etc.

**API Note:** This method can be used as an adapter between

BodySubscriber

and

Flow.Subscriber

.

For example:

```java
TextSubscriber subscriber = new TextSubscriber();
HttpResponse<Void> response = client.sendAsync(request,
BodyHandlers.fromSubscriber(subscriber)).join();
System.out.println(response.statusCode());
```
**Parameters:** subscriber

- the subscriber
**Returns:** a response body handler

- fromSubscriber

```java
public static <S extends
Flow.Subscriber
<? super
List
<
ByteBuffer
>>,​T>
HttpResponse.BodyHandler
<T> fromSubscriber​(S subscriber,

Function
<? super S,​? extends T> finisher)
```

Returns a response body handler that returns a

BodySubscriber

<T>

obtained from

HttpResponse.BodySubscribers.fromSubscriber(Subscriber, Function)

, with the
given

subscriber

and

finisher

function.

The given

finisher

function is applied after the given
subscriber's

onComplete

has been invoked. The

finisher

function is invoked with the given subscriber, and returns a value
that is set as the response's body.

**API Note:** This method can be used as an adapter between

BodySubscriber

and

Flow.Subscriber

.

For example:

```java
TextSubscriber subscriber = ...; // accumulates bytes and transforms them into a String
HttpResponse<String> response = client.sendAsync(request,
BodyHandlers.fromSubscriber(subscriber, TextSubscriber::getTextResult)).join();
String text = response.body();
```
**Type Parameters:** S

- the type of the Subscriber
**Type Parameters:** T

- the type of the response body
**Parameters:** subscriber

- the subscriber
**Parameters:** finisher

- a function to be applied after the subscriber has completed
**Returns:** a response body handler

- fromLineSubscriber

```java
public static
HttpResponse.BodyHandler
<
Void
> fromLineSubscriber​(
Flow.Subscriber
<? super
String
> subscriber)
```

Returns a response body handler that returns a

BodySubscriber

<Void>

obtained from

BodySubscribers.fromLineSubscriber(subscriber, s -> null, charset, null)

,
with the given

subscriber

.
The

charset

used to decode the response body bytes is
obtained from the HTTP response headers as specified by

ofString()

,
and lines are delimited in the manner of

BufferedReader.readLine()

.

The response body is not available through this, or the

HttpResponse

API, but instead all response body is forwarded to the
given

subscriber

, which should make it available, if
appropriate, through some other mechanism, e.g. an entry in a
database, etc.

**API Note:** This method can be used as an adapter between a

BodySubscriber

and a text based

Flow.Subscriber

that parses
text line by line.

For example:

```java
// A PrintSubscriber that implements Flow.Subscriber<String>
// and print lines received by onNext() on System.out
PrintSubscriber subscriber = new PrintSubscriber(System.out);
client.sendAsync(request, BodyHandlers.fromLineSubscriber(subscriber))
.thenApply(HttpResponse::statusCode)
.thenAccept((status) -> {
if (status != 200) {
System.err.printf("ERROR: %d status received%n", status);
}
});
```
**Parameters:** subscriber

- the subscriber
**Returns:** a response body handler

- fromLineSubscriber

```java
public static <S extends
Flow.Subscriber
<? super
String
>,​T>
HttpResponse.BodyHandler
<T> fromLineSubscriber​(S subscriber,

Function
<? super S,​? extends T> finisher,

String
lineSeparator)
```

Returns a response body handler that returns a

BodySubscriber

<T>

obtained from

BodySubscribers.fromLineSubscriber(subscriber, finisher, charset, lineSeparator)

,
with the given

subscriber

,

finisher

function, and line separator.
The

charset

used to decode the response body bytes is
obtained from the HTTP response headers as specified by

ofString()

.

The given

finisher

function is applied after the given
subscriber's

onComplete

has been invoked. The

finisher

function is invoked with the given subscriber, and returns a value
that is set as the response's body.

**API Note:** This method can be used as an adapter between a

BodySubscriber

and a text based

Flow.Subscriber

that parses
text line by line.

For example:

```java
// A LineParserSubscriber that implements Flow.Subscriber<String>
// and accumulates lines that match a particular pattern
Pattern pattern = ...;
LineParserSubscriber subscriber = new LineParserSubscriber(pattern);
HttpResponse<List<String>> response = client.send(request,
BodyHandlers.fromLineSubscriber(subscriber, s -> s.getMatchingLines(), "\n"));
if (response.statusCode() != 200) {
System.err.printf("ERROR: %d status received%n", response.statusCode());
}
```
**Type Parameters:** S

- the type of the Subscriber
**Type Parameters:** T

- the type of the response body
**Parameters:** subscriber

- the subscriber
**Parameters:** finisher

- a function to be applied after the subscriber has completed
**Parameters:** lineSeparator

- an optional line separator: can be

null

,
in which case lines will be delimited in the manner of

BufferedReader.readLine()

.
**Returns:** a response body handler
**Throws:** IllegalArgumentException

- if the supplied

lineSeparator

is the empty string

- discarding

```java
public static
HttpResponse.BodyHandler
<
Void
> discarding()
```

Returns a response body handler that discards the response body.

**Returns:** a response body handler

- replacing

```java
public static <U>
HttpResponse.BodyHandler
<U> replacing​(U value)
```

Returns a response body handler that returns the given replacement
value, after discarding the response body.

**Type Parameters:** U

- the response body type
**Parameters:** value

- the value of U to return as the body, may be

null
**Returns:** a response body handler

- ofString

```java
public static
HttpResponse.BodyHandler
<
String
> ofString​(
Charset
charset)
```

Returns a

BodyHandler<String>

that returns a

BodySubscriber

<String>

obtained from

BodySubscribers.ofString(Charset)

.
The body is decoded using the given character set.

**Parameters:** charset

- the character set to convert the body with
**Returns:** a response body handler

- ofFile

```java
public static
HttpResponse.BodyHandler
<
Path
> ofFile​(
Path
file,

OpenOption
... openOptions)
```

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<Path>

obtained from

BodySubscribers.ofFile(Path,OpenOption...)

.

When the

HttpResponse

object is returned, the body has
been completely written to the file, and

HttpResponse.body()

returns a
reference to its

Path

.

Security manager permission checks are performed in this factory
method, when the

BodyHandler

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

**Parameters:** file

- the file to store the body in
**Parameters:** openOptions

- any options to use when opening/creating the file
**Returns:** a response body handler
**Throws:** IllegalArgumentException

- if an invalid set of open options
are specified
**Throws:** SecurityException

- If a security manager has been installed
and it denies

write access

to the file.

- ofFile

```java
public static
HttpResponse.BodyHandler
<
Path
> ofFile​(
Path
file)
```

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<Path>

.

Equivalent to:

ofFile(file, CREATE, WRITE)

Security manager permission checks are performed in this factory
method, when the

BodyHandler

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

**Parameters:** file

- the file to store the body in
**Returns:** a response body handler
**Throws:** SecurityException

- If a security manager has been installed
and it denies

write access

to the file.

- ofFileDownload

```java
public static
HttpResponse.BodyHandler
<
Path
> ofFileDownload​(
Path
directory,

OpenOption
... openOptions)
```

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<

Path

>
where the download directory is specified, but the filename is
obtained from the

Content-Disposition

response header. The

Content-Disposition

header must specify the

attachment

type and must also contain a

filename

parameter. If the
filename specifies multiple path components only the final component
is used as the filename (with the given directory name).

When the

HttpResponse

object is returned, the body has
been completely written to the file and

HttpResponse.body()

returns a

Path

object for the file. The returned

Path

is the
combination of the supplied directory name and the file name supplied
by the server. If the destination directory does not exist or cannot
be written to, then the response will fail with an

IOException

.

Security manager permission checks are performed in this factory
method, when the

BodyHandler

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

**Parameters:** directory

- the directory to store the file in
**Parameters:** openOptions

- open options used when opening the file
**Returns:** a response body handler
**Throws:** IllegalArgumentException

- if the given path does not exist,
is not a directory, is not writable, or if an invalid set
of open options are specified
**Throws:** SecurityException

- If a security manager has been installed
and it denies

read access

to the directory, or it denies

write access

to the directory, or it denies

write access

to the files within the directory.

- ofInputStream

```java
public static
HttpResponse.BodyHandler
<
InputStream
> ofInputStream()
```

Returns a

BodyHandler<InputStream>

that returns a

BodySubscriber

<InputStream>

obtained from

BodySubscribers.ofInputStream

.

When the

HttpResponse

object is returned, the response
headers will have been completely read, but the body may not have
been fully received yet. The

HttpResponse.body()

method returns an

InputStream

from which the body can be read as it is received.

**API Note:** See

HttpResponse.BodySubscribers.ofInputStream()

for more
information.
**Returns:** a response body handler

- ofLines

```java
public static
HttpResponse.BodyHandler
<
Stream
<
String
>> ofLines()
```

Returns a

BodyHandler<Stream<String>>

that returns a

BodySubscriber

<Stream<String>>

obtained
from

BodySubscribers.ofLines(charset)

.
The

charset

used to decode the response body bytes is
obtained from the HTTP response headers as specified by

ofString()

,
and lines are delimited in the manner of

BufferedReader.readLine()

.

When the

HttpResponse

object is returned, the body may
not have been completely received.

**Returns:** a response body handler

- ofByteArrayConsumer

```java
public static
HttpResponse.BodyHandler
<
Void
> ofByteArrayConsumer​(
Consumer
<
Optional
<byte[]>> consumer)
```

Returns a

BodyHandler<Void>

that returns a

BodySubscriber

<Void>

obtained from

BodySubscribers.ofByteArrayConsumer(Consumer)

.

When the

HttpResponse

object is returned, the body has
been completely written to the consumer.

**API Note:** The subscriber returned by this handler is not flow controlled.
Therefore, the supplied consumer must be able to process whatever
amount of data is delivered in a timely fashion.
**Parameters:** consumer

- a Consumer to accept the response body
**Returns:** a response body handler

- ofByteArray

```java
public static
HttpResponse.BodyHandler
<byte[]> ofByteArray()
```

Returns a

BodyHandler<byte[]>

that returns a

BodySubscriber

<

byte[]

> obtained
from

BodySubscribers.ofByteArray()

.

When the

HttpResponse

object is returned, the body has
been completely written to the byte array.

**Returns:** a response body handler

- ofString

```java
public static
HttpResponse.BodyHandler
<
String
> ofString()
```

Returns a

BodyHandler<String>

that returns a

BodySubscriber

<String>

obtained from

BodySubscribers.ofString(Charset)

.
The body is decoded using the character set specified in
the

Content-Type

response header. If there is no such
header, or the character set is not supported, then

UTF_8

is used.

When the

HttpResponse

object is returned, the body has
been completely written to the string.

**Returns:** a response body handler

- ofPublisher

```java
public static
HttpResponse.BodyHandler
<
Flow.Publisher
<
List
<
ByteBuffer
>>> ofPublisher()
```

Returns a

BodyHandler<Publisher<List<ByteBuffer>>>

that creates a

BodySubscriber

<Publisher<List<ByteBuffer>>>

obtained from

BodySubscribers.ofPublisher()

.

When the

HttpResponse

object is returned, the response
headers will have been completely read, but the body may not have
been fully received yet. The

HttpResponse.body()

method returns a

Publisher

>

from which the body
response bytes can be obtained as they are received. The publisher
can and must be subscribed to only once.

**API Note:** See

HttpResponse.BodySubscribers.ofPublisher()

for more
information.
**Returns:** a response body handler

- buffering

```java
public static <T>
HttpResponse.BodyHandler
<T> buffering​(
HttpResponse.BodyHandler
<T> downstreamHandler,
int bufferSize)
```

Returns a

BodyHandler

which, when invoked, returns a

buffering BodySubscriber

that buffers data before delivering it to the downstream subscriber.
These

BodySubscriber

instances are created by calling

BodySubscribers.buffering

with a subscriber obtained from the given
downstream handler and the

bufferSize

parameter.

**Type Parameters:** T

- the response body type
**Parameters:** downstreamHandler

- the downstream handler
**Parameters:** bufferSize

- the buffer size parameter passed to

BodySubscribers.buffering
**Returns:** a body handler
**Throws:** IllegalArgumentException

- if

bufferSize <= 0

---

#### Method Detail

fromSubscriber

```java
public static
HttpResponse.BodyHandler
<
Void
> fromSubscriber​(
Flow.Subscriber
<? super
List
<
ByteBuffer
>> subscriber)
```

Returns a response body handler that returns a

BodySubscriber

<Void>

obtained from

HttpResponse.BodySubscribers.fromSubscriber(Subscriber)

, with the given

subscriber

.

The response body is not available through this, or the

HttpResponse

API, but instead all response body is forwarded to the
given

subscriber

, which should make it available, if
appropriate, through some other mechanism, e.g. an entry in a
database, etc.

**API Note:** This method can be used as an adapter between

BodySubscriber

and

Flow.Subscriber

.

For example:

```java
TextSubscriber subscriber = new TextSubscriber();
HttpResponse<Void> response = client.sendAsync(request,
BodyHandlers.fromSubscriber(subscriber)).join();
System.out.println(response.statusCode());
```
**Parameters:** subscriber

- the subscriber
**Returns:** a response body handler

---

#### fromSubscriber

public static

HttpResponse.BodyHandler

<

Void

> fromSubscriber​(

Flow.Subscriber

<? super

List

<

ByteBuffer

>> subscriber)

Returns a response body handler that returns a

BodySubscriber

<Void>

obtained from

HttpResponse.BodySubscribers.fromSubscriber(Subscriber)

, with the given

subscriber

.

The response body is not available through this, or the

HttpResponse

API, but instead all response body is forwarded to the
given

subscriber

, which should make it available, if
appropriate, through some other mechanism, e.g. an entry in a
database, etc.

The response body is not available through this, or the

HttpResponse

API, but instead all response body is forwarded to the
given

subscriber

, which should make it available, if
appropriate, through some other mechanism, e.g. an entry in a
database, etc.

For example:

```java
TextSubscriber subscriber = new TextSubscriber();
HttpResponse<Void> response = client.sendAsync(request,
BodyHandlers.fromSubscriber(subscriber)).join();
System.out.println(response.statusCode());
```

TextSubscriber subscriber = new TextSubscriber();
HttpResponse<Void> response = client.sendAsync(request,
BodyHandlers.fromSubscriber(subscriber)).join();
System.out.println(response.statusCode());

fromSubscriber

```java
public static <S extends
Flow.Subscriber
<? super
List
<
ByteBuffer
>>,​T>
HttpResponse.BodyHandler
<T> fromSubscriber​(S subscriber,

Function
<? super S,​? extends T> finisher)
```

Returns a response body handler that returns a

BodySubscriber

<T>

obtained from

HttpResponse.BodySubscribers.fromSubscriber(Subscriber, Function)

, with the
given

subscriber

and

finisher

function.

The given

finisher

function is applied after the given
subscriber's

onComplete

has been invoked. The

finisher

function is invoked with the given subscriber, and returns a value
that is set as the response's body.

**API Note:** This method can be used as an adapter between

BodySubscriber

and

Flow.Subscriber

.

For example:

```java
TextSubscriber subscriber = ...; // accumulates bytes and transforms them into a String
HttpResponse<String> response = client.sendAsync(request,
BodyHandlers.fromSubscriber(subscriber, TextSubscriber::getTextResult)).join();
String text = response.body();
```
**Type Parameters:** S

- the type of the Subscriber
**Type Parameters:** T

- the type of the response body
**Parameters:** subscriber

- the subscriber
**Parameters:** finisher

- a function to be applied after the subscriber has completed
**Returns:** a response body handler

---

#### fromSubscriber

public static <S extends

Flow.Subscriber

<? super

List

<

ByteBuffer

>>,​T>

HttpResponse.BodyHandler

<T> fromSubscriber​(S subscriber,

Function

<? super S,​? extends T> finisher)

Returns a response body handler that returns a

BodySubscriber

<T>

obtained from

HttpResponse.BodySubscribers.fromSubscriber(Subscriber, Function)

, with the
given

subscriber

and

finisher

function.

The given

finisher

function is applied after the given
subscriber's

onComplete

has been invoked. The

finisher

function is invoked with the given subscriber, and returns a value
that is set as the response's body.

The given

finisher

function is applied after the given
subscriber's

onComplete

has been invoked. The

finisher

function is invoked with the given subscriber, and returns a value
that is set as the response's body.

For example:

```java
TextSubscriber subscriber = ...; // accumulates bytes and transforms them into a String
HttpResponse<String> response = client.sendAsync(request,
BodyHandlers.fromSubscriber(subscriber, TextSubscriber::getTextResult)).join();
String text = response.body();
```

TextSubscriber subscriber = ...; // accumulates bytes and transforms them into a String
HttpResponse<String> response = client.sendAsync(request,
BodyHandlers.fromSubscriber(subscriber, TextSubscriber::getTextResult)).join();
String text = response.body();

fromLineSubscriber

```java
public static
HttpResponse.BodyHandler
<
Void
> fromLineSubscriber​(
Flow.Subscriber
<? super
String
> subscriber)
```

Returns a response body handler that returns a

BodySubscriber

<Void>

obtained from

BodySubscribers.fromLineSubscriber(subscriber, s -> null, charset, null)

,
with the given

subscriber

.
The

charset

used to decode the response body bytes is
obtained from the HTTP response headers as specified by

ofString()

,
and lines are delimited in the manner of

BufferedReader.readLine()

.

The response body is not available through this, or the

HttpResponse

API, but instead all response body is forwarded to the
given

subscriber

, which should make it available, if
appropriate, through some other mechanism, e.g. an entry in a
database, etc.

**API Note:** This method can be used as an adapter between a

BodySubscriber

and a text based

Flow.Subscriber

that parses
text line by line.

For example:

```java
// A PrintSubscriber that implements Flow.Subscriber<String>
// and print lines received by onNext() on System.out
PrintSubscriber subscriber = new PrintSubscriber(System.out);
client.sendAsync(request, BodyHandlers.fromLineSubscriber(subscriber))
.thenApply(HttpResponse::statusCode)
.thenAccept((status) -> {
if (status != 200) {
System.err.printf("ERROR: %d status received%n", status);
}
});
```
**Parameters:** subscriber

- the subscriber
**Returns:** a response body handler

---

#### fromLineSubscriber

public static

HttpResponse.BodyHandler

<

Void

> fromLineSubscriber​(

Flow.Subscriber

<? super

String

> subscriber)

Returns a response body handler that returns a

BodySubscriber

<Void>

obtained from

BodySubscribers.fromLineSubscriber(subscriber, s -> null, charset, null)

,
with the given

subscriber

.
The

charset

used to decode the response body bytes is
obtained from the HTTP response headers as specified by

ofString()

,
and lines are delimited in the manner of

BufferedReader.readLine()

.

The response body is not available through this, or the

HttpResponse

API, but instead all response body is forwarded to the
given

subscriber

, which should make it available, if
appropriate, through some other mechanism, e.g. an entry in a
database, etc.

The response body is not available through this, or the

HttpResponse

API, but instead all response body is forwarded to the
given

subscriber

, which should make it available, if
appropriate, through some other mechanism, e.g. an entry in a
database, etc.

For example:

```java
// A PrintSubscriber that implements Flow.Subscriber<String>
// and print lines received by onNext() on System.out
PrintSubscriber subscriber = new PrintSubscriber(System.out);
client.sendAsync(request, BodyHandlers.fromLineSubscriber(subscriber))
.thenApply(HttpResponse::statusCode)
.thenAccept((status) -> {
if (status != 200) {
System.err.printf("ERROR: %d status received%n", status);
}
});
```

// A PrintSubscriber that implements Flow.Subscriber<String>
// and print lines received by onNext() on System.out
PrintSubscriber subscriber = new PrintSubscriber(System.out);
client.sendAsync(request, BodyHandlers.fromLineSubscriber(subscriber))
.thenApply(HttpResponse::statusCode)
.thenAccept((status) -> {
if (status != 200) {
System.err.printf("ERROR: %d status received%n", status);
}
});

fromLineSubscriber

```java
public static <S extends
Flow.Subscriber
<? super
String
>,​T>
HttpResponse.BodyHandler
<T> fromLineSubscriber​(S subscriber,

Function
<? super S,​? extends T> finisher,

String
lineSeparator)
```

Returns a response body handler that returns a

BodySubscriber

<T>

obtained from

BodySubscribers.fromLineSubscriber(subscriber, finisher, charset, lineSeparator)

,
with the given

subscriber

,

finisher

function, and line separator.
The

charset

used to decode the response body bytes is
obtained from the HTTP response headers as specified by

ofString()

.

The given

finisher

function is applied after the given
subscriber's

onComplete

has been invoked. The

finisher

function is invoked with the given subscriber, and returns a value
that is set as the response's body.

**API Note:** This method can be used as an adapter between a

BodySubscriber

and a text based

Flow.Subscriber

that parses
text line by line.

For example:

```java
// A LineParserSubscriber that implements Flow.Subscriber<String>
// and accumulates lines that match a particular pattern
Pattern pattern = ...;
LineParserSubscriber subscriber = new LineParserSubscriber(pattern);
HttpResponse<List<String>> response = client.send(request,
BodyHandlers.fromLineSubscriber(subscriber, s -> s.getMatchingLines(), "\n"));
if (response.statusCode() != 200) {
System.err.printf("ERROR: %d status received%n", response.statusCode());
}
```
**Type Parameters:** S

- the type of the Subscriber
**Type Parameters:** T

- the type of the response body
**Parameters:** subscriber

- the subscriber
**Parameters:** finisher

- a function to be applied after the subscriber has completed
**Parameters:** lineSeparator

- an optional line separator: can be

null

,
in which case lines will be delimited in the manner of

BufferedReader.readLine()

.
**Returns:** a response body handler
**Throws:** IllegalArgumentException

- if the supplied

lineSeparator

is the empty string

---

#### fromLineSubscriber

public static <S extends

Flow.Subscriber

<? super

String

>,​T>

HttpResponse.BodyHandler

<T> fromLineSubscriber​(S subscriber,

Function

<? super S,​? extends T> finisher,

String

lineSeparator)

Returns a response body handler that returns a

BodySubscriber

<T>

obtained from

BodySubscribers.fromLineSubscriber(subscriber, finisher, charset, lineSeparator)

,
with the given

subscriber

,

finisher

function, and line separator.
The

charset

used to decode the response body bytes is
obtained from the HTTP response headers as specified by

ofString()

.

The given

finisher

function is applied after the given
subscriber's

onComplete

has been invoked. The

finisher

function is invoked with the given subscriber, and returns a value
that is set as the response's body.

The given

finisher

function is applied after the given
subscriber's

onComplete

has been invoked. The

finisher

function is invoked with the given subscriber, and returns a value
that is set as the response's body.

For example:

```java
// A LineParserSubscriber that implements Flow.Subscriber<String>
// and accumulates lines that match a particular pattern
Pattern pattern = ...;
LineParserSubscriber subscriber = new LineParserSubscriber(pattern);
HttpResponse<List<String>> response = client.send(request,
BodyHandlers.fromLineSubscriber(subscriber, s -> s.getMatchingLines(), "\n"));
if (response.statusCode() != 200) {
System.err.printf("ERROR: %d status received%n", response.statusCode());
}
```

// A LineParserSubscriber that implements Flow.Subscriber<String>
// and accumulates lines that match a particular pattern
Pattern pattern = ...;
LineParserSubscriber subscriber = new LineParserSubscriber(pattern);
HttpResponse<List<String>> response = client.send(request,
BodyHandlers.fromLineSubscriber(subscriber, s -> s.getMatchingLines(), "\n"));
if (response.statusCode() != 200) {
System.err.printf("ERROR: %d status received%n", response.statusCode());
}

discarding

```java
public static
HttpResponse.BodyHandler
<
Void
> discarding()
```

Returns a response body handler that discards the response body.

**Returns:** a response body handler

---

#### discarding

public static

HttpResponse.BodyHandler

<

Void

> discarding()

Returns a response body handler that discards the response body.

replacing

```java
public static <U>
HttpResponse.BodyHandler
<U> replacing​(U value)
```

Returns a response body handler that returns the given replacement
value, after discarding the response body.

**Type Parameters:** U

- the response body type
**Parameters:** value

- the value of U to return as the body, may be

null
**Returns:** a response body handler

---

#### replacing

public static <U>

HttpResponse.BodyHandler

<U> replacing​(U value)

Returns a response body handler that returns the given replacement
value, after discarding the response body.

ofString

```java
public static
HttpResponse.BodyHandler
<
String
> ofString​(
Charset
charset)
```

Returns a

BodyHandler<String>

that returns a

BodySubscriber

<String>

obtained from

BodySubscribers.ofString(Charset)

.
The body is decoded using the given character set.

**Parameters:** charset

- the character set to convert the body with
**Returns:** a response body handler

---

#### ofString

public static

HttpResponse.BodyHandler

<

String

> ofString​(

Charset

charset)

Returns a

BodyHandler<String>

that returns a

BodySubscriber

<String>

obtained from

BodySubscribers.ofString(Charset)

.
The body is decoded using the given character set.

ofFile

```java
public static
HttpResponse.BodyHandler
<
Path
> ofFile​(
Path
file,

OpenOption
... openOptions)
```

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<Path>

obtained from

BodySubscribers.ofFile(Path,OpenOption...)

.

When the

HttpResponse

object is returned, the body has
been completely written to the file, and

HttpResponse.body()

returns a
reference to its

Path

.

Security manager permission checks are performed in this factory
method, when the

BodyHandler

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

**Parameters:** file

- the file to store the body in
**Parameters:** openOptions

- any options to use when opening/creating the file
**Returns:** a response body handler
**Throws:** IllegalArgumentException

- if an invalid set of open options
are specified
**Throws:** SecurityException

- If a security manager has been installed
and it denies

write access

to the file.

---

#### ofFile

public static

HttpResponse.BodyHandler

<

Path

> ofFile​(

Path

file,

OpenOption

... openOptions)

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<Path>

obtained from

BodySubscribers.ofFile(Path,OpenOption...)

.

When the

HttpResponse

object is returned, the body has
been completely written to the file, and

HttpResponse.body()

returns a
reference to its

Path

.

Security manager permission checks are performed in this factory
method, when the

BodyHandler

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

When the

HttpResponse

object is returned, the body has
been completely written to the file, and

HttpResponse.body()

returns a
reference to its

Path

.

Security manager permission checks are performed in this factory
method, when the

BodyHandler

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

Security manager permission checks are performed in this factory
method, when the

BodyHandler

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

ofFile

```java
public static
HttpResponse.BodyHandler
<
Path
> ofFile​(
Path
file)
```

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<Path>

.

Equivalent to:

ofFile(file, CREATE, WRITE)

Security manager permission checks are performed in this factory
method, when the

BodyHandler

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

**Parameters:** file

- the file to store the body in
**Returns:** a response body handler
**Throws:** SecurityException

- If a security manager has been installed
and it denies

write access

to the file.

---

#### ofFile

public static

HttpResponse.BodyHandler

<

Path

> ofFile​(

Path

file)

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<Path>

.

Equivalent to:

ofFile(file, CREATE, WRITE)

Security manager permission checks are performed in this factory
method, when the

BodyHandler

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

Equivalent to:

ofFile(file, CREATE, WRITE)

Security manager permission checks are performed in this factory
method, when the

BodyHandler

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

Security manager permission checks are performed in this factory
method, when the

BodyHandler

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

ofFileDownload

```java
public static
HttpResponse.BodyHandler
<
Path
> ofFileDownload​(
Path
directory,

OpenOption
... openOptions)
```

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<

Path

>
where the download directory is specified, but the filename is
obtained from the

Content-Disposition

response header. The

Content-Disposition

header must specify the

attachment

type and must also contain a

filename

parameter. If the
filename specifies multiple path components only the final component
is used as the filename (with the given directory name).

When the

HttpResponse

object is returned, the body has
been completely written to the file and

HttpResponse.body()

returns a

Path

object for the file. The returned

Path

is the
combination of the supplied directory name and the file name supplied
by the server. If the destination directory does not exist or cannot
be written to, then the response will fail with an

IOException

.

Security manager permission checks are performed in this factory
method, when the

BodyHandler

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

**Parameters:** directory

- the directory to store the file in
**Parameters:** openOptions

- open options used when opening the file
**Returns:** a response body handler
**Throws:** IllegalArgumentException

- if the given path does not exist,
is not a directory, is not writable, or if an invalid set
of open options are specified
**Throws:** SecurityException

- If a security manager has been installed
and it denies

read access

to the directory, or it denies

write access

to the directory, or it denies

write access

to the files within the directory.

---

#### ofFileDownload

public static

HttpResponse.BodyHandler

<

Path

> ofFileDownload​(

Path

directory,

OpenOption

... openOptions)

Returns a

BodyHandler<Path>

that returns a

BodySubscriber

<

Path

>
where the download directory is specified, but the filename is
obtained from the

Content-Disposition

response header. The

Content-Disposition

header must specify the

attachment

type and must also contain a

filename

parameter. If the
filename specifies multiple path components only the final component
is used as the filename (with the given directory name).

When the

HttpResponse

object is returned, the body has
been completely written to the file and

HttpResponse.body()

returns a

Path

object for the file. The returned

Path

is the
combination of the supplied directory name and the file name supplied
by the server. If the destination directory does not exist or cannot
be written to, then the response will fail with an

IOException

.

Security manager permission checks are performed in this factory
method, when the

BodyHandler

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

When the

HttpResponse

object is returned, the body has
been completely written to the file and

HttpResponse.body()

returns a

Path

object for the file. The returned

Path

is the
combination of the supplied directory name and the file name supplied
by the server. If the destination directory does not exist or cannot
be written to, then the response will fail with an

IOException

.

Security manager permission checks are performed in this factory
method, when the

BodyHandler

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

Security manager permission checks are performed in this factory
method, when the

BodyHandler

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

ofInputStream

```java
public static
HttpResponse.BodyHandler
<
InputStream
> ofInputStream()
```

Returns a

BodyHandler<InputStream>

that returns a

BodySubscriber

<InputStream>

obtained from

BodySubscribers.ofInputStream

.

When the

HttpResponse

object is returned, the response
headers will have been completely read, but the body may not have
been fully received yet. The

HttpResponse.body()

method returns an

InputStream

from which the body can be read as it is received.

**API Note:** See

HttpResponse.BodySubscribers.ofInputStream()

for more
information.
**Returns:** a response body handler

---

#### ofInputStream

public static

HttpResponse.BodyHandler

<

InputStream

> ofInputStream()

Returns a

BodyHandler<InputStream>

that returns a

BodySubscriber

<InputStream>

obtained from

BodySubscribers.ofInputStream

.

When the

HttpResponse

object is returned, the response
headers will have been completely read, but the body may not have
been fully received yet. The

HttpResponse.body()

method returns an

InputStream

from which the body can be read as it is received.

When the

HttpResponse

object is returned, the response
headers will have been completely read, but the body may not have
been fully received yet. The

HttpResponse.body()

method returns an

InputStream

from which the body can be read as it is received.

ofLines

```java
public static
HttpResponse.BodyHandler
<
Stream
<
String
>> ofLines()
```

Returns a

BodyHandler<Stream<String>>

that returns a

BodySubscriber

<Stream<String>>

obtained
from

BodySubscribers.ofLines(charset)

.
The

charset

used to decode the response body bytes is
obtained from the HTTP response headers as specified by

ofString()

,
and lines are delimited in the manner of

BufferedReader.readLine()

.

When the

HttpResponse

object is returned, the body may
not have been completely received.

**Returns:** a response body handler

---

#### ofLines

public static

HttpResponse.BodyHandler

<

Stream

<

String

>> ofLines()

Returns a

BodyHandler<Stream<String>>

that returns a

BodySubscriber

<Stream<String>>

obtained
from

BodySubscribers.ofLines(charset)

.
The

charset

used to decode the response body bytes is
obtained from the HTTP response headers as specified by

ofString()

,
and lines are delimited in the manner of

BufferedReader.readLine()

.

When the

HttpResponse

object is returned, the body may
not have been completely received.

When the

HttpResponse

object is returned, the body may
not have been completely received.

ofByteArrayConsumer

```java
public static
HttpResponse.BodyHandler
<
Void
> ofByteArrayConsumer​(
Consumer
<
Optional
<byte[]>> consumer)
```

Returns a

BodyHandler<Void>

that returns a

BodySubscriber

<Void>

obtained from

BodySubscribers.ofByteArrayConsumer(Consumer)

.

When the

HttpResponse

object is returned, the body has
been completely written to the consumer.

**API Note:** The subscriber returned by this handler is not flow controlled.
Therefore, the supplied consumer must be able to process whatever
amount of data is delivered in a timely fashion.
**Parameters:** consumer

- a Consumer to accept the response body
**Returns:** a response body handler

---

#### ofByteArrayConsumer

public static

HttpResponse.BodyHandler

<

Void

> ofByteArrayConsumer​(

Consumer

<

Optional

<byte[]>> consumer)

Returns a

BodyHandler<Void>

that returns a

BodySubscriber

<Void>

obtained from

BodySubscribers.ofByteArrayConsumer(Consumer)

.

When the

HttpResponse

object is returned, the body has
been completely written to the consumer.

When the

HttpResponse

object is returned, the body has
been completely written to the consumer.

ofByteArray

```java
public static
HttpResponse.BodyHandler
<byte[]> ofByteArray()
```

Returns a

BodyHandler<byte[]>

that returns a

BodySubscriber

<

byte[]

> obtained
from

BodySubscribers.ofByteArray()

.

When the

HttpResponse

object is returned, the body has
been completely written to the byte array.

**Returns:** a response body handler

---

#### ofByteArray

public static

HttpResponse.BodyHandler

<byte[]> ofByteArray()

Returns a

BodyHandler<byte[]>

that returns a

BodySubscriber

<

byte[]

> obtained
from

BodySubscribers.ofByteArray()

.

When the

HttpResponse

object is returned, the body has
been completely written to the byte array.

When the

HttpResponse

object is returned, the body has
been completely written to the byte array.

ofString

```java
public static
HttpResponse.BodyHandler
<
String
> ofString()
```

Returns a

BodyHandler<String>

that returns a

BodySubscriber

<String>

obtained from

BodySubscribers.ofString(Charset)

.
The body is decoded using the character set specified in
the

Content-Type

response header. If there is no such
header, or the character set is not supported, then

UTF_8

is used.

When the

HttpResponse

object is returned, the body has
been completely written to the string.

**Returns:** a response body handler

---

#### ofString

public static

HttpResponse.BodyHandler

<

String

> ofString()

Returns a

BodyHandler<String>

that returns a

BodySubscriber

<String>

obtained from

BodySubscribers.ofString(Charset)

.
The body is decoded using the character set specified in
the

Content-Type

response header. If there is no such
header, or the character set is not supported, then

UTF_8

is used.

When the

HttpResponse

object is returned, the body has
been completely written to the string.

When the

HttpResponse

object is returned, the body has
been completely written to the string.

ofPublisher

```java
public static
HttpResponse.BodyHandler
<
Flow.Publisher
<
List
<
ByteBuffer
>>> ofPublisher()
```

Returns a

BodyHandler<Publisher<List<ByteBuffer>>>

that creates a

BodySubscriber

<Publisher<List<ByteBuffer>>>

obtained from

BodySubscribers.ofPublisher()

.

When the

HttpResponse

object is returned, the response
headers will have been completely read, but the body may not have
been fully received yet. The

HttpResponse.body()

method returns a

Publisher

>

from which the body
response bytes can be obtained as they are received. The publisher
can and must be subscribed to only once.

**API Note:** See

HttpResponse.BodySubscribers.ofPublisher()

for more
information.
**Returns:** a response body handler

---

#### ofPublisher

public static

HttpResponse.BodyHandler

<

Flow.Publisher

<

List

<

ByteBuffer

>>> ofPublisher()

Returns a

BodyHandler<Publisher<List<ByteBuffer>>>

that creates a

BodySubscriber

<Publisher<List<ByteBuffer>>>

obtained from

BodySubscribers.ofPublisher()

.

When the

HttpResponse

object is returned, the response
headers will have been completely read, but the body may not have
been fully received yet. The

HttpResponse.body()

method returns a

Publisher

>

from which the body
response bytes can be obtained as they are received. The publisher
can and must be subscribed to only once.

When the

HttpResponse

object is returned, the response
headers will have been completely read, but the body may not have
been fully received yet. The

HttpResponse.body()

method returns a

Publisher

>

from which the body
response bytes can be obtained as they are received. The publisher
can and must be subscribed to only once.

buffering

```java
public static <T>
HttpResponse.BodyHandler
<T> buffering​(
HttpResponse.BodyHandler
<T> downstreamHandler,
int bufferSize)
```

Returns a

BodyHandler

which, when invoked, returns a

buffering BodySubscriber

that buffers data before delivering it to the downstream subscriber.
These

BodySubscriber

instances are created by calling

BodySubscribers.buffering

with a subscriber obtained from the given
downstream handler and the

bufferSize

parameter.

**Type Parameters:** T

- the response body type
**Parameters:** downstreamHandler

- the downstream handler
**Parameters:** bufferSize

- the buffer size parameter passed to

BodySubscribers.buffering
**Returns:** a body handler
**Throws:** IllegalArgumentException

- if

bufferSize <= 0

---

#### buffering

public static <T>

HttpResponse.BodyHandler

<T> buffering​(

HttpResponse.BodyHandler

<T> downstreamHandler,
int bufferSize)

Returns a

BodyHandler

which, when invoked, returns a

buffering BodySubscriber

that buffers data before delivering it to the downstream subscriber.
These

BodySubscriber

instances are created by calling

BodySubscribers.buffering

with a subscriber obtained from the given
downstream handler and the

bufferSize

parameter.

---

