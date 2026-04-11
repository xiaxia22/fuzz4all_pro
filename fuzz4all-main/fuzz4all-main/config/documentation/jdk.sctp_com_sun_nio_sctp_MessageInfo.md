# Class MessageInfo

**Source:** `jdk.sctp\com\sun\nio\sctp\MessageInfo.html`

### Class Description

```java
public abstract class
MessageInfo

extends
Object
```

The

MessageInfo

class provides additional ancillary information about
messages.

Received SCTP messages, returned by

SctpChannel.receive

and

SctpMultiChannel.receive

,
return a

MessageInfo

instance that can be queried to determine
ancillary information about the received message. Messages being sent should
use one of the

createOutgoing

methods to provide ancillary data for the message being
sent, and may use the appropriate setter methods to override the default
values provided for

unordered

,

timeToLive

,

complete

and

payloadProtocolID

, before sending the message.

For out going messages the

timeToLive

parameter is a time period
that the sending side SCTP stack may expire the message if it has not been
sent. This time period is an indication to the stack that the message is no
longer required to be sent after the time period expires. It is not a hard
timeout and may be influenced by whether the association supports the partial
reliability extension,

RFC 3758

.

MessageInfo

instances are not safe for use by multiple concurrent
threads. If a MessageInfo is to be used by more than one thread then access
to the MessageInfo should be controlled by appropriate synchronization.

**Since:** 1.7

---

### Field Details

*No entries found.*

### Constructor Details

#### protected MessageInfo()

Initializes a new instance of this class.

---

### Method Details

#### public static
MessageInfo
createOutgoing​(
SocketAddress
address,
int streamNumber)

Creates a

MessageInfo

instance suitable for use when
sending a message.

The returned instance will have its

unordered

value set to

false

, its

timeToLive

value
set to

0

, its

complete

value set
to

true

, and its

payloadProtocolID

value set to

0

. These values, if required, can be set through
the appropriate setter method before sending the message.

**Parameters:**
- address

- For a connected

SctpChannel

the address is the
preferred peer address of the association to send the message
to, or

null

to use the peer primary address. For an

SctpMultiChannel

the address is used to determine
the association, or if no association exists with a peer of that
address then one is setup.
- streamNumber

- The stream number that the message will be sent on

**Returns:**
- The outgoing message info

**Throws:**
- IllegalArgumentException

- If the streamNumber is negative or greater than

65536

---

#### public static
MessageInfo
createOutgoing​(
Association
association,

SocketAddress
address,
int streamNumber)

Creates a

MessageInfo

instance suitable for use when
sending a message to a given association. Typically used for

SctpMultiChannel

when an association has already been setup.

The returned instance will have its

unordered

value set to

false

, its

timeToLive

value
set to

0

, its

complete

value set
to

true

, and its

payloadProtocolID

value set to

0

. These values, if required, can be set through
the appropriate setter method before sending the message.

**Parameters:**
- association

- The association to send the message on
- address

- The preferred peer address of the association to send the message
to, or

null

to use the peer primary address
- streamNumber

- The stream number that the message will be sent on.

**Returns:**
- The outgoing message info

**Throws:**
- IllegalArgumentException

- If

association

is

null

, or the streamNumber is
negative or greater than

65536

---

#### public abstract
SocketAddress
address()

Returns the source socket address if the message has been received,
otherwise the preferred destination of the message to be sent.

**Returns:**
- The socket address, or

null

if this instance is to be
used for sending a message and has been construced without
specifying a preferred destination address

---

#### public abstract
Association
association()

Returns the association that the message was received on, if the message
has been received, otherwise the association that the message is to be
sent on.

**Returns:**
- The association, or

null

if this instance is to be
used for sending a message and has been construced using the
the

createOutgoing(SocketAddress,int)

static factory method

---

#### public abstract int bytes()

Returns the number of bytes read for the received message.

This method is only appicable for received messages, it has no
meaning for messages being sent.

**Returns:**
- The number of bytes read,

-1

if the channel is an

SctpChannel

that has reached end-of-stream, otherwise

0

---

#### public abstract boolean isComplete()

Tells whether or not the message is complete.

For received messages

true

indicates that the message was
completely received. For messages being sent

true

indicates that
the message is complete,

false

indicates that the message is not
complete. How the send channel interprets this value depends on the value
of its

SCTP_EXPLICIT_COMPLETE

socket option.

**Returns:**
- true

if, and only if, the message is complete

---

#### public abstract
MessageInfo
complete​(boolean complete)

Sets whether or not the message is complete.

For messages being sent

true

indicates that
the message is complete,

false

indicates that the message is not
complete. How the send channel interprets this value depends on the value
of its

SCTP_EXPLICIT_COMPLETE

socket option.

**Parameters:**
- complete

-

true

if, and only if, the message is complete

**Returns:**
- This MessageInfo

