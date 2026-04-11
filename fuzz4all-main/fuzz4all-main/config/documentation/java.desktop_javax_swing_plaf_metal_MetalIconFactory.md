# Class MetalIconFactory

**Source:** `java.desktop\javax\swing\plaf\metal\MetalIconFactory.html`

### Class Description

```java
public class
MetalIconFactory

extends
Object

implements
Serializable
```

Factory object that vends

Icon

s for
the Java™ look and feel (Metal).
These icons are used extensively in Metal via the defaults mechanism.
While other look and feels often use GIFs for icons, creating icons
in code facilitates switching to other themes.

Each method in this class returns
either an

Icon

or

null

,
where

null

implies that there is no default icon.

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

**All Implemented Interfaces:** Serializable

---

### Field Details

#### public static final boolean DARK

DARK

is used for the property

Tree.expandedIcon

.

**See Also:**
- Constant Field Values

---

#### public static final boolean LIGHT

LIGHT

is used for the property

Tree.collapsedIcon

.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public MetalIconFactory()

*No description found.*

---

### Method Details

#### public static
Icon
getFileChooserDetailViewIcon()

Returns the instance of

FileChooserDetailViewIcon

.

**Returns:**
- the instance of

FileChooserDetailViewIcon

---

#### public static
Icon
getFileChooserHomeFolderIcon()

Returns the instance of

FileChooserHomeFolderIcon

.

**Returns:**
- the instance of

FileChooserHomeFolderIcon

---

#### public static
Icon
getFileChooserListViewIcon()

Returns the instance of

FileChooserListViewIcon

.

**Returns:**
- the instance of

FileChooserListViewIcon

---

#### public static
Icon
getFileChooserNewFolderIcon()

Returns the instance of

FileChooserNewFolderIcon

.

**Returns:**
- the instance of

FileChooserNewFolderIcon

---

#### public static
Icon
getFileChooserUpFolderIcon()

Returns the instance of

FileChooserUpFolderIcon

.

**Returns:**
- the instance of

FileChooserUpFolderIcon

---

#### public static
Icon
getInternalFrameAltMaximizeIcon​(int size)

Constructs a new instance of

InternalFrameAltMaximizeIcon

.

**Parameters:**
- size

- the size of the icon

**Returns:**
- a new instance of

InternalFrameAltMaximizeIcon

---

#### public static
Icon
getInternalFrameCloseIcon​(int size)

Constructs a new instance of

InternalFrameCloseIcon

.

**Parameters:**
- size

- the size of the icon

**Returns:**
- a new instance of

InternalFrameCloseIcon

---

#### public static
Icon
getInternalFrameDefaultMenuIcon()

Returns the instance of

InternalFrameDefaultMenuIcon

.

**Returns:**
- the instance of

InternalFrameDefaultMenuIcon

---

#### public static
Icon
getInternalFrameMaximizeIcon​(int size)

Constructs a new instance of

InternalFrameMaximizeIcon

.

**Parameters:**
- size

- the size of the icon

**Returns:**
- a new instance of

InternalFrameMaximizeIcon

---

#### public static
Icon
getInternalFrameMinimizeIcon​(int size)

Constructs a new instance of

InternalFrameMinimizeIcon

.

**Parameters:**
- size

- the size of the icon

**Returns:**
- a new instance of

InternalFrameMinimizeIcon

---

#### public static
Icon
getRadioButtonIcon()

Returns the instance of

RadioButtonIcon

.

**Returns:**
- the instance of

RadioButtonIcon

---

#### public static
Icon
getCheckBoxIcon()

Returns a checkbox icon.

**Returns:**
- a checkbox icon

**Since:**
- 1.3

---

#### public static
Icon
getTreeComputerIcon()

Returns the instance of

TreeComputerIcon

.

**Returns:**
- the instance of

TreeComputerIcon

---

#### public static
Icon
getTreeFloppyDriveIcon()

Returns the instance of

TreeFloppyDriveIcon

.

**Returns:**
- the instance of

TreeFloppyDriveIcon

---

#### public static
Icon
getTreeFolderIcon()

Constructs a new instance of

TreeFolderIcon

.

**Returns:**
- a new instance of

TreeFolderIcon

---

#### public static
Icon
getTreeHardDriveIcon()

Returns the instance of

TreeHardDriveIcon

.

**Returns:**
- the instance of

TreeHardDriveIcon

---

#### public static
Icon
getTreeLeafIcon()

Constructs a new instance of

TreeLeafIcon

.

**Returns:**
- a new instance of

TreeLeafIcon

---

#### public static
Icon
getTreeControlIcon​(boolean isCollapsed)

Constructs a new instance of

TreeControlIcon

.

**Parameters:**
- isCollapsed

- if

true

the icon is collapsed

**Returns:**
- a new instance of

TreeControlIcon

---

#### public static
Icon
getMenuArrowIcon()

Returns an icon to be used by

JMenu

.

**Returns:**
- an icon to be used by

JMenu

---

