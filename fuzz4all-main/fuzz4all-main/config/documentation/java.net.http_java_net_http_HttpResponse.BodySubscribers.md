# Class HttpResponse.BodySubscribers

**Source:** `java.net.http\java\net\http\HttpResponse.BodySubscribers.html`

### Class Description

```java
public static class
HttpResponse.BodySubscribers

extends
Object
```

Implementations of

BodySubscriber

that implement
various useful subscribers, such as converting the response body bytes
into a String, or streaming the bytes to a file.

The following are examples of using the predefined body subscribers
to convert a flow of response body data into common high-level Java
objects:

```java
// Streams the response body to a File
HttpResponse<byte[]> response = client
.send(request, responseInfo -> BodySubscribers.ofByteArray());

// Accumulates the response body and returns it as a byte[]
HttpResponse<byte[]> response = client
.send(request, responseInfo -> BodySubscribers.ofByteArray());

// Discards the response body
HttpResponse<Void> response = client
.send(request, responseInfo -> BodySubscribers.discarding());

// Accumulates the response body as a String then maps it to its bytes
HttpResponse<byte[]> response = client
.send(request, responseInfo ->
BodySubscribers.mapping(BodySubscribers.ofString(UTF_8), String::getBytes));
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
HttpResponse.BodySubscriber
<
Void
> fromSubscriber​(
Flow.Subscriber
<? super
List
<
ByteBuffer
>> subscriber)

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

. The

completion stage

of the returned body subscriber completes after one
of the given subscribers

onComplete

or

onError

has
been invoked.

**Parameters:**
- subscriber

- the subscriber

**Returns:**
- a body subscriber

**API Note:**
- This method can be used as an adapter between

BodySubscriber

and

Flow.Subscriber

.

---

#### public static <S extends
Flow.Subscriber
<? super
List
<
ByteBuffer
>>,​T>
HttpResponse.BodySubscriber
<T> fromSubscriber​(S subscriber,

Function
<? super S,​? extends T> finisher)

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

. The

completion stage

of the returned body subscriber completes after one
of the given subscribers

onComplete

or

onError

has
been invoked.

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

- a function to be applied after the subscriber has
completed

**Returns:**
- a body subscriber

**API Note:**
- This method can be used as an adapter between

BodySubscriber

and

Flow.Subscriber

.

**Type Parameters:**
- S

- the type of the Subscriber
- T

- the type of the response body

---

#### public static
HttpResponse.BodySubscriber
<
Void
> fromLineSubscriber​(
Flow.Subscriber
<? super
String
> subscriber)

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

, line by line.
The

completion
stage

of the returned body subscriber completes after one of the
given subscribers

onComplete

or

onError

has been
invoked.
Bytes are decoded using the

UTF-8

charset, and lines are delimited in the manner of

BufferedReader.readLine()

.

**Parameters:**
- subscriber

- the subscriber

**Returns:**
- a body subscriber

**API Note:**
- This method can be used as an adapter between

BodySubscriber

and

Flow.Subscriber

.

**Implementation Note:**
- This is equivalent to calling

```java
fromLineSubscriber(subscriber, s -> null, StandardCharsets.UTF_8, null)
```

---

#### public static <S extends
Flow.Subscriber
<? super
String
>,​T>
HttpResponse.BodySubscriber
<T> fromLineSubscriber​(S subscriber,

Function
<? super S,​? extends T> finisher,

Charset
charset,

String
lineSeparator)

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

, line by line. The

completion stage

of the returned body
subscriber completes after one of the given subscribers

onComplete

or

onError

has been invoked.

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

- a function to be applied after the subscriber has
completed
- charset

- a

Charset

to decode the bytes
- lineSeparator

- an optional line separator: can be

null

,
in which case lines will be delimited in the manner of

BufferedReader.readLine()

.

**Returns:**
- a body subscriber

**Throws:**
- IllegalArgumentException

- if the supplied

lineSeparator

is the empty string

**API Note:**
- This method can be used as an adapter between

BodySubscriber

and

Flow.Subscriber

.

**Type Parameters:**
- S

- the type of the Subscriber
- T

- the type of the response body

---

#### public static
HttpResponse.BodySubscriber
<
String
> ofString​(
Charset
charset)

Returns a body subscriber which stores the response body as a

String

converted using the given

Charset

.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

**Parameters:**
- charset

- the character set to convert the String with

**Returns:**
- a body subscriber

---

#### public static
HttpResponse.BodySubscriber
<byte[]> ofByteArray()

Returns a

BodySubscriber

which stores the response body as a
byte array.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

**Returns:**
- a body subscriber

---

#### public static
HttpResponse.BodySubscriber
<
Path
> ofFile​(
Path
file,

OpenOption
... openOptions)

Returns a

BodySubscriber

which stores the response body in a
file opened with the given options and name. The file will be opened
with the given options using

FileChannel.open

just before the body is read. Any exception thrown
will be returned or thrown from

HttpClient::send

or

HttpClient::sendAsync

as appropriate.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

Security manager permission checks are performed in this factory
method, when the

BodySubscriber

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

**Parameters:**
- file

- the file to store the body in
- openOptions

- the list of options to open the file with

**Returns:**
- a body subscriber

**Throws:**
- IllegalArgumentException

- if an invalid set of open options
are specified
- SecurityException

- if a security manager has been installed
and it denies

write access

to the file

---

#### public static
HttpResponse.BodySubscriber
<
Path
> ofFile​(
Path
file)

Returns a

BodySubscriber

which stores the response body in a
file opened with the given name.

Equivalent to:

ofFile(file, CREATE, WRITE)

Security manager permission checks are performed in this factory
method, when the

BodySubscriber

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

**Parameters:**
- file

- the file to store the body in

**Returns:**
- a body subscriber

**Throws:**
- SecurityException

- if a security manager has been installed
and it denies

write access

to the file

---

#### public static
HttpResponse.BodySubscriber
<
Void
> ofByteArrayConsumer​(
Consumer
<
Optional
<byte[]>> consumer)

Returns a

BodySubscriber

which provides the incoming body
data to the provided Consumer of

Optional<byte[]>

. Each
call to

Consumer.accept()

will contain a non empty

Optional

, except for the final
invocation after all body data has been read, when the

Optional

will be empty.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

**Parameters:**
- consumer

- a Consumer of byte arrays

**Returns:**
- a BodySubscriber

**API Note:**
- This subscriber is not flow controlled.
Therefore, the supplied consumer must be able to process whatever
amount of data is delivered in a timely fashion.

---

#### public static
HttpResponse.BodySubscriber
<
InputStream
> ofInputStream()

Returns a

BodySubscriber

which streams the response body as
an

InputStream

.

The

HttpResponse

using this subscriber is available
immediately after the response headers have been read, without
requiring to wait for the entire body to be processed. The response
body can then be read directly from the

InputStream

.

**Returns:**
- a body subscriber that streams the response body as an

InputStream

.

**API Note:**
- To ensure that all resources associated with the
corresponding exchange are properly released the caller must
ensure to either read all bytes until EOF is reached, or call

InputStream.close()

if it is unable or unwilling to do so.
Calling

close

before exhausting the stream may cause
the underlying HTTP connection to be closed and prevent it
from being reused for subsequent operations.

---

#### public static
HttpResponse.BodySubscriber
<
Stream
<
String
>> ofLines​(
Charset
charset)

Returns a

BodySubscriber

which streams the response body as
a

Stream

, where each string in the stream
corresponds to a line as defined by

BufferedReader.lines()

.

The

HttpResponse

using this subscriber is available
immediately after the response headers have been read, without
requiring to wait for the entire body to be processed. The response
body can then be read directly from the

Stream

.

**Parameters:**
- charset

- the character set to use when converting bytes to characters

**Returns:**
- a body subscriber that streams the response body as a

Stream

.

**See Also:**
- BufferedReader.lines()

**API Note:**
- To ensure that all resources associated with the
corresponding exchange are properly released the caller must
ensure to either read all lines until the stream is exhausted,
or call

BaseStream.close()

if it is unable or unwilling to do so.
Calling

close

before exhausting the stream may cause
the underlying HTTP connection to be closed and prevent it
from being reused for subsequent operations.

---

#### public static
HttpResponse.BodySubscriber
<
Flow.Publisher
<
List
<
ByteBuffer
>>> ofPublisher()

Returns a response subscriber which publishes the response body
through a

Publisher<List<ByteBuffer>>

.

The

HttpResponse

using this subscriber is available
immediately after the response headers have been read, without
requiring to wait for the entire body to be processed. The response
body bytes can then be obtained by subscribing to the publisher
returned by the

HttpResponse

body

method.

The publisher returned by the

body

method can be subscribed to only once. The first subscriber will
receive the body response bytes if successfully subscribed, or will
cause the subscription to be cancelled otherwise.
If more subscriptions are attempted, the subsequent subscribers will
be immediately subscribed with an empty subscription and their

onError

method
will be invoked with an

IllegalStateException

.

**Returns:**
- A

BodySubscriber

which publishes the response body
through a

Publisher<List<ByteBuffer>>

.

**API Note:**
- To ensure that all resources associated with the
corresponding exchange are properly released the caller must
ensure that the provided publisher is subscribed once, and either

requests

all bytes
until

onComplete

or

onError

are invoked, or
cancel the provided

subscription

if it is unable or unwilling to do so.
Note that depending on the actual HTTP protocol

version

used for the exchange, cancelling the
subscription instead of exhausting the flow may cause the underlying
HTTP connection to be closed and prevent it from being reused for
subsequent operations.

---

#### public static <U>
HttpResponse.BodySubscriber
<U> replacing​(U value)

Returns a response subscriber which discards the response body. The
supplied value is the value that will be returned from

HttpResponse.body()

.

**Parameters:**
- value

- the value to return from HttpResponse.body(), may be

null

**Returns:**
- a

BodySubscriber

**Type Parameters:**
- U

- the type of the response body

---

#### public static
HttpResponse.BodySubscriber
<
Void
> discarding()

Returns a response subscriber which discards the response body.

**Returns:**
- a response body subscriber

---

#### public static <T>
HttpResponse.BodySubscriber
<T> buffering​(
HttpResponse.BodySubscriber
<T> downstream,
int bufferSize)

Returns a

BodySubscriber

which buffers data before delivering
it to the given downstream subscriber. The subscriber guarantees to
deliver

bufferSize

bytes of data to each invocation of the
downstream's

onNext

method,
except for the final invocation, just before

onComplete

is invoked. The final
invocation of

onNext

may contain fewer than

bufferSize

bytes.

The returned subscriber delegates its

getBody()

method to the downstream subscriber.

**Parameters:**
- downstream

- the downstream subscriber
- bufferSize

- the buffer size

**Returns:**
- a buffering body subscriber

**Throws:**
- IllegalArgumentException

- if

bufferSize <= 0

**Type Parameters:**
- T

- the type of the response body

---

#### public static <T,​U>
HttpResponse.BodySubscriber
<U> mapping​(
HttpResponse.BodySubscriber
<T> upstream,

Function
<? super T,​? extends U> mapper)

Returns a

BodySubscriber

whose response body value is that of
the result of applying the given function to the body object of the
given

upstream

BodySubscriber

.

The mapping function is executed using the client's

executor

, and can therefore be used to map any
response body type, including blocking

InputStream

, as shown
in the following example which uses a well-known JSON parser to
convert an

InputStream

into any annotated Java type.

For example:

```java
public static <W> BodySubscriber<W> asJSON(Class<W> targetType) {
BodySubscriber<InputStream> upstream = BodySubscribers.ofInputStream();

BodySubscriber<W> downstream = BodySubscribers.mapping(
upstream,
(InputStream is) -> {
try (InputStream stream = is) {
ObjectMapper objectMapper = new ObjectMapper();
return objectMapper.readValue(stream, targetType);
} catch (IOException e) {
throw new UncheckedIOException(e);
}
});
return downstream;
}
```

**Parameters:**
- upstream

- the body subscriber to be mapped
- mapper

- the mapping function

**Returns:**
- a mapping body subscriber

**Type Parameters:**
- T

- the upstream body type
- U

- the type of the body subscriber returned

---

### Additional Sections

#### Class HttpResponse.BodySubscribers

java.lang.Object

- java.net.http.HttpResponse.BodySubscribers

java.net.http.HttpResponse.BodySubscribers

**Enclosing interface:** HttpResponse

<

T

>

```java
public static class
HttpResponse.BodySubscribers

