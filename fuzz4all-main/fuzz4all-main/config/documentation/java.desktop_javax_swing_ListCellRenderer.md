# Interface ListCellRenderer<E>

**Source:** `java.desktop\javax\swing\ListCellRenderer.html`

### Class Description

```java
public interface
ListCellRenderer<E>
```

Identifies components that can be used as "rubber stamps" to paint
the cells in a JList. For example, to use a JLabel as a
ListCellRenderer, you would write something like this:

```java
class MyCellRenderer extends JLabel implements ListCellRenderer<Object> {
public MyCellRenderer() {
setOpaque(true);
}

public Component getListCellRendererComponent(JList<?> list,
Object value,
int index,
boolean isSelected,
boolean cellHasFocus) {

setText(value.toString());

Color background;
Color foreground;

// check if this cell represents the current DnD drop location
JList.DropLocation dropLocation = list.getDropLocation();
if (dropLocation != null
&& !dropLocation.isInsert()
&& dropLocation.getIndex() == index) {

background = Color.BLUE;
foreground = Color.WHITE;

// check if this cell is selected
} else if (isSelected) {
background = Color.RED;
foreground = Color.WHITE;

// unselected, and not the DnD drop location
} else {
background = Color.WHITE;
foreground = Color.BLACK;
};

setBackground(background);
setForeground(foreground);

return this;
}
}
```

**Type Parameters:** E

- the type of values this renderer can be used for

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Component
getListCellRendererComponent​(
JList
<? extends
E
> list,

E
value,
int index,
boolean isSelected,
boolean cellHasFocus)

Return a component that has been configured to display the specified
value. That component's

paint

method is then called to
"render" the cell. If it is necessary to compute the dimensions
of a list because the list cells do not have a fixed size, this method
is called to generate a component on which

getPreferredSize

can be invoked.

**Parameters:**
- list

- The JList we're painting.
- value

- The value returned by list.getModel().getElementAt(index).
- index

- The cells index.
- isSelected

- True if the specified cell was selected.
- cellHasFocus

- True if the specified cell has the focus.

**Returns:**
- A component whose paint() method will render the specified value.

**See Also:**
- JList

,

ListSelectionModel

,

ListModel

---

### Additional Sections

#### Interface ListCellRenderer<E>

**Type Parameters:** E

- the type of values this renderer can be used for

**All Known Implementing Classes:** BasicComboBoxRenderer

,

BasicComboBoxRenderer.UIResource

,

DefaultListCellRenderer

,

DefaultListCellRenderer.UIResource

,

MetalFileChooserUI.FileRenderer

,

MetalFileChooserUI.FilterComboBoxRenderer

```java
public interface
ListCellRenderer<E>
```

Identifies components that can be used as "rubber stamps" to paint
the cells in a JList. For example, to use a JLabel as a
ListCellRenderer, you would write something like this:

```java
class MyCellRenderer extends JLabel implements ListCellRenderer<Object> {
public MyCellRenderer() {
setOpaque(true);
}

public Component getListCellRendererComponent(JList<?> list,
Object value,
int index,
boolean isSelected,
boolean cellHasFocus) {

setText(value.toString());

Color background;
Color foreground;

// check if this cell represents the current DnD drop location
JList.DropLocation dropLocation = list.getDropLocation();
if (dropLocation != null
&& !dropLocation.isInsert()
&& dropLocation.getIndex() == index) {

background = Color.BLUE;
foreground = Color.WHITE;

// check if this cell is selected
} else if (isSelected) {
background = Color.RED;
foreground = Color.WHITE;

// unselected, and not the DnD drop location
} else {
background = Color.WHITE;
foreground = Color.BLACK;
};

setBackground(background);
setForeground(foreground);

return this;
}
}
```

**Since:** 1.2
**See Also:** JList

,

DefaultListCellRenderer

public interface

ListCellRenderer<E>

Identifies components that can be used as "rubber stamps" to paint
the cells in a JList. For example, to use a JLabel as a
ListCellRenderer, you would write something like this:

```java
class MyCellRenderer extends JLabel implements ListCellRenderer<Object> {
public MyCellRenderer() {
setOpaque(true);
}

public Component getListCellRendererComponent(JList<?> list,
Object value,
int index,
boolean isSelected,
boolean cellHasFocus) {

setText(value.toString());

Color background;
Color foreground;

// check if this cell represents the current DnD drop location
JList.DropLocation dropLocation = list.getDropLocation();
if (dropLocation != null
&& !dropLocation.isInsert()
&& dropLocation.getIndex() == index) {

background = Color.BLUE;
foreground = Color.WHITE;

// check if this cell is selected
} else if (isSelected) {
background = Color.RED;
foreground = Color.WHITE;

// unselected, and not the DnD drop location
} else {
background = Color.WHITE;
foreground = Color.BLACK;
};

setBackground(background);
setForeground(foreground);

return this;
}
}
```