#### public static
Icon
getMenuItemCheckIcon()

Returns an icon to be used by

JCheckBoxMenuItem

.

**Returns:**
- the default icon for check box menu items,
or

null

if no default exists

---

#### public static
Icon
getMenuItemArrowIcon()

Returns an icon to be used by

JMenuItem

.

**Returns:**
- an icon to be used by

JMenuItem

---

#### public static
Icon
getCheckBoxMenuItemIcon()

Returns an icon to be used by

JCheckBoxMenuItem

.

**Returns:**
- an icon to be used by

JCheckBoxMenuItem

---

#### public static
Icon
getRadioButtonMenuItemIcon()

Returns an icon to be used by

JRadioButtonMenuItem

.

**Returns:**
- an icon to be used by

JRadioButtonMenuItem

---

#### public static
Icon
getHorizontalSliderThumbIcon()

Returns a thumb icon to be used by horizontal slider.

**Returns:**
- a thumb icon to be used by horizontal slider

---

#### public static
Icon
getVerticalSliderThumbIcon()

Returns a thumb icon to be used by vertical slider.

**Returns:**
- a thumb icon to be used by vertical slider

---

### Additional Sections

#### Class MetalIconFactory

java.lang.Object

- javax.swing.plaf.metal.MetalIconFactory

javax.swing.plaf.metal.MetalIconFactory

**All Implemented Interfaces:** Serializable

```java
public class
MetalIconFactory

extends
Object

implements
Serializable
```

Factory object that vends

Icon

s for
the Java™ look and feel (Metal).
These icons are used extensively in Metal via the defaults mechanism.
While other look and feels often use GIFs for icons, creating icons
in code facilitates switching to other themes.

Each method in this class returns
either an

Icon

or

null

,
where

null

implies that there is no default icon.

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

**See Also:** Serialized Form

public class

MetalIconFactory

extends

Object

implements

Serializable

Factory object that vends

Icon

s for
the Java™ look and feel (Metal).
These icons are used extensively in Metal via the defaults mechanism.
While other look and feels often use GIFs for icons, creating icons
in code facilitates switching to other themes.

Each method in this class returns
either an

Icon

or

null

,
where

null

implies that there is no default icon.

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

Each method in this class returns
either an

Icon

or

null

,
where

null

implies that there is no default icon.

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

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

MetalIconFactory.FileIcon16

Warning:

Serialized objects of this class will not be compatible with
future Swing releases.

static class

MetalIconFactory.FolderIcon16

Warning:

Serialized objects of this class will not be compatible with
future Swing releases.

static class

MetalIconFactory.PaletteCloseIcon

Defines an icon for Palette close

static class

MetalIconFactory.TreeControlIcon

Warning:

Serialized objects of this class will not be compatible with
future Swing releases.

static class

MetalIconFactory.TreeFolderIcon

Warning:

Serialized objects of this class will not be compatible with
future Swing releases.

static class

MetalIconFactory.TreeLeafIcon

The class represents a tree leaf icon.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static boolean

DARK

DARK

is used for the property

Tree.expandedIcon

.

static boolean

LIGHT

LIGHT

is used for the property

Tree.collapsedIcon

.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

MetalIconFactory

()

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Icon

getCheckBoxIcon

()

Returns a checkbox icon.

static

Icon

getCheckBoxMenuItemIcon

()

Returns an icon to be used by

JCheckBoxMenuItem

.

static

Icon

getFileChooserDetailViewIcon

()

Returns the instance of

FileChooserDetailViewIcon

.

static

Icon

getFileChooserHomeFolderIcon

()

Returns the instance of

FileChooserHomeFolderIcon

.

static

Icon

getFileChooserListViewIcon

()

Returns the instance of

FileChooserListViewIcon

.

static

Icon

getFileChooserNewFolderIcon

()

Returns the instance of

FileChooserNewFolderIcon

.

static

Icon

getFileChooserUpFolderIcon

()

Returns the instance of

FileChooserUpFolderIcon

.

static

Icon

getHorizontalSliderThumbIcon

()

Returns a thumb icon to be used by horizontal slider.

static

Icon

getInternalFrameAltMaximizeIcon

​(int size)

Constructs a new instance of

InternalFrameAltMaximizeIcon

.

static

Icon

getInternalFrameCloseIcon

​(int size)

Constructs a new instance of

InternalFrameCloseIcon

.

static

Icon

getInternalFrameDefaultMenuIcon

()

Returns the instance of

InternalFrameDefaultMenuIcon

.

static

Icon

getInternalFrameMaximizeIcon

​(int size)

Constructs a new instance of

InternalFrameMaximizeIcon

.

static

Icon

getInternalFrameMinimizeIcon

​(int size)

Constructs a new instance of

InternalFrameMinimizeIcon

.

static

Icon

getMenuArrowIcon

()

Returns an icon to be used by

JMenu

.

static

Icon

getMenuItemArrowIcon

()

Returns an icon to be used by

JMenuItem

.

static

Icon

getMenuItemCheckIcon