extends
Object
```

Implementations of

BodySubscriber

that implement
various useful subscribers, such as converting the response body bytes
into a String, or streaming the bytes to a file.

The following are examples of using the predefined body subscribers
to convert a flow of response body data into common high-level Java
objects:

```java
// Streams the response body to a File
HttpResponse<byte[]> response = client
.send(request, responseInfo -> BodySubscribers.ofByteArray());

// Accumulates the response body and returns it as a byte[]
HttpResponse<byte[]> response = client
.send(request, responseInfo -> BodySubscribers.ofByteArray());

// Discards the response body
HttpResponse<Void> response = client
.send(request, responseInfo -> BodySubscribers.discarding());

// Accumulates the response body as a String then maps it to its bytes
HttpResponse<byte[]> response = client
.send(request, responseInfo ->
BodySubscribers.mapping(BodySubscribers.ofString(UTF_8), String::getBytes));
```

**Since:** 11

public static class

HttpResponse.BodySubscribers

extends

Object

Implementations of

BodySubscriber

that implement
various useful subscribers, such as converting the response body bytes
into a String, or streaming the bytes to a file.

The following are examples of using the predefined body subscribers
to convert a flow of response body data into common high-level Java
objects:

```java
// Streams the response body to a File
HttpResponse<byte[]> response = client
.send(request, responseInfo -> BodySubscribers.ofByteArray());

// Accumulates the response body and returns it as a byte[]
HttpResponse<byte[]> response = client
.send(request, responseInfo -> BodySubscribers.ofByteArray());

// Discards the response body
HttpResponse<Void> response = client
.send(request, responseInfo -> BodySubscribers.discarding());

// Accumulates the response body as a String then maps it to its bytes
HttpResponse<byte[]> response = client
.send(request, responseInfo ->
BodySubscribers.mapping(BodySubscribers.ofString(UTF_8), String::getBytes));
```

The following are examples of using the predefined body subscribers
to convert a flow of response body data into common high-level Java
objects:

```java
// Streams the response body to a File
HttpResponse<byte[]> response = client
.send(request, responseInfo -> BodySubscribers.ofByteArray());

// Accumulates the response body and returns it as a byte[]
HttpResponse<byte[]> response = client
.send(request, responseInfo -> BodySubscribers.ofByteArray());

// Discards the response body
HttpResponse<Void> response = client
.send(request, responseInfo -> BodySubscribers.discarding());

