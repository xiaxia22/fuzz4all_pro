# Class Region

**Source:** `java.desktop\javax\swing\plaf\synth\Region.html`

### Class Description

```java
public class
Region

extends
Object
```

A distinct rendering area of a Swing component. A component may
support one or more regions. Specific component regions are defined
by the typesafe enumeration in this class.

Regions are typically used as a way to identify the

Component

s
and areas a particular style is to apply to. Synth's file format allows you
to bind styles based on the name of a

Region

.
The name is derived from the field name of the constant:

- Map all characters to lowercase.

Map the first character to uppercase.

Map the first character after underscores to uppercase.

Remove all underscores.

For example, to identify the

SPLIT_PANE

Region

you would use

SplitPane

.
The following shows a custom

SynthStyleFactory

that returns a specific style for split panes:

```java
public SynthStyle getStyle(JComponent c, Region id) {
if (id == Region.SPLIT_PANE) {
return splitPaneStyle;
}
...
}
```

The following

xml

accomplishes the same thing:

```java
<style id="splitPaneStyle">
...
</style>
<bind style="splitPaneStyle" type="region" key="SplitPane"/>
```

**Since:** 1.5

---

### Field Details

#### public static final
Region
ARROW_BUTTON

ArrowButton's are special types of buttons that also render a
directional indicator, typically an arrow. ArrowButtons are used by
composite components, for example ScrollBar's contain ArrowButtons.
To bind a style to this

Region

use the name

ArrowButton

.

---

#### public static final
Region
BUTTON

Button region. To bind a style to this

Region

use the name

Button

.

---

#### public static final
Region
CHECK_BOX

CheckBox region. To bind a style to this

Region

use the name

CheckBox

.

---

#### public static final
Region
CHECK_BOX_MENU_ITEM

CheckBoxMenuItem region. To bind a style to this

Region

use
the name

CheckBoxMenuItem

.

---

#### public static final
Region
COLOR_CHOOSER

ColorChooser region. To bind a style to this

Region

use
the name

ColorChooser

.

---

#### public static final
Region
COMBO_BOX

ComboBox region. To bind a style to this

Region

use
the name

ComboBox

.

---

#### public static final
Region
DESKTOP_PANE

DesktopPane region. To bind a style to this

Region

use
the name

DesktopPane

.

---

#### public static final
Region
DESKTOP_ICON

DesktopIcon region. To bind a style to this

Region

use
the name

DesktopIcon

.

---

#### public static final
Region
EDITOR_PANE

EditorPane region. To bind a style to this

Region

use
the name

EditorPane

.

---

#### public static final
Region
FILE_CHOOSER

FileChooser region. To bind a style to this

Region

use
the name

FileChooser

.

---

#### public static final
Region
FORMATTED_TEXT_FIELD

FormattedTextField region. To bind a style to this

Region

use
the name

FormattedTextField

.

---

#### public static final
Region
INTERNAL_FRAME

InternalFrame region. To bind a style to this

Region

use
the name

InternalFrame

.

---

#### public static final
Region
INTERNAL_FRAME_TITLE_PANE

TitlePane of an InternalFrame. The TitlePane typically
shows a menu, title, widgets to manipulate the internal frame.
To bind a style to this

Region

use the name

InternalFrameTitlePane

.

---

#### public static final
Region
LABEL

Label region. To bind a style to this

Region

use the name

Label

.

---

#### public static final
Region
LIST

List region. To bind a style to this

Region

use the name

List

.

---

#### public static final
Region
MENU

Menu region. To bind a style to this

Region

use the name

Menu

.

---

#### public static final
Region
MENU_BAR

MenuBar region. To bind a style to this

Region

use the name

MenuBar

.

---

#### public static final
Region
MENU_ITEM

MenuItem region. To bind a style to this

Region

use the name

MenuItem

.

---

#### public static final
Region
MENU_ITEM_ACCELERATOR

Accelerator region of a MenuItem. To bind a style to this

Region

use the name

MenuItemAccelerator

.

---

#### public static final
Region
OPTION_PANE

OptionPane region. To bind a style to this

Region

use
the name

OptionPane

.

---

#### public static final
Region
PANEL

Panel region. To bind a style to this

Region

use the name

Panel

.

---

#### public static final
Region
PASSWORD_FIELD

PasswordField region. To bind a style to this

Region

use
the name

PasswordField

.

---

#### public static final
Region
POPUP_MENU

PopupMenu region. To bind a style to this

Region

use
the name

PopupMenu

.

---

#### public static final
Region
POPUP_MENU_SEPARATOR

PopupMenuSeparator region. To bind a style to this

Region

use the name

PopupMenuSeparator

.

---

#### public static final
Region
PROGRESS_BAR

ProgressBar region. To bind a style to this

Region

use the name

ProgressBar

.

---

#### public static final
Region
RADIO_BUTTON

RadioButton region. To bind a style to this

Region

use the name

RadioButton

.

---

#### public static final
Region
RADIO_BUTTON_MENU_ITEM

RegionButtonMenuItem region. To bind a style to this

Region

use the name

RadioButtonMenuItem

.

---

#### public static final
Region
ROOT_PANE

RootPane region. To bind a style to this

Region

use
the name

RootPane

.

---

#### public static final
Region
SCROLL_BAR

ScrollBar region. To bind a style to this

Region

use
the name

ScrollBar

.

---

#### public static final
Region
SCROLL_BAR_TRACK

Track of the ScrollBar. To bind a style to this

Region

use
the name

ScrollBarTrack

.

---

#### public static final
Region
SCROLL_BAR_THUMB

Thumb of the ScrollBar. The thumb is the region of the ScrollBar
that gives a graphical depiction of what percentage of the View is
currently visible. To bind a style to this

Region

use
the name

ScrollBarThumb

.

---

#### public static final
Region
SCROLL_PANE

ScrollPane region. To bind a style to this

Region

use
the name

ScrollPane

.

---

#### public static final
Region
SEPARATOR

Separator region. To bind a style to this

Region

use
the name

Separator

.

---

#### public static final
Region
SLIDER

Slider region. To bind a style to this

Region

use
the name

Slider

.

---

#### public static final
Region
SLIDER_TRACK

Track of the Slider. To bind a style to this

Region

use
the name

SliderTrack

.

---

#### public static final
Region
SLIDER_THUMB

Thumb of the Slider. The thumb of the Slider identifies the current
value. To bind a style to this

Region

use the name

SliderThumb

.

---

#### public static final
Region
SPINNER

Spinner region. To bind a style to this

Region

use the name

Spinner

.

---

#### public static final
Region
SPLIT_PANE

SplitPane region. To bind a style to this

Region

use the name

SplitPane

.

---

#### public static final
Region
SPLIT_PANE_DIVIDER

Divider of the SplitPane. To bind a style to this

Region

use the name

SplitPaneDivider

.

---

#### public static final
Region
TABBED_PANE

TabbedPane region. To bind a style to this

Region

use
the name

TabbedPane

.

---

#### public static final
Region
TABBED_PANE_TAB

Region of a TabbedPane for one tab. To bind a style to this

Region

use the name

TabbedPaneTab

.

---

#### public static final
Region
TABBED_PANE_TAB_AREA

Region of a TabbedPane containing the tabs. To bind a style to this

Region

use the name

TabbedPaneTabArea

.

---

#### public static final
Region
TABBED_PANE_CONTENT

Region of a TabbedPane containing the content. To bind a style to this

Region

use the name

TabbedPaneContent

.

---

#### public static final
Region
TABLE

Table region. To bind a style to this

Region

use
the name

Table

.

---

#### public static final
Region
TABLE_HEADER

TableHeader region. To bind a style to this

Region

use
the name

TableHeader

.

---

#### public static final
Region
TEXT_AREA

TextArea region. To bind a style to this

Region

use
the name

TextArea

.

---

#### public static final
Region
TEXT_FIELD

TextField region. To bind a style to this

Region

use
the name

TextField

.

---

#### public static final
Region
TEXT_PANE

TextPane region. To bind a style to this

Region

use
the name

TextPane

.

---

#### public static final
Region
TOGGLE_BUTTON

ToggleButton region. To bind a style to this

Region

use
the name

ToggleButton

.

---

#### public static final
Region
TOOL_BAR

ToolBar region. To bind a style to this

Region

use
the name

