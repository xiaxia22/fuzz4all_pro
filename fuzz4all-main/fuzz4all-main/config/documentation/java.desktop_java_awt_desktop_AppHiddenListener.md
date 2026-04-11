# Interface AppHiddenListener

**Source:** `java.desktop\java\awt\desktop\AppHiddenListener.html`

### Class Description

```java
public interface
AppHiddenListener

extends
SystemEventListener
```

Implementors are notified when the app is hidden or shown by the user. This
notification is helpful for discontinuing a costly animation if it's not
visible to the user.

**All Superinterfaces:** EventListener

,

SystemEventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void appHidden​(
AppHiddenEvent
e)

Called the app is hidden.

**Parameters:**
- e

- event

---

#### void appUnhidden​(
AppHiddenEvent
e)

Called when the hidden app is shown again (but not necessarily brought to
the foreground).

**Parameters:**
- e

- event

---

### Additional Sections

#### Interface AppHiddenListener

**All Superinterfaces:** EventListener

,

SystemEventListener

```java
public interface
AppHiddenListener

extends
SystemEventListener
```

Implementors are notified when the app is hidden or shown by the user. This
notification is helpful for discontinuing a costly animation if it's not
visible to the user.

**Since:** 9

public interface

AppHiddenListener

extends

SystemEventListener

Implementors are notified when the app is hidden or shown by the user. This
notification is helpful for discontinuing a costly animation if it's not
visible to the user.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

appHidden

​(

AppHiddenEvent

e)

Called the app is hidden.

void

appUnhidden

​(

AppHiddenEvent

e)

Called when the hidden app is shown again (but not necessarily brought to
the foreground).

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

appHidden

​(

AppHiddenEvent

e)

Called the app is hidden.

void

appUnhidden

​(

AppHiddenEvent

e)

Called when the hidden app is shown again (but not necessarily brought to
the foreground).

---

#### Method Summary

Called the app is hidden.

Called when the hidden app is shown again (but not necessarily brought to
the foreground).

============ METHOD DETAIL ==========

- Method Detail

- appHidden

```java
void appHidden​(
AppHiddenEvent
e)
```

Called the app is hidden.

**Parameters:** e

- event

- appUnhidden

```java
void appUnhidden​(
AppHiddenEvent
e)
```

Called when the hidden app is shown again (but not necessarily brought to
the foreground).

**Parameters:** e

- event

Method Detail

- appHidden

```java
void appHidden​(
AppHiddenEvent
e)
```

Called the app is hidden.

**Parameters:** e

- event

- appUnhidden

```java
void appUnhidden​(
AppHiddenEvent
e)
```

Called when the hidden app is shown again (but not necessarily brought to
the foreground).

**Parameters:** e

- event

---

#### Method Detail

appHidden

```java
void appHidden​(
AppHiddenEvent
e)
```

Called the app is hidden.

**Parameters:** e

- event

---

#### appHidden

void appHidden​(

AppHiddenEvent

e)

Called the app is hidden.

appUnhidden

```java
void appUnhidden​(
AppHiddenEvent
e)
```

Called when the hidden app is shown again (but not necessarily brought to
the foreground).

**Parameters:** e

- event

---

#### appUnhidden

void appUnhidden​(

AppHiddenEvent

e)

Called when the hidden app is shown again (but not necessarily brought to
the foreground).

---