**See Also:**
- isComplete()

---

#### public abstract boolean isUnordered()

Tells whether or not the message is unordered. For received messages

true

indicates that the message was sent non-ordered. For
messages being sent

true

requests the un-ordered delivery of the
message,

false

indicates that the message is ordered.

**Returns:**
- true

if the message is unordered, otherwise

false

---

#### public abstract
MessageInfo
unordered​(boolean unordered)

Sets whether or not the message is unordered.

**Parameters:**
- unordered

-

true

requests the un-ordered delivery of the message,

false

indicates that the message is ordered.

**Returns:**
- This MessageInfo

**See Also:**
- isUnordered()

---

#### public abstract int payloadProtocolID()

Returns the payload protocol Identifier.

A value indicating the type of payload protocol data being
transmitted/received. This value is passed as opaque data by SCTP.

0

indicates an unspecified payload protocol identifier.

**Returns:**
- The Payload Protocol Identifier

---

#### public abstract
MessageInfo
payloadProtocolID​(int ppid)

Sets the payload protocol Identifier.

A value indicating the type of payload protocol data being
transmitted. This value is passed as opaque data by SCTP.

**Parameters:**
- ppid

- The Payload Protocol Identifier, or

0

indicate an
unspecified payload protocol identifier.

**Returns:**
- This MessageInfo

**See Also:**
- payloadProtocolID()

---

#### public abstract int streamNumber()

Returns the stream number that the message was received on, if the
message has been received, otherwise the stream number that the message
is to be sent on.

**Returns:**
- The stream number

---

#### public abstract
MessageInfo
streamNumber​(int streamNumber)

Sets the stream number that the message is to be sent on.

**Parameters:**
- streamNumber

- The stream number

**Returns:**
- This MessageInfo

**Throws:**
- IllegalArgumentException

- If the streamNumber is negative or greater than

65536

---

#### public abstract long timeToLive()

The time period that the sending side may expire the message if it has
not been sent, or

0

to indicate that no timeout should occur. This
value is only applicable for messages being sent, it has no meaning for
received messages.

**Returns:**
- The time period in milliseconds, or

0

---

#### public abstract
MessageInfo
timeToLive​(long millis)

Sets the time period that the sending side may expire the message if it
has not been sent.

**Parameters:**
- millis

- The time period in milliseconds, or

0

to indicate that no
timeout should occur

**Returns:**
- This MessageInfo

**See Also:**
- timeToLive()

---

### Additional Sections

#### Class MessageInfo

java.lang.Object

- com.sun.nio.sctp.MessageInfo

com.sun.nio.sctp.MessageInfo

```java
public abstract class
MessageInfo

extends
Object
```

The

MessageInfo

class provides additional ancillary information about
messages.

Received SCTP messages, returned by

SctpChannel.receive

and

SctpMultiChannel.receive

,
return a

MessageInfo

instance that can be queried to determine
ancillary information about the received message. Messages being sent should
use one of the

createOutgoing

methods to provide ancillary data for the message being
sent, and may use the appropriate setter methods to override the default
values provided for

unordered

,

timeToLive

,

complete

and

payloadProtocolID

, before sending the message.

For out going messages the

timeToLive

parameter is a time period
that the sending side SCTP stack may expire the message if it has not been
sent. This time period is an indication to the stack that the message is no
longer required to be sent after the time period expires. It is not a hard
timeout and may be influenced by whether the association supports the partial
reliability extension,

RFC 3758

.

MessageInfo

instances are not safe for use by multiple concurrent
threads. If a MessageInfo is to be used by more than one thread then access
to the MessageInfo should be controlled by appropriate synchronization.

**Since:** 1.7

public abstract class

MessageInfo

extends

Object

The

MessageInfo

class provides additional ancillary information about
messages.

Received SCTP messages, returned by

SctpChannel.receive

and

SctpMultiChannel.receive

,
return a

MessageInfo

instance that can be queried to determine
ancillary information about the received message. Messages being sent should
use one of the

createOutgoing

methods to provide ancillary data for the message being
sent, and may use the appropriate setter methods to override the default
values provided for

unordered

,

timeToLive

,

complete

and

payloadProtocolID

, before sending the message.

For out going messages the

timeToLive

parameter is a time period
that the sending side SCTP stack may expire the message if it has not been
sent. This time period is an indication to the stack that the message is no
longer required to be sent after the time period expires. It is not a hard
timeout and may be influenced by whether the association supports the partial
reliability extension,

RFC 3758

.

MessageInfo

instances are not safe for use by multiple concurrent
threads. If a MessageInfo is to be used by more than one thread then access
to the MessageInfo should be controlled by appropriate synchronization.

Received SCTP messages, returned by

SctpChannel.receive

and

SctpMultiChannel.receive

,
return a

MessageInfo

