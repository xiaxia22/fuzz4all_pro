# Class HttpRequest.BodyPublishers

**Source:** `java.net.http\java\net\http\HttpRequest.BodyPublishers.html`

### Class Description

```java
public static class
HttpRequest.BodyPublishers

extends
Object
```

Implementations of

BodyPublisher

that implement
various useful publishers, such as publishing the request body from a
String, or from a file.

The following are examples of using the predefined body publishers to
convert common high-level Java objects into a flow of data suitable for
sending as a request body:

```java
// Request body from a String
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.header("Content-Type", "text/plain; charset=UTF-8")
.POST(BodyPublishers.ofString("some body text"))
.build();

// Request body from a File
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.header("Content-Type", "application/json")
.POST(BodyPublishers.ofFile(Paths.get("file.json")))
.build();

// Request body from a byte array
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.POST(BodyPublishers.ofByteArray(new byte[] { ... }))
.build();
```

**Enclosing class:** HttpRequest

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
HttpRequest.BodyPublisher
fromPublisher​(
Flow.Publisher
<? extends
ByteBuffer
> publisher)

Returns a request body publisher whose body is retrieved from the
given

Flow.Publisher

. The returned request body publisher
has an unknown content length.

**Parameters:**
- publisher

- the publisher responsible for publishing the body

**Returns:**
- a BodyPublisher

**API Note:**
- This method can be used as an adapter between

BodyPublisher

and

Flow.Publisher

, where the amount of
request body that the publisher will publish is unknown.

---

#### public static
HttpRequest.BodyPublisher
fromPublisher​(
Flow.Publisher
<? extends
ByteBuffer
> publisher,
long contentLength)

Returns a request body publisher whose body is retrieved from the
given

Flow.Publisher

. The returned request body publisher
has the given content length.

The given

contentLength

is a positive number, that
represents the exact amount of bytes the

publisher

must
publish.

**Parameters:**
- publisher

- the publisher responsible for publishing the body
- contentLength

- a positive number representing the exact
amount of bytes the publisher will publish

**Returns:**
- a BodyPublisher

**Throws:**
- IllegalArgumentException

- if the content length is
non-positive

**API Note:**
- This method can be used as an adapter between

BodyPublisher

and

Flow.Publisher

, where the amount of
request body that the publisher will publish is known.

---

#### public static
HttpRequest.BodyPublisher
ofString​(
String
body)

Returns a request body publisher whose body is the given

String

, converted using the

UTF_8

character set.

**Parameters:**
- body

- the String containing the body

**Returns:**
- a BodyPublisher

---

#### public static
HttpRequest.BodyPublisher
ofString​(
String
s,

Charset
charset)

Returns a request body publisher whose body is the given

String

, converted using the given character set.

**Parameters:**
- s

- the String containing the body
- charset

- the character set to convert the string to bytes

**Returns:**
- a BodyPublisher

---

#### public static
HttpRequest.BodyPublisher
ofInputStream​(
Supplier
<? extends
InputStream
> streamSupplier)

A request body publisher that reads its data from an

InputStream

. A

Supplier

of

InputStream

is used in
case the request needs to be repeated, as the content is not buffered.
The

Supplier

may return

null

on subsequent attempts,
in which case the request fails.

**Parameters:**
- streamSupplier

- a Supplier of open InputStreams

**Returns:**
- a BodyPublisher

---

#### public static
HttpRequest.BodyPublisher
ofByteArray​(byte[] buf)

Returns a request body publisher whose body is the given byte array.

**Parameters:**
- buf

- the byte array containing the body

**Returns:**
- a BodyPublisher

---

#### public static
HttpRequest.BodyPublisher
ofByteArray​(byte[] buf,
int offset,
int length)

Returns a request body publisher whose body is the content of the
given byte array of

length

bytes starting from the specified

offset

.

**Parameters:**
- buf

- the byte array containing the body
- offset

- the offset of the first byte
- length

- the number of bytes to use

**Returns:**
- a BodyPublisher

**Throws:**
- IndexOutOfBoundsException