// Accumulates the response body as a String then maps it to its bytes
HttpResponse<byte[]> response = client
.send(request, responseInfo ->
BodySubscribers.mapping(BodySubscribers.ofString(UTF_8), String::getBytes));
```

// Streams the response body to a File
HttpResponse<byte[]> response = client
.send(request, responseInfo -> BodySubscribers.ofByteArray());

// Accumulates the response body and returns it as a byte[]
HttpResponse<byte[]> response = client
.send(request, responseInfo -> BodySubscribers.ofByteArray());

// Discards the response body
HttpResponse<Void> response = client
.send(request, responseInfo -> BodySubscribers.discarding());

// Accumulates the response body as a String then maps it to its bytes
HttpResponse<byte[]> response = client
.send(request, responseInfo ->
BodySubscribers.mapping(BodySubscribers.ofString(UTF_8), String::getBytes));

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static <T>

HttpResponse.BodySubscriber

<T>

buffering

​(

HttpResponse.BodySubscriber

<T> downstream,
int bufferSize)

Returns a

BodySubscriber

which buffers data before delivering
it to the given downstream subscriber.

static

HttpResponse.BodySubscriber

<

Void

>

discarding

()

Returns a response subscriber which discards the response body.

static

HttpResponse.BodySubscriber

<

Void

>

fromLineSubscriber

​(

Flow.Subscriber

<? super

String

> subscriber)

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

, line by line.

static <S extends

Flow.Subscriber

<? super

String

>,​T>

HttpResponse.BodySubscriber

<T>

fromLineSubscriber

​(S subscriber,

Function

<? super S,​? extends T> finisher,

Charset

charset,

String

lineSeparator)

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

, line by line.

static

HttpResponse.BodySubscriber

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

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

.

static <S extends

Flow.Subscriber

<? super

List

<

ByteBuffer

>>,​T>

HttpResponse.BodySubscriber

<T>

fromSubscriber

​(S subscriber,

Function

<? super S,​? extends T> finisher)

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

.

static <T,​U>

HttpResponse.BodySubscriber

<U>

mapping

​(

HttpResponse.BodySubscriber

<T> upstream,

Function

<? super T,​? extends U> mapper)

Returns a

BodySubscriber

whose response body value is that of
the result of applying the given function to the body object of the
given

upstream

BodySubscriber

.

static

HttpResponse.BodySubscriber

<byte[]>

ofByteArray

()

Returns a

BodySubscriber

which stores the response body as a
byte array.

static

HttpResponse.BodySubscriber

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

BodySubscriber

which provides the incoming body
data to the provided Consumer of

Optional<byte[]>

.

static

HttpResponse.BodySubscriber

<

Path

>

ofFile

​(

Path

file)

Returns a

BodySubscriber

which stores the response body in a
file opened with the given name.

static

HttpResponse.BodySubscriber

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

BodySubscriber

which stores the response body in a
file opened with the given options and name.

static

HttpResponse.BodySubscriber

<

InputStream

>

ofInputStream

()

Returns a

BodySubscriber

which streams the response body as
an

InputStream

.

static

HttpResponse.BodySubscriber

<

Stream

<

String

>>

ofLines

​(

Charset

charset)

Returns a

BodySubscriber

which streams the response body as
a

Stream

, where each string in the stream
corresponds to a line as defined by

BufferedReader.lines()

.

static

HttpResponse.BodySubscriber

<

Flow.Publisher

<

List

<

ByteBuffer

>>>

ofPublisher

()

Returns a response subscriber which publishes the response body
through a

Publisher<List<ByteBuffer>>

.

static

HttpResponse.BodySubscriber

<

String

>

ofString

​(

Charset

charset)

Returns a body subscriber which stores the response body as a

String

converted using the given

Charset

.

static <U>

HttpResponse.BodySubscriber

<U>

replacing

​(U value)

Returns a response subscriber which discards the response body.

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

HttpResponse.BodySubscriber

<T>

buffering

​(

HttpResponse.BodySubscriber

<T> downstream,
int bufferSize)

Returns a

BodySubscriber

which buffers data before delivering
it to the given downstream subscriber.

static

HttpResponse.BodySubscriber

<

Void

>

discarding

()

Returns a response subscriber which discards the response body.

static

HttpResponse.BodySubscriber

<

Void

>

fromLineSubscriber

​(

Flow.Subscriber

<? super

String

> subscriber)

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

, line by line.

static <S extends

Flow.Subscriber

<? super

String

>,​T>

HttpResponse.BodySubscriber

<T>

fromLineSubscriber

​(S subscriber,

Function

<? super S,​? extends T> finisher,

Charset

charset,

String

lineSeparator)

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

, line by line.

static

HttpResponse.BodySubscriber

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

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

.

static <S extends

Flow.Subscriber

<? super

List

<

ByteBuffer

>>,​T>

HttpResponse.BodySubscriber

<T>

fromSubscriber

​(S subscriber,

Function

<? super S,​? extends T> finisher)

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

.

static <T,​U>

HttpResponse.BodySubscriber

<U>

mapping

​(

HttpResponse.BodySubscriber

<T> upstream,

Function

<? super T,​? extends U> mapper)

Returns a

BodySubscriber

whose response body value is that of
the result of applying the given function to the body object of the
given

upstream

BodySubscriber

.

static

HttpResponse.BodySubscriber

<byte[]>

ofByteArray

()

Returns a

BodySubscriber

which stores the response body as a
byte array.

static

HttpResponse.BodySubscriber

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

BodySubscriber

which provides the incoming body
data to the provided Consumer of

Optional<byte[]>

.

static

HttpResponse.BodySubscriber

<

Path

>

ofFile

​(

Path

file)

Returns a

BodySubscriber

which stores the response body in a
file opened with the given name.

static

HttpResponse.BodySubscriber

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

BodySubscriber

which stores the response body in a
file opened with the given options and name.

static

HttpResponse.BodySubscriber

<

InputStream

>

ofInputStream

()

Returns a

BodySubscriber

which streams the response body as
an

InputStream

.

static

HttpResponse.BodySubscriber

<

Stream

<

String

>>

ofLines

​(

Charset

charset)

Returns a

BodySubscriber

which streams the response body as
a

Stream

, where each string in the stream
corresponds to a line as defined by

BufferedReader.lines()

.

static

HttpResponse.BodySubscriber

<

Flow.Publisher

<

List

<

ByteBuffer

>>>

ofPublisher

()

Returns a response subscriber which publishes the response body
through a

Publisher<List<ByteBuffer>>

.

static

HttpResponse.BodySubscriber

<

String

>

ofString

​(

Charset

charset)

Returns a body subscriber which stores the response body as a

String

converted using the given

Charset

.

static <U>

HttpResponse.BodySubscriber

<U>

replacing

​(U value)

Returns a response subscriber which discards the response body.

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

BodySubscriber

which buffers data before delivering
it to the given downstream subscriber.

Returns a response subscriber which discards the response body.

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

, line by line.

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

.

Returns a

BodySubscriber

whose response body value is that of
the result of applying the given function to the body object of the
given

upstream

BodySubscriber

.

Returns a

BodySubscriber

which stores the response body as a
byte array.

Returns a

BodySubscriber

which provides the incoming body
data to the provided Consumer of

Optional<byte[]>

.

Returns a

BodySubscriber

which stores the response body in a
file opened with the given name.

Returns a

BodySubscriber

which stores the response body in a
file opened with the given options and name.

Returns a

BodySubscriber

which streams the response body as
an

InputStream

.

Returns a

BodySubscriber

which streams the response body as
a

Stream

, where each string in the stream
corresponds to a line as defined by

BufferedReader.lines()

.

Returns a response subscriber which publishes the response body
through a

Publisher<List<ByteBuffer>>

.

Returns a body subscriber which stores the response body as a

String

converted using the given

Charset

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

============ METHOD DETAIL ==========

- Method Detail

- fromSubscriber

```java
public static
HttpResponse.BodySubscriber
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

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

. The

completion stage

of the returned body subscriber completes after one
of the given subscribers

onComplete

or

onError

has
been invoked.

**API Note:** This method can be used as an adapter between

BodySubscriber

and

Flow.Subscriber

.
**Parameters:** subscriber

- the subscriber
**Returns:** a body subscriber

- fromSubscriber

```java
public static <S extends
Flow.Subscriber
<? super
List
<
ByteBuffer
>>,​T>
HttpResponse.BodySubscriber
<T> fromSubscriber​(S subscriber,

Function
<? super S,​? extends T> finisher)
```

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

. The

completion stage

of the returned body subscriber completes after one
of the given subscribers

onComplete

or

onError

has
been invoked.

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
**Type Parameters:** S

- the type of the Subscriber
**Type Parameters:** T

- the type of the response body
**Parameters:** subscriber

- the subscriber
**Parameters:** finisher

- a function to be applied after the subscriber has
completed
**Returns:** a body subscriber

- fromLineSubscriber

```java
public static
HttpResponse.BodySubscriber
<
Void
> fromLineSubscriber​(
Flow.Subscriber
<? super
String
> subscriber)
```

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

, line by line.
The

completion
stage

of the returned body subscriber completes after one of the
given subscribers

onComplete

or

onError

has been
invoked.
Bytes are decoded using the

UTF-8

charset, and lines are delimited in the manner of

BufferedReader.readLine()

.

**API Note:** This method can be used as an adapter between

BodySubscriber

and

Flow.Subscriber

.
**Implementation Note:** This is equivalent to calling

```java
fromLineSubscriber(subscriber, s -> null, StandardCharsets.UTF_8, null)
```
**Parameters:** subscriber

- the subscriber
**Returns:** a body subscriber

- fromLineSubscriber

```java
public static <S extends
Flow.Subscriber
<? super
String
>,​T>
HttpResponse.BodySubscriber
<T> fromLineSubscriber​(S subscriber,

Function
<? super S,​? extends T> finisher,

Charset
charset,

String
lineSeparator)
```

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

, line by line. The

