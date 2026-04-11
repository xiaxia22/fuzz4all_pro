# Class BasicColorChooserUI

**Source:** `java.desktop\javax\swing\plaf\basic\BasicColorChooserUI.html`

### Class Description

```java
public class
BasicColorChooserUI

extends
ColorChooserUI
```

Provides the basic look and feel for a JColorChooser.

**Direct Known Subclasses:** SynthColorChooserUI

---

### Field Details

#### protected
JColorChooser
chooser

JColorChooser this BasicColorChooserUI is installed on.

**Since:**
- 1.5

---

#### protected
AbstractColorChooserPanel
[] defaultChoosers

The array of default color choosers.

---

#### protected
ChangeListener
previewListener

The instance of

ChangeListener

.

---

#### protected
PropertyChangeListener
propertyChangeListener

The instance of

PropertyChangeListener

.

---

### Constructor Details

#### public BasicColorChooserUI()

*No description found.*

---

### Method Details

#### public static
ComponentUI
createUI​(
JComponent
c)

Returns a new instance of

BasicColorChooserUI

.

**Parameters:**
- c

- a component

**Returns:**
- a new instance of

BasicColorChooserUI

---

#### protected
AbstractColorChooserPanel
[] createDefaultChoosers()

Returns an array of default color choosers.

**Returns:**
- an array of default color choosers

---

#### protected void uninstallDefaultChoosers()

Uninstalls default color choosers.

---

#### protected void installPreviewPanel()

Installs preview panel.

---

#### protected void uninstallPreviewPanel()

Removes installed preview panel from the UI delegate.

**Since:**
- 1.7

---

#### protected void installDefaults()

Installs default properties.

---

#### protected void uninstallDefaults()

Uninstalls default properties.

---

#### protected void installListeners()

Registers listeners.

---

#### protected
PropertyChangeListener
createPropertyChangeListener()

Returns an instance of

PropertyChangeListener

.

**Returns:**
- an instance of

PropertyChangeListener

---

#### protected void uninstallListeners()

Unregisters listeners.

---

### Additional Sections

#### Class BasicColorChooserUI

java.lang.Object

- javax.swing.plaf.ComponentUI
- - javax.swing.plaf.ColorChooserUI
- - javax.swing.plaf.basic.BasicColorChooserUI

javax.swing.plaf.ComponentUI

- javax.swing.plaf.ColorChooserUI
- - javax.swing.plaf.basic.BasicColorChooserUI

javax.swing.plaf.ColorChooserUI

- javax.swing.plaf.basic.BasicColorChooserUI

javax.swing.plaf.basic.BasicColorChooserUI

**Direct Known Subclasses:** SynthColorChooserUI

```java
public class
BasicColorChooserUI

extends
ColorChooserUI
```

Provides the basic look and feel for a JColorChooser.

public class

BasicColorChooserUI

extends

ColorChooserUI

Provides the basic look and feel for a JColorChooser.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

BasicColorChooserUI.PropertyHandler

This class should be treated as a "protected" inner class.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

protected

JColorChooser

chooser

JColorChooser this BasicColorChooserUI is installed on.

protected

AbstractColorChooserPanel

[]

defaultChoosers

The array of default color choosers.

protected

ChangeListener

previewListener

The instance of

ChangeListener

.

protected

PropertyChangeListener

propertyChangeListener

The instance of

PropertyChangeListener

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

BasicColorChooserUI

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

AbstractColorChooserPanel

[]

createDefaultChoosers

()

Returns an array of default color choosers.

protected

PropertyChangeListener

createPropertyChangeListener

()

Returns an instance of

PropertyChangeListener

.

static

ComponentUI

createUI

​(

JComponent

c)

Returns a new instance of

BasicColorChooserUI

.

protected void

installDefaults

()

Installs default properties.

protected void

installListeners

()

Registers listeners.

protected void

installPreviewPanel

()

Installs preview panel.

protected void

uninstallDefaultChoosers

()

Uninstalls default color choosers.

protected void

uninstallDefaults

()

Uninstalls default properties.

protected void

uninstallListeners

()

Unregisters listeners.

protected void

uninstallPreviewPanel

()

Removes installed preview panel from the UI delegate.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

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

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

class

BasicColorChooserUI.PropertyHandler

This class should be treated as a "protected" inner class.

---

#### Nested Class Summary

This class should be treated as a "protected" inner class.

