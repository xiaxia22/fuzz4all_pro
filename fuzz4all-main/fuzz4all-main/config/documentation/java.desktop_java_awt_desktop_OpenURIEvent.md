# Class OpenURIEvent

**Source:** `java.desktop\java\awt\desktop\OpenURIEvent.html`

### Class Description

```java
public final class
OpenURIEvent

extends
AppEvent
```

Event sent when the app is asked to open a

URI

.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public OpenURIEvent​(
URI
uri)

Constructs an

OpenURIEvent

.

**Parameters:**
- uri

- the

URI

the app was asked to open

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

#### public
URI
getURI()

Get the

URI

the app was asked to open

**Returns:**
- the

URI

---

### Additional Sections

#### Class OpenURIEvent

java.lang.Object

- java.util.EventObject
- - java.awt.desktop.AppEvent
- - java.awt.desktop.OpenURIEvent

java.util.EventObject

- java.awt.desktop.AppEvent
- - java.awt.desktop.OpenURIEvent

java.awt.desktop.AppEvent

- java.awt.desktop.OpenURIEvent

java.awt.desktop.OpenURIEvent

**All Implemented Interfaces:** Serializable

```java
public final class
OpenURIEvent

extends
AppEvent
```

Event sent when the app is asked to open a

URI

.

**Since:** 9
**See Also:** OpenURIHandler.openURI(OpenURIEvent)

,

Serialized Form

public final class

OpenURIEvent

extends

AppEvent

Event sent when the app is asked to open a

URI

.

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

OpenURIEvent

​(

URI

uri)

Constructs an

OpenURIEvent

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

URI

getURI

()

Get the

URI

the app was asked to open

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

OpenURIEvent

​(

URI

uri)

Constructs an

OpenURIEvent

.

---

#### Constructor Summary

Constructs an

OpenURIEvent

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

URI

getURI

()

Get the

URI

the app was asked to open

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

Get the

URI

the app was asked to open

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

- OpenURIEvent

```java
public OpenURIEvent​(
URI
uri)
```

Constructs an

OpenURIEvent

.

**Parameters:** uri

- the

URI

the app was asked to open
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

============ METHOD DETAIL ==========

- Method Detail

- getURI

```java
public
URI
getURI()
```

Get the

URI

the app was asked to open

**Returns:** the

URI

Constructor Detail

- OpenURIEvent

```java
public OpenURIEvent​(
URI
uri)
```

Constructs an

OpenURIEvent

.

**Parameters:** uri

- the

URI

the app was asked to open
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

OpenURIEvent

```java
public OpenURIEvent​(
URI
uri)
```

Constructs an

OpenURIEvent

.

**Parameters:** uri

- the

URI

the app was asked to open
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

#### OpenURIEvent

public OpenURIEvent​(

URI

uri)

Constructs an

OpenURIEvent

.

Method Detail

- getURI

```java
public
URI
getURI()
```

Get the

URI

the app was asked to open

**Returns:** the

URI

---

#### Method Detail

getURI

```java
public
URI
getURI()
```

Get the

URI

the app was asked to open

**Returns:** the

URI

---

#### getURI

public

URI

getURI()

Get the

URI

the app was asked to open

---

