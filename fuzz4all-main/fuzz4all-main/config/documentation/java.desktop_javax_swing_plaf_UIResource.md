# Interface UIResource

**Source:** `java.desktop\javax\swing\plaf\UIResource.html`

### Class Description

```java
public interface
UIResource
```

This interface is used to mark objects created by ComponentUI delegates.
The

ComponentUI.installUI()

and

ComponentUI.uninstallUI()

methods can use this interface
to decide if a properties value has been overridden. For example, the
JList cellRenderer property is initialized by BasicListUI.installUI(),
only if it's initial value is null:

```java
if (list.getCellRenderer() == null) {
list.setCellRenderer((ListCellRenderer)(UIManager.get("List.cellRenderer")));
}
```

At uninstallUI() time we reset the property to null if its value
is an instance of UIResource:

```java
if (list.getCellRenderer() instanceof UIResource) {
list.setCellRenderer(null);
}
```

This pattern applies to all properties except the java.awt.Component
properties font, foreground, and background. If one of these
properties isn't initialized, or is explicitly set to null,
its container provides the value. For this reason the

"== null"

is unreliable when installUI() is called
to dynamically change a components look and feel. So at installUI()
time we check to see if the current value is a UIResource:

```java
if (!(list.getFont() instanceof UIResource)) {
list.setFont(UIManager.getFont("List.font"));
}
```

**All Known Implementing Classes:** ActionMapUIResource

,

BasicBorders.ButtonBorder

,

BasicBorders.FieldBorder

,

BasicBorders.MarginBorder

,

BasicBorders.MenuBarBorder

,

BasicBorders.RadioButtonBorder

,

BasicBorders.RolloverButtonBorder

,

BasicBorders.SplitPaneBorder

,

BasicBorders.ToggleButtonBorder

,

BasicComboBoxEditor.UIResource

,

BasicComboBoxRenderer.UIResource

,

BasicTextUI.BasicCaret

,

BasicTextUI.BasicHighlighter

,

BorderUIResource

,

BorderUIResource.BevelBorderUIResource

,

BorderUIResource.CompoundBorderUIResource

,

BorderUIResource.EmptyBorderUIResource

,

BorderUIResource.EtchedBorderUIResource

,

BorderUIResource.LineBorderUIResource

,

BorderUIResource.MatteBorderUIResource

,

BorderUIResource.TitledBorderUIResource

,

ColorUIResource

,

ComponentInputMapUIResource

,

DefaultListCellRenderer.UIResource

,

DefaultMenuLayout

,

DefaultTableCellRenderer.UIResource

,

DimensionUIResource

,

FontUIResource

,

IconUIResource

,

InputMapUIResource

,

InsetsUIResource

,

JScrollPane.ScrollBar

,

MetalBorders.ButtonBorder

,

MetalBorders.Flush3DBorder

,

MetalBorders.InternalFrameBorder

,

MetalBorders.MenuBarBorder

,

MetalBorders.MenuItemBorder

,

MetalBorders.OptionDialogBorder

,

MetalBorders.PaletteBorder

,

MetalBorders.PopupMenuBorder

,

MetalBorders.RolloverButtonBorder

,

MetalBorders.ScrollPaneBorder

,

MetalBorders.TextFieldBorder

,

MetalBorders.ToggleButtonBorder

,

MetalBorders.ToolBarBorder

,

MetalCheckBoxIcon

,

MetalComboBoxEditor.UIResource

,

MetalIconFactory.PaletteCloseIcon

,

ScrollPaneLayout.UIResource

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Interface UIResource

**All Known Implementing Classes:** ActionMapUIResource

,

BasicBorders.ButtonBorder

,

BasicBorders.FieldBorder

,

BasicBorders.MarginBorder

,

BasicBorders.MenuBarBorder

,

BasicBorders.RadioButtonBorder

,

BasicBorders.RolloverButtonBorder

,

BasicBorders.SplitPaneBorder

,

BasicBorders.ToggleButtonBorder

,

BasicComboBoxEditor.UIResource

,

BasicComboBoxRenderer.UIResource

,

BasicTextUI.BasicCaret

,

BasicTextUI.BasicHighlighter

,