ToolBar

.

---

#### public static final
Region
TOOL_BAR_CONTENT

Region of the ToolBar containing the content. To bind a style to this

Region

use the name

ToolBarContent

.

---

#### public static final
Region
TOOL_BAR_DRAG_WINDOW

Region for the Window containing the ToolBar. To bind a style to this

Region

use the name

ToolBarDragWindow

.

---

#### public static final
Region
TOOL_TIP

ToolTip region. To bind a style to this

Region

use
the name

ToolTip

.

---

#### public static final
Region
TOOL_BAR_SEPARATOR

ToolBar separator region. To bind a style to this

Region

use
the name

ToolBarSeparator

.

---

#### public static final
Region
TREE

Tree region. To bind a style to this

Region

use the name

Tree

.

---

#### public static final
Region
TREE_CELL

Region of the Tree for one cell. To bind a style to this

Region

use the name

TreeCell

.

---

#### public static final
Region
VIEWPORT

Viewport region. To bind a style to this

Region

use
the name

Viewport

.

---

### Constructor Details

#### protected Region​(
String
name,

String
ui,
boolean subregion)

Creates a Region with the specified name. This should only be
used if you are creating your own

JComponent

subclass
with a custom

ComponentUI

class.

**Parameters:**
- name

- Name of the region
- ui

- String that will be returned from

component.getUIClassID

. This will be null
if this is a subregion.
- subregion

- Whether or not this is a subregion.

---

### Method Details

#### public boolean isSubregion()

Returns true if the Region is a subregion of a Component, otherwise
false. For example,

Region.BUTTON

corresponds do a

Component

so that

Region.BUTTON.isSubregion()

returns false.

**Returns:**
- true if the Region is a subregion of a Component.

---

#### public
String
getName()

Returns the name of the region.

**Returns:**
- name of the Region.

---

#### public
String
toString()

Returns the name of the Region.

**Overrides:**
- toString

in class

Object

**Returns:**
- name of the Region.

---

### Additional Sections

#### Class Region

java.lang.Object

- javax.swing.plaf.synth.Region

javax.swing.plaf.synth.Region

```java
public class
Region

extends
Object
```

A distinct rendering area of a Swing component. A component may
support one or more regions. Specific component regions are defined
by the typesafe enumeration in this class.

Regions are typically used as a way to identify the

Component

s
and areas a particular style is to apply to. Synth's file format allows you
to bind styles based on the name of a

Region

.
The name is derived from the field name of the constant:

- Map all characters to lowercase.

Map the first character to uppercase.

Map the first character after underscores to uppercase.

Remove all underscores.

For example, to identify the

SPLIT_PANE

Region

you would use

SplitPane

.
The following shows a custom

SynthStyleFactory

that returns a specific style for split panes:

```java
public SynthStyle getStyle(JComponent c, Region id) {
if (id == Region.SPLIT_PANE) {
return splitPaneStyle;
}
...
}
```

The following

xml

accomplishes the same thing:

```java
<style id="splitPaneStyle">
...
</style>
<bind style="splitPaneStyle" type="region" key="SplitPane"/>
```

**Since:** 1.5

public class

Region

extends

Object

A distinct rendering area of a Swing component. A component may
support one or more regions. Specific component regions are defined
by the typesafe enumeration in this class.

Regions are typically used as a way to identify the

Component

s
and areas a particular style is to apply to. Synth's file format allows you
to bind styles based on the name of a

Region

.
The name is derived from the field name of the constant:

- Map all characters to lowercase.

Map the first character to uppercase.

Map the first character after underscores to uppercase.

Remove all underscores.

For example, to identify the

SPLIT_PANE

Region

you would use

SplitPane

.
The following shows a custom

SynthStyleFactory

that returns a specific style for split panes:

```java
public SynthStyle getStyle(JComponent c, Region id) {
if (id == Region.SPLIT_PANE) {
return splitPaneStyle;
}
...
}
```

The following

xml

accomplishes the same thing:

```java
<style id="splitPaneStyle">
...
</style>
<bind style="splitPaneStyle" type="region" key="SplitPane"/>
```

Regions are typically used as a way to identify the

Component

s
and areas a particular style is to apply to. Synth's file format allows you
to bind styles based on the name of a

Region

.
The name is derived from the field name of the constant:

- Map all characters to lowercase.

Map the first character to uppercase.

Map the first character after underscores to uppercase.

Remove all underscores.

For example, to identify the

SPLIT_PANE

Region

you would use

SplitPane

.
The following shows a custom

SynthStyleFactory

that returns a specific style for split panes:

```java
public SynthStyle getStyle(JComponent c, Region id) {
if (id == Region.SPLIT_PANE) {
return splitPaneStyle;
}
...
}
```

The following

xml

accomplishes the same thing:

```java
<style id="splitPaneStyle">
...
</style>
<bind style="splitPaneStyle" type="region" key="SplitPane"/>
```

Map all characters to lowercase.

Map the first character to uppercase.

Map the first character after underscores to uppercase.

Remove all underscores.

public SynthStyle getStyle(JComponent c, Region id) {
if (id == Region.SPLIT_PANE) {
return splitPaneStyle;
}
...
}

<style id="splitPaneStyle">
...
</style>
<bind style="splitPaneStyle" type="region" key="SplitPane"/>

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

Region

ARROW_BUTTON

ArrowButton's are special types of buttons that also render a
directional indicator, typically an arrow.

static

Region

BUTTON

Button region.

static

Region

CHECK_BOX

CheckBox region.

static

Region

CHECK_BOX_MENU_ITEM

CheckBoxMenuItem region.

static

Region

COLOR_CHOOSER

ColorChooser region.

static

Region

COMBO_BOX

ComboBox region.

static

Region

DESKTOP_ICON

DesktopIcon region.

static

Region

DESKTOP_PANE

DesktopPane region.

static

Region

EDITOR_PANE

EditorPane region.

static

Region

FILE_CHOOSER

FileChooser region.

static

Region

FORMATTED_TEXT_FIELD

FormattedTextField region.

static

Region

INTERNAL_FRAME

InternalFrame region.

static

Region

INTERNAL_FRAME_TITLE_PANE

TitlePane of an InternalFrame.

static

Region

LABEL

Label region.

static

Region

LIST

List region.

static

Region

MENU

Menu region.

static

Region

MENU_BAR

MenuBar region.

static

Region

MENU_ITEM

MenuItem region.

static

Region

MENU_ITEM_ACCELERATOR

Accelerator region of a MenuItem.

static

Region

OPTION_PANE

OptionPane region.

static

Region

PANEL

Panel region.

static

Region

PASSWORD_FIELD

PasswordField region.

static

Region

POPUP_MENU

PopupMenu region.

static

Region

POPUP_MENU_SEPARATOR

PopupMenuSeparator region.

static

Region

PROGRESS_BAR

ProgressBar region.

static

Region

RADIO_BUTTON

RadioButton region.

static

Region

RADIO_BUTTON_MENU_ITEM

RegionButtonMenuItem region.

static

Region

ROOT_PANE

RootPane region.

static

Region

SCROLL_BAR

ScrollBar region.

static

Region

SCROLL_BAR_THUMB

Thumb of the ScrollBar.

static

Region

SCROLL_BAR_TRACK

Track of the ScrollBar.

static

Region

SCROLL_PANE

ScrollPane region.

static

Region

SEPARATOR

Separator region.

static

Region

SLIDER

Slider region.

static

Region

SLIDER_THUMB

Thumb of the Slider.

static

Region

SLIDER_TRACK

Track of the Slider.

static

Region

SPINNER

Spinner region.

static

Region

SPLIT_PANE

SplitPane region.

static

Region

SPLIT_PANE_DIVIDER

Divider of the SplitPane.

static

Region

TABBED_PANE

TabbedPane region.

static

Region

TABBED_PANE_CONTENT

Region of a TabbedPane containing the content.

static

Region

TABBED_PANE_TAB

Region of a TabbedPane for one tab.

static

Region

TABBED_PANE_TAB_AREA

Region of a TabbedPane containing the tabs.

static

Region

TABLE

Table region.

static

Region

TABLE_HEADER

TableHeader region.

static

Region

TEXT_AREA

TextArea region.

static

Region

TEXT_FIELD

TextField region.

static

Region

TEXT_PANE

TextPane region.