completion stage

of the returned body
subscriber completes after one of the given subscribers

onComplete

or

onError

has been invoked.

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
**Type Parameters:** S

- the type of the Subscriber
**Type Parameters:** T

- the type of the response body
**Parameters:** subscriber

- the subscriber
**Parameters:** finisher

- a function to be applied after the subscriber has
completed
**Parameters:** charset

- a

Charset

to decode the bytes
**Parameters:** lineSeparator

- an optional line separator: can be

null

,
in which case lines will be delimited in the manner of

BufferedReader.readLine()

.
**Returns:** a body subscriber
**Throws:** IllegalArgumentException

- if the supplied

lineSeparator

is the empty string

- ofString

```java
public static
HttpResponse.BodySubscriber
<
String
> ofString​(
Charset
charset)
```

Returns a body subscriber which stores the response body as a

String

converted using the given

Charset

.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

**Parameters:** charset

- the character set to convert the String with
**Returns:** a body subscriber

- ofByteArray

```java
public static
HttpResponse.BodySubscriber
<byte[]> ofByteArray()
```

Returns a

BodySubscriber

which stores the response body as a
byte array.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

**Returns:** a body subscriber

- ofFile

```java
public static
HttpResponse.BodySubscriber
<
Path
> ofFile​(
Path
file,

OpenOption
... openOptions)
```

Returns a

BodySubscriber

which stores the response body in a
file opened with the given options and name. The file will be opened
with the given options using

FileChannel.open

just before the body is read. Any exception thrown
will be returned or thrown from

HttpClient::send

or

HttpClient::sendAsync

as appropriate.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

Security manager permission checks are performed in this factory
method, when the

BodySubscriber

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

**Parameters:** file

- the file to store the body in
**Parameters:** openOptions

- the list of options to open the file with
**Returns:** a body subscriber
**Throws:** IllegalArgumentException

- if an invalid set of open options
are specified
**Throws:** SecurityException

- if a security manager has been installed
and it denies

write access

to the file

- ofFile

```java
public static
HttpResponse.BodySubscriber
<
Path
> ofFile​(
Path
file)
```

Returns a

BodySubscriber

which stores the response body in a
file opened with the given name.

Equivalent to:

ofFile(file, CREATE, WRITE)

Security manager permission checks are performed in this factory
method, when the

BodySubscriber

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

**Parameters:** file

- the file to store the body in
**Returns:** a body subscriber
**Throws:** SecurityException

- if a security manager has been installed
and it denies

write access

to the file

- ofByteArrayConsumer

```java
public static
HttpResponse.BodySubscriber
<
Void
> ofByteArrayConsumer​(
Consumer
<
Optional
<byte[]>> consumer)
```

Returns a

BodySubscriber

which provides the incoming body
data to the provided Consumer of

Optional<byte[]>

. Each
call to

Consumer.accept()

will contain a non empty

Optional

, except for the final
invocation after all body data has been read, when the

Optional

will be empty.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

**API Note:** This subscriber is not flow controlled.
Therefore, the supplied consumer must be able to process whatever
amount of data is delivered in a timely fashion.
**Parameters:** consumer

- a Consumer of byte arrays
**Returns:** a BodySubscriber

- ofInputStream

```java
public static
HttpResponse.BodySubscriber
<
InputStream
> ofInputStream()
```

Returns a

BodySubscriber

which streams the response body as
an

InputStream

.

The

HttpResponse

using this subscriber is available
immediately after the response headers have been read, without
requiring to wait for the entire body to be processed. The response
body can then be read directly from the

InputStream

.

**API Note:** To ensure that all resources associated with the
corresponding exchange are properly released the caller must
ensure to either read all bytes until EOF is reached, or call

InputStream.close()

if it is unable or unwilling to do so.
Calling

close

before exhausting the stream may cause
the underlying HTTP connection to be closed and prevent it
from being reused for subsequent operations.
**Returns:** a body subscriber that streams the response body as an

InputStream

.

- ofLines

```java
public static
HttpResponse.BodySubscriber
<
Stream
<
String
>> ofLines​(
Charset
charset)
```

Returns a

BodySubscriber

which streams the response body as
a

Stream

, where each string in the stream
corresponds to a line as defined by

BufferedReader.lines()

.

The

HttpResponse

using this subscriber is available
immediately after the response headers have been read, without
requiring to wait for the entire body to be processed. The response
body can then be read directly from the

Stream

.

**API Note:** To ensure that all resources associated with the
corresponding exchange are properly released the caller must
ensure to either read all lines until the stream is exhausted,
or call

BaseStream.close()

if it is unable or unwilling to do so.
Calling

close

before exhausting the stream may cause
the underlying HTTP connection to be closed and prevent it
from being reused for subsequent operations.
**Parameters:** charset

- the character set to use when converting bytes to characters
**Returns:** a body subscriber that streams the response body as a

Stream

.
**See Also:** BufferedReader.lines()

- ofPublisher

```java
public static
HttpResponse.BodySubscriber
<
Flow.Publisher
<
List
<
ByteBuffer
>>> ofPublisher()
```

Returns a response subscriber which publishes the response body
through a

Publisher<List<ByteBuffer>>

.

The

HttpResponse

using this subscriber is available
immediately after the response headers have been read, without
requiring to wait for the entire body to be processed. The response
body bytes can then be obtained by subscribing to the publisher
returned by the

HttpResponse

body

method.

The publisher returned by the

body

method can be subscribed to only once. The first subscriber will
receive the body response bytes if successfully subscribed, or will
cause the subscription to be cancelled otherwise.
If more subscriptions are attempted, the subsequent subscribers will
be immediately subscribed with an empty subscription and their

onError

method
will be invoked with an

IllegalStateException

.

**API Note:** To ensure that all resources associated with the
corresponding exchange are properly released the caller must
ensure that the provided publisher is subscribed once, and either

requests

all bytes
until

onComplete

or

onError

are invoked, or
cancel the provided

subscription

if it is unable or unwilling to do so.
Note that depending on the actual HTTP protocol

version

used for the exchange, cancelling the
subscription instead of exhausting the flow may cause the underlying
HTTP connection to be closed and prevent it from being reused for
subsequent operations.
**Returns:** A

BodySubscriber

which publishes the response body
through a

Publisher<List<ByteBuffer>>

.

- replacing

```java
public static <U>
HttpResponse.BodySubscriber
<U> replacing​(U value)
```

Returns a response subscriber which discards the response body. The
supplied value is the value that will be returned from

HttpResponse.body()

.

**Type Parameters:** U

- the type of the response body
**Parameters:** value

- the value to return from HttpResponse.body(), may be

null
**Returns:** a

BodySubscriber

- discarding

```java
public static
HttpResponse.BodySubscriber
<
Void
> discarding()
```

Returns a response subscriber which discards the response body.

**Returns:** a response body subscriber

- buffering

```java
public static <T>
HttpResponse.BodySubscriber
<T> buffering​(
HttpResponse.BodySubscriber
<T> downstream,
int bufferSize)
```

Returns a

BodySubscriber

which buffers data before delivering
it to the given downstream subscriber. The subscriber guarantees to
deliver

bufferSize

bytes of data to each invocation of the
downstream's

onNext

method,
except for the final invocation, just before

onComplete

is invoked. The final
invocation of

onNext

may contain fewer than

bufferSize

bytes.

The returned subscriber delegates its

getBody()

method to the downstream subscriber.

**Type Parameters:** T

- the type of the response body
**Parameters:** downstream

- the downstream subscriber
**Parameters:** bufferSize

- the buffer size
**Returns:** a buffering body subscriber
**Throws:** IllegalArgumentException

- if

bufferSize <= 0

- mapping

```java
public static <T,​U>
HttpResponse.BodySubscriber
<U> mapping​(
HttpResponse.BodySubscriber
<T> upstream,

Function
<? super T,​? extends U> mapper)
```

Returns a

BodySubscriber

whose response body value is that of
the result of applying the given function to the body object of the
given

upstream

BodySubscriber

.

The mapping function is executed using the client's

executor

, and can therefore be used to map any
response body type, including blocking

InputStream

, as shown
in the following example which uses a well-known JSON parser to
convert an

InputStream

into any annotated Java type.

For example:

