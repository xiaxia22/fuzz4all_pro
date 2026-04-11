# Interface JComboBox.KeySelectionManager

**Source:** `java.desktop\javax\swing\JComboBox.KeySelectionManager.html`

### Class Description

```java
public static interface
JComboBox.KeySelectionManager
```

The interface that defines a

KeySelectionManager

.
To qualify as a

KeySelectionManager

,
the class needs to implement the method
that identifies the list index given a character and the
combo box data model.

**Enclosing class:** JComboBox

<

E

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### int selectionForKey​(char aKey,

ComboBoxModel
<?> aModel)

Given

aKey

and the model, returns the row
that should become selected. Return -1 if no match was
found.

**Parameters:**
- aKey

- a char value, usually indicating a keyboard key that
was pressed
- aModel

- a ComboBoxModel -- the component's data model, containing
the list of selectable items

**Returns:**
- an int equal to the selected row, where 0 is the
first item and -1 is none.

---

### Additional Sections

#### Interface JComboBox.KeySelectionManager

**Enclosing class:** JComboBox

<

E

>

```java
public static interface
JComboBox.KeySelectionManager
```

The interface that defines a

KeySelectionManager

.
To qualify as a

KeySelectionManager

,
the class needs to implement the method
that identifies the list index given a character and the
combo box data model.

public static interface

JComboBox.KeySelectionManager

The interface that defines a

KeySelectionManager

.
To qualify as a

KeySelectionManager

,
the class needs to implement the method
that identifies the list index given a character and the
combo box data model.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

selectionForKey

​(char aKey,

ComboBoxModel

<?> aModel)

Given

aKey

and the model, returns the row
that should become selected.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

int

selectionForKey

​(char aKey,

ComboBoxModel

<?> aModel)

Given

aKey

and the model, returns the row
that should become selected.

---

#### Method Summary

Given

aKey

and the model, returns the row
that should become selected.

============ METHOD DETAIL ==========

- Method Detail

- selectionForKey

```java
int selectionForKey​(char aKey,

ComboBoxModel
<?> aModel)
```

Given

aKey

and the model, returns the row
that should become selected. Return -1 if no match was
found.

**Parameters:** aKey

- a char value, usually indicating a keyboard key that
was pressed
**Parameters:** aModel

- a ComboBoxModel -- the component's data model, containing
the list of selectable items
**Returns:** an int equal to the selected row, where 0 is the
first item and -1 is none.

Method Detail

- selectionForKey

```java
int selectionForKey​(char aKey,

ComboBoxModel
<?> aModel)
```

Given

aKey

and the model, returns the row
that should become selected. Return -1 if no match was
found.

**Parameters:** aKey

- a char value, usually indicating a keyboard key that
was pressed
**Parameters:** aModel

- a ComboBoxModel -- the component's data model, containing
the list of selectable items
**Returns:** an int equal to the selected row, where 0 is the
first item and -1 is none.

---

#### Method Detail

selectionForKey

```java
int selectionForKey​(char aKey,

ComboBoxModel
<?> aModel)
```

Given

aKey

and the model, returns the row
that should become selected. Return -1 if no match was
found.

**Parameters:** aKey

- a char value, usually indicating a keyboard key that
was pressed
**Parameters:** aModel

- a ComboBoxModel -- the component's data model, containing
the list of selectable items
**Returns:** an int equal to the selected row, where 0 is the
first item and -1 is none.

---

#### selectionForKey

int selectionForKey​(char aKey,

ComboBoxModel

<?> aModel)

Given

aKey

and the model, returns the row
that should become selected. Return -1 if no match was
found.

---

