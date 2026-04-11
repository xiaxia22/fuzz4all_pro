# Interface GUIInitializedListener

**Source:** `jdk.accessibility\com\sun\java\accessibility\util\GUIInitializedListener.html`

### Class Description

```java
public interface
GUIInitializedListener

extends
EventListener
```

The

GUIInitializedListener

interface is used by the

EventQueueMonitor

class to notify an interested party when the GUI subsystem has been
initialized. This is necessary because assistive technologies can
be loaded before the GUI subsystem is initialized. As a result,
assistive technologies should check the

isGUIInitialized

method
of

EventQueueMonitor

before creating any GUI components. If the
return value is true, assistive technologies can create GUI components
following the same thread restrictions as any other application. If
the return value is false, the assistive technology should register
a

GUIInitializedListener

with the

EventQueueMonitor

to be notified
when the GUI subsystem is initialized.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void guiInitialized()

Invoked when the GUI subsystem is initialized and it's OK for
the assisitive technology to create instances of GUI objects.

---

### Additional Sections

#### Interface GUIInitializedListener

**All Superinterfaces:** EventListener

```java
public interface
GUIInitializedListener

extends
EventListener
```

The

GUIInitializedListener

interface is used by the

EventQueueMonitor

class to notify an interested party when the GUI subsystem has been
initialized. This is necessary because assistive technologies can
be loaded before the GUI subsystem is initialized. As a result,
assistive technologies should check the

isGUIInitialized

method
of

EventQueueMonitor

before creating any GUI components. If the
return value is true, assistive technologies can create GUI components
following the same thread restrictions as any other application. If
the return value is false, the assistive technology should register
a

GUIInitializedListener

with the

EventQueueMonitor

to be notified
when the GUI subsystem is initialized.

**See Also:** EventQueueMonitor

,

EventQueueMonitor.isGUIInitialized()

,

EventQueueMonitor.addGUIInitializedListener(com.sun.java.accessibility.util.GUIInitializedListener)

,

EventQueueMonitor.removeGUIInitializedListener(com.sun.java.accessibility.util.GUIInitializedListener)

public interface

GUIInitializedListener

extends

EventListener

The

GUIInitializedListener

interface is used by the

EventQueueMonitor

class to notify an interested party when the GUI subsystem has been
initialized. This is necessary because assistive technologies can
be loaded before the GUI subsystem is initialized. As a result,
assistive technologies should check the

isGUIInitialized

method
of

EventQueueMonitor

before creating any GUI components. If the
return value is true, assistive technologies can create GUI components
following the same thread restrictions as any other application. If
the return value is false, the assistive technology should register
a

GUIInitializedListener

with the

EventQueueMonitor

to be notified
when the GUI subsystem is initialized.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

guiInitialized

()

Invoked when the GUI subsystem is initialized and it's OK for
the assisitive technology to create instances of GUI objects.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

guiInitialized

()

Invoked when the GUI subsystem is initialized and it's OK for
the assisitive technology to create instances of GUI objects.

---

#### Method Summary

Invoked when the GUI subsystem is initialized and it's OK for
the assisitive technology to create instances of GUI objects.

============ METHOD DETAIL ==========

- Method Detail

- guiInitialized

```java
void guiInitialized()
```

Invoked when the GUI subsystem is initialized and it's OK for
the assisitive technology to create instances of GUI objects.

Method Detail

- guiInitialized

```java
void guiInitialized()
```

Invoked when the GUI subsystem is initialized and it's OK for
the assisitive technology to create instances of GUI objects.

---

#### Method Detail

guiInitialized

```java
void guiInitialized()
```

Invoked when the GUI subsystem is initialized and it's OK for
the assisitive technology to create instances of GUI objects.

---

#### guiInitialized

void guiInitialized()

Invoked when the GUI subsystem is initialized and it's OK for
the assisitive technology to create instances of GUI objects.

---

