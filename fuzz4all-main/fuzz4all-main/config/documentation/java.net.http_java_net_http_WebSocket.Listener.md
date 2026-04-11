# Interface WebSocket.Listener

**Source:** `java.net.http\java\net\http\WebSocket.Listener.html`

### Class Description

```java
public static interface
WebSocket.Listener
```

The receiving interface of

WebSocket

.

A

WebSocket

invokes methods of the associated listener
passing itself as an argument. These methods are invoked in a thread-safe
manner, such that the next invocation may start only after the previous
one has finished.

When data has been received, the

WebSocket

invokes a receive
method. Methods

onText

,

onBinary

,

onPing

and

onPong

must return a

CompletionStage

that completes once
the message has been received by the listener. If a listener's method
returns

null

rather than a

CompletionStage

,

WebSocket

will behave as if the listener returned a

CompletionStage

that is already completed normally.

An

IOException

raised in

WebSocket

will result in an
invocation of

onError

with that exception (if the input is not
closed). Unless otherwise stated if the listener's method throws an
exception or a

CompletionStage

returned from a method completes
exceptionally, the WebSocket will invoke

onError

with this
exception.

**Enclosing interface:** WebSocket

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### default void onOpen​(
WebSocket
webSocket)

A

WebSocket

has been connected.

This is the initial invocation and it is made once. It is
typically used to make a request for more invocations.

**Parameters:**
- webSocket

- the WebSocket that has been connected

**Implementation Requirements:**
- The default implementation is equivalent to:

```java
webSocket.request(1);
```

---

#### default
CompletionStage
<?> onText​(
WebSocket
webSocket,

CharSequence
data,
boolean last)

A textual data has been received.

Return a

CompletionStage

which will be used by the

WebSocket

as an indication it may reclaim the

CharSequence

. Do not access the

CharSequence

after
this

CompletionStage

has completed.

**Parameters:**
- webSocket

- the WebSocket on which the data has been received
- data

- the data
- last

- whether this invocation completes the message

**Returns:**
- a

CompletionStage

which completes when the

CharSequence

may be reclaimed; or

null

if it may be
reclaimed immediately

**Implementation Requirements:**
- The default implementation is equivalent to:

```java
webSocket.request(1);
return null;
```

**Implementation Note:**
- The

data

is always a legal UTF-16 sequence.

---

#### default
CompletionStage
<?> onBinary​(
WebSocket
webSocket,

ByteBuffer
data,
boolean last)

A binary data has been received.

This data is located in bytes from the buffer's position to its
limit.

Return a

CompletionStage

which will be used by the

WebSocket

as an indication it may reclaim the

ByteBuffer

. Do not access the

ByteBuffer

after
this

CompletionStage

has completed.

**Parameters:**
- webSocket

- the WebSocket on which the data has been received
- data

- the data
- last

- whether this invocation completes the message

**Returns:**
- a

CompletionStage

which completes when the

ByteBuffer

may be reclaimed; or

null

if it may be
reclaimed immediately

**Implementation Requirements:**
- The default implementation is equivalent to:

```java
webSocket.request(1);
return null;
```

---

#### default
CompletionStage
<?> onPing​(
WebSocket
webSocket,

ByteBuffer
message)

A Ping message has been received.

As guaranteed by the WebSocket Protocol, the message consists of
not more than

125

bytes. These bytes are located from the
buffer's position to its limit.

Given that the WebSocket implementation will automatically send a
reciprocal pong when a ping is received, it is rarely required to
send a pong message explicitly when a ping is received.

Return a

CompletionStage

which will be used by the

WebSocket

as a signal it may reclaim the

ByteBuffer

. Do not access the

ByteBuffer

after
this

CompletionStage

has completed.

**Parameters:**
- webSocket

- the WebSocket on which the message has been received
- message

- the message

**Returns:**
- a

CompletionStage

which completes when the

ByteBuffer

may be reclaimed; or

null

if it may be
reclaimed immediately

**Implementation Requirements:**
- The default implementation is equivalent to:

```java
webSocket.request(1);
return null;
```

---

#### default
CompletionStage
<?> onPong​(
WebSocket
webSocket,

ByteBuffer
message)

A Pong message has been received.

As guaranteed by the WebSocket Protocol, the message consists of
not more than

125

bytes. These bytes are located from the
buffer's position to its limit.

Return a

CompletionStage

which will be used by the

WebSocket

as a signal it may reclaim the

ByteBuffer

. Do not access the

ByteBuffer

after
this

CompletionStage

has completed.

**Parameters:**
- webSocket

- the WebSocket on which the message has been received
- message

- the message

**Returns:**
- a

CompletionStage

which completes when the

ByteBuffer

may be reclaimed; or

null

if it may be
reclaimed immediately

**Implementation Requirements:**
- The default implementation is equivalent to:

```java
webSocket.request(1);
return null;
```

---

#### default
CompletionStage
<?> onClose​(
WebSocket
webSocket,
int statusCode,

String
reason)

Receives a Close message indicating the WebSocket's input has been
closed.

This is the last invocation from the specified

WebSocket

.
By the time this invocation begins the WebSocket's input will have
been closed.

A Close message consists of a status code and a reason for
closing. The status code is an integer from the range

1000 <= code <= 65535

. The

reason

