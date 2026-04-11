# Interface ComboBoxEditor

**Source:** `java.desktop\javax\swing\ComboBoxEditor.html`

### Class Description

```java
public interface
ComboBoxEditor
```

The editor component used for JComboBox components.

**All Known Implementing Classes:** BasicComboBoxEditor

,

BasicComboBoxEditor.UIResource

,

MetalComboBoxEditor

,

MetalComboBoxEditor.UIResource

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Component
getEditorComponent()

Returns the component that should be added to the tree hierarchy for
this editor

**Returns:**
- the component

---

#### void setItem​(
Object
anObject)

Set the item that should be edited. Cancel any editing if necessary

**Parameters:**
- anObject

- an item

---

#### Object
getItem()

Returns the edited item

**Returns:**
- the edited item

---

#### void selectAll()

Ask the editor to start editing and to select everything

---

#### void addActionListener​(
ActionListener
l)

Add an ActionListener. An action event is generated when the edited item changes

**Parameters:**
- l

- an

ActionListener

---

#### void removeActionListener​(
ActionListener
l)

Remove an ActionListener

**Parameters:**
- l

- an

ActionListener

---

### Additional Sections

#### Interface ComboBoxEditor

**All Known Implementing Classes:** BasicComboBoxEditor

,

BasicComboBoxEditor.UIResource

,

MetalComboBoxEditor

,

MetalComboBoxEditor.UIResource

```java
public interface
ComboBoxEditor
```

The editor component used for JComboBox components.

**Since:** 1.2

public interface

ComboBoxEditor

The editor component used for JComboBox components.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addActionListener

​(

ActionListener

l)

Add an ActionListener.

Component

getEditorComponent

()

Returns the component that should be added to the tree hierarchy for
this editor

Object

getItem

()

Returns the edited item

void

removeActionListener

​(

ActionListener

l)

Remove an ActionListener

void

selectAll

()

Ask the editor to start editing and to select everything

void

setItem

​(

Object

anObject)

Set the item that should be edited.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addActionListener

​(

ActionListener

l)

Add an ActionListener.

Component

getEditorComponent

()

Returns the component that should be added to the tree hierarchy for
this editor

Object

getItem

()

Returns the edited item

void

removeActionListener

​(

ActionListener

l)

Remove an ActionListener

void

selectAll

()

Ask the editor to start editing and to select everything

void

setItem

​(

Object

anObject)

Set the item that should be edited.

---

#### Method Summary

Add an ActionListener.

Returns the component that should be added to the tree hierarchy for
this editor

Returns the edited item

Remove an ActionListener

Ask the editor to start editing and to select everything

Set the item that should be edited.

============ METHOD DETAIL ==========

- Method Detail

- getEditorComponent

```java
Component
getEditorComponent()
```

Returns the component that should be added to the tree hierarchy for
this editor

**Returns:** the component

- setItem

```java
void setItem​(
Object
anObject)
```

Set the item that should be edited. Cancel any editing if necessary

**Parameters:** anObject

- an item

- getItem

```java
Object
getItem()
```

Returns the edited item

**Returns:** the edited item

- selectAll

```java
void selectAll()
```

Ask the editor to start editing and to select everything

- addActionListener

```java
void addActionListener​(
ActionListener
l)
```

Add an ActionListener. An action event is generated when the edited item changes

**Parameters:** l

- an

ActionListener

- removeActionListener

```java
void removeActionListener​(
ActionListener
l)
```

Remove an ActionListener

**Parameters:** l

- an

ActionListener

Method Detail

- getEditorComponent

```java
Component
getEditorComponent()
```

Returns the component that should be added to the tree hierarchy for
this editor

**Returns:** the component

- setItem

```java
void setItem​(
Object
anObject)
```

Set the item that should be edited. Cancel any editing if necessary

**Parameters:** anObject

- an item

- getItem

```java
Object
getItem()
```

Returns the edited item

**Returns:** the edited item

- selectAll

```java
void selectAll()
```

Ask the editor to start editing and to select everything

- addActionListener

```java
void addActionListener​(
ActionListener
l)
```

Add an ActionListener. An action event is generated when the edited item changes

**Parameters:** l

- an

ActionListener

- removeActionListener

```java
void removeActionListener​(
ActionListener
l)
```

Remove an ActionListener

**Parameters:** l

- an

ActionListener

---

#### Method Detail

getEditorComponent

```java
Component
getEditorComponent()
```

Returns the component that should be added to the tree hierarchy for
this editor

**Returns:** the component

---

#### getEditorComponent

Component

getEditorComponent()

Returns the component that should be added to the tree hierarchy for
this editor

setItem

```java
void setItem​(
Object
anObject)
```

Set the item that should be edited. Cancel any editing if necessary

**Parameters:** anObject

- an item

---

#### setItem

void setItem​(

Object

anObject)

Set the item that should be edited. Cancel any editing if necessary

getItem

```java
Object
getItem()
```

Returns the edited item

**Returns:** the edited item

---

#### getItem

Object

getItem()

Returns the edited item

selectAll

```java
void selectAll()
```

Ask the editor to start editing and to select everything

---

#### selectAll

void selectAll()

Ask the editor to start editing and to select everything

addActionListener

```java
void addActionListener​(
ActionListener
l)
```

Add an ActionListener. An action event is generated when the edited item changes

**Parameters:** l

- an

ActionListener

---

#### addActionListener

void addActionListener​(

ActionListener

l)

Add an ActionListener. An action event is generated when the edited item changes

removeActionListener

```java
void removeActionListener​(
ActionListener
l)
```

Remove an ActionListener

**Parameters:** l

- an

ActionListener

---

#### removeActionListener

void removeActionListener​(

ActionListener

l)

Remove an ActionListener

---

