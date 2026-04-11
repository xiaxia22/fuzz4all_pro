# Interface MenuListener

**Source:** `java.desktop\javax\swing\event\MenuListener.html`

### Class Description

```java
public interface
MenuListener

extends
EventListener
```

Defines a listener for menu events.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void menuSelected​(
MenuEvent
e)

Invoked when a menu is selected.

**Parameters:**
- e

- a MenuEvent object

---

#### void menuDeselected​(
MenuEvent
e)

Invoked when the menu is deselected.

**Parameters:**
- e

- a MenuEvent object

---

#### void menuCanceled​(
MenuEvent
e)

Invoked when the menu is canceled.

**Parameters:**
- e

- a MenuEvent object

---

### Additional Sections

#### Interface MenuListener

**All Superinterfaces:** EventListener

```java
public interface
MenuListener

extends
EventListener
```

Defines a listener for menu events.

public interface

MenuListener

extends

EventListener

Defines a listener for menu events.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

menuCanceled

​(

MenuEvent

e)

Invoked when the menu is canceled.

void

menuDeselected

​(

MenuEvent

e)

Invoked when the menu is deselected.

void

menuSelected

​(

MenuEvent

e)

Invoked when a menu is selected.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

menuCanceled

​(

MenuEvent

e)

Invoked when the menu is canceled.

void

menuDeselected

​(

MenuEvent

e)

Invoked when the menu is deselected.

void

menuSelected

​(

MenuEvent

e)

Invoked when a menu is selected.

---

#### Method Summary

Invoked when the menu is canceled.

Invoked when the menu is deselected.

Invoked when a menu is selected.

============ METHOD DETAIL ==========

- Method Detail

- menuSelected

```java
void menuSelected​(
MenuEvent
e)
```

Invoked when a menu is selected.

**Parameters:** e

- a MenuEvent object

- menuDeselected

```java
void menuDeselected​(
MenuEvent
e)
```

Invoked when the menu is deselected.

**Parameters:** e

- a MenuEvent object

- menuCanceled

```java
void menuCanceled​(
MenuEvent
e)
```

Invoked when the menu is canceled.

**Parameters:** e

- a MenuEvent object

Method Detail

- menuSelected

```java
void menuSelected​(
MenuEvent
e)
```

Invoked when a menu is selected.

**Parameters:** e

- a MenuEvent object

- menuDeselected

```java
void menuDeselected​(
MenuEvent
e)
```

Invoked when the menu is deselected.

**Parameters:** e

- a MenuEvent object

- menuCanceled

```java
void menuCanceled​(
MenuEvent
e)
```

Invoked when the menu is canceled.

**Parameters:** e

- a MenuEvent object

---

#### Method Detail

menuSelected

```java
void menuSelected​(
MenuEvent
e)
```

Invoked when a menu is selected.

**Parameters:** e

- a MenuEvent object

---

#### menuSelected

void menuSelected​(

MenuEvent

e)

Invoked when a menu is selected.

menuDeselected

```java
void menuDeselected​(
MenuEvent
e)
```

Invoked when the menu is deselected.

**Parameters:** e

- a MenuEvent object

---

#### menuDeselected

void menuDeselected​(

MenuEvent

e)

Invoked when the menu is deselected.

menuCanceled

```java
void menuCanceled​(
MenuEvent
e)
```

Invoked when the menu is canceled.

**Parameters:** e

- a MenuEvent object

---

#### menuCanceled

void menuCanceled​(

MenuEvent

e)

Invoked when the menu is canceled.

---

