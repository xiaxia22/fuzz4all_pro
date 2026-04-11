# Class Card

**Source:** `java.smartcardio\javax\smartcardio\Card.html`

### Class Description

```java
public abstract class
Card

extends
Object
```

A Smart Card with which a connection has been established. Card objects
are obtained by calling

CardTerminal.connect()

.

**Since:** 1.6
**See Also:** CardTerminal

---

### Field Details

*No entries found.*

### Constructor Details

#### protected Card()

Constructs a new Card object.

This constructor is called by subclasses only. Application should
call the

CardTerminal.connect()

method to obtain a Card
object.

---

### Method Details

#### public abstract
ATR
getATR()

Returns the ATR of this card.

**Returns:**
- the ATR of this card.

---

#### public abstract
String
getProtocol()

Returns the protocol in use for this card.

**Returns:**
- the protocol in use for this card, for example "T=0" or "T=1"

---

#### public abstract
CardChannel
getBasicChannel()

Returns the CardChannel for the basic logical channel. The basic
logical channel has a channel number of 0.

**Returns:**
- the CardChannel for the basic logical channel

**Throws:**
- SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission
- IllegalStateException

- if this card object has been disposed of
via the

disconnect()

method

---

#### public abstract
CardChannel
openLogicalChannel()
throws
CardException

Opens a new logical channel to the card and returns it. The channel is
opened by issuing a

MANAGE CHANNEL

command that should use
the format

[00 70 00 00 01]

.

**Returns:**
- the logical channel which has been opened

**Throws:**
- SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission
- CardException

- is a new logical channel could not be opened
- IllegalStateException

- if this card object has been disposed of
via the

disconnect()

method

---

#### public abstract void beginExclusive()
throws
CardException

Requests exclusive access to this card.

Once a thread has invoked

beginExclusive

, only this
thread is allowed to communicate with this card until it calls

endExclusive

. Other threads attempting communication
will receive a CardException.

Applications have to ensure that exclusive access is correctly
released. This can be achieved by executing
the

beginExclusive()

and

endExclusive

calls
in a

try ... finally

block.

**Throws:**
- SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission
- CardException

- if exclusive access has already been set
or if exclusive access could not be established
- IllegalStateException

- if this card object has been disposed of
via the

disconnect()

method

---

#### public abstract void endExclusive()
throws
CardException

Releases the exclusive access previously established using

beginExclusive

.

**Throws:**
- SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission
- IllegalStateException

- if the active Thread does not currently have
exclusive access to this card or
if this card object has been disposed of
via the

disconnect()

method
- CardException

- if the operation failed

---

#### public abstract byte[] transmitControlCommand​(int controlCode,
byte[] command)
throws
CardException

Transmits a control command to the terminal device.

This can be used to, for example, control terminal functions like
a built-in PIN pad or biometrics.

**Parameters:**
- controlCode

- the control code of the command
- command

- the command data

**Returns:**
- the response from the terminal device

**Throws:**
- SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission
- NullPointerException

- if command is null
- CardException

- if the card operation failed
- IllegalStateException

- if this card object has been disposed of
via the

disconnect()

method

---

#### public abstract void disconnect​(boolean reset)
throws
CardException

Disconnects the connection with this card. After this method returns,
calling methods on this object or in CardChannels associated with this
object that require interaction with the card will raise an
IllegalStateException.

**Parameters:**
- reset

- whether to reset the card after disconnecting.

**Throws:**
- CardException

- if the card operation failed
- SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission

---

### Additional Sections

#### Class Card

java.lang.Object

- javax.smartcardio.Card

javax.smartcardio.Card

```java
public abstract class
Card

extends
Object
```

A Smart Card with which a connection has been established. Card objects
are obtained by calling

CardTerminal.connect()

.

**Since:** 1.6
**See Also:** CardTerminal

public abstract class

Card

extends

Object

A Smart Card with which a connection has been established. Card objects
are obtained by calling

CardTerminal.connect()

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Card

()

Constructs a new Card object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract void

beginExclusive

()

Requests exclusive access to this card.

abstract void

disconnect

​(boolean reset)

Disconnects the connection with this card.

abstract void

endExclusive

()

Releases the exclusive access previously established using

beginExclusive

.

abstract

ATR

getATR

()

Returns the ATR of this card.

abstract

CardChannel

getBasicChannel

()

Returns the CardChannel for the basic logical channel.

abstract

String

getProtocol

()

Returns the protocol in use for this card.

abstract

CardChannel

openLogicalChannel

()

Opens a new logical channel to the card and returns it.

abstract byte[]

