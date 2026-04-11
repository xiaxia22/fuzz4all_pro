# Interface ComboPopup

**Source:** `java.desktop\javax\swing\plaf\basic\ComboPopup.html`

### Class Description

```java
public interface
ComboPopup
```

The interface which defines the methods required for the implementation of the popup
portion of a combo box.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

**All Known Implementing Classes:** BasicComboPopup

,

MetalComboBoxUI.MetalComboPopup

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void show()

Shows the popup

---

#### void hide()

Hides the popup

---

#### boolean isVisible()

Returns true if the popup is visible (currently being displayed).

**Returns:**
- true

if the component is visible;

false

otherwise.

---

#### JList
<
Object
> getList()

Returns the list that is being used to draw the items in the combo box.
This method is highly implementation specific and should not be used
for general list manipulation.

**Returns:**
- the list that is being used to draw the items in the combo box

---

#### MouseListener
getMouseListener()

Returns a mouse listener that will be added to the combo box or null.
If this method returns null then it will not be added to the combo box.

**Returns:**
- a

MouseListener

or null

---

#### MouseMotionListener
getMouseMotionListener()

Returns a mouse motion listener that will be added to the combo box or null.
If this method returns null then it will not be added to the combo box.

**Returns:**
- a

MouseMotionListener

or null

---

#### KeyListener
getKeyListener()

Returns a key listener that will be added to the combo box or null.
If this method returns null then it will not be added to the combo box.

**Returns:**
- a key listener that will be added to the combo box or null

---

#### void uninstallingUI()

Called to inform the ComboPopup that the UI is uninstalling.
If the ComboPopup added any listeners in the component, it should remove them here.

---

### Additional Sections

#### Interface ComboPopup

**All Known Implementing Classes:** BasicComboPopup

,

MetalComboBoxUI.MetalComboPopup

```java
public interface
ComboPopup
```

The interface which defines the methods required for the implementation of the popup
portion of a combo box.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

public interface

ComboPopup

The interface which defines the methods required for the implementation of the popup
portion of a combo box.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

Warning:

Serialized objects of this class will not be compatible with
future Swing releases. The current serialization support is
appropriate for short term storage or RMI between applications running
the same version of Swing. As of 1.4, support for long term storage
of all JavaBeans™
has been added to the

java.beans

package.
Please see

XMLEncoder

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

KeyListener

getKeyListener

()

Returns a key listener that will be added to the combo box or null.

JList

<

Object

>

getList

()

Returns the list that is being used to draw the items in the combo box.

MouseListener

getMouseListener

()

Returns a mouse listener that will be added to the combo box or null.

MouseMotionListener

getMouseMotionListener

()

Returns a mouse motion listener that will be added to the combo box or null.

void

hide

()

Hides the popup

boolean

isVisible

()

Returns true if the popup is visible (currently being displayed).

void

show

()

Shows the popup

void

uninstallingUI

()

Called to inform the ComboPopup that the UI is uninstalling.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

KeyListener

getKeyListener

()

Returns a key listener that will be added to the combo box or null.

JList

<

Object

>

getList

()

Returns the list that is being used to draw the items in the combo box.

MouseListener

getMouseListener

()

Returns a mouse listener that will be added to the combo box or null.

MouseMotionListener

getMouseMotionListener

()

Returns a mouse motion listener that will be added to the combo box or null.

void

hide

()

Hides the popup

boolean

isVisible

()

Returns true if the popup is visible (currently being displayed).

void

show

()

Shows the popup

void

uninstallingUI

()

Called to inform the ComboPopup that the UI is uninstalling.

---

#### Method Summary

Returns a key listener that will be added to the combo box or null.

Returns the list that is being used to draw the items in the combo box.

Returns a mouse listener that will be added to the combo box or null.

Returns a mouse motion listener that will be added to the combo box or null.

Hides the popup

Returns true if the popup is visible (currently being displayed).

Shows the popup

Called to inform the ComboPopup that the UI is uninstalling.

============ METHOD DETAIL ==========

- Method Detail

- show

```java
void show()
```

Shows the popup

- hide

```java
void hide()
```

Hides the popup

- isVisible

```java
boolean isVisible()
```

Returns true if the popup is visible (currently being displayed).

**Returns:** true

if the component is visible;

false

otherwise.

- getList

```java
JList
<
Object
> getList()
```

Returns the list that is being used to draw the items in the combo box.
This method is highly implementation specific and should not be used
for general list manipulation.

**Returns:** the list that is being used to draw the items in the combo box

- getMouseListener

```java
MouseListener
getMouseListener()
```