- if the sub-range is defined to be
out of bounds

---

#### public static
HttpRequest.BodyPublisher
ofFile​(
Path
path)
throws
FileNotFoundException

A request body publisher that takes data from the contents of a File.

Security manager permission checks are performed in this factory
method, when the

BodyPublisher

is created. Care must be taken
that the

BodyPublisher

is not shared with untrusted code.

**Parameters:**
- path

- the path to the file containing the body

**Returns:**
- a BodyPublisher

**Throws:**
- FileNotFoundException

- if the path is not found
- SecurityException

- if a security manager has been installed
and it denies

read access

to the given file

---

#### public static
HttpRequest.BodyPublisher
ofByteArrays​(
Iterable
<byte[]> iter)

A request body publisher that takes data from an

Iterable

of byte arrays. An

Iterable

is provided which supplies

Iterator

instances. Each attempt to send the request results
in one invocation of the

Iterable

.

**Parameters:**
- iter

- an Iterable of byte arrays

**Returns:**
- a BodyPublisher

---

#### public static
HttpRequest.BodyPublisher
noBody()

A request body publisher which sends no request body.

**Returns:**
- a BodyPublisher which completes immediately and sends
no request body.

---

### Additional Sections

#### Class HttpRequest.BodyPublishers

java.lang.Object

- java.net.http.HttpRequest.BodyPublishers

java.net.http.HttpRequest.BodyPublishers

**Enclosing class:** HttpRequest

```java
public static class
HttpRequest.BodyPublishers

extends
Object
```

Implementations of

BodyPublisher

that implement
various useful publishers, such as publishing the request body from a
String, or from a file.

The following are examples of using the predefined body publishers to
convert common high-level Java objects into a flow of data suitable for
sending as a request body:

```java
// Request body from a String
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.header("Content-Type", "text/plain; charset=UTF-8")
.POST(BodyPublishers.ofString("some body text"))
.build();

// Request body from a File
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.header("Content-Type", "application/json")
.POST(BodyPublishers.ofFile(Paths.get("file.json")))
.build();

// Request body from a byte array
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.POST(BodyPublishers.ofByteArray(new byte[] { ... }))
.build();
```

**Since:** 11

public static class

HttpRequest.BodyPublishers

extends

Object

Implementations of

BodyPublisher

that implement
various useful publishers, such as publishing the request body from a
String, or from a file.

The following are examples of using the predefined body publishers to
convert common high-level Java objects into a flow of data suitable for
sending as a request body:

```java
// Request body from a String
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.header("Content-Type", "text/plain; charset=UTF-8")
.POST(BodyPublishers.ofString("some body text"))
.build();

// Request body from a File
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.header("Content-Type", "application/json")
.POST(BodyPublishers.ofFile(Paths.get("file.json")))
.build();

// Request body from a byte array
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.POST(BodyPublishers.ofByteArray(new byte[] { ... }))
.build();
```

The following are examples of using the predefined body publishers to
convert common high-level Java objects into a flow of data suitable for
sending as a request body:

```java
// Request body from a String
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.header("Content-Type", "text/plain; charset=UTF-8")
.POST(BodyPublishers.ofString("some body text"))
.build();

// Request body from a File
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.header("Content-Type", "application/json")
.POST(BodyPublishers.ofFile(Paths.get("file.json")))
.build();

// Request body from a byte array
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.POST(BodyPublishers.ofByteArray(new byte[] { ... }))
.build();
```

// Request body from a String
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.header("Content-Type", "text/plain; charset=UTF-8")
.POST(BodyPublishers.ofString("some body text"))
.build();

// Request body from a File
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.header("Content-Type", "application/json")
.POST(BodyPublishers.ofFile(Paths.get("file.json")))
.build();

// Request body from a byte array
HttpRequest request = HttpRequest.newBuilder()
.uri(URI.create("https://foo.com/"))
.POST(BodyPublishers.ofByteArray(new byte[] { ... }))
.build();

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

HttpRequest.BodyPublisher

fromPublisher