static

Region

TOGGLE_BUTTON

ToggleButton region.

static

Region

TOOL_BAR

ToolBar region.

static

Region

TOOL_BAR_CONTENT

Region of the ToolBar containing the content.

static

Region

TOOL_BAR_DRAG_WINDOW

Region for the Window containing the ToolBar.

static

Region

TOOL_BAR_SEPARATOR

ToolBar separator region.

static

Region

TOOL_TIP

ToolTip region.

static

Region

TREE

Tree region.

static

Region

TREE_CELL

Region of the Tree for one cell.

static

Region

VIEWPORT

Viewport region.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Region

​(

String

name,

String

ui,
boolean subregion)

Creates a Region with the specified name.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getName

()

Returns the name of the region.

boolean

isSubregion

()

Returns true if the Region is a subregion of a Component, otherwise
false.

String

toString

()

Returns the name of the Region.

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

wait

,

wait

,

wait

Field Summary

Fields

Modifier and Type

Field

Description

static

Region

ARROW_BUTTON

ArrowButton's are special types of buttons that also render a
directional indicator, typically an arrow.

static

Region

BUTTON

Button region.

static

Region

CHECK_BOX

CheckBox region.

static

Region

CHECK_BOX_MENU_ITEM

CheckBoxMenuItem region.

static

Region

COLOR_CHOOSER

ColorChooser region.

static

Region

COMBO_BOX

ComboBox region.

static

Region

DESKTOP_ICON

DesktopIcon region.

static

Region

DESKTOP_PANE

DesktopPane region.

static

Region

EDITOR_PANE

EditorPane region.

static

Region

FILE_CHOOSER

FileChooser region.

static

Region

FORMATTED_TEXT_FIELD

FormattedTextField region.

static

Region

INTERNAL_FRAME

InternalFrame region.

static

Region

INTERNAL_FRAME_TITLE_PANE

TitlePane of an InternalFrame.

static

Region

LABEL

Label region.

static

Region

LIST

List region.

static

Region

MENU

Menu region.

static

Region

MENU_BAR

MenuBar region.

static

Region

MENU_ITEM

MenuItem region.

static

Region

MENU_ITEM_ACCELERATOR

Accelerator region of a MenuItem.

static

Region

OPTION_PANE

OptionPane region.

static

Region

PANEL

Panel region.

static

Region

PASSWORD_FIELD

PasswordField region.

static

Region

POPUP_MENU

PopupMenu region.

static

Region

POPUP_MENU_SEPARATOR

PopupMenuSeparator region.

static

Region

PROGRESS_BAR

ProgressBar region.

static

Region

RADIO_BUTTON

RadioButton region.

static

Region

RADIO_BUTTON_MENU_ITEM

RegionButtonMenuItem region.

static

Region

ROOT_PANE

RootPane region.

static

Region

SCROLL_BAR

ScrollBar region.

static

Region

SCROLL_BAR_THUMB

Thumb of the ScrollBar.

static

Region

SCROLL_BAR_TRACK

Track of the ScrollBar.

static

Region

SCROLL_PANE

ScrollPane region.

static

Region

SEPARATOR

Separator region.

static

Region

SLIDER

Slider region.

static

Region

SLIDER_THUMB

Thumb of the Slider.

static

Region

SLIDER_TRACK

Track of the Slider.

static

Region

SPINNER

Spinner region.

static

Region

SPLIT_PANE

SplitPane region.

static

Region

SPLIT_PANE_DIVIDER

Divider of the SplitPane.

static

Region

TABBED_PANE

TabbedPane region.

static

Region

TABBED_PANE_CONTENT

Region of a TabbedPane containing the content.

static

Region

TABBED_PANE_TAB

Region of a TabbedPane for one tab.

static

Region

TABBED_PANE_TAB_AREA

Region of a TabbedPane containing the tabs.

static

Region

TABLE

Table region.

static

Region

TABLE_HEADER

TableHeader region.

static

Region

TEXT_AREA

TextArea region.

static

Region

TEXT_FIELD

TextField region.

static

Region

TEXT_PANE

TextPane region.

static

Region

TOGGLE_BUTTON

ToggleButton region.

static

Region

TOOL_BAR

ToolBar region.

static

Region

TOOL_BAR_CONTENT

Region of the ToolBar containing the content.

static

Region

TOOL_BAR_DRAG_WINDOW

Region for the Window containing the ToolBar.

static

Region

TOOL_BAR_SEPARATOR

ToolBar separator region.

static

Region

TOOL_TIP

ToolTip region.

static

Region

TREE

Tree region.

static

Region

TREE_CELL

Region of the Tree for one cell.

static

Region

VIEWPORT

Viewport region.

---

#### Field Summary

ArrowButton's are special types of buttons that also render a
directional indicator, typically an arrow.

Button region.

CheckBox region.

CheckBoxMenuItem region.

ColorChooser region.

ComboBox region.

DesktopIcon region.

DesktopPane region.

EditorPane region.

FileChooser region.

FormattedTextField region.

InternalFrame region.

TitlePane of an InternalFrame.

Label region.

List region.

Menu region.

MenuBar region.

MenuItem region.

Accelerator region of a MenuItem.

OptionPane region.

Panel region.

PasswordField region.

PopupMenu region.

PopupMenuSeparator region.

ProgressBar region.

RadioButton region.

RegionButtonMenuItem region.

RootPane region.

ScrollBar region.

Thumb of the ScrollBar.

Track of the ScrollBar.

ScrollPane region.

Separator region.

Slider region.

Thumb of the Slider.

Track of the Slider.

Spinner region.

SplitPane region.

Divider of the SplitPane.

TabbedPane region.

Region of a TabbedPane containing the content.

Region of a TabbedPane for one tab.

Region of a TabbedPane containing the tabs.

Table region.

TableHeader region.

TextArea region.

TextField region.

TextPane region.

ToggleButton region.

ToolBar region.

Region of the ToolBar containing the content.

Region for the Window containing the ToolBar.

ToolBar separator region.

ToolTip region.

Tree region.

Region of the Tree for one cell.

Viewport region.

Constructor Summary

Constructors

Modifier

Constructor

Description

protected

Region

​(

String

name,

String

ui,
boolean subregion)

Creates a Region with the specified name.

---

#### Constructor Summary

Creates a Region with the specified name.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

getName

()

Returns the name of the region.

boolean

isSubregion

()

Returns true if the Region is a subregion of a Component, otherwise
false.

String

toString

()

Returns the name of the Region.

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

wait

,

wait

,

wait

---

#### Method Summary

Returns the name of the region.

Returns true if the Region is a subregion of a Component, otherwise
false.

Returns the name of the Region.

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

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

============ FIELD DETAIL ===========

- Field Detail

- ARROW_BUTTON

```java
public static final
Region
ARROW_BUTTON
```

ArrowButton's are special types of buttons that also render a
directional indicator, typically an arrow. ArrowButtons are used by
composite components, for example ScrollBar's contain ArrowButtons.
To bind a style to this

Region

use the name

ArrowButton

.

- BUTTON

```java
public static final
Region
BUTTON
```

Button region. To bind a style to this

Region

use the name

Button

.

- CHECK_BOX

```java
public static final
Region
CHECK_BOX
```

CheckBox region. To bind a style to this

Region

use the name

CheckBox

.

- CHECK_BOX_MENU_ITEM

```java
public static final
Region
CHECK_BOX_MENU_ITEM
```

CheckBoxMenuItem region. To bind a style to this

Region

use
the name

CheckBoxMenuItem

.

- COLOR_CHOOSER

```java
public static final
Region
COLOR_CHOOSER
```

ColorChooser region. To bind a style to this

Region

use
the name

ColorChooser

.

- COMBO_BOX

```java
public static final
Region
COMBO_BOX
```

ComboBox region. To bind a style to this

Region

use
the name

ComboBox

.

- DESKTOP_PANE

```java
public static final
Region
DESKTOP_PANE
```

DesktopPane region. To bind a style to this

Region

use
the name

DesktopPane

.

- DESKTOP_ICON

```java
public static final
Region
DESKTOP_ICON
```

DesktopIcon region. To bind a style to this

Region

use
the name

DesktopIcon

.

- EDITOR_PANE

```java
public static final
Region
EDITOR_PANE
```

EditorPane region. To bind a style to this