is a string which
has a UTF-8 representation not longer than

123

bytes.

If the WebSocket's output is not already closed, the

CompletionStage

returned by this method will be used as an
indication that the WebSocket's output may be closed. The WebSocket
will close its output at the earliest of completion of the returned

CompletionStage

or invoking either of the

sendClose

or

abort

methods.

**Parameters:**
- webSocket

- the WebSocket on which the message has been received
- statusCode

- the status code
- reason

- the reason

**Returns:**
- a

CompletionStage

which completes when the

WebSocket

may be closed; or

null

if it may be
closed immediately

**API Note:**
- Returning a

CompletionStage

that never completes,
effectively disables the reciprocating closure of the output.

To specify a custom closure code or reason code the

sendClose

method may be invoked from inside the

onClose

invocation:

```java
public CompletionStage<?> onClose(WebSocket webSocket,
int statusCode,
String reason) {
webSocket.sendClose(CUSTOM_STATUS_CODE, CUSTOM_REASON);
return new CompletableFuture<Void>();
}
```

**Implementation Requirements:**
- The default implementation of this method returns

null

, indicating that the output should be closed
immediately.

---

#### default void onError​(
WebSocket
webSocket,

Throwable
error)

An error has occurred.

This is the last invocation from the specified WebSocket. By the
time this invocation begins both the WebSocket's input and output
will have been closed. A WebSocket may invoke this method on the
associated listener at any time after it has invoked

onOpen

,
regardless of whether or not any invocations have been requested from
the WebSocket.

If an exception is thrown from this method, resulting behavior is
undefined.

**Parameters:**
- webSocket

- the WebSocket on which the error has occurred
- error

- the error

---

### Additional Sections

#### Interface WebSocket.Listener

**Enclosing interface:** WebSocket

```java
public static interface
WebSocket.Listener
```

The receiving interface of

WebSocket

.

A

WebSocket

invokes methods of the associated listener
passing itself as an argument. These methods are invoked in a thread-safe
manner, such that the next invocation may start only after the previous
one has finished.

When data has been received, the

WebSocket

invokes a receive
method. Methods

onText

,

onBinary

,

onPing

and

onPong

must return a

CompletionStage

that completes once
the message has been received by the listener. If a listener's method
returns

null

rather than a

CompletionStage

,

WebSocket

will behave as if the listener returned a

CompletionStage

that is already completed normally.

An

IOException

raised in

WebSocket

will result in an
invocation of

onError

with that exception (if the input is not
closed). Unless otherwise stated if the listener's method throws an
exception or a

CompletionStage

returned from a method completes
exceptionally, the WebSocket will invoke

onError

with this
exception.

**API Note:** The strict sequential order of invocations from

WebSocket

to

Listener

means, in particular, that the

Listener

's methods are treated as non-reentrant. This means that

Listener

implementations do not need to be concerned with
possible recursion or the order in which they invoke

WebSocket.request

in relation to their processing logic.

Careful attention may be required if a listener is associated
with more than a single

WebSocket

. In this case invocations
related to different instances of

WebSocket

may not be ordered
and may even happen concurrently.

CompletionStage

s returned from the receive methods have
nothing to do with the

counter of invocations

.
Namely, a

CompletionStage

does not have to be completed in order
to receive more invocations of the listener's methods.
Here is an example of a listener that requests invocations, one at a
time, until a complete message has been accumulated, then processes
the result, and completes the

CompletionStage

:

```java
WebSocket.Listener listener = new WebSocket.Listener() {

List<CharSequence> parts = new ArrayList<>();
CompletableFuture<?> accumulatedMessage = new CompletableFuture<>();

public CompletionStage<?> onText(WebSocket webSocket,
CharSequence message,
boolean last) {
parts.add(message);
webSocket.request(1);
if (last) {
processWholeText(parts);
parts = new ArrayList<>();
accumulatedMessage.complete(null);
CompletionStage<?> cf = accumulatedMessage;
accumulatedMessage = new CompletableFuture<>();
return cf;
}
return accumulatedMessage;
}
...
}
```
**Since:** 11

public static interface

WebSocket.Listener

The receiving interface of

WebSocket

.

A

WebSocket

invokes methods of the associated listener
passing itself as an argument. These methods are invoked in a thread-safe
manner, such that the next invocation may start only after the previous
one has finished.

When data has been received, the

WebSocket

invokes a receive
method. Methods

onText

,

onBinary

,

onPing

and

onPong

must return a

CompletionStage

that completes once
the message has been received by the listener. If a listener's method
returns

null

rather than a

CompletionStage

,

WebSocket

will behave as if the listener returned a

CompletionStage

that is already completed normally.

An

IOException

raised in

WebSocket

will result in an
invocation of

onError

with that exception (if the input is not
closed). Unless otherwise stated if the listener's method throws an
exception or a

CompletionStage

returned from a method completes
exceptionally, the WebSocket will invoke

onError

with this
exception.

A

WebSocket

invokes methods of the associated listener
passing itself as an argument. These methods are invoked in a thread-safe
manner, such that the next invocation may start only after the previous
one has finished.

When data has been received, the

WebSocket

invokes a receive
method. Methods

onText

,

onBinary

,

onPing

and

onPong

must return a

CompletionStage

that completes once
the message has been received by the listener. If a listener's method
returns

