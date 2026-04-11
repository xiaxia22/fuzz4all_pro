# Class QuitEvent

**Source:** `java.desktop\java\awt\desktop\QuitEvent.html`

### Class Description

```java
public final class
QuitEvent

extends
AppEvent
```

Event sent when the application is asked to quit.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public QuitEvent()

Constructs a

QuitEvent

.

**Throws:**
- HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
- UnsupportedOperationException

- if Desktop API is not supported on
the current platform

**See Also:**
- Desktop.isDesktopSupported()

,

GraphicsEnvironment.isHeadless()

---

### Method Details

*No entries found.*

### Additional Sections

#### Class QuitEvent

java.lang.Object

- java.util.EventObject
- - java.awt.desktop.AppEvent
- - java.awt.desktop.QuitEvent

java.util.EventObject

- java.awt.desktop.AppEvent
- - java.awt.desktop.QuitEvent

java.awt.desktop.AppEvent

- java.awt.desktop.QuitEvent

java.awt.desktop.QuitEvent

**All Implemented Interfaces:** Serializable

```java
public final class
QuitEvent

extends
AppEvent
```

Event sent when the application is asked to quit.

**Since:** 9
**See Also:** QuitHandler.handleQuitRequestWith(QuitEvent, QuitResponse)

,

Serialized Form

public final class

QuitEvent

extends

AppEvent

Event sent when the application is asked to quit.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.util.

EventObject

source

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

QuitEvent

()

Constructs a

QuitEvent

.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

wait

,

wait

,

wait

Field Summary

- Fields declared in class java.util.

EventObject

source

---

#### Field Summary

Fields declared in class java.util.

EventObject

source

---

#### Fields declared in class java.util. EventObject

Constructor Summary

Constructors

Constructor

Description

QuitEvent

()

Constructs a

QuitEvent

.

---

#### Constructor Summary

Constructs a

QuitEvent

.

Method Summary

- Methods declared in class java.util.

EventObject

getSource

,

toString

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

wait

,

wait

,

wait

---

#### Method Summary

Methods declared in class java.util.

EventObject

getSource

,

toString

---

#### Methods declared in class java.util. EventObject

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- QuitEvent

```java
public QuitEvent()
```

Constructs a

QuitEvent

.

**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** UnsupportedOperationException

- if Desktop API is not supported on
the current platform
**See Also:** Desktop.isDesktopSupported()

,

GraphicsEnvironment.isHeadless()

Constructor Detail

- QuitEvent

```java
public QuitEvent()
```

Constructs a

QuitEvent

.

**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** UnsupportedOperationException

- if Desktop API is not supported on
the current platform
**See Also:** Desktop.isDesktopSupported()

,

GraphicsEnvironment.isHeadless()

---

#### Constructor Detail

QuitEvent

```java
public QuitEvent()
```

Constructs a

QuitEvent

.

**Throws:** HeadlessException

- if

GraphicsEnvironment.isHeadless()

returns

true
**Throws:** UnsupportedOperationException

- if Desktop API is not supported on
the current platform
**See Also:** Desktop.isDesktopSupported()

,

GraphicsEnvironment.isHeadless()

---

#### QuitEvent

public QuitEvent()

Constructs a

QuitEvent

.

---

