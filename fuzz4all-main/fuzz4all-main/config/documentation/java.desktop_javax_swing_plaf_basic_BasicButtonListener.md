# Class BasicButtonListener

**Source:** `java.desktop\javax\swing\plaf\basic\BasicButtonListener.html`

### Class Description

```java
public class
BasicButtonListener

extends
Object

implements
MouseListener
,
MouseMotionListener
,
FocusListener
,
ChangeListener
,
PropertyChangeListener
```

Button Listener

**All Implemented Interfaces:** FocusListener

,

MouseListener

,

MouseMotionListener

,

PropertyChangeListener

,

EventListener

,

ChangeListener

---

### Field Details

*No entries found.*

### Constructor Details

#### public BasicButtonListener​(
AbstractButton
b)

Constructs a new instance of

BasicButtonListener

.

**Parameters:**
- b

- an abstract button

---

### Method Details

#### protected void checkOpacity​(
AbstractButton
b)

Checks the opacity of the

AbstractButton

.

**Parameters:**
- b

- an abstract button

---

#### public void installKeyboardActions​(
JComponent
c)

Register default key actions: pressing space to "click" a
button and registering the keyboard mnemonic (if any).

**Parameters:**
- c

- a component

---

#### public void uninstallKeyboardActions​(
JComponent
c)

Unregister default key actions.

**Parameters:**
- c

- a component

---

### Additional Sections

#### Class BasicButtonListener

java.lang.Object

- javax.swing.plaf.basic.BasicButtonListener

javax.swing.plaf.basic.BasicButtonListener

**All Implemented Interfaces:** FocusListener

,

MouseListener

,

MouseMotionListener

,

PropertyChangeListener

,

EventListener

,

ChangeListener

```java
public class
BasicButtonListener

extends
Object

implements
MouseListener
,
MouseMotionListener
,
FocusListener
,
ChangeListener
,
PropertyChangeListener
```

Button Listener

public class

BasicButtonListener

extends

Object

implements

MouseListener

,

MouseMotionListener

,

FocusListener

,

ChangeListener

,

PropertyChangeListener

Button Listener

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicButtonListener

​(

AbstractButton

b)

Constructs a new instance of

BasicButtonListener

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

checkOpacity

​(

AbstractButton

b)

Checks the opacity of the

AbstractButton

.

void

installKeyboardActions

​(

JComponent

c)

Register default key actions: pressing space to "click" a
button and registering the keyboard mnemonic (if any).

void

uninstallKeyboardActions

​(

JComponent

c)

Unregister default key actions.

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

- Methods declared in interface javax.swing.event.

ChangeListener

stateChanged

- Methods declared in interface java.awt.event.

FocusListener

focusGained

,

focusLost

- Methods declared in interface java.awt.event.

MouseListener

mouseClicked

,

mouseEntered

,

mouseExited

,

mousePressed

,

mouseReleased

- Methods declared in interface java.awt.event.

MouseMotionListener

mouseDragged

,

mouseMoved

- Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

Constructor Summary

Constructors

Constructor

Description

BasicButtonListener

​(

AbstractButton

b)

Constructs a new instance of

BasicButtonListener

.

---

#### Constructor Summary

Constructs a new instance of

BasicButtonListener

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected void

checkOpacity

​(

AbstractButton

b)

Checks the opacity of the

AbstractButton

.

void

installKeyboardActions

​(

JComponent

c)

Register default key actions: pressing space to "click" a
button and registering the keyboard mnemonic (if any).

void

uninstallKeyboardActions

​(

JComponent

c)

Unregister default key actions.

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

- Methods declared in interface javax.swing.event.

ChangeListener

stateChanged

- Methods declared in interface java.awt.event.

FocusListener

focusGained

,

focusLost

- Methods declared in interface java.awt.event.

MouseListener

mouseClicked

,

mouseEntered

,

mouseExited

,

mousePressed

,

mouseReleased

- Methods declared in interface java.awt.event.

MouseMotionListener

mouseDragged

