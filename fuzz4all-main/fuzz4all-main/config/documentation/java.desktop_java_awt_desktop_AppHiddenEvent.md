# Class AppHiddenEvent

**Source:** `java.desktop\java\awt\desktop\AppHiddenEvent.html`

### Class Description

```java
public final class
AppHiddenEvent

extends
AppEvent
```

Event sent when the application has been hidden or shown.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public AppHiddenEvent()

Constructs an

AppHiddenEvent

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

#### Class AppHiddenEvent

java.lang.Object

- java.util.EventObject
- - java.awt.desktop.AppEvent
- - java.awt.desktop.AppHiddenEvent

java.util.EventObject

- java.awt.desktop.AppEvent
- - java.awt.desktop.AppHiddenEvent

java.awt.desktop.AppEvent

- java.awt.desktop.AppHiddenEvent

java.awt.desktop.AppHiddenEvent

**All Implemented Interfaces:** Serializable

```java
public final class
AppHiddenEvent

extends
AppEvent
```

Event sent when the application has been hidden or shown.

**Since:** 9
**See Also:** AppHiddenListener.appHidden(AppHiddenEvent)

,

AppHiddenListener.appUnhidden(AppHiddenEvent)

,

Serialized Form

public final class

AppHiddenEvent

extends

AppEvent

Event sent when the application has been hidden or shown.

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

AppHiddenEvent

()

Constructs an

AppHiddenEvent

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

AppHiddenEvent

()

Constructs an

AppHiddenEvent

.

---

#### Constructor Summary

Constructs an

AppHiddenEvent

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

- AppHiddenEvent

```java
public AppHiddenEvent()
```

Constructs an

AppHiddenEvent

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

- AppHiddenEvent

```java
public AppHiddenEvent()
```

Constructs an

AppHiddenEvent

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

AppHiddenEvent

```java
public AppHiddenEvent()
```

Constructs an

AppHiddenEvent

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

#### AppHiddenEvent

public AppHiddenEvent()

Constructs an

AppHiddenEvent

.

---