```java
public static <W> BodySubscriber<W> asJSON(Class<W> targetType) {
BodySubscriber<InputStream> upstream = BodySubscribers.ofInputStream();

BodySubscriber<W> downstream = BodySubscribers.mapping(
upstream,
(InputStream is) -> {
try (InputStream stream = is) {
ObjectMapper objectMapper = new ObjectMapper();
return objectMapper.readValue(stream, targetType);
} catch (IOException e) {
throw new UncheckedIOException(e);
}
});
return downstream;
}
```

**Type Parameters:** T

- the upstream body type
**Type Parameters:** U

- the type of the body subscriber returned
**Parameters:** upstream

- the body subscriber to be mapped
**Parameters:** mapper

- the mapping function
**Returns:** a mapping body subscriber

Method Detail

- fromSubscriber

```java
public static
HttpResponse.BodySubscriber
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

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

. The

completion stage

of the returned body subscriber completes after one
of the given subscribers

onComplete

or

onError

has
been invoked.

**API Note:** This method can be used as an adapter between

BodySubscriber

and

Flow.Subscriber

.
**Parameters:** subscriber

- the subscriber
**Returns:** a body subscriber

- fromSubscriber

```java
public static <S extends
Flow.Subscriber
<? super
List
<
ByteBuffer
>>,​T>
HttpResponse.BodySubscriber
<T> fromSubscriber​(S subscriber,

Function
<? super S,​? extends T> finisher)
```

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

. The

completion stage

of the returned body subscriber completes after one
of the given subscribers

onComplete

or

onError

has
been invoked.

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
**Type Parameters:** S

- the type of the Subscriber
**Type Parameters:** T

- the type of the response body
**Parameters:** subscriber

- the subscriber
**Parameters:** finisher

- a function to be applied after the subscriber has
completed
**Returns:** a body subscriber

- fromLineSubscriber

```java
public static
HttpResponse.BodySubscriber
<
Void
> fromLineSubscriber​(
Flow.Subscriber
<? super
String
> subscriber)
```

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

, line by line.
The

completion
stage

of the returned body subscriber completes after one of the
given subscribers

onComplete

or

onError

has been
invoked.
Bytes are decoded using the

UTF-8

charset, and lines are delimited in the manner of

BufferedReader.readLine()

.

**API Note:** This method can be used as an adapter between

BodySubscriber

and

Flow.Subscriber

.
**Implementation Note:** This is equivalent to calling

```java
fromLineSubscriber(subscriber, s -> null, StandardCharsets.UTF_8, null)
```
**Parameters:** subscriber

- the subscriber
**Returns:** a body subscriber

- fromLineSubscriber

```java
public static <S extends
Flow.Subscriber
<? super
String
>,​T>
HttpResponse.BodySubscriber
<T> fromLineSubscriber​(S subscriber,

Function
<? super S,​? extends T> finisher,

Charset
charset,

String
lineSeparator)
```

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

, line by line. The

completion stage

of the returned body
subscriber completes after one of the given subscribers

onComplete

or

onError

has been invoked.

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
**Type Parameters:** S

- the type of the Subscriber
**Type Parameters:** T

- the type of the response body
**Parameters:** subscriber

- the subscriber
**Parameters:** finisher

- a function to be applied after the subscriber has
completed
**Parameters:** charset

- a

Charset

to decode the bytes
**Parameters:** lineSeparator

- an optional line separator: can be

null

,
in which case lines will be delimited in the manner of

BufferedReader.readLine()

.
**Returns:** a body subscriber
**Throws:** IllegalArgumentException

- if the supplied

lineSeparator

is the empty string

- ofString

```java
public static
HttpResponse.BodySubscriber
<
String
> ofString​(
Charset
charset)
```

Returns a body subscriber which stores the response body as a

String

converted using the given

Charset

.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

**Parameters:** charset

- the character set to convert the String with
**Returns:** a body subscriber

- ofByteArray

```java
public static
HttpResponse.BodySubscriber
<byte[]> ofByteArray()
```

Returns a

BodySubscriber

which stores the response body as a
byte array.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

**Returns:** a body subscriber

- ofFile

```java
public static
HttpResponse.BodySubscriber
<
Path
> ofFile​(
Path
file,

OpenOption
... openOptions)
```

Returns a

BodySubscriber

which stores the response body in a
file opened with the given options and name. The file will be opened
with the given options using

FileChannel.open

just before the body is read. Any exception thrown
will be returned or thrown from

HttpClient::send

or

HttpClient::sendAsync

as appropriate.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

Security manager permission checks are performed in this factory
method, when the

BodySubscriber

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

**Parameters:** file

- the file to store the body in
**Parameters:** openOptions

- the list of options to open the file with
**Returns:** a body subscriber
**Throws:** IllegalArgumentException

- if an invalid set of open options
are specified
**Throws:** SecurityException

- if a security manager has been installed
and it denies

write access

to the file

- ofFile

```java
public static
HttpResponse.BodySubscriber
<
Path
> ofFile​(
Path
file)
```

Returns a

BodySubscriber

which stores the response body in a
file opened with the given name.

Equivalent to:

ofFile(file, CREATE, WRITE)

Security manager permission checks are performed in this factory
method, when the

BodySubscriber

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

**Parameters:** file

- the file to store the body in
**Returns:** a body subscriber
**Throws:** SecurityException

- if a security manager has been installed
and it denies

write access

to the file

- ofByteArrayConsumer

```java
public static
HttpResponse.BodySubscriber
<
Void
> ofByteArrayConsumer​(
Consumer
<
Optional
<byte[]>> consumer)
```

Returns a

BodySubscriber

which provides the incoming body
data to the provided Consumer of

Optional<byte[]>

. Each
call to

Consumer.accept()

will contain a non empty

Optional

, except for the final
invocation after all body data has been read, when the

Optional

will be empty.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

**API Note:** This subscriber is not flow controlled.
Therefore, the supplied consumer must be able to process whatever
amount of data is delivered in a timely fashion.
**Parameters:** consumer

- a Consumer of byte arrays
**Returns:** a BodySubscriber

- ofInputStream

```java
public static
HttpResponse.BodySubscriber
<
InputStream
> ofInputStream()
```

Returns a

BodySubscriber

which streams the response body as
an

InputStream

.

The

HttpResponse

using this subscriber is available
immediately after the response headers have been read, without
requiring to wait for the entire body to be processed. The response
body can then be read directly from the

InputStream

.

**API Note:** To ensure that all resources associated with the
corresponding exchange are properly released the caller must
ensure to either read all bytes until EOF is reached, or call

InputStream.close()

if it is unable or unwilling to do so.
Calling

close

before exhausting the stream may cause
the underlying HTTP connection to be closed and prevent it
from being reused for subsequent operations.
**Returns:** a body subscriber that streams the response body as an

InputStream

.

- ofLines

```java
public static
HttpResponse.BodySubscriber
<
Stream
<
String
>> ofLines​(
Charset
charset)
```

Returns a

BodySubscriber

which streams the response body as
a

Stream

, where each string in the stream
corresponds to a line as defined by

BufferedReader.lines()

.

The

HttpResponse

using this subscriber is available
immediately after the response headers have been read, without
requiring to wait for the entire body to be processed. The response
body can then be read directly from the

Stream

.

**API Note:** To ensure that all resources associated with the
corresponding exchange are properly released the caller must
ensure to either read all lines until the stream is exhausted,
or call

BaseStream.close()

if it is unable or unwilling to do so.
Calling

close

before exhausting the stream may cause
the underlying HTTP connection to be closed and prevent it
from being reused for subsequent operations.
**Parameters:** charset

- the character set to use when converting bytes to characters
**Returns:** a body subscriber that streams the response body as a

Stream

.
**See Also:** BufferedReader.lines()

- ofPublisher

```java
public static
HttpResponse.BodySubscriber
<
Flow.Publisher
<
List
<
ByteBuffer
>>> ofPublisher()
```

Returns a response subscriber which publishes the response body
through a

Publisher<List<ByteBuffer>>

.

The

HttpResponse

using this subscriber is available
immediately after the response headers have been read, without
requiring to wait for the entire body to be processed. The response
body bytes can then be obtained by subscribing to the publisher
returned by the

HttpResponse

body

method.

The publisher returned by the

body

method can be subscribed to only once. The first subscriber will
receive the body response bytes if successfully subscribed, or will
cause the subscription to be cancelled otherwise.
If more subscriptions are attempted, the subsequent subscribers will
be immediately subscribed with an empty subscription and their

onError

method
will be invoked with an

IllegalStateException

.

**API Note:** To ensure that all resources associated with the
corresponding exchange are properly released the caller must
ensure that the provided publisher is subscribed once, and either

requests

all bytes
until

onComplete

or

onError

are invoked, or
cancel the provided

subscription

if it is unable or unwilling to do so.
Note that depending on the actual HTTP protocol

version

used for the exchange, cancelling the
subscription instead of exhausting the flow may cause the underlying
HTTP connection to be closed and prevent it from being reused for
subsequent operations.
**Returns:** A

BodySubscriber

which publishes the response body
through a

Publisher<List<ByteBuffer>>

.

- replacing

```java
public static <U>
HttpResponse.BodySubscriber
<U> replacing​(U value)
```

Returns a response subscriber which discards the response body. The
supplied value is the value that will be returned from

HttpResponse.body()

.

**Type Parameters:** U

- the type of the response body
**Parameters:** value

- the value to return from HttpResponse.body(), may be

null
**Returns:** a

BodySubscriber

- discarding

```java
public static
HttpResponse.BodySubscriber
<
Void
> discarding()
```

Returns a response subscriber which discards the response body.

**Returns:** a response body subscriber

- buffering

```java
public static <T>
HttpResponse.BodySubscriber
<T> buffering​(
HttpResponse.BodySubscriber
<T> downstream,
int bufferSize)
```

Returns a

BodySubscriber

which buffers data before delivering
it to the given downstream subscriber. The subscriber guarantees to
deliver

bufferSize

bytes of data to each invocation of the
downstream's

onNext

method,
except for the final invocation, just before

onComplete

is invoked. The final
invocation of

onNext

may contain fewer than

bufferSize

bytes.

The returned subscriber delegates its

getBody()

method to the downstream subscriber.

**Type Parameters:** T

- the type of the response body
**Parameters:** downstream

- the downstream subscriber
**Parameters:** bufferSize

- the buffer size
**Returns:** a buffering body subscriber
**Throws:** IllegalArgumentException

- if

bufferSize <= 0

- mapping

```java
public static <T,​U>
HttpResponse.BodySubscriber
<U> mapping​(
HttpResponse.BodySubscriber
<T> upstream,

Function
<? super T,​? extends U> mapper)
```

Returns a

BodySubscriber

whose response body value is that of
the result of applying the given function to the body object of the
given

upstream

BodySubscriber

.

The mapping function is executed using the client's

executor

, and can therefore be used to map any
response body type, including blocking

InputStream

, as shown
in the following example which uses a well-known JSON parser to
convert an

InputStream

into any annotated Java type.

For example:

```java
public static <W> BodySubscriber<W> asJSON(Class<W> targetType) {
BodySubscriber<InputStream> upstream = BodySubscribers.ofInputStream();

BodySubscriber<W> downstream = BodySubscribers.mapping(
upstream,
(InputStream is) -> {
try (InputStream stream = is) {
ObjectMapper objectMapper = new ObjectMapper();
return objectMapper.readValue(stream, targetType);
} catch (IOException e) {
throw new UncheckedIOException(e);
}
});
return downstream;
}
```

**Type Parameters:** T

- the upstream body type
**Type Parameters:** U

- the type of the body subscriber returned
**Parameters:** upstream

- the body subscriber to be mapped
**Parameters:** mapper

- the mapping function
**Returns:** a mapping body subscriber

---

#### Method Detail

fromSubscriber

```java
public static
HttpResponse.BodySubscriber
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

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

