# Interface VetoableChangeListener

**Source:** `java.desktop\java\beans\VetoableChangeListener.html`

### Class Description

```java
public interface
VetoableChangeListener

extends
EventListener
```

A VetoableChange event gets fired whenever a bean changes a "constrained"
property. You can register a VetoableChangeListener with a source bean
so as to be notified of any constrained property updates.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void vetoableChange​(
PropertyChangeEvent
evt)
throws
PropertyVetoException

This method gets called when a constrained property is changed.

**Parameters:**
- evt

- a

PropertyChangeEvent

object describing the
event source and the property that has changed.

**Throws:**
- PropertyVetoException

- if the recipient wishes the property
change to be rolled back.

---

### Additional Sections

#### Interface VetoableChangeListener

**All Superinterfaces:** EventListener

**All Known Implementing Classes:** BeanContextServicesSupport

,

BeanContextSupport

,

VetoableChangeListenerProxy

```java
public interface
VetoableChangeListener

extends
EventListener
```

A VetoableChange event gets fired whenever a bean changes a "constrained"
property. You can register a VetoableChangeListener with a source bean
so as to be notified of any constrained property updates.

**Since:** 1.1

public interface

VetoableChangeListener

extends

EventListener

A VetoableChange event gets fired whenever a bean changes a "constrained"
property. You can register a VetoableChangeListener with a source bean
so as to be notified of any constrained property updates.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

vetoableChange

​(

PropertyChangeEvent

evt)

This method gets called when a constrained property is changed.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

vetoableChange

​(

PropertyChangeEvent

evt)

This method gets called when a constrained property is changed.

---

#### Method Summary

This method gets called when a constrained property is changed.

============ METHOD DETAIL ==========

- Method Detail

- vetoableChange

```java
void vetoableChange​(
PropertyChangeEvent
evt)
throws
PropertyVetoException
```

This method gets called when a constrained property is changed.

**Parameters:** evt

- a

PropertyChangeEvent

object describing the
event source and the property that has changed.
**Throws:** PropertyVetoException

- if the recipient wishes the property
change to be rolled back.

Method Detail

- vetoableChange

```java
void vetoableChange​(
PropertyChangeEvent
evt)
throws
PropertyVetoException
```

This method gets called when a constrained property is changed.

**Parameters:** evt

- a

PropertyChangeEvent

object describing the
event source and the property that has changed.
**Throws:** PropertyVetoException

- if the recipient wishes the property
change to be rolled back.

---

#### Method Detail

vetoableChange

```java
void vetoableChange​(
PropertyChangeEvent
evt)
throws
PropertyVetoException
```

This method gets called when a constrained property is changed.

**Parameters:** evt

- a

PropertyChangeEvent

object describing the
event source and the property that has changed.
**Throws:** PropertyVetoException

- if the recipient wishes the property
change to be rolled back.

---

#### vetoableChange

void vetoableChange​(

PropertyChangeEvent

evt)
throws

PropertyVetoException

This method gets called when a constrained property is changed.

---