​(

Flow.Publisher

<? extends

ByteBuffer

> publisher)

Returns a request body publisher whose body is retrieved from the
given

Flow.Publisher

.

static

HttpRequest.BodyPublisher

fromPublisher

​(

Flow.Publisher

<? extends

ByteBuffer

> publisher,
long contentLength)

Returns a request body publisher whose body is retrieved from the
given

Flow.Publisher

.

static

HttpRequest.BodyPublisher

noBody

()

A request body publisher which sends no request body.

static

HttpRequest.BodyPublisher

ofByteArray

​(byte[] buf)

Returns a request body publisher whose body is the given byte array.

static

HttpRequest.BodyPublisher

ofByteArray

​(byte[] buf,
int offset,
int length)

Returns a request body publisher whose body is the content of the
given byte array of

length

bytes starting from the specified

offset

.

static

HttpRequest.BodyPublisher

ofByteArrays

​(

Iterable

<byte[]> iter)

A request body publisher that takes data from an

Iterable

of byte arrays.

static

HttpRequest.BodyPublisher

ofFile

​(

Path

path)

A request body publisher that takes data from the contents of a File.

static

HttpRequest.BodyPublisher

ofInputStream

​(

Supplier

<? extends

InputStream

> streamSupplier)

A request body publisher that reads its data from an

InputStream

.

static

HttpRequest.BodyPublisher

ofString

​(

String

body)

Returns a request body publisher whose body is the given

String

, converted using the

UTF_8

character set.

static

HttpRequest.BodyPublisher

ofString

​(

String

s,

Charset

charset)

Returns a request body publisher whose body is the given

String

, converted using the given character set.

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

static

HttpRequest.BodyPublisher

fromPublisher

​(

Flow.Publisher

<? extends

ByteBuffer

> publisher)

Returns a request body publisher whose body is retrieved from the
given

Flow.Publisher

.

static

HttpRequest.BodyPublisher

fromPublisher

​(

Flow.Publisher

<? extends

ByteBuffer

> publisher,
long contentLength)

Returns a request body publisher whose body is retrieved from the
given

Flow.Publisher

.

static

HttpRequest.BodyPublisher

noBody

()

A request body publisher which sends no request body.

static

HttpRequest.BodyPublisher

ofByteArray

​(byte[] buf)

Returns a request body publisher whose body is the given byte array.

static

HttpRequest.BodyPublisher

ofByteArray

​(byte[] buf,
int offset,
int length)

Returns a request body publisher whose body is the content of the
given byte array of

length

bytes starting from the specified

offset

.

static

HttpRequest.BodyPublisher

ofByteArrays

​(

Iterable

<byte[]> iter)

A request body publisher that takes data from an

Iterable

of byte arrays.

static

HttpRequest.BodyPublisher

ofFile

​(

Path

path)

A request body publisher that takes data from the contents of a File.

static

HttpRequest.BodyPublisher

ofInputStream

​(

Supplier

<? extends

InputStream

> streamSupplier)

A request body publisher that reads its data from an

InputStream

.

static

HttpRequest.BodyPublisher

ofString

​(

String

body)

Returns a request body publisher whose body is the given

String

, converted using the

UTF_8

character set.

static

HttpRequest.BodyPublisher

ofString

​(

String

s,

Charset

charset)

Returns a request body publisher whose body is the given

String

, converted using the given character set.

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

Returns a request body publisher whose body is retrieved from the
given

Flow.Publisher

.

A request body publisher which sends no request body.

Returns a request body publisher whose body is the given byte array.

Returns a request body publisher whose body is the content of the
given byte array of

length

bytes starting from the specified

offset

.

A request body publisher that takes data from an

Iterable

of byte arrays.

A request body publisher that takes data from the contents of a File.

A request body publisher that reads its data from an

InputStream

.

Returns a request body publisher whose body is the given

String

, converted using the

UTF_8

character set.

Returns a request body publisher whose body is the given

String

, converted using the given character set.

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

- fromPublisher