. The

completion stage

of the returned body subscriber completes after one
of the given subscribers

onComplete

or

onError

has
been invoked.

**API Note:** This method can be used as an adapter between

BodySubscriber

and

Flow.Subscriber

.
**Parameters:** subscriber

- the subscriber
**Returns:** a body subscriber

---

#### fromSubscriber

public static

HttpResponse.BodySubscriber

<

Void

> fromSubscriber​(

Flow.Subscriber

<? super

List

<

ByteBuffer

>> subscriber)

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

. The

completion stage

of the returned body subscriber completes after one
of the given subscribers

onComplete

or

onError

has
been invoked.

fromSubscriber

```java
public static <S extends
Flow.Subscriber
<? super
List
<
ByteBuffer
>>,​T>
HttpResponse.BodySubscriber
<T> fromSubscriber​(S subscriber,

Function
<? super S,​? extends T> finisher)
```

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

. The

completion stage

of the returned body subscriber completes after one
of the given subscribers

onComplete

or

onError

has
been invoked.

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
**Type Parameters:** S

- the type of the Subscriber
**Type Parameters:** T

- the type of the response body
**Parameters:** subscriber

- the subscriber
**Parameters:** finisher

- a function to be applied after the subscriber has
completed
**Returns:** a body subscriber

---

#### fromSubscriber

public static <S extends

Flow.Subscriber

<? super

List

<

ByteBuffer

>>,​T>

HttpResponse.BodySubscriber

<T> fromSubscriber​(S subscriber,

Function

<? super S,​? extends T> finisher)

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

. The

completion stage

of the returned body subscriber completes after one
of the given subscribers

onComplete

or

onError

has
been invoked.

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

fromLineSubscriber

```java
public static
HttpResponse.BodySubscriber
<
Void
> fromLineSubscriber​(
Flow.Subscriber
<? super
String
> subscriber)
```

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

, line by line.
The

completion
stage

of the returned body subscriber completes after one of the
given subscribers

onComplete

or

onError

has been
invoked.
Bytes are decoded using the

UTF-8

charset, and lines are delimited in the manner of

BufferedReader.readLine()

.

**API Note:** This method can be used as an adapter between

BodySubscriber

and

Flow.Subscriber

.
**Implementation Note:** This is equivalent to calling

```java
fromLineSubscriber(subscriber, s -> null, StandardCharsets.UTF_8, null)
```
**Parameters:** subscriber

- the subscriber
**Returns:** a body subscriber

---

#### fromLineSubscriber

public static

HttpResponse.BodySubscriber

<

Void

> fromLineSubscriber​(

Flow.Subscriber

<? super

String

> subscriber)

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

, line by line.
The

completion
stage

of the returned body subscriber completes after one of the
given subscribers

onComplete

or

onError

has been
invoked.
Bytes are decoded using the

UTF-8

charset, and lines are delimited in the manner of

BufferedReader.readLine()

.

fromLineSubscriber(subscriber, s -> null, StandardCharsets.UTF_8, null)

fromLineSubscriber

```java
public static <S extends
Flow.Subscriber
<? super
String
>,​T>
HttpResponse.BodySubscriber
<T> fromLineSubscriber​(S subscriber,

Function
<? super S,​? extends T> finisher,

Charset
charset,

String
lineSeparator)
```

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

, line by line. The

completion stage

of the returned body
subscriber completes after one of the given subscribers

onComplete

or

onError

has been invoked.

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
**Type Parameters:** S

- the type of the Subscriber
**Type Parameters:** T

- the type of the response body
**Parameters:** subscriber

- the subscriber
**Parameters:** finisher

- a function to be applied after the subscriber has
completed
**Parameters:** charset

- a

Charset

to decode the bytes
**Parameters:** lineSeparator

- an optional line separator: can be

null

,
in which case lines will be delimited in the manner of

BufferedReader.readLine()

.
**Returns:** a body subscriber
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

HttpResponse.BodySubscriber

<T> fromLineSubscriber​(S subscriber,

Function

<? super S,​? extends T> finisher,

Charset

charset,

String

lineSeparator)

Returns a body subscriber that forwards all response body to the
given

Flow.Subscriber

, line by line. The

completion stage

of the returned body
subscriber completes after one of the given subscribers

onComplete

or

onError

has been invoked.

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

ofString

```java
public static
HttpResponse.BodySubscriber
<
String
> ofString​(
Charset
charset)
```

Returns a body subscriber which stores the response body as a

String

converted using the given

Charset

.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

**Parameters:** charset

- the character set to convert the String with
**Returns:** a body subscriber

---

#### ofString

public static

HttpResponse.BodySubscriber

<

String

> ofString​(

Charset

charset)

Returns a body subscriber which stores the response body as a

String

converted using the given

Charset