()

Returns an icon to be used by

JCheckBoxMenuItem

.

static

Icon

getRadioButtonIcon

()

Returns the instance of

RadioButtonIcon

.

static

Icon

getRadioButtonMenuItemIcon

()

Returns an icon to be used by

JRadioButtonMenuItem

.

static

Icon

getTreeComputerIcon

()

Returns the instance of

TreeComputerIcon

.

static

Icon

getTreeControlIcon

​(boolean isCollapsed)

Constructs a new instance of

TreeControlIcon

.

static

Icon

getTreeFloppyDriveIcon

()

Returns the instance of

TreeFloppyDriveIcon

.

static

Icon

getTreeFolderIcon

()

Constructs a new instance of

TreeFolderIcon

.

static

Icon

getTreeHardDriveIcon

()

Returns the instance of

TreeHardDriveIcon

.

static

Icon

getTreeLeafIcon

()

Constructs a new instance of

TreeLeafIcon

.

static

Icon

getVerticalSliderThumbIcon

()

Returns a thumb icon to be used by vertical slider.

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

static class

MetalIconFactory.FileIcon16

Warning:

Serialized objects of this class will not be compatible with
future Swing releases.

static class

MetalIconFactory.FolderIcon16

Warning:

Serialized objects of this class will not be compatible with
future Swing releases.

static class

MetalIconFactory.PaletteCloseIcon

Defines an icon for Palette close

static class

MetalIconFactory.TreeControlIcon

Warning:

Serialized objects of this class will not be compatible with
future Swing releases.

static class

MetalIconFactory.TreeFolderIcon

Warning:

Serialized objects of this class will not be compatible with
future Swing releases.

static class

MetalIconFactory.TreeLeafIcon

The class represents a tree leaf icon.

---

#### Nested Class Summary

Warning:

Serialized objects of this class will not be compatible with
future Swing releases.

Defines an icon for Palette close

The class represents a tree leaf icon.

Field Summary

Fields

Modifier and Type

Field

Description

static boolean

DARK

DARK

is used for the property

Tree.expandedIcon

.

static boolean

LIGHT

LIGHT

is used for the property

Tree.collapsedIcon

.

---

#### Field Summary

DARK

is used for the property

Tree.expandedIcon

.

LIGHT

is used for the property

Tree.collapsedIcon

.

Constructor Summary

Constructors

Constructor

Description

MetalIconFactory

()

---

#### Constructor Summary

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

Icon

getCheckBoxIcon

()

Returns a checkbox icon.

static

Icon

getCheckBoxMenuItemIcon

()

Returns an icon to be used by

JCheckBoxMenuItem

.

static

Icon

getFileChooserDetailViewIcon

()

Returns the instance of

FileChooserDetailViewIcon

.

static

Icon

getFileChooserHomeFolderIcon

()

Returns the instance of

FileChooserHomeFolderIcon

.

static

Icon

getFileChooserListViewIcon

()

Returns the instance of

FileChooserListViewIcon

.

static

Icon

getFileChooserNewFolderIcon

()

Returns the instance of

FileChooserNewFolderIcon

.

static

Icon

getFileChooserUpFolderIcon

()

Returns the instance of

FileChooserUpFolderIcon

.

static

Icon

getHorizontalSliderThumbIcon

()

Returns a thumb icon to be used by horizontal slider.

static

Icon

getInternalFrameAltMaximizeIcon

​(int size)

Constructs a new instance of

InternalFrameAltMaximizeIcon

.

static

Icon

getInternalFrameCloseIcon

​(int size)

Constructs a new instance of

InternalFrameCloseIcon

.

static

Icon

getInternalFrameDefaultMenuIcon

()

Returns the instance of

InternalFrameDefaultMenuIcon

.

static

Icon

getInternalFrameMaximizeIcon

​(int size)

Constructs a new instance of

InternalFrameMaximizeIcon

.

static

Icon

getInternalFrameMinimizeIcon

​(int size)

Constructs a new instance of

InternalFrameMinimizeIcon

.

static

Icon

getMenuArrowIcon

()

Returns an icon to be used by

JMenu

.

static

Icon

getMenuItemArrowIcon

()

Returns an icon to be used by

JMenuItem

.

static

Icon

getMenuItemCheckIcon

()

Returns an icon to be used by

JCheckBoxMenuItem

.

static

Icon

getRadioButtonIcon

()

Returns the instance of

RadioButtonIcon

.

static

Icon

getRadioButtonMenuItemIcon

()

Returns an icon to be used by

JRadioButtonMenuItem

.

static

Icon

getTreeComputerIcon

()

Returns the instance of

TreeComputerIcon

.

static

Icon

getTreeControlIcon

​(boolean isCollapsed)

Constructs a new instance of

TreeControlIcon

.

static

Icon

getTreeFloppyDriveIcon

()

Returns the instance of

TreeFloppyDriveIcon

.

static

Icon

getTreeFolderIcon

()

Constructs a new instance of

TreeFolderIcon