Field Summary

Fields

Modifier and Type

Field

Description

protected

JColorChooser

chooser

JColorChooser this BasicColorChooserUI is installed on.

protected

AbstractColorChooserPanel

[]

defaultChoosers

The array of default color choosers.

protected

ChangeListener

previewListener

The instance of

ChangeListener

.

protected

PropertyChangeListener

propertyChangeListener

The instance of

PropertyChangeListener

.

---

#### Field Summary

JColorChooser this BasicColorChooserUI is installed on.

The array of default color choosers.

The instance of

ChangeListener

.

The instance of

PropertyChangeListener

.

Constructor Summary

Constructors

Constructor

Description

BasicColorChooserUI

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

protected

AbstractColorChooserPanel

[]

createDefaultChoosers

()

Returns an array of default color choosers.

protected

PropertyChangeListener

createPropertyChangeListener

()

Returns an instance of

PropertyChangeListener

.

static

ComponentUI

createUI

​(

JComponent

c)

Returns a new instance of

BasicColorChooserUI

.

protected void

installDefaults

()

Installs default properties.

protected void

installListeners

()

Registers listeners.

protected void

installPreviewPanel

()

Installs preview panel.

protected void

uninstallDefaultChoosers

()

Uninstalls default color choosers.

protected void

uninstallDefaults

()

Uninstalls default properties.

protected void

uninstallListeners

()

Unregisters listeners.

protected void

uninstallPreviewPanel

()

Removes installed preview panel from the UI delegate.

- Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

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

---

#### Method Summary

Returns an array of default color choosers.

Returns an instance of

PropertyChangeListener

.

Returns a new instance of

BasicColorChooserUI

.

Installs default properties.

Registers listeners.

Installs preview panel.

Uninstalls default color choosers.

Uninstalls default properties.

Unregisters listeners.

Removes installed preview panel from the UI delegate.

Methods declared in class javax.swing.plaf.

ComponentUI

contains

,

getAccessibleChild

,

getAccessibleChildrenCount

,

getBaseline

,

getBaselineResizeBehavior

,

getMaximumSize

,

getMinimumSize

,

getPreferredSize

,

installUI

,

paint

,

uninstallUI

,

update

---

#### Methods declared in class javax.swing.plaf. ComponentUI

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

============ FIELD DETAIL ===========

- Field Detail

- chooser

```java
protected
JColorChooser
chooser
```

JColorChooser this BasicColorChooserUI is installed on.

**Since:** 1.5

- defaultChoosers

```java
protected
AbstractColorChooserPanel
[] defaultChoosers
```

The array of default color choosers.

- previewListener

```java
protected
ChangeListener
previewListener
```

The instance of

ChangeListener

.

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

The instance of

PropertyChangeListener

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- BasicColorChooserUI

```java
public BasicColorChooserUI()
```

============ METHOD DETAIL ==========

- Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns a new instance of

BasicColorChooserUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicColorChooserUI

- createDefaultChoosers

```java
protected
AbstractColorChooserPanel
[] createDefaultChoosers()
```

Returns an array of default color choosers.

**Returns:** an array of default color choosers

- uninstallDefaultChoosers

```java
protected void uninstallDefaultChoosers()
```

Uninstalls default color choosers.

- installPreviewPanel

```java
protected void installPreviewPanel()
```

Installs preview panel.

- uninstallPreviewPanel

```java
protected void uninstallPreviewPanel()
```

Removes installed preview panel from the UI delegate.

**Since:** 1.7

- installDefaults

```java
protected void installDefaults()
```

Installs default properties.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

- installListeners

```java
protected void installListeners()
```

Registers listeners.

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Returns an instance of

PropertyChangeListener

.

**Returns:** an instance of

PropertyChangeListener

- uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

Field Detail

- chooser

```java
protected
JColorChooser
chooser
```

JColorChooser this BasicColorChooserUI is installed on.

**Since:** 1.5

- defaultChoosers

```java
protected
AbstractColorChooserPanel
[] defaultChoosers
```

The array of default color choosers.

- previewListener

```java
protected
ChangeListener
previewListener
```

The instance of

ChangeListener

.

- propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

The instance of

PropertyChangeListener

.

---

#### Field Detail

chooser

```java
protected
JColorChooser
chooser
```

JColorChooser this BasicColorChooserUI is installed on.

**Since:** 1.5

---

#### chooser

protected

JColorChooser

