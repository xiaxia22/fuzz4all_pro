# Class CardTerminals

**Source:** `java.smartcardio\javax\smartcardio\CardTerminals.html`

### Class Description

```java
public abstract class
CardTerminals

extends
Object
```

The set of terminals supported by a TerminalFactory.
This class allows applications to enumerate the available CardTerminals,
obtain a specific CardTerminal, or wait for the insertion or removal of
cards.

This class is multi-threading safe and can be used by multiple
threads concurrently. However, this object keeps track of the card
presence state of each of its terminals. Multiple objects should be used
if independent calls to

waitForChange()

are required.

Applications can obtain instances of this class by calling

TerminalFactory.terminals()

.

**Since:** 1.6
**See Also:** TerminalFactory

,

CardTerminal

---

### Field Details

*No entries found.*

### Constructor Details

#### protected CardTerminals()

Constructs a new CardTerminals object.

This constructor is called by subclasses only. Application should
call

TerminalFactory.terminals()

to obtain a CardTerminals object.

---

### Method Details

#### public
List
<
CardTerminal
> list()
throws
CardException

Returns an unmodifiable list of all available terminals.

**Returns:**
- an unmodifiable list of all available terminals.

**Throws:**
- CardException

- if the card operation failed

---

#### public abstract
List
<
CardTerminal
> list​(
CardTerminals.State
state)
throws
CardException

Returns an unmodifiable list of all terminals matching the specified
state.

If state is

State.ALL

, this method returns
all CardTerminals encapsulated by this object.
If state is

State.CARD_PRESENT

or

State.CARD_ABSENT

, it returns all
CardTerminals where a card is currently present or absent, respectively.

If state is

State.CARD_INSERTION

or

State.CARD_REMOVAL

, it returns all
CardTerminals for which an insertion (or removal, respectively)
was detected during the last call to

waitForChange()

.
If

waitForChange()

has not been called on this object,

CARD_INSERTION

is equivalent to

CARD_PRESENT

and

CARD_REMOVAL

is equivalent to

CARD_ABSENT

.
For an example of the use of

CARD_INSERTION

,
see

waitForChange()

.

**Parameters:**
- state

- the State

**Returns:**
- an unmodifiable list of all terminals matching the specified
state.

**Throws:**
- NullPointerException

- if state is null
- CardException

- if the card operation failed

---

#### public
CardTerminal
getTerminal​(
String
name)

Returns the terminal with the specified name or null if no such
terminal exists.

**Parameters:**
- name

- the terminal name

**Returns:**
- the terminal with the specified name or null if no such
terminal exists.

**Throws:**
- NullPointerException

- if name is null

---

#### public void waitForChange()
throws
CardException

Waits for card insertion or removal in any of the terminals of this
object.

This call is equivalent to calling

waitForChange(0)

.

**Throws:**
- IllegalStateException

- if this

CardTerminals

object does not contain any terminals
- CardException

- if the card operation failed

---

#### public abstract boolean waitForChange​(long timeout)
throws
CardException

Waits for card insertion or removal in any of the terminals of this
object or until the timeout expires.

This method examines each CardTerminal of this object.
If a card was inserted into or removed from a CardTerminal since the
previous call to

waitForChange()

, it returns
immediately.
Otherwise, or if this is the first call to

waitForChange()

on this object, it blocks until a card is inserted into or removed from
a CardTerminal.

If

timeout

is greater than 0, the method returns after

timeout

milliseconds even if there is no change in state.
In that case, this method returns

false

; otherwise it
returns

true

.

This method is often used in a loop in combination with

list(State.CARD_INSERTION)

,
for example:

```java
TerminalFactory factory = ...;
CardTerminals terminals = factory.terminals();
while (true) {
for (CardTerminal terminal : terminals.list(CARD_INSERTION)) {
// examine Card in terminal, return if it matches
}
terminals.waitForChange();
}
```

**Parameters:**
- timeout

- if positive, block for up to

timeout

milliseconds; if zero, block indefinitely; must not be negative