```java
public static
HttpRequest.BodyPublisher
fromPublisher​(
Flow.Publisher
<? extends
ByteBuffer
> publisher)
```

Returns a request body publisher whose body is retrieved from the
given

Flow.Publisher

. The returned request body publisher
has an unknown content length.

**API Note:** This method can be used as an adapter between

BodyPublisher

and

Flow.Publisher

, where the amount of
request body that the publisher will publish is unknown.
**Parameters:** publisher

- the publisher responsible for publishing the body
**Returns:** a BodyPublisher

- fromPublisher

```java
public static
HttpRequest.BodyPublisher
fromPublisher​(
Flow.Publisher
<? extends
ByteBuffer
> publisher,
long contentLength)
```

Returns a request body publisher whose body is retrieved from the
given

Flow.Publisher

. The returned request body publisher
has the given content length.

The given

contentLength

is a positive number, that
represents the exact amount of bytes the

publisher

must
publish.

**API Note:** This method can be used as an adapter between

BodyPublisher

and

Flow.Publisher

, where the amount of
request body that the publisher will publish is known.
**Parameters:** publisher

- the publisher responsible for publishing the body
**Parameters:** contentLength

- a positive number representing the exact
amount of bytes the publisher will publish
**Returns:** a BodyPublisher
**Throws:** IllegalArgumentException

- if the content length is
non-positive

- ofString

```java
public static
HttpRequest.BodyPublisher
ofString​(
String
body)
```

Returns a request body publisher whose body is the given

String

, converted using the

UTF_8

character set.

**Parameters:** body

- the String containing the body
**Returns:** a BodyPublisher

- ofString

```java
public static
HttpRequest.BodyPublisher
ofString​(
String
s,

Charset
charset)
```

Returns a request body publisher whose body is the given

String

, converted using the given character set.

**Parameters:** s

- the String containing the body
**Parameters:** charset

- the character set to convert the string to bytes
**Returns:** a BodyPublisher

- ofInputStream

```java
public static
HttpRequest.BodyPublisher
ofInputStream​(
Supplier
<? extends
InputStream
> streamSupplier)
```

A request body publisher that reads its data from an

InputStream

. A

Supplier

of

InputStream

is used in
case the request needs to be repeated, as the content is not buffered.
The

Supplier

may return

null

on subsequent attempts,
in which case the request fails.

**Parameters:** streamSupplier

- a Supplier of open InputStreams
**Returns:** a BodyPublisher

- ofByteArray

```java
public static
HttpRequest.BodyPublisher
ofByteArray​(byte[] buf)
```

Returns a request body publisher whose body is the given byte array.

**Parameters:** buf

- the byte array containing the body
**Returns:** a BodyPublisher

- ofByteArray

```java
public static
HttpRequest.BodyPublisher
ofByteArray​(byte[] buf,
int offset,
int length)
```

Returns a request body publisher whose body is the content of the
given byte array of

length

bytes starting from the specified

offset

.

**Parameters:** buf

- the byte array containing the body
**Parameters:** offset

- the offset of the first byte
**Parameters:** length

- the number of bytes to use
**Returns:** a BodyPublisher
**Throws:** IndexOutOfBoundsException

- if the sub-range is defined to be
out of bounds

- ofFile

```java
public static
HttpRequest.BodyPublisher
ofFile​(
Path
path)
throws
FileNotFoundException
```

A request body publisher that takes data from the contents of a File.

Security manager permission checks are performed in this factory
method, when the

BodyPublisher

is created. Care must be taken
that the

BodyPublisher

is not shared with untrusted code.

**Parameters:** path

- the path to the file containing the body
**Returns:** a BodyPublisher
**Throws:** FileNotFoundException

- if the path is not found
**Throws:** SecurityException

- if a security manager has been installed
and it denies

read access

to the given file

- ofByteArrays

```java
public static
HttpRequest.BodyPublisher
ofByteArrays​(
Iterable
<byte[]> iter)
```

A request body publisher that takes data from an

Iterable

of byte arrays. An

Iterable

is provided which supplies

Iterator

instances. Each attempt to send the request results
in one invocation of the

