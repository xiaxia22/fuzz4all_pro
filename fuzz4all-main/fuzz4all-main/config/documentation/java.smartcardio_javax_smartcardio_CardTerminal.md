# Class CardTerminal

**Source:** `java.smartcardio\javax\smartcardio\CardTerminal.html`

### Class Description

```java
public abstract class
CardTerminal

extends
Object
```

A Smart Card terminal, sometimes referred to as a Smart Card Reader.
A CardTerminal object can be obtained by calling

CardTerminals.list()

or

CardTerminals.getTerminal()

.

Note that physical card readers with slots for multiple cards are
represented by one

CardTerminal

object per such slot.

**Since:** 1.6
**See Also:** CardTerminals

,

TerminalFactory

---

### Field Details

*No entries found.*

### Constructor Details

#### protected CardTerminal()

Constructs a new CardTerminal object.

This constructor is called by subclasses only. Application should
call

list()

or

getTerminal()

to obtain a CardTerminal object.

---

### Method Details

#### public abstract
String
getName()

Returns the unique name of this terminal.

**Returns:**
- the unique name of this terminal.

---

#### public abstract
Card
connect​(
String
protocol)
throws
CardException

Establishes a connection to the card.
If a connection has previously established using
the specified protocol, this method returns the same Card object as
the previous call.

**Parameters:**
- protocol

- the protocol to use ("T=0", "T=1", or "T=CL"), or "*" to
connect using any available protocol.

**Returns:**
- the card the connection has been established with

**Throws:**
- NullPointerException

- if protocol is null
- IllegalArgumentException

- if protocol is an invalid protocol
specification
- CardNotPresentException

- if no card is present in this terminal
- CardException

- if a connection could not be established
using the specified protocol or if a connection has previously been
established using a different protocol
- SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission

---

#### public abstract boolean isCardPresent()
throws
CardException

Returns whether a card is present in this terminal.

**Returns:**
- whether a card is present in this terminal.

**Throws:**
- CardException

- if the status could not be determined

---

#### public abstract boolean waitForCardPresent​(long timeout)
throws
CardException

Waits until a card is present in this terminal or the timeout
expires. If the method returns due to an expired timeout, it returns
false. Otherwise it return true.

If a card is present in this terminal when this
method is called, it returns immediately.

**Parameters:**
- timeout

- if positive, block for up to

timeout

milliseconds; if zero, block indefinitely; must not be negative

**Returns:**
- false if the method returns due to an expired timeout,
true otherwise.

**Throws:**
- IllegalArgumentException

- if timeout is negative
- CardException

- if the operation failed

---

#### public abstract boolean waitForCardAbsent​(long timeout)
throws
CardException

Waits until a card is absent in this terminal or the timeout
expires. If the method returns due to an expired timeout, it returns
false. Otherwise it return true.

If no card is present in this terminal when this
method is called, it returns immediately.

**Parameters:**
- timeout

- if positive, block for up to

timeout

milliseconds; if zero, block indefinitely; must not be negative

**Returns:**
- false if the method returns due to an expired timeout,
true otherwise.

**Throws:**
- IllegalArgumentException

- if timeout is negative
- CardException

- if the operation failed

---

### Additional Sections

#### Class CardTerminal

java.lang.Object

- javax.smartcardio.CardTerminal

javax.smartcardio.CardTerminal

```java
public abstract class
CardTerminal

extends
Object
```

A Smart Card terminal, sometimes referred to as a Smart Card Reader.
A CardTerminal object can be obtained by calling

CardTerminals.list()

or

CardTerminals.getTerminal()

.

Note that physical card readers with slots for multiple cards are
represented by one

CardTerminal

object per such slot.

**Since:** 1.6
**See Also:** CardTerminals

,

TerminalFactory

public abstract class

CardTerminal

extends

Object

A Smart Card terminal, sometimes referred to as a Smart Card Reader.
A CardTerminal object can be obtained by calling

CardTerminals.list()

or

CardTerminals.getTerminal()

.

Note that physical card readers with slots for multiple cards are
represented by one

CardTerminal

object per such slot.

Note that physical card readers with slots for multiple cards are
represented by one

CardTerminal

object per such slot.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CardTerminal

()

Constructs a new CardTerminal object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Card

connect

​(

String

protocol)

Establishes a connection to the card.

abstract

String

getName

()

Returns the unique name of this terminal.

abstract boolean

isCardPresent

()

Returns whether a card is present in this terminal.

abstract boolean

waitForCardAbsent

​(long timeout)

Waits until a card is absent in this terminal or the timeout
expires.

abstract boolean

waitForCardPresent

​(long timeout)

Waits until a card is present in this terminal or the timeout
expires.

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

CardTerminal

()

Constructs a new CardTerminal object.

---

#### Constructor Summary

Constructs a new CardTerminal object.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

abstract

Card

connect

​(

String

protocol)

Establishes a connection to the card.

