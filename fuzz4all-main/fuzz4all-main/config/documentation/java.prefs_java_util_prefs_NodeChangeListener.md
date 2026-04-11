# Interface NodeChangeListener

**Source:** `java.prefs\java\util\prefs\NodeChangeListener.html`

### Class Description

```java
public interface
NodeChangeListener

extends
EventListener
```

A listener for receiving preference node change events.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void childAdded​(
NodeChangeEvent
evt)

This method gets called when a child node is added.

**Parameters:**
- evt

- A node change event object describing the parent
and child node.

---

#### void childRemoved​(
NodeChangeEvent
evt)

This method gets called when a child node is removed.

**Parameters:**
- evt

- A node change event object describing the parent
and child node.

---

### Additional Sections

#### Interface NodeChangeListener

**All Superinterfaces:** EventListener

```java
public interface
NodeChangeListener

extends
EventListener
```

A listener for receiving preference node change events.

**Since:** 1.4
**See Also:** Preferences

,

NodeChangeEvent

,

PreferenceChangeListener

public interface

NodeChangeListener

extends

EventListener

A listener for receiving preference node change events.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

childAdded

​(

NodeChangeEvent

evt)

This method gets called when a child node is added.

void

childRemoved

​(

NodeChangeEvent

evt)

This method gets called when a child node is removed.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

childAdded

​(

NodeChangeEvent

evt)

This method gets called when a child node is added.

void

childRemoved

​(

NodeChangeEvent

evt)

This method gets called when a child node is removed.

---

#### Method Summary

This method gets called when a child node is added.

This method gets called when a child node is removed.

============ METHOD DETAIL ==========

- Method Detail

- childAdded

```java
void childAdded​(
NodeChangeEvent
evt)
```

This method gets called when a child node is added.

**Parameters:** evt

- A node change event object describing the parent
and child node.

- childRemoved

```java
void childRemoved​(
NodeChangeEvent
evt)
```

This method gets called when a child node is removed.

**Parameters:** evt

- A node change event object describing the parent
and child node.

Method Detail

- childAdded

```java
void childAdded​(
NodeChangeEvent
evt)
```

This method gets called when a child node is added.

**Parameters:** evt

- A node change event object describing the parent
and child node.

- childRemoved

```java
void childRemoved​(
NodeChangeEvent
evt)
```

This method gets called when a child node is removed.

**Parameters:** evt

- A node change event object describing the parent
and child node.

---

#### Method Detail

childAdded

```java
void childAdded​(
NodeChangeEvent
evt)
```

This method gets called when a child node is added.

**Parameters:** evt

- A node change event object describing the parent
and child node.

---

#### childAdded

void childAdded​(

NodeChangeEvent

evt)

This method gets called when a child node is added.

childRemoved

```java
void childRemoved​(
NodeChangeEvent
evt)
```

This method gets called when a child node is removed.

**Parameters:** evt

- A node change event object describing the parent
and child node.

---

#### childRemoved

void childRemoved​(

NodeChangeEvent

evt)

This method gets called when a child node is removed.

---