Region

use
the name

EditorPane

.

- FILE_CHOOSER

```java
public static final
Region
FILE_CHOOSER
```

FileChooser region. To bind a style to this

Region

use
the name

FileChooser

.

- FORMATTED_TEXT_FIELD

```java
public static final
Region
FORMATTED_TEXT_FIELD
```

FormattedTextField region. To bind a style to this

Region

use
the name

FormattedTextField

.

- INTERNAL_FRAME

```java
public static final
Region
INTERNAL_FRAME
```

InternalFrame region. To bind a style to this

Region

use
the name

InternalFrame

.

- INTERNAL_FRAME_TITLE_PANE

```java
public static final
Region
INTERNAL_FRAME_TITLE_PANE
```

TitlePane of an InternalFrame. The TitlePane typically
shows a menu, title, widgets to manipulate the internal frame.
To bind a style to this

Region

use the name

InternalFrameTitlePane

.

- LABEL

```java
public static final
Region
LABEL
```

Label region. To bind a style to this

Region

use the name

Label

.

- LIST

```java
public static final
Region
LIST
```

List region. To bind a style to this

Region

use the name

List

.

- MENU

```java
public static final
Region
MENU
```

Menu region. To bind a style to this

Region

use the name

Menu

.

- MENU_BAR

```java
public static final
Region
MENU_BAR
```

MenuBar region. To bind a style to this

Region

use the name

MenuBar

.

- MENU_ITEM

```java
public static final
Region
MENU_ITEM
```

MenuItem region. To bind a style to this

Region

use the name

MenuItem

.

- MENU_ITEM_ACCELERATOR

```java
public static final
Region
MENU_ITEM_ACCELERATOR
```

Accelerator region of a MenuItem. To bind a style to this

Region

use the name

MenuItemAccelerator

.

- OPTION_PANE

```java
public static final
Region
OPTION_PANE
```

OptionPane region. To bind a style to this

Region

use
the name

OptionPane

.

- PANEL

```java
public static final
Region
PANEL
```

Panel region. To bind a style to this

Region

use the name

Panel

.

- PASSWORD_FIELD

```java
public static final
Region
PASSWORD_FIELD
```

PasswordField region. To bind a style to this

Region

use
the name

PasswordField

.

- POPUP_MENU

```java
public static final
Region
POPUP_MENU
```

PopupMenu region. To bind a style to this

Region

use
the name

PopupMenu

.

- POPUP_MENU_SEPARATOR

```java
public static final
Region
POPUP_MENU_SEPARATOR
```

PopupMenuSeparator region. To bind a style to this

Region

use the name

PopupMenuSeparator

.

- PROGRESS_BAR

```java
public static final
Region
PROGRESS_BAR
```

ProgressBar region. To bind a style to this

Region

use the name

ProgressBar

.

- RADIO_BUTTON

```java
public static final
Region
RADIO_BUTTON
```

RadioButton region. To bind a style to this

Region

use the name

RadioButton

.

- RADIO_BUTTON_MENU_ITEM

```java
public static final
Region
RADIO_BUTTON_MENU_ITEM
```

RegionButtonMenuItem region. To bind a style to this

Region

use the name

RadioButtonMenuItem

.

- ROOT_PANE

```java
public static final
Region
ROOT_PANE
```

RootPane region. To bind a style to this

Region

use
the name

RootPane

.

- SCROLL_BAR

```java
public static final
Region
SCROLL_BAR
```

ScrollBar region. To bind a style to this

Region

use
the name

ScrollBar

.

- SCROLL_BAR_TRACK

```java
public static final
Region
SCROLL_BAR_TRACK
```

Track of the ScrollBar. To bind a style to this

Region

use
the name

ScrollBarTrack

.

- SCROLL_BAR_THUMB

```java
public static final
Region
SCROLL_BAR_THUMB
```

Thumb of the ScrollBar. The thumb is the region of the ScrollBar
that gives a graphical depiction of what percentage of the View is
currently visible. To bind a style to this

Region

use
the name

ScrollBarThumb

.

- SCROLL_PANE

```java
public static final
Region
SCROLL_PANE
```

ScrollPane region. To bind a style to this

Region

use
the name

ScrollPane

.

- SEPARATOR

```java
public static final
Region
SEPARATOR
```

Separator region. To bind a style to this

Region

use
the name

Separator

.

- SLIDER

```java
public static final
Region
SLIDER
```

Slider region. To bind a style to this

Region

use
the name

Slider

.

- SLIDER_TRACK

```java
public static final
Region
SLIDER_TRACK
```

Track of the Slider. To bind a style to this

Region

use
the name

SliderTrack

.

- SLIDER_THUMB

```java
public static final
Region
SLIDER_THUMB
```

Thumb of the Slider. The thumb of the Slider identifies the current
value. To bind a style to this

Region

use the name

SliderThumb

.

- SPINNER

```java
public static final
Region
SPINNER
```

Spinner region. To bind a style to this

Region

use the name

Spinner

.

- SPLIT_PANE

```java
public static final
Region
SPLIT_PANE
```

SplitPane region. To bind a style to this

Region

use the name

SplitPane

.

- SPLIT_PANE_DIVIDER

```java
public static final
Region
SPLIT_PANE_DIVIDER
```

Divider of the SplitPane. To bind a style to this

Region

use the name

SplitPaneDivider

.

- TABBED_PANE

```java
public static final
Region
TABBED_PANE
```

TabbedPane region. To bind a style to this

Region

use
the name

TabbedPane

.

- TABBED_PANE_TAB

```java
public static final
Region
TABBED_PANE_TAB
```

Region of a TabbedPane for one tab. To bind a style to this

Region

use the name

TabbedPaneTab

.

- TABBED_PANE_TAB_AREA

```java
public static final
Region
TABBED_PANE_TAB_AREA
```

Region of a TabbedPane containing the tabs. To bind a style to this

Region

use the name

TabbedPaneTabArea

.

- TABBED_PANE_CONTENT

```java
public static final
Region
TABBED_PANE_CONTENT
```

Region of a TabbedPane containing the content. To bind a style to this

Region

use the name

TabbedPaneContent

.

- TABLE

```java
public static final
Region
TABLE
```

Table region. To bind a style to this

Region

use
the name

Table

.

- TABLE_HEADER

```java
public static final
Region
TABLE_HEADER
```

TableHeader region. To bind a style to this

Region

use
the name

TableHeader

.

- TEXT_AREA

```java
public static final
Region
TEXT_AREA
```

TextArea region. To bind a style to this

Region

use
the name

TextArea

.

- TEXT_FIELD

```java
public static final
Region
TEXT_FIELD
```

TextField region. To bind a style to this

Region

use
the name

TextField

.

- TEXT_PANE

```java
public static final
Region
TEXT_PANE
```

TextPane region. To bind a style to this

Region

use
the name

TextPane

.

- TOGGLE_BUTTON

```java
public static final
Region
TOGGLE_BUTTON
```

ToggleButton region. To bind a style to this

Region

use
the name

ToggleButton

.

- TOOL_BAR

```java
public static final
Region
TOOL_BAR
```

ToolBar region. To bind a style to this

Region

use
the name

ToolBar

.

- TOOL_BAR_CONTENT

```java
public static final
Region
TOOL_BAR_CONTENT
```

Region of the ToolBar containing the content. To bind a style to this

Region

use the name

ToolBarContent

.

- TOOL_BAR_DRAG_WINDOW

```java
public static final
Region
TOOL_BAR_DRAG_WINDOW
```

Region for the Window containing the ToolBar. To bind a style to this

Region

use the name

ToolBarDragWindow

.

- TOOL_TIP

```java
public static final
Region
TOOL_TIP
```

ToolTip region. To bind a style to this

Region

use
the name

ToolTip

.

- TOOL_BAR_SEPARATOR

```java
public static final
Region
TOOL_BAR_SEPARATOR
```

ToolBar separator region. To bind a style to this

Region

use
the name

ToolBarSeparator

.

- TREE

```java
public static final
Region
TREE
```

Tree region. To bind a style to this

Region

use the name

Tree

.

- TREE_CELL

```java
public static final
Region
TREE_CELL
```

Region of the Tree for one cell. To bind a style to this

Region

use the name

TreeCell

.

- VIEWPORT

```java
public static final
Region
VIEWPORT
```