**Returns:**
- false if the method returns due to an expired timeout,
true otherwise.

**Throws:**
- IllegalStateException

- if this

CardTerminals

object does not contain any terminals
- IllegalArgumentException

- if timeout is negative
- CardException

- if the card operation failed

---

### Additional Sections

#### Class CardTerminals

java.lang.Object

- javax.smartcardio.CardTerminals

javax.smartcardio.CardTerminals

```java
public abstract class
CardTerminals

extends
Object
```

The set of terminals supported by a TerminalFactory.
This class allows applications to enumerate the available CardTerminals,
obtain a specific CardTerminal, or wait for the insertion or removal of
cards.

This class is multi-threading safe and can be used by multiple
threads concurrently. However, this object keeps track of the card
presence state of each of its terminals. Multiple objects should be used
if independent calls to

waitForChange()

are required.

Applications can obtain instances of this class by calling

TerminalFactory.terminals()

.

**Since:** 1.6
**See Also:** TerminalFactory

,

CardTerminal

public abstract class

CardTerminals

extends

Object

The set of terminals supported by a TerminalFactory.
This class allows applications to enumerate the available CardTerminals,
obtain a specific CardTerminal, or wait for the insertion or removal of
cards.

This class is multi-threading safe and can be used by multiple
threads concurrently. However, this object keeps track of the card
presence state of each of its terminals. Multiple objects should be used
if independent calls to

waitForChange()

are required.

Applications can obtain instances of this class by calling

TerminalFactory.terminals()

.

This class is multi-threading safe and can be used by multiple
threads concurrently. However, this object keeps track of the card
presence state of each of its terminals. Multiple objects should be used
if independent calls to

waitForChange()

are required.

Applications can obtain instances of this class by calling

TerminalFactory.terminals()

.

Applications can obtain instances of this class by calling

TerminalFactory.terminals()

.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

CardTerminals.State

Enumeration of attributes of a CardTerminal.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CardTerminals

()

Constructs a new CardTerminals object.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

CardTerminal

getTerminal

​(

String

name)

Returns the terminal with the specified name or null if no such
terminal exists.

List

<

CardTerminal

>

list

()

Returns an unmodifiable list of all available terminals.

abstract

List

<

CardTerminal

>

list

​(

CardTerminals.State

state)

Returns an unmodifiable list of all terminals matching the specified
state.

void

waitForChange

()

Waits for card insertion or removal in any of the terminals of this
object.

abstract boolean

waitForChange

​(long timeout)

Waits for card insertion or removal in any of the terminals of this
object or until the timeout expires.

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

CardTerminals.State

Enumeration of attributes of a CardTerminal.

---

#### Nested Class Summary

Enumeration of attributes of a CardTerminal.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

CardTerminals

()

Constructs a new CardTerminals object.

---

#### Constructor Summary

Constructs a new CardTerminals object.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

CardTerminal

getTerminal

​(

String

name)

Returns the terminal with the specified name or null if no such
terminal exists.

List

<

CardTerminal

>

list

()

Returns an unmodifiable list of all available terminals.

abstract

List

<

CardTerminal

>

list

​(

CardTerminals.State

state)

Returns an unmodifiable list of all terminals matching the specified
state.

void

waitForChange

()

Waits for card insertion or removal in any of the terminals of this
object.

abstract boolean

waitForChange

​(long timeout)

Waits for card insertion or removal in any of the terminals of this
object or until the timeout expires.

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

Returns the terminal with the specified name or null if no such
terminal exists.

Returns an unmodifiable list of all available terminals.

Returns an unmodifiable list of all terminals matching the specified
state.

Waits for card insertion or removal in any of the terminals of this
object.

Waits for card insertion or removal in any of the terminals of this
object or until the timeout expires.

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

- CardTerminals

```java
protected CardTerminals()
```

Constructs a new CardTerminals object.

This constructor is called by subclasses only. Application should
call

TerminalFactory.terminals()

to obtain a CardTerminals object.

============ METHOD DETAIL ==========

- Method Detail

- list

