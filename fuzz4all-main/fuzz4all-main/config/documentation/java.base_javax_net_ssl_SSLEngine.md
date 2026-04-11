# Class SSLEngine

**Source:** `java.base\javax\net\ssl\SSLEngine.html`

### Class Description

```java
public abstract class
SSLEngine

extends
Object
```

A class which enables secure communications using protocols such as
the Secure Sockets Layer (SSL) or

IETF RFC 2246 "Transport
Layer Security" (TLS)

protocols, but is transport independent.

The secure communications modes include:

- Integrity Protection

. SSL/TLS/DTLS protects against
modification of messages by an active wiretapper.

Authentication

. In most modes, SSL/TLS/DTLS provides
peer authentication. Servers are usually authenticated, and
clients may be authenticated as requested by servers.

Confidentiality (Privacy Protection)

. In most
modes, SSL/TLS/DTLS encrypts data being sent between client and
server. This protects the confidentiality of data, so that
passive wiretappers won't see sensitive data such as financial
information or personal information of many kinds.

These kinds of protection are specified by a "cipher suite", which
is a combination of cryptographic algorithms used by a given SSL
connection. During the negotiation process, the two endpoints must
agree on a cipher suite that is available in both environments. If
there is no such suite in common, no SSL connection can be
established, and no data can be exchanged.

The cipher suite used is established by a negotiation process called
"handshaking". The goal of this process is to create or rejoin a
"session", which may protect many connections over time. After
handshaking has completed, you can access session attributes by
using the

getSession()

method.

The

SSLSocket

class provides much of the same security
functionality, but all of the inbound and outbound data is
automatically transported using the underlying

Socket

, which by design uses a blocking model.
While this is appropriate for many applications, this model does not
provide the scalability required by large servers.

The primary distinction of an

SSLEngine

is that it
operates on inbound and outbound byte streams, independent of the
transport mechanism. It is the responsibility of the

SSLEngine

user to arrange for reliable I/O transport to
the peer. By separating the SSL/TLS/DTLS abstraction from the I/O
transport mechanism, the

SSLEngine

can be used for a
wide variety of I/O types, such as

non-blocking I/O (polling)

,

selectable non-blocking I/O

,

Socket

and the
traditional Input/OutputStreams, local

ByteBuffers

or byte arrays,

future asynchronous
I/O models

, and so on.

At a high level, the

SSLEngine

appears thus:

```java
app data

| ^
| | |
v | |
+----+-----|-----+----+
| | |
| SSL|Engine |
wrap() | | | unwrap()
| OUTBOUND | INBOUND |
| | |
+----+-----|-----+----+
| | ^
| | |
v |

net data
```

Application data (also known as plaintext or cleartext) is data which
is produced or consumed by an application. Its counterpart is
network data, which consists of either handshaking and/or ciphertext
(encrypted) data, and destined to be transported via an I/O
mechanism. Inbound data is data which has been received from the
peer, and outbound data is destined for the peer.

(In the context of an

SSLEngine

, the term "handshake
data" is taken to mean any data exchanged to establish and control a
secure connection. Handshake data includes the SSL/TLS/DTLS messages
"alert", "change_cipher_spec," and "handshake.")

There are five distinct phases to an

SSLEngine

.

- Creation - The

SSLEngine

has been created and
initialized, but has not yet been used. During this phase, an
application may set any

SSLEngine

-specific settings
(enabled cipher suites, whether the

SSLEngine

should
handshake in client or server mode, and so on). Once
handshaking has begun, though, any new settings (except
client/server mode, see below) will be used for
the next handshake.

Initial Handshake - The initial handshake is a procedure by
which the two peers exchange communication parameters until an
SSLSession is established. Application data can not be sent during
this phase.

Application Data - Once the communication parameters have
been established and the handshake is complete, application data
may flow through the

SSLEngine

. Outbound
application messages are encrypted and integrity protected,
and inbound messages reverse the process.

Rehandshaking - Either side may request a renegotiation of
the session at any time during the Application Data phase. New
handshaking data can be intermixed among the application data.
Before starting the rehandshake phase, the application may
reset the SSL/TLS/DTLS communication parameters such as the list of
enabled ciphersuites and whether to use client authentication,
but can not change between client/server modes. As before, once
handshaking has begun, any new

SSLEngine

configuration settings will not be used until the next
handshake.

Closure - When the connection is no longer needed, the client
and the server applications should each close both sides of their
respective connections. For

SSLEngine

objects, an
application should call

closeOutbound()

and
send any remaining messages to the peer. Likewise, an application
should receive any remaining messages from the peer before calling

closeInbound()

. The underlying transport mechanism
can then be closed after both sides of the

SSLEngine

have
been closed. If the connection is not closed in an orderly manner
(for example

closeInbound()

is called before the
peer's write closure notification has been received), exceptions
will be raised to indicate that an error has occurred. Once an
engine is closed, it is not reusable: a new

SSLEngine

must be created.

An

SSLEngine

is created by calling

SSLContext.createSSLEngine()

from an initialized

SSLContext

. Any configuration
parameters should be set before making the first call to

wrap()

,

unwrap()

, or

beginHandshake()

. These methods all trigger the
initial handshake.

Data moves through the engine by calling

wrap()

or

unwrap()

on outbound or inbound data, respectively. Depending on
the state of the

SSLEngine

, a

wrap()

call
may consume application data from the source buffer and may produce
network data in the destination buffer. The outbound data
may contain application and/or handshake data. A call to

unwrap()

will examine the source buffer and may
advance the handshake if the data is handshaking information, or
may place application data in the destination buffer if the data
is application. The state of the underlying SSL/TLS/DTLS algorithm
will determine when data is consumed and produced.

Calls to

wrap()

and

unwrap()

return an

SSLEngineResult

which indicates the status of the
operation, and (optionally) how to interact with the engine to make
progress.

The

SSLEngine

produces/consumes complete SSL/TLS/DTLS
packets only, and does not store application data internally between
calls to

wrap()/unwrap()

. Thus input and output

ByteBuffer

s must be sized appropriately to hold the
maximum record that can be produced. Calls to

SSLSession.getPacketBufferSize()

and

SSLSession.getApplicationBufferSize()

should be used to determine
the appropriate buffer sizes. The size of the outbound application
data buffer generally does not matter. If buffer conditions do not
allow for the proper consumption/production of data, the application
must determine (via

SSLEngineResult

) and correct the
problem, and then try the call again.

For example,

unwrap()

will return a

SSLEngineResult.Status.BUFFER_OVERFLOW

result if the engine
determines that there is not enough destination buffer space available.
Applications should call

SSLSession.getApplicationBufferSize()

and compare that value with the space available in the destination buffer,
enlarging the buffer if necessary. Similarly, if

unwrap()

were to return a

SSLEngineResult.Status.BUFFER_UNDERFLOW

, the
application should call

SSLSession.getPacketBufferSize()

to ensure
that the source buffer has enough room to hold a record (enlarging if
necessary), and then obtain more inbound data.

```java
SSLEngineResult r = engine.unwrap(src, dst);
switch (r.getStatus()) {
BUFFER_OVERFLOW:
// Could attempt to drain the dst buffer of any already obtained
// data, but we'll just increase it to the size needed.
int appSize = engine.getSession().getApplicationBufferSize();
ByteBuffer b = ByteBuffer.allocate(appSize + dst.position());
dst.flip();
b.put(dst);
dst = b;
// retry the operation.
break;
BUFFER_UNDERFLOW:
int netSize = engine.getSession().getPacketBufferSize();
// Resize buffer if needed.
if (netSize > dst.capacity()) {
ByteBuffer b = ByteBuffer.allocate(netSize);
src.flip();
b.put(src);
src = b;
}
// Obtain more inbound network data for src,
// then retry the operation.
break;
// other cases: CLOSED, OK.
}
```

Unlike

SSLSocket

, all methods of SSLEngine are
non-blocking.

SSLEngine

implementations may
require the results of tasks that may take an extended period of
time to complete, or may even block. For example, a TrustManager
may need to connect to a remote certificate validation service,
or a KeyManager might need to prompt a user to determine which
certificate to use as part of client authentication. Additionally,
creating cryptographic signatures and verifying them can be slow,
seemingly blocking.

For any operation which may potentially block, the

SSLEngine

will create a

Runnable

delegated task. When

SSLEngineResult

indicates that a
delegated task result is needed, the application must call

getDelegatedTask()

to obtain an outstanding delegated task and
call its

run()

method (possibly using
a different thread depending on the compute strategy). The
application should continue obtaining delegated tasks until no more
exist, and try the original operation again.

At the end of a communication session, applications should properly
close the SSL/TLS/DTLS link. The SSL/TLS/DTLS protocols have closure
handshake messages, and these messages should be communicated to the
peer before releasing the

SSLEngine

and closing the
underlying transport mechanism. A close can be initiated by one of:
an SSLException, an inbound closure handshake message, or one of the
close methods. In all cases, closure handshake messages are
generated by the engine, and

wrap()

should be repeatedly
called until the resulting

SSLEngineResult

's status
returns "CLOSED", or

isOutboundDone()

returns true. All
data obtained from the

wrap()

method should be sent to the
peer.

closeOutbound()

is used to signal the engine that the
application will not be sending any more data.

A peer will signal its intent to close by sending its own closure
handshake message. After this message has been received and
processed by the local

SSLEngine

's

unwrap()

call, the application can detect the close by calling

unwrap()

and looking for a

SSLEngineResult

with status "CLOSED", or if

isInboundDone()

returns true.
If for some reason the peer closes the communication link without
sending the proper SSL/TLS/DTLS closure message, the application can
detect the end-of-stream and can signal the engine via

closeInbound()

that there will no more inbound messages to
process. Some applications might choose to require orderly shutdown
messages from a peer, in which case they can check that the closure
was generated by a handshake message and not by an end-of-stream
condition.

There are two groups of cipher suites which you will need to know
about when managing cipher suites:

- Supported

cipher suites: all the suites which are
supported by the SSL implementation. This list is reported
using

getSupportedCipherSuites()

.

Enabled

cipher suites, which may be fewer than
the full set of supported suites. This group is set using the

setEnabledCipherSuites(String [])

method, and
queried using the

getEnabledCipherSuites()

method.
Initially, a default set of cipher suites will be enabled on a
new engine that represents the minimum suggested
configuration.

Implementation defaults require that only cipher suites which
authenticate servers and provide confidentiality be enabled by
default. Only if both sides explicitly agree to unauthenticated
and/or non-private (unencrypted) communications will such a
cipher suite be selected.

Each SSL/TLS/DTLS connection must have one client and one server, thus
each endpoint must decide which role to assume. This choice determines
who begins the handshaking process as well as which type of messages
should be sent by each party. The method

setUseClientMode(boolean)

configures the mode. Note that the
default mode for a new

SSLEngine

is provider-specific.
Applications should set the mode explicitly before invoking other
methods of the

SSLEngine

. Once the initial handshaking has
started, an

SSLEngine

can not switch between client and server
modes, even when performing renegotiations.

Applications might choose to process delegated tasks in different
threads. When an

SSLEngine

is created, the current

AccessControlContext

is saved. All future delegated tasks will be processed using this
context: that is, all access control decisions will be made using the
context captured at engine creation.

Concurrency Notes

:
There are two concurrency issues to be aware of:

- The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

**Since:** 1.5
**See Also:** SSLContext

,

SSLSocket

,

SSLServerSocket

,

SSLSession

,

Socket

---

### Field Details

*No entries found.*

### Constructor Details

#### protected SSLEngine()

Constructor for an

SSLEngine

providing no hints
for an internal session reuse strategy.

**See Also:**
- SSLContext.createSSLEngine()

,

SSLSessionContext

---

#### protected SSLEngine​(
String
peerHost,
int peerPort)

Constructor for an

SSLEngine

.

SSLEngine

implementations may use the

peerHost

and

peerPort

parameters as hints
for their internal session reuse strategy.

Some cipher suites (such as Kerberos) require remote hostname
information. Implementations of this class should use this
constructor to use Kerberos.

The parameters are not authenticated by the

SSLEngine

.

**Parameters:**
- peerHost

- the name of the peer host
- peerPort

- the port number of the peer

**See Also:**
- SSLContext.createSSLEngine(String, int)

,

SSLSessionContext

---

### Method Details

#### public
String
getPeerHost()

Returns the host name of the peer.

Note that the value is not authenticated, and should not be
relied upon.

**Returns:**
- the host name of the peer, or null if nothing is
available.

---

#### public int getPeerPort()

Returns the port number of the peer.

Note that the value is not authenticated, and should not be
relied upon.

**Returns:**
- the port number of the peer, or -1 if nothing is
available.

---

#### public
SSLEngineResult
wrap​(
ByteBuffer
src,

ByteBuffer
dst)
throws
SSLException

Attempts to encode a buffer of plaintext application data into
SSL/TLS/DTLS network data.

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.wrap(new ByteBuffer [] { src }, 0, 1, dst);
```

**Parameters:**
- src

- a

ByteBuffer

containing outbound application data
- dst

- a

ByteBuffer

to hold outbound network data

**Returns:**
- an

SSLEngineResult

describing the result
of this operation.

**Throws:**
- SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
- ReadOnlyBufferException

- if the

dst

buffer is read-only.
- IllegalArgumentException

- if either

src

or

dst

is null.
- IllegalStateException

- if the client/server mode
has not yet been set.

**See Also:**
- wrap(ByteBuffer [], int, int, ByteBuffer)

---

#### public
SSLEngineResult
wrap​(
ByteBuffer
[] srcs,

ByteBuffer
dst)
throws
SSLException

Attempts to encode plaintext bytes from a sequence of data
buffers into SSL/TLS/DTLS network data.

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.wrap(srcs, 0, srcs.length, dst);
```

**Parameters:**
- srcs

- an array of

ByteBuffers

containing the
outbound application data
- dst

- a

ByteBuffer

to hold outbound network data

**Returns:**
- an

SSLEngineResult

describing the result
of this operation.

**Throws:**
- SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
- ReadOnlyBufferException

- if the

dst

buffer is read-only.
- IllegalArgumentException

- if either

srcs

or

dst

is null, or if any element in

srcs

is null.
- IllegalStateException

- if the client/server mode
has not yet been set.

**See Also:**
- wrap(ByteBuffer [], int, int, ByteBuffer)

---

#### public abstract
SSLEngineResult
wrap​(
ByteBuffer
[] srcs,
int offset,
int length,

ByteBuffer
dst)
throws
SSLException

Attempts to encode plaintext bytes from a subsequence of data
buffers into SSL/TLS/DTLS network data. This

"gathering"

operation encodes, in a single invocation, a sequence of bytes
from one or more of a given sequence of buffers. Gathering
wraps are often useful when implementing network protocols or
file formats that, for example, group data into segments
consisting of one or more fixed-length headers followed by a
variable-length body. See

GatheringByteChannel

for more
information on gathering, and

GatheringByteChannel.write(ByteBuffer[],
int, int)

for more information on the subsequence
behavior.

Depending on the state of the SSLEngine, this method may produce
network data without consuming any application data (for example,
it may generate handshake data.)

The application is responsible for reliably transporting the
network data to the peer, and for ensuring that data created by
multiple calls to wrap() is transported in the same order in which
it was generated. The application must properly synchronize
multiple calls to this method.

If this

SSLEngine

has not yet started its initial
handshake, this method will automatically start the handshake.

This method will attempt to produce SSL/TLS/DTLS records, and will
consume as much source data as possible, but will never consume
more than the sum of the bytes remaining in each buffer. Each

ByteBuffer

's position is updated to reflect the
amount of data consumed or produced. The limits remain the
same.

The underlying memory used by the

srcs

and

dst ByteBuffer

s must not be the same.

See the class description for more information on engine closure.

**Parameters:**
- srcs

- an array of

ByteBuffers

containing the
outbound application data
- offset

- The offset within the buffer array of the first buffer from
which bytes are to be retrieved; it must be non-negative
and no larger than

srcs.length
- length

- The maximum number of buffers to be accessed; it must be
non-negative and no larger than

srcs.length

-

offset
- dst

- a

ByteBuffer

to hold outbound network data

**Returns:**
- an

SSLEngineResult

describing the result
of this operation.

**Throws:**
- SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
- IndexOutOfBoundsException

- if the preconditions on the

offset

and

length

parameters do not hold.
- ReadOnlyBufferException

- if the

dst

buffer is read-only.
- IllegalArgumentException

- if either

srcs

or

dst

is null, or if any element in the

srcs

subsequence specified is null.
- IllegalStateException

- if the client/server mode
has not yet been set.

**See Also:**
- GatheringByteChannel

,

GatheringByteChannel.write(
ByteBuffer[], int, int)

---

#### public
SSLEngineResult
unwrap​(
ByteBuffer
src,

ByteBuffer
dst)
throws
SSLException

Attempts to decode SSL/TLS/DTLS network data into a plaintext
application data buffer.

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.unwrap(src, new ByteBuffer [] { dst }, 0, 1);
```

**Parameters:**
- src

- a

ByteBuffer

containing inbound network data.
- dst

- a

ByteBuffer

to hold inbound application data.

**Returns:**
- an

SSLEngineResult

describing the result
of this operation.

**Throws:**
- SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
- ReadOnlyBufferException

- if the

dst

buffer is read-only.
- IllegalArgumentException

- if either

src

or

dst

is null.
- IllegalStateException

- if the client/server mode
has not yet been set.

**See Also:**
- unwrap(ByteBuffer, ByteBuffer [], int, int)

---

#### public
SSLEngineResult
unwrap​(
ByteBuffer
src,

ByteBuffer
[] dsts)
throws
SSLException

Attempts to decode SSL/TLS/DTLS network data into a sequence of plaintext
application data buffers.

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.unwrap(src, dsts, 0, dsts.length);
```

**Parameters:**
- src

- a

ByteBuffer

containing inbound network data.
- dsts

- an array of

ByteBuffer

s to hold inbound
application data.

**Returns:**
- an

SSLEngineResult

describing the result
of this operation.

**Throws:**
- SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
- ReadOnlyBufferException

- if any of the

dst

buffers are read-only.
- IllegalArgumentException

- if either

src

or

dsts

is null, or if any element in

dsts

is null.
- IllegalStateException

- if the client/server mode
has not yet been set.

**See Also:**
- unwrap(ByteBuffer, ByteBuffer [], int, int)

---

#### public abstract
SSLEngineResult
unwrap​(
ByteBuffer
src,

ByteBuffer
[] dsts,
int offset,
int length)
throws
SSLException

Attempts to decode SSL/TLS/DTLS network data into a subsequence of
plaintext application data buffers. This

"scattering"

operation decodes, in a single invocation, a sequence of bytes
into one or more of a given sequence of buffers. Scattering
unwraps are often useful when implementing network protocols or
file formats that, for example, group data into segments
consisting of one or more fixed-length headers followed by a
variable-length body. See

ScatteringByteChannel

for more
information on scattering, and

ScatteringByteChannel.read(ByteBuffer[],
int, int)

for more information on the subsequence
behavior.

Depending on the state of the SSLEngine, this method may consume
network data without producing any application data (for example,
it may consume handshake data.)

The application is responsible for reliably obtaining the network
data from the peer, and for invoking unwrap() on the data in the
order it was received. The application must properly synchronize
multiple calls to this method.

If this

SSLEngine

has not yet started its initial
handshake, this method will automatically start the handshake.

This method will attempt to consume one complete SSL/TLS/DTLS network
packet, but will never consume more than the sum of the bytes
remaining in the buffers. Each

ByteBuffer

's
position is updated to reflect the amount of data consumed or
produced. The limits remain the same.

The underlying memory used by the

src

and

dsts ByteBuffer

s must not be the same.

The inbound network buffer may be modified as a result of this
call: therefore if the network data packet is required for some
secondary purpose, the data should be duplicated before calling this
method. Note: the network data will not be useful to a second
SSLEngine, as each SSLEngine contains unique random state which
influences the SSL/TLS/DTLS messages.

See the class description for more information on engine closure.

**Parameters:**
- src

- a

ByteBuffer

containing inbound network data.
- dsts

- an array of

ByteBuffer

s to hold inbound
application data.
- offset

- The offset within the buffer array of the first buffer from
which bytes are to be transferred; it must be non-negative
and no larger than

dsts.length

.
- length

- The maximum number of buffers to be accessed; it must be
non-negative and no larger than

dsts.length

-

offset

.

**Returns:**
- an

SSLEngineResult

describing the result
of this operation.

**Throws:**
- SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
- IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold.
- ReadOnlyBufferException

- if any of the

dst

buffers are read-only.
- IllegalArgumentException

- if either

src

or

dsts

is null, or if any element in the

dsts

subsequence specified is null.
- IllegalStateException

- if the client/server mode
has not yet been set.

**See Also:**
- ScatteringByteChannel

,

ScatteringByteChannel.read(
ByteBuffer[], int, int)

---

#### public abstract
Runnable
getDelegatedTask()

Returns a delegated

Runnable

task for
this

SSLEngine

.

SSLEngine

operations may require the results of
operations that block, or may take an extended period of time to
complete. This method is used to obtain an outstanding

Runnable

operation (task). Each task must be assigned
a thread (possibly the current) to perform the

run

operation. Once the

run

method returns, the

Runnable

object
is no longer needed and may be discarded.

Delegated tasks run in the

AccessControlContext

in place when this object was created.

A call to this method will return each outstanding task
exactly once.

Multiple delegated tasks can be run in parallel.

**Returns:**
- a delegated

Runnable

task, or null
if none are available.

---

#### public abstract void closeInbound()
throws
SSLException

Signals that no more inbound network data will be sent
to this

SSLEngine

.

If the application initiated the closing process by calling

closeOutbound()

, under some circumstances it is not
required that the initiator wait for the peer's corresponding
close message. (See section 7.2.1 of the TLS specification (

RFC 2246

) for more
information on waiting for closure alerts.) In such cases, this
method need not be called.

But if the application did not initiate the closure process, or
if the circumstances above do not apply, this method should be
called whenever the end of the SSL/TLS/DTLS data stream is reached.
This ensures closure of the inbound side, and checks that the
peer followed the SSL/TLS/DTLS close procedure properly, thus
detecting possible truncation attacks.

This method is idempotent: if the inbound side has already
been closed, this method does not do anything.

wrap()

should be
called to flush any remaining handshake data.

**Throws:**
- SSLException

- if this engine has not received the proper SSL/TLS/DTLS close
notification message from the peer.

**See Also:**
- isInboundDone()

,

isOutboundDone()

---

#### public abstract boolean isInboundDone()

Returns whether

unwrap(ByteBuffer, ByteBuffer)

will
accept any more inbound data messages.

**Returns:**
- true if the

SSLEngine

will not
consume anymore network data (and by implication,
will not produce any more application data.)

**See Also:**
- closeInbound()

---

#### public abstract void closeOutbound()

Signals that no more outbound application data will be sent
on this

SSLEngine

.

This method is idempotent: if the outbound side has already
been closed, this method does not do anything.

wrap(ByteBuffer, ByteBuffer)

should be
called to flush any remaining handshake data.

**See Also:**
- isOutboundDone()

---

#### public abstract boolean isOutboundDone()

Returns whether

wrap(ByteBuffer, ByteBuffer)

will
produce any more outbound data messages.

Note that during the closure phase, a

SSLEngine

may
generate handshake closure data that must be sent to the peer.

wrap()

must be called to generate this data. When
this method returns true, no more outbound data will be created.

**Returns:**
- true if the

SSLEngine

will not produce
any more network data

**See Also:**
- closeOutbound()

,

closeInbound()

---

#### public abstract
String
[] getSupportedCipherSuites()

Returns the names of the cipher suites which could be enabled for use
on this engine. Normally, only a subset of these will actually
be enabled by default, since this list may include cipher suites which
do not meet quality of service requirements for those defaults. Such
cipher suites might be useful in specialized applications.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:**
- an array of cipher suite names

**See Also:**
- getEnabledCipherSuites()

,

setEnabledCipherSuites(String [])

---

#### public abstract
String
[] getEnabledCipherSuites()

Returns the names of the SSL cipher suites which are currently
enabled for use on this engine. When an SSLEngine is first
created, all enabled cipher suites support a minimum quality of
service. Thus, in some environments this value might be empty.

Note that even if a suite is enabled, it may never be used. This
can occur if the peer does not support it, or its use is restricted,
or the requisite certificates (and private keys) for the suite are
not available, or an anonymous suite is enabled but authentication
is required.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:**
- an array of cipher suite names

**See Also:**
- getSupportedCipherSuites()

,

setEnabledCipherSuites(String [])

---

#### public abstract void setEnabledCipherSuites​(
String
[] suites)

Sets the cipher suites enabled for use on this engine.

Each cipher suite in the

suites

parameter must have
been listed by getSupportedCipherSuites(), or the method will
fail. Following a successful call to this method, only suites
listed in the

suites

parameter are enabled for use.

Note that the standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list or might not
use the recommended name for a certain cipher suite.

See

getEnabledCipherSuites()

for more information
on why a specific cipher suite may never be used on a engine.

**Parameters:**
- suites

- Names of all the cipher suites to enable

**Throws:**
- IllegalArgumentException

- when one or more of the ciphers
named by the parameter is not supported, or when the
parameter is null.

**See Also:**
- getSupportedCipherSuites()

,

getEnabledCipherSuites()

---

#### public abstract
String
[] getSupportedProtocols()

Returns the names of the protocols which could be enabled for use
with this

SSLEngine

.

**Returns:**
- an array of protocols supported

---

#### public abstract
String
[] getEnabledProtocols()

Returns the names of the protocol versions which are currently
enabled for use with this

SSLEngine

.

Note that even if a protocol is enabled, it may never be used.
This can occur if the peer does not support the protocol, or its
use is restricted, or there are no enabled cipher suites supported
by the protocol.

**Returns:**
- an array of protocols

**See Also:**
- setEnabledProtocols(String [])

---

#### public abstract void setEnabledProtocols​(
String
[] protocols)

Set the protocol versions enabled for use on this engine.

The protocols must have been listed by getSupportedProtocols()
as being supported. Following a successful call to this method,
only protocols listed in the

protocols

parameter
are enabled for use.

**Parameters:**
- protocols

- Names of all the protocols to enable.

**Throws:**
- IllegalArgumentException

- when one or more of
the protocols named by the parameter is not supported or
when the protocols parameter is null.

**See Also:**
- getEnabledProtocols()

---

#### public abstract
SSLSession
getSession()

Returns the

SSLSession

in use in this

SSLEngine

.

These can be long lived, and frequently correspond to an entire
login session for some user. The session specifies a particular
cipher suite which is being actively used by all connections in
that session, as well as the identities of the session's client
and server.

Unlike

SSLSocket.getSession()

this method does not block until handshaking is complete.

Until the initial handshake has completed, this method returns
a session object which reports an invalid cipher suite of
"SSL_NULL_WITH_NULL_NULL".

**Returns:**
- the

SSLSession

for this

SSLEngine

**See Also:**
- SSLSession

---

#### public
SSLSession
getHandshakeSession()

Returns the

SSLSession

being constructed during a SSL/TLS/DTLS
handshake.

TLS/DTLS protocols may negotiate parameters that are needed when using
an instance of this class, but before the

SSLSession

has
been completely initialized and made available via

getSession

.
For example, the list of valid signature algorithms may restrict
the type of certificates that can be used during TrustManager
decisions, or the maximum TLS/DTLS fragment packet sizes can be
resized to better support the network environment.

This method provides early access to the

SSLSession

being
constructed. Depending on how far the handshake has progressed,
some data may not yet be available for use. For example, if a
remote server will be sending a Certificate chain, but that chain
has yet not been processed, the

getPeerCertificates

method of

SSLSession

will throw a
SSLPeerUnverifiedException. Once that chain has been processed,

getPeerCertificates

will return the proper value.

**Returns:**
- null if this instance is not currently handshaking, or
if the current handshake has not progressed far enough to
create a basic SSLSession. Otherwise, this method returns the

SSLSession

currently being negotiated.

**Throws:**
- UnsupportedOperationException

- if the underlying provider
does not implement the operation.

**See Also:**
- SSLSocket

,

SSLSession

,

ExtendedSSLSession

,

X509ExtendedKeyManager

,

X509ExtendedTrustManager

**Since:**
- 1.7

---

#### public abstract void beginHandshake()
throws
SSLException

Initiates handshaking (initial or renegotiation) on this SSLEngine.

This method is not needed for the initial handshake, as the

wrap()

and

unwrap()

methods will
implicitly call this method if handshaking has not already begun.

Note that the peer may also request a session renegotiation with
this

SSLEngine

by sending the appropriate
session renegotiate handshake message.

Unlike the

SSLSocket#startHandshake()

method, this method does not block
until handshaking is completed.

To force a complete SSL/TLS/DTLS session renegotiation, the current
session should be invalidated prior to calling this method.

Some protocols may not support multiple handshakes on an existing
engine and may throw an

SSLException

.

**Throws:**
- SSLException

- if a problem was encountered while signaling the

SSLEngine

to begin a new handshake.
See the class description for more information on
engine closure.
- IllegalStateException

- if the client/server mode
has not yet been set.

**See Also:**
- SSLSession.invalidate()

---

#### public abstract
SSLEngineResult.HandshakeStatus
getHandshakeStatus()

Returns the current handshake status for this

SSLEngine

.

**Returns:**
- the current

SSLEngineResult.HandshakeStatus

.

---

#### public abstract void setUseClientMode​(boolean mode)

Configures the engine to use client (or server) mode when
handshaking.

This method must be called before any handshaking occurs.
Once handshaking has begun, the mode can not be reset for the
life of this engine.

Servers normally authenticate themselves, and clients
are not required to do so.

**Parameters:**
- mode

- true if the engine should start its handshaking
in "client" mode

**Throws:**
- IllegalArgumentException

- if a mode change is attempted
after the initial handshake has begun.

**See Also:**
- getUseClientMode()

**Implementation Note:**
- The JDK SunJSSE provider implementation default for this mode is false.

---

#### public abstract boolean getUseClientMode()

Returns true if the engine is set to use client mode when
handshaking.

**Returns:**
- true if the engine should do handshaking
in "client" mode

**See Also:**
- setUseClientMode(boolean)

**Implementation Note:**
- The JDK SunJSSE provider implementation returns false unless

setUseClientMode(boolean)

is used to change the mode to true.

---

#### public abstract void setNeedClientAuth​(boolean need)

Configures the engine to

require

client authentication. This
option is only useful for engines in the server mode.

An engine's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setWantClientAuth(boolean)

, if this option is set and
the client chooses not to provide authentication information
about itself,

the negotiations will stop and the engine will
begin its closure procedure

.

Calling this method overrides any previous setting made by
this method or

setWantClientAuth(boolean)

.

**Parameters:**
- need

- set to true if client authentication is required,
or false if no client authentication is desired.

**See Also:**
- getNeedClientAuth()

,

setWantClientAuth(boolean)

,

getWantClientAuth()

,

setUseClientMode(boolean)

---

#### public abstract boolean getNeedClientAuth()

Returns true if the engine will

require

client authentication.
This option is only useful to engines in the server mode.

**Returns:**
- true if client authentication is required,
or false if no client authentication is desired.

**See Also:**
- setNeedClientAuth(boolean)

,

setWantClientAuth(boolean)

,

getWantClientAuth()

,

setUseClientMode(boolean)

---

#### public abstract void setWantClientAuth​(boolean want)

Configures the engine to

request

client authentication.
This option is only useful for engines in the server mode.

An engine's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setNeedClientAuth(boolean)

, if this option is set and
the client chooses not to provide authentication information
about itself,

the negotiations will continue

.

Calling this method overrides any previous setting made by
this method or

setNeedClientAuth(boolean)

.

**Parameters:**
- want

- set to true if client authentication is requested,
or false if no client authentication is desired.

**See Also:**
- getWantClientAuth()

,

setNeedClientAuth(boolean)

,

getNeedClientAuth()

,

setUseClientMode(boolean)

---

#### public abstract boolean getWantClientAuth()

Returns true if the engine will

request

client authentication.
This option is only useful for engines in the server mode.

**Returns:**
- true if client authentication is requested,
or false if no client authentication is desired.

**See Also:**
- setNeedClientAuth(boolean)

,

getNeedClientAuth()

,

setWantClientAuth(boolean)

,

setUseClientMode(boolean)

---

#### public abstract void setEnableSessionCreation​(boolean flag)

Controls whether new SSL sessions may be established by this engine.
If session creations are not allowed, and there are no
existing sessions to resume, there will be no successful
handshaking.

**Parameters:**
- flag

- true indicates that sessions may be created; this
is the default. false indicates that an existing session
must be resumed

**See Also:**
- getEnableSessionCreation()

---

#### public abstract boolean getEnableSessionCreation()

Returns true if new SSL sessions may be established by this engine.

**Returns:**
- true indicates that sessions may be created; this
is the default. false indicates that an existing session
must be resumed

**See Also:**
- setEnableSessionCreation(boolean)

---

#### public
SSLParameters
getSSLParameters()

Returns the SSLParameters in effect for this SSLEngine.
The ciphersuites and protocols of the returned SSLParameters
are always non-null.

**Returns:**
- the SSLParameters in effect for this SSLEngine.

**Since:**
- 1.6

---

#### public void setSSLParameters​(
SSLParameters
params)

Applies SSLParameters to this engine.

This means:

- If

params.getCipherSuites()

is non-null,

setEnabledCipherSuites()

is called with that value.
- If

params.getProtocols()

is non-null,

setEnabledProtocols()

is called with that value.
- If

params.getNeedClientAuth()

or

params.getWantClientAuth()

return

true

,

setNeedClientAuth(true)

and

setWantClientAuth(true)

are called, respectively;
otherwise

setWantClientAuth(false)

is called.
- If

params.getServerNames()

is non-null, the engine will
configure its server names with that value.
- If

params.getSNIMatchers()

is non-null, the engine will
configure its SNI matchers with that value.

**Parameters:**
- params

- the parameters

**Throws:**
- IllegalArgumentException

- if the setEnabledCipherSuites() or
the setEnabledProtocols() call fails

**Since:**
- 1.6

---

#### public
String
getApplicationProtocol()

Returns the most recent application protocol value negotiated for this
connection.

If supported by the underlying SSL/TLS/DTLS implementation,
application name negotiation mechanisms such as

RFC 7301

, the
Application-Layer Protocol Negotiation (ALPN), can negotiate
application-level values between peers.

**Returns:**
- null if it has not yet been determined if application
protocols might be used for this connection, an empty

String

if application protocols values will not
be used, or a non-empty application protocol

String

if a value was successfully negotiated.

**Throws:**
- UnsupportedOperationException

- if the underlying provider
does not implement the operation.

**Since:**
- 9

**Implementation Requirements:**
- The implementation in this class throws

UnsupportedOperationException

and performs no other action.

---

#### public
String
getHandshakeApplicationProtocol()

Returns the application protocol value negotiated on a SSL/TLS
handshake currently in progress.

Like

getHandshakeSession()

,
a connection may be in the middle of a handshake. The
application protocol may or may not yet be available.

**Returns:**
- null if it has not yet been determined if application
protocols might be used for this handshake, an empty

String

if application protocols values will not
be used, or a non-empty application protocol

String

if a value was successfully negotiated.

**Throws:**
- UnsupportedOperationException

- if the underlying provider
does not implement the operation.

**Since:**
- 9

**Implementation Requirements:**
- The implementation in this class throws

UnsupportedOperationException

and performs no other action.

---

#### public void setHandshakeApplicationProtocolSelector​(
BiFunction
<
SSLEngine
,​
List
<
String
>,​
String
> selector)

Registers a callback function that selects an application protocol
value for a SSL/TLS/DTLS handshake.
The function overrides any values supplied using

SSLParameters.setApplicationProtocols

and it supports the following
type parameters:

For example, the following call registers a callback function that
examines the TLS handshake parameters and selects an application protocol
name:

```java
serverEngine.setHandshakeApplicationProtocolSelector(
(serverEngine, clientProtocols) -> {
SSLSession session = serverEngine.getHandshakeSession();
return chooseApplicationProtocol(
serverEngine,
clientProtocols,
session.getProtocol(),
session.getCipherSuite());
});
```

---

#### public
BiFunction
<
SSLEngine
,​
List
<
String
>,​
String
> getHandshakeApplicationProtocolSelector()

Retrieves the callback function that selects an application protocol
value during a SSL/TLS/DTLS handshake.
See

setHandshakeApplicationProtocolSelector

for the function's type parameters.

**Returns:**
- the callback function, or null if none has been set.

**Throws:**
- UnsupportedOperationException

- if the underlying provider
does not implement the operation.