Viewport region. To bind a style to this

Region

use
the name

Viewport

.

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- Region

```java
protected Region​(
String
name,

String
ui,
boolean subregion)
```

Creates a Region with the specified name. This should only be
used if you are creating your own

JComponent

subclass
with a custom

ComponentUI

class.

**Parameters:** name

- Name of the region
**Parameters:** ui

- String that will be returned from

component.getUIClassID

. This will be null
if this is a subregion.
**Parameters:** subregion

- Whether or not this is a subregion.

============ METHOD DETAIL ==========

- Method Detail

- isSubregion

```java
public boolean isSubregion()
```

Returns true if the Region is a subregion of a Component, otherwise
false. For example,

Region.BUTTON

corresponds do a

Component

so that

Region.BUTTON.isSubregion()

returns false.

**Returns:** true if the Region is a subregion of a Component.

- getName

```java
public
String
getName()
```

Returns the name of the region.

**Returns:** name of the Region.

- toString

```java
public
String
toString()
```

Returns the name of the Region.

**Overrides:** toString

in class

Object
**Returns:** name of the Region.

Field Detail

- ARROW_BUTTON

```java
public static final
Region
ARROW_BUTTON
```

ArrowButton's are special types of buttons that also render a
directional indicator, typically an arrow. ArrowButtons are used by
composite components, for example ScrollBar's contain ArrowButtons.
To bind a style to this

Region

use the name

ArrowButton

.

- BUTTON

```java
public static final
Region
BUTTON
```

Button region. To bind a style to this

Region

use the name

Button

.

- CHECK_BOX

```java
public static final
Region
CHECK_BOX
```

CheckBox region. To bind a style to this

Region

use the name

CheckBox

.

- CHECK_BOX_MENU_ITEM

```java
public static final
Region
CHECK_BOX_MENU_ITEM
```

CheckBoxMenuItem region. To bind a style to this

Region

use
the name

CheckBoxMenuItem

.

- COLOR_CHOOSER

```java
public static final
Region
COLOR_CHOOSER
```

ColorChooser region. To bind a style to this

Region

use
the name

ColorChooser

.

- COMBO_BOX

```java
public static final
Region
COMBO_BOX
```

ComboBox region. To bind a style to this

Region

use
the name

ComboBox

.

- DESKTOP_PANE

```java
public static final
Region
DESKTOP_PANE
```

DesktopPane region. To bind a style to this

Region

use
the name

DesktopPane

.

- DESKTOP_ICON

```java
public static final
Region
DESKTOP_ICON
```

DesktopIcon region. To bind a style to this

Region

use
the name

DesktopIcon

.

- EDITOR_PANE

```java
public static final
Region
EDITOR_PANE
```

EditorPane region. To bind a style to this

Region

use
the name

EditorPane

.

- FILE_CHOOSER

```java
public static final
Region
FILE_CHOOSER
```

FileChooser region. To bind a style to this

Region

use
the name

FileChooser

.

- FORMATTED_TEXT_FIELD

```java
public static final
Region
FORMATTED_TEXT_FIELD
```

FormattedTextField region. To bind a style to this

Region

use
the name

FormattedTextField

.

- INTERNAL_FRAME

```java
public static final
Region
INTERNAL_FRAME
```

InternalFrame region. To bind a style to this

Region

use
the name

InternalFrame

.

- INTERNAL_FRAME_TITLE_PANE

```java
public static final
Region
INTERNAL_FRAME_TITLE_PANE
```

TitlePane of an InternalFrame. The TitlePane typically
shows a menu, title, widgets to manipulate the internal frame.
To bind a style to this

Region

use the name

InternalFrameTitlePane

.

- LABEL

```java
public static final
Region
LABEL
```

Label region. To bind a style to this

Region

use the name

Label

.

- LIST

```java
public static final
Region
LIST
```

List region. To bind a style to this

Region

use the name

List

.

- MENU

```java
public static final
Region
MENU
```

Menu region. To bind a style to this

Region

use the name

Menu

.

- MENU_BAR

```java
public static final
Region
MENU_BAR
```

MenuBar region. To bind a style to this

Region

use the name

MenuBar

.

- MENU_ITEM

```java
public static final
Region
MENU_ITEM
```

MenuItem region. To bind a style to this

Region

use the name

MenuItem

.

- MENU_ITEM_ACCELERATOR

```java
public static final
Region
MENU_ITEM_ACCELERATOR
```

Accelerator region of a MenuItem. To bind a style to this

Region

use the name

MenuItemAccelerator

.

- OPTION_PANE

```java
public static final
Region
OPTION_PANE
```

OptionPane region. To bind a style to this

Region

use
the name

OptionPane

.

- PANEL

```java
public static final
Region
PANEL
```

Panel region. To bind a style to this

Region

use the name

Panel

.

- PASSWORD_FIELD

```java
public static final
Region
PASSWORD_FIELD
```

PasswordField region. To bind a style to this

Region

use
the name

PasswordField

.

- POPUP_MENU

```java
public static final
Region
POPUP_MENU
```

PopupMenu region. To bind a style to this

Region

use
the name

PopupMenu

.

- POPUP_MENU_SEPARATOR

```java
public static final
Region
POPUP_MENU_SEPARATOR
```

PopupMenuSeparator region. To bind a style to this

Region

use the name

PopupMenuSeparator

.

- PROGRESS_BAR

```java
public static final
Region
PROGRESS_BAR
```

ProgressBar region. To bind a style to this

Region

use the name

ProgressBar

.

- RADIO_BUTTON

```java
public static final
Region
RADIO_BUTTON
```

RadioButton region. To bind a style to this

Region

use the name

RadioButton

.

- RADIO_BUTTON_MENU_ITEM

```java
public static final
Region
RADIO_BUTTON_MENU_ITEM
```

RegionButtonMenuItem region. To bind a style to this

Region

use the name

RadioButtonMenuItem

.

- ROOT_PANE

```java
public static final
Region
ROOT_PANE
```

RootPane region. To bind a style to this

Region

use
the name

RootPane

.

- SCROLL_BAR

```java
public static final
Region
SCROLL_BAR
```

ScrollBar region. To bind a style to this

Region

use
the name

ScrollBar

.

- SCROLL_BAR_TRACK

```java
public static final
Region
SCROLL_BAR_TRACK
```

Track of the ScrollBar. To bind a style to this

Region

use
the name

ScrollBarTrack

.

- SCROLL_BAR_THUMB

```java
public static final
Region
SCROLL_BAR_THUMB
```

Thumb of the ScrollBar. The thumb is the region of the ScrollBar
that gives a graphical depiction of what percentage of the View is
currently visible. To bind a style to this

Region

use
the name

ScrollBarThumb

.

- SCROLL_PANE

```java
public static final
Region
SCROLL_PANE
```

ScrollPane region. To bind a style to this

Region

use
the name

ScrollPane

.

- SEPARATOR

```java
public static final
Region
SEPARATOR
```

Separator region. To bind a style to this

Region

use
the name

Separator

.

- SLIDER

```java
public static final
Region
SLIDER
```

Slider region. To bind a style to this

Region

use
the name

Slider

.

- SLIDER_TRACK

```java
public static final
Region
SLIDER_TRACK
```

Track of the Slider. To bind a style to this

Region

use
the name

SliderTrack

.

- SLIDER_THUMB

```java
public static final
Region
SLIDER_THUMB
```

Thumb of the Slider. The thumb of the Slider identifies the current
value. To bind a style to this

Region

use the name

SliderThumb

.

- SPINNER

```java
public static final
Region
SPINNER
```

Spinner region. To bind a style to this

Region

use the name

Spinner

.

- SPLIT_PANE

```java
public static final
Region
SPLIT_PANE
```

SplitPane region. To bind a style to this

Region

use the name

SplitPane

.

- SPLIT_PANE_DIVIDER

```java
public static final
Region
SPLIT_PANE_DIVIDER
```

Divider of the SplitPane. To bind a style to this

Region

use the name

SplitPaneDivider

.

- TABBED_PANE

```java
public static final
Region
TABBED_PANE
```

TabbedPane region. To bind a style to this

Region

use
the name

TabbedPane

.

- TABBED_PANE_TAB

```java
public static final
Region
TABBED_PANE_TAB
```

Region of a TabbedPane for one tab. To bind a style to this

