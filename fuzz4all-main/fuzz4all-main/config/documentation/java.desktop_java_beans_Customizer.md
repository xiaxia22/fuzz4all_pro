# Interface Customizer

**Source:** `java.desktop\java\beans\Customizer.html`

### Class Description

```java
public interface
Customizer
```

A customizer class provides a complete custom GUI for customizing
a target Java Bean.

Each customizer should inherit from the java.awt.Component class so
it can be instantiated inside an AWT dialog or panel.

Each customizer should have a null constructor.

**Since:** 1.1

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void setObject​(
Object
bean)

Set the object to be customized. This method should be called only
once, before the Customizer has been added to any parent AWT container.

**Parameters:**
- bean

- The object to be customized.

---

#### void addPropertyChangeListener​(
PropertyChangeListener
listener)

Register a listener for the PropertyChange event. The customizer
should fire a PropertyChange event whenever it changes the target
bean in a way that might require the displayed properties to be
refreshed.

**Parameters:**
- listener

- An object to be invoked when a PropertyChange
event is fired.

---

#### void removePropertyChangeListener​(
PropertyChangeListener
listener)

Remove a listener for the PropertyChange event.

**Parameters:**
- listener

- The PropertyChange listener to be removed.

---

### Additional Sections

#### Interface Customizer

```java
public interface
Customizer
```

A customizer class provides a complete custom GUI for customizing
a target Java Bean.

Each customizer should inherit from the java.awt.Component class so
it can be instantiated inside an AWT dialog or panel.

Each customizer should have a null constructor.

**Since:** 1.1

public interface

Customizer

A customizer class provides a complete custom GUI for customizing
a target Java Bean.

Each customizer should inherit from the java.awt.Component class so
it can be instantiated inside an AWT dialog or panel.

Each customizer should have a null constructor.

Each customizer should inherit from the java.awt.Component class so
it can be instantiated inside an AWT dialog or panel.

Each customizer should have a null constructor.

Each customizer should have a null constructor.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addPropertyChangeListener

​(

PropertyChangeListener

listener)

Register a listener for the PropertyChange event.

void

removePropertyChangeListener

​(

PropertyChangeListener

listener)

Remove a listener for the PropertyChange event.

void

setObject

​(

Object

bean)

Set the object to be customized.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addPropertyChangeListener

​(

PropertyChangeListener

listener)

Register a listener for the PropertyChange event.

void

removePropertyChangeListener

​(

PropertyChangeListener

listener)

Remove a listener for the PropertyChange event.

void

setObject

​(

Object

bean)

Set the object to be customized.

---

#### Method Summary

Register a listener for the PropertyChange event.

Remove a listener for the PropertyChange event.

Set the object to be customized.

============ METHOD DETAIL ==========

- Method Detail

- setObject

```java
void setObject​(
Object
bean)
```

Set the object to be customized. This method should be called only
once, before the Customizer has been added to any parent AWT container.

**Parameters:** bean

- The object to be customized.

- addPropertyChangeListener

```java
void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Register a listener for the PropertyChange event. The customizer
should fire a PropertyChange event whenever it changes the target
bean in a way that might require the displayed properties to be
refreshed.

**Parameters:** listener

- An object to be invoked when a PropertyChange
event is fired.

- removePropertyChangeListener

```java
void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Remove a listener for the PropertyChange event.

**Parameters:** listener

- The PropertyChange listener to be removed.

Method Detail

- setObject

```java
void setObject​(
Object
bean)
```

Set the object to be customized. This method should be called only
once, before the Customizer has been added to any parent AWT container.

**Parameters:** bean

- The object to be customized.

- addPropertyChangeListener

```java
void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Register a listener for the PropertyChange event. The customizer
should fire a PropertyChange event whenever it changes the target
bean in a way that might require the displayed properties to be
refreshed.

**Parameters:** listener

- An object to be invoked when a PropertyChange
event is fired.

- removePropertyChangeListener

```java
void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Remove a listener for the PropertyChange event.

**Parameters:** listener

- The PropertyChange listener to be removed.

---

#### Method Detail

setObject

```java
void setObject​(
Object
bean)
```

Set the object to be customized. This method should be called only
once, before the Customizer has been added to any parent AWT container.

**Parameters:** bean

- The object to be customized.

---

#### setObject

void setObject​(

Object

bean)

Set the object to be customized. This method should be called only
once, before the Customizer has been added to any parent AWT container.

addPropertyChangeListener

```java
void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Register a listener for the PropertyChange event. The customizer
should fire a PropertyChange event whenever it changes the target
bean in a way that might require the displayed properties to be
refreshed.

**Parameters:** listener

- An object to be invoked when a PropertyChange
event is fired.

---

#### addPropertyChangeListener

void addPropertyChangeListener​(

PropertyChangeListener

listener)

Register a listener for the PropertyChange event. The customizer
should fire a PropertyChange event whenever it changes the target
bean in a way that might require the displayed properties to be
refreshed.

removePropertyChangeListener

```java
void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Remove a listener for the PropertyChange event.

**Parameters:** listener

- The PropertyChange listener to be removed.

---

#### removePropertyChangeListener

void removePropertyChangeListener​(

PropertyChangeListener

listener)

Remove a listener for the PropertyChange event.

---

