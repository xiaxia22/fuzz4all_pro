# Class CardChannel

**Source:** `java.smartcardio\javax\smartcardio\CardChannel.html`

### Class Description

```java
public abstract class
CardChannel

extends
Object
```

A logical channel connection to a Smart Card. It is used to exchange APDUs
with a Smart Card.
A CardChannel object can be obtained by calling the method

Card.getBasicChannel()

or

Card.openLogicalChannel()

.

**Since:** 1.6
**See Also:** Card

,

CommandAPDU

,

ResponseAPDU

---

### Field Details

*No entries found.*

### Constructor Details

#### protected CardChannel()

Constructs a new CardChannel object.

This constructor is called by subclasses only. Application should
call the

Card.getBasicChannel()

and

Card.openLogicalChannel()

methods to obtain a CardChannel
object.

---

### Method Details

#### public abstract
Card
getCard()

Returns the Card this channel is associated with.

**Returns:**
- the Card this channel is associated with

---

#### public abstract int getChannelNumber()

Returns the channel number of this CardChannel. A channel number of
0 indicates the basic logical channel.

**Returns:**
- the channel number of this CardChannel.

**Throws:**
- IllegalStateException

- if this channel has been

closed

or if the corresponding Card has been

disconnected

.

---

#### public abstract
ResponseAPDU
transmit​(
CommandAPDU
command)
throws
CardException

Transmits the specified command APDU to the Smart Card and returns the
response APDU.

The CLA byte of the command APDU is automatically adjusted to
match the channel number of this CardChannel.

Note that this method cannot be used to transmit

MANAGE CHANNEL

APDUs. Logical channels should be managed
using the

Card.openLogicalChannel()

and

CardChannel.close()

methods.

Implementations should transparently handle artifacts
of the transmission protocol.
For example, when using the T=0 protocol, the following processing
should occur as described in ISO/IEC 7816-4:

- if the response APDU has an SW1 of

61

, the
implementation should issue a

GET RESPONSE

command
using

SW2

as the

Le

field.
This process is repeated as long as an SW1 of

61

is
received. The response body of these exchanges is concatenated
to form the final response body.

if the response APDU is

6C XX

, the implementation
should reissue the command using

XX

as the

Le

field.

The ResponseAPDU returned by this method is the result
after this processing has been performed.

**Parameters:**
- command

- the command APDU

**Returns:**
- the response APDU received from the card

**Throws:**
- IllegalStateException

- if this channel has been

closed

or if the corresponding Card has been

disconnected

.
- IllegalArgumentException

- if the APDU encodes a

MANAGE CHANNEL

command
- NullPointerException

- if command is null
- CardException

- if the card operation failed

---

#### public abstract int transmit​(
ByteBuffer
command,

ByteBuffer
response)
throws
CardException

Transmits the command APDU stored in the command ByteBuffer and receives
the response APDU in the response ByteBuffer.

The command buffer must contain valid command APDU data starting
at

command.position()

and the APDU must be

command.remaining()

bytes long.
Upon return, the command buffer's position will be equal
to its limit; its limit will not have changed. The output buffer
will have received the response APDU bytes. Its position will have
advanced by the number of bytes received, which is also the return
value of this method.

The CLA byte of the command APDU is automatically adjusted to
match the channel number of this CardChannel.

Note that this method cannot be used to transmit

MANAGE CHANNEL

APDUs. Logical channels should be managed
using the

Card.openLogicalChannel()

and

CardChannel.close()

methods.

See

transmit()

for a discussion of the handling
of response APDUs with the SW1 values

61

or

6C

.

**Parameters:**
- command

- the buffer containing the command APDU
- response

- the buffer that shall receive the response APDU from
the card

**Returns:**
- the length of the received response APDU

**Throws:**
- IllegalStateException

- if this channel has been

closed

or if the corresponding Card has been

disconnected

.
- NullPointerException

- if command or response is null
- ReadOnlyBufferException