```java
public
List
<
CardTerminal
> list()
throws
CardException
```

Returns an unmodifiable list of all available terminals.

**Returns:** an unmodifiable list of all available terminals.
**Throws:** CardException

- if the card operation failed

- list

```java
public abstract
List
<
CardTerminal
> list​(
CardTerminals.State
state)
throws
CardException
```

Returns an unmodifiable list of all terminals matching the specified
state.

If state is

State.ALL

, this method returns
all CardTerminals encapsulated by this object.
If state is

State.CARD_PRESENT

or

State.CARD_ABSENT

, it returns all
CardTerminals where a card is currently present or absent, respectively.

If state is

State.CARD_INSERTION

or

State.CARD_REMOVAL

, it returns all
CardTerminals for which an insertion (or removal, respectively)
was detected during the last call to

waitForChange()

.
If

waitForChange()

has not been called on this object,

CARD_INSERTION

is equivalent to

CARD_PRESENT

and

CARD_REMOVAL

is equivalent to

CARD_ABSENT

.
For an example of the use of

CARD_INSERTION

,
see

waitForChange()

.

**Parameters:** state

- the State
**Returns:** an unmodifiable list of all terminals matching the specified
state.
**Throws:** NullPointerException

- if state is null
**Throws:** CardException

- if the card operation failed

- getTerminal

```java
public
CardTerminal
getTerminal​(
String
name)
```

Returns the terminal with the specified name or null if no such
terminal exists.

**Parameters:** name

- the terminal name
**Returns:** the terminal with the specified name or null if no such
terminal exists.
**Throws:** NullPointerException

- if name is null

- waitForChange

```java
public void waitForChange()
throws
CardException
```

Waits for card insertion or removal in any of the terminals of this
object.

This call is equivalent to calling

waitForChange(0)

.

**Throws:** IllegalStateException

- if this

CardTerminals

object does not contain any terminals
**Throws:** CardException

- if the card operation failed

- waitForChange

```java
public abstract boolean waitForChange​(long timeout)
throws
CardException
```

Waits for card insertion or removal in any of the terminals of this
object or until the timeout expires.

This method examines each CardTerminal of this object.
If a card was inserted into or removed from a CardTerminal since the
previous call to

waitForChange()

, it returns
immediately.
Otherwise, or if this is the first call to

waitForChange()

on this object, it blocks until a card is inserted into or removed from
a CardTerminal.

If

timeout

is greater than 0, the method returns after

timeout

milliseconds even if there is no change in state.
In that case, this method returns

false

; otherwise it
returns

true

.

This method is often used in a loop in combination with

list(State.CARD_INSERTION)

,
for example:

```java
TerminalFactory factory = ...;
CardTerminals terminals = factory.terminals();
while (true) {
for (CardTerminal terminal : terminals.list(CARD_INSERTION)) {
// examine Card in terminal, return if it matches
}
terminals.waitForChange();
}
```

**Parameters:** timeout

- if positive, block for up to

timeout

milliseconds; if zero, block indefinitely; must not be negative
**Returns:** false if the method returns due to an expired timeout,
true otherwise.
**Throws:** IllegalStateException

- if this

CardTerminals

object does not contain any terminals
**Throws:** IllegalArgumentException

- if timeout is negative
**Throws:** CardException

- if the card operation failed

Constructor Detail

- CardTerminals

```java
protected CardTerminals()
```

Constructs a new CardTerminals object.

This constructor is called by subclasses only. Application should
call

TerminalFactory.terminals()

to obtain a CardTerminals object.

---

#### Constructor Detail

CardTerminals

```java
protected CardTerminals()
```

Constructs a new CardTerminals object.

This constructor is called by subclasses only. Application should
call

TerminalFactory.terminals()

to obtain a CardTerminals object.

---

#### CardTerminals

protected CardTerminals()

Constructs a new CardTerminals object.

This constructor is called by subclasses only. Application should
call

TerminalFactory.terminals()

to obtain a CardTerminals object.

This constructor is called by subclasses only. Application should
call

TerminalFactory.terminals()