instance that can be queried to determine
ancillary information about the received message. Messages being sent should
use one of the

createOutgoing

methods to provide ancillary data for the message being
sent, and may use the appropriate setter methods to override the default
values provided for

unordered

,

timeToLive

,

complete

and

payloadProtocolID

, before sending the message.

For out going messages the

timeToLive

parameter is a time period
that the sending side SCTP stack may expire the message if it has not been
sent. This time period is an indication to the stack that the message is no
longer required to be sent after the time period expires. It is not a hard
timeout and may be influenced by whether the association supports the partial
reliability extension,

RFC 3758

.

MessageInfo

instances are not safe for use by multiple concurrent
threads. If a MessageInfo is to be used by more than one thread then access
to the MessageInfo should be controlled by appropriate synchronization.

For out going messages the

timeToLive

parameter is a time period
that the sending side SCTP stack may expire the message if it has not been
sent. This time period is an indication to the stack that the message is no
longer required to be sent after the time period expires. It is not a hard
timeout and may be influenced by whether the association supports the partial
reliability extension,

RFC 3758

.

MessageInfo

instances are not safe for use by multiple concurrent
threads. If a MessageInfo is to be used by more than one thread then access
to the MessageInfo should be controlled by appropriate synchronization.

MessageInfo

instances are not safe for use by multiple concurrent
threads. If a MessageInfo is to be used by more than one thread then access
to the MessageInfo should be controlled by appropriate synchronization.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

MessageInfo

()

Initializes a new instance of this class.

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

abstract

SocketAddress

address

()

Returns the source socket address if the message has been received,
otherwise the preferred destination of the message to be sent.

abstract

Association

association

()

Returns the association that the message was received on, if the message
has been received, otherwise the association that the message is to be
sent on.

abstract int

bytes

()

Returns the number of bytes read for the received message.

abstract

MessageInfo

complete

​(boolean complete)

Sets whether or not the message is complete.

static

MessageInfo

createOutgoing

​(

Association

association,

SocketAddress

address,
int streamNumber)

Creates a

MessageInfo

instance suitable for use when
sending a message to a given association.

static

MessageInfo

createOutgoing

​(

SocketAddress

address,
int streamNumber)

Creates a

MessageInfo

instance suitable for use when
sending a message.

abstract boolean

isComplete

()

Tells whether or not the message is complete.

abstract boolean

isUnordered

()

Tells whether or not the message is unordered.

abstract int

payloadProtocolID

()

Returns the payload protocol Identifier.

abstract

MessageInfo

payloadProtocolID

​(int ppid)

Sets the payload protocol Identifier.

abstract int

streamNumber

()

Returns the stream number that the message was received on, if the
message has been received, otherwise the stream number that the message
is to be sent on.

abstract

MessageInfo

streamNumber

​(int streamNumber)

Sets the stream number that the message is to be sent on.

abstract long

timeToLive

()

The time period that the sending side may expire the message if it has
not been sent, or

0

to indicate that no timeout should occur.

abstract

MessageInfo

timeToLive

​(long millis)

Sets the time period that the sending side may expire the message if it
has not been sent.

abstract

MessageInfo

unordered

​(boolean unordered)

Sets whether or not the message is unordered.

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

MessageInfo

()

Initializes a new instance of this class.

---

#### Constructor Summary

Initializes a new instance of this class.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

abstract

SocketAddress

address

()

Returns the source socket address if the message has been received,
otherwise the preferred destination of the message to be sent.

abstract

Association

association

()

Returns the association that the message was received on, if the message
has been received, otherwise the association that the message is to be
sent on.

abstract int

bytes

()

Returns the number of bytes read for the received message.

abstract

MessageInfo

complete

​(boolean complete)

Sets whether or not the message is complete.

static

MessageInfo

createOutgoing

​(

Association

association,

SocketAddress

address,
int streamNumber)

Creates a

MessageInfo

instance suitable for use when
sending a message to a given association.

static

MessageInfo

createOutgoing

​(

SocketAddress

address,
int streamNumber)

Creates a

MessageInfo

instance suitable for use when
sending a message.

abstract boolean

isComplete

()

Tells whether or not the message is complete.

abstract boolean

isUnordered

()

Tells whether or not the message is unordered.

abstract int

payloadProtocolID

()

Returns the payload protocol Identifier.

abstract

MessageInfo

payloadProtocolID

​(int ppid)

Sets the payload protocol Identifier.

abstract int

streamNumber

()

Returns the stream number that the message was received on, if the
message has been received, otherwise the stream number that the message
is to be sent on.

abstract

MessageInfo

streamNumber

​(int streamNumber)

Sets the stream number that the message is to be sent on.

abstract long

timeToLive

()

The time period that the sending side may expire the message if it has
not been sent, or

0

to indicate that no timeout should occur.

abstract

MessageInfo

timeToLive