- if the response buffer is read-only
- IllegalArgumentException

- if command and response are the
same object, if

response

may not have
sufficient space to receive the response APDU
or if the APDU encodes a

MANAGE CHANNEL

command
- CardException

- if the card operation failed

---

#### public abstract void close()
throws
CardException

Closes this CardChannel. The logical channel is closed by issuing
a

MANAGE CHANNEL

command that should use the format

[xx 70 80 0n]

where

n

is the channel number
of this channel and

xx

is the

CLA

byte that encodes this logical channel and has all other bits set to 0.
After this method returns, calling other
methods in this class will raise an IllegalStateException.

Note that the basic logical channel cannot be closed using this
method. It can be closed by calling

Card.disconnect(boolean)

.

**Throws:**
- CardException

- if the card operation failed
- IllegalStateException

- if this CardChannel represents a
connection the basic logical channel

---

### Additional Sections

#### Class CardChannel

java.lang.Object

- javax.smartcardio.CardChannel

javax.smartcardio.CardChannel

```java
public abstract class
CardChannel

extends
Object
```

A logical channel connection to a Smart Card. It is used to exchange APDUs
with a Smart Card.
A CardChannel object can be obtained by calling the method

Card.getBasicChannel()

or

Card.openLogicalChannel()

.

**Since:** 1.6
**See Also:** Card

,

CommandAPDU

,

ResponseAPDU

public abstract class

CardChannel

extends

Object

A logical channel connection to a Smart Card. It is used to exchange APDUs
with a Smart Card.
A CardChannel object can be obtained by calling the method

Card.getBasicChannel()

or

Card.openLogicalChannel()

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CardChannel

()

Constructs a new CardChannel object.

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

Closes this CardChannel.

abstract

Card

getCard

()

Returns the Card this channel is associated with.

abstract int

getChannelNumber

()

Returns the channel number of this CardChannel.

abstract int

transmit

​(

ByteBuffer

command,

ByteBuffer

response)

Transmits the command APDU stored in the command ByteBuffer and receives
the response APDU in the response ByteBuffer.

abstract

ResponseAPDU

transmit

​(

CommandAPDU

command)

Transmits the specified command APDU to the Smart Card and returns the
response APDU.

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

CardChannel

()

Constructs a new CardChannel object.

---

#### Constructor Summary

Constructs a new CardChannel object.

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

Closes this CardChannel.

abstract

Card

getCard

()

Returns the Card this channel is associated with.

abstract int

getChannelNumber

()

Returns the channel number of this CardChannel.

abstract int

transmit

​(

ByteBuffer

command,

ByteBuffer

response)

Transmits the command APDU stored in the command ByteBuffer and receives
the response APDU in the response ByteBuffer.

abstract

ResponseAPDU

transmit

​(

CommandAPDU

command)

Transmits the specified command APDU to the Smart Card and returns the
response APDU.

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

Closes this CardChannel.

Returns the Card this channel is associated with.

Returns the channel number of this CardChannel.

Transmits the command APDU stored in the command ByteBuffer and receives
the response APDU in the response ByteBuffer.

Transmits the specified command APDU to the Smart Card and returns the
response APDU.

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

- CardChannel

```java
protected CardChannel()
```

Constructs a new CardChannel object.

This constructor is called by subclasses only. Application should
call the

Card.getBasicChannel()

and

Card.openLogicalChannel()

methods to obtain a CardChannel
object.

============ METHOD DETAIL ==========

- Method Detail

- getCard

```java
public abstract
Card
getCard()
```

Returns the Card this channel is associated with.

**Returns:** the Card this channel is associated with

- getChannelNumber

```java
public abstract int getChannelNumber()
```

Returns the channel number of this CardChannel. A channel number of
0 indicates the basic logical channel.

**Returns:** the channel number of this CardChannel.
**Throws:** IllegalStateException

- if this channel has been

closed

or if the corresponding Card has been

disconnected

.

- transmit