abstract

String

getName

()

Returns the unique name of this terminal.

abstract boolean

isCardPresent

()

Returns whether a card is present in this terminal.

abstract boolean

waitForCardAbsent

​(long timeout)

Waits until a card is absent in this terminal or the timeout
expires.

abstract boolean

waitForCardPresent

​(long timeout)

Waits until a card is present in this terminal or the timeout
expires.

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

Establishes a connection to the card.

Returns the unique name of this terminal.

Returns whether a card is present in this terminal.

Waits until a card is absent in this terminal or the timeout
expires.

Waits until a card is present in this terminal or the timeout
expires.

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

- CardTerminal

```java
protected CardTerminal()
```

Constructs a new CardTerminal object.

This constructor is called by subclasses only. Application should
call

list()

or

getTerminal()

to obtain a CardTerminal object.

============ METHOD DETAIL ==========

- Method Detail

- getName

```java
public abstract
String
getName()
```

Returns the unique name of this terminal.

**Returns:** the unique name of this terminal.

- connect

```java
public abstract
Card
connect​(
String
protocol)
throws
CardException
```

Establishes a connection to the card.
If a connection has previously established using
the specified protocol, this method returns the same Card object as
the previous call.

**Parameters:** protocol

- the protocol to use ("T=0", "T=1", or "T=CL"), or "*" to
connect using any available protocol.
**Returns:** the card the connection has been established with
**Throws:** NullPointerException

- if protocol is null
**Throws:** IllegalArgumentException

- if protocol is an invalid protocol
specification
**Throws:** CardNotPresentException

- if no card is present in this terminal
**Throws:** CardException

- if a connection could not be established
using the specified protocol or if a connection has previously been
established using a different protocol
**Throws:** SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission

- isCardPresent

```java
public abstract boolean isCardPresent()
throws
CardException
```

Returns whether a card is present in this terminal.

**Returns:** whether a card is present in this terminal.
**Throws:** CardException

- if the status could not be determined

- waitForCardPresent

```java
public abstract boolean waitForCardPresent​(long timeout)
throws
CardException
```

Waits until a card is present in this terminal or the timeout
expires. If the method returns due to an expired timeout, it returns
false. Otherwise it return true.

If a card is present in this terminal when this
method is called, it returns immediately.

**Parameters:** timeout

- if positive, block for up to

timeout

milliseconds; if zero, block indefinitely; must not be negative
**Returns:** false if the method returns due to an expired timeout,
true otherwise.
**Throws:** IllegalArgumentException

- if timeout is negative
**Throws:** CardException

- if the operation failed

- waitForCardAbsent

```java
public abstract boolean waitForCardAbsent​(long timeout)
throws
CardException
```

Waits until a card is absent in this terminal or the timeout
expires. If the method returns due to an expired timeout, it returns
false. Otherwise it return true.

If no card is present in this terminal when this
method is called, it returns immediately.

**Parameters:** timeout

- if positive, block for up to

timeout

milliseconds; if zero, block indefinitely; must not be negative
**Returns:** false if the method returns due to an expired timeout,
true otherwise.
**Throws:** IllegalArgumentException

- if timeout is negative
**Throws:** CardException

- if the operation failed

Constructor Detail

- CardTerminal

```java
protected CardTerminal()
```

Constructs a new CardTerminal object.

This constructor is called by subclasses only. Application should
call

list()

or

getTerminal()

to obtain a CardTerminal object.

---

#### Constructor Detail

CardTerminal

```java
protected CardTerminal()
```

Constructs a new CardTerminal object.

This constructor is called by subclasses only. Application should
call

list()

or

getTerminal()

to obtain a CardTerminal object.

---

#### CardTerminal

protected CardTerminal()

Constructs a new CardTerminal object.

This constructor is called by subclasses only. Application should
call

list()

or

getTerminal()

to obtain a CardTerminal object.

This constructor is called by subclasses only. Application should
call

list()

or

getTerminal()

to obtain a CardTerminal object.

Method Detail

- getName

```java
public abstract
String
getName()
```

Returns the unique name of this terminal.

**Returns:** the unique name of this terminal.

- connect

```java
public abstract
Card
connect​(
String
protocol)
throws
CardException
```

Establishes a connection to the card.
If a connection has previously established using
the specified protocol, this method returns the same Card object as
the previous call.

**Parameters:** protocol

- the protocol to use ("T=0", "T=1", or "T=CL"), or "*" to
connect using any available protocol.
**Returns:** the card the connection has been established with
**Throws:** NullPointerException

- if protocol is null
**Throws:** IllegalArgumentException

- if protocol is an invalid protocol
specification
**Throws:** CardNotPresentException

- if no card is present in this terminal
**Throws:** CardException

- if a connection could not be established
using the specified protocol or if a connection has previously been
established using a different protocol
**Throws:** SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission

- isCardPresent

```java
public abstract boolean isCardPresent()
throws
CardException
```