chooser

JColorChooser this BasicColorChooserUI is installed on.

defaultChoosers

```java
protected
AbstractColorChooserPanel
[] defaultChoosers
```

The array of default color choosers.

---

#### defaultChoosers

protected

AbstractColorChooserPanel

[] defaultChoosers

The array of default color choosers.

previewListener

```java
protected
ChangeListener
previewListener
```

The instance of

ChangeListener

.

---

#### previewListener

protected

ChangeListener

previewListener

The instance of

ChangeListener

.

propertyChangeListener

```java
protected
PropertyChangeListener
propertyChangeListener
```

The instance of

PropertyChangeListener

.

---

#### propertyChangeListener

protected

PropertyChangeListener

propertyChangeListener

The instance of

PropertyChangeListener

.

Constructor Detail

- BasicColorChooserUI

```java
public BasicColorChooserUI()
```

---

#### Constructor Detail

BasicColorChooserUI

```java
public BasicColorChooserUI()
```

---

#### BasicColorChooserUI

public BasicColorChooserUI()

Method Detail

- createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns a new instance of

BasicColorChooserUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicColorChooserUI

- createDefaultChoosers

```java
protected
AbstractColorChooserPanel
[] createDefaultChoosers()
```

Returns an array of default color choosers.

**Returns:** an array of default color choosers

- uninstallDefaultChoosers

```java
protected void uninstallDefaultChoosers()
```

Uninstalls default color choosers.

- installPreviewPanel

```java
protected void installPreviewPanel()
```

Installs preview panel.

- uninstallPreviewPanel

```java
protected void uninstallPreviewPanel()
```

Removes installed preview panel from the UI delegate.

**Since:** 1.7

- installDefaults

```java
protected void installDefaults()
```

Installs default properties.

- uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

- installListeners

```java
protected void installListeners()
```

Registers listeners.

- createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Returns an instance of

PropertyChangeListener

.

**Returns:** an instance of

PropertyChangeListener

- uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

---

#### Method Detail

createUI

```java
public static
ComponentUI
createUI​(
JComponent
c)
```

Returns a new instance of

BasicColorChooserUI

.

**Parameters:** c

- a component
**Returns:** a new instance of

BasicColorChooserUI

---

#### createUI

public static

ComponentUI

createUI​(

JComponent

c)

Returns a new instance of

BasicColorChooserUI

.

createDefaultChoosers

```java
protected
AbstractColorChooserPanel
[] createDefaultChoosers()
```

Returns an array of default color choosers.

**Returns:** an array of default color choosers

---

#### createDefaultChoosers

protected

AbstractColorChooserPanel

[] createDefaultChoosers()

Returns an array of default color choosers.

uninstallDefaultChoosers

```java
protected void uninstallDefaultChoosers()
```

Uninstalls default color choosers.

---

#### uninstallDefaultChoosers

protected void uninstallDefaultChoosers()

Uninstalls default color choosers.

installPreviewPanel

```java
protected void installPreviewPanel()
```

Installs preview panel.

---

#### installPreviewPanel

protected void installPreviewPanel()

Installs preview panel.

uninstallPreviewPanel

```java
protected void uninstallPreviewPanel()
```

Removes installed preview panel from the UI delegate.

**Since:** 1.7

---

#### uninstallPreviewPanel

protected void uninstallPreviewPanel()

Removes installed preview panel from the UI delegate.

installDefaults

```java
protected void installDefaults()
```

Installs default properties.

---

#### installDefaults

protected void installDefaults()

Installs default properties.

uninstallDefaults

```java
protected void uninstallDefaults()
```

Uninstalls default properties.

---

#### uninstallDefaults

protected void uninstallDefaults()

Uninstalls default properties.

installListeners

```java
protected void installListeners()
```

Registers listeners.

---

#### installListeners

protected void installListeners()

Registers listeners.

createPropertyChangeListener

```java
protected
PropertyChangeListener
createPropertyChangeListener()
```

Returns an instance of

PropertyChangeListener

.

**Returns:** an instance of

PropertyChangeListener

---

#### createPropertyChangeListener

protected

PropertyChangeListener

createPropertyChangeListener()

Returns an instance of

PropertyChangeListener

.

uninstallListeners

```java
protected void uninstallListeners()
```

Unregisters listeners.

---

#### uninstallListeners

protected void uninstallListeners()

Unregisters listeners.

---