,

mouseMoved

- Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

---

#### Method Summary

Checks the opacity of the

AbstractButton

.

Register default key actions: pressing space to "click" a
button and registering the keyboard mnemonic (if any).

Unregister default key actions.

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

Methods declared in interface javax.swing.event.

ChangeListener

stateChanged

---

#### Methods declared in interface javax.swing.event. ChangeListener

Methods declared in interface java.awt.event.

FocusListener

focusGained

,

focusLost

---

#### Methods declared in interface java.awt.event. FocusListener

Methods declared in interface java.awt.event.

MouseListener

mouseClicked

,

mouseEntered

,

mouseExited

,

mousePressed

,

mouseReleased

---

#### Methods declared in interface java.awt.event. MouseListener

Methods declared in interface java.awt.event.

MouseMotionListener

mouseDragged

,

mouseMoved

---

#### Methods declared in interface java.awt.event. MouseMotionListener

Methods declared in interface java.beans.

PropertyChangeListener

propertyChange

---

#### Methods declared in interface java.beans. PropertyChangeListener

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicButtonListener

```java
public BasicButtonListener​(
AbstractButton
b)
```

Constructs a new instance of

BasicButtonListener

.

**Parameters:** b

- an abstract button

============ METHOD DETAIL ==========

- Method Detail

- checkOpacity

```java
protected void checkOpacity​(
AbstractButton
b)
```

Checks the opacity of the

AbstractButton

.

**Parameters:** b

- an abstract button

- installKeyboardActions

```java
public void installKeyboardActions​(
JComponent
c)
```

Register default key actions: pressing space to "click" a
button and registering the keyboard mnemonic (if any).

**Parameters:** c

- a component

- uninstallKeyboardActions

```java
public void uninstallKeyboardActions​(
JComponent
c)
```

Unregister default key actions.

**Parameters:** c

- a component

Constructor Detail

- BasicButtonListener

```java
public BasicButtonListener​(
AbstractButton
b)
```

Constructs a new instance of

BasicButtonListener

.

**Parameters:** b

- an abstract button

---

#### Constructor Detail

BasicButtonListener

```java
public BasicButtonListener​(
AbstractButton
b)
```

Constructs a new instance of

BasicButtonListener

.

**Parameters:** b

- an abstract button

---

#### BasicButtonListener

public BasicButtonListener​(

AbstractButton

b)

Constructs a new instance of

BasicButtonListener

.

Method Detail

- checkOpacity

```java
protected void checkOpacity​(
AbstractButton
b)
```

Checks the opacity of the

AbstractButton

.

**Parameters:** b

- an abstract button

- installKeyboardActions

```java
public void installKeyboardActions​(
JComponent
c)
```

Register default key actions: pressing space to "click" a
button and registering the keyboard mnemonic (if any).

**Parameters:** c

- a component

- uninstallKeyboardActions

```java
public void uninstallKeyboardActions​(
JComponent
c)
```

Unregister default key actions.

**Parameters:** c

- a component

---

#### Method Detail

checkOpacity

```java
protected void checkOpacity​(
AbstractButton
b)
```

Checks the opacity of the

AbstractButton

.

**Parameters:** b

- an abstract button

---

#### checkOpacity

protected void checkOpacity​(

AbstractButton

b)

Checks the opacity of the

AbstractButton

.

installKeyboardActions

```java
public void installKeyboardActions​(
JComponent
c)
```

Register default key actions: pressing space to "click" a
button and registering the keyboard mnemonic (if any).

**Parameters:** c

- a component

---

#### installKeyboardActions

public void installKeyboardActions​(

JComponent

c)

Register default key actions: pressing space to "click" a
button and registering the keyboard mnemonic (if any).

uninstallKeyboardActions

```java
public void uninstallKeyboardActions​(
JComponent
c)
```

Unregister default key actions.

**Parameters:** c

- a component

---

#### uninstallKeyboardActions

public void uninstallKeyboardActions​(

JComponent

c)

Unregister default key actions.

---