.

static

Icon

getTreeHardDriveIcon

()

Returns the instance of

TreeHardDriveIcon

.

static

Icon

getTreeLeafIcon

()

Constructs a new instance of

TreeLeafIcon

.

static

Icon

getVerticalSliderThumbIcon

()

Returns a thumb icon to be used by vertical slider.

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

Returns a checkbox icon.

Returns an icon to be used by

JCheckBoxMenuItem

.

Returns the instance of

FileChooserDetailViewIcon

.

Returns the instance of

FileChooserHomeFolderIcon

.

Returns the instance of

FileChooserListViewIcon

.

Returns the instance of

FileChooserNewFolderIcon

.

Returns the instance of

FileChooserUpFolderIcon

.

Returns a thumb icon to be used by horizontal slider.

Constructs a new instance of

InternalFrameAltMaximizeIcon

.

Constructs a new instance of

InternalFrameCloseIcon

.

Returns the instance of

InternalFrameDefaultMenuIcon

.

Constructs a new instance of

InternalFrameMaximizeIcon

.

Constructs a new instance of

InternalFrameMinimizeIcon

.

Returns an icon to be used by

JMenu

.

Returns an icon to be used by

JMenuItem

.

Returns the instance of

RadioButtonIcon

.

Returns an icon to be used by

JRadioButtonMenuItem

.

Returns the instance of

TreeComputerIcon

.

Constructs a new instance of

TreeControlIcon

.

Returns the instance of

TreeFloppyDriveIcon

.

Constructs a new instance of

TreeFolderIcon

.

Returns the instance of

TreeHardDriveIcon

.

Constructs a new instance of

TreeLeafIcon

.

Returns a thumb icon to be used by vertical slider.

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

- DARK

```java
public static final boolean DARK
```

DARK

is used for the property

Tree.expandedIcon

.

**See Also:** Constant Field Values

- LIGHT

```java
public static final boolean LIGHT
```

LIGHT

is used for the property

Tree.collapsedIcon

.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- MetalIconFactory

```java
public MetalIconFactory()
```

============ METHOD DETAIL ==========

- Method Detail

- getFileChooserDetailViewIcon

```java
public static
Icon
getFileChooserDetailViewIcon()
```

Returns the instance of

FileChooserDetailViewIcon

.

**Returns:** the instance of

FileChooserDetailViewIcon

- getFileChooserHomeFolderIcon

```java
public static
Icon
getFileChooserHomeFolderIcon()
```

Returns the instance of

FileChooserHomeFolderIcon

.

**Returns:** the instance of

FileChooserHomeFolderIcon

- getFileChooserListViewIcon

```java
public static
Icon
getFileChooserListViewIcon()
```

Returns the instance of

FileChooserListViewIcon

.

**Returns:** the instance of

FileChooserListViewIcon

- getFileChooserNewFolderIcon

```java
public static
Icon
getFileChooserNewFolderIcon()
```

Returns the instance of

FileChooserNewFolderIcon

.

**Returns:** the instance of

FileChooserNewFolderIcon

- getFileChooserUpFolderIcon

```java
public static
Icon
getFileChooserUpFolderIcon()
```

Returns the instance of

FileChooserUpFolderIcon

.

**Returns:** the instance of

FileChooserUpFolderIcon

- getInternalFrameAltMaximizeIcon

```java
public static
Icon
getInternalFrameAltMaximizeIcon​(int size)
```

Constructs a new instance of

InternalFrameAltMaximizeIcon

.

**Parameters:** size

- the size of the icon
**Returns:** a new instance of

InternalFrameAltMaximizeIcon

- getInternalFrameCloseIcon

```java
public static
Icon
getInternalFrameCloseIcon​(int size)
```

Constructs a new instance of

InternalFrameCloseIcon

.

**Parameters:** size

- the size of the icon
**Returns:** a new instance of

InternalFrameCloseIcon

- getInternalFrameDefaultMenuIcon

```java
public static
Icon
getInternalFrameDefaultMenuIcon()
```

Returns the instance of

InternalFrameDefaultMenuIcon

.

**Returns:** the instance of

InternalFrameDefaultMenuIcon

- getInternalFrameMaximizeIcon

```java
public static
Icon
getInternalFrameMaximizeIcon​(int size)
```

Constructs a new instance of

InternalFrameMaximizeIcon

.

**Parameters:** size

- the size of the icon
**Returns:** a new instance of

InternalFrameMaximizeIcon

- getInternalFrameMinimizeIcon

```java
public static
Icon
getInternalFrameMinimizeIcon​(int size)
```

Constructs a new instance of

InternalFrameMinimizeIcon

.

**Parameters:** size

- the size of the icon
**Returns:** a new instance of

InternalFrameMinimizeIcon

- getRadioButtonIcon

```java
public static
Icon
getRadioButtonIcon()
```

Returns the instance of

RadioButtonIcon

.

**Returns:** the instance of

RadioButtonIcon

- getCheckBoxIcon