transmitControlCommand

​(int controlCode,
byte[] command)

Transmits a control command to the terminal device.

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

Card

()

Constructs a new Card object.

---

#### Constructor Summary

Constructs a new Card object.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract void

beginExclusive

()

Requests exclusive access to this card.

abstract void

disconnect

​(boolean reset)

Disconnects the connection with this card.

abstract void

endExclusive

()

Releases the exclusive access previously established using

beginExclusive

.

abstract

ATR

getATR

()

Returns the ATR of this card.

abstract

CardChannel

getBasicChannel

()

Returns the CardChannel for the basic logical channel.

abstract

String

getProtocol

()

Returns the protocol in use for this card.

abstract

CardChannel

openLogicalChannel

()

Opens a new logical channel to the card and returns it.

abstract byte[]

transmitControlCommand

​(int controlCode,
byte[] command)

Transmits a control command to the terminal device.

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

Requests exclusive access to this card.

Disconnects the connection with this card.

Releases the exclusive access previously established using

beginExclusive

.

Returns the ATR of this card.

Returns the CardChannel for the basic logical channel.

Returns the protocol in use for this card.

Opens a new logical channel to the card and returns it.

Transmits a control command to the terminal device.

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

- Card

```java
protected Card()
```

Constructs a new Card object.

This constructor is called by subclasses only. Application should
call the

CardTerminal.connect()

method to obtain a Card
object.

============ METHOD DETAIL ==========

- Method Detail

- getATR

```java
public abstract
ATR
getATR()
```

Returns the ATR of this card.

**Returns:** the ATR of this card.

- getProtocol

```java
public abstract
String
getProtocol()
```

Returns the protocol in use for this card.

**Returns:** the protocol in use for this card, for example "T=0" or "T=1"

- getBasicChannel

```java
public abstract
CardChannel
getBasicChannel()
```

Returns the CardChannel for the basic logical channel. The basic
logical channel has a channel number of 0.

**Returns:** the CardChannel for the basic logical channel
**Throws:** SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission
**Throws:** IllegalStateException

- if this card object has been disposed of
via the

disconnect()

method

- openLogicalChannel

```java
public abstract
CardChannel
openLogicalChannel()
throws
CardException
```

Opens a new logical channel to the card and returns it. The channel is
opened by issuing a

MANAGE CHANNEL

command that should use
the format

[00 70 00 00 01]

.

**Returns:** the logical channel which has been opened
**Throws:** SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission
**Throws:** CardException

- is a new logical channel could not be opened
**Throws:** IllegalStateException

- if this card object has been disposed of
via the

disconnect()

method

- beginExclusive

```java
public abstract void beginExclusive()
throws
CardException
```

Requests exclusive access to this card.

Once a thread has invoked

beginExclusive

, only this
thread is allowed to communicate with this card until it calls

endExclusive

. Other threads attempting communication
will receive a CardException.

Applications have to ensure that exclusive access is correctly
released. This can be achieved by executing
the

beginExclusive()

and

endExclusive

calls
in a

try ... finally

block.

**Throws:** SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission
**Throws:** CardException

- if exclusive access has already been set
or if exclusive access could not be established
**Throws:** IllegalStateException

- if this card object has been disposed of
via the

disconnect()

method

- endExclusive

```java
public abstract void endExclusive()
throws
CardException
```

Releases the exclusive access previously established using

beginExclusive

.

**Throws:** SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission
**Throws:** IllegalStateException

- if the active Thread does not currently have
exclusive access to this card or
if this card object has been disposed of
via the

disconnect()

method
**Throws:** CardException

- if the operation failed

- transmitControlCommand

```java
public abstract byte[] transmitControlCommand​(int controlCode,
byte[] command)
throws
CardException
```

Transmits a control command to the terminal device.

This can be used to, for example, control terminal functions like
a built-in PIN pad or biometrics.

**Parameters:** controlCode

- the control code of the command
**Parameters:** command

- the command data
**Returns:** the response from the terminal device
**Throws:** SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission
**Throws:** NullPointerException

- if command is null
**Throws:** CardException

- if the card operation failed
**Throws:** IllegalStateException

- if this card object has been disposed of
via the

disconnect()

method

- disconnect

```java
public abstract void disconnect​(boolean reset)
throws
CardException
```

Disconnects the connection with this card. After this method returns,
calling methods on this object or in CardChannels associated with this
object that require interaction with the card will raise an
IllegalStateException.

**Parameters:** reset

- whether to reset the card after disconnecting.
**Throws:** CardException

- if the card operation failed
**Throws:** SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission

Constructor Detail