Iterable

.

**Parameters:** iter

- an Iterable of byte arrays
**Returns:** a BodyPublisher

- noBody

```java
public static
HttpRequest.BodyPublisher
noBody()
```

A request body publisher which sends no request body.

**Returns:** a BodyPublisher which completes immediately and sends
no request body.

Method Detail

- fromPublisher

```java
public static
HttpRequest.BodyPublisher
fromPublisher​(
Flow.Publisher
<? extends
ByteBuffer
> publisher)
```

Returns a request body publisher whose body is retrieved from the
given

Flow.Publisher

. The returned request body publisher
has an unknown content length.

**API Note:** This method can be used as an adapter between

BodyPublisher

and

Flow.Publisher

, where the amount of
request body that the publisher will publish is unknown.
**Parameters:** publisher

- the publisher responsible for publishing the body
**Returns:** a BodyPublisher

- fromPublisher

```java
public static
HttpRequest.BodyPublisher
fromPublisher​(
Flow.Publisher
<? extends
ByteBuffer
> publisher,
long contentLength)
```

Returns a request body publisher whose body is retrieved from the
given

Flow.Publisher

. The returned request body publisher
has the given content length.

The given

contentLength

is a positive number, that
represents the exact amount of bytes the

publisher

must
publish.

**API Note:** This method can be used as an adapter between

BodyPublisher

and

Flow.Publisher

, where the amount of
request body that the publisher will publish is known.
**Parameters:** publisher

- the publisher responsible for publishing the body
**Parameters:** contentLength

- a positive number representing the exact
amount of bytes the publisher will publish
**Returns:** a BodyPublisher
**Throws:** IllegalArgumentException

- if the content length is
non-positive

- ofString

```java
public static
HttpRequest.BodyPublisher
ofString​(
String
body)
```

Returns a request body publisher whose body is the given

String

, converted using the

UTF_8

character set.

**Parameters:** body

- the String containing the body
**Returns:** a BodyPublisher

- ofString

```java
public static
HttpRequest.BodyPublisher
ofString​(
String
s,

Charset
charset)
```

Returns a request body publisher whose body is the given

String

, converted using the given character set.

**Parameters:** s

- the String containing the body
**Parameters:** charset

- the character set to convert the string to bytes
**Returns:** a BodyPublisher

- ofInputStream

```java
public static
HttpRequest.BodyPublisher
ofInputStream​(
Supplier
<? extends
InputStream
> streamSupplier)
```

A request body publisher that reads its data from an

InputStream

. A

Supplier

of

InputStream

is used in
case the request needs to be repeated, as the content is not buffered.
The

Supplier

may return

null

on subsequent attempts,
in which case the request fails.

**Parameters:** streamSupplier

- a Supplier of open InputStreams
**Returns:** a BodyPublisher

- ofByteArray

```java
public static
HttpRequest.BodyPublisher
ofByteArray​(byte[] buf)
```

Returns a request body publisher whose body is the given byte array.

**Parameters:** buf

- the byte array containing the body
**Returns:** a BodyPublisher

- ofByteArray

```java
public static
HttpRequest.BodyPublisher
ofByteArray​(byte[] buf,
int offset,
int length)
```

Returns a request body publisher whose body is the content of the
given byte array of

length

bytes starting from the specified

offset

.

**Parameters:** buf

- the byte array containing the body
**Parameters:** offset

- the offset of the first byte
**Parameters:** length

- the number of bytes to use
**Returns:** a BodyPublisher
**Throws:** IndexOutOfBoundsException

- if the sub-range is defined to be
out of bounds

- ofFile

```java
public static
HttpRequest.BodyPublisher
ofFile​(
Path
path)
throws
FileNotFoundException
```

A request body publisher that takes data from the contents of a File.

Security manager permission checks are performed in this factory
method, when the

BodyPublisher

is created. Care must be taken
that the

BodyPublisher

is not shared with untrusted code.

**Parameters:** path

- the path to the file containing the body
**Returns:** a BodyPublisher
**Throws:** FileNotFoundException

