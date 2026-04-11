# Class FocusAdapter

**Source:** `java.desktop\java\awt\event\FocusAdapter.html`

### Class Description

```java
public abstract class
FocusAdapter

extends
Object

implements
FocusListener
```

An abstract adapter class for receiving keyboard focus events.
The methods in this class are empty. This class exists as
convenience for creating listener objects.

Extend this class to create a

FocusEvent

listener
and override the methods for the events of interest. (If you implement the

FocusListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a component using the component's

addFocusListener

method. When the component gains or loses the keyboard focus,
the relevant method in the listener object is invoked,
and the

FocusEvent

is passed to it.

**All Implemented Interfaces:** FocusListener

,

EventListener

---

### Field Details

*No entries found.*

### Constructor Details

#### public FocusAdapter()

*No description found.*

---

### Method Details

#### public void focusGained​(
FocusEvent
e)

Invoked when a component gains the keyboard focus.

**Specified by:**
- focusGained

in interface

FocusListener

**Parameters:**
- e

- the event to be processed

---

#### public void focusLost​(
FocusEvent
e)

Invoked when a component loses the keyboard focus.

**Specified by:**
- focusLost

in interface

FocusListener

**Parameters:**
- e

- the event to be processed

---

### Additional Sections

#### Class FocusAdapter

java.lang.Object

- java.awt.event.FocusAdapter

java.awt.event.FocusAdapter

**All Implemented Interfaces:** FocusListener

,

EventListener

**Direct Known Subclasses:** BasicSplitPaneUI.FocusHandler

,

BasicTabbedPaneUI.FocusHandler

```java
public abstract class
FocusAdapter

extends
Object

implements
FocusListener
```

An abstract adapter class for receiving keyboard focus events.
The methods in this class are empty. This class exists as
convenience for creating listener objects.

Extend this class to create a

FocusEvent

listener
and override the methods for the events of interest. (If you implement the

FocusListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a component using the component's

addFocusListener

method. When the component gains or loses the keyboard focus,
the relevant method in the listener object is invoked,
and the

FocusEvent

is passed to it.

**Since:** 1.1
**See Also:** FocusEvent

,

FocusListener

,

Tutorial: Writing a Focus Listener

public abstract class

FocusAdapter

extends

Object

implements

FocusListener

An abstract adapter class for receiving keyboard focus events.
The methods in this class are empty. This class exists as
convenience for creating listener objects.

Extend this class to create a

FocusEvent

listener
and override the methods for the events of interest. (If you implement the

FocusListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a component using the component's

addFocusListener

method. When the component gains or loses the keyboard focus,
the relevant method in the listener object is invoked,
and the

FocusEvent

is passed to it.

Extend this class to create a

FocusEvent

listener
and override the methods for the events of interest. (If you implement the

FocusListener

interface, you have to define all of
the methods in it. This abstract class defines null methods for them
all, so you can only have to define methods for events you care about.)

Create a listener object using the extended class and then register it with
a component using the component's

addFocusListener

method. When the component gains or loses the keyboard focus,
the relevant method in the listener object is invoked,
and the

FocusEvent

is passed to it.

Create a listener object using the extended class and then register it with
a component using the component's

addFocusListener

method. When the component gains or loses the keyboard focus,
the relevant method in the listener object is invoked,
and the

FocusEvent

is passed to it.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

FocusAdapter

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

focusGained

​(

FocusEvent

e)

Invoked when a component gains the keyboard focus.

void

focusLost

​(

FocusEvent

e)

Invoked when a component loses the keyboard focus.

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

FocusAdapter

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

focusGained

​(

FocusEvent

e)

Invoked when a component gains the keyboard focus.

void

focusLost

​(

FocusEvent

e)

Invoked when a component loses the keyboard focus.

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

Invoked when a component gains the keyboard focus.

Invoked when a component loses the keyboard focus.

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

- FocusAdapter

```java
public FocusAdapter()
```

============ METHOD DETAIL ==========

- Method Detail

- focusGained

```java
public void focusGained​(
FocusEvent
e)
```

Invoked when a component gains the keyboard focus.

**Specified by:** focusGained

in interface

FocusListener
**Parameters:** e

- the event to be processed

- focusLost

```java
public void focusLost​(
FocusEvent
e)
```

Invoked when a component loses the keyboard focus.

**Specified by:** focusLost

in interface

FocusListener
**Parameters:** e

- the event to be processed

Constructor Detail

- FocusAdapter

```java
public FocusAdapter()
```

---

#### Constructor Detail

FocusAdapter

```java
public FocusAdapter()
```

---

#### FocusAdapter

public FocusAdapter()

Method Detail

- focusGained

```java
public void focusGained​(
FocusEvent
e)
```

Invoked when a component gains the keyboard focus.

**Specified by:** focusGained

in interface

FocusListener
**Parameters:** e

- the event to be processed

- focusLost

```java
public void focusLost​(
FocusEvent
e)
```

Invoked when a component loses the keyboard focus.

**Specified by:** focusLost

in interface

FocusListener
**Parameters:** e

- the event to be processed

---

#### Method Detail

focusGained

```java
public void focusGained​(
FocusEvent
e)
```

Invoked when a component gains the keyboard focus.

**Specified by:** focusGained

in interface

FocusListener
**Parameters:** e

- the event to be processed

---

#### focusGained

public void focusGained​(

FocusEvent

e)

Invoked when a component gains the keyboard focus.

focusLost

```java
public void focusLost​(
FocusEvent
e)
```

Invoked when a component loses the keyboard focus.

**Specified by:** focusLost

in interface

FocusListener
**Parameters:** e

- the event to be processed

---

#### focusLost

public void focusLost​(

FocusEvent

e)

Invoked when a component loses the keyboard focus.

---