```java
public abstract
ResponseAPDU
transmit​(
CommandAPDU
command)
throws
CardException
```

Transmits the specified command APDU to the Smart Card and returns the
response APDU.

The CLA byte of the command APDU is automatically adjusted to
match the channel number of this CardChannel.

Note that this method cannot be used to transmit

MANAGE CHANNEL

APDUs. Logical channels should be managed
using the

Card.openLogicalChannel()

and

CardChannel.close()

methods.

Implementations should transparently handle artifacts
of the transmission protocol.
For example, when using the T=0 protocol, the following processing
should occur as described in ISO/IEC 7816-4:

- if the response APDU has an SW1 of

61

, the
implementation should issue a

GET RESPONSE

command
using

SW2

as the

Le

field.
This process is repeated as long as an SW1 of

61

is
received. The response body of these exchanges is concatenated
to form the final response body.

if the response APDU is

6C XX

, the implementation
should reissue the command using

XX

as the

Le

field.

The ResponseAPDU returned by this method is the result
after this processing has been performed.

**Parameters:** command

- the command APDU
**Returns:** the response APDU received from the card
**Throws:** IllegalStateException

- if this channel has been

closed

or if the corresponding Card has been

disconnected

.
**Throws:** IllegalArgumentException

- if the APDU encodes a

MANAGE CHANNEL

command
**Throws:** NullPointerException

- if command is null
**Throws:** CardException

- if the card operation failed

- transmit

```java
public abstract int transmit​(
ByteBuffer
command,

ByteBuffer
response)
throws
CardException
```

Transmits the command APDU stored in the command ByteBuffer and receives
the response APDU in the response ByteBuffer.

The command buffer must contain valid command APDU data starting
at

command.position()

and the APDU must be

command.remaining()

bytes long.
Upon return, the command buffer's position will be equal
to its limit; its limit will not have changed. The output buffer
will have received the response APDU bytes. Its position will have
advanced by the number of bytes received, which is also the return
value of this method.

The CLA byte of the command APDU is automatically adjusted to
match the channel number of this CardChannel.

Note that this method cannot be used to transmit

MANAGE CHANNEL

APDUs. Logical channels should be managed
using the

Card.openLogicalChannel()

and

CardChannel.close()

methods.

See

transmit()

for a discussion of the handling
of response APDUs with the SW1 values

61

or

6C

.

**Parameters:** command

- the buffer containing the command APDU
**Parameters:** response

- the buffer that shall receive the response APDU from
the card
**Returns:** the length of the received response APDU
**Throws:** IllegalStateException

- if this channel has been

closed

or if the corresponding Card has been

disconnected

.
**Throws:** NullPointerException

- if command or response is null
**Throws:** ReadOnlyBufferException

- if the response buffer is read-only
**Throws:** IllegalArgumentException

- if command and response are the
same object, if

response

may not have
sufficient space to receive the response APDU
or if the APDU encodes a

MANAGE CHANNEL

command
**Throws:** CardException

- if the card operation failed

- close

```java
public abstract void close()
throws
CardException
```

Closes this CardChannel. The logical channel is closed by issuing
a

MANAGE CHANNEL

command that should use the format

[xx 70 80 0n]

where

n

is the channel number
of this channel and

xx

is the

CLA

byte that encodes this logical channel and has all other bits set to 0.
After this method returns, calling other
methods in this class will raise an IllegalStateException.

Note that the basic logical channel cannot be closed using this
method. It can be closed by calling

Card.disconnect(boolean)

.

**Throws:** CardException

- if the card operation failed
**Throws:** IllegalStateException

- if this CardChannel represents a
connection the basic logical channel

Constructor Detail

- CardChannel

```java
protected CardChannel()
```

Constructs a new CardChannel object.

This constructor is called by subclasses only. Application should
call the

Card.getBasicChannel()

and

Card.openLogicalChannel()

methods to obtain a CardChannel
object.

---

#### Constructor Detail

CardChannel

```java
protected CardChannel()
```