​(long millis)

Sets the time period that the sending side may expire the message if it
has not been sent.

abstract

MessageInfo

unordered

​(boolean unordered)

Sets whether or not the message is unordered.

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

Returns the source socket address if the message has been received,
otherwise the preferred destination of the message to be sent.

Returns the association that the message was received on, if the message
has been received, otherwise the association that the message is to be
sent on.

Returns the number of bytes read for the received message.

Sets whether or not the message is complete.

Creates a

MessageInfo

instance suitable for use when
sending a message to a given association.

Creates a

MessageInfo

instance suitable for use when
sending a message.

Tells whether or not the message is complete.

Tells whether or not the message is unordered.

Returns the payload protocol Identifier.

Sets the payload protocol Identifier.

Returns the stream number that the message was received on, if the
message has been received, otherwise the stream number that the message
is to be sent on.

Sets the stream number that the message is to be sent on.

The time period that the sending side may expire the message if it has
not been sent, or

0

to indicate that no timeout should occur.

Sets the time period that the sending side may expire the message if it
has not been sent.

Sets whether or not the message is unordered.

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

- MessageInfo

```java
protected MessageInfo()
```

Initializes a new instance of this class.

============ METHOD DETAIL ==========

- Method Detail

- createOutgoing

```java
public static
MessageInfo
createOutgoing​(
SocketAddress
address,
int streamNumber)
```

Creates a

MessageInfo

instance suitable for use when
sending a message.

The returned instance will have its

unordered

value set to

false

, its

timeToLive

value
set to

0

, its

complete

value set
to

true

, and its

payloadProtocolID

value set to

0

. These values, if required, can be set through
the appropriate setter method before sending the message.

**Parameters:** address

- For a connected

SctpChannel

the address is the
preferred peer address of the association to send the message
to, or

null

to use the peer primary address. For an

SctpMultiChannel

the address is used to determine
the association, or if no association exists with a peer of that
address then one is setup.
**Parameters:** streamNumber

- The stream number that the message will be sent on
**Returns:** The outgoing message info
**Throws:** IllegalArgumentException

- If the streamNumber is negative or greater than

65536

- createOutgoing

```java
public static
MessageInfo
createOutgoing​(
Association
association,

SocketAddress
address,
int streamNumber)
```

Creates a

MessageInfo

instance suitable for use when
sending a message to a given association. Typically used for

SctpMultiChannel

when an association has already been setup.

The returned instance will have its

unordered

value set to

false

, its

timeToLive

value
set to

0

, its

complete

value set
to

true

, and its

payloadProtocolID

value set to

0

. These values, if required, can be set through
the appropriate setter method before sending the message.

**Parameters:** association

- The association to send the message on
**Parameters:** address

- The preferred peer address of the association to send the message
to, or

null

to use the peer primary address
**Parameters:** streamNumber

- The stream number that the message will be sent on.
**Returns:** The outgoing message info
**Throws:** IllegalArgumentException

- If

association

is

null

, or the streamNumber is
negative or greater than

65536

- address

```java
public abstract
SocketAddress
address()
```

Returns the source socket address if the message has been received,
otherwise the preferred destination of the message to be sent.

**Returns:** The socket address, or

null

if this instance is to be
used for sending a message and has been construced without
specifying a preferred destination address

- association

```java
public abstract
Association
association()
```

Returns the association that the message was received on, if the message
has been received, otherwise the association that the message is to be
sent on.

**Returns:** The association, or

null

if this instance is to be
used for sending a message and has been construced using the
the

createOutgoing(SocketAddress,int)

static factory method

- bytes

```java
public abstract int bytes()
```

Returns the number of bytes read for the received message.

This method is only appicable for received messages, it has no
meaning for messages being sent.

**Returns:** The number of bytes read,

-1

if the channel is an

SctpChannel

that has reached end-of-stream, otherwise

0

- isComplete

```java
public abstract boolean isComplete()
```

Tells whether or not the message is complete.

For received messages

true

indicates that the message was
completely received. For messages being sent

true

indicates that
the message is complete,

false

indicates that the message is not
complete. How the send channel interprets this value depends on the value
of its

SCTP_EXPLICIT_COMPLETE

socket option.

**Returns:** true

if, and only if, the message is complete

- complete

```java
public abstract
MessageInfo
complete​(boolean complete)
```

Sets whether or not the message is complete.

For messages being sent

true

indicates that
the message is complete,

false

indicates that the message is not
complete. How the send channel interprets this value depends on the value
of its

SCTP_EXPLICIT_COMPLETE

socket option.

**Parameters:** complete

-

true

if, and only if, the message is complete
**Returns:** This MessageInfo
**See Also:** isComplete()

- isUnordered

```java
public abstract boolean isUnordered()
```

Tells whether or not the message is unordered. For received messages

true