Returns whether a card is present in this terminal.

**Returns:** whether a card is present in this terminal.
**Throws:** CardException

- if the status could not be determined

- waitForCardPresent

```java
public abstract boolean waitForCardPresent​(long timeout)
throws
CardException
```

Waits until a card is present in this terminal or the timeout
expires. If the method returns due to an expired timeout, it returns
false. Otherwise it return true.

If a card is present in this terminal when this
method is called, it returns immediately.

**Parameters:** timeout

- if positive, block for up to

timeout

milliseconds; if zero, block indefinitely; must not be negative
**Returns:** false if the method returns due to an expired timeout,
true otherwise.
**Throws:** IllegalArgumentException

- if timeout is negative
**Throws:** CardException

- if the operation failed

- waitForCardAbsent

```java
public abstract boolean waitForCardAbsent​(long timeout)
throws
CardException
```

Waits until a card is absent in this terminal or the timeout
expires. If the method returns due to an expired timeout, it returns
false. Otherwise it return true.

If no card is present in this terminal when this
method is called, it returns immediately.

**Parameters:** timeout

- if positive, block for up to

timeout

milliseconds; if zero, block indefinitely; must not be negative
**Returns:** false if the method returns due to an expired timeout,
true otherwise.
**Throws:** IllegalArgumentException

- if timeout is negative
**Throws:** CardException

- if the operation failed

---

#### Method Detail

getName

```java
public abstract
String
getName()
```

Returns the unique name of this terminal.

**Returns:** the unique name of this terminal.

---

#### getName

public abstract

String

getName()

Returns the unique name of this terminal.

connect

```java
public abstract
Card
connect​(
String
protocol)
throws
CardException
```

Establishes a connection to the card.
If a connection has previously established using
the specified protocol, this method returns the same Card object as
the previous call.

**Parameters:** protocol

- the protocol to use ("T=0", "T=1", or "T=CL"), or "*" to
connect using any available protocol.
**Returns:** the card the connection has been established with
**Throws:** NullPointerException

- if protocol is null
**Throws:** IllegalArgumentException

- if protocol is an invalid protocol
specification
**Throws:** CardNotPresentException

- if no card is present in this terminal
**Throws:** CardException

- if a connection could not be established
using the specified protocol or if a connection has previously been
established using a different protocol
**Throws:** SecurityException

- if a SecurityManager exists and the
caller does not have the required

permission

---

#### connect

public abstract

Card

connect​(

String

protocol)
throws

CardException

Establishes a connection to the card.
If a connection has previously established using
the specified protocol, this method returns the same Card object as
the previous call.

isCardPresent

```java
public abstract boolean isCardPresent()
throws
CardException
```

Returns whether a card is present in this terminal.

**Returns:** whether a card is present in this terminal.
**Throws:** CardException

- if the status could not be determined

---

#### isCardPresent

public abstract boolean isCardPresent()
throws

CardException

Returns whether a card is present in this terminal.

waitForCardPresent

```java
public abstract boolean waitForCardPresent​(long timeout)
throws
CardException
```

Waits until a card is present in this terminal or the timeout
expires. If the method returns due to an expired timeout, it returns
false. Otherwise it return true.

If a card is present in this terminal when this
method is called, it returns immediately.

**Parameters:** timeout

- if positive, block for up to

timeout

milliseconds; if zero, block indefinitely; must not be negative
**Returns:** false if the method returns due to an expired timeout,
true otherwise.
**Throws:** IllegalArgumentException

- if timeout is negative
**Throws:** CardException

- if the operation failed

---

#### waitForCardPresent

public abstract boolean waitForCardPresent​(long timeout)
throws

CardException

Waits until a card is present in this terminal or the timeout
expires. If the method returns due to an expired timeout, it returns
false. Otherwise it return true.

If a card is present in this terminal when this
method is called, it returns immediately.

If a card is present in this terminal when this
method is called, it returns immediately.

waitForCardAbsent

```java
public abstract boolean waitForCardAbsent​(long timeout)
throws
CardException
```

Waits until a card is absent in this terminal or the timeout
expires. If the method returns due to an expired timeout, it returns
false. Otherwise it return true.

If no card is present in this terminal when this
method is called, it returns immediately.

**Parameters:** timeout

- if positive, block for up to

timeout

milliseconds; if zero, block indefinitely; must not be negative
**Returns:** false if the method returns due to an expired timeout,
true otherwise.
**Throws:** IllegalArgumentException

- if timeout is negative
**Throws:** CardException

- if the operation failed

---

#### waitForCardAbsent

public abstract boolean waitForCardAbsent​(long timeout)
throws

CardException

Waits until a card is absent in this terminal or the timeout
expires. If the method returns due to an expired timeout, it returns
false. Otherwise it return true.

If no card is present in this terminal when this
method is called, it returns immediately.

If no card is present in this terminal when this
method is called, it returns immediately.

---