Constructs a new CardChannel object.

This constructor is called by subclasses only. Application should
call the

Card.getBasicChannel()

and

Card.openLogicalChannel()

methods to obtain a CardChannel
object.

---

#### CardChannel

protected CardChannel()

Constructs a new CardChannel object.

This constructor is called by subclasses only. Application should
call the

Card.getBasicChannel()

and

Card.openLogicalChannel()

methods to obtain a CardChannel
object.

This constructor is called by subclasses only. Application should
call the

Card.getBasicChannel()

and

Card.openLogicalChannel()

methods to obtain a CardChannel
object.

Method Detail

- getCard

```java
public abstract
Card
getCard()
```

Returns the Card this channel is associated with.

**Returns:** the Card this channel is associated with

- getChannelNumber

```java
public abstract int getChannelNumber()
```

Returns the channel number of this CardChannel. A channel number of
0 indicates the basic logical channel.

**Returns:** the channel number of this CardChannel.
**Throws:** IllegalStateException

- if this channel has been

closed

or if the corresponding Card has been

disconnected

.

- transmit

```java
public abstract
ResponseAPDU
transmit​(
CommandAPDU
command)
throws
CardException
```

Transmits the specified command APDU to the Smart Card and returns the
response APDU.

The CLA byte of the command APDU is automatically adjusted to
match the channel number of this CardChannel.

Note that this method cannot be used to transmit

MANAGE CHANNEL

APDUs. Logical channels should be managed
using the

Card.openLogicalChannel()

and

CardChannel.close()

methods.

Implementations should transparently handle artifacts
of the transmission protocol.
For example, when using the T=0 protocol, the following processing
should occur as described in ISO/IEC 7816-4:

- if the response APDU has an SW1 of

61

, the
implementation should issue a

GET RESPONSE

command
using

SW2

as the

Le

field.
This process is repeated as long as an SW1 of

61

is
received. The response body of these exchanges is concatenated
to form the final response body.

if the response APDU is

6C XX

, the implementation
should reissue the command using

XX

as the

Le

field.

The ResponseAPDU returned by this method is the result
after this processing has been performed.

**Parameters:** command

- the command APDU
**Returns:** the response APDU received from the card
**Throws:** IllegalStateException

- if this channel has been

closed

or if the corresponding Card has been

disconnected

.
**Throws:** IllegalArgumentException

- if the APDU encodes a

MANAGE CHANNEL

command
**Throws:** NullPointerException

- if command is null
**Throws:** CardException

- if the card operation failed

- transmit

```java
public abstract int transmit​(
ByteBuffer
command,

ByteBuffer
response)
throws
CardException
```

Transmits the command APDU stored in the command ByteBuffer and receives
the response APDU in the response ByteBuffer.

The command buffer must contain valid command APDU data starting
at

command.position()

and the APDU must be

command.remaining()

bytes long.
Upon return, the command buffer's position will be equal
to its limit; its limit will not have changed. The output buffer
will have received the response APDU bytes. Its position will have
advanced by the number of bytes received, which is also the return
value of this method.

The CLA byte of the command APDU is automatically adjusted to
match the channel number of this CardChannel.

Note that this method cannot be used to transmit

MANAGE CHANNEL

APDUs. Logical channels should be managed
using the

Card.openLogicalChannel()

and

CardChannel.close()

methods.

See

transmit()

for a discussion of the handling
of response APDUs with the SW1 values

61

or

6C

.

**Parameters:** command

- the buffer containing the command APDU
**Parameters:** response

- the buffer that shall receive the response APDU from
the card
**Returns:** the length of the received response APDU
**Throws:** IllegalStateException

- if this channel has been

closed

or if the corresponding Card has been

disconnected

.
**Throws:** NullPointerException

- if command or response is null
**Throws:** ReadOnlyBufferException

- if the response buffer is read-only
**Throws:** IllegalArgumentException

- if command and response are the
same object, if

response

may not have
sufficient space to receive the response APDU
or if the APDU encodes a