- Card

```java
protected Card()
```

Constructs a new Card object.

This constructor is called by subclasses only. Application should
call the

CardTerminal.connect()

method to obtain a Card
object.

---

#### Constructor Detail

Card

```java
protected Card()
```

Constructs a new Card object.

This constructor is called by subclasses only. Application should
call the

CardTerminal.connect()

method to obtain a Card
object.

---

#### Card

protected Card()

Constructs a new Card object.

This constructor is called by subclasses only. Application should
call the

CardTerminal.connect()

method to obtain a Card
object.

This constructor is called by subclasses only. Application should
call the

CardTerminal.connect()

method to obtain a Card
object.

Method Detail

- getATR

```java
public abstract
ATR
getATR()
```

Returns the ATR of this card.

**Returns:** the ATR of this card.

- getProtocol

```java
public abstract
String
getProtocol()
```

Returns the protocol in use for this card.

**Returns:** the protocol in use for this card, for example "T=0" or "T=1"

- getBasicChannel

```java
public abstract
CardChannel
getBasicChannel()
```

Returns the CardChannel for the basic logical channel. The basic
logical channel has a channel number of 0.

**Returns:** the CardChannel for the basic logical channel
**Throws:** SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission
**Throws:** IllegalStateException

- if this card object has been disposed of
via the

disconnect()

method

- openLogicalChannel

```java
public abstract
CardChannel
openLogicalChannel()
throws
CardException
```

Opens a new logical channel to the card and returns it. The channel is
opened by issuing a

MANAGE CHANNEL

command that should use
the format

[00 70 00 00 01]

.

**Returns:** the logical channel which has been opened
**Throws:** SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission
**Throws:** CardException

- is a new logical channel could not be opened
**Throws:** IllegalStateException

- if this card object has been disposed of
via the

disconnect()

method

- beginExclusive

```java
public abstract void beginExclusive()
throws
CardException
```

Requests exclusive access to this card.

Once a thread has invoked

beginExclusive

, only this
thread is allowed to communicate with this card until it calls

endExclusive

. Other threads attempting communication
will receive a CardException.

Applications have to ensure that exclusive access is correctly
released. This can be achieved by executing
the

beginExclusive()

and

endExclusive

calls
in a

try ... finally

block.

**Throws:** SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission
**Throws:** CardException

- if exclusive access has already been set
or if exclusive access could not be established
**Throws:** IllegalStateException

- if this card object has been disposed of
via the

disconnect()

method

- endExclusive

```java
public abstract void endExclusive()
throws
CardException
```

Releases the exclusive access previously established using

beginExclusive

.

**Throws:** SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission
**Throws:** IllegalStateException

- if the active Thread does not currently have
exclusive access to this card or
if this card object has been disposed of
via the

disconnect()

method
**Throws:** CardException

- if the operation failed

- transmitControlCommand

```java
public abstract byte[] transmitControlCommand​(int controlCode,
byte[] command)
throws
CardException
```

Transmits a control command to the terminal device.

This can be used to, for example, control terminal functions like
a built-in PIN pad or biometrics.

**Parameters:** controlCode

- the control code of the command
**Parameters:** command

- the command data
**Returns:** the response from the terminal device
**Throws:** SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission
**Throws:** NullPointerException

- if command is null
**Throws:** CardException

- if the card operation failed
**Throws:** IllegalStateException

- if this card object has been disposed of
via the

disconnect()

method

- disconnect

```java
public abstract void disconnect​(boolean reset)
throws
CardException
```

Disconnects the connection with this card. After this method returns,
calling methods on this object or in CardChannels associated with this
object that require interaction with the card will raise an
IllegalStateException.

**Parameters:** reset

- whether to reset the card after disconnecting.
**Throws:** CardException

- if the card operation failed
**Throws:** SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission

---

#### Method Detail

getATR

```java
public abstract
ATR
getATR()
```

Returns the ATR of this card.

**Returns:** the ATR of this card.

---

#### getATR

public abstract

ATR

getATR()

Returns the ATR of this card.

getProtocol

```java
public abstract
String
getProtocol()
```

Returns the protocol in use for this card.

**Returns:** the protocol in use for this card, for example "T=0" or "T=1"

---

#### getProtocol

public abstract

String

getProtocol()

Returns the protocol in use for this card.

getBasicChannel

```java
public abstract
CardChannel
getBasicChannel()
```

Returns the CardChannel for the basic logical channel. The basic
logical channel has a channel number of 0.

**Returns:** the CardChannel for the basic logical channel
**Throws:** SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission
**Throws:** IllegalStateException

