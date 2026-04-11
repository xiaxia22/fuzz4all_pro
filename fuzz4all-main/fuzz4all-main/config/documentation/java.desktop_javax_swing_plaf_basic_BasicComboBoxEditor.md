# Class BasicComboBoxEditor

**Source:** `java.desktop\javax\swing\plaf\basic\BasicComboBoxEditor.html`

### Class Description

```java
public class
BasicComboBoxEditor

extends
Object

implements
ComboBoxEditor
,
FocusListener
```

The default editor for editable combo boxes. The editor is implemented as a JTextField.

**All Implemented Interfaces:** FocusListener

,

EventListener

,

ComboBoxEditor

---

### Field Details

#### protected
JTextField
editor

An instance of

JTextField

.

---

### Constructor Details

#### public BasicComboBoxEditor()

Constructs a new instance of

BasicComboBoxEditor

.

---

### Method Details

#### protected
JTextField
createEditorComponent()

Creates the internal editor component. Override this to provide
a custom implementation.

**Returns:**
- a new editor component

**Since:**
- 1.6

---

#### public void setItem​(
Object
anObject)

Sets the item that should be edited.

**Specified by:**
- setItem

in interface

ComboBoxEditor

**Parameters:**
- anObject

- the displayed value of the editor

---

### Additional Sections

#### Class BasicComboBoxEditor

java.lang.Object

- javax.swing.plaf.basic.BasicComboBoxEditor

javax.swing.plaf.basic.BasicComboBoxEditor

**All Implemented Interfaces:** FocusListener

,

EventListener

,

ComboBoxEditor

**Direct Known Subclasses:** BasicComboBoxEditor.UIResource

,

MetalComboBoxEditor

```java
public class
BasicComboBoxEditor

extends
Object

implements
ComboBoxEditor
,
FocusListener
```

The default editor for editable combo boxes. The editor is implemented as a JTextField.

public class

BasicComboBoxEditor

extends

Object

implements

ComboBoxEditor

,

FocusListener

The default editor for editable combo boxes. The editor is implemented as a JTextField.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

BasicComboBoxEditor.UIResource

A subclass of BasicComboBoxEditor that implements UIResource.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

JTextField

editor

An instance of

JTextField

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicComboBoxEditor

()

Constructs a new instance of

BasicComboBoxEditor

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

JTextField

createEditorComponent

()

Creates the internal editor component.

void

setItem

​(

Object

anObject)

Sets the item that should be edited.

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

toString

,

wait

,

wait

,

wait

- Methods declared in interface javax.swing.

ComboBoxEditor

addActionListener

,

getEditorComponent

,

getItem

,

removeActionListener

,

selectAll

- Methods declared in interface java.awt.event.

FocusListener

focusGained

,

focusLost

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

BasicComboBoxEditor.UIResource

A subclass of BasicComboBoxEditor that implements UIResource.

---

#### Nested Class Summary

A subclass of BasicComboBoxEditor that implements UIResource.

Field Summary

Fields

Modifier and Type

Field

Description

protected

JTextField

editor

An instance of

JTextField

.

---

#### Field Summary

An instance of

JTextField

.

Constructor Summary

Constructors

Constructor

Description

BasicComboBoxEditor

()

Constructs a new instance of

BasicComboBoxEditor

.

---

#### Constructor Summary

Constructs a new instance of

BasicComboBoxEditor

.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

JTextField

createEditorComponent

()

Creates the internal editor component.

void

setItem

​(

Object

anObject)

Sets the item that should be edited.

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

toString

,

wait

,

wait

,

wait

- Methods declared in interface javax.swing.

ComboBoxEditor

addActionListener

,

getEditorComponent

,

getItem

,

removeActionListener

,

selectAll

- Methods declared in interface java.awt.event.

FocusListener

focusGained

,

focusLost

---

#### Method Summary

Creates the internal editor component.

Sets the item that should be edited.

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

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface javax.swing.

ComboBoxEditor

addActionListener

,

getEditorComponent

,

getItem

,

removeActionListener

,

selectAll

---

#### Methods declared in interface javax.swing. ComboBoxEditor

Methods declared in interface java.awt.event.

FocusListener

focusGained

,

focusLost

---

#### Methods declared in interface java.awt.event. FocusListener

============ FIELD DETAIL ===========

- Field Detail

- editor

```java
protected
JTextField
editor
```

An instance of

JTextField

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicComboBoxEditor

```java
public BasicComboBoxEditor()
```

Constructs a new instance of

BasicComboBoxEditor

.

============ METHOD DETAIL ==========

- Method Detail

- createEditorComponent

```java
protected
JTextField
createEditorComponent()
```

Creates the internal editor component. Override this to provide
a custom implementation.

**Returns:** a new editor component
**Since:** 1.6

- setItem

```java
public void setItem​(
Object
anObject)
```

Sets the item that should be edited.

**Specified by:** setItem

in interface

ComboBoxEditor
**Parameters:** anObject

- the displayed value of the editor

Field Detail

- editor

```java
protected
JTextField
editor
```

An instance of

JTextField

.

---

#### Field Detail

editor

```java
protected
JTextField
editor
```

An instance of

JTextField

.

---

#### editor

protected

JTextField

editor

An instance of

JTextField

.

Constructor Detail

- BasicComboBoxEditor

```java
public BasicComboBoxEditor()
```

Constructs a new instance of

BasicComboBoxEditor

.

---

#### Constructor Detail

BasicComboBoxEditor

```java
public BasicComboBoxEditor()
```

Constructs a new instance of

BasicComboBoxEditor

.

---

#### BasicComboBoxEditor

public BasicComboBoxEditor()

Constructs a new instance of

BasicComboBoxEditor

.

Method Detail

- createEditorComponent

```java
protected
JTextField
createEditorComponent()
```

Creates the internal editor component. Override this to provide
a custom implementation.

**Returns:** a new editor component
**Since:** 1.6

- setItem

```java
public void setItem​(
Object
anObject)
```

Sets the item that should be edited.

**Specified by:** setItem

in interface

ComboBoxEditor
**Parameters:** anObject

- the displayed value of the editor

---

#### Method Detail

createEditorComponent

```java
protected
JTextField
createEditorComponent()
```

Creates the internal editor component. Override this to provide
a custom implementation.

**Returns:** a new editor component
**Since:** 1.6

---

#### createEditorComponent

protected

JTextField

createEditorComponent()

Creates the internal editor component. Override this to provide
a custom implementation.

setItem

```java
public void setItem​(
Object
anObject)
```

Sets the item that should be edited.

**Specified by:** setItem

in interface

ComboBoxEditor
**Parameters:** anObject

- the displayed value of the editor

---

#### setItem

public void setItem​(

Object

anObject)

Sets the item that should be edited.

---