Returns a mouse listener that will be added to the combo box or null.
If this method returns null then it will not be added to the combo box.

**Returns:** a

MouseListener

or null

- getMouseMotionListener

```java
MouseMotionListener
getMouseMotionListener()
```

Returns a mouse motion listener that will be added to the combo box or null.
If this method returns null then it will not be added to the combo box.

**Returns:** a

MouseMotionListener

or null

- getKeyListener

```java
KeyListener
getKeyListener()
```

Returns a key listener that will be added to the combo box or null.
If this method returns null then it will not be added to the combo box.

**Returns:** a key listener that will be added to the combo box or null

- uninstallingUI

```java
void uninstallingUI()
```

Called to inform the ComboPopup that the UI is uninstalling.
If the ComboPopup added any listeners in the component, it should remove them here.

Method Detail

- show

```java
void show()
```

Shows the popup

- hide

```java
void hide()
```

Hides the popup

- isVisible

```java
boolean isVisible()
```

Returns true if the popup is visible (currently being displayed).

**Returns:** true

if the component is visible;

false

otherwise.

- getList

```java
JList
<
Object
> getList()
```

Returns the list that is being used to draw the items in the combo box.
This method is highly implementation specific and should not be used
for general list manipulation.

**Returns:** the list that is being used to draw the items in the combo box

- getMouseListener

```java
MouseListener
getMouseListener()
```

Returns a mouse listener that will be added to the combo box or null.
If this method returns null then it will not be added to the combo box.

**Returns:** a

MouseListener

or null

- getMouseMotionListener

```java
MouseMotionListener
getMouseMotionListener()
```

Returns a mouse motion listener that will be added to the combo box or null.
If this method returns null then it will not be added to the combo box.

**Returns:** a

MouseMotionListener

or null

- getKeyListener

```java
KeyListener
getKeyListener()
```

Returns a key listener that will be added to the combo box or null.
If this method returns null then it will not be added to the combo box.

**Returns:** a key listener that will be added to the combo box or null

- uninstallingUI

```java
void uninstallingUI()
```

Called to inform the ComboPopup that the UI is uninstalling.
If the ComboPopup added any listeners in the component, it should remove them here.

---

#### Method Detail

show

```java
void show()
```

Shows the popup

---

#### show

void show()

Shows the popup

hide

```java
void hide()
```

Hides the popup

---

#### hide

void hide()

Hides the popup

isVisible

```java
boolean isVisible()
```

Returns true if the popup is visible (currently being displayed).

**Returns:** true

if the component is visible;

false

otherwise.

---

#### isVisible

boolean isVisible()

Returns true if the popup is visible (currently being displayed).

getList

```java
JList
<
Object
> getList()
```

Returns the list that is being used to draw the items in the combo box.
This method is highly implementation specific and should not be used
for general list manipulation.

**Returns:** the list that is being used to draw the items in the combo box

---

#### getList

JList

<

Object

> getList()

Returns the list that is being used to draw the items in the combo box.
This method is highly implementation specific and should not be used
for general list manipulation.

getMouseListener

```java
MouseListener
getMouseListener()
```

Returns a mouse listener that will be added to the combo box or null.
If this method returns null then it will not be added to the combo box.

**Returns:** a

MouseListener

or null

---

#### getMouseListener

MouseListener

getMouseListener()

Returns a mouse listener that will be added to the combo box or null.
If this method returns null then it will not be added to the combo box.

getMouseMotionListener

```java
MouseMotionListener
getMouseMotionListener()
```

Returns a mouse motion listener that will be added to the combo box or null.
If this method returns null then it will not be added to the combo box.

**Returns:** a

MouseMotionListener

or null

---

#### getMouseMotionListener

MouseMotionListener

getMouseMotionListener()

Returns a mouse motion listener that will be added to the combo box or null.
If this method returns null then it will not be added to the combo box.

getKeyListener

```java
KeyListener
getKeyListener()
```

Returns a key listener that will be added to the combo box or null.
If this method returns null then it will not be added to the combo box.

**Returns:** a key listener that will be added to the combo box or null

---

#### getKeyListener

KeyListener

getKeyListener()

Returns a key listener that will be added to the combo box or null.
If this method returns null then it will not be added to the combo box.

uninstallingUI

```java
void uninstallingUI()
```

Called to inform the ComboPopup that the UI is uninstalling.
If the ComboPopup added any listeners in the component, it should remove them here.

---

#### uninstallingUI

void uninstallingUI()

Called to inform the ComboPopup that the UI is uninstalling.
If the ComboPopup added any listeners in the component, it should remove them here.

---