.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

ofByteArray

```java
public static
HttpResponse.BodySubscriber
<byte[]> ofByteArray()
```

Returns a

BodySubscriber

which stores the response body as a
byte array.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

**Returns:** a body subscriber

---

#### ofByteArray

public static

HttpResponse.BodySubscriber

<byte[]> ofByteArray()

Returns a

BodySubscriber

which stores the response body as a
byte array.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

ofFile

```java
public static
HttpResponse.BodySubscriber
<
Path
> ofFile​(
Path
file,

OpenOption
... openOptions)
```

Returns a

BodySubscriber

which stores the response body in a
file opened with the given options and name. The file will be opened
with the given options using

FileChannel.open

just before the body is read. Any exception thrown
will be returned or thrown from

HttpClient::send

or

HttpClient::sendAsync

as appropriate.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

Security manager permission checks are performed in this factory
method, when the

BodySubscriber

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

**Parameters:** file

- the file to store the body in
**Parameters:** openOptions

- the list of options to open the file with
**Returns:** a body subscriber
**Throws:** IllegalArgumentException

- if an invalid set of open options
are specified
**Throws:** SecurityException

- if a security manager has been installed
and it denies

write access

to the file

---

#### ofFile

public static

HttpResponse.BodySubscriber

<

Path

> ofFile​(

Path

file,

OpenOption

... openOptions)

Returns a

BodySubscriber

which stores the response body in a
file opened with the given options and name. The file will be opened
with the given options using

FileChannel.open

just before the body is read. Any exception thrown
will be returned or thrown from

HttpClient::send

or

HttpClient::sendAsync

as appropriate.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

Security manager permission checks are performed in this factory
method, when the

BodySubscriber

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

Security manager permission checks are performed in this factory
method, when the

BodySubscriber

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

Security manager permission checks are performed in this factory
method, when the

BodySubscriber

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

ofFile

```java
public static
HttpResponse.BodySubscriber
<
Path
> ofFile​(
Path
file)
```

Returns a

BodySubscriber

which stores the response body in a
file opened with the given name.

Equivalent to:

ofFile(file, CREATE, WRITE)

Security manager permission checks are performed in this factory
method, when the

BodySubscriber

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

**Parameters:** file

- the file to store the body in
**Returns:** a body subscriber
**Throws:** SecurityException

- if a security manager has been installed
and it denies

write access

to the file

---

#### ofFile

public static

HttpResponse.BodySubscriber

<

Path

> ofFile​(

Path

file)

Returns a

BodySubscriber

which stores the response body in a
file opened with the given name.

Equivalent to:

ofFile(file, CREATE, WRITE)

Security manager permission checks are performed in this factory
method, when the

BodySubscriber

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

Equivalent to:

ofFile(file, CREATE, WRITE)

Security manager permission checks are performed in this factory
method, when the

BodySubscriber

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

Security manager permission checks are performed in this factory
method, when the

BodySubscriber

is created. Care must be taken
that the

BodyHandler

is not shared with untrusted code.

ofByteArrayConsumer

```java
public static
HttpResponse.BodySubscriber
<
Void
> ofByteArrayConsumer​(
Consumer
<
Optional
<byte[]>> consumer)
```

Returns a

BodySubscriber

which provides the incoming body
data to the provided Consumer of

Optional<byte[]>

. Each
call to

Consumer.accept()

will contain a non empty

Optional

, except for the final
invocation after all body data has been read, when the

Optional

will be empty.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

**API Note:** This subscriber is not flow controlled.
Therefore, the supplied consumer must be able to process whatever
amount of data is delivered in a timely fashion.
**Parameters:** consumer

- a Consumer of byte arrays
**Returns:** a BodySubscriber

---

#### ofByteArrayConsumer

public static

HttpResponse.BodySubscriber

<

Void

> ofByteArrayConsumer​(

Consumer

<

Optional

<byte[]>> consumer)

Returns a

BodySubscriber

which provides the incoming body
data to the provided Consumer of

Optional<byte[]>

. Each
call to

Consumer.accept()

will contain a non empty

Optional

, except for the final
invocation after all body data has been read, when the

Optional

will be empty.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

The

HttpResponse

using this subscriber is available after
the entire response has been read.

ofInputStream

```java
public static
HttpResponse.BodySubscriber
<
InputStream
> ofInputStream()
```

Returns a

BodySubscriber

which streams the response body as
an

InputStream

.

The

HttpResponse

using this subscriber is available
immediately after the response headers have been read, without
requiring to wait for the entire body to be processed. The response
body can then be read directly from the

InputStream

.

**API Note:** To ensure that all resources associated with the
corresponding exchange are properly released the caller must
ensure to either read all bytes until EOF is reached, or call

InputStream.close()

if it is unable or unwilling to do so.
Calling

close

before exhausting the stream may cause
the underlying HTTP connection to be closed and prevent it
from being reused for subsequent operations.
**Returns:** a body subscriber that streams the response body as an

InputStream

.

---

#### ofInputStream

public static

HttpResponse.BodySubscriber

<

InputStream

> ofInputStream()

Returns a

BodySubscriber

which streams the response body as
an

InputStream

.

The

HttpResponse

using this subscriber is available
immediately after the response headers have been read, without
requiring to wait for the entire body to be processed. The response
body can then be read directly from the

InputStream

.

The

HttpResponse

using this subscriber is available
immediately after the response headers have been read, without
requiring to wait for the entire body to be processed. The response
body can then be read directly from the

InputStream

.

ofLines

```java
public static
HttpResponse.BodySubscriber
<
Stream
<
String
>> ofLines​(
Charset
charset)
```

Returns a

BodySubscriber

which streams the response body as
a

Stream

, where each string in the stream
corresponds to a line as defined by

BufferedReader.lines()

.

The

HttpResponse

using this subscriber is available
immediately after the response headers have been read, without
requiring to wait for the entire body to be processed. The response
body can then be read directly from the

Stream

.

**API Note:** To ensure that all resources associated with the
corresponding exchange are properly released the caller must
ensure to either read all lines until the stream is exhausted,
or call

BaseStream.close()

if it is unable or unwilling to do so.
Calling

close

before exhausting the stream may cause
the underlying HTTP connection to be closed and prevent it
from being reused for subsequent operations.
**Parameters:** charset

- the character set to use when converting bytes to characters
**Returns:** a body subscriber that streams the response body as a

Stream

.
**See Also:** BufferedReader.lines()

---

#### ofLines

public static

HttpResponse.BodySubscriber

<

Stream

<

String

>> ofLines​(

Charset

charset)

Returns a

BodySubscriber

which streams the response body as
a

Stream

, where each string in the stream
corresponds to a line as defined by

BufferedReader.lines()

.

The

HttpResponse

using this subscriber is available
immediately after the response headers have been read, without
requiring to wait for the entire body to be processed. The response
body can then be read directly from the

Stream

.

The

HttpResponse

using this subscriber is available
immediately after the response headers have been read, without
requiring to wait for the entire body to be processed. The response
body can then be read directly from the

Stream

.

ofPublisher

```java
public static
HttpResponse.BodySubscriber
<
Flow.Publisher
<
List
<
ByteBuffer
>>> ofPublisher()
```

Returns a response subscriber which publishes the response body
through a

Publisher<List<ByteBuffer>>

.

The

HttpResponse

using this subscriber is available
immediately after the response headers have been read, without
requiring to wait for the entire body to be processed. The response
body bytes can then be obtained by subscribing to the publisher
returned by the

HttpResponse

body

method.

The publisher returned by the

body

method can be subscribed to only once. The first subscriber will
receive the body response bytes if successfully subscribed, or will
cause the subscription to be cancelled otherwise.
If more subscriptions are attempted, the subsequent subscribers will
be immediately subscribed with an empty subscription and their

onError

method
will be invoked with an

IllegalStateException

.

**API Note:** To ensure that all resources associated with the
corresponding exchange are properly released the caller must
ensure that the provided publisher is subscribed once, and either

requests

all bytes
until

onComplete

or

onError

are invoked, or
cancel the provided

subscription

if it is unable or unwilling to do so.
Note that depending on the actual HTTP protocol

version

used for the exchange, cancelling the
subscription instead of exhausting the flow may cause the underlying
HTTP connection to be closed and prevent it from being reused for
subsequent operations.
**Returns:** A