**Since:**
- 9

**Implementation Requirements:**
- The implementation in this class throws

UnsupportedOperationException

and performs no other action.

---

### Additional Sections

#### Class SSLEngine

java.lang.Object

- javax.net.ssl.SSLEngine

javax.net.ssl.SSLEngine

```java
public abstract class
SSLEngine

extends
Object
```

A class which enables secure communications using protocols such as
the Secure Sockets Layer (SSL) or

IETF RFC 2246 "Transport
Layer Security" (TLS)

protocols, but is transport independent.

The secure communications modes include:

- Integrity Protection

. SSL/TLS/DTLS protects against
modification of messages by an active wiretapper.

Authentication

. In most modes, SSL/TLS/DTLS provides
peer authentication. Servers are usually authenticated, and
clients may be authenticated as requested by servers.

Confidentiality (Privacy Protection)

. In most
modes, SSL/TLS/DTLS encrypts data being sent between client and
server. This protects the confidentiality of data, so that
passive wiretappers won't see sensitive data such as financial
information or personal information of many kinds.

These kinds of protection are specified by a "cipher suite", which
is a combination of cryptographic algorithms used by a given SSL
connection. During the negotiation process, the two endpoints must
agree on a cipher suite that is available in both environments. If
there is no such suite in common, no SSL connection can be
established, and no data can be exchanged.

The cipher suite used is established by a negotiation process called
"handshaking". The goal of this process is to create or rejoin a
"session", which may protect many connections over time. After
handshaking has completed, you can access session attributes by
using the

getSession()

method.

The

SSLSocket

class provides much of the same security
functionality, but all of the inbound and outbound data is
automatically transported using the underlying

Socket

, which by design uses a blocking model.
While this is appropriate for many applications, this model does not
provide the scalability required by large servers.

The primary distinction of an

SSLEngine

is that it
operates on inbound and outbound byte streams, independent of the
transport mechanism. It is the responsibility of the

SSLEngine

user to arrange for reliable I/O transport to
the peer. By separating the SSL/TLS/DTLS abstraction from the I/O
transport mechanism, the

SSLEngine

can be used for a
wide variety of I/O types, such as

non-blocking I/O (polling)

,

selectable non-blocking I/O

,

Socket

and the
traditional Input/OutputStreams, local

ByteBuffers

or byte arrays,

future asynchronous
I/O models

, and so on.

At a high level, the

SSLEngine

appears thus:

```java
app data

| ^
| | |
v | |
+----+-----|-----+----+
| | |
| SSL|Engine |
wrap() | | | unwrap()
| OUTBOUND | INBOUND |
| | |
+----+-----|-----+----+
| | ^
| | |
v |

net data
```

Application data (also known as plaintext or cleartext) is data which
is produced or consumed by an application. Its counterpart is
network data, which consists of either handshaking and/or ciphertext
(encrypted) data, and destined to be transported via an I/O
mechanism. Inbound data is data which has been received from the
peer, and outbound data is destined for the peer.

(In the context of an

SSLEngine

, the term "handshake
data" is taken to mean any data exchanged to establish and control a
secure connection. Handshake data includes the SSL/TLS/DTLS messages
"alert", "change_cipher_spec," and "handshake.")

There are five distinct phases to an

SSLEngine

.

- Creation - The

SSLEngine

has been created and
initialized, but has not yet been used. During this phase, an
application may set any

SSLEngine

-specific settings
(enabled cipher suites, whether the

SSLEngine

should
handshake in client or server mode, and so on). Once
handshaking has begun, though, any new settings (except
client/server mode, see below) will be used for
the next handshake.

Initial Handshake - The initial handshake is a procedure by
which the two peers exchange communication parameters until an
SSLSession is established. Application data can not be sent during
this phase.

Application Data - Once the communication parameters have
been established and the handshake is complete, application data
may flow through the

SSLEngine

. Outbound
application messages are encrypted and integrity protected,
and inbound messages reverse the process.

Rehandshaking - Either side may request a renegotiation of
the session at any time during the Application Data phase. New
handshaking data can be intermixed among the application data.
Before starting the rehandshake phase, the application may
reset the SSL/TLS/DTLS communication parameters such as the list of
enabled ciphersuites and whether to use client authentication,
but can not change between client/server modes. As before, once
handshaking has begun, any new

SSLEngine

configuration settings will not be used until the next
handshake.

Closure - When the connection is no longer needed, the client
and the server applications should each close both sides of their
respective connections. For

SSLEngine

objects, an
application should call

closeOutbound()

and
send any remaining messages to the peer. Likewise, an application
should receive any remaining messages from the peer before calling

closeInbound()

. The underlying transport mechanism
can then be closed after both sides of the

SSLEngine