indicates that the message was sent non-ordered. For
messages being sent

true

requests the un-ordered delivery of the
message,

false

indicates that the message is ordered.

**Returns:** true

if the message is unordered, otherwise

false

- unordered

```java
public abstract
MessageInfo
unordered​(boolean unordered)
```

Sets whether or not the message is unordered.

**Parameters:** unordered

-

true

requests the un-ordered delivery of the message,

false

indicates that the message is ordered.
**Returns:** This MessageInfo
**See Also:** isUnordered()

- payloadProtocolID

```java
public abstract int payloadProtocolID()
```

Returns the payload protocol Identifier.

A value indicating the type of payload protocol data being
transmitted/received. This value is passed as opaque data by SCTP.

0

indicates an unspecified payload protocol identifier.

**Returns:** The Payload Protocol Identifier

- payloadProtocolID

```java
public abstract
MessageInfo
payloadProtocolID​(int ppid)
```

Sets the payload protocol Identifier.

A value indicating the type of payload protocol data being
transmitted. This value is passed as opaque data by SCTP.

**Parameters:** ppid

- The Payload Protocol Identifier, or

0

indicate an
unspecified payload protocol identifier.
**Returns:** This MessageInfo
**See Also:** payloadProtocolID()

- streamNumber

```java
public abstract int streamNumber()
```

Returns the stream number that the message was received on, if the
message has been received, otherwise the stream number that the message
is to be sent on.

**Returns:** The stream number

- streamNumber

```java
public abstract
MessageInfo
streamNumber​(int streamNumber)
```

Sets the stream number that the message is to be sent on.

**Parameters:** streamNumber

- The stream number
**Returns:** This MessageInfo
**Throws:** IllegalArgumentException

- If the streamNumber is negative or greater than

65536

- timeToLive

```java
public abstract long timeToLive()
```

The time period that the sending side may expire the message if it has
not been sent, or

0

to indicate that no timeout should occur. This
value is only applicable for messages being sent, it has no meaning for
received messages.

**Returns:** The time period in milliseconds, or

0

- timeToLive

```java
public abstract
MessageInfo
timeToLive​(long millis)
```

Sets the time period that the sending side may expire the message if it
has not been sent.

**Parameters:** millis

- The time period in milliseconds, or

0

to indicate that no
timeout should occur
**Returns:** This MessageInfo
**See Also:** timeToLive()

Constructor Detail

- MessageInfo

```java
protected MessageInfo()
```

Initializes a new instance of this class.

---

#### Constructor Detail

MessageInfo

```java
protected MessageInfo()
```

Initializes a new instance of this class.

---

#### MessageInfo

protected MessageInfo()

Initializes a new instance of this class.

Method Detail

- createOutgoing

```java
public static
MessageInfo
createOutgoing​(
SocketAddress
address,
int streamNumber)
```

Creates a

MessageInfo

instance suitable for use when
sending a message.

The returned instance will have its

unordered

value set to

false

, its

timeToLive

value
set to

0

, its

complete

value set
to

true

, and its

payloadProtocolID

value set to

0

. These values, if required, can be set through
the appropriate setter method before sending the message.

**Parameters:** address

- For a connected

SctpChannel

the address is the
preferred peer address of the association to send the message
to, or

null

to use the peer primary address. For an

SctpMultiChannel

the address is used to determine
the association, or if no association exists with a peer of that
address then one is setup.
**Parameters:** streamNumber

- The stream number that the message will be sent on
**Returns:** The outgoing message info
**Throws:** IllegalArgumentException

- If the streamNumber is negative or greater than

65536

- createOutgoing

```java
public static
MessageInfo
createOutgoing​(
Association
association,

SocketAddress
address,
int streamNumber)
```

Creates a

MessageInfo

instance suitable for use when
sending a message to a given association. Typically used for

SctpMultiChannel

when an association has already been setup.

The returned instance will have its

unordered

value set to

false

, its

timeToLive

value
set to

0

, its

complete

value set
to

true

, and its

payloadProtocolID

value set to

0

. These values, if required, can be set through
the appropriate setter method before sending the message.

**Parameters:** association

- The association to send the message on
**Parameters:** address

- The preferred peer address of the association to send the message
to, or

null

to use the peer primary address
**Parameters:** streamNumber

- The stream number that the message will be sent on.
**Returns:** The outgoing message info
**Throws:** IllegalArgumentException

- If

association

is

null

, or the streamNumber is
negative or greater than

65536

- address

```java
public abstract
SocketAddress
address()
```

Returns the source socket address if the message has been received,
otherwise the preferred destination of the message to be sent.

**Returns:** The socket address, or

null

if this instance is to be
used for sending a message and has been construced without
specifying a preferred destination address

- association

```java
public abstract
Association
association()
```

Returns the association that the message was received on, if the message
has been received, otherwise the association that the message is to be
sent on.