to obtain a CardTerminals object.

Method Detail

- list

```java
public
List
<
CardTerminal
> list()
throws
CardException
```

Returns an unmodifiable list of all available terminals.

**Returns:** an unmodifiable list of all available terminals.
**Throws:** CardException

- if the card operation failed

- list

```java
public abstract
List
<
CardTerminal
> list​(
CardTerminals.State
state)
throws
CardException
```

Returns an unmodifiable list of all terminals matching the specified
state.

If state is

State.ALL

, this method returns
all CardTerminals encapsulated by this object.
If state is

State.CARD_PRESENT

or

State.CARD_ABSENT

, it returns all
CardTerminals where a card is currently present or absent, respectively.

If state is

State.CARD_INSERTION

or

State.CARD_REMOVAL

, it returns all
CardTerminals for which an insertion (or removal, respectively)
was detected during the last call to

waitForChange()

.
If

waitForChange()

has not been called on this object,

CARD_INSERTION

is equivalent to

CARD_PRESENT

and

CARD_REMOVAL

is equivalent to

CARD_ABSENT

.
For an example of the use of

CARD_INSERTION

,
see

waitForChange()

.

**Parameters:** state

- the State
**Returns:** an unmodifiable list of all terminals matching the specified
state.
**Throws:** NullPointerException

- if state is null
**Throws:** CardException

- if the card operation failed

- getTerminal

```java
public
CardTerminal
getTerminal​(
String
name)
```

Returns the terminal with the specified name or null if no such
terminal exists.

**Parameters:** name

- the terminal name
**Returns:** the terminal with the specified name or null if no such
terminal exists.
**Throws:** NullPointerException

- if name is null

- waitForChange

```java
public void waitForChange()
throws
CardException
```

Waits for card insertion or removal in any of the terminals of this
object.

This call is equivalent to calling

waitForChange(0)

.

**Throws:** IllegalStateException

- if this

CardTerminals

object does not contain any terminals
**Throws:** CardException

- if the card operation failed

- waitForChange

```java
public abstract boolean waitForChange​(long timeout)
throws
CardException
```

Waits for card insertion or removal in any of the terminals of this
object or until the timeout expires.

This method examines each CardTerminal of this object.
If a card was inserted into or removed from a CardTerminal since the
previous call to

waitForChange()

, it returns
immediately.
Otherwise, or if this is the first call to

waitForChange()

on this object, it blocks until a card is inserted into or removed from
a CardTerminal.

If

timeout

is greater than 0, the method returns after

timeout

milliseconds even if there is no change in state.
In that case, this method returns

false

; otherwise it
returns

true

.

This method is often used in a loop in combination with

list(State.CARD_INSERTION)

,
for example:

```java
TerminalFactory factory = ...;
CardTerminals terminals = factory.terminals();
while (true) {
for (CardTerminal terminal : terminals.list(CARD_INSERTION)) {
// examine Card in terminal, return if it matches
}
terminals.waitForChange();
}
```

**Parameters:** timeout

- if positive, block for up to

timeout

milliseconds; if zero, block indefinitely; must not be negative
**Returns:** false if the method returns due to an expired timeout,
true otherwise.
**Throws:** IllegalStateException

- if this

CardTerminals

object does not contain any terminals
**Throws:** IllegalArgumentException

- if timeout is negative
**Throws:** CardException

- if the card operation failed

---

#### Method Detail

list

```java
public
List
<
CardTerminal
> list()
throws
CardException
```

Returns an unmodifiable list of all available terminals.

**Returns:** an unmodifiable list of all available terminals.
**Throws:** CardException

- if the card operation failed

---

#### list

public

List

<

CardTerminal

> list()
throws

CardException

Returns an unmodifiable list of all available terminals.

list

```java
public abstract
List
<
CardTerminal
> list​(
CardTerminals.State
state)
throws
CardException
```

Returns an unmodifiable list of all terminals matching the specified
state.

If state is

State.ALL

, this method returns
all CardTerminals encapsulated by this object.
If state is

State.CARD_PRESENT