MANAGE CHANNEL

command
**Throws:** CardException

- if the card operation failed

- close

```java
public abstract void close()
throws
CardException
```

Closes this CardChannel. The logical channel is closed by issuing
a

MANAGE CHANNEL

command that should use the format

[xx 70 80 0n]

where

n

is the channel number
of this channel and

xx

is the

CLA

byte that encodes this logical channel and has all other bits set to 0.
After this method returns, calling other
methods in this class will raise an IllegalStateException.

Note that the basic logical channel cannot be closed using this
method. It can be closed by calling

Card.disconnect(boolean)

.

**Throws:** CardException

- if the card operation failed
**Throws:** IllegalStateException

- if this CardChannel represents a
connection the basic logical channel

---

#### Method Detail

getCard

```java
public abstract
Card
getCard()
```

Returns the Card this channel is associated with.

**Returns:** the Card this channel is associated with

---

#### getCard

public abstract

Card

getCard()

Returns the Card this channel is associated with.

getChannelNumber

```java
public abstract int getChannelNumber()
```

Returns the channel number of this CardChannel. A channel number of
0 indicates the basic logical channel.

**Returns:** the channel number of this CardChannel.
**Throws:** IllegalStateException

- if this channel has been

closed

or if the corresponding Card has been

disconnected

.

---

#### getChannelNumber

public abstract int getChannelNumber()

Returns the channel number of this CardChannel. A channel number of
0 indicates the basic logical channel.

transmit

```java
public abstract
ResponseAPDU
transmit​(
CommandAPDU
command)
throws
CardException
```

Transmits the specified command APDU to the Smart Card and returns the
response APDU.

The CLA byte of the command APDU is automatically adjusted to
match the channel number of this CardChannel.

Note that this method cannot be used to transmit

MANAGE CHANNEL

APDUs. Logical channels should be managed
using the

Card.openLogicalChannel()

and

CardChannel.close()

methods.

Implementations should transparently handle artifacts
of the transmission protocol.
For example, when using the T=0 protocol, the following processing
should occur as described in ISO/IEC 7816-4:

- if the response APDU has an SW1 of

61

, the
implementation should issue a

GET RESPONSE

command
using

SW2

as the

Le

field.
This process is repeated as long as an SW1 of

61

is
received. The response body of these exchanges is concatenated
to form the final response body.

if the response APDU is

6C XX

, the implementation
should reissue the command using

XX

as the

Le

field.

The ResponseAPDU returned by this method is the result
after this processing has been performed.

**Parameters:** command

- the command APDU
**Returns:** the response APDU received from the card
**Throws:** IllegalStateException

- if this channel has been

closed

or if the corresponding Card has been

disconnected

.
**Throws:** IllegalArgumentException

- if the APDU encodes a

MANAGE CHANNEL

command
**Throws:** NullPointerException

- if command is null
**Throws:** CardException

- if the card operation failed

---

#### transmit

public abstract

ResponseAPDU

transmit​(

CommandAPDU

command)
throws

CardException

Transmits the specified command APDU to the Smart Card and returns the
response APDU.

The CLA byte of the command APDU is automatically adjusted to
match the channel number of this CardChannel.

Note that this method cannot be used to transmit

MANAGE CHANNEL

APDUs. Logical channels should be managed
using the

Card.openLogicalChannel()

and

CardChannel.close()

methods.

Implementations should transparently handle artifacts
of the transmission protocol.
For example, when using the T=0 protocol, the following processing
should occur as described in ISO/IEC 7816-4:

- if the response APDU has an SW1 of

61

, the
implementation should issue a

GET RESPONSE

command
using

SW2

as the

Le

field.
This process is repeated as long as an SW1 of

61

is
received. The response body of these exchanges is concatenated
to form the final response body.

if the response APDU is

6C XX

, the implementation
should reissue the command using

XX

as the

Le

field.

The ResponseAPDU returned by this method is the result
after this processing has been performed.

