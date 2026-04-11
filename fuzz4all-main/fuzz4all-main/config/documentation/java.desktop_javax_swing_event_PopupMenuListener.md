# Interface PopupMenuListener

**Source:** `java.desktop\javax\swing\event\PopupMenuListener.html`

### Class Description

```java
public interface
PopupMenuListener

extends
EventListener
```

A popup menu listener

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void popupMenuWillBecomeVisible​(
PopupMenuEvent
e)

This method is called before the popup menu becomes visible

**Parameters:**
- e

- a

PopupMenuEvent

containing the source of the event

---

#### void popupMenuWillBecomeInvisible​(
PopupMenuEvent
e)

This method is called before the popup menu becomes invisible
Note that a JPopupMenu can become invisible any time

**Parameters:**
- e

- a

PopupMenuEvent

containing the source of the event

---

#### void popupMenuCanceled​(
PopupMenuEvent
e)

This method is called when the popup menu is canceled

**Parameters:**
- e

- a

PopupMenuEvent

containing the source of the event

---

### Additional Sections

#### Interface PopupMenuListener

**All Superinterfaces:** EventListener

```java
public interface
PopupMenuListener

extends
EventListener
```

A popup menu listener

public interface

PopupMenuListener

extends

EventListener

A popup menu listener

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

popupMenuCanceled

​(

PopupMenuEvent

e)

This method is called when the popup menu is canceled

void

popupMenuWillBecomeInvisible

​(

PopupMenuEvent

e)

This method is called before the popup menu becomes invisible
Note that a JPopupMenu can become invisible any time

void

popupMenuWillBecomeVisible

​(

PopupMenuEvent

e)

This method is called before the popup menu becomes visible

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

popupMenuCanceled

​(

PopupMenuEvent

e)

This method is called when the popup menu is canceled

void

popupMenuWillBecomeInvisible

​(

PopupMenuEvent

e)

This method is called before the popup menu becomes invisible
Note that a JPopupMenu can become invisible any time

void

popupMenuWillBecomeVisible

​(

PopupMenuEvent

e)

This method is called before the popup menu becomes visible

---

#### Method Summary

This method is called when the popup menu is canceled

This method is called before the popup menu becomes invisible
Note that a JPopupMenu can become invisible any time

This method is called before the popup menu becomes visible

============ METHOD DETAIL ==========

- Method Detail

- popupMenuWillBecomeVisible

```java
void popupMenuWillBecomeVisible​(
PopupMenuEvent
e)
```

This method is called before the popup menu becomes visible

**Parameters:** e

- a

PopupMenuEvent

containing the source of the event

- popupMenuWillBecomeInvisible

```java
void popupMenuWillBecomeInvisible​(
PopupMenuEvent
e)
```

This method is called before the popup menu becomes invisible
Note that a JPopupMenu can become invisible any time

**Parameters:** e

- a

PopupMenuEvent

containing the source of the event

- popupMenuCanceled

```java
void popupMenuCanceled​(
PopupMenuEvent
e)
```

This method is called when the popup menu is canceled

**Parameters:** e

- a

PopupMenuEvent

containing the source of the event

Method Detail

- popupMenuWillBecomeVisible

```java
void popupMenuWillBecomeVisible​(
PopupMenuEvent
e)
```

This method is called before the popup menu becomes visible

**Parameters:** e

- a

PopupMenuEvent

containing the source of the event

- popupMenuWillBecomeInvisible

```java
void popupMenuWillBecomeInvisible​(
PopupMenuEvent
e)
```

This method is called before the popup menu becomes invisible
Note that a JPopupMenu can become invisible any time

**Parameters:** e

- a

PopupMenuEvent

containing the source of the event

- popupMenuCanceled

```java
void popupMenuCanceled​(
PopupMenuEvent
e)
```

This method is called when the popup menu is canceled

**Parameters:** e

- a

PopupMenuEvent

containing the source of the event

---

#### Method Detail

popupMenuWillBecomeVisible

```java
void popupMenuWillBecomeVisible​(
PopupMenuEvent
e)
```

This method is called before the popup menu becomes visible

**Parameters:** e

- a

PopupMenuEvent

containing the source of the event

---

#### popupMenuWillBecomeVisible

void popupMenuWillBecomeVisible​(

PopupMenuEvent

e)

This method is called before the popup menu becomes visible

popupMenuWillBecomeInvisible

```java
void popupMenuWillBecomeInvisible​(
PopupMenuEvent
e)
```

This method is called before the popup menu becomes invisible
Note that a JPopupMenu can become invisible any time

**Parameters:** e

- a

PopupMenuEvent

containing the source of the event

---

#### popupMenuWillBecomeInvisible

void popupMenuWillBecomeInvisible​(

PopupMenuEvent

e)

This method is called before the popup menu becomes invisible
Note that a JPopupMenu can become invisible any time

popupMenuCanceled

```java
void popupMenuCanceled​(
PopupMenuEvent
e)
```

This method is called when the popup menu is canceled

**Parameters:** e

- a

PopupMenuEvent

containing the source of the event

---

#### popupMenuCanceled

void popupMenuCanceled​(

PopupMenuEvent

e)

This method is called when the popup menu is canceled

---

