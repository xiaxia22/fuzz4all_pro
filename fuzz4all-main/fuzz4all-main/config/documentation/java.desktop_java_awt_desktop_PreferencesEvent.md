# Class PreferencesEvent

**Source:** `java.desktop\java\awt\desktop\PreferencesEvent.html`

### Class Description

```java
public final class
PreferencesEvent

extends
AppEvent
```

Event sent when the application is asked to open its preferences window.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public PreferencesEvent()

Constructs a

PreferencesEvent

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

#### Class PreferencesEvent

java.lang.Object

- java.util.EventObject
- - java.awt.desktop.AppEvent
- - java.awt.desktop.PreferencesEvent

java.util.EventObject

- java.awt.desktop.AppEvent
- - java.awt.desktop.PreferencesEvent

java.awt.desktop.AppEvent

- java.awt.desktop.PreferencesEvent

java.awt.desktop.PreferencesEvent

**All Implemented Interfaces:** Serializable

```java
public final class
PreferencesEvent

extends
AppEvent
```

Event sent when the application is asked to open its preferences window.

**Since:** 9
**See Also:** PreferencesHandler.handlePreferences(java.awt.desktop.PreferencesEvent)

,

Serialized Form

public final class

PreferencesEvent

extends

AppEvent

Event sent when the application is asked to open its preferences window.

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

PreferencesEvent

()

Constructs a

PreferencesEvent

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

PreferencesEvent

()

Constructs a

PreferencesEvent

.

---

#### Constructor Summary

Constructs a

PreferencesEvent

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

- PreferencesEvent

```java
public PreferencesEvent()
```

Constructs a

PreferencesEvent

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

- PreferencesEvent

```java
public PreferencesEvent()
```

Constructs a

PreferencesEvent

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

PreferencesEvent

```java
public PreferencesEvent()
```

Constructs a

PreferencesEvent

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

#### PreferencesEvent

public PreferencesEvent()

Constructs a

PreferencesEvent

.

---

