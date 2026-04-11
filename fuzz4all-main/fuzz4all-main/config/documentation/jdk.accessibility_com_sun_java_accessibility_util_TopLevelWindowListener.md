# Interface TopLevelWindowListener

**Source:** `jdk.accessibility\com\sun\java\accessibility\util\TopLevelWindowListener.html`

### Class Description

```java
public interface
TopLevelWindowListener

extends
EventListener
```

The

TopLevelWindowListener

interface is used by the

EventQueueMonitor

class to notify an interested party when a top level window is created
or destroyed in the Java Virtual Machine. Classes wishing to express
an interest in top level window events should implement this interface
and register themselves with the

EventQueueMonitor

by calling the

EventQueueMonitor.addTopLevelWindowListener

class method.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void topLevelWindowCreated​(
Window
w)

Invoked when a new top level window has been created.

**Parameters:**
- w

- the Window that was created

---

#### void topLevelWindowDestroyed​(
Window
w)

Invoked when a top level window has been destroyed.

**Parameters:**
- w

- the Window that was destroyed

---

### Additional Sections

#### Interface TopLevelWindowListener

**All Superinterfaces:** EventListener

```java
public interface
TopLevelWindowListener

extends
EventListener
```

The

TopLevelWindowListener

interface is used by the

EventQueueMonitor

class to notify an interested party when a top level window is created
or destroyed in the Java Virtual Machine. Classes wishing to express
an interest in top level window events should implement this interface
and register themselves with the

EventQueueMonitor

by calling the

EventQueueMonitor.addTopLevelWindowListener

class method.

**See Also:** EventQueueMonitor

,

EventQueueMonitor.addTopLevelWindowListener(com.sun.java.accessibility.util.TopLevelWindowListener)

,

EventQueueMonitor.removeTopLevelWindowListener(com.sun.java.accessibility.util.TopLevelWindowListener)

public interface

TopLevelWindowListener

extends

EventListener

The

TopLevelWindowListener

interface is used by the

EventQueueMonitor

class to notify an interested party when a top level window is created
or destroyed in the Java Virtual Machine. Classes wishing to express
an interest in top level window events should implement this interface
and register themselves with the

EventQueueMonitor

by calling the

EventQueueMonitor.addTopLevelWindowListener

class method.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

topLevelWindowCreated

​(

Window

w)

Invoked when a new top level window has been created.

void

topLevelWindowDestroyed

​(

Window

w)

Invoked when a top level window has been destroyed.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

topLevelWindowCreated

​(

Window

w)

Invoked when a new top level window has been created.

void

topLevelWindowDestroyed

​(

Window

w)

Invoked when a top level window has been destroyed.

---

#### Method Summary

Invoked when a new top level window has been created.

Invoked when a top level window has been destroyed.

============ METHOD DETAIL ==========

- Method Detail

- topLevelWindowCreated

```java
void topLevelWindowCreated​(
Window
w)
```

Invoked when a new top level window has been created.

**Parameters:** w

- the Window that was created

- topLevelWindowDestroyed

```java
void topLevelWindowDestroyed​(
Window
w)
```

Invoked when a top level window has been destroyed.

**Parameters:** w

- the Window that was destroyed

Method Detail

- topLevelWindowCreated

```java
void topLevelWindowCreated​(
Window
w)
```

Invoked when a new top level window has been created.

**Parameters:** w

- the Window that was created

- topLevelWindowDestroyed

```java
void topLevelWindowDestroyed​(
Window
w)
```

Invoked when a top level window has been destroyed.

**Parameters:** w

- the Window that was destroyed

---

#### Method Detail

topLevelWindowCreated

```java
void topLevelWindowCreated​(
Window
w)
```

Invoked when a new top level window has been created.

**Parameters:** w

- the Window that was created

---

#### topLevelWindowCreated

void topLevelWindowCreated​(

Window

w)

Invoked when a new top level window has been created.

topLevelWindowDestroyed

```java
void topLevelWindowDestroyed​(
Window
w)
```

Invoked when a top level window has been destroyed.

**Parameters:** w

- the Window that was destroyed

---

#### topLevelWindowDestroyed

void topLevelWindowDestroyed​(

Window

w)

Invoked when a top level window has been destroyed.

---

