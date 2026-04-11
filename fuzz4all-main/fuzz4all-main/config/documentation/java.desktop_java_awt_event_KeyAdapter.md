# Class KeyAdapter

**Source:** `java.desktop\java\awt\event\KeyAdapter.html`

### Class Description

```java
public abstract class
KeyAdapter

extends
Object

implements
KeyListener
```

An abstract adapter class for receiving keyboard events.
The methods in this class are empty. This class exists as
convenience for creating listener objects.

Extend this class to create a

KeyEvent

listener
and override the methods for the events of interest. (If you implement the

KeyListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a component using the component's

addKeyListener

method. When a key is pressed, released, or typed,
the relevant method in the listener object is invoked,
and the

KeyEvent

is passed to it.

**All Implemented Interfaces:** KeyListener

,

EventListener

---

### Field Details

*No entries found.*

### Constructor Details

#### public KeyAdapter()

*No description found.*

---

### Method Details

#### public void keyTyped​(
KeyEvent
e)

Invoked when a key has been typed.
This event occurs when a key press is followed by a key release.

**Specified by:**
- keyTyped

in interface

KeyListener

**Parameters:**
- e

- the event to be processed

---

#### public void keyPressed​(
KeyEvent
e)

Invoked when a key has been pressed.

**Specified by:**
- keyPressed

in interface

KeyListener

**Parameters:**
- e

- the event to be processed

---

#### public void keyReleased​(
KeyEvent
e)

Invoked when a key has been released.

**Specified by:**
- keyReleased

in interface

KeyListener

**Parameters:**
- e

- the event to be processed

---

### Additional Sections

#### Class KeyAdapter

java.lang.Object

- java.awt.event.KeyAdapter

java.awt.event.KeyAdapter

**All Implemented Interfaces:** KeyListener

,

EventListener

**Direct Known Subclasses:** BasicComboBoxUI.KeyHandler

,

BasicComboPopup.InvocationKeyHandler

,

BasicTreeUI.KeyHandler

```java
public abstract class
KeyAdapter

extends
Object

implements
KeyListener
```

An abstract adapter class for receiving keyboard events.
The methods in this class are empty. This class exists as
convenience for creating listener objects.

Extend this class to create a

KeyEvent

listener
and override the methods for the events of interest. (If you implement the

KeyListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a component using the component's

addKeyListener

method. When a key is pressed, released, or typed,
the relevant method in the listener object is invoked,
and the

KeyEvent

is passed to it.

**Since:** 1.1
**See Also:** KeyEvent

,

KeyListener

,

Tutorial: Writing a Key Listener

public abstract class

KeyAdapter

extends

Object

implements

KeyListener

An abstract adapter class for receiving keyboard events.
The methods in this class are empty. This class exists as
convenience for creating listener objects.

Extend this class to create a

KeyEvent

listener
and override the methods for the events of interest. (If you implement the

KeyListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a component using the component's

addKeyListener

method. When a key is pressed, released, or typed,
the relevant method in the listener object is invoked,
and the

KeyEvent

is passed to it.

Extend this class to create a

KeyEvent

listener
and override the methods for the events of interest. (If you implement the

KeyListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a component using the component's

addKeyListener

method. When a key is pressed, released, or typed,
the relevant method in the listener object is invoked,
and the

KeyEvent

is passed to it.

Create a listener object using the extended class and then register it with
a component using the component's

addKeyListener

method. When a key is pressed, released, or typed,
the relevant method in the listener object is invoked,
and the

KeyEvent

is passed to it.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

KeyAdapter

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

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

Constructor

Description

KeyAdapter

()

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

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

Invoked when a key has been pressed.

Invoked when a key has been released.

Invoked when a key has been typed.

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

- KeyAdapter

```java
public KeyAdapter()
```

============ METHOD DETAIL ==========

- Method Detail

- keyTyped

```java
public void keyTyped​(
KeyEvent
e)
```

Invoked when a key has been typed.
This event occurs when a key press is followed by a key release.

**Specified by:** keyTyped

in interface

KeyListener
**Parameters:** e

- the event to be processed

- keyPressed

```java
public void keyPressed​(
KeyEvent
e)
```

Invoked when a key has been pressed.

**Specified by:** keyPressed

in interface

KeyListener
**Parameters:** e

- the event to be processed

- keyReleased

```java
public void keyReleased​(
KeyEvent
e)
```

Invoked when a key has been released.

**Specified by:** keyReleased

in interface

KeyListener
**Parameters:** e

- the event to be processed

Constructor Detail

- KeyAdapter

```java
public KeyAdapter()
```

---

#### Constructor Detail

KeyAdapter

```java
public KeyAdapter()
```

---

#### KeyAdapter

public KeyAdapter()

Method Detail

- keyTyped

```java
public void keyTyped​(
KeyEvent
e)
```

Invoked when a key has been typed.
This event occurs when a key press is followed by a key release.

**Specified by:** keyTyped

in interface

KeyListener
**Parameters:** e

- the event to be processed

- keyPressed

```java
public void keyPressed​(
KeyEvent
e)
```

Invoked when a key has been pressed.

**Specified by:** keyPressed

in interface

KeyListener
**Parameters:** e

- the event to be processed

- keyReleased

```java
public void keyReleased​(
KeyEvent
e)
```

Invoked when a key has been released.

**Specified by:** keyReleased

in interface

KeyListener
**Parameters:** e

- the event to be processed

---

#### Method Detail

keyTyped

```java
public void keyTyped​(
KeyEvent
e)
```

Invoked when a key has been typed.
This event occurs when a key press is followed by a key release.

**Specified by:** keyTyped

in interface

KeyListener
**Parameters:** e

- the event to be processed

---

#### keyTyped

public void keyTyped​(

KeyEvent

e)

Invoked when a key has been typed.
This event occurs when a key press is followed by a key release.

keyPressed

```java
public void keyPressed​(
KeyEvent
e)
```

Invoked when a key has been pressed.

**Specified by:** keyPressed

in interface

KeyListener
**Parameters:** e

- the event to be processed

---

#### keyPressed

public void keyPressed​(

KeyEvent

e)

Invoked when a key has been pressed.

keyReleased

```java
public void keyReleased​(
KeyEvent
e)
```

Invoked when a key has been released.

**Specified by:** keyReleased

in interface

KeyListener
**Parameters:** e

- the event to be processed

---

#### keyReleased

public void keyReleased​(

KeyEvent

e)

Invoked when a key has been released.

---