BorderUIResource

,

BorderUIResource.BevelBorderUIResource

,

BorderUIResource.CompoundBorderUIResource

,

BorderUIResource.EmptyBorderUIResource

,

BorderUIResource.EtchedBorderUIResource

,

BorderUIResource.LineBorderUIResource

,

BorderUIResource.MatteBorderUIResource

,

BorderUIResource.TitledBorderUIResource

,

ColorUIResource

,

ComponentInputMapUIResource

,

DefaultListCellRenderer.UIResource

,

DefaultMenuLayout

,

DefaultTableCellRenderer.UIResource

,

DimensionUIResource

,

FontUIResource

,

IconUIResource

,

InputMapUIResource

,

InsetsUIResource

,

JScrollPane.ScrollBar

,

MetalBorders.ButtonBorder

,

MetalBorders.Flush3DBorder

,

MetalBorders.InternalFrameBorder

,

MetalBorders.MenuBarBorder

,

MetalBorders.MenuItemBorder

,

MetalBorders.OptionDialogBorder

,

MetalBorders.PaletteBorder

,

MetalBorders.PopupMenuBorder

,

MetalBorders.RolloverButtonBorder

,

MetalBorders.ScrollPaneBorder

,

MetalBorders.TextFieldBorder

,

MetalBorders.ToggleButtonBorder

,

MetalBorders.ToolBarBorder

,

MetalCheckBoxIcon

,

MetalComboBoxEditor.UIResource

,

MetalIconFactory.PaletteCloseIcon

,

ScrollPaneLayout.UIResource

```java
public interface
UIResource
```

This interface is used to mark objects created by ComponentUI delegates.
The

ComponentUI.installUI()

and

ComponentUI.uninstallUI()

methods can use this interface
to decide if a properties value has been overridden. For example, the
JList cellRenderer property is initialized by BasicListUI.installUI(),
only if it's initial value is null:

```java
if (list.getCellRenderer() == null) {
list.setCellRenderer((ListCellRenderer)(UIManager.get("List.cellRenderer")));
}
```

At uninstallUI() time we reset the property to null if its value
is an instance of UIResource:

```java
if (list.getCellRenderer() instanceof UIResource) {
list.setCellRenderer(null);
}
```

This pattern applies to all properties except the java.awt.Component
properties font, foreground, and background. If one of these
properties isn't initialized, or is explicitly set to null,
its container provides the value. For this reason the

"== null"

is unreliable when installUI() is called
to dynamically change a components look and feel. So at installUI()
time we check to see if the current value is a UIResource:

```java
if (!(list.getFont() instanceof UIResource)) {
list.setFont(UIManager.getFont("List.font"));
}
```

**See Also:** ComponentUI

public interface

UIResource

This interface is used to mark objects created by ComponentUI delegates.
The

ComponentUI.installUI()

and

ComponentUI.uninstallUI()

methods can use this interface
to decide if a properties value has been overridden. For example, the
JList cellRenderer property is initialized by BasicListUI.installUI(),
only if it's initial value is null:

```java
if (list.getCellRenderer() == null) {
list.setCellRenderer((ListCellRenderer)(UIManager.get("List.cellRenderer")));
}
```

At uninstallUI() time we reset the property to null if its value
is an instance of UIResource:

```java
if (list.getCellRenderer() instanceof UIResource) {
list.setCellRenderer(null);
}
```

This pattern applies to all properties except the java.awt.Component
properties font, foreground, and background. If one of these
properties isn't initialized, or is explicitly set to null,
its container provides the value. For this reason the

"== null"

is unreliable when installUI() is called
to dynamically change a components look and feel. So at installUI()
time we check to see if the current value is a UIResource:

```java
if (!(list.getFont() instanceof UIResource)) {
list.setFont(UIManager.getFont("List.font"));
}
```

if (list.getCellRenderer() == null) {
list.setCellRenderer((ListCellRenderer)(UIManager.get("List.cellRenderer")));
}

if (list.getCellRenderer() instanceof UIResource) {
list.setCellRenderer(null);
}

if (!(list.getFont() instanceof UIResource)) {
list.setFont(UIManager.getFont("List.font"));
}

---