- if the path is not found
**Throws:** SecurityException

- if a security manager has been installed
and it denies

read access

to the given file

- ofByteArrays

```java
public static
HttpRequest.BodyPublisher
ofByteArrays​(
Iterable
<byte[]> iter)
```

A request body publisher that takes data from an

Iterable

of byte arrays. An

Iterable

is provided which supplies

Iterator

instances. Each attempt to send the request results
in one invocation of the

Iterable

.

**Parameters:** iter

- an Iterable of byte arrays
**Returns:** a BodyPublisher

- noBody

```java
public static
HttpRequest.BodyPublisher
noBody()
```

A request body publisher which sends no request body.

**Returns:** a BodyPublisher which completes immediately and sends
no request body.

---

#### Method Detail

fromPublisher

```java
public static
HttpRequest.BodyPublisher
fromPublisher​(
Flow.Publisher
<? extends
ByteBuffer
> publisher)
```

Returns a request body publisher whose body is retrieved from the
given

Flow.Publisher

. The returned request body publisher
has an unknown content length.

**API Note:** This method can be used as an adapter between

BodyPublisher

and

Flow.Publisher

, where the amount of
request body that the publisher will publish is unknown.
**Parameters:** publisher

- the publisher responsible for publishing the body
**Returns:** a BodyPublisher

---

#### fromPublisher

public static

HttpRequest.BodyPublisher

fromPublisher​(

Flow.Publisher

<? extends

ByteBuffer

> publisher)

Returns a request body publisher whose body is retrieved from the
given

Flow.Publisher

. The returned request body publisher
has an unknown content length.

fromPublisher

```java
public static
HttpRequest.BodyPublisher
fromPublisher​(
Flow.Publisher
<? extends
ByteBuffer
> publisher,
long contentLength)
```

Returns a request body publisher whose body is retrieved from the
given

Flow.Publisher

. The returned request body publisher
has the given content length.

The given

contentLength

is a positive number, that
represents the exact amount of bytes the

publisher

must
publish.

**API Note:** This method can be used as an adapter between

BodyPublisher

and

Flow.Publisher

, where the amount of
request body that the publisher will publish is known.
**Parameters:** publisher

- the publisher responsible for publishing the body
**Parameters:** contentLength

- a positive number representing the exact
amount of bytes the publisher will publish
**Returns:** a BodyPublisher
**Throws:** IllegalArgumentException

- if the content length is
non-positive

---

#### fromPublisher

public static

HttpRequest.BodyPublisher

fromPublisher​(

Flow.Publisher

<? extends

ByteBuffer

> publisher,
long contentLength)

Returns a request body publisher whose body is retrieved from the
given

Flow.Publisher

. The returned request body publisher
has the given content length.

The given

contentLength

is a positive number, that
represents the exact amount of bytes the

publisher

must
publish.

The given

contentLength

is a positive number, that
represents the exact amount of bytes the

publisher

must
publish.

ofString

```java
public static
HttpRequest.BodyPublisher
ofString​(
String
body)
```

Returns a request body publisher whose body is the given

String

, converted using the

UTF_8

character set.

**Parameters:** body

- the String containing the body
**Returns:** a BodyPublisher

---

#### ofString

public static

HttpRequest.BodyPublisher

ofString​(

String

body)

Returns a request body publisher whose body is the given

String

, converted using the

UTF_8

character set.

ofString

```java
public static
HttpRequest.BodyPublisher
ofString​(
String
s,

Charset
charset)
```

Returns a request body publisher whose body is the given

String

, converted using the given character set.

**Parameters:** s

- the String containing the body
**Parameters:** charset

- the character set to convert the string to bytes
**Returns:** a BodyPublisher

---

#### ofString

public static

HttpRequest.BodyPublisher

ofString​(

String

s,

Charset

charset)

Returns a request body publisher whose body is the given

String

, converted using the given character set.

ofInputStream

```java
public static
HttpRequest.BodyPublisher
ofInputStream​(
Supplier
<? extends
InputStream
> streamSupplier)
```