null

rather than a

CompletionStage

,

WebSocket

will behave as if the listener returned a

CompletionStage

that is already completed normally.

An

IOException

raised in

WebSocket

will result in an
invocation of

onError

with that exception (if the input is not
closed). Unless otherwise stated if the listener's method throws an
exception or a

CompletionStage

returned from a method completes
exceptionally, the WebSocket will invoke

onError

with this
exception.

When data has been received, the

WebSocket

invokes a receive
method. Methods

onText

,

onBinary

,

onPing

and

onPong

must return a

CompletionStage

that completes once
the message has been received by the listener. If a listener's method
returns

null

rather than a

CompletionStage

,

WebSocket

will behave as if the listener returned a

CompletionStage

that is already completed normally.

An

IOException

raised in

WebSocket

will result in an
invocation of

onError

with that exception (if the input is not
closed). Unless otherwise stated if the listener's method throws an
exception or a

CompletionStage

returned from a method completes
exceptionally, the WebSocket will invoke

onError

with this
exception.

An

IOException

raised in

WebSocket

will result in an
invocation of

onError

with that exception (if the input is not
closed). Unless otherwise stated if the listener's method throws an
exception or a

CompletionStage

returned from a method completes
exceptionally, the WebSocket will invoke

onError

with this
exception.

Careful attention may be required if a listener is associated
with more than a single

WebSocket

. In this case invocations
related to different instances of

WebSocket

may not be ordered
and may even happen concurrently.

CompletionStage

s returned from the receive methods have
nothing to do with the

counter of invocations

.
Namely, a

CompletionStage

does not have to be completed in order
to receive more invocations of the listener's methods.
Here is an example of a listener that requests invocations, one at a
time, until a complete message has been accumulated, then processes
the result, and completes the

CompletionStage

:

```java
WebSocket.Listener listener = new WebSocket.Listener() {

List<CharSequence> parts = new ArrayList<>();
CompletableFuture<?> accumulatedMessage = new CompletableFuture<>();

public CompletionStage<?> onText(WebSocket webSocket,
CharSequence message,
boolean last) {
parts.add(message);
webSocket.request(1);
if (last) {
processWholeText(parts);
parts = new ArrayList<>();
accumulatedMessage.complete(null);
CompletionStage<?> cf = accumulatedMessage;
accumulatedMessage = new CompletableFuture<>();
return cf;
}
return accumulatedMessage;
}
...
}
```

CompletionStage

s returned from the receive methods have
nothing to do with the

counter of invocations

.
Namely, a

CompletionStage

does not have to be completed in order
to receive more invocations of the listener's methods.
Here is an example of a listener that requests invocations, one at a
time, until a complete message has been accumulated, then processes
the result, and completes the

CompletionStage

:

```java
WebSocket.Listener listener = new WebSocket.Listener() {

List<CharSequence> parts = new ArrayList<>();
CompletableFuture<?> accumulatedMessage = new CompletableFuture<>();

public CompletionStage<?> onText(WebSocket webSocket,
CharSequence message,
boolean last) {
parts.add(message);
webSocket.request(1);
if (last) {
processWholeText(parts);
parts = new ArrayList<>();
accumulatedMessage.complete(null);
CompletionStage<?> cf = accumulatedMessage;
accumulatedMessage = new CompletableFuture<>();
return cf;
}
return accumulatedMessage;
}
...
}
```

WebSocket.Listener listener = new WebSocket.Listener() {

List<CharSequence> parts = new ArrayList<>();
CompletableFuture<?> accumulatedMessage = new CompletableFuture<>();

public CompletionStage<?> onText(WebSocket webSocket,
CharSequence message,
boolean last) {
parts.add(message);
webSocket.request(1);
if (last) {
processWholeText(parts);
parts = new ArrayList<>();
accumulatedMessage.complete(null);
CompletionStage<?> cf = accumulatedMessage;
accumulatedMessage = new CompletableFuture<>();
return cf;
}
return accumulatedMessage;
}
...
}

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Default Methods

Modifier and Type

Method

Description

default

CompletionStage

<?>

onBinary

​(

WebSocket

webSocket,

ByteBuffer

data,
boolean last)

A binary data has been received.

default

CompletionStage

<?>

onClose

​(

WebSocket

webSocket,
int statusCode,

String

reason)

Receives a Close message indicating the WebSocket's input has been
closed.

default void

onError

​(

WebSocket

webSocket,

Throwable

error)

An error has occurred.

default void

onOpen

​(

WebSocket

webSocket)

A

WebSocket

has been connected.

default

CompletionStage

<?>

onPing

​(

WebSocket

webSocket,

ByteBuffer

message)

A Ping message has been received.

default

CompletionStage

<?>

onPong

​(

WebSocket

webSocket,

ByteBuffer

message)

A Pong message has been received.

default

CompletionStage

<?>

onText

​(

WebSocket

webSocket,

CharSequence

data,
boolean last)

A textual data has been received.

Method Summary

All Methods

Instance Methods

Default Methods

Modifier and Type

Method

Description

default

CompletionStage

<?>

onBinary

​(

WebSocket

webSocket,

ByteBuffer

data,
boolean last)

A binary data has been received.

default

CompletionStage

<?>

onClose

​(

WebSocket

webSocket,
int statusCode,

String

reason)