```java
public static
Icon
getCheckBoxIcon()
```

Returns a checkbox icon.

**Returns:** a checkbox icon
**Since:** 1.3

- getTreeComputerIcon

```java
public static
Icon
getTreeComputerIcon()
```

Returns the instance of

TreeComputerIcon

.

**Returns:** the instance of

TreeComputerIcon

- getTreeFloppyDriveIcon

```java
public static
Icon
getTreeFloppyDriveIcon()
```

Returns the instance of

TreeFloppyDriveIcon

.

**Returns:** the instance of

TreeFloppyDriveIcon

- getTreeFolderIcon

```java
public static
Icon
getTreeFolderIcon()
```

Constructs a new instance of

TreeFolderIcon

.

**Returns:** a new instance of

TreeFolderIcon

- getTreeHardDriveIcon

```java
public static
Icon
getTreeHardDriveIcon()
```

Returns the instance of

TreeHardDriveIcon

.

**Returns:** the instance of

TreeHardDriveIcon

- getTreeLeafIcon

```java
public static
Icon
getTreeLeafIcon()
```

Constructs a new instance of

TreeLeafIcon

.

**Returns:** a new instance of

TreeLeafIcon

- getTreeControlIcon

```java
public static
Icon
getTreeControlIcon​(boolean isCollapsed)
```

Constructs a new instance of

TreeControlIcon

.

**Parameters:** isCollapsed

- if

true

the icon is collapsed
**Returns:** a new instance of

TreeControlIcon

- getMenuArrowIcon

```java
public static
Icon
getMenuArrowIcon()
```

Returns an icon to be used by

JMenu

.

**Returns:** an icon to be used by

JMenu

- getMenuItemCheckIcon

```java
public static
Icon
getMenuItemCheckIcon()
```

Returns an icon to be used by

JCheckBoxMenuItem

.

**Returns:** the default icon for check box menu items,
or

null

if no default exists

- getMenuItemArrowIcon

```java
public static
Icon
getMenuItemArrowIcon()
```

Returns an icon to be used by

JMenuItem

.

**Returns:** an icon to be used by

JMenuItem

- getCheckBoxMenuItemIcon

```java
public static
Icon
getCheckBoxMenuItemIcon()
```

Returns an icon to be used by

JCheckBoxMenuItem

.

**Returns:** an icon to be used by

JCheckBoxMenuItem

- getRadioButtonMenuItemIcon

```java
public static
Icon
getRadioButtonMenuItemIcon()
```

Returns an icon to be used by

JRadioButtonMenuItem

.

**Returns:** an icon to be used by

JRadioButtonMenuItem

- getHorizontalSliderThumbIcon

```java
public static
Icon
getHorizontalSliderThumbIcon()
```

Returns a thumb icon to be used by horizontal slider.

**Returns:** a thumb icon to be used by horizontal slider

- getVerticalSliderThumbIcon

```java
public static
Icon
getVerticalSliderThumbIcon()
```

Returns a thumb icon to be used by vertical slider.

**Returns:** a thumb icon to be used by vertical slider

Field Detail

- DARK

```java
public static final boolean DARK
```

DARK

is used for the property

Tree.expandedIcon

.

**See Also:** Constant Field Values

- LIGHT

```java
public static final boolean LIGHT
```

LIGHT

is used for the property

Tree.collapsedIcon

.

**See Also:** Constant Field Values

---

#### Field Detail

DARK

```java
public static final boolean DARK
```

DARK

is used for the property

Tree.expandedIcon

.

**See Also:** Constant Field Values

---

#### DARK

public static final boolean DARK

DARK

is used for the property

Tree.expandedIcon

.

LIGHT

```java
public static final boolean LIGHT
```

LIGHT

is used for the property

Tree.collapsedIcon

.

**See Also:** Constant Field Values

---

#### LIGHT

public static final boolean LIGHT

LIGHT

is used for the property

Tree.collapsedIcon

.

Constructor Detail

- MetalIconFactory

```java
public MetalIconFactory()
```

---

#### Constructor Detail

MetalIconFactory

```java
public MetalIconFactory()
```

---

#### MetalIconFactory

public MetalIconFactory()

Method Detail

- getFileChooserDetailViewIcon

```java
public static
Icon
getFileChooserDetailViewIcon()
```

Returns the instance of

FileChooserDetailViewIcon

.

**Returns:** the instance of

FileChooserDetailViewIcon

- getFileChooserHomeFolderIcon

```java
public static
Icon
getFileChooserHomeFolderIcon()
```

Returns the instance of

FileChooserHomeFolderIcon

.

**Returns:** the instance of

FileChooserHomeFolderIcon

- getFileChooserListViewIcon

```java
public static
Icon
getFileChooserListViewIcon()
```

Returns the instance of

FileChooserListViewIcon

.

**Returns:** the instance of

FileChooserListViewIcon

- getFileChooserNewFolderIcon

```java
public static
Icon
getFileChooserNewFolderIcon()
```

Returns the instance of

FileChooserNewFolderIcon

