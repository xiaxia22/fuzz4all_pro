# Class AboutEvent

**Source:** `java.desktop\java\awt\desktop\AboutEvent.html`

### Class Description

```java
public final class
AboutEvent

extends
AppEvent
```

Event sent when the application is asked to open its about window.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public AboutEvent()

Constructs an

AboutEvent

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

#### Class AboutEvent

java.lang.Object

- java.util.EventObject
- - java.awt.desktop.AppEvent
- - java.awt.desktop.AboutEvent

java.util.EventObject

- java.awt.desktop.AppEvent
- - java.awt.desktop.AboutEvent

java.awt.desktop.AppEvent

- java.awt.desktop.AboutEvent

java.awt.desktop.AboutEvent

**All Implemented Interfaces:** Serializable

```java
public final class
AboutEvent

extends
AppEvent
```

Event sent when the application is asked to open its about window.

**Since:** 9
**See Also:** AboutHandler.handleAbout(java.awt.desktop.AboutEvent)

,

Serialized Form

public final class

AboutEvent

extends

AppEvent

Event sent when the application is asked to open its about window.

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

AboutEvent

()

Constructs an

AboutEvent

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

AboutEvent

()

Constructs an

AboutEvent

.

---

#### Constructor Summary

Constructs an

AboutEvent

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

- AboutEvent

```java
public AboutEvent()
```

Constructs an

AboutEvent

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

- AboutEvent

```java
public AboutEvent()
```

Constructs an

AboutEvent

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

AboutEvent

```java
public AboutEvent()
```

Constructs an

AboutEvent

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

#### AboutEvent

public AboutEvent()

Constructs an

AboutEvent

.

---