Receives a Close message indicating the WebSocket's input has been
closed.

default void

onError

​(

WebSocket

webSocket,

Throwable

error)

An error has occurred.

default void

onOpen

​(

WebSocket

webSocket)

A

WebSocket

has been connected.

default

CompletionStage

<?>

onPing

​(

WebSocket

webSocket,

ByteBuffer

message)

A Ping message has been received.

default

CompletionStage

<?>

onPong

​(

WebSocket

webSocket,

ByteBuffer

message)

A Pong message has been received.

default

CompletionStage

<?>

onText

​(

WebSocket

webSocket,

CharSequence

data,
boolean last)

A textual data has been received.

---

#### Method Summary

A binary data has been received.

Receives a Close message indicating the WebSocket's input has been
closed.

An error has occurred.

A

WebSocket

has been connected.

A Ping message has been received.

A Pong message has been received.

A textual data has been received.

============ METHOD DETAIL ==========

- Method Detail

- onOpen

```java
default void onOpen​(
WebSocket
webSocket)
```

A

WebSocket

has been connected.

This is the initial invocation and it is made once. It is
typically used to make a request for more invocations.

**Implementation Requirements:** The default implementation is equivalent to:

```java
webSocket.request(1);
```
**Parameters:** webSocket

- the WebSocket that has been connected

- onText

```java
default
CompletionStage
<?> onText​(
WebSocket
webSocket,

CharSequence
data,
boolean last)
```

A textual data has been received.

Return a

CompletionStage

which will be used by the

WebSocket

as an indication it may reclaim the

CharSequence

. Do not access the

CharSequence

after
this

CompletionStage

has completed.

**Implementation Requirements:** The default implementation is equivalent to:

```java
webSocket.request(1);
return null;
```
**Implementation Note:** The

data

is always a legal UTF-16 sequence.
**Parameters:** webSocket

- the WebSocket on which the data has been received
**Parameters:** data

- the data
**Parameters:** last

- whether this invocation completes the message
**Returns:** a

CompletionStage

which completes when the

CharSequence

may be reclaimed; or

null

if it may be
reclaimed immediately

- onBinary

```java
default
CompletionStage
<?> onBinary​(
WebSocket
webSocket,

ByteBuffer
data,
boolean last)
```

A binary data has been received.

This data is located in bytes from the buffer's position to its
limit.

Return a

CompletionStage

which will be used by the

WebSocket

as an indication it may reclaim the

ByteBuffer

. Do not access the

ByteBuffer

after
this

CompletionStage

has completed.

**Implementation Requirements:** The default implementation is equivalent to:

```java
webSocket.request(1);
return null;
```
**Parameters:** webSocket

- the WebSocket on which the data has been received
**Parameters:** data

- the data
**Parameters:** last

- whether this invocation completes the message
**Returns:** a

CompletionStage

which completes when the

ByteBuffer

may be reclaimed; or

null

if it may be
reclaimed immediately

- onPing

```java
default
CompletionStage
<?> onPing​(
WebSocket
webSocket,

ByteBuffer
message)
```

A Ping message has been received.

As guaranteed by the WebSocket Protocol, the message consists of
not more than

125

bytes. These bytes are located from the
buffer's position to its limit.

Given that the WebSocket implementation will automatically send a
reciprocal pong when a ping is received, it is rarely required to
send a pong message explicitly when a ping is received.

Return a

CompletionStage

which will be used by the

WebSocket

as a signal it may reclaim the

ByteBuffer

. Do not access the

ByteBuffer

after
this

CompletionStage

has completed.

**Implementation Requirements:** The default implementation is equivalent to:

```java
webSocket.request(1);
return null;
```
**Parameters:** webSocket

- the WebSocket on which the message has been received
**Parameters:** message

- the message
**Returns:** a

CompletionStage

which completes when the

ByteBuffer

may be reclaimed; or

null

if it may be
reclaimed immediately

- onPong

```java
default
CompletionStage
<?> onPong​(
WebSocket
webSocket,

ByteBuffer
message)
```

A Pong message has been received.

As guaranteed by the WebSocket Protocol, the message consists of
not more than

125

bytes. These bytes are located from the
buffer's position to its limit.

Return a

CompletionStage

which will be used by the

WebSocket

as a signal it may reclaim the

ByteBuffer

. Do not access the

ByteBuffer

after
this

CompletionStage

has completed.

**Implementation Requirements:** The default implementation is equivalent to:

```java
webSocket.request(1);
return null;
```
**Parameters:** webSocket

- the WebSocket on which the message has been received
**Parameters:** message

- the message
**Returns:** a

CompletionStage

which completes when the

ByteBuffer

may be reclaimed; or

null

if it may be
reclaimed immediately

- onClose

```java
default
CompletionStage
<?> onClose​(
WebSocket
webSocket,
int statusCode,

String
reason)
```

Receives a Close message indicating the WebSocket's input has been
closed.

This is the last invocation from the specified

WebSocket

.
By the time this invocation begins the WebSocket's input will have
been closed.

A Close message consists of a status code and a reason for
closing. The status code is an integer from the range

1000 <= code <= 65535

. The

reason

is a string which
has a UTF-8 representation not longer than

123

bytes.

If the WebSocket's output is not already closed, the

CompletionStage