- if this card object has been disposed of
via the

disconnect()

method

---

#### getBasicChannel

public abstract

CardChannel

getBasicChannel()

Returns the CardChannel for the basic logical channel. The basic
logical channel has a channel number of 0.

openLogicalChannel

```java
public abstract
CardChannel
openLogicalChannel()
throws
CardException
```

Opens a new logical channel to the card and returns it. The channel is
opened by issuing a

MANAGE CHANNEL

command that should use
the format

[00 70 00 00 01]

.

**Returns:** the logical channel which has been opened
**Throws:** SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission
**Throws:** CardException

- is a new logical channel could not be opened
**Throws:** IllegalStateException

- if this card object has been disposed of
via the

disconnect()

method

---

#### openLogicalChannel

public abstract

CardChannel

openLogicalChannel()
throws

CardException

Opens a new logical channel to the card and returns it. The channel is
opened by issuing a

MANAGE CHANNEL

command that should use
the format

[00 70 00 00 01]

.

beginExclusive

```java
public abstract void beginExclusive()
throws
CardException
```

Requests exclusive access to this card.

Once a thread has invoked

beginExclusive

, only this
thread is allowed to communicate with this card until it calls

endExclusive

. Other threads attempting communication
will receive a CardException.

Applications have to ensure that exclusive access is correctly
released. This can be achieved by executing
the

beginExclusive()

and

endExclusive

calls
in a

try ... finally

block.

**Throws:** SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission
**Throws:** CardException

- if exclusive access has already been set
or if exclusive access could not be established
**Throws:** IllegalStateException

- if this card object has been disposed of
via the

disconnect()

method

---

#### beginExclusive

public abstract void beginExclusive()
throws

CardException

Requests exclusive access to this card.

Once a thread has invoked

beginExclusive

, only this
thread is allowed to communicate with this card until it calls

endExclusive

. Other threads attempting communication
will receive a CardException.

Applications have to ensure that exclusive access is correctly
released. This can be achieved by executing
the

beginExclusive()

and

endExclusive

calls
in a

try ... finally

block.

Once a thread has invoked

beginExclusive

, only this
thread is allowed to communicate with this card until it calls

endExclusive

. Other threads attempting communication
will receive a CardException.

Applications have to ensure that exclusive access is correctly
released. This can be achieved by executing
the

beginExclusive()

and

endExclusive

calls
in a

try ... finally

block.

Applications have to ensure that exclusive access is correctly
released. This can be achieved by executing
the

beginExclusive()

and

endExclusive

calls
in a

try ... finally

block.

endExclusive

```java
public abstract void endExclusive()
throws
CardException
```

Releases the exclusive access previously established using

beginExclusive

.

**Throws:** SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission
**Throws:** IllegalStateException

- if the active Thread does not currently have
exclusive access to this card or
if this card object has been disposed of
via the

disconnect()

method
**Throws:** CardException

- if the operation failed

---

#### endExclusive

public abstract void endExclusive()
throws

CardException

Releases the exclusive access previously established using

beginExclusive

.

transmitControlCommand

```java
public abstract byte[] transmitControlCommand​(int controlCode,
byte[] command)
throws
CardException
```

Transmits a control command to the terminal device.

This can be used to, for example, control terminal functions like
a built-in PIN pad or biometrics.

**Parameters:** controlCode

- the control code of the command
**Parameters:** command

- the command data
**Returns:** the response from the terminal device
**Throws:** SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission
**Throws:** NullPointerException

- if command is null
**Throws:** CardException

- if the card operation failed
**Throws:** IllegalStateException

- if this card object has been disposed of
via the

disconnect()

method

---

#### transmitControlCommand

public abstract byte[] transmitControlCommand​(int controlCode,
byte[] command)
throws

CardException

Transmits a control command to the terminal device.

This can be used to, for example, control terminal functions like
a built-in PIN pad or biometrics.

This can be used to, for example, control terminal functions like
a built-in PIN pad or biometrics.

disconnect

```java
public abstract void disconnect​(boolean reset)
throws
CardException
```

Disconnects the connection with this card. After this method returns,
calling methods on this object or in CardChannels associated with this
object that require interaction with the card will raise an
IllegalStateException.

**Parameters:** reset

- whether to reset the card after disconnecting.
**Throws:** CardException

- if the card operation failed
**Throws:** SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission

---

#### disconnect

public abstract void disconnect​(boolean reset)
throws

CardException

Disconnects the connection with this card. After this method returns,
calling methods on this object or in CardChannels associated with this
object that require interaction with the card will raise an
IllegalStateException.

---