have
been closed. If the connection is not closed in an orderly manner
(for example

closeInbound()

is called before the
peer's write closure notification has been received), exceptions
will be raised to indicate that an error has occurred. Once an
engine is closed, it is not reusable: a new

SSLEngine

must be created.

An

SSLEngine

is created by calling

SSLContext.createSSLEngine()

from an initialized

SSLContext

. Any configuration
parameters should be set before making the first call to

wrap()

,

unwrap()

, or

beginHandshake()

. These methods all trigger the
initial handshake.

Data moves through the engine by calling

wrap()

or

unwrap()

on outbound or inbound data, respectively. Depending on
the state of the

SSLEngine

, a

wrap()

call
may consume application data from the source buffer and may produce
network data in the destination buffer. The outbound data
may contain application and/or handshake data. A call to

unwrap()

will examine the source buffer and may
advance the handshake if the data is handshaking information, or
may place application data in the destination buffer if the data
is application. The state of the underlying SSL/TLS/DTLS algorithm
will determine when data is consumed and produced.

Calls to

wrap()

and

unwrap()

return an

SSLEngineResult

which indicates the status of the
operation, and (optionally) how to interact with the engine to make
progress.

The

SSLEngine

produces/consumes complete SSL/TLS/DTLS
packets only, and does not store application data internally between
calls to

wrap()/unwrap()

. Thus input and output

ByteBuffer

s must be sized appropriately to hold the
maximum record that can be produced. Calls to

SSLSession.getPacketBufferSize()

and

SSLSession.getApplicationBufferSize()

should be used to determine
the appropriate buffer sizes. The size of the outbound application
data buffer generally does not matter. If buffer conditions do not
allow for the proper consumption/production of data, the application
must determine (via

SSLEngineResult

) and correct the
problem, and then try the call again.

For example,

unwrap()

will return a

SSLEngineResult.Status.BUFFER_OVERFLOW

result if the engine
determines that there is not enough destination buffer space available.
Applications should call

SSLSession.getApplicationBufferSize()

and compare that value with the space available in the destination buffer,
enlarging the buffer if necessary. Similarly, if

unwrap()

were to return a

SSLEngineResult.Status.BUFFER_UNDERFLOW

, the
application should call

SSLSession.getPacketBufferSize()

to ensure
that the source buffer has enough room to hold a record (enlarging if
necessary), and then obtain more inbound data.

```java
SSLEngineResult r = engine.unwrap(src, dst);
switch (r.getStatus()) {
BUFFER_OVERFLOW:
// Could attempt to drain the dst buffer of any already obtained
// data, but we'll just increase it to the size needed.
int appSize = engine.getSession().getApplicationBufferSize();
ByteBuffer b = ByteBuffer.allocate(appSize + dst.position());
dst.flip();
b.put(dst);
dst = b;
// retry the operation.
break;
BUFFER_UNDERFLOW:
int netSize = engine.getSession().getPacketBufferSize();
// Resize buffer if needed.
if (netSize > dst.capacity()) {
ByteBuffer b = ByteBuffer.allocate(netSize);
src.flip();
b.put(src);
src = b;
}
// Obtain more inbound network data for src,
// then retry the operation.
break;
// other cases: CLOSED, OK.
}
```

Unlike

SSLSocket

, all methods of SSLEngine are
non-blocking.

SSLEngine

implementations may
require the results of tasks that may take an extended period of
time to complete, or may even block. For example, a TrustManager
may need to connect to a remote certificate validation service,
or a KeyManager might need to prompt a user to determine which
certificate to use as part of client authentication. Additionally,
creating cryptographic signatures and verifying them can be slow,
seemingly blocking.

For any operation which may potentially block, the

SSLEngine

will create a

Runnable

delegated task. When

SSLEngineResult

indicates that a
delegated task result is needed, the application must call

getDelegatedTask()

to obtain an outstanding delegated task and
call its

run()

method (possibly using
a different thread depending on the compute strategy). The
application should continue obtaining delegated tasks until no more
exist, and try the original operation again.

At the end of a communication session, applications should properly
close the SSL/TLS/DTLS link. The SSL/TLS/DTLS protocols have closure
handshake messages, and these messages should be communicated to the
peer before releasing the

SSLEngine

and closing the
underlying transport mechanism. A close can be initiated by one of:
an SSLException, an inbound closure handshake message, or one of the
close methods. In all cases, closure handshake messages are
generated by the engine, and

wrap()

should be repeatedly
called until the resulting

SSLEngineResult

's status
returns "CLOSED", or

isOutboundDone()

returns true. All
data obtained from the

wrap()

method should be sent to the
peer.

closeOutbound()

is used to signal the engine that the
application will not be sending any more data.

A peer will signal its intent to close by sending its own closure
handshake message. After this message has been received and
processed by the local

SSLEngine

's

unwrap()

call, the application can detect the close by calling

unwrap()

and looking for a

SSLEngineResult

with status "CLOSED", or if

isInboundDone()

returns true.
If for some reason the peer closes the communication link without
sending the proper SSL/TLS/DTLS closure message, the application can
detect the end-of-stream and can signal the engine via

closeInbound()

that there will no more inbound messages to
process. Some applications might choose to require orderly shutdown
messages from a peer, in which case they can check that the closure
was generated by a handshake message and not by an end-of-stream
condition.

There are two groups of cipher suites which you will need to know
about when managing cipher suites:

- Supported

cipher suites: all the suites which are
supported by the SSL implementation. This list is reported
using

getSupportedCipherSuites()

.

Enabled

cipher suites, which may be fewer than
the full set of supported suites. This group is set using the

setEnabledCipherSuites(String [])

method, and
queried using the

getEnabledCipherSuites()

method.
Initially, a default set of cipher suites will be enabled on a
new engine that represents the minimum suggested
configuration.

Implementation defaults require that only cipher suites which
authenticate servers and provide confidentiality be enabled by
default. Only if both sides explicitly agree to unauthenticated
and/or non-private (unencrypted) communications will such a
cipher suite be selected.

Each SSL/TLS/DTLS connection must have one client and one server, thus
each endpoint must decide which role to assume. This choice determines
who begins the handshaking process as well as which type of messages
should be sent by each party. The method

setUseClientMode(boolean)

configures the mode. Note that the
default mode for a new

SSLEngine

is provider-specific.
Applications should set the mode explicitly before invoking other
methods of the

SSLEngine

. Once the initial handshaking has
started, an

SSLEngine

can not switch between client and server
modes, even when performing renegotiations.

Applications might choose to process delegated tasks in different
threads. When an

SSLEngine

is created, the current

AccessControlContext

is saved. All future delegated tasks will be processed using this
context: that is, all access control decisions will be made using the
context captured at engine creation.

Concurrency Notes

:
There are two concurrency issues to be aware of:

- The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

**Since:** 1.5
**See Also:** SSLContext

,

SSLSocket

,

SSLServerSocket

,

SSLSession

,

Socket

public abstract class

SSLEngine

extends

Object

A class which enables secure communications using protocols such as
the Secure Sockets Layer (SSL) or

IETF RFC 2246 "Transport
Layer Security" (TLS)

protocols, but is transport independent.

The secure communications modes include:

- Integrity Protection

. SSL/TLS/DTLS protects against
modification of messages by an active wiretapper.

Authentication

. In most modes, SSL/TLS/DTLS provides
peer authentication. Servers are usually authenticated, and
clients may be authenticated as requested by servers.

Confidentiality (Privacy Protection)

. In most
modes, SSL/TLS/DTLS encrypts data being sent between client and
server. This protects the confidentiality of data, so that
passive wiretappers won't see sensitive data such as financial
information or personal information of many kinds.

These kinds of protection are specified by a "cipher suite", which
is a combination of cryptographic algorithms used by a given SSL
connection. During the negotiation process, the two endpoints must
agree on a cipher suite that is available in both environments. If
there is no such suite in common, no SSL connection can be
established, and no data can be exchanged.

The cipher suite used is established by a negotiation process called
"handshaking". The goal of this process is to create or rejoin a
"session", which may protect many connections over time. After
handshaking has completed, you can access session attributes by
using the

getSession()

method.

The

SSLSocket

class provides much of the same security
functionality, but all of the inbound and outbound data is
automatically transported using the underlying

Socket

, which by design uses a blocking model.
While this is appropriate for many applications, this model does not
provide the scalability required by large servers.

The primary distinction of an

SSLEngine

is that it
operates on inbound and outbound byte streams, independent of the
transport mechanism. It is the responsibility of the

SSLEngine

user to arrange for reliable I/O transport to
the peer. By separating the SSL/TLS/DTLS abstraction from the I/O
transport mechanism, the

SSLEngine

can be used for a
wide variety of I/O types, such as

non-blocking I/O (polling)

,

selectable non-blocking I/O

,

Socket

and the
traditional Input/OutputStreams, local

ByteBuffers

or byte arrays,

future asynchronous
I/O models

, and so on.

At a high level, the

SSLEngine

appears thus:

```java
app data

| ^
| | |
v | |
+----+-----|-----+----+
| | |
| SSL|Engine |
wrap() | | | unwrap()
| OUTBOUND | INBOUND |
| | |
+----+-----|-----+----+
| | ^
| | |
v |

net data
```

Application data (also known as plaintext or cleartext) is data which
is produced or consumed by an application. Its counterpart is
network data, which consists of either handshaking and/or ciphertext
(encrypted) data, and destined to be transported via an I/O
mechanism. Inbound data is data which has been received from the
peer, and outbound data is destined for the peer.

(In the context of an

SSLEngine

, the term "handshake
data" is taken to mean any data exchanged to establish and control a
secure connection. Handshake data includes the SSL/TLS/DTLS messages
"alert", "change_cipher_spec," and "handshake.")

There are five distinct phases to an

SSLEngine

.

- Creation - The

SSLEngine

has been created and
initialized, but has not yet been used. During this phase, an
application may set any

SSLEngine

-specific settings
(enabled cipher suites, whether the

SSLEngine

should
handshake in client or server mode, and so on). Once
handshaking has begun, though, any new settings (except
client/server mode, see below) will be used for
the next handshake.

Initial Handshake - The initial handshake is a procedure by
which the two peers exchange communication parameters until an
SSLSession is established. Application data can not be sent during
this phase.

Application Data - Once the communication parameters have
been established and the handshake is complete, application data
may flow through the

SSLEngine

. Outbound
application messages are encrypted and integrity protected,
and inbound messages reverse the process.

Rehandshaking - Either side may request a renegotiation of
the session at any time during the Application Data phase. New
handshaking data can be intermixed among the application data.
Before starting the rehandshake phase, the application may
reset the SSL/TLS/DTLS communication parameters such as the list of
enabled ciphersuites and whether to use client authentication,
but can not change between client/server modes. As before, once
handshaking has begun, any new

SSLEngine

configuration settings will not be used until the next
handshake.

Closure - When the connection is no longer needed, the client
and the server applications should each close both sides of their
respective connections. For

SSLEngine

objects, an
application should call

closeOutbound()

and
send any remaining messages to the peer. Likewise, an application
should receive any remaining messages from the peer before calling

closeInbound()

. The underlying transport mechanism
can then be closed after both sides of the

SSLEngine

have
been closed. If the connection is not closed in an orderly manner
(for example

closeInbound()

is called before the
peer's write closure notification has been received), exceptions
will be raised to indicate that an error has occurred. Once an
engine is closed, it is not reusable: a new

SSLEngine

must be created.

An

SSLEngine

is created by calling

SSLContext.createSSLEngine()

from an initialized

SSLContext

. Any configuration
parameters should be set before making the first call to

wrap()

,

unwrap()

, or

beginHandshake()

. These methods all trigger the
initial handshake.

Data moves through the engine by calling

wrap()

or

unwrap()

on outbound or inbound data, respectively. Depending on
the state of the

SSLEngine

, a

wrap()

call
may consume application data from the source buffer and may produce
network data in the destination buffer. The outbound data
may contain application and/or handshake data. A call to

unwrap()

will examine the source buffer and may
advance the handshake if the data is handshaking information, or
may place application data in the destination buffer if the data
is application. The state of the underlying SSL/TLS/DTLS algorithm
will determine when data is consumed and produced.

Calls to

wrap()

and

unwrap()

return an

SSLEngineResult

which indicates the status of the
operation, and (optionally) how to interact with the engine to make
progress.

The

SSLEngine

produces/consumes complete SSL/TLS/DTLS
packets only, and does not store application data internally between
calls to

wrap()/unwrap()

. Thus input and output

ByteBuffer

s must be sized appropriately to hold the
maximum record that can be produced. Calls to

SSLSession.getPacketBufferSize()

and

SSLSession.getApplicationBufferSize()

should be used to determine
the appropriate buffer sizes. The size of the outbound application
data buffer generally does not matter. If buffer conditions do not
allow for the proper consumption/production of data, the application
must determine (via

SSLEngineResult

) and correct the
problem, and then try the call again.

For example,

unwrap()

will return a

SSLEngineResult.Status.BUFFER_OVERFLOW

result if the engine
determines that there is not enough destination buffer space available.
Applications should call

SSLSession.getApplicationBufferSize()

and compare that value with the space available in the destination buffer,
enlarging the buffer if necessary. Similarly, if

unwrap()

were to return a

SSLEngineResult.Status.BUFFER_UNDERFLOW

, the
application should call

SSLSession.getPacketBufferSize()

to ensure
that the source buffer has enough room to hold a record (enlarging if
necessary), and then obtain more inbound data.

```java
SSLEngineResult r = engine.unwrap(src, dst);
switch (r.getStatus()) {
BUFFER_OVERFLOW:
// Could attempt to drain the dst buffer of any already obtained
// data, but we'll just increase it to the size needed.
int appSize = engine.getSession().getApplicationBufferSize();
ByteBuffer b = ByteBuffer.allocate(appSize + dst.position());
dst.flip();
b.put(dst);
dst = b;
// retry the operation.
break;
BUFFER_UNDERFLOW:
int netSize = engine.getSession().getPacketBufferSize();
// Resize buffer if needed.
if (netSize > dst.capacity()) {
ByteBuffer b = ByteBuffer.allocate(netSize);
src.flip();
b.put(src);
src = b;
}
// Obtain more inbound network data for src,
// then retry the operation.
break;
// other cases: CLOSED, OK.
}
```

Unlike

SSLSocket

, all methods of SSLEngine are
non-blocking.

SSLEngine

implementations may
require the results of tasks that may take an extended period of
time to complete, or may even block. For example, a TrustManager
may need to connect to a remote certificate validation service,
or a KeyManager might need to prompt a user to determine which
certificate to use as part of client authentication. Additionally,
creating cryptographic signatures and verifying them can be slow,
seemingly blocking.

For any operation which may potentially block, the

SSLEngine

will create a

Runnable

delegated task. When

SSLEngineResult

indicates that a
delegated task result is needed, the application must call

getDelegatedTask()

to obtain an outstanding delegated task and
call its

run()

method (possibly using
a different thread depending on the compute strategy). The
application should continue obtaining delegated tasks until no more
exist, and try the original operation again.

At the end of a communication session, applications should properly
close the SSL/TLS/DTLS link. The SSL/TLS/DTLS protocols have closure
handshake messages, and these messages should be communicated to the
peer before releasing the

SSLEngine

and closing the
underlying transport mechanism. A close can be initiated by one of:
an SSLException, an inbound closure handshake message, or one of the
close methods. In all cases, closure handshake messages are
generated by the engine, and

wrap()

should be repeatedly
called until the resulting

SSLEngineResult

's status
returns "CLOSED", or

isOutboundDone()

returns true. All
data obtained from the

wrap()

method should be sent to the
peer.

closeOutbound()

is used to signal the engine that the
application will not be sending any more data.

A peer will signal its intent to close by sending its own closure
handshake message. After this message has been received and
processed by the local

SSLEngine

's

unwrap()

call, the application can detect the close by calling

unwrap()

and looking for a

SSLEngineResult

with status "CLOSED", or if

isInboundDone()

returns true.
If for some reason the peer closes the communication link without
sending the proper SSL/TLS/DTLS closure message, the application can
detect the end-of-stream and can signal the engine via

closeInbound()

that there will no more inbound messages to
process. Some applications might choose to require orderly shutdown
messages from a peer, in which case they can check that the closure
was generated by a handshake message and not by an end-of-stream
condition.

There are two groups of cipher suites which you will need to know
about when managing cipher suites:

- Supported

cipher suites: all the suites which are
supported by the SSL implementation. This list is reported
using

getSupportedCipherSuites()

.

Enabled

cipher suites, which may be fewer than
the full set of supported suites. This group is set using the

setEnabledCipherSuites(String [])

method, and
queried using the

getEnabledCipherSuites()

method.
Initially, a default set of cipher suites will be enabled on a
new engine that represents the minimum suggested
configuration.

Implementation defaults require that only cipher suites which
authenticate servers and provide confidentiality be enabled by
default. Only if both sides explicitly agree to unauthenticated
and/or non-private (unencrypted) communications will such a
cipher suite be selected.

Each SSL/TLS/DTLS connection must have one client and one server, thus
each endpoint must decide which role to assume. This choice determines
who begins the handshaking process as well as which type of messages
should be sent by each party. The method

setUseClientMode(boolean)

configures the mode. Note that the
default mode for a new

SSLEngine

is provider-specific.
Applications should set the mode explicitly before invoking other
methods of the

SSLEngine

. Once the initial handshaking has
started, an

SSLEngine

can not switch between client and server
modes, even when performing renegotiations.

Applications might choose to process delegated tasks in different
threads. When an

SSLEngine

is created, the current

AccessControlContext

is saved. All future delegated tasks will be processed using this
context: that is, all access control decisions will be made using the
context captured at engine creation.

Concurrency Notes

:
There are two concurrency issues to be aware of:

- The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

The secure communications modes include:

- Integrity Protection

. SSL/TLS/DTLS protects against
modification of messages by an active wiretapper.

Authentication

. In most modes, SSL/TLS/DTLS provides
peer authentication. Servers are usually authenticated, and
clients may be authenticated as requested by servers.

Confidentiality (Privacy Protection)

. In most
modes, SSL/TLS/DTLS encrypts data being sent between client and
server. This protects the confidentiality of data, so that
passive wiretappers won't see sensitive data such as financial
information or personal information of many kinds.

These kinds of protection are specified by a "cipher suite", which
is a combination of cryptographic algorithms used by a given SSL
connection. During the negotiation process, the two endpoints must
agree on a cipher suite that is available in both environments. If
there is no such suite in common, no SSL connection can be
established, and no data can be exchanged.

The cipher suite used is established by a negotiation process called
"handshaking". The goal of this process is to create or rejoin a
"session", which may protect many connections over time. After
handshaking has completed, you can access session attributes by
using the

getSession()

method.

The

SSLSocket

class provides much of the same security
functionality, but all of the inbound and outbound data is
automatically transported using the underlying

Socket

, which by design uses a blocking model.
While this is appropriate for many applications, this model does not
provide the scalability required by large servers.

The primary distinction of an

SSLEngine

is that it
operates on inbound and outbound byte streams, independent of the
transport mechanism. It is the responsibility of the

SSLEngine

user to arrange for reliable I/O transport to
the peer. By separating the SSL/TLS/DTLS abstraction from the I/O
transport mechanism, the

SSLEngine

can be used for a
wide variety of I/O types, such as

non-blocking I/O (polling)

,

selectable non-blocking I/O

,

Socket

and the
traditional Input/OutputStreams, local

ByteBuffers

or byte arrays,

future asynchronous
I/O models

, and so on.

At a high level, the

SSLEngine

appears thus:

```java
app data

| ^
| | |
v | |
+----+-----|-----+----+
| | |
| SSL|Engine |
wrap() | | | unwrap()
| OUTBOUND | INBOUND |
| | |
+----+-----|-----+----+
| | ^
| | |
v |

net data
```

Application data (also known as plaintext or cleartext) is data which
is produced or consumed by an application. Its counterpart is
network data, which consists of either handshaking and/or ciphertext
(encrypted) data, and destined to be transported via an I/O
mechanism. Inbound data is data which has been received from the
peer, and outbound data is destined for the peer.

(In the context of an

SSLEngine

, the term "handshake
data" is taken to mean any data exchanged to establish and control a
secure connection. Handshake data includes the SSL/TLS/DTLS messages
"alert", "change_cipher_spec," and "handshake.")

There are five distinct phases to an

SSLEngine

.

- Creation - The

SSLEngine

has been created and
initialized, but has not yet been used. During this phase, an
application may set any

SSLEngine

-specific settings
(enabled cipher suites, whether the

SSLEngine

should
handshake in client or server mode, and so on). Once
handshaking has begun, though, any new settings (except
client/server mode, see below) will be used for
the next handshake.

Initial Handshake - The initial handshake is a procedure by
which the two peers exchange communication parameters until an
SSLSession is established. Application data can not be sent during
this phase.

Application Data - Once the communication parameters have
been established and the handshake is complete, application data
may flow through the

SSLEngine

. Outbound
application messages are encrypted and integrity protected,
and inbound messages reverse the process.

Rehandshaking - Either side may request a renegotiation of
the session at any time during the Application Data phase. New
handshaking data can be intermixed among the application data.
Before starting the rehandshake phase, the application may
reset the SSL/TLS/DTLS communication parameters such as the list of
enabled ciphersuites and whether to use client authentication,
but can not change between client/server modes. As before, once
handshaking has begun, any new

SSLEngine

configuration settings will not be used until the next
handshake.

Closure - When the connection is no longer needed, the client
and the server applications should each close both sides of their
respective connections. For

SSLEngine

objects, an
application should call

closeOutbound()

and
send any remaining messages to the peer. Likewise, an application
should receive any remaining messages from the peer before calling

closeInbound()

. The underlying transport mechanism
can then be closed after both sides of the

SSLEngine

have
been closed. If the connection is not closed in an orderly manner
(for example

closeInbound()

is called before the
peer's write closure notification has been received), exceptions
will be raised to indicate that an error has occurred. Once an
engine is closed, it is not reusable: a new

SSLEngine

must be created.

An

SSLEngine

is created by calling

SSLContext.createSSLEngine()

from an initialized

SSLContext

. Any configuration
parameters should be set before making the first call to

wrap()

,

unwrap()

, or

beginHandshake()

. These methods all trigger the
initial handshake.

Data moves through the engine by calling

wrap()

or

unwrap()

on outbound or inbound data, respectively. Depending on
the state of the

SSLEngine

, a

wrap()

call
may consume application data from the source buffer and may produce
network data in the destination buffer. The outbound data
may contain application and/or handshake data. A call to

unwrap()

will examine the source buffer and may
advance the handshake if the data is handshaking information, or
may place application data in the destination buffer if the data
is application. The state of the underlying SSL/TLS/DTLS algorithm
will determine when data is consumed and produced.

Calls to

wrap()

and

unwrap()

return an

SSLEngineResult

which indicates the status of the
operation, and (optionally) how to interact with the engine to make
progress.

The

SSLEngine

produces/consumes complete SSL/TLS/DTLS
packets only, and does not store application data internally between
calls to

wrap()/unwrap()

. Thus input and output

ByteBuffer

s must be sized appropriately to hold the
maximum record that can be produced. Calls to

SSLSession.getPacketBufferSize()

and

SSLSession.getApplicationBufferSize()

should be used to determine
the appropriate buffer sizes. The size of the outbound application
data buffer generally does not matter. If buffer conditions do not
allow for the proper consumption/production of data, the application
must determine (via

SSLEngineResult

) and correct the
problem, and then try the call again.

For example,

unwrap()

will return a

SSLEngineResult.Status.BUFFER_OVERFLOW

result if the engine
determines that there is not enough destination buffer space available.
Applications should call

SSLSession.getApplicationBufferSize()

and compare that value with the space available in the destination buffer,
enlarging the buffer if necessary. Similarly, if

unwrap()

were to return a

SSLEngineResult.Status.BUFFER_UNDERFLOW

, the
application should call

SSLSession.getPacketBufferSize()

to ensure
that the source buffer has enough room to hold a record (enlarging if
necessary), and then obtain more inbound data.

```java
SSLEngineResult r = engine.unwrap(src, dst);
switch (r.getStatus()) {
BUFFER_OVERFLOW:
// Could attempt to drain the dst buffer of any already obtained
// data, but we'll just increase it to the size needed.
int appSize = engine.getSession().getApplicationBufferSize();
ByteBuffer b = ByteBuffer.allocate(appSize + dst.position());
dst.flip();
b.put(dst);
dst = b;
// retry the operation.
break;
BUFFER_UNDERFLOW:
int netSize = engine.getSession().getPacketBufferSize();
// Resize buffer if needed.
if (netSize > dst.capacity()) {
ByteBuffer b = ByteBuffer.allocate(netSize);
src.flip();
b.put(src);
src = b;
}
// Obtain more inbound network data for src,
// then retry the operation.
break;
// other cases: CLOSED, OK.
}
```

Unlike

SSLSocket

, all methods of SSLEngine are
non-blocking.

SSLEngine

implementations may
require the results of tasks that may take an extended period of
time to complete, or may even block. For example, a TrustManager
may need to connect to a remote certificate validation service,
or a KeyManager might need to prompt a user to determine which
certificate to use as part of client authentication. Additionally,
creating cryptographic signatures and verifying them can be slow,
seemingly blocking.

For any operation which may potentially block, the

SSLEngine

will create a

Runnable

delegated task. When

SSLEngineResult

indicates that a
delegated task result is needed, the application must call

getDelegatedTask()

to obtain an outstanding delegated task and
call its

run()

method (possibly using
a different thread depending on the compute strategy). The
application should continue obtaining delegated tasks until no more
exist, and try the original operation again.

At the end of a communication session, applications should properly
close the SSL/TLS/DTLS link. The SSL/TLS/DTLS protocols have closure
handshake messages, and these messages should be communicated to the
peer before releasing the

SSLEngine

and closing the
underlying transport mechanism. A close can be initiated by one of:
an SSLException, an inbound closure handshake message, or one of the
close methods. In all cases, closure handshake messages are
generated by the engine, and

wrap()

should be repeatedly
called until the resulting

SSLEngineResult

's status
returns "CLOSED", or

isOutboundDone()

returns true. All
data obtained from the

wrap()

method should be sent to the
peer.

closeOutbound()

is used to signal the engine that the
application will not be sending any more data.

A peer will signal its intent to close by sending its own closure
handshake message. After this message has been received and
processed by the local

SSLEngine

's

unwrap()

call, the application can detect the close by calling

unwrap()

and looking for a

SSLEngineResult

with status "CLOSED", or if

isInboundDone()

returns true.
If for some reason the peer closes the communication link without
sending the proper SSL/TLS/DTLS closure message, the application can
detect the end-of-stream and can signal the engine via

closeInbound()

that there will no more inbound messages to
process. Some applications might choose to require orderly shutdown
messages from a peer, in which case they can check that the closure
was generated by a handshake message and not by an end-of-stream
condition.

There are two groups of cipher suites which you will need to know
about when managing cipher suites:

- Supported

cipher suites: all the suites which are
supported by the SSL implementation. This list is reported
using

getSupportedCipherSuites()

.

Enabled

cipher suites, which may be fewer than
the full set of supported suites. This group is set using the

setEnabledCipherSuites(String [])

method, and
queried using the

getEnabledCipherSuites()

method.
Initially, a default set of cipher suites will be enabled on a
new engine that represents the minimum suggested
configuration.

Implementation defaults require that only cipher suites which
authenticate servers and provide confidentiality be enabled by
default. Only if both sides explicitly agree to unauthenticated
and/or non-private (unencrypted) communications will such a
cipher suite be selected.

Each SSL/TLS/DTLS connection must have one client and one server, thus
each endpoint must decide which role to assume. This choice determines
who begins the handshaking process as well as which type of messages
should be sent by each party. The method

setUseClientMode(boolean)

configures the mode. Note that the
default mode for a new

SSLEngine

is provider-specific.
Applications should set the mode explicitly before invoking other
methods of the

SSLEngine

. Once the initial handshaking has
started, an

SSLEngine

can not switch between client and server
modes, even when performing renegotiations.

Applications might choose to process delegated tasks in different
threads. When an

SSLEngine

is created, the current

AccessControlContext

is saved. All future delegated tasks will be processed using this
context: that is, all access control decisions will be made using the
context captured at engine creation.

Concurrency Notes

:
There are two concurrency issues to be aware of:

- The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

Integrity Protection

. SSL/TLS/DTLS protects against
modification of messages by an active wiretapper.

Authentication

. In most modes, SSL/TLS/DTLS provides
peer authentication. Servers are usually authenticated, and
clients may be authenticated as requested by servers.

Confidentiality (Privacy Protection)

. In most
modes, SSL/TLS/DTLS encrypts data being sent between client and
server. This protects the confidentiality of data, so that
passive wiretappers won't see sensitive data such as financial
information or personal information of many kinds.

The cipher suite used is established by a negotiation process called
"handshaking". The goal of this process is to create or rejoin a
"session", which may protect many connections over time. After
handshaking has completed, you can access session attributes by
using the

getSession()

method.

The

SSLSocket

class provides much of the same security
functionality, but all of the inbound and outbound data is
automatically transported using the underlying

Socket

, which by design uses a blocking model.
While this is appropriate for many applications, this model does not
provide the scalability required by large servers.

The primary distinction of an

SSLEngine

is that it
operates on inbound and outbound byte streams, independent of the
transport mechanism. It is the responsibility of the

SSLEngine

user to arrange for reliable I/O transport to
the peer. By separating the SSL/TLS/DTLS abstraction from the I/O
transport mechanism, the

SSLEngine

can be used for a
wide variety of I/O types, such as

non-blocking I/O (polling)

,

selectable non-blocking I/O

,

Socket

and the
traditional Input/OutputStreams, local

ByteBuffers

or byte arrays,

future asynchronous
I/O models

, and so on.

At a high level, the

SSLEngine

appears thus:

```java
app data

| ^
| | |
v | |
+----+-----|-----+----+
| | |
| SSL|Engine |
wrap() | | | unwrap()
| OUTBOUND | INBOUND |
| | |
+----+-----|-----+----+
| | ^
| | |
v |

net data
```

Application data (also known as plaintext or cleartext) is data which
is produced or consumed by an application. Its counterpart is
network data, which consists of either handshaking and/or ciphertext
(encrypted) data, and destined to be transported via an I/O
mechanism. Inbound data is data which has been received from the
peer, and outbound data is destined for the peer.

(In the context of an

SSLEngine

, the term "handshake
data" is taken to mean any data exchanged to establish and control a
secure connection. Handshake data includes the SSL/TLS/DTLS messages
"alert", "change_cipher_spec," and "handshake.")

There are five distinct phases to an

SSLEngine

.

- Creation - The

SSLEngine

has been created and
initialized, but has not yet been used. During this phase, an
application may set any

SSLEngine

-specific settings
(enabled cipher suites, whether the

SSLEngine

should
handshake in client or server mode, and so on). Once
handshaking has begun, though, any new settings (except
client/server mode, see below) will be used for
the next handshake.

Initial Handshake - The initial handshake is a procedure by
which the two peers exchange communication parameters until an
SSLSession is established. Application data can not be sent during
this phase.

Application Data - Once the communication parameters have
been established and the handshake is complete, application data
may flow through the

SSLEngine

. Outbound
application messages are encrypted and integrity protected,
and inbound messages reverse the process.

Rehandshaking - Either side may request a renegotiation of
the session at any time during the Application Data phase. New
handshaking data can be intermixed among the application data.
Before starting the rehandshake phase, the application may
reset the SSL/TLS/DTLS communication parameters such as the list of
enabled ciphersuites and whether to use client authentication,
but can not change between client/server modes. As before, once
handshaking has begun, any new

SSLEngine

configuration settings will not be used until the next
handshake.

Closure - When the connection is no longer needed, the client
and the server applications should each close both sides of their
respective connections. For

SSLEngine

objects, an
application should call

closeOutbound()

and
send any remaining messages to the peer. Likewise, an application
should receive any remaining messages from the peer before calling

closeInbound()

. The underlying transport mechanism
can then be closed after both sides of the

SSLEngine

have
been closed. If the connection is not closed in an orderly manner
(for example

closeInbound()

is called before the
peer's write closure notification has been received), exceptions
will be raised to indicate that an error has occurred. Once an
engine is closed, it is not reusable: a new

SSLEngine

must be created.

An

SSLEngine

is created by calling

SSLContext.createSSLEngine()

from an initialized

SSLContext

. Any configuration
parameters should be set before making the first call to

wrap()

,

unwrap()

, or

beginHandshake()

. These methods all trigger the
initial handshake.

Data moves through the engine by calling

wrap()

or

unwrap()

on outbound or inbound data, respectively. Depending on
the state of the

SSLEngine

, a

wrap()

call
may consume application data from the source buffer and may produce
network data in the destination buffer. The outbound data
may contain application and/or handshake data. A call to

unwrap()

will examine the source buffer and may
advance the handshake if the data is handshaking information, or
may place application data in the destination buffer if the data
is application. The state of the underlying SSL/TLS/DTLS algorithm
will determine when data is consumed and produced.

Calls to

wrap()

and

unwrap()

return an

SSLEngineResult

which indicates the status of the
operation, and (optionally) how to interact with the engine to make
progress.

The

SSLEngine

produces/consumes complete SSL/TLS/DTLS
packets only, and does not store application data internally between
calls to

wrap()/unwrap()

. Thus input and output

ByteBuffer

s must be sized appropriately to hold the
maximum record that can be produced. Calls to

SSLSession.getPacketBufferSize()

and

SSLSession.getApplicationBufferSize()

should be used to determine
the appropriate buffer sizes. The size of the outbound application
data buffer generally does not matter. If buffer conditions do not
allow for the proper consumption/production of data, the application
must determine (via

SSLEngineResult

) and correct the
problem, and then try the call again.

For example,

unwrap()

will return a

SSLEngineResult.Status.BUFFER_OVERFLOW

result if the engine
determines that there is not enough destination buffer space available.
Applications should call

SSLSession.getApplicationBufferSize()

and compare that value with the space available in the destination buffer,
enlarging the buffer if necessary. Similarly, if

unwrap()

were to return a

SSLEngineResult.Status.BUFFER_UNDERFLOW

, the
application should call

SSLSession.getPacketBufferSize()

to ensure
that the source buffer has enough room to hold a record (enlarging if
necessary), and then obtain more inbound data.

```java
SSLEngineResult r = engine.unwrap(src, dst);
switch (r.getStatus()) {
BUFFER_OVERFLOW:
// Could attempt to drain the dst buffer of any already obtained
// data, but we'll just increase it to the size needed.
int appSize = engine.getSession().getApplicationBufferSize();
ByteBuffer b = ByteBuffer.allocate(appSize + dst.position());
dst.flip();
b.put(dst);
dst = b;
// retry the operation.
break;
BUFFER_UNDERFLOW:
int netSize = engine.getSession().getPacketBufferSize();
// Resize buffer if needed.
if (netSize > dst.capacity()) {
ByteBuffer b = ByteBuffer.allocate(netSize);
src.flip();
b.put(src);
src = b;
}
// Obtain more inbound network data for src,
// then retry the operation.
break;
// other cases: CLOSED, OK.
}
```

Unlike

SSLSocket

, all methods of SSLEngine are
non-blocking.

SSLEngine

implementations may
require the results of tasks that may take an extended period of
time to complete, or may even block. For example, a TrustManager
may need to connect to a remote certificate validation service,
or a KeyManager might need to prompt a user to determine which
certificate to use as part of client authentication. Additionally,
creating cryptographic signatures and verifying them can be slow,
seemingly blocking.

For any operation which may potentially block, the

SSLEngine

will create a

Runnable

delegated task. When

SSLEngineResult

indicates that a
delegated task result is needed, the application must call

getDelegatedTask()

to obtain an outstanding delegated task and
call its

run()

method (possibly using
a different thread depending on the compute strategy). The
application should continue obtaining delegated tasks until no more
exist, and try the original operation again.

At the end of a communication session, applications should properly
close the SSL/TLS/DTLS link. The SSL/TLS/DTLS protocols have closure
handshake messages, and these messages should be communicated to the
peer before releasing the

SSLEngine

and closing the
underlying transport mechanism. A close can be initiated by one of:
an SSLException, an inbound closure handshake message, or one of the
close methods. In all cases, closure handshake messages are
generated by the engine, and

wrap()

should be repeatedly
called until the resulting

SSLEngineResult

's status
returns "CLOSED", or

isOutboundDone()

returns true. All
data obtained from the

wrap()

method should be sent to the
peer.

closeOutbound()

is used to signal the engine that the
application will not be sending any more data.

A peer will signal its intent to close by sending its own closure
handshake message. After this message has been received and
processed by the local

SSLEngine

's

unwrap()

call, the application can detect the close by calling

unwrap()

and looking for a

SSLEngineResult

with status "CLOSED", or if

isInboundDone()

returns true.
If for some reason the peer closes the communication link without
sending the proper SSL/TLS/DTLS closure message, the application can
detect the end-of-stream and can signal the engine via

closeInbound()

that there will no more inbound messages to
process. Some applications might choose to require orderly shutdown
messages from a peer, in which case they can check that the closure
was generated by a handshake message and not by an end-of-stream
condition.

There are two groups of cipher suites which you will need to know
about when managing cipher suites:

- Supported

cipher suites: all the suites which are
supported by the SSL implementation. This list is reported
using

getSupportedCipherSuites()

.

Enabled

cipher suites, which may be fewer than
the full set of supported suites. This group is set using the

setEnabledCipherSuites(String [])

method, and
queried using the

getEnabledCipherSuites()

method.
Initially, a default set of cipher suites will be enabled on a
new engine that represents the minimum suggested
configuration.

Implementation defaults require that only cipher suites which
authenticate servers and provide confidentiality be enabled by
default. Only if both sides explicitly agree to unauthenticated
and/or non-private (unencrypted) communications will such a
cipher suite be selected.

Each SSL/TLS/DTLS connection must have one client and one server, thus
each endpoint must decide which role to assume. This choice determines
who begins the handshaking process as well as which type of messages
should be sent by each party. The method

setUseClientMode(boolean)

configures the mode. Note that the
default mode for a new

SSLEngine

is provider-specific.
Applications should set the mode explicitly before invoking other
methods of the

SSLEngine

. Once the initial handshaking has
started, an

SSLEngine

can not switch between client and server
modes, even when performing renegotiations.

Applications might choose to process delegated tasks in different
threads. When an

SSLEngine

is created, the current

AccessControlContext

is saved. All future delegated tasks will be processed using this
context: that is, all access control decisions will be made using the
context captured at engine creation.

Concurrency Notes

:
There are two concurrency issues to be aware of:

- The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

The

SSLSocket

class provides much of the same security
functionality, but all of the inbound and outbound data is
automatically transported using the underlying

Socket

, which by design uses a blocking model.
While this is appropriate for many applications, this model does not
provide the scalability required by large servers.

The primary distinction of an

SSLEngine

is that it
operates on inbound and outbound byte streams, independent of the
transport mechanism. It is the responsibility of the

SSLEngine

user to arrange for reliable I/O transport to
the peer. By separating the SSL/TLS/DTLS abstraction from the I/O
transport mechanism, the

SSLEngine

can be used for a
wide variety of I/O types, such as

non-blocking I/O (polling)

,

selectable non-blocking I/O

,

Socket

and the
traditional Input/OutputStreams, local

ByteBuffers

or byte arrays,

future asynchronous
I/O models

, and so on.

At a high level, the

SSLEngine

appears thus:

```java
app data

| ^
| | |
v | |
+----+-----|-----+----+
| | |
| SSL|Engine |
wrap() | | | unwrap()
| OUTBOUND | INBOUND |
| | |
+----+-----|-----+----+
| | ^
| | |
v |

net data
```

Application data (also known as plaintext or cleartext) is data which
is produced or consumed by an application. Its counterpart is
network data, which consists of either handshaking and/or ciphertext
(encrypted) data, and destined to be transported via an I/O
mechanism. Inbound data is data which has been received from the
peer, and outbound data is destined for the peer.

(In the context of an

SSLEngine

, the term "handshake
data" is taken to mean any data exchanged to establish and control a
secure connection. Handshake data includes the SSL/TLS/DTLS messages
"alert", "change_cipher_spec," and "handshake.")

There are five distinct phases to an

SSLEngine

.

- Creation - The

SSLEngine

has been created and
initialized, but has not yet been used. During this phase, an
application may set any

SSLEngine

-specific settings
(enabled cipher suites, whether the

SSLEngine

should
handshake in client or server mode, and so on). Once
handshaking has begun, though, any new settings (except
client/server mode, see below) will be used for
the next handshake.

Initial Handshake - The initial handshake is a procedure by
which the two peers exchange communication parameters until an
SSLSession is established. Application data can not be sent during
this phase.

Application Data - Once the communication parameters have
been established and the handshake is complete, application data
may flow through the

SSLEngine

. Outbound
application messages are encrypted and integrity protected,
and inbound messages reverse the process.

Rehandshaking - Either side may request a renegotiation of
the session at any time during the Application Data phase. New
handshaking data can be intermixed among the application data.
Before starting the rehandshake phase, the application may
reset the SSL/TLS/DTLS communication parameters such as the list of
enabled ciphersuites and whether to use client authentication,
but can not change between client/server modes. As before, once
handshaking has begun, any new

SSLEngine

configuration settings will not be used until the next
handshake.

Closure - When the connection is no longer needed, the client
and the server applications should each close both sides of their
respective connections. For

SSLEngine

objects, an
application should call

closeOutbound()

and
send any remaining messages to the peer. Likewise, an application
should receive any remaining messages from the peer before calling

closeInbound()

. The underlying transport mechanism
can then be closed after both sides of the

SSLEngine

have
been closed. If the connection is not closed in an orderly manner
(for example

closeInbound()

is called before the
peer's write closure notification has been received), exceptions
will be raised to indicate that an error has occurred. Once an
engine is closed, it is not reusable: a new

SSLEngine

must be created.

An

SSLEngine

is created by calling

SSLContext.createSSLEngine()

from an initialized

SSLContext

. Any configuration
parameters should be set before making the first call to

wrap()

,

unwrap()

, or

beginHandshake()

. These methods all trigger the
initial handshake.

Data moves through the engine by calling

wrap()

or

unwrap()

on outbound or inbound data, respectively. Depending on
the state of the

SSLEngine

, a

wrap()

call
may consume application data from the source buffer and may produce
network data in the destination buffer. The outbound data
may contain application and/or handshake data. A call to

unwrap()

will examine the source buffer and may
advance the handshake if the data is handshaking information, or
may place application data in the destination buffer if the data
is application. The state of the underlying SSL/TLS/DTLS algorithm
will determine when data is consumed and produced.

Calls to

wrap()

and

unwrap()

return an

SSLEngineResult

which indicates the status of the
operation, and (optionally) how to interact with the engine to make
progress.

The

SSLEngine

produces/consumes complete SSL/TLS/DTLS
packets only, and does not store application data internally between
calls to

wrap()/unwrap()

. Thus input and output

ByteBuffer

s must be sized appropriately to hold the
maximum record that can be produced. Calls to

SSLSession.getPacketBufferSize()

and

SSLSession.getApplicationBufferSize()

should be used to determine
the appropriate buffer sizes. The size of the outbound application
data buffer generally does not matter. If buffer conditions do not
allow for the proper consumption/production of data, the application
must determine (via

SSLEngineResult

) and correct the
problem, and then try the call again.

For example,

unwrap()

will return a

SSLEngineResult.Status.BUFFER_OVERFLOW

result if the engine
determines that there is not enough destination buffer space available.
Applications should call

SSLSession.getApplicationBufferSize()

and compare that value with the space available in the destination buffer,
enlarging the buffer if necessary. Similarly, if

unwrap()

were to return a

SSLEngineResult.Status.BUFFER_UNDERFLOW

, the
application should call

SSLSession.getPacketBufferSize()

to ensure
that the source buffer has enough room to hold a record (enlarging if
necessary), and then obtain more inbound data.

```java
SSLEngineResult r = engine.unwrap(src, dst);
switch (r.getStatus()) {
BUFFER_OVERFLOW:
// Could attempt to drain the dst buffer of any already obtained
// data, but we'll just increase it to the size needed.
int appSize = engine.getSession().getApplicationBufferSize();
ByteBuffer b = ByteBuffer.allocate(appSize + dst.position());
dst.flip();
b.put(dst);
dst = b;
// retry the operation.
break;
BUFFER_UNDERFLOW:
int netSize = engine.getSession().getPacketBufferSize();
// Resize buffer if needed.
if (netSize > dst.capacity()) {
ByteBuffer b = ByteBuffer.allocate(netSize);
src.flip();
b.put(src);
src = b;
}
// Obtain more inbound network data for src,
// then retry the operation.
break;
// other cases: CLOSED, OK.
}
```

Unlike

SSLSocket

, all methods of SSLEngine are
non-blocking.

SSLEngine

implementations may
require the results of tasks that may take an extended period of
time to complete, or may even block. For example, a TrustManager
may need to connect to a remote certificate validation service,
or a KeyManager might need to prompt a user to determine which
certificate to use as part of client authentication. Additionally,
creating cryptographic signatures and verifying them can be slow,
seemingly blocking.

For any operation which may potentially block, the

SSLEngine

will create a

Runnable

delegated task. When

SSLEngineResult

indicates that a
delegated task result is needed, the application must call

getDelegatedTask()

to obtain an outstanding delegated task and
call its

run()

method (possibly using
a different thread depending on the compute strategy). The
application should continue obtaining delegated tasks until no more
exist, and try the original operation again.

At the end of a communication session, applications should properly
close the SSL/TLS/DTLS link. The SSL/TLS/DTLS protocols have closure
handshake messages, and these messages should be communicated to the
peer before releasing the

SSLEngine

and closing the
underlying transport mechanism. A close can be initiated by one of:
an SSLException, an inbound closure handshake message, or one of the
close methods. In all cases, closure handshake messages are
generated by the engine, and

wrap()

should be repeatedly
called until the resulting

SSLEngineResult

's status
returns "CLOSED", or

isOutboundDone()

returns true. All
data obtained from the

wrap()

method should be sent to the
peer.

closeOutbound()

is used to signal the engine that the
application will not be sending any more data.

A peer will signal its intent to close by sending its own closure
handshake message. After this message has been received and
processed by the local

SSLEngine

's

unwrap()

call, the application can detect the close by calling

unwrap()

and looking for a

SSLEngineResult

with status "CLOSED", or if

isInboundDone()

returns true.
If for some reason the peer closes the communication link without
sending the proper SSL/TLS/DTLS closure message, the application can
detect the end-of-stream and can signal the engine via

closeInbound()

that there will no more inbound messages to
process. Some applications might choose to require orderly shutdown
messages from a peer, in which case they can check that the closure
was generated by a handshake message and not by an end-of-stream
condition.

There are two groups of cipher suites which you will need to know
about when managing cipher suites:

- Supported

cipher suites: all the suites which are
supported by the SSL implementation. This list is reported
using

getSupportedCipherSuites()

.

Enabled

cipher suites, which may be fewer than
the full set of supported suites. This group is set using the

setEnabledCipherSuites(String [])

method, and
queried using the

getEnabledCipherSuites()

method.
Initially, a default set of cipher suites will be enabled on a
new engine that represents the minimum suggested
configuration.

Implementation defaults require that only cipher suites which
authenticate servers and provide confidentiality be enabled by
default. Only if both sides explicitly agree to unauthenticated
and/or non-private (unencrypted) communications will such a
cipher suite be selected.

Each SSL/TLS/DTLS connection must have one client and one server, thus
each endpoint must decide which role to assume. This choice determines
who begins the handshaking process as well as which type of messages
should be sent by each party. The method

setUseClientMode(boolean)

configures the mode. Note that the
default mode for a new

SSLEngine

is provider-specific.
Applications should set the mode explicitly before invoking other
methods of the

SSLEngine

. Once the initial handshaking has
started, an

SSLEngine

can not switch between client and server
modes, even when performing renegotiations.

Applications might choose to process delegated tasks in different
threads. When an

SSLEngine

is created, the current

AccessControlContext

is saved. All future delegated tasks will be processed using this
context: that is, all access control decisions will be made using the
context captured at engine creation.

Concurrency Notes

:
There are two concurrency issues to be aware of:

- The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

The primary distinction of an

SSLEngine

is that it
operates on inbound and outbound byte streams, independent of the
transport mechanism. It is the responsibility of the

SSLEngine

user to arrange for reliable I/O transport to
the peer. By separating the SSL/TLS/DTLS abstraction from the I/O
transport mechanism, the

SSLEngine

can be used for a
wide variety of I/O types, such as

non-blocking I/O (polling)

,

selectable non-blocking I/O

,

Socket

and the
traditional Input/OutputStreams, local

ByteBuffers

or byte arrays,

future asynchronous
I/O models

, and so on.

At a high level, the

SSLEngine

appears thus:

```java
app data

| ^
| | |
v | |
+----+-----|-----+----+
| | |
| SSL|Engine |
wrap() | | | unwrap()
| OUTBOUND | INBOUND |
| | |
+----+-----|-----+----+
| | ^
| | |
v |

net data
```

Application data (also known as plaintext or cleartext) is data which
is produced or consumed by an application. Its counterpart is
network data, which consists of either handshaking and/or ciphertext
(encrypted) data, and destined to be transported via an I/O
mechanism. Inbound data is data which has been received from the
peer, and outbound data is destined for the peer.

(In the context of an

SSLEngine

, the term "handshake
data" is taken to mean any data exchanged to establish and control a
secure connection. Handshake data includes the SSL/TLS/DTLS messages
"alert", "change_cipher_spec," and "handshake.")

There are five distinct phases to an

SSLEngine

.

- Creation - The

SSLEngine

has been created and
initialized, but has not yet been used. During this phase, an
application may set any

SSLEngine

-specific settings
(enabled cipher suites, whether the

SSLEngine

should
handshake in client or server mode, and so on). Once
handshaking has begun, though, any new settings (except
client/server mode, see below) will be used for
the next handshake.

Initial Handshake - The initial handshake is a procedure by
which the two peers exchange communication parameters until an
SSLSession is established. Application data can not be sent during
this phase.

Application Data - Once the communication parameters have
been established and the handshake is complete, application data
may flow through the

SSLEngine

. Outbound
application messages are encrypted and integrity protected,
and inbound messages reverse the process.

Rehandshaking - Either side may request a renegotiation of
the session at any time during the Application Data phase. New
handshaking data can be intermixed among the application data.
Before starting the rehandshake phase, the application may
reset the SSL/TLS/DTLS communication parameters such as the list of
enabled ciphersuites and whether to use client authentication,
but can not change between client/server modes. As before, once
handshaking has begun, any new

SSLEngine

configuration settings will not be used until the next
handshake.

Closure - When the connection is no longer needed, the client
and the server applications should each close both sides of their
respective connections. For

SSLEngine

objects, an
application should call

closeOutbound()

and
send any remaining messages to the peer. Likewise, an application
should receive any remaining messages from the peer before calling

closeInbound()

. The underlying transport mechanism
can then be closed after both sides of the

SSLEngine

have
been closed. If the connection is not closed in an orderly manner
(for example

closeInbound()

is called before the
peer's write closure notification has been received), exceptions
will be raised to indicate that an error has occurred. Once an
engine is closed, it is not reusable: a new

SSLEngine

must be created.

An

SSLEngine

is created by calling

SSLContext.createSSLEngine()

from an initialized

SSLContext

. Any configuration
parameters should be set before making the first call to

wrap()

,

unwrap()

, or

beginHandshake()

. These methods all trigger the
initial handshake.

Data moves through the engine by calling

wrap()

or

unwrap()

on outbound or inbound data, respectively. Depending on
the state of the

SSLEngine

, a

wrap()

call
may consume application data from the source buffer and may produce
network data in the destination buffer. The outbound data
may contain application and/or handshake data. A call to

unwrap()

will examine the source buffer and may
advance the handshake if the data is handshaking information, or
may place application data in the destination buffer if the data
is application. The state of the underlying SSL/TLS/DTLS algorithm
will determine when data is consumed and produced.

Calls to

wrap()

and

unwrap()

return an

SSLEngineResult

which indicates the status of the
operation, and (optionally) how to interact with the engine to make
progress.

The

SSLEngine

produces/consumes complete SSL/TLS/DTLS
packets only, and does not store application data internally between
calls to

wrap()/unwrap()

. Thus input and output

ByteBuffer

s must be sized appropriately to hold the
maximum record that can be produced. Calls to

SSLSession.getPacketBufferSize()

and

SSLSession.getApplicationBufferSize()

should be used to determine
the appropriate buffer sizes. The size of the outbound application
data buffer generally does not matter. If buffer conditions do not
allow for the proper consumption/production of data, the application
must determine (via

SSLEngineResult

) and correct the
problem, and then try the call again.

For example,

unwrap()

will return a

SSLEngineResult.Status.BUFFER_OVERFLOW

result if the engine
determines that there is not enough destination buffer space available.
Applications should call

SSLSession.getApplicationBufferSize()

and compare that value with the space available in the destination buffer,
enlarging the buffer if necessary. Similarly, if

unwrap()

were to return a

SSLEngineResult.Status.BUFFER_UNDERFLOW

, the
application should call

SSLSession.getPacketBufferSize()

to ensure
that the source buffer has enough room to hold a record (enlarging if
necessary), and then obtain more inbound data.

```java
SSLEngineResult r = engine.unwrap(src, dst);
switch (r.getStatus()) {
BUFFER_OVERFLOW:
// Could attempt to drain the dst buffer of any already obtained
// data, but we'll just increase it to the size needed.
int appSize = engine.getSession().getApplicationBufferSize();
ByteBuffer b = ByteBuffer.allocate(appSize + dst.position());
dst.flip();
b.put(dst);
dst = b;
// retry the operation.
break;
BUFFER_UNDERFLOW:
int netSize = engine.getSession().getPacketBufferSize();
// Resize buffer if needed.
if (netSize > dst.capacity()) {
ByteBuffer b = ByteBuffer.allocate(netSize);
src.flip();
b.put(src);
src = b;
}
// Obtain more inbound network data for src,
// then retry the operation.
break;
// other cases: CLOSED, OK.
}
```

Unlike

SSLSocket

, all methods of SSLEngine are
non-blocking.

SSLEngine

implementations may
require the results of tasks that may take an extended period of
time to complete, or may even block. For example, a TrustManager
may need to connect to a remote certificate validation service,
or a KeyManager might need to prompt a user to determine which
certificate to use as part of client authentication. Additionally,
creating cryptographic signatures and verifying them can be slow,
seemingly blocking.

For any operation which may potentially block, the

SSLEngine

will create a

Runnable

delegated task. When

SSLEngineResult

indicates that a
delegated task result is needed, the application must call

getDelegatedTask()

to obtain an outstanding delegated task and
call its

run()

method (possibly using
a different thread depending on the compute strategy). The
application should continue obtaining delegated tasks until no more
exist, and try the original operation again.

At the end of a communication session, applications should properly
close the SSL/TLS/DTLS link. The SSL/TLS/DTLS protocols have closure
handshake messages, and these messages should be communicated to the
peer before releasing the

SSLEngine

and closing the
underlying transport mechanism. A close can be initiated by one of:
an SSLException, an inbound closure handshake message, or one of the
close methods. In all cases, closure handshake messages are
generated by the engine, and

wrap()

should be repeatedly
called until the resulting

SSLEngineResult

's status
returns "CLOSED", or

isOutboundDone()

returns true. All
data obtained from the

wrap()

method should be sent to the
peer.

closeOutbound()

is used to signal the engine that the
application will not be sending any more data.

A peer will signal its intent to close by sending its own closure
handshake message. After this message has been received and
processed by the local

SSLEngine

's

unwrap()

call, the application can detect the close by calling

unwrap()

and looking for a

SSLEngineResult

with status "CLOSED", or if

isInboundDone()

returns true.
If for some reason the peer closes the communication link without
sending the proper SSL/TLS/DTLS closure message, the application can
detect the end-of-stream and can signal the engine via

closeInbound()

that there will no more inbound messages to
process. Some applications might choose to require orderly shutdown
messages from a peer, in which case they can check that the closure
was generated by a handshake message and not by an end-of-stream
condition.

There are two groups of cipher suites which you will need to know
about when managing cipher suites:

- Supported

cipher suites: all the suites which are
supported by the SSL implementation. This list is reported
using

getSupportedCipherSuites()

.

Enabled

cipher suites, which may be fewer than
the full set of supported suites. This group is set using the

setEnabledCipherSuites(String [])

method, and
queried using the

getEnabledCipherSuites()

method.
Initially, a default set of cipher suites will be enabled on a
new engine that represents the minimum suggested
configuration.

Implementation defaults require that only cipher suites which
authenticate servers and provide confidentiality be enabled by
default. Only if both sides explicitly agree to unauthenticated
and/or non-private (unencrypted) communications will such a
cipher suite be selected.

Each SSL/TLS/DTLS connection must have one client and one server, thus
each endpoint must decide which role to assume. This choice determines
who begins the handshaking process as well as which type of messages
should be sent by each party. The method

setUseClientMode(boolean)

configures the mode. Note that the
default mode for a new

SSLEngine

is provider-specific.
Applications should set the mode explicitly before invoking other
methods of the

SSLEngine

. Once the initial handshaking has
started, an

SSLEngine

can not switch between client and server
modes, even when performing renegotiations.

Applications might choose to process delegated tasks in different
threads. When an

SSLEngine

is created, the current

AccessControlContext

is saved. All future delegated tasks will be processed using this
context: that is, all access control decisions will be made using the
context captured at engine creation.

Concurrency Notes

:
There are two concurrency issues to be aware of:

- The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

At a high level, the

SSLEngine

appears thus:

```java
app data

| ^
| | |
v | |
+----+-----|-----+----+
| | |
| SSL|Engine |
wrap() | | | unwrap()
| OUTBOUND | INBOUND |
| | |
+----+-----|-----+----+
| | ^
| | |
v |

net data
```

Application data (also known as plaintext or cleartext) is data which
is produced or consumed by an application. Its counterpart is
network data, which consists of either handshaking and/or ciphertext
(encrypted) data, and destined to be transported via an I/O
mechanism. Inbound data is data which has been received from the
peer, and outbound data is destined for the peer.

(In the context of an

SSLEngine

, the term "handshake
data" is taken to mean any data exchanged to establish and control a
secure connection. Handshake data includes the SSL/TLS/DTLS messages
"alert", "change_cipher_spec," and "handshake.")

There are five distinct phases to an

SSLEngine

.

- Creation - The

SSLEngine

has been created and
initialized, but has not yet been used. During this phase, an
application may set any

SSLEngine

-specific settings
(enabled cipher suites, whether the

SSLEngine

should
handshake in client or server mode, and so on). Once
handshaking has begun, though, any new settings (except
client/server mode, see below) will be used for
the next handshake.

Initial Handshake - The initial handshake is a procedure by
which the two peers exchange communication parameters until an
SSLSession is established. Application data can not be sent during
this phase.

Application Data - Once the communication parameters have
been established and the handshake is complete, application data
may flow through the

SSLEngine

. Outbound
application messages are encrypted and integrity protected,
and inbound messages reverse the process.

Rehandshaking - Either side may request a renegotiation of
the session at any time during the Application Data phase. New
handshaking data can be intermixed among the application data.
Before starting the rehandshake phase, the application may
reset the SSL/TLS/DTLS communication parameters such as the list of
enabled ciphersuites and whether to use client authentication,
but can not change between client/server modes. As before, once
handshaking has begun, any new

SSLEngine

configuration settings will not be used until the next
handshake.

Closure - When the connection is no longer needed, the client
and the server applications should each close both sides of their
respective connections. For

SSLEngine

objects, an
application should call

closeOutbound()

and
send any remaining messages to the peer. Likewise, an application
should receive any remaining messages from the peer before calling

closeInbound()

. The underlying transport mechanism
can then be closed after both sides of the

SSLEngine

have
been closed. If the connection is not closed in an orderly manner
(for example

closeInbound()

is called before the
peer's write closure notification has been received), exceptions
will be raised to indicate that an error has occurred. Once an
engine is closed, it is not reusable: a new

SSLEngine

must be created.

An

SSLEngine

is created by calling

SSLContext.createSSLEngine()

from an initialized

SSLContext

. Any configuration
parameters should be set before making the first call to

wrap()

,

unwrap()

, or

beginHandshake()

. These methods all trigger the
initial handshake.

Data moves through the engine by calling

wrap()

or

unwrap()

on outbound or inbound data, respectively. Depending on
the state of the

SSLEngine

, a

wrap()

call
may consume application data from the source buffer and may produce
network data in the destination buffer. The outbound data
may contain application and/or handshake data. A call to

unwrap()

will examine the source buffer and may
advance the handshake if the data is handshaking information, or
may place application data in the destination buffer if the data
is application. The state of the underlying SSL/TLS/DTLS algorithm
will determine when data is consumed and produced.

Calls to

wrap()

and

unwrap()

return an

SSLEngineResult

which indicates the status of the
operation, and (optionally) how to interact with the engine to make
progress.

The

SSLEngine

produces/consumes complete SSL/TLS/DTLS
packets only, and does not store application data internally between
calls to

wrap()/unwrap()

. Thus input and output

ByteBuffer

s must be sized appropriately to hold the
maximum record that can be produced. Calls to

SSLSession.getPacketBufferSize()

and

SSLSession.getApplicationBufferSize()

should be used to determine
the appropriate buffer sizes. The size of the outbound application
data buffer generally does not matter. If buffer conditions do not
allow for the proper consumption/production of data, the application
must determine (via

SSLEngineResult

) and correct the
problem, and then try the call again.

For example,

unwrap()

will return a

SSLEngineResult.Status.BUFFER_OVERFLOW

result if the engine
determines that there is not enough destination buffer space available.
Applications should call

SSLSession.getApplicationBufferSize()

and compare that value with the space available in the destination buffer,
enlarging the buffer if necessary. Similarly, if

unwrap()

were to return a

SSLEngineResult.Status.BUFFER_UNDERFLOW

, the
application should call

SSLSession.getPacketBufferSize()

to ensure
that the source buffer has enough room to hold a record (enlarging if
necessary), and then obtain more inbound data.

```java
SSLEngineResult r = engine.unwrap(src, dst);
switch (r.getStatus()) {
BUFFER_OVERFLOW:
// Could attempt to drain the dst buffer of any already obtained
// data, but we'll just increase it to the size needed.
int appSize = engine.getSession().getApplicationBufferSize();
ByteBuffer b = ByteBuffer.allocate(appSize + dst.position());
dst.flip();
b.put(dst);
dst = b;
// retry the operation.
break;
BUFFER_UNDERFLOW:
int netSize = engine.getSession().getPacketBufferSize();
// Resize buffer if needed.
if (netSize > dst.capacity()) {
ByteBuffer b = ByteBuffer.allocate(netSize);
src.flip();
b.put(src);
src = b;
}
// Obtain more inbound network data for src,
// then retry the operation.
break;
// other cases: CLOSED, OK.
}
```

Unlike

SSLSocket

, all methods of SSLEngine are
non-blocking.

SSLEngine

implementations may
require the results of tasks that may take an extended period of
time to complete, or may even block. For example, a TrustManager
may need to connect to a remote certificate validation service,
or a KeyManager might need to prompt a user to determine which
certificate to use as part of client authentication. Additionally,
creating cryptographic signatures and verifying them can be slow,
seemingly blocking.

For any operation which may potentially block, the

SSLEngine

will create a

Runnable

delegated task. When

SSLEngineResult

indicates that a
delegated task result is needed, the application must call

getDelegatedTask()

to obtain an outstanding delegated task and
call its

run()

method (possibly using
a different thread depending on the compute strategy). The
application should continue obtaining delegated tasks until no more
exist, and try the original operation again.

At the end of a communication session, applications should properly
close the SSL/TLS/DTLS link. The SSL/TLS/DTLS protocols have closure
handshake messages, and these messages should be communicated to the
peer before releasing the

SSLEngine

and closing the
underlying transport mechanism. A close can be initiated by one of:
an SSLException, an inbound closure handshake message, or one of the
close methods. In all cases, closure handshake messages are
generated by the engine, and

wrap()

should be repeatedly
called until the resulting

SSLEngineResult

's status
returns "CLOSED", or

isOutboundDone()

returns true. All
data obtained from the

wrap()

method should be sent to the
peer.

closeOutbound()

is used to signal the engine that the
application will not be sending any more data.

A peer will signal its intent to close by sending its own closure
handshake message. After this message has been received and
processed by the local

SSLEngine

's

unwrap()

call, the application can detect the close by calling

unwrap()

and looking for a

SSLEngineResult

with status "CLOSED", or if

isInboundDone()

returns true.
If for some reason the peer closes the communication link without
sending the proper SSL/TLS/DTLS closure message, the application can
detect the end-of-stream and can signal the engine via

closeInbound()

that there will no more inbound messages to
process. Some applications might choose to require orderly shutdown
messages from a peer, in which case they can check that the closure
was generated by a handshake message and not by an end-of-stream
condition.

There are two groups of cipher suites which you will need to know
about when managing cipher suites:

- Supported

cipher suites: all the suites which are
supported by the SSL implementation. This list is reported
using

getSupportedCipherSuites()

.

Enabled

cipher suites, which may be fewer than
the full set of supported suites. This group is set using the

setEnabledCipherSuites(String [])

method, and
queried using the

getEnabledCipherSuites()

method.
Initially, a default set of cipher suites will be enabled on a
new engine that represents the minimum suggested
configuration.

Implementation defaults require that only cipher suites which
authenticate servers and provide confidentiality be enabled by
default. Only if both sides explicitly agree to unauthenticated
and/or non-private (unencrypted) communications will such a
cipher suite be selected.

Each SSL/TLS/DTLS connection must have one client and one server, thus
each endpoint must decide which role to assume. This choice determines
who begins the handshaking process as well as which type of messages
should be sent by each party. The method

setUseClientMode(boolean)

configures the mode. Note that the
default mode for a new

SSLEngine

is provider-specific.
Applications should set the mode explicitly before invoking other
methods of the

SSLEngine

. Once the initial handshaking has
started, an

SSLEngine

can not switch between client and server
modes, even when performing renegotiations.

Applications might choose to process delegated tasks in different
threads. When an

SSLEngine

is created, the current

AccessControlContext

is saved. All future delegated tasks will be processed using this
context: that is, all access control decisions will be made using the
context captured at engine creation.

Concurrency Notes

:
There are two concurrency issues to be aware of:

- The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

app data

| ^
| | |
v | |
+----+-----|-----+----+
| | |
| SSL|Engine |
wrap() | | | unwrap()
| OUTBOUND | INBOUND |
| | |
+----+-----|-----+----+
| | ^
| | |
v |

net data

(In the context of an

SSLEngine

, the term "handshake
data" is taken to mean any data exchanged to establish and control a
secure connection. Handshake data includes the SSL/TLS/DTLS messages
"alert", "change_cipher_spec," and "handshake.")

There are five distinct phases to an

SSLEngine

.

- Creation - The

SSLEngine

has been created and
initialized, but has not yet been used. During this phase, an
application may set any

SSLEngine

-specific settings
(enabled cipher suites, whether the

SSLEngine

should
handshake in client or server mode, and so on). Once
handshaking has begun, though, any new settings (except
client/server mode, see below) will be used for
the next handshake.

Initial Handshake - The initial handshake is a procedure by
which the two peers exchange communication parameters until an
SSLSession is established. Application data can not be sent during
this phase.

Application Data - Once the communication parameters have
been established and the handshake is complete, application data
may flow through the

SSLEngine

. Outbound
application messages are encrypted and integrity protected,
and inbound messages reverse the process.

Rehandshaking - Either side may request a renegotiation of
the session at any time during the Application Data phase. New
handshaking data can be intermixed among the application data.
Before starting the rehandshake phase, the application may
reset the SSL/TLS/DTLS communication parameters such as the list of
enabled ciphersuites and whether to use client authentication,
but can not change between client/server modes. As before, once
handshaking has begun, any new

SSLEngine

configuration settings will not be used until the next
handshake.

Closure - When the connection is no longer needed, the client
and the server applications should each close both sides of their
respective connections. For

SSLEngine

objects, an
application should call

closeOutbound()

and
send any remaining messages to the peer. Likewise, an application
should receive any remaining messages from the peer before calling

closeInbound()

. The underlying transport mechanism
can then be closed after both sides of the

SSLEngine

have
been closed. If the connection is not closed in an orderly manner
(for example

closeInbound()

is called before the
peer's write closure notification has been received), exceptions
will be raised to indicate that an error has occurred. Once an
engine is closed, it is not reusable: a new

SSLEngine

must be created.

An

SSLEngine

is created by calling

SSLContext.createSSLEngine()

from an initialized

SSLContext

. Any configuration
parameters should be set before making the first call to

wrap()

,

unwrap()

, or

beginHandshake()

. These methods all trigger the
initial handshake.

Data moves through the engine by calling

wrap()

or

unwrap()

on outbound or inbound data, respectively. Depending on
the state of the

SSLEngine

, a

wrap()

call
may consume application data from the source buffer and may produce
network data in the destination buffer. The outbound data
may contain application and/or handshake data. A call to

unwrap()

will examine the source buffer and may
advance the handshake if the data is handshaking information, or
may place application data in the destination buffer if the data
is application. The state of the underlying SSL/TLS/DTLS algorithm
will determine when data is consumed and produced.

Calls to

wrap()

and

unwrap()

return an

SSLEngineResult

which indicates the status of the
operation, and (optionally) how to interact with the engine to make
progress.

The

SSLEngine

produces/consumes complete SSL/TLS/DTLS
packets only, and does not store application data internally between
calls to

wrap()/unwrap()

. Thus input and output

ByteBuffer

s must be sized appropriately to hold the
maximum record that can be produced. Calls to

SSLSession.getPacketBufferSize()

and

SSLSession.getApplicationBufferSize()

should be used to determine
the appropriate buffer sizes. The size of the outbound application
data buffer generally does not matter. If buffer conditions do not
allow for the proper consumption/production of data, the application
must determine (via

SSLEngineResult

) and correct the
problem, and then try the call again.

For example,

unwrap()

will return a

SSLEngineResult.Status.BUFFER_OVERFLOW

result if the engine
determines that there is not enough destination buffer space available.
Applications should call

SSLSession.getApplicationBufferSize()

and compare that value with the space available in the destination buffer,
enlarging the buffer if necessary. Similarly, if

unwrap()

were to return a

SSLEngineResult.Status.BUFFER_UNDERFLOW

, the
application should call

SSLSession.getPacketBufferSize()

to ensure
that the source buffer has enough room to hold a record (enlarging if
necessary), and then obtain more inbound data.

```java
SSLEngineResult r = engine.unwrap(src, dst);
switch (r.getStatus()) {
BUFFER_OVERFLOW:
// Could attempt to drain the dst buffer of any already obtained
// data, but we'll just increase it to the size needed.
int appSize = engine.getSession().getApplicationBufferSize();
ByteBuffer b = ByteBuffer.allocate(appSize + dst.position());
dst.flip();
b.put(dst);
dst = b;
// retry the operation.
break;
BUFFER_UNDERFLOW:
int netSize = engine.getSession().getPacketBufferSize();
// Resize buffer if needed.
if (netSize > dst.capacity()) {
ByteBuffer b = ByteBuffer.allocate(netSize);
src.flip();
b.put(src);
src = b;
}
// Obtain more inbound network data for src,
// then retry the operation.
break;
// other cases: CLOSED, OK.
}
```

Unlike

SSLSocket

, all methods of SSLEngine are
non-blocking.

SSLEngine

implementations may
require the results of tasks that may take an extended period of
time to complete, or may even block. For example, a TrustManager
may need to connect to a remote certificate validation service,
or a KeyManager might need to prompt a user to determine which
certificate to use as part of client authentication. Additionally,
creating cryptographic signatures and verifying them can be slow,
seemingly blocking.

For any operation which may potentially block, the

SSLEngine

will create a

Runnable

delegated task. When

SSLEngineResult

indicates that a
delegated task result is needed, the application must call

getDelegatedTask()

to obtain an outstanding delegated task and
call its

run()

method (possibly using
a different thread depending on the compute strategy). The
application should continue obtaining delegated tasks until no more
exist, and try the original operation again.

At the end of a communication session, applications should properly
close the SSL/TLS/DTLS link. The SSL/TLS/DTLS protocols have closure
handshake messages, and these messages should be communicated to the
peer before releasing the

SSLEngine

and closing the
underlying transport mechanism. A close can be initiated by one of:
an SSLException, an inbound closure handshake message, or one of the
close methods. In all cases, closure handshake messages are
generated by the engine, and

wrap()

should be repeatedly
called until the resulting

SSLEngineResult

's status
returns "CLOSED", or

isOutboundDone()

returns true. All
data obtained from the

wrap()

method should be sent to the
peer.

closeOutbound()

is used to signal the engine that the
application will not be sending any more data.

A peer will signal its intent to close by sending its own closure
handshake message. After this message has been received and
processed by the local

SSLEngine

's

unwrap()

call, the application can detect the close by calling

unwrap()

and looking for a

SSLEngineResult

with status "CLOSED", or if

isInboundDone()

returns true.
If for some reason the peer closes the communication link without
sending the proper SSL/TLS/DTLS closure message, the application can
detect the end-of-stream and can signal the engine via

closeInbound()

that there will no more inbound messages to
process. Some applications might choose to require orderly shutdown
messages from a peer, in which case they can check that the closure
was generated by a handshake message and not by an end-of-stream
condition.

There are two groups of cipher suites which you will need to know
about when managing cipher suites:

- Supported

cipher suites: all the suites which are
supported by the SSL implementation. This list is reported
using

getSupportedCipherSuites()

.

Enabled

cipher suites, which may be fewer than
the full set of supported suites. This group is set using the

setEnabledCipherSuites(String [])

method, and
queried using the

getEnabledCipherSuites()

method.
Initially, a default set of cipher suites will be enabled on a
new engine that represents the minimum suggested
configuration.

Implementation defaults require that only cipher suites which
authenticate servers and provide confidentiality be enabled by
default. Only if both sides explicitly agree to unauthenticated
and/or non-private (unencrypted) communications will such a
cipher suite be selected.

Each SSL/TLS/DTLS connection must have one client and one server, thus
each endpoint must decide which role to assume. This choice determines
who begins the handshaking process as well as which type of messages
should be sent by each party. The method

setUseClientMode(boolean)

configures the mode. Note that the
default mode for a new

SSLEngine

is provider-specific.
Applications should set the mode explicitly before invoking other
methods of the

SSLEngine

. Once the initial handshaking has
started, an

SSLEngine

can not switch between client and server
modes, even when performing renegotiations.

Applications might choose to process delegated tasks in different
threads. When an

SSLEngine

is created, the current

AccessControlContext

is saved. All future delegated tasks will be processed using this
context: that is, all access control decisions will be made using the
context captured at engine creation.

Concurrency Notes

:
There are two concurrency issues to be aware of:

- The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

There are five distinct phases to an

SSLEngine

.

- Creation - The

SSLEngine

has been created and
initialized, but has not yet been used. During this phase, an
application may set any

SSLEngine

-specific settings
(enabled cipher suites, whether the

SSLEngine

should
handshake in client or server mode, and so on). Once
handshaking has begun, though, any new settings (except
client/server mode, see below) will be used for
the next handshake.

Initial Handshake - The initial handshake is a procedure by
which the two peers exchange communication parameters until an
SSLSession is established. Application data can not be sent during
this phase.

Application Data - Once the communication parameters have
been established and the handshake is complete, application data
may flow through the

SSLEngine

. Outbound
application messages are encrypted and integrity protected,
and inbound messages reverse the process.

Rehandshaking - Either side may request a renegotiation of
the session at any time during the Application Data phase. New
handshaking data can be intermixed among the application data.
Before starting the rehandshake phase, the application may
reset the SSL/TLS/DTLS communication parameters such as the list of
enabled ciphersuites and whether to use client authentication,
but can not change between client/server modes. As before, once
handshaking has begun, any new

SSLEngine

configuration settings will not be used until the next
handshake.

Closure - When the connection is no longer needed, the client
and the server applications should each close both sides of their
respective connections. For

SSLEngine

objects, an
application should call

closeOutbound()

and
send any remaining messages to the peer. Likewise, an application
should receive any remaining messages from the peer before calling

closeInbound()

. The underlying transport mechanism
can then be closed after both sides of the

SSLEngine

have
been closed. If the connection is not closed in an orderly manner
(for example

closeInbound()

is called before the
peer's write closure notification has been received), exceptions
will be raised to indicate that an error has occurred. Once an
engine is closed, it is not reusable: a new

SSLEngine

must be created.

An

SSLEngine

is created by calling

SSLContext.createSSLEngine()

from an initialized

SSLContext

. Any configuration
parameters should be set before making the first call to

wrap()

,

unwrap()

, or

beginHandshake()

. These methods all trigger the
initial handshake.

Data moves through the engine by calling

wrap()

or

unwrap()

on outbound or inbound data, respectively. Depending on
the state of the

SSLEngine

, a

wrap()

call
may consume application data from the source buffer and may produce
network data in the destination buffer. The outbound data
may contain application and/or handshake data. A call to

unwrap()

will examine the source buffer and may
advance the handshake if the data is handshaking information, or
may place application data in the destination buffer if the data
is application. The state of the underlying SSL/TLS/DTLS algorithm
will determine when data is consumed and produced.

Calls to

wrap()

and

unwrap()

return an

SSLEngineResult

which indicates the status of the
operation, and (optionally) how to interact with the engine to make
progress.

The

SSLEngine

produces/consumes complete SSL/TLS/DTLS
packets only, and does not store application data internally between
calls to

wrap()/unwrap()

. Thus input and output

ByteBuffer

s must be sized appropriately to hold the
maximum record that can be produced. Calls to

SSLSession.getPacketBufferSize()

and

SSLSession.getApplicationBufferSize()

should be used to determine
the appropriate buffer sizes. The size of the outbound application
data buffer generally does not matter. If buffer conditions do not
allow for the proper consumption/production of data, the application
must determine (via

SSLEngineResult

) and correct the
problem, and then try the call again.

For example,

unwrap()

will return a

SSLEngineResult.Status.BUFFER_OVERFLOW

result if the engine
determines that there is not enough destination buffer space available.
Applications should call

SSLSession.getApplicationBufferSize()

and compare that value with the space available in the destination buffer,
enlarging the buffer if necessary. Similarly, if

unwrap()

were to return a

SSLEngineResult.Status.BUFFER_UNDERFLOW

, the
application should call

SSLSession.getPacketBufferSize()

to ensure
that the source buffer has enough room to hold a record (enlarging if
necessary), and then obtain more inbound data.

```java
SSLEngineResult r = engine.unwrap(src, dst);
switch (r.getStatus()) {
BUFFER_OVERFLOW:
// Could attempt to drain the dst buffer of any already obtained
// data, but we'll just increase it to the size needed.
int appSize = engine.getSession().getApplicationBufferSize();
ByteBuffer b = ByteBuffer.allocate(appSize + dst.position());
dst.flip();
b.put(dst);
dst = b;
// retry the operation.
break;
BUFFER_UNDERFLOW:
int netSize = engine.getSession().getPacketBufferSize();
// Resize buffer if needed.
if (netSize > dst.capacity()) {
ByteBuffer b = ByteBuffer.allocate(netSize);
src.flip();
b.put(src);
src = b;
}
// Obtain more inbound network data for src,
// then retry the operation.
break;
// other cases: CLOSED, OK.
}
```

Unlike

SSLSocket

, all methods of SSLEngine are
non-blocking.

SSLEngine

implementations may
require the results of tasks that may take an extended period of
time to complete, or may even block. For example, a TrustManager
may need to connect to a remote certificate validation service,
or a KeyManager might need to prompt a user to determine which
certificate to use as part of client authentication. Additionally,
creating cryptographic signatures and verifying them can be slow,
seemingly blocking.

For any operation which may potentially block, the

SSLEngine

will create a

Runnable

delegated task. When

SSLEngineResult

indicates that a
delegated task result is needed, the application must call

getDelegatedTask()

to obtain an outstanding delegated task and
call its

run()

method (possibly using
a different thread depending on the compute strategy). The
application should continue obtaining delegated tasks until no more
exist, and try the original operation again.

At the end of a communication session, applications should properly
close the SSL/TLS/DTLS link. The SSL/TLS/DTLS protocols have closure
handshake messages, and these messages should be communicated to the
peer before releasing the

SSLEngine

and closing the
underlying transport mechanism. A close can be initiated by one of:
an SSLException, an inbound closure handshake message, or one of the
close methods. In all cases, closure handshake messages are
generated by the engine, and

wrap()

should be repeatedly
called until the resulting

SSLEngineResult

's status
returns "CLOSED", or

isOutboundDone()

returns true. All
data obtained from the

wrap()

method should be sent to the
peer.

closeOutbound()

is used to signal the engine that the
application will not be sending any more data.

A peer will signal its intent to close by sending its own closure
handshake message. After this message has been received and
processed by the local

SSLEngine

's

unwrap()

call, the application can detect the close by calling

unwrap()

and looking for a

SSLEngineResult

with status "CLOSED", or if

isInboundDone()

returns true.
If for some reason the peer closes the communication link without
sending the proper SSL/TLS/DTLS closure message, the application can
detect the end-of-stream and can signal the engine via

closeInbound()

that there will no more inbound messages to
process. Some applications might choose to require orderly shutdown
messages from a peer, in which case they can check that the closure
was generated by a handshake message and not by an end-of-stream
condition.

There are two groups of cipher suites which you will need to know
about when managing cipher suites:

- Supported

cipher suites: all the suites which are
supported by the SSL implementation. This list is reported
using

getSupportedCipherSuites()

.

Enabled

cipher suites, which may be fewer than
the full set of supported suites. This group is set using the

setEnabledCipherSuites(String [])

method, and
queried using the

getEnabledCipherSuites()

method.
Initially, a default set of cipher suites will be enabled on a
new engine that represents the minimum suggested
configuration.

Implementation defaults require that only cipher suites which
authenticate servers and provide confidentiality be enabled by
default. Only if both sides explicitly agree to unauthenticated
and/or non-private (unencrypted) communications will such a
cipher suite be selected.

Each SSL/TLS/DTLS connection must have one client and one server, thus
each endpoint must decide which role to assume. This choice determines
who begins the handshaking process as well as which type of messages
should be sent by each party. The method

setUseClientMode(boolean)

configures the mode. Note that the
default mode for a new

SSLEngine

is provider-specific.
Applications should set the mode explicitly before invoking other
methods of the

SSLEngine

. Once the initial handshaking has
started, an

SSLEngine

can not switch between client and server
modes, even when performing renegotiations.

Applications might choose to process delegated tasks in different
threads. When an

SSLEngine

is created, the current

AccessControlContext

is saved. All future delegated tasks will be processed using this
context: that is, all access control decisions will be made using the
context captured at engine creation.

Concurrency Notes

:
There are two concurrency issues to be aware of:

- The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

Creation - The

SSLEngine

has been created and
initialized, but has not yet been used. During this phase, an
application may set any

SSLEngine

-specific settings
(enabled cipher suites, whether the

SSLEngine

should
handshake in client or server mode, and so on). Once
handshaking has begun, though, any new settings (except
client/server mode, see below) will be used for
the next handshake.

Initial Handshake - The initial handshake is a procedure by
which the two peers exchange communication parameters until an
SSLSession is established. Application data can not be sent during
this phase.

Application Data - Once the communication parameters have
been established and the handshake is complete, application data
may flow through the

SSLEngine

. Outbound
application messages are encrypted and integrity protected,
and inbound messages reverse the process.

Rehandshaking - Either side may request a renegotiation of
the session at any time during the Application Data phase. New
handshaking data can be intermixed among the application data.
Before starting the rehandshake phase, the application may
reset the SSL/TLS/DTLS communication parameters such as the list of
enabled ciphersuites and whether to use client authentication,
but can not change between client/server modes. As before, once
handshaking has begun, any new

SSLEngine

configuration settings will not be used until the next
handshake.

Closure - When the connection is no longer needed, the client
and the server applications should each close both sides of their
respective connections. For

SSLEngine

objects, an
application should call

closeOutbound()

and
send any remaining messages to the peer. Likewise, an application
should receive any remaining messages from the peer before calling

closeInbound()

. The underlying transport mechanism
can then be closed after both sides of the

SSLEngine

have
been closed. If the connection is not closed in an orderly manner
(for example

closeInbound()

is called before the
peer's write closure notification has been received), exceptions
will be raised to indicate that an error has occurred. Once an
engine is closed, it is not reusable: a new

SSLEngine

must be created.

Data moves through the engine by calling

wrap()

or

unwrap()

on outbound or inbound data, respectively. Depending on
the state of the

SSLEngine

, a

wrap()

call
may consume application data from the source buffer and may produce
network data in the destination buffer. The outbound data
may contain application and/or handshake data. A call to

unwrap()

will examine the source buffer and may
advance the handshake if the data is handshaking information, or
may place application data in the destination buffer if the data
is application. The state of the underlying SSL/TLS/DTLS algorithm
will determine when data is consumed and produced.

Calls to

wrap()

and

unwrap()

return an

SSLEngineResult

which indicates the status of the
operation, and (optionally) how to interact with the engine to make
progress.

The

SSLEngine

produces/consumes complete SSL/TLS/DTLS
packets only, and does not store application data internally between
calls to

wrap()/unwrap()

. Thus input and output

ByteBuffer

s must be sized appropriately to hold the
maximum record that can be produced. Calls to

SSLSession.getPacketBufferSize()

and

SSLSession.getApplicationBufferSize()

should be used to determine
the appropriate buffer sizes. The size of the outbound application
data buffer generally does not matter. If buffer conditions do not
allow for the proper consumption/production of data, the application
must determine (via

SSLEngineResult

) and correct the
problem, and then try the call again.

For example,

unwrap()

will return a

SSLEngineResult.Status.BUFFER_OVERFLOW

result if the engine
determines that there is not enough destination buffer space available.
Applications should call

SSLSession.getApplicationBufferSize()

and compare that value with the space available in the destination buffer,
enlarging the buffer if necessary. Similarly, if

unwrap()

were to return a

SSLEngineResult.Status.BUFFER_UNDERFLOW

, the
application should call

SSLSession.getPacketBufferSize()

to ensure
that the source buffer has enough room to hold a record (enlarging if
necessary), and then obtain more inbound data.

```java
SSLEngineResult r = engine.unwrap(src, dst);
switch (r.getStatus()) {
BUFFER_OVERFLOW:
// Could attempt to drain the dst buffer of any already obtained
// data, but we'll just increase it to the size needed.
int appSize = engine.getSession().getApplicationBufferSize();
ByteBuffer b = ByteBuffer.allocate(appSize + dst.position());
dst.flip();
b.put(dst);
dst = b;
// retry the operation.
break;
BUFFER_UNDERFLOW:
int netSize = engine.getSession().getPacketBufferSize();
// Resize buffer if needed.
if (netSize > dst.capacity()) {
ByteBuffer b = ByteBuffer.allocate(netSize);
src.flip();
b.put(src);
src = b;
}
// Obtain more inbound network data for src,
// then retry the operation.
break;
// other cases: CLOSED, OK.
}
```

Unlike

SSLSocket

, all methods of SSLEngine are
non-blocking.

SSLEngine

implementations may
require the results of tasks that may take an extended period of
time to complete, or may even block. For example, a TrustManager
may need to connect to a remote certificate validation service,
or a KeyManager might need to prompt a user to determine which
certificate to use as part of client authentication. Additionally,
creating cryptographic signatures and verifying them can be slow,
seemingly blocking.

For any operation which may potentially block, the

SSLEngine

will create a

Runnable

delegated task. When

SSLEngineResult

indicates that a
delegated task result is needed, the application must call

getDelegatedTask()

to obtain an outstanding delegated task and
call its

run()

method (possibly using
a different thread depending on the compute strategy). The
application should continue obtaining delegated tasks until no more
exist, and try the original operation again.

At the end of a communication session, applications should properly
close the SSL/TLS/DTLS link. The SSL/TLS/DTLS protocols have closure
handshake messages, and these messages should be communicated to the
peer before releasing the

SSLEngine

and closing the
underlying transport mechanism. A close can be initiated by one of:
an SSLException, an inbound closure handshake message, or one of the
close methods. In all cases, closure handshake messages are
generated by the engine, and

wrap()

should be repeatedly
called until the resulting

SSLEngineResult

's status
returns "CLOSED", or

isOutboundDone()

returns true. All
data obtained from the

wrap()

method should be sent to the
peer.

closeOutbound()

is used to signal the engine that the
application will not be sending any more data.

A peer will signal its intent to close by sending its own closure
handshake message. After this message has been received and
processed by the local

SSLEngine

's

unwrap()

call, the application can detect the close by calling

unwrap()

and looking for a

SSLEngineResult

with status "CLOSED", or if

isInboundDone()

returns true.
If for some reason the peer closes the communication link without
sending the proper SSL/TLS/DTLS closure message, the application can
detect the end-of-stream and can signal the engine via

closeInbound()

that there will no more inbound messages to
process. Some applications might choose to require orderly shutdown
messages from a peer, in which case they can check that the closure
was generated by a handshake message and not by an end-of-stream
condition.

There are two groups of cipher suites which you will need to know
about when managing cipher suites:

- Supported

cipher suites: all the suites which are
supported by the SSL implementation. This list is reported
using

getSupportedCipherSuites()

.

Enabled

cipher suites, which may be fewer than
the full set of supported suites. This group is set using the

setEnabledCipherSuites(String [])

method, and
queried using the

getEnabledCipherSuites()

method.
Initially, a default set of cipher suites will be enabled on a
new engine that represents the minimum suggested
configuration.

Implementation defaults require that only cipher suites which
authenticate servers and provide confidentiality be enabled by
default. Only if both sides explicitly agree to unauthenticated
and/or non-private (unencrypted) communications will such a
cipher suite be selected.

Each SSL/TLS/DTLS connection must have one client and one server, thus
each endpoint must decide which role to assume. This choice determines
who begins the handshaking process as well as which type of messages
should be sent by each party. The method

setUseClientMode(boolean)

configures the mode. Note that the
default mode for a new

SSLEngine

is provider-specific.
Applications should set the mode explicitly before invoking other
methods of the

SSLEngine

. Once the initial handshaking has
started, an

SSLEngine

can not switch between client and server
modes, even when performing renegotiations.

Applications might choose to process delegated tasks in different
threads. When an

SSLEngine

is created, the current

AccessControlContext

is saved. All future delegated tasks will be processed using this
context: that is, all access control decisions will be made using the
context captured at engine creation.

Concurrency Notes

:
There are two concurrency issues to be aware of:

- The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

Calls to

wrap()

and

unwrap()

return an

SSLEngineResult

which indicates the status of the
operation, and (optionally) how to interact with the engine to make
progress.

The

SSLEngine

produces/consumes complete SSL/TLS/DTLS
packets only, and does not store application data internally between
calls to

wrap()/unwrap()

. Thus input and output

ByteBuffer

s must be sized appropriately to hold the
maximum record that can be produced. Calls to

SSLSession.getPacketBufferSize()

and

SSLSession.getApplicationBufferSize()

should be used to determine
the appropriate buffer sizes. The size of the outbound application
data buffer generally does not matter. If buffer conditions do not
allow for the proper consumption/production of data, the application
must determine (via

SSLEngineResult

) and correct the
problem, and then try the call again.

For example,

unwrap()

will return a

SSLEngineResult.Status.BUFFER_OVERFLOW

result if the engine
determines that there is not enough destination buffer space available.
Applications should call

SSLSession.getApplicationBufferSize()

and compare that value with the space available in the destination buffer,
enlarging the buffer if necessary. Similarly, if

unwrap()

were to return a

SSLEngineResult.Status.BUFFER_UNDERFLOW

, the
application should call

SSLSession.getPacketBufferSize()

to ensure
that the source buffer has enough room to hold a record (enlarging if
necessary), and then obtain more inbound data.

```java
SSLEngineResult r = engine.unwrap(src, dst);
switch (r.getStatus()) {
BUFFER_OVERFLOW:
// Could attempt to drain the dst buffer of any already obtained
// data, but we'll just increase it to the size needed.
int appSize = engine.getSession().getApplicationBufferSize();
ByteBuffer b = ByteBuffer.allocate(appSize + dst.position());
dst.flip();
b.put(dst);
dst = b;
// retry the operation.
break;
BUFFER_UNDERFLOW:
int netSize = engine.getSession().getPacketBufferSize();
// Resize buffer if needed.
if (netSize > dst.capacity()) {
ByteBuffer b = ByteBuffer.allocate(netSize);
src.flip();
b.put(src);
src = b;
}
// Obtain more inbound network data for src,
// then retry the operation.
break;
// other cases: CLOSED, OK.
}
```

Unlike

SSLSocket

, all methods of SSLEngine are
non-blocking.

SSLEngine

implementations may
require the results of tasks that may take an extended period of
time to complete, or may even block. For example, a TrustManager
may need to connect to a remote certificate validation service,
or a KeyManager might need to prompt a user to determine which
certificate to use as part of client authentication. Additionally,
creating cryptographic signatures and verifying them can be slow,
seemingly blocking.

For any operation which may potentially block, the

SSLEngine

will create a

Runnable

delegated task. When

SSLEngineResult

indicates that a
delegated task result is needed, the application must call

getDelegatedTask()

to obtain an outstanding delegated task and
call its

run()

method (possibly using
a different thread depending on the compute strategy). The
application should continue obtaining delegated tasks until no more
exist, and try the original operation again.

At the end of a communication session, applications should properly
close the SSL/TLS/DTLS link. The SSL/TLS/DTLS protocols have closure
handshake messages, and these messages should be communicated to the
peer before releasing the

SSLEngine

and closing the
underlying transport mechanism. A close can be initiated by one of:
an SSLException, an inbound closure handshake message, or one of the
close methods. In all cases, closure handshake messages are
generated by the engine, and

wrap()

should be repeatedly
called until the resulting

SSLEngineResult

's status
returns "CLOSED", or

isOutboundDone()

returns true. All
data obtained from the

wrap()

method should be sent to the
peer.

closeOutbound()

is used to signal the engine that the
application will not be sending any more data.

A peer will signal its intent to close by sending its own closure
handshake message. After this message has been received and
processed by the local

SSLEngine

's

unwrap()

call, the application can detect the close by calling

unwrap()

and looking for a

SSLEngineResult

with status "CLOSED", or if

isInboundDone()

returns true.
If for some reason the peer closes the communication link without
sending the proper SSL/TLS/DTLS closure message, the application can
detect the end-of-stream and can signal the engine via

closeInbound()

that there will no more inbound messages to
process. Some applications might choose to require orderly shutdown
messages from a peer, in which case they can check that the closure
was generated by a handshake message and not by an end-of-stream
condition.

There are two groups of cipher suites which you will need to know
about when managing cipher suites:

- Supported

cipher suites: all the suites which are
supported by the SSL implementation. This list is reported
using

getSupportedCipherSuites()

.

Enabled

cipher suites, which may be fewer than
the full set of supported suites. This group is set using the

setEnabledCipherSuites(String [])

method, and
queried using the

getEnabledCipherSuites()

method.
Initially, a default set of cipher suites will be enabled on a
new engine that represents the minimum suggested
configuration.

Implementation defaults require that only cipher suites which
authenticate servers and provide confidentiality be enabled by
default. Only if both sides explicitly agree to unauthenticated
and/or non-private (unencrypted) communications will such a
cipher suite be selected.

Each SSL/TLS/DTLS connection must have one client and one server, thus
each endpoint must decide which role to assume. This choice determines
who begins the handshaking process as well as which type of messages
should be sent by each party. The method

setUseClientMode(boolean)

configures the mode. Note that the
default mode for a new

SSLEngine

is provider-specific.
Applications should set the mode explicitly before invoking other
methods of the

SSLEngine

. Once the initial handshaking has
started, an

SSLEngine

can not switch between client and server
modes, even when performing renegotiations.

Applications might choose to process delegated tasks in different
threads. When an

SSLEngine

is created, the current

AccessControlContext

is saved. All future delegated tasks will be processed using this
context: that is, all access control decisions will be made using the
context captured at engine creation.

Concurrency Notes

:
There are two concurrency issues to be aware of:

- The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

The

SSLEngine

produces/consumes complete SSL/TLS/DTLS
packets only, and does not store application data internally between
calls to

wrap()/unwrap()

. Thus input and output

ByteBuffer

s must be sized appropriately to hold the
maximum record that can be produced. Calls to

SSLSession.getPacketBufferSize()

and

SSLSession.getApplicationBufferSize()

should be used to determine
the appropriate buffer sizes. The size of the outbound application
data buffer generally does not matter. If buffer conditions do not
allow for the proper consumption/production of data, the application
must determine (via

SSLEngineResult

) and correct the
problem, and then try the call again.

For example,

unwrap()

will return a

SSLEngineResult.Status.BUFFER_OVERFLOW

result if the engine
determines that there is not enough destination buffer space available.
Applications should call

SSLSession.getApplicationBufferSize()

and compare that value with the space available in the destination buffer,
enlarging the buffer if necessary. Similarly, if

unwrap()

were to return a

SSLEngineResult.Status.BUFFER_UNDERFLOW

, the
application should call

SSLSession.getPacketBufferSize()

to ensure
that the source buffer has enough room to hold a record (enlarging if
necessary), and then obtain more inbound data.

```java
SSLEngineResult r = engine.unwrap(src, dst);
switch (r.getStatus()) {
BUFFER_OVERFLOW:
// Could attempt to drain the dst buffer of any already obtained
// data, but we'll just increase it to the size needed.
int appSize = engine.getSession().getApplicationBufferSize();
ByteBuffer b = ByteBuffer.allocate(appSize + dst.position());
dst.flip();
b.put(dst);
dst = b;
// retry the operation.
break;
BUFFER_UNDERFLOW:
int netSize = engine.getSession().getPacketBufferSize();
// Resize buffer if needed.
if (netSize > dst.capacity()) {
ByteBuffer b = ByteBuffer.allocate(netSize);
src.flip();
b.put(src);
src = b;
}
// Obtain more inbound network data for src,
// then retry the operation.
break;
// other cases: CLOSED, OK.
}
```

Unlike

SSLSocket

, all methods of SSLEngine are
non-blocking.

SSLEngine

implementations may
require the results of tasks that may take an extended period of
time to complete, or may even block. For example, a TrustManager
may need to connect to a remote certificate validation service,
or a KeyManager might need to prompt a user to determine which
certificate to use as part of client authentication. Additionally,
creating cryptographic signatures and verifying them can be slow,
seemingly blocking.

For any operation which may potentially block, the

SSLEngine

will create a

Runnable

delegated task. When

SSLEngineResult

indicates that a
delegated task result is needed, the application must call

getDelegatedTask()

to obtain an outstanding delegated task and
call its

run()

method (possibly using
a different thread depending on the compute strategy). The
application should continue obtaining delegated tasks until no more
exist, and try the original operation again.

At the end of a communication session, applications should properly
close the SSL/TLS/DTLS link. The SSL/TLS/DTLS protocols have closure
handshake messages, and these messages should be communicated to the
peer before releasing the

SSLEngine

and closing the
underlying transport mechanism. A close can be initiated by one of:
an SSLException, an inbound closure handshake message, or one of the
close methods. In all cases, closure handshake messages are
generated by the engine, and

wrap()

should be repeatedly
called until the resulting

SSLEngineResult

's status
returns "CLOSED", or

isOutboundDone()

returns true. All
data obtained from the

wrap()

method should be sent to the
peer.

closeOutbound()

is used to signal the engine that the
application will not be sending any more data.

A peer will signal its intent to close by sending its own closure
handshake message. After this message has been received and
processed by the local

SSLEngine

's

unwrap()

call, the application can detect the close by calling

unwrap()

and looking for a

SSLEngineResult

with status "CLOSED", or if

isInboundDone()

returns true.
If for some reason the peer closes the communication link without
sending the proper SSL/TLS/DTLS closure message, the application can
detect the end-of-stream and can signal the engine via

closeInbound()

that there will no more inbound messages to
process. Some applications might choose to require orderly shutdown
messages from a peer, in which case they can check that the closure
was generated by a handshake message and not by an end-of-stream
condition.

There are two groups of cipher suites which you will need to know
about when managing cipher suites:

- Supported

cipher suites: all the suites which are
supported by the SSL implementation. This list is reported
using

getSupportedCipherSuites()

.

Enabled

cipher suites, which may be fewer than
the full set of supported suites. This group is set using the

setEnabledCipherSuites(String [])

method, and
queried using the

getEnabledCipherSuites()

method.
Initially, a default set of cipher suites will be enabled on a
new engine that represents the minimum suggested
configuration.

Implementation defaults require that only cipher suites which
authenticate servers and provide confidentiality be enabled by
default. Only if both sides explicitly agree to unauthenticated
and/or non-private (unencrypted) communications will such a
cipher suite be selected.

Each SSL/TLS/DTLS connection must have one client and one server, thus
each endpoint must decide which role to assume. This choice determines
who begins the handshaking process as well as which type of messages
should be sent by each party. The method

setUseClientMode(boolean)

configures the mode. Note that the
default mode for a new

SSLEngine

is provider-specific.
Applications should set the mode explicitly before invoking other
methods of the

SSLEngine

. Once the initial handshaking has
started, an

SSLEngine

can not switch between client and server
modes, even when performing renegotiations.

Applications might choose to process delegated tasks in different
threads. When an

SSLEngine

is created, the current

AccessControlContext

is saved. All future delegated tasks will be processed using this
context: that is, all access control decisions will be made using the
context captured at engine creation.

Concurrency Notes

:
There are two concurrency issues to be aware of:

- The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

For example,

unwrap()

will return a

SSLEngineResult.Status.BUFFER_OVERFLOW

result if the engine
determines that there is not enough destination buffer space available.
Applications should call

SSLSession.getApplicationBufferSize()

and compare that value with the space available in the destination buffer,
enlarging the buffer if necessary. Similarly, if

unwrap()

were to return a

SSLEngineResult.Status.BUFFER_UNDERFLOW

, the
application should call

SSLSession.getPacketBufferSize()

to ensure
that the source buffer has enough room to hold a record (enlarging if
necessary), and then obtain more inbound data.

```java
SSLEngineResult r = engine.unwrap(src, dst);
switch (r.getStatus()) {
BUFFER_OVERFLOW:
// Could attempt to drain the dst buffer of any already obtained
// data, but we'll just increase it to the size needed.
int appSize = engine.getSession().getApplicationBufferSize();
ByteBuffer b = ByteBuffer.allocate(appSize + dst.position());
dst.flip();
b.put(dst);
dst = b;
// retry the operation.
break;
BUFFER_UNDERFLOW:
int netSize = engine.getSession().getPacketBufferSize();
// Resize buffer if needed.
if (netSize > dst.capacity()) {
ByteBuffer b = ByteBuffer.allocate(netSize);
src.flip();
b.put(src);
src = b;
}
// Obtain more inbound network data for src,
// then retry the operation.
break;
// other cases: CLOSED, OK.
}
```

Unlike

SSLSocket

, all methods of SSLEngine are
non-blocking.

SSLEngine

implementations may
require the results of tasks that may take an extended period of
time to complete, or may even block. For example, a TrustManager
may need to connect to a remote certificate validation service,
or a KeyManager might need to prompt a user to determine which
certificate to use as part of client authentication. Additionally,
creating cryptographic signatures and verifying them can be slow,
seemingly blocking.

For any operation which may potentially block, the

SSLEngine

will create a

Runnable

delegated task. When

SSLEngineResult

indicates that a
delegated task result is needed, the application must call

getDelegatedTask()

to obtain an outstanding delegated task and
call its

run()

method (possibly using
a different thread depending on the compute strategy). The
application should continue obtaining delegated tasks until no more
exist, and try the original operation again.

At the end of a communication session, applications should properly
close the SSL/TLS/DTLS link. The SSL/TLS/DTLS protocols have closure
handshake messages, and these messages should be communicated to the
peer before releasing the

SSLEngine

and closing the
underlying transport mechanism. A close can be initiated by one of:
an SSLException, an inbound closure handshake message, or one of the
close methods. In all cases, closure handshake messages are
generated by the engine, and

wrap()

should be repeatedly
called until the resulting

SSLEngineResult

's status
returns "CLOSED", or

isOutboundDone()

returns true. All
data obtained from the

wrap()

method should be sent to the
peer.

closeOutbound()

is used to signal the engine that the
application will not be sending any more data.

A peer will signal its intent to close by sending its own closure
handshake message. After this message has been received and
processed by the local

SSLEngine

's

unwrap()

call, the application can detect the close by calling

unwrap()

and looking for a

SSLEngineResult

with status "CLOSED", or if

isInboundDone()

returns true.
If for some reason the peer closes the communication link without
sending the proper SSL/TLS/DTLS closure message, the application can
detect the end-of-stream and can signal the engine via

closeInbound()

that there will no more inbound messages to
process. Some applications might choose to require orderly shutdown
messages from a peer, in which case they can check that the closure
was generated by a handshake message and not by an end-of-stream
condition.

There are two groups of cipher suites which you will need to know
about when managing cipher suites:

- Supported

cipher suites: all the suites which are
supported by the SSL implementation. This list is reported
using

getSupportedCipherSuites()

.

Enabled

cipher suites, which may be fewer than
the full set of supported suites. This group is set using the

setEnabledCipherSuites(String [])

method, and
queried using the

getEnabledCipherSuites()

method.
Initially, a default set of cipher suites will be enabled on a
new engine that represents the minimum suggested
configuration.

Implementation defaults require that only cipher suites which
authenticate servers and provide confidentiality be enabled by
default. Only if both sides explicitly agree to unauthenticated
and/or non-private (unencrypted) communications will such a
cipher suite be selected.

Each SSL/TLS/DTLS connection must have one client and one server, thus
each endpoint must decide which role to assume. This choice determines
who begins the handshaking process as well as which type of messages
should be sent by each party. The method

setUseClientMode(boolean)

configures the mode. Note that the
default mode for a new

SSLEngine

is provider-specific.
Applications should set the mode explicitly before invoking other
methods of the

SSLEngine

. Once the initial handshaking has
started, an

SSLEngine

can not switch between client and server
modes, even when performing renegotiations.

Applications might choose to process delegated tasks in different
threads. When an

SSLEngine

is created, the current

AccessControlContext

is saved. All future delegated tasks will be processed using this
context: that is, all access control decisions will be made using the
context captured at engine creation.

Concurrency Notes

:
There are two concurrency issues to be aware of:

- The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

SSLEngineResult r = engine.unwrap(src, dst);
switch (r.getStatus()) {
BUFFER_OVERFLOW:
// Could attempt to drain the dst buffer of any already obtained
// data, but we'll just increase it to the size needed.
int appSize = engine.getSession().getApplicationBufferSize();
ByteBuffer b = ByteBuffer.allocate(appSize + dst.position());
dst.flip();
b.put(dst);
dst = b;
// retry the operation.
break;
BUFFER_UNDERFLOW:
int netSize = engine.getSession().getPacketBufferSize();
// Resize buffer if needed.
if (netSize > dst.capacity()) {
ByteBuffer b = ByteBuffer.allocate(netSize);
src.flip();
b.put(src);
src = b;
}
// Obtain more inbound network data for src,
// then retry the operation.
break;
// other cases: CLOSED, OK.
}

Unlike

SSLSocket

, all methods of SSLEngine are
non-blocking.

SSLEngine

implementations may
require the results of tasks that may take an extended period of
time to complete, or may even block. For example, a TrustManager
may need to connect to a remote certificate validation service,
or a KeyManager might need to prompt a user to determine which
certificate to use as part of client authentication. Additionally,
creating cryptographic signatures and verifying them can be slow,
seemingly blocking.

For any operation which may potentially block, the

SSLEngine

will create a

Runnable

delegated task. When

SSLEngineResult

indicates that a
delegated task result is needed, the application must call

getDelegatedTask()

to obtain an outstanding delegated task and
call its

run()

method (possibly using
a different thread depending on the compute strategy). The
application should continue obtaining delegated tasks until no more
exist, and try the original operation again.

At the end of a communication session, applications should properly
close the SSL/TLS/DTLS link. The SSL/TLS/DTLS protocols have closure
handshake messages, and these messages should be communicated to the
peer before releasing the

SSLEngine

and closing the
underlying transport mechanism. A close can be initiated by one of:
an SSLException, an inbound closure handshake message, or one of the
close methods. In all cases, closure handshake messages are
generated by the engine, and

wrap()

should be repeatedly
called until the resulting

SSLEngineResult

's status
returns "CLOSED", or

isOutboundDone()

returns true. All
data obtained from the

wrap()

method should be sent to the
peer.

closeOutbound()

is used to signal the engine that the
application will not be sending any more data.

A peer will signal its intent to close by sending its own closure
handshake message. After this message has been received and
processed by the local

SSLEngine

's

unwrap()

call, the application can detect the close by calling

unwrap()

and looking for a

SSLEngineResult

with status "CLOSED", or if

isInboundDone()

returns true.
If for some reason the peer closes the communication link without
sending the proper SSL/TLS/DTLS closure message, the application can
detect the end-of-stream and can signal the engine via

closeInbound()

that there will no more inbound messages to
process. Some applications might choose to require orderly shutdown
messages from a peer, in which case they can check that the closure
was generated by a handshake message and not by an end-of-stream
condition.

There are two groups of cipher suites which you will need to know
about when managing cipher suites:

- Supported

cipher suites: all the suites which are
supported by the SSL implementation. This list is reported
using

getSupportedCipherSuites()

.

Enabled

cipher suites, which may be fewer than
the full set of supported suites. This group is set using the

setEnabledCipherSuites(String [])

method, and
queried using the

getEnabledCipherSuites()

method.
Initially, a default set of cipher suites will be enabled on a
new engine that represents the minimum suggested
configuration.

Implementation defaults require that only cipher suites which
authenticate servers and provide confidentiality be enabled by
default. Only if both sides explicitly agree to unauthenticated
and/or non-private (unencrypted) communications will such a
cipher suite be selected.

Each SSL/TLS/DTLS connection must have one client and one server, thus
each endpoint must decide which role to assume. This choice determines
who begins the handshaking process as well as which type of messages
should be sent by each party. The method

setUseClientMode(boolean)

configures the mode. Note that the
default mode for a new

SSLEngine

is provider-specific.
Applications should set the mode explicitly before invoking other
methods of the

SSLEngine

. Once the initial handshaking has
started, an

SSLEngine

can not switch between client and server
modes, even when performing renegotiations.

Applications might choose to process delegated tasks in different
threads. When an

SSLEngine

is created, the current

AccessControlContext

is saved. All future delegated tasks will be processed using this
context: that is, all access control decisions will be made using the
context captured at engine creation.

Concurrency Notes

:
There are two concurrency issues to be aware of:

- The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

For any operation which may potentially block, the

SSLEngine

will create a

Runnable

delegated task. When

SSLEngineResult

indicates that a
delegated task result is needed, the application must call

getDelegatedTask()

to obtain an outstanding delegated task and
call its

run()

method (possibly using
a different thread depending on the compute strategy). The
application should continue obtaining delegated tasks until no more
exist, and try the original operation again.

At the end of a communication session, applications should properly
close the SSL/TLS/DTLS link. The SSL/TLS/DTLS protocols have closure
handshake messages, and these messages should be communicated to the
peer before releasing the

SSLEngine

and closing the
underlying transport mechanism. A close can be initiated by one of:
an SSLException, an inbound closure handshake message, or one of the
close methods. In all cases, closure handshake messages are
generated by the engine, and

wrap()

should be repeatedly
called until the resulting

SSLEngineResult

's status
returns "CLOSED", or

isOutboundDone()

returns true. All
data obtained from the

wrap()

method should be sent to the
peer.

closeOutbound()

is used to signal the engine that the
application will not be sending any more data.

A peer will signal its intent to close by sending its own closure
handshake message. After this message has been received and
processed by the local

SSLEngine

's

unwrap()

call, the application can detect the close by calling

unwrap()

and looking for a

SSLEngineResult

with status "CLOSED", or if

isInboundDone()

returns true.
If for some reason the peer closes the communication link without
sending the proper SSL/TLS/DTLS closure message, the application can
detect the end-of-stream and can signal the engine via

closeInbound()

that there will no more inbound messages to
process. Some applications might choose to require orderly shutdown
messages from a peer, in which case they can check that the closure
was generated by a handshake message and not by an end-of-stream
condition.

There are two groups of cipher suites which you will need to know
about when managing cipher suites:

- Supported

cipher suites: all the suites which are
supported by the SSL implementation. This list is reported
using

getSupportedCipherSuites()

.

Enabled

cipher suites, which may be fewer than
the full set of supported suites. This group is set using the

setEnabledCipherSuites(String [])

method, and
queried using the

getEnabledCipherSuites()

method.
Initially, a default set of cipher suites will be enabled on a
new engine that represents the minimum suggested
configuration.

Implementation defaults require that only cipher suites which
authenticate servers and provide confidentiality be enabled by
default. Only if both sides explicitly agree to unauthenticated
and/or non-private (unencrypted) communications will such a
cipher suite be selected.

Each SSL/TLS/DTLS connection must have one client and one server, thus
each endpoint must decide which role to assume. This choice determines
who begins the handshaking process as well as which type of messages
should be sent by each party. The method

setUseClientMode(boolean)

configures the mode. Note that the
default mode for a new

SSLEngine

is provider-specific.
Applications should set the mode explicitly before invoking other
methods of the

SSLEngine

. Once the initial handshaking has
started, an

SSLEngine

can not switch between client and server
modes, even when performing renegotiations.

Applications might choose to process delegated tasks in different
threads. When an

SSLEngine

is created, the current

AccessControlContext

is saved. All future delegated tasks will be processed using this
context: that is, all access control decisions will be made using the
context captured at engine creation.

Concurrency Notes

:
There are two concurrency issues to be aware of:

- The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

At the end of a communication session, applications should properly
close the SSL/TLS/DTLS link. The SSL/TLS/DTLS protocols have closure
handshake messages, and these messages should be communicated to the
peer before releasing the

SSLEngine

and closing the
underlying transport mechanism. A close can be initiated by one of:
an SSLException, an inbound closure handshake message, or one of the
close methods. In all cases, closure handshake messages are
generated by the engine, and

wrap()

should be repeatedly
called until the resulting

SSLEngineResult

's status
returns "CLOSED", or

isOutboundDone()

returns true. All
data obtained from the

wrap()

method should be sent to the
peer.

closeOutbound()

is used to signal the engine that the
application will not be sending any more data.

A peer will signal its intent to close by sending its own closure
handshake message. After this message has been received and
processed by the local

SSLEngine

's

unwrap()

call, the application can detect the close by calling

unwrap()

and looking for a

SSLEngineResult

with status "CLOSED", or if

isInboundDone()

returns true.
If for some reason the peer closes the communication link without
sending the proper SSL/TLS/DTLS closure message, the application can
detect the end-of-stream and can signal the engine via

closeInbound()

that there will no more inbound messages to
process. Some applications might choose to require orderly shutdown
messages from a peer, in which case they can check that the closure
was generated by a handshake message and not by an end-of-stream
condition.

There are two groups of cipher suites which you will need to know
about when managing cipher suites:

- Supported

cipher suites: all the suites which are
supported by the SSL implementation. This list is reported
using

getSupportedCipherSuites()

.

Enabled

cipher suites, which may be fewer than
the full set of supported suites. This group is set using the

setEnabledCipherSuites(String [])

method, and
queried using the

getEnabledCipherSuites()

method.
Initially, a default set of cipher suites will be enabled on a
new engine that represents the minimum suggested
configuration.

Implementation defaults require that only cipher suites which
authenticate servers and provide confidentiality be enabled by
default. Only if both sides explicitly agree to unauthenticated
and/or non-private (unencrypted) communications will such a
cipher suite be selected.

Each SSL/TLS/DTLS connection must have one client and one server, thus
each endpoint must decide which role to assume. This choice determines
who begins the handshaking process as well as which type of messages
should be sent by each party. The method

setUseClientMode(boolean)

configures the mode. Note that the
default mode for a new

SSLEngine

is provider-specific.
Applications should set the mode explicitly before invoking other
methods of the

SSLEngine

. Once the initial handshaking has
started, an

SSLEngine

can not switch between client and server
modes, even when performing renegotiations.

Applications might choose to process delegated tasks in different
threads. When an

SSLEngine

is created, the current

AccessControlContext

is saved. All future delegated tasks will be processed using this
context: that is, all access control decisions will be made using the
context captured at engine creation.

Concurrency Notes

:
There are two concurrency issues to be aware of:

- The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

closeOutbound()

is used to signal the engine that the
application will not be sending any more data.

A peer will signal its intent to close by sending its own closure
handshake message. After this message has been received and
processed by the local

SSLEngine

's

unwrap()

call, the application can detect the close by calling

unwrap()

and looking for a

SSLEngineResult

with status "CLOSED", or if

isInboundDone()

returns true.
If for some reason the peer closes the communication link without
sending the proper SSL/TLS/DTLS closure message, the application can
detect the end-of-stream and can signal the engine via

closeInbound()

that there will no more inbound messages to
process. Some applications might choose to require orderly shutdown
messages from a peer, in which case they can check that the closure
was generated by a handshake message and not by an end-of-stream
condition.

There are two groups of cipher suites which you will need to know
about when managing cipher suites:

- Supported

cipher suites: all the suites which are
supported by the SSL implementation. This list is reported
using

getSupportedCipherSuites()

.

Enabled

cipher suites, which may be fewer than
the full set of supported suites. This group is set using the

setEnabledCipherSuites(String [])

method, and
queried using the

getEnabledCipherSuites()

method.
Initially, a default set of cipher suites will be enabled on a
new engine that represents the minimum suggested
configuration.

Implementation defaults require that only cipher suites which
authenticate servers and provide confidentiality be enabled by
default. Only if both sides explicitly agree to unauthenticated
and/or non-private (unencrypted) communications will such a
cipher suite be selected.

Each SSL/TLS/DTLS connection must have one client and one server, thus
each endpoint must decide which role to assume. This choice determines
who begins the handshaking process as well as which type of messages
should be sent by each party. The method

setUseClientMode(boolean)

configures the mode. Note that the
default mode for a new

SSLEngine

is provider-specific.
Applications should set the mode explicitly before invoking other
methods of the

SSLEngine

. Once the initial handshaking has
started, an

SSLEngine

can not switch between client and server
modes, even when performing renegotiations.

Applications might choose to process delegated tasks in different
threads. When an

SSLEngine

is created, the current

AccessControlContext

is saved. All future delegated tasks will be processed using this
context: that is, all access control decisions will be made using the
context captured at engine creation.

Concurrency Notes

:
There are two concurrency issues to be aware of:

- The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

A peer will signal its intent to close by sending its own closure
handshake message. After this message has been received and
processed by the local

SSLEngine

's

unwrap()

call, the application can detect the close by calling

unwrap()

and looking for a

SSLEngineResult

with status "CLOSED", or if

isInboundDone()

returns true.
If for some reason the peer closes the communication link without
sending the proper SSL/TLS/DTLS closure message, the application can
detect the end-of-stream and can signal the engine via

closeInbound()

that there will no more inbound messages to
process. Some applications might choose to require orderly shutdown
messages from a peer, in which case they can check that the closure
was generated by a handshake message and not by an end-of-stream
condition.

There are two groups of cipher suites which you will need to know
about when managing cipher suites:

- Supported

cipher suites: all the suites which are
supported by the SSL implementation. This list is reported
using

getSupportedCipherSuites()

.

Enabled

cipher suites, which may be fewer than
the full set of supported suites. This group is set using the

setEnabledCipherSuites(String [])

method, and
queried using the

getEnabledCipherSuites()

method.
Initially, a default set of cipher suites will be enabled on a
new engine that represents the minimum suggested
configuration.

Implementation defaults require that only cipher suites which
authenticate servers and provide confidentiality be enabled by
default. Only if both sides explicitly agree to unauthenticated
and/or non-private (unencrypted) communications will such a
cipher suite be selected.

Each SSL/TLS/DTLS connection must have one client and one server, thus
each endpoint must decide which role to assume. This choice determines
who begins the handshaking process as well as which type of messages
should be sent by each party. The method

setUseClientMode(boolean)

configures the mode. Note that the
default mode for a new

SSLEngine

is provider-specific.
Applications should set the mode explicitly before invoking other
methods of the

SSLEngine

. Once the initial handshaking has
started, an

SSLEngine

can not switch between client and server
modes, even when performing renegotiations.

Applications might choose to process delegated tasks in different
threads. When an

SSLEngine

is created, the current

AccessControlContext

is saved. All future delegated tasks will be processed using this
context: that is, all access control decisions will be made using the
context captured at engine creation.

Concurrency Notes

:
There are two concurrency issues to be aware of:

- The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

There are two groups of cipher suites which you will need to know
about when managing cipher suites:

- Supported

cipher suites: all the suites which are
supported by the SSL implementation. This list is reported
using

getSupportedCipherSuites()

.

Enabled

cipher suites, which may be fewer than
the full set of supported suites. This group is set using the

setEnabledCipherSuites(String [])

method, and
queried using the

getEnabledCipherSuites()

method.
Initially, a default set of cipher suites will be enabled on a
new engine that represents the minimum suggested
configuration.

Implementation defaults require that only cipher suites which
authenticate servers and provide confidentiality be enabled by
default. Only if both sides explicitly agree to unauthenticated
and/or non-private (unencrypted) communications will such a
cipher suite be selected.

Each SSL/TLS/DTLS connection must have one client and one server, thus
each endpoint must decide which role to assume. This choice determines
who begins the handshaking process as well as which type of messages
should be sent by each party. The method

setUseClientMode(boolean)

configures the mode. Note that the
default mode for a new

SSLEngine

is provider-specific.
Applications should set the mode explicitly before invoking other
methods of the

SSLEngine

. Once the initial handshaking has
started, an

SSLEngine

can not switch between client and server
modes, even when performing renegotiations.

Applications might choose to process delegated tasks in different
threads. When an

SSLEngine

is created, the current

AccessControlContext

is saved. All future delegated tasks will be processed using this
context: that is, all access control decisions will be made using the
context captured at engine creation.

Concurrency Notes

:
There are two concurrency issues to be aware of:

- The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

Supported

cipher suites: all the suites which are
supported by the SSL implementation. This list is reported
using

getSupportedCipherSuites()

.

Enabled

cipher suites, which may be fewer than
the full set of supported suites. This group is set using the

setEnabledCipherSuites(String [])

method, and
queried using the

getEnabledCipherSuites()

method.
Initially, a default set of cipher suites will be enabled on a
new engine that represents the minimum suggested
configuration.

Each SSL/TLS/DTLS connection must have one client and one server, thus
each endpoint must decide which role to assume. This choice determines
who begins the handshaking process as well as which type of messages
should be sent by each party. The method

setUseClientMode(boolean)

configures the mode. Note that the
default mode for a new

SSLEngine

is provider-specific.
Applications should set the mode explicitly before invoking other
methods of the

SSLEngine

. Once the initial handshaking has
started, an

SSLEngine

can not switch between client and server
modes, even when performing renegotiations.

Applications might choose to process delegated tasks in different
threads. When an

SSLEngine

is created, the current

AccessControlContext

is saved. All future delegated tasks will be processed using this
context: that is, all access control decisions will be made using the
context captured at engine creation.

Concurrency Notes

:
There are two concurrency issues to be aware of:

- The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

Applications might choose to process delegated tasks in different
threads. When an

SSLEngine

is created, the current

AccessControlContext

is saved. All future delegated tasks will be processed using this
context: that is, all access control decisions will be made using the
context captured at engine creation.

Concurrency Notes

:
There are two concurrency issues to be aware of:

- The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

The

wrap()

and

unwrap()

methods
may execute concurrently of each other.

The SSL/TLS/DTLS protocols employ ordered packets.
Applications must take care to ensure that generated packets
are delivered in sequence. If packets arrive
out-of-order, unexpected or fatal results may occur.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

For example:

```java
synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}
```

As a corollary, two threads must not attempt to call the same method
(either

wrap()

or

unwrap()

) concurrently,
because there is no way to guarantee the eventual packet ordering.

synchronized (outboundLock) {
sslEngine.wrap(src, dst);
outboundQueue.put(dst);
}

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

SSLEngine

()

Constructor for an

SSLEngine

providing no hints
for an internal session reuse strategy.

protected

SSLEngine

​(

String

peerHost,
int peerPort)

Constructor for an

SSLEngine

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract void

beginHandshake

()

Initiates handshaking (initial or renegotiation) on this SSLEngine.

abstract void

closeInbound

()

Signals that no more inbound network data will be sent
to this

SSLEngine

.

abstract void

closeOutbound

()

Signals that no more outbound application data will be sent
on this

SSLEngine

.

String

getApplicationProtocol

()

Returns the most recent application protocol value negotiated for this
connection.

abstract

Runnable

getDelegatedTask

()

Returns a delegated

Runnable

task for
this

SSLEngine

.

abstract

String

[]

getEnabledCipherSuites

()

Returns the names of the SSL cipher suites which are currently
enabled for use on this engine.

abstract

String

[]

getEnabledProtocols

()

Returns the names of the protocol versions which are currently
enabled for use with this

SSLEngine

.

abstract boolean

getEnableSessionCreation

()

Returns true if new SSL sessions may be established by this engine.

String

getHandshakeApplicationProtocol

()

Returns the application protocol value negotiated on a SSL/TLS
handshake currently in progress.

BiFunction

<

SSLEngine

,​

List

<

String

>,​

String

>

getHandshakeApplicationProtocolSelector

()

Retrieves the callback function that selects an application protocol
value during a SSL/TLS/DTLS handshake.

SSLSession

getHandshakeSession

()

Returns the

SSLSession

being constructed during a SSL/TLS/DTLS
handshake.

abstract

SSLEngineResult.HandshakeStatus

getHandshakeStatus

()

Returns the current handshake status for this

SSLEngine

.

abstract boolean

getNeedClientAuth

()

Returns true if the engine will

require

client authentication.

String

getPeerHost

()

Returns the host name of the peer.

int

getPeerPort

()

Returns the port number of the peer.

abstract

SSLSession

getSession

()

Returns the

SSLSession

in use in this

SSLEngine

.

SSLParameters

getSSLParameters

()

Returns the SSLParameters in effect for this SSLEngine.

abstract

String

[]

getSupportedCipherSuites

()

Returns the names of the cipher suites which could be enabled for use
on this engine.

abstract

String

[]

getSupportedProtocols

()

Returns the names of the protocols which could be enabled for use
with this

SSLEngine

.

abstract boolean

getUseClientMode

()

Returns true if the engine is set to use client mode when
handshaking.

abstract boolean

getWantClientAuth

()

Returns true if the engine will

request

client authentication.

abstract boolean

isInboundDone

()

Returns whether

unwrap(ByteBuffer, ByteBuffer)

will
accept any more inbound data messages.

abstract boolean

isOutboundDone

()

Returns whether

wrap(ByteBuffer, ByteBuffer)

will
produce any more outbound data messages.

abstract void

setEnabledCipherSuites

​(

String

[] suites)

Sets the cipher suites enabled for use on this engine.

abstract void

setEnabledProtocols

​(

String

[] protocols)

Set the protocol versions enabled for use on this engine.

abstract void

setEnableSessionCreation

​(boolean flag)

Controls whether new SSL sessions may be established by this engine.

void

setHandshakeApplicationProtocolSelector

​(

BiFunction

<

SSLEngine

,​

List

<

String

>,​

String

> selector)

Registers a callback function that selects an application protocol
value for a SSL/TLS/DTLS handshake.

abstract void

setNeedClientAuth

​(boolean need)

Configures the engine to

require

client authentication.

void

setSSLParameters

​(

SSLParameters

params)

Applies SSLParameters to this engine.

abstract void

setUseClientMode

​(boolean mode)

Configures the engine to use client (or server) mode when
handshaking.

abstract void

setWantClientAuth

​(boolean want)

Configures the engine to

request

client authentication.

SSLEngineResult

unwrap

​(

ByteBuffer

src,

ByteBuffer

dst)

Attempts to decode SSL/TLS/DTLS network data into a plaintext
application data buffer.

SSLEngineResult

unwrap

​(

ByteBuffer

src,

ByteBuffer

[] dsts)

Attempts to decode SSL/TLS/DTLS network data into a sequence of plaintext
application data buffers.

abstract

SSLEngineResult

unwrap

​(

ByteBuffer

src,

ByteBuffer

[] dsts,
int offset,
int length)

Attempts to decode SSL/TLS/DTLS network data into a subsequence of
plaintext application data buffers.

abstract

SSLEngineResult

wrap

​(

ByteBuffer

[] srcs,
int offset,
int length,

ByteBuffer

dst)

Attempts to encode plaintext bytes from a subsequence of data
buffers into SSL/TLS/DTLS network data.

SSLEngineResult

wrap

​(

ByteBuffer

[] srcs,

ByteBuffer

dst)

Attempts to encode plaintext bytes from a sequence of data
buffers into SSL/TLS/DTLS network data.

SSLEngineResult

wrap

​(

ByteBuffer

src,

ByteBuffer

dst)

Attempts to encode a buffer of plaintext application data into
SSL/TLS/DTLS network data.

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

SSLEngine

()

Constructor for an

SSLEngine

providing no hints
for an internal session reuse strategy.

protected

SSLEngine

​(

String

peerHost,
int peerPort)

Constructor for an

SSLEngine

.

---

#### Constructor Summary

Constructor for an

SSLEngine

providing no hints
for an internal session reuse strategy.

Constructor for an

SSLEngine

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract void

beginHandshake

()

Initiates handshaking (initial or renegotiation) on this SSLEngine.

abstract void

closeInbound

()

Signals that no more inbound network data will be sent
to this

SSLEngine

.

abstract void

closeOutbound

()

Signals that no more outbound application data will be sent
on this

SSLEngine

.

String

getApplicationProtocol

()

Returns the most recent application protocol value negotiated for this
connection.

abstract

Runnable

getDelegatedTask

()

Returns a delegated

Runnable

task for
this

SSLEngine

.

abstract

String

[]

getEnabledCipherSuites

()

Returns the names of the SSL cipher suites which are currently
enabled for use on this engine.

abstract

String

[]

getEnabledProtocols

()

Returns the names of the protocol versions which are currently
enabled for use with this

SSLEngine

.

abstract boolean

getEnableSessionCreation

()

Returns true if new SSL sessions may be established by this engine.

String

getHandshakeApplicationProtocol

()

Returns the application protocol value negotiated on a SSL/TLS
handshake currently in progress.

BiFunction

<

SSLEngine

,​

List

<

String

>,​

String

>

getHandshakeApplicationProtocolSelector

()

Retrieves the callback function that selects an application protocol
value during a SSL/TLS/DTLS handshake.

SSLSession

getHandshakeSession

()

Returns the

SSLSession

being constructed during a SSL/TLS/DTLS
handshake.

abstract

SSLEngineResult.HandshakeStatus

getHandshakeStatus

()

Returns the current handshake status for this

SSLEngine

.

abstract boolean

getNeedClientAuth

()

Returns true if the engine will

require

client authentication.

String

getPeerHost

()

Returns the host name of the peer.

int

getPeerPort

()

Returns the port number of the peer.

abstract

SSLSession

getSession

()

Returns the

SSLSession

in use in this

SSLEngine

.

SSLParameters

getSSLParameters

()

Returns the SSLParameters in effect for this SSLEngine.

abstract

String

[]

getSupportedCipherSuites

()

Returns the names of the cipher suites which could be enabled for use
on this engine.

abstract

String

[]

getSupportedProtocols

()

Returns the names of the protocols which could be enabled for use
with this

SSLEngine

.

abstract boolean

getUseClientMode

()

Returns true if the engine is set to use client mode when
handshaking.

abstract boolean

getWantClientAuth

()

Returns true if the engine will

request

client authentication.

abstract boolean

isInboundDone

()

Returns whether

unwrap(ByteBuffer, ByteBuffer)

will
accept any more inbound data messages.

abstract boolean

isOutboundDone

()

Returns whether

wrap(ByteBuffer, ByteBuffer)

will
produce any more outbound data messages.

abstract void

setEnabledCipherSuites

​(

String

[] suites)

Sets the cipher suites enabled for use on this engine.

abstract void

setEnabledProtocols

​(

String

[] protocols)

Set the protocol versions enabled for use on this engine.

abstract void

setEnableSessionCreation

​(boolean flag)

Controls whether new SSL sessions may be established by this engine.

void

setHandshakeApplicationProtocolSelector

​(

BiFunction

<

SSLEngine

,​

List

<

String

>,​

String

> selector)

Registers a callback function that selects an application protocol
value for a SSL/TLS/DTLS handshake.

abstract void

setNeedClientAuth

​(boolean need)

Configures the engine to

require

client authentication.

void

setSSLParameters

​(

SSLParameters

params)

Applies SSLParameters to this engine.

abstract void

setUseClientMode

​(boolean mode)

Configures the engine to use client (or server) mode when
handshaking.

abstract void

setWantClientAuth

​(boolean want)

Configures the engine to

request

client authentication.

SSLEngineResult

unwrap

​(

ByteBuffer

src,

ByteBuffer

dst)

Attempts to decode SSL/TLS/DTLS network data into a plaintext
application data buffer.

SSLEngineResult

unwrap

​(

ByteBuffer

src,

ByteBuffer

[] dsts)

Attempts to decode SSL/TLS/DTLS network data into a sequence of plaintext
application data buffers.

abstract

SSLEngineResult

unwrap

​(

ByteBuffer

src,

ByteBuffer

[] dsts,
int offset,
int length)

Attempts to decode SSL/TLS/DTLS network data into a subsequence of
plaintext application data buffers.

abstract

SSLEngineResult

wrap

​(

ByteBuffer

[] srcs,
int offset,
int length,

ByteBuffer

dst)

Attempts to encode plaintext bytes from a subsequence of data
buffers into SSL/TLS/DTLS network data.

SSLEngineResult

wrap

​(

ByteBuffer

[] srcs,

ByteBuffer

dst)

Attempts to encode plaintext bytes from a sequence of data
buffers into SSL/TLS/DTLS network data.

SSLEngineResult

wrap

​(

ByteBuffer

src,

ByteBuffer

dst)

Attempts to encode a buffer of plaintext application data into
SSL/TLS/DTLS network data.

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

Initiates handshaking (initial or renegotiation) on this SSLEngine.

Signals that no more inbound network data will be sent
to this

SSLEngine

.

Signals that no more outbound application data will be sent
on this

SSLEngine

.

Returns the most recent application protocol value negotiated for this
connection.

Returns a delegated

Runnable

task for
this

SSLEngine

.

Returns the names of the SSL cipher suites which are currently
enabled for use on this engine.

Returns the names of the protocol versions which are currently
enabled for use with this

SSLEngine

.

Returns true if new SSL sessions may be established by this engine.

Returns the application protocol value negotiated on a SSL/TLS
handshake currently in progress.

Retrieves the callback function that selects an application protocol
value during a SSL/TLS/DTLS handshake.

Returns the

SSLSession

being constructed during a SSL/TLS/DTLS
handshake.

Returns the current handshake status for this

SSLEngine

.

Returns true if the engine will

require

client authentication.

Returns the host name of the peer.

Returns the port number of the peer.

Returns the

SSLSession

in use in this

SSLEngine

.

Returns the SSLParameters in effect for this SSLEngine.

Returns the names of the cipher suites which could be enabled for use
on this engine.

Returns the names of the protocols which could be enabled for use
with this

SSLEngine

.

Returns true if the engine is set to use client mode when
handshaking.

Returns true if the engine will

request

client authentication.

Returns whether

unwrap(ByteBuffer, ByteBuffer)

will
accept any more inbound data messages.

Returns whether

wrap(ByteBuffer, ByteBuffer)

will
produce any more outbound data messages.

Sets the cipher suites enabled for use on this engine.

Set the protocol versions enabled for use on this engine.

Controls whether new SSL sessions may be established by this engine.

Registers a callback function that selects an application protocol
value for a SSL/TLS/DTLS handshake.

Configures the engine to

require

client authentication.

Applies SSLParameters to this engine.

Configures the engine to use client (or server) mode when
handshaking.

Configures the engine to

request

client authentication.

Attempts to decode SSL/TLS/DTLS network data into a plaintext
application data buffer.

Attempts to decode SSL/TLS/DTLS network data into a sequence of plaintext
application data buffers.

Attempts to decode SSL/TLS/DTLS network data into a subsequence of
plaintext application data buffers.

Attempts to encode plaintext bytes from a subsequence of data
buffers into SSL/TLS/DTLS network data.

Attempts to encode plaintext bytes from a sequence of data
buffers into SSL/TLS/DTLS network data.

Attempts to encode a buffer of plaintext application data into
SSL/TLS/DTLS network data.

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

- SSLEngine

```java
protected SSLEngine()
```

Constructor for an

SSLEngine

providing no hints
for an internal session reuse strategy.

**See Also:** SSLContext.createSSLEngine()

,

SSLSessionContext

- SSLEngine

```java
protected SSLEngine​(
String
peerHost,
int peerPort)
```

Constructor for an

SSLEngine

.

SSLEngine

implementations may use the

peerHost

and

peerPort

parameters as hints
for their internal session reuse strategy.

Some cipher suites (such as Kerberos) require remote hostname
information. Implementations of this class should use this
constructor to use Kerberos.

The parameters are not authenticated by the

SSLEngine

.

**Parameters:** peerHost

- the name of the peer host
**Parameters:** peerPort

- the port number of the peer
**See Also:** SSLContext.createSSLEngine(String, int)

,

SSLSessionContext

============ METHOD DETAIL ==========

- Method Detail

- getPeerHost

```java
public
String
getPeerHost()
```

Returns the host name of the peer.

Note that the value is not authenticated, and should not be
relied upon.

**Returns:** the host name of the peer, or null if nothing is
available.

- getPeerPort

```java
public int getPeerPort()
```

Returns the port number of the peer.

Note that the value is not authenticated, and should not be
relied upon.

**Returns:** the port number of the peer, or -1 if nothing is
available.

- wrap

```java
public
SSLEngineResult
wrap​(
ByteBuffer
src,

ByteBuffer
dst)
throws
SSLException
```

Attempts to encode a buffer of plaintext application data into
SSL/TLS/DTLS network data.

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.wrap(new ByteBuffer [] { src }, 0, 1, dst);
```

**Parameters:** src

- a

ByteBuffer

containing outbound application data
**Parameters:** dst

- a

ByteBuffer

to hold outbound network data
**Returns:** an

SSLEngineResult

describing the result
of this operation.
**Throws:** SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
**Throws:** ReadOnlyBufferException

- if the

dst

buffer is read-only.
**Throws:** IllegalArgumentException

- if either

src

or

dst

is null.
**Throws:** IllegalStateException

- if the client/server mode
has not yet been set.
**See Also:** wrap(ByteBuffer [], int, int, ByteBuffer)

- wrap

```java
public
SSLEngineResult
wrap​(
ByteBuffer
[] srcs,

ByteBuffer
dst)
throws
SSLException
```

Attempts to encode plaintext bytes from a sequence of data
buffers into SSL/TLS/DTLS network data.

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.wrap(srcs, 0, srcs.length, dst);
```

**Parameters:** srcs

- an array of

ByteBuffers

containing the
outbound application data
**Parameters:** dst

- a

ByteBuffer

to hold outbound network data
**Returns:** an

SSLEngineResult

describing the result
of this operation.
**Throws:** SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
**Throws:** ReadOnlyBufferException

- if the

dst

buffer is read-only.
**Throws:** IllegalArgumentException

- if either

srcs

or

dst

is null, or if any element in

srcs

is null.
**Throws:** IllegalStateException

- if the client/server mode
has not yet been set.
**See Also:** wrap(ByteBuffer [], int, int, ByteBuffer)

- wrap

```java
public abstract
SSLEngineResult
wrap​(
ByteBuffer
[] srcs,
int offset,
int length,

ByteBuffer
dst)
throws
SSLException
```

Attempts to encode plaintext bytes from a subsequence of data
buffers into SSL/TLS/DTLS network data. This

"gathering"

operation encodes, in a single invocation, a sequence of bytes
from one or more of a given sequence of buffers. Gathering
wraps are often useful when implementing network protocols or
file formats that, for example, group data into segments
consisting of one or more fixed-length headers followed by a
variable-length body. See

GatheringByteChannel

for more
information on gathering, and

GatheringByteChannel.write(ByteBuffer[],
int, int)

for more information on the subsequence
behavior.

Depending on the state of the SSLEngine, this method may produce
network data without consuming any application data (for example,
it may generate handshake data.)

The application is responsible for reliably transporting the
network data to the peer, and for ensuring that data created by
multiple calls to wrap() is transported in the same order in which
it was generated. The application must properly synchronize
multiple calls to this method.

If this

SSLEngine

has not yet started its initial
handshake, this method will automatically start the handshake.

This method will attempt to produce SSL/TLS/DTLS records, and will
consume as much source data as possible, but will never consume
more than the sum of the bytes remaining in each buffer. Each

ByteBuffer

's position is updated to reflect the
amount of data consumed or produced. The limits remain the
same.

The underlying memory used by the

srcs

and

dst ByteBuffer

s must not be the same.

See the class description for more information on engine closure.

**Parameters:** srcs

- an array of

ByteBuffers

containing the
outbound application data
**Parameters:** offset

- The offset within the buffer array of the first buffer from
which bytes are to be retrieved; it must be non-negative
and no larger than

srcs.length
**Parameters:** length

- The maximum number of buffers to be accessed; it must be
non-negative and no larger than

srcs.length

-

offset
**Parameters:** dst

- a

ByteBuffer

to hold outbound network data
**Returns:** an

SSLEngineResult

describing the result
of this operation.
**Throws:** SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
**Throws:** IndexOutOfBoundsException

- if the preconditions on the

offset

and

length

parameters do not hold.
**Throws:** ReadOnlyBufferException

- if the

dst

buffer is read-only.
**Throws:** IllegalArgumentException

- if either

srcs

or

dst

is null, or if any element in the

srcs

subsequence specified is null.
**Throws:** IllegalStateException

- if the client/server mode
has not yet been set.
**See Also:** GatheringByteChannel

,

GatheringByteChannel.write(
ByteBuffer[], int, int)

- unwrap

```java
public
SSLEngineResult
unwrap​(
ByteBuffer
src,

ByteBuffer
dst)
throws
SSLException
```

Attempts to decode SSL/TLS/DTLS network data into a plaintext
application data buffer.

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.unwrap(src, new ByteBuffer [] { dst }, 0, 1);
```

**Parameters:** src

- a

ByteBuffer

containing inbound network data.
**Parameters:** dst

- a

ByteBuffer

to hold inbound application data.
**Returns:** an

SSLEngineResult

describing the result
of this operation.
**Throws:** SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
**Throws:** ReadOnlyBufferException

- if the

dst

buffer is read-only.
**Throws:** IllegalArgumentException

- if either

src

or

dst

is null.
**Throws:** IllegalStateException

- if the client/server mode
has not yet been set.
**See Also:** unwrap(ByteBuffer, ByteBuffer [], int, int)

- unwrap

```java
public
SSLEngineResult
unwrap​(
ByteBuffer
src,

ByteBuffer
[] dsts)
throws
SSLException
```

Attempts to decode SSL/TLS/DTLS network data into a sequence of plaintext
application data buffers.

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.unwrap(src, dsts, 0, dsts.length);
```

**Parameters:** src

- a

ByteBuffer

containing inbound network data.
**Parameters:** dsts

- an array of

ByteBuffer

s to hold inbound
application data.
**Returns:** an

SSLEngineResult

describing the result
of this operation.
**Throws:** SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
**Throws:** ReadOnlyBufferException

- if any of the

dst

buffers are read-only.
**Throws:** IllegalArgumentException

- if either

src

or

dsts

is null, or if any element in

dsts

is null.
**Throws:** IllegalStateException

- if the client/server mode
has not yet been set.
**See Also:** unwrap(ByteBuffer, ByteBuffer [], int, int)

- unwrap

```java
public abstract
SSLEngineResult
unwrap​(
ByteBuffer
src,

ByteBuffer
[] dsts,
int offset,
int length)
throws
SSLException
```

Attempts to decode SSL/TLS/DTLS network data into a subsequence of
plaintext application data buffers. This

"scattering"

operation decodes, in a single invocation, a sequence of bytes
into one or more of a given sequence of buffers. Scattering
unwraps are often useful when implementing network protocols or
file formats that, for example, group data into segments
consisting of one or more fixed-length headers followed by a
variable-length body. See

ScatteringByteChannel

for more
information on scattering, and

ScatteringByteChannel.read(ByteBuffer[],
int, int)

for more information on the subsequence
behavior.

Depending on the state of the SSLEngine, this method may consume
network data without producing any application data (for example,
it may consume handshake data.)

The application is responsible for reliably obtaining the network
data from the peer, and for invoking unwrap() on the data in the
order it was received. The application must properly synchronize
multiple calls to this method.

If this

SSLEngine

has not yet started its initial
handshake, this method will automatically start the handshake.

This method will attempt to consume one complete SSL/TLS/DTLS network
packet, but will never consume more than the sum of the bytes
remaining in the buffers. Each

ByteBuffer

's
position is updated to reflect the amount of data consumed or
produced. The limits remain the same.

The underlying memory used by the

src

and

dsts ByteBuffer

s must not be the same.

The inbound network buffer may be modified as a result of this
call: therefore if the network data packet is required for some
secondary purpose, the data should be duplicated before calling this
method. Note: the network data will not be useful to a second
SSLEngine, as each SSLEngine contains unique random state which
influences the SSL/TLS/DTLS messages.

See the class description for more information on engine closure.

**Parameters:** src

- a

ByteBuffer

containing inbound network data.
**Parameters:** dsts

- an array of

ByteBuffer

s to hold inbound
application data.
**Parameters:** offset

- The offset within the buffer array of the first buffer from
which bytes are to be transferred; it must be non-negative
and no larger than

dsts.length

.
**Parameters:** length

- The maximum number of buffers to be accessed; it must be
non-negative and no larger than

dsts.length

-

offset

.
**Returns:** an

SSLEngineResult

describing the result
of this operation.
**Throws:** SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold.
**Throws:** ReadOnlyBufferException

- if any of the

dst

buffers are read-only.
**Throws:** IllegalArgumentException

- if either

src

or

dsts

is null, or if any element in the

dsts

subsequence specified is null.
**Throws:** IllegalStateException

- if the client/server mode
has not yet been set.
**See Also:** ScatteringByteChannel

,

ScatteringByteChannel.read(
ByteBuffer[], int, int)

- getDelegatedTask

```java
public abstract
Runnable
getDelegatedTask()
```

Returns a delegated

Runnable

task for
this

SSLEngine

.

SSLEngine

operations may require the results of
operations that block, or may take an extended period of time to
complete. This method is used to obtain an outstanding

Runnable

operation (task). Each task must be assigned
a thread (possibly the current) to perform the

run

operation. Once the

run

method returns, the

Runnable

object
is no longer needed and may be discarded.

Delegated tasks run in the

AccessControlContext

in place when this object was created.

A call to this method will return each outstanding task
exactly once.

Multiple delegated tasks can be run in parallel.

**Returns:** a delegated

Runnable

task, or null
if none are available.

- closeInbound

```java
public abstract void closeInbound()
throws
SSLException
```

Signals that no more inbound network data will be sent
to this

SSLEngine

.

If the application initiated the closing process by calling

closeOutbound()

, under some circumstances it is not
required that the initiator wait for the peer's corresponding
close message. (See section 7.2.1 of the TLS specification (

RFC 2246

) for more
information on waiting for closure alerts.) In such cases, this
method need not be called.

But if the application did not initiate the closure process, or
if the circumstances above do not apply, this method should be
called whenever the end of the SSL/TLS/DTLS data stream is reached.
This ensures closure of the inbound side, and checks that the
peer followed the SSL/TLS/DTLS close procedure properly, thus
detecting possible truncation attacks.

This method is idempotent: if the inbound side has already
been closed, this method does not do anything.

wrap()

should be
called to flush any remaining handshake data.

**Throws:** SSLException

- if this engine has not received the proper SSL/TLS/DTLS close
notification message from the peer.
**See Also:** isInboundDone()

,

isOutboundDone()

- isInboundDone

```java
public abstract boolean isInboundDone()
```

Returns whether

unwrap(ByteBuffer, ByteBuffer)

will
accept any more inbound data messages.

**Returns:** true if the

SSLEngine

will not
consume anymore network data (and by implication,
will not produce any more application data.)
**See Also:** closeInbound()

- closeOutbound

```java
public abstract void closeOutbound()
```

Signals that no more outbound application data will be sent
on this

SSLEngine

.

This method is idempotent: if the outbound side has already
been closed, this method does not do anything.

wrap(ByteBuffer, ByteBuffer)

should be
called to flush any remaining handshake data.

**See Also:** isOutboundDone()

- isOutboundDone

```java
public abstract boolean isOutboundDone()
```

Returns whether

wrap(ByteBuffer, ByteBuffer)

will
produce any more outbound data messages.

Note that during the closure phase, a

SSLEngine

may
generate handshake closure data that must be sent to the peer.

wrap()

must be called to generate this data. When
this method returns true, no more outbound data will be created.

**Returns:** true if the

SSLEngine

will not produce
any more network data
**See Also:** closeOutbound()

,

closeInbound()

- getSupportedCipherSuites

```java
public abstract
String
[] getSupportedCipherSuites()
```

Returns the names of the cipher suites which could be enabled for use
on this engine. Normally, only a subset of these will actually
be enabled by default, since this list may include cipher suites which
do not meet quality of service requirements for those defaults. Such
cipher suites might be useful in specialized applications.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:** an array of cipher suite names
**See Also:** getEnabledCipherSuites()

,

setEnabledCipherSuites(String [])

- getEnabledCipherSuites

```java
public abstract
String
[] getEnabledCipherSuites()
```

Returns the names of the SSL cipher suites which are currently
enabled for use on this engine. When an SSLEngine is first
created, all enabled cipher suites support a minimum quality of
service. Thus, in some environments this value might be empty.

Note that even if a suite is enabled, it may never be used. This
can occur if the peer does not support it, or its use is restricted,
or the requisite certificates (and private keys) for the suite are
not available, or an anonymous suite is enabled but authentication
is required.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:** an array of cipher suite names
**See Also:** getSupportedCipherSuites()

,

setEnabledCipherSuites(String [])

- setEnabledCipherSuites

```java
public abstract void setEnabledCipherSuites​(
String
[] suites)
```

Sets the cipher suites enabled for use on this engine.

Each cipher suite in the

suites

parameter must have
been listed by getSupportedCipherSuites(), or the method will
fail. Following a successful call to this method, only suites
listed in the

suites

parameter are enabled for use.

Note that the standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list or might not
use the recommended name for a certain cipher suite.

See

getEnabledCipherSuites()

for more information
on why a specific cipher suite may never be used on a engine.

**Parameters:** suites

- Names of all the cipher suites to enable
**Throws:** IllegalArgumentException

- when one or more of the ciphers
named by the parameter is not supported, or when the
parameter is null.
**See Also:** getSupportedCipherSuites()

,

getEnabledCipherSuites()

- getSupportedProtocols

```java
public abstract
String
[] getSupportedProtocols()
```

Returns the names of the protocols which could be enabled for use
with this

SSLEngine

.

**Returns:** an array of protocols supported

- getEnabledProtocols

```java
public abstract
String
[] getEnabledProtocols()
```

Returns the names of the protocol versions which are currently
enabled for use with this

SSLEngine

.

Note that even if a protocol is enabled, it may never be used.
This can occur if the peer does not support the protocol, or its
use is restricted, or there are no enabled cipher suites supported
by the protocol.

**Returns:** an array of protocols
**See Also:** setEnabledProtocols(String [])

- setEnabledProtocols

```java
public abstract void setEnabledProtocols​(
String
[] protocols)
```

Set the protocol versions enabled for use on this engine.

The protocols must have been listed by getSupportedProtocols()
as being supported. Following a successful call to this method,
only protocols listed in the

protocols

parameter
are enabled for use.

**Parameters:** protocols

- Names of all the protocols to enable.
**Throws:** IllegalArgumentException

- when one or more of
the protocols named by the parameter is not supported or
when the protocols parameter is null.
**See Also:** getEnabledProtocols()

- getSession

```java
public abstract
SSLSession
getSession()
```

Returns the

SSLSession

in use in this

SSLEngine

.

These can be long lived, and frequently correspond to an entire
login session for some user. The session specifies a particular
cipher suite which is being actively used by all connections in
that session, as well as the identities of the session's client
and server.

Unlike

SSLSocket.getSession()

this method does not block until handshaking is complete.

Until the initial handshake has completed, this method returns
a session object which reports an invalid cipher suite of
"SSL_NULL_WITH_NULL_NULL".

**Returns:** the

SSLSession

for this

SSLEngine
**See Also:** SSLSession

- getHandshakeSession

```java
public
SSLSession
getHandshakeSession()
```

Returns the

SSLSession

being constructed during a SSL/TLS/DTLS
handshake.

TLS/DTLS protocols may negotiate parameters that are needed when using
an instance of this class, but before the

SSLSession

has
been completely initialized and made available via

getSession

.
For example, the list of valid signature algorithms may restrict
the type of certificates that can be used during TrustManager
decisions, or the maximum TLS/DTLS fragment packet sizes can be
resized to better support the network environment.

This method provides early access to the

SSLSession

being
constructed. Depending on how far the handshake has progressed,
some data may not yet be available for use. For example, if a
remote server will be sending a Certificate chain, but that chain
has yet not been processed, the

getPeerCertificates

method of

SSLSession

will throw a
SSLPeerUnverifiedException. Once that chain has been processed,

getPeerCertificates

will return the proper value.

**Returns:** null if this instance is not currently handshaking, or
if the current handshake has not progressed far enough to
create a basic SSLSession. Otherwise, this method returns the

SSLSession

currently being negotiated.
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation.
**Since:** 1.7
**See Also:** SSLSocket

,

SSLSession

,

ExtendedSSLSession

,

X509ExtendedKeyManager

,

X509ExtendedTrustManager

- beginHandshake

```java
public abstract void beginHandshake()
throws
SSLException
```

Initiates handshaking (initial or renegotiation) on this SSLEngine.

This method is not needed for the initial handshake, as the

wrap()

and

unwrap()

methods will
implicitly call this method if handshaking has not already begun.

Note that the peer may also request a session renegotiation with
this

SSLEngine

by sending the appropriate
session renegotiate handshake message.

Unlike the

SSLSocket#startHandshake()

method, this method does not block
until handshaking is completed.

To force a complete SSL/TLS/DTLS session renegotiation, the current
session should be invalidated prior to calling this method.

Some protocols may not support multiple handshakes on an existing
engine and may throw an

SSLException

.

**Throws:** SSLException

- if a problem was encountered while signaling the

SSLEngine

to begin a new handshake.
See the class description for more information on
engine closure.
**Throws:** IllegalStateException

- if the client/server mode
has not yet been set.
**See Also:** SSLSession.invalidate()

- getHandshakeStatus

```java
public abstract
SSLEngineResult.HandshakeStatus
getHandshakeStatus()
```

Returns the current handshake status for this

SSLEngine

.

**Returns:** the current

SSLEngineResult.HandshakeStatus

.

- setUseClientMode

```java
public abstract void setUseClientMode​(boolean mode)
```

Configures the engine to use client (or server) mode when
handshaking.

This method must be called before any handshaking occurs.
Once handshaking has begun, the mode can not be reset for the
life of this engine.

Servers normally authenticate themselves, and clients
are not required to do so.

**Implementation Note:** The JDK SunJSSE provider implementation default for this mode is false.
**Parameters:** mode

- true if the engine should start its handshaking
in "client" mode
**Throws:** IllegalArgumentException

- if a mode change is attempted
after the initial handshake has begun.
**See Also:** getUseClientMode()

- getUseClientMode

```java
public abstract boolean getUseClientMode()
```

Returns true if the engine is set to use client mode when
handshaking.

**Implementation Note:** The JDK SunJSSE provider implementation returns false unless

setUseClientMode(boolean)

is used to change the mode to true.
**Returns:** true if the engine should do handshaking
in "client" mode
**See Also:** setUseClientMode(boolean)

- setNeedClientAuth

```java
public abstract void setNeedClientAuth​(boolean need)
```

Configures the engine to

require

client authentication. This
option is only useful for engines in the server mode.

An engine's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setWantClientAuth(boolean)

, if this option is set and
the client chooses not to provide authentication information
about itself,

the negotiations will stop and the engine will
begin its closure procedure

.

Calling this method overrides any previous setting made by
this method or

setWantClientAuth(boolean)

.

**Parameters:** need

- set to true if client authentication is required,
or false if no client authentication is desired.
**See Also:** getNeedClientAuth()

,

setWantClientAuth(boolean)

,

getWantClientAuth()

,

setUseClientMode(boolean)

- getNeedClientAuth

```java
public abstract boolean getNeedClientAuth()
```

Returns true if the engine will

require

client authentication.
This option is only useful to engines in the server mode.

**Returns:** true if client authentication is required,
or false if no client authentication is desired.
**See Also:** setNeedClientAuth(boolean)

,

setWantClientAuth(boolean)

,

getWantClientAuth()

,

setUseClientMode(boolean)

- setWantClientAuth

```java
public abstract void setWantClientAuth​(boolean want)
```

Configures the engine to

request

client authentication.
This option is only useful for engines in the server mode.

An engine's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setNeedClientAuth(boolean)

, if this option is set and
the client chooses not to provide authentication information
about itself,

the negotiations will continue

.

Calling this method overrides any previous setting made by
this method or

setNeedClientAuth(boolean)

.

**Parameters:** want

- set to true if client authentication is requested,
or false if no client authentication is desired.
**See Also:** getWantClientAuth()

,

setNeedClientAuth(boolean)

,

getNeedClientAuth()

,

setUseClientMode(boolean)

- getWantClientAuth

```java
public abstract boolean getWantClientAuth()
```

Returns true if the engine will

request

client authentication.
This option is only useful for engines in the server mode.

**Returns:** true if client authentication is requested,
or false if no client authentication is desired.
**See Also:** setNeedClientAuth(boolean)

,

getNeedClientAuth()

,

setWantClientAuth(boolean)

,

setUseClientMode(boolean)

- setEnableSessionCreation

```java
public abstract void setEnableSessionCreation​(boolean flag)
```

Controls whether new SSL sessions may be established by this engine.
If session creations are not allowed, and there are no
existing sessions to resume, there will be no successful
handshaking.

**Parameters:** flag

- true indicates that sessions may be created; this
is the default. false indicates that an existing session
must be resumed
**See Also:** getEnableSessionCreation()

- getEnableSessionCreation

```java
public abstract boolean getEnableSessionCreation()
```

Returns true if new SSL sessions may be established by this engine.

**Returns:** true indicates that sessions may be created; this
is the default. false indicates that an existing session
must be resumed
**See Also:** setEnableSessionCreation(boolean)

- getSSLParameters

```java
public
SSLParameters
getSSLParameters()
```

Returns the SSLParameters in effect for this SSLEngine.
The ciphersuites and protocols of the returned SSLParameters
are always non-null.

**Returns:** the SSLParameters in effect for this SSLEngine.
**Since:** 1.6

- setSSLParameters

```java
public void setSSLParameters​(
SSLParameters
params)
```

Applies SSLParameters to this engine.

This means:

- If

params.getCipherSuites()

is non-null,

setEnabledCipherSuites()

is called with that value.
- If

params.getProtocols()

is non-null,

setEnabledProtocols()

is called with that value.
- If

params.getNeedClientAuth()

or

params.getWantClientAuth()

return

true

,

setNeedClientAuth(true)

and

setWantClientAuth(true)

are called, respectively;
otherwise

setWantClientAuth(false)

is called.
- If

params.getServerNames()

is non-null, the engine will
configure its server names with that value.
- If

params.getSNIMatchers()

is non-null, the engine will
configure its SNI matchers with that value.

**Parameters:** params

- the parameters
**Throws:** IllegalArgumentException

- if the setEnabledCipherSuites() or
the setEnabledProtocols() call fails
**Since:** 1.6

- getApplicationProtocol

```java
public
String
getApplicationProtocol()
```

Returns the most recent application protocol value negotiated for this
connection.

If supported by the underlying SSL/TLS/DTLS implementation,
application name negotiation mechanisms such as

RFC 7301

, the
Application-Layer Protocol Negotiation (ALPN), can negotiate
application-level values between peers.

**Implementation Requirements:** The implementation in this class throws

UnsupportedOperationException

and performs no other action.
**Returns:** null if it has not yet been determined if application
protocols might be used for this connection, an empty

String

if application protocols values will not
be used, or a non-empty application protocol

String

if a value was successfully negotiated.
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation.
**Since:** 9

- getHandshakeApplicationProtocol

```java
public
String
getHandshakeApplicationProtocol()
```

Returns the application protocol value negotiated on a SSL/TLS
handshake currently in progress.

Like

getHandshakeSession()

,
a connection may be in the middle of a handshake. The
application protocol may or may not yet be available.

**Implementation Requirements:** The implementation in this class throws

UnsupportedOperationException

and performs no other action.
**Returns:** null if it has not yet been determined if application
protocols might be used for this handshake, an empty

String

if application protocols values will not
be used, or a non-empty application protocol

String

if a value was successfully negotiated.
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation.
**Since:** 9

- setHandshakeApplicationProtocolSelector

```java
public void setHandshakeApplicationProtocolSelector​(
BiFunction
<
SSLEngine
,​
List
<
String
>,​
String
> selector)
```

Registers a callback function that selects an application protocol
value for a SSL/TLS/DTLS handshake.
The function overrides any values supplied using

SSLParameters.setApplicationProtocols

and it supports the following
type parameters:

For example, the following call registers a callback function that
examines the TLS handshake parameters and selects an application protocol
name:

```java
serverEngine.setHandshakeApplicationProtocolSelector(
(serverEngine, clientProtocols) -> {
SSLSession session = serverEngine.getHandshakeSession();
return chooseApplicationProtocol(
serverEngine,
clientProtocols,
session.getProtocol(),
session.getCipherSuite());
});
```

**API Note:** This method should be called by TLS server applications before the TLS
handshake begins. Also, this

SSLEngine

should be configured with
parameters that are compatible with the application protocol selected by
the callback function. For example, enabling a poor choice of cipher
suites could result in no suitable application protocol.
See

SSLParameters

.
**Implementation Requirements:** The implementation in this class throws

UnsupportedOperationException

and performs no other action.
**Parameters:** selector

- the callback function, or null to disable the callback
functionality.
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation.
**Since:** 9

- getHandshakeApplicationProtocolSelector

```java
public
BiFunction
<
SSLEngine
,​
List
<
String
>,​
String
> getHandshakeApplicationProtocolSelector()
```

Retrieves the callback function that selects an application protocol
value during a SSL/TLS/DTLS handshake.
See

setHandshakeApplicationProtocolSelector

for the function's type parameters.

**Implementation Requirements:** The implementation in this class throws

UnsupportedOperationException

and performs no other action.
**Returns:** the callback function, or null if none has been set.
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation.
**Since:** 9

Constructor Detail

- SSLEngine

```java
protected SSLEngine()
```

Constructor for an

SSLEngine

providing no hints
for an internal session reuse strategy.

**See Also:** SSLContext.createSSLEngine()

,

SSLSessionContext

- SSLEngine

```java
protected SSLEngine​(
String
peerHost,
int peerPort)
```

Constructor for an

SSLEngine

.

SSLEngine

implementations may use the

peerHost

and

peerPort

parameters as hints
for their internal session reuse strategy.

Some cipher suites (such as Kerberos) require remote hostname
information. Implementations of this class should use this
constructor to use Kerberos.

The parameters are not authenticated by the

SSLEngine

.

**Parameters:** peerHost

- the name of the peer host
**Parameters:** peerPort

- the port number of the peer
**See Also:** SSLContext.createSSLEngine(String, int)

,

SSLSessionContext

---

#### Constructor Detail

SSLEngine

```java
protected SSLEngine()
```

Constructor for an

SSLEngine

providing no hints
for an internal session reuse strategy.

**See Also:** SSLContext.createSSLEngine()

,

SSLSessionContext

---

#### SSLEngine

protected SSLEngine()

Constructor for an

SSLEngine

providing no hints
for an internal session reuse strategy.

SSLEngine

```java
protected SSLEngine​(
String
peerHost,
int peerPort)
```

Constructor for an

SSLEngine

.

SSLEngine

implementations may use the

peerHost

and

peerPort

parameters as hints
for their internal session reuse strategy.

Some cipher suites (such as Kerberos) require remote hostname
information. Implementations of this class should use this
constructor to use Kerberos.

The parameters are not authenticated by the

SSLEngine

.

**Parameters:** peerHost

- the name of the peer host
**Parameters:** peerPort

- the port number of the peer
**See Also:** SSLContext.createSSLEngine(String, int)

,

SSLSessionContext

---

#### SSLEngine

protected SSLEngine​(

String

peerHost,
int peerPort)

Constructor for an

SSLEngine

.

SSLEngine

implementations may use the

peerHost

and

peerPort

parameters as hints
for their internal session reuse strategy.

Some cipher suites (such as Kerberos) require remote hostname
information. Implementations of this class should use this
constructor to use Kerberos.

The parameters are not authenticated by the

SSLEngine

.

SSLEngine

implementations may use the

peerHost

and

peerPort

parameters as hints
for their internal session reuse strategy.

Some cipher suites (such as Kerberos) require remote hostname
information. Implementations of this class should use this
constructor to use Kerberos.

The parameters are not authenticated by the

SSLEngine

.

Some cipher suites (such as Kerberos) require remote hostname
information. Implementations of this class should use this
constructor to use Kerberos.

The parameters are not authenticated by the

SSLEngine

.

The parameters are not authenticated by the

SSLEngine

.

Method Detail

- getPeerHost

```java
public
String
getPeerHost()
```

Returns the host name of the peer.

Note that the value is not authenticated, and should not be
relied upon.

**Returns:** the host name of the peer, or null if nothing is
available.

- getPeerPort

```java
public int getPeerPort()
```

Returns the port number of the peer.

Note that the value is not authenticated, and should not be
relied upon.

**Returns:** the port number of the peer, or -1 if nothing is
available.

- wrap

```java
public
SSLEngineResult
wrap​(
ByteBuffer
src,

ByteBuffer
dst)
throws
SSLException
```

Attempts to encode a buffer of plaintext application data into
SSL/TLS/DTLS network data.

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.wrap(new ByteBuffer [] { src }, 0, 1, dst);
```

**Parameters:** src

- a

ByteBuffer

containing outbound application data
**Parameters:** dst

- a

ByteBuffer

to hold outbound network data
**Returns:** an

SSLEngineResult

describing the result
of this operation.
**Throws:** SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
**Throws:** ReadOnlyBufferException

- if the

dst

buffer is read-only.
**Throws:** IllegalArgumentException

- if either

src

or

dst

is null.
**Throws:** IllegalStateException

- if the client/server mode
has not yet been set.
**See Also:** wrap(ByteBuffer [], int, int, ByteBuffer)

- wrap

```java
public
SSLEngineResult
wrap​(
ByteBuffer
[] srcs,

ByteBuffer
dst)
throws
SSLException
```

Attempts to encode plaintext bytes from a sequence of data
buffers into SSL/TLS/DTLS network data.

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.wrap(srcs, 0, srcs.length, dst);
```

**Parameters:** srcs

- an array of

ByteBuffers

containing the
outbound application data
**Parameters:** dst

- a

ByteBuffer

to hold outbound network data
**Returns:** an

SSLEngineResult

describing the result
of this operation.
**Throws:** SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
**Throws:** ReadOnlyBufferException

- if the

dst

buffer is read-only.
**Throws:** IllegalArgumentException

- if either

srcs

or

dst

is null, or if any element in

srcs

is null.
**Throws:** IllegalStateException

- if the client/server mode
has not yet been set.
**See Also:** wrap(ByteBuffer [], int, int, ByteBuffer)

- wrap

```java
public abstract
SSLEngineResult
wrap​(
ByteBuffer
[] srcs,
int offset,
int length,

ByteBuffer
dst)
throws
SSLException
```

Attempts to encode plaintext bytes from a subsequence of data
buffers into SSL/TLS/DTLS network data. This

"gathering"

operation encodes, in a single invocation, a sequence of bytes
from one or more of a given sequence of buffers. Gathering
wraps are often useful when implementing network protocols or
file formats that, for example, group data into segments
consisting of one or more fixed-length headers followed by a
variable-length body. See

GatheringByteChannel

for more
information on gathering, and

GatheringByteChannel.write(ByteBuffer[],
int, int)

for more information on the subsequence
behavior.

Depending on the state of the SSLEngine, this method may produce
network data without consuming any application data (for example,
it may generate handshake data.)

The application is responsible for reliably transporting the
network data to the peer, and for ensuring that data created by
multiple calls to wrap() is transported in the same order in which
it was generated. The application must properly synchronize
multiple calls to this method.

If this

SSLEngine

has not yet started its initial
handshake, this method will automatically start the handshake.

This method will attempt to produce SSL/TLS/DTLS records, and will
consume as much source data as possible, but will never consume
more than the sum of the bytes remaining in each buffer. Each

ByteBuffer

's position is updated to reflect the
amount of data consumed or produced. The limits remain the
same.

The underlying memory used by the

srcs

and

dst ByteBuffer

s must not be the same.

See the class description for more information on engine closure.

**Parameters:** srcs

- an array of

ByteBuffers

containing the
outbound application data
**Parameters:** offset

- The offset within the buffer array of the first buffer from
which bytes are to be retrieved; it must be non-negative
and no larger than

srcs.length
**Parameters:** length

- The maximum number of buffers to be accessed; it must be
non-negative and no larger than

srcs.length

-

offset
**Parameters:** dst

- a

ByteBuffer

to hold outbound network data
**Returns:** an

SSLEngineResult

describing the result
of this operation.
**Throws:** SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
**Throws:** IndexOutOfBoundsException

- if the preconditions on the

offset

and

length

parameters do not hold.
**Throws:** ReadOnlyBufferException

- if the

dst

buffer is read-only.
**Throws:** IllegalArgumentException

- if either

srcs

or

dst

is null, or if any element in the

srcs

subsequence specified is null.
**Throws:** IllegalStateException

- if the client/server mode
has not yet been set.
**See Also:** GatheringByteChannel

,

GatheringByteChannel.write(
ByteBuffer[], int, int)

- unwrap

```java
public
SSLEngineResult
unwrap​(
ByteBuffer
src,

ByteBuffer
dst)
throws
SSLException
```

Attempts to decode SSL/TLS/DTLS network data into a plaintext
application data buffer.

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.unwrap(src, new ByteBuffer [] { dst }, 0, 1);
```

**Parameters:** src

- a

ByteBuffer

containing inbound network data.
**Parameters:** dst

- a

ByteBuffer

to hold inbound application data.
**Returns:** an

SSLEngineResult

describing the result
of this operation.
**Throws:** SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
**Throws:** ReadOnlyBufferException

- if the

dst

buffer is read-only.
**Throws:** IllegalArgumentException

- if either

src

or

dst

is null.
**Throws:** IllegalStateException

- if the client/server mode
has not yet been set.
**See Also:** unwrap(ByteBuffer, ByteBuffer [], int, int)

- unwrap

```java
public
SSLEngineResult
unwrap​(
ByteBuffer
src,

ByteBuffer
[] dsts)
throws
SSLException
```

Attempts to decode SSL/TLS/DTLS network data into a sequence of plaintext
application data buffers.

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.unwrap(src, dsts, 0, dsts.length);
```

**Parameters:** src

- a

ByteBuffer

containing inbound network data.
**Parameters:** dsts

- an array of

ByteBuffer

s to hold inbound
application data.
**Returns:** an

SSLEngineResult

describing the result
of this operation.
**Throws:** SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
**Throws:** ReadOnlyBufferException

- if any of the

dst

buffers are read-only.
**Throws:** IllegalArgumentException

- if either

src

or

dsts

is null, or if any element in

dsts

is null.
**Throws:** IllegalStateException

- if the client/server mode
has not yet been set.
**See Also:** unwrap(ByteBuffer, ByteBuffer [], int, int)

- unwrap

```java
public abstract
SSLEngineResult
unwrap​(
ByteBuffer
src,

ByteBuffer
[] dsts,
int offset,
int length)
throws
SSLException
```

Attempts to decode SSL/TLS/DTLS network data into a subsequence of
plaintext application data buffers. This

"scattering"

operation decodes, in a single invocation, a sequence of bytes
into one or more of a given sequence of buffers. Scattering
unwraps are often useful when implementing network protocols or
file formats that, for example, group data into segments
consisting of one or more fixed-length headers followed by a
variable-length body. See

ScatteringByteChannel

for more
information on scattering, and

ScatteringByteChannel.read(ByteBuffer[],
int, int)

for more information on the subsequence
behavior.

Depending on the state of the SSLEngine, this method may consume
network data without producing any application data (for example,
it may consume handshake data.)

The application is responsible for reliably obtaining the network
data from the peer, and for invoking unwrap() on the data in the
order it was received. The application must properly synchronize
multiple calls to this method.

If this

SSLEngine

has not yet started its initial
handshake, this method will automatically start the handshake.

This method will attempt to consume one complete SSL/TLS/DTLS network
packet, but will never consume more than the sum of the bytes
remaining in the buffers. Each

ByteBuffer

's
position is updated to reflect the amount of data consumed or
produced. The limits remain the same.

The underlying memory used by the

src

and

dsts ByteBuffer

s must not be the same.

The inbound network buffer may be modified as a result of this
call: therefore if the network data packet is required for some
secondary purpose, the data should be duplicated before calling this
method. Note: the network data will not be useful to a second
SSLEngine, as each SSLEngine contains unique random state which
influences the SSL/TLS/DTLS messages.

See the class description for more information on engine closure.

**Parameters:** src

- a

ByteBuffer

containing inbound network data.
**Parameters:** dsts

- an array of

ByteBuffer

s to hold inbound
application data.
**Parameters:** offset

- The offset within the buffer array of the first buffer from
which bytes are to be transferred; it must be non-negative
and no larger than

dsts.length

.
**Parameters:** length

- The maximum number of buffers to be accessed; it must be
non-negative and no larger than

dsts.length

-

offset

.
**Returns:** an

SSLEngineResult

describing the result
of this operation.
**Throws:** SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold.
**Throws:** ReadOnlyBufferException

- if any of the

dst

buffers are read-only.
**Throws:** IllegalArgumentException

- if either

src

or

dsts

is null, or if any element in the

dsts

subsequence specified is null.
**Throws:** IllegalStateException

- if the client/server mode
has not yet been set.
**See Also:** ScatteringByteChannel

,

ScatteringByteChannel.read(
ByteBuffer[], int, int)

- getDelegatedTask

```java
public abstract
Runnable
getDelegatedTask()
```

Returns a delegated

Runnable

task for
this

SSLEngine

.

SSLEngine

operations may require the results of
operations that block, or may take an extended period of time to
complete. This method is used to obtain an outstanding

Runnable

operation (task). Each task must be assigned
a thread (possibly the current) to perform the

run

operation. Once the

run

method returns, the

Runnable

object
is no longer needed and may be discarded.

Delegated tasks run in the

AccessControlContext

in place when this object was created.

A call to this method will return each outstanding task
exactly once.

Multiple delegated tasks can be run in parallel.

**Returns:** a delegated

Runnable

task, or null
if none are available.

- closeInbound

```java
public abstract void closeInbound()
throws
SSLException
```

Signals that no more inbound network data will be sent
to this

SSLEngine

.

If the application initiated the closing process by calling

closeOutbound()

, under some circumstances it is not
required that the initiator wait for the peer's corresponding
close message. (See section 7.2.1 of the TLS specification (

RFC 2246

) for more
information on waiting for closure alerts.) In such cases, this
method need not be called.

But if the application did not initiate the closure process, or
if the circumstances above do not apply, this method should be
called whenever the end of the SSL/TLS/DTLS data stream is reached.
This ensures closure of the inbound side, and checks that the
peer followed the SSL/TLS/DTLS close procedure properly, thus
detecting possible truncation attacks.

This method is idempotent: if the inbound side has already
been closed, this method does not do anything.

wrap()

should be
called to flush any remaining handshake data.

**Throws:** SSLException

- if this engine has not received the proper SSL/TLS/DTLS close
notification message from the peer.
**See Also:** isInboundDone()

,

isOutboundDone()

- isInboundDone

```java
public abstract boolean isInboundDone()
```

Returns whether

unwrap(ByteBuffer, ByteBuffer)

will
accept any more inbound data messages.

**Returns:** true if the

SSLEngine

will not
consume anymore network data (and by implication,
will not produce any more application data.)
**See Also:** closeInbound()

- closeOutbound

```java
public abstract void closeOutbound()
```

Signals that no more outbound application data will be sent
on this

SSLEngine

.

This method is idempotent: if the outbound side has already
been closed, this method does not do anything.

wrap(ByteBuffer, ByteBuffer)

should be
called to flush any remaining handshake data.

**See Also:** isOutboundDone()

- isOutboundDone

```java
public abstract boolean isOutboundDone()
```

Returns whether

wrap(ByteBuffer, ByteBuffer)

will
produce any more outbound data messages.

Note that during the closure phase, a

SSLEngine

may
generate handshake closure data that must be sent to the peer.

wrap()

must be called to generate this data. When
this method returns true, no more outbound data will be created.

**Returns:** true if the

SSLEngine

will not produce
any more network data
**See Also:** closeOutbound()

,

closeInbound()

- getSupportedCipherSuites

```java
public abstract
String
[] getSupportedCipherSuites()
```

Returns the names of the cipher suites which could be enabled for use
on this engine. Normally, only a subset of these will actually
be enabled by default, since this list may include cipher suites which
do not meet quality of service requirements for those defaults. Such
cipher suites might be useful in specialized applications.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:** an array of cipher suite names
**See Also:** getEnabledCipherSuites()

,

setEnabledCipherSuites(String [])

- getEnabledCipherSuites

```java
public abstract
String
[] getEnabledCipherSuites()
```

Returns the names of the SSL cipher suites which are currently
enabled for use on this engine. When an SSLEngine is first
created, all enabled cipher suites support a minimum quality of
service. Thus, in some environments this value might be empty.

Note that even if a suite is enabled, it may never be used. This
can occur if the peer does not support it, or its use is restricted,
or the requisite certificates (and private keys) for the suite are
not available, or an anonymous suite is enabled but authentication
is required.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:** an array of cipher suite names
**See Also:** getSupportedCipherSuites()

,

setEnabledCipherSuites(String [])

- setEnabledCipherSuites

```java
public abstract void setEnabledCipherSuites​(
String
[] suites)
```

Sets the cipher suites enabled for use on this engine.

Each cipher suite in the

suites

parameter must have
been listed by getSupportedCipherSuites(), or the method will
fail. Following a successful call to this method, only suites
listed in the

suites

parameter are enabled for use.

Note that the standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list or might not
use the recommended name for a certain cipher suite.

See

getEnabledCipherSuites()

for more information
on why a specific cipher suite may never be used on a engine.

**Parameters:** suites

- Names of all the cipher suites to enable
**Throws:** IllegalArgumentException

- when one or more of the ciphers
named by the parameter is not supported, or when the
parameter is null.
**See Also:** getSupportedCipherSuites()

,

getEnabledCipherSuites()

- getSupportedProtocols

```java
public abstract
String
[] getSupportedProtocols()
```

Returns the names of the protocols which could be enabled for use
with this

SSLEngine

.

**Returns:** an array of protocols supported

- getEnabledProtocols

```java
public abstract
String
[] getEnabledProtocols()
```

Returns the names of the protocol versions which are currently
enabled for use with this

SSLEngine

.

Note that even if a protocol is enabled, it may never be used.
This can occur if the peer does not support the protocol, or its
use is restricted, or there are no enabled cipher suites supported
by the protocol.

**Returns:** an array of protocols
**See Also:** setEnabledProtocols(String [])

- setEnabledProtocols

```java
public abstract void setEnabledProtocols​(
String
[] protocols)
```

Set the protocol versions enabled for use on this engine.

The protocols must have been listed by getSupportedProtocols()
as being supported. Following a successful call to this method,
only protocols listed in the

protocols

parameter
are enabled for use.

**Parameters:** protocols

- Names of all the protocols to enable.
**Throws:** IllegalArgumentException

- when one or more of
the protocols named by the parameter is not supported or
when the protocols parameter is null.
**See Also:** getEnabledProtocols()

- getSession

```java
public abstract
SSLSession
getSession()
```

Returns the

SSLSession

in use in this

SSLEngine

.

These can be long lived, and frequently correspond to an entire
login session for some user. The session specifies a particular
cipher suite which is being actively used by all connections in
that session, as well as the identities of the session's client
and server.

Unlike

SSLSocket.getSession()

this method does not block until handshaking is complete.

Until the initial handshake has completed, this method returns
a session object which reports an invalid cipher suite of
"SSL_NULL_WITH_NULL_NULL".

**Returns:** the

SSLSession

for this

SSLEngine
**See Also:** SSLSession

- getHandshakeSession

```java
public
SSLSession
getHandshakeSession()
```

Returns the

SSLSession

being constructed during a SSL/TLS/DTLS
handshake.

TLS/DTLS protocols may negotiate parameters that are needed when using
an instance of this class, but before the

SSLSession

has
been completely initialized and made available via

getSession

.
For example, the list of valid signature algorithms may restrict
the type of certificates that can be used during TrustManager
decisions, or the maximum TLS/DTLS fragment packet sizes can be
resized to better support the network environment.

This method provides early access to the

SSLSession

being
constructed. Depending on how far the handshake has progressed,
some data may not yet be available for use. For example, if a
remote server will be sending a Certificate chain, but that chain
has yet not been processed, the

getPeerCertificates

method of

SSLSession

will throw a
SSLPeerUnverifiedException. Once that chain has been processed,

getPeerCertificates

will return the proper value.

**Returns:** null if this instance is not currently handshaking, or
if the current handshake has not progressed far enough to
create a basic SSLSession. Otherwise, this method returns the

SSLSession

currently being negotiated.
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation.
**Since:** 1.7
**See Also:** SSLSocket

,

SSLSession

,

ExtendedSSLSession

,

X509ExtendedKeyManager

,

X509ExtendedTrustManager

- beginHandshake

```java
public abstract void beginHandshake()
throws
SSLException
```

Initiates handshaking (initial or renegotiation) on this SSLEngine.

This method is not needed for the initial handshake, as the

wrap()

and

unwrap()

methods will
implicitly call this method if handshaking has not already begun.

Note that the peer may also request a session renegotiation with
this

SSLEngine

by sending the appropriate
session renegotiate handshake message.

Unlike the

SSLSocket#startHandshake()

method, this method does not block
until handshaking is completed.

To force a complete SSL/TLS/DTLS session renegotiation, the current
session should be invalidated prior to calling this method.

Some protocols may not support multiple handshakes on an existing
engine and may throw an

SSLException

.

**Throws:** SSLException

- if a problem was encountered while signaling the

SSLEngine

to begin a new handshake.
See the class description for more information on
engine closure.
**Throws:** IllegalStateException

- if the client/server mode
has not yet been set.
**See Also:** SSLSession.invalidate()

- getHandshakeStatus

```java
public abstract
SSLEngineResult.HandshakeStatus
getHandshakeStatus()
```

Returns the current handshake status for this

SSLEngine

.

**Returns:** the current

SSLEngineResult.HandshakeStatus

.

- setUseClientMode

```java
public abstract void setUseClientMode​(boolean mode)
```

Configures the engine to use client (or server) mode when
handshaking.

This method must be called before any handshaking occurs.
Once handshaking has begun, the mode can not be reset for the
life of this engine.

Servers normally authenticate themselves, and clients
are not required to do so.

**Implementation Note:** The JDK SunJSSE provider implementation default for this mode is false.
**Parameters:** mode

- true if the engine should start its handshaking
in "client" mode
**Throws:** IllegalArgumentException

- if a mode change is attempted
after the initial handshake has begun.
**See Also:** getUseClientMode()

- getUseClientMode

```java
public abstract boolean getUseClientMode()
```

Returns true if the engine is set to use client mode when
handshaking.

**Implementation Note:** The JDK SunJSSE provider implementation returns false unless

setUseClientMode(boolean)

is used to change the mode to true.
**Returns:** true if the engine should do handshaking
in "client" mode
**See Also:** setUseClientMode(boolean)

- setNeedClientAuth

```java
public abstract void setNeedClientAuth​(boolean need)
```

Configures the engine to

require

client authentication. This
option is only useful for engines in the server mode.

An engine's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setWantClientAuth(boolean)

, if this option is set and
the client chooses not to provide authentication information
about itself,

the negotiations will stop and the engine will
begin its closure procedure

.

Calling this method overrides any previous setting made by
this method or

setWantClientAuth(boolean)

.

**Parameters:** need

- set to true if client authentication is required,
or false if no client authentication is desired.
**See Also:** getNeedClientAuth()

,

setWantClientAuth(boolean)

,

getWantClientAuth()

,

setUseClientMode(boolean)

- getNeedClientAuth

```java
public abstract boolean getNeedClientAuth()
```

Returns true if the engine will

require

client authentication.
This option is only useful to engines in the server mode.

**Returns:** true if client authentication is required,
or false if no client authentication is desired.
**See Also:** setNeedClientAuth(boolean)

,

setWantClientAuth(boolean)

,

getWantClientAuth()

,

setUseClientMode(boolean)

- setWantClientAuth

```java
public abstract void setWantClientAuth​(boolean want)
```

Configures the engine to

request

client authentication.
This option is only useful for engines in the server mode.

An engine's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setNeedClientAuth(boolean)

, if this option is set and
the client chooses not to provide authentication information
about itself,

the negotiations will continue

.

Calling this method overrides any previous setting made by
this method or

setNeedClientAuth(boolean)

.

**Parameters:** want

- set to true if client authentication is requested,
or false if no client authentication is desired.
**See Also:** getWantClientAuth()

,

setNeedClientAuth(boolean)

,

getNeedClientAuth()

,

setUseClientMode(boolean)

- getWantClientAuth

```java
public abstract boolean getWantClientAuth()
```

Returns true if the engine will

request

client authentication.
This option is only useful for engines in the server mode.

**Returns:** true if client authentication is requested,
or false if no client authentication is desired.
**See Also:** setNeedClientAuth(boolean)

,

getNeedClientAuth()

,

setWantClientAuth(boolean)

,

setUseClientMode(boolean)

- setEnableSessionCreation

```java
public abstract void setEnableSessionCreation​(boolean flag)
```

Controls whether new SSL sessions may be established by this engine.
If session creations are not allowed, and there are no
existing sessions to resume, there will be no successful
handshaking.

**Parameters:** flag

- true indicates that sessions may be created; this
is the default. false indicates that an existing session
must be resumed
**See Also:** getEnableSessionCreation()

- getEnableSessionCreation

```java
public abstract boolean getEnableSessionCreation()
```

Returns true if new SSL sessions may be established by this engine.

**Returns:** true indicates that sessions may be created; this
is the default. false indicates that an existing session
must be resumed
**See Also:** setEnableSessionCreation(boolean)

- getSSLParameters

```java
public
SSLParameters
getSSLParameters()
```

Returns the SSLParameters in effect for this SSLEngine.
The ciphersuites and protocols of the returned SSLParameters
are always non-null.

**Returns:** the SSLParameters in effect for this SSLEngine.
**Since:** 1.6

- setSSLParameters

```java
public void setSSLParameters​(
SSLParameters
params)
```

Applies SSLParameters to this engine.

This means:

- If

params.getCipherSuites()

is non-null,

setEnabledCipherSuites()

is called with that value.
- If

params.getProtocols()

is non-null,

setEnabledProtocols()

is called with that value.
- If

params.getNeedClientAuth()

or

params.getWantClientAuth()

return

true

,

setNeedClientAuth(true)

and

setWantClientAuth(true)

are called, respectively;
otherwise

setWantClientAuth(false)

is called.
- If

params.getServerNames()

is non-null, the engine will
configure its server names with that value.
- If

params.getSNIMatchers()

is non-null, the engine will
configure its SNI matchers with that value.

**Parameters:** params

- the parameters
**Throws:** IllegalArgumentException

- if the setEnabledCipherSuites() or
the setEnabledProtocols() call fails
**Since:** 1.6

- getApplicationProtocol

```java
public
String
getApplicationProtocol()
```

Returns the most recent application protocol value negotiated for this
connection.

If supported by the underlying SSL/TLS/DTLS implementation,
application name negotiation mechanisms such as

RFC 7301

, the
Application-Layer Protocol Negotiation (ALPN), can negotiate
application-level values between peers.

**Implementation Requirements:** The implementation in this class throws

UnsupportedOperationException

and performs no other action.
**Returns:** null if it has not yet been determined if application
protocols might be used for this connection, an empty

String

if application protocols values will not
be used, or a non-empty application protocol

String

if a value was successfully negotiated.
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation.
**Since:** 9

- getHandshakeApplicationProtocol

```java
public
String
getHandshakeApplicationProtocol()
```

Returns the application protocol value negotiated on a SSL/TLS
handshake currently in progress.

Like

getHandshakeSession()

,
a connection may be in the middle of a handshake. The
application protocol may or may not yet be available.

**Implementation Requirements:** The implementation in this class throws

UnsupportedOperationException

and performs no other action.
**Returns:** null if it has not yet been determined if application
protocols might be used for this handshake, an empty

String

if application protocols values will not
be used, or a non-empty application protocol

String

if a value was successfully negotiated.
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation.
**Since:** 9

- setHandshakeApplicationProtocolSelector

```java
public void setHandshakeApplicationProtocolSelector​(
BiFunction
<
SSLEngine
,​
List
<
String
>,​
String
> selector)
```

Registers a callback function that selects an application protocol
value for a SSL/TLS/DTLS handshake.
The function overrides any values supplied using

SSLParameters.setApplicationProtocols

and it supports the following
type parameters:

For example, the following call registers a callback function that
examines the TLS handshake parameters and selects an application protocol
name:

```java
serverEngine.setHandshakeApplicationProtocolSelector(
(serverEngine, clientProtocols) -> {
SSLSession session = serverEngine.getHandshakeSession();
return chooseApplicationProtocol(
serverEngine,
clientProtocols,
session.getProtocol(),
session.getCipherSuite());
});
```

**API Note:** This method should be called by TLS server applications before the TLS
handshake begins. Also, this

SSLEngine

should be configured with
parameters that are compatible with the application protocol selected by
the callback function. For example, enabling a poor choice of cipher
suites could result in no suitable application protocol.
See

SSLParameters

.
**Implementation Requirements:** The implementation in this class throws

UnsupportedOperationException

and performs no other action.
**Parameters:** selector

- the callback function, or null to disable the callback
functionality.
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation.
**Since:** 9

- getHandshakeApplicationProtocolSelector

```java
public
BiFunction
<
SSLEngine
,​
List
<
String
>,​
String
> getHandshakeApplicationProtocolSelector()
```

Retrieves the callback function that selects an application protocol
value during a SSL/TLS/DTLS handshake.
See

setHandshakeApplicationProtocolSelector

for the function's type parameters.

**Implementation Requirements:** The implementation in this class throws

UnsupportedOperationException

and performs no other action.
**Returns:** the callback function, or null if none has been set.
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation.
**Since:** 9

---

#### Method Detail

getPeerHost

```java
public
String
getPeerHost()
```

Returns the host name of the peer.

Note that the value is not authenticated, and should not be
relied upon.

**Returns:** the host name of the peer, or null if nothing is
available.

---

#### getPeerHost

public

String

getPeerHost()

Returns the host name of the peer.

Note that the value is not authenticated, and should not be
relied upon.

Note that the value is not authenticated, and should not be
relied upon.

getPeerPort

```java
public int getPeerPort()
```

Returns the port number of the peer.

Note that the value is not authenticated, and should not be
relied upon.

**Returns:** the port number of the peer, or -1 if nothing is
available.

---

#### getPeerPort

public int getPeerPort()

Returns the port number of the peer.

Note that the value is not authenticated, and should not be
relied upon.

Note that the value is not authenticated, and should not be
relied upon.

wrap

```java
public
SSLEngineResult
wrap​(
ByteBuffer
src,

ByteBuffer
dst)
throws
SSLException
```

Attempts to encode a buffer of plaintext application data into
SSL/TLS/DTLS network data.

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.wrap(new ByteBuffer [] { src }, 0, 1, dst);
```

**Parameters:** src

- a

ByteBuffer

containing outbound application data
**Parameters:** dst

- a

ByteBuffer

to hold outbound network data
**Returns:** an

SSLEngineResult

describing the result
of this operation.
**Throws:** SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
**Throws:** ReadOnlyBufferException

- if the

dst

buffer is read-only.
**Throws:** IllegalArgumentException

- if either

src

or

dst

is null.
**Throws:** IllegalStateException

- if the client/server mode
has not yet been set.
**See Also:** wrap(ByteBuffer [], int, int, ByteBuffer)

---

#### wrap

public

SSLEngineResult

wrap​(

ByteBuffer

src,

ByteBuffer

dst)
throws

SSLException

Attempts to encode a buffer of plaintext application data into
SSL/TLS/DTLS network data.

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.wrap(new ByteBuffer [] { src }, 0, 1, dst);
```

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.wrap(new ByteBuffer [] { src }, 0, 1, dst);
```

engine.wrap(new ByteBuffer [] { src }, 0, 1, dst);

wrap

```java
public
SSLEngineResult
wrap​(
ByteBuffer
[] srcs,

ByteBuffer
dst)
throws
SSLException
```

Attempts to encode plaintext bytes from a sequence of data
buffers into SSL/TLS/DTLS network data.

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.wrap(srcs, 0, srcs.length, dst);
```

**Parameters:** srcs

- an array of

ByteBuffers

containing the
outbound application data
**Parameters:** dst

- a

ByteBuffer

to hold outbound network data
**Returns:** an

SSLEngineResult

describing the result
of this operation.
**Throws:** SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
**Throws:** ReadOnlyBufferException

- if the

dst

buffer is read-only.
**Throws:** IllegalArgumentException

- if either

srcs

or

dst

is null, or if any element in

srcs

is null.
**Throws:** IllegalStateException

- if the client/server mode
has not yet been set.
**See Also:** wrap(ByteBuffer [], int, int, ByteBuffer)

---

#### wrap

public

SSLEngineResult

wrap​(

ByteBuffer

[] srcs,

ByteBuffer

dst)
throws

SSLException

Attempts to encode plaintext bytes from a sequence of data
buffers into SSL/TLS/DTLS network data.

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.wrap(srcs, 0, srcs.length, dst);
```

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.wrap(srcs, 0, srcs.length, dst);
```

engine.wrap(srcs, 0, srcs.length, dst);

wrap

```java
public abstract
SSLEngineResult
wrap​(
ByteBuffer
[] srcs,
int offset,
int length,

ByteBuffer
dst)
throws
SSLException
```

Attempts to encode plaintext bytes from a subsequence of data
buffers into SSL/TLS/DTLS network data. This

"gathering"

operation encodes, in a single invocation, a sequence of bytes
from one or more of a given sequence of buffers. Gathering
wraps are often useful when implementing network protocols or
file formats that, for example, group data into segments
consisting of one or more fixed-length headers followed by a
variable-length body. See

GatheringByteChannel

for more
information on gathering, and

GatheringByteChannel.write(ByteBuffer[],
int, int)

for more information on the subsequence
behavior.

Depending on the state of the SSLEngine, this method may produce
network data without consuming any application data (for example,
it may generate handshake data.)

The application is responsible for reliably transporting the
network data to the peer, and for ensuring that data created by
multiple calls to wrap() is transported in the same order in which
it was generated. The application must properly synchronize
multiple calls to this method.

If this

SSLEngine

has not yet started its initial
handshake, this method will automatically start the handshake.

This method will attempt to produce SSL/TLS/DTLS records, and will
consume as much source data as possible, but will never consume
more than the sum of the bytes remaining in each buffer. Each

ByteBuffer

's position is updated to reflect the
amount of data consumed or produced. The limits remain the
same.

The underlying memory used by the

srcs

and

dst ByteBuffer

s must not be the same.

See the class description for more information on engine closure.

**Parameters:** srcs

- an array of

ByteBuffers

containing the
outbound application data
**Parameters:** offset

- The offset within the buffer array of the first buffer from
which bytes are to be retrieved; it must be non-negative
and no larger than

srcs.length
**Parameters:** length

- The maximum number of buffers to be accessed; it must be
non-negative and no larger than

srcs.length

-

offset
**Parameters:** dst

- a

ByteBuffer

to hold outbound network data
**Returns:** an

SSLEngineResult

describing the result
of this operation.
**Throws:** SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
**Throws:** IndexOutOfBoundsException

- if the preconditions on the

offset

and

length

parameters do not hold.
**Throws:** ReadOnlyBufferException

- if the

dst

buffer is read-only.
**Throws:** IllegalArgumentException

- if either

srcs

or

dst

is null, or if any element in the

srcs

subsequence specified is null.
**Throws:** IllegalStateException

- if the client/server mode
has not yet been set.
**See Also:** GatheringByteChannel

,

GatheringByteChannel.write(
ByteBuffer[], int, int)

---

#### wrap

public abstract

SSLEngineResult

wrap​(

ByteBuffer

[] srcs,
int offset,
int length,

ByteBuffer

dst)
throws

SSLException

Attempts to encode plaintext bytes from a subsequence of data
buffers into SSL/TLS/DTLS network data. This

"gathering"

operation encodes, in a single invocation, a sequence of bytes
from one or more of a given sequence of buffers. Gathering
wraps are often useful when implementing network protocols or
file formats that, for example, group data into segments
consisting of one or more fixed-length headers followed by a
variable-length body. See

GatheringByteChannel

for more
information on gathering, and

GatheringByteChannel.write(ByteBuffer[],
int, int)

for more information on the subsequence
behavior.

Depending on the state of the SSLEngine, this method may produce
network data without consuming any application data (for example,
it may generate handshake data.)

The application is responsible for reliably transporting the
network data to the peer, and for ensuring that data created by
multiple calls to wrap() is transported in the same order in which
it was generated. The application must properly synchronize
multiple calls to this method.

If this

SSLEngine

has not yet started its initial
handshake, this method will automatically start the handshake.

This method will attempt to produce SSL/TLS/DTLS records, and will
consume as much source data as possible, but will never consume
more than the sum of the bytes remaining in each buffer. Each

ByteBuffer

's position is updated to reflect the
amount of data consumed or produced. The limits remain the
same.

The underlying memory used by the

srcs

and

dst ByteBuffer

s must not be the same.

See the class description for more information on engine closure.

Depending on the state of the SSLEngine, this method may produce
network data without consuming any application data (for example,
it may generate handshake data.)

The application is responsible for reliably transporting the
network data to the peer, and for ensuring that data created by
multiple calls to wrap() is transported in the same order in which
it was generated. The application must properly synchronize
multiple calls to this method.

If this

SSLEngine

has not yet started its initial
handshake, this method will automatically start the handshake.

This method will attempt to produce SSL/TLS/DTLS records, and will
consume as much source data as possible, but will never consume
more than the sum of the bytes remaining in each buffer. Each

ByteBuffer

's position is updated to reflect the
amount of data consumed or produced. The limits remain the
same.

The underlying memory used by the

srcs

and

dst ByteBuffer

s must not be the same.

See the class description for more information on engine closure.

The application is responsible for reliably transporting the
network data to the peer, and for ensuring that data created by
multiple calls to wrap() is transported in the same order in which
it was generated. The application must properly synchronize
multiple calls to this method.

If this

SSLEngine

has not yet started its initial
handshake, this method will automatically start the handshake.

This method will attempt to produce SSL/TLS/DTLS records, and will
consume as much source data as possible, but will never consume
more than the sum of the bytes remaining in each buffer. Each

ByteBuffer

's position is updated to reflect the
amount of data consumed or produced. The limits remain the
same.

The underlying memory used by the

srcs

and

dst ByteBuffer

s must not be the same.

See the class description for more information on engine closure.

If this

SSLEngine

has not yet started its initial
handshake, this method will automatically start the handshake.

This method will attempt to produce SSL/TLS/DTLS records, and will
consume as much source data as possible, but will never consume
more than the sum of the bytes remaining in each buffer. Each

ByteBuffer

's position is updated to reflect the
amount of data consumed or produced. The limits remain the
same.

The underlying memory used by the

srcs

and

dst ByteBuffer

s must not be the same.

See the class description for more information on engine closure.

This method will attempt to produce SSL/TLS/DTLS records, and will
consume as much source data as possible, but will never consume
more than the sum of the bytes remaining in each buffer. Each

ByteBuffer

's position is updated to reflect the
amount of data consumed or produced. The limits remain the
same.

The underlying memory used by the

srcs

and

dst ByteBuffer

s must not be the same.

See the class description for more information on engine closure.

The underlying memory used by the

srcs

and

dst ByteBuffer

s must not be the same.

See the class description for more information on engine closure.

See the class description for more information on engine closure.

unwrap

```java
public
SSLEngineResult
unwrap​(
ByteBuffer
src,

ByteBuffer
dst)
throws
SSLException
```

Attempts to decode SSL/TLS/DTLS network data into a plaintext
application data buffer.

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.unwrap(src, new ByteBuffer [] { dst }, 0, 1);
```

**Parameters:** src

- a

ByteBuffer

containing inbound network data.
**Parameters:** dst

- a

ByteBuffer

to hold inbound application data.
**Returns:** an

SSLEngineResult

describing the result
of this operation.
**Throws:** SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
**Throws:** ReadOnlyBufferException

- if the

dst

buffer is read-only.
**Throws:** IllegalArgumentException

- if either

src

or

dst

is null.
**Throws:** IllegalStateException

- if the client/server mode
has not yet been set.
**See Also:** unwrap(ByteBuffer, ByteBuffer [], int, int)

---

#### unwrap

public

SSLEngineResult

unwrap​(

ByteBuffer

src,

ByteBuffer

dst)
throws

SSLException

Attempts to decode SSL/TLS/DTLS network data into a plaintext
application data buffer.

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.unwrap(src, new ByteBuffer [] { dst }, 0, 1);
```

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.unwrap(src, new ByteBuffer [] { dst }, 0, 1);
```

engine.unwrap(src, new ByteBuffer [] { dst }, 0, 1);

unwrap

```java
public
SSLEngineResult
unwrap​(
ByteBuffer
src,

ByteBuffer
[] dsts)
throws
SSLException
```

Attempts to decode SSL/TLS/DTLS network data into a sequence of plaintext
application data buffers.

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.unwrap(src, dsts, 0, dsts.length);
```

**Parameters:** src

- a

ByteBuffer

containing inbound network data.
**Parameters:** dsts

- an array of

ByteBuffer

s to hold inbound
application data.
**Returns:** an

SSLEngineResult

describing the result
of this operation.
**Throws:** SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
**Throws:** ReadOnlyBufferException

- if any of the

dst

buffers are read-only.
**Throws:** IllegalArgumentException

- if either

src

or

dsts

is null, or if any element in

dsts

is null.
**Throws:** IllegalStateException

- if the client/server mode
has not yet been set.
**See Also:** unwrap(ByteBuffer, ByteBuffer [], int, int)

---

#### unwrap

public

SSLEngineResult

unwrap​(

ByteBuffer

src,

ByteBuffer

[] dsts)
throws

SSLException

Attempts to decode SSL/TLS/DTLS network data into a sequence of plaintext
application data buffers.

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.unwrap(src, dsts, 0, dsts.length);
```

An invocation of this method behaves in exactly the same manner
as the invocation:

```java
engine.unwrap(src, dsts, 0, dsts.length);
```

engine.unwrap(src, dsts, 0, dsts.length);

unwrap

```java
public abstract
SSLEngineResult
unwrap​(
ByteBuffer
src,

ByteBuffer
[] dsts,
int offset,
int length)
throws
SSLException
```

Attempts to decode SSL/TLS/DTLS network data into a subsequence of
plaintext application data buffers. This

"scattering"

operation decodes, in a single invocation, a sequence of bytes
into one or more of a given sequence of buffers. Scattering
unwraps are often useful when implementing network protocols or
file formats that, for example, group data into segments
consisting of one or more fixed-length headers followed by a
variable-length body. See

ScatteringByteChannel

for more
information on scattering, and

ScatteringByteChannel.read(ByteBuffer[],
int, int)

for more information on the subsequence
behavior.

Depending on the state of the SSLEngine, this method may consume
network data without producing any application data (for example,
it may consume handshake data.)

The application is responsible for reliably obtaining the network
data from the peer, and for invoking unwrap() on the data in the
order it was received. The application must properly synchronize
multiple calls to this method.

If this

SSLEngine

has not yet started its initial
handshake, this method will automatically start the handshake.

This method will attempt to consume one complete SSL/TLS/DTLS network
packet, but will never consume more than the sum of the bytes
remaining in the buffers. Each

ByteBuffer

's
position is updated to reflect the amount of data consumed or
produced. The limits remain the same.

The underlying memory used by the

src

and

dsts ByteBuffer

s must not be the same.

The inbound network buffer may be modified as a result of this
call: therefore if the network data packet is required for some
secondary purpose, the data should be duplicated before calling this
method. Note: the network data will not be useful to a second
SSLEngine, as each SSLEngine contains unique random state which
influences the SSL/TLS/DTLS messages.

See the class description for more information on engine closure.

**Parameters:** src

- a

ByteBuffer

containing inbound network data.
**Parameters:** dsts

- an array of

ByteBuffer

s to hold inbound
application data.
**Parameters:** offset

- The offset within the buffer array of the first buffer from
which bytes are to be transferred; it must be non-negative
and no larger than

dsts.length

.
**Parameters:** length

- The maximum number of buffers to be accessed; it must be
non-negative and no larger than

dsts.length

-

offset

.
**Returns:** an

SSLEngineResult

describing the result
of this operation.
**Throws:** SSLException

- A problem was encountered while processing the
data that caused the

SSLEngine

to abort.
See the class description for more information on
engine closure.
**Throws:** IndexOutOfBoundsException

- If the preconditions on the

offset

and

length

parameters do not hold.
**Throws:** ReadOnlyBufferException

- if any of the

dst

buffers are read-only.
**Throws:** IllegalArgumentException

- if either

src

or

dsts

is null, or if any element in the

dsts

subsequence specified is null.
**Throws:** IllegalStateException

- if the client/server mode
has not yet been set.
**See Also:** ScatteringByteChannel

,

ScatteringByteChannel.read(
ByteBuffer[], int, int)

---

#### unwrap

public abstract

SSLEngineResult

unwrap​(

ByteBuffer

src,

ByteBuffer

[] dsts,
int offset,
int length)
throws

SSLException

Attempts to decode SSL/TLS/DTLS network data into a subsequence of
plaintext application data buffers. This

"scattering"

operation decodes, in a single invocation, a sequence of bytes
into one or more of a given sequence of buffers. Scattering
unwraps are often useful when implementing network protocols or
file formats that, for example, group data into segments
consisting of one or more fixed-length headers followed by a
variable-length body. See

ScatteringByteChannel

for more
information on scattering, and

ScatteringByteChannel.read(ByteBuffer[],
int, int)

for more information on the subsequence
behavior.

Depending on the state of the SSLEngine, this method may consume
network data without producing any application data (for example,
it may consume handshake data.)

The application is responsible for reliably obtaining the network
data from the peer, and for invoking unwrap() on the data in the
order it was received. The application must properly synchronize
multiple calls to this method.

If this

SSLEngine

has not yet started its initial
handshake, this method will automatically start the handshake.

This method will attempt to consume one complete SSL/TLS/DTLS network
packet, but will never consume more than the sum of the bytes
remaining in the buffers. Each

ByteBuffer

's
position is updated to reflect the amount of data consumed or
produced. The limits remain the same.

The underlying memory used by the

src

and

dsts ByteBuffer

s must not be the same.

The inbound network buffer may be modified as a result of this
call: therefore if the network data packet is required for some
secondary purpose, the data should be duplicated before calling this
method. Note: the network data will not be useful to a second
SSLEngine, as each SSLEngine contains unique random state which
influences the SSL/TLS/DTLS messages.

See the class description for more information on engine closure.

Depending on the state of the SSLEngine, this method may consume
network data without producing any application data (for example,
it may consume handshake data.)

The application is responsible for reliably obtaining the network
data from the peer, and for invoking unwrap() on the data in the
order it was received. The application must properly synchronize
multiple calls to this method.

If this

SSLEngine

has not yet started its initial
handshake, this method will automatically start the handshake.

This method will attempt to consume one complete SSL/TLS/DTLS network
packet, but will never consume more than the sum of the bytes
remaining in the buffers. Each

ByteBuffer

's
position is updated to reflect the amount of data consumed or
produced. The limits remain the same.

The underlying memory used by the

src

and

dsts ByteBuffer

s must not be the same.

The inbound network buffer may be modified as a result of this
call: therefore if the network data packet is required for some
secondary purpose, the data should be duplicated before calling this
method. Note: the network data will not be useful to a second
SSLEngine, as each SSLEngine contains unique random state which
influences the SSL/TLS/DTLS messages.

See the class description for more information on engine closure.

The application is responsible for reliably obtaining the network
data from the peer, and for invoking unwrap() on the data in the
order it was received. The application must properly synchronize
multiple calls to this method.

If this

SSLEngine

has not yet started its initial
handshake, this method will automatically start the handshake.

This method will attempt to consume one complete SSL/TLS/DTLS network
packet, but will never consume more than the sum of the bytes
remaining in the buffers. Each

ByteBuffer

's
position is updated to reflect the amount of data consumed or
produced. The limits remain the same.

The underlying memory used by the

src

and

dsts ByteBuffer

s must not be the same.

The inbound network buffer may be modified as a result of this
call: therefore if the network data packet is required for some
secondary purpose, the data should be duplicated before calling this
method. Note: the network data will not be useful to a second
SSLEngine, as each SSLEngine contains unique random state which
influences the SSL/TLS/DTLS messages.

See the class description for more information on engine closure.

If this

SSLEngine

has not yet started its initial
handshake, this method will automatically start the handshake.

This method will attempt to consume one complete SSL/TLS/DTLS network
packet, but will never consume more than the sum of the bytes
remaining in the buffers. Each

ByteBuffer

's
position is updated to reflect the amount of data consumed or
produced. The limits remain the same.

The underlying memory used by the

src

and

dsts ByteBuffer

s must not be the same.

The inbound network buffer may be modified as a result of this
call: therefore if the network data packet is required for some
secondary purpose, the data should be duplicated before calling this
method. Note: the network data will not be useful to a second
SSLEngine, as each SSLEngine contains unique random state which
influences the SSL/TLS/DTLS messages.

See the class description for more information on engine closure.

This method will attempt to consume one complete SSL/TLS/DTLS network
packet, but will never consume more than the sum of the bytes
remaining in the buffers. Each

ByteBuffer

's
position is updated to reflect the amount of data consumed or
produced. The limits remain the same.

The underlying memory used by the

src

and

dsts ByteBuffer

s must not be the same.

The inbound network buffer may be modified as a result of this
call: therefore if the network data packet is required for some
secondary purpose, the data should be duplicated before calling this
method. Note: the network data will not be useful to a second
SSLEngine, as each SSLEngine contains unique random state which
influences the SSL/TLS/DTLS messages.

See the class description for more information on engine closure.

The underlying memory used by the

src

and

dsts ByteBuffer

s must not be the same.

The inbound network buffer may be modified as a result of this
call: therefore if the network data packet is required for some
secondary purpose, the data should be duplicated before calling this
method. Note: the network data will not be useful to a second
SSLEngine, as each SSLEngine contains unique random state which
influences the SSL/TLS/DTLS messages.

See the class description for more information on engine closure.

The inbound network buffer may be modified as a result of this
call: therefore if the network data packet is required for some
secondary purpose, the data should be duplicated before calling this
method. Note: the network data will not be useful to a second
SSLEngine, as each SSLEngine contains unique random state which
influences the SSL/TLS/DTLS messages.

See the class description for more information on engine closure.

See the class description for more information on engine closure.

getDelegatedTask

```java
public abstract
Runnable
getDelegatedTask()
```

Returns a delegated

Runnable

task for
this

SSLEngine

.

SSLEngine

operations may require the results of
operations that block, or may take an extended period of time to
complete. This method is used to obtain an outstanding

Runnable

operation (task). Each task must be assigned
a thread (possibly the current) to perform the

run

operation. Once the

run

method returns, the

Runnable

object
is no longer needed and may be discarded.

Delegated tasks run in the

AccessControlContext

in place when this object was created.

A call to this method will return each outstanding task
exactly once.

Multiple delegated tasks can be run in parallel.

**Returns:** a delegated

Runnable

task, or null
if none are available.

---

#### getDelegatedTask

public abstract

Runnable

getDelegatedTask()

Returns a delegated

Runnable

task for
this

SSLEngine

.

SSLEngine

operations may require the results of
operations that block, or may take an extended period of time to
complete. This method is used to obtain an outstanding

Runnable

operation (task). Each task must be assigned
a thread (possibly the current) to perform the

run

operation. Once the

run

method returns, the

Runnable

object
is no longer needed and may be discarded.

Delegated tasks run in the

AccessControlContext

in place when this object was created.

A call to this method will return each outstanding task
exactly once.

Multiple delegated tasks can be run in parallel.

SSLEngine

operations may require the results of
operations that block, or may take an extended period of time to
complete. This method is used to obtain an outstanding

Runnable

operation (task). Each task must be assigned
a thread (possibly the current) to perform the

run

operation. Once the

run

method returns, the

Runnable

object
is no longer needed and may be discarded.

Delegated tasks run in the

AccessControlContext

in place when this object was created.

A call to this method will return each outstanding task
exactly once.

Multiple delegated tasks can be run in parallel.

Delegated tasks run in the

AccessControlContext

in place when this object was created.

A call to this method will return each outstanding task
exactly once.

Multiple delegated tasks can be run in parallel.

A call to this method will return each outstanding task
exactly once.

Multiple delegated tasks can be run in parallel.

Multiple delegated tasks can be run in parallel.

closeInbound

```java
public abstract void closeInbound()
throws
SSLException
```

Signals that no more inbound network data will be sent
to this

SSLEngine

.

If the application initiated the closing process by calling

closeOutbound()

, under some circumstances it is not
required that the initiator wait for the peer's corresponding
close message. (See section 7.2.1 of the TLS specification (

RFC 2246

) for more
information on waiting for closure alerts.) In such cases, this
method need not be called.

But if the application did not initiate the closure process, or
if the circumstances above do not apply, this method should be
called whenever the end of the SSL/TLS/DTLS data stream is reached.
This ensures closure of the inbound side, and checks that the
peer followed the SSL/TLS/DTLS close procedure properly, thus
detecting possible truncation attacks.

This method is idempotent: if the inbound side has already
been closed, this method does not do anything.

wrap()

should be
called to flush any remaining handshake data.

**Throws:** SSLException

- if this engine has not received the proper SSL/TLS/DTLS close
notification message from the peer.
**See Also:** isInboundDone()

,

isOutboundDone()

---

#### closeInbound

public abstract void closeInbound()
throws

SSLException

Signals that no more inbound network data will be sent
to this

SSLEngine

.

If the application initiated the closing process by calling

closeOutbound()

, under some circumstances it is not
required that the initiator wait for the peer's corresponding
close message. (See section 7.2.1 of the TLS specification (

RFC 2246

) for more
information on waiting for closure alerts.) In such cases, this
method need not be called.

But if the application did not initiate the closure process, or
if the circumstances above do not apply, this method should be
called whenever the end of the SSL/TLS/DTLS data stream is reached.
This ensures closure of the inbound side, and checks that the
peer followed the SSL/TLS/DTLS close procedure properly, thus
detecting possible truncation attacks.

This method is idempotent: if the inbound side has already
been closed, this method does not do anything.

wrap()

should be
called to flush any remaining handshake data.

If the application initiated the closing process by calling

closeOutbound()

, under some circumstances it is not
required that the initiator wait for the peer's corresponding
close message. (See section 7.2.1 of the TLS specification (

RFC 2246

) for more
information on waiting for closure alerts.) In such cases, this
method need not be called.

But if the application did not initiate the closure process, or
if the circumstances above do not apply, this method should be
called whenever the end of the SSL/TLS/DTLS data stream is reached.
This ensures closure of the inbound side, and checks that the
peer followed the SSL/TLS/DTLS close procedure properly, thus
detecting possible truncation attacks.

This method is idempotent: if the inbound side has already
been closed, this method does not do anything.

wrap()

should be
called to flush any remaining handshake data.

But if the application did not initiate the closure process, or
if the circumstances above do not apply, this method should be
called whenever the end of the SSL/TLS/DTLS data stream is reached.
This ensures closure of the inbound side, and checks that the
peer followed the SSL/TLS/DTLS close procedure properly, thus
detecting possible truncation attacks.

This method is idempotent: if the inbound side has already
been closed, this method does not do anything.

wrap()

should be
called to flush any remaining handshake data.

This method is idempotent: if the inbound side has already
been closed, this method does not do anything.

wrap()

should be
called to flush any remaining handshake data.

wrap()

should be
called to flush any remaining handshake data.

isInboundDone

```java
public abstract boolean isInboundDone()
```

Returns whether

unwrap(ByteBuffer, ByteBuffer)

will
accept any more inbound data messages.

**Returns:** true if the

SSLEngine

will not
consume anymore network data (and by implication,
will not produce any more application data.)
**See Also:** closeInbound()

---

#### isInboundDone

public abstract boolean isInboundDone()

Returns whether

unwrap(ByteBuffer, ByteBuffer)

will
accept any more inbound data messages.

closeOutbound

```java
public abstract void closeOutbound()
```

Signals that no more outbound application data will be sent
on this

SSLEngine

.

This method is idempotent: if the outbound side has already
been closed, this method does not do anything.

wrap(ByteBuffer, ByteBuffer)

should be
called to flush any remaining handshake data.

**See Also:** isOutboundDone()

---

#### closeOutbound

public abstract void closeOutbound()

Signals that no more outbound application data will be sent
on this

SSLEngine

.

This method is idempotent: if the outbound side has already
been closed, this method does not do anything.

wrap(ByteBuffer, ByteBuffer)

should be
called to flush any remaining handshake data.

This method is idempotent: if the outbound side has already
been closed, this method does not do anything.

wrap(ByteBuffer, ByteBuffer)

should be
called to flush any remaining handshake data.

wrap(ByteBuffer, ByteBuffer)

should be
called to flush any remaining handshake data.

isOutboundDone

```java
public abstract boolean isOutboundDone()
```

Returns whether

wrap(ByteBuffer, ByteBuffer)

will
produce any more outbound data messages.

Note that during the closure phase, a

SSLEngine

may
generate handshake closure data that must be sent to the peer.

wrap()

must be called to generate this data. When
this method returns true, no more outbound data will be created.

**Returns:** true if the

SSLEngine

will not produce
any more network data
**See Also:** closeOutbound()

,

closeInbound()

---

#### isOutboundDone

public abstract boolean isOutboundDone()

Returns whether

wrap(ByteBuffer, ByteBuffer)

will
produce any more outbound data messages.

Note that during the closure phase, a

SSLEngine

may
generate handshake closure data that must be sent to the peer.

wrap()

must be called to generate this data. When
this method returns true, no more outbound data will be created.

Note that during the closure phase, a

SSLEngine

may
generate handshake closure data that must be sent to the peer.

wrap()

must be called to generate this data. When
this method returns true, no more outbound data will be created.

getSupportedCipherSuites

```java
public abstract
String
[] getSupportedCipherSuites()
```

Returns the names of the cipher suites which could be enabled for use
on this engine. Normally, only a subset of these will actually
be enabled by default, since this list may include cipher suites which
do not meet quality of service requirements for those defaults. Such
cipher suites might be useful in specialized applications.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:** an array of cipher suite names
**See Also:** getEnabledCipherSuites()

,

setEnabledCipherSuites(String [])

---

#### getSupportedCipherSuites

public abstract

String

[] getSupportedCipherSuites()

Returns the names of the cipher suites which could be enabled for use
on this engine. Normally, only a subset of these will actually
be enabled by default, since this list may include cipher suites which
do not meet quality of service requirements for those defaults. Such
cipher suites might be useful in specialized applications.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

getEnabledCipherSuites

```java
public abstract
String
[] getEnabledCipherSuites()
```

Returns the names of the SSL cipher suites which are currently
enabled for use on this engine. When an SSLEngine is first
created, all enabled cipher suites support a minimum quality of
service. Thus, in some environments this value might be empty.

Note that even if a suite is enabled, it may never be used. This
can occur if the peer does not support it, or its use is restricted,
or the requisite certificates (and private keys) for the suite are
not available, or an anonymous suite is enabled but authentication
is required.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

**Returns:** an array of cipher suite names
**See Also:** getSupportedCipherSuites()

,

setEnabledCipherSuites(String [])

---

#### getEnabledCipherSuites

public abstract

String

[] getEnabledCipherSuites()

Returns the names of the SSL cipher suites which are currently
enabled for use on this engine. When an SSLEngine is first
created, all enabled cipher suites support a minimum quality of
service. Thus, in some environments this value might be empty.

Note that even if a suite is enabled, it may never be used. This
can occur if the peer does not support it, or its use is restricted,
or the requisite certificates (and private keys) for the suite are
not available, or an anonymous suite is enabled but authentication
is required.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

Note that even if a suite is enabled, it may never be used. This
can occur if the peer does not support it, or its use is restricted,
or the requisite certificates (and private keys) for the suite are
not available, or an anonymous suite is enabled but authentication
is required.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

The returned array includes cipher suites from the list of standard
cipher suite names in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation, and may also
include other cipher suites that the provider supports.

setEnabledCipherSuites

```java
public abstract void setEnabledCipherSuites​(
String
[] suites)
```

Sets the cipher suites enabled for use on this engine.

Each cipher suite in the

suites

parameter must have
been listed by getSupportedCipherSuites(), or the method will
fail. Following a successful call to this method, only suites
listed in the

suites

parameter are enabled for use.

Note that the standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list or might not
use the recommended name for a certain cipher suite.

See

getEnabledCipherSuites()

for more information
on why a specific cipher suite may never be used on a engine.

**Parameters:** suites

- Names of all the cipher suites to enable
**Throws:** IllegalArgumentException

- when one or more of the ciphers
named by the parameter is not supported, or when the
parameter is null.
**See Also:** getSupportedCipherSuites()

,

getEnabledCipherSuites()

---

#### setEnabledCipherSuites

public abstract void setEnabledCipherSuites​(

String

[] suites)

Sets the cipher suites enabled for use on this engine.

Each cipher suite in the

suites

parameter must have
been listed by getSupportedCipherSuites(), or the method will
fail. Following a successful call to this method, only suites
listed in the

suites

parameter are enabled for use.

Note that the standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list or might not
use the recommended name for a certain cipher suite.

See

getEnabledCipherSuites()

for more information
on why a specific cipher suite may never be used on a engine.

Each cipher suite in the

suites

parameter must have
been listed by getSupportedCipherSuites(), or the method will
fail. Following a successful call to this method, only suites
listed in the

suites

parameter are enabled for use.

Note that the standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list or might not
use the recommended name for a certain cipher suite.

See

getEnabledCipherSuites()

for more information
on why a specific cipher suite may never be used on a engine.

Note that the standard list of cipher suite names may be found in the

JSSE Cipher Suite Names

section of the Java Cryptography
Architecture Standard Algorithm Name Documentation. Providers
may support cipher suite names not found in this list or might not
use the recommended name for a certain cipher suite.

See

getEnabledCipherSuites()

for more information
on why a specific cipher suite may never be used on a engine.

See

getEnabledCipherSuites()

for more information
on why a specific cipher suite may never be used on a engine.

getSupportedProtocols

```java
public abstract
String
[] getSupportedProtocols()
```

Returns the names of the protocols which could be enabled for use
with this

SSLEngine

.

**Returns:** an array of protocols supported

---

#### getSupportedProtocols

public abstract

String

[] getSupportedProtocols()

Returns the names of the protocols which could be enabled for use
with this

SSLEngine

.

getEnabledProtocols

```java
public abstract
String
[] getEnabledProtocols()
```

Returns the names of the protocol versions which are currently
enabled for use with this

SSLEngine

.

Note that even if a protocol is enabled, it may never be used.
This can occur if the peer does not support the protocol, or its
use is restricted, or there are no enabled cipher suites supported
by the protocol.

**Returns:** an array of protocols
**See Also:** setEnabledProtocols(String [])

---

#### getEnabledProtocols

public abstract

String

[] getEnabledProtocols()

Returns the names of the protocol versions which are currently
enabled for use with this

SSLEngine

.

Note that even if a protocol is enabled, it may never be used.
This can occur if the peer does not support the protocol, or its
use is restricted, or there are no enabled cipher suites supported
by the protocol.

Note that even if a protocol is enabled, it may never be used.
This can occur if the peer does not support the protocol, or its
use is restricted, or there are no enabled cipher suites supported
by the protocol.

setEnabledProtocols

```java
public abstract void setEnabledProtocols​(
String
[] protocols)
```

Set the protocol versions enabled for use on this engine.

The protocols must have been listed by getSupportedProtocols()
as being supported. Following a successful call to this method,
only protocols listed in the

protocols

parameter
are enabled for use.

**Parameters:** protocols

- Names of all the protocols to enable.
**Throws:** IllegalArgumentException

- when one or more of
the protocols named by the parameter is not supported or
when the protocols parameter is null.
**See Also:** getEnabledProtocols()

---

#### setEnabledProtocols

public abstract void setEnabledProtocols​(

String

[] protocols)

Set the protocol versions enabled for use on this engine.

The protocols must have been listed by getSupportedProtocols()
as being supported. Following a successful call to this method,
only protocols listed in the

protocols

parameter
are enabled for use.

The protocols must have been listed by getSupportedProtocols()
as being supported. Following a successful call to this method,
only protocols listed in the

protocols

parameter
are enabled for use.

getSession

```java
public abstract
SSLSession
getSession()
```

Returns the

SSLSession

in use in this

SSLEngine

.

These can be long lived, and frequently correspond to an entire
login session for some user. The session specifies a particular
cipher suite which is being actively used by all connections in
that session, as well as the identities of the session's client
and server.

Unlike

SSLSocket.getSession()

this method does not block until handshaking is complete.

Until the initial handshake has completed, this method returns
a session object which reports an invalid cipher suite of
"SSL_NULL_WITH_NULL_NULL".

**Returns:** the

SSLSession

for this

SSLEngine
**See Also:** SSLSession

---

#### getSession

public abstract

SSLSession

getSession()

Returns the

SSLSession

in use in this

SSLEngine

.

These can be long lived, and frequently correspond to an entire
login session for some user. The session specifies a particular
cipher suite which is being actively used by all connections in
that session, as well as the identities of the session's client
and server.

Unlike

SSLSocket.getSession()

this method does not block until handshaking is complete.

Until the initial handshake has completed, this method returns
a session object which reports an invalid cipher suite of
"SSL_NULL_WITH_NULL_NULL".

These can be long lived, and frequently correspond to an entire
login session for some user. The session specifies a particular
cipher suite which is being actively used by all connections in
that session, as well as the identities of the session's client
and server.

Unlike

SSLSocket.getSession()

this method does not block until handshaking is complete.

Until the initial handshake has completed, this method returns
a session object which reports an invalid cipher suite of
"SSL_NULL_WITH_NULL_NULL".

Unlike

SSLSocket.getSession()

this method does not block until handshaking is complete.

Until the initial handshake has completed, this method returns
a session object which reports an invalid cipher suite of
"SSL_NULL_WITH_NULL_NULL".

Until the initial handshake has completed, this method returns
a session object which reports an invalid cipher suite of
"SSL_NULL_WITH_NULL_NULL".

getHandshakeSession

```java
public
SSLSession
getHandshakeSession()
```

Returns the

SSLSession

being constructed during a SSL/TLS/DTLS
handshake.

TLS/DTLS protocols may negotiate parameters that are needed when using
an instance of this class, but before the

SSLSession

has
been completely initialized and made available via

getSession

.
For example, the list of valid signature algorithms may restrict
the type of certificates that can be used during TrustManager
decisions, or the maximum TLS/DTLS fragment packet sizes can be
resized to better support the network environment.

This method provides early access to the

SSLSession

being
constructed. Depending on how far the handshake has progressed,
some data may not yet be available for use. For example, if a
remote server will be sending a Certificate chain, but that chain
has yet not been processed, the

getPeerCertificates

method of

SSLSession

will throw a
SSLPeerUnverifiedException. Once that chain has been processed,

getPeerCertificates

will return the proper value.

**Returns:** null if this instance is not currently handshaking, or
if the current handshake has not progressed far enough to
create a basic SSLSession. Otherwise, this method returns the

SSLSession

currently being negotiated.
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation.
**Since:** 1.7
**See Also:** SSLSocket

,

SSLSession

,

ExtendedSSLSession

,

X509ExtendedKeyManager

,

X509ExtendedTrustManager

---

#### getHandshakeSession

public

SSLSession

getHandshakeSession()

Returns the

SSLSession

being constructed during a SSL/TLS/DTLS
handshake.

TLS/DTLS protocols may negotiate parameters that are needed when using
an instance of this class, but before the

SSLSession

has
been completely initialized and made available via

getSession

.
For example, the list of valid signature algorithms may restrict
the type of certificates that can be used during TrustManager
decisions, or the maximum TLS/DTLS fragment packet sizes can be
resized to better support the network environment.

This method provides early access to the

SSLSession

being
constructed. Depending on how far the handshake has progressed,
some data may not yet be available for use. For example, if a
remote server will be sending a Certificate chain, but that chain
has yet not been processed, the

getPeerCertificates

method of

SSLSession

will throw a
SSLPeerUnverifiedException. Once that chain has been processed,

getPeerCertificates

will return the proper value.

TLS/DTLS protocols may negotiate parameters that are needed when using
an instance of this class, but before the

SSLSession

has
been completely initialized and made available via

getSession

.
For example, the list of valid signature algorithms may restrict
the type of certificates that can be used during TrustManager
decisions, or the maximum TLS/DTLS fragment packet sizes can be
resized to better support the network environment.

This method provides early access to the

SSLSession

being
constructed. Depending on how far the handshake has progressed,
some data may not yet be available for use. For example, if a
remote server will be sending a Certificate chain, but that chain
has yet not been processed, the

getPeerCertificates

method of

SSLSession

will throw a
SSLPeerUnverifiedException. Once that chain has been processed,

getPeerCertificates

will return the proper value.

This method provides early access to the

SSLSession

being
constructed. Depending on how far the handshake has progressed,
some data may not yet be available for use. For example, if a
remote server will be sending a Certificate chain, but that chain
has yet not been processed, the

getPeerCertificates

method of

SSLSession

will throw a
SSLPeerUnverifiedException. Once that chain has been processed,

getPeerCertificates

will return the proper value.

beginHandshake

```java
public abstract void beginHandshake()
throws
SSLException
```

Initiates handshaking (initial or renegotiation) on this SSLEngine.

This method is not needed for the initial handshake, as the

wrap()

and

unwrap()

methods will
implicitly call this method if handshaking has not already begun.

Note that the peer may also request a session renegotiation with
this

SSLEngine

by sending the appropriate
session renegotiate handshake message.

Unlike the

SSLSocket#startHandshake()

method, this method does not block
until handshaking is completed.

To force a complete SSL/TLS/DTLS session renegotiation, the current
session should be invalidated prior to calling this method.

Some protocols may not support multiple handshakes on an existing
engine and may throw an

SSLException

.

**Throws:** SSLException

- if a problem was encountered while signaling the

SSLEngine

to begin a new handshake.
See the class description for more information on
engine closure.
**Throws:** IllegalStateException

- if the client/server mode
has not yet been set.
**See Also:** SSLSession.invalidate()

---

#### beginHandshake

public abstract void beginHandshake()
throws

SSLException

Initiates handshaking (initial or renegotiation) on this SSLEngine.

This method is not needed for the initial handshake, as the

wrap()

and

unwrap()

methods will
implicitly call this method if handshaking has not already begun.

Note that the peer may also request a session renegotiation with
this

SSLEngine

by sending the appropriate
session renegotiate handshake message.

Unlike the

SSLSocket#startHandshake()

method, this method does not block
until handshaking is completed.

To force a complete SSL/TLS/DTLS session renegotiation, the current
session should be invalidated prior to calling this method.

Some protocols may not support multiple handshakes on an existing
engine and may throw an

SSLException

.

This method is not needed for the initial handshake, as the

wrap()

and

unwrap()

methods will
implicitly call this method if handshaking has not already begun.

Note that the peer may also request a session renegotiation with
this

SSLEngine

by sending the appropriate
session renegotiate handshake message.

Unlike the

SSLSocket#startHandshake()

method, this method does not block
until handshaking is completed.

To force a complete SSL/TLS/DTLS session renegotiation, the current
session should be invalidated prior to calling this method.

Some protocols may not support multiple handshakes on an existing
engine and may throw an

SSLException

.

Note that the peer may also request a session renegotiation with
this

SSLEngine

by sending the appropriate
session renegotiate handshake message.

Unlike the

SSLSocket#startHandshake()

method, this method does not block
until handshaking is completed.

To force a complete SSL/TLS/DTLS session renegotiation, the current
session should be invalidated prior to calling this method.

Some protocols may not support multiple handshakes on an existing
engine and may throw an

SSLException

.

Unlike the

SSLSocket#startHandshake()

method, this method does not block
until handshaking is completed.

To force a complete SSL/TLS/DTLS session renegotiation, the current
session should be invalidated prior to calling this method.

Some protocols may not support multiple handshakes on an existing
engine and may throw an

SSLException

.

To force a complete SSL/TLS/DTLS session renegotiation, the current
session should be invalidated prior to calling this method.

Some protocols may not support multiple handshakes on an existing
engine and may throw an

SSLException

.

Some protocols may not support multiple handshakes on an existing
engine and may throw an

SSLException

.

getHandshakeStatus

```java
public abstract
SSLEngineResult.HandshakeStatus
getHandshakeStatus()
```

Returns the current handshake status for this

SSLEngine

.

**Returns:** the current

SSLEngineResult.HandshakeStatus

.

---

#### getHandshakeStatus

public abstract

SSLEngineResult.HandshakeStatus

getHandshakeStatus()

Returns the current handshake status for this

SSLEngine

.

setUseClientMode

```java
public abstract void setUseClientMode​(boolean mode)
```

Configures the engine to use client (or server) mode when
handshaking.

This method must be called before any handshaking occurs.
Once handshaking has begun, the mode can not be reset for the
life of this engine.

Servers normally authenticate themselves, and clients
are not required to do so.

**Implementation Note:** The JDK SunJSSE provider implementation default for this mode is false.
**Parameters:** mode

- true if the engine should start its handshaking
in "client" mode
**Throws:** IllegalArgumentException

- if a mode change is attempted
after the initial handshake has begun.
**See Also:** getUseClientMode()

---

#### setUseClientMode

public abstract void setUseClientMode​(boolean mode)

Configures the engine to use client (or server) mode when
handshaking.

This method must be called before any handshaking occurs.
Once handshaking has begun, the mode can not be reset for the
life of this engine.

Servers normally authenticate themselves, and clients
are not required to do so.

This method must be called before any handshaking occurs.
Once handshaking has begun, the mode can not be reset for the
life of this engine.

Servers normally authenticate themselves, and clients
are not required to do so.

Servers normally authenticate themselves, and clients
are not required to do so.

getUseClientMode

```java
public abstract boolean getUseClientMode()
```

Returns true if the engine is set to use client mode when
handshaking.

**Implementation Note:** The JDK SunJSSE provider implementation returns false unless

setUseClientMode(boolean)

is used to change the mode to true.
**Returns:** true if the engine should do handshaking
in "client" mode
**See Also:** setUseClientMode(boolean)

---

#### getUseClientMode

public abstract boolean getUseClientMode()

Returns true if the engine is set to use client mode when
handshaking.

setNeedClientAuth

```java
public abstract void setNeedClientAuth​(boolean need)
```

Configures the engine to

require

client authentication. This
option is only useful for engines in the server mode.

An engine's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setWantClientAuth(boolean)

, if this option is set and
the client chooses not to provide authentication information
about itself,

the negotiations will stop and the engine will
begin its closure procedure

.

Calling this method overrides any previous setting made by
this method or

setWantClientAuth(boolean)

.

**Parameters:** need

- set to true if client authentication is required,
or false if no client authentication is desired.
**See Also:** getNeedClientAuth()

,

setWantClientAuth(boolean)

,

getWantClientAuth()

,

setUseClientMode(boolean)

---

#### setNeedClientAuth

public abstract void setNeedClientAuth​(boolean need)

Configures the engine to

require

client authentication. This
option is only useful for engines in the server mode.

An engine's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setWantClientAuth(boolean)

, if this option is set and
the client chooses not to provide authentication information
about itself,

the negotiations will stop and the engine will
begin its closure procedure

.

Calling this method overrides any previous setting made by
this method or

setWantClientAuth(boolean)

.

An engine's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setWantClientAuth(boolean)

, if this option is set and
the client chooses not to provide authentication information
about itself,

the negotiations will stop and the engine will
begin its closure procedure

.

Calling this method overrides any previous setting made by
this method or

setWantClientAuth(boolean)

.

client authentication required

client authentication requested

no client authentication desired

Unlike

setWantClientAuth(boolean)

, if this option is set and
the client chooses not to provide authentication information
about itself,

the negotiations will stop and the engine will
begin its closure procedure

.

Calling this method overrides any previous setting made by
this method or

setWantClientAuth(boolean)

.

Calling this method overrides any previous setting made by
this method or

setWantClientAuth(boolean)

.

getNeedClientAuth

```java
public abstract boolean getNeedClientAuth()
```

Returns true if the engine will

require

client authentication.
This option is only useful to engines in the server mode.

**Returns:** true if client authentication is required,
or false if no client authentication is desired.
**See Also:** setNeedClientAuth(boolean)

,

setWantClientAuth(boolean)

,

getWantClientAuth()

,

setUseClientMode(boolean)

---

#### getNeedClientAuth

public abstract boolean getNeedClientAuth()

Returns true if the engine will

require

client authentication.
This option is only useful to engines in the server mode.

setWantClientAuth

```java
public abstract void setWantClientAuth​(boolean want)
```

Configures the engine to

request

client authentication.
This option is only useful for engines in the server mode.

An engine's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setNeedClientAuth(boolean)

, if this option is set and
the client chooses not to provide authentication information
about itself,

the negotiations will continue

.

Calling this method overrides any previous setting made by
this method or

setNeedClientAuth(boolean)

.

**Parameters:** want

- set to true if client authentication is requested,
or false if no client authentication is desired.
**See Also:** getWantClientAuth()

,

setNeedClientAuth(boolean)

,

getNeedClientAuth()

,

setUseClientMode(boolean)

---

#### setWantClientAuth

public abstract void setWantClientAuth​(boolean want)

Configures the engine to

request

client authentication.
This option is only useful for engines in the server mode.

An engine's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setNeedClientAuth(boolean)

, if this option is set and
the client chooses not to provide authentication information
about itself,

the negotiations will continue

.

Calling this method overrides any previous setting made by
this method or

setNeedClientAuth(boolean)

.

An engine's client authentication setting is one of the following:

- client authentication required

client authentication requested

no client authentication desired

Unlike

setNeedClientAuth(boolean)

, if this option is set and
the client chooses not to provide authentication information
about itself,

the negotiations will continue

.

Calling this method overrides any previous setting made by
this method or

setNeedClientAuth(boolean)

.

client authentication required

client authentication requested

no client authentication desired

Unlike

setNeedClientAuth(boolean)

, if this option is set and
the client chooses not to provide authentication information
about itself,

the negotiations will continue

.

Calling this method overrides any previous setting made by
this method or

setNeedClientAuth(boolean)

.

Calling this method overrides any previous setting made by
this method or

setNeedClientAuth(boolean)

.

getWantClientAuth

```java
public abstract boolean getWantClientAuth()
```

Returns true if the engine will

request

client authentication.
This option is only useful for engines in the server mode.

**Returns:** true if client authentication is requested,
or false if no client authentication is desired.
**See Also:** setNeedClientAuth(boolean)

,

getNeedClientAuth()

,

setWantClientAuth(boolean)

,

setUseClientMode(boolean)

---

#### getWantClientAuth

public abstract boolean getWantClientAuth()

Returns true if the engine will

request

client authentication.
This option is only useful for engines in the server mode.

setEnableSessionCreation

```java
public abstract void setEnableSessionCreation​(boolean flag)
```

Controls whether new SSL sessions may be established by this engine.
If session creations are not allowed, and there are no
existing sessions to resume, there will be no successful
handshaking.

**Parameters:** flag

- true indicates that sessions may be created; this
is the default. false indicates that an existing session
must be resumed
**See Also:** getEnableSessionCreation()

---

#### setEnableSessionCreation

public abstract void setEnableSessionCreation​(boolean flag)

Controls whether new SSL sessions may be established by this engine.
If session creations are not allowed, and there are no
existing sessions to resume, there will be no successful
handshaking.

getEnableSessionCreation

```java
public abstract boolean getEnableSessionCreation()
```

Returns true if new SSL sessions may be established by this engine.

**Returns:** true indicates that sessions may be created; this
is the default. false indicates that an existing session
must be resumed
**See Also:** setEnableSessionCreation(boolean)

---

#### getEnableSessionCreation

public abstract boolean getEnableSessionCreation()

Returns true if new SSL sessions may be established by this engine.

getSSLParameters

```java
public
SSLParameters
getSSLParameters()
```

Returns the SSLParameters in effect for this SSLEngine.
The ciphersuites and protocols of the returned SSLParameters
are always non-null.

**Returns:** the SSLParameters in effect for this SSLEngine.
**Since:** 1.6

---

#### getSSLParameters

public

SSLParameters

getSSLParameters()

Returns the SSLParameters in effect for this SSLEngine.
The ciphersuites and protocols of the returned SSLParameters
are always non-null.

setSSLParameters

```java
public void setSSLParameters​(
SSLParameters
params)
```

Applies SSLParameters to this engine.

This means:

- If

params.getCipherSuites()

is non-null,

setEnabledCipherSuites()

is called with that value.
- If

params.getProtocols()

is non-null,

setEnabledProtocols()

is called with that value.
- If

params.getNeedClientAuth()

or

params.getWantClientAuth()

return

true

,

setNeedClientAuth(true)

and

setWantClientAuth(true)

are called, respectively;
otherwise

setWantClientAuth(false)

is called.
- If

params.getServerNames()

is non-null, the engine will
configure its server names with that value.
- If

params.getSNIMatchers()

is non-null, the engine will
configure its SNI matchers with that value.

**Parameters:** params

- the parameters
**Throws:** IllegalArgumentException

- if the setEnabledCipherSuites() or
the setEnabledProtocols() call fails
**Since:** 1.6

---

#### setSSLParameters

public void setSSLParameters​(

SSLParameters

params)

Applies SSLParameters to this engine.

This means:

- If

params.getCipherSuites()

is non-null,

setEnabledCipherSuites()

is called with that value.
- If

params.getProtocols()

is non-null,

setEnabledProtocols()

is called with that value.
- If

params.getNeedClientAuth()

or

params.getWantClientAuth()

return

true

,

setNeedClientAuth(true)

and

setWantClientAuth(true)

are called, respectively;
otherwise

setWantClientAuth(false)

is called.
- If

params.getServerNames()

is non-null, the engine will
configure its server names with that value.
- If

params.getSNIMatchers()

is non-null, the engine will
configure its SNI matchers with that value.

This means:

- If

params.getCipherSuites()

is non-null,

setEnabledCipherSuites()

is called with that value.
- If

params.getProtocols()

is non-null,

setEnabledProtocols()

is called with that value.
- If

params.getNeedClientAuth()

or

params.getWantClientAuth()

return

true

,

setNeedClientAuth(true)

and

setWantClientAuth(true)

are called, respectively;
otherwise

setWantClientAuth(false)

is called.
- If

params.getServerNames()

is non-null, the engine will
configure its server names with that value.
- If

params.getSNIMatchers()

is non-null, the engine will
configure its SNI matchers with that value.

If

params.getCipherSuites()

is non-null,

setEnabledCipherSuites()

is called with that value.

If

params.getProtocols()

is non-null,

setEnabledProtocols()

is called with that value.

If

params.getNeedClientAuth()

or

params.getWantClientAuth()

return

true

,

setNeedClientAuth(true)

and

setWantClientAuth(true)

are called, respectively;
otherwise

setWantClientAuth(false)

is called.

If

params.getServerNames()

is non-null, the engine will
configure its server names with that value.

If

params.getSNIMatchers()

is non-null, the engine will
configure its SNI matchers with that value.

getApplicationProtocol

```java
public
String
getApplicationProtocol()
```

Returns the most recent application protocol value negotiated for this
connection.

If supported by the underlying SSL/TLS/DTLS implementation,
application name negotiation mechanisms such as

RFC 7301

, the
Application-Layer Protocol Negotiation (ALPN), can negotiate
application-level values between peers.

**Implementation Requirements:** The implementation in this class throws

UnsupportedOperationException

and performs no other action.
**Returns:** null if it has not yet been determined if application
protocols might be used for this connection, an empty

String

if application protocols values will not
be used, or a non-empty application protocol

String

if a value was successfully negotiated.
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation.
**Since:** 9

---

#### getApplicationProtocol

public

String

getApplicationProtocol()

Returns the most recent application protocol value negotiated for this
connection.

If supported by the underlying SSL/TLS/DTLS implementation,
application name negotiation mechanisms such as

RFC 7301

, the
Application-Layer Protocol Negotiation (ALPN), can negotiate
application-level values between peers.

If supported by the underlying SSL/TLS/DTLS implementation,
application name negotiation mechanisms such as

RFC 7301

, the
Application-Layer Protocol Negotiation (ALPN), can negotiate
application-level values between peers.

getHandshakeApplicationProtocol

```java
public
String
getHandshakeApplicationProtocol()
```

Returns the application protocol value negotiated on a SSL/TLS
handshake currently in progress.

Like

getHandshakeSession()

,
a connection may be in the middle of a handshake. The
application protocol may or may not yet be available.

**Implementation Requirements:** The implementation in this class throws

UnsupportedOperationException

and performs no other action.
**Returns:** null if it has not yet been determined if application
protocols might be used for this handshake, an empty

String

if application protocols values will not
be used, or a non-empty application protocol

String

if a value was successfully negotiated.
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation.
**Since:** 9

---

#### getHandshakeApplicationProtocol

public

String

getHandshakeApplicationProtocol()

Returns the application protocol value negotiated on a SSL/TLS
handshake currently in progress.

Like

getHandshakeSession()

,
a connection may be in the middle of a handshake. The
application protocol may or may not yet be available.

Like

getHandshakeSession()

,
a connection may be in the middle of a handshake. The
application protocol may or may not yet be available.

setHandshakeApplicationProtocolSelector

```java
public void setHandshakeApplicationProtocolSelector​(
BiFunction
<
SSLEngine
,​
List
<
String
>,​
String
> selector)
```

Registers a callback function that selects an application protocol
value for a SSL/TLS/DTLS handshake.
The function overrides any values supplied using

SSLParameters.setApplicationProtocols

and it supports the following
type parameters:

For example, the following call registers a callback function that
examines the TLS handshake parameters and selects an application protocol
name:

```java
serverEngine.setHandshakeApplicationProtocolSelector(
(serverEngine, clientProtocols) -> {
SSLSession session = serverEngine.getHandshakeSession();
return chooseApplicationProtocol(
serverEngine,
clientProtocols,
session.getProtocol(),
session.getCipherSuite());
});
```

**API Note:** This method should be called by TLS server applications before the TLS
handshake begins. Also, this

SSLEngine

should be configured with
parameters that are compatible with the application protocol selected by
the callback function. For example, enabling a poor choice of cipher
suites could result in no suitable application protocol.
See

SSLParameters

.
**Implementation Requirements:** The implementation in this class throws

UnsupportedOperationException

and performs no other action.
**Parameters:** selector

- the callback function, or null to disable the callback
functionality.
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation.
**Since:** 9

---

#### setHandshakeApplicationProtocolSelector

public void setHandshakeApplicationProtocolSelector​(

BiFunction

<

SSLEngine

,​

List

<

String

>,​

String

> selector)

Registers a callback function that selects an application protocol
value for a SSL/TLS/DTLS handshake.
The function overrides any values supplied using

SSLParameters.setApplicationProtocols

and it supports the following
type parameters:

For example, the following call registers a callback function that
examines the TLS handshake parameters and selects an application protocol
name:

```java
serverEngine.setHandshakeApplicationProtocolSelector(
(serverEngine, clientProtocols) -> {
SSLSession session = serverEngine.getHandshakeSession();
return chooseApplicationProtocol(
serverEngine,
clientProtocols,
session.getProtocol(),
session.getCipherSuite());
});
```

serverEngine.setHandshakeApplicationProtocolSelector(
(serverEngine, clientProtocols) -> {
SSLSession session = serverEngine.getHandshakeSession();
return chooseApplicationProtocol(
serverEngine,
clientProtocols,
session.getProtocol(),
session.getCipherSuite());
});

getHandshakeApplicationProtocolSelector

```java
public
BiFunction
<
SSLEngine
,​
List
<
String
>,​
String
> getHandshakeApplicationProtocolSelector()
```

Retrieves the callback function that selects an application protocol
value during a SSL/TLS/DTLS handshake.
See

setHandshakeApplicationProtocolSelector

for the function's type parameters.

**Implementation Requirements:** The implementation in this class throws

UnsupportedOperationException

and performs no other action.
**Returns:** the callback function, or null if none has been set.
**Throws:** UnsupportedOperationException

- if the underlying provider
does not implement the operation.
**Since:** 9

---

#### getHandshakeApplicationProtocolSelector

public

BiFunction

<

SSLEngine

,​

List

<

String

>,​

String

> getHandshakeApplicationProtocolSelector()

Retrieves the callback function that selects an application protocol
value during a SSL/TLS/DTLS handshake.
See

setHandshakeApplicationProtocolSelector

for the function's type parameters.

---