returned by this method will be used as an
indication that the WebSocket's output may be closed. The WebSocket
will close its output at the earliest of completion of the returned

CompletionStage

or invoking either of the

sendClose

or

abort

methods.

**API Note:** Returning a

CompletionStage

that never completes,
effectively disables the reciprocating closure of the output.

To specify a custom closure code or reason code the

sendClose

method may be invoked from inside the

onClose

invocation:

```java
public CompletionStage<?> onClose(WebSocket webSocket,
int statusCode,
String reason) {
webSocket.sendClose(CUSTOM_STATUS_CODE, CUSTOM_REASON);
return new CompletableFuture<Void>();
}
```
**Implementation Requirements:** The default implementation of this method returns

null

, indicating that the output should be closed
immediately.
**Parameters:** webSocket

- the WebSocket on which the message has been received
**Parameters:** statusCode

- the status code
**Parameters:** reason

- the reason
**Returns:** a

CompletionStage

which completes when the

WebSocket

may be closed; or

null

if it may be
closed immediately

- onError

```java
default void onError​(
WebSocket
webSocket,

Throwable
error)
```

An error has occurred.

This is the last invocation from the specified WebSocket. By the
time this invocation begins both the WebSocket's input and output
will have been closed. A WebSocket may invoke this method on the
associated listener at any time after it has invoked

onOpen

,
regardless of whether or not any invocations have been requested from
the WebSocket.

If an exception is thrown from this method, resulting behavior is
undefined.

**Parameters:** webSocket

- the WebSocket on which the error has occurred
**Parameters:** error

- the error

Method Detail

- onOpen

```java
default void onOpen​(
WebSocket
webSocket)
```

A

WebSocket

has been connected.

This is the initial invocation and it is made once. It is
typically used to make a request for more invocations.

**Implementation Requirements:** The default implementation is equivalent to:

```java
webSocket.request(1);
```
**Parameters:** webSocket

- the WebSocket that has been connected

- onText

```java
default
CompletionStage
<?> onText​(
WebSocket
webSocket,

CharSequence
data,
boolean last)
```

A textual data has been received.

Return a

CompletionStage

which will be used by the

WebSocket

as an indication it may reclaim the

CharSequence

. Do not access the

CharSequence

after
this

CompletionStage

has completed.

**Implementation Requirements:** The default implementation is equivalent to:

```java
webSocket.request(1);
return null;
```
**Implementation Note:** The

data

is always a legal UTF-16 sequence.
**Parameters:** webSocket

- the WebSocket on which the data has been received
**Parameters:** data

- the data
**Parameters:** last

- whether this invocation completes the message
**Returns:** a

CompletionStage

which completes when the

CharSequence

may be reclaimed; or

null

if it may be
reclaimed immediately

- onBinary

```java
default
CompletionStage
<?> onBinary​(
WebSocket
webSocket,

ByteBuffer
data,
boolean last)
```

A binary data has been received.

This data is located in bytes from the buffer's position to its
limit.

Return a

CompletionStage

which will be used by the

WebSocket

as an indication it may reclaim the

ByteBuffer

. Do not access the

ByteBuffer

after
this

CompletionStage

has completed.

**Implementation Requirements:** The default implementation is equivalent to:

```java
webSocket.request(1);
return null;
```
**Parameters:** webSocket

- the WebSocket on which the data has been received
**Parameters:** data

- the data
**Parameters:** last

- whether this invocation completes the message
**Returns:** a

CompletionStage

which completes when the

ByteBuffer

may be reclaimed; or

null

if it may be
reclaimed immediately

- onPing

```java
default
CompletionStage
<?> onPing​(
WebSocket
webSocket,

ByteBuffer
message)
```

A Ping message has been received.

As guaranteed by the WebSocket Protocol, the message consists of
not more than

125

bytes. These bytes are located from the
buffer's position to its limit.

Given that the WebSocket implementation will automatically send a
reciprocal pong when a ping is received, it is rarely required to
send a pong message explicitly when a ping is received.

Return a

CompletionStage

which will be used by the

WebSocket

as a signal it may reclaim the

ByteBuffer

. Do not access the

ByteBuffer

after
this

CompletionStage

has completed.

**Implementation Requirements:** The default implementation is equivalent to:

```java
webSocket.request(1);
return null;
```
**Parameters:** webSocket

- the WebSocket on which the message has been received
**Parameters:** message

- the message
**Returns:** a

CompletionStage

which completes when the

ByteBuffer

may be reclaimed; or

null

if it may be
reclaimed immediately

- onPong

```java
default
CompletionStage
<?> onPong​(
WebSocket
webSocket,

ByteBuffer
message)
```

A Pong message has been received.

As guaranteed by the WebSocket Protocol, the message consists of
not more than

125

bytes. These bytes are located from the
buffer's position to its limit.

Return a

CompletionStage

which will be used by the

WebSocket

as a signal it may reclaim the

ByteBuffer

. Do not access the

ByteBuffer

after
this

CompletionStage

has completed.

**Implementation Requirements:** The default implementation is equivalent to:

```java
webSocket.request(1);
return null;
```
**Parameters:** webSocket

- the WebSocket on which the message has been received
**Parameters:** message

- the message
**Returns:** a

CompletionStage

which completes when the

ByteBuffer

may be reclaimed; or

null