or

State.CARD_ABSENT

, it returns all
CardTerminals where a card is currently present or absent, respectively.

If state is

State.CARD_INSERTION

or

State.CARD_REMOVAL

, it returns all
CardTerminals for which an insertion (or removal, respectively)
was detected during the last call to

waitForChange()

.
If

waitForChange()

has not been called on this object,

CARD_INSERTION

is equivalent to

CARD_PRESENT

and

CARD_REMOVAL

is equivalent to

CARD_ABSENT

.
For an example of the use of

CARD_INSERTION

,
see

waitForChange()

.

**Parameters:** state

- the State
**Returns:** an unmodifiable list of all terminals matching the specified
state.
**Throws:** NullPointerException

- if state is null
**Throws:** CardException

- if the card operation failed

---

#### list

public abstract

List

<

CardTerminal

> list​(

CardTerminals.State

state)
throws

CardException

Returns an unmodifiable list of all terminals matching the specified
state.

If state is

State.ALL

, this method returns
all CardTerminals encapsulated by this object.
If state is

State.CARD_PRESENT

or

State.CARD_ABSENT

, it returns all
CardTerminals where a card is currently present or absent, respectively.

If state is

State.CARD_INSERTION

or

State.CARD_REMOVAL

, it returns all
CardTerminals for which an insertion (or removal, respectively)
was detected during the last call to

waitForChange()

.
If

waitForChange()

has not been called on this object,

CARD_INSERTION

is equivalent to

CARD_PRESENT

and

CARD_REMOVAL

is equivalent to

CARD_ABSENT

.
For an example of the use of

CARD_INSERTION

,
see

waitForChange()

.

If state is

State.ALL

, this method returns
all CardTerminals encapsulated by this object.
If state is

State.CARD_PRESENT

or

State.CARD_ABSENT

, it returns all
CardTerminals where a card is currently present or absent, respectively.

If state is

State.CARD_INSERTION

or

State.CARD_REMOVAL

, it returns all
CardTerminals for which an insertion (or removal, respectively)
was detected during the last call to

waitForChange()

.
If

waitForChange()

has not been called on this object,

CARD_INSERTION

is equivalent to

CARD_PRESENT

and

CARD_REMOVAL

is equivalent to

CARD_ABSENT

.
For an example of the use of

CARD_INSERTION

,
see

waitForChange()

.

If state is

State.CARD_INSERTION

or

State.CARD_REMOVAL

, it returns all
CardTerminals for which an insertion (or removal, respectively)
was detected during the last call to

waitForChange()

.
If

waitForChange()

has not been called on this object,

CARD_INSERTION

is equivalent to

CARD_PRESENT

and

CARD_REMOVAL

is equivalent to

CARD_ABSENT

.
For an example of the use of

CARD_INSERTION

,
see

waitForChange()

.

getTerminal

```java
public
CardTerminal
getTerminal​(
String
name)
```

Returns the terminal with the specified name or null if no such
terminal exists.

**Parameters:** name

- the terminal name
**Returns:** the terminal with the specified name or null if no such
terminal exists.
**Throws:** NullPointerException

- if name is null

---

#### getTerminal

public

CardTerminal

getTerminal​(

String

name)

Returns the terminal with the specified name or null if no such
terminal exists.

waitForChange

```java
public void waitForChange()
throws
CardException
```

Waits for card insertion or removal in any of the terminals of this
object.

This call is equivalent to calling

waitForChange(0)

.

**Throws:** IllegalStateException

- if this

CardTerminals

object does not contain any terminals
**Throws:** CardException

- if the card operation failed

---

#### waitForChange

public void waitForChange()
throws

CardException

Waits for card insertion or removal in any of the terminals of this
object.

This call is equivalent to calling

waitForChange(0)

.

This call is equivalent to calling

waitForChange(0)

.

waitForChange

```java
public abstract boolean waitForChange​(long timeout)
throws
CardException
```

Waits for card insertion or removal in any of the terminals of this
object or until the timeout expires.