**Returns:** The association, or

null

if this instance is to be
used for sending a message and has been construced using the
the

createOutgoing(SocketAddress,int)

static factory method

- bytes

```java
public abstract int bytes()
```

Returns the number of bytes read for the received message.

This method is only appicable for received messages, it has no
meaning for messages being sent.

**Returns:** The number of bytes read,

-1

if the channel is an

SctpChannel

that has reached end-of-stream, otherwise

0

- isComplete

```java
public abstract boolean isComplete()
```

Tells whether or not the message is complete.

For received messages

true

indicates that the message was
completely received. For messages being sent

true

indicates that
the message is complete,

false

indicates that the message is not
complete. How the send channel interprets this value depends on the value
of its

SCTP_EXPLICIT_COMPLETE

socket option.

**Returns:** true

if, and only if, the message is complete

- complete

```java
public abstract
MessageInfo
complete​(boolean complete)
```

Sets whether or not the message is complete.

For messages being sent

true

indicates that
the message is complete,

false

indicates that the message is not
complete. How the send channel interprets this value depends on the value
of its

SCTP_EXPLICIT_COMPLETE

socket option.

**Parameters:** complete

-

true

if, and only if, the message is complete
**Returns:** This MessageInfo
**See Also:** isComplete()

- isUnordered

```java
public abstract boolean isUnordered()
```

Tells whether or not the message is unordered. For received messages

true

indicates that the message was sent non-ordered. For
messages being sent

true

requests the un-ordered delivery of the
message,

false

indicates that the message is ordered.

**Returns:** true

if the message is unordered, otherwise

false

- unordered

```java
public abstract
MessageInfo
unordered​(boolean unordered)
```

Sets whether or not the message is unordered.

**Parameters:** unordered

-

true

requests the un-ordered delivery of the message,

false

indicates that the message is ordered.
**Returns:** This MessageInfo
**See Also:** isUnordered()

- payloadProtocolID

```java
public abstract int payloadProtocolID()
```

Returns the payload protocol Identifier.

A value indicating the type of payload protocol data being
transmitted/received. This value is passed as opaque data by SCTP.

0

indicates an unspecified payload protocol identifier.

**Returns:** The Payload Protocol Identifier

- payloadProtocolID

```java
public abstract
MessageInfo
payloadProtocolID​(int ppid)
```

Sets the payload protocol Identifier.

A value indicating the type of payload protocol data being
transmitted. This value is passed as opaque data by SCTP.

**Parameters:** ppid

- The Payload Protocol Identifier, or

0

indicate an
unspecified payload protocol identifier.
**Returns:** This MessageInfo
**See Also:** payloadProtocolID()

- streamNumber

```java
public abstract int streamNumber()
```

Returns the stream number that the message was received on, if the
message has been received, otherwise the stream number that the message
is to be sent on.

**Returns:** The stream number

- streamNumber

```java
public abstract
MessageInfo
streamNumber​(int streamNumber)
```

Sets the stream number that the message is to be sent on.

**Parameters:** streamNumber

- The stream number
**Returns:** This MessageInfo
**Throws:** IllegalArgumentException

- If the streamNumber is negative or greater than

65536

- timeToLive

```java
public abstract long timeToLive()
```

The time period that the sending side may expire the message if it has
not been sent, or

0

to indicate that no timeout should occur. This
value is only applicable for messages being sent, it has no meaning for
received messages.

**Returns:** The time period in milliseconds, or

0

- timeToLive

```java
public abstract
MessageInfo
timeToLive​(long millis)
```

Sets the time period that the sending side may expire the message if it
has not been sent.

**Parameters:** millis

- The time period in milliseconds, or

0

to indicate that no
timeout should occur
**Returns:** This MessageInfo
**See Also:** timeToLive()

---

#### Method Detail

createOutgoing

```java
public static
MessageInfo
createOutgoing​(
SocketAddress
address,
int streamNumber)
```

Creates a

MessageInfo

instance suitable for use when
sending a message.

The returned instance will have its

unordered

value set to

false

, its

timeToLive

value
set to

0

, its

complete

value set
to

true

, and its

payloadProtocolID

value set to

0

. These values, if required, can be set through
the appropriate setter method before sending the message.

**Parameters:** address

- For a connected

SctpChannel

the address is the
preferred peer address of the association to send the message
to, or

null

to use the peer primary address. For an

SctpMultiChannel

the address is used to determine
the association, or if no association exists with a peer of that
address then one is setup.
**Parameters:** streamNumber

- The stream number that the message will be sent on
**Returns:** The outgoing message info
**Throws:** IllegalArgumentException

- If the streamNumber is negative or greater than

65536

---

#### createOutgoing

public static

MessageInfo

createOutgoing​(

SocketAddress

address,
int streamNumber)

Creates a

MessageInfo