The CLA byte of the command APDU is automatically adjusted to
match the channel number of this CardChannel.

Note that this method cannot be used to transmit

MANAGE CHANNEL

APDUs. Logical channels should be managed
using the

Card.openLogicalChannel()

and

CardChannel.close()

methods.

Implementations should transparently handle artifacts
of the transmission protocol.
For example, when using the T=0 protocol, the following processing
should occur as described in ISO/IEC 7816-4:

- if the response APDU has an SW1 of

61

, the
implementation should issue a

GET RESPONSE

command
using

SW2

as the

Le

field.
This process is repeated as long as an SW1 of

61

is
received. The response body of these exchanges is concatenated
to form the final response body.

if the response APDU is

6C XX

, the implementation
should reissue the command using

XX

as the

Le

field.

The ResponseAPDU returned by this method is the result
after this processing has been performed.

Note that this method cannot be used to transmit

MANAGE CHANNEL

APDUs. Logical channels should be managed
using the

Card.openLogicalChannel()

and

CardChannel.close()

methods.

Implementations should transparently handle artifacts
of the transmission protocol.
For example, when using the T=0 protocol, the following processing
should occur as described in ISO/IEC 7816-4:

- if the response APDU has an SW1 of

61

, the
implementation should issue a

GET RESPONSE

command
using

SW2

as the

Le

field.
This process is repeated as long as an SW1 of

61

is
received. The response body of these exchanges is concatenated
to form the final response body.

if the response APDU is

6C XX

, the implementation
should reissue the command using

XX

as the

Le

field.

The ResponseAPDU returned by this method is the result
after this processing has been performed.

Implementations should transparently handle artifacts
of the transmission protocol.
For example, when using the T=0 protocol, the following processing
should occur as described in ISO/IEC 7816-4:

- if the response APDU has an SW1 of

61

, the
implementation should issue a

GET RESPONSE

command
using

SW2

as the

Le

field.
This process is repeated as long as an SW1 of

61

is
received. The response body of these exchanges is concatenated
to form the final response body.

if the response APDU is

6C XX

, the implementation
should reissue the command using

XX

as the

Le

field.

The ResponseAPDU returned by this method is the result
after this processing has been performed.

if the response APDU has an SW1 of

61

, the
implementation should issue a

GET RESPONSE

command
using

SW2

as the

Le

field.
This process is repeated as long as an SW1 of

61

is
received. The response body of these exchanges is concatenated
to form the final response body.

if the response APDU is

6C XX

, the implementation
should reissue the command using

XX

as the

Le

field.

if the response APDU is

6C XX

, the implementation
should reissue the command using

XX

as the

Le

field.

The ResponseAPDU returned by this method is the result
after this processing has been performed.

transmit

```java
public abstract int transmit​(
ByteBuffer
command,

ByteBuffer
response)
throws
CardException
```

Transmits the command APDU stored in the command ByteBuffer and receives
the response APDU in the response ByteBuffer.

The command buffer must contain valid command APDU data starting
at

command.position()

and the APDU must be

command.remaining()

bytes long.
Upon return, the command buffer's position will be equal
to its limit; its limit will not have changed. The output buffer
will have received the response APDU bytes. Its position will have
advanced by the number of bytes received, which is also the return
value of this method.

The CLA byte of the command APDU is automatically adjusted to
match the channel number of this CardChannel.

Note that this method cannot be used to transmit

MANAGE CHANNEL

APDUs. Logical channels should be managed
using the

Card.openLogicalChannel()

and

CardChannel.close()

methods.

See

transmit()

for a discussion of the handling
of response APDUs with the SW1 values

61

or

6C

.

**Parameters:** command

- the buffer containing the command APDU
**Parameters:** response

- the buffer that shall receive the response APDU from
the card
**Returns:** the length of the received response APDU
**Throws:** IllegalStateException

- if this channel has been

closed

or if the corresponding Card has been

disconnected

.
**Throws:** NullPointerException