Region

use the name

TabbedPaneTab

.

- TABBED_PANE_TAB_AREA

```java
public static final
Region
TABBED_PANE_TAB_AREA
```

Region of a TabbedPane containing the tabs. To bind a style to this

Region

use the name

TabbedPaneTabArea

.

- TABBED_PANE_CONTENT

```java
public static final
Region
TABBED_PANE_CONTENT
```

Region of a TabbedPane containing the content. To bind a style to this

Region

use the name

TabbedPaneContent

.

- TABLE

```java
public static final
Region
TABLE
```

Table region. To bind a style to this

Region

use
the name

Table

.

- TABLE_HEADER

```java
public static final
Region
TABLE_HEADER
```

TableHeader region. To bind a style to this

Region

use
the name

TableHeader

.

- TEXT_AREA

```java
public static final
Region
TEXT_AREA
```

TextArea region. To bind a style to this

Region

use
the name

TextArea

.

- TEXT_FIELD

```java
public static final
Region
TEXT_FIELD
```

TextField region. To bind a style to this

Region

use
the name

TextField

.

- TEXT_PANE

```java
public static final
Region
TEXT_PANE
```

TextPane region. To bind a style to this

Region

use
the name

TextPane

.

- TOGGLE_BUTTON

```java
public static final
Region
TOGGLE_BUTTON
```

ToggleButton region. To bind a style to this

Region

use
the name

ToggleButton

.

- TOOL_BAR

```java
public static final
Region
TOOL_BAR
```

ToolBar region. To bind a style to this

Region

use
the name

ToolBar

.

- TOOL_BAR_CONTENT

```java
public static final
Region
TOOL_BAR_CONTENT
```

Region of the ToolBar containing the content. To bind a style to this

Region

use the name

ToolBarContent

.

- TOOL_BAR_DRAG_WINDOW

```java
public static final
Region
TOOL_BAR_DRAG_WINDOW
```

Region for the Window containing the ToolBar. To bind a style to this

Region

use the name

ToolBarDragWindow

.

- TOOL_TIP

```java
public static final
Region
TOOL_TIP
```

ToolTip region. To bind a style to this

Region

use
the name

ToolTip

.

- TOOL_BAR_SEPARATOR

```java
public static final
Region
TOOL_BAR_SEPARATOR
```

ToolBar separator region. To bind a style to this

Region

use
the name

ToolBarSeparator

.

- TREE

```java
public static final
Region
TREE
```

Tree region. To bind a style to this

Region

use the name

Tree

.

- TREE_CELL

```java
public static final
Region
TREE_CELL
```

Region of the Tree for one cell. To bind a style to this

Region

use the name

TreeCell

.

- VIEWPORT

```java
public static final
Region
VIEWPORT
```

Viewport region. To bind a style to this

Region

use
the name

Viewport

.

---

#### Field Detail

ARROW_BUTTON

```java
public static final
Region
ARROW_BUTTON
```

ArrowButton's are special types of buttons that also render a
directional indicator, typically an arrow. ArrowButtons are used by
composite components, for example ScrollBar's contain ArrowButtons.
To bind a style to this

Region

use the name

ArrowButton

.

---

#### ARROW_BUTTON

public static final

Region

ARROW_BUTTON

ArrowButton's are special types of buttons that also render a
directional indicator, typically an arrow. ArrowButtons are used by
composite components, for example ScrollBar's contain ArrowButtons.
To bind a style to this

Region

use the name

ArrowButton

.

BUTTON

```java
public static final
Region
BUTTON
```

Button region. To bind a style to this

Region

use the name

Button

.

---

#### BUTTON

public static final

Region

BUTTON

Button region. To bind a style to this

Region

use the name

Button

.

CHECK_BOX

```java
public static final
Region
CHECK_BOX
```

CheckBox region. To bind a style to this

Region

use the name

CheckBox

.

---

#### CHECK_BOX

public static final

Region

CHECK_BOX

CheckBox region. To bind a style to this

Region

use the name

CheckBox

.

CHECK_BOX_MENU_ITEM

```java
public static final
Region
CHECK_BOX_MENU_ITEM
```

CheckBoxMenuItem region. To bind a style to this

Region

use
the name

CheckBoxMenuItem

.

---

#### CHECK_BOX_MENU_ITEM

public static final

Region

CHECK_BOX_MENU_ITEM

CheckBoxMenuItem region. To bind a style to this

Region

use
the name

CheckBoxMenuItem

.

COLOR_CHOOSER

```java
public static final
Region
COLOR_CHOOSER
```

ColorChooser region. To bind a style to this

Region

use
the name

ColorChooser

.

---

#### COLOR_CHOOSER

public static final

Region

COLOR_CHOOSER

ColorChooser region. To bind a style to this

Region

use
the name

ColorChooser

.

COMBO_BOX

```java
public static final
Region
COMBO_BOX
```

ComboBox region. To bind a style to this

Region

use
the name

ComboBox

.

---

#### COMBO_BOX

public static final

Region

COMBO_BOX

ComboBox region. To bind a style to this

Region

use
the name

ComboBox

.

DESKTOP_PANE

```java
public static final
Region
DESKTOP_PANE
```

DesktopPane region. To bind a style to this

Region

use
the name

DesktopPane

.

---

#### DESKTOP_PANE

public static final

Region

DESKTOP_PANE

DesktopPane region. To bind a style to this

Region

use
the name

DesktopPane

.

DESKTOP_ICON

```java
public static final
Region
DESKTOP_ICON
```

DesktopIcon region. To bind a style to this

Region

use
the name

DesktopIcon

.

---

#### DESKTOP_ICON

public static final

Region

DESKTOP_ICON

DesktopIcon region. To bind a style to this

Region

use
the name

DesktopIcon

.

EDITOR_PANE

```java
public static final
Region
EDITOR_PANE
```

EditorPane region. To bind a style to this

Region

use
the name

EditorPane

.

---

#### EDITOR_PANE

public static final

Region

EDITOR_PANE

EditorPane region. To bind a style to this

Region

use
the name

EditorPane

.

FILE_CHOOSER

```java
public static final
Region
FILE_CHOOSER
```

FileChooser region. To bind a style to this

Region

use
the name

FileChooser

.

---

#### FILE_CHOOSER

public static final

Region

FILE_CHOOSER

FileChooser region. To bind a style to this

Region

use
the name

FileChooser

.

FORMATTED_TEXT_FIELD

```java
public static final
Region
FORMATTED_TEXT_FIELD
```

FormattedTextField region. To bind a style to this

Region

use
the name

FormattedTextField

.

---

#### FORMATTED_TEXT_FIELD

public static final

Region

FORMATTED_TEXT_FIELD

FormattedTextField region. To bind a style to this

Region

use
the name

FormattedTextField

.

INTERNAL_FRAME

```java
public static final
Region
INTERNAL_FRAME
```

InternalFrame region. To bind a style to this

Region

use
the name

InternalFrame

.

---

#### INTERNAL_FRAME

public static final

Region

INTERNAL_FRAME

InternalFrame region. To bind a style to this

Region

use
the name

InternalFrame

.

INTERNAL_FRAME_TITLE_PANE

```java
public static final
Region
INTERNAL_FRAME_TITLE_PANE
```

TitlePane of an InternalFrame. The TitlePane typically
shows a menu, title, widgets to manipulate the internal frame.
To bind a style to this

Region

use the name

InternalFrameTitlePane

.

---

#### INTERNAL_FRAME_TITLE_PANE

public static final

Region

INTERNAL_FRAME_TITLE_PANE

TitlePane of an InternalFrame. The TitlePane typically
shows a menu, title, widgets to manipulate the internal frame.
To bind a style to this

Region

use the name

InternalFrameTitlePane

.

LABEL

```java
public static final
Region
LABEL
```

Label region. To bind a style to this

Region

use the name

Label

.

---

#### LABEL

public static final

Region

LABEL

Label region. To bind a style to this

Region

use the name

Label

.

LIST

```java
public static final
Region
LIST
```

List region. To bind a style to this

Region

use the name

List

.

---

#### LIST

public static final

Region

LIST

List region. To bind a style to this

Region

use the name

List

.

MENU

```java
public static final
Region
MENU
```

Menu region. To bind a style to this

Region

use the name

Menu

.

---

#### MENU