instance suitable for use when
sending a message.

The returned instance will have its

unordered

value set to

false

, its

timeToLive

value
set to

0

, its

complete

value set
to

true

, and its

payloadProtocolID

value set to

0

. These values, if required, can be set through
the appropriate setter method before sending the message.

The returned instance will have its

unordered

value set to

false

, its

timeToLive

value
set to

0

, its

complete

value set
to

true

, and its

payloadProtocolID

value set to

0

. These values, if required, can be set through
the appropriate setter method before sending the message.

createOutgoing

```java
public static
MessageInfo
createOutgoing​(
Association
association,

SocketAddress
address,
int streamNumber)
```

Creates a

MessageInfo

instance suitable for use when
sending a message to a given association. Typically used for

SctpMultiChannel

when an association has already been setup.

The returned instance will have its

unordered

value set to

false

, its

timeToLive

value
set to

0

, its

complete

value set
to

true

, and its

payloadProtocolID

value set to

0

. These values, if required, can be set through
the appropriate setter method before sending the message.

**Parameters:** association

- The association to send the message on
**Parameters:** address

- The preferred peer address of the association to send the message
to, or

null

to use the peer primary address
**Parameters:** streamNumber

- The stream number that the message will be sent on.
**Returns:** The outgoing message info
**Throws:** IllegalArgumentException

- If

association

is

null

, or the streamNumber is
negative or greater than

65536

---

#### createOutgoing

public static

MessageInfo

createOutgoing​(

Association

association,

SocketAddress

address,
int streamNumber)

Creates a

MessageInfo

instance suitable for use when
sending a message to a given association. Typically used for

SctpMultiChannel

when an association has already been setup.

The returned instance will have its

unordered

value set to

false

, its

timeToLive

value
set to

0

, its

complete

value set
to

true

, and its

payloadProtocolID

value set to

0

. These values, if required, can be set through
the appropriate setter method before sending the message.

The returned instance will have its

unordered

value set to

false

, its

timeToLive

value
set to

0

, its

complete

value set
to

true

, and its

payloadProtocolID

value set to

0

. These values, if required, can be set through
the appropriate setter method before sending the message.

address

```java
public abstract
SocketAddress
address()
```

Returns the source socket address if the message has been received,
otherwise the preferred destination of the message to be sent.

**Returns:** The socket address, or

null

if this instance is to be
used for sending a message and has been construced without
specifying a preferred destination address

---

#### address

public abstract

SocketAddress

address()

Returns the source socket address if the message has been received,
otherwise the preferred destination of the message to be sent.

association

```java
public abstract
Association
association()
```

Returns the association that the message was received on, if the message
has been received, otherwise the association that the message is to be
sent on.

**Returns:** The association, or

null

if this instance is to be
used for sending a message and has been construced using the
the

createOutgoing(SocketAddress,int)

static factory method

---

#### association

public abstract

Association

association()

Returns the association that the message was received on, if the message
has been received, otherwise the association that the message is to be
sent on.

bytes

```java
public abstract int bytes()
```

Returns the number of bytes read for the received message.

This method is only appicable for received messages, it has no
meaning for messages being sent.

**Returns:** The number of bytes read,

-1

if the channel is an

SctpChannel

that has reached end-of-stream, otherwise

0

---

#### bytes

public abstract int bytes()

Returns the number of bytes read for the received message.

This method is only appicable for received messages, it has no
meaning for messages being sent.

This method is only appicable for received messages, it has no
meaning for messages being sent.

isComplete

```java
public abstract boolean isComplete()
```

Tells whether or not the message is complete.

For received messages

true

indicates that the message was
completely received. For messages being sent

true

indicates that
the message is complete,

false

indicates that the message is not
complete. How the send channel interprets this value depends on the value
of its

SCTP_EXPLICIT_COMPLETE

socket option.

**Returns:** true

if, and only if, the message is complete

---

#### isComplete

public abstract boolean isComplete()

Tells whether or not the message is complete.

For received messages

true

indicates that the message was
completely received. For messages being sent

true

indicates that
the message is complete,

false

indicates that the message is not
complete. How the send channel interprets this value depends on the value
of its

SCTP_EXPLICIT_COMPLETE

socket option.

For received messages

true

indicates that the message was
completely received. For messages being sent

true

indicates that
the message is complete,

false

indicates that the message is not
complete. How the send channel interprets this value depends on the value
of its

SCTP_EXPLICIT_COMPLETE

socket option.

complete

```java
public abstract
MessageInfo
complete​(boolean complete)
```

Sets whether or not the message is complete.

For messages being sent

true

indicates that
the message is complete,

false

indicates that the message is not
complete. How the send channel interprets this value depends on the value
of its

SCTP_EXPLICIT_COMPLETE

socket option.

**Parameters:** complete

-

true