- if command or response is null
**Throws:** ReadOnlyBufferException

- if the response buffer is read-only
**Throws:** IllegalArgumentException

- if command and response are the
same object, if

response

may not have
sufficient space to receive the response APDU
or if the APDU encodes a

MANAGE CHANNEL

command
**Throws:** CardException

- if the card operation failed

---

#### transmit

public abstract int transmit​(

ByteBuffer

command,

ByteBuffer

response)
throws

CardException

Transmits the command APDU stored in the command ByteBuffer and receives
the response APDU in the response ByteBuffer.

The command buffer must contain valid command APDU data starting
at

command.position()

and the APDU must be

command.remaining()

bytes long.
Upon return, the command buffer's position will be equal
to its limit; its limit will not have changed. The output buffer
will have received the response APDU bytes. Its position will have
advanced by the number of bytes received, which is also the return
value of this method.

The CLA byte of the command APDU is automatically adjusted to
match the channel number of this CardChannel.

Note that this method cannot be used to transmit

MANAGE CHANNEL

APDUs. Logical channels should be managed
using the

Card.openLogicalChannel()

and

CardChannel.close()

methods.

See

transmit()

for a discussion of the handling
of response APDUs with the SW1 values

61

or

6C

.

The command buffer must contain valid command APDU data starting
at

command.position()

and the APDU must be

command.remaining()

bytes long.
Upon return, the command buffer's position will be equal
to its limit; its limit will not have changed. The output buffer
will have received the response APDU bytes. Its position will have
advanced by the number of bytes received, which is also the return
value of this method.

The CLA byte of the command APDU is automatically adjusted to
match the channel number of this CardChannel.

Note that this method cannot be used to transmit

MANAGE CHANNEL

APDUs. Logical channels should be managed
using the

Card.openLogicalChannel()

and

CardChannel.close()

methods.

See

transmit()

for a discussion of the handling
of response APDUs with the SW1 values

61

or

6C

.

The CLA byte of the command APDU is automatically adjusted to
match the channel number of this CardChannel.

Note that this method cannot be used to transmit

MANAGE CHANNEL

APDUs. Logical channels should be managed
using the

Card.openLogicalChannel()

and

CardChannel.close()

methods.

See

transmit()

for a discussion of the handling
of response APDUs with the SW1 values

61

or

6C

.

Note that this method cannot be used to transmit

MANAGE CHANNEL

APDUs. Logical channels should be managed
using the

Card.openLogicalChannel()

and

CardChannel.close()

methods.

See

transmit()

for a discussion of the handling
of response APDUs with the SW1 values

61

or

6C

.

See

transmit()

for a discussion of the handling
of response APDUs with the SW1 values

61

or

6C

.

close

```java
public abstract void close()
throws
CardException
```

Closes this CardChannel. The logical channel is closed by issuing
a

MANAGE CHANNEL

command that should use the format

[xx 70 80 0n]

where

n

is the channel number
of this channel and

xx

is the

CLA

byte that encodes this logical channel and has all other bits set to 0.
After this method returns, calling other
methods in this class will raise an IllegalStateException.

Note that the basic logical channel cannot be closed using this
method. It can be closed by calling

Card.disconnect(boolean)

.

**Throws:** CardException

- if the card operation failed
**Throws:** IllegalStateException

- if this CardChannel represents a
connection the basic logical channel

---

#### close

public abstract void close()
throws

CardException

Closes this CardChannel. The logical channel is closed by issuing
a

MANAGE CHANNEL

command that should use the format

[xx 70 80 0n]

where

n

is the channel number
of this channel and

xx

is the

CLA

byte that encodes this logical channel and has all other bits set to 0.
After this method returns, calling other
methods in this class will raise an IllegalStateException.

Note that the basic logical channel cannot be closed using this
method. It can be closed by calling

Card.disconnect(boolean)

.

Note that the basic logical channel cannot be closed using this
method. It can be closed by calling

Card.disconnect(boolean)

.

---