.

**Returns:** the instance of

FileChooserNewFolderIcon

- getFileChooserUpFolderIcon

```java
public static
Icon
getFileChooserUpFolderIcon()
```

Returns the instance of

FileChooserUpFolderIcon

.

**Returns:** the instance of

FileChooserUpFolderIcon

- getInternalFrameAltMaximizeIcon

```java
public static
Icon
getInternalFrameAltMaximizeIcon​(int size)
```

Constructs a new instance of

InternalFrameAltMaximizeIcon

.

**Parameters:** size

- the size of the icon
**Returns:** a new instance of

InternalFrameAltMaximizeIcon

- getInternalFrameCloseIcon

```java
public static
Icon
getInternalFrameCloseIcon​(int size)
```

Constructs a new instance of

InternalFrameCloseIcon

.

**Parameters:** size

- the size of the icon
**Returns:** a new instance of

InternalFrameCloseIcon

- getInternalFrameDefaultMenuIcon

```java
public static
Icon
getInternalFrameDefaultMenuIcon()
```

Returns the instance of

InternalFrameDefaultMenuIcon

.

**Returns:** the instance of

InternalFrameDefaultMenuIcon

- getInternalFrameMaximizeIcon

```java
public static
Icon
getInternalFrameMaximizeIcon​(int size)
```

Constructs a new instance of

InternalFrameMaximizeIcon

.

**Parameters:** size

- the size of the icon
**Returns:** a new instance of

InternalFrameMaximizeIcon

- getInternalFrameMinimizeIcon

```java
public static
Icon
getInternalFrameMinimizeIcon​(int size)
```

Constructs a new instance of

InternalFrameMinimizeIcon

.

**Parameters:** size

- the size of the icon
**Returns:** a new instance of

InternalFrameMinimizeIcon

- getRadioButtonIcon

```java
public static
Icon
getRadioButtonIcon()
```

Returns the instance of

RadioButtonIcon

.

**Returns:** the instance of

RadioButtonIcon

- getCheckBoxIcon

```java
public static
Icon
getCheckBoxIcon()
```

Returns a checkbox icon.

**Returns:** a checkbox icon
**Since:** 1.3

- getTreeComputerIcon

```java
public static
Icon
getTreeComputerIcon()
```

Returns the instance of

TreeComputerIcon

.

**Returns:** the instance of

TreeComputerIcon

- getTreeFloppyDriveIcon

```java
public static
Icon
getTreeFloppyDriveIcon()
```

Returns the instance of

TreeFloppyDriveIcon

.

**Returns:** the instance of

TreeFloppyDriveIcon

- getTreeFolderIcon

```java
public static
Icon
getTreeFolderIcon()
```

Constructs a new instance of

TreeFolderIcon

.

**Returns:** a new instance of

TreeFolderIcon

- getTreeHardDriveIcon

```java
public static
Icon
getTreeHardDriveIcon()
```

Returns the instance of

TreeHardDriveIcon

.

**Returns:** the instance of

TreeHardDriveIcon

- getTreeLeafIcon

```java
public static
Icon
getTreeLeafIcon()
```

Constructs a new instance of

TreeLeafIcon

.

**Returns:** a new instance of

TreeLeafIcon

- getTreeControlIcon

```java
public static
Icon
getTreeControlIcon​(boolean isCollapsed)
```

Constructs a new instance of

TreeControlIcon

.

**Parameters:** isCollapsed

- if

true

the icon is collapsed
**Returns:** a new instance of

TreeControlIcon

- getMenuArrowIcon

```java
public static
Icon
getMenuArrowIcon()
```

Returns an icon to be used by

JMenu

.

**Returns:** an icon to be used by

JMenu

- getMenuItemCheckIcon

```java
public static
Icon
getMenuItemCheckIcon()
```

Returns an icon to be used by

JCheckBoxMenuItem

.

**Returns:** the default icon for check box menu items,
or

null

if no default exists

- getMenuItemArrowIcon

```java
public static
Icon
getMenuItemArrowIcon()
```

Returns an icon to be used by

JMenuItem

.

**Returns:** an icon to be used by

JMenuItem

- getCheckBoxMenuItemIcon

```java
public static
Icon
getCheckBoxMenuItemIcon()
```

Returns an icon to be used by

JCheckBoxMenuItem

.

**Returns:** an icon to be used by

JCheckBoxMenuItem

- getRadioButtonMenuItemIcon

```java
public static
Icon
getRadioButtonMenuItemIcon()
```

Returns an icon to be used by

JRadioButtonMenuItem

.

**Returns:** an icon to be used by

JRadioButtonMenuItem

- getHorizontalSliderThumbIcon

```java
public static
Icon
getHorizontalSliderThumbIcon()
```

Returns a thumb icon to be used by horizontal slider.

**Returns:** a thumb icon to be used by horizontal slider

- getVerticalSliderThumbIcon

```java
public static
Icon
getVerticalSliderThumbIcon()
```