if, and only if, the message is complete
**Returns:** This MessageInfo
**See Also:** isComplete()

---

#### complete

public abstract

MessageInfo

complete​(boolean complete)

Sets whether or not the message is complete.

For messages being sent

true

indicates that
the message is complete,

false

indicates that the message is not
complete. How the send channel interprets this value depends on the value
of its

SCTP_EXPLICIT_COMPLETE

socket option.

For messages being sent

true

indicates that
the message is complete,

false

indicates that the message is not
complete. How the send channel interprets this value depends on the value
of its

SCTP_EXPLICIT_COMPLETE

socket option.

isUnordered

```java
public abstract boolean isUnordered()
```

Tells whether or not the message is unordered. For received messages

true

indicates that the message was sent non-ordered. For
messages being sent

true

requests the un-ordered delivery of the
message,

false

indicates that the message is ordered.

**Returns:** true

if the message is unordered, otherwise

false

---

#### isUnordered

public abstract boolean isUnordered()

Tells whether or not the message is unordered. For received messages

true

indicates that the message was sent non-ordered. For
messages being sent

true

requests the un-ordered delivery of the
message,

false

indicates that the message is ordered.

unordered

```java
public abstract
MessageInfo
unordered​(boolean unordered)
```

Sets whether or not the message is unordered.

**Parameters:** unordered

-

true

requests the un-ordered delivery of the message,

false

indicates that the message is ordered.
**Returns:** This MessageInfo
**See Also:** isUnordered()

---

#### unordered

public abstract

MessageInfo

unordered​(boolean unordered)

Sets whether or not the message is unordered.

payloadProtocolID

```java
public abstract int payloadProtocolID()
```

Returns the payload protocol Identifier.

A value indicating the type of payload protocol data being
transmitted/received. This value is passed as opaque data by SCTP.

0

indicates an unspecified payload protocol identifier.

**Returns:** The Payload Protocol Identifier

---

#### payloadProtocolID

public abstract int payloadProtocolID()

Returns the payload protocol Identifier.

A value indicating the type of payload protocol data being
transmitted/received. This value is passed as opaque data by SCTP.

0

indicates an unspecified payload protocol identifier.

A value indicating the type of payload protocol data being
transmitted/received. This value is passed as opaque data by SCTP.

0

indicates an unspecified payload protocol identifier.

payloadProtocolID

```java
public abstract
MessageInfo
payloadProtocolID​(int ppid)
```

Sets the payload protocol Identifier.

A value indicating the type of payload protocol data being
transmitted. This value is passed as opaque data by SCTP.

**Parameters:** ppid

- The Payload Protocol Identifier, or

0

indicate an
unspecified payload protocol identifier.
**Returns:** This MessageInfo
**See Also:** payloadProtocolID()

---

#### payloadProtocolID

public abstract

MessageInfo

payloadProtocolID​(int ppid)

Sets the payload protocol Identifier.

A value indicating the type of payload protocol data being
transmitted. This value is passed as opaque data by SCTP.

A value indicating the type of payload protocol data being
transmitted. This value is passed as opaque data by SCTP.

streamNumber

```java
public abstract int streamNumber()
```

Returns the stream number that the message was received on, if the
message has been received, otherwise the stream number that the message
is to be sent on.

**Returns:** The stream number

---

#### streamNumber

public abstract int streamNumber()

Returns the stream number that the message was received on, if the
message has been received, otherwise the stream number that the message
is to be sent on.

streamNumber

```java
public abstract
MessageInfo
streamNumber​(int streamNumber)
```

Sets the stream number that the message is to be sent on.

**Parameters:** streamNumber

- The stream number
**Returns:** This MessageInfo
**Throws:** IllegalArgumentException

- If the streamNumber is negative or greater than

65536

---

#### streamNumber

public abstract

MessageInfo

streamNumber​(int streamNumber)

Sets the stream number that the message is to be sent on.

timeToLive

```java
public abstract long timeToLive()
```

The time period that the sending side may expire the message if it has
not been sent, or

0

to indicate that no timeout should occur. This
value is only applicable for messages being sent, it has no meaning for
received messages.

**Returns:** The time period in milliseconds, or

0

---

#### timeToLive

public abstract long timeToLive()

The time period that the sending side may expire the message if it has
not been sent, or

0

to indicate that no timeout should occur. This
value is only applicable for messages being sent, it has no meaning for
received messages.

timeToLive

```java
public abstract
MessageInfo
timeToLive​(long millis)
```

Sets the time period that the sending side may expire the message if it
has not been sent.

**Parameters:** millis

- The time period in milliseconds, or

0

to indicate that no
timeout should occur
**Returns:** This MessageInfo
**See Also:** timeToLive()

---

#### timeToLive

public abstract

MessageInfo

timeToLive​(long millis)

Sets the time period that the sending side may expire the message if it
has not been sent.

---