public static final

Region

MENU

Menu region. To bind a style to this

Region

use the name

Menu

.

MENU_BAR

```java
public static final
Region
MENU_BAR
```

MenuBar region. To bind a style to this

Region

use the name

MenuBar

.

---

#### MENU_BAR

public static final

Region

MENU_BAR

MenuBar region. To bind a style to this

Region

use the name

MenuBar

.

MENU_ITEM

```java
public static final
Region
MENU_ITEM
```

MenuItem region. To bind a style to this

Region

use the name

MenuItem

.

---

#### MENU_ITEM

public static final

Region

MENU_ITEM

MenuItem region. To bind a style to this

Region

use the name

MenuItem

.

MENU_ITEM_ACCELERATOR

```java
public static final
Region
MENU_ITEM_ACCELERATOR
```

Accelerator region of a MenuItem. To bind a style to this

Region

use the name

MenuItemAccelerator

.

---

#### MENU_ITEM_ACCELERATOR

public static final

Region

MENU_ITEM_ACCELERATOR

Accelerator region of a MenuItem. To bind a style to this

Region

use the name

MenuItemAccelerator

.

OPTION_PANE

```java
public static final
Region
OPTION_PANE
```

OptionPane region. To bind a style to this

Region

use
the name

OptionPane

.

---

#### OPTION_PANE

public static final

Region

OPTION_PANE

OptionPane region. To bind a style to this

Region

use
the name

OptionPane

.

PANEL

```java
public static final
Region
PANEL
```

Panel region. To bind a style to this

Region

use the name

Panel

.

---

#### PANEL

public static final

Region

PANEL

Panel region. To bind a style to this

Region

use the name

Panel

.

PASSWORD_FIELD

```java
public static final
Region
PASSWORD_FIELD
```

PasswordField region. To bind a style to this

Region

use
the name

PasswordField

.

---

#### PASSWORD_FIELD

public static final

Region

PASSWORD_FIELD

PasswordField region. To bind a style to this

Region

use
the name

PasswordField

.

POPUP_MENU

```java
public static final
Region
POPUP_MENU
```

PopupMenu region. To bind a style to this

Region

use
the name

PopupMenu

.

---

#### POPUP_MENU

public static final

Region

POPUP_MENU

PopupMenu region. To bind a style to this

Region

use
the name

PopupMenu

.

POPUP_MENU_SEPARATOR

```java
public static final
Region
POPUP_MENU_SEPARATOR
```

PopupMenuSeparator region. To bind a style to this

Region

use the name

PopupMenuSeparator

.

---

#### POPUP_MENU_SEPARATOR

public static final

Region

POPUP_MENU_SEPARATOR

PopupMenuSeparator region. To bind a style to this

Region

use the name

PopupMenuSeparator

.

PROGRESS_BAR

```java
public static final
Region
PROGRESS_BAR
```

ProgressBar region. To bind a style to this

Region

use the name

ProgressBar

.

---

#### PROGRESS_BAR

public static final

Region

PROGRESS_BAR

ProgressBar region. To bind a style to this

Region

use the name

ProgressBar

.

RADIO_BUTTON

```java
public static final
Region
RADIO_BUTTON
```

RadioButton region. To bind a style to this

Region

use the name

RadioButton

.

---

#### RADIO_BUTTON

public static final

Region

RADIO_BUTTON

RadioButton region. To bind a style to this

Region

use the name

RadioButton

.

RADIO_BUTTON_MENU_ITEM

```java
public static final
Region
RADIO_BUTTON_MENU_ITEM
```

RegionButtonMenuItem region. To bind a style to this

Region

use the name

RadioButtonMenuItem

.

---

#### RADIO_BUTTON_MENU_ITEM

public static final

Region

RADIO_BUTTON_MENU_ITEM

RegionButtonMenuItem region. To bind a style to this

Region

use the name

RadioButtonMenuItem

.

ROOT_PANE

```java
public static final
Region
ROOT_PANE
```

RootPane region. To bind a style to this

Region

use
the name

RootPane

.

---

#### ROOT_PANE

public static final

Region

ROOT_PANE

RootPane region. To bind a style to this

Region

use
the name

RootPane

.

SCROLL_BAR

```java
public static final
Region
SCROLL_BAR
```

ScrollBar region. To bind a style to this

Region

use
the name

ScrollBar

.

---

#### SCROLL_BAR

public static final

Region

SCROLL_BAR

ScrollBar region. To bind a style to this

Region

use
the name

ScrollBar

.

SCROLL_BAR_TRACK

```java
public static final
Region
SCROLL_BAR_TRACK
```

Track of the ScrollBar. To bind a style to this

Region

use
the name

ScrollBarTrack

.

---

#### SCROLL_BAR_TRACK

public static final

Region

SCROLL_BAR_TRACK

Track of the ScrollBar. To bind a style to this

Region

use
the name

ScrollBarTrack

.

SCROLL_BAR_THUMB

```java
public static final
Region
SCROLL_BAR_THUMB
```

Thumb of the ScrollBar. The thumb is the region of the ScrollBar
that gives a graphical depiction of what percentage of the View is
currently visible. To bind a style to this

Region

use
the name

ScrollBarThumb

.

---

#### SCROLL_BAR_THUMB

public static final

Region

SCROLL_BAR_THUMB

Thumb of the ScrollBar. The thumb is the region of the ScrollBar
that gives a graphical depiction of what percentage of the View is
currently visible. To bind a style to this

Region

use
the name

ScrollBarThumb

.

SCROLL_PANE

```java
public static final
Region
SCROLL_PANE
```

ScrollPane region. To bind a style to this

Region

use
the name

ScrollPane

.

---

#### SCROLL_PANE

public static final

Region

SCROLL_PANE

ScrollPane region. To bind a style to this

Region

use
the name

ScrollPane

.

SEPARATOR

```java
public static final
Region
SEPARATOR
```

Separator region. To bind a style to this

Region

use
the name

Separator

.

---

#### SEPARATOR

public static final

Region

SEPARATOR

Separator region. To bind a style to this

Region

use
the name

Separator

.

SLIDER

```java
public static final
Region
SLIDER
```

Slider region. To bind a style to this

Region

use
the name

Slider

.

---

#### SLIDER

public static final

Region

SLIDER

Slider region. To bind a style to this

Region

use
the name

Slider

.

SLIDER_TRACK

```java
public static final
Region
SLIDER_TRACK
```

Track of the Slider. To bind a style to this

Region

use
the name

SliderTrack

.

---

#### SLIDER_TRACK

public static final

Region

SLIDER_TRACK

Track of the Slider. To bind a style to this

Region

use
the name

SliderTrack

.

SLIDER_THUMB

```java
public static final
Region
SLIDER_THUMB
```

Thumb of the Slider. The thumb of the Slider identifies the current
value. To bind a style to this

Region

use the name

SliderThumb

.

---

#### SLIDER_THUMB

public static final

Region

SLIDER_THUMB

Thumb of the Slider. The thumb of the Slider identifies the current
value. To bind a style to this

Region

use the name

SliderThumb

.

SPINNER

```java
public static final
Region
SPINNER
```

Spinner region. To bind a style to this

Region

use the name

Spinner

.

---

#### SPINNER

public static final

Region

SPINNER

Spinner region. To bind a style to this

Region

use the name

Spinner

.

SPLIT_PANE

```java
public static final
Region
SPLIT_PANE
```

SplitPane region. To bind a style to this

Region

use the name

SplitPane

.

---

#### SPLIT_PANE

public static final

Region

SPLIT_PANE

SplitPane region. To bind a style to this

Region

use the name

SplitPane

.

SPLIT_PANE_DIVIDER

```java
public static final
Region
SPLIT_PANE_DIVIDER
```

Divider of the SplitPane. To bind a style to this

Region

use the name

SplitPaneDivider

.

---

#### SPLIT_PANE_DIVIDER

public static final

Region

SPLIT_PANE_DIVIDER

Divider of the SplitPane. To bind a style to this

Region

use the name

SplitPaneDivider

.

TABBED_PANE

```java
public static final
Region
TABBED_PANE
```

TabbedPane region. To bind a style to this

Region

use
the name

TabbedPane

.

---

#### TABBED_PANE

public static final

Region

TABBED_PANE

TabbedPane region. To bind a style to this

Region

use
the name