This method examines each CardTerminal of this object.
If a card was inserted into or removed from a CardTerminal since the
previous call to

waitForChange()

, it returns
immediately.
Otherwise, or if this is the first call to

waitForChange()

on this object, it blocks until a card is inserted into or removed from
a CardTerminal.

If

timeout

is greater than 0, the method returns after

timeout

milliseconds even if there is no change in state.
In that case, this method returns

false

; otherwise it
returns

true

.

This method is often used in a loop in combination with

list(State.CARD_INSERTION)

,
for example:

```java
TerminalFactory factory = ...;
CardTerminals terminals = factory.terminals();
while (true) {
for (CardTerminal terminal : terminals.list(CARD_INSERTION)) {
// examine Card in terminal, return if it matches
}
terminals.waitForChange();
}
```

**Parameters:** timeout

- if positive, block for up to

timeout

milliseconds; if zero, block indefinitely; must not be negative
**Returns:** false if the method returns due to an expired timeout,
true otherwise.
**Throws:** IllegalStateException

- if this

CardTerminals

object does not contain any terminals
**Throws:** IllegalArgumentException

- if timeout is negative
**Throws:** CardException

- if the card operation failed

---

#### waitForChange

public abstract boolean waitForChange​(long timeout)
throws

CardException

Waits for card insertion or removal in any of the terminals of this
object or until the timeout expires.

This method examines each CardTerminal of this object.
If a card was inserted into or removed from a CardTerminal since the
previous call to

waitForChange()

, it returns
immediately.
Otherwise, or if this is the first call to

waitForChange()

on this object, it blocks until a card is inserted into or removed from
a CardTerminal.

If

timeout

is greater than 0, the method returns after

timeout

milliseconds even if there is no change in state.
In that case, this method returns

false

; otherwise it
returns

true

.

This method is often used in a loop in combination with

list(State.CARD_INSERTION)

,
for example:

```java
TerminalFactory factory = ...;
CardTerminals terminals = factory.terminals();
while (true) {
for (CardTerminal terminal : terminals.list(CARD_INSERTION)) {
// examine Card in terminal, return if it matches
}
terminals.waitForChange();
}
```

This method examines each CardTerminal of this object.
If a card was inserted into or removed from a CardTerminal since the
previous call to

waitForChange()

, it returns
immediately.
Otherwise, or if this is the first call to

waitForChange()

on this object, it blocks until a card is inserted into or removed from
a CardTerminal.

If

timeout

is greater than 0, the method returns after

timeout

milliseconds even if there is no change in state.
In that case, this method returns

false

; otherwise it
returns

true

.

This method is often used in a loop in combination with

list(State.CARD_INSERTION)

,
for example:

```java
TerminalFactory factory = ...;
CardTerminals terminals = factory.terminals();
while (true) {
for (CardTerminal terminal : terminals.list(CARD_INSERTION)) {
// examine Card in terminal, return if it matches
}
terminals.waitForChange();
}
```

If

timeout

is greater than 0, the method returns after

timeout

milliseconds even if there is no change in state.
In that case, this method returns

false

; otherwise it
returns

true

.

This method is often used in a loop in combination with

list(State.CARD_INSERTION)

,
for example:

```java
TerminalFactory factory = ...;
CardTerminals terminals = factory.terminals();
while (true) {
for (CardTerminal terminal : terminals.list(CARD_INSERTION)) {
// examine Card in terminal, return if it matches
}
terminals.waitForChange();
}
```

This method is often used in a loop in combination with

list(State.CARD_INSERTION)

,
for example:

```java
TerminalFactory factory = ...;
CardTerminals terminals = factory.terminals();
while (true) {
for (CardTerminal terminal : terminals.list(CARD_INSERTION)) {
// examine Card in terminal, return if it matches
}
terminals.waitForChange();
}
```

TerminalFactory factory = ...;
CardTerminals terminals = factory.terminals();
while (true) {
for (CardTerminal terminal : terminals.list(CARD_INSERTION)) {
// examine Card in terminal, return if it matches
}
terminals.waitForChange();
}

---