BodySubscriber

which publishes the response body
through a

Publisher<List<ByteBuffer>>

.

---

#### ofPublisher

public static

HttpResponse.BodySubscriber

<

Flow.Publisher

<

List

<

ByteBuffer

>>> ofPublisher()

Returns a response subscriber which publishes the response body
through a

Publisher<List<ByteBuffer>>

.

The

HttpResponse

using this subscriber is available
immediately after the response headers have been read, without
requiring to wait for the entire body to be processed. The response
body bytes can then be obtained by subscribing to the publisher
returned by the

HttpResponse

body

method.

The publisher returned by the

body

method can be subscribed to only once. The first subscriber will
receive the body response bytes if successfully subscribed, or will
cause the subscription to be cancelled otherwise.
If more subscriptions are attempted, the subsequent subscribers will
be immediately subscribed with an empty subscription and their

onError

method
will be invoked with an

IllegalStateException

.

The

HttpResponse

using this subscriber is available
immediately after the response headers have been read, without
requiring to wait for the entire body to be processed. The response
body bytes can then be obtained by subscribing to the publisher
returned by the

HttpResponse

body

method.

The publisher returned by the

body

method can be subscribed to only once. The first subscriber will
receive the body response bytes if successfully subscribed, or will
cause the subscription to be cancelled otherwise.
If more subscriptions are attempted, the subsequent subscribers will
be immediately subscribed with an empty subscription and their

onError

method
will be invoked with an

IllegalStateException

.

The publisher returned by the

body

method can be subscribed to only once. The first subscriber will
receive the body response bytes if successfully subscribed, or will
cause the subscription to be cancelled otherwise.
If more subscriptions are attempted, the subsequent subscribers will
be immediately subscribed with an empty subscription and their

onError

method
will be invoked with an

IllegalStateException

.

replacing

```java
public static <U>
HttpResponse.BodySubscriber
<U> replacing​(U value)
```

Returns a response subscriber which discards the response body. The
supplied value is the value that will be returned from

HttpResponse.body()

.

**Type Parameters:** U

- the type of the response body
**Parameters:** value

- the value to return from HttpResponse.body(), may be

null
**Returns:** a

BodySubscriber

---

#### replacing

public static <U>

HttpResponse.BodySubscriber

<U> replacing​(U value)

Returns a response subscriber which discards the response body. The
supplied value is the value that will be returned from

HttpResponse.body()

.

discarding

```java
public static
HttpResponse.BodySubscriber
<
Void
> discarding()
```

Returns a response subscriber which discards the response body.

**Returns:** a response body subscriber

---

#### discarding

public static

HttpResponse.BodySubscriber

<

Void

> discarding()

Returns a response subscriber which discards the response body.

buffering

```java
public static <T>
HttpResponse.BodySubscriber
<T> buffering​(
HttpResponse.BodySubscriber
<T> downstream,
int bufferSize)
```

Returns a

BodySubscriber

which buffers data before delivering
it to the given downstream subscriber. The subscriber guarantees to
deliver

bufferSize

bytes of data to each invocation of the
downstream's

onNext

method,
except for the final invocation, just before

onComplete

is invoked. The final
invocation of

onNext

may contain fewer than

bufferSize

bytes.

The returned subscriber delegates its

getBody()

method to the downstream subscriber.

**Type Parameters:** T

- the type of the response body
**Parameters:** downstream

- the downstream subscriber
**Parameters:** bufferSize

- the buffer size
**Returns:** a buffering body subscriber
**Throws:** IllegalArgumentException

- if

bufferSize <= 0

---

#### buffering

public static <T>

HttpResponse.BodySubscriber

<T> buffering​(

HttpResponse.BodySubscriber

<T> downstream,
int bufferSize)

Returns a

BodySubscriber

which buffers data before delivering
it to the given downstream subscriber. The subscriber guarantees to
deliver

bufferSize

bytes of data to each invocation of the
downstream's

onNext

method,
except for the final invocation, just before

onComplete

is invoked. The final
invocation of

onNext

may contain fewer than

bufferSize

bytes.

The returned subscriber delegates its

getBody()

method to the downstream subscriber.

The returned subscriber delegates its

getBody()

method to the downstream subscriber.

mapping

```java
public static <T,​U>
HttpResponse.BodySubscriber
<U> mapping​(
HttpResponse.BodySubscriber
<T> upstream,

Function
<? super T,​? extends U> mapper)
```

Returns a

BodySubscriber

whose response body value is that of
the result of applying the given function to the body object of the
given

upstream

BodySubscriber

.

The mapping function is executed using the client's

executor

, and can therefore be used to map any
response body type, including blocking

InputStream

, as shown
in the following example which uses a well-known JSON parser to
convert an

InputStream

into any annotated Java type.

For example:

```java
public static <W> BodySubscriber<W> asJSON(Class<W> targetType) {
BodySubscriber<InputStream> upstream = BodySubscribers.ofInputStream();

BodySubscriber<W> downstream = BodySubscribers.mapping(
upstream,
(InputStream is) -> {
try (InputStream stream = is) {
ObjectMapper objectMapper = new ObjectMapper();
return objectMapper.readValue(stream, targetType);
} catch (IOException e) {
throw new UncheckedIOException(e);
}
});
return downstream;
}
```

**Type Parameters:** T

- the upstream body type
**Type Parameters:** U

- the type of the body subscriber returned
**Parameters:** upstream

- the body subscriber to be mapped
**Parameters:** mapper

- the mapping function
**Returns:** a mapping body subscriber

---

#### mapping

public static <T,​U>

HttpResponse.BodySubscriber

<U> mapping​(

HttpResponse.BodySubscriber

<T> upstream,

Function

<? super T,​? extends U> mapper)

Returns a

BodySubscriber

whose response body value is that of
the result of applying the given function to the body object of the
given

upstream

BodySubscriber

.

The mapping function is executed using the client's

executor

, and can therefore be used to map any
response body type, including blocking

InputStream

, as shown
in the following example which uses a well-known JSON parser to
convert an

InputStream

into any annotated Java type.

For example:

```java
public static <W> BodySubscriber<W> asJSON(Class<W> targetType) {
BodySubscriber<InputStream> upstream = BodySubscribers.ofInputStream();

BodySubscriber<W> downstream = BodySubscribers.mapping(
upstream,
(InputStream is) -> {
try (InputStream stream = is) {
ObjectMapper objectMapper = new ObjectMapper();
return objectMapper.readValue(stream, targetType);
} catch (IOException e) {
throw new UncheckedIOException(e);
}
});
return downstream;
}
```

The mapping function is executed using the client's

executor

, and can therefore be used to map any
response body type, including blocking

InputStream

, as shown
in the following example which uses a well-known JSON parser to
convert an

InputStream

into any annotated Java type.

For example:

```java
public static <W> BodySubscriber<W> asJSON(Class<W> targetType) {
BodySubscriber<InputStream> upstream = BodySubscribers.ofInputStream();

BodySubscriber<W> downstream = BodySubscribers.mapping(
upstream,
(InputStream is) -> {
try (InputStream stream = is) {
ObjectMapper objectMapper = new ObjectMapper();
return objectMapper.readValue(stream, targetType);
} catch (IOException e) {
throw new UncheckedIOException(e);
}
});
return downstream;
}
```

For example:

```java
public static <W> BodySubscriber<W> asJSON(Class<W> targetType) {
BodySubscriber<InputStream> upstream = BodySubscribers.ofInputStream();

BodySubscriber<W> downstream = BodySubscribers.mapping(
upstream,
(InputStream is) -> {
try (InputStream stream = is) {
ObjectMapper objectMapper = new ObjectMapper();
return objectMapper.readValue(stream, targetType);
} catch (IOException e) {
throw new UncheckedIOException(e);
}
});
return downstream;
}
```

public static <W> BodySubscriber<W> asJSON(Class<W> targetType) {
BodySubscriber<InputStream> upstream = BodySubscribers.ofInputStream();

BodySubscriber<W> downstream = BodySubscribers.mapping(
upstream,
(InputStream is) -> {
try (InputStream stream = is) {
ObjectMapper objectMapper = new ObjectMapper();
return objectMapper.readValue(stream, targetType);
} catch (IOException e) {
throw new UncheckedIOException(e);
}
});
return downstream;
}

---