TabbedPane

.

TABBED_PANE_TAB

```java
public static final
Region
TABBED_PANE_TAB
```

Region of a TabbedPane for one tab. To bind a style to this

Region

use the name

TabbedPaneTab

.

---

#### TABBED_PANE_TAB

public static final

Region

TABBED_PANE_TAB

Region of a TabbedPane for one tab. To bind a style to this

Region

use the name

TabbedPaneTab

.

TABBED_PANE_TAB_AREA

```java
public static final
Region
TABBED_PANE_TAB_AREA
```

Region of a TabbedPane containing the tabs. To bind a style to this

Region

use the name

TabbedPaneTabArea

.

---

#### TABBED_PANE_TAB_AREA

public static final

Region

TABBED_PANE_TAB_AREA

Region of a TabbedPane containing the tabs. To bind a style to this

Region

use the name

TabbedPaneTabArea

.

TABBED_PANE_CONTENT

```java
public static final
Region
TABBED_PANE_CONTENT
```

Region of a TabbedPane containing the content. To bind a style to this

Region

use the name

TabbedPaneContent

.

---

#### TABBED_PANE_CONTENT

public static final

Region

TABBED_PANE_CONTENT

Region of a TabbedPane containing the content. To bind a style to this

Region

use the name

TabbedPaneContent

.

TABLE

```java
public static final
Region
TABLE
```

Table region. To bind a style to this

Region

use
the name

Table

.

---

#### TABLE

public static final

Region

TABLE

Table region. To bind a style to this

Region

use
the name

Table

.

TABLE_HEADER

```java
public static final
Region
TABLE_HEADER
```

TableHeader region. To bind a style to this

Region

use
the name

TableHeader

.

---

#### TABLE_HEADER

public static final

Region

TABLE_HEADER

TableHeader region. To bind a style to this

Region

use
the name

TableHeader

.

TEXT_AREA

```java
public static final
Region
TEXT_AREA
```

TextArea region. To bind a style to this

Region

use
the name

TextArea

.

---

#### TEXT_AREA

public static final

Region

TEXT_AREA

TextArea region. To bind a style to this

Region

use
the name

TextArea

.

TEXT_FIELD

```java
public static final
Region
TEXT_FIELD
```

TextField region. To bind a style to this

Region

use
the name

TextField

.

---

#### TEXT_FIELD

public static final

Region

TEXT_FIELD

TextField region. To bind a style to this

Region

use
the name

TextField

.

TEXT_PANE

```java
public static final
Region
TEXT_PANE
```

TextPane region. To bind a style to this

Region

use
the name

TextPane

.

---

#### TEXT_PANE

public static final

Region

TEXT_PANE

TextPane region. To bind a style to this

Region

use
the name

TextPane

.

TOGGLE_BUTTON

```java
public static final
Region
TOGGLE_BUTTON
```

ToggleButton region. To bind a style to this

Region

use
the name

ToggleButton

.

---

#### TOGGLE_BUTTON

public static final

Region

TOGGLE_BUTTON

ToggleButton region. To bind a style to this

Region

use
the name

ToggleButton

.

TOOL_BAR

```java
public static final
Region
TOOL_BAR
```

ToolBar region. To bind a style to this

Region

use
the name

ToolBar

.

---

#### TOOL_BAR

public static final

Region

TOOL_BAR

ToolBar region. To bind a style to this

Region

use
the name

ToolBar

.

TOOL_BAR_CONTENT

```java
public static final
Region
TOOL_BAR_CONTENT
```

Region of the ToolBar containing the content. To bind a style to this

Region

use the name

ToolBarContent

.

---

#### TOOL_BAR_CONTENT

public static final

Region

TOOL_BAR_CONTENT

Region of the ToolBar containing the content. To bind a style to this

Region

use the name

ToolBarContent

.

TOOL_BAR_DRAG_WINDOW

```java
public static final
Region
TOOL_BAR_DRAG_WINDOW
```

Region for the Window containing the ToolBar. To bind a style to this

Region

use the name

ToolBarDragWindow

.

---

#### TOOL_BAR_DRAG_WINDOW

public static final

Region

TOOL_BAR_DRAG_WINDOW

Region for the Window containing the ToolBar. To bind a style to this

Region

use the name

ToolBarDragWindow

.

TOOL_TIP

```java
public static final
Region
TOOL_TIP
```

ToolTip region. To bind a style to this

Region

use
the name

ToolTip

.

---

#### TOOL_TIP

public static final

Region

TOOL_TIP

ToolTip region. To bind a style to this

Region

use
the name

ToolTip

.

TOOL_BAR_SEPARATOR

```java
public static final
Region
TOOL_BAR_SEPARATOR
```

ToolBar separator region. To bind a style to this

Region

use
the name

ToolBarSeparator

.

---

#### TOOL_BAR_SEPARATOR

public static final

Region

TOOL_BAR_SEPARATOR

ToolBar separator region. To bind a style to this

Region

use
the name

ToolBarSeparator

.

TREE

```java
public static final
Region
TREE
```

Tree region. To bind a style to this

Region

use the name

Tree

.

---

#### TREE

public static final

Region

TREE

Tree region. To bind a style to this

Region

use the name

Tree

.

TREE_CELL

```java
public static final
Region
TREE_CELL
```

Region of the Tree for one cell. To bind a style to this

Region

use the name

TreeCell

.

---

#### TREE_CELL

public static final

Region

TREE_CELL

Region of the Tree for one cell. To bind a style to this

Region

use the name

TreeCell

.

VIEWPORT

```java
public static final
Region
VIEWPORT
```

Viewport region. To bind a style to this

Region

use
the name

Viewport

.

---

#### VIEWPORT

public static final

Region

VIEWPORT

Viewport region. To bind a style to this

Region

use
the name

Viewport

.

Constructor Detail

- Region

```java
protected Region​(
String
name,

String
ui,
boolean subregion)
```

Creates a Region with the specified name. This should only be
used if you are creating your own

JComponent

subclass
with a custom

ComponentUI

class.

**Parameters:** name

- Name of the region
**Parameters:** ui

- String that will be returned from

component.getUIClassID

. This will be null
if this is a subregion.
**Parameters:** subregion

- Whether or not this is a subregion.

---

#### Constructor Detail

Region

```java
protected Region​(
String
name,

String
ui,
boolean subregion)
```

Creates a Region with the specified name. This should only be
used if you are creating your own

JComponent

subclass
with a custom

ComponentUI

class.

**Parameters:** name

- Name of the region
**Parameters:** ui

- String that will be returned from

component.getUIClassID

. This will be null
if this is a subregion.
**Parameters:** subregion

- Whether or not this is a subregion.

---

#### Region

protected Region​(

String

name,

String

ui,
boolean subregion)

Creates a Region with the specified name. This should only be
used if you are creating your own

JComponent

subclass
with a custom

ComponentUI

class.

Method Detail

- isSubregion

```java
public boolean isSubregion()
```

Returns true if the Region is a subregion of a Component, otherwise
false. For example,

Region.BUTTON

corresponds do a

Component

so that

Region.BUTTON.isSubregion()

returns false.

**Returns:** true if the Region is a subregion of a Component.

- getName

```java
public
String
getName()
```

Returns the name of the region.

**Returns:** name of the Region.

- toString

```java
public
String
toString()
```

Returns the name of the Region.

**Overrides:** toString

in class

Object
**Returns:** name of the Region.

---

#### Method Detail

isSubregion

```java
public boolean isSubregion()
```

Returns true if the Region is a subregion of a Component, otherwise
false. For example,

Region.BUTTON

corresponds do a

Component

so that

Region.BUTTON.isSubregion()

returns false.

**Returns:** true if the Region is a subregion of a Component.

---

#### isSubregion

public boolean isSubregion()

Returns true if the Region is a subregion of a Component, otherwise
false. For example,

Region.BUTTON

corresponds do a

Component

so that

Region.BUTTON.isSubregion()

returns false.

getName

```java
public
String
getName()
```

Returns the name of the region.

**Returns:** name of the Region.

---

#### getName

public

String

getName()

Returns the name of the region.

toString

```java
public
String
toString()
```

Returns the name of the Region.

**Overrides:** toString

in class

Object
**Returns:** name of the Region.

---

#### toString

public

String

toString()

Returns the name of the Region.

---

