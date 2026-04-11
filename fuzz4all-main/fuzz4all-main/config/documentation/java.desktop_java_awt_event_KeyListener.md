# Interface KeyListener

**Source:** `java.desktop\java\awt\event\KeyListener.html`

### Class Description

```java
public interface
KeyListener

extends
EventListener
```

The listener interface for receiving keyboard events (keystrokes).
The class that is interested in processing a keyboard event
either implements this interface (and all the methods it
contains) or extends the abstract

KeyAdapter

class
(overriding only the methods of interest).

The listener object created from that class is then registered with a
component using the component's

addKeyListener

method. A keyboard event is generated when a key is pressed, released,
or typed. The relevant method in the listener
object is then invoked, and the

KeyEvent

is passed to it.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void keyTyped​(
KeyEvent
e)

Invoked when a key has been typed.
See the class description for

KeyEvent

for a definition of
a key typed event.

**Parameters:**
- e

- the event to be processed

---

#### void keyPressed​(
KeyEvent
e)

Invoked when a key has been pressed.
See the class description for

KeyEvent

for a definition of
a key pressed event.

**Parameters:**
- e

- the event to be processed

---

#### void keyReleased​(
KeyEvent
e)

Invoked when a key has been released.
See the class description for

KeyEvent

for a definition of
a key released event.

**Parameters:**
- e

- the event to be processed

---

### Additional Sections

#### Interface KeyListener

**All Superinterfaces:** EventListener

**All Known Implementing Classes:** AWTEventMulticaster

,

BasicComboBoxUI.KeyHandler

,

BasicComboPopup.InvocationKeyHandler

,

BasicTableUI.KeyHandler

,

BasicTreeUI.KeyHandler

,

KeyAdapter

```java
public interface
KeyListener

extends
EventListener
```

The listener interface for receiving keyboard events (keystrokes).
The class that is interested in processing a keyboard event
either implements this interface (and all the methods it
contains) or extends the abstract

KeyAdapter

class
(overriding only the methods of interest).

The listener object created from that class is then registered with a
component using the component's

addKeyListener

method. A keyboard event is generated when a key is pressed, released,
or typed. The relevant method in the listener
object is then invoked, and the

KeyEvent

is passed to it.

**Since:** 1.1
**See Also:** KeyAdapter

,

KeyEvent

,

Tutorial: Writing a Key Listener

public interface

KeyListener

extends

EventListener

The listener interface for receiving keyboard events (keystrokes).
The class that is interested in processing a keyboard event
either implements this interface (and all the methods it
contains) or extends the abstract

KeyAdapter

class
(overriding only the methods of interest).

The listener object created from that class is then registered with a
component using the component's

addKeyListener

method. A keyboard event is generated when a key is pressed, released,
or typed. The relevant method in the listener
object is then invoked, and the

KeyEvent

is passed to it.

The listener object created from that class is then registered with a
component using the component's

addKeyListener

method. A keyboard event is generated when a key is pressed, released,
or typed. The relevant method in the listener
object is then invoked, and the

KeyEvent

is passed to it.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

keyPressed

​(

KeyEvent

e)

Invoked when a key has been pressed.

void

keyReleased

​(

KeyEvent

e)

Invoked when a key has been released.

void

keyTyped

​(

KeyEvent

e)

Invoked when a key has been typed.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

keyPressed

​(

KeyEvent

e)

Invoked when a key has been pressed.

void

keyReleased

​(

KeyEvent

e)

Invoked when a key has been released.

void

keyTyped

​(

KeyEvent

e)

Invoked when a key has been typed.

---

#### Method Summary

Invoked when a key has been pressed.

Invoked when a key has been released.

Invoked when a key has been typed.

============ METHOD DETAIL ==========

- Method Detail

- keyTyped

```java
void keyTyped​(
KeyEvent
e)
```

Invoked when a key has been typed.
See the class description for

KeyEvent

for a definition of
a key typed event.

**Parameters:** e

- the event to be processed

- keyPressed

```java
void keyPressed​(
KeyEvent
e)
```

Invoked when a key has been pressed.
See the class description for

KeyEvent

for a definition of
a key pressed event.

**Parameters:** e

- the event to be processed

- keyReleased

```java
void keyReleased​(
KeyEvent
e)
```

Invoked when a key has been released.
See the class description for

KeyEvent

for a definition of
a key released event.

**Parameters:** e

- the event to be processed

Method Detail

- keyTyped

```java
void keyTyped​(
KeyEvent
e)
```

Invoked when a key has been typed.
See the class description for

KeyEvent

for a definition of
a key typed event.

**Parameters:** e

- the event to be processed

- keyPressed

```java
void keyPressed​(
KeyEvent
e)
```

Invoked when a key has been pressed.
See the class description for

KeyEvent

for a definition of
a key pressed event.

**Parameters:** e

- the event to be processed

- keyReleased

```java
void keyReleased​(
KeyEvent
e)
```

Invoked when a key has been released.
See the class description for

KeyEvent

for a definition of
a key released event.

**Parameters:** e

- the event to be processed

---

#### Method Detail

keyTyped

```java
void keyTyped​(
KeyEvent
e)
```

Invoked when a key has been typed.
See the class description for

KeyEvent

for a definition of
a key typed event.

**Parameters:** e

- the event to be processed

---

#### keyTyped

void keyTyped​(

KeyEvent

e)

Invoked when a key has been typed.
See the class description for

KeyEvent

for a definition of
a key typed event.

keyPressed

```java
void keyPressed​(
KeyEvent
e)
```

Invoked when a key has been pressed.
See the class description for

KeyEvent

for a definition of
a key pressed event.

**Parameters:** e

- the event to be processed

---

#### keyPressed

void keyPressed​(

KeyEvent

e)

Invoked when a key has been pressed.
See the class description for

KeyEvent

for a definition of
a key pressed event.

keyReleased

```java
void keyReleased​(
KeyEvent
e)
```

Invoked when a key has been released.
See the class description for

KeyEvent

for a definition of
a key released event.

**Parameters:** e

- the event to be processed

---

#### keyReleased

void keyReleased​(

KeyEvent

e)

Invoked when a key has been released.
See the class description for

KeyEvent

for a definition of
a key released event.

---