A request body publisher that reads its data from an

InputStream

. A

Supplier

of

InputStream

is used in
case the request needs to be repeated, as the content is not buffered.
The

Supplier

may return

null

on subsequent attempts,
in which case the request fails.

**Parameters:** streamSupplier

- a Supplier of open InputStreams
**Returns:** a BodyPublisher

---

#### ofInputStream

public static

HttpRequest.BodyPublisher

ofInputStream​(

Supplier

<? extends

InputStream

> streamSupplier)

A request body publisher that reads its data from an

InputStream

. A

Supplier

of

InputStream

is used in
case the request needs to be repeated, as the content is not buffered.
The

Supplier

may return

null

on subsequent attempts,
in which case the request fails.

ofByteArray

```java
public static
HttpRequest.BodyPublisher
ofByteArray​(byte[] buf)
```

Returns a request body publisher whose body is the given byte array.

**Parameters:** buf

- the byte array containing the body
**Returns:** a BodyPublisher

---

#### ofByteArray

public static

HttpRequest.BodyPublisher

ofByteArray​(byte[] buf)

Returns a request body publisher whose body is the given byte array.

ofByteArray

```java
public static
HttpRequest.BodyPublisher
ofByteArray​(byte[] buf,
int offset,
int length)
```

Returns a request body publisher whose body is the content of the
given byte array of

length

bytes starting from the specified

offset

.

**Parameters:** buf

- the byte array containing the body
**Parameters:** offset

- the offset of the first byte
**Parameters:** length

- the number of bytes to use
**Returns:** a BodyPublisher
**Throws:** IndexOutOfBoundsException

- if the sub-range is defined to be
out of bounds

---

#### ofByteArray

public static

HttpRequest.BodyPublisher

ofByteArray​(byte[] buf,
int offset,
int length)

Returns a request body publisher whose body is the content of the
given byte array of

length

bytes starting from the specified

offset

.

ofFile

```java
public static
HttpRequest.BodyPublisher
ofFile​(
Path
path)
throws
FileNotFoundException
```

A request body publisher that takes data from the contents of a File.

Security manager permission checks are performed in this factory
method, when the

BodyPublisher

is created. Care must be taken
that the

BodyPublisher

is not shared with untrusted code.

**Parameters:** path

- the path to the file containing the body
**Returns:** a BodyPublisher
**Throws:** FileNotFoundException

- if the path is not found
**Throws:** SecurityException

- if a security manager has been installed
and it denies

read access

to the given file

---

#### ofFile

public static

HttpRequest.BodyPublisher

ofFile​(

Path

path)
throws

FileNotFoundException

A request body publisher that takes data from the contents of a File.

Security manager permission checks are performed in this factory
method, when the

BodyPublisher

is created. Care must be taken
that the

BodyPublisher

is not shared with untrusted code.

Security manager permission checks are performed in this factory
method, when the

BodyPublisher

is created. Care must be taken
that the

BodyPublisher

is not shared with untrusted code.

ofByteArrays

```java
public static
HttpRequest.BodyPublisher
ofByteArrays​(
Iterable
<byte[]> iter)
```

A request body publisher that takes data from an

Iterable

of byte arrays. An

Iterable

is provided which supplies

Iterator

instances. Each attempt to send the request results
in one invocation of the

Iterable

.

**Parameters:** iter

- an Iterable of byte arrays
**Returns:** a BodyPublisher

---

#### ofByteArrays

public static

HttpRequest.BodyPublisher

ofByteArrays​(

Iterable

<byte[]> iter)

A request body publisher that takes data from an

Iterable

of byte arrays. An

Iterable

is provided which supplies

Iterator

instances. Each attempt to send the request results
in one invocation of the

Iterable

.

noBody

```java
public static
HttpRequest.BodyPublisher
noBody()
```

A request body publisher which sends no request body.

**Returns:** a BodyPublisher which completes immediately and sends
no request body.

---

#### noBody

public static

HttpRequest.BodyPublisher

noBody()

A request body publisher which sends no request body.

---