if it may be
reclaimed immediately

- onClose

```java
default
CompletionStage
<?> onClose​(
WebSocket
webSocket,
int statusCode,

String
reason)
```

Receives a Close message indicating the WebSocket's input has been
closed.

This is the last invocation from the specified

WebSocket

.
By the time this invocation begins the WebSocket's input will have
been closed.

A Close message consists of a status code and a reason for
closing. The status code is an integer from the range

1000 <= code <= 65535

. The

reason

is a string which
has a UTF-8 representation not longer than

123

bytes.

If the WebSocket's output is not already closed, the

CompletionStage

returned by this method will be used as an
indication that the WebSocket's output may be closed. The WebSocket
will close its output at the earliest of completion of the returned

CompletionStage

or invoking either of the

sendClose

or

abort

methods.

**API Note:** Returning a

CompletionStage

that never completes,
effectively disables the reciprocating closure of the output.

To specify a custom closure code or reason code the

sendClose

method may be invoked from inside the

onClose

invocation:

```java
public CompletionStage<?> onClose(WebSocket webSocket,
int statusCode,
String reason) {
webSocket.sendClose(CUSTOM_STATUS_CODE, CUSTOM_REASON);
return new CompletableFuture<Void>();
}
```
**Implementation Requirements:** The default implementation of this method returns

null

, indicating that the output should be closed
immediately.
**Parameters:** webSocket

- the WebSocket on which the message has been received
**Parameters:** statusCode

- the status code
**Parameters:** reason

- the reason
**Returns:** a

CompletionStage

which completes when the

WebSocket

may be closed; or

null

if it may be
closed immediately

- onError

```java
default void onError​(
WebSocket
webSocket,

Throwable
error)
```

An error has occurred.

This is the last invocation from the specified WebSocket. By the
time this invocation begins both the WebSocket's input and output
will have been closed. A WebSocket may invoke this method on the
associated listener at any time after it has invoked

onOpen

,
regardless of whether or not any invocations have been requested from
the WebSocket.

If an exception is thrown from this method, resulting behavior is
undefined.

**Parameters:** webSocket

- the WebSocket on which the error has occurred
**Parameters:** error

- the error

---

#### Method Detail

onOpen

```java
default void onOpen​(
WebSocket
webSocket)
```

A

WebSocket

has been connected.

This is the initial invocation and it is made once. It is
typically used to make a request for more invocations.

**Implementation Requirements:** The default implementation is equivalent to:

```java
webSocket.request(1);
```
**Parameters:** webSocket

- the WebSocket that has been connected

---

#### onOpen

default void onOpen​(

WebSocket

webSocket)

A

WebSocket

has been connected.

This is the initial invocation and it is made once. It is
typically used to make a request for more invocations.

This is the initial invocation and it is made once. It is
typically used to make a request for more invocations.

webSocket.request(1);

onText

```java
default
CompletionStage
<?> onText​(
WebSocket
webSocket,

CharSequence
data,
boolean last)
```

A textual data has been received.

Return a

CompletionStage

which will be used by the

WebSocket

as an indication it may reclaim the

CharSequence

. Do not access the

CharSequence

after
this

CompletionStage

has completed.

**Implementation Requirements:** The default implementation is equivalent to:

```java
webSocket.request(1);
return null;
```
**Implementation Note:** The

data

is always a legal UTF-16 sequence.
**Parameters:** webSocket

- the WebSocket on which the data has been received
**Parameters:** data

- the data
**Parameters:** last

- whether this invocation completes the message
**Returns:** a

CompletionStage

which completes when the

CharSequence

may be reclaimed; or

null

if it may be
reclaimed immediately

---

#### onText

default

CompletionStage

<?> onText​(

WebSocket

webSocket,

CharSequence

data,
boolean last)

A textual data has been received.

Return a

CompletionStage

which will be used by the

WebSocket

as an indication it may reclaim the

CharSequence

. Do not access the

CharSequence

after
this

CompletionStage

has completed.

Return a

CompletionStage

which will be used by the

WebSocket

as an indication it may reclaim the

CharSequence

. Do not access the

CharSequence

after
this

CompletionStage

has completed.

webSocket.request(1);
return null;

onBinary

```java
default
CompletionStage
<?> onBinary​(
WebSocket
webSocket,

ByteBuffer
data,
boolean last)
```

A binary data has been received.

This data is located in bytes from the buffer's position to its
limit.

Return a

CompletionStage

which will be used by the

WebSocket

as an indication it may reclaim the

ByteBuffer

. Do not access the

ByteBuffer

after
this

CompletionStage

has completed.

**Implementation Requirements:** The default implementation is equivalent to:

```java
webSocket.request(1);
return null;
```
**Parameters:** webSocket

- the WebSocket on which the data has been received
**Parameters:** data

- the data
**Parameters:** last

- whether this invocation completes the message
**Returns:** a

CompletionStage

which completes when the

ByteBuffer

may be reclaimed; or

null

if it may be
reclaimed immediately

---

#### onBinary

default

CompletionStage

<?> onBinary​(

WebSocket

webSocket,

ByteBuffer

data,
boolean last)

A binary data has been received.

This data is located in bytes from the buffer's position to its
limit.

Return a

CompletionStage

which will be used by the

WebSocket

as an indication it may reclaim the