class MyCellRenderer extends JLabel implements ListCellRenderer<Object> {
public MyCellRenderer() {
setOpaque(true);
}

public Component getListCellRendererComponent(JList<?> list,
Object value,
int index,
boolean isSelected,
boolean cellHasFocus) {

setText(value.toString());

Color background;
Color foreground;

// check if this cell represents the current DnD drop location
JList.DropLocation dropLocation = list.getDropLocation();
if (dropLocation != null
&& !dropLocation.isInsert()
&& dropLocation.getIndex() == index) {

background = Color.BLUE;
foreground = Color.WHITE;

// check if this cell is selected
} else if (isSelected) {
background = Color.RED;
foreground = Color.WHITE;

// unselected, and not the DnD drop location
} else {
background = Color.WHITE;
foreground = Color.BLACK;
};

setBackground(background);
setForeground(foreground);

return this;
}
}

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Component

getListCellRendererComponent

​(

JList

<? extends

E

> list,

E

value,
int index,
boolean isSelected,
boolean cellHasFocus)

Return a component that has been configured to display the specified
value.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Component

getListCellRendererComponent

​(

JList

<? extends

E

> list,

E

value,
int index,
boolean isSelected,
boolean cellHasFocus)

Return a component that has been configured to display the specified
value.

---

#### Method Summary

Return a component that has been configured to display the specified
value.

============ METHOD DETAIL ==========

- Method Detail

- getListCellRendererComponent

```java
Component
getListCellRendererComponent​(
JList
<? extends
E
> list,

E
value,
int index,
boolean isSelected,
boolean cellHasFocus)
```

Return a component that has been configured to display the specified
value. That component's

paint

method is then called to
"render" the cell. If it is necessary to compute the dimensions
of a list because the list cells do not have a fixed size, this method
is called to generate a component on which

getPreferredSize

can be invoked.

**Parameters:** list

- The JList we're painting.
**Parameters:** value

- The value returned by list.getModel().getElementAt(index).
**Parameters:** index

- The cells index.
**Parameters:** isSelected

- True if the specified cell was selected.
**Parameters:** cellHasFocus

- True if the specified cell has the focus.
**Returns:** A component whose paint() method will render the specified value.
**See Also:** JList

,

ListSelectionModel

,

ListModel

Method Detail

- getListCellRendererComponent

```java
Component
getListCellRendererComponent​(
JList
<? extends
E
> list,

E
value,
int index,
boolean isSelected,
boolean cellHasFocus)
```

Return a component that has been configured to display the specified
value. That component's

paint

method is then called to
"render" the cell. If it is necessary to compute the dimensions
of a list because the list cells do not have a fixed size, this method
is called to generate a component on which

getPreferredSize

can be invoked.

**Parameters:** list

- The JList we're painting.
**Parameters:** value

- The value returned by list.getModel().getElementAt(index).
**Parameters:** index

- The cells index.
**Parameters:** isSelected

- True if the specified cell was selected.
**Parameters:** cellHasFocus

- True if the specified cell has the focus.
**Returns:** A component whose paint() method will render the specified value.
**See Also:** JList

,

ListSelectionModel

,

ListModel

---

#### Method Detail

getListCellRendererComponent

```java
Component
getListCellRendererComponent​(
JList
<? extends
E
> list,

E
value,
int index,
boolean isSelected,
boolean cellHasFocus)
```

Return a component that has been configured to display the specified
value. That component's

paint

method is then called to
"render" the cell. If it is necessary to compute the dimensions
of a list because the list cells do not have a fixed size, this method
is called to generate a component on which

getPreferredSize

can be invoked.

**Parameters:** list

- The JList we're painting.
**Parameters:** value

- The value returned by list.getModel().getElementAt(index).
**Parameters:** index

- The cells index.
**Parameters:** isSelected

- True if the specified cell was selected.
**Parameters:** cellHasFocus

- True if the specified cell has the focus.
**Returns:** A component whose paint() method will render the specified value.
**See Also:** JList

,

ListSelectionModel

,

ListModel

---

#### getListCellRendererComponent

Component

getListCellRendererComponent​(

JList

<? extends

E

> list,

E

value,
int index,
boolean isSelected,
boolean cellHasFocus)

Return a component that has been configured to display the specified
value. That component's

paint

method is then called to
"render" the cell. If it is necessary to compute the dimensions
of a list because the list cells do not have a fixed size, this method
is called to generate a component on which

getPreferredSize

can be invoked.

---