Returns a thumb icon to be used by vertical slider.

**Returns:** a thumb icon to be used by vertical slider

---

#### Method Detail

getFileChooserDetailViewIcon

```java
public static
Icon
getFileChooserDetailViewIcon()
```

Returns the instance of

FileChooserDetailViewIcon

.

**Returns:** the instance of

FileChooserDetailViewIcon

---

#### getFileChooserDetailViewIcon

public static

Icon

getFileChooserDetailViewIcon()

Returns the instance of

FileChooserDetailViewIcon

.

getFileChooserHomeFolderIcon

```java
public static
Icon
getFileChooserHomeFolderIcon()
```

Returns the instance of

FileChooserHomeFolderIcon

.

**Returns:** the instance of

FileChooserHomeFolderIcon

---

#### getFileChooserHomeFolderIcon

public static

Icon

getFileChooserHomeFolderIcon()

Returns the instance of

FileChooserHomeFolderIcon

.

getFileChooserListViewIcon

```java
public static
Icon
getFileChooserListViewIcon()
```

Returns the instance of

FileChooserListViewIcon

.

**Returns:** the instance of

FileChooserListViewIcon

---

#### getFileChooserListViewIcon

public static

Icon

getFileChooserListViewIcon()

Returns the instance of

FileChooserListViewIcon

.

getFileChooserNewFolderIcon

```java
public static
Icon
getFileChooserNewFolderIcon()
```

Returns the instance of

FileChooserNewFolderIcon

.

**Returns:** the instance of

FileChooserNewFolderIcon

---

#### getFileChooserNewFolderIcon

public static

Icon

getFileChooserNewFolderIcon()

Returns the instance of

FileChooserNewFolderIcon

.

getFileChooserUpFolderIcon

```java
public static
Icon
getFileChooserUpFolderIcon()
```

Returns the instance of

FileChooserUpFolderIcon

.

**Returns:** the instance of

FileChooserUpFolderIcon

---

#### getFileChooserUpFolderIcon

public static

Icon

getFileChooserUpFolderIcon()

Returns the instance of

FileChooserUpFolderIcon

.

getInternalFrameAltMaximizeIcon

```java
public static
Icon
getInternalFrameAltMaximizeIcon​(int size)
```

Constructs a new instance of

InternalFrameAltMaximizeIcon

.

**Parameters:** size

- the size of the icon
**Returns:** a new instance of

InternalFrameAltMaximizeIcon

---

#### getInternalFrameAltMaximizeIcon

public static

Icon

getInternalFrameAltMaximizeIcon​(int size)

Constructs a new instance of

InternalFrameAltMaximizeIcon

.

getInternalFrameCloseIcon

```java
public static
Icon
getInternalFrameCloseIcon​(int size)
```

Constructs a new instance of

InternalFrameCloseIcon

.

**Parameters:** size

- the size of the icon
**Returns:** a new instance of

InternalFrameCloseIcon

---

#### getInternalFrameCloseIcon

public static

Icon

getInternalFrameCloseIcon​(int size)

Constructs a new instance of

InternalFrameCloseIcon

.

getInternalFrameDefaultMenuIcon

```java
public static
Icon
getInternalFrameDefaultMenuIcon()
```

Returns the instance of

InternalFrameDefaultMenuIcon

.

**Returns:** the instance of

InternalFrameDefaultMenuIcon

---

#### getInternalFrameDefaultMenuIcon

public static

Icon

getInternalFrameDefaultMenuIcon()

Returns the instance of

InternalFrameDefaultMenuIcon

.

getInternalFrameMaximizeIcon

```java
public static
Icon
getInternalFrameMaximizeIcon​(int size)
```

Constructs a new instance of

InternalFrameMaximizeIcon

.

**Parameters:** size

- the size of the icon
**Returns:** a new instance of

InternalFrameMaximizeIcon

---

#### getInternalFrameMaximizeIcon

public static

Icon

getInternalFrameMaximizeIcon​(int size)

Constructs a new instance of

InternalFrameMaximizeIcon

.

getInternalFrameMinimizeIcon

```java
public static
Icon
getInternalFrameMinimizeIcon​(int size)
```

Constructs a new instance of

InternalFrameMinimizeIcon

.

**Parameters:** size

- the size of the icon
**Returns:** a new instance of

InternalFrameMinimizeIcon

---

#### getInternalFrameMinimizeIcon

public static

Icon

getInternalFrameMinimizeIcon​(int size)

Constructs a new instance of

InternalFrameMinimizeIcon

.

getRadioButtonIcon

```java
public static
Icon
getRadioButtonIcon()
```

Returns the instance of

RadioButtonIcon

.

**Returns:** the instance of

RadioButtonIcon

---

#### getRadioButtonIcon

public static

Icon

getRadioButtonIcon()

Returns the instance of

RadioButtonIcon

.

getCheckBoxIcon

```java
public static
Icon
getCheckBoxIcon()
```

Returns a checkbox icon.

**Returns:** a checkbox icon
**Since:** 1.3