ByteBuffer

. Do not access the

ByteBuffer

after
this

CompletionStage

has completed.

This data is located in bytes from the buffer's position to its
limit.

Return a

CompletionStage

which will be used by the

WebSocket

as an indication it may reclaim the

ByteBuffer

. Do not access the

ByteBuffer

after
this

CompletionStage

has completed.

Return a

CompletionStage

which will be used by the

WebSocket

as an indication it may reclaim the

ByteBuffer

. Do not access the

ByteBuffer

after
this

CompletionStage

has completed.

webSocket.request(1);
return null;

onPing

```java
default
CompletionStage
<?> onPing​(
WebSocket
webSocket,

ByteBuffer
message)
```

A Ping message has been received.

As guaranteed by the WebSocket Protocol, the message consists of
not more than

125

bytes. These bytes are located from the
buffer's position to its limit.

Given that the WebSocket implementation will automatically send a
reciprocal pong when a ping is received, it is rarely required to
send a pong message explicitly when a ping is received.

Return a

CompletionStage

which will be used by the

WebSocket

as a signal it may reclaim the

ByteBuffer

. Do not access the

ByteBuffer

after
this

CompletionStage

has completed.

**Implementation Requirements:** The default implementation is equivalent to:

```java
webSocket.request(1);
return null;
```
**Parameters:** webSocket

- the WebSocket on which the message has been received
**Parameters:** message

- the message
**Returns:** a

CompletionStage

which completes when the

ByteBuffer

may be reclaimed; or

null

if it may be
reclaimed immediately

---

#### onPing

default

CompletionStage

<?> onPing​(

WebSocket

webSocket,

ByteBuffer

message)

A Ping message has been received.

As guaranteed by the WebSocket Protocol, the message consists of
not more than

125

bytes. These bytes are located from the
buffer's position to its limit.

Given that the WebSocket implementation will automatically send a
reciprocal pong when a ping is received, it is rarely required to
send a pong message explicitly when a ping is received.

Return a

CompletionStage

which will be used by the

WebSocket

as a signal it may reclaim the

ByteBuffer

. Do not access the

ByteBuffer

after
this

CompletionStage

has completed.

As guaranteed by the WebSocket Protocol, the message consists of
not more than

125

bytes. These bytes are located from the
buffer's position to its limit.

Given that the WebSocket implementation will automatically send a
reciprocal pong when a ping is received, it is rarely required to
send a pong message explicitly when a ping is received.

Return a

CompletionStage

which will be used by the

WebSocket

as a signal it may reclaim the

ByteBuffer

. Do not access the

ByteBuffer

after
this

CompletionStage

has completed.

Given that the WebSocket implementation will automatically send a
reciprocal pong when a ping is received, it is rarely required to
send a pong message explicitly when a ping is received.

Return a

CompletionStage

which will be used by the

WebSocket

as a signal it may reclaim the

ByteBuffer

. Do not access the

ByteBuffer

after
this

CompletionStage

has completed.

Return a

CompletionStage

which will be used by the

WebSocket

as a signal it may reclaim the

ByteBuffer

. Do not access the

ByteBuffer

after
this

CompletionStage

has completed.

webSocket.request(1);
return null;

onPong

```java
default
CompletionStage
<?> onPong​(
WebSocket
webSocket,

ByteBuffer
message)
```

A Pong message has been received.

As guaranteed by the WebSocket Protocol, the message consists of
not more than

125

bytes. These bytes are located from the
buffer's position to its limit.

Return a

CompletionStage

which will be used by the

WebSocket

as a signal it may reclaim the

ByteBuffer

. Do not access the

ByteBuffer

after
this

CompletionStage

has completed.

**Implementation Requirements:** The default implementation is equivalent to:

```java
webSocket.request(1);
return null;
```
**Parameters:** webSocket

- the WebSocket on which the message has been received
**Parameters:** message

- the message
**Returns:** a

CompletionStage

which completes when the

ByteBuffer

may be reclaimed; or

null

if it may be
reclaimed immediately

---

#### onPong

default

CompletionStage

<?> onPong​(

WebSocket

webSocket,

ByteBuffer

message)

A Pong message has been received.

As guaranteed by the WebSocket Protocol, the message consists of
not more than

125

bytes. These bytes are located from the
buffer's position to its limit.

Return a

CompletionStage

which will be used by the

WebSocket

as a signal it may reclaim the

ByteBuffer

. Do not access the

ByteBuffer

after
this

CompletionStage

has completed.

As guaranteed by the WebSocket Protocol, the message consists of
not more than

125

bytes. These bytes are located from the
buffer's position to its limit.

Return a

CompletionStage

which will be used by the

WebSocket

as a signal it may reclaim the

ByteBuffer

. Do not access the

ByteBuffer

after
this

CompletionStage

has completed.

Return a

CompletionStage

which will be used by the

WebSocket

as a signal it may reclaim the

ByteBuffer

. Do not access the

ByteBuffer

after
this

CompletionStage

has completed.

webSocket.request(1);
return null;

onClose

```java
default
CompletionStage
<?> onClose​(
WebSocket
webSocket,
int statusCode,

String
reason)
```

Receives a Close message indicating the WebSocket's input has been
closed.

This is the last invocation from the specified

WebSocket

.
By the time this invocation begins the WebSocket's input will have
been closed.

A Close message consists of a status code and a reason for
closing. The status code is an integer from the range

1000 <= code <= 65535

. The

reason

is a string which
has a UTF-8 representation not longer than

123

bytes.

If the WebSocket's output is not already closed, the

CompletionStage

returned by this method will be used as an
indication that the WebSocket's output may be closed. The WebSocket
will close its output at the earliest of completion of the returned

CompletionStage

or invoking either of the

sendClose

or

abort

methods.

**API Note:** Returning a

CompletionStage

that never completes,
effectively disables the reciprocating closure of the output.

To specify a custom closure code or reason code the

sendClose

method may be invoked from inside the

onClose

invocation:

```java
public CompletionStage<?> onClose(WebSocket webSocket,
int statusCode,
String reason) {
webSocket.sendClose(CUSTOM_STATUS_CODE, CUSTOM_REASON);
return new CompletableFuture<Void>();
}
```
**Implementation Requirements:** The default implementation of this method returns

null

, indicating that the output should be closed
immediately.
**Parameters:** webSocket

- the WebSocket on which the message has been received
**Parameters:** statusCode

- the status code
**Parameters:** reason

- the reason
**Returns:** a

CompletionStage

which completes when the

WebSocket

may be closed; or

null

if it may be
closed immediately

---

#### onClose

default

CompletionStage

<?> onClose​(

WebSocket

webSocket,
int statusCode,

String

reason)

Receives a Close message indicating the WebSocket's input has been
closed.

This is the last invocation from the specified

WebSocket

.
By the time this invocation begins the WebSocket's input will have
been closed.

A Close message consists of a status code and a reason for
closing. The status code is an integer from the range

1000 <= code <= 65535

. The

reason

is a string which
has a UTF-8 representation not longer than

123

bytes.

If the WebSocket's output is not already closed, the

CompletionStage

returned by this method will be used as an
indication that the WebSocket's output may be closed. The WebSocket
will close its output at the earliest of completion of the returned

CompletionStage

or invoking either of the

sendClose

or

abort

methods.

This is the last invocation from the specified

WebSocket

.
By the time this invocation begins the WebSocket's input will have
been closed.

A Close message consists of a status code and a reason for
closing. The status code is an integer from the range

1000 <= code <= 65535

. The

reason

is a string which
has a UTF-8 representation not longer than

123

bytes.

If the WebSocket's output is not already closed, the

CompletionStage

returned by this method will be used as an
indication that the WebSocket's output may be closed. The WebSocket
will close its output at the earliest of completion of the returned

CompletionStage

or invoking either of the

sendClose

or

abort

methods.

A Close message consists of a status code and a reason for
closing. The status code is an integer from the range

1000 <= code <= 65535

. The

reason

is a string which
has a UTF-8 representation not longer than

123

bytes.

If the WebSocket's output is not already closed, the

CompletionStage

returned by this method will be used as an
indication that the WebSocket's output may be closed. The WebSocket
will close its output at the earliest of completion of the returned

CompletionStage

or invoking either of the

sendClose

or

abort

methods.

If the WebSocket's output is not already closed, the

CompletionStage

returned by this method will be used as an
indication that the WebSocket's output may be closed. The WebSocket
will close its output at the earliest of completion of the returned

CompletionStage

or invoking either of the

sendClose

or

abort

methods.

To specify a custom closure code or reason code the

sendClose

method may be invoked from inside the

onClose

invocation:

```java
public CompletionStage<?> onClose(WebSocket webSocket,
int statusCode,
String reason) {
webSocket.sendClose(CUSTOM_STATUS_CODE, CUSTOM_REASON);
return new CompletableFuture<Void>();
}
```

public CompletionStage<?> onClose(WebSocket webSocket,
int statusCode,
String reason) {
webSocket.sendClose(CUSTOM_STATUS_CODE, CUSTOM_REASON);
return new CompletableFuture<Void>();
}

onError

```java
default void onError​(
WebSocket
webSocket,

Throwable
error)
```

An error has occurred.

This is the last invocation from the specified WebSocket. By the
time this invocation begins both the WebSocket's input and output
will have been closed. A WebSocket may invoke this method on the
associated listener at any time after it has invoked

onOpen

,
regardless of whether or not any invocations have been requested from
the WebSocket.

If an exception is thrown from this method, resulting behavior is
undefined.

**Parameters:** webSocket

- the WebSocket on which the error has occurred
**Parameters:** error

- the error

---

#### onError

default void onError​(

WebSocket

webSocket,

Throwable

error)

An error has occurred.

This is the last invocation from the specified WebSocket. By the
time this invocation begins both the WebSocket's input and output
will have been closed. A WebSocket may invoke this method on the
associated listener at any time after it has invoked

onOpen

,
regardless of whether or not any invocations have been requested from
the WebSocket.

If an exception is thrown from this method, resulting behavior is
undefined.

This is the last invocation from the specified WebSocket. By the
time this invocation begins both the WebSocket's input and output
will have been closed. A WebSocket may invoke this method on the
associated listener at any time after it has invoked

onOpen

,
regardless of whether or not any invocations have been requested from
the WebSocket.

If an exception is thrown from this method, resulting behavior is
undefined.

If an exception is thrown from this method, resulting behavior is
undefined.

---