---

#### getCheckBoxIcon

public static

Icon

getCheckBoxIcon()

Returns a checkbox icon.

getTreeComputerIcon

```java
public static
Icon
getTreeComputerIcon()
```

Returns the instance of

TreeComputerIcon

.

**Returns:** the instance of

TreeComputerIcon

---

#### getTreeComputerIcon

public static

Icon

getTreeComputerIcon()

Returns the instance of

TreeComputerIcon

.

getTreeFloppyDriveIcon

```java
public static
Icon
getTreeFloppyDriveIcon()
```

Returns the instance of

TreeFloppyDriveIcon

.

**Returns:** the instance of

TreeFloppyDriveIcon

---

#### getTreeFloppyDriveIcon

public static

Icon

getTreeFloppyDriveIcon()

Returns the instance of

TreeFloppyDriveIcon

.

getTreeFolderIcon

```java
public static
Icon
getTreeFolderIcon()
```

Constructs a new instance of

TreeFolderIcon

.

**Returns:** a new instance of

TreeFolderIcon

---

#### getTreeFolderIcon

public static

Icon

getTreeFolderIcon()

Constructs a new instance of

TreeFolderIcon

.

getTreeHardDriveIcon

```java
public static
Icon
getTreeHardDriveIcon()
```

Returns the instance of

TreeHardDriveIcon

.

**Returns:** the instance of

TreeHardDriveIcon

---

#### getTreeHardDriveIcon

public static

Icon

getTreeHardDriveIcon()

Returns the instance of

TreeHardDriveIcon

.

getTreeLeafIcon

```java
public static
Icon
getTreeLeafIcon()
```

Constructs a new instance of

TreeLeafIcon

.

**Returns:** a new instance of

TreeLeafIcon

---

#### getTreeLeafIcon

public static

Icon

getTreeLeafIcon()

Constructs a new instance of

TreeLeafIcon

.

getTreeControlIcon

```java
public static
Icon
getTreeControlIcon​(boolean isCollapsed)
```

Constructs a new instance of

TreeControlIcon

.

**Parameters:** isCollapsed

- if

true

the icon is collapsed
**Returns:** a new instance of

TreeControlIcon

---

#### getTreeControlIcon

public static

Icon

getTreeControlIcon​(boolean isCollapsed)

Constructs a new instance of

TreeControlIcon

.

getMenuArrowIcon

```java
public static
Icon
getMenuArrowIcon()
```

Returns an icon to be used by

JMenu

.

**Returns:** an icon to be used by

JMenu

---

#### getMenuArrowIcon

public static

Icon

getMenuArrowIcon()

Returns an icon to be used by

JMenu

.

getMenuItemCheckIcon

```java
public static
Icon
getMenuItemCheckIcon()
```

Returns an icon to be used by

JCheckBoxMenuItem

.

**Returns:** the default icon for check box menu items,
or

null

if no default exists

---

#### getMenuItemCheckIcon

public static

Icon

getMenuItemCheckIcon()

Returns an icon to be used by

JCheckBoxMenuItem

.

getMenuItemArrowIcon

```java
public static
Icon
getMenuItemArrowIcon()
```

Returns an icon to be used by

JMenuItem

.

**Returns:** an icon to be used by

JMenuItem

---

#### getMenuItemArrowIcon

public static

Icon

getMenuItemArrowIcon()

Returns an icon to be used by

JMenuItem

.

getCheckBoxMenuItemIcon

```java
public static
Icon
getCheckBoxMenuItemIcon()
```

Returns an icon to be used by

JCheckBoxMenuItem

.

**Returns:** an icon to be used by

JCheckBoxMenuItem

---

#### getCheckBoxMenuItemIcon

public static

Icon

getCheckBoxMenuItemIcon()

Returns an icon to be used by

JCheckBoxMenuItem

.

getRadioButtonMenuItemIcon

```java
public static
Icon
getRadioButtonMenuItemIcon()
```

Returns an icon to be used by

JRadioButtonMenuItem

.

**Returns:** an icon to be used by

JRadioButtonMenuItem

---

#### getRadioButtonMenuItemIcon

public static

Icon

getRadioButtonMenuItemIcon()

Returns an icon to be used by

JRadioButtonMenuItem

.

getHorizontalSliderThumbIcon

```java
public static
Icon
getHorizontalSliderThumbIcon()
```

Returns a thumb icon to be used by horizontal slider.

**Returns:** a thumb icon to be used by horizontal slider

---

#### getHorizontalSliderThumbIcon

public static

Icon

getHorizontalSliderThumbIcon()

Returns a thumb icon to be used by horizontal slider.

getVerticalSliderThumbIcon

```java
public static
Icon
getVerticalSliderThumbIcon()
```

Returns a thumb icon to be used by vertical slider.

**Returns:** a thumb icon to be used by vertical slider

---

#### getVerticalSliderThumbIcon

public static

Icon

getVerticalSliderThumbIcon()

Returns a thumb icon to be used by vertical slider.

---

